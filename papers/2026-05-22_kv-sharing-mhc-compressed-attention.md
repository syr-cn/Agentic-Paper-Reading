# KV Sharing, mHC & Compressed Attention 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention
- **Alias:** KV-Sharing-mHC-CompressedAttn
- **Authors / Org:** Sebastian Raschka, PhD (Ahead of AI / Lightning AI)
- **Venue / Status:** Substack 技术博客（Ahead of AI）
- **Date:** 2026-05-16
- **Links:**
  - Blog: https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures
  - LLM Architecture Gallery: https://sebastianraschka.com/llm-architecture-gallery/
  - Code (Gemma 4 from scratch): referenced in blog
- **Tags:** long-context, KV-cache, attention-efficiency, architecture-survey, MoE, compressed-attention
- **My rating:** ★★★★☆
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = **4/5**

| Dimension | Score | Reason |
|---|---|---|
| Type | B (Harness Engineering / Survey) | 综述+可视化解读，非原创方法 |
| Relevance | 4/5 | 直接关联 long-context efficiency，对 agentic memory 系统的底层推理成本有直接影响 |
| Quality | 4/5 | 可视化极佳、技术准确、覆盖全面；但作为综述无独立实验验证 |

---

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：** 2026 年 4-5 月的 open-weight LLM（Gemma 4, Laguna XS.2, ZAYA1-8B, DeepSeek V4）全部将架构改进聚焦在 long-context inference efficiency——KV cache 压缩、注意力预算分配、序列维度压缩成为新共识；核心观察是 **transformer block 正在定向进化为"长上下文特化引擎"**，而质量提升主要由数据和训练 recipe 驱动。

---

## 2) CRGP 拆解 Introduction
### C — Context
- Reasoning model 和 agent workflow 持续增加上下文长度需求，KV-cache 大小、内存带宽、注意力计算成本成为主要瓶颈。
- 2026 年 4-5 月密集发布 open-weight LLM：Gemma 4, Qwen3.6, Laguna XS.2, ZAYA1-8B, DeepSeek V4。

### R — Related work
- GQA/MQA（已被广泛采用）减少 KV head 数量。
- MLA（DeepSeek V2/V3）将 KV 投影到低维 latent space 减少 per-token cache。
- Sliding-window attention（Mistral 系列）限制局部注意力范围。
- DeepSeek Sparse Attention (DSA) 稀疏选择历史 block。

### G — Research gap
- 单一技巧（GQA/MLA/sliding-window）各有局限，长上下文下仍不够。
- 尚无综合视角将 2026 Q2 的多条架构线索串联在一起分析 trade-off。

### P — Proposal
- 博文从四个模型中提炼四类 **互补** 的长上下文架构设计：
  1. Cross-layer KV sharing（序列维度不变，cache 层数减半）
  2. Per-layer attention budgeting（按层分配 query head 数）
  3. Compressed Convolutional Attention（在压缩 latent space 内做 attention）
  4. mHC + CSA/HCA（残差流加宽 + 序列维度压缩）

---

## 3) Figure 区

- 图1（架构总览）：
  ![fig1](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2026-05-16-architecture-overview.png)
  解释：2026年4-5月 open-weight 模型架构对比图，虚线框标出本文详细讨论的模型。所有模型都在注意力或 KV cache 层面引入了新设计。

- 图2（CCA vs MLA）：
  文中 Figure 13 对比 MLA 和 CCA 的信息流差异：MLA 在原始空间做 attention、用 latent 存 cache；CCA 直接在 compressed space 做 attention + conv mixing，同时压缩 FLOPs 和 cache。

- 图3（CSA/HCA 对比）：
  文中 Figure 21-22 展示 DeepSeek V4 的两种压缩注意力：CSA（4x 压缩 + sparse top-k 选择）和 HCA（128x 压缩 + dense attention），二者互补交替。

---

## 4) Experiments
### 4.1 核心数字（来自各原始论文，博文汇总）

