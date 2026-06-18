#!/usr/bin/env python3
"""dev/ 开发 OS 完整性校验器（通用骨架版）。

跑：  python dev/scripts/validate_dev.py      （仓库根或任意目录均可）
退出码 0 = 全过；1 = 有 FAIL。CI / pre-commit 可挂这个。

通用结构检查 + 项目锚点。**适配本项目只需改下面"项目配置"两个 list。**

OS 自带 · 源自 dev-os clone · 除"项目配置"块外勿改(改了就不是这套 OS 的自检)。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEV = Path(__file__).resolve().parents[1]          # dev/
ROOT = DEV.parent                                  # 仓库根

# ── 项目配置（每项目改这里）─────────────────────────────────────────
# 项目关键文件锚点（存在性检查，相对仓库根）；空 = 不检查。
PROJECT_ANCHORS: list[str] = [
    # 例: "app/backend/app/lineage/ids.py",
]
# 活跃文档不应再出现的"迁移前旧路径"（防悬空引用）；空 = 不检查。
STALE_PREFIXES: list[str] = [
    # 例: "docs/old_location/",
]
# ────────────────────────────────────────────────────────────────────

fails: list[str] = []
oks: list[str] = []


def ok(msg: str) -> None:
    oks.append(msg)


def fail(msg: str) -> None:
    fails.append(msg)


# --- 1. 四台必需文件 -------------------------------------------------------
REQUIRED = [
    "GOAL.md", "STATE.md", "RULES.md", "RULES.project.md", "DECISIONS.md",
    "ISSUES.md", "README.md",
    "tasks/BOARD.md", "research/INDEX.md", "exec/HANDOFF.md", "exec/LOG.md",
]
for rel in REQUIRED:
    (ok if (DEV / rel).is_file() else fail)(f"四台文件 {rel}")

# --- 2. 任务台 + 研究台目录 -----------------------------------------------
for rel in ["tasks/active", "tasks/done", "tasks/_templates",
            "research/active", "research/ideas", "research/findings"]:
    (ok if (DEV / rel).is_dir() else fail)(f"目录 {rel}/")

# --- 3 + 4. BOARD ✅done ↔ done/<id>/ -------------------------------------
board = (DEV / "tasks/BOARD.md").read_text(encoding="utf-8") if (DEV / "tasks/BOARD.md").is_file() else ""
done_in_board: set[str] = set()
for line in board.splitlines():
    if "✅" in line and "done" in line:
        m = re.search(r"\bT-\d{3,4}\b", line)
        if m:
            done_in_board.add(m.group(0))

done_dirs = {p.name for p in (DEV / "tasks/done").glob("T-*") if p.is_dir()}

for tid in sorted(done_in_board):
    if (DEV / "tasks/done" / tid / "TASK.md").is_file():
        ok(f"落档一致 {tid}（BOARD done ↔ done/{tid}/TASK.md）")
    else:
        fail(f"{tid} 在 BOARD 标 ✅done 但缺 done/{tid}/TASK.md（落档纪律漏了）")

for tid in sorted(done_dirs):
    if not (DEV / "tasks/done" / tid / "TASK.md").is_file():
        fail(f"done/{tid}/ 缺 TASK.md")

# --- 5. 活跃文档无迁移前旧路径悬空引用 ------------------------------------
LIVE_DOCS = [
    "GOAL.md", "STATE.md", "RULES.md", "RULES.project.md", "README.md", "ISSUES.md",
    "tasks/BOARD.md", "research/INDEX.md", "exec/HANDOFF.md", "exec/LOG.md",
]
stale_hits = 0
for rel in LIVE_DOCS:
    p = DEV / rel
    if not p.is_file():
        continue
    text = p.read_text(encoding="utf-8")
    for pre in STALE_PREFIXES:
        if pre in text:
            fail(f"活跃文档 {rel} 含迁移前旧路径 `{pre}`（悬空引用）")
            stale_hits += 1
if not STALE_PREFIXES or stale_hits == 0:
    ok("活跃文档无迁移前旧路径悬空引用")

# --- 6. 项目锚点 -----------------------------------------------------------
for rel in PROJECT_ANCHORS:
    (ok if (ROOT / rel).is_file() else fail)(f"项目锚点 {rel}")
if not PROJECT_ANCHORS:
    ok("（未配置项目锚点，跳过 §6）")

# --- 报告 ------------------------------------------------------------------
print(f"dev/ 完整性校验 —— {len(oks)} ✅  /  {len(fails)} ❌\n")
for m in oks:
    print(f"  ✅ {m}")
if fails:
    print()
    for m in fails:
        print(f"  ❌ {m}")
    print(f"\nFAIL（{len(fails)} 项）")
    sys.exit(1)
print("\nPASS —— harness 自检通过")
sys.exit(0)
