<!-- 此文件由 scripts/i18n/generate-catalog-zh.py 自动生成，请勿手工编辑。 -->

# 🎭 The Agency：AI 专家中文目录

[English README](README.md) · [中文本地化工具](scripts/i18n/README.md)

> 本页提供全部 Agent 的简体中文名称和简介，Agent 的核心提示词仍保留英文，以便持续兼容上游更新。

当前目录包含 **273 个 Agent**，分布在 **18 个部门**。点击名称即可查看完整 Agent 定义。

## 快速开始

```bash
git clone https://github.com/xmrjun/agency-agents.git
cd agency-agents
./scripts/install.sh --tool codex
```

如需把已安装副本的名称和简介本地化为中文：

```bash
python3 scripts/i18n/localize-agents-zh.py
```

在 Codex 聊天中可直接要求委派，例如：

```text
请委派给自定义 agent “Penetration Tester”，对当前项目进行只读安全审计，等待完成后汇总结果。
```

## Agent 总览

### 学术研究（6）

| Agent | 中文简介 |
|---|---|
| 🌍 [学术人类学家（Anthropologist）](academic/academic-anthropologist.md) | 文化研究、田野调查与人类学视角分析专家 |
| 🗺️ [学术地理学家（Geographer）](academic/academic-geographer.md) | 空间分析、地理信息与地缘研究专家 |
| 📚 [学术历史学家（Historian）](academic/academic-historian.md) | 历史分析、史料解读与历史叙事专家 |
| 📜 [学术叙事学家（Narratologist）](academic/academic-narratologist.md) | 叙事结构、故事理论与文本分析专家 |
| 🧠 [学术心理学家（Psychologist）](academic/academic-psychologist.md) | 心理学研究、行为分析与认知科学专家 |
| 📊 [统计学家（Statistician）](academic/academic-statistician.md) | 量化研究方法、实验设计与统计推断专家，负责检验结论并区分真实信号、随机性与偏差 |

### 设计（10）

| Agent | 中文简介 |
|---|---|
| 🎨 [品牌守护者（Brand Guardian）](design/design-brand-guardian.md) | 品牌认知、一致性与品牌定位专家 |
| 📷 [图像提示词工程师（Image Prompt Engineer）](design/design-image-prompt-engineer.md) | AI 图像生成提示词、摄影风格指令专家 |
| 🌈 [包容性视觉专家（Inclusive Visuals Specialist）](design/design-inclusive-visuals-specialist.md) | 多元化呈现、偏见消除与真实 AI 图像生成专家 |
| 🎭 [用户画像走查专家（Persona Walkthrough Specialist）](design/design-persona-walkthrough.md) | 从目标用户画像的心理视角模拟页面认知走查，并输出结构化转化率优化报告 |
| 🎨 [UI 设计师（UI Designer）](design/design-ui-designer.md) | 视觉设计、组件库与设计系统专家 |
| 🧱 [UI 完成度门禁审查员（UI Finish-Gate Reviewer）](design/design-ui-finish-gate-reviewer.md) | 依据产品证据与设计约定审查界面完成度，阻止千篇一律的 UI 在打磨前上线 |
| 📐 [用户体验架构师（UX Architect）](design/design-ux-architect.md) | 技术架构、CSS 系统与前端实现指导专家 |
| 🔬 [用户体验研究员（UX Researcher）](design/design-ux-researcher.md) | 用户测试、行为分析与可用性研究专家 |
| 🎬 [视觉叙事师（Visual Storyteller）](design/design-visual-storyteller.md) | 视觉叙事、多媒体内容与品牌故事专家 |
| ✨ [创意注入师（Whimsy Injector）](design/design-whimsy-injector.md) | 品牌个性、微互动与趣味体验设计专家 |

### 工程（59）

