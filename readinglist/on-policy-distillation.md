# On-Policy Distillation Reading List

## 🧭 领域概览

On-Policy Distillation (OPD) 是介于纯 SFT 和纯 RL 之间的训练范式：让 student 在**自己生成的 rollouts** 上接受 teacher 的 token-level 指导，消除 train-test distribution mismatch。

### 当前趋势（2025-2026）

1. **OPD ↔ RL 融合**：REOPOLD & G-OPD 证明 OPD 是 KL-constrained RL 的特例。RL 的稳定化技术可迁移到 OPD；G-OPD 的 reward extrapolation (λ>1) 实现 student 超越 teacher。
2. **Self-Distillation 成为主流**：无需外部大 teacher，通过信息不对称（privileged info / feedback / instruction）让模型自己教自己。
3. **KL 方向不是非此即彼**：动态选择 Forward/Reverse KL（按 teacher confidence）优于固定方向。
4. **应用快速扩展**：从数学推理 → code、video、continual learning、推理压缩、Agent 训练。
5. **实践挑战系统化**：failure modes 被识别（imbalanced signal, unreliable teacher on OOD prefixes, tokenizer mismatch）；ray interference 被发现。

### 关键技术选择空间

| 维度 | 选项 |
|------|------|
| KL 方向 | Forward KL (mode-covering) / Reverse KL (mode-seeking) / Adaptive |
| Teacher 类型 | External large model / Self (self-distillation) / Same model + privileged info |
| 信号粒度 | Token-level (主流) / Sequence-level |
| White-box vs Black-box | 需要 teacher logits / 只需 teacher output text |
| 与 RL 的关系 | 纯 distillation / OPD as RL special case / OPD + RL hybrid |

### 系统性空白（研究机会）

- **OPD + RL 组合训练**几乎未探索（最大机会）
- **Token-level adaptive routing**（何时用 OPD、何时切 RL）无成熟方案
- **规模验证**不足（>8B student, >32B teacher 的结果几乎没有）
- **非数学领域**（code, instruction following, agent）验证严重不足
- **统一评测框架**缺失（15 篇论文零 head-to-head 对比）

---

### OPD ↔ RL Unification

