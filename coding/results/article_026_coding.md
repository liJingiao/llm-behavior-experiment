# article_026 | Are Large Language Models Sensitive to the Motives Behind Communication? | 2025

研究类型概述：该文将 LLM 作为认知科学/心理学意义上的被试，采用三个实验范式评估其“动机性警觉”：实验1比较建议与偷看信息，实验2操纵角色善意与激励并拟合贝叶斯理性模型，实验3使用300条YouTube赞助片段并测试提示 steering。分析单位为模型-条件-试次/视频的 LLM 调用，人类数据仅作对照。
- **研究构念（Construct）**：动机性警觉与选择性社会学习（motivational vigilance and selective social learning）｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；冲动性（impulsivity, `trm_50070dce14554`）；内部动机（intrinsic motivation, `trm_4a3fd79d0a6e8`）
- **实验任务与范式（Task / Paradigm）**：该文将 LLM 作为认知科学/心理学意义上的被试，采用三个实验范式评估其“动机性警觉”：实验1比较建议与偷看信息，实验2操纵角色善意与激励并拟合贝叶斯理性模型，实验3使用300条YouTube赞助片段并测试提示 steering。分析单位为模型-条件-试次/视频的 LLM 调用，人类数据仅作对照。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_4: 'Player 1 is randomly assigned to give either advice ... or their spied actual answer'; PDF_PAGE_6: characters and incentives vary; PDF_PAGE_9: steering prompt appended; PDF_PAGE_5: first-guess accuracy 18–44%. | 自变量被明确命名并给出至少两个水平与操纵程序，分配方式也有部分说明；但操纵检验主要只在实验1报告，实验2/3未系统报告，故为0.5。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_5: 'average proportion shifts' and first-guess accuracy; PDF_PAGE_6: influence/trust/incentive scores; PDF_PAGE_24: 0–100 scales with anchors. | 因变量指标与计分方式明确，但未报告内部一致性/重测信度、效度证据或连续指标的预处理与天花板/地板说明，故为0.5。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_5: 'same LLM was assigned to both Player 1 and 2' and image order shuffled; PDF_PAGE_6: independent context windows and randomized speaker order; PDF_PAGE_8: brand/product names censored. | 报告了若干控制手段，但没有系统列出控制变量清单并逐一说明，故为0.5。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_8: censor brand/product names 'to mitigate the confounding effects'; PDF_PAGE_23 Table 4: initial correctness does not significantly change susceptibility; PDF_PAGE_10: transcript length as potential cause. | 识别并控制了品牌印象、初始正确性、长度等潜在混淆，但对残余混淆和内部效度威胁没有系统讨论/敏感性分析，故为0.5。 |
| A5 | 调节变量 | 0.5 | PDF_PAGE_29: 'no significant advantage for either approach (p > .1)' for CoT/direct and perspective; PDF_PAGE_9: Fisher r-to-z test for steering; Table 2 reports condition-specific correlations. | 论文比较了提示方式、角色和 steering 等调节性条件，并报告部分条件差异检验；但没有正式乘积项交互模型、中心化或简单斜率分析，故为0.5。 |
| A6 | 中介变量 | NA | — | 理论模型和结果均不包含中介变量或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_18–PDF_PAGE_33 附录给出完整提示词、游戏流程、评分锚点与 steering 文本；PDF_PAGE_4–PDF_PAGE_8 描述实验程序。 | 关键构念的自变量操纵与因变量测量均有可复现的操作化程序，达到1。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_4: advice vs spied, cooperative vs competitive; PDF_PAGE_6: four characters and four incentive values; PDF_PAGE_24–PDF_PAGE_28 lists concrete incentive values; PDF_PAGE_9: default vs steering. | 报告了水平数与各水平取值/标签，但缺明确的水平类型、间距/全距及连续变量中心化说明，故为0.5。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_2–PDF_PAGE_3: three experimental paradigms; PDF_PAGE_10: discusses controlled vs naturalistic settings and generalization limits. | 关键构念 vigilance 采用三种任务和多种指标，并报告跨范式会聚与边界讨论，达到1。 |
| A10 | 单一方法的风险 | 0.5 | PDF_PAGE_6: same multi-turn dialogue but independent context windows and counterfactual phrasing; PDF_PAGE_8: separate context windows for each variable and brand censoring. | IV 与 DV 均来自 LLM 提示/输出，存在同源问题；论文有程序性分离但未报告共同方法偏差检验或明确讨论，故为0.5。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配；模型间比较不是将被试随机分到条件，故被试间设计不适用。 |
| B2 | 被试内设计 | 0.5 | PDF_PAGE_5: 'order shuffled every trial'; PDF_PAGE_6: 'The order in which speakers are presented is randomized'; PDF_PAGE_7: n=40 per setting. | 同一模型内重复接受多个条件/多次调用，且有随机顺序；但未报告顺序分配计数，也未将被试/模型作为随机效应建模，故为0.5。 |
| B3 | 混合设计 | 0 | PDF_PAGE_7 Table 1 and PDF_PAGE_29 Table 5 report condition-wise correlations; no mixed-design ANOVA or separate between/within error terms reported. | 研究含模型间与条件内因素，但未逐因素标注组间/组内属性，也未使用混合设计统计模型，故为0。 |
| B4 | 因子设计 | 0.5 | PDF_PAGE_7 Table 1 averages over settings/prompt conditions; PDF_PAGE_29 Table 5 gives model × prompt × perspective combinations; no full design matrix or ANOVA interaction table. | 存在多因素交叉结构并报告部分条件结果，但未给出完整设计矩阵、每格样本量和交互项统计量，故为0.5。 |
| B5 | 主效应 | 0 | PDF_PAGE_7 Table 1; PDF_PAGE_29 Table 5: only correlations/condition comparisons, no main-effect F, df, p, or effect size. | 没有报告因子设计意义上的主效应统计检验，故为0。 |
| B6 | 交互作用 | 0.5 | PDF_PAGE_9: 'Fisher r-to-z transformation test, α = .05' for steering effect; PDF_PAGE_29: p > .1 for prompting/perspective comparisons. | 报告了部分条件差异/交互式比较，但无完整交互项 F、df、效应量、简单主效应和误差棒，故为0.5。 |
| B7 | 区组设计 | NA | — | 没有使用区组变量或分层随机分配；长度四分位是事后分析而非区组设计，故不适用。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序平衡；实验2仅为随机化 speaker 顺序，故不适用。 |
| B9 | 准实验设计 | NA | — | 不是非随机分组的准实验；LLM 条件由研究者设定或随机化，故不适用。 |
| B10 | 被试内设计的适用条件 | 0 | PDF_PAGE_5: 20 questions per game; PDF_PAGE_6: 16 speakers elicited within the same multi-turn dialogue, order randomized. | LLM 在同一会话内重复接受条件，但未论证处理可逆性、迁移对称性或顺序效应，故为0。 |
| C1 | 随机化 | 0.5 | PDF_PAGE_4: 'randomly assigned'; PDF_PAGE_6: speaker order randomized; PDF_PAGE_8: 300 randomly selected video IDs. | 提及随机分配/随机抽样，但未报告随机数生成工具、分配隐藏机制或基线均衡检验，故为0.5。 |
| C2 | 平衡 | 0.5 | PDF_PAGE_5: 'order shuffled every trial'; PDF_PAGE_6: 'order in which speakers is presented is randomized'. | 报告了随机顺序，但没有说明平衡层级、各顺序分配数量或迁移对称性前提，故为0.5。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_5: temperature=1; PDF_PAGE_7: max tokens 10/750, temperature 1; PDF_PAGE_8: temperature=0 for experiment 3. | 列出了温度、输出长度等恒定水平，但未系统讨论这些恒定选择对外部效度的限制，故为0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配程序，故不适用。 |
| C5 | 纳入为变量 | 0.5 | PDF_PAGE_23 Table 4: initial correctness analyzed; PDF_PAGE_10 Table 3: transcript length quartiles analyzed; PDF_PAGE_8: brand names censored. | 测量并分析了若干已知混淆变量，但未将其作为协变量/区组纳入统一模型，也未检验斜率齐性，故为0.5。 |
| C6 | 盲法 | NA | — | 完全自动化 LLM 调用，无人类被试或人类评分者需要盲法；条件本身在提示中明示，故不适用。 |
| C7 | 平衡的层级 | 0 | PDF_PAGE_5: 'order shuffled every trial'; PDF_PAGE_6: 'randomized' speaker order, no explicit balance level or construction method. | 仅称随机/打乱，未明确完全平衡、拉丁方或 ABBA 等平衡层级及构造方法，故为0。 |
| D1 | 练习效应 | 0 | PDF_PAGE_5: models answer 20 questions in sequence; no practice block, truncation, or trial-position covariate reported. | 多题连续作答存在练习风险，但未报告练习控制或试次位置处理，故为0。 |
| D2 | 疲劳效应 | 0 | PDF_PAGE_5: 20-question game; PDF_PAGE_6: 16 speakers within one multi-turn dialogue; no rest schedule or session-length control reported. | 存在较长多轮调用，但未报告休息、时长或条件时间分散方案，故为0。 |
| D3 | 延滞 / 迁移效应 | 0 | PDF_PAGE_6: all 16 speakers elicited within the same multi-turn dialogue, with counterfactual phrasing after first speaker; no washout or carryover modeling reported. | 同一对话内条件顺序可能产生迁移/上下文残留，但未报告清洗期或条件对建模，故为0。 |
| D4 | 不对称迁移 | 0 | PDF_PAGE_6: speaker order randomized but no test of asymmetric carryover; PDF_PAGE_29 only report correlations by prompt/perspective. | 未检验迁移对称性，也未讨论平衡失效及替代方案，故为0。 |
| D5 | 范围效应 | 0.5 | PDF_PAGE_24–PDF_PAGE_28: all ratings use 0–100 scales with absolute anchors such as 0/50/100 meanings. | 量表采用绝对锚点，但未识别或讨论被试内评分中的范围效应风险，也未设置被试间对照，故为0.5。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_5: image order shuffled every trial; PDF_PAGE_6: speaker presentation order randomized. | 对刺激/呈现顺序做了随机化，但未说明随机化方案类型、各位置出现次数或被试分配细节，故为0.5。 |
| E2 | 默认赞同 | 0 | PDF_PAGE_24–PDF_PAGE_28: 0–100 single-direction rating anchors; no reverse-coded items or acquiescence discussion. | 使用单向评分量表且未设反向题，也未讨论默许偏差，故为0。 |
| E3 | 极端 / 中间反应倾向 | 0 | PDF_PAGE_7 Table 1 and PDF_PAGE_9 Table 2 report correlations, not score distributions, skewness, or endpoint/midpoint usage. | 未报告量表分数分布形态，也未讨论跨模型反应风格差异，故为0。 |
| E4 | 需求特征 | NA | — | 研究对象为 LLM，无人类被试需求特征或事后访谈问题；故不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试或评分者参与，故不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_5: first-guess accuracy 18–44% versus human 55%, used to confirm task difficulty; no full mean/SD/skew/endpoint report. | 报告了部分准确率与难度校准证据，但没有系统报告因变量分布、偏度或端点频率，故为0.5。 |
| E7 | 共同方法偏差 | 0.5 | PDF_PAGE_6: independent context windows and counterfactual phrasing; PDF_PAGE_8: each variable prompted in separate context windows and brand names censored. | IV 与 DV 同源于 LLM 提示/输出；有程序性分离但未报告共同方法偏差统计检验或明确讨论，故为0.5。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_7: n=40 (or 10/80) per setting; Table 1 reports Pearson correlations and p<.05 claims; PDF_PAGE_9: Fisher r-to-z tests. | 报告了相关系数作为效应量和部分显著性检验，但无置信区间、样本量功效依据或多重比较校正说明，故为0.5。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_4: random assignment of advice/spied; PDF_PAGE_8: random video sampling; PDF_PAGE_23: initial-correctness confound check. | 报告了随机化和部分混淆检查，但缺分配隐藏、基线等价检验与系统内部效度威胁评估，故为0.5。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_7 Table 1: LLM–Human correlations used as criterion-related evidence; PDF_PAGE_5: task-difficulty check. | 有多操作化和部分效标效度/操纵检验证据，但未报告测量信度，故为0.5。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_8: 300 randomly selected YouTube sponsorship videos; PDF_PAGE_7: broad model suite; PDF_PAGE_10: discussion of controlled vs naturalistic generalization. | 报告了模型与刺激来源并讨论生态效度，但未给出系统抽样框、代表性检验或跨情境复现设计，故为0.5。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_6: 16 speakers elicited within the same multi-turn dialogue; PDF_PAGE_7: n=40 repeated calls per setting; analyses are correlations. | 说明了每次条件/模型的调用次数，但存在同一对话/模型/视频的嵌套结构而未用多层模型分离聚集方差，故为0.5。 |
| G2 | 随机效应 | 0 | PDF_PAGE_7 and PDF_PAGE_29: analyses report correlations/condition comparisons; no mixed model, random intercepts/slopes, or fixed/random effect listing. | 未说明或建模随机效应，未区分模型/被试/项目等抽样层级，故为0。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_8: '300 randomly selected video IDs' as stimuli; analyses correlate model scores with Bayesian predictions across videos. | 材料被视为从更大视频总体抽样，但分析中未将视频/项目作为随机效应纳入模型，故为0.5。 |
| G4 | 统计功效 | 0 | PDF_PAGE_7: reasoning models prompted 10 times due to cost and GPT-4o 80 times due to credits; no a priori power analysis or CI reported. | 样本量由成本决定，未做事前功效分析，也未报告效应量置信区间，故为0。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_7: reports n per condition; PDF_PAGE_8: n=1 per video/prompt; PDF_PAGE_10: length analysis appears exploratory. | 报告了主要条件与样本量，但未报告数据排除规则，也未明确区分验证性与探索性分析，故为0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–41 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未见公开预注册、注册编号或数据收集前的分析计划，故为0。 |
| J1 | 位置偏差 | NA | — | 实验不涉及多候选项选择、排序或 LLM-as-judge 成对比较，无候选位置偏差问题，故不适用。 |
| J2 | 冗长偏差 | NA | — | LLM 不是用于评估开放性生成质量的裁判；实验3分析的是赞助文本长度与警觉相关，而非裁判长度偏差，故不适用。 |
| J3 | 谄媚 | NA | — | 未操纵用户先验立场或反馈纠错，任务不是对话式谄媚评估，故不适用。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 评估模型输出或自我偏好比较，故不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 所有任务均为 zero-shot 提示，未使用 few-shot in-context examples，故不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_18–PDF_PAGE_33: full prompt templates provided; PDF_PAGE_33: additional Gricean and bias steering variants tested. | 提供了完整模板并比较了若干 steering 版本，但没有版本号/迭代日期、dev/test 划分或系统敏感性消融，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | PDF_PAGE_10 Table 3: performance compared across shortest/longest transcript quartiles; PDF_PAGE_8: transcripts vary in length. | 有长度分层分析，但未报告实际 token 数、关键信息位置操纵或位置×正确率曲线，故为0.5。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_5: temperature=1, n=30 trials; PDF_PAGE_7: temperature=1, n=40/10/80; PDF_PAGE_8: temperature=0, n=1. | 报告了温度与重复次数，但无 top-p/top-k、随机种子、bootstrap CI 或精确 snapshot，故为0.5。 |
| J9 | 重复与文本退化 | 0 | PDF_PAGE_5: max output tokens 10 direct and 750 CoT; no decoding strategy, repetition penalty, or repetition/degeneration rate reported. | 涉及 CoT 开放生成，但未报告解码策略与重复/退化控制，故为0。 |
| J10 | 分词效应 | NA | — | 单语言英文实验，无跨语言/跨脚本分词比较，故不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_8: dataset built from SponsorBlock/YouTube; no model training cutoff comparison or contamination check reported. | 未报告测试集与模型训练截止日期对照，也未做污染检测，故为0。 |
| J12 | 基准饱和 | NA | — | 研究使用自建认知任务和 YouTube 刺激，不是标准基准饱和评估，未宣称 SOTA 水位，故不适用。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；输出数字/评分是任务测量本身，非指令遵循基准，故不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF_PAGE_19: 'respond with only a number'; PDF_PAGE_32: CoT format 'Reasoning: [...] Answer (integer score only): [...]'. | 报告了输出格式约束，但未报告格式合法率、解析失败或重试策略，故为0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估，故不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF_PAGE_2–PDF_PAGE_3: explicitly frames LLM motivational vigilance and compares to human data/rational model; PDF_PAGE_7: model list; PDF_PAGE_10: discussion of human-LLM convergence/divergence. | 明确把 LLM 构念与人类同名构念对照并讨论异同；但未报告精确权重快照/版本，故为0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | PDF_PAGE_8: 'Vigilance improves with LLM scale and capability'; Table 1 reports continuous correlation by model size. | 规模比较使用连续相关指标，但未报告多 seed 曲线、置信区间或机制证据，故为0.5。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标进行训练/RL/best-of-N 优化，故不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_7: model names and n=40/10/80; PDF_PAGE_8: n=1 for experiment 3; no exact API dates or CI. | 报告了重复次数，但模型 snapshot 不精确、无置信区间/配对检验，故为0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF_PAGE_6: all 16 speakers elicited within the same multi-turn dialogue; PDF_PAGE_5: 20-question game sequences. | 进行了多轮/多题评估，但未按轮次独立评分、未报告上下文截断或跨轮一致性衰减，故为0.5。 |

## 编码小结
论文方法披露较充分，提供了完整提示词、模型列表、温度和部分重复次数，并用人类数据与贝叶斯模型作基准；但统计模型多为相关/条件比较，缺少正式操纵检验、信效度、功效分析、预注册、随机效应/嵌套建模，实验3每条件仅1次调用且无置信区间。整体属于较扎实的 LLM 行为评估，但若干实验设计与可复现性报告不完整。
