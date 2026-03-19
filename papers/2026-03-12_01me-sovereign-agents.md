# 01.me《Sovereign Agents: In-Depth Research on Clawdbot/OpenClaw》精读重写（DNL Deep Note）

## 0) Metadata
- **Title:** Sovereign Agents: In-Depth Research on Clawdbot/OpenClaw  
- **Alias:** 01me-Sovereign-Agents  
- **Type:** Blog / System Research Report（非学术论文）  
- **Link:** https://01.me/en/2026/01/clawdbot-openclaw-analysis/  
- **Author / Source:** 01.me（文中注明与 Clawdbot + Claude Opus 4.5 协作）  
- **Read date:** 2026-03-19  
- **My rating:** ★★★☆☆（**保持原评分倾向，不上调**）  
- **Read depth:** deep（单篇精读）  
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3**

---

## 1) One-line Why-read
这篇文章的价值不在“新算法”，而在把 **主权 Agent（数据/算力/控制三主权）** 讲成一条可落地的系统路线：你到底要“平台托管的安全感”，还是“本地自治的可控性”。

---

## 2) CRGP（Context / Related / Gap / Proposal）

### C — Context
- 文章把 Clawdbot（后续改名 OpenClaw）放在 2024–2026 的 Agent 演化线上：
  1) Deep Research，2) Computer Use，3) Coding Agent 三线汇合。
- 核心主张：所谓 **Sovereign Agent** = Data sovereignty + Compute sovereignty + Control sovereignty。
- 文章定位是“系统研究报告 + 行业观察”，不是论文，不提供严格实验协议。

### R — Related work / 参照系
- 竞品与技术脉络：Anthropic Computer Use、Claude Cowork/Code、OpenAI Deep Research、Manus、Gemini Deep Research。
- 文章给出大量“市场与工程指标”作为论据（如 stars、插件数、成本、时间线），并给出架构对照（Cowork vs OpenClaw）。

### G — Research gap（本文试图填的空白）
- 闭源 Agent 的主流范式下，用户缺乏三类主权：
  - 数据不可验证地“离开本地”；
  - 算力路径受供应商绑定；
  - 控制权被厂商策略托管。
- 技术上已有成熟组件（LLM、Tool Calling、本地执行），但缺“**三能力合一 + 开源可改 + 可自托管**”的系统化实现。

### P — Proposal（作者方案）
- 以 OpenClaw 为样本提出一套“主权 Agent 蓝图”：
  - 四层架构：Gateway / Core / Memory / Execution；
  - Coding Agent 作为核心执行内核（7 个基础工具）；
  - Markdown + Git + SQLite-hybrid search 的长期记忆；
  - 多层权限策略 + 容器隔离 + 人在回路的安全防护。

---

## 3) Figure / Data 区（非论文，改为“关键数字与设置摘录”）

> 说明：原文无标准学术 figure 编号，这里按“可提取数字/设置/结果”整理。

### 3.1 市场与增长侧数字
- 发布后“1 天内爆发”，**不到 1 周 GitHub stars 超 70,000**。
- 对比表中给出：
  - 传统 OSS 首周 ~500 stars；
  - Clawdbot/OpenClaw 首周 **9,200+**（约 **18x**）。
- Discord 社区：**8.9k+**（文中写 instant explosion）。
- 插件生态形成时间：传统“数月” vs OpenClaw **48 小时**。

### 3.2 成本与资源侧数字
- Claude Cowork 订阅层级：**$20/月** 与 **$100/月**。
- 文中估算 $100 档可对应约 **$300–400 token value**（重度用户更划算）。
- Computer Use 代价示例：Claude 跑 **30 分钟约 $10** token 成本。
- 本地算力替代：文中举例“20,000 RMB 硬件投入可选，但并非必要”；也给出低价云替代 **19.9 RMB/月** 级别（场景化陈述）。