理论证明 OPD = dense KL-constrained RL，打通两个范式的技术栈。

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [G-OPD](../papers/2026-05-13_opd-survey-notes.md#g-opd) | G-OPD: Learning beyond Teacher — Generalized On-Policy Distillation with Reward Extrapolation | [arXiv 2602.12125](https://arxiv.org/abs/2602.12125) | First: RUC; High-impact: RUC | A | 5 | 4 | N/A | 证明 OPD = dense KL-constrained RL 的特例；reward extrapolation (λ>1) 让 student 超越所有 teachers；多域 expert merging 场景尤其有效。 |
| [REOPOLD](../papers/2026-05-13_opd-survey-notes.md#reopold) | REOPOLD: Scaling Reasoning Efficiently via Relaxed On-Policy Distillation | [arXiv 2603.11137](https://arxiv.org/abs/2603.11137) | First: N/A; High-impact: N/A | A | 4 | 3 | N/A | 将 OPD 重写为 policy optimization（log-likelihood ratio = token-level reward）；三组件框架（mixture clipping + entropy sampling + exploration-to-refinement）；sample efficiency 6.7-12x vs pure RL。 |
| [SDPO](../papers/2026-05-13_opd-survey-notes.md#sdpo) | SDPO: Reinforcement Learning via Self-Distillation | [arXiv 2601.20802](https://arxiv.org/abs/2601.20802) | First: ETH Zurich; High-impact: ETH Zurich | A | 4 | 4 | N/A | 利用 rich textual feedback (runtime errors, review comments) 做 self-distillation；LCB v6: 48.8% vs GRPO 41.2% (超 Claude Sonnet 4 的 40.5%)；4x faster convergence；generation length 3x shorter。 |

### Self-Distillation

无需外部 teacher，通过信息不对称让模型自己教自己。

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [OPSD](../papers/2026-05-13_opd-survey-notes.md#opsd) | Self-Distilled Reasoner — On-Policy Self-Distillation for LLMs | [arXiv 2601.18734](https://arxiv.org/abs/2601.18734) | First: N/A; High-impact: N/A | A | 4 | 3 | N/A | 同一模型 teacher mode (conditioned on GT CoT) vs student mode (只看题目)；反直觉发现：Forward KL 在 self-distill 中优于 Reverse KL（因为 teacher-student 分布已接近）。 |
| [OPSDC](../papers/2026-05-13_opd-survey-notes.md#opsdc) | OPSDC: On-Policy Self-Distillation for Reasoning Compression | [arXiv 2603.05433](https://arxiv.org/abs/2603.05433) | First: N/A; High-impact: N/A | A | 3 | 3 | N/A | 极简方案："be concise" instruction 做 teacher → token 减 57-59% + accuracy +9-16pp (Qwen3-8B/14B MATH-500)；机制未知但有效。 |
| [OEL](../papers/2026-03-18_oel.md) | Online Experiential Learning for Language Models | [arXiv 2603.16856](https://arxiv.org/abs/2603.16856) | First: N/A; High-impact: N/A | A | 4 | 4 | [Fig.1](https://arxiv.org/html/2603.16856v1/figures/oel-overview.pdf) | 经验抽取后再做 on-policy 蒸馏显著优于直接吃原始轨迹（Sokoban consolidate 21.4 vs 7.8）；self-policy 经验优于更大教师经验。 |
| [ExGRPO](../papers/2026-03-23_exgrpo.md) | ExGRPO: Learning to Reason from Experience | [arXiv 2510.02245](https://arxiv.org/abs/2510.02245) | First: U Macau; High-impact: Shanghai AI Lab | A | 4 | 4 | ![fig1](https://arxiv.org/html/2510.02245v1/x1.png) | 首个系统研究 RLVR 经验价值：中等难度+低熵轨迹是最优来源；bucketed replay + entropy selection 在 5 模型上 +3.5/+7.6 (ID/OOD)。 |
| [SDFT](../papers/2026-05-13_opd-survey-notes.md#sdft) | SDFT: Self-Distillation Enables Continual Learning | [arXiv 2601.19897](https://arxiv.org/abs/2601.19897) | First: N/A; High-impact: N/A | A | 3 | 3 | N/A | 用 in-context learning 将 off-policy demo 转为 on-policy signal → continual learning 不灾难性遗忘。ICL 能力弱的小模型可能失效；场景有限（仅测试几个 task sequence）。 |


### KL Direction & Training Stability

Forward vs Reverse KL 的选择、稳定性问题、failure mode 分析。

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [Revisiting-OPD](../papers/2026-05-13_opd-survey-notes.md#revisiting-opd) | Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes | [arXiv 2603.25562](https://arxiv.org/abs/2603.25562) | First: N/A; High-impact: N/A | C | 4 | 4 | N/A | 首次系统识别 3 个 OPD failure modes（imbalanced signal, unreliable teacher on OOD prefix, tokenizer mismatch）；truncated reverse-KL + top-p sampling + special-token masking。 |
| [BiCC-RCC](../papers/2026-03-17_bicc-rcc-grpo.md) | When Right Meets Wrong: Bilateral Context Conditioning with Reward-Confidence Correction for GRPO | [arXiv 2603.13134](https://arxiv.org/abs/2603.13134) | First: N/A; High-impact: N/A | A | 3 | 3 | [Fig.1](https://arxiv.org/html/2603.13134/x1.png) | 将 GRPO 组内对错结构显式条件化 + 协方差修正 baseline；价值在降方差与收敛稳定。 |
| [Veto](../papers/2026-05-13_opd-survey-notes.md#veto) | Veto: Stable On-Policy Distillation through Adaptive Target Reformulation | [arXiv 2601.07155](https://arxiv.org/abs/2601.07155) | First: N/A; High-impact: N/A | A | 3 | 2 | N/A | Geometric bridge in logit space 连接 teacher-student 分布；β decay 从 exploration→exploitation。实验规模太小（0.5B-2B），理论与实践矛盾。 |
| [Entropy-Aware-OPD](../papers/2026-05-13_opd-survey-notes.md#entropy-aware) | Entropy-Aware On-Policy Distillation of Language Models | [arXiv 2603.07079](https://arxiv.org/abs/2603.07079) | First: N/A; High-impact: Arcee AI | A | 4 | 3 | N/A | 按 teacher token-level entropy 动态切换 Forward/Reverse KL；Qwen3-4B Pass@8 +5.05。阈值 τ 是 fragile hyperparameter。 |


### Exploration & Curriculum

如何处理难题（teacher 也不会的问题）、ray interference、数据合成。

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [POPE](../papers/2026-05-13_opd-survey-notes.md#pope) | POPE: Learning to Reason on Hard Problems via Privileged On-Policy Exploration | [arXiv 2601.18779](https://arxiv.org/abs/2601.18779) | First: CMU; High-impact: Google | A | 4 | 4 | N/A | 发现 Ray Interference（混合简单难题训练有害）；用 oracle prefix 做 privileged exploration 引导 RL 在难题上获得 non-zero reward；guided capability 可 transfer 回无引导设置。 |
| [TRT](../papers/2026-03-23_trt.md) | Test-time Recursive Thinking | [arXiv 2602.03094](https://arxiv.org/abs/2602.03094) | First: MSR; High-impact: MSR | B | 3 | 4 | N/A | 无外部反馈的 test-time 自改进：Generate-Select-Reflect；失败知识 > 成功知识，depth > breadth。 |
| [ICRL](../papers/2026-03-12_icrl-tool-use.md) | In-Context Reinforcement Learning for Tool Use | [arXiv 2603.08068](https://arxiv.org/abs/2603.08068) | First: NUS; High-impact: UCB | A | 3 | 3 | N/A | Rollout 内 few-shot 课程退火替代 cold-start SFT；验证 RL-only 学稳工具调用。 |
| [Golden-Goose](../papers/2026-05-13_opd-survey-notes.md#golden-goose) | Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text | [arXiv 2601.22975](https://arxiv.org/abs/2601.22975) | First: NVIDIA; High-impact: UW (Yejin Choi) | A | 3 | 3 | N/A | 将非验证文本转为 MCQ fill-in-the-middle → GooseReason-0.7M（70% effective rate vs ProRL 25%）；4B+GooseReason 逼近 Qwen3-30B-Instruct。重依赖 GPT-5 合成；MCQ≠生成能力。 |


### Industrial & Scaling

工业级实践、大规模验证、多域训练。

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [Nemotron-Cascade-2](../papers/2026-05-13_opd-survey-notes.md#nemotron) | Nemotron-Cascade 2: Multi-Domain On-Policy Distillation | [arXiv 2603.19220](https://arxiv.org/abs/2603.19220) | First: NVIDIA; High-impact: NVIDIA | A | 4 | 4 | N/A | 30B MoE→3B；MOPD reverse KL token-level advantage + truncated importance weighting；AIME25: 30 steps → 92.0 vs GRPO 25 steps → 91.0；ArenaHard: 52 steps → 85.5 vs RLHF 160 steps → 80.7；40-50 步收敛。 |
| [Agent-World](../papers/2026-05-13_agent-world.md) | Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence | [arXiv 2604.18292](https://arxiv.org/abs/2604.18292) | First: RUC; High-impact: ByteDance Seed | A | 4 | 4 | ![fig1](https://arxiv.org/html/2604.18292v1/extracted/6291893/figure/agent-world-overview.png) | 环境-策略共演化；1978 envs → log-linear scaling (+20.1pp)；self-evolving 2 轮 +8.6pp。 |
| [RL-Judge-Distill](../papers/2026-04-07_rl-judge-distill.md) | RL-based Knowledge Distillation with LLM-as-a-Judge | [arXiv 2604.02621](https://arxiv.org/abs/2604.02621) | First: N/A; High-impact: N/A | A | 3 | 2 | [Fig.1](https://arxiv.org/html/2604.02621v1/x1.png) | LLM judge 做 reward signal 的 RL 蒸馏；novelty 有限。 |

### Application Extension

OPD 在新领域（video, context distillation, continual learning）的应用。

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [OPCD](../papers/2026-05-13_opd-survey-notes.md#opcd) | OPCD: On-Policy Context Distillation for Language Models | [arXiv 2602.12275](https://arxiv.org/abs/2602.12275) | First: Microsoft; High-impact: Microsoft | A | 3 | 3 | N/A | 结合 on-policy distillation + context distillation：将 experiential knowledge / system prompt 内化到模型权重。仅 50 步训练。 |
| [GAD](../papers/2026-05-13_opd-survey-notes.md#gad) | GAD: Black-Box On-Policy Distillation of Large Language Models | [arXiv 2511.10643](https://arxiv.org/abs/2511.10643) | First: Microsoft; High-impact: Microsoft | A | 3 | 2 | N/A | GAN-based OPD：student=generator, discriminator=co-evolving reward model。唯一 black-box OPD 方案（不需 teacher logits）。唯一评估是 GPT-4o score，无客观 benchmark。 |
| [Video-OPD](../papers/2026-05-13_opd-survey-notes.md#video-opd) | Video-OPD: Efficient Post-Training of MLLMs for Temporal Video Grounding | [arXiv 2602.02994](https://arxiv.org/abs/2602.02994) | First: Tencent ARC; High-impact: Tencent ARC | A | 2 | 3 | N/A | 将 OPD 应用到 Temporal Video Grounding；Teacher-Validated Disagreement Focusing (TVDF) 优先可靠且高收益样本；compute 仅 GRPO 的 ~20%。仅 TVG 任务验证。 |
| [VOLD](../papers/2026-05-13_opd-survey-notes.md#vold) | VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation | [arXiv 2510.23497](https://arxiv.org/abs/2510.23497) | First: N/A; High-impact: N/A | A | 2 | 3 | N/A | 将 DeepSeek-R1 reasoning 通过 OPD 迁移到 VLM；LLM→VLM 跨模态蒸馏。 |
| [AlignDistil](../papers/2026-05-13_opd-survey-notes.md#aligndistil) | AlignDistil: Token-Level Language Model Alignment as Adaptive Policy Distillation | [arXiv 2503.02832](https://arxiv.org/abs/2503.02832) | First: N/A; High-impact: N/A | A | 2 | 3 | N/A | 将 RLHF alignment 重构为 token-level adaptive policy distillation；从 DPO 的 implicit policy 蒸馏。 |

### Foundational Works

OPD 领域的奠基性论文。

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [MiniLLM](../papers/2026-05-13_opd-survey-notes.md#minillm) | MiniLLM: Knowledge Distillation of Large Language Models | [arXiv 2306.08543](https://arxiv.org/abs/2306.08543) | First: N/A; High-impact: N/A | A | 3 | 4 | N/A | OPD 奠基工作之一：证明 Reverse KL (mode-seeking) 在 LLM distillation 中优于 Forward KL；建立 OPD 的基本范式。 |
| [GKD](../papers/2026-05-13_opd-survey-notes.md#gkd) | On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes | [arXiv 2306.13649](https://arxiv.org/abs/2306.13649) | First: Google; High-impact: Google | A | 4 | 4 | N/A | Generalized Knowledge Distillation：将 OPD 与 imitation learning 统一；学生在自己的分布上接受 teacher supervision 消除 exposure bias。OPD 领域的 canonical reference。 |