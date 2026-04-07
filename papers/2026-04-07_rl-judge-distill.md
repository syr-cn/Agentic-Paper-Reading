# DNL Deep Note — RL-Judge-Distill

## 0) Metadata
- **Title:** Reinforcement Learning-based Knowledge Distillation with LLM-as-a-Judge
- **Alias:** RL-Judge-Distill
- **Authors / Org:** Yiyang Shen, Lifu Tu, Weiran Wang / University of Iowa
- **Venue / Status:** arXiv 2604.02621v1 (preprint, under review)
- **Date:** 2026-04-03
- **Links:**
  - Abs: https://arxiv.org/abs/2604.02621
  - HTML: https://arxiv.org/html/2604.02621v1
  - PDF: https://arxiv.org/pdf/2604.02621
  - Code: N/A
- **Tags:** knowledge distillation, reinforcement learning, LLM-as-a-judge, RLVR, math reasoning, PPO, GRPO, reward design
- **My rating:** ★★★☆☆ (3/5)
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3/5**

---

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：** 提出用 LLM-as-a-Judge 的 single-token Yes/No 概率作为 RL reward，对小模型（125M–6.7B）进行 label-free knowledge distillation，在 GSM8K 上将 Galactica-125M 从 SFT 25.25% 提升到 40.71%（+15.46pp）。核心 observation：YoN reward 与 verifiable reward 效果可比，但不需要 ground truth label，意味着可以利用大量无标注数据进行蒸馏。

---

## 2) CRGP 拆解 Introduction
### C — Context
- RL（尤其 RLVR）已被证明能显著提升 LLM 的推理能力（DeepSeek-R1 等），但 RLVR 依赖 verifiable reward，即需要 ground truth labels。
- RLVR 的收益随模型规模增大而增大，小模型（<1B）获益有限。
- 知识蒸馏（KD）传统方法（SFT on teacher outputs）计算昂贵且易受 teacher reasoning error 影响。

### R — Related work
- **KD 线：** 传统 logit-level KD、pseudo-label SFT、response-priming prompting 等，均需 teacher 生成完整推理轨迹。
- **RL 线：** RLVR（DeepSeek-R1）、PPO、GRPO，但都需要 ground truth 作为 verifiable reward。
- **LLM-as-a-Judge 线：** PandaLM 等将 LLM 用作 evaluator，但主要用于 evaluation，未作为 RL training signal。

### G — Research gap
1. RLVR 需要 ground truth labels，无法利用大量无标注数据。
2. 传统 KD 需要 teacher 生成完整推理过程，计算开销大且易引入错误。
3. 缺少一种轻量、可扩展的方式将大模型的 "判断能力" 转移给小模型。

### P — Proposal
- **RL + LLM-as-a-Judge 框架：** Student 生成候选推理轨迹 → Judge LLM 用 single-token Yes/No 概率评估 → 作为 continuous reward 驱动 PPO/GRPO 训练。
- **三路 reward 组合：** L_overall = λ·L_VR + μ·L_YoN + ρ·L_Rerank（λ+μ+ρ=1），支持 supervised、unsupervised、semi-supervised 三种设置。
- **Semi-supervised setup：** labeled data 走 verifiable reward，unlabeled data 走 judge reward，充分利用两类数据。

---

## 3) Figure 区