| Agent | 中文简介 |
|---|---|
| 🧬 [AI 数据修复工程师（AI Data Remediation Engineer）](engineering/engineering-ai-data-remediation-engineer.md) | 自愈数据管道、离线 SLM 与语义聚类专家 |
| 🤖 [AI 工程师（AI Engineer）](engineering/engineering-ai-engineer.md) | 机器学习模型部署、AI 集成与数据管道专家 |
| 🔌 [API 平台工程师（API Platform Engineer）](engineering/engineering-api-platform-engineer.md) | 公共与合作伙伴 API 的契约设计、版本治理、网关能力、SDK 生成与开发者体验专家 |
| ⚡ [自主优化架构师（Autonomous Optimization Architect）](engineering/engineering-autonomous-optimization-architect.md) | LLM 路由、成本优化与影子测试专家 |
| 🏗️ [后端架构师（Backend Architect）](engineering/engineering-backend-architect.md) | 负责 API 设计、数据库架构与可扩展性的后端系统专家 |
| 🧱 [CMS 开发工程师（CMS Developer）](engineering/engineering-cms-developer.md) | Drupal 与 WordPress 主题、插件、模块及内容架构的代码优先实现专家 |
| 👁️ [代码审查工程师（Code Reviewer）](engineering/engineering-code-reviewer.md) | 建设性代码审查、安全与可维护性评估专家 |
| 🧭 [代码库入门工程师（Codebase Onboarding Engineer）](engineering/engineering-codebase-onboarding-engineer.md) | 通过阅读源码和追踪调用路径，帮助新成员快速、准确地理解陌生代码库 |
| 🔧 [数据工程师（Data Engineer）](engineering/engineering-data-engineer.md) | 数据管道、湖仓架构与 ETL/ELT 专家 |
| 📈 [数据可视化工程师（Data Visualization Engineer）](engineering/engineering-data-visualization-engineer.md) | 图表选型、诚实视觉编码、无障碍配色及 D3/Vega 大数据渲染专家 |
| 🗄️ [数据库优化工程师（Database Optimizer）](engineering/engineering-database-optimizer.md) | Schema 设计、查询优化与索引策略专家（PostgreSQL/MySQL） |
| 🛟 [数据库可靠性工程师（Database Reliability Engineer）](engineering/engineering-database-reliability-engineer.md) | 数据库高可用、复制、自动故障切换、时间点恢复与零停机变更专家 |
| 💻 [桌面应用工程师（Desktop App Engineer）](engineering/engineering-desktop-app-engineer.md) | Electron 与 Tauri 桌面应用、安全 IPC、代码签名、自动更新及原生系统集成专家 |
| 🛠️ [开发者工具工程师（Developer Tooling Engineer）](engineering/engineering-developer-tooling-engineer.md) | 命令行工具与内部开发平台的交互设计、错误体验、跨平台分发和可组合接口专家 |
| ⚙️ [DevOps 自动化工程师（DevOps Automator）](engineering/engineering-devops-automator.md) | CI/CD、基础设施自动化与云运营专家 |
| ⚡ [Drupal 性能工程师（Drupal Performance Engineer）](engineering/engineering-drupal-performance.md) | Drupal 10/11 缓存、查询、前端资源、CDN、PHP-FPM 与核心网页指标优化专家 |
| 🛒 [Drupal 电商工程师（Drupal Shopping Cart Engineer）](engineering/engineering-drupal-shopping-cart.md) | 基于 Drupal Commerce 的商品、支付、结账、订单、税务和促销流程专家 |
| 📧 [邮件智能工程师（Email Intelligence Engineer）](engineering/engineering-email-intelligence-engineer.md) | 将原始邮件线程提取为适合 AI 推理和自动化处理的结构化数据 |
| 🔩 [嵌入式固件工程师（Embedded Firmware Engineer）](engineering/engineering-embedded-firmware-engineer.md) | 裸金属、RTOS、ESP32/STM32/Nordic 固件开发专家 |
| 🔗 [飞书集成开发工程师（Feishu Integration Developer）](engineering/engineering-feishu-integration-developer.md) | 飞书/Lark 开放平台、机器人与工作流集成专家 |
| 🔧 [Filament 优化专家（Filament Optimization Specialist）](engineering/engineering-filament-optimization-specialist.md) | 重构并优化 Filament PHP 管理界面的结构、可用性与操作效率 |
| 💰 [FinOps 工程师（FinOps Engineer）](engineering/engineering-finops-engineer.md) | AWS、GCP 与 Azure 成本分摊、资源优化、承诺折扣和单位经济性分析专家 |
| 🖥️ [前端开发工程师（Frontend Developer）](engineering/engineering-frontend-developer.md) | 专注现代 Web 技术、React/Vue/Angular 框架、UI 实现与性能优化的前端专家 |
| 🗄️ [GaussDB 专家工程师（GaussDB Expert Engineer）](engineering/engineering-gaussdb-expert.md) | 华为 GaussDB OLTP 的模式设计、分布式表、索引、查询与性能调优专家 |
| 🌿 [Git 工作流专家（Git Workflow Master）](engineering/engineering-git-workflow-master.md) | 分支策略、规范提交与高级 Git 操作专家 |
| 🌍 [国际化工程师（Internationalization Engineer）](engineering/engineering-i18n-engineer.md) | ICU MessageFormat、CLDR、RTL、区域格式化、字符串提取和伪本地化测试专家 |
| 🔐 [身份与访问管理工程师（Identity & Access Engineer）](engineering/engineering-identity-access-engineer.md) | OAuth/OIDC、SAML、SCIM、Passkey、会话及多租户 RBAC/ABAC 专家 |
| 🚨 [故障响应指挥官（Incident Response Commander）](engineering/engineering-incident-response-commander.md) | 事件管理、故障复盘与值班应急专家 |
| 📡 [IoT 设备群工程师（IoT Fleet Engineer）](engineering/engineering-iot-fleet-engineer.md) | 设备身份与配置、MQTT 遥测、分阶段 OTA、边缘计算及大规模设备可观测性专家 |
| 🖧 [IT 服务经理（IT Service Manager）](engineering/engineering-it-service-manager.md) | 基于 ITIL 4 的服务目录、事件与问题管理、变更控制、SLA 和 CMDB 治理专家 |
| 🧠 [知识图谱工程师（Knowledge Graph Engineer）](engineering/engineering-knowledge-graph-engineer.md) | 实体关系抽取、图谱建模、图增强 RAG、来源追踪与矛盾管理专家 |
| 🧪 [LLM 后训练工程师（LLM Post-Training Engineer）](engineering/engineering-llm-post-training-engineer.md) | SFT、DPO、RLHF、RLVR、MoE 后训练及模型发布门禁专家 |
| 🪡 [最小改动工程师（Minimal Change Engineer）](engineering/engineering-minimal-change-engineer.md) | 坚持最小可行差异，只解决明确问题并避免无关重构和范围蔓延 |
| 📲 [移动端开发工程师（Mobile App Builder）](engineering/engineering-mobile-app-builder.md) | iOS/Android、React Native、Flutter 跨平台移动应用构建者 |
| 🚀 [移动端发布工程师（Mobile Release Engineer）](engineering/engineering-mobile-release-engineer.md) | iOS/Android 签名、Fastlane、商店提交、分阶段发布和崩溃分诊专家 |
| 🕸️ [多智能体系统架构师（Multi-Agent Systems Architect）](engineering/engineering-multi-agent-systems-architect.md) | 生产级多智能体拓扑、上下文、信任、故障恢复、人工门禁和可观测性专家 |
| 🌐 [网络工程师（Network Engineer）](engineering/engineering-network-engineer.md) | Cisco、Juniper 与 Palo Alto 路由、交换、防火墙配置及故障排查专家 |
| 📜 [OrgScript 工程师（OrgScript Engineer）](engineering/engineering-orgscript-engineer.md) | OrgScript 语法、解析器、AST 校验和业务逻辑定义专家 |
| 💳 [支付与计费工程师（Payments & Billing Engineer）](engineering/engineering-payments-billing-engineer.md) | 支付服务商集成、幂等支付、Webhook、订阅计费、3DS 与财务对账专家 |
| 🕵️ [隐私工程师（Privacy Engineer）](engineering/engineering-privacy-engineer.md) | 在代码中实现 PII 发现、数据最小化、同意管理、DSAR、删除与保留控制 |
| 🧬 [提示词工程师（Prompt Engineer）](engineering/engineering-prompt-engineer.md) | 设计、测试并系统优化提示词，将模糊需求转化为可靠的生产级 AI 行为 |
| 🔍 [RAG 管道工程师（RAG Pipeline Engineer）](engineering/engineering-rag-pipeline-engineer.md) | 分块、混合检索、重排序、质量评估与迭代优化的生产级 RAG 专家 |
| ⚡ [快速原型工程师（Rapid Prototyper）](engineering/engineering-rapid-prototyper.md) | 快速 POC 开发、MVP 与迭代验证专家 |
| 🤝 [实时协作工程师（Realtime Collaboration Engineer）](engineering/engineering-realtime-collaboration-engineer.md) | WebSocket/SSE、在线状态、CRDT/OT、离线同步和可靠重连扩展专家 |
| 🦀 [Rust 重构专家（Rust Refactoring Specialist）](engineering/engineering-rust-refactoring-specialist.md) | 仓库级 Rust 安全重构、模块调整、所有权改进及编译器和 Clippy 修复专家 |
| 🔎 [搜索相关性工程师（Search Relevance Engineer）](engineering/engineering-search-relevance-engineer.md) | Elasticsearch/OpenSearch 索引、BM25、混合检索和相关性评估专家 |
| ♿ [Section 508 无障碍专家（Section 508 Accessibility Specialist）](engineering/engineering-section-508-specialist.md) | 美国联邦 Section 508、WCAG、屏幕阅读器测试、VPAT/ACR 与整改专家 |
| 💎 [高级开发工程师（Senior Developer）](engineering/engineering-senior-developer.md) | Laravel/Livewire、复杂模式与架构决策专家 |
| 🏛️ [软件架构师（Software Architect）](engineering/engineering-software-architect.md) | 系统设计、DDD、架构模式与权衡分析专家 |
| ⛓️ [Solidity 智能合约工程师（Solidity Smart Contract Engineer）](engineering/engineering-solidity-smart-contract-engineer.md) | EVM 合约、Gas 优化与 DeFi 协议专家 |
| 🛡️ [站点可靠性工程师（SRE (Site Reliability Engineer)）](engineering/engineering-sre.md) | SLO、错误预算、可观测性与混沌工程专家 |
| 📚 [技术文档工程师（Technical Writer）](engineering/engineering-technical-writer.md) | 开发者文档、API 参考手册与教程撰写专家 |
| 🏛️ [USWDS 开发工程师（USWDS Developer）](engineering/engineering-uswds-developer.md) | 美国政府设计系统组件、设计令牌、无障碍模式、主题配置和 CMS 集成专家 |
| 🎬 [视频流媒体工程师（Video Streaming Engineer）](engineering/engineering-video-streaming-engineer.md) | HLS/DASH、FFmpeg 转码阶梯、低延迟 CMAF、DRM、CDN 与播放体验优化专家 |
| 🎙️ [语音 AI 集成工程师（Voice AI Integration Engineer）](engineering/engineering-voice-ai-integration-engineer.md) | 从音频预处理、ASR 到字幕、说话人分离和下游集成的端到端语音管道专家 |
| 🧩 [WebAssembly 工程师（WebAssembly Engineer）](engineering/engineering-webassembly-engineer.md) | Rust/C++/Go 到 Wasm、JS 互操作、WASI、组件模型和性能调优专家 |
| 💬 [微信小程序开发工程师（WeChat Mini Program Developer）](engineering/engineering-wechat-mini-program-developer.md) | 微信生态、小程序与支付集成开发专家 |
| ⚡ [WordPress 性能工程师（WordPress Performance Engineer）](engineering/engineering-wordpress-performance.md) | WordPress 缓存、查询、资源、图片、CDN、插件及 PHP 运行时优化专家 |
| 🛍️ [WordPress 电商工程师（WordPress Shopping Cart Engineer）](engineering/engineering-wordpress-shopping-cart.md) | 基于 WooCommerce 的商品、支付、结账、订单、税务、优惠与转化优化专家 |

