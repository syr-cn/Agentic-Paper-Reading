# Evo-Memory 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory
- **Alias:** Evo-Memory
- **Authors / Org:** Noveen Sachdeva et al.；Google DeepMind × UIUC
- **Venue / Status:** arXiv 2511.20857v1
- **Date:** 2025-11-25
- **Links:**
  - Abs: https://arxiv.org/abs/2511.20857
  - HTML: https://arxiv.org/html/2511.20857v1
  - PDF: https://arxiv.org/pdf/2511.20857
  - Code: (paper states “will release”, link not provided in v1)
- **Tags:** agent-memory, test-time-learning, streaming-benchmark, retrieval, embodied-agent
- **My rating:** ★★★★★（维持原倾向）
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 2 = **5/5**

---

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：** 这篇把 memory 评估从“对话事实召回”升级到“连续任务中的经验复用与演化”，并用统一 benchmark（Evo-Memory）+ 强基线（ExpRAG）+ 强方法（ReMem）给出可复现实验闭环；最关键观察是：多轮任务下收益远大于单轮任务，且效率（steps）显著下降。

---

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- LLM agent 已能推理、调用工具、执行多步任务，但 memory 仍常被当作“被动缓存”。
- 现实 agent 在部署时要面对连续任务流，核心问题是能否从历史交互中学会可迁移策略。

### R — Related work
- Test-time adaptation / self-improvement：Reflexion、Voyager 等强调在线反思。
- Memory 系统：RAG、Mem0、MemOS、workflow/procedural memory 等强调检索与存储机制。
- 现有评测多是静态 recall 或 retention，缺少“检索-整合-演化”一体化比较。

### G — Research gap
- 缺统一流式基准：同时覆盖单轮 reasoning/QA 与多轮 embodied 任务。
- 缺统一协议：不同 memory 方法难以公平比较，尤其在 test-time learning 下。

### P — Proposal
- 提出 **Evo-Memory**：将静态数据重组为任务序列，统一 **Search → Synthesis → Evolve**。
- 实现并评测 10+ memory 模块。
- 提出两类代表方案：
  - **ExpRAG**：轻量经验检索聚合基线；
  - **ReMem**：Think / Act / Refine Memory 三操作循环，显式 memory refinement。

---

