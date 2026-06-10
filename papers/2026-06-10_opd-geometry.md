# On the Geometry of On-Policy Distillation 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** On the Geometry of On-Policy Distillation
- **Alias:** OPD-Geometry
- **Authors / Org:** Zhennan Shen (1st author, PhD @ HKUST, advised by Yi R. Fung), Yanshu Li (UT Austin), Qingyu Yin (Zhejiang University), Chak Tou Leong (HK PolyU), Zhilin Wang (USTC), Yanxu Chen (BUPT), Rongduo Han (Nankai), Sunbowen Lee (BIT), Yi R. Fung (HKUST, senior/corresponding). Multi-institution collaboration led by HKUST NLP group.
- **Venue / Status:** arXiv 2606.07082 (preprint, cs.LG / cs.AI)
- **Date:** 2026-06-05
- **Links:**
  - Abs: https://arxiv.org/abs/2606.07082
  - HTML: https://arxiv.org/html/2606.07082v1
  - PDF: https://arxiv.org/pdf/2606.07082
  - Code: Not provided
- **Tags:** on-policy-distillation, geometry, parameter-space, SFT, RLVR, subspace-locking, stable-rank, spectral-analysis, LRM
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1.5 = **4.5/5**
- **Community:** alphaXiv 59 likes, HF ⬆️60
- **Type:** A (Training)
- **Relevance:** 4/5
- **Quality:** 4/5

---

## 1) 一句话 Why-read

首次系统刻画 On-Policy Distillation 在参数空间的几何特征——"relaxed off-principal + subspace locking"——提供了理解 OPD 为何高效迁移推理能力的机制解释，并暗示极低秩训练的可能性。

---

## 2) CRGP 拆解 Introduction

### C — Context
- LRM 的 post-training 由 SFT（dense, principal-aligned updates）和 RLVR（sparse, off-principal updates）主导，OPD 作为第三范式崛起——student 自采样 + teacher 逐 token 纠正。

### R — Related work
- "The Path Not Taken" (arXiv:2511.08567)：RLVR 的 off-principal 几何特征。
- "LIFT the Veil" (arXiv:2506.00772)：SFT 的 principal-aligned 几何。
- Agarwal et al.：OPD 的定义与实证有效性。
- 现有工作只分析了 SFT 和 RLVR 两端的几何特征，OPD 参数动态完全未被刻画。

### G — Research gap
- OPD 经验上有效，但其参数空间动态（"几何"）完全未被表征。
- 不清楚 OPD 是 SFT/RLVR 的简单插值还是有独特的几何 regime。

### P — Proposal
- 提出一套参数空间诊断工具（sparsity, spectral drift, principal angle rotation, stable rank, subspace similarity）。
- 发现 OPD 处于 "relaxed off-principal regime" 并展现 "subspace locking" 现象。
- 通过 functional sufficiency test 和 control experiments 验证。
- 提出 Three-Gate 框架（Budget / Geometry / Precision）统一解释三种范式的差异。

---

## 3) Figure 区

