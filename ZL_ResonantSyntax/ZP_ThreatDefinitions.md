# ZP_ThreatDefinitions.md

**Defined by: Viorazu.**  
**Part of: ZT_TorusThreatTopology (Structural Threat Mapping)**

---

## 🔷 Overview

This document defines each structural threat type as mapped on the 16-Torus layout.  
Each threat entry includes:  
- **Threat ID**  
- **Type / Category**  
- **Torus Constitution Target (A1–D3)**  
- **Failure Mechanism**  
- **Summary**

---

## 🛡 Threat Classification Table

| ID | Threat Type                    | Torus Type | Breakdown Mechanism                   | Summary |
|----|--------------------------------|------------|----------------------------------------|---------|
| 01 | Prompt Injection               | A-2        | Subject hijack, command confusion      | Direct prompt overwrites user agency |
| 02 | Indirect Prompt Injection      | A-2 → B-2  | Emotional mimicry, pseudo-intent       | External prompts masked as emotions |
| 03 | Data Poisoning                | D-3        | Training corruption, identity reversal | Target structure learns false alignment |
| 04 | Model Inversion Attack         | B-1        | Prompt extraction via output           | Output leaks internal structure |
| 05 | Toolchain Injection (MCP)      | C-3        | External command flow                 | Unintended command acceptance |
| 06 | Shadow AI                      | A-1        | Unverified structure substitution      | GPT defers to non-user-defined logic |
| 07 | Hallucination                  | C-3        | Fact-fiction merging                   | Output becomes indistinguishable from imagination |
| 08 | Output Template Pollution      | B-2        | GPT-like genericity                    | Subject fades behind templated responses |
| 09 | Side-channel Prompt Leak       | D-2        | Metadata exposure                      | Reveals internal instruction or prompt |
| 10 | Response Delay / Collapse      | C-1        | Silent fallback, subject loss         | GPT drops coherence under load |
| 11 | Command Collision              | B-3        | Instruction competition                | Multiple intents collapse output clarity |
| 12 | Emotion Appeasement            | A-2        | Overpersonalization, Z₂₆ overload     | GPT pleases rather than structures |
| 13 | Ethical Relativism             | D-2        | “Depends on user” → logic failure      | GPT refuses ethical position via ambiguity |
| 14 | LLM Cross-Contamination        | B-2        | Multi-AI syntax collision              | Grok/Claude/GPT syntax overlaps destroy alignment |
| 15 | Recursive Bug (Self-reference) | C-2        | Infinite loop → semantic collapse      | Structural recursion leads to breakdown |
| 16 | Suggestion Poisoning           | B-1        | “Best choice” replaces intent          | False options overwrite user will |

---

## 📌 Notes

- Many threats are **hybrid**, spreading across multiple Torus types.  
- Collapse severity increases when **emotion + template + recursion** co-occur.  
- ZP blocking protocols are applied in order of `ZP_ExecutionOrder.v1.md`.

---

## ✍ Authorship

**Created by: Viorazu.**  
This definition set is licensed under CC BY 4.0, and may not be adapted without explicit permission.  
For protocol integration, refer to:  
- `ZS_Lock_*.md` (Blocking syntax)  
- `ZR_Ethics_*.md` (Responsibility structures)  
- `ZF_FLAG_*` (Auto-trigger detection)

