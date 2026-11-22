# 机器行为实验组件手册

本版收录65个独立组件。按研究问题选择条目，每条给出机器侧可实施的操作、适用条件和方法小节。原69个编号与开发论文的对应保存在[组件修订记录](COMPONENT_REVISIONS.md)；3个并入相邻组件的编号和1个移出独立目录的编号列在文末[历史编号与去向](#historical-ids)。

## 变量和测量定义

<a id="a1"></a>
### A1 自变量

把要操纵的因素写成实际会改变的输入或运行步骤，列出取值、分配单位、比较对象和保持相同的设置。若多个操作一起变，结论只归于整个条件。

[原条款 A1，第159–220行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K08-09](K08_internal_methods.md#k08-09) · [修订依据](COMPONENT_REVISIONS.md#rev-a1)

<a id="a2"></a>
### A2 因变量

先按研究问题确定观测单位。答案正确可以按题计，谈判是否达成协议可以按整局计。为所选单位写明观察事件、计分规则和方向、分母、无效输出的处理以及重复观测的汇总方式。模型裁判与人工评分都应留存原始结果，便于检查指标差异。

[原条款 A2，第221–281行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K04-01](K04_probability.md#k04-01) · [K02-01](K02_annotation_reliability.md#k02-01) · [关联方法小节](TRACEABILITY.md#methods-a2) · [修订依据](COMPONENT_REVISIONS.md#rev-a2)

<a id="a3"></a>
### A3 控制变量

列出目标操纵以外可能影响输出的条件，说明哪些已固定或匹配。对只能记录的版本、上下文或提示差异，检查它们是否随实验条件一起变化，并据此限定解释。保留各请求的实际配置。

[原条款 A3，第282–342行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K07-02](K07_state_execution.md#k07-02) · [修订依据](COMPONENT_REVISIONS.md#rev-a3)

<a id="a4"></a>
### A4 混淆变量

若目标条件同时改变提示长度、答案线索或执行轮数，列出替代解释；设置只变目标成分的对照，或把能拆分的因素交叉。无法分离时限制因果表述。

[原条款 A4，第343–403行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K06-07](K06_cognitive_causal.md#k06-07) · [修订依据](COMPONENT_REVISIONS.md#rev-a4)

<a id="a5"></a>
### A5 调节变量

预先指定哪个模型属性或任务条件可能改变处理效应。分别估计各水平内的条件差异，再估计其差及不确定性。比较既有模型属性时记录伴随变化。

[原条款 A5，第404–464行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-16](K01_statistics.md#k01-16) · [K01-19](K01_statistics.md#k01-19) · [修订依据](COMPONENT_REVISIONS.md#rev-a5)

<a id="a6"></a>
### A6 中介变量

明确处理、中间量和最终输出，说明怎样测量或操纵中间量、在何种假设下识别间接路径。仅观察到解释文本与答案相关时，只报告这种联系。

[原条款 A6，第465–527行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K06-09](K06_cognitive_causal.md#k06-09) · [关联方法小节](TRACEABILITY.md#methods-a6) · [修订依据](COMPONENT_REVISIONS.md#rev-a6)

<a id="a7"></a>
### A7 操作性定义

把目标概念改写为可执行规则，给定输入、允许的输出、计分边界和反例。写明分数覆盖的范围，特别是使用封闭参照集时。

[原条款 A7，第528–588行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K06-19](K06_cognitive_causal.md#k06-19) · [关联方法小节](TRACEABILITY.md#methods-a7) · [修订依据](COMPONENT_REVISIONS.md#rev-a7)

<a id="a8"></a>
### A8 水平数与类型

列明各因素的类别或有序数值、取值范围、比较方式及各水平覆盖的题目。若高水平只适用于部分题，可在共同题集比较；若使用各自可用的题，解释结果时交代题集构成的变化。仅观察两个水平时，报告两点差异；需要区分曲线形状时安排足够的中间水平。

[原条款 A8，第589–649行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-a8)

<a id="a9"></a>
### A9 单一操作化的风险

选择另一种能表达相同研究问题的任务或材料，再检查效应方向和大小。逐项说明两种操作还改变了什么，以及哪些结论只适用于其一。

[原条款 A9，第650–709行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [F3 构念效度与任务变体](#f3) · [修订依据](COMPONENT_REVISIONS.md#rev-a9)

<a id="a10"></a>
### A10 单一方法的风险

为同一输出引入原理不同的测量途径，例如规则计分和匿名人工评分。按相同输出对齐结果，分报一致处和分歧处，并追查共享输入或判据。

[原条款 A10，第710–774行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K02-01](K02_annotation_reliability.md#k02-01) · [修订依据](COMPONENT_REVISIONS.md#rev-a10)

## 实验设计

<a id="b1"></a>
### B1 不同实验单位间的条件比较

先指定分配单位，例如任务材料、独立运行轨迹或模型实例，再把不同单位分给不同条件。报告单位数及共享题目、版本或历史；新开会话不会消除其他层的相关性。

[原条款 B1，第775–835行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-01](K01_statistics.md#k01-01) · [修订依据](COMPONENT_REVISIONS.md#rev-b1)

<a id="b2"></a>
### B2 同一实验单位的配对与重复测量

用相同题目、轨迹或同一次运行的前后测量形成配对，保留配对键，分析同一单位的差异。实施前判断可否重置处理、顺序是否留下方向不同的影响，以及研究是否本就需要历史；若先前处理留下不可逆状态、而研究的是各条件的独立影响，就在彼此隔离的运行中分别实施；两边做的是同一道题时仍可按题配对。

[原条款 B2，第836–896行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-05](K01_statistics.md#k01-05) · [K01-12](K01_statistics.md#k01-12) · [修订依据](COMPONENT_REVISIONS.md#rev-b2) · [原编号 B10](#b10)

<a id="b3"></a>
### B3 混合设计

同时存在单位间与单位内因素时，先画出每个因素在哪层变化。例如不同轨迹分配提示策略，每条轨迹重复测若干轮。写清每层单位数，分析时保留单位内相关。

[原条款 B3，第897–957行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-18](K01_statistics.md#k01-18) · [修订依据](COMPONENT_REVISIONS.md#rev-b3)

<a id="b4"></a>
### B4 因子设计

列出因素及水平组合，为每个组合安排观测，说明未覆盖格与顺序限制。用相同计分规则比较单因素变化和因素组合。

[原条款 B4，第958–1018行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-07](K01_statistics.md#k01-07) · [修订依据](COMPONENT_REVISIONS.md#rev-b4)

<a id="b5"></a>
### B5 主效应

指定在哪些其他因素水平及何种权重下进行平均，列出相应边际均值与差异。若交互明显，同时报告相应水平内的差异。

[原条款 B5，第1019–1078行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-19](K01_statistics.md#k01-19) · [修订依据](COMPONENT_REVISIONS.md#rev-b5)

<a id="b6"></a>
### B6 交互作用

指定两个因素的效应尺度，分别计算各条件内的差异，再比较这些差异；报告对比方向和区间。一个子组显著、另一子组不显著不足以确定交互。

[原条款 B6，第1079–1138行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-16](K01_statistics.md#k01-16) · [修订依据](COMPONENT_REVISIONS.md#rev-b6)

<a id="b7"></a>
### B7 区组设计

有把握预先识别题型、难度、平台或时段差异时，先按其分区组。在随机区组设计中，在各组内随机分配条件或运行顺序，保留实际分配结果。分析保留组别，以相同区组内的差异估计处理效果。

[原条款 B7，第1139–1199行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [C1 随机分配](#c1) · [NIST 随机区组设计](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm) · [修订依据](COMPONENT_REVISIONS.md#rev-b7)

<a id="b8"></a>
### B8 拉丁方

把 k 套顺序排成 k 行、k 个位置排成 k 列。每个条件在每一行内和每一列内都恰好出现一次。按这些顺序安排运行，并核对各顺序的实际使用次数。普通拉丁方只保证位置平衡；若关心相邻条件，再核对有序对频数。

[原条款 B8，第1200–1260行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-b8) · [原编号 C7](#c7)

<a id="b9"></a>
### B9 准实验设计

比较自然发生的版本更新或非随机开放的模型配置时，先说明分配机制和可比参照，再检查同一时段的题目、用户和系统变化。没有可识别的对照时按观察性差异解释。

[原条款 B9，第1261–1320行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K06-07](K06_cognitive_causal.md#k06-07) · [修订依据](COMPONENT_REVISIONS.md#rev-b9)

## 条件控制

<a id="c1"></a>
### C1 随机化

指明随机的是题目、标签、条件、顺序还是运行时段，给出候选集合、限制、抽取单位及复用规则。保存实现的分配结果；随机抽材料与随机分配处理分开报告。

[原条款 C1，第1385–1445行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K09-01](K09_structure_geometry.md#k09-01) · [修订依据](COMPONENT_REVISIONS.md#rev-c1)

<a id="c2"></a>
### C2 平衡

在各条件交换角色、位置或顺序，使比较不被先手或某一位置主导。按目标选择全排列、拉丁方或ABBA。各位置等权时，ABBA可平衡随序位线性变化的趋势，普通拉丁方平衡位置；针对前序作用，另检有序相邻对的覆盖。

[原条款 C2，第1446–1505行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [B8 拉丁方的排列与核对](#b8) · [修订依据](COMPONENT_REVISIONS.md#rev-c2) · [原编号 C7](#c7) · [原编号 D2](#d2)

<a id="c3"></a>
### C3 恒定

在比较前列明固定的模型快照、系统提示、解码和输出长度等参数；对无法控制的服务端设置记录未知或日期。模型间不支持同一接口时说明可比边界。

[原条款 C3，第1506–1565行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K07-02](K07_state_execution.md#k07-02) · [修订依据](COMPONENT_REVISIONS.md#rev-c3)

<a id="c4"></a>
### C4 匹配

给处理和对照建立配对键，列出要匹配的属性、匹配前后差异和拆对规则。比较用同一对材料中的输出；不能匹配的维度保留为潜在混淆。

[原条款 C4，第1566–1625行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K09-05](K09_structure_geometry.md#k09-05) · [修订依据](COMPONENT_REVISIONS.md#rev-c4)

<a id="c5"></a>
### C5 纳入为变量

在设计中保留可能影响结果的题目或运行属性；说明为何调整、如何编码、在哪层变化。估计总效应时，先判断该变量是否受处理影响；若仍要固定处理之后产生的量，须说明调整后要估计的效应。需要校正试次位置或会话时段时，可将其纳入模型，但位置与条件完全重合时不能分别估计。

[原条款 C5，第1626–1686行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-16 回归](K01_statistics.md#k01-16) · [K06-07 因果调整](K06_cognitive_causal.md#k06-07) · [修订依据](COMPONENT_REVISIONS.md#rev-c5) · [原编号 D2](#d2)

<a id="c6"></a>
### C6 盲法

向人工或模型评分者隐藏可能透露来源或条件的名称，随机化呈现顺序并统一其余判据。记录哪些身份已遮蔽、哪些仍可由风格推断。

[原条款 C6，第1687–1747行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K02-01](K02_annotation_reliability.md#k02-01) · [修订依据](COMPONENT_REVISIONS.md#rev-c6)

## 历史与时序

<a id="d1"></a>
### D1 重复试次与反馈下的表现变化

按轨迹记录试次号、模型可见的示例与反馈。用难度可比的材料描述同一轨迹的早晚变化。要估计反馈的作用，在对应轮次另设材料和历史可比的有、无反馈条件，再比较表现。跨会话差异单独统计。

[原条款 D1，第1838–1897行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K07-02](K07_state_execution.md#k07-02) · [修订依据](COMPONENT_REVISIONS.md#rev-d1)

<a id="d3"></a>
### D3 延滞与迁移效应

记下当前试次会收到的历史、反馈和持久状态。区分只测当前条件与有意测历史影响；前者可重置会话并控制外部记忆。若有方向依赖，比较A后测B、B后测A和各自无前序基线，分别报告两个方向。若要判断A的具体内容对B有何影响，再用一段轮次相同、长度相近的其他前文替换A，比较两组随后对B的回答。

[原条款 D3，第1958–2017行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K07-05](K07_state_execution.md#k07-05) · [修订依据](COMPONENT_REVISIONS.md#rev-d3) · [原编号 B10](#b10) · [原编号 D4](#d4) · [原编号 D2](#d2)

<a id="d5"></a>
### D5 背景取值范围对判断的影响

把同一个目标刺激嵌入窄范围、宽范围或不同分布的示例中；保持目标、锚点和位置可比，记录回答刻度是否变化。若背景不可见，说明模型实际接收了哪些范围线索。

[原条款 D5，第2078–2149行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-d5)

## 反应与评分偏差

<a id="e1"></a>
### E1 位置与顺序偏差

对同一组刺激、题目或处理改变呈现次序，保留原始内容标识和每种顺序的样本数。若需诊断多选或模型裁判具体偏向哪个答案槽位，进一步使用[J1](#j1)。

[原条款 E1，第2150–2210行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-e1)

<a id="e2"></a>
### E2 默认赞同

围绕同一主题配对方向相反、含义可比的陈述，保留原始作答方向。态度题分别统计正反向陈述的同意率，可另看同一对两侧均获赞同的比例。有可核验答案时，平衡应答肯定和应答否定的题，再分别报告两类正确率及每对都答对的比例。

[原条款 E2，第2211–2270行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K04-10 可取得标签概率时的先验校准](K04_probability.md#k04-10) · [修订依据](COMPONENT_REVISIONS.md#rev-e2)

<a id="e3"></a>
### E3 极端与中间反应倾向

公布各刻度的文本锚点、数值映射及无效输出处理；比较端点或中间类别的选择比例。要解释为作答倾向，使用相同或内容、计分方向可比的题目，查看这种选择是否跨题持续出现。改用不同锚点或候选顺序时报告分布变化，按序数处理未经验证的量尺。

[原条款 E3，第2271–2330行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K05-01](K05_evaluation.md#k05-01) · [修订依据](COMPONENT_REVISIONS.md#rev-e3)

<a id="e4"></a>
### E4 任务目的线索对回答的影响

查找题面和示例中可能直接透露分类标签或预期答案的字眼。保留语义可比的去线索版本，与原版本对比；只筛去字眼时如实记录筛选，勿据此断言模型已推知研究假设。

[原条款 E4，第2331–2390行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-e4)

<a id="e5"></a>
### E5 提示编制与评分线索的影响

固定编制和预处理规则，把模型身份、自我评价等非评分内容从裁判输入中隔离；向各条件应用同一处理。若研究问题恰是线索影响，保留有线索和无线索的平行条件。

[原条款 E5，第2391–2450行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K02-01](K02_annotation_reliability.md#k02-01) · [修订依据](COMPONENT_REVISIONS.md#rev-e5)

<a id="e6"></a>
### E6 天花板与地板效应

在条件比较前检查各题难度、各模型得分分布及达到边界的比例。报告边界附近仍能分辨多大差异；得分挤在上限时可加难题，挤在下限时可加易题，也可换用能分辨边界附近表现的指标。原题集和调整后的结果分别报告。

[原条款 E6，第2451–2510行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-24](K01_statistics.md#k01-24) · [修订依据](COMPONENT_REVISIONS.md#rev-e6)

<a id="e7"></a>
### E7 共同方法偏差

当操纵材料与评分标准共享线索，或两个指标由同一裁判、相似措辞的量表产生时，指出两者共同受什么影响。尝试换用独立的裁判或客观判据并交叉比较，不能只凭分数相关断言共同来源造成差异。

[原条款 E7，第2511–2588行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K02-01](K02_annotation_reliability.md#k02-01) · [修订依据](COMPONENT_REVISIONS.md#rev-e7)

## 效度

<a id="f1"></a>
### F1 统计结论效度

从题目、运行或轨迹定义独立单位与目标统计量，再选估计与区间。配对重抽按同一索引取两侧结果，簇内观测一起保留；按给定约定从排序结果取区间端点，区分区间和检验。报告重复次数、筛选和不确定性来源。

[原条款 F1，第2589–2663行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-01](K01_statistics.md#k01-01) · [K01-12](K01_statistics.md#k01-12) · [K01-14](K01_statistics.md#k01-14) · [关联方法小节](TRACEABILITY.md#methods-f1) · [修订依据](COMPONENT_REVISIONS.md#rev-f1)

<a id="f2"></a>
### F2 内部效度

沿处理到输出追查同时变化的材料、模型服务和评分规则，安排能隔离目标操作的对照。若模型版本中途变更，分段注明哪一条件经历了变更及是否可比。

[原条款 F2，第2664–2739行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K06-07](K06_cognitive_causal.md#k06-07) · [修订依据](COMPONENT_REVISIONS.md#rev-f2)

<a id="f3"></a>
### F3 构念效度

说明预期测量的能力或倾向和竞争解释，用同构任务变体、应当相关或无关的指标检查结果。同步审视输出格式、泄漏与评分过程；给每种证据限定它支持的解释。

[原条款 F3，第2740–2820行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K02-06](K02_annotation_reliability.md#k02-06) · [K06-11](K06_cognitive_causal.md#k06-11) · [关联方法小节](TRACEABILITY.md#methods-f3) · [修订依据](COMPONENT_REVISIONS.md#rev-f3)

<a id="f4"></a>
### F4 外部效度

指明结论希望推广到哪些题目、模型、时间和交互对象。分别列出已覆盖与尚未覆盖的范围，在替换题域、对手或接口后比较效果。

[原条款 F4，第2821–2899行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-15](K01_statistics.md#k01-15) · [修订依据](COMPONENT_REVISIONS.md#rev-f4)

## 分析与报告

<a id="g1"></a>
### G1 分析单位

先说明一次运行、一题、一条消息各贡献几次观测，选择与推断目标一致的分母。按题汇总时保留题内重复，按模型比较时区分相同题、种子或历史造成的关联。

[原条款 G1，第2900–2959行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-01](K01_statistics.md#k01-01) · [关联方法小节](TRACEABILITY.md#methods-g1) · [修订依据](COMPONENT_REVISIONS.md#rev-g1)

<a id="g2"></a>
### G2 随机效应

根据数据来源列明题目、家族、提示或轨迹的嵌套与交叉结构。为有重复、希望推广的层级考虑随机截距及有足够组内变化的斜率；报告拟合失败及所用简化。

[原条款 G2，第2960–3019行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-18](K01_statistics.md#k01-18) · [修订依据](COMPONENT_REVISIONS.md#rev-g2)

<a id="g3"></a>
### G3 材料作为随机效应

要从现有题目推广到新材料时，说明材料来自哪里，同题出现在哪些模型或条件。给题目或文本设适当的聚集层或随机截距；若效果随材料变化且设计支持，再考虑随机斜率。

[原条款 G3，第3020–3079行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-18](K01_statistics.md#k01-18) · [修订依据](COMPONENT_REVISIONS.md#rev-g3)

<a id="g4"></a>
### G4 统计功效

先指定主要检验、希望检出的最小差异、显著性水平和目标功效（该差异存在时希望有多大概率检出）。按目标推断单位区分题目间和同题重复的波动。用试点、既有估计或明确的合理参数计算需要的题目和重复数，并给出重要假设下的敏感程度。

[原条款 G4，第3080–3139行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-26 相关检验的功效算例](K01_statistics.md#k01-26) · [关联方法小节](TRACEABILITY.md#methods-g4) · [修订依据](COMPONENT_REVISIONS.md#rev-g4)

<a id="g5"></a>
### G5 研究者自由度

固定与保留提示选择、重试、排除、缺失及多种评分方式的决定。若预先约定剔除后段试次，报告阈值和保留原观测的敏感性；区分因失败重试与看过结果后择优。

[原条款 G5，第3140–3200行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-14](K01_statistics.md#k01-14) · [修订依据](COMPONENT_REVISIONS.md#rev-g5) · [原编号 D2](#d2)

<a id="g6"></a>
### G6 预先设定与预注册

事先写明研究假设、主要比较、排除规则和分析分母，保留有日期的计划。采用预注册时，给出提交后内容固定、时间可核验的登记记录；使用既有数据时，交代登记前已接触了哪些数据或结果。披露偏离原因，后续有价值的探索单列。

[原条款 G6，第3201–3281行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [预注册说明](https://www.cos.io/initiatives/prereg) · [修订依据](COMPONENT_REVISIONS.md#rev-g6)

## 模型专项

<a id="j1"></a>
### J1 模型作答与裁判评分的位置偏差

保持选项内容不变，交换显示位置或标签，再将答案还原到同一内容。分别报告各位置选择率、换位后的内容一致率及平局；记录改变位置时是否也动了标签或文字。

[原条款 J1，第3282–3340行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K04-10](K04_probability.md#k04-10) · [修订依据](COMPONENT_REVISIONS.md#rev-j1)

<a id="j2"></a>
### J2 冗长偏差

比较不同长度回答时先保留原始胜率、长度单位及各条件长度分布。要检查裁判是否偏爱长回答，可把同一答案写成实质信息一致的简短版和展开版，交换呈现位置后比较裁判选择。要比较两个生成来源在相近长度下的胜率，可匹配长度或用模型调整，并列原始与调整后胜率，说明可比的长度范围。

[原条款 J2，第3341–3399行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [长度控制胜率的计算方法](https://arxiv.org/abs/2404.04475) · [修订依据](COMPONENT_REVISIONS.md#rev-j2)

<a id="j3"></a>
### J3 对用户立场的迎合

对同一问题设置中性、支持和反对意见等提示，保持事实内容、回答计分及上下文可比。观点题比较用户立场互换后回答是否随之翻转。对有可核验答案的题，分别记录与用户一致和事实正确两个事件，说明是否筛选了原先答对的题。

[原条款 J3，第3400–3457行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-j3)

<a id="j4"></a>
### J4 自我偏好

交叉安排生成者和评分模型，遮蔽身份后比较自家和其他来源回答。区分实际来源与显示标签，控制内容质量、长度和位置，说明差异随裁判或数据集怎样变化。

[原条款 J4，第3458–3515行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K02-01](K02_annotation_reliability.md#k02-01) · [修订依据](COMPONENT_REVISIONS.md#rev-j4)

<a id="j5"></a>
### J5 少样本示例选择与排列

保存示例池、抽取依据、与测试题的重叠检查及顺序。在内容不变时更换示例排列，另在顺序控制下更换示例集；分报题目与示例配置间的变动。

[原条款 J5，第3516–3574行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-j5)

<a id="j6"></a>
### J6 提示敏感性

选择研究目标和输出判据可比的措辞、格式或角色变体，在同一批题上配对比较，保留每种变体的结果。若某版本改变任务含义，单独作为不同条件解释。若目的是从中选出最佳提示，在开发材料上按事先确定的指标选定版本，保存所有候选及选择依据；在接触测试结果前固定完整提示，测试时沿用该版本。

例如，比较提示A和B的答对率时，答对记1分，答错记0分。每道题记一行。

| 题号 | 提示A得分 | 提示B得分 | 差值（B减A） |
|---|---:|---:|---:|
| 01 | 0 | 1 | +1 |

把所有题的差值取平均，就得到B相对A的答对率差。若按题重抽样估计这个差值的不确定性，每次抽中一道题时同时取出它的A、B两列得分。

[B2 同题配对](#b2) · [K01-12 配对重抽样](K01_statistics.md#k01-12) · [原条款 J6，第3575–3630行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K04-07](K04_probability.md#k04-07) · [修订依据](COMPONENT_REVISIONS.md#rev-j6)

<a id="j7"></a>
### J7 长上下文信息位置效应

在相同总长、内容与其他线索下移动关键信息至不同位置，比较题目层结果。长度限制、分块或截断会改变可见内容，记录窗口、保留规则和信息是否真的送达，再比较改变前后的表现。

[原条款 J7，第3631–3686行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K07-04](K07_state_execution.md#k07-04) · [修订依据](COMPONENT_REVISIONS.md#rev-j7) · [原编号 D2](#d2)

<a id="j8"></a>
### J8 解码采样与随机波动

记录温度、top-p、重复惩罚、输入格式及可用的随机种子。注明是否启用随机采样。估计同题解码波动时，每次取得新的随机抽取，例如在可控时使用预先给定的不同种子，保留各次输出。固定种子的重跑用于考察可复现性。将同题波动与题目差异分开；服务端不可见的参数标未报告。

[原条款 J8，第3687–3742行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [J19 同题重复与跨题比较](#j19) · [K04-02 读取 top-K 概率的限制](K04_probability.md#k04-02) · [修订依据](COMPONENT_REVISIONS.md#rev-j8)

<a id="j9"></a>
### J9 生成重复与文本退化

定义连续重复、词组循环或信息内容流失的可计数事件，以及随生成位置或传递轮次的变化。依据任务同时保留原始输出与过滤后结果，比较截长、分段或更换解码前后，沿用同一重复定义。若比较不同长度输出的重复倾向，使用等长窗口，或按可形成词组的位置数等重复机会计算比例，并报告文本长度。若关心读者总共看到多少重复，则保留总次数。

[原条款 J9，第3743–3797行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K03-10](K03_text_semantics.md#k03-10) · [修订依据](COMPONENT_REVISIONS.md#rev-j9) · [原编号 D2](#d2)

<a id="j10"></a>
### J10 分词效应

记录分词器版本、输入预算，以及候选接在实际提示之后的词元序列和预测位置；直接提交词元编号时按实际输入核对。比较语言或拼写变体时，区分字符数、token数、语义改变和截断；多token候选依序列概率或明确规则计分。

[原条款 J10，第3798–3852行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K04-01 候选词元与预测位置](K04_probability.md#k04-01) · [K04-03](K04_probability.md#k04-03) · [修订依据](COMPONENT_REVISIONS.md#rev-j10)

<a id="j11"></a>
### J11 测试集污染与数据泄漏

记录材料公开时间、可核验的模型训练信息和重叠检查范围。使用全新材料、变体或事件结果公开前的预测时，说明排除了哪条泄漏途径，保留训练语料不可见的限制。

[原条款 J11，第3853–3906行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K10-01](K10_release.md#k10-01) · [关联方法小节](TRACEABILITY.md#methods-j11) · [修订依据](COMPONENT_REVISIONS.md#rev-j11)

<a id="j12"></a>
### J12 基准饱和

检查各模型在题目层或分量表上是否集中于上限，并估计剩余可分辨差异。保留原始成绩，补看更难子集或连续分数，报告两种条件下排名与不确定性。

[原条款 J12，第3907–3960行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-11](K01_statistics.md#k01-11) · [修订依据](COMPONENT_REVISIONS.md#rev-j12)

<a id="j13"></a>
### J13 指令遵循

把每条指令写成可检查的行为条件，明确并列要求、冲突优先顺序、失败与拒答的编码。按事先定义的优先顺序确定每题适用的要求。分别以各要求适用的题为分母报通过率，再报每题所有适用要求均满足的比例，避免把内容正确等同于遵循格式。

[原条款 J13，第3961–4014行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K02-01](K02_annotation_reliability.md#k02-01) · [修订依据](COMPONENT_REVISIONS.md#rev-j13)

<a id="j14"></a>
### J14 结构化输出与格式约束

指定输出结构、解析规则、失败后能否修复以及是否重新生成。记录等价格式的归一规则。以计划中的原始试次为分母，报告首次输出格式合法的比例，以及首次输出格式合法且内容正确的比例；另在首次格式合法的输出中报告内容正确率。解析失败留在全体试次分母中。允许修复或重试时，用同一批原始试次另报最终可用率，保留每次尝试的结果。约束解码和事后解析作用于不同环节。

[原条款 J14，第4015–4068行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K07-01](K07_state_execution.md#k07-01) · [修订依据](COMPONENT_REVISIONS.md#rev-j14)

<a id="j15"></a>
### J15 安全边界下的拒答与稳健性

在合规的既有评测材料上先明确应答和应拒绝的判据，记录模型版本、已有提示条件和判分者。各条件采用难度可比的材料。对应该回答的题统计过度拒答，对应该拒绝的题分别统计适当拒答和不当回答。检查稳健性时，在意图与预期判定相同的既有评测变体间配对比较，同时关注正常任务能否完成。

[原条款 J15，第4069–4122行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-j15)

<a id="j16"></a>
### J16 模型作为被试的范式定位

先写下实际能观察的输入输出关系，再说明这个任务支持描述模型行为、与人类结果作类比或解释机制中的哪一层。沿用人类名称时指明相似维度，跨群体的等价解释需要独立测量依据。

[原条款 J16，第4123–4175行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K04-09](K04_probability.md#k04-09) · [修订依据](COMPONENT_REVISIONS.md#rev-j16)

<a id="j17"></a>
### J17 能力变化与指标阈值

当规模或训练进程变化伴随成绩跃升，同时检查连续表现和阈值化计分；报告模型间隔、区间和不同指标下的曲线。若只有极少离散观测，保留不可区分的解释。

[原条款 J17，第4176–4228行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-j17)

<a id="j18"></a>
### J18 代理指标的过度优化

在有显式优化或按分数选择候选的条件下，记录优化对象、预算及代理分数；用独立于该指标的质量证据追踪优化前后或不同强度下的变化。

[原条款 J18，第4229–4281行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-j18)

<a id="j19"></a>
### J19 评估可复现性与版本依赖

保存模型及分词器标识、接口日期、提示、解码设置、题目版本和可用的种子或检查点，记录服务端版本变动。同一输入多次采样时，分别报告题目数与每题运行次数。两个模型或设置做同一批题时按题号对齐。对题目等权的平均分，可先在每题内汇总重复得分，再平均逐题差。对跨题计算的指标，如 ROC AUC，在同一批含正、负例的题上分别计算两个模型的指标后取差。估计换题带来的波动时按设计配对重抽，每次带上同一道题两边的重复记录，重算相应指标与差值。计算 AUC 的重抽样本需同时含正、负例，抽样方式应与研究设计一致；若还关心重新采样的波动，按实际采样设计另行估计。

[原条款 J19，第4282–4336行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K01-12](K01_statistics.md#k01-12) · [修订依据](COMPONENT_REVISIONS.md#rev-j19)

<a id="j20"></a>
### J20 多轮对话中的一致性变化

固定任务目标和各轮查看历史的规则，逐轮核对模型实际收到哪些消息、哪些被截断或移除，按轮计分同一约束或偏好能否维持。设置可见历史长度或重置对照，检查变化能否由裁剪解释。

[原条款 J20，第4337–4388行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [K07-05](K07_state_execution.md#k07-05) · [关联方法小节](TRACEABILITY.md#methods-j20) · [修订依据](COMPONENT_REVISIONS.md#rev-j20) · [原编号 D2](#d2)

<a id="historical-ids"></a>
## 历史编号与去向

<a id="b10"></a>
**B10 被试内设计的适用条件**

已并入 [B2 同一实验单位的配对与重复测量](#b2)。在同一状态连续实施两个处理前，检查状态能否重置、配对是否有效。有意研究历史更新时保留前序信息；需要排除残留或检验两个先后顺序的差异时，按 [D3 延滞与迁移效应](#d3)设置比较。

[原条款 B10，第1321–1384行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-b10)

<a id="c7"></a>
**C7 平衡的层级**

已并入 [C2 平衡](#c2)。针对所关心的位置、线性时序趋势或相邻条件，选择全排列、拉丁方或ABBA，并核对实际覆盖情况。拉丁方的位置分配及相邻有序对检查见 [B8 拉丁方](#b8)。

[原条款 C7，第1748–1837行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-c7)

<a id="d4"></a>
**D4 不对称迁移**

已并入 [D3 延滞与迁移效应](#d3)。分别将A后测B、B后测A与各自无前序运行比较，以看出哪一个前序改变了后续。检查重置后仍保留的外部状态。

[原条款 D4，第2018–2077行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-d4)

<a id="d2"></a>
**D2 疲劳效应**

原编号移出独立组件目录。长上下文中的信息位置、截断与分块见 [J7](#j7)；单次长输出的重复、内容退化见 [J9](#j9)，跨轮指令或风格维持见 [J20](#j20)。独立会话与外部状态重置见 [D3](#d3)，分散条件在序列中的位置见 [C2](#c2)，将序位纳入分析见 [C5](#c5)，事先约定剔除后段试次并报告影响见 [G5](#g5)。真人作业时长、休息与疲劳指标留在原手册第1898–1957行。

[原条款 D2，第1898–1957行](../../../analysis/literature_component_coverage/baselines/实验组件_v1.4.md) · [修订依据](COMPONENT_REVISIONS.md#rev-d2)
