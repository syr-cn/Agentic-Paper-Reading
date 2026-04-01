# DNL Deep Note — FS-Researcher

## 0) Metadata
- **Title:** FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents
- **Alias:** FS-Researcher
- **Authors / Org:** Chiwei Zhu, Benfeng Xu, Mingxuan Du, Shaohan Wang, Xiaorui Wang, Zhendong Mao, Yongdong Zhang（USTC / Metastone Technology）
- **Venue / Status:** arXiv 2602.01566v1（preprint）
- **Date:** 2026-02-03
- **Links:**
  - Abs: https://arxiv.org/abs/2602.01566
  - HTML: https://arxiv.org/html/2602.01566v1
  - PDF: https://arxiv.org/pdf/2602.01566
  - Code: (anonymously open-sourced, link TBD)
- **Tags:** deep research, file-system agent, test-time scaling, dual-agent, knowledge base, long-horizon
- **My rating:** ★★★★☆（4/5）
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = **4/5**

---

## 1) 一句话 Why-read
- **Key claim/contribution + key observation：** FS-Researcher 用文件系统作为持久化外部记忆和跨 agent 协调媒介，将 deep research 拆成 Context Builder（建知识库）+ Report Writer（写报告）两阶段，突破 context window 限制，实现 test-time scaling：Context Builder 投入越多轮次，报告质量越高。

---

## 2) CRGP 拆解 Introduction
### C — Context
- Deep research 是 LLM agent 的代表性长程任务，需要大规模信息搜集与综合分析。
- 现有方法（OpenAI/Gemini/Claude DeepResearch）的长轨迹常超出 context window，压缩了证据搜集和报告写作的 token 预算。

### R — Related work
- **商业方案：** OpenAI-DeepResearch、Gemini-2.5-Pro-DeepResearch、Claude-DeepResearch。
- **开源方案：** LangChain-Open-Deep-Research、WebWeaver（dual-agent planner+writer）、RhinoInsight、EnterpriseDeepResearch。
- 这些方案要么在单一 context 内完成所有工作，要么缺乏持久化的结构化知识库。

### G — Gap
1. 长轨迹超出 context window 后，token 预算被压缩，证据搜集和报告写作互相挤占。
2. 缺乏持久化工作区使得跨 session 的迭代精炼困难，中间产物（计划、错误日志）无法持久保存和重访。
3. 现有 test-time scaling 研究主要针对推理任务，在 agent 长程任务上的 scaling 规律尚未充分探索。

### P — Proposal
- **文件系统作为持久化工作区：** 信息存储远超 context window，按需访问不会 context overflow。
- **双 agent 架构：** Context Builder（图书管理员）浏览网络、写结构化笔记、归档原始源到层次化知识库；Report Writer 逐章节编写报告，以知识库为唯一事实来源。
- **工作区控制文件：** index.md（KB 目录 + checklist）、log 文件，实现任务状态感知和迭代精炼。

---

## 3) Figure 区

- 图1（文件系统范式对比）：

