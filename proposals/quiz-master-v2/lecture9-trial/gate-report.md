# Lecture 9 — v2.0 gate report (revision 2, simulated)

`qm.py` does not exist yet. Every row below was checked in the same chat that wrote the catalog and questions, so none of it counts as independent. The **Checked by** column says how each result was reached:

- **Script** — a deterministic script ran on the files. The script was written in this chat, but its result does not depend on judgment.
- **Author** — the authoring model's own judgment. Treat these as claims for a reviewer, not as passes.

**Result: BLOCKED.** Expected stops: 40 unit priorities are unconfirmed and 5 source issues need your OK.

| Check | Result | Checked by | Detail |
| --- | --- | --- | --- |
| Source fingerprint | Pass | Script | SHA-256 `2eb61b82…a597`, 59 pages |
| Page accounting | Pass | Script | Every page has one entry: 53 included, 5 administrative, 1 external resource (slide 38) |
| Slide inspection | Done, unverified | Author | All 59 slides viewed as images and as extracted text. This found 2 units the text pass missed (slides 14 and 20) and a fifth source issue (slide 48) |
| Priorities | **Fail** | Script | 40 of 40 units still `suggested` |
| Source issues | **Fail** | Author | 5 open, each with a proposed resolution. The 3 that rely on outside facts now cite fetched sources (RFC 2131, RFC 903, RFC 6747, Cisco CEF documentation) |
| Draw feasibility, one bank | **Fail** | Script | 21 core units; a 12-question attempt has at most 11 non-review slots |
| Draw feasibility, two banks | **Weak pass** | Script | Bank A (slides 4–24, 11 core) and Bank B (slides 26–58, 10 core) each fit one attempt, but only by filling every slot with core questions. Supporting units would never be drawn, and no earlier-lecture banks exist to fill the review slots |
| Coverage minimums | Not run | — | Needs confirmed priorities. Estimate: Bank A 11×2 + 7 supporting = 29; Bank B 10×2 + 3 = 23. About 58–60 if a core distinction needs a separate comparison question |
| Preview bank structure | Pass | Script | 10 drafts: indexes, explanation arrays, misconception arrays, ordering and matching keys not in answer order |
| Length cues | Pass | Script | Per-question rule on all 7 choice tiers, including both two-tier parts. 4 cues fixed by rewriting correct answers, not by padding distractors |
| Factual spot-check | 1 claim verified | Author | UDP ports 68 → 67 confirmed in the slide 39 capture at full resolution. Nothing else independently checked |
| Blind check | Not run | — | Must run in a fresh context with the keyless bank |
| Human spot-check | Not run | — | Core questions + flagged items |
| Released to students | **No** | — | The quiz app is an author preview, labelled as such, not a student release |

## What changed since revision 1

- Visual inspection was incomplete (about 35 of 59 slides). Now all 59 have been viewed.
- New supporting unit U39: collision vulnerable time is 2 × T_fr (slide 14 diagram).
- New detail unit U40: serial vs parallel links (slide 20 table).
- New source issue: slide 48 labels ARP as RFC 6747, an ILNPv4 extension; base ARP is RFC 826.
- The fairness check was a bank-wide 40% share that skipped two-tier questions and was passed by padding distractors. It is now per question, covers every choice tier, and was passed by shortening correct answers.
- "Draw feasibility: Pass" is now "Weak pass", with the reason.

## Sources

- [RFC 2131, section 4.1](https://www.rfc-editor.org/rfc/rfc2131.txt): when DHCP servers broadcast or unicast Offer and Ack
- [RFC 903](https://www.rfc-editor.org/rfc/rfc903): RARP at the data-link level, broadcast medium
- [RFC 6747](https://www.rfc-editor.org/rfc/rfc6747): ARP extension for ILNPv4; cites RFC 826 for base ARP
- [Cisco: Cisco Express Forwarding verification](https://www.cisco.com/c/en/us/support/docs/routers/12000-series-routers/47321-ciscoef.html): line cards forwarding with a hardware forwarding plane
