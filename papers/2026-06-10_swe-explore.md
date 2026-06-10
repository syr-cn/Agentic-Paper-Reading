# SWE-Explore 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** SWE-Explore: Benchmarking How Coding Agents Explore Repositories
- **Alias:** SWE-Explore
- **Authors / Org:** Shaoqiu Zhang (1st author, PhD @ SJTU, GitHub: Qiushao-E), Yuhang Wang, Jialiang Liang, Yuling Shi, Wenhao Zeng, Maoquan Wang, Shilin He, Ningyuan Xu, Siyu Ye, Kai Cai, Xiaodong Gu (corresponding, faculty @ HKUST(GZ)). Group: SJTU Software Engineering + HKUST(GZ) collaboration, focus on AI for SE.
- **Venue / Status:** arXiv 2606.07297 (cs.SE, cs.CL)
- **Date:** 2026-06-05
- **Links:**
  - Abs: https://arxiv.org/abs/2606.07297
  - HTML: https://arxiv.org/html/2606.07297v1
  - PDF: https://arxiv.org/pdf/2606.07297
  - Code: https://github.com/Qiushao-E/SWE-Explore-Bench
  - Dataset: https://huggingface.co/datasets/SWE-Explore-Bench/SWE-Explore-Bench
- **Tags:** benchmark, coding-agent, repository-exploration, SWE-bench, code-localization, line-level-evaluation
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = **4/5**
- **Community:** alphaXiv 11 likes, HF ⬆️98 (#2 Paper of the day)
- **Type:** C (Benchmark)
- **Relevance:** 3/5
- **Quality:** 4/5

---

## 1) 一句话 Why-read

SWE-bench 只看 pass/fail，本文首次将 coding agent 的"代码仓库探索"能力单独拆出来做 line-level 评估，发现即使最强 agent file-level 定位很好但 line-level recall <20%——这是自动修 bug 的真正瓶颈。

---

## 2) CRGP 拆解 Introduction

### C — Context
- SWE-bench 等端到端 benchmark 只给 binary resolved/unresolved，无法区分 agent 失败是因为找不到代码(exploration)还是不会修(generation)。

### R — Related work
- SWE-bench Verified、SWE-bench-Pro 等后续工作改善了 ground truth 质量但仍是 binary 评估。
- Code localization（BM25、dense retriever、AutoCodeRover、CoSIL）作为独立任务存在但缺乏统一 benchmark。

### G — Research gap
- 缺少独立评估 repository exploration 的 benchmark。
- 传统 retrieval (BM25/dense) 不够，agentic explorer 只在长 trajectory 末端被评估。
- 无 line-level 粒度的 ground truth。

### P — Proposal
- SWE-Explore：隔离评估 exploration phase，给定 issue q + repo R，要求返回 ranked code regions P=(r₁,...,rₖ)。
- Trajectory-grounded 方法构建 ground truth：从多个成功 repair trajectory 中提取共识 core context。
- 三维度评测：line-level recall / nDCG@B / context efficiency。

---

## 3) Figure 区

- 图1（SWE-Explore vs Existing Benchmarks）：
  ![fig1](https://arxiv.org/html/2606.07297v1/extracted/6523456/figures/figure1.png)
  解释：传统端到端评估 vs SWE-Explore 框架，后者将 exploration 阶段单独隔离评估，展示了从 issue → exploration → ranked code regions 的完整流程。

- 图2（Construction pipeline）：
  trajectory extraction → consensus aggregation → LLM refinement (core/optional) → human audit。848 instances 分布于 10 种编程语言，203 repos。

---

## 4) Experiments

### 4.1 Experimental setup
- **数据集:** 848 issues, 10 languages, 203 open-source repos (来自 SWE-bench Verified + SWE-bench-Pro)
- **Ground truth 构建:** 多个独立成功 agent trajectory → 取读代码交集 → LLM 分类 R_core/R_opt → 人工审计
- **评估体系:** (1) Line-level Recall = |P∩R_core| / |R_core|; (2) nDCG@B (ranked quality under budget); (3) Context Efficiency (relevant/total retrieved)
- **Baselines:** BM25, dense retrievers, agentic explorers (Claude Code, OpenHands, Mini-SWE-Agent, Cursor), specialized localizers (CoSIL, AutoCodeRover, LocAgent)

### 4.2 Main result table
| Explorer Category | HitFile | Line Recall | nDCG@B | Context Eff. |
|---|---|---|---|---|
| BM25 / Dense Retriever | Low | Very Low | Low | Low |
| General Coding Agents (Claude Code, OpenHands) | High | <20% | Medium | Medium |
| Specialized Localizers (CoSIL) | High | Higher | Higher | Higher |

**Key finding:** Agentic explorers >> classical retrieval. 但即使最好的 agent, line-level recall 仍 <20%。

### 4.3 Analysis experiments
- **现象：** Context Efficiency 与 resolve rate 相关性 r=0.950
  **解释（作者）：** 探索精度直接决定下游修复成功率，证明指标有效。

- **现象：** 缺失 >25-50% core evidence 时 success rate 骤降
  **解释（作者）：** 存在 threshold effect——不是线性退化而是断崖式下降。
  **【标注】：** 这对 RAG/context curation 有重要启示——宁多不少。

- **现象：** 加入无关代码对修复成功率影响远小于漏掉关键行
  **解释（作者）：** Noise robustness > recall sensitivity，agent 能过滤噪声但不能无中生有。

---

## 5) Why it matters for our work

**Author/Group Analysis:**
- Xiaodong Gu 是 HKUST(GZ) 的 faculty，研究方向是 AI for Software Engineering
- 团队主体在 SJTU，做 coding agent + SE evaluation
- 这是该组在 agent evaluation 方向的一篇定义性工作，likely 会成为 coding agent 领域的标准评测

**对我们工作的意义：**
1. **Agent 评估拆解思路:** 将复杂任务分解为独立可评估的子能力（exploration vs generation），可借鉴到 agentic memory evaluation
2. **Exploration 是瓶颈:** Line-level recall <20% → navigation strategy (code graph search, AST-aware retrieval) 是高杠杆
3. **Context efficiency 强相关下游:** 给 agent 精准 context 比给更多 context 重要——支持我们做 context curation
4. **Trajectory-grounded GT 方法:** 从成功轨迹中自动提取 ground truth 的方法论可迁移到 memory evaluation

---

## 6) Actionable next step
- [ ] 将"拆解子能力评估"思路迁移到 agentic memory benchmark 设计
- [ ] 研究 CoSIL 的 code-graph-aware exploration，看能否迁移到通用 agent retrieval
- [ ] Context Efficiency 作为 agent dev loop 的早期 proxy metric

---

## 7) 评分解释
- **质量分 2/2：** Ground truth 构建方法 (trajectory-grounded + human audit) 扎实；validation 实验证明指标与下游强相关 (r>0.9)；覆盖面广 (10 languages, 203 repos, 多类 explorer)。
- **Observation 分 1/2：** "Line recall <20% 是瓶颈"有指导意义但不算特别意外；threshold effect 和 noise robustness 有一定新意但不够深。
- **总分 4/5**
- **为什么不是更高分：** (1) Insight 层面未超越"exploration 很重要"的直觉；(2) 与我们的 memory/long-context 核心方向距离稍远（Relevance 3）；(3) 未提出改进 exploration 的新方法，纯 benchmark。
