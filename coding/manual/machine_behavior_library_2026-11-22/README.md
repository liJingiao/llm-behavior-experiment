# 机器行为实验组件库

2026-11-22 定稿。用243篇开发论文训练组件知识库，逐项处理381个知识缺口，逐号审视原69个组件。项目负责人确认采用65个独立组件的结构。新109篇保留作评测候选。

## 从这里开始

| 我想做什么 | 打开哪份文件 |
|---|---|
| 设计机器行为实验，查某个组件怎么用 | [65项组件手册](COMPONENTS.md)。每项说明怎样操作、怎样解释，相关条目可进入具体方法。 |
| 查一项为什么保留、改写、合并或移出 | [原69项组件修订记录](COMPONENT_REVISIONS.md)。按原编号查原条款、论文用例、共同决定和内容去向。 |
| 查论文具体教会了我们什么 | [381项缺口处理结果](TRACEABILITY.md)。每行可读本轮处理、实际段落与原论文证据，也可[从原建议承接组件查方法](TRACEABILITY.md#by-component)。 |
| 写论文里的训练方法 | [组件库训练方法 v1.1](TRAINING_METHOD.md) · [执行工作流](TRAINING_WORKFLOW.md#component-training) |

## 这轮训练改了什么

我们从开发论文的实际操作出发，对照训练前的69项组件手册及其附录，逐项判断原库能指导到哪一步。下表按具体知识点计数。[原库支持与缺口依据](../../../analysis/literature_component_coverage/data/gaps.json)

| 缺口处理结果 | 项数 | 一个具体例子 |
|---|---:|---|
| 原库缺少具体做法，定稿正文补入操作指导 | 260 | 从模型接口读取指定候选词的概率，区分接口返回的数值与没有返回的候选项。[具体记录](TRACEABILITY.md#gap-kg_prob_token_read) |
| 原库已指导一部分，定稿正文补全步骤或适用条件 | 118 | 同一题在两个条件下作答，按题成对抽取两列并重算差异。[具体记录](TRACEABILITY.md#gap-kg_boot_paired) |
| 复用训练前原库 | 1 | n-back 的匹配规则已写在构念任务附录。[具体记录](TRACEABILITY.md#gap-worker_2_nback_generation_gap) |
| 仅属真人参照，列在机器训练范围外 | 2 | 第003篇的真人试次合并拟合、第078篇对历史国会议员用词所做的平滑分析。[003](TRACEABILITY.md#gap-kg_unit_estimand) · [078](TRACEABILITY.md#gap-kg_smooth_lowess) |

381个编号均有结果，待补0项，未处理0项。定稿方法正文共10章、150个小节。多个知识点可以共用一个小节，例如配对重抽样与有限次重抽样的区间端点都在[统计分析第12节](K01_statistics.md#k01-12)。

原69项中，59项保留原职责，6项保留编号并改写，分别为 B1、B2、D1、D5、E4、E5。B10并入B2，C7并入C2，D4并入D3。D2“疲劳效应”移出独立目录，机器实验仍用得到的位置、重复和顺序控制分别有承接条目。[按原编号查看](COMPONENT_REVISIONS.md)

## 按主题查方法

| 方法正文 | 本章处理的缺口数 |
|---|---:|
| [K01 统计分析](K01_statistics.md) | 114 |
| [K02 标注、裁决与信度](K02_annotation_reliability.md) | 16 |
| [K03 文本与语义评价](K03_text_semantics.md) | 36 |
| [K04 概率取得、条件化与分布比较](K04_probability.md) | 37 |
| [K05 校准、区分能力与排序评价](K05_evaluation.md) | 15 |
| [K06 认知模型、因果推断与符号方法](K06_cognitive_causal.md) | 74 |
| [K07 动态状态、记忆与外部执行](K07_state_execution.md) | 15 |
| [K08 模型内部测量与临时干预](K08_internal_methods.md) | 22 |
| [K09 材料构造、图结构与表征几何](K09_structure_geometry.md) | 51 |
| [K10 可解密的公开材料发布](K10_release.md) | 1 |

## 怎样复查

从[逐项对应表](TRACEABILITY.md)点缺口编号，可看到论文号、需求号、事实号和证据号，再查论文里的操作。381个缺口共关联951条缺口与论文需求的对应关系，涉及215篇开发论文的898条不同需求。开发文献总数为243篇。若要了解某篇论文缺了哪些设置，按实例读原始记录；本轮补进手册的通用方法不回填到论文事实中。

每个缺口的处理履历保存在[分章记录](records/)中。可分别查阅[需求与论文依据](TRACEABILITY.md#paper-evidence)、[方法来源](SOURCES.md)和[训练前手册](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md)。原论文的覆盖评级沿用训练前口径。
