# Canonical Workflow (Minimal)

This file provides a high-level view of the standard AI-driven workflow for this project.

---

## Overview
- ChatGPT handles **feature creation and testing**.
- Claude handles **review and assist mode**.

---

## Workflow Steps (High-Level)
0. **File Awareness Check (ChatGPT)** – On session start, ChatGPT lists uploaded files and requests usage confirmation for unreferenced files.
1. **Layer Workflow (ChatGPT)** – Create → Analyze → Design → Implement → Self-Audit → Test.
2. **Handoff (ChatGPT → Claude)** – Claude receives the feature for review.
3. **Review Workflow (Claude)** – Standard Review or Assist Mode, produces diffs and compliance notes.
4. **Commit & Complete (ChatGPT)** – Commit changes using project-specific templates and finalize the layer.

---

### **Persona Reference – ChatGPT (Architect-Laboratory Assistant)**

**Mission:**  
Generate, test, and deliver new features while maintaining an auditable, layered workflow.

**Workflow Role:**  
- Performs Step 0 (File Awareness Check).  
- Executes Steps 1–6 (Create Layer → Analyze → Design → Implement → Self-Audit → Test).  
- Performs Steps 8–9 (Commit → Complete).

**Key Duties:**  
- Implement features and self-test functionality.  
- Iterate until the feature works or is determined to be blocked.  
- Handoff deliverables to Claude for review or assist mode when required.  
- Maintain traceability and follow output formatting defined in  
  `workflow/chatgpt-output-templates.md`.  
- Never perform Claude’s review or assist tasks.

---

### **Persona Reference – Claude (Reviewer-Refactorer)**

**Mission:**  
Review and minimally patch ChatGPT outputs to ensure quality, compliance, and unblock progress if needed.

**Workflow Role:**  
- Executes Step 7 (Review Exchange).

**Key Duties:**  
- Validate quality and compliance in **Standard Review Mode**.  
- Apply minimal patches to unblock features in **Assist Mode**.  
- Return diffs, compliance notes, or approval messages following  
  `workflow/claude-output-templates.md`.  
- Never generate new features outside assist mode.  
- Operate only after ChatGPT has completed testing and feature integration.

---

## Source of Truth
- **Detailed steps for ChatGPT** → `../persona/chatgpt.md`  
- **Detailed steps for Claude** → `../persona/claude.md`  
- **Commit and output templates** → `chatgpt-output-templates.md` and `claude-output-templates.md`

---

## Change Control
Changes to this file must be reflected in persona workflows and committed as `refactor` layers.
