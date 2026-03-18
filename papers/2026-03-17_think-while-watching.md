# Think-While-Watching 阅读笔记

## 0) Metadata
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

## 1) Core Insight
- 真正有意思的不是“流式视频更快了”，而是它把**记忆单元从 frame-level 提升到 segment-level**，并在因果约束下实现“边看边想”的并行推理，缓解了多轮交互里的记忆衰减。

## 2) Interesting Observations
- **Observation 1（效率）**：在多轮设置里，输出 token 可降约 56%，说明方法不仅增准，还显著减少无效推理开销。
- **Observation 2（性能）**：StreamingBench +2.6%、OVO-Bench +3.79%，增益不是极端大，但在 streaming 任务里属于稳定可复现实用收益。
- **Observation 3（系统）**：perception/reasoning overlap 的 pipeline 设计，对线上实时 agent 的 latency profile 很关键。

## 3) Method
- 段级在线记忆锚定（segment-level memory anchoring）
- streaming causal mask + streaming positional encoding（保证严格因果）
- watch/thinking overlap pipeline（提高吞吐）

## 4) Evidence & Limitations
- 证据：在两类 streaming benchmark 的单轮与多轮协议下均有收益。
- 限制：超长视频和高帧率场景下的资源成本曲线仍需更多公开 profile。

## 5) Why It Matters for Your Work
- 你做多模态记忆系统时，最痛点是“在线长程依赖崩掉”；这篇提供了一个可直接借鉴的**段级记忆抽象**。

## 6) Actionable Next Step
- 把你现有视频/轨迹记忆模块改成 segment-level 索引做 A/B。
- 单独测三项：正确率、延迟、token开销（尤其多轮）。

## 7) Why not higher score
- 不是更高分的原因：observation 还偏系统工程层，机制性 failure 分析不够深入。
