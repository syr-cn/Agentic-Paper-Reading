# DNL Deep Note — Agentic-MME

## 0) Metadata
- **Title:** Agentic-MME: What Agentic Capability Really Brings to Multimodal Intelligence?
- **Alias:** Agentic-MME
- **Authors / Org:** Qianshan Wei, Yishan Yang, Siyi Wang, Jinglin Chen, Binyu Wang, Jiaming Wang, Shuang Chen, Zechen Li, Yang Shi, Yuqi Tang, Weining Wang, Yi Yu, Chaoyou Fu, Qi Li, Yi-Fan Zhang
- **Venue / Status:** arXiv 2604.03016v1 (preprint)
- **Date:** 2026-04-03
- **Links:**
  - Abs: https://arxiv.org/abs/2604.03016
  - HTML: https://arxiv.org/html/2604.03016v1
  - PDF: https://arxiv.org/pdf/2604.03016
  - Code: N/A
- **Tags:** multimodal agents, benchmark, process verification, tool use, visual expansion, knowledge expansion, agentic evaluation
- **My rating:** ★★★★☆ (4/5)
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = **4/5**

---

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：** Agentic-MME 提出首个 **process-verified** 的多模态 Agentic benchmark，包含 418 个真实世界任务和 2000+ 人工标注的 stepwise checkpoints（平均每题 10+ 人时标注），通过 dual-axis（S-axis 审计 Knowledge Expansion，V-axis 审计 Visual Expansion）实现中间过程精细验证，并引入 Overthink metric 量化效率。核心发现：最强模型 Gemini3-pro 整体仅 56.3% 准确率，Level-3 协同任务暴跌至 23.0%，暴露了当前多模态 agent 在视觉-知识协同推理上的巨大差距。

---

## 2) CRGP 拆解 Introduction
### C — Context
- MLLM 正从被动观察者进化为主动 agent，通过 **Visual Expansion**（调用视觉工具裁剪/旋转/增强图像）和 **Knowledge Expansion**（开放网络搜索）解决问题。
- 这一范式转变被称为 **multimodal agentic capability**。

### R — Related work
- **Tool-augmented visual reasoning：** GTA、TIR、RealUnify 等 benchmark 探索了多工具执行和视觉操作，但将 open-web retrieval 视为边缘功能（如 o3/GPT-5 中 google_search 调用占比 <7%），未充分评估 Visual + Knowledge Expansion 的协同。
- **Multimodal search & process-aware evaluation：** MMSearch 系列评估搜索中的视觉集成，但如 CodeV 所指出，仅检查最终答案无法发现 unfaithful tool execution。近期 benchmark 推进了文本溯源追踪，但中间视觉 artifacts 仍未被验证。
- **Deep research frameworks：** MMDeepResearch 等长文报告生成系统的视觉操作局限于预处理（如解析网页截图），缺乏主动视觉操纵工具。

### G — Research gap
1. 现有 benchmark **缺乏灵活统一的工具集成**——visual tools 和 search tools 被割裂评测。
2. **Visual 与 Knowledge Expansion 的协同** largely unexplored——没有设计需要两者深度耦合的 realistic scenarios。
3. **缺乏严格的过程验证**——仅检查 final answer 无法区分失败是感知问题、跳过工具调用、错误执行（裁剪错误区域）还是冗余试错。

### P — Proposal
- **Agentic-MME：** 一个 process-verified 的多模态 Agentic benchmark，通过统一的 sandboxed 执行框架（支持 code generation 和 function-calling 两种模式），跨 6 个领域、3 个难度等级的 418 个真实任务，配合 dual-axis stepwise checkpoints 实现过程级验证。

---

## 3) Figure 区

