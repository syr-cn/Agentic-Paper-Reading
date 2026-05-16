# Memory & Long-Horizon Reading List

> Memory systems + evaluation + Long-horizon reasoning + context management

### Memory Systems

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [Evo-Memory](../papers/2026-03-11_evo-memory.md) | Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory | [arXiv 2511.20857](https://arxiv.org/abs/2511.20857) | First: DeepMind; High-impact: DeepMind | C | 5 | 4 | ![fig1](https://arxiv.org/html/2511.20857v1/x1.png) | LLM Agent 的记忆应在部署中持续从经验学习并自我演化；自演化记忆在多轮任务中大幅提升表现和效率。 |
| [MemMA](../papers/2026-03-28_memma.md) | MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution | [arXiv 2603.18718](https://arxiv.org/abs/2603.18718) | First: Penn State; High-impact: Microsoft | — | — | — | [Fig.1](https://arxiv.org/html/2603.18718v1/x1.png) | 首次将记忆系统建模为前向+反向双路径闭环；in-situ self-evolving（probe QA → verify → repair）是比 retrieval tuning 更本质的记忆质量保障；plug-and-play 在 Single-Agent 上 ACC 52.60→84.87（+32.27），直接对标 ReMemR1。 |
| [GEMS](../papers/2026-04-01_gems.md) | GEMS: Agent-Native Multimodal Generation with Memory and Skills | [arXiv 2603.28088](https://arxiv.org/abs/2603.28088) | First: N/A; High-impact: N/A | — | — | — | [Fig.1](https://arxiv.org/html/2603.28088v1/x2.png) | 将 T2I 生成重构为 agentic 迭代优化（Loop+Memory+Skill）；核心发现：compressed experience memory 比 raw traces 有效（+2.5 vs +0）；6B 轻量模型超 Nano Banana 2（GenEval2 63.5 vs 60.7）。 |
| [Unify-Agent](../papers/2026-04-02_unify-agent.md) | Unify-Agent: Towards Unified Visual Generation and Understanding via Agent | [arXiv 2603.29620](https://arxiv.org/abs/2603.29620) | First: UCLA; High-impact: Tencent Hunyuan | — | — | — | N/A | 用 agent 框架统一视觉生成与理解；核心发现：generation helps understanding（VAE+ViT synergy）；FactIP 73.2 vs Bagel 50.9（+22.3），KiTTEN 4.08 new SOTA。 |
| [ByteRover](../papers/2026-04-07_agent-native-memory.md) | Agent-Native Memory Through LLM-Curated Hierarchical Context | [arXiv 2604.01599](https://arxiv.org/abs/2604.01599) | First: N/A; High-impact: N/A | — | — | — | N/A | LLM 自主整理的层次化 agent 记忆架构，文件级知识图谱 + 渐进检索；与 ReMemR1 方向直接可比。 |
| [Memory-Forgetting](../papers/2026-04-07_memory-forgetting.md) | Novel Memory Forgetting Techniques for Autonomous AI Agents | [arXiv 2604.02280](https://arxiv.org/abs/2604.02280) | First: N/A; High-impact: N/A | — | — | — | [Fig.1](https://arxiv.org/html/2604.02280v1/arch_abff.png) | 自适应遗忘框架（relevance scoring + temporal decay + budget constraint）防止 agent 记忆无限膨胀；选题好但实验偏弱。 |
| [MIA](../papers/2026-04-08_mia.md) | Memory Intelligence Agent | [arXiv 2604.04503](https://arxiv.org/abs/2604.04503) | First: N/A; High-impact: N/A | — | — | — | N/A | 双阶段交替 RL（planner+executor）训练 agent 终身记忆；非参数记忆做对比经验 + 参数记忆做长期固化；跨模型一致提升。 |

### Memory Evaluation

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [MemLens](../papers/2026-05-16_memlens.md) | MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models | [arXiv 2605.14906](https://arxiv.org/abs/2605.14906) | First: NVIDIA; High-impact: NVIDIA + HKUST | C | 5 | 4 | N/A（HTML 暂未公开） | 首个系统对比 long-context LVLMs vs memory-augmented agents 的多模态 benchmark；789 questions × 5 abilities × 4 lengths；核心发现：前者随 context 退化，后者丢视觉保真度，MSR <30%。 |
| [MemEye](../papers/2026-05-16_memeye.md) | MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory | [arXiv 2605.15128](https://arxiv.org/abs/2605.15128) | First: Rutgers; High-impact: Princeton (Mengdi Wang) | C | 5 | 4 | ![fig1](https://arxiv.org/html/2605.15128v1/x4.png) | 2D evaluation matrix (X=视觉粒度 scene→pixel, Y=推理深度 atomic→evolving)；13 方法×4 backbone；核心发现：semantic similarity ≠ temporal validity，fine-grained + evolving state 是 compound failure zone。 |

### Long-Horizon & Context

| Alias (link to note) | Title | Source | Institution | Type | Rel | Qual | Figure 1 | Summary |
|---|---|---|---|:---:|:---:|:---:|---|---|
| [Think-While-Watching](../papers/2026-03-17_think-while-watching.md) | Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models | [arXiv 2603.11896](https://arxiv.org/abs/2603.11896) | First: CASIA; High-impact: BAAI | — | — | — | N/A（arXiv 未提供可用 HTML Figure 资源） | 核心贡献是 segment-level 在线记忆 + watch/thinking 解耦：多轮流式场景在保持准确率的同时显著降 token 与 TTFT，缓解 memory erosion。 |
| [Reasoning-Shift](../papers/2026-04-07_reasoning-shift.md) | Reasoning Shift: How Context Silently Shortens LLM Reasoning | [arXiv 2604.01161](https://arxiv.org/abs/2604.01161) | First: N/A; High-impact: N/A | — | — | — | N/A | 揭示 reasoning 模型在长 context/多轮场景中推理链默默缩短 50%；self-verification 退化是关键机制；对 agentic reasoning 系统设计有直接警示意义。 |
| [BCR](../papers/2026-04-07_bcr.md) | Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning | [arXiv 2604.02322](https://arxiv.org/abs/2604.02322) | First: N/A; High-impact: N/A | — | — | — | [Fig.1](https://arxiv.org/html/2604.02322v1/x1.png) | 多题 batching 创造资源竞争，激活 LLM 隐藏的高密度推理模式，token 减少 92% 且准确率不降；发现 task-scaling law。 |
| [ContextBudget](../papers/2026-04-08_context-budget.md) | ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents | [arXiv 2604.01664](https://arxiv.org/abs/2604.01664) | First: N/A; High-impact: N/A | — | — | — | N/A | 将 context management 建模为 budget-constrained 决策问题；30B 8k budget 超越 235B 128k；对比 Search-R1 和 MEM1。 |