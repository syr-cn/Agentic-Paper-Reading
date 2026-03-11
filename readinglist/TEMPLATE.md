# Reading List Table Template

> 用法：每篇论文一行；`Summary` 建议控制在 3-8 行要点。

## Markdown 表格模板

| Alias | Title | Source | Institution | Benchmarking | ⭐ | Figure 1 | Summary |
|---|---|---|---|---|---:|---|---|
| Paper-Alias | Paper Title | [arxiv 2511](https://arxiv.org/pdf/2511.20857) | Org / University | Benchmark1, Benchmark2 | 0.0-5.0 | ![fig1](https://arxiv.org/html/2511.20857v1/x1.png) | 1) 核心洞察；2) 方法亮点；3) 结果与局限 |

## CSV 表头模板（与上表一致）

```csv
Alias,Title,Source,Institution,Benchmarking,⭐,Framework,Summary
```

> 说明：`Source` 在 Markdown 中建议写成 `[arxiv xxxx](url)`，便于展示简洁超链接。

## 示例（参考 Evo-Memory）

| Alias | Title | Source | Institution | Benchmarking | ⭐ | Figure 1 | Summary |
|---|---|---|---|---|---:|---|---|
| Evo-Memory | Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory | [arxiv 2511](https://arxiv.org/pdf/2511.20857) | Google DeepMind | MMLU-Pro, GPQA-Diamond, AIME24/25, ToolBench, AlfWorld, BabyAI, ScienceWorld | 4.5 | ![fig1](https://arxiv.org/html/2511.20857v1/x1.png) | 提出测试时“自进化记忆”；ExpRAG做经验检索，ReMem做 think-act-memory refine 循环；多任务下显著优于仅会话回忆。 |
