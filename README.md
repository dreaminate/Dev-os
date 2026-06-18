# dev-os · 可复用开发操作系统

把 `dev/` + `CLAUDE.md` 放进**任何项目的根目录**,就得到一套**强制读、可自检、防漂移**的开发操作系统:
**目标台 / 任务台 / 研究台 / 执行台** + Goal Loop + 诚实 gap 纪律。新开的 Claude Code 一进来自动读 `CLAUDE.md` → 被导向 `dev/`,而不是把仓库当普通项目乱翻。

## 怎么用(实例化到你的项目)

1. 复制本仓库的 **`dev/` 和 `CLAUDE.md`** 到你的项目根。
2. 填项目内容(模板都带 `<...>` 占位):
   - `dev/GOAL.md` — 项目终态契约
   - `dev/RULES.project.md` — 本项目红线(冻结文件 / 范围 / 安全不变量)
   - `dev/exec/HANDOFF.md` — 新 session 入口(填项目名/示例任务)
3. 改 `dev/scripts/validate_project.py` 的 `PROJECT_ANCHORS`(项目关键文件)+ `STALE_PREFIXES`(可选);**别动 `validate_dev.py`**(【开发os级别】勿改)。
4. 跑 `python dev/scripts/validate_dev.py` 自检（会自动连带跑 `validate_project.py`）;`python dev/scripts/build_ledger.py` 看全含量任务表。
5. 开干:第一个任务录进 `dev/tasks/BOARD.md`,按 Goal Loop 走。

## 【开发os级别】 vs 【项目级别】(边界)

- **【开发os级别】(本骨架自带,勿改)**:四台结构 · Goal Loop · `dev/README.md` 方法 · `dev/RULES.md`(OS 铁律,含审计纪律) · 模板 · validator 核心 · 防漂纪律。
- **【项目级别】(你填)**:GOAL/STATE/BOARD/DECISIONS/ISSUES 内容 · `dev/RULES.project.md` · `dev/scripts/validate_project.py`(锚点/旧路径)。

完整方法与哲学见 [`dev/README.md`](dev/README.md)(随骨架走,每个项目都带一份)。

> ⚠️ 不是每个项目都适配这套 OS——它面向「**目标驱动 + 严谨验收 + 长周期**」的开发。轻量一次性脚本别套。