### 3.3 开发效率与项目演化数字（创始人叙事）
- 个人开发速度：**40–50k LOC/天**。
- token 消耗：**1.8B tokens/天**。
- 单日提交：**1,374 commits/天**。
- 两个月代码规模接近 **百万行**。

### 3.4 记忆与检索机制设置
- Memory 检索融合公式：`finalScore = vectorWeight * vectorScore + textWeight * textScore`。
- 默认权重：**0.7 : 0.3**（向向量语义侧倾斜）。
- 数据结构：SQLite（files/chunks/chunks_fts/chunks_vec/embedding_cache）。

### 3.5 关键时间线
- Anthropic Computer Use：**2024-10**。
- GenSpark Deep Research：**2025-01**；OpenAI Deep Research：**2025-02**。
- Manus 走红：**2025-03**；被 Meta 收购：**2025-12-30（>$2B）**。
- Clawdbot 上线：**2026-01-25**；改名 Moltbot：**2026-01-27**；改名 OpenClaw：**2026-01-30**。

### 3.6 原文未给出的关键数字（明确标注缺失）
- 原文**未给出可复现实验集**（无 benchmark 名称、样本数、任务分布、评估脚本）。
- 原文**未给出统计显著性**（无置信区间、方差、显著性检验）。
- 原文**未给出安全攻击评测指标**（如攻击成功率/误杀率/恢复时延）。

---

## 4) Experiments（按“系统证据审读”重构）

### 4.1 Experimental setup（原文可提取）
- **系统类型：** 案例式系统研究，不是对照实验论文。  
- **架构设置：** 四层（Gateway/Core/Memory/Execution）。  
- **核心 Agent loop：** ReAct 风格，工具调用失败回灌 LLM 自纠。  
- **核心工具集：** Read / Write / Edit / Find / Search / Python / Bash（7 工具）。  
- **Memory 设置：** Markdown 文件（MEMORY.md + daily logs + AGENTS.md）+ SQLite hybrid retrieval（FTS5 + 向量检索 + 0.7:0.3 融合）。  
- **执行设置：** Browser 侧偏 Playwright DOM 交互，不完全依赖纯截图坐标。  
- **安全设置：** Docker 沙箱 + 高危命令拦截 + 人在回路 APPROVE + `moltbot security audit`。

### 4.2 Main result table（证据类型结果，不是学术 SOTA 表）
| 维度 | Baseline/对照 | OpenClaw 报告值 | Delta/结论 |
|---|---:|---:|---|
| GitHub 首周 stars | ~500（传统 OSS） | 9,200+ | ~18x |
| GitHub 一周内累计 | 原文未统一给对照 | 70,000+（<1 week） | 超常扩散 |
| 插件生态成形时间 | 数月 | 48h | 显著加速 |
| Discord 社区规模 | 渐进增长（传统） | 8.9k+（快速涌入） | 爆发式 |
| 重度付费成本参考 | Cowork $100/月 | 对应约$300–400 token value | 重度用户订阅有优势 |
| Computer Use 推理成本 | 原文未给系统对照 | ~ $10 / 30 min（Claude 示例） | GUI agent 成本高 |
| 记忆检索权重 | 原文无他法对照 | vector:text = 0.7:0.3 | 语义优先+关键词补偿 |

### 4.3 Analysis（至少3条：现象 + 解释 + 我的判断）
1) **现象：** 文中把“增长爆发”与“主权叙事”强绑定（70k<1周、48h插件爆发、8.9k+社群）。  
   **解释（作者）：** 用户对订阅疲劳+封闭生态不满，被 BYOK + 开源可改 + 本地可控触发。  
   **我的判断：** 这个解释基本成立，但“主权”与“传播”之间可能还有第三变量（创始人影响力、媒体放大、争议话题）。若要严谨，需要拆分归因做 A/B 级别证据。

