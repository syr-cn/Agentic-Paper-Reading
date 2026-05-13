# PAPER_PREFERENCES.md

> 本文件与 RESEARCH_PREFERENCES.md 的评分准则保持同步。最后更新：2026-05-13。

## Primary Interests (High Priority)
1. Agentic memory systems (episodic/semantic/procedural memory for agents)
2. **Memory evaluation & benchmarks** (LongMemEval-V2, MEME style — diagnosing failure modes, multi-entity/evolving evaluation)
3. Long-context reasoning and revisitable memory
4. Retrieval-augmented reasoning (not only retrieval-augmented generation)
5. Multi-modal memory for agents (vision-language-action)
6. RL for tool-using / planning agents

## Secondary Interests
- Scientific literature understanding and automation
- Efficient memory compression, indexing, replay, and forgetting
- Test-time compute × memory interaction
- Training-time curriculum for memory capabilities
- Continual learning / online adaptation for agents (Fast-and-Slow, Continual Harness style)
- Self-improving / self-evolving agents

## Three Method Types (Master 2026-05-13 手写)

论文按方法类型分类，不同类型用不同标准评判：

| 类型 | 描述 | 发论文方便性 | 理念先进性要求 |
|------|------|-------------|---------------|
| **Type A: RL Training** | evolving/自进化/memory/long-horizon 的训练方法 | 最高 | 相对宽容 |
| **Type B: Harness Engineering** | 不训练但系统设计/理念有价值 | 最低 | 最高 |
| **Type C: Benchmark** | 对问题本身的看法有价值 | 中等 | 最高 |

理念先进性排序：benchmark ≈ harness > training
发论文方便性排序：training > benchmark > harness

## Dual-Dimension Scoring (双维度评分)

每篇论文两个独立维度，各 5 分制，不合并：

### 维度一：话题相关性（Relevance）
- 5 = 核心命中（agentic memory / long-context / memory evaluation）
- 4 = 强相关（RL for agents, evolving, harness engineering）
- 3 = 有启发（方法论可迁移）
- 2 = 边缘相关
- 1 = 无关

### 维度二：论文质量（Quality）
按类型分别评判：
- **指标 1**：作者/机构影响力（citation、大组、大公司）
- **指标 2**：叙事逻辑 + related work + 方法质量
- **指标 3**：性能提升幅度 + 有趣实验现象

评分标准详见 RESEARCH_PREFERENCES.md § 评分准则。

## Priority Sources
- arXiv: cs.CL, cs.AI, cs.LG, cs.CV
- HuggingFace Daily Papers (prefer to keep strong coverage)
- Top venues: NeurIPS / ICLR / ICML / ACL / EMNLP / CVPR

## Balance Constraint
When generating daily picks, avoid source collapse:
- keep at least ~30% from HuggingFace Daily Papers when candidate quality is comparable
- avoid all-venue domination by a single source

## Output Tone Preference
- concise, technical, non-marketing
- avoid fluffy AI-style phrasing
- prefer concrete claims with evidence pointers
