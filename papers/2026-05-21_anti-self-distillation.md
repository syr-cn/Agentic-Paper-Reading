# DNL Deep Note — Anti-Self-Distillation (AntiSD)

## 0) Metadata
- **Title:** Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information
- **Alias:** AntiSD
- **Authors / Org:** Guobin Shen, Xiang Cheng, Chenxiao Zhao, Lei Huang (Xiaohongshu Inc.) + Jindong Li, Dongcheng Zhao (中科院自动化所)
- **Venue / Status:** arXiv 2605.11609v1（preprint, 2026-05-12）
- **Date:** 2026-05-12
- **Links:**
  - Abs: https://arxiv.org/abs/2605.11609
  - HTML: https://arxiv.org/html/2605.11609v1
  - PDF: https://arxiv.org/pdf/2605.11609
  - Code: https://github.com/FloyedShen/AntiSD
  - W&B: https://wandb.ai/brain-cog/AntiSD
- **Tags:** RLVR, self-distillation, PMI, credit assignment, GRPO, reasoning, post-training
- **My rating:** ★★★★☆（4/5）
- **Read depth:** deep（方法 + 主实验 + 消融）
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = **4/5**
- **alphaXiv link:** https://www.alphaxiv.org/overview/2605.11609
- **Community stats:** HF Daily Papers ⬆️61

---

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：** On-policy self-distillation 在 math reasoning 上失效的根因是 PMI 信号极性反转——privileged context（答案）inflate 了 shortcut tokens（Given, holds）的信心，deflate 了 deliberation tokens（Wait, Let, Maybe）的信心。AntiSD 通过 **ascend** JSD divergence 反转极性，配合 entropy-triggered gate，2–10× 更少步数达到 GRPO baseline 精度，最终精度提升最高 +11.5 points。

---

## 2) CRGP 拆解 Introduction
### C — Context
- RLVR（如 GRPO）是 reasoning post-training 主范式，但 reward 是 trajectory-level sparse scalar，credit assignment 到单步是 open problem。
- 两条路线：PRM（需要外部 reward model）和 on-policy distillation（OPD，需要 stronger teacher）。

### R — Related work
- **Self-distillation 线：** Zhao et al. 2026, Hübotter et al. 2026, Ye et al. 2026, Sang et al. 2026 — 把 teacher 替换为"自己 conditioned on privileged context"，无需外部模型。
- **成功案例：** instruction-following、scientific QA、tool-use 上有效。
- **失败案例：** math reasoning 上 gains inconsistent，response 越来越短。

### G — Gap
- 没人分析"为什么 self-distillation 在 math 上失效"。作者通过 PMI 分析发现 privileged context **极性反转**：奖励了不该奖励的 tokens、惩罚了应该保护的 tokens。

### P — Proposal
1. **PMI 诊断**：识别 u_t = PMI(y_t; c | x, y<t) 的 shortcut bias — u_t > 0 奖励 shortcut tokens，u_t < 0 惩罚 deliberation tokens。
2. **AntiSD**：ascend JSD divergence（而非 descent KL），反转 per-token sign。JSD 的 softplus 形状天然 bound deliberation 侧的 heavy tail，缓解梯度爆炸。
3. **Entropy-triggered gate**：teacher entropy 塌缩到阈值以下时关闭 AntiSD term（u_t 不再携带有用信息）。

---

## 3) Figure 区

- 图2（PMI 分析 — 核心洞察图）