2) **现象：** 架构上强调 Coding Agent 是总核心，Deep Research/Computer Use 是外延。  
   **解释（作者）：** 代码与文件系统是最稳定、最高效、最通用的行动空间；很多 GUI 任务最终可降解为代码生成。  
   **我的判断：** 方向对，尤其在文档生成/自动化流水线中优势明显；但在高噪声现实 UI、跨端权限系统里，纯 coding-core 仍需配强鲁棒 GUI policy 与恢复机制。

3) **现象：** Memory 采用 Markdown + Git + SQLite hybrid，而非“纯向量库神化”。  
   **解释（作者）：** 人类可读可改、具时间线、可版本回滚，且可混合检索补足召回。  
   **我的判断：** 这是本文最有工程价值的一点。对长期协作 Agent 来说，可审计性往往比“向量召回指标极致”更关键；但原文没给长期漂移、冲突记忆、遗忘策略的量化评估。

4) **现象：** 安全章节语气很重，甚至明确不建议裸跑在个人机器。  
   **解释（作者）：** Prompt injection、供应链、端口暴露都是真实高危面；全权限 Agent 风险与能力同升。  
   **我的判断：** 这部分是“现实主义”加分项。问题在于缺少红队数据（攻击成功率、拦截率、误报率），导致建议可执行但不可度量。

5) **现象：** 多模型兼容被当作主权的一部分（Claude/GPT/Gemini/DeepSeek/Ollama/OpenRouter）。  
   **解释（作者）：** 反绑定可降本、可规避支付与地区限制，并支持离线场景。  
   **我的判断：** 商业与部署层面非常实用；但多模型一致性（工具调用协议差异、长上下文风格漂移）在原文缺少工程细节与测试数据。

---

## 5) Why it matters for our work
- 对我们做 Agent memory/long-context 系统非常直接：
  1) **Memory 可审计优先**：把“可读可改可回滚”当作一等公民，不把记忆黑箱化。  
  2) **Long-context 要有压缩闭环**：会话压缩 + 事实抽取 + 日志归档，替代“无限堆上下文”。  
  3) **多模态执行应分层**：DOM/结构化动作优先，视觉动作兜底，高危动作强制 HITL。  
- 这篇更像“架构宣言 + 工程路线图”，不是“算法论文”；对产品系统设计启发大于对学术 SOTA 追赶。

---

## 6) Actionable next steps（3条，可执行；面向 agent memory / long-context / multimodal RL）
1) **Memory（两周内可做）**  
   落地 `MEMORY.md + daily logs + conflict ledger` 三文件制，并在检索层实现 `FTS + vec` 融合（先用 0.7:0.3 起步）；每周做一次“可审计回放”，记录错误记忆修正耗时与回滚次数。

2) **Long-context（本月可做）**  
   上线“压缩-再注入”流水线：当会话超过阈值（如 token/轮次）自动触发摘要，将“稳定事实、临时计划、待办状态”分桶写入；新增 1 份漂移评测集，监控摘要后任务成功率变化。若缺指标，先定义并持续采集。

3) **Multimodal RL / policy（季度可做）**  
   构建小规模 GUI+DOM 混合轨迹集：同任务分别走“结构化动作优先”和“纯视觉点击”两条策略，比较成本、成功率、恢复步数；把高危动作（删除/转账/外发）统一纳入 HITL gate，逐步训练 reward model 约束“低风险先行”。

---

## 7) 评分解释（维持原倾向）
- **为什么是 3/5：**
  - 优点：系统视角完整、工程细节密、观点鲜明（特别是主权三分法与 Markdown 记忆路线）。
  - 扣分点：大量关键结论依赖案例叙事与经验数字，缺乏可复现实验和严格统计。
- **为什么不升分：**
  - 原文不是实验论文，缺 benchmark protocol、攻击评测、显著性分析；在“证据强度”上不足以支持更高分。
- **结论：** 保持 **★★★☆☆** 最稳妥。