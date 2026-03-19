# 01.me《Sovereign Agents: In-Depth Research on Clawdbot/OpenClaw》精读重做（DNL Deep Note）

## 0) Metadata
- **Title:** Sovereign Agents: In-Depth Research on Clawdbot/OpenClaw  
- **Alias:** 01me-Sovereign-Agents  
- **Type:** Blog / System Research Report（非同行评审论文）  
- **Link:** https://01.me/en/2026/01/clawdbot-openclaw-analysis/  
- **Author / Source:** 01.me（文中注明与 Clawdbot + Claude Opus 4.5 协作）  
- **Read date:** 2026-03-19  
- **My rating:** ★★★☆☆（**保持原评分倾向，不上调**）  
- **Read depth:** deep（单篇重读+结构化重做）  
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3/5**

---

## 1) One-line Why-read
这篇的核心价值不在算法创新，而在给出一个可落地的系统命题：**把 Data / Compute / Control 三种主权，统一到同一个开源 Agent 运行时里**。

---

## 2) CRGP（Context / Related / Gap / Proposal）

### C — Context
- 文章把 2024–2026 的 Agent 演进归纳为三条线汇合：
  1) Deep Research，2) Computer Use，3) Coding Agent。  
- 主张“主权智能体（Sovereign Agent）”三要素：
  - 数据主权（数据尽量不离开本地）
  - 算力主权（云 API 与本地模型可切换）
  - 控制主权（用户承担最终控制与风险）
- 体裁是“系统观察 + 工程拆解”，不是实验论文。

### R — Related / Baselines
- 对照对象（文中高频出现）：Claude Cowork、Claude Code、Computer Use、OpenAI Deep Research、Manus、Gemini 等。
- 技术参照：
  - ReAct 工具循环
  - Playwright/DOM 交互 vs 纯截图循环
  - Markdown + SQLite 混合检索记忆

### G — Gap
- 闭源 Agent 的现实限制被归纳为三类缺口：
  1) 数据路径不可验证；
  2) 算力路径被厂商绑定；
  3) 行为边界由供应商策略决定。  
- **证据缺口（学术视角）**：缺少公开 benchmark、任务定义、统计显著性、安全红队量化。

### P — Proposal
- 以 OpenClaw 为样本提出“主权 Agent 蓝图”：
  - 四层架构：Gateway / Core / Memory / Execution
  - Coding Agent 作为主执行核心（7 基础工具）
  - Memory 走 Markdown + Git + SQLite hybrid 路线
  - 安全上采用沙箱、审批门、命令拦截与审计

---

## 3) Figure / Data（真图链 + 数字摘录 + 缺失标注）

> 说明：原文非学术论文，几乎无标准 figure 编号；本节按“真图链 + 可核数字”重建。

### 3.1 Figure 真图链（>=1）
- **Figure-1（封面图链）**：https://cover.sli.dev  
  （来自作者公开 Slidev 源 `https://01.me/files/clawdbot/slides.md` 的 `background` 字段）
- **Figure-2（Slidev 图标链）**：https://cdn.jsdelivr.net/gh/slidevjs/slidev/assets/favicon.png

### 3.2 关键数字（文章/配套 slides 可抽取）
- GitHub 爆发：**<1 周 70,000+ stars**。  
- 首周对照：传统 OSS ~500 vs OpenClaw **9,200+**（~18x）。  
- Discord：**8.9k+**（即时爆发）。  
- 插件生态成形：传统“数月” vs OpenClaw **48 小时**。  
- 付费参考：Claude Cowork **$20 / $100** 档；文中估算 $100 档对应约 **$300–400 token value**。  
- GUI agent 成本示例：Computer Use **30 分钟约 $10**。  
- 开发叙事数字：**40–50k LOC/天、1.8B tokens/天、1374 commits/天、两个月近百万行代码**。

### 3.3 关键缺失（必须标注）
- **[缺失]** 无公开 benchmark 名称与任务分布。  
- **[缺失]** 无样本规模、统计方差、显著性检验。  
- **[缺失]** 无统一安全评测指标（攻击成功率/误报率/恢复时延）。  
- **[缺失]** 无跨模型一致性测试细节（工具调用协议差异、回归测试）。

---

## 4) Experiments（按“系统证据审读”重构）

### 4.1 Experimental setup（可还原设置）
- 系统类型：案例式系统报告，非控制变量实验。  
- 架构：Gateway/Core/Memory/Execution 四层。  
- 运行循环：ReAct 风格工具调用，错误回灌模型做自纠。  
- 工具核心：Read / Write / Edit / Find / Search / Python / Bash（7 工具）。  
- 记忆：Markdown 文件 + SQLite FTS5 + 向量检索，融合权重 **0.7:0.3**。  
- 执行：浏览器动作强调 DOM 能力（Playwright），非纯视觉点击。  
- 安全：Docker、HITL `APPROVE`、高危命令拦截、安全审计命令。

