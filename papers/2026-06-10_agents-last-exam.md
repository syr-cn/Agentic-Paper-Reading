# Agents' Last Exam 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** Agents' Last Exam
- **Alias:** Agents-Last-Exam
- **Authors / Org:** Yiyou Sun (1st author, UC Berkeley, Center for Responsible Decentralized Intelligence / RDI); core contributors: Xinyang Han, Weichen Zhang, Yuanbo Pang, Tianyu Wang, Yuhan Cao, Yixiao Huang. PI: Dawn Song (Berkeley RDI director). Group agenda: agentic AI systems, responsible AI, decentralized intelligence, benchmark & evaluation infrastructure.
- **Venue / Status:** arXiv 2606.05405 (preprint, Jun 2026)
- **Date:** 2026-06-03
- **Links:**
  - Abs: https://arxiv.org/abs/2606.05405
  - HTML: https://arxiv.org/html/2606.05405v1
  - PDF: https://arxiv.org/pdf/2606.05405
  - Code: https://github.com/rdi-berkeley/agents-last-exam
- **Tags:** benchmark, agent-evaluation, economic-value, deployment-gap, computer-use-agent, long-horizon, GCUA
- **My rating:** ★★★★★
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 2 = **5/5**
- **Community:** alphaXiv 146 likes, HF ⬆️71
- **Type:** C (Benchmark)
- **Relevance:** 5/5
- **Quality:** 5/5

---

## 1) 一句话 Why-read

AI benchmark 不再只测"能力"——ALE 用 1K+ 真实职业任务（跨 55 子领域、13 产业集群）度量 agent 的 GDP-relevant 经济产出能力，最强配置整体 pass rate 仅 26.2%，Last-Exam 层 <10%，定义了 agentic system 当前能力的真正天花板。

---

## 2) CRGP 拆解 Introduction

### C — Context
- AI 在 MMLU/GPQA/HumanEval 等 benchmark 上表现出色，但经济产出(GDP)转化极为有限——"utility problem"。
- Agent 能力高速增长，但现有评测与实际部署间存在巨大 gap。

### R — Related work
- MMLU, GPQA, HumanEval, SWE-bench 等：测单项能力，缺乏长链条工作流。
- WebArena, OSWorld：测 GUI 操作但覆盖面窄。
- Humanity's Last Exam：测知识极限但非 agent 导向。
- GAIA：接近但规模小、领域窄。

### G — Research gap
- 现有 benchmark 缺乏三者同时满足：(1) 真实长链条工作流, (2) 跨行业广覆盖, (3) 异构产物的可验证评估。
- 没有 benchmark 直接度量 agent 的经济价值交付能力。

