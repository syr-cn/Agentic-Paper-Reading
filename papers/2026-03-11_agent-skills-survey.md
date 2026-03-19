# Agent Skills for LLMs 综述｜DNL Deep Note

## 0) Metadata
- **Title:** Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward
- **Alias:** Agent-Skills-Survey
- **Authors / Org:** Renjun Xu, Yang Yan（原文页面未提供可提取机构字段）
- **Venue / Status:** arXiv 2602.12430v3（survey）
- **Date:** 2026-02-17（v3）
- **Links:**
  - Abs: https://arxiv.org/abs/2602.12430
  - HTML: https://arxiv.org/html/2602.12430v3
  - PDF: https://arxiv.org/pdf/2602.12430
  - Code: https://github.com/scienceaix/agentskills
- **Tags:** survey, agent skills, MCP, CUA, security governance
- **My rating:** ★★★☆☆（保持原评分倾向）
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3**

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：** 这篇综述把“Agent Skill”明确为独立于 tool/RAG 的抽象层，系统梳理了 architecture→acquisition→deployment→security 全链条；最关键观察是技能生态已出现显著安全风险（**26.1% 漏洞率**），因此能力扩展必须与治理同构设计。

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- 单体 LLM 在真实任务里缺少可组合的程序性经验；仅靠微调成本高、可移植性差。
- RAG 可补知识，但检索到的是“被动文本”，不直接携带可执行流程与权限边界。
- Agent Skills 把经验外部化为 SKILL.md + scripts + assets 的可加载包。

### R — Related work
- 既有综述覆盖 LLM agent/tool use/GUI agent，但未单独聚焦“skill abstraction layer”。
- 相关先行：Voyager、Toolformer、Tool Makers 等，更多是受限环境内的“工具/技能生成”，不是面向生产的标准化技能治理。

### G — Research gap
- 缺少对 skill 体系的统一综述：架构、获取、部署、安全通常分散讨论。
- 缺少把安全风险与部署权限联动的治理框架。
- skill 库扩张后出现路由复杂性与选择退化（phase transition）问题，缺系统性讨论。

### P — Proposal
- 论文提出四轴综述框架：
  1) 架构基础：progressive disclosure + SKILL.md + MCP 互补；
  2) 技能获取：人工编写、RL、自主探索、组合合成；
  3) 大规模部署：CUA 栈与 OSWorld / SWE-bench 等进展；
  4) 安全治理：综合 3 项安全实证并提出四级信任生命周期框架（G1–G4, T1–T4）。

## 3) Figure 区（至少 1 张，抓主图，不跳过）
- 图1（方法主图，progressive disclosure）：

