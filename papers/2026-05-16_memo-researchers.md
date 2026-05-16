# Research Note — MeMo: Memory as a Model (Researcher Analysis)

## Paper Overview
- **Title:** MeMo: Memory as a Model
- **arXiv:** 2605.15156
- **Date:** 2026-05-14
- **Key Contribution:** 将新知识编码到独立的 memory model 中，保持 LLM 参数不变；plug-and-play 兼容开源和闭源 LLM；retrieval cost 与 corpus size 无关

**核心优势：**
- (a) 捕获跨文档复杂关系
- (b) 对 retrieval noise 鲁棒
- (c) 避免 catastrophic forgetting
- (d) 不需要 LLM weights/logits 访问（黑盒兼容）
- (e) 推理时检索成本与语料规模无关

**Benchmarks:** BrowseComp-Plus, NarrativeQA, MuSiQue

---

## Researcher Profiles

### Senior Authors (Why This Team Matters)

#### Daniela Rus — MIT CSAIL Director
- **Position:** MIT Panasonic Professor of CS; Director of CSAIL
- **Lab:** Distributed Robotics Laboratory
- **Recognition:** MacArthur Fellow (2002), IEEE Edison Medal (2025), NAS member (2024), NAE member (2015)
- **H-index:** ~130+（最被引用的机器人学家之一）
- **Research:** Robotics, mobile computing, data science, AI/ML, human-robot interaction
- **Relevance to MeMo:** Systems-level thinking — 部署 AI 到真实世界需要高效知识整合

#### Armando Solar-Lezama — MIT CSAIL
- **Position:** Professor, MIT EECS; leads Computer Assisted Programming Group
- **Research:** Program synthesis, neurosymbolic programming
- **Notable Work:** "Program Synthesis by Sketching" — 奠基性 program synthesis 工作
- **H-index:** ~50-60+
- **Relevance to MeMo:** Neurosymbolic 背景 → memory model 可能有 formal/compositional properties；把 memory 当作 learnable computational entity

#### Bryan Kian Hsiang Low — NUS
- **Position:** Professor, National University of Singapore; leads GLOW.AI lab
- **Research:** Data-Centric AI (data valuation, attribution, unlearning, distillation), Bayesian optimization, federated learning
- **H-index:** ~40-50+
- **Relevance to MeMo:** Data-centric 专长 → 知识如何被选择、编码、管理到 memory model 中；模块化/plug-and-play 设计

#### Nancy F. Chen — A*STAR Singapore
- **Position:** A*STAR Institute for Infocomm Research (I2R)
- **Research:** Speech/NLP, multilingual NLP, conversational AI
- **H-index:** ~30-40+
- **Relevance to MeMo:** NLP grounding，informed benchmark 选择和实际应用评估

---

## Team Composition Analysis

**MIT-Singapore 联合团队**，四个维度的专长完美互补：

```
Daniela Rus (MIT)          → 系统/部署视角
Armando Solar-Lezama (MIT) → 形式化/neurosymbolic 建模
Bryan K.H. Low (NUS)       → 数据管理/知识蒸馏
Nancy F. Chen (A*STAR)     → NLP/语言理解应用
```

**为什么这个组合对 memory paper 特别有意义：**
1. **黑盒兼容**的设计（不需要 LLM weights）需要 Solar-Lezama 的 formal modeling + Rus 的系统思维
2. **Retrieval cost independent of corpus size** 暗示可能有 learned compression/distillation 机制 → Low 的 data-centric 专长
3. MIT-Singapore axis 可能有 A*STAR-MIT Alliance 资助支撑
4. Junior authors (Quek, Lee, Leong, Verma, Prakash) 主要在 Singapore 做实现

**对我们的启示：** 这是一个"把 memory 当作一等公民 model 来训练"的方向 — 与 RAG 的"检索+拼接"或 fine-tuning 的"改 LLM 权重"都不同。值得密切关注后续论文。
