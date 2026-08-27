# 🇨🇳 简体中文（zh-CN）本地化

[查看完整中文 Agent 目录](../../README.zh-CN.md)

本目录维护 Agent 的简体中文名称和简介。当前映射覆盖仓库中的全部 **273 个有效 Agent**，并保留少量历史兼容别名。

中文只应用于名称与简介；核心提示词继续保留英文，以便兼容上游更新，并避免翻译改变 Agent 的专业行为。

## 文件说明

| 文件 | 用途 |
|---|---|
| `agent-names-zh.json` | 英文 Agent 名称到中文名称、简介的映射，是中文元数据的唯一数据源 |
| `localize-agents-zh.py` | 跨平台本地化工具，支持 Markdown Agent 与 Codex TOML Agent |
| `localize-agents-zh.ps1` | 面向 Windows Copilot 安装目录的旧版 PowerShell 工具 |
| `generate-catalog-zh.py` | 根据 Agent 源文件和中文映射生成根目录的 `README.zh-CN.md` |

## 本地化已安装的 Agent

安装 Agent 后运行：

```bash
python3 scripts/i18n/localize-agents-zh.py
```

默认检测以下目录：

- `~/.github/agents/`
- `~/.copilot/agents/`
- `~/.codex/agents/`

先试运行、不写文件：

```bash
python3 scripts/i18n/localize-agents-zh.py --dry-run
```

只处理指定目录：

```bash
python3 scripts/i18n/localize-agents-zh.py \
  --target-dir ~/.codex/agents
```

Markdown Agent 会使用纯中文名称。Codex Agent 默认使用“中文（English）”双语名称，例如：

```toml
name = "渗透测试员 (Penetration Tester)"
description = "仅在明确授权范围内，对网络、Web 应用和云基础设施开展渗透测试、红队行动与漏洞评估"
```

保留英文名可以避免中文同名冲突，也便于在聊天中准确指定 Agent。如确实只需要中文名，可运行：

```bash
python3 scripts/i18n/localize-agents-zh.py --codex-name-style chinese
```

本地化只修改已安装副本。重新安装 Agent 会恢复仓库中的英文元数据，届时再次运行本工具即可。

### Windows PowerShell 旧版用法

仅本地化 GitHub Copilot Markdown Agent 时，也可以使用：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/i18n/localize-agents-zh.ps1
```

## 生成中文目录

新增或更新 Agent 后：

1. 在 `agent-names-zh.json` 中补充中文名称和简介。
2. 重新生成中文目录。
3. 运行检查，确认没有漏译或过期目录。

```bash
python3 scripts/i18n/generate-catalog-zh.py
python3 scripts/i18n/generate-catalog-zh.py --check
```

如果任何有效 Agent 缺少中文映射，生成脚本会列出名称和文件路径并返回失败状态。
