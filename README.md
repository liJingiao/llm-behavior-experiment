# llm-behavior-experiment
llm-behavior-experiment

中关村学院科研实践营项目 · 面向大语言模型行为实验的组件资源库与协议生成平台

15 周研究原型（MVP）。目标是把 LLM 行为实验从「一次性脚本」变成「可复用组件 + 可生成协议 + 可复现执行」的流程。

三个模块
模块	说明	对应目录
行为实验组件资源库	把实验范式拆成可复用的最小单元（刺激模板、应答格式、计分逻辑）	components/
协议生成 Copilot	由构念与实验目标出发，生成结构化实验协议	constructs/, protocols/
实验 Runner	执行协议、调用模型、记录原始输出与日志	runner/
目录结构
constructs/     构念体系定义与 schema
components/     行为实验组件资源库
protocols/      实验协议及版本记录
runner/         实验执行与日志
coding/         coding manual、rubric、信度记录
analysis/       数据分析脚本与结果
docs/           会议纪要、设计文档、周报

每个目录下的 README.md 说明该目录的文件命名与格式约定，新增文件前先读。
