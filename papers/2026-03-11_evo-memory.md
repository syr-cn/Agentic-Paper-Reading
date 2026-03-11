# Evo-Memory 阅读笔记

## 0) Metadata
- **Title:** Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory
- **Alias:** Evo-Memory
- **Authors / Org:** Google DeepMind + UIUC
- **Venue / Status:** arXiv 2511.20857v1
- **Date:** 2025-11
- **Links:**
  - HTML: https://arxiv.org/html/2511.20857v1
  - PDF: https://arxiv.org/pdf/2511.20857
- **Tags:** agent-memory, test-time-learning, continual-adaptation, benchmark, ReAct
- **My rating (0-5):** 4.5
- **Read depth:** normal

## 1) TL;DR (3-6 bullets)
- 论文核心判断很准：现有 memory 方法多数在做“对话回忆”，而不是“经验复用”；真正缺的是部署阶段持续学习（test-time evolution）。
- 提出 **Evo-Memory**：把静态 benchmark 重构成流式任务序列，统一评估 Search → Synthesis → Evolve 循环中的记忆演化能力。
- 给出两类代表性方法：**ExpRAG**（简单经验检索基线）和 **ReMem**（Think-Act-Refine 三元循环）。
- 结果上，多轮任务收益非常显著：例如 Claude 3.7 Sonnet 在 AlfWorld 成功率 **0.50 → 0.92**，平均步数 **22.6 → 11.5**。
- 记忆增益与任务相似度强相关（文中报告 Pearson r=0.717 / 0.563），说明“可迁移经验密度”是 memory 方法上限的关键因子。

## 2) Problem & Motivation
- 以前方法的核心缺口：主流 memory 评测关注“是否记住历史事实”，很少评估“是否把历史任务中的策略抽象出来并复用到未来任务”。
- 这篇 paper 想解决什么：给出统一、可比较的测试平台，专门测 agent 在连续任务流中的 **经验检索 + 策略整合 + 记忆更新**能力。
- 为什么现在值得做：LLM agent 已进入长时部署场景（tool-use、interactive environment、长期助手），如果 memory 不能演化，模型会反复解同类问题，推理成本和错误率都高。

## 3) Method (结构化)
### 3.1 Setting / Formulation
- 将 memory-augmented agent 统一抽象为 (F, U, R, C)：
  - F: base LLM
  - R: retrieval（Search）
  - C: context construction（Synthesis）
  - U: memory update（Evolve）
- 每个时间步执行：`(x_t, M_t) -> R_t -> y_hat_t -> M_{t+1}`。

### 3.2 Main Components
- **Evo-Memory Benchmark**：覆盖单轮（MMLU-Pro / GPQA / AIME / ToolBench）+ 多轮环境（AlfWorld / BabyAI / PDDL / ScienceWorld / Jericho）。
- **ExpRAG**：把历史 `(input, output, feedback)` 编成经验条目，top-k 检索后做 in-context reuse。
- **ReMem**：在 ReAct 的 Think/Act 基础上引入 **Refine Memory**，允许主动剪枝噪声、重组经验、提升后续可检索性。

### 3.3 What is actually new?
- 增量 1：不是单一新算法，而是把“test-time memory evolution”系统化为 benchmark + protocol（价值在评测范式）。
- 增量 2：ReMem 明确把 memory 操作变成 agent action space 的一部分（Think/Act/Refine），而非被动外挂检索。
- 增量 3：强调 sequence-level 评价（任务顺序、失败经验混入、步数效率、鲁棒性），比单点准确率更接近真实部署。

## 4) Experiments & Evidence
### 4.1 Benchmarks / Tasks
- 单轮：AIME24/25, GPQA, MMLU-Pro(若干子域), ToolBench。
- 多轮：AlfWorld, BabyAI, PDDL, ScienceWorld（文中还提及 Jericho）。

### 4.2 Main Results (with concrete numbers)
- **多轮提升最明显**：Claude 3.7 Sonnet 上 ReMem 在 AlfWorld 从 baseline **0.18 提到 0.92**（成功率列）；平均 progress 也显著提高。
- **步数效率**：AlfWorld 平均步数从 **22.6 降到 11.5**（文中重点结论之一）。
- **单轮任务**：提升较温和但一致；ExpRAG 已可超过多种复杂 memory 方法，说明“任务级经验复用”本身很强。

### 4.3 Ablation / Analysis
- **任务相似度相关性**：ReMem 增益与数据集内任务相似度相关（Pearson r=0.717 on Gemini Flash；r=0.563 on Claude Sonnet）。
- **任务顺序效应**：Easy→Hard 与 Hard→Easy 的结果差异明显，说明 benchmark 必须标准化 task ordering。
- **失败经验混入**：传统方法容易退化；ReMem 由于有主动 refine，鲁棒性更好。

### 4.4 Failure / Limitation
- API 预算限制导致模型覆盖不完整。
- 以文本 / 目标导向任务为主，对多模态与真实物理环境外推有限。
- 部分方法在 embodied setting 不完全兼容（作者也在实验里做了方法筛选）。

## 5) My Technical Take
### 5.1 What I believe
- 这篇 paper 最有价值的是“把 memory 的评估目标从 recall 改成 reusable experience”。方向判断非常对。
- ExpRAG 的结果很有说服力：很多时候复杂 memory 框架不如一个做对了数据组织与检索目标的简单基线。

### 5.2 What I doubt
- 当前评测仍偏文本环境，真实 agent 系统中的工具失败模式、长期偏好漂移、跨模态噪声还没真正打到。
- ReMem 的 Refine 触发策略与预算敏感性值得更细分析（什么时候 refine、refine 多深、代价多少）。

### 5.3 Transfer to our projects
- 可直接迁移：
  - 在现有 agent memory 中加入“失败经验标注 + 反事实摘要 + 可检索策略条目”。
  - 把 memory entry 从对话片段升级为 `task signature + solution sketch + failure mode + feedback`。
- 需要改造后迁移：
  - 在多模态 agent 中实现 Think-Act-Refine 的统一 action space。
  - 在长上下文 setting 里加入“相似任务簇”驱动的 memory budget 分配。
- 暂不建议投入：
  - 仅做更复杂索引结构而不改变经验表示目标，收益可能有限。

## 6) Repro Checklist
- [x] 任务定义清晰
- [x] 评测协议可复现（统一 search-synthesis-evolve）
- [x] baseline 覆盖较全面
- [ ] 资源开销可接受（API 成本仍偏高）
- [ ] 代码/数据完全可得（论文称将发布，需二次确认）

## 7) Next Actions (for me)
- [ ] 复刻一个 mini Evo-Memory 子集（AlfWorld + ScienceWorld）做快速 sanity check。
- [ ] 在现有 memory agent 中实现轻量 Refine（失败样本降权 + 冗余去重 + 策略抽象）。
- [ ] 设计“任务相似度分层采样”实验，验证增益是否仍与相似度强相关。

## Appendix
- Figure 1 (HTML): https://arxiv.org/html/2511.20857v1/x1.png
- 关键句（我的改写）：当前 LLM memory 大多“记住说过什么”，但缺“记住学到什么”；后者才是长期 agent 的核心能力。