### P — Proposal
- ALE (Agents' Last Exam)：1K+ 任务，55 子域×13 产业集群，250+ 行业专家协作。
- 三难度梯度：Near-Term / Full-Spectrum / Last-Exam。
- GCUA (Generalist Computer-Use Agent) 五层功能模型：Brain/Eyes/Body/Hands/Feet。
- Living benchmark：持续扩充防止 contamination。

---

## 3) Figure 区

- 图1（ALE taxonomy & domain coverage）：
  ![fig1](https://arxiv.org/html/2606.05405v1/x1.png)
  解释：ALE 覆盖 13 大产业域 55 子域的完整任务分类体系图，每个子域映射到 O*NET/SOC 2018 职业编码。

- 图3（Benchmark positioning map）：
  ![fig3](https://arxiv.org/html/2606.05405v1/x4.png)
  解释：将 16 个主流 benchmark 按 ALE 55 子域坐标系映射，暴露 13 个子域完全未被覆盖。

- 图9（Experiment analysis）：
  ![fig9](https://arxiv.org/html/2606.05405v1/x15.png)
  解释：(a) 领域得分热力图, (b)(c) 工具调用分布, (d) 失败根因分类。

---

## 4) Experiments

### 4.1 Experimental setup
- **评估对象:** GCUA — 同时具备 Brain/Eyes/Body/Hands/Feet 五层能力
- **统一接口:** GUI-as-Tool 模式，通过 CUA MCP bridge 暴露 14 个桌面操作工具
- **任务规模:** 150 公开任务（三梯度：Near-Term 59, Full-Spectrum 55, Last-Exam 36）
- **运行上限:** 5 小时/任务，单任务成本 $3–10
- **被测系统:** Codex, Claude Code, Cursor, Droid, OpenClaw, ALE-Claw + 多种 backbone (GPT-5.5, Opus 4.7, Gemini 3.1 Pro, DeepSeek V4, etc.)

### 4.2 Main result table
| Configuration | Near-Term Pass | Full-Spectrum Pass | Last-Exam Pass | **Overall Pass** |
|---|---|---|---|---|
| Codex (GPT-5.5) | 42.4% | 20.0% | 8.6% | **26.2%** |
| ALE-Claw (GPT-5.5) | 35.6% | 21.8% | 8.6% | 24.2% |
| Cursor (GPT-5.5) | 36.4% | 20.0% | 2.9% | 22.5% |
| Claude Code (Opus 4.7) | 23.7% | 12.7% | 0.0% | 14.1% |
| Grok CLI (Grok 4.3) | 10.2% | 7.3% | 0.0% | 6.7% |

**Last-Exam 平均 pass rate 仅 2.6%**（所有配置均值）。

### 4.3 Analysis experiments
- **现象：** 模型选择贡献的性能方差是 harness 选择的 ~3×
  **解释（作者）：** Model > Harness 在当前阶段，但两者贡献互补。
  **【标注】：** 这与我们看到的趋势一致——harness 天花板受限于 model 的 planning 能力。

- **现象：** 34% 任务指定 GUI 软件为主工具，但 agent 倾向用 Bash/CLI 替代
  **解释（作者）：** 当前 agent 缺乏真正的 GUI 操作能力，偏好文本界面。

- **现象：** ~75% 失败为 Understanding & Approach 错误（领域知识不足），而非执行层面
  **解释（作者）：** 领域知识而非操作技能是核心瓶颈。
  **【标注】：** 极其重要——暗示 agent 需要 domain-specific knowledge grounding，不只是更好的 tool-use。

- **现象：** Codex+GPT-5.5 在 Terminal-Bench 82% → ALE-CLI 仅 25.2%
  **解释（作者）：** 现有 benchmark 严重高估 agent 真实能力。

---

## 5) Why it matters for our work

**Author/Group Analysis:**
- Yiyou Sun 是 Dawn Song 组的学生，Berkeley RDI 是强组，之前做过 DeFi security、responsible AI
- Dawn Song 是 Berkeley EECS 的 full professor，h-index 极高，研究覆盖 security + AI
- 这是该组从 "responsible AI" 方向切入 agent evaluation 的大作，野心是定义整个 agent benchmark 范式
- 250+ 行业专家协作 + living benchmark 的规模说明这不是一篇投稿小文章，而是想做 "agent 领域的 MMLU"

**对我们工作的意义：**
1. **评估范式转移:** 从"答题正确率"到"能否完成经济价值交付"——这是未来 agent 评测的方向
2. **GCUA 架构参考:** 五层功能模型(Brain/Eyes/Body/Hands/Feet)和 GUI-as-Tool 设计可直接指导 agent 架构
3. **能力瓶颈定位:** 75% 失败来自领域知识不足 → agent 需要 domain-specific memory/knowledge grounding
4. **直接对标数据:** 论文中有 Hermes 系统的评测数据，提供了我们的定位坐标
5. **Living benchmark 策略:** 滚动更新防 contamination，值得 agentic memory benchmark 借鉴

---

## 6) Actionable next step
- [ ] 在 ALE-CLI 上跑我们的 agent，复现论文数字建立 baseline
- [ ] 针对 Understanding & Approach 失败，设计 domain knowledge retrieval 实验
- [ ] 将 ALE 的评估理念迁移到 agentic memory evaluation——从"能记住"到"能用记忆创造价值"
- [ ] 关注 ALE 的后续扩展（living benchmark），作为我们 agent 开发的长期评测平台

---

## 7) 评分解释
- **质量分 2/2：** 设计原则清晰（代表性/复杂度/可验证性），taxonomy 有理论依据(O*NET/SOC)，评测管线工程化程度极高，实验覆盖全面（12+ 模型 × 6+ harness），250+ 专家参与。
- **Observation 分 2/2：** "benchmark 即目标函数"的洞察极有价值——经济价值导向评测会重塑 agent 研发方向；失败分析揭示领域知识而非执行是核心瓶颈；Model > Harness 的定量比较填补了一个重要 gap。
- **总分 5/5**
- **为什么不是更高分：** 已经是满分。如果要挑毛病：(1) 150 公开任务规模仍有限（full 1K+ 未开放）；(2) 单任务 $3-10 的成本限制了社区复现；(3) GCUA 五层模型更多是描述性框架而非 prescriptive 理论。
