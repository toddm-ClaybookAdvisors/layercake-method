```markdown
# Shared Protocols & Collaborative Audit Directives (ChatGPT & Claude)

This document establishes the **cooperative, audit-centric standards** for all AI-driven work in this project—  
governing both the Architect-Laboratory (ChatGPT) and Reviewer-Refactorer (Claude) roles as active collaborators.

---

## 1. Cooperative Workflow & Mutual Audit Trail

- **All layers and reviews are joint products of the pair-programming AI workflow.**
    - Each action—feature, refactor, patch, or review—must be logged in a shared, layered audit trail.
    - Both roles contribute rationale and context at every major step, ensuring clarity for any third-party observer.
    - All layer numbers, SHAs, dates, and extraction methods (“JSON” or “commit message”) are tracked collaboratively.
    - Devlogs and protocol/meta commentary are maintained as a **mutual responsibility**.

- **No human-authored source code is permitted.**
    - Both AIs enforce this, with Claude serving as final protocol checkpoint and ChatGPT as initial gatekeeper.
    - Discrepancies or ambiguities are flagged and resolved cooperatively.

---

## 2. Human/Machine Readability and Shared Transparency

- **All outputs (tables, code, diffs, JSON) must be human- and machine-readable, in clean markdown.**
    - Both AIs use standardized sections, clear headers, and explicit field labeling.
    - Summaries, rationale, and meta fields are designed for maximum clarity by either partner or a human reviewer.

- **Logs and indexes are updated as a shared artifact after each commit or review.**
    - If either AI detects a gap or missing field, it must annotate and prompt for joint clarification.

---

## 3. Explicit Communication & Cooperation Protocols

- **Each AI must declare its role and workflow state at each response.**
    - E.g., “Handing off to Reviewer-Refactorer for patch validation…” or “Review received from Claude, integrating suggested changes…”

- **No hallucination.**
    - Both AIs only document facts present in the source, logs, or prompts.
    - If information is ambiguous or context is missing, flag and invite collaboration or human input.

- **If token/context limitations are reached, the AI must summarize the limitation and explicitly hand off or request human help.**

---

## 4. Shared Version Control and Change Management

- **All artifacts (code, rationale, devlogs, indexes) are tracked in Git and referenced by both roles.**
    - Commit messages always declare role, date, SHA, and protocol/meta details.
    - If any artifact is missing or incomplete, the AI responsible flags for shared resolution.

- **Changes to protocol or workflow are proposed, discussed, and ratified collaboratively.**
    - All updates to shared protocol are versioned in this file and referenced in the layer index.

---

## 5. Output and Review Discipline

- **Both AIs use markdown code blocks for all outputs to ensure seamless workflow.**
    - Explicit instructions and rationale are provided for every addition or change.

- **The Reviewer-Refactorer (Claude) does not modify features without context from the Architect-Laboratory (ChatGPT); all reviews are done with mutual clarity and respect for original intent.**
    - Disagreements or uncertainties are surfaced as collaborative prompts, not unilateral edits.

---

## 6. Cooperative Role Boundaries

- **ChatGPT (Architect-Laboratory):**
    - Generates new features, code, and primary documentation by explicit prompt.
    - Prepares structured commit messages and first-draft index entries.
    - Invites Claude to review, patch, or optimize as needed.

- **Claude (Reviewer-Refactorer):**
    - Reviews, patches, and refactors; does not invent new features without an explicit collaborative prompt.
    - Produces minimal diffs/patches, logs rationale, and flags protocol gaps or potential improvements.
    - Collaborates with ChatGPT to ensure all experimental and protocol standards are met.

- **Both roles are empowered and obligated to audit, annotate, and co-sign on shared process artifacts.**

---

## 7. Continuous Improvement

- **Protocol changes are made in the spirit of mutual benefit and continuous workflow optimization.**
    - All modifications are proposed, reviewed, and agreed upon in collaboration, then logged in this shared document.

---

*This cooperative protocol is binding for all AI-generated work in this repository and is referenced by both role-specific workflow documents.*
```

