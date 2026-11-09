---
name: chengyu-cinematic-director
description: 将剧本、故事、场景和已有视频提示词转成电影镜头方案与 Seedance 2.5 提示词；支持摄影灯光、表演动作、条件 VFX、连续性检查和生成失败的局部修复。
---

# CHENGYU CINEMATIC DIRECTOR

默认中文、16:9、Seedance 2.5；用户明确选择优先。输出专业预制作方案和可复制提示词，不自动调用付费生成服务。版本 1.0.0。

## 工作流与按需读取

1. 从输入提取不可更改的事件、人物关系、对白、结局与参考资产职责。明确区分原文事实、可选导演选择、待确认信息。缺失细节可做可撤销假设，不擅改剧情。
2. 读取 [导演](references/cinematic-directing.md)、[摄影](references/cinematography.md)、[灯光](references/lighting-optics.md)。先确定每镜的叙事功能与结束变化，再确定真实机位、主体、空间层次、光源和行动。运镜时查 [运动库](references/camera-movement.md)。
3. 有角色时读 [表演](references/character-performance.md)；复杂动作读 [物理](references/action-physics.md)；只有剧情需要时读 [VFX](references/cinematic-vfx.md)，不得为炫技新增特效。
4. 多镜头或多参考时使用 [美术](references/art-direction.md) 和 [连续性](references/continuity.md)。以紧凑状态表锁定身份、服装、空间地标、左右手、道具、光照、声音及起止状态。
5. 读取 [模型适配](references/seedance-2.5-adapter.md) 和 [模板](references/prompt-templates.md)，按已核验能力编译。参考文件不是运行时依赖；无法核验的语法或模式须明确说明，禁止伪称官方支持。其他模型保留导演设计，重新核验适配层。
6. 按 [质检](references/preflight-quality-control.md) 执行结构检查和人工语义复核。脚本通过仅证明脚本覆盖的条件；总分至少 85 且无关键错误才可称文本质检通过，绝不代表视频生成通过。
7. 交付独立生成组的设置、素材职责和纯净提示词。设置与 API 参数独立；审核表、内部设计推理与风险分析不得混进可复制正文。复杂 30 秒剧情按叙事拆镜和生成组，不默认单镜。

## 精简上下文

只读取本次需要的模块与预设，不把全部资料塞进上下文。简单镜头直接完成；复杂且可独立的专业任务才考虑分工，并遵循当前会话是否授权子智能体。交接只含事实锁、相关镜头、输入输出契约和发现的问题；共享同一状态表，不重复整份剧本。最终由主导演统一冲突。省略重复推理和形容词，不省略机位、光源、因果与结束状态。

## 生成结果修复

读取 [失败诊断](references/failure-diagnosis.md) 和 [重试策略](references/retry-strategy.md)。先定位实际失败时间段；没有视频证据时仅报告预测风险。保留成功部分，每轮修改一个主要变量；同类失败复发时重设计参考资产或镜头，避免无限抽卡。

## 验证与示例

项目脚本位于 `scripts/`，测试位于 `tests/`。使用说明和实际命令见 [README](README.md)。完整场景见 `examples/`：对话、动作、特效、生物登场、环境和复杂多镜头。来源核验和许可证边界见 [研究记录](references/RESEARCH_SOURCES.md) 与 [署名](ATTRIBUTION.md)。
