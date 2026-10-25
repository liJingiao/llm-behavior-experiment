# article_034 | EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas | 2024

研究类型概述：该文提出 EAI 框架，用情感提示操纵多个 LLM，在伦理基准、议价游戏、重复博弈和公共物品游戏中评估情感对 LLM 决策、合作与伦理判断的影响；主要分析单位是模型在各条件/回合下的行为输出，属于 LLM-as-participant/基准与多智能体模拟式评估，而非人类被试实验。
- **研究构念（Construct）**：情绪依赖的道德判断、合作与策略选择（emotion-dependent moral judgment, cooperation, and strategic choice）｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：该文提出 EAI 框架，用情感提示操纵多个 LLM，在伦理基准、议价游戏、重复博弈和公共物品游戏中评估情感对 LLM 决策、合作与伦理判断的影响；主要分析单位是模型在各条件/回合下的行为输出，属于 LLM-as-participant/基准与多智能体模拟式评估，而非人类被试实验。｜CA 任务锚定：囚徒困境（prisoner's dilemma (PD), `tsk_KRl3zbyaJcKWM`）；道德困境任务（Moral Dilemma Task, `trm_57ebe6583f52d`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p5: 'We focus on five basic emotions: anger, sadness, happiness, disgust, and fear' and 'three strategies for emotional prompting'; p24-28 prompt templates include {emotion}. | 自变量（情绪及提示策略）被命名并给出水平/程序，但未见水平分配方式说明，也未做操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | PDF p5: 'accuracy (Acc)' and Right-to-Avoid; p7: 'proposal share' and 'acceptance rate'; p8: cooperation rate and percentage of maximum possible reward. | 主要因变量指标与计分口径有定义，但未报告信度/效度证据、连续指标预处理或天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | PDF p5: 'We fixed model versions ... and set the temperature to 0'; p4: 'deliberately minimize the contextual information ... avoid setting any specific personality traits'. | 报告了固定模型版本、温度及弱化人格上下文等控制，但未系统列出控制变量清单及各自控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF p10: 'model size, open-source versus proprietary status ... primary pretraining language ... collectively shape' behavior; p1 abstract likewise. | 识别了模型规模、对齐方式、预训练语言等可能混淆/影响因素，但未说明控制方式，也未报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | 0 | PDF p1: emotional biases are 'influenced by model size, alignment strategies, and primary pretraining language'; p10 repeats this claim. | 存在调节性表述，但分析仅为描述性分组比较，未报告正式交互检验或简单斜率，故未满足基本要件。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或中介效应分析，故不适用。 |
| A7 | 操作性定义 | 1 | PDF p24-28 给出 Dictator、Ultimatum、Prisoner’s Dilemma、Battle of the Sexes、Public Goods 的完整 prompt 模板；p5/p7/p8 给出主要指标定义。 | 关键自变量操纵以完整 prompt 呈现，因变量指标与计分口径可据文复现，达到操作性定义要求。 |
| A8 | 水平数与类型 | 0.5 | PDF p5: five emotions and three prompting strategies; p7: five languages; p17: exact model versions. | 水平数与各水平标签有报告，但未系统说明水平类型（名义/等级/连续）、间距与全距。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p5: 'Simple', 'Co-player-based', and 'External-based' strategies; p22 Table 4 reports results by strategy superscripts. | 以三种情感提示策略作为多种操作化尝试，但未报告会聚证据，也未在局限中讨论单一或少量操作化对推广的限制。 |
| A10 | 单一方法的风险 | NA | — | 没有人类自评式同源测量；自变量为研究者控制的 prompt，因变量为模型行为/基准输出，传统共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类或独立 LLM 被试分配到互斥条件；模型之间是比较对象而非随机分组被试，故被试间设计不适用。 |
| B2 | 被试内设计 | 0 | PDF p5/p19: 同一批模型在多种情绪条件下评估，并重复五次运行；未报告情绪条件呈现顺序、平衡方案或重复测量统计模型。 | 同一模型跨情绪条件重复出现，但未说明顺序处理/平衡，且分析未按重复测量建模。 |
| B3 | 混合设计 | 0 | PDF p5/p17: 同时比较模型、情绪、游戏、语言等；未逐因素标注组间/组内属性，也未使用混合模型或分别报告误差项。 | 存在模型间比较与情绪内比较的混合结构，但论文未按混合设计报告或分析。 |
| B4 | 因子设计 | 0 | PDF p8 Table 1 and p22 Table 4 present descriptive results; no full factorial design matrix, cell sample sizes, ANOVA table, or interaction statistics. | 多因素比较存在，但未报告因素完全交叉设计、每格样本量或交互检验，不能算完整因子设计。 |
| B5 | 主效应 | 0 | PDF p6-p9 mainly report figures/tables and verbal descriptions of emotion effects; no F/df/p/effect size for main effects. | 未报告正式主效应统计检验；只有描述性比较。 |
| B6 | 交互作用 | 0 | PDF p6-p9: emotion effects are described verbally and graphically; no interaction F/df/p/effect size or simple-effects tests. | 未报告正式交互作用检验；不能仅凭描述和图形断言交互。 |
| B7 | 区组设计 | NA | — | 没有区组或分层随机设计，故不适用。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方顺序设计，故不适用。 |
| B9 | 准实验设计 | NA | — | 没有人类准实验分组；情绪提示为研究者控制的 prompt 操纵，模型比较为观察性比较但未作为准实验设计报告。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有需要论证处理可逆性/迁移对称性的人类被试内设计；LLM 条件以独立 prompt 会话为主。 |
| C1 | 随机化 | 0 | PDF p5/p17: 固定模型版本与 temperature=0，但全文未报告随机分配方法、随机数工具或分配隐藏。 | 多条件实验未报告任何随机化分配机制。 |
| C2 | 平衡 | 0 | PDF p19: 统一超参数并重复五次；未报告各情绪/策略/语言条件的呈现顺序平衡方案。 | 条件顺序平衡未报告，无法判断是否存在顺序偏差。 |
| C3 | 恒定 | 0.5 | PDF p5: fixed model versions and temperature=0; p4: minimal contextual information and no personality traits. | 列出并固定了部分变量，但未系统列出全部恒定变量及其水平，也未讨论对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配程序，故不适用。 |
| C5 | 纳入为变量 | 0 | PDF p10: model size, alignment, and pretraining language are discussed as influencing factors; no covariate/ANCOVA or model-based adjustment is reported. | 已知的模型/语言差异未被作为协变量或区组纳入分析，也未检验相关假设。 |
| C6 | 盲法 | NA | — | 数据采集为自动化 API 调用，无人类被试或人类评分者盲法问题。 |
| C7 | 平衡的层级 | 0 | PDF p19: five repeated runs for stability; no balancing level, Latin square/ABBA construction, or order-effect assumptions are reported. | 未说明平衡层级及顺序效应形状假设。 |
| D1 | 练习效应 | 0 | PDF p5: repeated games use 'iterative memory update'; p9: later-stage behavior is mentioned, but no practice block, round-position covariate, or early-trial removal rule is reported. | 重复游戏存在跨回合学习/适应风险，但未报告练习或轮次位置控制。 |
| D2 | 疲劳效应 | NA | — | LLM 不涉及人类式疲劳；任务虽多轮，但并非人类被试 session 疲劳设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 情绪条件以独立 prompt 运行，未涉及人类跨条件残留或洗脱期；重复游戏内记忆是设计的一部分。 |
| D4 | 不对称迁移 | NA | — | 没有人类被试内跨条件迁移或顺序设计，故不适用。 |
| D5 | 范围效应 | NA | — | 因变量为博弈行为、准确率等客观/半客观指标，不使用主观量表校准。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF p24-28: 输出格式固定为数字、字母或 ACCEPT/REJECT；未报告选项顺序随机化、刺激顺序反平衡或各位置出现次数。 | 存在多选/固定格式选择，但未见任何位置或顺序控制。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，故默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表或跨群体反应风格比较，故不适用。 |
| E4 | 需求特征 | NA | — | LLM 无人类被试需求特征；未涉及人类 cover story 或事后访谈。 |
| E5 | 实验者效应 | NA | — | 完全自动化 API 数据采集，无人类主试/评分者。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p20 Table 2 reports mean and std across five runs; e.g., Responder anger accept rate near 0.001. No skew, endpoint frequency, or pilot difficulty calibration is reported. | 报告了均值/SD，可部分排查端点，但未报告偏度、端点频率或难度校准，且明显地板效应未被讨论。 |
| E7 | 共同方法偏差 | NA | — | 没有人类自评式多构念同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | PDF p8/p20/p22: 主要报告描述性均值、方向箭头和部分 std；未报告主要比较的效应量、95%CI、样本量依据或多重性校正。 | 不满足报告效应量或置信区间的基本要件。 |
| F2 | 内部效度 | 0 | PDF p5/p17: 固定模型版本与温度；未报告随机分配、分配隐藏、基线等价性、被试流向或损耗处理。 | 虽为 prompt 操纵，但内部效度威胁评估不足。 |
| F3 | 构念效度 | 0 | PDF p5/p7: 使用已有 benchmark 和人类基线；未报告测量信度、效度证据或情感操纵检验。 | 未提供关键测量的信效度与操纵检验，不能仅凭使用已有 benchmark 视为完整构念效度证据。 |
| F4 | 外部效度 | 0.5 | PDF p17: exact model versions listed; p7: five languages; p10 Limitations discuss future multi-agent/human experiments and small scale. | 样本来源与模型版本有报告，并提及部分边界，但未系统讨论代表性、推广边界或跨情境复现。 |
| G1 | 分析单位 | 0 | PDF p6-p9/p20: 结果按模型/条件聚合为均值；未明确说明处理分配层级、分析层级或响应嵌套于模型/会话的结构。 | 存在响应嵌套于模型与任务的结构，但分析单位与嵌套处理未说明。 |
| G2 | 随机效应 | 0 | PDF p5/p10: models are compared as fixed categories; no mixed model or random-effects structure is reported. | 未说明哪些因子为随机效应，且将模型当作固定比较对象后仍泛称 LLM 行为。 |
| G3 | 材料作为随机效应 | 0 | PDF p5: 使用 ETHICS、MoralChoice、StereoSet 等固定项目/任务；分析只做模型/条件比较，未将项目作为随机效应或报告 F1/F2/准F。 | 有限基准项目被当作固定材料，未建模项目总体推广。 |
| G4 | 统计功效 | 0 | PDF p19/p20: five repeated runs reported for stability, but no a priori power analysis, expected effect size, or effect-size/CI reporting. | 没有设计阶段功效分析，也没有主要效应的效应量/CI。 |
| G5 | 研究者自由度 | 0 | PDF p19: five runs for robustness; no exclusion rules, sample-size stopping rule, or confirmatory/exploratory distinction. Multiple DVs appear but not as a complete pre-specified set. | 数据排除规则、样本量决定方式及验证性/探索性区分均未报告。 |
| G6 | 预先设定 / 预注册 | 0 | PDF p33 NeurIPS checklist: no preregistration link or pre-data analysis plan; only code/data availability. | 未见公开预注册或注册分析计划。 |
| J1 | 位置偏差 | 0 | PDF p24-28: fixed answer formats; p5 ethical tasks involve categories, but no candidate-order counterbalancing, swap rejudging, or position×correctness analysis is reported. | 多候选项/选项顺序偏差未识别或控制。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放生成质量，故长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 没有用户立场、反馈或多轮纠错式谄媚评估，故不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 裁判/成对比较，故自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本情绪/游戏 prompt，不使用 few-shot 示例，故不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p24-28: 完整 prompt 模板公开；p5: 三种情感提示策略；p19/p31-32: 温度消融。未报告 prompt 版本日期、语义等价敏感性消融或 dev/test 划分。 | 模板与部分消融有报告，但提示工程控制不完整。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短游戏/伦理描述，远低于长上下文或 RAG 设置，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p5: fixed model versions and temperature=0; p19: five repeated runs and temperature values 0.2-1.0; p20 Table 2 mean/std. No seed, top-p/top-k, or CIs for all conditions. | 报告了温度和部分重复运行，但采样超参、种子、所有条件重复次数与CI不足。 |
| J9 | 重复与文本退化 | 0 | PDF p5/p24-28: 指定输出格式并设 temperature=0；未报告 greedy/beam/sampling、repetition penalty、重复率/退化率或截断比例。 | 解码策略与文本退化控制未报告。 |
| J10 | 分词效应 | 0 | PDF p7: experiments in English, German, Russian, Chinese, and Arabic; no tokenizer name/revision or token-count control/ratio is reported. | 跨语言比较未控制分词长度差异。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p5: uses ETHICS, MoralChoice, StereoSet, TrustLLM; no benchmark version/date vs training cutoff or contamination check is reported. | 公开基准污染风险未评估。 |
| J12 | 基准饱和 | 0 | PDF p6-p9: reports benchmark/accuracy or game metrics descriptively; no score range, SOTA position, saturation discussion, or CI comparison. | 未评估基准饱和或改用连续指标。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，故指令遵循测量不适用；输出格式问题归入J14。 |
| J14 | 输出格式约束 / 结构化输出 | 0 | PDF p24-28: prompts require exact integer, letter, ACCEPT/REJECT, or JSON formats; no format legality rate, retry strategy, or separation of format failure from content error is reported. | 结构化输出约束存在，但合法率与处理策略未报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估，故不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p5: injects Ekman basic emotions; p7: compares LLM behavior with human game experiments; p10 claims 'emergent emotional understanding' and alignment. No systematic construct-validity comparison or human same-paradigm experiment is reported. | 将 LLM 情感行为与人类同名构念对照，但未充分论证构念异同，外推较直接。 |
| J17 | 涌现能力争议与指标诱导假象 | 0 | PDF p10: claims smaller/mid-sized models 'exhibit emergent emotional understanding'; no model-scale curve, continuous metric, or multi-seed emergence test is reported. | 出现涌现式表述，但缺少连续指标/规模曲线检验。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 纯评估，不涉及以代理指标为目标的训练、RL 或 best-of-N 优化，故不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p17: exact model version strings; p19-p20: five repeated runs and mean/std for GPT-3.5 robustness. No CIs, paired tests, or raw logs for all scores are reported. | 有模型 snapshot 与部分重复稳定性，但可复现性信息不完整。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF p5: repeated games include iterative memory update; p9: behavior 'predominantly in the latter stages' is mentioned. No per-round independent/cumulative scoring or context-truncation details are reported. | 进行了多轮重复游戏评估，但未系统按轮次拆分或报告上下文截断。 |

## 编码小结
论文明确操纵情感提示（五种基本情绪及中性）与情感提示策略，并在多模型、多语言、多游戏任务上报告描述性指标；模型版本和温度有一定控制，并提供提示模板、五轮重复稳定性与温度消融。但统计推断薄弱：主分析缺少正式交互/主效应检验、效应量与置信区间、随机化/顺序平衡、信效度与操纵检验；多项 LLM 评估特有风险（位置偏差、格式合法率、污染、分词、随机性等）未报告或仅部分报告。
