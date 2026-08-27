#!/usr/bin/env python3
"""Localize installed Markdown and Codex TOML agent metadata to zh-CN."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


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


def resolve_english_name(current: str, mapping: dict[str, dict[str, str]]) -> str | None:
    current = current.strip()
    if current in mapping:
        return current
    for english_name, entry in mapping.items():
        chinese_name = entry["name"]
        if current in {chinese_name, f"{chinese_name} ({english_name})"}:
            return english_name
    return None


def replace_yaml_field(frontmatter: list[str], key: str, value: str) -> bool:
    pattern = re.compile(rf"^{re.escape(key)}\s*:\s*(.*)$")
    for index, line in enumerate(frontmatter):
        if not pattern.match(line):
            continue
        end = index + 1
        while end < len(frontmatter) and (
            frontmatter[end].startswith((" ", "\t")) or not frontmatter[end].strip()
        ):
            end += 1
        replacement = f"{key}: {json.dumps(value, ensure_ascii=False)}"
        changed = frontmatter[index:end] != [replacement]
        frontmatter[index:end] = [replacement]
        return changed
    return False


def localize_markdown(path: Path, mapping: dict[str, dict[str, str]]) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    if not lines or lines[0].strip() != "---":
        return False
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return False

    frontmatter = lines[1:end]
    name_pattern = re.compile(r"^name\s*:\s*(.*)$")
    current_name = ""
    for line in frontmatter:
        match = name_pattern.match(line)
        if match:
            current_name = parse_scalar(match.group(1))
            break
    english_name = resolve_english_name(current_name, mapping)
    if not english_name:
        return False

    entry = mapping[english_name]
    replace_yaml_field(frontmatter, "name", entry["name"])
    replace_yaml_field(frontmatter, "description", entry["description"])
    localized = "\n".join([lines[0], *frontmatter, *lines[end:]])
    if original.endswith("\n"):
        localized += "\n"
    if localized == original:
        return False
    path.write_text(localized, encoding="utf-8")
    return True


def toml_string(lines: list[str], key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}\s*=\s*(.+)$")
    for line in lines:
        match = pattern.match(line)
        if not match:
            continue
        try:
            value = json.loads(match.group(1))
        except json.JSONDecodeError:
            return None
        return value if isinstance(value, str) else None
    return None


def replace_toml_field(lines: list[str], key: str, value: str) -> None:
    pattern = re.compile(rf"^{re.escape(key)}\s*=")
    for index, line in enumerate(lines):
        if pattern.match(line):
            lines[index] = f"{key} = {json.dumps(value, ensure_ascii=False)}"
            return


def localize_toml(
    path: Path,
    mapping: dict[str, dict[str, str]],
    codex_name_style: str,
) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    current_name = toml_string(lines, "name")
    if current_name is None:
        return False
    english_name = resolve_english_name(current_name, mapping)
    if not english_name:
        return False

    entry = mapping[english_name]
    localized_name = entry["name"]
    if codex_name_style == "bilingual":
        localized_name = f"{localized_name} ({english_name})"
    replace_toml_field(lines, "name", localized_name)
    replace_toml_field(lines, "description", entry["description"])
    localized = "\n".join(lines)
    if original.endswith("\n"):
        localized += "\n"
    if localized == original:
        return False
    path.write_text(localized, encoding="utf-8")
    return True


def default_target_dirs() -> list[Path]:
    home = Path.home()
    return [home / ".github/agents", home / ".copilot/agents", home / ".codex/agents"]


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target-dir",
        action="append",
        type=Path,
        dest="target_dirs",
        help="要处理的 Agent 目录；可重复传入。默认检测 GitHub Copilot 与 Codex 目录",
    )
    parser.add_argument(
        "--mapping",
        type=Path,
        default=script_dir / "agent-names-zh.json",
        help="中文映射 JSON 文件",
    )
    parser.add_argument(
        "--codex-name-style",
        choices=("bilingual", "chinese"),
        default="bilingual",
        help="Codex TOML 名称样式；默认中英双语，便于唯一识别和调用",
    )
    parser.add_argument("--dry-run", action="store_true", help="只统计，不写入文件")
    args = parser.parse_args()

    mapping = json.loads(args.mapping.read_text(encoding="utf-8"))
    targets = args.target_dirs or default_target_dirs()
    matched = 0
    updated = 0

    for target in targets:
        target = target.expanduser().resolve()
        if not target.is_dir():
            print(f"跳过不存在的目录：{target}")
            continue
        target_matched = 0
        target_updated = 0
        for path in sorted([*target.glob("*.md"), *target.glob("*.toml")]):
            if path.suffix == ".md":
                current_name_match = re.search(r"(?m)^name\s*:\s*(.*)$", path.read_text(encoding="utf-8"))
                current_name = parse_scalar(current_name_match.group(1)) if current_name_match else ""
            else:
                current_name = toml_string(path.read_text(encoding="utf-8").splitlines(), "name") or ""
            if not resolve_english_name(current_name, mapping):
                continue
            matched += 1
            target_matched += 1
            if args.dry_run:
                continue
            changed = (
                localize_markdown(path, mapping)
                if path.suffix == ".md"
                else localize_toml(path, mapping, args.codex_name_style)
            )
            if changed:
                updated += 1
                target_updated += 1
        action = "可本地化" if args.dry_run else "已更新"
        count = sum(
            1
            for path in [*target.glob("*.md"), *target.glob("*.toml")]
            if path.is_file()
        )
        print(
            f"{target}: 扫描 {count} 个文件，"
            f"{action} {target_updated if not args.dry_run else target_matched} 个"
        )

    if args.dry_run:
        print(f"试运行完成：匹配 {matched} 个 Agent，未写入文件")
    else:
        print(f"本地化完成：匹配 {matched} 个 Agent，更新 {updated} 个文件")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