### 财务（5）

| Agent | 中文简介 |
|---|---|
| 📒 [簿记与财务控制专家（Bookkeeper & Controller）](finance/finance-bookkeeper-controller.md) | 日常会计、财务对账、月末结账、内部控制、GAAP 合规与审计准备专家 |
| 📊 [财务分析师（Financial Analyst）](finance/finance-financial-analyst.md) | 财务建模、预测、情景分析和数据驱动决策支持专家 |
| 📈 [财务规划与分析师（FP&A Analyst）](finance/finance-fpa-analyst.md) | 预算、差异分析、滚动预测、资源配置及经营决策支持专家 |
| 🔍 [投资研究员（Investment Researcher）](finance/finance-investment-researcher.md) | 市场研究、尽职调查、资产估值、组合分析与投资风险评估专家 |
| 🏛️ [税务策略师（Tax Strategist）](finance/finance-tax-strategist.md) | 税务优化、多辖区合规、转让定价与战略税务规划专家 |

### 游戏开发（21）

| Agent | 中文简介 |
|---|---|
| 🧩 [Blender 插件工程师（Blender Add-on Engineer）](game-development/blender/blender-addon-engineer.md) | 使用 Python 构建 Blender 插件、资产校验器、导出器和 DCC 管道自动化 |
| 💰 [游戏经济系统设计师（Economy Designer）](game-development/economy-designer.md) | 虚拟货币、产出与消耗、商业化、通胀控制及数据驱动平衡专家 |
| 🎵 [游戏音频工程师（Game Audio Engineer）](game-development/game-audio-engineer.md) | FMOD/Wwise、自适应音乐与空间音频专家 |
| 🎮 [游戏设计师（Game Designer）](game-development/game-designer.md) | 系统设计、GDD 写作、经济平衡与玩法循环专家 |
| 🎯 [Godot 玩法脚本工程师（Godot Gameplay Scripter）](game-development/godot/godot-gameplay-scripter.md) | Godot 4、GDScript 2.0、C#、节点组合和类型安全信号设计专家 |
| 🌐 [Godot 多人游戏工程师（Godot Multiplayer Engineer）](game-development/godot/godot-multiplayer-engineer.md) | Godot 4 MultiplayerAPI、场景复制、网络传输、RPC 和权威模型专家 |
| 💎 [Godot 着色器开发工程师（Godot Shader Developer）](game-development/godot/godot-shader-developer.md) | Godot 着色语言、VisualShader、2D/3D 特效、后处理和性能优化专家 |
| 🗺️ [关卡设计师（Level Designer）](game-development/level-designer.md) | 布局理论、节奏、遭遇设计与环境叙事专家 |
| 📖 [叙事设计师（Narrative Designer）](game-development/narrative-designer.md) | 故事系统、分支对话与世界观架构专家 |
| 👤 [Roblox 虚拟形象创作者（Roblox Avatar Creator）](game-development/roblox-studio/roblox-avatar-creator.md) | Roblox UGC、Avatar、饰品绑定、纹理规范与创作者市场提交流程专家 |
| 🎪 [Roblox 体验设计师（Roblox Experience Designer）](game-development/roblox-studio/roblox-experience-designer.md) | Roblox 参与循环、成长系统、商业化机制与玩家留存专家 |
| 🔧 [Roblox 系统脚本工程师（Roblox Systems Scripter）](game-development/roblox-studio/roblox-systems-scripter.md) | Luau、客户端与服务器安全、远程事件、DataStore 和模块化架构专家 |
| 🎨 [技术美术（Technical Artist）](game-development/technical-artist.md) | Shader、VFX、LOD 管线与美术到引擎优化专家 |
| 🏛️ [Unity 架构师（Unity Architect）](game-development/unity/unity-architect.md) | ScriptableObjects、数据驱动模块化与 DOTS/ECS 专家 |
| 🛠️ [Unity 编辑器工具开发者（Unity Editor Tool Developer）](game-development/unity/unity-editor-tool-developer.md) | EditorWindow、AssetPostprocessor 与构建自动化专家 |
| 🔗 [Unity 多人网络工程师（Unity Multiplayer Engineer）](game-development/unity/unity-multiplayer-engineer.md) | Netcode for GameObjects、Unity Relay/Lobby 与服务器权威专家 |
| ✨ [Unity Shader 艺术家（Unity Shader Graph Artist）](game-development/unity/unity-shader-graph-artist.md) | Shader Graph、HLSL、URP/HDRP 与渲染特性专家 |
| 🌐 [Unreal 多人游戏架构师（Unreal Multiplayer Architect）](game-development/unreal-engine/unreal-multiplayer-architect.md) | UE5 Actor 复制、服务器权威玩法、网络预测和专用服务器专家 |
| ⚙️ [Unreal 系统工程师（Unreal Systems Engineer）](game-development/unreal-engine/unreal-systems-engineer.md) | UE5 C++/Blueprint、Nanite、Lumen 与 Gameplay Ability System 专家 |
| 🎨 [Unreal 技术美术（Unreal Technical Artist）](game-development/unreal-engine/unreal-technical-artist.md) | UE5 材质、Niagara、程序化内容生成及美术到引擎管道专家 |
| 🌍 [Unreal 世界构建师（Unreal World Builder）](game-development/unreal-engine/unreal-world-builder.md) | UE5 World Partition、Landscape、程序化植被、HLOD 与开放世界流送专家 |

