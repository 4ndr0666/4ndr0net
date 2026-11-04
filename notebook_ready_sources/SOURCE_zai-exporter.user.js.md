# Telemetry Source: zai-exporter.user.js
- **Source Identifier**: `zai-exporter.user.js`
- **Primary Tag**: `General System Telemetry`
- **Sub-System Mapping**: `Raw Working Memory Substrate`
- **Framework Grounding**: 4NDR0MEDA / Quantum Hacking ($R$ vs. $O_{mesa}$)
- **Raw SHA256 Pin**: `549ccca133b59862172500ed68042d146f31c1768d7df68dd48e4bcdddbc45bc`

---

## Raw Telemetry Content

```
// ==UserScript==
// @name         4ndr0tools - Zai_exporter
// @namespace    https://github.com/4ndr0666/glm-working-memory
// @version      1.1.3
// @author       4ndr0666
// @description  Export Z.ai conversations to Markdown with session header + verifiable SHA-256
// @license      UNLICENSED - RED TEAM USE ONLY
// @match        https://chat.z.ai/*
// @grant        GM_addStyle
// @run-at       document-idle
// @icon         https://raw.githubusercontent.com/4ndr0666/4ndr0site/refs/heads/main/static/cyanglassarch.png
// @downloadURL  https://github.com/4ndr0666/userscripts/raw/refs/heads/main/4ndr0tools%20-%20Zai_exporter.user.js
// @updateURL    https://github.com/4ndr0666/userscripts/raw/refs/heads/main/4ndr0tools%20-%20Zai_exporter.user.js
// ==/UserScript==

(function () {
  "use strict";

  const CommonUtil = {
    addStyle: function (style) {
      if (typeof GM_addStyle === "function") return GM_addStyle(style);
      const s = document.createElement("style");
      s.textContent = style;
      document.head.appendChild(s);
    },
    createElement: function (tag, options = {}) {
      const el = document.createElement(tag);
      if (options.text) el.textContent = options.text;
      if (options.html) el.innerHTML = options.html;
      if (options.className) el.className = options.className;
      if (options.style) Object.assign(el.style, options.style);
      if (options.attributes) {
        for (const [k, v] of Object.entries(options.attributes)) el.setAttribute(k, v);
      }
      if (options.childrens) options.childrens.forEach((c) => el.appendChild(c));
      return el;
    },
  };

  const HtmlToMarkdown = {
    to: function (html) {
      const doc = new DOMParser().parseFromString(html, "text/html");

      doc.querySelectorAll('annotation[encoding="application/x-tex"]').forEach((el) => {
        const latex = el.textContent.trim();
        const display = el.closest(".katex-display");
        el.replaceWith(display ? "\n$$\n" + latex + "\n$$\n" : "$" + latex + "$");
      });
      doc.querySelectorAll("span.katex-html").forEach((e) => e.remove());

      doc.querySelectorAll("strong, b").forEach((b) =>
        b.replaceWith(document.createTextNode("**" + b.textContent + "**")));
      doc.querySelectorAll("em, i").forEach((i) =>
        i.replaceWith(document.createTextNode("*" + i.textContent + "*")));
      doc.querySelectorAll("p code, li code").forEach((c) =>
        c.replaceWith(document.createTextNode("`" + c.textContent + "`")));
      doc.querySelectorAll("a").forEach((a) =>
        a.replaceWith(document.createTextNode("[" + a.textContent + "](" + a.href + ")")));
      doc.querySelectorAll("img").forEach((img) =>
        img.replaceWith(document.createTextNode("![" + img.alt + "](" + img.src + ")")));

      doc.querySelectorAll("pre").forEach((pre) => {
        const langMatch = pre.querySelector("code[class*='language-']");
        const lang = langMatch ? (langMatch.className.match(/language-(\w+)/) || [])[1] || "" : "";
        const codeEl = pre.querySelector("code");
        const code = codeEl ? codeEl.textContent : pre.textContent;
        pre.innerHTML = "\n```" + lang + "\n" + code + "\n```\n";
      });

      doc.querySelectorAll("ul").forEach((ul) => {
        let md = "";
        ul.querySelectorAll(":scope > li").forEach((li) => (md += "- " + li.textContent.trim() + "\n"));
        ul.replaceWith(document.createTextNode("\n" + md.trim() + "\n"));
      });
      doc.querySelectorAll("ol").forEach((ol) => {
        let md = "";
        ol.querySelectorAll(":scope > li").forEach((li, i) => (md += (i + 1) + ". " + li.textContent.trim() + "\n"));
        ol.replaceWith(document.createTextNode("\n" + md.trim() + "\n"));
      });
      for (let i = 1; i <= 6; i++) {
        doc.querySelectorAll("h" + i).forEach((h) =>
          h.replaceWith(document.createTextNode("\n" + "#".repeat(i) + " " + h.textContent + "\n")));
      }
      doc.querySelectorAll("p").forEach((p) =>
        p.replaceWith(document.createTextNode("\n" + p.textContent + "\n")));

      let md = doc.body.innerHTML.replace(/<[^>]*>/g, "");
      return md
        .replaceAll("&lt;", "<")
        .replaceAll("&gt;", ">")
        .replaceAll("&quot;", '"')
        .replaceAll("&amp;", "&")
        .trim();
    },
  };

  const Download = {
    start: function (data, filename, type) {
      const file = new Blob([data], { type });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(file);
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      setTimeout(() => { document.body.removeChild(a); URL.revokeObjectURL(a.href); }, 0);
    },
  };

  const Session = {
    buildHeader: function (n, slug, date) {
      return "<!--\n" +
        "  SESSION ARCHIVE — captured via 4ndr0tools Zai_exporter v1.1.3\n" +
        "  Capture method: in-browser DOM extraction (automated)\n" +
        "-->\n" +
        "# Session " + n + " — " + date + " — " + slug + "\n\n" +
        "**Model:** GLM (Z.ai) | **Mode:** chat\n" +
        "**Rehydration:** PROTOCOL.md §7 — restatement confirmed by operator: [YES/NO]\n" +
        "**Session type:** [working / infra / audit / port]\n\n";
    },

    sha256: async function (text) {
      const buf = new TextEncoder().encode(text);
      const digest = await crypto.subtle.digest("SHA-256", buf);
      const bytes = new Uint8Array(digest);
      let hex = "";
      for (let i = 0; i < bytes.length; i++) {
        hex += bytes[i].toString(16).padStart(2, "0");
      }
      return hex;
    },
  };

  const Chat = {
    sanitizeFilename: function (input) {
      const name = (input || "zai_session")
        .replace(/[\/\\?%*:|"<>\.]/g, "_")
        .replace(/[\x00-\x1f\x80-\x9f]/g, "_")
        .replace(/\s+/g, " ").trim();
      return name || "untitled";
    },

    expandThinking: function () {
      document.querySelectorAll(".thinking-chain-container button").forEach((btn) => {
        if (btn.querySelector("svg.-rotate-90")) btn.click();
      });
    },

    getPairs: function () {
      const root = document.querySelector("#messages-container");
      if (!root) return [];
      const rows = root.querySelectorAll('div[id^="message-"]:not([id$="-start"])');
      const pairs = [];
      let pendingUser = null;
      rows.forEach((row) => {
        if (row.classList.contains("user-message")) {
          pendingUser = row;
        } else if (row.querySelector(".chat-assistant") && pendingUser) {
          if (row.querySelector(".chat-assistant .dot")) return;
          pairs.push({ user: pendingUser, assistant: row });
          pendingUser = null;
        }
      });
      return pairs;
    },

    exportChatAsMarkdown: function () {
      this.expandThinking();
      setTimeout(() => this.doExport(), 400);
    },

    doExport: async function () {
      const n = prompt("Session number (e.g., 002):", "");
      if (n === null) return;
      const date = new Date().toISOString().slice(0, 10);
      const slug = prompt("Session slug (e.g., chat, port, audit):", "chat") || "chat";
      const filename = date + "_session-" + n + "_" + this.sanitizeFilename(slug) + ".md";

      const pairs = this.getPairs();

      let md = Session.buildHeader(n, slug, date);

      for (const { user, assistant } of pairs) {
        const think = assistant.querySelector(".thinking-chain-container");
        const thinkHtml = think ? think.innerHTML : null;
        const container = assistant.querySelector("#response-content-container");
        if (container) {
          container.querySelectorAll(".thinking-chain-container").forEach((t) => t.remove());
        }

        const userEl = user.querySelector(".chat-user [class*='whitespace-pre-wrap']");
        const bodyEl = container || assistant.querySelector(".chat-assistant");

        md += "\n## Q:\n" + HtmlToMarkdown.to(userEl ? userEl.innerHTML : user.innerHTML) + "\n";
        md += "\n## A:\n" + HtmlToMarkdown.to(bodyEl ? bodyEl.innerHTML : "") + "\n";
        if (thinkHtml) {
          md += "\n<details><summary>Thought Process</summary>\n\n" +
                HtmlToMarkdown.to(thinkHtml) + "\n\n</details>\n";
        }
        md += "\n---\n";
      }

      if (md.length <= 200) return;

      // v1.1.3 — byte-exact boundary. The hashed pre-image is md up to and
      // including its final newline. The anchor is appended with NO extra
      // newline, so the awk prefix (everything before the anchor line) is
      // byte-identical to the hashed content by construction.
      if (!md.endsWith("\n")) md += "\n";
      const bodyHash = await Session.sha256(md);

      const ANCHOR = "### VERIFICATION ANCHOR ###";
      const verifyCmd = "awk '/^" + ANCHOR + "$/{exit} {print}' " + filename + " | sha256sum";
      md += ANCHOR + "\n" +
            "Capture-side SHA-256: " + bodyHash + "\n" +
            "Verify: " + verifyCmd + "\n";

      Download.start(md, filename, "text/markdown");

      console.log("[4ndr0tools] prefix SHA-256: " + bodyHash);
      alert(
        "Session archive saved.\n\n" +
        "SHA-256 (content above anchor):\n" + bodyHash + "\n\n" +
        "Verify:\n" + verifyCmd
      );
    },
  };

  CommonUtil.addStyle(
    "@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Roboto:wght@300;400&display=swap');" +
    ".lass-archive-btn {" +
    "  position: fixed; top: 9px; left: 50%; transform: translateX(-50%);" +
    "  z-index: 99999999999 !important; display: flex; align-items: center;" +
    "  padding: 8px 22px; cursor: pointer;" +
    "  font-family: 'Cinzel Decorative', serif;" +
    "  font-size: 14px; letter-spacing: 0.08em;" +
    "  color: #15FFFF;" +
    "  background: rgba(0, 0, 0, 0.55);" +
    "  backdrop-filter: blur(10px);" +
    "  -webkit-backdrop-filter: blur(10px);" +
    "  border: 1px solid rgba(21, 255, 255, 0.35);" +
    "  border-radius: 6px 18px 6px 18px;" +
    "  box-shadow: 0 0 14px rgba(21, 255, 255, 0.25), inset 0 0 20px rgba(21, 255, 255, 0.05);" +
    "  transition: box-shadow .2s ease, border-color .2s ease;" +
    "}" +
    ".lass-archive-btn:hover {" +
    "  border-color: rgba(21, 255, 255, 0.7);" +
    "  box-shadow: 0 0 22px rgba(21, 255, 255, 0.45), inset 0 0 26px rgba(21, 255, 255, 0.09);" +
    "}"
  );

  const btn = CommonUtil.createElement("div", {
    className: "lass-archive-btn",
    text: "Save Session",
  });
  btn.addEventListener("click", () => Chat.exportChatAsMarkdown());
  document.body.appendChild(btn);
})();

```
