# On-Policy Distillation 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes
- **Alias:** opd-pitfalls
- **Authors / Org:** Siqi Zhu et al.；UIUC × 人民大学 × 北大
- **Venue / Status:** arXiv 2605.11182v1
- **Date:** 2026-05-11
- **Links:**
  - Abs: https://arxiv.org/abs/2605.11182
  - HTML: (暂无 HTML 版本)
  - PDF: https://arxiv.org/pdf/2605.11182
  - Code: (未提供)
- **Tags:** distillation, on-policy, reverse-KL, OPSD, LLM-training, failure-analysis
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Type:** A (RL Training / Post-training)
- **Relevance:** 3/5 (有启发但非核心 agentic memory)
- **Quality:** 4/5
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1.5 = 4.5/5

## 1) 一句话 Why-read

On-policy distillation 看似优雅（student 自身分布上获得 teacher token-level supervision），但本文系统性地揭示了**三个独立的失败机制**（prefix corruption、TopK RKL gradient bias、PI-free aggregation），并给出对应 fix——核心洞察是 **distribution alignment > absolute teacher capability**（Qwen3-1.7B-GRPO teacher 竟然吊打 Qwen3-8B teacher）。

## 2) CRGP 拆解 Introduction

### C — Context
- On-policy distillation (OPD) 和 on-policy self-distillation (OPSD) 是 LLM post-training 的新兴方法
- 提供 dense token-level supervision on student's own distribution → 避免 off-policy distribution mismatch
- 已在 system prompt internalization、knowledge distillation 中展现潜力
- 但已有结果 mixed：有报告 instability 和 degradation

### R — Related work
- Off-policy KD (SeqKD 等) → distribution mismatch 问题
- On-policy KD (GKD, MiniLLM, DistillSpec 等) → student 采样 + teacher supervision
- OPSD (self-distillation with privileged information) → teacher = student + extra context
- Reverse KL vs Forward KL 在 LLM distillation 中的选择争论
- TopK token filtering 作为 vocabulary 降噪手段

### G — Research gap
- 没有人系统性诊断 OPD/OPSD **为什么失败**——已有工作只报告 "它不 work" 或在特定 setting 下 work
- 三个关键盲区：
  1. Teacher 在 student prefix 上的 degradation 未被量化
  2. TopK + Reverse KL 的 gradient bias 未被理论分析
  3. OPSD 的 PI-free aggregation 限制未被形式化

### P — Proposal
- 系统性 empirical study：when OPD/OPSD work vs fail vs why
- 识别三个 failure mechanisms 并提出对应 fixes：
  - **Fix 1:** Stop-gradient TopK KL（消除 gradient bias）
  - **Fix 2:** Normalized TopK Reverse KL（消除 +1 term bias）
  - **Fix 3:** RLVR-enhanced teacher + SFT warm-up（提供 distribution-aligned supervision）
- 关键发现：OPSD 对 shared latent rules (system prompts) 有效，对 instance-specific PI (math answers) 失败

## 3) Figure 区

> ⚠️ arXiv HTML 版本暂不可用，以下为 PDF 中关键图表描述与核心公式。

- **Figure 1（Mechanism 1 实证）：** Teacher accuracy 在 student-generated prefix 上暴跌。Qwen3-14B on GPQA-Diamond：clean prefix 62.1% → student prefix 46.0%（Δ = -16.1pp）。Teacher 在学生前缀后倾向给 "wait"、"but" 等修正 token 高概率。

- **Figure 2（Mechanism 2 数学推导）：** TopK Reverse KL gradient bias 核心公式：
  - Full vocabulary: $\sum_v p_\theta(v)\nabla_\theta \log p_\theta(v) = 0$（+1 项消去）
  - TopK truncated: $\sum_{v\in S_K} \pi_S(v)\nabla_\theta \log \pi_S(v) = \nabla_\theta \sum_{v\in S_K} \pi_S(v) \neq 0$（+1 项残留 → systematic bias）
  - 导致 token 仅在 $\pi_T(v) > e \cdot \pi_S(v)$ 时被提升

- **Figure 3（Mechanism 3 理论）：** OPSD 最优 PI-free 策略 = 归一化几何均值：
  $$p_S^*(y|x) = \frac{\exp(\mathbb{E}_{I}[\log p_T(y|x,I)])}{\sum_{y'}\exp(\mathbb{E}_{I}[\log p_T(y'|x,I)])}$$
  当 PI 是 instance-specific（如数学答案）→ 不同 PI 诱导不兼容的 teacher 行为 → geometric mean 退化为 uniform-like → 学生失去判别力。

## 4) Experiments

### 4.1 Experimental setup
- **模型:** Qwen3 系列 (1.7B, 4B, 8B, 14B)
- **Teacher 选择:** Qwen3-8B (vanilla), Qwen3-14B, Qwen3-1.7B-GRPO (RL-aligned)
- **Benchmarks:** GPQA-Diamond, Math500, AIME24, AIME25, CharacterBench, EmotionBench
- **Loss variants:** Full-vocab RKL, TopK RKL (unnormalized), TopK RKL (normalized), Stop-gradient TopK, Forward KL
- **Hardware:** 10× NVIDIA RTX PRO 6000 Blackwell
- **Hyperparams:** lr=2e-6, Adam(β1=0.9, β2=0.98), cosine decay, TopK=20, temp=1.0, top-p=0.95