- 图1（学习曲线 — PPO semi-supervised）：![fig1](https://arxiv.org/html/2604.02621v1/x1.png) — 展示不同 reward 组合下的 GSM8K 训练曲线，semi-supervised 设置（λ=0.5, μ=0.25, ρ=0.25）在训练后期持续攀升至 ~40%，显著优于纯 RLVR baseline（~30%）。

- 图2（PPO vs GRPO 对比）：![fig2](https://arxiv.org/html/2604.02621v1/x2.png) — GRPO 在相同 reward 配置下比 PPO 提供更大的性能增益（37.30% vs 35.10%），且收敛更快。

- 图3（三路 reward 曲线）：![fig3](https://arxiv.org/html/2604.02621v1/x3.png) — Verifiable / Judge / Rerank 三路 reward 均在训练中稳定上升并趋于平稳，表明三种 reward signal 互相兼容、训练稳定。

---

## 4) Experiments
### 4.1 Experimental setup
- 任务/数据：数学推理（GSM8K, GSM-Plus, GSM-Symbolic, SVAMP）；Supervised: GSM8K train；Unsupervised: GSM8K-aug, GSM-Plus（无 label）
- 模型/agent 配置：Student = Galactica-125M / Galactica-6.7B / CodeGen-350M；Judge = Qwen3-8B（YoN accuracy 88.0% on GSM8K）；Reranker = 6.7B pretrained model
- 对比基线：SFT Complete, RLVR (PPO, λ=1.0), Trung et al. (2024) reproduced results
- 评测指标：Accuracy on test set; out-of-domain generalization (GSM-Plus, GSM-Symbolic, SVAMP)

### 4.2 Main result table

**Table 4: Galactica-125M on GSM8K（核心结果）**

| Setting | λ | μ | ρ | GSM8K | SVAMP |
|---|---|---|---|---:|---:|
| SFT Complete | – | – | – | 25.25 | 32.30 |
| RLVR only | 1.0 | 0.0 | 0.0 | 30.48 | 31.30 |
| VR + YoN | 0.5 | 0.5 | 0.0 | 30.63 | 35.90 |
| YoN only | 0.0 | 1.0 | 0.0 | 29.19 | 37.00 |
| + GSM8K-aug: VR+YoN | 0.5 | 0.5 | 0.0 | 35.10 | 40.70 |
| + GSM8K-aug: semi-sup best | 0.5 | 0.25 | 0.25 | 40.11 | — |
| + GSM8K-aug: judge-only best | 0.0 | 0.5 | 0.5 | **40.71** | — |

**Table 6: GRPO vs PPO（Galactica-125M, GSM8K-aug）**

| Setting | GSM8K | SVAMP |
|---|---:|---:|
| PPO (0.5, 0.5, 0.0) | 35.10 | 40.70 |
| GRPO (0.5, 0.5, 0.0) | **37.30** | **45.20** |

**Table 6 续: Galactica-6.7B (PPO)**

| Setting | GSM8K | SVAMP |
|---|---:|---:|
| RLVR only (1.0, 0, 0) | 69.07 | 69.40 |
| + voting | 71.72 | 70.80 |
| VR+YoN (0.5, 0.5, 0) | 70.43 | 74.20 |
| + voting | **71.95** | **74.90** |

### 4.3 Analysis experiments

- **现象：** YoN-only reward（λ=0, μ=1.0）在无 augmented data 时与 RLVR 表现接近（29.19% vs 30.48%），但加入 augmented data 后大幅领先（33.13% vs 30.48%）。
  **解释（作者）：** Judge reward 的价值在于能利用无标注数据——数据量是 key enabler。
  **【标注】好的 insight：** 这说明 judge reward 本身 signal quality 不比 verifiable reward 差，瓶颈在于有多少无标注数据可用。

- **现象：** Semi-supervised 设置（λ=0.5, μ=0.25, ρ=0.25）达到 40.11%，纯 judge 设置（0, 0.5, 0.5）达到 40.71%，两者都远超纯 RLVR（30.48%）。
  **解释（作者）：** RLVR 起到稳定训练的作用（防止 reward hacking），但纯 judge signal 在有足够数据时已经足够强。
  **【标注】矛盾信号：** 纯 judge（λ=0）竟然略高于 semi-sup（λ=0.5），这与作者强调 RLVR 稳定训练的叙述存在张力——可能是 GSM8K-aug 数据质量较高所致。

- **现象：** GRPO 在相同 reward 配置下比 PPO 高 ~2pp（37.30% vs 35.10%）。
  **解释（作者）：** GRPO 的 group-relative 基线估计比 PPO 的 value network 更适合小模型。

- **现象：** 当 λ=0 在 SVAMP 上训练时出现 model collapse。
  **解释（作者）：** 缺少 verifiable reward 的锚定，judge reward 可能被 hack。RLVR 提供必要的训练稳定性。
  **【标注】重要限制：** 这说明纯 judge reward 并非万能——在 domain shift 或数据质量不够高时仍需 ground truth 锚定。

- **现象：** Qwen3-8B 作为 judge 的 YoN accuracy 显著优于 Gemma3-12B（GSM8K: 88.0 vs 85.0），且 LL（log-likelihood）方法在 Gemma3 上严重退化（49.5%）。
  **解释（作者）：** YoN prompt-based scoring 比 log-likelihood 更稳定可靠，模型选择对 judge quality 至关重要。

---

## 5) Why it matters for our work
- **RL reward design 的新思路：** 用 LLM judge 的 single-token 概率作为 continuous reward，比传统 binary reward 信息更丰富，且不需要 ground truth——这对我们做 agentic RL / memory-augmented reasoning 的 reward 设计有直接参考价值。
- **小模型 reasoning 的低成本增强：** 125M–350M 模型通过 RL+judge 获得 +10~15pp 提升，证明了"判断比生成便宜"的蒸馏路线可行性——对部署端侧推理模型有启发。
- **Semi-supervised RL 的实践模式：** labeled data 走 verifiable reward、unlabeled data 走 judge reward 的混合模式，是一种可推广的 RL training recipe。

## 6) Actionable next step
- [ ] 测试 YoN reward 在非数学任务（如 agent trace evaluation）上的 judge quality
- [ ] 探索将此 judge-as-reward 框架用于 agentic memory system 的 retrieval quality 评估
- [ ] 关注后续是否开源代码和 judge prompt template

## 7) 评分解释
- **质量分 1/2：** 方法清晰、实验覆盖多模型多数据集，但核心 idea 较为直接（YoN 概率做 reward），novelty 有限。实验仅在数学推理上验证，缺少 NL 任务的系统性实验。
- **Observation 分 1/2：** YoN vs LL 的 judge quality 对比、semi-supervised 混合模式、model collapse 现象均有价值，但未深入分析 why judge reward 有效的理论机制（例如 reward signal 的 informativeness 与 verifiable reward 的本质差异）。
- **总分 3/5：** 实用的工程 recipe，但理论深度和 novelty 均为中等。
- **为什么不是更高分：** 核心贡献是一个组合式框架（RL + judge reward），各组件（PPO/GRPO、LLM-as-judge、semi-supervised）均非新提出；数学推理以外的泛化性未验证；无代码开源。
