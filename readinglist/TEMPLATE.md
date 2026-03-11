# Reading List Table Template

> 用法：每篇论文一行；`Summary` 建议控制在 3-8 行要点。

## Markdown 表格模板

| Alias | Title | Source | Institution | Technique Tags | Scene | Benchmarking | ⭐ | Framework | Summary |
|---|---|---|---|---|---|---|---:|---|---|
| Paper-Alias | Paper Title | https://arxiv.org/... | Org / University | Tag1, Tag2 | Math, Tool Use | Benchmark1, Benchmark2 | 0.0-5.0 | 简述框架 | 1) 核心洞察；2) 方法亮点；3) 结果与局限 |

## CSV 表头模板（与上表一致）

```csv
Alias,Title,Source,Institution,Technique Tags,Scene,Benchmarking,⭐,Framework,Summary
```

## 示例（参考你给的 Evo-Memory）

| Alias | Title | Source | Institution | Technique Tags | Scene | Benchmarking | ⭐ | Framework | Summary |
|---|---|---|---|---|---|---|---:|---|---|
| Evo-Memory | Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory | https://arxiv.org/pdf/2511.20857 | Google DeepMind | Zero-shot Pipeline | Math, Agentic Tool Using | MMLU-Pro, GPQA-Diamond, AIME24/25, ToolBench, AlfWorld, BabyAI, ScienceWorld | 4.5 | ExpRAG + ReMem | 提出测试时“自进化记忆”；ExpRAG做经验检索，ReMem做 think-act-memory refine 循环；多任务下显著优于仅会话回忆。 |
