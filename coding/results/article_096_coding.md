# article_096 | Context versus Prior Knowledge in Language Models | 2024

研究类型概述：这是一项 NLP/LLM 行为与测量方法研究：提出并验证两个基于互信息的指标（persuasion score 与 susceptibility score），在 122 个 YAGO 关系、真实/虚假实体、不同语境模板、开放/封闭问题以及 6 个 Pythia 模型规模上计算模型下一 token 分布变化，并用置换检验、BH 校正、相关分析与案例研究评估指标及模型行为。研究没有人类被试，分析单位是模型×查询/实体/语境及其派生分数。
- **研究构念（Construct）**：先验知识—语境证据整合、熟悉度与可说服性｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；态度（attitude, `trm_4a3fd79d09947`）
- **实验任务与范式（Task / Paradigm）**：这是一项 NLP/LLM 行为与测量方法研究：提出并验证两个基于互信息的指标（persuasion score 与 susceptibility score），在 122 个 YAGO 关系、真实/虚假实体、不同语境模板、开放/封闭问题以及 6 个 Pythia 模型规模上计算模型下一 token 分布变化，并用置换检验、BH 校正、相关分析与案例研究评估指标及模型行为。研究没有人类被试，分析单位是模型×查询/实体/语境及其派生分数。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4 §4.1: “600 contexts are evenly distributed between assertive, base, and negation context types”; p6 §4.3: relevance, assertiveness, negation comparisons; p4: six Pythia model sizes 70m–12b. | 明确命名的操纵/构造因素包括语境类型、相关性、断言性与模型规模，并给出水平；但未报告操纵检验，且条件分配/随机化与部分模板构造细节不完整。 |
| A2 | 因变量 | 0.5 | p4: Eq. (2) persuasion score 与 Eq. (3) susceptibility score；p4 “approximate the model’s answer distribution with the next-token distribution”；p5 Fig. 4 报告跨 seed 与 query form 的方差；p5 报告 convergent validity。 | 因变量指标与计分公式、单位（nats）明确，并报告了信度/效度证据；但没有说明连续指标的预处理、剔除标准或天花板/地板风险。 |
| A3 | 控制变量 | 0.5 | p4: 122 relations, 100 entities per relation, 600 contexts, each entity mentioned in 6 contexts; p15 App. C 给出固定模板与采样约束；p4 使用固定 Pythia 模型族。 | 报告了若干保持恒定的刺激/模型设置与平衡约束，但没有以控制变量清单形式系统列出并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p7: “potential spurious correlations/token biases associating … the word not with the model outputting No”; p16: closed queries 可能因原始答案均为 Yes 而产生 artifact；p10 Limitations: next-token approximation “could be a noisy signal”; sampled contexts “may not be representative”。 | 识别了 token bias、closed-query artifact、下一 token 近似与语境抽样等潜在混淆，并讨论残余威胁；但未系统说明这些混淆的控制方式或做正式敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有设定正式的调节变量模型；模型大小只作为分组描述和跨模型重复展示，没有以交互项检验的调节分析，因此该组件不适用。 |
| A6 | 中介变量 | NA | — | 论文不包含中介变量、直接/间接效应分解或中介路径假设，故不适用。 |
| A7 | 操作性定义 | 1 | p3–4: 给出 persuasion/susceptibility 的联合分布、Eq. (2)(3) 与下一 token 近似；p4 §4.1 与 p15 App. C 详细说明实体采样、语境构造、查询模板与分值计算。 | 关键构念和测量均可按公式与构造步骤复现，操作化程序明确。 |
| A8 | 水平数与类型 | 0.5 | p4: three context types (assertive, base, negation), open/closed query forms, six Pythia sizes from 70m to 12b; p6 §4.3 给出 relevance/assertiveness/negation 水平。 | 报告了水平数与各水平标签，但未统一说明水平类型（名义/等级/连续）、间距/全距，也未说明连续变量入模是否中心化。 |
| A9 | 单一操作化的风险 | 1 | p5: persuasion score 与模型实际答案一致性做 convergent validity；p5 Fig. 3: susceptibility 与 per-entity memorization ratio 对照；p8: familiarity 同时用 Pile co-occurrence frequency 与 YAGO degree 检查。 | 关键构念使用多种操作化/验证指标，并报告了会聚证据与跨模型、跨 seed 的稳健性。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是人类自评/问卷式多构念测量，IV 与 DV 均来自模型概率与构造刺激，不涉及传统同源共同方法偏差检验，因此不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组分配；同一模型/查询/语境在不同条件间被重复计算，不存在被试间设计。 |
| B2 | 被试内设计 | NA | — | 虽有同一模型在不同语境/问题形式下的重复计算，但没有人类被试内重复测量设计、顺序平衡和被试随机效应，故不按人类被试内设计编码。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内因素的人类混合设计，故不适用。 |
| B4 | 因子设计 | NA | — | 研究不是全交叉因子实验；语境质量、模型规模、问题形式等分别比较或描述，无完整设计矩阵与交互项分析，故不适用。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应 ANOVA，故不适用。 |
| B6 | 交互作用 | NA | — | 没有全因子设计中的交互项检验，故不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机分配设计，故不适用。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计，故不适用。 |
| B9 | 准实验设计 | NA | — | 没有准实验分组或非随机人类分配，故不适用。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理顺序，不存在处理可逆性/迁移对称性问题，故不适用。 |
| C1 | 随机化 | NA | — | 没有把独立分析单位随机分配到互斥实验条件的程序；语境是构造并抽样用于模型打分，不涉及人类或独立实验单位随机化。 |
| C2 | 平衡 | NA | — | 不存在被试间条件顺序需要平衡，故不适用。 |
| C3 | 恒定 | 0.5 | p4: 使用 Pythia 70m–12b，均基于 deduplicated Pile；p15 App. C: GPT-4 版本 “gpt-4-1106-preview, January 2024”；p10 讨论 sampled contexts 的外部推广限制。 | 报告了模型版本/训练语料与数据生成模型等恒定设置，但没有集中列出所有恒定变量及具体水平，外部效度限制讨论也较有限。 |
| C4 | 匹配 | NA | — | 未使用匹配/配对分配程序，故不适用。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入 ANCOVA/回归模型进行控制；频率/度数被作为分析变量而非协变量控制，故不适用。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人工评分者，故盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 不存在条件顺序平衡层级，故不适用。 |
| D1 | 练习效应 | NA | — | 每个语境/查询是独立模型打分，无人类练习块或试次位置协变量，故不适用。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长、休息或疲劳控制问题，故不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各模型调用与语境打分不形成跨条件残留或清洗期问题，故不适用。 |
| D4 | 不对称迁移 | NA | — | 没有说话人/被试跨条件迁移，故不适用。 |
| D5 | 范围效应 | NA | — | 不涉及人类绝对判断或量表范围效应，故不适用。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选项、排序或刺激序列呈现给人类被试；每个 prompt 是单一语境加查询，故不适用。 |
| E2 | 默认赞同 | NA | — | 未使用 Likert/态度自评量表，故默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 未使用等级量表或跨群体反应风格比较，故不适用。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征或事后推断研究假设的问题，故不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者，故实验者效应不适用。 |
| E6 | 天花板 / 地板效应 | NA | — | 因变量为互信息量/模型概率派生分数，不是典型有端点堆积的正确率或量表；论文展示了分布但无 pilot 难度校准问题，故按本编码不适用。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，故共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p6: “permutation test … α = 0.05 with the BH correction”; p17 Fig. 12 等报告 effect size 与 p-values；p8/p19 报告 Spearman ρ；但未见 95% CI 或事前功效分析。 | 报告了效应量、多重比较校正与主要检验结果；但缺少样本量确定依据、置信区间和统计假设检验细节。 |
| F2 | 内部效度 | 0.5 | p4: 通过固定模板、每实体 6 个语境、三类语境均分来控制构造；p7 脚注 10: 过滤训练数据中出现的 fake entities；p10 Limitations 讨论 sampled contexts 与近似误差。 | 有构造层面的控制与内部效度讨论，但不是随机分配设计，也未报告基线等价性、流向图或损耗处理；因此只有部分满足。 |
| F3 | 构念效度 | 1 | p5: “Convergent Validity” 用答案一致性与 persuasion score 对照；p5 Fig. 3 用 memorization ratio 验证 susceptibility；p5–6 与 Fig. 4 报告跨 seed/query form 的 construct reliability。 | 对关键测量报告了信度（跨 seed 与 query form 方差）和效度（与已有指标/实际答案一致性）证据，构念对应关系论证充分。 |
| F4 | 外部效度 | 1 | p4: 122 个 YAGO relations、每关系 100 entities、600 contexts；p8–9 报告 6 个模型规模的跨模型结果；p10 Limitations 明确讨论 sampled contexts、next-token approximation 等推广边界。 | 报告了材料来源、模型族与规模范围，并在局限中明确推广边界；虽有外部效度限制，但报告较完整。 |
| G1 | 分析单位 | 0.5 | p4: contexts sampled with each entity mentioned in 6 contexts；p5: “For each of the 122 queries” 计算均值并做检验；p15 App. C: permutation test per comparison。 | 说明了按 query/entity/context 汇总与检验，但没有显式处理 contexts 嵌套于 entities/queries 的多层结构，主要用聚合或逐 query 检验。 |
| G2 | 随机效应 | 0.5 | p4: “We take a sample size of 600 contexts”; p5: “across three random seeds”；p6 Fig. 4 报告 variance；但无混合模型或随机效应结构。 | 承认语境抽样与 seed 变异并报告方差，但未说明哪些因子为随机效应，也未用随机截距/随机斜率建模；因此只部分满足。 |
| G3 | 材料作为随机效应 | 0.5 | p4: 600 random contexts，每实体 6 contexts；p5 Fig. 4 报告跨 seed/query form 方差；p15 App. C 说明语境采样。 | 材料/语境被视为抽样而非穷尽，并报告了跨 seed 稳定性；但统计模型未把 item/context 作为随机效应，不能充分推广到材料总体。 |
| G4 | 统计功效 | 0.5 | p4: “Due to computational constraints …” 与 600 contexts；p17 Fig. 12、p18 Fig. 13/14 报告 effect sizes；但无事前 power analysis 或 CI。 | 结果中报告了效应量，但样本量主要由计算约束而非功效分析决定，且缺置信区间，故为部分满足。 |
| G5 | 研究者自由度 | 0.5 | p7 脚注 10 说明过滤训练数据中出现的 fake entities；p4/p15 说明构造流程；p9 Applications 标记为案例探索；但未见完整排除表、全部条件/模型的分析清单或停止规则。 | 报告了部分排除规则与主要分析，但没有完整列出所有试次排除、样本量决定方式和探索性/验证性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p1–10 全文未见预注册平台、注册编号或“pre-registered”声明。 | 没有公开预注册；按本编码口径，正文完整且适用时缺失预注册记 0。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM-as-judge、多项选择排序或候选位置比较；模型输出通过下一 token 概率计算，故位置偏差不适用。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放生成质量，也不比较回答长度与质量，故冗长偏差不适用。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错对话操纵；语境说服力不是用户谄媚，故不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 对被评模型输出做成对比较或评分；GPT-4 仅用于数据生成，故自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验不是 few-shot in-context learning 示例选择研究，故不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p4/p15 给出 open/closed query 与 base/assertive/negation context 模板；p5 通过 query form 方差检查措辞稳健性；GitHub 链接提供代码。 | 有模板示例与 query-form 稳健性检查，但未系统版本化全部 prompt、未做语义等价措辞的完整敏感性消融，也未说明 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 语境很短，不涉及长上下文、RAG 或关键信息位置操纵，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | p4: “sample size of 600 contexts”；p5 Fig. 4 与 p4 “across three random seeds”；p15: GPT-4 版本 “gpt-4-1106-preview”。 | 报告了随机 seed 与方差、部分模型版本；但未报告 temperature/top-p 等采样超参，模型评估主要用 next-token 概率而非生成采样，信息不完整。 |
| J9 | 重复与文本退化 | NA | — | 不涉及开放文本生成与重复/退化评估；模型输出为下一 token 分布，故不适用。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文材料，无跨语言/跨脚本比较，故分词效应不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p7 脚注 10: “We filter out fake entities that appear in the training data”；p15 App. C: fake entities generated with GPT-4；p8/p19 使用 Pile frequency 分析 familiarity。 | 对 fake entity 的训练数据重叠做了过滤，并使用 Pile 频率；但没有系统报告测试集版本、污染检测指标或污染率。 |
| J12 | 基准饱和 | NA | — | 不是基准准确率评估，也没有接近天花板的基准分数问题，故不适用。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循，无约束指令遵循测量，故不适用。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/文法约束输出，故不适用。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全、对齐或越狱评估，故不适用。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文将 persuasion/susceptibility 明确形式化为互信息量，研究目标是 LLM 测量指标与模型行为，不主张测量人类心理构念，也没有把模型作为人类心理学被试外推；故不按心理学被试定位编码。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文跨模型规模展示趋势，但未宣称“涌现/突变”，也没有用连续指标与多 seed 曲线检验涌现争议，故不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对 benchmark/奖励模型/LLM-judge 的优化训练或 best-of-N 代理优化，故不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p4: “three random seeds”；p5 Fig. 4 报告 variance across seeds 与 query forms；p4/p15 报告 Pythia 模型与 GPT-4 snapshot；但未报告 95% CI 或配对模型比较。 | 有重复 seed、方差与较清楚的模型版本，但缺少置信区间、精确 snapshot 标识（如 commit hash）及配对检验细节。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮 prompt 打分，无多轮对话历史累积，故不适用。 |

## 编码小结
指标定义清楚、构念操作化与效度/信度验证较强，统计上报告了效应量与多重比较校正；但缺少预注册、事前功效分析、置信区间，且未用多层/混合模型显式处理实体、语境与查询的抽样嵌套。大量人类实验设计组件因无人类被试分配、无量表自评、无多轮对话等而不适用；适用性判断应优先按 LLM 计算实验与分析单位处理。
