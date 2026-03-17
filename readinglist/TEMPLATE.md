# Reading List Table Template

> 用法：每篇论文一行；`Alias` 列请写成**指向具体阅读笔记的超链接**（例如 `[Evo-Memory](../papers/2026-03-11_evo-memory.md)`）。

## Markdown 表格模板

| Alias (link to note) | Title | Source | Institution | Benchmarking | ⭐ | Figure 1 | Summary |
|---|---|---|---|---|---:|---|---|
| [Paper-Alias](../papers/YYYY-MM-DD_short-title.md) | Paper Title | [arxiv 2511](https://arxiv.org/pdf/2511.20857) | First: Org A; High-impact: Org B | Benchmark1, Benchmark2 | ★★☆☆☆ | ![fig1](https://arxiv.org/html/2511.20857v1/x1.png) | 核心发现 |

## CSV 表头模板（与上表一致）

```csv
Alias,NoteLink,Title,Source,Institution,Benchmarking,⭐,Figure1,Summary
```

> 说明：
> - `Alias` 在 Markdown 中建议写成 `[Alias](相对路径)`，直接跳到阅读报告。
> - `Source` 建议写成 `[arxiv xxxx](url)`，便于展示简洁超链接。
> - `Institution` 规则：若为多机构，写成 `First: <第一机构>; High-impact: <你判断影响力最高机构>`；若 HTML 缺失机构信息，必须继续在 PDF 中查找。
> - 中国境内机构统一使用简称（如 CAS、BAAI、THU、PKU、SJTU、ZJU、FDU、USTC、HIT、NJU、SEU）。
> - `Figure 1` 必须显式填写：
>   1) 优先 `https://arxiv.org/html/<id-version>/x1.png`；
>   2) 若不可用，尝试 HTML 中首个论文插图资源（如 `figures/...`）；
>   3) 若仍不可得，写 `N/A（arXiv 未提供可用 HTML Figure 资源）`。

## 示例（参考 Evo-Memory）

| Alias (link to note) | Title | Source | Institution | Benchmarking | ⭐ | Figure 1 | Summary |
|---|---|---|---|---|---:|---|---|
| [Evo-Memory](../papers/2026-03-11_evo-memory.md) | Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory | [arxiv 2511](https://arxiv.org/pdf/2511.20857) | First: DeepMind; High-impact: DeepMind | MMLU-Pro, GPQA-Diamond, AIME24/25, ToolBench, AlfWorld, BabyAI, ScienceWorld | ★★★★★ | ![fig1](https://arxiv.org/html/2511.20857v1/x1.png) | LLM Agent 的记忆不应只是“回忆过去说了什么”，而应能在部署过程中持续从经验中学习并自我演化，实验证明这种自演化记忆（尤其在多轮任务中）能大幅提升表现和效率。 |
