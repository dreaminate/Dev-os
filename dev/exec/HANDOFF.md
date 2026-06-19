# HANDOFF · 新 session 入口提示词

> **慢变 · 怎么更新**:只在**入口/路由本身**变时改;进度、下一步全在 `BOARD`/`STATE`(实时源)、**不写进这里** —— 不需要 per-loop 刷新。

把下面整段复制给新 session 即可接上:

---
继续在本项目用 dev/ 开发 OS 干活。先读 dev/ 四台,再按 BOARD 接着建。

1. 读 `dev/GOAL.md`(终态) + `dev/STATE.md`(现状 gap) + `dev/tasks/BOARD.md`(下一步) + `dev/RULES.md`(OS 铁律) + `dev/RULES.project.md`(本项目红线) + `dev/DECISIONS.md`(已决,不重议)。重资料 `dev/research/archive/` read-on-demand。
2. 按 BOARD 取**最高优先 `todo`**(以 BOARD 实时为准,**别在此写死 task id**——防漂)。读对应 `dev/research/findings/` 设计的接线 + 对抗测试要点。
3. 复用现有模块(**<填:本项目可复用的模块/范式>**),写实现 + 对抗测试(「种已知 bug 门必抓」),跑绿测试(命令:**<填,如 `cd app/backend && python -m pytest`>**)。
4. 完成:`tasks/active/<id>/` 落档到 `tasks/done/<id>/`、更新 `BOARD.md`、刷新 `STATE.md`(诚实标 ✅/🟡/⬜)、跑 `python dev/scripts/validate_dev.py`。
5. 红线见 `RULES.md`(通用) + `RULES.project.md`(本项目);不擅自 commit;致命错误即停工。遇 `DECISIONS.md` 没覆盖的新岔路、**或 BOARD/卡标注的前置闸门(若有)**,停下问用户。

先用三五句复述你的理解 + 当前任务的设计要点,再动手。
---
