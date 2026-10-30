# llm-behavior-experiment

中关村学院科研实践营项目 · 面向大语言模型行为实验的组件资源库与协议生成平台

---

## 三个模块

| 模块 | 说明 | 对应目录 |
|---|---|---|
| 行为实验组件资源库 | 把实验范式拆成可复用的最小单元（刺激模板、应答格式、计分逻辑） | `components/` |
| 协议生成 Copilot | 由构念与实验目标出发，生成结构化实验协议 | `constructs/`, `protocols/` |
| 实验 Runner | 执行协议、调用模型、记录原始输出与日志 | `runner/` |

## 目录结构

```
constructs/     构念体系定义与 schema
components/     行为实验组件资源库
protocols/      实验协议及版本记录
runner/         实验执行与日志
coding/         coding manual、rubric、信度记录
analysis/       数据分析脚本与结果
docs/           会议纪要、设计文档、周报
```

## 文献中的组件使用与知识缺口

基于243篇已入选文献，查看69项组件的使用频率、方法知识支持及381项具体补充建议。

- [成果阅读入口](analysis/literature_component_coverage/README.md)：先看两张主要结果表，再用真实论文例子理解单元、事实和方法需求。
- [可筛选工作簿](analysis/literature_component_coverage/tables/组件覆盖与补缺.xlsx)：组件频率、具体缺口、方法关联及文献索引；A/B链接需随完整目录使用。
- [整理标准与统计口径](analysis/literature_component_coverage/METHODS.md)：计数、支持等级与证据定位。

本成果评价组件知识对论文方法的支持，与 `coding/results/` 的论文设计和报告评分分开；知识覆盖不等于实验复现成功。
