# 01.me 文章阅读笔记

## 0) Metadata
- **Title:** The Dilemma of Continuous Learning for Agents: Why a Reasoner Is Not a True Agent
- **Alias:** 01me-Agent-Continual-Learning
- **Type:** Blog / Research Talk
- **Link:** https://01.me/en/2025/10/agent-continual-learning/
- **My rating:** ★★★☆☆
- **Read depth:** normal
- **Scoring (1+2+2):** 基础 1 + 质量 0 + Observation 2 = 3

## 1) Core Insight
- “Reasoner ≠ Agent”的分水岭是持续学习能力，而不是单轮推理强弱。

## 2) Interesting Observations
- 长上下文本身不会自动蒸馏知识，memory 需要主动结构化与可检索组织。
- 仅 reward 学习不足，observation 学习（world-model 侧）应并行建模。
- 实时 Agent 应从 ReAct 串行转向 event-driven 并发循环。

## 3) Evidence / Claims
- 文章以系统经验与架构论证为主，提出 Dual-LoRA（policy/world-model 解耦）方向。

## 4) Why It Matters for Your Work
- 直接呼应你的主线：长期记忆与在线演化不能只靠“更多上下文”，要有内化机制。

## 5) Actionable Next Step
- 设计小实验：policy loss + observation prediction loss 双头训练。

## 6) Why not higher score
- 不是更高分的原因：观点强，但缺系统化公开实证。