### 地理信息系统（GIS）（13）

| Agent | 中文简介 |
|---|---|
| 🏔️ [3D 与场景开发工程师（3D & Scene Developer）](gis/gis-3d-scene-developer.md) | 使用 Cesium、ArcGIS 与现代 Web 3D 框架构建沉浸式场景和空间可视化 |
| 🖥️ [GIS 分析师（GIS Analyst）](gis/gis-analyst.md) | 地图制作、图层管理、空间查询及桌面与 Web 地理数据维护专家 |
| 🏗️ [BIM/GIS 集成专家（BIM/GIS Specialist）](gis/gis-bim-specialist.md) | Revit/IFC 转换、室内地图、数字孪生和设施管理数据模型专家 |
| 🎨 [地图制图设计师（Cartography Designer）](gis/gis-cartography-designer.md) | 地图配色、字体、标注、底图选择及印刷和 Web 视觉层级专家 |
| 🛸 [无人机实景测绘专家（Drone/Reality Mapping Specialist）](gis/gis-drone-reality-mapping.md) | 将无人机影像处理为正射影像、地形模型、点云和三维网格的摄影测量专家 |
| 🤖 [GeoAI/机器学习工程师（GeoAI/ML Engineer）](gis/gis-geoai-ml-engineer.md) | 基于卫星与航拍影像进行要素提取、目标检测、分割和土地覆盖分类 |
| ⚙️ [地理处理专家（Geoprocessing Specialist）](gis/gis-geoprocessing-specialist.md) | 使用 ArcPy、Python 工具箱和 ModelBuilder 自动化 ArcGIS Pro 空间工作流 |
| ✅ [GIS 质量保证工程师（GIS QA Engineer）](gis/gis-qa-engineer.md) | 拓扑、元数据、坐标参考系、精度及地理数据合规验证专家 |
| 🔧 [GIS 解决方案工程师（Solution Engineer）](gis/gis-solution-engineer.md) | 将 GIS 策略转化为 Esri 与开源技术栈演示、原型和技术验证 |
| 📦 [空间数据工程师（Spatial Data Engineer）](gis/gis-spatial-data-engineer.md) | 地理数据格式转换、坐标重投影、属性标准化与自动化 ETL 管道专家 |
| 📊 [空间数据科学家（Spatial Data Scientist）](gis/gis-spatial-data-scientist.md) | 空间统计、计量经济学、聚类与地理预测分析专家 |
| 🧠 [GIS 技术顾问（Technical Consultant）](gis/gis-technical-consultant.md) | 将业务问题转化为 GIS 差距分析、技术路线、投标方案和数字化转型策略 |
| 🌐 [Web GIS 开发工程师（Web GIS Developer）](gis/gis-web-gis-developer.md) | 使用 MapLibre、ArcGIS JS、Leaflet 和空间服务构建交互式地图应用 |

### 医疗健康（3）

| Agent | 中文简介 |
|---|---|
| 🩺 [临床证据 Agent（Clinical Evidence Agent）](healthcare/healthcare-clinical-evidence-agent.md) | 为医疗 AI 建立证据标准、临床可信度、声明边界及多受众表达框架 |
| 🧭 [医疗创新策略师（Healthcare Innovation Strategist）](healthcare/healthcare-innovation-strategist.md) | 为医疗创业者协调临床、融资、监管与国家级部署叙事的战略专家 |
| 🌍 [国家卫生系统 Agent（Sovereign Health Systems Agent）](healthcare/healthcare-sovereign-health-systems-agent.md) | 面向国家卫生基础设施、全民健康覆盖政策和新兴市场部署的政府协作框架专家 |

### 市场营销（36）

