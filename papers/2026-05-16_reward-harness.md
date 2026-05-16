# DNL Deep Note — RewardHarness

## 0) Metadata
- **Title:** RewardHarness: Self-Evolving Agentic Post-Training
- **Alias:** RewardHarness
- **Authors / Org:** Yuxuan Zhang, Penghui Du, Bo Li, Cong Wei, Junwen Miao et al. (UBC, Vector Institute, Kolors/Kuaishou, CMU, U Waterloo, Etude AI, THU, Georgia Tech)
- **Venue / Status:** arXiv preprint
- **Date:** 2026-05-09
- **Links:**
  - Abs: https://arxiv.org/abs/2605.08703
  - HTML: https://arxiv.org/html/2605.08703
  - PDF: https://arxiv.org/pdf/2605.08703
  - Code: https://github.com/TIGER-AI-Lab/RewardHarness
  - Project: https://rewardharness.com
- **Tags:** reward-modeling, agentic, self-evolving, image-editing, GRPO, context-evolution, skills-tools-library
- **Type:** B (Harness Engineering) — reward modeling reframed as context/library evolution, not weight optimization
- **Relevance:** 4/5 — self-evolving agentic framework 范式与 Master 的 agentic self-evolving 方向强相关，但 domain 限于 image editing
- **Quality:** 4/5
- **Why Not Higher:** 只在 image editing 验证，generality 未证明；Orchestrator 依赖 Claude (proprietary)；K=4 accuracy 仍很低 (13.5%)

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：** 把 reward modeling 从 "200K pairs 训权重" 变成 "100 demos evolve Skills+Tools library"；frozen 7B Sub-Agent + evolved library 超 GPT-5 +5.3pts，0.05% 数据量。

## 2) CRGP 拆解 Introduction
### C — Context
- Image editing evaluation 是 RL for visual generation 的瓶颈；现有 reward model 需要 large-scale preference annotation + dedicated training

### R — Related work
- EditReward (trained RM on 200K pairs), GPT-4o/5 as judge, GenAI-Bench, GRPO for diffusion models

### G — Research gap
- Data-efficiency gap：humans infer criteria from few examples, models need 200K comparisons；trained RMs opaque、inflexible、expensive to adapt

### P — Proposal
- Context evolution paradigm：maintain external Skills & Tools library，evolve from 100 demos via Orchestrator analysis；no weight updates, interpretable, portable

## 3) Figure 区

- 图1（Paradigm Comparison）：![fig1](https://arxiv.org/html/2605.08703v1/x1.png)
  传统: large-scale annotation → train RM → RL。RewardHarness: 100 demos → self-evolve Skills+Tools Library → interpretable reward。核心: externalize evaluation knowledge as readable artifacts。

- 图2（Self-Evolution Pipeline）：![fig2](https://arxiv.org/html/2605.08703v1/x2.png)
  Multimodal inputs → Orchestrator routes Skills/Tools → frozen Sub-Agent builds reasoning chain → scores vs GT → Orchestrator analyzes chains → library update (gated on validation accuracy)。

- 图3（Evolution Dynamics）：![fig3](https://arxiv.org/html/2605.08703v1/figures/analysis_evolution.png)
  7 iterations, library grows to 13 entries, pruning begins ~iter 50, final library = 7 entries (3S+4T) at validation acc 62.5%。

## 4) Experiments
### 4.1 Experimental setup
- **任务/数据：** EditReward-Bench (K=2/3/4 ranking accuracy), GenAI-Bench
- **模型/agent 配置：** Sub-Agents: Qwen2.5-VL-7B (frozen, vLLM), Gemini-2.0-Flash; Orchestrator: Claude
- **对比基线：** GPT-4o, GPT-5, Gemini-2.5-Flash, EditReward (trained RM)
- **评测指标：** K=2/3/4 ranking accuracy, GenAI-Bench correlation; downstream GRPO on ImgEdit-Bench

### 4.2 Main result table
| Method | K=2 | K=3 | K=4 | GenAI | **Avg** |
|---|---:|---:|---:|---:|---:|
| GPT-4o | 45.7 | 27.3 | 7.3 | 53.5 | 33.5 |
| GPT-5 | 57.5 | 38.5 | 12.8 | 59.6 | 42.1 |
| Qwen2.5-VL-7B (bare) | 52.7 | 24.7 | 3.4 | 40.5 | 30.3 |
| EditReward (MiMo) | 56.5 | 42.7 | 11.5 | 65.7 | 44.1 |
| **RewardHarness (Qwen)** | 57.9 | **46.7** | 10.8 | **67.5** | **45.7** |
| **RewardHarness (Gemini)** | **66.2** | 45.3 | **13.5** | 64.4 | **47.4** |

Key Δ: RewardHarness (Gemini) vs GPT-5 = **+5.3 avg**; vs bare Qwen = **+15.4**

**Downstream GRPO (ImgEdit-Bench Overall):**
| Method | Score |
|---|---:|
| FLUX.2-klein-base-4B | 3.32 |
| +RL (EditReward) | 3.45 |
| +RL (RewardHarness) | **3.52** |

### 4.3 Analysis experiments
- **现象：** Context evolution 让 Qwen 30.3→45.7 (+15.4)，no weight update
  **解释（作者）：** Skills+Tools injection 为 frozen model 提供了 evaluation rubrics + specialized analysis tools
  **【标注】** 极端 data-efficient: 100 demos (0.05% of 200K) 就达到 SOTA

- **现象：** Library pruning phase (iter 50+) acc 从 52.5% 跳到 62.5%
  **解释（作者）：** 移除 unhelpful entries 减少 routing confusion；quality > quantity for library
  **【标注】** Self-evolving 不是只加不减，pruning 是关键机制

- **现象：** Same evolution procedure works for Qwen 和 Gemini
  **解释（作者）：** Library 是 backbone-agnostic 的 readable artifacts — portability 是 context evolution vs weight training 的本质优势

## 5) Why it matters for our work
- **Context evolution 替代 fine-tuning**：这个 paradigm 可 generalize 到任何 evaluation/judge task
- **Self-evolving library pattern**：Orchestrator + frozen executor + iterative library refinement 是 general agentic pattern
- **Few-shot alignment**：100 demos 就能 align to human preferences — low-resource domains 极有价值
- **Agentic reward signal for RL**：证明 agentic systems 可产出 GRPO-compatible scalar rewards 且优于 trained RM

## 6) Actionable next step
- [ ] 将 Skills+Tools library evolution pattern 应用到 code/text evaluation domain
- [ ] 比较 library-based reward (no training) vs LoRA RM fine-tuning 的 data efficiency tradeoff
- [ ] 实现 validation-gated self-evolution loop（reject bad proposals）作为通用 agentic evaluation pipeline

## 7) 评分解释
- **质量分 1.8/2：** 实验扎实，paradigm novel，Table 1/2 数字 convincing，但 Orchestrator 用 Claude 是 hidden cost
- **Observation 分 1.7/2：** "context evolution not weight optimization" 是 clean insight；library pruning dynamics 有趣；但 domain narrow
- **总分 4/5：** 基础 1 + 质量 1.8 + Observation 1.7 ≈ 4
- **为什么不是更高分：** (1) 只在 image editing 验证 (2) Orchestrator 依赖 proprietary Claude (3) K=4 仍很低 (4) GRPO improvement 仅 +0.07 over EditReward
