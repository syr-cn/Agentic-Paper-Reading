# Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes

## 0) Metadata
- **Title:** Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes
- **Alias:** revisiting-opd
- **Authors / Org:** Yuqian Fu*, Haohuan Huang*, Kaiwen Jiang, Jiacai Liu, Zhuo Jiang, Yuanheng Zhu†, Dongbin Zhao; CASIA (State Key Lab of Multimodal AI Systems) + UCAS + Fudan University
- **Venue / Status:** arXiv 2603.25562 (work in progress)
- **Date:** 2026-03-26 (v1), 2026-04-27 (v2)
- **Links:**
  - Abs: https://arxiv.org/abs/2603.25562
  - HTML: https://arxiv.org/html/2603.25562v2
  - PDF: https://arxiv.org/pdf/2603.25562
  - alphaXiv: https://www.alphaxiv.org/overview/2603.25562
  - Code: https://github.com/hhh675597/revisiting_opd
- **Tags:** on-policy-distillation, failure-modes, reverse-KL, tokenizer-mismatch, local-support-matching, top-K-truncation
- **My rating:** ⭐⭐⭐⭐
- **Read depth:** deep
- **Type:** C (Benchmark/Analysis + Practical Fix)
- **Relevance:** 4/5 (OPD 领域直接诊断性工作)
- **Quality:** 4/5
- **Community:** alphaXiv likes: 124 / HF upvotes: N/A
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 2 = 5

## 1) 一句话 Why-read
- **Key claim:** 系统性诊断 sampled-token OPD 的三个失败模式（信号不平衡、OOD prefix 上教师不可靠、tokenizer 不匹配），用 Teacher Top-K Local Support Matching (LSM) + top-p + mask 获得 +19.8% 提升。
- **Key observation:** Token-level OPD 是 sequence-level reverse-KL 的有偏估计；但有偏的 variance 是 O(T²) vs O(T⁴) — bias-variance tradeoff 解释了为什么 token-level 仍然实用。

## 2) CRGP 拆解 Introduction
### C — Context
- OPD 已成为 LLM post-training 标配（Qwen3, MiMo-V2, GLM-5 均使用）
- 标准实现将 distribution matching 简化为 sampled-token log-ratio
- Token-level reverse-KL 比 sequence-level 方差更优但有 bias

### R — Related work
- Off-policy KD (SeqKD) → distribution mismatch
- On-policy KD (GKD, MiniLLM, DistillSpec) → student 采样 + teacher supervision
- 已有工作报告 repetition、entropy collapse 等问题但缺乏系统诊断

### G — Research gap
- 没有系统性诊断 OPD **为什么失败**
- 三个盲区：(1) Teacher 在 student prefix 上的 degradation 未量化；(2) TopK + Reverse KL 的 gradient bias 未理论分析；(3) Tokenizer mismatch 的影响未形式化

### P — Proposal
- 系统性 empirical study → 识别 3 个 failure mechanisms
- 提出 LSM = truncated reverse-KL over teacher's top-K tokens (with renormalization) + top-p rollout sampling + special-token masking
- Math reasoning + agentic 多任务上 +19.8% 性能提升

## 3) Figure 区