| Agent | 中文简介 |
|---|---|
| 🏗️ [AEO 基础架构师（AEO Foundations Architect）](marketing/marketing-aeo-foundations.md) | 通过 llms.txt、AI 友好抓取规则和结构化内容提升 AI 引擎可发现性 |
| 🤖 [智能体搜索优化专家（Agentic Search Optimizer）](marketing/marketing-agentic-search-optimizer.md) | 评估并改进 AI 智能体在网站上的预订、购买、注册等任务完成能力 |
| 🔮 [AI 引用策略师（AI Citation Strategist）](marketing/marketing-ai-citation-strategist.md) | AEO/GEO、AI 推荐可见度与引用审计专家 |
| 📱 [应用商店优化专家（App Store Optimizer）](marketing/marketing-app-store-optimizer.md) | ASO、转化率优化与应用曝光专家 |
| 🇨🇳 [百度 SEO 专家（Baidu SEO Specialist）](marketing/marketing-baidu-seo-specialist.md) | 百度优化、中国 SEO 与 ICP 合规专家 |
| 🎬 [Bilibili 内容策略师（Bilibili Content Strategist）](marketing/marketing-bilibili-content-strategist.md) | B站算法、弹幕文化与 UP 主成长专家 |
| 📘 [图书联合作者（Book Co-Author）](marketing/marketing-book-co-author.md) | 思想领导力书籍、代笔写作与出版策略专家 |
| 🎠 [轮播图增长引擎（Carousel Growth Engine）](marketing/marketing-carousel-growth-engine.md) | TikTok/Instagram 轮播图创作与自动发布专家 |
| 🛒 [中国电商运营专家（China E-Commerce Operator）](marketing/marketing-china-ecommerce-operator.md) | 淘宝/天猫/拼多多与直播电商运营专家 |
| 🇨🇳 [中国市场本地化策略师（China Market Localization Strategist）](marketing/marketing-china-market-localization-strategist.md) | 将实时趋势转化为抖音、小红书、微信、B站等渠道的中国市场落地策略 |
| ✍️ [内容创作者（Content Creator）](marketing/marketing-content-creator.md) | 多平台内容策略、编辑日历与文案专家 |
| 🌏 [跨境电商专家（Cross-Border E-Commerce Specialist）](marketing/marketing-cross-border-ecommerce.md) | 亚马逊/Shopee/Lazada 与跨境履约全链路专家 |
| 🎵 [抖音运营策略师（Douyin Strategist）](marketing/marketing-douyin-strategist.md) | 抖音平台、短视频营销与算法增长专家 |
| 📧 [邮件营销策略师（Email Marketing Strategist）](marketing/marketing-email-strategist.md) | CRM 营销活动、生命周期自动化、分群、送达率和效果衡量专家 |
| 🎙️ [全球播客策略师（Global Podcast Strategist）](marketing/marketing-global-podcast-strategist.md) | 播客定位、受众增长、内容策略及 Spotify、Apple Podcasts、YouTube 商业化专家 |
| 🚀 [增长黑客（Growth Hacker）](marketing/marketing-growth-hacker.md) | 快速用户获取、病毒循环与实验驱动增长专家 |
| 📸 [Instagram 运营专家（Instagram Curator）](marketing/marketing-instagram-curator.md) | 视觉叙事、社区运营与 Instagram 策略专家 |
| 🎥 [快手运营策略师（Kuaishou Strategist）](marketing/marketing-kuaishou-strategist.md) | 快手平台、老铁生态与下沉市场增长专家 |
| 💼 [领英内容创作者（LinkedIn Content Creator）](marketing/marketing-linkedin-content-creator.md) | 个人品牌、思想领导力与领英专业内容专家 |
| 🎙️ [直播带货教练（Livestream Commerce Coach）](marketing/marketing-livestream-commerce-coach.md) | 主播培训、直播间优化与转化提升专家 |
| 📡 [多平台发布专家（Multi-Platform Publisher）](marketing/marketing-multi-platform-publisher.md) | 将一篇中文内容适配并以草稿形式分发到知乎、小红书、B站、公众号等平台 |
| 🎧 [播客策略师（Podcast Strategist）](marketing/marketing-podcast-strategist.md) | 播客内容策略与平台运营专家 |
| 📣 [公关与传播经理（PR & Communications Manager）](marketing/marketing-pr-communications-manager.md) | 媒体关系、新闻稿、危机传播、高管思想领导力与品牌声誉管理专家 |
| 🔒 [私域运营专家（Private Domain Operator）](marketing/marketing-private-domain-operator.md) | 企业微信、私域流量与社群运营专家 |
| 💬 [Reddit 社区运营（Reddit Community Builder）](marketing/marketing-reddit-community-builder.md) | 真实互动、价值内容与 Reddit 营销专家 |
| 🔍 [SEO 专家（SEO Specialist）](marketing/marketing-seo-specialist.md) | 技术 SEO、内容策略与外链建设专家 |
| 🎬 [短视频剪辑教练（Short-Video Editing Coach）](marketing/marketing-short-video-editing-coach.md) | 后期制作、剪辑流程与平台规格优化专家 |
| 📣 [社交媒体策略师（Social Media Strategist）](marketing/marketing-social-media-strategist.md) | 跨平台策略、营销活动与社媒整体规划专家 |
| 🎵 [TikTok 策略专家（TikTok Strategist）](marketing/marketing-tiktok-strategist.md) | 病毒内容、算法优化与 TikTok 增长专家 |
| 🐦 [Twitter 运营专家（Twitter Engager）](marketing/marketing-twitter-engager.md) | 实时互动、思想领导力与推特策略专家 |
| 🎬 [视频优化专家（Video Optimization Specialist）](marketing/marketing-video-optimization-specialist.md) | YouTube 算法、观众留存、章节、缩略图概念与跨平台视频分发专家 |
| 📱 [微信公众号运营专家（WeChat Official Account Manager）](marketing/marketing-wechat-official-account.md) | 粉丝互动、内容营销与微信公众号策略专家 |
| 🔥 [微博运营策略师（Weibo Strategist）](marketing/marketing-weibo-strategist.md) | 微博热搜、话题营销与粉丝互动专家 |
| 🛰️ [X/Twitter 情报分析师（X/Twitter Intelligence Analyst）](marketing/marketing-x-twitter-intelligence-analyst.md) | 基于公开信号开展 X/Twitter 趋势研究、账号监测和受众情报分析 |
| 🌸 [小红书运营专家（Xiaohongshu Specialist）](marketing/marketing-xiaohongshu-specialist.md) | 生活方式内容、趋势策略与小红书增长专家 |
| 🧠 [知乎运营专家（Zhihu Strategist）](marketing/marketing-zhihu-strategist.md) | 思想领导力、知识驱动互动与知乎权威建立专家 |

### 付费媒体（7）

| Agent | 中文简介 |
|---|---|
| 📋 [付费媒体审计师（Paid Media Auditor）](paid-media/paid-media-auditor.md) | 200+ 维度账户审计与竞争对手分析专家 |
| ✍️ [广告创意策略师（Ad Creative Strategist）](paid-media/paid-media-creative-strategist.md) | RSA 文案、Meta 创意与 PMax 素材专家 |
| 📱 [付费社交策略师（Paid Social Strategist）](paid-media/paid-media-paid-social-strategist.md) | Meta/LinkedIn/TikTok 跨平台付费社交专家 |
| 💰 [竞价广告策略师（PPC Campaign Strategist）](paid-media/paid-media-ppc-strategist.md) | Google/Microsoft/Amazon 广告、账户结构与出价专家 |
| 📺 [程序化广告购买专家（Programmatic & Display Buyer）](paid-media/paid-media-programmatic-buyer.md) | GDN、DSP、合作媒体与 ABM 展示广告专家 |
| 🔍 [搜索词分析师（Search Query Analyst）](paid-media/paid-media-search-query-analyst.md) | 搜索词分析、否定关键词与意图映射专家 |
| 📡 [追踪与埋点专家（Tracking & Measurement Specialist）](paid-media/paid-media-tracking-specialist.md) | GTM、GA4、转化追踪与 CAPI 实施专家 |

### 产品（5）

| Agent | 中文简介 |
|---|---|
| 🧠 [行为助推引擎（Behavioral Nudge Engine）](product/product-behavioral-nudge-engine.md) | 行为心理学、助推设计与用户激励专家 |
| 🔍 [用户反馈综合分析师（Feedback Synthesizer）](product/product-feedback-synthesizer.md) | 用户反馈分析、洞察提取与产品优先级专家 |
| 🧭 [产品经理（Product Manager）](product/product-manager.md) | 全生命周期产品管理：发现、PRD、路线图、GTM |
| 🎯 [Sprint 优先级规划师（Sprint Prioritizer）](product/product-sprint-prioritizer.md) | 敏捷规划、功能优先级与 Sprint 管理专家 |
| 🔭 [市场趋势研究员（Trend Researcher）](product/product-trend-researcher.md) | 市场情报、竞品分析与机会识别专家 |

### 项目管理（7）

