# Reading List Table Template

> 用法：每篇论文一行；`Summary` 建议控制在 3-8 行要点。

## Markdown 表格模板

| Alias | Title | Source | Institution | Benchmarking | ⭐ | Figure 1 | Summary |
|---|---|---|---|---|---:|---|---|
| Paper-Alias | Paper Title | [arxiv 2511](https://arxiv.org/pdf/2511.20857) | Org / University | Benchmark1, Benchmark2 | 0.0-5.0 | ![fig1](https://arxiv.org/html/2511.20857v1/x1.png) | 核心发现 |

## CSV 表头模板（与上表一致）

```csv
Alias,Title,Source,Institution,Benchmarking,⭐,Framework,Summary
```

> 说明：`Source` 在 Markdown 中建议写成 `[arxiv xxxx](url)`，便于展示简洁超链接。

## 示例（参考 Evo-Memory）

| Alias | Title | Source | Institution | Benchmarking | ⭐ | Figure 1 | Summary |
|---|---|---|---|---|---:|---|---|
| Evo-Memory | Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory | [arxiv 2511](https://arxiv.org/pdf/2511.20857) | Google DeepMind | MMLU-Pro, GPQA-Diamond, AIME24/25, ToolBench, AlfWorld, BabyAI, ScienceWorld | 4.5 | ![fig1](https://arxiv.org/html/2511.20857v1/x1.png) | LLM Agent 的记忆不应只是"回忆过去说了什么"，而应能在部署过程中持续从经验中学习并自我演化，实验证明这种自演化记忆（尤其在多轮任务中）能大幅提升表现和效率。 |
