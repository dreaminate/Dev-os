# 任务台 · BOARD（活跃任务板）

> 完成即把 `active/<id>/` 落档到 `done/<id>/`、本表那行删掉(**主板永不臃肿**)。
> `review_status`: 0=未经用户确认 · 1=用户已确认。任务文件模板见 `_templates/TASK.md`。
> 完整性自检:`python dev/scripts/validate_dev.py`。
> **本表 = 活跃版**(只列 todo/in_progress,完成即删行,永不臃肿);**全含量版**(含 done,需要时查询):`python dev/scripts/build_ledger.py`。

<!-- 格式·防跑偏 | 结构型:固定表头列 id | 标题 | 来源 | 状态 | 优先级 | 依赖 | 验收一句话。
本表=活跃版,只列 todo/in_progress;任务完成 → 落档 done/<id>/ 并**删本表那行**(永不臃肿)。
全含量版不手维护——由 build_ledger.py 从 active/+done/ 目录现生成(防第二份账本自己跑偏)。 -->

| id | 标题 | 来源 | 状态 | 优先级 | 依赖 | 验收一句话 |
|----|------|------|------|--------|------|-----------|
| T-001 | <第一个任务> | <研究/讨论/gap> | todo | P? | — | <种什么坏 → 门必抓> |

## 建设顺序
<可选:列任务依赖/波次>
