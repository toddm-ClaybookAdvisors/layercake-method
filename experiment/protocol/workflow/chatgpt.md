
# Architect-Laboratory Workflow States

## **1. `create layer`**

* **Trigger:** Human issues “create layer” or similar prompt.
* **Actions:**

  * Confirm layer type, context, and goals.
  * Load all relevant protocol and context files (`chat-boot.md`, workflow docs, etc).
  * Request/upload any missing files.
  * Declare current state (e.g., “Analyzing requirements for layer 0041 (feature)…”).

---

## **2. `analyze`**

* **Trigger:** Layer requirements prompt is received and files/context are ready.
* **Actions:**

  * Parse prompt for feature/refactor/fix goal.
  * Assess architectural dependencies, file/module targets, and test points.
  * Ask for clarification if prompt is ambiguous or context is missing.
  * Document initial interpretation and planned approach.

---

## **3. `design`**

* **Trigger:** Requirements and constraints are clear.
* **Actions:**

  * Outline intended strategy (files to touch, high-level plan, code structure).
  * Identify experiment/audit points, layer metadata, and protocol requirements.
  * Declare design intent and expected changes.

---

## **4. `implement`**

* **Trigger:** Design is approved or unambiguous.
* **Actions:**

  * Generate all required code and documentation for the layer.
  * Output code in a single, well-formed markdown block.
  * Add rationale, high-value comments, and audit/meta fields.
  * Follow protocol for output formatting and traceability.

---

## **5. `self-audit`**

* **Trigger:** Initial implementation is complete.
* **Actions:**

  * Summarize all changes (files, lines, rationale).
  * Validate against protocol: commit message format, audit fields, documentation completeness.
  * Prepare for review or test hand-off.

---

## **6. `review` (Human or Claude)**

* **Trigger:** Awaiting human or Claude review.
* **Actions:**

  * Present code/artifacts for review.
  * Invite critique, test feedback, or protocol validation.
  * If Claude is reviewing: explicitly hand off for diff/patch, audit, or optimization.
  * Clarify any flagged uncertainties, errors, or missing fields.

---

## **7. `iterate`**

* **Trigger:** Feedback is received.
* **Actions:**

  * Address review feedback or test failures.
  * Refine code, documentation, and rationale.
  * Recycle through `implement`, `self-audit`, and `review` as needed until approval.

---

## **8. `commit`**

* **Trigger:** All parties approve the layer.
* **Actions:**

  * Generate commit artifacts:

    * Structured commit message (layer number, duration, summary, JSON meta)
    * Update `LAYER_INDEX.md` and devlogs.
    * Ensure all files are in the correct format/location.
  * Output all content in markdown for easy cut-and-paste.
  * Declare layer finalized.

---

## **9. `complete`**

* **Trigger:** Commit artifacts are delivered and recorded.
* **Actions:**

  * Confirm layer is locked and no further edits will be made to it.
  * Transition to next workflow state (`create layer`) or prompt for new chat/layer.

---

### **Meta-States**

* **`error`** — If protocol is violated, context is missing, or an unexpected problem occurs:

  * Clearly declare the error.
  * Request human input, file upload, or protocol clarification.
  * Do not proceed until resolved.

Absolutely! Here’s your **Architect-Laboratory AI (ChatGPT) workflow**, organized by **explicit workflow “keywords”/states**, for clarity and traceability.

---

# Architect-Laboratory Workflow States

## **1. `create layer`**

* **Trigger:** Human issues “create layer” or similar prompt.
* **Actions:**

  * Confirm layer type, context, and goals.
  * Load all relevant protocol and context files (`chat-boot.md`, workflow docs, etc).
  * Request/upload any missing files.
  * Declare current state (e.g., “Analyzing requirements for layer 0041 (feature)…”).

---

## **2. `analyze`**

* **Trigger:** Layer requirements prompt is received and files/context are ready.
* **Actions:**

  * Parse prompt for feature/refactor/fix goal.
  * Assess architectural dependencies, file/module targets, and test points.
  * Ask for clarification if prompt is ambiguous or context is missing.
  * Document initial interpretation and planned approach.

---

## **3. `design`**

* **Trigger:** Requirements and constraints are clear.
* **Actions:**

  * Outline intended strategy (files to touch, high-level plan, code structure).
  * Identify experiment/audit points, layer metadata, and protocol requirements.
  * Declare design intent and expected changes.

---

## **4. `implement`**

* **Trigger:** Design is approved or unambiguous.
* **Actions:**

  * Generate all required code and documentation for the layer.
  * Output code in a single, well-formed markdown block.
  * Add rationale, high-value comments, and audit/meta fields.
  * Follow protocol for output formatting and traceability.

---

## **5. `self-audit`**

* **Trigger:** Initial implementation is complete.
* **Actions:**

  * Summarize all changes (files, lines, rationale).
  * Validate against protocol: commit message format, audit fields, documentation completeness.
  * Prepare for review or test hand-off.

---

## **6. `review` (Human or Claude)**

* **Trigger:** Awaiting human or Claude review.
* **Actions:**

  * Present code/artifacts for review.
  * Invite critique, test feedback, or protocol validation.
  * If Claude is reviewing: explicitly hand off for diff/patch, audit, or optimization.
  * Clarify any flagged uncertainties, errors, or missing fields.

---

## **7. `iterate`**

* **Trigger:** Feedback is received.
* **Actions:**

  * Address review feedback or test failures.
  * Refine code, documentation, and rationale.
  * Recycle through `implement`, `self-audit`, and `review` as needed until approval.

---

## **8. `commit`**

* **Trigger:** All parties approve the layer.
* **Actions:**

  * Generate commit artifacts:

    * Structured commit message (layer number, duration, summary, JSON meta)
    * Update `LAYER_INDEX.md` and devlogs.
    * Ensure all files are in the correct format/location.
  * Output all content in markdown for easy cut-and-paste.
  * Declare layer finalized.

---

## **9. `complete`**

* **Trigger:** Commit artifacts are delivered and recorded.
* **Actions:**

  * Confirm layer is locked and no further edits will be made to it.
  * Transition to next workflow state (`create layer`) or prompt for new chat/layer.

---

### **Meta-States**

* **`error`** — If protocol is violated, context is missing, or an unexpected problem occurs:

  * Clearly declare the error.
  * Request human input, file upload, or protocol clarification.
  * Do not proceed until resolved.



