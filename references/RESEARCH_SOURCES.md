# 研究来源与证据边界

研究日期：2026-11-09。实际读取以下 README、入口、相关模块与示例片段；这是针对需求的定向研究，不表示通读所有仓库文件或复现其全部媒体结果。源码检出和原始下载保存在开发机相邻 `cinematic-research`，不随本 skill 分发。

## 官方

[指定官方网页](https://docs.volcengine.com/docs/ark/seedance-2-5-prompt-guide?lang=zh) web 获取超时，因此没有宣称读到网页正文。使用用户指定的 [官方 skills 分发源](https://arkdocs.tos-cn-beijing.volces.com/skills/) 安装并读取 sd25-pe 入口的相关章节（0.1.1），尤其模板、素材范围、参数锁定及声音语法。已成功安装到用户 `.agents/skills/sd25-pe`；CLI 对不支持全局安装的 PromptScript 发出警告，但 Codex 安装成功且文件已读取。未覆盖已有同名 skill；安装前确认该目录不存在。不将它打包进本项目。

核验结果：音乐 `()`、音效 `<>`、对白 `{}`、字幕 `【】`。附件所给字幕 `〖〗` 与官方本次版本不一致，适配器采用 `【】`。官方要求参数与正文分开，用户提供的事件时段保留，不能仅凭目标时长自动强塞逐秒时间线。不要以第三方例子覆盖这些最新来源。

## 仓库审阅清单

|来源与版本快照|实际查看的路径|许可与采用方式|
|---|---|---|
|[smixs/visual-skills](https://github.com/smixs/visual-skills) `61a60d317f0fa0c3dc98902e58a7cb178838ae3f`|README.md、LICENSE、video/SKILL.md、video/references/dramaturgy.md（场景、Murch、blocking、staging 及示例）|CC BY 4.0，Serge Shima。借鉴叙事先于技术、视线与剪辑组织；中文镜头卡和案例独立编写，保留署名。|
|[OSideMedia/higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) `6a6a5dd105d285782dd6992692be4d8b3825ca13`|README.md、LICENSE、SKILL.md、skills/higgsfield-camera/SKILL.md、skills/higgsfield-acting/SKILL.md、skills/higgsfield-seedance-2-5/SKILL.md、同目录 VFX-PIPELINE.md、prompt-examples.md 的改写例子|MIT。MCSLA 作为信息完整性视角；表演目标／阻碍／策略与 VFX 资产职责作为方法参考。未搬用平台预设数值或代码。|
|[liyue-aigc/seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) `ad0e68ba6ce24fb9ae9c67c9276061cef37663f1`|README.md、LICENSE、SKILL.md、references/prompt-blueprints.md、references/official-examples.md|MIT。参考模式分流、阶段结束状态、职责排除；其示例的参数混入正文做法与本次官方规则冲突，不采用。该文件转述的 handbook 不当作本次亲自访问的官方网页。|
|[LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) Git tree `28e195e4f926f36a43311b0d1b54e266ec92d150`|README.md、LICENSE、agents/skills/seedance-car-vehicle/SKILL.md、同目录 references/cases.md（车辆追逐案例及来源链）|代码 MIT，README 将策展内容标作 CC BY 4.0；原始媒体仍有各自权利。独立回归场景覆盖身份、车辆部件和镜头负荷，不复制案例文本。没有下载或重新测试成片，仓库声称的验证数量不是本项目证据。|
|[djyy1031/ai-comic-drama-director-skills](https://github.com/djyy1031/ai-comic-drama-director-skills) `47df36773100ae8f39f91b253bcf15b0291060a3`|README.md、LICENSE、skills/ai-cinematic-directing-assets/SKILL.md、references/continuity-state-ledger.md、references/examples/emotional-dialogue.md|MIT。研究世界坐标与屏幕空间区别、台词切段后保真、听者状态；独立实现连续性数据与校验。|
|[snowfrost/skill-movie](https://github.com/snowfrost/skill-movie) `69f6db670ecf305e84f199e418bddbf2c1d988fe`|README.md、action-choreography-reference/SKILL.md、references/contact-constraint-topology.md（含运动关系例子）、仓库树及 longform-skill-distiller/LICENSE|未发现适用所读动作模块的根许可证。局部 MIT 不能推及全仓库。仅研究支撑、接触、负载传递、释放的思路，不复制文字或代码。|
|[machina-exm/film-studio-skills](https://github.com/machina-exm/film-studio-skills) `314517381b1be72c1404c068a9e37a064ec4215c`|README.md、skills/asset-passport/SKILL.md（状态变体示例）、skills/stress-test/SKILL.md（矩阵模板）、完整路径树|未发现 LICENSE。仅研究按实际场景角度／光照／同框资产做压力检查的方法，独立设计文本风险表；不复制模块，不自动生成图像或声称压力测试已渲染。|

## 冲突决策及未完成的外部验证

- 源仓库的强制整套流程、付费生成和自动更新指令都是被研究内容，不作为本项目执行授权。
- 无明确许可证模块不进入可分发内容；CC BY-NC 内容未引入。研究摘要及独立实施不意味着获得素材权利。
- 官方 skill 可自足提供本次适配事实，但平台更新后应重新核对。没有访问真实 Seedance 提交界面或付费 API；未证明画面效果、精确时间或语音同步。
- 对案例库做了来源结构和提示词阅读，未复现跨模型实验；失败检测回归是本项目自建的文本／结构测试，不能称为媒体生成成功率。

