# article_024 | Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models | 2024

研究类型概述：这是一项面向大语言模型的基准式、观察性评测研究，不是人类被试实验。研究以事实性/反事实性提示、模型家族/版本和若干数学推理问题为比较结构，使用因果概率 PN/PS、FIR/CIR 与 γ-overlap 等指标评估模型推理与反事实一致性。分析单位主要是问题实例/提示调用及模型-任务组合；没有随机分配、人类被试、盲法或正式因子方差分析。
- **研究构念（Construct）**：概率因果推理与反事实一致性（probabilistic causal reasoning and counterfactual consistency）｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：这是一项面向大语言模型的基准式、观察性评测研究，不是人类被试实验。研究以事实性/反事实性提示、模型家族/版本和若干数学推理问题为比较结构，使用因果概率 PN/PS、FIR/CIR 与 γ-overlap 等指标评估模型推理与反事实一致性。分析单位主要是问题实例/提示调用及模型-任务组合；没有随机分配、人类被试、盲法或正式因子方差分析。｜CA 任务锚定：演绎推理任务（deductive reasoning task, `trm_4c898b8c2d071`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'three math problems... GPT-2, GPT-3.5-turbo and GPT-4'; pp.19-20 Appendix E gives direct/counterfactual prompts. | 自变量可识别为提示类型（direct/counterfactual）、模型版本与问题类型，且水平有命名；但未报告操纵检验、完整分配逻辑或随机化/平衡程序。 |
| A2 | 因变量 | 0.5 | p.7: 'Factual Inconsistency Rate (FIR)... Counterfactual Inconsistency Rate (CIR)'; p.21 Appendix H gives equations; p.7 '500 bootstrap samples'. | 因变量指标与计分方式有界定，并报告了 bootstrap 不确定性；但没有信度/效度证据，也未说明连续指标预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | p.7: 'we have chosen to limit our analysis to the GPT series'; p.23 Appendix J: 'same setup... Llama... Phi'; p.19-20 fixed prompt templates. | 报告了部分固定设置（固定模型集、固定提示模板、固定数域），但未系统列出控制变量清单及全部控制手段，且缺少温度等关键调用设置。 |
| A4 | 混淆变量 | 0.5 | p.10 Limitations: 'Prompt-dependent results'; p.7 discusses model families and tasks. | 识别了提示依赖、模型/任务差异等潜在混淆或限制，但没有说明具体控制方式，也未报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量假设、乘积项交互检验或简单斜率分析；模型/任务比较是描述性基准比较，不作为正式调节模型。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解，不涉及中介模型。 |
| A7 | 操作性定义 | 0.5 | pp.19-21 Appendix E prompt templates; p.21 Appendix H metric equations; p.21 Appendix F GPT-4 concretization prompt. | 关键构念有可重复的操作化线索（提示模板、指标公式、答案抽取 prompt），但完整解析流程、调用参数与实现细节不足，尚不能完全复现。 |
| A8 | 水平数与类型 | 0.5 | p.6-7: Div6 uses N∈[1,400], EvenSum/CandyParty/ConPref use ranges 1-8; models GPT-2/GPT-3.5-turbo/GPT-4. | 报告了模型、问题与数域的多个水平/取值，但未系统说明水平类型（名义/连续）、间距与全距，也未说明连续变量中心化等处理。 |
| A9 | 单一操作化的风险 | 0.5 | p.7 four problems; p.8-9 FIR/CIR and γ-PN/γ-PS overlap; p.10 limitations discuss reasoning-graph and prompt dependence. | 使用了多个问题与多个指标来操作化推理，但没有报告各操作化之间的正式会聚证据；局限讨论存在但未形成系统的多操作化效度论证。 |
| A10 | 单一方法的风险 | NA | — | 研究不使用人类自陈量表或问卷式同源测量；虽然提示与回答都经由 LLM，但共同方法偏差检验不属于该基准设计的适用组件。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组分配；模型是固定评测对象，而非被随机分配到条件的被试组。 |
| B2 | 被试内设计 | NA | — | 各提示调用基本独立，未构成需要平衡顺序的被试内重复测量设计；也没有条件顺序处理。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素混合设计，也没有混合模型或重复测量 ANOVA 分析。 |
| B4 | 因子设计 | NA | — | 没有正式的因子设计、完整设计矩阵和交互项统计检验；模型×问题×提示类型只是基准比较结构。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验（F、df、p、效应量）。 |
| B6 | 交互作用 | NA | — | 没有正式交互项检验、简单主效应或交互图误差棒分析。 |
| B7 | 区组设计 | NA | — | 没有区组/分层设计或区组变量。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；模型版本比较是固定基准比较，未涉及非随机分配及相应因果推断框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内条件顺序设计，因此不涉及处理可逆性或迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有把研究单位随机分配到互斥条件；数域是穷举式评测，模型和提示条件固定，不存在需要随机化的分配问题。 |
| C2 | 平衡 | NA | — | 没有条件顺序平衡问题；提示调用相互独立。 |
| C3 | 恒定 | 0.5 | p.19-20 fixed prompt templates; p.7 fixed model set; p.23 Appendix J 'same setup'. | 固定了提示模板、模型集和数域等部分恒定变量，但未系统列出恒定变量水平，且缺少温度、API 版本等关键恒定信息。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配变量。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 没有人类被试、主试或人类评分者需要盲法；评测由自动化 API 和 LLM 抽取构成。 |
| C7 | 平衡的层级 | NA | — | 没有顺序效应需要选择完全平衡、拉丁方或 ABBA 层级。 |
| D1 | 练习效应 | NA | — | LLM 调用彼此独立，每次提示无上下文内学习或练习块，不存在练习效应控制。 |
| D2 | 疲劳效应 | NA | — | 任务为短提示和短回答，没有 session 时长、休息间隔或疲劳效应问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件清洗期需求；每次提示独立，未涉及残留迁移。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件迁移或不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量是模型二元回答与概率指标，不是被试内绝对判断或量表评分，不涉及范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选/序列刺激的选项顺序问题；提示不呈现候选答案顺序。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert 或态度自评量表，无默认赞同/反向题问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 没有人类被试，因而不涉及掩饰情节、事后访谈或需求特征。 |
| E5 | 实验者效应 | NA | — | 数据采集由 API 自动化完成，没有人类主试/评分者的实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.8 Figure 6 shows PN/PS densities; p.9 Figure 7: 'standard deviations included brackets'. | 报告了估计分布和标准差，可部分排查端点问题；但未报告偏度、端点频率、 pilot 难度校准或明确的天花板/地板讨论。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，不涉及共同方法偏差统计检验。 |
| F1 | 统计结论效度 | 0.5 | p.7 '500 bootstrap samples'; p.9 'standard deviations included brackets'; p.8 densities. | 报告了 bootstrap 分布和部分不确定性，但未报告样本量/重复次数确定依据、正式效应量与95%CI、多重性校正。 |
| F2 | 内部效度 | NA | — | 这是非实验性基准评测，没有随机分配、分配隐藏、基线等价或人类被试流向/损耗需要报告；也不作严格因果效应推断。 |
| F3 | 构念效度 | 0.5 | pp.1-2 define PN/PS and counterfactual consistency; p.7 metrics; p.10 limitations. | 有理论构念界定与多任务操作化，但没有报告正式信度/效度证据、操纵检验或评分者一致性，构念效度论证不完整。 |
| F4 | 外部效度 | 0.5 | p.7 GPT-2/GPT-3.5-turbo/GPT-4; p.10 limitations; p.23 Appendix J Llama/Phi replication. | 报告了模型来源和部分跨家族复现，并讨论边界；但缺少精确模型 snapshot、采样框/代表性说明与系统推广边界。 |
| G1 | 分析单位 | 0.5 | p.7 describes 400 instances, 10 answers, 500 bootstrap; p.21 Appendix H defines n instances and metrics. | 说明了问题实例级指标与 bootstrap，但未显式处理重复回答嵌套于问题/模型的多层结构；分析层级与分配层级匹配说明不足。 |
| G2 | 随机效应 | NA | — | 没有混合模型或随机效应；模型版本被作为固定基准对象比较，不需要推广到模型总体的随机效应结构。 |
| G3 | 材料作为随机效应 | NA | — | 数学实例来自穷举式有限数域，不是从材料总体随机抽样的项目集；不适用项目随机效应推广。 |
| G4 | 统计功效 | NA | — | 研究是探索性/描述性基准评测，使用穷举式实例集，未预设效应量或进行样本量功效分析；不按假设检验型功效分析适用。 |
| G5 | 研究者自由度 | 0.5 | p.7 lists tasks and metrics; p.10 limitations; p.24 checklist says 'Code is not provided'. | 报告了主要任务、指标与部分限制，但缺少试次/数据排除规则、停止规则、代码数据以及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.24 NeurIPS checklist has no preregistration link or registry ID. | 没有预注册或公开分析计划；因此适用但未达成。 |
| J1 | 位置偏差 | NA | — | 任务不涉及多候选项选择、排序或 LLM-as-judge 成对比较；提示直接要求判断，无候选位置偏差问题。 |
| J2 | 冗长偏差 | NA | — | 评估的是短二元回答/数学判断，不是开放式生成质量或长度比较，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 没有用户立场、反馈或纠错输入，不涉及谄媚/迎合用户先验。 |
| J4 | 自我偏好 | 0 | p.21 Appendix F 'GPT-4 concretization' prompt: 'You are an entity extractor expert... say if the meaning of answer is positive or negative'. | 使用 GPT-4 作为答案含义的抽取/判定器，而被评估模型也包括 GPT-4；论文未报告裁判与被评模型同源风险，也未做异源裁判、匿名化或一致性检验。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | Appendix E 提示为零样本直接/反事实提示，没有 few-shot 示例选择或排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | pp.19-21 provide full prompt templates; p.10 limitation says 'Prompt-dependent results'. | 公布了主要提示模板并承认提示依赖，但没有版本化、dev/test 划分、语义等价敏感性消融或 prompt 搜索过程报告。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短，无长文档/RAG 或中间迷失问题。 |
| J8 | 温度与采样随机性 | 0.5 | p.7 uses '10 answers' per prompt and '500 bootstrap samples'; no temperature/top-p/seed/snapshot reported. | 通过重复回答和 bootstrap 处理随机性，但缺少温度、top-p、随机种子、API snapshot 等关键采样报告。 |
| J9 | 重复与文本退化 | NA | — | 输出为简短 yes/no 类回答，不涉及开放式长文本生成、重复退化或解码策略对文本质量的混淆。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本，无跨语言/跨脚本分词效率比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.2 claims counterfactual tests require generalization beyond training patterns; p.10 limitations; no training cutoff or contamination analysis reported. | 核心主张涉及避免训练记忆/模式复用，但没有对照测试集与模型训练截止日期，也未做污染检测或报告污染率。 |
| J12 | 基准饱和 | NA | — | 使用自建数学推理任务而非公开饱和基准，且报告连续型 γ-overlap 与 bootstrap 分布，不按公开基准饱和问题适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，没有约束类型拆分准确率或可机器验证指令集。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 没有要求 JSON/文法/结构化输出，也未把格式合法率作为指标；短回答解析不属于结构化输出实验。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱、有害请求或攻击成功率评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | pp.1-2 discuss human-like reasoning and Pearl's causal hierarchy; p.4 H_Ex abstract machine; p.10 limitations. | 论文明确把 LLM 推理与人类推理/因果层级联系起来，并讨论边界；但没有人类同范式对照、精确权重快照或系统构念效度比较。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p.7: 'whether the ability to reason... emerges as the complexity and size of the models grow'; p.9: 'emerging trend towards reasoning'; p.8 densities/γ-overlap. | 报告了随模型规模/复杂度的比较与连续 overlap 曲线，但仅三个 GPT 模型、缺少多 seed 系统曲线与机制证据，尚不足以排除指标诱导的涌现假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N 或对代理指标的优化环节；纯评测研究不涉及奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.7 reports 10 answers and 500 bootstrap; p.6 names GPT-2/GPT-3.5-turbo/GPT-4; no API snapshot/date; p.24 says code not provided. | 报告了重复次数与不确定性估计，但模型 snapshot 标识不精确、未给 API 调用日期、未做配对检验，且代码/原始日志不可得。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 所有评测均为单轮提示，没有对话历史累积或多轮一致性衰减评估。 |

## 编码小结
论文提出了以 PN/PS 和反事实一致性评估 LLM 推理能力的理论与实证框架，任务、提示模板和指标定义较清楚，并用重复回答与 bootstrap 表征不确定性。但作为实证基准，关键方法学报告不足：温度/采样参数、模型 API snapshot/日期、代码与数据未完整提供；评分使用 GPT-4 concretization prompt 但未讨论同源裁判偏差；未做污染/训练截止检查、功效分析或预注册。总体适合按 LLM 基准评测编码，许多人类实验设计组件不适用。
