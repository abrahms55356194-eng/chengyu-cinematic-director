# 失败诊断

生成前逐项检查风险；有视频时记录时间段、可见证据、影响与最小修订。不根据提示词推断视频已成功。无视频只标预测风险。

|风险|证据|最小修复|
|---|---|---|
|Face Drift|转脸时五官跳变|固定脸部参考，减小极端转角|
|Identity Drift|跨镜换人|复用唯一角色 ID 与同一身份资产|
|Wardrobe Drift|衣服颜色款式变|锁服装层次与当前湿污状态|
|Camera Path Failure|穿墙或瞬移|画出净空路径并缩短距离|
|Camera Shake|无因抖动|只改稳定方式与运动幅度|
|Anatomy Failure|手指肢体错位|减少遮挡重叠，分开手部动作|
|Action Physics Failure|滑步提前受击|分离发力接触反馈并标支撑脚|
|Prop Discontinuity|换手消失|锁持有人左右手与交接节点|
|Environment Drift|门窗位置漂移|固定地标与可见空间，不虚构背面|
|Lighting Inconsistency|光源方向跳变|锁主源方向及跨镜时间|
|VFX Integration Failure|贴纸光效|补遮挡接触反射与残留|
|Timing Overload|动作未完成|拆镜或延时，保原剧情|
|Audio Desynchronization|错人说话口型偏差|逐字绑定说话者，留朗读时间|
|Motion Blur Failure|主体不可读|匹配跟随速度，降低模糊强度|
|Composition Failure|主主体被遮|只改机位或遮挡关系|
