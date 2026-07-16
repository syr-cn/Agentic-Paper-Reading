# Monthly Paper Reading

轻量级论文收集系统。

## 使用方式

### 你（Master）做的事：
1. 打开 Obsidian，找到 `monthly/2026-MM.md`
2. 随手写一行：`- [ ] [标题](link) 一句话想法`
3. Done. 就这样。

### 或者直接跟 Twilight 说：
> "把这篇丢进去：https://arxiv.org/abs/xxxx.xxxxx"
> "记一下 XXX 那篇 关于 YYY 的"

### Twilight 自动做的事：
- 补全元信息（作者、研究组、tags）
- 按主题分类放到对应 section
- 月底生成 monthly summary
- 定期刷新 `views/` 下的跨月聚类视图

## 结构

```
monthly/
├── 2026-07.md          ← 当月 inbox（按月滚动）
├── 2026-06.md          ← 往月归档
├── README.md           ← 你在看的这个
└── views/
    ├── by-topic.md     ← 按研究主题聚类（auto-generated）
    ├── by-group.md     ← 按研究组/人聚类（auto-generated）
    └── highlights.md   ← 跨月精选（auto-generated）
```

## 约定
- `- [ ]` 未读 / `- [x]` 已读
- 反引号内的是 tags：`` `组名` `` `` `会议` `` `` `PI名` ``
- 每月文件按主题 section 分组（Twilight 负责归类）
- 如果你当时有 insight 想记，直接写在那行后面用 `—` 分隔
