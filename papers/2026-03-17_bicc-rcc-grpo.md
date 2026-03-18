# BiCC-RCC-GRPO 阅读笔记

## 0) Metadata
- **Title:** When Right Meets Wrong: Bilateral Context Conditioning with Reward-Confidence Correction for GRPO
- **Alias:** BiCC-RCC
- **Authors / Org:** Yu Li, Tian Lan, Zhengling Qi（已检查 arXiv HTML/PDF，未显式给出机构）
- **Venue / Status:** arXiv 2603.13134v1
- **Date:** 2026-03
- **Links:**
  - Abs: https://arxiv.org/abs/2603.13134
  - PDF: https://arxiv.org/pdf/2603.13134
  - HTML: https://arxiv.org/html/2603.13134
  - Code: https://github.com/Skylanding/BiCC
- **Tags:** GRPO, RLHF, reasoning-model, contrastive-optimization, variance-reduction
- **My rating:** ★★★☆☆
- **Read depth:** normal
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = 3

## 1) Core Insight
- 这篇最有价值的点不是“又改了个 GRPO loss”，而是把 GRPO 重新解释为**组内对/错样本的对比优化问题**：如果训练目标没有显式利用 right-vs-wrong 结构，就在浪费监督信号。

## 2) Interesting Observations
- **Observation 1（机制层）**：GRPO 用 group-relative advantage，但优化时仍偏“样本独立”视角，组内结构信息没有被充分利用。
- **Observation 2（工程层）**：BICC + RCC 都是低侵入插件，不需要额外采样或额外奖励模型，适合已有 GRPO pipeline 直接插入。
- **Observation 3（稳定性层）**：RCC强调“reward-confidence 协方差修正 baseline”，核心目标是降方差而不是只追涨分。

## 3) Method (结构化)
### 3.1 Setting / Formulation
- 将同组样本按 reward 分成较优/较差，目标变成拉开 policy ratio 的间隔（margin view）。

### 3.2 Main Components
- **BICC**：正确/错误轨迹双向条件化，让更新方向显式利用对比信息。
- **RCC**：按 reward-confidence 统计量校正 baseline，减少高噪声梯度影响。

### 3.3 What is actually new?
- 新意：把 GRPO 的“组结构”从隐含信息变成显式训练信号。
- 可能偏工程：confidence 估计具体形式与超参较依赖实现细节。

## 4) Experiments & Evidence
### 4.1 Benchmarks / Tasks
- 数学推理类 benchmark（论文摘要层面未完整列出）。

### 4.2 Main Results
- 摘要给出“consistent improvements”；具体数值需以正文表格为准。

### 4.3 Limitations
- 是否能稳定迁移到非数学任务、噪声 reward 更高的场景，证据还不够。

## 5) Why It Matters for Your Work
- 你在 reasoning post-training 里会频繁碰到“reward noisy + 训练不稳”问题；这篇给的是一组**低成本稳态改造**思路，适合直接做 ablation。

## 6) Actionable Next Step
- 在你现有 GRPO 分支做三组对照：Baseline / +BICC / +BICC+RCC。
- 重点记录：梯度方差、收敛速度、长链推理错误类型，而不仅是最终 pass@1。

## 7) Why not higher score
- 不是更高分的原因：目前可验证的“有趣 observation”偏机制解释层，跨任务硬证据还不够密。
