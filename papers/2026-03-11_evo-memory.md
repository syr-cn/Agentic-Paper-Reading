# Evo-Memory 阅读笔记

## 0) Metadata
- **Title:** Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory
- **Alias:** Evo-Memory
- **Authors / Org:** Google DeepMind + UIUC
- **Venue / Status:** arXiv 2511.20857v1
- **Links:** Abs https://arxiv.org/abs/2511.20857 | PDF https://arxiv.org/pdf/2511.20857
- **My rating:** ★★★★★
- **Read depth:** normal
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 2 = 5

## 1) Core Insight
- 这篇把 memory 评估目标从“记住说过什么”升级为“是否学会可复用经验”，是该方向非常关键的范式校正。

## 2) Interesting Observations
- test-time 演化带来多轮任务显著收益，且步数效率同步改善。
- memory 增益与任务相似度强相关，说明“可迁移经验密度”决定上限。
- 简洁经验检索基线（ExpRAG）在不少场景已很强，复杂框架不一定占优。

## 3) Evidence / Method
- Evo-Memory benchmark 统一 Search→Synthesis→Evolve 循环评测。
- 覆盖单轮与多轮任务，报告 ReMem/ExpRAG 等方法系统对比。

## 4) Why It Matters for Your Work
- 与你的研究核心高度一致：长期 agent 的关键不是 recall，而是持续策略演化与经验内化。

## 5) Actionable Next Step
- 复刻一个 mini Evo-Memory 子集，并加入你现有 memory 模块做对照。

## 6) Why not higher score
- 保持 5 星：它同时有范式 insight 与可操作评测协议，且与你主线强耦合。
