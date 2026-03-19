# Evo-Memory 阅读笔记

## 0 Metadata
- **Title:** Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory
- **Alias:** Evo-Memory
- **Authors / Org:** Google DeepMind + UIUC
- **Venue / Status:** arXiv 2511.20857v1
- **Links:** Abs https://arxiv.org/abs/2511.20857 | PDF https://arxiv.org/pdf/2511.20857
- **My rating:** ★★★★★
- **Read depth:** normal
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 2 = 5

## 1 一句话 Why-read
- 这篇把 memory 评估目标从“记住说过什么”升级为“是否学会可复用经验”，是该方向非常关键的范式校正。

## 2 CRGP
### C — Context
- 这篇把 memory 评估目标从“记住说过什么”升级为“是否学会可复用经验”，是该方向非常关键的范式校正。

### R — Related work
- - test-time 演化带来多轮任务显著收益，且步数效率同步改善。

### G — Research gap
- 待补证据（需从原文引言补充明确 gap 描述）

### P — Proposal
- - Evo-Memory benchmark 统一 Search→Synthesis→Evolve 循环评测。

## 3 Figure 区
- 待补证据（建议补 1 张方法图或主结果图）
- 可定位链接：- **Links:** Abs https://arxiv.org/abs/2511.20857 | PDF https://arxiv.org/pdf/2511.20857

## 4 Experiments
### 4.1 Experimental setup
- Evo-Memory benchmark 统一 Search→Synthesis→Evolve 循环评测。
- 覆盖单轮与多轮任务，报告 ReMem/ExpRAG 等方法系统对比。

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 原文摘要 | 原文未给出可提取数字 | 原文未给出可提取数字 | 原文未给出可提取数字 |

### 4.3 Analysis
- **现象：** test-time 演化带来多轮任务显著收益，且步数效率同步改善。
  **解释（作者）：** 待补证据。
  **【标注】（我的判断，可选）：** 待补证据。

## 5 Why it matters for our work
- 与你的研究核心高度一致：长期 agent 的关键不是 recall，而是持续策略演化与经验内化。

## 6 Actionable next step
- 复刻一个 mini Evo-Memory 子集，并加入你现有 memory 模块做对照。

## 7 评分解释
- 维持原评分倾向，不做无根据上调。
- 保持 5 星：它同时有范式 insight 与可操作评测协议，且与你主线强耦合。
