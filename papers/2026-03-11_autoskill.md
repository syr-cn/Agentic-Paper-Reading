# AutoSkill 精读笔记（DNL Deep Note）

## 0) Metadata
- **Title:** AutoSkill: Experience-Driven Lifelong Learning via Skill Self-Evolution  
- **Alias:** AutoSkill  
- **Authors / Org:** Yutao Yang, Junsong Li, Qianjun Pan, Bihao Zhan, Yuxuan Cai, Lin Du, Jie Zhou, Kai Chen, Qin Chen, Xin Li, Bo Zhang, Liang He（ECNU + Shanghai AI Lab）  
- **Venue / Status:** arXiv 2603.01145v1（preprint）  
- **Date:** 2026-03-03  
- **Links:**  
  - Abs: https://arxiv.org/abs/2603.01145  
  - HTML: https://arxiv.org/html/2603.01145v1  
  - PDF: https://arxiv.org/pdf/2603.01145  
  - Code: https://github.com/ECNU-ICALK/AutoSkill  
- **Tags:** lifelong-learning, agent-memory, skill-evolution, training-free, personalization  
- **My rating:** ★★★☆☆（维持原倾向）  
- **Read depth:** deep  
- **Scoring (1+2+2):** 基础 1 + 质量 1 + Observation 1 = **3**

## 1) 一句话 Why-read（必填）
- **Key claim/contribution + key observation：**AutoSkill 把长期记忆从“历史片段检索”升级为“可维护技能工件（SKILL.md）”，在不训练底座模型前提下实现在线检索+异步演化；但当前证据更偏系统规模统计，任务效果对比仍不足。

## 2) CRGP 拆解 Introduction（必填）
### C — Context
- 实际 LLM 应用里，用户偏好（风格、格式、流程约束）会反复出现，但常常每次会话都要重说。
- 传统做法要么靠参数更新（代价高），要么靠对话片段记忆（可复用行为沉淀不足）。

### R — Related work
- 相关方向包含：memory/RAG、self-evolution、agent skill learning、lifelong agent。
- 作者认为这几类方法普遍缺“显式可维护技能对象”，技能多是隐式存在于 prompt/trajectory/policy。

### G — Research gap
- 缺少一种可部署、可解释、可迭代的 lifelong 层：
  1) 不改模型参数；
  2) 能把交互经验变成可复用能力；
  3) 能做 add/merge/discard 与版本演化治理。

### P — Proposal
- 提出 AutoSkill 双循环：
  - 在线：query rewrite → hybrid retrieval → skill-conditioned generation；
  - 后台：skill extraction → neighbor retrieval → judge(add/merge/discard) → versioned merge。
- 技能对象统一为 `s=(n,d,p,τ,γ,ξ,v)`，并以 `SKILL.md` 存储与迭代。