![fig1](https://arxiv.org/html/2602.01566v1/x1.png)

  解释：对比三种 agent 范式——(a) 传统 context-based（所有信息塞在 context 里），(b) 工具增强（用 RAG/搜索但无持久化），(c) FS-Researcher 的文件系统范式（持久化工作区 + 层次化知识库）。文件系统范式让信息存储脱离 context window 限制。

- 图2（整体框架）：

![fig2](https://arxiv.org/html/2602.01566v1/x2.png)

  解释：左侧 Context Builder 浏览网页、构建 index.md + knowledge_base/ + sources/ 三层结构；右侧 Report Writer 从知识库按需读取、逐章节生成 report.md。两个 agent 共享同一工作区。

---

## 4) Experiments
### 4.1 Experimental setup
- **基准：** DeepResearch Bench（PhD 级学术查询）+ DeepConsult（真实咨询请求）。
- **评测指标：**
  - RACE（Reference-based Adaptive Criteria-driven Evaluation）：4 维度——Comprehensiveness、Insight/Depth、Instruction-Following、Readability。
  - FACT：Effective Citations (Eff. c.) + Citation Accuracy (C.acc.)。
  - DeepConsult：pairwise win/tie/lose + 平均分。
- **骨干模型：** Claude-Sonnet-4.5、GPT-5。
- **Context Builder 预算：** 默认 3 轮，scaling 实验测试 3/5/10 轮。
- **Report Writer：** 无轮次限制。
- **对比基线：** OpenAI-DeepResearch、Gemini-2.5-Pro-DeepResearch、Claude-DeepResearch、LangChain-Open-Deep-Research、WebWeaver、RhinoInsight、EnterpriseDeepResearch 等。
- **工具集：** 文件系统工具（ls、grep、read_file、insert/delete/replace）+ 网络浏览工具（search_web、read_webpage）。

### 4.2 Main result table
#### DeepResearch Bench (RACE score)
| Method | Backbone | RACE | Comp. | Insight | Instr. | Read. |
|---|---|---:|---:|---:|---:|---:|
| Gemini-2.5-Pro-DeepResearch | Gemini | 49.51 | 49.45 | 50.12 | 50.00 | 49.71 |
| RhinoInsight | - | 50.92 | - | - | - | - |
| WebWeaver | Qwen3-235B | 50.80 | 51.39 | 50.26 | 48.98 | - |
| LangChain-Open-DR | GPT-5 | 50.06 | 50.76 | 51.31 | 49.72 | 50.60 |
| **FS-Researcher** | GPT-5 | **52.22** | - | - | - | - |
| **FS-Researcher** | Claude-4.5 | **53.94** | +3.74 best | +4.4 best | competitive | competitive |

Delta vs RhinoInsight (prev SOTA): **+3.02 RACE**
Delta vs LangChain (same GPT-5): **+2.16 RACE**

#### DeepConsult (Claude-Sonnet-4.5)
| Metric | Value |
|---|---|
| Win rate | **80.00%** |
| Avg score | **8.33** |
| Loss rate | 9.58% |

### 4.3 Analysis experiments
- **现象1：** 移除持久化工作区后，RACE 从 52.76 降到 48.69（-4.07），其中 Insight 降幅最大（-7.95）。
  **解释（作者）：** 没有显式任务状态和结构化知识库，agent 难以识别信息空白、整合证据、跨迭代精炼假说。
  **【标注】：** 工作区对"深度"的贡献远大于对"格式"的贡献——Instruction Following 和 Readability 降幅小得多。

- **现象2：** 合并为单 agent 后，RACE 从 52.76 暴降到 42.41（-10.35），Insight -16.89，Comp. -11.06。
  **解释（作者）：** 单 agent 必须在同一 session 里同时搜集证据和写报告，导致 premature synthesis——还没搜集够就开始写，context 被浏览和写作互相挤占。
  **【标注】：** 这是本文最有说服力的消融。证明"分离搜集与写作"不是工程偏好，而是性能关键。

- **现象3：** Context Builder 轮次从 3→5→10，报告质量持续提升，LLM 成本从 6.10→8.16→12.54 $/query。
  **解释（作者）：** 更多 test-time compute 投入到知识库构建，质量正相关，验证了文件系统范式下的 test-time scaling。
  **【标注】：** 成本翻倍但质量增益的边际递减情况未详细报告，这是一个遗留问题。

---

## 5) Why it matters for our work
- **Agent memory 设计：** FS-Researcher 的文件系统 = 持久化外部记忆，index.md = 工作记忆的结构化索引。这与 ReMemR1 的"可重访记忆"理念高度一致——关键不是记住所有东西，而是按需检索 + 结构化组织。
- **Long-context agent：** 证明了"把信息从 context 卸载到外部存储"在长程任务上的显著优势。对 MemOCR 的启发：OCR 结果也可以用类似的层次化文件系统来组织，而非全塞进 context。
- **Test-time scaling for agents：** 不是简单的 majority voting / best-of-N，而是通过迭代精炼知识库来 scale——更接近人类做研究的方式。

---

## 6) Actionable next step
- [ ] 在 agentic memory 项目中实验"文件系统作为外部记忆"的范式，对比 context-based memory vs file-based memory 在长程任务上的表现差异。
- [ ] 借鉴 Context Builder 的 checklist + iterative refinement 机制，在 agent 训练中引入"自查→补漏→再搜集"的循环。
- [ ] 研究 test-time scaling 在 agent memory 场景的表现：更多 compute 投入记忆构建/检索是否持续提升下游任务表现？

---

## 7) 评分解释
- **质量分 2/2：** 双 agent 框架设计清晰，实验覆盖两个基准多个骨干模型，消融实验有说服力（尤其单 agent 消融 -10.35 RACE）。
- **Observation 分 1/2：** "文件系统作为 agent 外部记忆"的范式启发强，但本文聚焦 deep research 单一场景，跨任务泛化（coding、tool-use、multi-modal）证据不足。
- **总分 4/5**
- **为什么不是更高分：** (1) test-time scaling 的边际递减未充分分析；(2) 仅在 deep research 验证，未测试其他长程 agent 任务；(3) Context Builder 的知识库质量没有独立评估指标。
