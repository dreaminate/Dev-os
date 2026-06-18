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
5. **种 memory**(推荐):把下方「memory seed」存成 `~/.claude/projects/<你的项目路径 slug>/memory/MEMORY.md` —— 让 agent 从第一天就知道 memory 与 dev/ 的分工(详见 [memory 与 dev/ 协同](#memory-与-dev-协同可复用契约))。
6. 开干:第一个任务录进 `dev/tasks/BOARD.md`,按 Goal Loop 走。

## 【开发os级别】 vs 【项目级别】(边界)

- **【开发os级别】(本骨架自带,勿改)**:四台结构 · Goal Loop · `dev/README.md` 方法 · `dev/RULES.md`(OS 铁律,含审计纪律) · 模板 · validator 核心 · 防漂纪律。
- **【项目级别】(你填)**:GOAL/STATE/BOARD/DECISIONS/ISSUES 内容 · `dev/RULES.project.md` · `dev/scripts/validate_project.py`(锚点/旧路径)。

完整方法与哲学见 [`dev/README.md`](dev/README.md)(随骨架走,每个项目都带一份)。

## memory 与 dev/ 协同(可复用契约)

每个项目有两个**自动加载**的上下文源:**项目 memory**(`~/.claude/projects/<本项目>/`,私有、不进 git)和 **dev/**(在仓库、人人 clone 可见)。协同契约(已写进 `CLAUDE.md`,跟着每个新项目走):

- **dev/ = 项目状态**:目标 / 进度 / 决策 / 任务 / 红线 —— 在仓库、可 `validate_dev.py` 自检、不漂。**项目的事一律以它为准。**
- **项目 memory = dev/ 装不下的那层**,只装三类:① **操作者画像**(谁在操作、怎么和 agent 协作) ② **工作偏好**(commit 习惯、协作节奏、复核口味等) ③ **外部参考 / 凭据**(token/key 的存在与额度——**不是密钥本身**、外部方法论 URL)。
- **铁律(防飘)**:① 绝不把 dev/ 项目状态复制进 memory(双源必漂),引用 dev/ 按**章节名**钉、别只钉号; ② memory 里某条成熟成**项目规则** → 升级进 dev/(RULES.project / DECISIONS),不留第二份。

**判一条事实放哪:** 是项目状态 / 该让任何 clone 的人看到 → `dev/`;其余(操作者画像 / 工作偏好 / 外部凭据)→ **项目 memory**。

**新项目「项目 memory」seed**(存成 `~/.claude/projects/<你的项目 slug>/memory/MEMORY.md`):

```markdown
# <项目名> memory 索引(项目级 · 私有)

> **项目状态全在仓库 `dev/`**(新 session 读根 `CLAUDE.md` → dev/ 四台)。
> 本 memory 只装 dev/ 装不下的那层:操作者画像 / 工作偏好 / 外部参考凭据。
> 铁律:① 别复制 dev/ 项目状态(双源必漂),引用按**章节名**钉 ② 某条成熟成项目规则→升级进 dev/,不留第二份。

**操作者 / 怎么协作(user)**
- (按需:谁在操作、中/英、怎么和 agent 协作、谁动真钱)

**工作偏好(feedback)**
- (按需:commit 习惯、协作节奏、复核口味等)

**外部参考 / 凭据(reference)**
- (按需:token/key 的存在与额度、外部方法论 URL)
```

> ⚠️ 不是每个项目都适配这套 OS——它面向「**目标驱动 + 严谨验收 + 长周期**」的开发。轻量一次性脚本别套。