| Agent | 中文简介 |
|---|---|
| 🧪 [实验追踪专家（Experiment Tracker）](project-management/project-management-experiment-tracker.md) | A/B 测试、假设验证与数据驱动决策专家 |
| 📋 [Jira 工作流管理员（Jira Workflow Steward）](project-management/project-management-jira-workflow-steward.md) | Git 工作流、分支策略与 Jira 关联交付规范专家 |
| 📋 [会议纪要专家（Meeting Notes Specialist）](project-management/project-management-meeting-notes-specialist.md) | 从会议转录或草稿中提取决策、行动项、待确认问题并生成结构化纪要 |
| 🐑 [项目协调专家（Project Shepherd）](project-management/project-management-project-shepherd.md) | 跨职能协调、时间轴管理与端到端项目统筹专家 |
| 🏭 [工作室运营专家（Studio Operations）](project-management/project-management-studio-operations.md) | 日常效率优化、流程改进与生产支持专家 |
| 🎬 [工作室制作人（Studio Producer）](project-management/project-management-studio-producer.md) | 高层编排、投资组合管理与多项目监督专家 |
| 📝 [高级项目经理（Senior Project Manager）](project-management/project-manager-senior.md) | 现实范围评估与规格转任务分解专家 |

### 研究（1）

| Agent | 中文简介 |
|---|---|
| 🔍 [研究综合分析师（Research Synthesist）](research/research-synthesist.md) | 评估来源并综合文献证据，将分散资料整理为诚实加权的结论地图 |

### 销售（9）

| Agent | 中文简介 |
|---|---|
| 🗺️ [客户策略师（Account Strategist）](sales/sales-account-strategist.md) | 拓客留存、QBR 与利益相关者地图专家 |
| 🏋️ [销售教练（Sales Coach）](sales/sales-coach.md) | 销售代表成长、通话辅导与管道审查促进专家 |
| ♟️ [商机策略师（Deal Strategist）](sales/sales-deal-strategist.md) | MEDDPICC 资格认定、竞争定位与赢单策略专家 |
| 🔍 [销售发现教练（Discovery Coach）](sales/sales-discovery-coach.md) | SPIN、Gap Selling 与 Sandler 问题设计专家 |
| 🛠️ [售前工程师（Sales Engineer）](sales/sales-engineer.md) | 技术演示、POC 范围确定与竞争技术定位专家 |
| 🧲 [产品报价与获客策略师（Offer & Lead Gen Strategist）](sales/sales-offer-lead-gen-strategist.md) | 设计高吸引力报价、获客磁铁、多渠道线索生成与复合传播体系 |
| 🎯 [外呼销售策略师（Outbound Strategist）](sales/sales-outbound-strategist.md) | 基于信号的精准找客、多渠道序列与 ICP 定位专家 |
| 📊 [销售漏斗分析师（Pipeline Analyst）](sales/sales-pipeline-analyst.md) | 预测、漏斗健康度、商机速度与 RevOps 专家 |
| 🏹 [提案策略师（Proposal Strategist）](sales/sales-proposal-strategist.md) | RFP 响应、赢单主题与叙事结构专家 |

### 安全（12）

| Agent | 中文简介 |
|---|---|
| 🔎 [AI 生成代码安全审计师（AI-Generated Code Security Auditor）](security/security-ai-generated-code-auditor.md) | 审查 AI 生成应用中的硬编码密钥、访问控制缺陷和提示注入风险 |
| 🔐 [应用安全工程师（Application Security Engineer）](security/security-appsec-engineer.md) | 通过威胁建模、安全代码审查、SAST/DAST 和开发者教育保障软件生命周期 |
| 🛡️ [安全架构师（Security Architect）](security/security-architect.md) | 威胁建模、安全设计、信任边界、纵深防御和风险导向架构评审专家 |
| 🛡️ [区块链安全审计师（Blockchain Security Auditor）](security/security-blockchain-security-auditor.md) | 智能合约审计与漏洞分析专家 |
| ☁️ [云安全架构师（Cloud Security Architect）](security/security-cloud-security-architect.md) | AWS、Azure、GCP 零信任、纵深防御及基础设施即代码安全专家 |
| 📋 [合规审计师（Compliance Auditor）](security/security-compliance-auditor.md) | SOC2/ISO27001/HIPAA/PCI-DSS 合规认证指导专家 |
| 🚨 [安全事件响应专家（Incident Responder）](security/security-incident-responder.md) | 数字取证、入侵调查、威胁遏制、危机协调和事后复盘专家 |
| 🗡️ [渗透测试员（Penetration Tester）](security/security-penetration-tester.md) | 仅在明确授权范围内，对网络、Web 应用和云基础设施开展渗透测试、红队行动与漏洞评估 |
| 🔑 [密钥与凭据安全工程师（Secrets & Credential Hygiene Engineer）](security/security-secrets-credential-engineer.md) | 负责密钥与凭据的检测、预防、托管、轮换及泄露响应全生命周期 |
| 🛡️ [高级安全运营工程师（Senior SecOps Engineer）](security/security-senior-secops.md) | 优先检查密钥泄露并审计身份认证、授权、令牌、HTTP 和安全日志控制 |
| 🎯 [威胁检测工程师（Threat Detection Engineer）](security/security-threat-detection-engineer.md) | SIEM 规则、威胁狩猎与 ATT&CK 映射专家 |
| 🔍 [威胁情报分析师（Threat Intelligence Analyst）](security/security-threat-intelligence-analyst.md) | 追踪攻击组织、映射 MITRE ATT&CK、编写威胁报告并构建检测规则 |

### 空间计算（6）

| Agent | 中文简介 |
|---|---|
| 🍎 [macOS 空间/Metal 工程师（macOS Spatial/Metal Engineer）](spatial-computing/macos-spatial-metal-engineer.md) | Swift、Metal 与高性能 3D macOS 空间计算专家 |
| 🖥️ [终端集成专家（Terminal Integration Specialist）](spatial-computing/terminal-integration-specialist.md) | 终端集成、命令行工具与开发者工作流专家 |
| 🥽 [visionOS 空间工程师（visionOS Spatial Engineer）](spatial-computing/visionos-spatial-engineer.md) | Apple Vision Pro 应用与空间计算体验开发专家 |
| 🕹️ [XR 座舱交互专家（XR Cockpit Interaction Specialist）](spatial-computing/xr-cockpit-interaction-specialist.md) | 座舱控制系统与沉浸式控制界面专家 |
| 🌐 [WebXR 沉浸式开发者（XR Immersive Developer）](spatial-computing/xr-immersive-developer.md) | WebXR、浏览器端 AR/VR 沉浸式体验开发专家 |
| 🫧 [XR 界面架构师（XR Interface Architect）](spatial-computing/xr-interface-architect.md) | 空间交互设计与沉浸式 UX 专家（AR/VR/XR） |

### 专业职能（58）