![fig1](https://arxiv.org/html/2602.12430v3/x1.png)

  解释：展示 skill 的三层按需加载（metadata → instruction body → resources/scripts），核心目的是在大技能库下控制上下文开销。文中仅给出“metadata 通常几十 token”，**原文未给出可提取精确 token 数**。

- 图2（部署架构图，CUA with skills）：

![fig2](https://arxiv.org/html/2602.12430v3/x2.png)

  解释：展示 skill library、感知- grounding-行动链路、MCP 连接层与 OS 环境的耦合关系，强调 skills 提供“what to do”、MCP 提供“how to connect”。

- 图3（治理框架图，security）：

![fig3](https://arxiv.org/html/2602.12430v3/x3.png)

  解释：把来源、验证、权限、运行时监控打通，形成 gate-based trust evolution；这是该综述相对有原创性的“框架化输出”。

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- **任务/数据：** 本文是 survey，不是单一实验论文；主要汇总 AppWorld、OSWorld、WindowsAgentArena、ScreenSpot-Pro、SWE-bench Verified 等结果。
- **模型/agent 配置：** 汇总 SAGE、SEAgent、CUA-Skill、UI-TARS-2、OpenCUA、Yuan et al. 等工作；协议不统一。
- **对比基线：** 各子论文使用各自 baseline（如 GRPO baseline、UI-TARS baseline、human baseline）。
- **评测指标：** Success Rate / Task Goal Completion / Scenario Goal Completion / token 与 interaction step 开销等。

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| SAGE on AppWorld（Scenario Goal Completion） | 51.8%（由 60.7-8.9 反推） | 60.7% | +8.9 pct |
| SAGE on AppWorld（Task Goal Completion） | 原文该段未给统一 baseline 数 | 72.0% | 原文未给出可提取 delta |
| SAGE token 开销 | 100% | 41% | -59% |
| SAGE interaction steps | 100% | 74% | -26% |
| SEAgent on OSWorld（5 novel apps） | 11.3%（UI-TARS） | 34.5% | +23.2 pct |
| CUA-Skill on WindowsAgentArena | 原文未给统一同表 baseline | 57.5% | 原文未给出可提取 delta |
| UI-TARS-2 on OSWorld | 原文该句未给同表 baseline | 47.5% | 原文未给出可提取 delta |
| UI-TARS-2 on AndroidWorld | 原文该句未给同表 baseline | 73.3% | 原文未给出可提取 delta |
| OpenCUA-72B on OSWorld-Verified | 原文该句未给同表 baseline | 45.0% | 原文未给出可提取 delta |
| Yuan et al. 7B on ScreenSpot-Pro | UI-TARS-72B 23.1%（由 47.3-24.2 反推） | 47.3% | +24.2 pct |
| OSWorld Human-level 对比（表3） | Human 72.4（文中另处 72.36） | Best agent 72.6 | +0.2（约） |
| SWE-bench Verified（表3） | 原文未给统一 baseline | Claude Opus 4.6: 79.2 | 原文未给出可提取 delta |
| Security（Liu et al.） | - | 26.1% vulnerabilities（31,132/42,447） | 风险高 |
| Security（scripts vs instruction-only） | OR=1 | OR=2.12（p<0.001） | 风险倍增 |
| Security（high-severity patterns） | - | 5.2% | - |
| Security（confirmed malicious） | - | 157 malicious / 98,380；632 vulnerabilities | - |

> 注：综述中的数值来自不同论文与协议，不构成严格同条件公平横比；多数结果**原文未给出可提取方差/置信区间**。

### 4.3 Analysis experiments（强制“现象+解释”）
- **现象：** 多个代表工作显示 skill 化不仅提准确率，也显著降成本（如 SAGE：+8.9pct SGC，token -59%，steps -26%）。
  **解释（作者）：** skill library + sequential rollout 提升跨任务经验复用，减少重复探索与无效推理。
  **【标注】（我的判断，可选）：** 这对生产最有意义：能力与成本同向改善，比“只追榜单分数”更可落地。

- **现象：** GUI 场景里小模型在特定 grounding 任务可超过更大模型（7B 在 ScreenSpot-Pro 47.3%，对 UI-TARS-72B +24.2pct）。
  **解释（作者）：** 关键瓶颈是训练数据和交互信号质量，而非参数规模本身。
  **【标注】（我的判断，可选）：** 对多模态 RL 是明确信号：优先做高质量轨迹与可验证反馈，收益常高于盲目增参。

- **现象：** 安全问题不是个例：社区技能大规模扫描有 26.1% 漏洞，脚本型技能风险 OR=2.12，且存在已确认恶意技能（157 个）。
  **解释（作者）：** skill 同时承载指令与可执行资产，天然形成 prompt injection + supply chain 复合攻击面。
  **【标注】（我的判断，可选）：** “可执行记忆”必须默认零信任；若没有 provenance、permission manifest、sandbox，skill-first 系统迟早暴露高危面。

- **现象：** 文中引用 phase transition：skill 库规模增长到阈值后，选择准确率会明显下降。
  **解释（作者）：** 路由空间组合爆炸，现有检索策略难稳定处理超大技能库。
  **【标注】（我的判断，可选）：** 对 long-context/memory 系统的启示是“治理优先于堆量”，层级索引与预算化检索是必做项。

## 5) Why it matters for our work
- 对 **agent memory**：skill 是“可执行记忆单元”，比纯文本记忆更接近真实任务闭环，但必须引入分级信任。
- 对 **long-context**：progressive disclosure 是高性价比范式——先轻量路由，再按需展开深层内容。
- 对 **multimodal RL**：CUA 结果显示 GUI grounding 与交互训练是高杠杆环节，可作为 skill-learning 的优先试验场。

## 6) Actionable next step
- [ ] 设计内部 **Skill Memory Card** 规范：`id/provenance/permission manifest/runtime audit`，先对现有技能做 T1–T4 分层。
- [ ] 在 agent runtime 落地三级加载：L1 metadata 常驻、L2 指令按需、L3 脚本受信任门控，并记录 token/成功率/误触发率。
- [ ] 在 GUI 任务做“小模型+技能库”对照：SFT-only vs RL self-evolution，统一比较成功率、token 成本、稳定性。

## 7) 评分解释（必填）
- **质量分 1/2：** 框架完整、数据密集，安全章节有较强工程价值；但主体证据来自外部论文汇编，非统一实验协议。
- **Observation 分 1/2：** 提出“skills × governance”联动视角和四级信任框架有启发；但原创算法与新实证有限。
- **总分 3/5：** 保持原评分倾向，不无依据改分。
- **为什么不是更高分：** 该文长于议程设置和系统化整合，弱于机制创新与统一可复现实验。