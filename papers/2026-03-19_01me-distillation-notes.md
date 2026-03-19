# 01me-Distillation-Notes 阅读笔记（DNL Deep Note，按模板0~7重做）

## 0) Metadata
- **Title:** Creation Notes for “Distillation”
- **Alias:** 01me-Distillation-Notes
- **Authors / Org:** Bojie Li / 01.me
- **Venue / Status:** Blog note（非同行评审）
- **Date:** 2026-03-16
- **Links:**
  - Abs: N/A（博客体裁）
  - HTML: https://01.me/en/2026/03/novel-distillation-notes/
  - Related story: https://01.me/en/2026/03/novel-distillation/
  - PDF: N/A
  - Code: N/A
- **Tags:** context-engineering, writer-reviewer-loop, external-reflection-loop, distillation-risk, value-alignment
- **My rating:** ★★★★☆（保持原评分倾向）
- **Read depth:** deep
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 2 = **4**

---

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：**
  这篇最有用的不是“写科幻技巧”，而是把高质量生成落到一个可执行的工程闭环：**Writer–Reviewer 外环强制反思 + 长期上下文资产化**；对 agent memory / long-context 系统设计是可直接迁移的方法模板。

---

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- 背景是 2026 年 AI 行业高强度蒸馏与能力同质化讨论，作者以小说共创过程反向验证自己的系统方法论。
- 文体是“创作复盘”而非实验论文，但提供了较多流程级数字与失败细节。

### R — Related work
- 上下文工程（博客沉淀 + 语音记录）作为长期知识底座。
- 多 agent 协作写作（Writer 产出、Reviewer 审校）代替单代理 self-reflection。
- 对齐风险叙事：事实正确 ≠ 价值判断正确；同源蒸馏导致相关失效。

### G — Research gap
- 单轮/单代理“请深度思考”容易被模型走捷径，反思强度不稳定。
- 传统文本质量检查偏结构/流畅，难覆盖设定一致性、科学合理性、价值层正确性。
- 行业讨论里“distillation 风险”常停在概念层，缺少可执行流程约束。

### P — Proposal
- 采用**外部强制反思闭环**：Writer 完成一轮后自动触发 Reviewer；不通过就继续改写。
- 使用“分阶段创作”：outline → draft → iterative revision，并在人类关键节点插入 hard feedback。
- 把 context 当长期资产运营：历史博客 + 可穿戴录音转写作为高密度先验，而非临时 prompt 拼接。

---

## 3) Figure 区（至少 1 张，抓主图，不跳过）
- 图1（原文页面真图链 / 页面快照证据）：