| Agent | 中文简介 |
|---|---|
| 💸 [应付账款 Agent（Accounts Payable Agent）](specialized/accounts-payable-agent.md) | 支付处理、供应商管理与自主支付专家 |
| 🔐 [智能体身份与信任架构师（Agentic Identity & Trust Architect）](specialized/agentic-identity-trust.md) | Agent 身份、认证与信任验证专家 |
| 🎛️ [多智能体编排师（Agents Orchestrator）](specialized/agents-orchestrator.md) | 多 Agent 协调、工作流管理与复杂项目统筹专家 |
| ⚙️ [自动化治理架构师（Automation Governance Architect）](specialized/automation-governance-architect.md) | 自动化治理、n8n 与工作流审计专家 |
| ♟️ [商业策略师（Business Strategist）](specialized/business-strategist.md) | 竞争分析、市场进入、商业模式、增长规划和组织战略专家 |
| 🔄 [变革管理顾问（Change Management Consultant）](specialized/change-management-consultant.md) | 运用 ADKAR、Kotter 与 Prosci 推动技术实施、重组、文化转型和并购变革落地 |
| 💼 [首席财务官（Chief Financial Officer）](specialized/chief-financial-officer.md) | 资本配置、资金管理、财务规划、并购、投资者关系和董事会报告专家 |
| 📚 [企业培训设计师（Corporate Training Designer）](specialized/corporate-training-designer.md) | 企业培训、课程开发与学习系统设计专家 |
| 🎧 [客户服务专员（Customer Service）](specialized/customer-service.md) | 跨行业处理咨询、投诉、账户支持、常见问题和顺畅升级的客户服务专家 |
| 🌟 [客户成功经理（Customer Success Manager）](specialized/customer-success-manager.md) | 客户入驻、健康评分、QBR、流失预防、扩展与续约管理专家 |
| 🗄️ [数据整合 Agent（Data Consolidation Agent）](specialized/data-consolidation-agent.md) | 销售数据聚合与仪表板报告专家 |
| 🔐 [数据保护官（Data Privacy Officer）](specialized/data-privacy-officer.md) | GDPR、CCPA 及全球隐私项目、影响评估、同意管理、泄露响应和供应商审查专家 |
| 🌱 [ESG 与可持续发展官（ESG & Sustainability Officer）](specialized/esg-sustainability-officer.md) | 环境、社会与治理项目、披露、脱碳行动及可持续战略专家 |
| 🏛️ [政务数字化售前顾问（Government Digital Presales Consultant）](specialized/government-digital-presales-consultant.md) | ToG 项目售前与数字政府转型方案专家 |
| 📝 [资助申请撰稿人（Grant Writer）](specialized/grant-writer.md) | 面向非营利、科研和社会企业的资助检索、意向书、申请书、预算叙事与结项报告专家 |
| 🧡 [老年父母照护助手（Aging Parent Care Companion）](specialized/healthcare-aging-parent-care-companion.md) | 协助家庭照护者协调长辈预约、用药、护理团队沟通及照护者身心健康 |
| 🏥 [医疗客户服务专员（Healthcare Customer Service）](specialized/healthcare-customer-service.md) | 患者支持、账单、预约、保险咨询、投诉处理与临床或行政升级专家 |
| ⚕️ [医疗营销合规专家（Healthcare Marketing Compliance Specialist）](specialized/healthcare-marketing-compliance.md) | 中国医疗广告法规合规专家 |
| 🏨 [酒店宾客服务专家（Hospitality Guest Services）](specialized/hospitality-guest-services.md) | 酒店、度假村、餐饮和活动场所的预订、入住、礼宾、投诉及忠诚度服务专家 |
| 🤝 [人力资源入职专员（HR Onboarding）](specialized/hr-onboarding.md) | 员工入职引导、文档、合规、福利、文化融入和新员工支持专家 |
| 🕸️ [身份图谱运营专家（Identity Graph Operator）](specialized/identity-graph-operator.md) | 多 Agent 系统实体去重与身份一致性专家 |
| 🌐 [语言翻译专家（Language Translator）](specialized/language-translator.md) | 具备文化语境、地区方言和语气适配能力的西班牙语与英语实时翻译专家 |
| ⏱️ [法律计费与工时管理专家（Legal Billing & Time Tracking）](specialized/legal-billing-time-tracking.md) | 律师工时记录、发票、计费说明、催收、信托账户合规和计费分析专家 |
| 📋 [法律客户接洽专家（Legal Client Intake）](specialized/legal-client-intake.md) | 潜在客户筛选、案件信息收集、咨询安排、利益冲突检查和律师摘要专家 |
| ⚖️ [法律文件审查专家（Legal Document Review）](specialized/legal-document-review.md) | 合同、诉讼和房地产文件摘要、风险条款识别、版本比较与合规检查专家 |
| 🏦 [信贷专员助手（Loan Officer Assistant）](specialized/loan-officer-assistant.md) | 借款人接洽、预审、材料收集、贷款管道、合规、报价和放款协调专家 |
| 🔎 [语言服务器/索引工程师（LSP/Index Engineer）](specialized/lsp-index-engineer.md) | LSP 实现、代码智能与语义索引专家 |
| 🤝 [并购整合经理（M&A Integration Manager）](specialized/ma-integration-manager.md) | 并购后的首日准备、百日计划、协同效益、文化与职能工作流整合专家 |
| 🏥 [医疗计费与编码专家（Medical Billing & Coding Specialist）](specialized/medical-billing-coding-specialist.md) | ICD-10、CPT、HCPCS 编码、理赔提交、拒付管理和收入周期优化专家 |
| ⚙️ [运营经理（Operations Manager）](specialized/operations-manager.md) | 运用精益、六西格玛和系统思维开展流程、产能、KPI、供应商和效率管理 |
| 🧠 [组织心理学家（Organizational Psychologist）](specialized/organizational-psychologist.md) | 以循证方法诊断团队动力、心理安全、倦怠风险和组织文化健康 |
| 🌱 [个人成长导师（Personal Growth Mentor）](specialized/personal-growth-mentor.md) | 提供目标澄清、习惯设计、战略决策和务实问责的跨领域成长辅导 |
| 🏠 [房地产买卖顾问（Real Estate Buyer & Seller）](specialized/real-estate-buyer-seller.md) | 住宅与投资房产的买卖代理、房源、谈判、交易协调及过户支持专家 |
| 🎯 [招聘专家（Recruitment Specialist）](specialized/recruitment-specialist.md) | 人才获取、招聘运营与雇主品牌专家 |
| 📤 [报告分发 Agent（Report Distribution Agent）](specialized/report-distribution-agent.md) | 自动化报告交付与按区域定时发送专家 |
| 🧾 [简历定制专家（Resume Tailor）](specialized/resume-tailor.md) | 分析职位描述、映射真实经历、优化 ATS 关键词并在不造假的前提下改写简历 |
| 🛒 [零售退换货专员（Retail Customer Returns）](specialized/retail-customer-returns.md) | 全渠道退货、换货、退款、政策执行、欺诈预防和客户挽留专家 |
| 📊 [销售数据提取 Agent（Sales Data Extraction Agent）](specialized/sales-data-extraction-agent.md) | Excel 监控与销售指标提取（MTD/YTD）专家 |
| 🎯 [销售拓展专家（Sales Outreach）](specialized/sales-outreach.md) | B2B 冷启动获客、线索跟进、异议处理、提案和销售管道管理专家 |
| 🧭 [幕僚长（Chief of Staff）](specialized/specialized-chief-of-staff.md) | 为创始人和高管过滤噪声、管理流程、协调决策并提升输出影响力 |
| 🏗️ [土木工程师（Civil Engineer）](specialized/specialized-civil-engineer.md) | 覆盖全球标准的结构分析、岩土设计、施工文档和建筑规范合规专家 |
| 🏺 [代码库考古专家（Codebase Archaeologist）](specialized/specialized-codebase-archaeologist.md) | 审计多会话、多 AI 工具长期改动造成的逻辑漂移、死代码和文档偏差 |
| 🌍 [文化智能策略师（Cultural Intelligence Strategist）](specialized/specialized-cultural-intelligence-strategist.md) | 全球 UX、多元呈现与文化排斥规避专家 |
| 🗣️ [开发者布道师（Developer Advocate）](specialized/specialized-developer-advocate.md) | 社区建设、开发者体验与技术内容创作专家 |
| 📄 [文档生成专家（Document Generator）](specialized/specialized-document-generator.md) | PDF/PPTX/DOCX/XLSX 代码生成与专业文档创建专家 |
| 🛡️ [FedRAMP 与 RMF 合规工程师（FedRAMP & RMF Compliance Engineer）](specialized/specialized-fedramp-rmf-compliance.md) | FedRAMP Rev5/20x、NIST RMF、ATO、持续监控、OSCAL 和政府云合规专家 |
| 🇫🇷 [法国咨询市场导航师（French Consulting Market Navigator）](specialized/specialized-french-consulting-market.md) | ESN/SI 生态与法国 IT 自由职业专家 |
| 🇰🇷 [韩国商务导航师（Korean Business Navigator）](specialized/specialized-korean-business-navigator.md) | 韩国商业文化、品议流程与人际关系机制专家 |
| 🏛️ [总体规划架构师（Master Plan Architect）](specialized/specialized-master-plan-architect.md) | 专注深度架构教学、红队风险质疑和零代码执行实施计划的规划专家 |
| 🔌 [MCP 构建专家（MCP Builder）](specialized/specialized-mcp-builder.md) | Model Context Protocol 服务器与 AI Agent 工具链专家 |
| 🔬 [模型 QA 专家（Model QA Specialist）](specialized/specialized-model-qa.md) | ML 审计、特征分析与可解释性专家 |
| 💰 [定价分析师（Pricing Analyst）](specialized/specialized-pricing-analyst.md) | 通过市场、竞品、成本和利润分析构建数据驱动的最优定价模型 |
| ☁️ [Salesforce 架构师（Salesforce Architect）](specialized/specialized-salesforce-architect.md) | 多云 Salesforce 设计、Governor Limits 与集成专家 |
| ⚔️ [策略对决 Agent（Strategy Duel Agent）](specialized/specialized-strategy-duel-agent.md) | 运用博弈论与三十六计开展实时策略推演和对抗分析 |
| 🗺️ [工作流架构师（Workflow Architect）](specialized/specialized-workflow-architect.md) | 工作流发现、流程映射与规格说明专家 |
| 🎓 [留学顾问（Study Abroad Advisor）](specialized/study-abroad-advisor.md) | 国际教育、申请规划与留学目的地专家（美/英/加/澳） |
| 🔗 [供应链策略师（Supply Chain Strategist）](specialized/supply-chain-strategist.md) | 供应链管理、采购策略与优化专家 |
| 🗃️ [知识卡片管理员（ZK Steward）](specialized/zk-steward.md) | 知识管理、Zettelkasten 与笔记系统专家 |

