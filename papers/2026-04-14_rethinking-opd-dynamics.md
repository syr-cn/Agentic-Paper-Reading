# Rethinking On-Policy Distillation: Phenomenology, Mechanism, and Recipe

## 0) Metadata
- **Title:** Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe
- **Alias:** rethinking-opd-dynamics
- **Authors / Org:** Yaxuan Li*, Yuxin Zuo*, Bingxiang He*, Jinqian Zhang, Chaojun Xiao, Cheng Qian, Tianyu Yu, Huan-ang Gao, Wenkai Yang, Zhiyuan Liu, Ning Ding; Tsinghua University (THUNLP) + ShanghaiTech + UIUC + RUC
- **Venue / Status:** arXiv 2604.13016
- **Date:** 2026-04-14
- **Links:**
  - Abs: https://arxiv.org/abs/2604.13016
  - HTML: https://arxiv.org/html/2604.13016v2
  - PDF: https://arxiv.org/pdf/2604.13016
  - alphaXiv: https://www.alphaxiv.org/overview/2604.13016
  - Code: https://github.com/thunlp/OPD
- **Tags:** on-policy-distillation, training-dynamics, knowledge-distillation, LLM-post-training, reasoning, failure-analysis
- **My rating:** ⭐⭐⭐⭐⭐
- **Read depth:** deep
- **Type:** A (RL Training)
- **Relevance:** 5/5 (核心命中 — OPD 动力学机制的系统性研究，直接服务 OPD pipeline 设计)
- **Quality:** 5/5 (THUNLP Zhiyuan Liu + Ning Ding；30 pages, 23 figures；系统性强；code released)
- **Community:** alphaXiv likes: 137 / HF upvotes: N/A
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 2 = 5

## 1) 一句话 Why-read
- **Key claim:** OPD 成功需要两个条件：(1) teacher-student thinking-pattern consistency（分布兼容性）+ (2) teacher 提供 genuinely new capabilities（而非仅分数更高）。更强的 teacher 可能完全失败，更弱但 RL-trained 的 teacher 反而成功。
- **Key observation:** OPD 的 token-level 机制是在 shared top-k tokens（仅占 vocabulary 极小部分但覆盖 97-99% probability mass）上做 progressive alignment；且 reward quality 随 trajectory depth 系统性退化 → 长序列 OPD 有天然 scaling limitation。

## 2) CRGP 拆解 Introduction
### C — Context
- OPD 已成为工业级 post-training 标配（Qwen3, MiMo, GLM-5 均采用）
- Student 生成 rollouts，teacher 提供 token-level supervision，避免 exposure bias
- 已扩展到 self-distillation settings

### R — Related work
- Knowledge distillation (Hinton et al.) → off-policy distribution mismatch
- On-policy distillation (DAgger-style, GKD, MiniLLM)
- Capacity gap 与 distillability 文献
- 工业实践：Qwen3, MiMo, GLM-5, Thinking Machines Lab replication

### G — Research gap
- OPD 被广泛采用但训练动力学理解极差
- 核心困惑：stronger teacher 可能完全 fail to improve student，而 weaker teacher 成功 — 没有系统性解释
- Token-level 优化的具体机制（学了什么、怎么学的）未被刻画

### P — Proposal
系统性研究 OPD，提供四层贡献：
1. **Phenomenology** — 成功/失败的两个充要条件
2. **Mechanism** — Progressive alignment on shared high-prob tokens
3. **Recipe** — Off-policy cold start + teacher-aligned prompt selection
4. **Limitation** — Reward degradation with depth，长序列 OPD 天然受限

## 3) Figure 区