### 4.2 Main result table（有数字 + 缺失并列）
| 维度 | 对照/基线 | OpenClaw 报告值 | 备注 |
|---|---:|---:|---|
| 首周 GitHub stars | ~500（传统 OSS） | 9,200+ | ~18x |
| 一周内累计 stars | [缺失统一基线] | 70,000+ | 爆发扩散 |
| 插件生态成形时间 | 数月 | 48h | 社区裂变 |
| Discord 社区规模 | 渐进增长 | 8.9k+ | 即时爆发 |
| Cowork 成本参考 | $20/$100 月费 | $100≈$300–400 token value | 重度用户更划算 |
| GUI 代理推理成本 | [缺失系统对照] | ~$10/30min（示例） | 成本偏高 |
| 检索融合策略 | [缺失他法对照] | 0.7(vector):0.3(text) | 语义优先 |

### 4.3 Case studies（硬要求：case >= 2）
**Case-1：Manus 的“能力证明—闭源回收”路径**  
- 现象：Manus 在 2025-03 爆红，2025-12-30 被 Meta 以 >$2B 收购并闭源化。  
- 意义：验证“通用 Agent”有强商业需求，但核心能力会被封闭生态吸收。  
- 对本文命题的支撑：OpenClaw 被定位为该趋势的开源反向样本。

**Case-2：Mac Mini 效应与 iMessage 物理桥梁**  
- 现象：社区出现显著 Mac Mini 采购潮（尤其 M4），文章将其与 iMessage 接入需求绑定。  
- 机制：Apple 生态下消息能力 + 本地运行需求叠加，导致“Agent 部署=硬件采购”联动。  
- 启示：主权路线不仅是软件议题，也会重塑硬件选择与家庭算力形态。

**Case-3：更名风波与 $CLAWD 诈骗事件（补充）**  
- 现象：Clawdbot→Moltbot→OpenClaw 更名期间，旧账号名被秒抢注并用于假币诈骗。  
- 启示：开源项目的品牌/分发链路也是安全面，影响社区信任与采用成本。

### 4.4 Analysis（>=3：现象 + 解释 + 判断）
1) **现象：** “70k<1周 + 48h 插件爆发 + 8.9k 社群”被解释为主权叙事胜利。  
   **解释：** 用户对订阅疲劳和封闭约束反弹，BYOK + 可改源码触发迁移。  
   **判断：** 方向成立，但需控制“创始人影响力/媒体放大/争议传播”这些混杂变量。

2) **现象：** 文中强调 Coding Agent 是三合一系统的核心执行引擎。  
   **解释：** 代码与文件系统动作成本低、表达力高，很多 GUI 任务可降解为代码生成。  
   **判断：** 工程上非常实用；但在高动态 UI 与跨权限系统中，仍需更强恢复策略与风险门控。

3) **现象：** Memory 选择 Markdown + Git + SQLite hybrid，而非纯向量库。  
   **解释：** 可读可改可回滚，比“黑箱召回”更适配长期协作与审计。  
   **判断：** 这是本文最有落地价值的设计；但缺长期漂移、冲突记忆与遗忘策略的量化结果。

4) **现象：** 安全章节语气强烈（不建议裸跑个人机）。  
   **解释：** 全权限 Agent 面临 prompt injection、插件供应链、端口暴露等复合风险。  
   **判断：** 风险判断靠谱，但缺可比较的安全基准数据，当前更像“操作建议”而非“可验证证据”。

---

## 5) Why it matters for our work
- **Agent memory：** “可审计记忆”优先于“只追召回率”，适合长期人机协作。  
- **Long-context：** 依赖压缩-归档-检索闭环，而不是无限堆上下文。  
- **Multimodal execution：** 结构化动作（DOM/工具）优先，视觉点击兜底，高危动作强制 HITL。  
- 对我们而言，这篇更像“系统路线图输入”，不是“算法上限证明”。

---

## 6) Actionable next steps（3条）
1. **Memory 侧（2 周）**：上线 `MEMORY.md + daily logs + conflict ledger`，检索先用 0.7:0.3 融合；每周做一次审计回放。  
2. **Long-context 侧（1 个月）**：实现会话阈值触发压缩，分桶写入“稳定事实/临时计划/待办状态”，跟踪摘要后成功率与偏移。  
3. **执行策略侧（季度）**：构建 DOM-first vs Vision-first 双策略对照集，记录成功率、成本、恢复步数，并统一高危动作审批门。

---

## 7) 评分解释（维持原倾向）
- **最终评分：★★★☆☆（3/5）**。  
- **给 3 分的理由：**
  - 主权三分法清晰，工程拆解具体；
  - 记忆与执行层有较强可迁移价值；
  - 对产品系统设计启发明显。  
- **不升分的理由：**
  - 证据仍以案例与叙事为主；
  - 缺 benchmark protocol 与统计检验；
  - 安全评估缺量化红队数据。  

> 结论：这是一篇**方向强、工程强、证据强度中等**的系统研究型博客，适合用于架构决策，不适合当作效果上限证据。
