# Agentic Paper Reading

> A research notebook for **agent memory / continual learning / retrieval reasoning** with dashboard-style navigation.

<p align="left">
  <img alt="Notes" src="https://img.shields.io/badge/Total%20Notes-18-4c1?style=flat-square" />
  <img alt="Reading Lists" src="https://img.shields.io/badge/Reading%20Lists-5-06b6d4?style=flat-square" />
  <img alt="This Month" src="https://img.shields.io/badge/2026--03-18%20notes-7c3aed?style=flat-square" />
  <img alt="Updated" src="https://img.shields.io/badge/Last%20Updated-2026-03-13-111827?style=flat-square" />
</p>

## 📊 Project Snapshot

| Metric | Value |
|---|---:|
| Total notes | **18** |
| Total reading lists | **5** |
| Notes added in 2026-03 | **18** |
| Last updated | **2026-03-13** |

---

## 🧭 Reading Lists

| List | Focus | #Notes | Last Update | Status |
|---|---|---:|---|---|
| [Agent Topic Reading List](readinglist/agent-topic.md) | Deep read on selected Agent papers | 6 | 2026-03-13 | OK |
| [Agentic Skills Reading List](readinglist/agentic-skills.md) | Skills as Agent capability (survey, methods, benchmark) | 7 | 2026-03-11 | OK |
| [Blog Topic Reading List](readinglist/blog-topic.md) | High-signal blog analyses mapped to agent research | 4 | 2026-03-12 | OK |
| [Later Queue](readinglist/later.md) | Backlog queue | 0 | 2026-03-11 | OK |
| [Now Reading Queue](readinglist/now.md) | Current reading queue | 0 | 2026-03-11 | OK |

---

## 🗓️ Notes by Time (Year / Month)

### By Year

| Year | #Notes |
|---|---:|
| 2026 | 18 |

### By Month

| Month | #Notes |
|---|---:|
| 2026-03 | 18 |

---

## 🆕 Recent Additions (Latest 10)

| Date | Alias | Note |
|---|---|---|
| 2026-03-13 | Auto Rl Env | [papers/2026-03-13_auto-rl-env.md](papers/2026-03-13_auto-rl-env.md) |
| 2026-03-13 | Reasoning Judge | [papers/2026-03-13_reasoning-judge.md](papers/2026-03-13_reasoning-judge.md) |
| 2026-03-13 | Madqa | [papers/2026-03-13_madqa.md](papers/2026-03-13_madqa.md) |
| 2026-03-13 | Dive | [papers/2026-03-13_dive.md](papers/2026-03-13_dive.md) |
| 2026-03-12 | Retroagent | [papers/2026-03-12_retroagent.md](papers/2026-03-12_retroagent.md) |
| 2026-03-12 | Icrl Tool Use | [papers/2026-03-12_icrl-tool-use.md](papers/2026-03-12_icrl-tool-use.md) |
| 2026-03-12 | 01Me User Memory Cognition | [papers/2026-03-12_01me-user-memory-cognition.md](papers/2026-03-12_01me-user-memory-cognition.md) |
| 2026-03-12 | 01Me Sovereign Agents | [papers/2026-03-12_01me-sovereign-agents.md](papers/2026-03-12_01me-sovereign-agents.md) |
| 2026-03-12 | 01Me Digital Worker | [papers/2026-03-12_01me-digital-worker.md](papers/2026-03-12_01me-digital-worker.md) |
| 2026-03-12 | 01Me Agent Continual Learning | [papers/2026-03-12_01me-agent-continual-learning.md](papers/2026-03-12_01me-agent-continual-learning.md) |


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
