# Agent Skills for LLMs 综述｜DNL Deep Note（单篇精读重写）

## 0) Metadata
- **Title:** Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward
- **Alias:** Agent-Skills-Survey
- **Authors / Org:** Renjun Xu, Yang Yan（机构信息：原文页面未直接给出可提取字段）
- **Venue / Status:** arXiv 2602.12430v3（survey）
- **Date:** 2026-02-17（v3 更新）
- **Links:**
  - Abs: https://arxiv.org/abs/2602.12430
  - HTML: https://arxiv.org/html/2602.12430v3
  - PDF: https://arxiv.org/pdf/2602.12430
  - Code: https://github.com/scienceaix/agentskills
- **Tags:** survey, agent skills, MCP, CUA, security governance
- **My rating:** ★★★☆☆
- **Read depth:** skim（本次按“带数字复核”的精读式重写）
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = 3

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：** 这篇综述把“agent skill”从工程技巧提升为**独立抽象层**来讨论：一端连 architecture/acquisition/deployment，另一端连 security/governance，并给出一个四级信任与生命周期治理框架；最有价值的观察是，社区技能中**26.1% 存在漏洞**，说明“能力扩展”与“安全治理”必须同设为一等目标。

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- LLM 从“单体权重承载所有能力”转向“按需加载技能包（instructions+code+resources）”。
- 与 RAG 的区别：RAG 提供被动知识片段，skill 提供可执行流程与权限上下文。
- 与 MCP 的关系：论文给出“skills 负责 what to do，MCP 负责 how to connect”的分层叙事。

### R — Related work
- 既有方向覆盖了 agent/tool use/GUI agents，但未把“skill abstraction layer”单独系统化。
- 论文回顾了 Voyager、Toolformer、Tool Makers 等前作，指出这些多在受限环境或“模型自造工具”，而当下 Agent Skills 更强调**可移植、可治理、面向生产**。

### G — Research gap
- 缺口 1：缺少以 skill 为中心的统一综述（architecture + acquisition + deployment + security 一体化视角）。
- 缺口 2：缺少跨研究的安全综合结论与可执行治理框架。
- 缺口 3：随着 skill 库规模扩大，skill routing/selection 出现可扩展性瓶颈（文中引用 phase transition 现象）。

### P — Proposal
- 论文提出四块内容：
  1. 架构综述：SKILL.md + progressive disclosure + MCP 互补关系；
  2. 获取路径 taxonomy：人写、RL、自治探索、组合合成等；
  3. 部署评估：聚焦 CUA 与 OSWorld / SWE-bench 等基准进展；
  4. 安全治理：综合 3 项实证研究，并提出 Skill Trust and Lifecycle Governance Framework（四级信任、四道 gate）。

## 3) Figure 区（至少 1 张）
- **图1（Progressive disclosure architecture）**：三层按需加载（metadata → instruction body → resources/scripts）。
  - 可提取数字：文中仅称 metadata 为“typically a few dozen tokens”，**原文未给出可提取精确 token 数**。
- **图2（Skill-equipped CUA architecture）**：展示 skill library、perception-grounding-action pipeline、MCP 层、OS 环境的交互。
  - 定量细节：该图为结构图，**原文未给出可提取数字**。
- **图3（Skill Trust & Lifecycle Governance Framework）**：四阶段验证 G1–G4 + 四信任层 T1–T4 + runtime trust evolution。
  - 定量细节：图中强调与实证安全结果联动，但图注本身**未给出新增实验数字**。

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- **任务/数据：** 综述方法为文献系统梳理（arXiv、ACL、NeurIPS/ICML/ICLR、官方文档），聚焦 skills 生态，不做统一复现实验。
- **模型/agent 配置：** 非单一模型实验论文；主要汇总 SAGE、SEAgent、CUA-Skill、UI-TARS-2、OpenCUA、Yuan 等工作结果。
- **对比基线：** 各子论文自带基线（如 GRPO baseline、UI-TARS baseline、human baseline 等）。
- **评测指标：** Success Rate / Task Goal Completion / Scenario Goal Completion / token 与 step 开销等。

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| **SAGE on AppWorld（Scenario Goal Completion）** | 51.8%（由 60.7%-8.9% 反推） | 60.7% | +8.9 pct |
| **SAGE token 开销** | 100% | 41% | -59% |
| **SAGE interaction steps** | 100% | 74% | -26% |
| **SEAgent on OSWorld（5 novel apps）** | 11.3%（UI-TARS） | 34.5% | +23.2 pct |
| **CUA-Skill on WindowsAgentArena** | 原文未在该段给出统一可比 baseline | 57.5%（SOTA） | 原文未给出可提取 delta |
| **UI-TARS-2 on OSWorld** | 原文该句未给出同表 baseline | 47.5% | 原文未给出可提取 delta |
| **UI-TARS-2 on AndroidWorld** | 原文该句未给出同表 baseline | 73.3% | 原文未给出可提取 delta |
| **OpenCUA-72B on OSWorld-Verified** | 原文该句未给出同表 baseline | 45.0% | 原文未给出可提取 delta |
| **Yuan et al. 7B on ScreenSpot-Pro** | UI-TARS-72B 23.1%（由 47.3%-24.2% 反推） | 47.3% | +24.2 pct |
| **OSWorld human-level 对比（表3）** | Human 72.4（文中另处为 72.36） | Best agent 72.6 | +0.2（约） |
| **SWE-bench Verified（表3）** | 原文未给出统一 baseline | Claude Opus 4.6: 79.2 | 原文未给出可提取 delta |
| **Security: large-scale vulnerability rate** | - | 26.1%（31,132 analyzed / 42,447 collected） | 风险高 |
| **Security: scripts vs instruction-only** | OR=1 | OR=2.12（p<0.001） | 风险倍增 |
| **Security: high-severity patterns** | - | 5.2% | - |
| **Security: confirmed malicious** | - | 157 malicious / 98,380 verified；632 vulnerabilities | - |