![fig2](https://arxiv.org/html/2605.11609v1/x2.png)

  解释：(a) 单条 rollout 中 u_t 值沿 token 序列交替出现正/负极端值，deep red = shortcut tokens（u_t >> 0），deep blue = deliberation tokens（u_t << 0）。(b) (πS, πT) 热力图展示两个 off-diagonal lobes：deliberation lobe 更重（因为 rollout from πS 时 πS > πT 的 tokens 被 over-sample）。

- 图1（主结果训练曲线）

![fig1](https://arxiv.org/html/2605.11609v1/x1.png)

  解释：AntiSD 在训练早期即超越 GRPO，并维持更高的最终精度。SD（标准 self-distillation）在 math 上迅速退化。

---

## 4) Experiments
### 4.1 Experimental setup
- **模型：** 5 个 models — Qwen3-8B, Qwen3-4B-IT-2507, OLMo3-7B-IT, OLMo3-7B-TK (Think), Qwen3-30B-A3B
- **训练数据：** 未明确指定数据集名称（从 AIME-level 题库中采样）
- **训练步数：** 200 steps
- **GRPO 参数：** batch size 32 problems, group size 8, lr 1e-6, max seq 32K, clip 0.2, verl framework, 8× H20 GPUs
- **AntiSD 参数：** λ_max = 0.5, warmup 5 steps, τ_down = 0.93 · H_warm
- **评测：** AIME24, AIME25, AIME26, HMMT25, MinervaMath; Pass@1 w/ 32 rollouts (temperature 0.7, top-p 0.95)

### 4.2 Main result table

| Model | Method | AIME24 | AIME25 | AIME26 | HMMT25 | Minerva | Avg | Speedup |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Qwen3-8B | +GRPO | 73.5 | 65.2 | 64.2 | 39.2 | 45.1 | 57.4@200 | 1.0× |
| | +SD | 40.1 | 30.5 | 26.9 | 14.9 | 40.7 | 30.6@200 | ✗ |
| | **+AntiSD** | **78.4** | **73.4** | **73.7** | **54.4** | **48.5** | **65.7@180** | **5.0×** |
| Qwen3-4B-IT | +GRPO | 67.8 | 57.7 | 63.5 | 34.1 | 33.2 | 51.3@200 | 1.0× |
| | +SD | 59.8 | 45.8 | 52.0 | 28.8 | 43.0 | 45.9@10 | ✗ |
| | **+AntiSD** | **76.6** | **70.2** | **74.4** | **46.7** | **46.4** | **62.8@100** | **10.0×** |
| OLMo3-7B-IT | +GRPO | 57.0 | 45.3 | 52.1 | 31.2 | 29.1 | 43.0@190 | 1.0× |
| | **+AntiSD** | **62.4** | **49.1** | **55.2** | **32.3** | **42.4** | **48.3@200** | **9.5×** |
| OLMo3-7B-TK | +GRPO | 76.5 | 71.7 | 75.3 | 50.5 | 46.4 | 64.1@80 | 1.0× |
| | **+AntiSD** | **77.6** | **75.3** | **76.1** | **56.2** | **45.8** | **66.2@40** | **2.0×** |

**关键数字：** Qwen3-4B-IT 上 AntiSD vs GRPO：avg +11.5 points (62.8 vs 51.3)，且只需 100 steps（10× speedup）。

### 4.3 Analysis experiments

- **现象1：** 标准 SD 在所有 math 模型上显著退化（Qwen3-8B 从 57.4 暴跌到 30.6）。
  **解释（作者）：** PMI 极性反转系统性压制 deliberation tokens，模型"学会"跳过思考步骤直接给结论。
  **【标注】** 这解释了之前文献中反复报告的 "response shortening" 现象 — 不是 benign compression，是 structural shortcut。

- **现象2：** rev. KL 作为 ascent 目标直接崩溃（Qwen3-4B 从 51.3 降到 49.5），而 JSD ascent 在所有配置上有效。
  **解释（作者）：** rev. KL 的 per-token advantage u_t 在 deliberation 侧 unbounded（可达 -20），梯度方差爆炸。JSD 的 softplus 形状天然 cap deliberation 侧 at ½log2。
  **【标注】** divergence 选型的核心不是"哪个更 principled"，而是"哪个在 empirical token distribution 下 gradient 更 well-behaved"。

- **现象3：** Entropy gate 的 τ_down 选 0.93 效果最佳；无 gate 时部分配置掉点。
  **解释（作者）：** 一旦 teacher entropy 塌缩，u_t 不再携带条件信息（teacher 对所有 token 都极度自信），AntiSD 退化为噪声。
  **【标注】** 这是"信号质量感知"的 RL 设计原则 — 不是所有 token 都值得 per-token reward，要有动态开关。

- **现象4：** AntiSD 从 GRPO step 150 接力（+50 steps），效果接近从头训 200 steps 的 AntiSD（65.0 vs 65.7）。
  **解释（作者）：** AntiSD 可作为 drop-in 加速器，无需从头训。
  **【标注】** 工程价值高：对已训好的 GRPO checkpoint 直接"续训"50 steps 就能拿到大部分收益。

---

## 5) Why it matters for our work
- **Post-training/RLVR：** 直接给出"per-token credit assignment via PMI"的理论框架，对我们理解 GRPO 训练动态有直接帮助。
- **Deliberation token 保护：** 对 agentic reasoning（多步 plan/reflect/revise）同样适用 — 任何压制"思考 token"的 training signal 都会削弱 agent 的 multi-step search 能力。
- **信号质量 gating：** entropy-triggered gate 的设计模式可迁移到 memory-augmented RL — 当 memory retrieval 信号质量低时自动关闭 memory bonus。

---

## 6) Actionable next step
- [ ] 在 multi-modal RL 训练中监测 PMI(y_t; visual_context | x, y<t) 的极性分布，验证视觉 privileged context 是否存在类似 shortcut bias。
- [ ] 将 AntiSD 作为 drop-in module 集成到现有 GRPO pipeline（从 checkpoint 续训 50 steps），测试在 agentic task 上的效果。
- [ ] 借鉴 entropy-triggered gate 的思路，为 memory-conditioned generation 设计"memory quality gate"。

---

## 7) 评分解释
- **Type:** A (RL Training)
- **Relevance:** 4/5 — 直接命中 post-training/RLVR，对 reasoning RL credit assignment 有理论贡献；与 agentic memory 间接相关。
- **Quality:** 4/5 — 5 个模型覆盖 4B–30B，5 个 benchmark，消融完整（divergence 选型 + gate + 接力训练），W&B logs 公开。
- **质量分 2/2：** 理论（PMI 分析）+ 实验（跨模型一致提升）+ 工程（drop-in, 开源）三方面完整。
- **Observation 分 1/2：** "deliberation tokens 被 self-distillation 压制"的洞察有新意，但解法本身（flip gradient sign）并不 surprising — 一旦诊断出极性问题，修复方向是显然的。
- **总分：4/5**
- **为什么不是更高分：** (1) 仅在 math reasoning 验证，未扩展到 code/tool-use/agentic 场景；(2) 核心方法 = "发现 sign 反了，翻过来"，conceptual novelty 有限；(3) 对比 baseline 只有 GRPO 和 vanilla SD，缺少与 PRM 等 dense reward 方法的对照。
