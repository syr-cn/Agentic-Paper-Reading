# RetroAgent 阅读笔记

## 0) Metadata
- **Title:** RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback
- **Alias:** RetroAgent
- **Authors / Org:** Shanghai AI Lab, National University of Singapore
- **Venue / Status:** arXiv 2603.08561
- **Date:** 2026-03
- **Links:**
  - Abs: https://arxiv.org/abs/2603.08561
  - HTML: https://arxiv.org/html/2603.08561
  - PDF: https://arxiv.org/pdf/2603.08561
  - Code: https://github.com/zhangxy-2019/RetroAgent
- **Tags:** agent-rl, self-reflection, intrinsic-reward, memory-retrieval, continual-adaptation
- **My rating (★☆☆☆☆~★★★★★):** ★★★★★ (5/5)
- **Read depth:** deep

## 1) TL;DR
- 论文指出当前 agent RL 的双缺陷：过度 exploitation（探索不足）+ 经验只存在参数里（不可显式复用）。
- RetroAgent 用“**回顾式自反思**”产生双内在反馈：
  - 数值反馈（capability-evolution）鼓励有效探索；
  - 语言反馈（lesson memory）支持经验复用。
- 并提出 SimUtil-UCB 检索（语义相关性 + utility + UCB 探索）来取 memory lesson。
- 在 ALFWorld / WebShop / Sokoban / MineSweeper 上显著超过 GRPO 及多类 memory/meta-RL 基线。
- RL-trained reflection 版本进一步提升，显示“反思能力也可训练并与策略共进化”。

## 2) Problem & Motivation
- 现有 RL agent 更多在“找到一个可行解就停”，而不是“持续改进策略”。
- 两个核心瓶颈：
  1) sparse extrinsic reward 下探索不足，易陷局部最优；
  2) 经验不显式存储，无法检索式复用。
- RetroAgent 想把学习目标从 solving 变成 evolving。

## 3) Method (结构化)
### 3.1 Self-Reflection → Dual Intrinsic Feedback
- 每个 episode 后做 hindsight reflection，产出三元组：
  - 子任务完成潜力分 `φ`（用于内在数值奖励）；
  - 成功/失败判断 `c`；
  - 语言 lesson `m`（用于记忆）。

### 3.2 Intrinsic Numerical Feedback
- 用 capability-evolution reward：比较当前潜力分与历史基线，超过才给正奖励（rectified gain），以抑制随机偶然成功、鼓励持续改进。

### 3.3 Intrinsic Language Feedback + Memory
- 记忆条目含 task、lesson、trajectory、utility、retrieval count、success flag。
- 检索用 **SimUtil-UCB**：
  - 相关性：cosine(task embedding)；
  - utility：EMA 更新；
  - 探索：UCB bonus（兼顾少访问条目）。
- 最终得分是 relevance 与 UCB-utility 的加权融合。

### 3.4 两个版本
- **In-Context Reflection**：对比成功/失败轨迹做 pairwise induction。
- **RL-Trained Reflection**：引入 reflection reward，用 REINFORCE 训练 reflection policy，与 decision policy 共同优化。

## 4) Experiments & Evidence
### 4.1 Setup
- 模型：Qwen-2.5-7B-Instruct, Llama-3.1-8B-Instruct。
- 环境：ALFWorld、WebShop、Sokoban、MineSweeper。
- 优化：决策策略基于 GRPO；反思策略（RL variant）用 REINFORCE。

### 4.2 Main Results（Qwen2.5-7B，论文表 1）
- **GRPO baseline**：
  - ALFWorld 77.3
  - WebShop 66.9
  - Sokoban 11.2
  - MineSweeper 39.3
- **RetroAgent (In-Context)**：
  - ALFWorld 91.7
  - WebShop 78.9
  - Sokoban 32.6
  - MineSweeper 47.9
- **RetroAgent (RL-Trained)**：
  - ALFWorld **95.6**
  - WebShop **82.3**
  - Sokoban **38.3**
  - MineSweeper **48.2**

论文总结增益（对 GRPO）约：+14.4 / +12.0 / +21.4 / +8.6（按任务顺序）。

### 4.3 Test-Time Adaptation
- Discovery@k 结果显示随尝试次数增长，RetroAgent 快速逼近高成功率。
- 文中示例：WebShop 82.3% → 99.0%（k=1→3），ALFWorld OOD 92.9% → 100.0%。
- 去掉 test-time memory retrieval 影响有限，说明双反馈已较好内化进策略参数。

### 4.4 Key Ablations
- **Pairwise induction > Single induction**：
  - completion score 更接近 oracle；
  - lesson 幻觉率更低、utility 更高；
  - 下游成功率更高（文中表 4）。
- **Half-group memory augmentation > Full-group**：
  - 全量记忆增强会降低轨迹多样性，易过早收敛。
- **Capability-evolution reward** 比单纯 progress-style shaping 更稳且收益更高（文中表 5）。

### 4.5 Limitations
- 主要在文本交互/游戏任务，真实复杂多工具生产环境外推仍待验证。
- 反思质量对系统上限影响很大，可能受模型能力与提示模板约束。
- memory 机制需要额外检索与维护开销。

## 5) My Technical Take
### 5.1 What I believe
- 这篇把“探索激励”和“经验复用”统一到一个框架里，逻辑闭环非常完整。
- SimUtil-UCB 很实用：比纯相似度检索更接近真正在线学习需求。

### 5.2 What I doubt
- 不同环境下 utility 估计是否会漂移，长期训练稳定性要继续看。
- 反思器与策略共训是否对超参数更敏感（奖励权重、检索频率）。

### 5.3 Transfer to our projects
- 在 skill-RL 管线中加入 **dual intrinsic feedback**（数值+语言）。
- 记忆检索从“相似度 top-k”升级为“相似度×效用×探索”的 bandit 风格。
- 训练时保留一部分“无记忆增强”轨迹以维持探索多样性。

## 6) Repro Checklist
- [x] 任务与算法定义清晰
- [x] 主结果有多环境支撑
- [x] 与 memory/RL/meta-RL 多线基线对比
- [x] 开源代码可得
- [ ] 真实生产任务验证不足

## Appendix
- Figure 1: https://arxiv.org/html/2603.08561/x1.png
- 关键句（我的改写）：RetroAgent 的关键不是“多加一个 memory 模块”，而是让 memory 与探索奖励共同驱动策略持续演化。
