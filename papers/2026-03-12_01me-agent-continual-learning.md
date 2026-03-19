# 01.me 文章阅读笔记

## 0 Metadata
- **Title:** The Dilemma of Continuous Learning for Agents: Why a Reasoner Is Not a True Agent
- **Alias:** 01me-Agent-Continual-Learning
- **Type:** Blog / Research Talk
- **Link:** https://01.me/en/2025/10/agent-continual-learning/
- **My rating:** ★★★☆☆
- **Read depth:** normal
- **Scoring (1+2+2):** 基础 1 + 质量 0 + Observation 2 = 3

## 1 一句话 Why-read
- “Reasoner ≠ Agent”的分水岭是持续学习能力，而不是单轮推理强弱。

## 2 CRGP
### C — Context
- “Reasoner ≠ Agent”的分水岭是持续学习能力，而不是单轮推理强弱。

### R — Related work
- - 长上下文本身不会自动蒸馏知识，memory 需要主动结构化与可检索组织。

### G — Research gap
- 待补证据（需从原文引言补充明确 gap 描述）

### P — Proposal
- - 文章以系统经验与架构论证为主，提出 Dual-LoRA（policy/world-model 解耦）方向。

## 3 Figure 区
- N/A（非论文/博客条目）

## 4 Experiments
### 4.1 Experimental setup
- 文章以系统经验与架构论证为主，提出 Dual-LoRA（policy/world-model 解耦）方向。

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 原文摘要 | 原文未给出可提取数字 | 原文未给出可提取数字 | 原文未给出可提取数字 |

### 4.3 Analysis
- **现象：** 长上下文本身不会自动蒸馏知识，memory 需要主动结构化与可检索组织。
  **解释（作者）：** 待补证据。
  **【标注】（我的判断，可选）：** 待补证据。

## 5 Why it matters for our work
- 直接呼应你的主线：长期记忆与在线演化不能只靠“更多上下文”，要有内化机制。

## 6 Actionable next step
- 设计小实验：policy loss + observation prediction loss 双头训练。

## 7 评分解释
- 维持原评分倾向，不做无根据上调。
- 不是更高分的原因：观点强，但缺系统化公开实证。