## 3) Figure 区（至少 1 张，抓主图，不跳过）
- 图1（方法总览）：
  ![fig1](https://arxiv.org/html/2603.01145v1/2603.01145v1/x1.png)
  - 展示 AutoSkill 的两条闭环：上层 skill evolution、下层 skill-enhanced response generation，是全文核心架构图。

- 图2（类别分布，SVG 图源）：
  ![fig2](https://arxiv.org/html/2603.01145v1#S4.F2)
  - 对应 N=1858 的技能类别统计，编程、写作、Data/AI 是头部类别，长尾类别显著更少。

- 图3（平台分布，SVG 图源）：
  ![fig3](https://arxiv.org/html/2603.01145v1#S4.F3)
  - 平台提及集中在 Twitter/X、Instagram、YouTube，说明抽取到的平台技能具有明显头部集中效应。

## 4) Experiments（必须含具体数字）
### 4.1 Experimental setup
- 任务/数据：WildChat-1M；仅保留 **>8 turns** 对话。
- 子集划分：zh/en × GPT-3.5/GPT-4，共 4 个 SkillBank 子集。
- 模型/agent 配置：training-free、prompt-driven modular pipeline（rewrite/chat/extract/judge/merge + embedding）。
- 对比基线：论文主体未提供与主流 memory baseline 的统一量化对照（**原文未给出可提取数字**）。
- 评测指标：
  - 规模统计（conversations/messages/skills）；
  - 标签频率；
  - 类别分布与平台提及。
- 关键超参：
  - 检索融合权重 λ、管理阶段 α、Top-K、阈值 η 的具体数值：**原文未给出可提取数字**。

### 4.2 Main result table（必填）
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 全局技能数 | 0（无技能库存量） | 1858 | +1858 |
| Chinese GPT-3.5 子集 skills | 0 | 400 | +400 |
| English GPT-3.5 子集 skills | 0 | 631 | +631 |
| Chinese GPT-4 子集 skills | 0 | 224 | +224 |
| English GPT-4 子集 skills | 0 | 603 | +603 |

补充实验数字（来自 Table/Figure）：
- 四子集规模：
  - zh GPT-3.5：**5912 conversations / 134,670 messages / 22.78 msg per conv / 400 skills**
  - en GPT-3.5：**10,243 / 267,681 / 26.13 / 631**
  - zh GPT-4：**1,145 / 36,834 / 32.17 / 224**
  - en GPT-4：**5,211 / 157,508 / 30.23 / 603**
- Top tags（前 5）：python **98**、javascript **38**、excel **36**、c++ **35**、creative writing **35**。
- Figure 2 类别计数：Programming **482**、Writing **363**、Data&AI **354**、Systems **194**、Research **72**、Operations **23**、Other domain **14**、General/Mixed **356**。
- Figure 3 平台提及：Twitter/X **27**、Instagram **24**、YouTube **13**、Douyin/TikTok **6**、WeChat OA **4**、LinkedIn **4**、Xiaohongshu **3**、Weibo **1**。

### 4.3 Analysis experiments（强制“现象+解释”）
- **现象：** 技能类别呈“技术+写作”双峰，Programming(482) + Data/AI(354) + Writing(363)占据主体。  
  **解释（作者）：** 来自真实用户交互中高频需求的抽取结果，反映常见使用场景。  
  **【标注】（我的判断，可选）：** 这验证了“经验驱动会继承真实流量分布”，但也会压缩长尾能力，需要后续做稀有高价值技能保留策略。

- **现象：** GPT-4 子集平均对话更长（32.17/30.23）但技能总量不一定更高（zh GPT-4 仅224）。  
  **解释（作者）：** 论文主要给出统计事实，未给严格因果分析。  
  **【标注】（我的判断，可选）：** 对话更长不等于更易抽出可复用技能，可能存在“长对话里一次性内容比例更高”的问题。

- **现象：** 平台相关技能高度集中（27/24/13 后快速衰减至 6/4/4/3/1）。  
  **解释（作者）：** 头部平台在数据中更常见，因此技能沉淀也更集中。  
  **【标注】（我的判断，可选）：** 这对部署是双刃剑：头部收益明显，但跨平台泛化会受限，建议在检索时加入平台条件门控。

- **现象：** 论文强调 add/merge/discard + 版本迭代，但没有给出“质量收益曲线”。  
  **解释（作者）：** 本文定位更偏框架与系统化实现。  
  **【标注】（我的判断，可选）：** 目前证据支持“可建库、可维护”，但尚不足以证明“显著优于现有 memory 方法”。

## 5) Why it matters for our work
- 这篇对我们最大的价值是“记忆工件化”：把长期经验变成可审计、可回滚、可版本治理的对象。
- 对长上下文路线有启发：与其无限堆 context，不如把复用行为压缩成 skill artifacts。
- 对 agent 系统工程有现实意义：training-free sidecar 方式接入成本低，适合先做产品级 A/B。

## 6) Actionable next step
- [ ] 复刻最小版 AutoSkill sidecar（rewrite + hybrid retrieve + async extract + merge）并记录每次 merge 的证据 span。  
- [ ] 做三路对照：`纯长上下文` vs `摘要记忆` vs `技能工件记忆`，统一比较成功率/延迟/token。  
- [ ] 增加技能回归评测：每个高频 skill 维护固定测试集，避免版本上升但质量回退。

## 7) 评分解释（必填）
- **质量分 x/2：** 1/2（架构清晰、工程可落地，但任务级对比证据不足）
- **Observation 分 y/2：** 1/2（“技能工件化”有启发，但尚未给强因果收益）
- **总分 z/5：** **3/5**
- **为什么不是更高分：**
  - 与主流 baseline（memory summary / vector memory / reflective memory）的效果对比：**原文未给出可提取数字**；
  - 消融（去 rewrite / judge / merge）的任务级指标：**原文未给出可提取数字**；
  - 统计显著性与误差报告：**原文未给出可提取数字**。
