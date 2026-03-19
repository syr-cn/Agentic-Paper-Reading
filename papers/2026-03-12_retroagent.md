# RetroAgent 阅读笔记

## 0 Metadata
- **Title:** RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- **Alias:** RetroAgent
- **Authors / Org:** Shanghai AI Lab, NUS
- **Venue / Status:** arXiv 2603.08561
- **Links:** Abs https://arxiv.org/abs/2603.08561 | PDF https://arxiv.org/pdf/2603.08561 | Code https://github.com/zhangxy-2019/RetroAgent
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = 4

## 1 一句话 Why-read
- 把“探索激励”和“经验复用”合并为双内在反馈（数值+语言）是关键；它不只提升一次求解，而是推动策略持续演化。

## 2 CRGP
### C — Context
- 把“探索激励”和“经验复用”合并为双内在反馈（数值+语言）是关键；它不只提升一次求解，而是推动策略持续演化。

### R — Related work
- - test-time memory retrieval 关闭后性能下降有限，说明经验已部分内化进策略参数。

### G — Research gap
- 待补证据（需从原文引言补充明确 gap 描述）

### P — Proposal
- - hindsight reflection 产出 `潜力分 + 成败标记 + lesson`。

## 3 Figure 区
- 待补证据（建议补 1 张方法图或主结果图）
- 可定位链接：- **Links:** Abs https://arxiv.org/abs/2603.08561 | PDF https://arxiv.org/pdf/2603.08561 | Code https://github.com/zhangxy-2019/RetroAgent

## 4 Experiments
### 4.1 Experimental setup
- hindsight reflection 产出 `潜力分 + 成败标记 + lesson`。
- SimUtil-UCB 检索融合相似度、utility、探索项。
- 在 ALFWorld/WebShop/Sokoban/MineSweeper 对 GRPO 有稳定提升。

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 原文摘要 | 原文未给出可提取数字 | 原文未给出可提取数字 | 原文未给出可提取数字 |

### 4.3 Analysis
- **现象：** test-time memory retrieval 关闭后性能下降有限，说明经验已部分内化进策略参数。
  **解释（作者）：** 待补证据。
  **【标注】（我的判断，可选）：** 待补证据。

## 5 Why it matters for our work
- 与你的 memory-agent 主线高度一致：可直接借鉴双通道反馈与 bandit 风格记忆检索。

## 6 Actionable next step
- 在你现有 skill-RL 管线加入 `相似度×效用×探索` 检索打分，并测试 half-group 增强策略。

## 7 评分解释
- 维持原评分倾向，不做无根据上调。
- 不是更高分的原因：真实多工具生产环境外推证据仍有限。
