# 输出与结构化审核

先写导演方案，再编译自然语言提示词。脚本不自动理解剧本，也不生成电影创意。

## 可复制正文

视觉统一约束 → 每份实际上传素材的用途和排除项 → 按时间顺序的镜头（机位、路径、主体动作、光源、结束状态）→ 声音 → 必要连续性约束。每生成组单独代码块；设置、评分和风险报告放在代码块之外。素材标记和音频符号先查 [适配器](seedance-2.5-adapter.md)，未验证的语法不要称为原生语法。

## JSON 审核接口

数字时间字段仅用于内部估算预算及顺序审核，不是自动插入提示词的模型控制语法。用户未指定事件时段时，最终正文按开始／发展／结束编译；可仅输出经过语义复核的自然语言稿，未运行 JSON 校验就不得声称脚本通过。

完整可运行结构见 [cases.json](../tests/cases.json)。顶层：source_facts 为从原文提取的事实列表；locked_facts 为方案保留事实，二者逐项比较；source_dialogue / dialogue 比较原始对白；characters 是角色 ID 到身份描述映射；duration 是生成组秒数；needs_vfx 是剧情是否需要特效；shots 为连续镜头列表。

每镜 start/end 为秒，characters 为角色 ID 数组（环境镜头为空）；camera、lighting、action、按需 vfx 的必填键见 [校验器](../scripts/validate_prompt.py) 的 FIELDS。start_state/end_state 为相同语义键的状态字典，记录位置、朝向、视线、手持物、衣着、光源和声音。镜间变化必须在 transitions 中逐键解释，且由人工核实解释确实在剧本或镜头中成立。contradictions 记录未解决矛盾；有内容则阻断。

把 cases.json 的一个对象保存为 plan.json，然后运行 `py scripts/validate_prompt.py plan.json`（非 Windows 环境可用 `python`）。这个接口是本项目内部格式，不是 Seedance API 请求体。

可直接运行 `py scripts/validate_prompt.py examples/structured-plan.json`。assets 是实际上传标签到 {scope, exclude} 的字典；每镜 references 列出引用标签，未绑定会阻断。脚本只核对声明，不能证明文件真的上传。passed 只表示结构通过；text_quality_passed 另需 semantic_review 的 passed=true 和非空 evidence，由审查者填写，绝不能由脚本伪造。