### 4.2 Main result table

| Setting | Method | Result | Delta |
|---|---|---|---|
| Math OPSD (Qwen3-1.7B) | Self-distill w/ answers | Math500/AIME24/25 无改善 | 0 / negative |
| Math OPD (unnorm Top20 RKL) | Qwen3-8B teacher | 初始↑ → step 1000 崩溃为重复 "maybe" | catastrophic |
| Math OPD + PI (answer) | 额外 PI = ground truth answer | 不如 vanilla OPD | negative |
| Alignment OPSD (Qwen3-4B) | CharacterBench/EmotionBench | 收敛快于 GRPO 和 PPO | **positive** |
| OPSD 推理压缩 (Qwen3-8B) | 去 think 标签 | 长度↓ 且准确率不损 | **positive** |
| Teacher: Qwen3-8B | 直接蒸馏到 1.7B | 效果一般 | baseline |
| Teacher: Qwen3-1.7B-GRPO | RLVR-aligned 同族 | **显著优于 8B teacher** | +Δ large |
| Loss: unnorm TopK RKL (K=5) | — | 训练崩溃 | catastrophic |
| Loss: stop-gradient TopK | — | 稳定收敛 | **fix works** |
| Loss: normalized TopK RKL | — | 稳定收敛，性能相当 | **fix works** |

### 4.3 Analysis experiments

- **现象 1：Student prefix 污染 teacher**
  **解释（作者）：** Teacher 被 condition 在 student 生成的低质量 prefix 上，进入 OOD state → 准确率 -16pp → 形成负反馈循环
  **【标注】这与 agentic systems 的 context pollution 问题同构：错误的 action history 会 corrupt 后续 planning**

- **现象 2：Unnormalized TopK RKL 的训练崩溃**
  **解释（作者）：** +1 gradient term 在 TopK subset 上不消去 → token 只在 $\pi_T(v) > e \cdot \pi_S(v)$ 时被 upweight → teacher 偏好但 margin 小的 token 反被抑制 → optimization landscape 扭曲
  **【标注】这是非常 non-obvious 的发现——大多数人 TopK 截断时不会注意到 normalization constant 的梯度效应**

- **现象 3：OPSD 成功 vs 失败的边界条件**
  **解释（作者）：** PI 结构决定一切——shared latent rule (system prompt, 格式规则) → 所有 example 的 PI 一致 → geometric mean ≈ conditioned policy → 有效压缩。Instance-specific PI (数学答案) → 各 example PI 互相矛盾 → geometric mean → uniform → 崩溃。
  **【标注】这是全文最优雅的理论贡献，一个公式解释了为什么 OPSD 在 alignment 任务成功但在 math reasoning 失败**

- **现象 4：Distribution alignment >> absolute capability**
  **解释（作者）：** Qwen3-1.7B-GRPO（数学能力与 8B 相当）做 teacher 时效果显著优于 Qwen3-8B，因为 RLVR 后同族模型的 TopK vocabulary distribution 与 student 更 aligned
  **【标注】直接推翻 "bigger teacher always better" 假设。Practical implication: 先用 RL 训好一个 size-matched teacher，再蒸馏**

## 5) Why it matters for our work

- **Distribution alignment 原则**直接适用于 agentic memory distillation：从 large model 蒸馏 memory retrieval/compression 策略到 small model 时，teacher-student distribution gap 是核心问题
- **PI-free aggregation 失败**对 memory-augmented generation 有警示：如果 privileged information 是 instance-specific（如特定 memory context），OPSD 范式不适用
- **Prefix corruption ↔ Context pollution**：Agent 的错误 action history corrupt 后续 planning，与 Mechanism 1 同构——暗示 teacher-forcing on student traces 需要 safeguards
- **Stop-gradient trick** 在 memory policy distillation 中可能有用——避免 student 的 noisy retrieval 结果 corrupt teacher 的 generation quality

## 6) Actionable next step
- [ ] 在 memory distillation pipeline 中测试 distribution alignment 原则：用 RL-finetuned small teacher 替代 large base teacher
- [ ] 区分 shared-rule PI（如 retrieval strategy）vs instance-specific PI（如具体 memory content）决定是否用 OPSD
- [ ] 如果做 on-policy distillation for memory policies，实现 normalized TopK + stop-gradient 作为 default loss

## 7) 评分解释

- **质量分 2/2：** 三个 failure mechanism 诊断系统性强；Mechanism 2 的 gradient bias 推导和 Mechanism 3 的 geometric mean 证明 rigorous；实验覆盖 math reasoning + alignment + safety 多场景；写作清晰。
- **Observation 分 1.5/2：** "Distribution alignment > absolute capability" 是 non-obvious insight；TopK RKL bias 是新发现；PI 结构决定 OPSD 有效性的形式化有理论贡献。但整体偏 diagnostic（诊断问题）而非 constructive（新方法）。
- **总分 4.5/5**
- **为什么不是更高分：** Fixes 缺乏 novelty（stop-gradient、normalization、SFT warm-up 都是 standard tricks）；缺少 scaling 实验（只到 8B/14B）；没有提出统一的新蒸馏框架；与 RLVR 的 comprehensive comparison 不够充分。