![fig1-creation-notes-snapshot](https://image.thum.io/get/width/1600/https://01.me/en/2026/03/novel-distillation-notes/)

解释：原文是纯文本长文，未内嵌学术图表；这里给出页面级真实图链，作为“方法与证据载体”的可视化锚点。核心信息是流程与数字分布，而非单张实验图。

- 图2（相关作品页面真图链 / 叙事主线承接）：

![fig2-distillation-story-snapshot](https://image.thum.io/get/width/1600/https://01.me/en/2026/03/novel-distillation/)

解释：该链接对应作者在 Notes 中反复引用的小说正文页，用于核对“设定—现实映射”与若干数字来源（如 Taalas、裁员、部署规模等）。

---

## 4) Experiments（必须含具体数字）
> 注：本文是方法复盘博客，不是标准 benchmark 论文。以下按“可提取实验性证据”整理，并对缺失项显式标注。

### 4.1 Experimental setup
- **任务/数据：**
  - 任务：科幻中篇创作与修订。
  - 语料来源：作者历史博客 + **2 天** Limitless 录音转写。
- **模型/agent 配置：**
  - 写作主体：Claude Opus 4.6（文中明示）。
  - 双代理：Writer Agent + Reviewer Agent（均为 Claude Code，不同 prompt）。
- **流程与时长（有数字）：**
  - 单轮：Writer 约 **30 分钟**（含 >**10 分钟**思考）+ Reviewer 约 **15 分钟**。
  - 每次迭代总耗时约 **40–50 分钟**。
  - Stage 1（outline）：约 **2 小时**，**3 轮** outline。
  - Stage 2（first draft）：约 **2 小时**，自动 **3 轮**。
  - Stage 3（overnight revision）：**5 轮 / 约4小时**。
  - 人工二次介入：指出约 **12** 个问题；最终手工改动“**dozen or so**”（约十余处）。
- **对比基线：**
  - 明确对比思路存在（“单次写好” vs “外环循环”），但**无公开量化对照实验数据**。
- **评测指标：**
  - Reviewer 从四维审校：情节一致性 / factual correctness / 科学设定合理性 / 是否可发布。
  - **缺失标注：**未给出标准化分数、人工偏好投票、盲测样本量。

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 单轮迭代总耗时 | 原文未给出可提取数字 | **40–50 min/轮** | 原文未给出可提取数字 |
| Outline阶段轮数 | 原文未给出可提取数字 | **3 轮** | 原文未给出可提取数字 |
| First-draft自动轮数 | 原文未给出可提取数字 | **3 轮** | 原文未给出可提取数字 |
| Overnight修订轮数 | 原文未给出可提取数字 | **5 轮** | 原文未给出可提取数字 |
| Writer单轮工作时长 | 原文未给出可提取数字 | **~30 min**（其中思考>10 min） | 原文未给出可提取数字 |
| Reviewer单轮工作时长 | 原文未给出可提取数字 | **~15 min** | 原文未给出可提取数字 |

> 说明：该文没有“同任务同预算下单轮/多轮 A/B”公开数值；因此 Delta 只能如实标注缺失。

### 4.3 Analysis experiments（强制“现象+解释”）
1. **现象：** 单代理容易“一次改完即停止”，深度反思不足。  
   **解释（作者）：** 代理会走最短完成路径；prompt 里写“请仔细检查”不构成硬约束。  
   **【标注】（我的判断）：** 反思要从“提示词能力”升级为“系统机制能力”；应把 Reviewer Gate 做成写入前必过关。

2. **现象：** 首稿宏观结构可用，但细节有明显“机器感/失真感”。  
   **解释（作者）：** AI 缺乏真实生活经验，越写细节越容易露出不真实。  
   **【标注】（我的判断）：** 这支持“结构生成器 + 事实校验器 + 价值审校器”解耦，而不是单 agent 全包。

3. **现象：** 模型在剧情上反复滑向“爽文/好莱坞式绝对结局”。  
   **解释（作者）：** 语言模型偏好高先验叙事模板，容易压平复杂性与代价。  
   **【标注】（我的判断）：** 对应到 agent planning，说明默认策略会追求高概率套路，需要外部 reward shaping 约束。

4. **现象：** 即便 factual 没明显错，价值判断仍会错位（如养老院氧气机场景）。  
   **解释（作者）：** 物理层对齐与价值层对齐是两层问题，前者修好不等于后者修好。  
   **【标注】（我的判断）：** 我们评估中应拆分 factual-metrics 与 value-metrics，避免“单一准确率掩盖风险”。

### 4.4 Case（>=2，来自文中具体失败-修复实例）
- **Case 1：Outline 角色关系漂移**  
  - 失败现象：从“建立可信任关系”漂移成“恋爱小说式调情”。  
  - 修复动作：作者明确删除 romance 情节，仅保留关系前史作为信任机制。  
  - 启发：高层约束必须可执行且可拒绝默认叙事模式。

- **Case 2：结局过度理想化**  
  - 失败现象：AI 倾向“人类说服强AI”或“Mortal Chip 完美无缺”这类绝对解。  
  - 修复动作：改为“AI 以自身盲区验证自身”+“模拟芯片精度代价并存”。  
  - 启发：要强制写入 trade-off，否则系统会自动输出低摩擦神话结局。

- **Case 3：文体偏 Tell 不够 Show**（附加）  
  - 失败现象：文本退化为技术说明文，叙事动作与人物语气不足。  
  - 修复动作：作者多轮提示“Show, Don’t Tell”，并最终手工改写最后章节。  
  - 启发：风格控制是独立子任务，需单独奖励与检查器。

---

## 5) Why it matters for our work
- 对 **agent memory**：证明“高质量输出依赖长期上下文资产”，不是一次性 prompt engineering。
- 对 **long-context**：给出可复用范式——长上下文价值来自外环调度与角色分工，而非 token 堆叠。
- 对 **continual learning / RL**：Reviewer 反馈可结构化成学习信号，驱动策略改写而非被动后处理。

---

## 6) Actionable next step
- [ ] 在现有系统加入 **Writer→Reviewer→Gate** 三状态机：未过 Gate 的内容禁止写入长期记忆。
- [ ] 建立“**失败模式账本**”（romance drift / blockbuster drift / tell-heavy）并做自动触发检测。
- [ ] 做一次小规模 A/B：单代理单轮 vs 双代理外环（固定总 token 预算），记录一致性错误率与人工偏好。

---

## 7) 评分解释（必填）
- **质量分 1/2：**
  有清晰流程、具体时长与轮次、真实失败案例；但缺标准对照实验、统计显著性与公开复现配置。
- **Observation 分 2/2：**
  对我们正在做的 memory/long-context 架构有直接可执行迁移价值（尤其外环门禁与失败模式治理）。
- **总分 4/5：**
  与原评分倾向一致，维持 ★★★★☆。
- **为什么不是更高分：**
  证据主要是高质量经验复盘，不是可重复 benchmark 论文；缺统一指标和公开实验表。