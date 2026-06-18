# 开发 OS（dev/）· OS 规约

<!-- OS 自带 · 源自 dev-os clone · 勿改。本文件是 OS 规约/方法,跨项目一致。 -->

这里是「**怎么建**」——四台 + Goal Loop。本文件随骨架走,任何用本 OS 的项目都带一份。
产品本身的手册/运行数据放项目自己的 `docs/` 等处(app 运行时读的留在项目侧)。

## 四台 + 两本账 + 一道闸

| 件 | 文件/目录 | 职责 | 通用/项目 |
|---|---|---|---|
| 目标台 | `GOAL.md` | 项目**完整最终形态**(终态契约,慢变,所有 gap 对照它) | 项目填 |
| — | `STATE.md` | **诚实 gap 陈述器**输出:现状 vs GOAL(每 loop 重生;🟡未验证 ≠ ✅) | 项目填 |
| — | `DECISIONS.md` | 决策账本(**append-only**,锁定后不改既往) | 项目填 |
| — | `RULES.md` | **OS 通用铁律**(诚实/对抗测试/扩展不替换/防漂/审计纪律) | **OS 自带·勿删** |
| — | `RULES.project.md` | **本项目铁律**(冻结文件/范围/安全不变量) | 项目填 |
| — | `ISSUES.md` | **跨任务问题/风险登记册**(未决 Open Q 不掉地) | 项目填 |
| 任务台 | `tasks/` | `BOARD.md`(活跃板) + `active/<id>/` + `done/<id>/` + `_templates/` | 格式通用·内容项目 |
| 研究台 | `research/` | `INDEX.md` + `TRACE.md` + `ideas/`(创新入口) + `active/`(在研) + `findings/`(已蒸馏) + `archive/`(归档) | 结构通用·内容项目 |
| 执行台 | `exec/` | `LOG.md`(滚动记录台) + `HANDOFF.md`(新 session 入口) | 方法通用·内容项目 |
| 闸 | `scripts/validate_dev.py` | 一致性自检(四台齐全 / BOARD↔done / 结构) | 核心通用·锚点配置 |

## Goal Loop（开发循环）

```
诚实查现状(STATE gap) → gap 变任务(BOARD) → 执行(active/<id> 写实现 + 对抗测试,测试跑绿)
   → 完成落档(active→done, BOARD 刷新) → 重跑 gap 陈述器(STATE) → 再循环
```

## 蒸馏（研究 → 可落地）

原始研究又长又乐观,**蒸馏**= 打折乐观 + 拍板去伪存真 + 提炼成可落地:
`research/archive`(原料) → `research/findings`(蒸馏设计) → `DECISIONS.md`(拍板) → `tasks/`(实现)。
在研/创新走 `ideas/` → `active/<topic>/` → 成熟才进上面这条链。

## 核心纪律（全文 RULES.md）

- **诚实**:🟡 声称 ≠ ✅ 验证,状态文件不假绿灯。
- **对抗测试**:「种一个已知的坏,门必须抓住,否则门是纸做的」。
- **防漂**:易变的东西(测试数/进度/当前任务)**绝不写进慢变文件**(GOAL/RULES/CLAUDE),只在 STATE/BOARD。
- **审计先立框架**:大结构→小结构→细节;框架是假设、可被细节推翻(防过度审计 + 防漏审)。
- **不擅自 commit/push**;改现有文件「扩展不替换」。

## 自检

`python dev/scripts/validate_dev.py` —— harness 不靠手工纪律,能自检(四台文件齐全 / BOARD ✅done ↔ `done/<id>/` 一一对应 / 目录齐全 / 项目锚点在)。挂 CI 或 pre-commit 即防漂。

## 新 session 怎么开始

读 `GOAL.md`(终态) + `STATE.md`(现状) + `tasks/BOARD.md`(下一步),拿 `exec/HANDOFF.md` 当入口提示词。重资料在 `research/archive/`,**read-on-demand,不默认加载**——活跃面只 4 个小文件。
