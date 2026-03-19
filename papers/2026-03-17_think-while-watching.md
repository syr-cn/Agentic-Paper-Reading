# Think-While-Watching 阅读笔记

## 0 Metadata
- **Title:** Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models
- **Alias:** Think-While-Watching
- **Authors / Org:** Lu Wang, Zhuoran Jin, Yupu Hao, Yubo Chen, Kang Liu, Yulong Ao, Jun Zhao；First: CASIA; High-impact: BAAI
- **Venue / Status:** arXiv 2603.11896v1
- **Date:** 2026-03
- **Links:**
  - Abs: https://arxiv.org/abs/2603.11896
  - PDF: https://arxiv.org/pdf/2603.11896
  - HTML: https://arxiv.org/html/2603.11896
  - Code: https://github.com/wl666hhh/Think_While_Watching/
- **Tags:** streaming-video, multimodal-agent, online-reasoning, memory, long-context
- **My rating:** ★★★★☆
- **Read depth:** normal
- **Scoring (1+2+2):** 基础 1 + 质量 2 + Observation 1 = 4

## 1 一句话 Why-read
- 真正有意思的不是“流式视频更快了”，而是它把**记忆单元从 frame-level 提升到 segment-level**，并在因果约束下实现“边看边想”的并行推理，缓解了多轮交互里的记忆衰减。

## 2 CRGP
### C — Context
- 真正有意思的不是“流式视频更快了”，而是它把**记忆单元从 frame-level 提升到 segment-level**，并在因果约束下实现“边看边想”的并行推理，缓解了多轮交互里的记忆衰减。

### R — Related work
- - **Observation 1（效率）**：在多轮设置里，输出 token 可降约 56%，说明方法不仅增准，还显著减少无效推理开销。

### G — Research gap
- 待补证据（需从原文引言补充明确 gap 描述）

### P — Proposal
- - 证据：在两类 streaming benchmark 的单轮与多轮协议下均有收益。

## 3 Figure 区
- 待补证据（建议补 1 张方法图或主结果图）
- 可定位链接：  - Abs: https://arxiv.org/abs/2603.11896
  - PDF: https://arxiv.org/pdf/2603.11896
  - HTML: https://arxiv.org/html/2603.11896
  - Code: https://github.com/wl666hhh/Think_While_Watching/

## 4 Experiments
### 4.1 Experimental setup
- 证据：在两类 streaming benchmark 的单轮与多轮协议下均有收益。
- 限制：超长视频和高帧率场景下的资源成本曲线仍需更多公开 profile。

### 4.2 Main result table
| Setting | Baseline | Proposed | Delta |
|---|---:|---:|---:|
| 原文摘要 | 原文未给出可提取数字 | 原文未给出可提取数字 | 原文未给出可提取数字 |

### 4.3 Analysis
- **现象：** **Observation 1（效率）**：在多轮设置里，输出 token 可降约 56%，说明方法不仅增准，还显著减少无效推理开销。
  **解释（作者）：** 待补证据。
  **【标注】（我的判断，可选）：** 待补证据。

## 5 Why it matters for our work
- 你做多模态记忆系统时，最痛点是“在线长程依赖崩掉”；这篇提供了一个可直接借鉴的**段级记忆抽象**。

## 6 Actionable next step
- 把你现有视频/轨迹记忆模块改成 segment-level 索引做 A/B。
- 单独测三项：正确率、延迟、token开销（尤其多轮）。

## 7 评分解释
- 维持原评分倾向，不做无根据上调。
- 不是更高分的原因：observation 还偏系统工程层，机制性 failure 分析不够深入。
