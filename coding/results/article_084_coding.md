# article_084 | Think Twice: Perspective-Taking Improves Large Language Models’ Theory-of-Mind Capabilities | 2024

研究类型概述：该文是 LLM 零样本 Theory-of-Mind 基准评测与提示策略比较研究：在 BigTOM、ToMI 及小型 CosmosQA 定性子集上，对 Llama2-7b/13b-chat、GPT-3.5-Turbo、GPT-4 比较 0-shot、0-shot CoT、两阶段 SimToM 及其 Single/Multi/Domain/Oracle 消融。分析单位是模型×题目×提示条件下的多项选择准确率，不是人类被试实验，也不是以 LLM 作裁判的评估。
- **研究构念（Construct）**：Theory of Mind、视角采择与Simulation Theory｜CA 构念锚定：心理理论（theory of mind, `trm_4a3fd79d0b392`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：该文是 LLM 零样本 Theory-of-Mind 基准评测与提示策略比较研究：在 BigTOM、ToMI 及小型 CosmosQA 定性子集上，对 Llama2-7b/13b-chat、GPT-3.5-Turbo、GPT-4 比较 0-shot、0-shot CoT、两阶段 SimToM 及其 Single/Multi/Domain/Oracle 消融。分析单位是模型×题目×提示条件下的多项选择准确率，不是人类被试实验，也不是以 LLM 作裁判的评估。｜CA 任务锚定：心理理论任务（theory of mind task, `trm_4c8a8467304e2`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_4: “we evaluate LLMs 0-shot on ToM benchmarks with and without our SimToM prompting framework”; PDF_PAGE_6-7: Table 1/2 list 0-shot, 0-shot CoT, SimToM, SimToM-Single/Multi/Domain/Oracle. | 提示策略被明确命名并报告了多个水平及完整 prompt，但未说明条件如何分配到评测单位，也未报告操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_5: “we prompt models with a story, a question, and answer choices... choose the correct answer choice”; accuracy is aggregated for False Belief and All question types. | 因变量指标（MC 准确率）与计分方式清楚，但未报告测量信度、效度、重复运行/CI，也无连续指标预处理说明。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_5: “We query all models with temperature=0.0 for reproducibility”; “We run inference on the open source models on a single A100 GPU”. | 报告了温度与硬件等少量控制，但没有系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_6: “GPT-4... slight decrease... may be partly confounded by the fact that BigTOM was generated using GPT-4”; PDF_PAGE_2 mentions “possible dataset leakage to closed-source models’ training sets”. | 识别了若干潜在混淆（GPT-4 生成 BigTOM、数据泄漏），但未系统控制或做敏感性分析，残余威胁讨论有限。 |
| A5 | 调节变量 | NA | — | 全文没有正式定义或检验调节变量；模型/数据集差异只是描述性比较，不构成调节假设与交互分析。 |
| A6 | 中介变量 | NA | — | 全文没有中介变量假设，也没有直接效应与间接效应的分解。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_4-5: two-stage SimToM procedure; PDF_PAGE_12-16: full prompts in Appendices B–E; PDF_PAGE_5: sampling and deterministic parsing rules. | 关键构念（视角采择提示、ToM 问题回答）均有可复现操作化：完整 prompt、数据采样、解析与准确率计分；满足可复现要求。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_6-7: Table 1 and Table 2 list 0-shot, 0-shot CoT, SimToM, SimToM-Single, SimToM-Multi, SimToM-Domain, SimToM-Oracle. | 报告了各提示条件的标签与水平数，但未系统说明水平类型、间距/全距等；作为分类提示条件可识别，但信息不完整。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_7-8: ablations include SimToM-Single, SimToM-Multi, SimToM-Domain, SimToM-Oracle; PDF_PAGE_9: limitation discusses that perspective-taking is implemented by “hiding” information. | 对关键构念采用多种操作化/消融并在多个基准和模型上报告会聚结果，同时讨论单一实现的推广限制，满足 1。 |
| A10 | 单一方法的风险 | NA | — | 这是客观 MC 准确率基准评测，不是多构念自陈量表；IV 为提示文本、DV 为可判定的准确率，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类或 LLM 被试被分配到互斥条件；模型×提示条件是对同一基准的比较运行，不是被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有报告以被试/会话为单位的重复测量顺序设计；每次评测是独立提示调用，不构成需要顺序平衡的被试内设计。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合设计，也没有对应统计模型与误差项。 |
| B4 | 因子设计 | NA | — | 模型、提示策略、数据集构成评测网格，但未作为完整因子实验报告设计矩阵、每格样本量和 ANOVA 交互检验；不按因子设计编码。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验（F、df、p、效应量）。 |
| B6 | 交互作用 | NA | — | 没有正式交互项检验、简单主效应或带误差棒的交互图；模型×提示差异只作描述性比较。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计，也未报告区组变量与区内随机分配。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；没有非随机分组、选择偏差或 RDD/DiD 等结构。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有采用需要论证可逆性与迁移对称性的被试内处理设计。 |
| C1 | 随机化 | NA | — | 没有条件分配或随机化机制；ToMI 的 100 题/类型只是数据集抽样，不是实验条件随机分配。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，因此没有需要平衡的顺序。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_5: “temperature=0.0 for reproducibility”; “single A100 GPU”; closed-source models queried “using their API”. | 报告了温度、硬件与 API 等恒定条件，但未系统列出所有恒定变量及其水平，也未讨论这些恒定对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有匹配变量、配对或 PSM 等匹配程序。 |
| C5 | 纳入为变量 | NA | — | 没有把潜在混淆变量作为区组或协变量纳入统计模型；本文也未使用 ANCOVA/回归调整。 |
| C6 | 盲法 | NA | — | 主要评估为自动化评分；不存在需要对人类被试、主试或评分者施盲的条件隐藏设计。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | LLM 每个题目独立调用，没有练习块或跨试次学习设计。 |
| D2 | 疲劳效应 | NA | — | LLM 评测无疲劳效应；也没有长 session 或休息间隔设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各提示条件独立运行，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉条件，因此不存在不对称迁移检验。 |
| D5 | 范围效应 | NA | — | 因变量为客观 MC 准确率，不是 Likert/绝对量值估计，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF_PAGE_5: “we prompt models with a story, a question, and answer choices”; PDF_PAGE_6: ToMI is made binary by including “both possible answer choices (e.g., A and B)”. | 使用多项选择选项，但没有报告选项顺序随机化/反平衡，也未讨论固定选项位置对准确率的影响。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 研究对象是 LLM 输出，没有人类被试可推断研究假设或接受事后访谈的需求特征问题。 |
| E5 | 实验者效应 | NA | — | 主要数据采集与评分自动化，无人类主试/评分者期望传递；oracle 子集的人类标注不是结果评分。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_6: “GPT-4, which had saturated human performance 0-shot”; PDF_PAGE_17: Table 4 contains multiple 100.00 values (e.g., memory/reality). | 报告了均值型准确率并提到 GPT-4/BigTOM 饱和，但没有系统报告标准差、偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；共同方法偏差框架不适用。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_5: Table 1 reports accuracy and absolute accuracy differences in parentheses; PDF_PAGE_5: ToMI has 1000 samples and BigTOM 200 questions per type. | 报告了准确率差（可作效应量）和样本规模，但没有置信区间、事前功效分析、多重比较校正或统计假设检验。 |
| F2 | 内部效度 | NA | — | 无人类被试随机分配、分配隐藏、基线等价或流失处理问题；这是静态基准比较，内部效度混淆在 A4/J11 中处理。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_3: describes ToMI and BigTOM as established ToM benchmarks; PDF_PAGE_5: “updated version of ToMI... relabelled mislabelled second-order questions and disambiguated...” | 使用已有基准并提供部分效度依据，但没有测量信度、评分者信度或正式 manipulation check；对单一提示实现的构念对应关系仅部分论证。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_5: four models evaluated; PDF_PAGE_9 Limitations: “perspective-taking is currently implemented by ‘hiding’... ” and “we have not performed tests with smaller language models than 7B”. | 报告了模型与数据集来源，并讨论合成 Sally-Anne 任务、真实场景和模型规模边界，但没有正式跨样本/跨情境复现研究。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_5: “randomly sample 100 samples from each of the ten question types to create a balanced dataset of 1000 samples”; BigTOM “200 questions per question type”. | 分析层级基本是题目级准确率，但未说明题目嵌套于数据集/题型的聚集结构，也未使用多层模型或聚类稳健处理。 |
| G2 | 随机效应 | NA | — | 没有混合模型或随机效应结构；模型被当作固定基准系统而非从总体随机抽样的被试。对该类基准评测，随机效应模型并非必需。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_5: ToMI sampled 100 per question type; BigTOM uses 200 per question type and is described as balanced. | 材料/题目被视为有限基准题目，ToMI 有抽样但分析中没有把 item 作为随机效应；结论对材料总体的推广未通过混合模型处理。 |
| G4 | 统计功效 | 0 | PDF_PAGE_5-8: results report accuracy and absolute differences; no power analysis or target effect size is reported. | 没有事前功效分析、目标效应量来源、样本量推导；结果也缺少置信区间。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_5: models can decline to answer and reduce accuracy; PDF_PAGE_7-8: many ablations are reported; PDF_PAGE_5: fixed sampling rules (1000 ToMI, balanced BigTOM). | 报告了大量条件与消融，但未明确报告试次/模型输出剔除规则、所有可能未显著分析及样本量停止规则；部分满足。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–18 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册平台、注册号或数据收集前分析计划；也未区分预注册验证性与事后探索性分析。 |
| J1 | 位置偏差 | 0 | PDF_PAGE_5: answer choices are supplied to the model; PDF_PAGE_6: ToMI uses both possible choices A and B. No option-position randomization or swap analysis is reported. | 涉及二元/多项选择，但完全未报告候选位置反平衡、正确答案位置分布或交换前后翻转率；无法排除位置偏差。 |
| J2 | 冗长偏差 | NA | — | 评估是严格 MC 准确率，不使用 LLM 裁判比较开放生成质量，也不涉及长度与质量混淆。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或多轮纠错操纵，不涉及谄媚评估。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 或成对模型输出评审；准确率由答案匹配判定。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF_PAGE_8: “enhancing the SimToM with 3 examples of perspective-taking drawn from in-domain ToMI stories”; exact few-shot prompts are in PDF_PAGE_15 Appendix D. | 报告了示例来源与数量（3 个 in-domain ToMI 示例）并提供模板，但未报告每类标签比例、排列反平衡或多 seed 重采样。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_5: “Our prompts for SimToM vary somewhat based on the structure of the dataset, and vary minimally between Llama and GPT models”; full prompts in PDF_PAGE_12-16. | 提供了完整 prompt 模板，并说明按数据集/模型略有变化；但没有正式版本化、语义等价措辞敏感性消融或 dev/test 划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短故事，不是长上下文/RAG 设置；未涉及关键信息首中尾位置操纵或迷失中间问题。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_5: “We query all models with temperature=0.0 for reproducibility”; no seed, top-p, repeated sampling N, or CI is reported. | 报告了温度，但缺少 top-p/top-k/seed、每条件重复采样次数与方差估计；闭源 API 未给精确 snapshot。 |
| J9 | 重复与文本退化 | 0.5 | PDF_PAGE_5: temperature=0.0; PDF_PAGE_13: output-format instructions such as “Answer with a single word”. No repetition rate or degeneration QC is reported. | 报告了温度且多为短答案/中间过滤文本，但未明确解码策略（greedy/beam/sampling）、repetition penalty、n-gram 重复率或截断比例。 |
| J10 | 分词效应 | NA | PDF_PAGE_3: “Both datasets are available in the English language only.” | 单语言、单脚本研究，无跨语言/跨脚本 tokenization 比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | PDF_PAGE_2: mentions “possible dataset leakage to closed-source models’ training sets”; PDF_PAGE_6: GPT-4 result “may be partly confounded by the fact that BigTOM was generated using GPT-4”. | 识别了污染/生成泄漏风险，但没有报告测试集版本与训练截止日期的系统对照、n-gram 重叠或污染率检测。 |
| J12 | 基准饱和 | 0.5 | PDF_PAGE_6: “GPT-4... had saturated human performance 0-shot”; PDF_PAGE_17: Table 4 includes multiple 100.00 scores. | 在部分基准/子类上出现饱和，作者有提及，但仍主要报告离散准确率，未改用连续指标或给出 bootstrap CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；虽然 prompt 有格式要求，但核心测量是 ToM 问题准确率，不是约束遵循评估。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF_PAGE_13: “Answer as ’Answer:<option>)<answer>’”; PDF_PAGE_5: ambiguous/non-conforming outputs are discussed and parsed. | 有明确输出格式约束并说明解析方式，但未报告格式合法率、重试策略或把格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估，无有害请求或攻击成功率测量。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF_PAGE_2-4: frames ToM via Simulation Theory and perspective-taking; PDF_PAGE_2: cites human performance; PDF_PAGE_9: discusses limitations of hiding as implementation of perspective-taking. | 明确以人类 ToM/Simulation Theory 为理论来源并讨论 LLM 实施限制，但未系统给出 LLM 构念与人类同名构念的异同论证，也未有同范式人类对照数据；模型版本仅给名称。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告跨模型规模/训练进展的能力曲线，也不宣称“涌现/突变”。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有以 benchmark 或奖励模型为优化目标进行训练/RL/best-of-N 优化，不存在代理指标过优化监控问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | PDF_PAGE_5: temperature=0.0; results are single point accuracies in Tables 1–4; no repeated runs, confidence intervals, or exact API snapshot dates are reported. | 仅报告单点分数，无重复次数、CI/配对检验、精确 snapshot 标识；虽有代码与 prompt，仍不足以满足可复现性核心要求。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验是两阶段提示而非多轮用户对话，未评估随轮次增加的指令遵循或一致性衰减；不适用。 |

## 编码小结
论文提出并系统评测两阶段视角采择提示 SimToM，报告多模型、多基准的准确率提升，并提供大量提示模板与消融；但统计以点估计和绝对准确率差为主，缺少重复采样、置信区间、精确 API snapshot、位置平衡、正式污染检测与功效分析。作为 LLM 行为/认知评测，其方法复现性尚可，但实验设计与统计推断的严谨性有限。
