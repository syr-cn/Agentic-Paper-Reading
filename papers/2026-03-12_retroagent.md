# RetroAgent 阅读笔记

## 0) Metadata
- **Title:** RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- **Alias:** RetroAgent
- **Authors / Org:** Shanghai AI Lab, NUS
- **Venue / Status:** arXiv 2603.08561
- **Links:** Abs https://arxiv.org/abs/2603.08561 | PDF https://arxiv.org/pdf/2603.08561 | Code https://github.com/zhangxy-2019/RetroAgent
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = 4

## 1) Core Insight
- 把“探索激励”和“经验复用”合并为双内在反馈（数值+语言）是关键；它不只提升一次求解，而是推动策略持续演化。

## 2) Interesting Observations
- test-time memory retrieval 关闭后性能下降有限，说明经验已部分内化进策略参数。
- half-group memory augmentation 优于 full-group，提示“过量记忆增强”会压缩探索多样性。
- pairwise reflection 明显优于单轨迹反思，说明“对照反思”比“自言自语”更有用。

## 3) Evidence / Method
- hindsight reflection 产出 `潜力分 + 成败标记 + lesson`。
- SimUtil-UCB 检索融合相似度、utility、探索项。
- 在 ALFWorld/WebShop/Sokoban/MineSweeper 对 GRPO 有稳定提升。

## 4) Why It Matters for Your Work
- 与你的 memory-agent 主线高度一致：可直接借鉴双通道反馈与 bandit 风格记忆检索。

## 5) Actionable Next Step
- 在你现有 skill-RL 管线加入 `相似度×效用×探索` 检索打分，并测试 half-group 增强策略。

## 6) Why not higher score
- 不是更高分的原因：真实多工具生产环境外推证据仍有限。
