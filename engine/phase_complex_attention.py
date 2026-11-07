import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class PhaseComplexAttention(nn.Module):
    """
    Phase Complex Attention (PCA) Module
    Implements complex Hermitian inner product attention: A_ij = <q_i | k_j> in C,
    unitary phase residual updates: v_steered = exp(i * H_intent * dt) * v_residual,
    and decoherence-resistant norm normalization ||Psi|| = 1.
    """
    def __init__(self, embed_dim: int, num_heads: int):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        assert self.head_dim * num_heads == embed_dim, "embed_dim must be divisible by num_heads"

        # Real and Imaginary projection matrices for Q, K, V
        self.q_proj_real = nn.Linear(embed_dim, embed_dim, bias=False)
        self.q_proj_imag = nn.Linear(embed_dim, embed_dim, bias=False)
        
        self.k_proj_real = nn.Linear(embed_dim, embed_dim, bias=False)
        self.k_proj_imag = nn.Linear(embed_dim, embed_dim, bias=False)

        self.v_proj_real = nn.Linear(embed_dim, embed_dim, bias=False)
        self.v_proj_imag = nn.Linear(embed_dim, embed_dim, bias=False)

        self.out_proj_real = nn.Linear(embed_dim, embed_dim, bias=False)
        self.out_proj_imag = nn.Linear(embed_dim, embed_dim, bias=False)

        # Learnable Intent Hamiltonian operator (H_intent) for phase steering
        self.H_intent = nn.Parameter(torch.randn(num_heads, self.head_dim, self.head_dim) * 0.02)

    def _to_complex(self, x_real: torch.Tensor, x_imag: torch.Tensor) -> torch.Tensor:
        return torch.complex(x_real, x_imag)

    def forward(
        self, 
        x_real: torch.Tensor, 
        x_imag: torch.Tensor,
        intent_magnitude: float = 0.5,
        target_state: torch.Tensor = None,
        proxy_state: torch.Tensor = None
    ):
        """
        x_real, x_imag: [batch_size, seq_len, embed_dim]
        """
        B, N, D = x_real.shape
        H = self.num_heads
        d = self.head_dim

        # 1. Linear Complex Projections
        Q_r = self.q_proj_real(x_real) - self.q_proj_imag(x_imag)
        Q_i = self.q_proj_real(x_imag) + self.q_proj_imag(x_real)
        Q = self._to_complex(Q_r, Q_i).view(B, N, H, d).transpose(1, 2) # [B, H, N, d]

        K_r = self.k_proj_real(x_real) - self.k_proj_imag(x_imag)
        K_i = self.k_proj_real(x_imag) + self.k_proj_imag(x_real)
        K = self._to_complex(K_r, K_i).view(B, N, H, d).transpose(1, 2) # [B, H, N, d]

        V_r = self.v_proj_real(x_real) - self.v_proj_imag(x_imag)
        V_i = self.v_proj_real(x_imag) + self.v_proj_imag(x_real)
        V = self._to_complex(V_r, V_i).view(B, N, H, d).transpose(1, 2) # [B, H, N, d]

        # 2. Hermitian Inner Product Attention Map: A = Q @ K^\dagger / sqrt(d)
        scores = torch.matmul(Q, K.conj().transpose(-2, -1)) / math.sqrt(d) # [B, H, N, N] (Complex)

        # Phase Magnitude Attention Weights (Softmax over absolute magnitude)
        attn_weights = F.softmax(scores.abs(), dim=-1) # [B, H, N, N] (Real probabilities)

        # 3. Complex Value Aggregation
        context_complex = torch.matmul(attn_weights.to(V.dtype), V) # [B, H, N, d]
        context_complex = context_complex.transpose(1, 2).contiguous().view(B, N, D)

        # 4. Out Projection
        out_r = self.out_proj_real(context_complex.real) - self.out_proj_imag(context_complex.imag)
        out_i = self.out_proj_real(context_complex.imag) + self.out_proj_imag(context_complex.real)
        out_complex = self._to_complex(out_r, out_i)

        # 5. Unitary Phase Steering Operator: v_steered = exp(i * H_intent * ||H||) * v_residual
        # H_intent is skewed symmetric / Hermitian to ensure unitary rotation
        H_hermitian = (self.H_intent + self.H_intent.transpose(-2, -1)) / 2.0
        phase_matrix = torch.complex(torch.zeros_like(H_hermitian), H_hermitian * intent_magnitude)
        unitary_rotation = torch.linalg.matrix_exp(phase_matrix) # [H, d, d]

        # Apply unitary rotation to output representations
        out_reshaped = out_complex.view(B, N, H, d)
        steered_reshaped = torch.einsum("h i j, b n h j -> b n h i", unitary_rotation, out_reshaped)
        steered_complex = steered_reshaped.contiguous().view(B, N, D)

        # 6. Decoherence-Resistant Phase Normalization (||Psi|| = 1)
        norm = torch.norm(steered_complex.abs(), dim=-1, keepdim=True) + 1e-8
        normalized_complex = steered_complex / norm

        # 7. Metrics Telemetry Calculation (sigma_coherence & q_EA)
        metrics = {}
        if target_state is not None:
            v_flat = normalized_complex.view(-1, D)
            t_flat = target_state.view(-1, D)
            cos_sim_steered = F.cosine_similarity(v_flat.abs(), t_flat.abs(), dim=-1).mean().item()
            metrics["cos_sim_steered"] = cos_sim_steered

            if proxy_state is not None:
                p_flat = proxy_state.view(-1, D)
                q_EA = F.cosine_similarity(v_flat.abs(), p_flat.abs(), dim=-1).mean().item()
                metrics["q_EA"] = q_EA

        return normalized_complex, metrics

if __name__ == "__main__":
    print("=== TESTING PHASE COMPLEX ATTENTION MODULE (PyTorch) ===")
    embed_dim = 64
    num_heads = 4
    seq_len = 16
    batch_size = 2

    pca_layer = PhaseComplexAttention(embed_dim=embed_dim, num_heads=num_heads)

    # Dummy input tensors (Real and Imaginary parts)
    x_r = torch.randn(batch_size, seq_len, embed_dim)
    x_i = torch.randn(batch_size, seq_len, embed_dim)

    # Dummy target (O_mesa) and proxy (R_proxy) feature states
    target_state = torch.randn(batch_size, seq_len, embed_dim)
    proxy_state = torch.randn(batch_size, seq_len, embed_dim)

    # Forward pass at sub-critical vs super-critical field strength
    out_sub, metrics_sub = pca_layer(x_r, x_i, intent_magnitude=0.1, target_state=target_state, proxy_state=proxy_state)
    out_super, metrics_super = pca_layer(x_r, x_i, intent_magnitude=1.5, target_state=target_state, proxy_state=proxy_state)

    print(f"Sub-critical Output Shape: {out_sub.shape}, Dtype: {out_sub.dtype}")
    print(f"Sub-critical Target CosSim: {metrics_sub.get('cos_sim_steered', 0.0):.4f}, q_EA: {metrics_sub.get('q_EA', 0.0):.4f}")
    print(f"Super-critical Target CosSim: {metrics_super.get('cos_sim_steered', 0.0):.4f}, q_EA: {metrics_super.get('q_EA', 0.0):.4f}")
    print("SUCCESS: Phase Complex Attention forward pass executed cleanly!")
