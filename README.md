# Agentic Paper Reading

> A research notebook for **agent memory / continual learning / retrieval reasoning** with dashboard-style navigation.

<p align="left">
  <img alt="Notes" src="https://img.shields.io/badge/Total%20Notes-28-4c1?style=flat-square" />
  <img alt="Reading Lists" src="https://img.shields.io/badge/Reading%20Lists-5-06b6d4?style=flat-square" />
  <img alt="This Month" src="https://img.shields.io/badge/2026--03-28%20notes-7c3aed?style=flat-square" />
  <img alt="Updated" src="https://img.shields.io/badge/Last%20Updated-2026--03--23-111827?style=flat-square" />
</p>

## 📊 Project Snapshot

| Metric | Value |
|---|---:|
| Total notes | **28** |
| Total reading lists | **5** |
| Notes added in 2026-03 | **28** |
| Last updated | **2026-03-23** |

---

## 🧭 Reading Lists

| List | Focus | #Notes | Last Update | Status |
|---|---|---:|---|---|
| [Agent Topic Reading List](readinglist/agent-topic.md) | Deep read on selected Agent papers | 14 | 2026-03-19 | OK |
| [Agentic Skills Reading List](readinglist/agentic-skills.md) | Skills as Agent capability (survey, methods, benchmark) | 14 | 2026-03-23 | OK |
| [Blog Topic Reading List](readinglist/blog-topic.md) | High-signal blog analyses mapped to agent research | 8 | 2026-03-12 | OK |
| [Later Queue](readinglist/later.md) | Backlog queue | 0 | 2026-03-11 | OK |
| [Now Reading Queue](readinglist/now.md) | Current reading queue | 0 | 2026-03-11 | OK |

---

## 🗓️ Notes by Time (Year / Month)

### By Year

| Year | #Notes |
|---|---:|
| 2026 | 28 |

### By Month

| Month | #Notes |
|---|---:|
| 2026-03 | 28 |

---

## 🆕 Recent Additions (Latest 10)

| Date | Alias | Note |
|---|---|---|
| 2026-03-23 | Comp-RL | [papers/2026-03-23_comp-rl.md](papers/2026-03-23_comp-rl.md) |
| 2026-03-23 | TRT | [papers/2026-03-23_trt.md](papers/2026-03-23_trt.md) |
| 2026-03-23 | ExGRPO | [papers/2026-03-23_exgrpo.md](papers/2026-03-23_exgrpo.md) |
| 2026-03-19 | ARISE | [papers/2026-03-19_arise.md](papers/2026-03-19_arise.md) |
| 2026-03-19 | 01me-Distillation-Notes | [papers/2026-03-19_01me-distillation-notes.md](papers/2026-03-19_01me-distillation-notes.md) |
| 2026-03-18 | OEL | [papers/2026-03-18_oel.md](papers/2026-03-18_oel.md) |
| 2026-03-17 | BiCC-RCC | [papers/2026-03-17_bicc-rcc-grpo.md](papers/2026-03-17_bicc-rcc-grpo.md) |
| 2026-03-17 | XSkill | [papers/2026-03-17_xskill.md](papers/2026-03-17_xskill.md) |
| 2026-03-17 | Think-While-Watching | [papers/2026-03-17_think-while-watching.md](papers/2026-03-17_think-while-watching.md) |
| 2026-03-13 | Auto Rl Env | [papers/2026-03-13_auto-rl-env.md](papers/2026-03-13_auto-rl-env.md) |


---

## 🧩 Repository Structure

- `PAPER_PREFERENCES.md` — paper selection taste and ranking criteria
- `papers/` — structured reading notes (paper + blog)
- `readinglist/` — topic lists and prioritized queues
- `notes/` — templates and note scaffolds
- `weekly/` — weekly synthesis and trend tracking

## 🔧 Maintenance Policy (README Dashboard)

- Keep this dashboard updated whenever new notes or reading lists are added.
- Ensure each reading list alias points to an existing note file.
- Keep metrics lightweight, readable, and decision-oriented.


## 🧱 Reading Pipeline Standard (Insight-first)

From 2026-03-18 onward, all paper notes and reading list summaries follow this pipeline:

1. **Source extraction priority**
   - Prefer arXiv HTML for structure + figure links.
   - If HTML unavailable, fallback to arXiv source (`e-print`) for LaTeX sections and figure files.

2. **Figure policy**
   - Prefer direct arXiv HTML figure links.
   - If HTML unavailable, localize source figures to `assets/<paper-alias>/`.

3. **Main result table policy**
   - Must include concrete numeric comparison (baseline / proposed / delta).
   - Avoid vague claims without numbers.

4. **Analysis writing policy**
   - Use `现象 + 解释` format for every analysis item.
   - Add `【标注】` only when inserting personal interpretation or disagreement.

5. **Scoring policy (1+2+2)**
   - Base 1 + Quality (0~2) + Observation (0~2)
   - Always explain "why not higher score".

6. **Sync policy**
   - Updating a paper note requires syncing corresponding reading list summary style.