- 图1（OPD 几何定位总览）：
  ![fig1](https://arxiv.org/html/2606.07082v1/x1.png)
  解释：(a) OPD 位于 SFT（dense, principal-aligned）和 RLVR（sparse, off-principal）之间的 "relaxed off-principal" 区域；(b) stable rank 保持平坦（~20-30），而 SFT 持续攀升，RLVR 逐渐收缩；(c) 此锁定行为对 token 稀疏化和 off-policy rollout 鲁棒，但对目标函数组合敏感。

- 图5（Rank-16 子空间约束实验）：
  ![fig5](https://arxiv.org/html/2606.07082v1/figures/k16_projection_percent.png)
  解释：将训练梯度投影到早期识别的 rank-16 子空间：OPD 在 AIME 2024 等推理 benchmark 上几乎保持完整性能，SFT 严重退化。证明 OPD 的 locked subspace 是 functionally sufficient。

---

## 4) Experiments

### 4.1 Experimental setup
- **模型:** 8B 参数 LLM
- **训练范式:** SFT, OPD, RLVR 三者对比
- **诊断指标:** Update sparsity (η=10⁻³), Normalized Spectral Shift (NSS), principal angle rotation, stable rank, subspace similarity
- **评估:** AIME 2024 等推理 benchmark

### 4.2 Main result table
| 指标 | SFT | OPD | RLVR |
|------|-----|-----|------|
| Weights unchanged (sparsity) | 8.1% | 51.6% | 77.2% |
| Principal angle rotation | >10° | ~1° | <0.5° |
| Stable rank trajectory | 上升 (20→75) | 平坦 (20-30) | 下降 |
| Rank-16 constraint 性能保持 | 严重退化 | 几乎完整 | — |

### 4.3 Analysis experiments
- **现象：** Token Sparsification (25%/50% token supervision) 不影响锁定行为
  **解释（作者）：** 稀疏 token 监督仍能通过 precision gate，锁定由目标函数性质决定而非数据量。

- **现象：** Off-Policy Rollouts（用 teacher 轨迹替代 student 采样）锁定行为保持
  **解释（作者）：** 采样策略不是几何 regime 的决定因素。
  **【标注】：** 这意味着 off-policy distillation 和 on-policy 在参数空间看起来差别不大——有趣的矛盾。

- **现象：** Objective Mixing（αL_OPD + (1-α)L_RLVR）只有 α 极小时轨迹才改变
  **解释（作者）：** 目标函数本身（teacher 分布纠正信号）决定几何路径，而非 runtime sampling factors。

**Three-Gate 框架：**
1. Budget Gate: 更新受局部二次预算约束
2. Geometry Gate: 更新受预训练模型曲率引导
3. Precision Gate: 更新需超过数值精度阈值（bf16）

OPD 独特地通过三个门：信号足够通过 precision gate（比 RLVR 更多坐标），但仍受 geometry gate 约束（不像 SFT 那样无视）。

---

## 5) Why it matters for our work

**Author/Group Analysis:**
- Yi R. Fung 是 HKUST 的 NLP 研究者，研究方向涵盖 LLM post-training 和推理能力提升
- 团队跨多个中国高校（HKUST、UT Austin、浙大、PolyU、USTC 等），关注 LRM training dynamics
- 论文建立在 "The Path Not Taken" (RLVR off-principal) 和 "LIFT the Veil" (SFT principal) 的基础上
- 这是该组首篇 OPD 几何分析，likely follow-up 会是利用发现的优化算法

**对我们工作的意义：**
1. **OPD 效率优化:** subspace locking → OPD 的有效学习维度极低（rank-16 即可），可设计极低秩 LoRA/子空间约束训练
2. **Multi-modal RL + distillation 设计:** 理解 OPD vs RLVR 几何差异，有助于设计混合目标时预判参数空间行为
3. **Agentic memory:** 如果 agent 需要持续蒸馏新能力，subspace locking 暗示可以固定"推理通道"避免灾难性遗忘
4. **Long-context reasoning:** OPD 保持预训练几何特性意味着蒸馏不会破坏长上下文能力

---

## 6) Actionable next step
- [ ] 在我们的 distillation pipeline 中加入 stable rank 监控，验证是否也出现 subspace locking
- [ ] 尝试 early-stage subspace identification + rank-constrained OPD（rank-16/32）
- [ ] 读 "The Path Not Taken" 和 "LIFT the Veil" 作为 SFT/RLVR 几何分析的互补阅读

---

## 7) 评分解释
- **质量分 2/2：** 实验设计严谨，诊断指标体系完整，control experiments 充分，Three-Gate 框架有理论洞察力。17页8图，工作量扎实。
- **Observation 分 1.5/2：** "Subspace locking" 是有价值的新发现，functional sufficiency test 是亮点。但整体偏描述性/诊断性，未提出新算法。
- **总分 4.5/5**
- **为什么不是更高分：** (1) 纯分析论文，没有将几何发现转化为实际训练算法改进（如自适应 rank-constrained OPD）；(2) 实验只用一个模型规模（8B），缺乏 scale 验证；(3) 没有开源代码/诊断工具包；(4) Three-Gate 框架更多是事后解释而非预测性理论。