> 注：这是 survey 汇总表，不是同一实验 protocol 下的公平横向对比。原文未统一提供方差/置信区间，**原文未给出可提取统计显著性细节（除 OR 的 p 值）**。

### 4.3 Analysis experiments（强制“现象+解释”）
- **现象：** skill 机制在多个场景表现出“能力+效率”双提升（如 SAGE 同时提升 SGC +8.9pct 并降 token 59%）。  
  **解释（作者）：** 通过 sequential rollout 和可复用技能沉淀，把跨任务共享结构显式化，减少重复探索。  
  **【标注】（我的判断，可选）：** 这说明“外部化程序知识”比单纯扩大模型参数更像工程上可落地的增益路径；但要警惕 benchmark 泄漏式复用导致的高估。

- **现象：** 小模型在 GUI grounding 上可通过数据/训练策略反超大模型（7B 在 ScreenSpot-Pro 达 47.3%，超过 72B baseline 24.2pct）。  
  **解释（作者）：** 关键瓶颈在 grounding 数据与训练信号，而非单纯参数规模；RL self-evolution 与高质量 GUI 训练样本提升显著。  
  **【标注】（我的判断，可选）：** 对 multimodal RL 是强信号：应优先投资“交互轨迹质量+可验证奖励”，而不是先追更大 backbone。

- **现象：** skill 生态存在结构性安全风险（26.1% 漏洞率；脚本类技能风险 OR=2.12；5.2% 高危；98,380 中确认 157 个恶意技能）。  
  **解释（作者）：** skills 同时携带自然语言指令与可执行资产，且被 agent 高信任加载，形成 prompt injection + supply chain 复合攻击面。  
  **【标注】（我的判断，可选）：** 这不是“边角问题”，而是 skill-first 架构的主线约束；任何 memory/long-context 系统若支持 skill 持久化，必须做 provenance、permission manifest、sandbox 三件套。

- **现象：** 文中引用的 phase transition 提示 skill 库规模上升后，路由准确率可能突降。  
  **解释（作者）：** skill selection 在大库下成为组合爆炸问题，现有 tool search 只能部分缓解。  
  **【标注】（我的判断，可选）：** 对 long-context memory 设计的启示是：不要把“记住更多”当目标，应做层级索引和预算化检索（memory as routing substrate）。

## 5) Why it matters for our work
- 对 **agent memory**：skills 可视为“可执行记忆单元”，比纯文本 memory 更接近任务闭环；但需显式 trust tier 才能上线。
- 对 **long-context**：progressive disclosure 是实用范式——先极简 metadata 路由，再按需展开正文和脚本，控制上下文预算。
- 对 **multimodal RL**：CUA 进展显示 GUI 场景是技能学习与评估的高价值试验田，且数据飞轮 + grounding 强监督比盲目堆参数更有效。

## 6) Actionable next step
- [ ] **面向 agent memory：** 设计“Skill Memory Card”最小规范（id/provenance/permission manifest/runtime audit），先在内部 20~50 个技能库做分级（T1-T4）试点。  
- [ ] **面向 long-context：** 实做三级加载策略（L1 metadata 常驻 + L2 指令按需 + L3 脚本受控挂载），并记录每层 token/成功率/误触发率；若当前系统无日志，先补埋点。  
- [ ] **面向 multimodal RL：** 在 GUI 任务建立“小模型优先”训练线（7B 级别），比较 SFT-only vs RL self-evolution，在相同样本预算下看 grounding 成功率与成本曲线。

## 7) 评分解释（必填）
- **质量分 1/2：** 综述框架清晰、数字密集，尤其 security 汇总有实操价值；但多数结论依赖外部论文，非统一实验框架。
- **Observation 分 1/2：** 给出了“skills × governance”这一关键交叉视角，并提出四级信任生命周期框架；但原创算法/新实证有限。
- **总分 3/5：** 维持原评分倾向，不做无依据改分。
- **为什么不是更高分：** 本文主要是系统化整合与议程设置，不是机制突破型论文；部分表述（如若干 benchmark 对比）缺统一统计协议与误差报告。