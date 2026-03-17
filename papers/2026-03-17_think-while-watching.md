# Think-While-Watching 阅读笔记

## 0) Metadata
- **Title:** Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models
- **Alias:** Think-While-Watching
- **Authors / Org:** Lu Wang, Zhuoran Jin, Yupu Hao, Yubo Chen, Kang Liu, Yulong Ao, Jun Zhao；First: Institute of Automation, Chinese Academy of Sciences; High-impact: BAAI
- **Venue / Status:** arXiv 2603.11896v1
- **Date:** 2026-03
- **Links:**
  - Abs: https://arxiv.org/abs/2603.11896
  - PDF: https://arxiv.org/pdf/2603.11896
  - HTML: https://arxiv.org/html/2603.11896
  - Code: https://github.com/wl666hhh/Think_While_Watching/
- **Tags:** streaming-video, multimodal-agent, online-reasoning, memory, long-context
- **My rating (1-3):** 4.6
- **Read depth:** normal

## 1) TL;DR
- 目标是解决 MLLM 在**连续视频流 + 多轮问答**下的在线推理问题。
- 现有 streaming 方法常用“感知-生成交替”范式，导致不能并行、且随时间出现记忆衰减。
- 论文提出 **memory-anchored segment-level streaming** 框架，并用 segment-level causal mask + streaming positional encoding 保因果性。
- 推理阶段通过 watch/thinking pipeline overlap 提升吞吐。
- 基于 Qwen3-VL，在 StreamingBench +2.6%，OVO-Bench +3.79%，多轮设置下输出 token 降低 56%。

## 2) Problem & Motivation
- 以前方法的核心缺口：在线流式场景中长期依赖建模弱，且多轮交互效率低。
- 这篇 paper 想解决什么：维持连续段级记忆并提升多轮视频推理质量/效率。
- 为什么现在值得做：实时多模态 agent（监控、助手、机器人）对在线处理和长时记忆需求强。

## 3) Method (结构化)
### 3.1 Setting / Formulation
- 连续到达的视频片段 + 多轮问题，要求严格因果，不可偷看未来帧。

### 3.2 Main Components
- Component A: 段级记忆锚定（segment-level memory anchoring）。
- Component B: streaming causal mask + streaming positional encoding。
- Component C: 推理时 perception / reasoning overlap pipeline。

### 3.3 What is actually new?
- 相比最强相关工作，新增点：在线段级记忆机制与“边看边想”的并行推理设计。
- 可能只是 engineering 的部分：attention backend 的自适应选择。

## 4) Experiments & Evidence
### 4.1 Benchmarks / Tasks
- StreamingBench, OVO-Bench；单轮与多轮 streaming 协议。

### 4.2 Main Results (with concrete numbers)
- 单轮：StreamingBench +2.6%，OVO-Bench +3.79%。
- 多轮：性能维持同时输出 token -56%。

### 4.3 Ablation / Analysis
- 关键应看：去掉段级记忆、去掉流式 mask、去掉并行 pipeline 的退化幅度。

### 4.4 Failure / Limitation
- 对高帧率、超长时长视频的显存/延迟成本仍可能较高。

## 5) My Technical Take
### 5.1 What I believe
- 这篇和你的多模态 agent + 长程记忆兴趣高度对齐，尤其是“在线记忆不坍塌”这一点。

### 5.2 What I doubt
- 目前提升幅度不错，但跨数据域稳健性和长时漂移修复策略还需正文证据。

### 5.3 Transfer to our projects
- 可直接迁移：segment-level memory abstraction + 因果 mask 设计。
- 需要改造后迁移：与现有检索/记忆模块统一接口。
- 暂不建议投入：端侧资源非常受限场景。

## 6) Repro Checklist
- [x] 任务定义清晰
- [ ] 评测协议可复现（需正文细节）
- [ ] baseline 公平（需正文细节）
- [ ] 资源开销可接受（需真实 profile）
- [x] 代码/数据可得（代码已给）

## 7) Next Actions (for me)
- [ ] 拉代码看 streaming positional encoding 实现。
- [ ] 提取多轮 benchmark 的误差类型。
- [ ] 对比你现有视频记忆策略的可替换点。
