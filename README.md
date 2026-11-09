# llm-behavior-experiment

中关村学院科研实践营项目 · 面向大语言模型行为实验的组件资源库与协议生成平台

---

## 当前可用材料

| 内容 | 阅读入口 |
|---|---|
| 69项组件的定义与使用要求 | [组件手册v1.4](coding/manual/实验组件_v1.4.md) |
| 旧243篇的组件支持与知识缺口 | [243篇分析成果](analysis/literature_component_coverage/README.md) |
| 新109篇评测候选文献的方法需求与组件关系 | [109篇对应成果](analysis/test_candidate_component_matching/README.md) |

论文正文与两批文献的筛选范围见[文献总入口](literature/README.md)。两批成果分别保留，具体用途和统计口径见下文。

## 文献中的组件使用与知识缺口

基于243篇已入选文献，查看69项组件的使用频率、方法知识支持及381项具体补充建议。

- [成果阅读入口](analysis/literature_component_coverage/README.md)：先看两张主要结果表，再用真实论文例子理解单元、事实和方法需求。
- [可筛选工作簿](analysis/literature_component_coverage/tables/组件覆盖与补缺.xlsx)：组件频率、具体缺口、方法关联及文献索引；A/B链接需随完整目录使用。
- [整理标准与统计口径](analysis/literature_component_coverage/METHODS.md)：计数、支持等级与证据定位。

本成果评价组件知识对论文方法的支持，与 `coding/results/` 的论文设计和报告评分分开；知识覆盖不等于实验复现成功。

## 109篇评测候选文献与组件需求对应

从新增文献的具体研究方法出发，整理其与现有69项组件的关系，供后续评测任务设计查阅。

- [成果阅读入口](analysis/test_candidate_component_matching/README.md)：109篇文章、279条方法需求及705条需求与组件关系，涉及39项组件。
- [可筛选工作簿](analysis/test_candidate_component_matching/tables/109篇文献组件需求配对.xlsx)：文章目录、需求对应和组件反查；下载完整仓库后可沿相对链接查阅依据和正文。
- [论文全文与索引](literature/test_candidates/README.md)：109篇主版本PDF、来源和当前时间资格。
- [整理方法与统计口径](analysis/test_candidate_component_matching/METHODS.md)：原文事实、需求、组件对应及解释边界。

本成果整理的是方法需求与组件的关系，未新增组件或生成正式评测task。时间依据支持104篇，另5篇待补；最终测试集尚未定稿。旧243篇成果继续用于组件知识分析，两批结果分别保留。

## 平台模块规划

以下为平台的三个模块方向。当前main中的`components/`、`constructs/`、`protocols/`和`runner/`只有占位文件；现有组件知识文档位于`coding/manual/`。

| 模块 | 说明 | 对应目录 |
|---|---|---|
| 行为实验组件资源库 | 把实验范式拆成可复用的最小单元（刺激模板、应答格式、计分逻辑） | `components/` |
| 协议生成 Copilot | 由构念与实验目标出发，生成结构化实验协议 | `constructs/`, `protocols/` |
| 实验 Runner | 执行协议、调用模型、记录原始输出与日志 | `runner/` |

## 目录结构

```
literature/     论文正文、文献索引与筛选依据
coding/         组件手册、编码规则与论文设计和报告评分
analysis/       组件知识覆盖分析与评测候选文献需求对应
components/     组件实现（预留）
constructs/     构念体系与结构定义（预留）
protocols/      实验协议及版本记录（预留）
runner/         实验执行与日志（预留）
docs/           会议纪要、设计文档、周报（预留）
```