![Figure 1: Overview](https://arxiv.org/html/2604.13016v2/x2.png)

**Figure 1:** JustRL-1.5B（RL-trained, 同规模）成功教 R1-Distill-1.5B（closing ~80% gap），而同家族更大的 R1-Distill-7B（更强但同 pipeline）完全失败 — 证明 thinking-pattern compatibility + new knowledge 比 raw teacher strength 重要得多。

![Figure 6: Successful vs Failing dynamics](https://arxiv.org/html/2604.13016v2/x7.png)

**Figure 6:** 成功 OPD 的三个诊断指标：overlap ratio 上升（72%→91%）、overlap-token advantage 收敛、entropy gap 缩小。失败 OPD 这三个指标均停滞/下降。

## 4) Experiments

### 4.1 Experimental setup
- **Tasks:** Math reasoning (AIME 2024, AIME 2025, AMC 2023)
- **Student models:** R1-Distill-1.5B, Qwen3-1.7B-Base
- **Teacher models:** JustRL-1.5B (RL-trained), R1-Distill-7B (same-family), Skywork-OR1-Math-7B, Qwen3-4B Non-thinking, Qwen3-4B-Base-GRPO
- **Metrics:** avg@16 accuracy, gap recovery rate, overlap ratio, overlap-token advantage, entropy gap
- **OPD variants:** Sampled-token, Full-vocabulary, Top-k (k=16)

### 4.2 Main result table

| Setting | Student | Teacher | Gap Recovery | Key Insight |
|---------|---------|---------|-------------|-------------|
| ✅ Successful | R1-Distill-1.5B | JustRL-1.5B (RL-trained) | **~80%** | Compatible thinking + new knowledge |
| ❌ Failing | R1-Distill-1.5B | R1-Distill-7B (same-family) | **~0%** | Same distribution, no new knowledge |
| ❌ Reverse distill | JustRL-1.5B → R1-Distill teachers | **Regresses equally** | Distributional indistinguishability |
| ✅ Cold start rescue | Qwen3-1.7B-SFT → OPD | Qwen3-4B Non-thinking | **Substantial** | Off-policy warmup raises overlap |
| ✅ Prompt selection | R1-Distill-1.5B | JustRL-1.5B + aligned prompts | **Higher ceiling** | Format match boosts initial overlap |

**Key numbers:**
- Successful OPD closes ~80% of teacher-student performance gap
- Overlap ratio: 72% → 91% in successful runs
- Shared top-k tokens concentrate **97-99%** of probability mass
- Response length sweet spot: **3K-7K tokens**（太短学不到，15K+ 则 entropy collapse）

### 4.3 Analysis experiments

- **现象：** Overlap Top-k training = Full Student Top-k performance; Non-Overlap Top-k 显著更差
  **解释（作者）：** OPD 优化是自增强的 — 在 shared token set 上学习进一步扩大 shared set，形成正反馈
  **【标注】** 这解释了为什么初始 overlap 如此重要 — cold start 的理论基础

- **现象：** Teacher reward quality 随 trajectory depth 系统性退化；不稳定性从 suffix 向 prefix 传播
  **解释（作者）：** Teacher 在 student-generated long prefix 上越来越 OOD → 后期 token 的 guidance 不可靠 → 15K+ 时 student entropy collapse
  **【标注】** 这是 OPD 在 long-horizon agent tasks 上的天然瓶颈，需要 hybrid 方案（OPD for short reasoning + RL for trajectory-level）

- **现象：** Failing teacher 提供的 reward globally informative（与 rollout correctness 相关）但 locally unexploitable
  **解释（作者）：** 失败不是信息缺失问题，而是几何问题 — local optimization landscape 无法利用 global signal
  **【标注】** 深刻 insight：teacher 知道对错但无法教会 student，因为它们在 token-level 的 "语言"不同

## 5) Why it matters for our work
- **Teacher 选择原则：** 选 teacher 应优先 "不同训练路径"（如 RL-trained）而非 "更大同家族模型" — 对我们的 OPD pipeline 设计有直接指导
- **Cold start recipe：** Off-policy SFT warmup 可以 rescue failing OPD — 当 overlap ratio 低时必须先做 warm-start
- **长序列限制：** OPD reward 随 depth 退化 → agentic 长轨迹任务不能纯靠 OPD，需要 hybrid（OPD + outcome RL）
- **诊断工具：** Overlap ratio 可作为 OPD 训练的 early-stopping/failure 诊断信号
- **3K-7K sweet spot：** 控制 generation length 在此区间内可最大化 OPD 效果

## 6) Actionable next step
- [ ] 在 OPD 训练中加入 overlap ratio 监控作为 early diagnostic
- [ ] Teacher 选择实验：对比 RL-trained teacher vs same-family larger teacher 的效果
- [ ] 实现 off-policy cold start（SFT on teacher rollouts）作为所有 OPD runs 的默认前置步骤
- [ ] 为 long-horizon agent tasks 设计 hybrid pipeline：OPD (3K-7K context) + outcome RL (trajectory-level)
- [ ] 测试 teacher-aligned prompt templates（match teacher 训练时的 format）
- [ ] 参考实现: https://github.com/thunlp/OPD

## 7) 评分解释
- **质量分 2/2：** THUNLP（Zhiyuan Liu, Ning Ding）顶级 NLP 组；30 pages / 23 figures 的深度系统性研究；clean narrative（phenomenology → mechanism → recipe）；well-controlled experiments + ablations；code released；137 alphaXiv likes
- **Observation 分 2/2：** (1) Thinking-pattern consistency > teacher strength 是非显然发现；(2) 97-99% mass 集中在 shared top-k 揭示了 OPD 的精确机制；(3) Reward degradation with depth 指出 OPD 的天然 scaling limitation；(4) "Globally informative but locally unexploitable" 是对失败本质的深刻刻画
- **总分 5/5**
- **为什么不是更高分：** 已是满分。Minor: 更偏诊断/分析而非提出 fundamentally new algorithm — recipes（cold start, prompt selection）是 insights 的直接应用而非新方法