| Model/Technique | Metric | Value | Comparison |
|---|---|---|---|
| Gemma 4 E2B KV sharing | KV cache saving @128K | −2.7 GB (bfloat16) | vs. 无 sharing 的同架构 |
| Gemma 4 E4B KV sharing | KV cache saving @128K | −6 GB | 同上 |
| ZAYA1 CCA vs MLA | Perplexity | CCA < MLA | 同等压缩率下（CCA 论文报告） |
| DeepSeek V4-Pro @1M context | Inference FLOPs | 27% of V3.2 | vs. MLA + DSA |
| DeepSeek V4-Pro @1M context | KV cache size | 10% of V3.2 | 同上 |
| DeepSeek V4-Flash @1M context | Inference FLOPs | 10% of V3.2 | 同上 |
| DeepSeek V4-Flash @1M context | KV cache size | 7% of V3.2 | 同上 |
| mHC training overhead | Extra training time | +6.7% | n=4 streams, 27B model |

### 4.2 Analysis
- **现象：** DeepSeek V4 的 CSA/HCA 在 1M token 下将 KV cache 压到 V3.2 的 7-10%，但全文无消融实验分离 CSA/HCA 各自贡献。
  **解释（作者）：** 结果来自完整 recipe（数据+Muon optimizer+mHC+精度优化），无法归因到单一架构改动。
  **【标注】** 这是 DeepSeek 论文的老毛病——系统性结果强但可归因性差。对于想复现特定模块的研究者不友好。

- **现象：** CCA 在 compressed space 做 attention，conv mixing 只加在 Q/K 上而不加 V。
  **解释（作者）：** Q/K 决定 attention score 分布，V 是被平均的内容——压缩 Q/K 后需要用 conv 补偿表达力损失，V 不需要。
  **【标注】** 这是一个优雅的设计选择。conv on Q/K 成本极低但能显著恢复压缩后的 attention 质量。

- **现象：** mHC 的 Res Mapping 投影到 doubly stochastic 矩阵（行列和=1、非负），训练仅增加 6.7% 时间。
  **解释（作者）：** 约束防止深层模型中残差流信号的不可控放大/衰减。
  **【标注】** 类比 normalization 的思路——用数学约束换稳定性，而不是靠 LayerNorm 后补。如果这在更多模型上被验证有效，可能成为 residual design 的新范式。

---

## 5) Why it matters for our work
1. **Agentic memory 的底层成本约束**：agent 持续累积上下文→推理成本线性/二次增长。CSA/HCA 这类序列维度压缩直接决定了 agent 能"记住"多少 step 的历史。
2. **Memory system 设计启示**：如果架构层已经在做"历史压缩+稀疏选择"，那么 explicit memory module（如 Evo-Memory 的 retrieval）和 implicit architecture-level compression 形成互补——值得探索让 memory retrieval 与 attention sparsity pattern 对齐。
3. **Long-context eval 的 hardware-aware 视角**：做 memory/long-context benchmark 时，不能只看 accuracy，还要考虑不同架构下的实际推理成本差异（V4 @1M 仅用 V3.2 的 10% FLOPs，这意味着"同预算下能处理更长上下文"）。

---

## 6) Actionable next step
- [ ] 精读 DeepSeek V4 原始技术报告中 CSA/HCA 的具体实现细节，评估是否可用于 memory-augmented agent 的 KV 管理
- [ ] 关注 CCA 论文（arXiv 2510.04476）的后续实验，看 compressed-space attention 是否对 retrieval-heavy task 有特殊优势
- [ ] 跟踪 mHC 是否被其他团队复用——如果验证有效，可考虑在 memory agent 的 backbone 选型中优先选用 mHC 架构

---

## 7) 评分解释
- **质量分 2/2：** Raschka 的可视化和解释一贯高质量，架构对比清晰准确，涵盖四个模型的核心创新点。作为综述博文，信息密度和可读性都很高。
- **Observation 分 1/2：** 虽然串联了四条技术线索并给出"长上下文特化"的 meta-observation，但本身无实验验证，也没有提出新的 insight（如哪种方法在哪种场景更优）。属于高质量信息整合，但缺少创造性分析。
- **总分 4/5**
- **为什么不是更高分：** 纯综述无原创实验，DeepSeek V4 部分缺消融数据（这是原论文的问题，但博文也没有做补充分析），CCA 的实际大规模验证尚不充分。