- 图1（Benchmark Overview & Motivation）：![fig1](https://arxiv.org/html/2604.03016v1/2604.03016v1/x1.png)
  Level-3 协同任务示例：模型需先裁剪模糊 logo → 多跳搜索匹配候选品牌 → 交叉验证。单独使用视觉工具或盲目网络搜索均无法解决，展示了 Visual + Knowledge Expansion 深度耦合的必要性。

- 图2（Data Collection Pipeline）：![fig2](https://arxiv.org/html/2604.03016v1/2604.03016v1/x2.png)
  数据构建流程：Image Sourcing → Model-in-the-Loop Backward Drafting → Granular Step-wise Annotation → Quality Assurance。关键创新是 backward drafting——先让 SOTA 模型描述原图，标注员专攻模型遗漏/幻觉的细节，确保必须通过主动视觉操纵才能获取答案。

- 图3（Dataset Statistics）：![fig3](https://arxiv.org/html/2604.03016v1/2604.03016v1/x3.png)
  覆盖 6 大领域 35 子类别，Level 1→3 的 checkpoint 和 tool call 密度显著递增。超过 40% 实例的关键视觉证据占图像面积 <10%，证实了主动工具操纵的必要性。

- 图4（Fine-Grained Error Analysis）：![fig4](https://arxiv.org/html/2604.03016v1/2604.03016v1/x8.png)
  七种失败模式热力图：**reluctance to act**（被动猜测）占约 50% 错误，**overthinking collapse**（冗余工具调用循环）在强模型中显著，**unfaithful execution**（裁剪错误区域）持续存在。

---

## 4) Experiments
### 4.1 Experimental setup
- **任务/数据：** 418 个真实世界任务，6 个领域（文档、自然场景等），35 子类别，3 个难度等级（L1: 48.6%, L2: 32.1%, L3: 19.4%）
- **模型/agent 配置：** 两种交互模式——Gen（Code Generation，写 Python 执行视觉变换）和 Atm（Atomic，结构化 function-calling API）。工具集包含 13 种视觉操作 + 4 种 web 检索工具。
- **对比基线：** 开源（Qwen3 VL-235B, Qwen3 VL-32B/8B-think, DeepeyesV2, Thyme-RL）+ 闭源（Gemini 3 Pro, Kimi-k2.5, GPT 5.2, GPT-5-mini, Qwen3.5-plus）+ No-tool baseline (Gemini 3 pro-preview)
- **评测指标：** Acc (final answer), S (search checkpoints pass rate), V_tool (是否调用正确视觉工具), V_true (中间视觉 artifact 是否包含正确证据), Overthink (相对于人类轨迹的冗余度)

### 4.2 Main result table
| Setting | Human | Gemini 3 Pro (best) | Qwen3 VL-235B (best open) | No-tool Gemini 3 |
|---|---:|---:|---:|---:|
| Overall Acc | 93.8 | 56.3 | 34.9 | 30.2 |
| Level 1 Acc | 99.0 | 72.1 | 50.0 | 42.9 |
| Level 2 Acc | 92.6 | 47.7 | 30.1 | 24.6 |
| Level 3 Acc | 82.3 | 23.0 | 10.1 | 7.5 |
| Delta (L3 vs Human) | — | -59.3 | -72.2 | -74.8 |

### 4.3 Analysis experiments

- **现象：** 移除所有图像后准确率降至接近零（Gemini 3 Flash: 2.63%; GPT-5-mini: 1.44%）。
  **解释（作者）：** 证实 Agentic-MME 无数据泄漏，每个任务确实需要视觉证据。
  **【标注】：** 这是 benchmark 质量的基本保证，设计合理。

- **现象：** Tool availability ablation 中，Full (Img+Search) 在 L3 上的提升（Qwen3: 7.41% → 19.23%）远超 Image-only（6.25%）和 Search-only（11.11%）的简单加和。
  **解释（作者）：** Super-additive 效应验证了 Level-3 设计——这些任务无法靠单一能力解决，必须两者深度协同。不可靠的视觉工具在没有搜索验证时甚至可能有害（7.41% → 6.25%）。
  **【标注】：** 这个 super-additive 发现非常有价值，为 "synergy" 提供了定量证据。但 L3 样本仅 ~81 题（19.4%），统计 power 可能不足。

- **现象：** Oracle guidance（提供 ground-truth visual cues + stepwise description）大幅提升性能（Gemini 3 Flash: 52.24% → 76.21%），但在 L3 上仍未饱和（51.25%）。
  **解释（作者）：** 即使给出完美蓝图，agent 仍需自主写 API 调用、追踪长 context、避免 error compounding——连续执行远比单步感知困难。
  **【标注】：** 揭示了 "planning vs execution" 的根本性鸿沟，这对 agentic RL 训练很有启发——单纯提升规划能力不够，执行 reliability 才是瓶颈。

- **现象：** 效率分析显示 DeepeyesV2 工具使用不足（OT=0, Acc=22.5%），GPT-5-mini 严重过度探索（12.13 calls/task, Acc=33.5%），Gemini 3 Pro 在效率与准确率间取得最佳平衡。
  **解释（作者）：** 聚焦、可靠的工具执行远比穷举探索重要。
  **【标注】：** Overthink metric 是个好设计。暗示未来 agent 训练需要同时优化 accuracy 和 efficiency（类似 reasoning efficiency 的趋势）。

---

## 5) Why it matters for our work
- **直接关联 agentic memory + multi-modal agent 研究：** 本文的 process-level verification 框架（S-axis + V-axis + Overthink）为我们评估 agentic 系统提供了方法论参考。特别是 Overthink metric 可以借鉴到 memory-augmented agent 的效率评估中——agent 应该用最少的 memory read/write 完成任务。
- **Level-3 synergistic tasks 的设计思路：** 视觉线索 → 搜索验证 → 反馈精炼视觉操作的 hypothesis-verification loop，与 ReMemR1 中的 revisitable memory 机制有精神上的相似——都强调 agent 需要在多步交互中迭代修正而非一次性输出。
- **Error taxonomy 的启发：** "reluctance to act"（被动猜测占 ~50% 错误）和 "overthinking collapse" 两种失败模式，对 agentic RL 训练策略设计有直接参考价值——reward shaping 需要同时鼓励工具使用和惩罚冗余探索。

---

## 6) Actionable next step
- [ ] 研究 Agentic-MME 的 Overthink metric 设计，考虑是否可迁移到 memory-augmented agent 场景（定义 memory-access efficiency 指标）
- [ ] 关注 Level-3 tasks 的 hypothesis-verification loop 范式，思考如何在 RL reward 中编码这种 iterative refinement 行为
- [ ] 等待代码/数据公开后，用 Agentic-MME 评测我们的 multi-modal agent 系统

---

## 7) 评分解释
- **质量分 2/2：** 标注极其扎实（10+ 人时/题），dual-axis process verification 是当前 agentic benchmark 中最精细的；实验设计全面，包含 tool availability ablation、oracle guidance study、efficiency analysis、error taxonomy 等多维诊断。
- **Observation 分 1/2：** super-additive synergy 效应和 planning-execution gap 的发现有价值，但核心贡献是 benchmark 而非新方法/新理论。对我们工作的启发是间接的（evaluation methodology）而非直接可用的技术。
- **总分 4/5：**
- **为什么不是更高分：** 本文定位为 benchmark paper，不提出新的模型或训练方法。L3 样本量偏小（~81 题）可能限制统计可靠性。工具集（13 种视觉操作）的选择和设计合理性未做充分 ablation。对我们的直接 actionable value 有限，更多是评估方法论层面的参考。
