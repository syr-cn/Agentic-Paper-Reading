# Skill Reading List

> Skill evolution, skill benchmark, continual learning via skills

## Skill Discovery & Library

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [SkillRL](../papers/2026-03-11_skillrl.md) | Evolving Agents via Recursive Skill-Augmented Reinforcement Learning | [arXiv 2602.08234](https://arxiv.org/abs/2602.08234) | First: N/A; High-impact: N/A | — | — | — | [Fig.1](https://arxiv.org/html/2602.08234v1/x1.png) | 论文证明"轨迹记忆→技能记忆+递归演化"有效：复杂子任务增益大、收敛更快，并带来约 10.3% 上下文 token 缩减。 |
| SkillNet | SkillNet: Create, Evaluate, and Connect AI Skills | [arXiv 2603.04448](https://arxiv.org/abs/2603.04448) | First: ZJU (zjunlp); High-impact: ZJU | — | — | — | N/A | npm for AI Skills；异构来源创建+关系连接+评估。 |
| [AutoSkill](../papers/2026-03-11_autoskill.md) | Experience-Driven Lifelong Learning via Skill Self-Evolution | [arXiv 2603.01145](https://arxiv.org/abs/2603.01145) | First: ECNU; High-impact: Shanghai AI Lab | — | — | — | [Fig.1](https://arxiv.org/html/2603.01145v2/x1.png) | 把长期经验沉淀为可版本化 SKILL.md 并异步 merge/演化；工程价值在 training-free 个性化闭环。 |
| Trace2Skill | Trace2Skill: Distill Trajectory-Local Lessons into Transferable Skills | [arXiv 2603.25158](https://arxiv.org/abs/2603.25158) | First: N/A; High-impact: N/A | — | — | — | N/A | 并行 sub-agent fleet 归纳 → 统一 skill directory；证明经验可蒸馏为 transferable skills。 |
| SkillX | SkillX: Automatically Constructing Skill Knowledge Bases | [arXiv 2604.04804](https://arxiv.org/abs/2604.04804) | First: ZJU (zjunlp); High-impact: ZJU | — | — | — | N/A | 三级粒度: strategic→functional→atomic skill taxonomy。 |
| SkillClaw | SkillClaw: Let Skills Evolve Collectively with Agentic Evolver | [arXiv 2604.08377](https://arxiv.org/abs/2604.08377) | First: N/A; High-impact: N/A | — | — | — | N/A | 跨用户集体进化；cross-user knowledge transfer。 |
| Ctx2Skill | Ctx2Skill: From Context to Skills | [arXiv 2604.27660](https://arxiv.org/abs/2604.27660) | First: Tsinghua; High-impact: Tsinghua + UIUC | — | — | — | N/A | Multi-agent self-play；Cross-time Replay 防 collapse。 |

## Skill-Augmented RL

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [ARISE](../papers/2026-03-19_arise.md) | ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical RL | [arXiv 2603.16060](https://arxiv.org/abs/2603.16060) | First: GWU; High-impact: UT Dallas | — | — | — | https://arxiv.org/html/2603.16060v1 | 把"选 skill—解题—写 skill"并入同一 RL 策略闭环，关键收益来自把 skill 使用与更新内生到 policy gradient，而非外挂检索器。 |
| SLEA-RL | SLEA-RL: Step-Level Experience Augmented RL | [arXiv 2603.18079](https://arxiv.org/abs/2603.18079) | First: CMU; High-impact: CMU | — | — | — | N/A | 每步注入细粒度经验；更快收敛。 |
| D2Skill | D2Skill: Dynamic Dual-Granularity Skill Bank for Agentic RL | [arXiv 2603.28716](https://arxiv.org/abs/2603.28716) | First: N/A; High-impact: N/A | — | — | — | N/A | Task skills (高层) + step skills (纠错)；paired rollouts 计算 hindsight utility。 |
| COSPLAY | COSPLAY: Co-Evolving LLM Decision and Skill Bank Agents | [arXiv 2604.20987](https://arxiv.org/abs/2604.20987) | First: N/A; High-impact: N/A | — | — | — | N/A | Decision agent + skill bank agent 协同进化；8B 超 frontier +25.1%。 |
| SAGE | SAGE: RL for Self-Improving Agent with Skill Library | [arXiv 2512.17102](https://arxiv.org/abs/2512.17102) | First: Amazon; High-impact: Amazon | — | — | — | N/A | Skill Augmented GRPO；Sequential Rollout 跨同类任务迭代。 |
| Skill1 | Skill1: Unified Evolution of Skill-Augmented Agents via RL | [arXiv 2605.06130](https://arxiv.org/abs/2605.06130) | First: ZJU-REAL; High-impact: ZJU-REAL + Meituan | — | — | — | N/A | 统一 co-evolve selection/utilization/distillation；当前 SOTA。 |
| SkillFlow | SkillFlow: Flow-Driven Recursive Skill Evolution | [arXiv 2605.14089](https://arxiv.org/abs/2605.14089) | First: N/A; High-impact: N/A | — | — | — | N/A | Tempered Trajectory Balance flow-matching loss。 |
| [Comp-RL](../papers/2026-03-23_comp-rl.md) | Complementary Reinforcement Learning | [arXiv 2603.17621](https://arxiv.org/abs/2603.17621) | First: Alibaba Group; High-impact: HKUST | — | — | — | ![fig1](https://arxiv.org/html/2603.17621v1/x1.png) | 受 CLS 启发的 actor-extractor 共演化 RL 框架：静态经验随训练变为负资产，共演化闭环单任务 1.3× margin + 多任务 +7%；split-group GRPO 防止 actor 对经验过度依赖；异步训练零额外延迟；6-task 扩展增益不衰减（+8.1%）。 |

## Skill Lifecycle & Curation

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| SkillOS | SkillOS: Learning Skill Curation for Self-Evolving Agents | [arXiv 2605.06614](https://arxiv.org/abs/2605.06614) | First: N/A; High-impact: N/A | — | — | — | N/A | Curation 建模为 RL 问题；frozen executor + trainable curator；跨 backbone 泛化。 |
| SLIM | SLIM: Dynamic Skill Lifecycle Management for Agentic RL | [arXiv 2605.10923](https://arxiv.org/abs/2605.10923) | First: N/A; High-impact: N/A | — | — | — | N/A | Leave-one-skill-out → retain/retire/expand；发现 policy learning 和 external skill 不互斥。 |
| [SkillOrchestra](../papers/2026-03-11_skillorchestra.md) | SkillOrchestra: Learning to Route Agents via Skill Transfer | [arXiv 2602.19672](https://arxiv.org/abs/2602.19672) | First: UW-Madison; High-impact: Salesforce AI Research | — | — | — | N/A | 用"技能需求"而非 query 相似度做路由，能缓解 RL 路由 collapse，并在性能-成本 Pareto 上更稳。 |

## Experience & Memory (Skill-adjacent)

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| SimpleMem | SimpleMem: Efficient Lifelong Memory for LLM Agents | [arXiv 2601.02553](https://arxiv.org/abs/2601.02553) | First: N/A; High-impact: N/A | — | — | — | N/A | 高效 lifelong memory；Pareto 最优。 |
| MemRL | MemRL: Self-Evolving Agents via Runtime RL on Episodic Memory | [arXiv 2601.03192](https://arxiv.org/abs/2601.03192) | First: N/A; High-impact: N/A | — | — | — | N/A | Runtime RL on episodic memory；不修改权重。 |
| CLEANER | CLEANER: Self-Purified Trajectories Boost Agentic RL | [arXiv 2601.15141](https://arxiv.org/abs/2601.15141) | First: N/A; High-impact: N/A | — | — | — | N/A | SAAR 机制替换失败片段；1/3 训练步数达 SOTA。 |
| ProcMEM | ProcMEM: Learning Reusable Procedural Memory via Non-Parametric PPO | [arXiv 2602.01869](https://arxiv.org/abs/2602.01869) | First: N/A; High-impact: N/A | — | — | — | N/A | Semantic Gradients + PPO Gate；无参数更新的 skill-level 优化。 |
| [MemSkill](../papers/2026-03-11_memskill.md) | Learning and Evolving Memory Skills for Self-Evolving Agents | [arXiv 2602.02474](https://arxiv.org/abs/2602.02474) | First: N/A; High-impact: N/A | — | — | — | [Fig.1](https://arxiv.org/html/2602.02474v1/x1.png) | 把记忆操作做成可检索、可演化 skill（controller/executor/designer）是核心贡献；消融显示去掉 designer 退化最大，说明"持续增量技能"是关键而非静态记忆规则。 |
| CLEAR | CLEAR: Context Augmentation from Contrastive Learning | [arXiv 2604.07487](https://arxiv.org/abs/2604.07487) | First: N/A; High-impact: N/A | — | — | — | N/A | 对比分析轨迹 → Context Augmentation Model；AppWorld 72.6→81.2%。 |
| [XSkill](../papers/2026-03-17_xskill.md) | XSkill: Continual Learning from Experience and Skills in Multimodal Agents | [arXiv 2603.12056](https://arxiv.org/abs/2603.12056) | First: N/A; High-impact: N/A | — | — | — | https://arxiv.org/html/2603.12056/x1.png | 将持续学习拆成 experience（动作级）与 skill（任务级）双记忆流，并在视觉上下文中检索-改写-注入，training-free 仍能稳定提升多模态 agent。 |
| MetaClaw | MetaClaw: Continual Meta-Learning for LLM Agents | [arXiv 2603.17187](https://arxiv.org/abs/2603.17187) | First: N/A; High-impact: N/A | — | — | — | N/A | Continual meta-learning for agents。 |
| [RetroAgent](../papers/2026-03-12_retroagent.md) | RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback | [arXiv 2603.08561](https://arxiv.org/abs/2603.08561) | First: SAIL; High-impact: NUS | — | — | — | https://arxiv.org/html/2603.08561/x1.png | 用数值内在奖励（探索进展）+语言内在反馈（经验复用）联合驱动"求解→进化"，改进来自持续演化能力而非单次解题技巧。 |

## Benchmarks & Surveys

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [SoK-Agentic-Skills](../papers/2026-03-11_sok-agentic-skills.md) | Agentic Skills — Beyond Tool Use in LLM Agents | [arXiv 2602.20867](https://arxiv.org/abs/2602.20867) | First: N/A; High-impact: N/A | — | — | — | [Fig.1](https://arxiv.org/html/2602.20867v1/figures/skill-anatomy/figure.png) | 贡献在系统化：给出 skill 四元组与生命周期框架，并把供应链安全纳入同一评估视角。 |
| [Agent-Skills-Survey](../papers/2026-03-11_agent-skills-survey.md) | Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward | [arXiv 2602.12430](https://arxiv.org/abs/2602.12430) | First: N/A; High-impact: N/A | — | — | — | [Fig.1](https://arxiv.org/html/2602.12430v3/x1.png) | 价值在于把 architecture/acquisition/security/gov 串成一张图，并用大规模安全统计强调 skill 生态的治理刚需。 |
| [SkillsBench](../papers/2026-03-11_skillsbench.md) | Benchmarking How Well Agent Skills Work Across Diverse Tasks | [arXiv 2602.12670](https://arxiv.org/abs/2602.12670) | First: N/A; High-impact: N/A | — | — | — | N/A | 最关键结论：人工 curated skills 平均 +16.2pp，而 self-generated skills 平均退化（-3.3pp pass rate），说明 skill 质量控制比数量更重要。 |
| KARL | KARL: Knowledge Agents via Reinforcement Learning | [arXiv 2603.05218](https://arxiv.org/abs/2603.05218) | First: N/A; High-impact: N/A | — | — | — | N/A | Multi-step evidence-grounded reasoning；匹配 Claude Opus @ 47% lower latency。 |
| SkillLearnBench | SkillLearnBench: Benchmarking Continual Learning for Skill Generation | [arXiv 2604.20087](https://arxiv.org/abs/2604.20087) | First: CMU; High-impact: CMU | — | — | — | N/A | 20 tasks × 15 sub-domains；无方法一致领先。 |
| SkillFlow-Bench | SkillFlow Benchmark: Lifelong Skill Discovery and Evolution | [arXiv 2604.17308](https://arxiv.org/abs/2604.17308) | First: N/A; High-impact: N/A | — | — | — | N/A | 166 tasks × 20 families；creation-reuse coordination gap。 |
| Skill-Retrieval-Aug | Skill Retrieval Augmentation for Agentic AI | [arXiv 2604.24594](https://arxiv.org/abs/2604.24594) | First: N/A; High-impact: N/A | — | — | — | N/A | SkillsMP 平台 100w+ skills。 |
