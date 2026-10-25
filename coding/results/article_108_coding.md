# article_108 | A fine-grained comparison of pragmatic language understanding in humans and language models | 2023

研究类型概述：LLM 基准评测与人类行为对照研究：用七个语用现象的专家编制英语多选题，零样本提示 7 个语言模型，并与 374 名人类原始数据及 30 名无语境人类数据比较；另含选项顺序随机化、去语境和无序化扰动分析。分析单位为模型/任务/项目及人类被试的汇总表现。
- **研究构念（Construct）**：语用语言理解、共同知识推断与言外意义｜CA 构念锚定：语言理解（language comprehension, `trm_4a3fd79d0a775`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：LLM 基准评测与人类行为对照研究：用七个语用现象的专家编制英语多选题，零样本提示 7 个语言模型，并与 374 名人类原始数据及 30 名无语境人类数据比较；另含选项顺序随机化、去语境和无序化扰动分析。分析单位为模型/任务/项目及人类被试的汇总表现。｜CA 任务锚定：类比推理任务（analogical reasoning task, `trm_4f244f0286947`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3: 'Each task has 20-40 items'; p.8: 'we created a new set of stimuli by removing the context stories' and two scrambled versions by randomizing sentences/words. | 明确操纵了任务/现象、语境有无和乱序条件，并给出水平；但未报告操纵检验，条件分配也以全模型/全项目评估为主，报告不完整。 |
| A2 | 因变量 | 0.5 | p.5: 'The model is considered correct on a given item if it assigns highest probability to the correct answer token'; p.6 Figure 1 reports accuracy with 95% CI. | 因变量指标与计分方式清楚（正确率、答案 token 概率、人类选择频率）；但无内部一致性/重测信度、效度统计及连续指标预处理说明。 |
| A3 | 控制变量 | 0.5 | p.5: 'We generated 5 versions of each item by randomizing the order of answer options. This was done to control for the base probabilities of the answer tokens.' | 报告了选项顺序随机化这一控制手段，并提到零样本、不分析生成文本等；但未系统列出控制变量清单并逐一说明控制方式。 |
| A4 | 混淆变量 | 0.5 | p.9: 'Our experiments are not designed to tease apart the contributions of these training procedures'; p.10 Limitations discusses model size range and unknown API training. | 识别了模型规模/训练程序/未知 API 细节等潜在混淆，并讨论局限；但未系统控制或做敏感性分析来估计残余混淆。 |
| A5 | 调节变量 | NA | — | 理论模型不包含调节变量；模型规模与准确率的关系是描述性趋势，未作调节假设与交互检验。 |
| A6 | 中介变量 | NA | — | 未提出中介变量，也未做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.3 Table 1 gives an example item per task; p.5 describes prompt structure; Appendix A gives full prompt templates and answer options. | 对七个语用任务的操作化、材料结构、提示构造和正确性判定均给出可复现程序。 |
| A8 | 水平数与类型 | 0.5 | p.8: two scrambled versions and no-context versions; p.3: each task has 20-40 items and Table 1 lists option types. | 报告了主要条件的水平数与标签（七任务、语境两水平、乱序三水平、模型若干），但缺水平类型、间距/全距及连续模型规模的中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.2-3: seven pragmatic phenomena and item types; p.10 Limitations notes small item sets and stimuli not designed to require ToM. | 用多个语用任务覆盖宽泛构念，但每个现象基本只有单一任务族，未报告跨操作会聚证据；局限讨论也较概括。 |
| A10 | 单一方法的风险 | NA | — | 自变量为任务/语境等客观操纵，因变量为多选正确率或答案概率，不是同源自陈量表；共同方法偏差不构成主要适用风险。 |
| B1 | 被试间设计 | NA | — | 无随机被试间条件分配；原语境与无语境人类样本是不同样本的事后比较，模型也不是被随机分配到条件。 |
| B2 | 被试内设计 | 0.5 | p.16: 'Participants completed these tests during one individual testing session'; 'Items were presented within blocks according to their phenomenon... Blocks and items were presented in a random order.' | 人类被试接受全部现象任务，属重复测量/被试内结构，并报告随机顺序；但未报告各顺序分配，也未在统计模型中把被试作随机效应。 |
| B3 | 混合设计 | NA | — | 未采用或报告混合设计及对应混合模型/重复测量 ANOVA；模型与任务比较为描述性基准对照。 |
| B4 | 因子设计 | NA | — | 研究不是随机化因子实验，未进行任务×模型因子 ANOVA，也没报告设计矩阵与每格样本量；仅呈现实测单元格均值。 |
| B5 | 主效应 | NA | — | 无因子设计下的主效应统计检验；任务与模型差异以图和描述性准确率呈现。 |
| B6 | 交互作用 | NA | — | 未检验模型×任务交互项；结果讨论是任务间差异与模型表现对比，不是交互作用分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计；人类实验按现象分块只是施测组织方式，不是控制个体差异的区组变量。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方平衡；模型项目为独立提示，人类任务块为随机顺序。 |
| B9 | 准实验设计 | NA | — | 没有准实验分组或非随机处理分配下的因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无持久性处理或药物/学习类交叉处理；人类重复完成不同语用任务，不涉及处理可逆性论证。 |
| C1 | 随机化 | NA | — | 无被试/条件随机分配；选项顺序随机化在 E1 中编码，模型均为同一组项目全评估。 |
| C2 | 平衡 | 0.5 | p.16: 'Blocks and items were presented in a random order'; p.5: 5 versions by randomizing answer options. | 报告了随机顺序/选项随机化，但未说明平衡层级、各顺序人数或迁移对称性前提。 |
| C3 | 恒定 | 0.5 | p.5: 'All non-OpenAI models were accessed via Huggingface and run on a single NVIDIA A100 GPU'; p.5 zero-shot prompting; p.10 discusses English/Western and model-size limits. | 提到了固定模型版本、零样本提示和硬件等恒定条件，并讨论部分外部效度限制；但未系统列出所有恒定变量及水平。 |
| C4 | 匹配 | NA | — | 未使用匹配程序；模型/人类比较不是匹配样本设计。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 无处理分配的人类被试盲法或评分者盲法；任务为自动化多选，盲法不适用。 |
| C7 | 平衡的层级 | 0.5 | p.16: random order of blocks/items; p.5: randomizing answer options into 5 versions. | 使用了随机顺序/随机化，但未明确所选平衡层级、构造方法或顺序效应形状假设。 |
| D1 | 练习效应 | 0.5 | p.16: 'shown instructions and a training trial'; p.16: 105 trials in one session. | 有人类训练试次，但未报告练习块结束标准、是否截除前段试次或将试次位置作协变量。 |
| D2 | 疲劳效应 | 0.5 | p.16: 'took around 20 minutes to complete'; participants completed 105 trials in one session. | 报告了会话时长和试次数，但未报告休息间隔、条件时间分散方案或时间位置协变量。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM 每个提示独立、不分析生成文本；人类多选任务无药物/处理残留式迁移，无清洗期需求。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性设计或处理残留；不涉及平衡失效问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观正确率/答案概率，不是绝对量值估计或李克特量表，无范围效应校准问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.5: 'We generated 5 versions of each item by randomizing the order of answer options... to control for the base probabilities of the answer tokens.' | 对选项顺序做了随机化并说明目的；但未报告每位置出现次数、随机化方案细节、正确选项位置分布或翻转率。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分与默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 人类任务为客观语言多选，无欺骗性处理或明显假设引导；未做事后访谈，但需求特征风险低。 |
| E5 | 实验者效应 | NA | — | 数据采集主要为 MTurk/自动化模型 API，无人类主试或评分者期望传递场景。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Figure 1 reports accuracy with 95% CI; p.7 Figure 3 shows response distributions; p.10 notes small item sets. | 报告了均值/CI 和反应分布，但未系统报告偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 模型/人类均完成客观多选任务，IV 为任务/语境操纵，DV 为正确率/概率，非同源自评测量。 |
| F1 | 统计结论效度 | 0.5 | p.6 Figure 1 error bars denote 95% CI; p.9 Figure 5 reports Pearson correlations with significance codes. | 报告了置信区间、相关效应与显著标记；但无样本量/功效依据，未说明多重比较校正和统计假设检验。 |
| F2 | 内部效度 | 0.5 | p.9: 'Our experiments are not designed to tease apart the contributions of these training procedures'; p.10 Limitations lists model-size/API unknowns. | 报告了评估程序并讨论部分内部效度威胁；但无随机分配、分配隐藏或基线等价性检验。 |
| F3 | 构念效度 | 0.5 | p.3: items 'manually curated by expert researchers'; p.8 item-level model-human correlations; p.8 context/scrambling manipulations. | 有专家内容效度和人类对照/扰动操纵作为支持；但无信度统计、正式操纵检验或多操作会聚分析。 |
| F4 | 外部效度 | 0.5 | p.16: 30 MTurk participants from US/Canada/English-speaking countries; p.10 Limitations discusses English/Western materials and model-size range. | 报告了人类样本来源与部分推广边界；但未报告跨样本/跨语言复现，也未充分论证模型总体代表性。 |
| G1 | 分析单位 | 0.5 | p.8: 'For each task and model, we compute the Pearson correlation between by-item mean accuracy...'; p.16: 374 humans and 30 no-context humans. | 说明了项目层与模型/人类汇总层分析，但未用多层模型处理项目嵌套被试/模型的聚集结构，主要依赖聚合。 |
| G2 | 随机效应 | 0.5 | p.8 item-level correlations; p.16 human data aggregated; no mixed-model random effects reported. | 未报告随机效应结构；把人类被试和项目主要作聚合处理，无法清楚区分被试/项目随机方差。 |
| G3 | 材料作为随机效应 | 0.5 | p.8 item-level correlation between human accuracy and model probability; p.10 Limitations notes small item sets and lexical-item bias. | 有项目层分析并讨论小材料集局限，但未在混合模型中将材料/项目作为随机因子，结论对材料总体的推广仍有限。 |
| G4 | 统计功效 | 0.5 | p.6 Figure 1 reports 95% CI; p.10 Limitations mentions statistical power and small evaluation sets; no a priori power analysis. | 报告了 CI 和样本规模，但没有设计阶段功效分析或明确的最小效应量推导。 |
| G5 | 研究者自由度 | 0.5 | p.16 reports English proficiency/qualification screening; p.3 says 20-40 items per task; no stopping rule or full exclusion counts. | 报告了部分纳入/排除与全部任务，但未完整报告剔除数量、样本量决定方式和验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered report is mentioned in the main text or appendices. | 未发现公开预注册、分析计划或验证性/探索性区分；按规则记 0。 |
| J1 | 位置偏差 | 0.5 | p.5: 'We generated 5 versions of each item by randomizing the order of answer options... to control for the base probabilities of the answer tokens.' | 识别并随机化了选项位置以控制 token 基础概率；但未报告位置×正确率、交换翻转率或正确选项位置分布。 |
| J2 | 冗长偏差 | NA | — | 评估为多选答案 token 概率/正确率，不涉及开放式生成的长度—质量比较。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错式对话操纵，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge 评分；模型输出由答案 token 概率直接判定。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 使用零样本提示，无 few-shot 示例选择与排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5: 'Full example prompts are given in Appendix A'; Appendix A provides complete templates for all tasks. | 提供了完整提示模板与任务说明；但未报告版本号、语义等价措辞敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为 1-3 句短故事，远低于长上下文/RAG 场景，不涉及中间迷失或 chunk 排序。 |
| J8 | 温度与采样随机性 | 0.5 | p.5: 'Since we do not analyze generated text, the model results themselves are deterministic.' | 作者声明结果确定性且不生成文本，部分缓解随机采样问题；但未报告 temperature/top-p/seed 等采样参数。 |
| J9 | 重复与文本退化 | NA | — | 任务只比较答案选项 token 概率，不做开放式生成，重复退化不适用。 |
| J10 | 分词效应 | NA | — | 仅使用英语单脚本材料，无跨语言/跨脚本 token 数比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.2-3: materials are expert-curated from Floyd et al. (In prep) and linked to OSF; p.5 Table 2 lists model versions. | 测试材料为新编专家材料、版本来源较清楚，污染风险较低；但未报告训练截止日期对照或污染检测。 |
| J12 | 基准饱和 | NA | — | 所用任务分数总体未接近天花板，且论文没有在饱和基准上宣称显著提升；饱和问题不构成主要适用风险。 |
| J13 | 指令遵循 | NA | — | 因变量为语用解释选择，不是指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 输出为预定义答案选项 token，不要求 JSON/结构化文法约束输出。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 1 | p.1 Abstract asks whether pragmatic behaviors emerge without explicitly constructed mental-state representations; p.9 discusses two ToM-related hypotheses and cautions against extrapolation; p.5 Table 2 lists model families/versions. | 明确把 LLM 作为认知科学比较对象，讨论人类同名构念、ToM 关系、模型版本与人类同范式对照，并限制外推。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p.6 Figure 2 plots mean accuracy vs millions of parameters; p.6 notes 'stark jump in accuracy after 1B parameters' but 'model size does not fully explain variance'. | 报告了规模—准确率曲线，但仅用离散正确率、单次模型评估，未展示连续指标或多 seed 置信曲线来排除指标诱导的突变假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及 RL、奖励模型、benchmark 代理优化或 best-of-N 优化，无指标博弈/过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6 Figure 1 reports 95% CI; p.16 Appendix B Table 3 gives OpenAI API timestamps; p.5 lists model names/parameter counts. | 报告了区间估计、模型标识和 API 时间；但无精确 Huggingface revision、重复运行 N、配对检验或逐题日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评估，无多轮对话历史累积。 |

## 编码小结
研究对语用理解的多个现象做了细粒度、可复现的模型—人类对照，材料、提示与计分较透明；但多数实验设计/统计组件并非其核心，模型比较主要是描述性而非随机化因果实验，信效度、功效、随机效应与污染控制等报告不完整。
