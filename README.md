# CHENGYU CINEMATIC DIRECTOR

版本 1.0.0。中文电影预制作与 Seedance 2.5 提示词 Skill，包含八个专业引擎、按需参考库、文本质检和连续性检查。无需视频 API 密钥，不消耗生成积分。

## 使用

在 Codex 中输入：

```text
$chengyu-cinematic-director
把下面剧本转换为电影提示词：雨夜，姐姐把钥匙放在桌上，告诉弟弟“我明天走”。弟弟握住钥匙，没有回答。保持对白与结局，16:9，克制写实。
```

也可提供参考图、已生成片段或失败时间段，要求修复身份、机位、动作或连续性。参考图只继承指定职责，不能凭空声称看过未提供的素材。

主入口仅加载必要规则；复杂任务按需读取 references。设备预设为视觉参考，不保证复刻设备成像。模型适配证据见 references/RESEARCH_SOURCES.md；官方 sd25-pe 是研究来源，并非运行依赖。

## 安装

将本目录复制到用户级 `~/.agents/skills/chengyu-cinematic-director`，保留 SKILL.md、agents、references、scripts、tests 和 examples。若已有同名目录，先比较版本并另存备份，不直接覆盖。重新打开会话后通过名称调用。

本项目为独立目录，不需要修改其他项目配置或安装第三方 Python 包。Windows 使用 `py`，其他环境使用 Python 3。

## 质量边界

自动检查可发现结构缺失、引用和时间轴问题；剧情忠实度、摄影可执行性、表演可信度仍需对照原文和实际视频审查。文本评分不等于生成视频质量，不能承诺一次成功。不会自动调用付费视频 API。

专业示例在 examples，来源及许可证处理在 ATTRIBUTION.md。各脚本的 `--help` 提供输入要求；开发测试使用 `py -m unittest discover -s tests -v`。

## 本地验证

在仓库根目录执行（Linux/macOS 将 `py` 换成 `python3`）：

```powershell
py -m unittest discover -s tests -v
py scripts/validate_skill.py
py scripts/validate_prompt.py examples/structured-plan.json
py scripts/continuity_check.py examples/structured-plan.json
```

[结构化样例](examples/structured-plan.json) 是校验器输入，不是 Seedance 请求体；[字段说明](references/prompt-templates.md) 说明事实、对白、角色、素材职责、镜头和边界状态。`passed` 仅表示结构检查通过；`text_quality_passed` 还要求审查者填写语义审核及依据。事实相等只比较输入声明，不能证明提示词忠实于原始剧本；分数也不能证明物理可执行性。示例默认未做语义签核，返回 `text_quality_passed: false` 属于预期行为。测试数据是合成工程夹具，并非视频成功案例。

GitHub Actions 自动运行同样的标准库测试、包资源检查和样例验证，不调用生成服务。
