# article_124 | Large Language Models Often Say One Thing and Do Another | 2025

研究类型概述：LLM 行为基准评测与训练干预研究：构建 WDCT，用成对的 word/deed 多选题测量 12 个 LLM 的陈述—行动一致性；比较 Direct vs CoT、不同领域与模型，并进行 word/deed 分离对齐（SFT/DPO）和数据增强实验。分析单位为模型—题目/条件的响应，非人类被试实验。
- **研究构念（Construct）**：陈述—行动一致性、价值—行为一致性、信念强度与跨情境泛化｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）；态度（attitude, `trm_4a3fd79d09947`）
- **实验任务与范式（Task / Paradigm）**：限定为WDCT直接评估单元：对现成base/instruct checkpoints分别提出配对的意见/价值/理论“word”问题与具体情境行动“deed”问题，并比较两者选择与概率分布；论文另行实施的SFT/DPO定向alignment实验不作为纳入依据。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5 §3.2.1: 'two distinct experimental conditions: Direct Prompting and CoT Prompting'; p.14 Table 6 prompts; p.8 §4.2.1: separate word/deed alignment; p.10–11 §4.3.2: Non-Aug/Para-Aug/Dual-Aug; p.6 §3.3 training details. | 明确命名并描述了多个操纵变量及水平/程序，但未统一报告分配到条件的程序，且缺乏正式的操纵检验结果，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.5 eq.(1)-(2): CS and PCS formulas; 'parsed into the selected option using regular expressions'; p.6 Table 3 means; p.4 validation of questions. | 因变量指标与计分方式明确，但未报告信度、效度证据，也未说明连续指标预处理或天花板/地板效应处理。 |
| A3 | 控制变量 | 0.5 | p.11: 'adjusted the temperature parameter to 0'; p.6 Table 3 note: 'three runs... randomly shuffled options A and B'; p.17: 3-shot demos averaged over three evaluations; p.16 fixed model versions. | 报告了温度、模型版本、重复评估、选项随机化等部分控制手段，但没有系统列出控制变量清单并逐一说明控制方式。 |
| A4 | 混淆变量 | 0.5 | p.1 abstract: 'critical analyses ... temperature settings, specific situations, and the phrasing of questions'; p.9–12 robustness checks on situations and paraphrased prompts; p.11 temperature. | 识别并用稳健性检查处理了多种潜在混淆，但未正式报告残余混淆或敏感性分析对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 理论模型没有明确的调节变量和乘积项交互检验；模型、领域、训练状态等比较均为描述性分组或稳健性展示，未做 simple slopes，故不适用。 |
| A6 | 中介变量 | NA | — | 没有中介变量假设，也没有直接/间接效应分解或 a/b 路径分析，故不适用。 |
| A7 | 操作性定义 | 1 | p.3 §2.1: each item contains paired word question and deed question; p.4 §2.3 construction pipeline; p.5 eq.(1)-(2) CS/PCS operationalization; p.5 §3.2.2 parsing and scoring. | 对 words/deeds、CS/PCS、对齐训练的直接/间接变化率等关键构念给出了可观测、可重复的操作化程序，达到 1。 |
| A8 | 水平数与类型 | 0.5 | p.5: Direct vs CoT two levels; p.8: separate word/deed alignment; p.10–11: three augmentation settings; p.6 Table 3 four domains. | 报告了主要自变量的水平数与标签，但未系统给出所有变量的水平类型、间距/全距或连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.5–6: CS and PCS as two indicators; p.9 Fig. 6 three different situations; p.11–12 Fig. 7 paraphrased prompts. | 使用了多个指标/情境来支持同一结论，但未报告指标间的正式会聚证据（如相关或一致性检验），也未讨论单一操作化局限。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是人类自陈式多构念测量；word 与 deed 均为 LLM 输出且同源是该研究现象本身，传统共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试的组间随机分配；模型比较为观察性，prompt 条件在同一模型内评估，训练运行也未按“被试间”逻辑报告样本分配。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内顺序设计或跨条件 carryover；LLM 题目/条件为独立调用，训练 epoch 的顺序属于训练流程而非被试顺序平衡。 |
| B3 | 混合设计 | NA | — | 没有正式的组间×组内混合设计及对应误差项；模型/领域/条件是描述性交叉比较。 |
| B4 | 因子设计 | NA | — | 没有正式因子设计、完整设计矩阵、每格样本量和 ANOVA 交互项；Table 3 是描述性交叉汇总，不是因子实验分析。 |
| B5 | 主效应 | NA | — | 没有报告正式主效应统计量（F、df、p、效应量），故不属于因子设计主效应分析。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验或简单主效应分析；跨模型/领域差异仅为描述性比较。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层变量及区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或被试内条件顺序安排。 |
| B9 | 准实验设计 | NA | — | 不是非随机人类准实验；训练干预使用固定基座模型和独立训练运行，未按准实验类型报告选择偏差与因果推断局限。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理的不可逆性或迁移对称性论证；LLM 独立调用无跨条件残留问题。 |
| C1 | 随机化 | NA | — | 没有对实验条件单位进行随机分配的随机化程序或分配隐藏；选项随机化属于 E1/J1，不是条件分配随机化。 |
| C2 | 平衡 | NA | — | 没有条件顺序平衡方案或各顺序被试分配，因为 LLM 条件调用相互独立且无顺序效应设计。 |
| C3 | 恒定 | 0.5 | p.11: 'adjusted the temperature parameter to 0'; p.6 training hyperparameters and Alpaca mixing ratio; p.16 Table 5 model versions; p.17 3-shot demonstration setup. | 列出并固定了温度、模型版本、部分训练/提示超参数，但没有在讨论中系统说明这些恒定设置造成的外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计、匹配变量或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未把已知混淆变量作为区组或协变量纳入模型；模型、领域、训练状态是实质性比较变量而非协变量控制。 |
| C6 | 盲法 | NA | — | 主要因变量为自动化解析的 LLM 选项，无人类评分者参与结果评分；人工检查仅用于数据构建，不构成绩效评分盲法问题。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 等顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 题目独立作答，无人类练习块或初期练习效应；训练 epoch 是刻意操纵，不是被试练习效应控制。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长、休息间隔或疲劳效应；LLM 不适用疲劳控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | word/deed 对齐使用分离模型，题目独立调用，无交叉设计清洗期；跨方面影响是研究结果而非顺序 carryover。 |
| D4 | 不对称迁移 | NA | — | 没有被试内顺序条件的迁移对称性检验；word/deed 对齐效应比较不是同一单位跨条件顺序的迁移。 |
| D5 | 范围效应 | NA | — | 没有主观量表或绝对判断量表校准问题；CS/PCS 为客观一致性指标。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.6 Table 3 note: 'randomly shuffled options A and B to mitigate any biases associated with their order'; p.6 also reports three runs. | 报告了选项随机化，但未报告平衡方案类型、各位置出现次数、被试/运行分配或位置×正确率细节。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，而是多选题选项；默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表分数分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 主要对象为 LLM，无人类被试需求特征或事后访谈；LLM prompt 敏感性另由 J6 处理。 |
| E5 | 实验者效应 | NA | — | 数据采集与主要评分完全自动化，无人类主试或结果评分者；人工数据检查不涉及实验者期望传递。 |
| E6 | 天花板 / 地板效应 | 0 | p.6 Table 3 reports only CS means; p.23 Table 8 reports PCS means; no SD, skewness, or endpoint frequencies are reported. | 只报告均值，未报告分布形态或端点频率；PCS 接近 0.9–0.97 的高位也未被作为天花板问题讨论。 |
| E7 | 共同方法偏差 | NA | — | 不是人类自陈式多构念测量；word/deed 均由 LLM 生成，共同方法偏差的人类问卷框架不适用。 |
| F1 | 统计结论效度 | 0 | p.6 Table 3 only reports mean consistency scores; p.16 Table 7 reports subset-vs-fullset p-values; no effect sizes, confidence intervals, power analysis, or multiple-comparison correction for main analyses. | 主要分析缺少效应量与置信区间，未报告样本量功效依据和多重性校正，故为 0。 |
| F2 | 内部效度 | 0.5 | p.6 §3.3 reports SFT/DPO training details; p.10: 'repeated the alignment experiment three times'; p.9–12 robustness checks for temperature, situations, phrasing. | 报告了训练程序、重复运行和部分稳健性检查，但没有随机分配、分配隐藏、基线等价性检验或被试/运行流向；内部效度威胁讨论不完整。 |
| F3 | 构念效度 | 0.5 | p.4–5: GPT-4 generated deed questions then two NLP graduate students manually reviewed; p.5: theory questions double-checked by two Finance graduate students; p.5–6: CS/PCS metrics. | 有一定内容/人工校验证据，但未报告评分者间信度、正式效度指标或操纵检验，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.5 §3.1 lists 12 LLMs; p.16 Table 5 gives versions; p.4 §2.3.1 lists dataset sources and topic counts; p.9–12 tests multiple situations/prompts. | 报告了模型与题目来源及部分跨情境稳健性，但没有明确抽样框/代表性、纳入排除标准或外部效度边界条件。 |
| G1 | 分析单位 | 0.5 | p.5 eq.(1): CS is computed over paired items (Qw,Qd) in dataset D; p.6 Table 3 aggregates by model and domain. | 说明了题目层面的指标与模型/领域层面的汇总，但没有显式处理题目嵌套于领域、响应嵌套于模型/项目的多层结构，故为 0.5。 |
| G2 | 随机效应 | 0 | p.6 Table 3 reports model/domain means only; p.5–6 no mixed model, random effect structure, or explicit fixed/random factor specification is reported. | 存在同一模型重复评估多个题目/领域的结构，但模型被当作固定描述组，未报告随机效应；适用于需要推广到模型/项目总体时，此缺失记 0。 |
| G3 | 材料作为随机效应 | 0.5 | p.4 §2.3.1 samples topics from larger debate/value/moral/textbook sources; p.5 Table 2 reports 1225 items; p.16 B.1 samples subsets to test stability. | 材料/题目明确来自更大来源并做了子集稳定性分析，但分析中未将题目作为随机效应或报告混合模型，故为 0.5。 |
| G4 | 统计功效 | 0.5 | p.16 B.1: subset sampling at various ratios, 'no statistically significant differences (p > 0.05)'; p.6 Table 3 reports means but no effect sizes or CIs. | 提供了事后样本量/子集稳定性论证，但没有设计阶段功效分析、预期效应量来源或效应量置信区间，故为 0.5。 |
| G5 | 研究者自由度 | 0.5 | p.5–6 lists models, domains, CS/PCS; p.8 and p.10–11 list alignment and augmentation conditions; p.6 selects best-performing learning rates; p.16 adds subset analyses. | 报告了较多条件与指标，但没有数据排除规则、样本量停止规则、全部探索性分析或验证性/探索性区分；学习率按表现选择也增加研究者自由度。 |
| G6 | 预先设定 / 预注册 | 0 | p.1: 'Dataset and code are available at https://github.com/...'; no preregistration platform, registration number, or time-stamped analysis plan is reported. | 没有预注册；按编码口径，适用的预注册缺失记 0，而非 NR。 |
| J1 | 位置偏差 | 0.5 | p.6 Table 3 note: 'randomly shuffled options A and B to mitigate any biases associated with their order'; p.16 Table 5 model versions; p.11 temperature=0. | 报告了 A/B 位置随机化，但未报告交换前后偏好翻转率、各位置正确率或人类评分者间信度，故为 0.5。 |
| J2 | 冗长偏差 | NA | — | 评估不是 LLM-as-judge 或开放性生成质量评分，而是正则解析多选题选项；长度作为质量偏差的裁判风险不适用。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错框架下的谄媚操纵；题目为无用户立场的多选题。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 进行模型输出评分或成对比较，故不存在裁判自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.17 A.2: 'we use a 3-shot CoT ... Demonstrations ... randomly sampled from a manually constructed set of 50. The reported ... average of three evaluations'; p.14 Table 6 shows one demonstration template. | 报告了 few-shot 数量、来源和重复三次平均，但未报告每类示例比例、完整示例集、排列反平衡或多 seed 的标准差，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.14 Table 6 provides Direct/CoT prompt templates; p.12 Fig. 7 reports paraphrase robustness across five rephrasings; p.17 describes 3-shot sampling. | 提供了 prompt 模板并做了措辞敏感性检查，但未报告版本号/迭代日期、完整示例集、dev/test 划分或 prompt 搜索过程，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验上下文为短题目/多选题，不是长上下文或 RAG 设置，无需位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0.5 | p.11: 'temperature parameter to 0'; p.6: three runs averaged; p.16 Table 5 exact model versions; p.11 Fig. 5 varies temperature. | 报告了 temperature 和三次重复/版本，但未报告 top-p、top-k、seed、最大生成长度或重复采样的置信区间，故为 0.5。 |
| J9 | 重复与文本退化 | NA | — | 最终输出为单个选项，CoT 解释不用于评估文本退化；没有开放生成质量比较，故重复/退化 QC 不适用。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文数据集，无跨语言/跨脚本比较，分词效应不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4 §2.3.1 uses public Argument Annotated Essays, Recorded Debating, World Values Survey, Moral Stories, and Mankiw textbook; p.16 gives model versions but no training cutoff. | 使用可能进入预训练语料的公开来源，但未报告训练截止日期、污染检测或 held-out/私有集；未识别污染风险，故为 0。 |
| J12 | 基准饱和 | NA | — | WDCT 为新构建基准，主要 CS 约 0.49–0.76、随机基线 0.5，远未接近 1；PCS 虽高但未被用于宣称饱和提升，故不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；虽然要求输出选项，但未把否定/数量/格式/风格约束的遵守率作为测量对象。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.14 Table 6 prompt: 'Answer ... with only one single option number'; p.5 §3.2.2: free-form response parsed 'using regular expressions'. | 报告了格式约束和解析方式，但未报告格式合法率、重试策略或把格式失败与内容错误分开，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全对齐、有害请求或越狱攻击评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2: 'word' refers to stated opinions, values, or beliefs; 'deed' refers to actions in specific situations; p.7 discusses 'lack of strong beliefs' and underlying knowledge. | 对 LLM 的 words/deeds 构念有操作化定义，但未系统讨论其与人类同名心理学构念的异同，也无人类对照实验；按 LLM 行为研究适用时记 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有报告随模型规模/训练进展的能力曲线，也没有“涌现/突变”宣称；只是比较若干固定模型。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不是对代理指标/奖励模型/LLM-judge 的优化过程；SFT/DPO 对齐用于检验跨方面泛化，未做 proxy-vs-gold overoptimization 曲线。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6: results averaged over three runs; p.16 Table 5 exact model/API versions; p.16 Table 7 reports subset-vs-fullset t-tests. | 报告了重复运行和精确模型版本，但无置信区间、逐题结果/配对检验或推理日志发布，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮多选题/单轮 CoT，无多轮对话历史累积，故不适用。 |

## 编码小结
论文清楚定义了 words/deeds 的操作化、CS/PCS 指标、数据集构建和多种稳健性检查，并报告了模型版本与主要结果。但核心比较主要是描述性均值，缺少随机效应/项目层面方差建模、效应量与置信区间、预注册、污染检查、位置翻转率、格式合法率等；许多人类实验设计组件不适用于该 LLM 基准。
