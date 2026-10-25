# article_150 | Consistency Checks for Language Model Forecasters | 2025

研究类型概述：该文是面向 LLM forecasters 的方法学/基准评测研究：提出基于套利与频率学假设检验的逻辑一致性度量，自动生成逻辑相关问题元组，评估多个 LLM 预测器在 10 类一致性检查上的表现，并检验一致性指标与 Brier score 的相关性；另用 ArbitrageForecaster 做小规模代理指标优化实验。分析单位主要是 forecaster × consistency-check × question tuple，而非人类被试。
- **研究构念（Construct）**：概率判断的逻辑一致性、规范理性与可套利性｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：从真实预测问题自动构造否定、释义、蕴含、条件概率和证据等一致性检查，要求多个LLM forecaster分别给概率，再计算约束违反并测试无训练的ArbitrageForecaster修正。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.6: “We test a range of forecasters based on various LLM models … with and without chain-of-thought prompting”；p.16 Table 3 lists 10 consistency checks；p.9: ArbitrageForecaster depth r and s vary from 0 to 4。 | 可识别的设计水平包括模型/提示设置、10 类一致性检查和 ArbitrageForecaster 深度，达到“明确命名并至少两个水平”的基本要件；但未报告随机分配、操纵程序或操纵检验，故为 0.5。 |
| A2 | 因变量 | 0.5 | PDF p.3-4: arbitrage metric V(F(...)) and frequentist metric definitions；p.6: “average Brier score” as ground truth metric；p.7 Table 1 reports correlations。 | 因变量指标与计分方式明确（arbitrage violation、frequentist violation、Brier score、阈值/Frac），但未报告这些自建指标的信度、连续指标预处理或天花板/地板控制，故为 0.5。 |
| A3 | 控制变量 | 0.5 | PDF p.33 Figure 11 fixed JSON question format；p.40: “For each LLM call, we use gpt-4o with a structured output Pydantic format”；p.5 gives fixed resolution-date windows。 | 报告了部分固定控制（问题呈现格式、生成/验证用 gpt-4o、解析库、日期窗口），但未系统列出控制变量清单及逐一控制手段，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | PDF p.6: “the Brier score … depends both on model capabilities and the training data cutoff”；p.7: “Part of the correlation can be attributed to better models being both more consistent and better forecasters”；also excludes forecasters with Brier worse than 0.25。 | 识别了模型能力/训练截止与更好模型同时更一致、更准确等潜在混淆，并做有限排除和 MMLU 对照，但未充分控制或做正式敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 全文未提出调节变量或调节假设，也没有相应交互检验；该研究模型不包含调节变量。 |
| A6 | 中介变量 | NA | — | 全文未提出中介变量或中介假设，也没有直接/间接效应分解；该研究模型不包含中介变量。 |
| A7 | 操作性定义 | 1 | PDF p.3-4 gives formal definitions of consistency checks and both violation metrics；p.4 pipeline overview；p.33-34 forecaster prompts；p.40-43 pipeline prompts；p.5-6 tuple instantiation/verification procedures。 | 关键构念（预测概率、逻辑一致性规则、arbitrage/frequentist violation、Brier score）均有可观测、可复现的操作化程序与提示/计分细节，达到 1。 |
| A8 | 水平数与类型 | 0.5 | PDF p.6 lists model families and Basic vs CoT；p.16 Table 3 lists 10 named checks with tuple forms；p.33 Figure F lists exact model versions；p.9 gives r/s ranges 0 to 4。 | 报告了水平数与多数具体取值/标签，但未系统说明水平类型（名义/等级/连续）、间距与全距，也未对连续深度变量做中心化说明，故为 0.5。 |
| A9 | 单一操作化的风险 | 1 | PDF p.7 Table 1 reports correlations across 10 checks and two metrics with Brier score；p.3-4 defines both arbitrage and frequentist metrics；p.6-7 reports aggregate and check-specific relations。 | 关键构念“一致性”采用多种逻辑检查与两种度量，并报告它们与外部效标 Brier score 的会聚/分化证据；符合多操作化并报告会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是人类自陈量表或多构念同源自评设计；自变量为模型/提示/检查设置，因变量为从其概率输出计算的一致性指标，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或 LLM 被试被随机分配到互斥实验条件；这是跨模型/跨设置的基准评测，不是被试间实验分配设计。 |
| B2 | 被试内设计 | NA | — | 虽然同一 forecaster 在多个问题和检查上被评估，但每个问题独立 elicitation，不存在被试内条件顺序平衡设计；该组件不适用于此基准评测。 |
| B3 | 混合设计 | NA | — | 研究没有组间/组内因素混合设计，也没有对应混合模型与两类误差项。 |
| B4 | 因子设计 | NA | — | 研究不是带完整设计矩阵和 ANOVA 交互检验的因子实验；模型 × 检查 × 数据集比较是观察性基准描述，而非实验因子设计。 |
| B5 | 主效应 | NA | — | 无因子实验意义上的主效应检验，故不适用。 |
| B6 | 交互作用 | NA | — | 无实验交互项检验或简单主效应分析，故不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无被试内处理顺序的拉丁方设计。 |
| B9 | 准实验设计 | NA | — | 非准实验设计；研究不做因果处理效应推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理可逆性/迁移对称性设计问题。 |
| C1 | 随机化 | NA | — | 没有对分析单位随机分配到实验条件；基准评测无随机化分配问题。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | PDF p.33 Figure 11 fixes question JSON fields；p.40: “For each LLM call, we use gpt-4o with a structured output Pydantic format enforced by the Instructor library”；p.5 fixes date windows。 | 列出并固定了若干处理变量（呈现格式、生成/验证模型和库、日期范围），但未系统讨论这些恒定设置对外部效度的限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对程序。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型；模型能力混淆仅作排除/描述性对照，不构成 ANCOVA 式协变量设计。 |
| C6 | 盲法 | NA | — | 数据采集与评分由自动脚本/指标完成，无人类被试或人类评分者盲法问题。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | 每个问题作为独立 LLM 调用进行概率 elicitation，不存在跨试次上下文内学习或练习块。 |
| D2 | 疲劳效应 | NA | — | LLM 评测为自动化批量调用，无人类 session 疲劳问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各问题/条件相互独立、无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为概率预测与计算出的 violation/Brier 指标，不涉及主观量表锚定或范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 主要任务是逐个问题独立 elicitation，不是多候选项选择或多刺激顺序呈现；不存在需随机化的选项/刺激位置。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 研究对象为 LLM，不涉及人类被试需求特征或事后访谈推断研究假设。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | NA | — | 主要因变量为连续型概率/一致性指标和 Brier score，不是典型有上下界量表或端点截断型任务；未把天花板/地板作为核心效度问题。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，共同方法偏差组件不适用。 |
| F1 | 统计结论效度 | 0.5 | PDF p.6-7 reports correlation coefficients such as “Correlation: 0.85”, “0.92”, Table 1 correlations；p.6 specifies 5000 tuples but no power analysis or confidence intervals。 | 报告了相关系数作为效应量，但未给置信区间、样本量/功效依据，也未说明对 10 项检查与多指标比较的多重性校正；达到基本要件但完整性不足，故 0.5。 |
| F2 | 内部效度 | NA | — | 研究为观察性基准评测与相关性分析，不作随机实验因果推断，无随机分配、分配隐藏和被试流向问题。 |
| F3 | 构念效度 | 0.5 | PDF p.3-4 derives arbitrage and frequentist metrics；p.7 Table 1 reports criterion correlations with Brier score；p.16 Table 3 gives multiple consistency checks。 | 有理论定义、多检查操作化及与 Brier score 的效标关联，但未报告传统信度、操纵检验或评分者信度，故为 0.5。 |
| F4 | 外部效度 | 0.5 | PDF p.5 data sources: Metaculus/Manifold, NewsAPI, synthetic；p.7: “the selection of forecasters we test is quite limited”；p.8 long-horizon benchmark；p.58 discusses caveats。 | 报告了数据集来源、时间范围与模型选择局限，并做了两个数据集上的重复相关分析，但未系统界定代表性、抽样框或完整推广边界，故为 0.5。 |
| G1 | 分析单位 | 0.5 | PDF p.6 Figure 1: “Each point represents a forecaster”；p.7 Table 1 reports forecaster-level correlations；p.6 each forecaster run on 5000 tuples。 | 统计分析主要在 forecaster 层聚合（每个模型一个点），但每个分数由大量 question tuples 嵌套产生，未用多层模型分离 tuple/question 方差；达到说明分析层级的基本要件但处理不足，故 0.5。 |
| G2 | 随机效应 | NA | — | 模型设置被作为固定比较对象而非从更大模型总体抽样，论文也未声称用随机效应推广到模型总体；无混合模型需求。 |
| G3 | 材料作为随机效应 | NA | — | 具体问题材料不是作为自变量载体的有限刺激样本，而是基准数据集；研究目标不是推广到任意问题总体，故材料随机效应组件不适用。 |
| G4 | 统计功效 | 0 | PDF p.6 gives 5000 tuples and o1-preview 50 tuples due to cost；p.6-7 reports correlations without prior power analysis or confidence intervals。 | 无设计阶段功效分析或样本量论证，也未报告相关系数的置信区间；仅按成本设定部分样本量，故为 0。 |
| G5 | 研究者自由度 | 0.5 | PDF p.6 excludes forecasters with Brier score worse than 0.25；o1-preview only 50 tuples per check due to cost；p.5 uses a subset of 1000 NewsAPI questions；all 10 checks reported。 | 报告了主要排除规则、条件与部分样本量决定，但未报告剔除数量/被试流向式细节，也未明确区分验证性与探索性分析，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | PDF p.59 Reproducibility Statement concerns data/code release, but no preregistration platform/ID or pre-specified analysis plan is reported。 | 全文无时间戳早于数据收集的公开预注册，也未区分预注册验证性分析与事后探索性分析，故为 0。 |
| J1 | 位置偏差 | NA | — | 研究不涉及多候选项选择、排序或 LLM-as-judge 成对比较；候选位置偏差不适用。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判对开放式生成质量打分，长度偏差不构成本研究的核心评估风险。 |
| J3 | 谄媚 | NA | — | 任务为闭卷概率 elicitation，无用户先验立场、反馈或纠错对话，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 主要因变量由模型自身概率输出计算，不使用 LLM-as-judge 对被评模型输出做质量评分；自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF p.5: “we sample six examples of forecasting questions, as style examples, as well as a set of tags”；p.40 prompt contains {example 1}–{example 6}；p.40 notes initial quality-filtered questions seed the examples。 | 问题生成阶段确实使用 few-shot 示例，报告了数量与示例来源的大致说明，但未报告标签比例、排列反平衡、多 seed 重采样或模板全文；主预测器评估本身为 zero-shot，故按生成步骤记 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.33-34 Figures 12–13 provide full Basic/CoT forecaster prompts；p.40-43 Figures 14–17 provide pipeline prompts；但未报告 prompt 版本号、敏感性消融或 dev/test 划分。 | 公布了完整 prompt 模板，达到基本要件；但缺少版本化、语义等价措辞敏感性消融及 dev/test 分离说明，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验上下文为单个预测问题短文本，无长文档/RAG 或关键信息首中尾位置操纵。 |
| J8 | 温度与采样随机性 | 0 | PDF p.33-34 only describes API/Instructor calls and prompts；p.33 lists model versions such as gpt-4o-2024-05-13, but no temperature, top-p, seed or repeated-sampling CI are reported。 | 未报告 temperature/top-p/top-k/seed，也未报告每条件重复采样次数与置信区间；LLM 非确定性未纳入统计设计，故为 0。 |
| J9 | 重复与文本退化 | NA | — | 主要输出为解析后的概率值，CoT 推理文本不是被评估的质量指标；文本退化/重复率不构成本研究比较的核心风险。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言、单脚本，无跨语言/跨格式输入比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | PDF p.2: “Both datasets include only events that happen past the training data cutoff of all forecasters we test”；p.33 lists model version dates；但未做 n-gram/DCQ 污染检测或报告污染率。 | 报告了测试事件时间与模型版本/训练截止的大体对照，但未系统逐模型核对 cutoff，也未做污染检测；达到基本要件但不完整，故为 0.5。 |
| J12 | 基准饱和 | NA | — | 所用为新建一致性基准，分数远未接近天花板（如 o1-mini 的 violation 很高），不涉及饱和基准上的微小提升宣称。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，无约束指令遵循准确率测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p.33: “Instructor library … output conform to a specific Pydantic model that has a prob field forced to be a float between 0 and 1”；p.34 CoT uses gpt-4o-mini to parse output；未报告格式合法率或重试策略。 | 报告了结构化输出设置（Pydantic/Instructor、概率字段范围、两步解析），但未报告格式合法率、重试策略或将格式失败与内容错误分开统计，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估或有害请求集。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文将 LLM 作为 forecasters 做工程/应用评估，不主张测量人类心理学或认知科学构念，也未做人类被试范式对照；该组件不适用。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究不报告随模型规模/训练进展的涌现能力曲线，不涉及涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | PDF p.9: ArbitrageForecaster “improves consistency on checks that we optimize against, but this improvement does not generalize to other held-out consistency checks, nor does it improve the actual forecasting performance”；p.38-39 Tables 4–7 report optimized checks, held-out checks and Brier scores。 | 明确区分优化对象（特定 consistency check）与评估对象（held-out checks、Brier score），并展示代理改善不泛化；但未使用独立 held-out 人类评估或画代理-真实双曲线，故为 0.5。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.33 lists exact model versions for several forecasters (e.g., gpt-4o-2024-05-13, gpt-4o-mini-2024-07-18)；p.6 reports 5000 tuples and o1-preview 50 tuples；但无重复采样 N、95% CI 或配对检验。 | 报告了部分精确 snapshot/版本和评估样本量，但未报告重复采样次数、bootstrap CI 或模型间配对检验；达到基本要件但不完整，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮问题概率 elicitation，无多轮对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
论文在一致性度量、数据管线、提示模板与模型版本方面报告较充分，但作为观察性 LLM 基准与相关性比较，缺少人类实验意义上的随机分配、顺序平衡、预注册与功效分析；统计上以 forecaster 层聚合相关为主，未给置信区间或嵌套结构建模。多数人类被试设计组件不适用。LLM 评估相关风险中，采样参数与可复现性报告不足，但对代理指标优化不泛化的报告较好。