## 3) Figure 区（至少 1 张，抓主图，不跳过）
- 图1（问题定义对比）：
  ![fig1](https://arxiv.org/html/2511.20857v1/x1.png)
  解释：对比 conversational recall（记住说过什么）与 experience reuse（记住学到了什么策略），是全文动机核心。

- 图2（ReMem 总览）：
  ![fig2](https://arxiv.org/html/2511.20857v1/x3.png)
  解释：左侧是 test-time evolution 流，右侧是 Think/Act/Refine 三模块，强调 memory 是“可被主动改写”的对象。

- 图3（分析图：相关性）：
  ![fig3](https://arxiv.org/html/2511.20857v1/figures/correlation_side_by_side.png)
  解释：ReMem 相对 History 的收益与任务相似度正相关（Gemini r=0.717；Claude r=0.563），给出“什么时候 memory 更有效”的边界条件。

---

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- **任务/数据：** 共 10 个任务源。
  - 单轮：AIME24, AIME25, GPQA-Diamond, MMLU-Pro(Eco/Eng/Philo), ToolBench
  - 多轮：AlfWorld, BabyAI, PDDL, ScienceWorld（文中另提 Jericho 在 benchmark 描述中）
- **模型/agent 配置：** Gemini-2.5（Flash/Flash-Lite/Pro）与 Claude（3.5-Haiku / 3.7-Sonnet）；主表重点是 Gemini-2.5 Flash 与 Claude-3.7 Sonnet。
- **对比基线：** Baseline, History, ReAct, Amem, SelfRAG, Mem0, MemOS, LangMem, DC-Cu, DC-RS, AWM, ExpRecent, ExpRAG, ReMem。
- **检索配置：** Retriever = **BAAI/bge-base-en-v1.5**，默认 **top-k=4**，统一检索预算与提示长度约束。
- **评测指标：**
  - 单轮：Exact Match，ToolBench API/Acc
  - 多轮：Success(S) / Progress(P)
  - 分析：Step efficiency、Sequence robustness

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 单轮 Avg（Claude-3.7） | 0.54 | ExpRAG 0.59 | **+0.05** |
| 单轮 Avg（Gemini-2.5 Flash） | 0.59 | ReMem 0.65 | **+0.06** |
| 多轮 Avg S/P（Gemini-2.5 Flash） | 0.27 / 0.46 | ReMem 0.50 / 0.64 | **+0.23 / +0.18** |
| 多轮 Avg S/P（Claude-3.7） | 0.24 / 0.52 | ReMem 0.78 / 0.91 | **+0.54 / +0.39** |
| Claude-3.7, AlfWorld S/P | 0.18 / 0.49 | ReMem 0.92 / 0.96 | **+0.74 / +0.47** |
| Gemini-2.5 Flash, ToolBench API/Acc | 0.71 / 0.61 | ReMem 0.85 / 0.71 | **+0.14 / +0.10** |

补充单轮细节（Gemini-2.5 Flash, ReMem）：AIME24 **0.60**，AIME25 **0.53**，GPQA **0.51**，MMLU-Pro(Eco/Eng/Philo)=**0.85/0.46/0.79**。

### 4.3 Analysis experiments（强制“现象+解释”）
- **现象1：** 多轮任务收益明显大于单轮；Claude-3.7 下 ReMem 从 0.24/0.52 到 0.78/0.91。
  **解释（作者）：** 长时任务更依赖可复用程序性经验，memory refine 能累积优势。
  **【标注】（我的判断）：** 这说明 memory 的真实价值在“减少重复试错”，而不只是提升一次性答题准确率。

- **现象2：** ExpRAG 作为轻量方法非常强，在 Claude 单轮 Avg 上甚至优于 ReMem（0.59 vs 0.58）。
  **解释（作者）：** 任务级经验检索本身已带来强迁移，复杂机制并非总是必要。
  **【标注】（我的判断）：** 对工程落地是好消息：先做“经验粒度 + 检索质量”，再做复杂 controller。

- **现象3：** 收益与任务相似度显著相关（Gemini r=0.717，Claude r=0.563）。
  **解释（作者）：** 结构重复度高的任务更容易复用历史策略。
  **【标注】（我的判断）：** 如果目标场景高度异质，必须加更强路由/去噪，否则 memory 可能变噪声库。

- **现象4：** Step efficiency 显著改善，例如 AlfWorld 平均步数 **22.6 → 11.5**。
  **解释（作者）：** ReMem 的反思与重组让 action 更聚焦。
  **【标注】（我的判断）：** 这条比“分数+1~2点”更关键，直接关联真实推理成本和延迟。

- **现象5：** 混合成功/失败经验时，多数基线退化，ReMem 仍稳定（Table 4）。
  **解释（作者）：** naive 累积失败样本会污染检索；refine 可缓解。
  **【标注】（我的判断）：** failure memory 不是不能存，而是必须带触发条件与可解释标签。

#### Case（>=2）
- **Case 1（高相似任务，收益放大）：AlfWorld / PDDL**
  - 现象：Claude-3.7 上 ReMem 在 AlfWorld 达到 **0.92/0.96**，PDDL 达到 **0.83/0.95**。
  - 解释：任务结构重复、可复用子策略多，经验演化更容易形成“模板化解法”。

- **Case 2（低相似/高多样任务，收益受限）：AIME25 / GPQA**
  - 现象：单轮提升相对温和，且跨方法差距没有多轮大。
  - 解释：题目分布更异质，直接复用历史轨迹的收益小，memory 更依赖高质量抽象而非原样检索。

---

## 5) Why it matters for our work
- 对 **agentic memory**：提供了可复用的统一评估协议，尤其是 S/P + step + sequence robustness 的组合指标。
- 对 **long-context reasoning**：再次验证“长上下文 ≠ 长期学习”；关键是经验单元如何演化、被检索、被重组。
- 对 **tool-use / embodied agents**：Think-Act-Refine 可迁移到技能库更新、失败归因和在线策略压缩。

---

## 6) Actionable next step
- [ ] 先复刻 **ExpRAG**（任务级经验模板 + bge 检索 + top-k=4），作为统一低成本基线。
- [ ] 在现有 agent loop 里加入 **Refine**（去噪、合并、失败标签化），对比 S/P、steps、token cost。
- [ ] 做“**相似度-收益曲线**”诊断：若相关性弱，优先优化 memory routing，而非扩大 context window。

---

## 7) 评分解释（必填）
- **质量分 2/2：** 问题定义清晰、benchmark + 方法 + 分析一体化，且给出跨任务/跨模型证据。
- **Observation 分 2/2：** 除主结果外，提供了相似度相关性、步数效率、失败记忆鲁棒性等可落地洞察。
- **总分 5/5：** 基础 1 + 质量 2 + Observation 2。
- **为什么不是更高分：** 评分上限就是 5；若按更细粒度审稿标准，仍希望看到更多成本统计（token/latency）与跨实现细节的完全开源对齐。