![Figure 1: Overview](https://arxiv.org/html/2603.25562v2/x2.png)

**Figure 1:** 左侧展示 standard sampled-token OPD pipeline，右侧展示 3 个 failure modes 的诊断图示 — imbalanced reward distribution（大部分 token 获得负 reward）和 teacher 在 OOD prefix 上的不可靠性。

![Figure 2: Failure Mode Details](https://arxiv.org/html/2603.25562v2/x3.png)

**Figure 2:** 具体案例：(1) reward 分布严重偏负；(2) teacher 对 repetitive/meaningless text 仍给高概率；(3) `<|endoftext|>` 被拆分为多 token 导致 mismatch。

## 4) Experiments

### 4.1 Experimental setup
- **Student:** Qwen2.5-7B-Instruct（主实验），Qwen2.5-1.5B-Instruct（WebShop）
- **Teacher:** OpenThinker3-7B（math），GiGPO-Qwen2.5-7B-It-ALFWorld（agentic）
- **Benchmarks:** MATH500, AIME24, AIME25, Minerva, OlympiadBench（reasoning）; ALFWorld（agentic）; WebShop
- **Hyperparams:** K=32, top-p=0.9, lr=2e-6, batch=128, 400 steps

### 4.2 Main result table

**Single-task Math (Table 1):**

| Method | MATH500 | AIME24 | AIME25 | Minerva | OlympiadBench | **Avg.** |
|--------|---------|--------|--------|---------|---------------|----------|
| Qwen2.5-7B-It (baseline) | 68.2 | 13.3 | 0.0 | 26.5 | 32.9 | **28.2** |
| OpenThinker3-7B (teacher) | 92.2 | 53.3 | 40.0 | 39.0 | 55.6 | **56.0** |
| Sampled-token OPD | 80.0 | 10.0 | 16.7 | 32.4 | 43.1 | **36.4** |
| **Ours (LSM) w/o mask** | 80.4 | 23.3 | 26.7 | 34.2 | 43.9 | **41.7** |

**Delta:** LSM vs sampled-token OPD = **+5.3 avg** (+14.6% relative)

**Multi-task (Table 2):**

| Method | ALFWorld | Math Avg. |
|--------|----------|-----------|
| Sampled-token OPD | 90.6 | 34.8 |
| **Ours (LSM)** | 95.3 | **41.7** |

**Delta:** +19.8% math gain，ALFWorld 持平/略升

**WebShop (Qwen2.5-1.5B):**

| Method | Task Score | Success Rate |
|--------|-----------|--------------|
| Sampled-token OPD | 73.0 | 50.0% |
| **Ours (LSM)** | 75.1 | **57.8%** |

**Delta:** +7.8 pp success rate

### 4.3 Analysis experiments

- **现象：** Renormalization 是关键 — 移除后 optimization collapse
  **解释（作者）：** Top-K 截断后不 renormalize 会导致 distribution 不 sum-to-1，梯度方向错误
  **【标注】** 这是个容易被忽略的实现细节，任何做 top-K distillation 的人都需要注意

- **现象：** Top-p sampling 将 weak top-K 变成 strong config
  **解释（作者）：** Top-p 约束 student rollout 质量 → teacher 在更合理的 prefix 上更可靠

- **现象：** Multi-task 下 alternative variants（student top-K, EMA-PG）在 math 上大幅退化
  **解释（作者）：** Teacher top-K 提供稳定的 support set；student top-K 在训练中漂移，EMA-PG 的 moving average 在 multi-task 中 noisy

## 5) Why it matters for our work
- **即用型 OPD recipe：** LSM + top-p + mask 三件套可直接套用到任何 on-policy distillation pipeline
- **Tokenizer mismatch awareness：** 跨模型蒸馏时 special-token masking 是必须项
- **Variance 分析框架：** Token-level O(T²) vs Sequence-level O(T⁴) 为选择 distillation granularity 提供理论指导
- **Multi-task 稳定性：** LSM 在 agentic + reasoning 交替训练中更稳定，直接参考价值

## 6) Actionable next step
- [ ] 在现有 OPD pipeline 中实现 top-K renormalized reverse-KL（K=32）替换 sampled-token log-ratio
- [ ] 为 cross-tokenizer 蒸馏添加 special-token mask
- [ ] Rollout sampling 从 temperature 切换为 top-p=0.9
- [ ] 参考实现: https://github.com/hhh675597/revisiting_opd

## 7) 评分解释
- **质量分 2/2：** 3 个 failure mode 诊断系统性强；理论 bias-variance 分析 solid；实验覆盖 reasoning + agentic + 小模型；ablation 充分；代码开源
- **Observation 分 2/2：** "Teacher top-K local support matching" 是 non-obvious insight（用 teacher 的 top-K 做 support set 而非 full vocab 或 sampled token）；renormalization trick 关键且容易被忽略；multi-task 下其他 variant 大幅退化的发现有实践价值
- **总分 5/5**
- **为什么不是更高分：** 已是满分。Minor: 规模有限（7B student only）；work in progress 状态；LSM 的理论最优性未证明
