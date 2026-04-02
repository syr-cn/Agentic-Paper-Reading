# DNL Deep Note — Unify-Agent

## 0) Metadata
- **Title:** Unify-Agent: Towards Unified Visual Generation and Understanding via Agent
- **Alias:** Unify-Agent
- **Authors / Org:** Shuang Chen, Yi Lu, Yikun Liu, Jieneng Chen, Alan Yuille, Cihang Xie (UCLA, Tencent Hunyuan, CUHK, HKUST)
- **Venue / Status:** arXiv 2603.29620v1 (preprint)
- **Date:** 2026-03-31
- **Links:**
  - Abs: https://arxiv.org/abs/2603.29620
  - HTML: https://arxiv.org/html/2603.29620v1
  - PDF: https://arxiv.org/pdf/2603.29620
- **Tags:** unified vision model, agent framework, visual generation, visual understanding, tool use, multimodal
- **My rating:** ★★★★☆ (4/5)
- **Read depth:** deep
- **Scoring (1+2+1):** 基础 1 + 质量 2 + Observation 1 = **4/5**---

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：** Unify-Agent 用 agent 框架统一视觉生成与理解：一个 MLLM 做"大脑"调度 text-search、image-search、recaption 等工具来增强 prompt，然后调用专用生成器/理解器执行。核心发现：generation 和 understanding 互相增益——VAE decoder 帮助 ViT encoder 学到更好的视觉表征，反之亦然（FactIP 73.2 vs Bagel 50.9，+22.3）。---

## 2) CRGP 拆解 Introduction
### C — Context
- 视觉生成（T2I、editing）和视觉理解（VQA、captioning）长期被当作独立任务研究。
- 近期统一多模态模型（Janus, Bagel, MetaMorph）试图在单一模型内同时处理生成和理解，但性能往往不如各自的专用模型。

### R — Related work
- **统一模型线：** Janus（双 encoder）、Bagel（interleaved generation/understanding）、MetaMorph（token-level mixing）。
- **Agent 系统线：** VisAgent、GEMS 等用 agent 做图像生成，但聚焦于 single-task iterative refinement。
- **Tool-use 线：** Toolformer、ViperGPT 等让 LLM 调用工具，但未深入生成-理解联合优化。

### G — Gap
1. 统一模型的两难：模型越统一，单任务性能越容易被拖累（generation-understanding tradeoff）。
2. 现有 agent 方法只关注生成 OR 理解的一侧，没有利用两者的互补性。
3. 缺乏对 "generation helps understanding" 这一方向的系统性验证。

### P — Proposal
- **Agent 架构：** MLLM（基于 Qwen2.5-VL-72B）作为中央调度器，根据任务类型选择工具链：
  - 生成任务：text-search → image-search → recaption → 调用 FLUX 生成
  - 理解任务：直接推理或调用视觉工具辅助
- **统一训练：** 在 VAE decoder（生成）和 ViT encoder（理解）之间共享中间表征，让两个方向互相增益。
- **工具增强 prompt：** 通过 web search 和 image search 获取参考信息，recaption 重写用户 prompt 以消除歧义。---

## 3) Figure 区

- 图1（Unify-Agent 系统架构）：MLLM 大脑调度 text-search / image-search / recaption 三个工具增强 prompt，然后分发给 generation 模块（FLUX-based）或 understanding 模块（ViT-based）。generation 和 understanding 通过共享 latent space 互相增益。

- 图2（Generation-Understanding Synergy）：VAE decoder 和 ViT encoder 的联合训练示意。生成侧产生的 latent 表征被理解侧复用，反之亦然。---

## 4) Experiments — Key Numbers

### Main Results
| Benchmark | Metric | Unify-Agent | Best Baseline | Delta |
|-----------|--------|-------------|---------------|-------|
| FactIP | Overall | 73.2 | 50.9 (Bagel) | +22.3 |
| FactIP | Relevance | 72.4 | 44.9 (Bagel) | +27.5 |
| WiSE | Score | 0.77 | — | unified MLLM best |
| KiTTEN | Score | 4.08 | 3.50 (Imagen-3) | +0.58, new SOTA |
| T2I-FactBench | SKCM | 69.2 | — | — |

### Ablation (FactIP Overall)
- Full Unify-Agent: 73.2
- w/o text-search: 65.4 (-7.8)
- w/o image-search: 56.2 (-17.0) ← image search 贡献最大
- w/o recaption: 62.9 (-10.3)

### Key Finding: Generation Helps Understanding
- 联合训练后，understanding benchmark（VQA 等）性能也提升
- VAE + ViT synergy: 共享 latent space 让视觉表征更丰富
- 这是论文最有价值的 observation

### Limitations
- 依赖 72B 参数的 Qwen2.5-VL 做调度器，推理成本极高
- FLUX 作为生成后端，无法端到端微调
- Tool-use 的可靠性依赖 MLLM 的 instruction following 能力---

## 5) Why it matters — 对我研究的启发

1. **Generation-Understanding Synergy：** 这是最值得关注的发现。以往认为统一模型会互相拖累，但 Unify-Agent 证明通过 agent 框架解耦执行、共享表征，两者可以互相增益。这对 MemOCR（需要同时理解和生成 layout）有直接启示。
2. **Agent 作为统一接口：** 不同于 Janus/Bagel 等在模型架构层面做统一，Unify-Agent 在 agent 层面做统一——模型可以是异构的，agent 负责调度。这是一种更灵活、更工程友好的统一范式。
3. **Image search 的巨大贡献（-17.0）：** 说明 retrieval 在生成任务中的重要性被严重低估。这和 RAG 在 reasoning 中的角色异曲同工，值得在 agentic generation 研究中深入。
4. **对比 GEMS：** GEMS 聚焦于单任务迭代优化 + memory，Unify-Agent 聚焦于多任务统一 + tool use。两者可以互补——把 GEMS 的 memory 机制加到 Unify-Agent 的迭代流程中。

## 6) Actionable next step

- [ ] 对比 Unify-Agent 和 GEMS 的设计思路，整理一份 "Agentic Visual Generation" mini-survey
- [ ] 关注 generation-understanding synergy 在 layout 理解任务（MemOCR 方向）中的应用可能性
- [ ] 跟踪腾讯混元团队后续工作（Master 正在考虑混元实习，这是他们的核心方向之一）

## 7) 评分解释

**4/5（基础 1 + 质量 2 + Observation 1）**

- 基础 1：完整系统论文，多 benchmark 对比，有消融
- 质量 +2：FactIP +22.3 的大幅领先有说服力，消融设计清晰（三个工具逐一消除），KiTTEN SOTA 结果可信
- Observation +1："generation helps understanding" 的发现打破了统一模型必须 trade-off 的传统认知，对 Master 的多模态 agent 研究方向有直接参考价值
- 扣分项：72B 调度器成本高，缺少轻量化方案探讨；FLUX 后端非端到端可训练