"""Styling constants for a ChatGPT / Gemini-style Gradio interface."""

# AI Assistant Palette (Minimal Dark Space with Soft Accents)
PRIMARY = "#10a37f"       # ChatGPT Signature Emerald
SURFACE_BG = "#1e1e2e"    # Modern Deep Slate Background
CARD_BG = "#27273a"       # Floating Bubble / Sidebar Background
INPUT_BG = "#2f2f46"      # Input Field Fill Color
TEXT_PRIMARY = "#ececfe"  # Off-white crisp body text
TEXT_MUTED = "#9e9ebc"    # Muted secondary text

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = f"""
/* ---------- Global ChatGPT / Gemini Canvas ---------- */
:root {{
  --bg-dark: {SURFACE_BG};
  --surface-dark: {CARD_BG};
  --input-bg: {INPUT_BG};
  --accent-green: {PRIMARY};
  --text-main: {TEXT_PRIMARY};
  --text-muted: {TEXT_MUTED};
  --border-light: rgba(255, 255, 255, 0.08);
}}

html, body, gradio-app {{
  background-color: var(--bg-dark) !important;
  color: var(--text-main) !important;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
  height: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
}}

/* Expand container full screen */
.gradio-container {{
  background-color: var(--bg-dark) !important;
  max-width: 100% !important;
  width: 100% !important;
  height: 100vh !important;
  margin: 0 auto !important;
  padding: 0 !important;
  display: flex !important;
  flex-direction: column !important;
}}

.gradio-container .main {{
  height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
}}

/* ---------- Header Bar ---------- */
.gradio-container h1 {{
  color: var(--text-main) !important;
  font-size: 18px !important;
  font-weight: 600 !important;
  text-align: center !important;
  padding: 16px 0 !important;
  margin: 0 !important;
  border-bottom: 1px solid var(--border-light) !important;
  background: var(--bg-dark) !important;
}}

/* ---------- Clean Chat Area (No Outer Borders) ---------- */
.chatbot, .chatbot.block {{
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  flex-grow: 1 !important;
  height: auto !important;
  padding: 20px 0 !important;
  max-width: 800px !important;
  width: 100% !important;
  margin: 0 auto !important;
}}

/* Hide standard Gradio header tags & footers */
.chatbot > .block-label, .chatbot .label-wrap, footer, .built-with, .show-api {{
  display: none !important;
}}

/* ---------- Message Bubbles ---------- */
.message-row {{
  padding: 16px 0 !important;
  background: transparent !important;
  border: none !important;
}}

.message-row .message {{
  font-size: 15px !important;
  line-height: 1.65 !important;
  padding: 14px 20px !important;
  border-radius: 18px !important;
  max-width: 85% !important;
  box-shadow: none !important;
}}

/* User Message: Dark Slate Bubble Floating Right */
.message-row.user-row .message,
.message-row[data-role="user"] .message {{
  background-color: var(--surface-dark) !important;
  color: var(--text-main) !important;
  border: 1px solid var(--border-light) !important;
  border-bottom-right-radius: 4px !important;
}}

/* Assistant Message: Clean Text Left-Aligned */
.message-row.bot-row .message,
.message-row[data-role="assistant"] .message {{
  background-color: transparent !important;
  color: var(--text-main) !important;
  border: none !important;
  padding-left: 0 !important;
}}

/* Typography adjustments */
.message-row p {{
  margin-bottom: 12px !important;
}}
.message-row p:last-child {{
  margin-bottom: 0 !important;
}}

/* ---------- ChatGPT Floating Input Capsule ---------- */
.input-row, form[class*="input"], .chat-input-row {{
  max-width: 800px !important;
  width: 100% !important;
  margin: 0 auto 24px auto !important;
  padding: 0 16px !important;
  background: transparent !important;
}}

textarea, input[type="text"] {{
  background-color: var(--input-bg) !important;
  border: 1px solid var(--border-light) !important;
  color: var(--text-main) !important;
  border-radius: 26px !important;
  padding: 14px 22px !important;
  font-size: 15px !important;
  line-height: 1.5 !important;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2) !important;
  transition: border-color 0.2s ease !important;
}}

textarea:focus, input[type="text"]:focus {{
  border-color: rgba(255, 255, 255, 0.25) !important;
  outline: none !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3) !important;
}}

textarea::placeholder, input::placeholder {{
  color: var(--text-muted) !important;
}}

/* Circular Send Button */
button.primary, button.submit, .submit-button {{
  background-color: var(--accent-green) !important;
  border-radius: 50% !important;
  width: 42px !important;
  height: 42px !important;
  min-height: 42px !important;
  min-width: 42px !important;
  padding: 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  border: none !important;
  margin-left: 8px !important;
  align-self: center !important;
}}

button.primary:hover, button.submit:hover {{
  background-color: #0e8e6d !important;
  transform: scale(1.03);
}}

button.primary svg, button.submit svg {{
  fill: #ffffff !important;
  width: 18px !important;
  height: 18px !important;
}}

/* ---------- Floating Example Chips ---------- */
.examples, .examples-holder {{
  max-width: 800px !important;
  margin: 0 auto 16px auto !important;
  padding: 0 16px !important;
  background: transparent !important;
}}

.examples table, .examples-table {{
  background: transparent !important;
  border: none !important;
}}

.examples button, .example {{
  background-color: var(--surface-dark) !important;
  border: 1px solid var(--border-light) !important;
  color: var(--text-muted) !important;
  border-radius: 16px !important;
  font-size: 13px !important;
  padding: 8px 16px !important;
  transition: all 0.2s ease !important;
}}

.examples button:hover, .example:hover {{
  background-color: var(--input-bg) !important;
  color: var(--text-main) !important;
  border-color: rgba(255, 255, 255, 0.2) !important;
}}

/* Custom Minimal Scrollbar */
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{ background: rgba(255, 255, 255, 0.15); border-radius: 10px; }}
::-webkit-scrollbar-thumb:hover {{ background: rgba(255, 255, 255, 0.3); }}
"""

JS = """
() => {
  document.title = 'ChatGPT';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""