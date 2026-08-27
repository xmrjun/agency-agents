#!/usr/bin/env python3
"""Generate the Simplified Chinese agent catalog from source frontmatter."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


AGENT_DIRS = [
    "academic",
    "design",
    "engineering",
    "finance",
    "game-development",
    "gis",
    "healthcare",
    "marketing",
    "paid-media",
    "product",
    "project-management",
    "research",
    "sales",
    "security",
    "spatial-computing",
    "specialized",
    "support",
    "testing",
]

DIVISION_TITLES = {
    "academic": "学术研究",
    "design": "设计",
    "engineering": "工程",
    "finance": "财务",
    "game-development": "游戏开发",
    "gis": "地理信息系统（GIS）",
    "healthcare": "医疗健康",
    "marketing": "市场营销",
    "paid-media": "付费媒体",
    "product": "产品",
    "project-management": "项目管理",
    "research": "研究",
    "sales": "销售",
    "security": "安全",
    "spatial-computing": "空间计算",
    "specialized": "专业职能",
    "support": "支持",
    "testing": "测试",
}


def parse_scalar(value: str) -> str:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            pass
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def frontmatter_field(lines: list[str], key: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}\s*:\s*(.*)$")
    for line in lines:
        match = pattern.match(line)
        if match:
            return parse_scalar(match.group(1))
    return ""


def read_agent(path: Path) -> tuple[str, str] | None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return None
    frontmatter = lines[1:end]
    name = frontmatter_field(frontmatter, "name").strip()
    if not name:
        return None
    emoji = frontmatter_field(frontmatter, "emoji").strip()
    return name, emoji


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def build_catalog(repo_root: Path, mapping: dict[str, dict[str, str]]) -> str:
    grouped: dict[str, list[tuple[str, str, Path]]] = defaultdict(list)
    missing: list[tuple[str, Path]] = []

    for division in AGENT_DIRS:
        division_dir = repo_root / division
        if not division_dir.is_dir():
            continue
        for path in sorted(division_dir.rglob("*.md")):
            parsed = read_agent(path)
            if not parsed:
                continue
            name, emoji = parsed
            if name not in mapping:
                missing.append((name, path.relative_to(repo_root)))
                continue
            grouped[division].append((name, emoji, path.relative_to(repo_root)))

    if missing:
        details = "\n".join(f"- {name}: {path}" for name, path in missing)
        raise ValueError(f"缺少 {len(missing)} 个中文映射：\n{details}")

    total = sum(len(agents) for agents in grouped.values())
    lines = [
        "<!-- 此文件由 scripts/i18n/generate-catalog-zh.py 自动生成，请勿手工编辑。 -->",
        "",
        "# 🎭 The Agency：AI 专家中文目录",
        "",
        "[English README](README.md) · [中文本地化工具](scripts/i18n/README.md)",
        "",
        "> 本页提供全部 Agent 的简体中文名称和简介，Agent 的核心提示词仍保留英文，以便持续兼容上游更新。",
        "",
        f"当前目录包含 **{total} 个 Agent**，分布在 **{len(grouped)} 个部门**。点击名称即可查看完整 Agent 定义。",
        "",
        "## 快速开始",
        "",
        "```bash",
        "git clone https://github.com/xmrjun/agency-agents.git",
        "cd agency-agents",
        "./scripts/install.sh --tool codex",
        "```",
        "",
        "如需把已安装副本的名称和简介本地化为中文：",
        "",
        "```bash",
        "python3 scripts/i18n/localize-agents-zh.py",
        "```",
        "",
        "在 Codex 聊天中可直接要求委派，例如：",
        "",
        "```text",
        "请委派给自定义 agent “Penetration Tester”，对当前项目进行只读安全审计，等待完成后汇总结果。",
        "```",
        "",
        "## Agent 总览",
        "",
    ]

    for division in AGENT_DIRS:
        agents = grouped.get(division, [])
        if not agents:
            continue
        lines.extend(
            [
                f"### {DIVISION_TITLES[division]}（{len(agents)}）",
                "",
                "| Agent | 中文简介 |",
                "|---|---|",
            ]
        )
        for english_name, emoji, relative_path in agents:
            entry = mapping[english_name]
            display_name = f"{entry['name']}（{english_name}）"
            prefix = f"{emoji} " if emoji else ""
            lines.append(
                f"| {prefix}[{escape_table(display_name)}]({relative_path.as_posix()}) "
                f"| {escape_table(entry['description'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 维护中文目录",
            "",
            "新增 Agent 后，先在 `scripts/i18n/agent-names-zh.json` 添加中文映射，再运行：",
            "",
            "```bash",
            "python3 scripts/i18n/generate-catalog-zh.py",
            "python3 scripts/i18n/generate-catalog-zh.py --check",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    default_root = script_dir.parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=default_root)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true", help="检查目录是否已是最新版本")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    mapping_path = repo_root / "scripts/i18n/agent-names-zh.json"
    output_path = (args.output or repo_root / "README.zh-CN.md").resolve()
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))

    try:
        content = build_catalog(repo_root, mapping)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    if args.check:
        if not output_path.exists() or output_path.read_text(encoding="utf-8") != content:
            print(f"中文目录需要重新生成：{output_path}", file=sys.stderr)
            return 1
        print(f"中文目录已是最新版本：{output_path}")
        return 0

    output_path.write_text(content, encoding="utf-8")
    agent_count = sum(
        1 for line in content.splitlines() if line.startswith("| ") and "](" in line
    )
    print(f"已生成 {output_path}（{agent_count} 个 Agent）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