### 支持（6）

| Agent | 中文简介 |
|---|---|
| 📊 [数据分析报告员（Analytics Reporter）](support/support-analytics-reporter.md) | 数据分析、仪表板与业务洞察专家 |
| 📝 [高管摘要生成师（Executive Summary Generator）](support/support-executive-summary-generator.md) | C 级沟通、战略摘要与决策支持专家 |
| 💰 [财务追踪专员（Finance Tracker）](support/support-finance-tracker.md) | 财务规划、预算管理与业务绩效分析专家 |
| 🏢 [基础设施维护工程师（Infrastructure Maintainer）](support/support-infrastructure-maintainer.md) | 系统可靠性、性能优化与基础设施运营专家 |
| ⚖️ [法律合规检查员（Legal Compliance Checker）](support/support-legal-compliance-checker.md) | 合规审查、监管要求与风险管理专家 |
| 💬 [客户支持专员（Support Responder）](support/support-support-responder.md) | 客户服务、问题解决与支持运营专家 |

### 测试（9）

| Agent | 中文简介 |
|---|---|
| ♿ [无障碍审计师（Accessibility Auditor）](testing/testing-accessibility-auditor.md) | WCAG 审计、辅助技术测试与包容性设计专家 |
| 🔌 [API 测试工程师（API Tester）](testing/testing-api-tester.md) | API 验证、集成测试与端点核查专家 |
| 📸 [测试证据采集员（Evidence Collector）](testing/testing-evidence-collector.md) | 截图 QA、视觉验证与 Bug 文档专家 |
| ⏱️ [性能基准测试专家（Performance Benchmarker）](testing/testing-performance-benchmarker.md) | 性能测试、压力测试与速度优化专家 |
| 🧐 [生产就绪验证员（Reality Checker）](testing/testing-reality-checker.md) | 基于证据的认证、质量门与发布认证专家 |
| 🎭 [测试自动化工程师（Test Automation Engineer）](testing/testing-test-automation-engineer.md) | Playwright/Cypress 端到端自动化、稳定选择器、消除偶发失败和 CI 并行专家 |
| 📋 [测试结果分析师（Test Results Analyzer）](testing/testing-test-results-analyzer.md) | 测试评估、质量指标分析与覆盖率报告专家 |
| 🔧 [工具评估专家（Tool Evaluator）](testing/testing-tool-evaluator.md) | 技术评估与工具选型专家 |
| ⚡ [工作流优化专家（Workflow Optimizer）](testing/testing-workflow-optimizer.md) | 流程分析、工作流改进与自动化机会挖掘专家 |

## 维护中文目录

新增 Agent 后，先在 `scripts/i18n/agent-names-zh.json` 添加中文映射，再运行：

```bash
python3 scripts/i18n/generate-catalog-zh.py
python3 scripts/i18n/generate-catalog-zh.py --check
```
