# BiCC-RCC-GRPO 阅读笔记

## 0 Metadata
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

## 1 一句话 Why-read
- 这篇最有价值的点不是“又改了个 GRPO loss”，而是把 GRPO 重新解释为**组内对/错样本的对比优化问题**：如果训练目标没有显式利用 right-vs-wrong 结构，就在浪费监督信号。

## 2 CRGP
### C — Context
- 这篇最有价值的点不是“又改了个 GRPO loss”，而是把 GRPO 重新解释为**组内对/错样本的对比优化问题**：如果训练目标没有显式利用 right-vs-wrong 结构，就在浪费监督信号。

### R — Related work
- - **Observation 1（机制层）**：GRPO 用 group-relative advantage，但优化时仍偏“样本独立”视角，组内结构信息没有被充分利用。

### G — Research gap
- 待补证据（需从原文引言补充明确 gap 描述）

### P — Proposal
- ### 4.1 Benchmarks / Tasks

## 3 Figure 区
- 待补证据（建议补 1 张方法图或主结果图）
- 可定位链接：  - Abs: https://arxiv.org/abs/2603.13134
  - PDF: https://arxiv.org/pdf/2603.13134
  - HTML: https://arxiv.org/html/2603.13134
  - Code: https://github.com/Skylanding/BiCC

## 4 Experiments
### 4.1 Experimental setup
### 4.1 Benchmarks / Tasks
- 数学推理类 benchmark（论文摘要层面未完整列出）。

### 4.2 Main Results
- 摘要给出“consistent improvements”；具体数值需以正文表格为准。

### 4.3 Limitations
- 是否能稳定迁移到非数学任务、噪声 reward 更高的场景，证据还不够。

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 原文摘要 | 原文未给出可提取数字 | 原文未给出可提取数字 | 原文未给出可提取数字 |

### 4.3 Analysis
- **现象：** **Observation 1（机制层）**：GRPO 用 group-relative advantage，但优化时仍偏“样本独立”视角，组内结构信息没有被充分利用。
  **解释（作者）：** 待补证据。
  **【标注】（我的判断，可选）：** 待补证据。

## 5 Why it matters for our work
- 你在 reasoning post-training 里会频繁碰到“reward noisy + 训练不稳”问题；这篇给的是一组**低成本稳态改造**思路，适合直接做 ablation。

## 6 Actionable next step
- 在你现有 GRPO 分支做三组对照：Baseline / +BICC / +BICC+RCC。
- 重点记录：梯度方差、收敛速度、长链推理错误类型，而不仅是最终 pass@1。

## 7 评分解释
- 维持原评分倾向，不做无根据上调。
- 不是更高分的原因：目前可验证的“有趣 observation”偏机制解释层，跨任务硬证据还不够密。
