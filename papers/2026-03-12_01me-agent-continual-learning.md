# 01.me 文章阅读笔记

## 0) Metadata
- **Title:** The Dilemma of Continuous Learning for Agents: Why a Reasoner Is Not a True Agent
- **Alias:** 01me-Agent-Continual-Learning
- **Author / Org:** 01.me
- **Type:** Blog / Research Talk
- **Date:** 2025-10
- **Link:** https://01.me/en/2025/10/agent-continual-learning/
- **Tags:** continual-learning, agent-vs-reasoner, world-model, dual-lora, realtime-agent
- **My rating (★☆☆ / ★★☆ / ★★★):** 4.6
- **Read depth:** normal

## 1) TL;DR
- 文章核心观点：**Reasoner ≠ Agent**，真正 Agent 的分水岭是“持续学习能力”。
- 批判当前主流 RL（PPO/GRPO）样本效率低、只能从 reward 学习，难以利用环境反馈（observation）。
- 提出实践方向：通过 Dual LoRA 将 policy learning 与 world-model learning 解耦并行训练。
- 强调“长上下文不是自动知识蒸馏器”，memory 的关键是结构化抽取与可检索组织。

## 2) 关键观点
- Big World Hypothesis：世界信息无限，Agent 必须在任务中持续学习，而不是依赖一次性预训练。
- 上下文的本质更接近检索，不会自动完成规则归纳；需要主动 summary / structuring。
- 从工程上，Agent 架构应支持 think-while-listening / speak-while-thinking 的事件驱动模式。

## 3) 方法与启发（对我们研究）
- 可迁移 1：在 agent 训练里显式加入 observation prediction loss（类 world-model）。
- 可迁移 2：memory 从“日志堆积”升级为“规则提炼 + 检索触发”。
- 可迁移 3：对实时交互任务采用 Event-driven loop，降低 ReAct 串行等待损耗。

## 4) 局限与注意
- 博客含较多观点性推断，严格证据链不如论文完整。
- Dual LoRA 方案需要更多公开对照实验支撑。

## 5) Next Actions
- [ ] 做一版 policy loss + observation loss 的双头训练小实验。
- [ ] 在记忆模块里区分“事实卡片”和“策略规则卡片”。
