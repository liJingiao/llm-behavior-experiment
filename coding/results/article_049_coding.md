# article_049 | Quantifying the Persona Effect in LLM Simulations | 2024

研究类型概述：LLM模拟与基准评估研究：先用混合效应回归估计persona变量对人类标注方差的解释力，再用零样本persona prompting在多个LLM上比较含/不含persona条件的预测表现，并分析样本类型与ANES调查案例。无人类被试随机分配，主要分析单位为LLM预测/标注实例，嵌套于文本或问题；模型规模与数据集为观察性比较因素。
- **研究构念（Construct）**：人设条件化的主观判断与人类标注模拟（persona-conditioned subjective judgment and simulation of human annotation behavior）｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：LLM模拟与基准评估研究：先用混合效应回归估计persona变量对人类标注方差的解释力，再用零样本persona prompting在多个LLM上比较含/不含persona条件的预测表现，并分析样本类型与ANES调查案例。无人类被试随机分配，主要分析单位为LLM预测/标注实例，嵌套于文本或问题；模型规模与数据集为观察性比较因素。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_5: 'We prompt the LLMs twice: once with persona variables, and once without'; PDF_PAGE_14 provides prompt templates. | 明确命名persona变量并给出with/without两水平及零样本提示程序，但未报告操纵检验或条件分配/顺序的随机化，故为0.5。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_5-6: metrics are R2, Cohen’s Kappa, MAE and macro F1; Table 2 reports them. | 因变量指标与计分方式明确，但未报告测量信效度证据，也未系统说明连续指标的预处理或天花板/地板控制，故为0.5。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_3: 'fitting a random intercept for each text'; PDF_PAGE_5: prompt twice with/without persona; PDF_PAGE_19 robustness checks. | 报告了文本随机截距、固定样本量与提示顺序/改写稳健性等控制，但未形成系统控制变量清单及逐一控制手段，故为0.5。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_3: mixed model separates persona effects from 'inherent variation of the text'; PDF_PAGE_4 discusses unexplained variance. | 识别并控制了文本样本身份这一主要混淆，并讨论未解释方差和未测persona因素；但未做敏感性分析或系统量化残余混淆威胁，故为0.5。 |
| A5 | 调节变量 | 0.5 | PDF_PAGE_6-7: samples stratified into entropy/SD categories; one-way ANOVA and Tukey tests compare improvement across categories. | 样本类型作为类别调节变量被界定并检验，且报告了两两比较；但无正式乘积项交互模型、中心化说明或效应量，故为0.5。 |
| A6 | 中介变量 | NA | — | 研究未提出或检验中介变量，无直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_14: full prompt templates for AnnwAttitudes, Kumar et al. (2021), EPIC, POPQUORN-P; PDF_PAGE_3 gives regression formula. | 关键构念persona提示、任务提示与评分指标均有可复现操作化描述，达到可重复执行程度。 |
| A8 | 水平数与类型 | 1 | PDF_PAGE_5: with persona versus without persona; PDF_PAGE_14 prompt templates show concrete levels. | persona条件为二分类水平，具体标签明确；二分类无水平间距/全距问题，且未涉及连续变量中心化。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_19 Table 6: five persona-order configurations and five paraphrase versions; PDF_PAGE_10 limitations discuss group-level versus individual persona limits. | 关键构念通过多种提示顺序/语义改写与多数据集评估获得会聚性稳健性证据，并在局限中讨论单一persona操作化的推广边界。 |
| A10 | 单一方法的风险 | 0 | PDF_PAGE_4 Table 1 uses persona variables and annotations from same annotators in RQ1; no common-method bias test is reported. | RQ1中persona变量与人类标注同源，RQ2中提示与模型输出也来自同一LLM流程，但全文未报告共同方法偏差的程序控制或统计检验，故为0。 |
| B1 | 被试间设计 | NA | — | 无人类被试间条件分配；同一模型/样本接受含与不含persona两种条件，不是独立被试组设计。 |
| B2 | 被试内设计 | 0.5 | PDF_PAGE_5: 'We prompt the LLMs twice: once with persona variables, and once without'. | 同一模型/样本接受两种提示条件，属于重复测量式比较；但未报告条件顺序处理或平衡方案，故为0.5。 |
| B3 | 混合设计 | NA | — | 研究不是组间/组内因素混合设计，未使用混合设计ANOVA或对应误差项。 |
| B4 | 因子设计 | 0.5 | PDF_PAGE_6 Table 2 crosses models with persona/no-persona conditions; PDF_PAGE_19 Table 6 reports order/paraphrase variants. | 存在模型×persona条件等多因素交叉比较，但无完整设计矩阵、无正式交互项ANOVA或效应量报告，故为0.5。 |
| B5 | 主效应 | 0.5 | PDF_PAGE_6 Table 2 reports per-model with/without persona and 'Avg. ∆' with bootstrap significance stars. | 报告了persona条件的主效应式汇总与显著性，但未报告F值、自由度或正式效应量，故为0.5。 |
| B6 | 交互作用 | 0.5 | PDF_PAGE_6-7: one-way ANOVA and Tukey tests show category differences in persona-prompting improvement. | 对样本类型差异做了ANOVA/Tukey检验，可视为调节/交互式比较；但无正式模型交互项、无误差棒或效应量，故为0.5。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无人类被试内条件顺序的拉丁方设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；无人类非随机分组及因果推断限定问题。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM提示条件为独立调用，无跨条件学习/迁移的实质风险，故不适用被试内适用条件论证。 |
| C1 | 随机化 | NA | — | 无人类或LLM单位被随机分配到互斥条件；同一实例接受两条件，不存在分配隐藏问题。 |
| C2 | 平衡 | 0 | PDF_PAGE_5: prompt twice 'once with persona variables, and once without'; no order-balancing scheme reported. | 存在含/不含persona的重复条件，但未报告顺序平衡方案；按固定/未说明顺序处理，故为0。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_13-14: model versions, 4-bit quantization, A100 hardware, API access; PDF_PAGE_9-10 discusses U.S./English external-validity limits. | 报告了模型版本、量化与硬件等恒定设置并讨论部分外部效度限制，但未系统列出温度、最大生成长度等所有恒定变量，故为0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | PDF_PAGE_3: mixed model includes random intercept for each text to control text-specific variability. | 文本身份以随机截距纳入分析，部分起到控制混淆作用；但未报告协变量斜率齐性检验或调整后效应量，故为0.5。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人类评分者需要盲法。 |
| C7 | 平衡的层级 | 0 | PDF_PAGE_5: condition order not described; no balancing level stated. | 存在重复条件但未报告完全平衡、拉丁方或ABBA等平衡层级，故为0。 |
| D1 | 练习效应 | NA | — | LLM每条件为独立提示调用，无上下文内练习或学习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类session或疲劳效应风险。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM条件独立调用，无跨条件药物/学习残留迁移问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性检验需求。 |
| D5 | 范围效应 | NA | — | 不是人类被试内绝对判断或量表校准任务；无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_19 Table 6: five persona-variable order configurations; PDF_PAGE_14 shows fixed multiple-choice option order A–E. | 对persona变量顺序做了稳健性变动，但未随机化/反平衡答案选项位置，也未报告位置效应，故为0.5。 |
| E2 | 默认赞同 | NA | — | 研究未使用Likert/态度自评量表作为被试测量，不涉及反向计分题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无跨群体等级量表反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或掩饰情节问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_6 Table 2 reports target R2 with SD; PDF_PAGE_8 Figure 3 plots predicted versus target R2. | 报告了部分均值/SD与R2分布范围，但未报告偏度、端点频率或pilot难度校准，故为0.5。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；主要评估LLM对既有标注的预测，故不适用共同方法偏差组件。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_5: bootstrap with 1,000 replications; PDF_PAGE_6 Table 2 reports R2, κ, MAE, F1 and significance stars. | 报告了效应量指标与bootstrap显著性，但无样本量功效依据、未系统报告95%CI、未说明多重比较校正，故为0.5。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_5: with/without persona prompt procedure; PDF_PAGE_19 robustness order/paraphrase checks. | 报告了提示条件操作与部分稳健性检验，但无随机分配、分配隐藏或基线等价性检验，内部效度威胁评估不完整，故为0.5。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_9-10: discusses group-level persona mismatch, within-group heterogeneity and simulation fidelity; PDF_PAGE_19 robustness. | 对构念对应关系与解释边界有讨论，并做提示改写稳健性；但无正式信度/效度统计或操纵检验，故为0.5。 |
| F4 | 外部效度 | 1 | PDF_PAGE_4 Table 1 lists dataset sources, annotator countries and sizes; PDF_PAGE_9-10 discusses U.S./English and cross-language generalization limits. | 报告了样本来源、国家/平台特征与明确推广边界，并通过多数据集与ANES案例提供一定跨情境比较，达到1。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_3: annotation ∼ persona variables + (1 &#124; text_id); PDF_PAGE_5: fixed-effect regression for prediction evaluation. | RQ1明确使用文本随机截距处理嵌套，RQ2分析层级与文本嵌套关系说明不足，故为0.5。 |
| G2 | 随机效应 | 0.5 | PDF_PAGE_3: random intercept for text; annotator random effect considered but omitted. | 报告了文本随机效应及省略annotator随机效应的理由，但未给出完整随机效应结构/随机斜率，故为0.5。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_3: text treated as random effect in RQ1; PDF_PAGE_5: fixed-effect regression in RQ2. | RQ1将文本视为来自更大总体的随机材料，RQ2未在预测评估中显式纳入材料随机效应，故为0.5。 |
| G4 | 统计功效 | 0.5 | PDF_PAGE_5: 'Due to cost constraints, we sample 600 instances'; Table 2 reports effect-size-like metrics but no power analysis. | 报告了效应量类指标，但无事前功效分析或基于效应的样本量推导，故为0.5。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_5: 600 instances per dataset due to cost; PDF_PAGE_7: filtering and random downsampling for ANES; PDF_PAGE_19 robustness. | 报告了样本量决定、部分排除/抽样规则与稳健性，但未明确区分验证性与探索性分析，也未完整披露所有分析自由度，故为0.5。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered report is mentioned in the paper. | 全文无预注册平台、编号或分析计划，且未区分预注册验证性与事后探索性分析，故为0。 |
| J1 | 位置偏差 | 0 | PDF_PAGE_14: multiple-choice options are fixed as (A)–(E); no candidate-position randomization or swap analysis reported. | 涉及LLM多项选择输出，但未对答案选项位置做反平衡/随机化，也未报告位置翻转率，故为0。 |
| J2 | 冗长偏差 | NA | — | 不使用LLM-as-judge评估开放式生成质量，无长度偏差问题。 |
| J3 | 谄媚 | NA | — | 无用户先验立场或反馈对话，不涉及谄媚/附和偏差。 |
| J4 | 自我偏好 | NA | — | 不是LLM-as-judge或成对模型输出评审，无自我偏好裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本persona prompting，不使用few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_14 provides full prompt templates; PDF_PAGE_19 Table 6 reports five semantic paraphrases and five orders. | 公布了完整模板并做顺序/语义改写稳健性检验，但未说明dev/test分离或prompt搜索/版本迭代过程，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文或RAG设置，不涉及中间迷失/信息位置效应。 |
| J8 | 温度与采样随机性 | 0 | PDF_PAGE_13-14: implementation details mention models, quantization and API, but no temperature/top-p/seed or repeated sampling N. | 未报告采样超参、随机种子或每条件重复生成次数；bootstrap仅用于指标不确定性，不替代LLM采样随机性，故为0。 |
| J9 | 重复与文本退化 | NA | — | 任务仅预测下一个选项token，不涉及开放式长文本生成或重复退化。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言评估，无跨语言/跨脚本分词比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_4 Table 1 lists public datasets, but no training-cutoff comparison or contamination detection is reported. | 使用公开人类标注数据集评估模型，但未报告测试集与模型训练截止日期的对照，也未做污染检测，故为0。 |
| J12 | 基准饱和 | 0.5 | PDF_PAGE_6 Table 2 and PDF_PAGE_8 Figure 3 report R2 ranges; most target R2 are low, and continuous R2 is used. | 报告了基准分数量程与当前水位，并使用连续R2而非硬准确率；但未系统讨论饱和/SOTA位置或CI比较，故为0.5。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，无约束指令遵循评估。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF_PAGE_5: multiple-choice format and 'predict only the next token'; PDF_PAGE_14 shows A–E options. | 报告了结构化多项选择输出设置，但未报告格式合法率、重试策略或格式失败与内容错误的分离，故为0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估或有害请求拒绝率。 |
| J16 | LLM 作为被试的范式定位 | 1 | PDF_PAGE_1-2 frames LLM persona simulation; PDF_PAGE_9-10 discusses group-level versus individual simulation limits; human annotations are used as comparison. | 明确将LLM输出定位于模拟人类标注而非直接等同于人类心理构念，报告模型版本并讨论构念差异与推广限制，达到1。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | PDF_PAGE_16 Table 4 and PDF_PAGE_17 Figure 4 compare 7b, 13b and 70b models across continuous R2 metrics. | 存在跨模型规模比较且使用连续R2，但未宣称涌现/突变，也未报告多seed/CI或机制证据；按规模比较记0.5。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及训练、RL、best-of-N或对代理指标的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_5 uses 1,000 bootstrap replications; PDF_PAGE_6 names GPT-4-0613, GPT-3.5-Turbo-0613 and Llama/Tulu versions. | 报告了模型snapshot名称与bootstrap，但未报告LLM重复采样N、95%CI、配对检验或原始推理日志，故为0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示，无多轮对话历史累积或一致性衰减问题。 |

## 编码小结
研究提供了较完整的prompt模板、模型版本与多数据集评估，并报告了bootstrap显著性、稳健性顺序/改写检验和构念限制讨论。但作为LLM模拟评估，缺少persona条件顺序平衡、采样超参与重复生成报告、答案选项位置控制、污染检查与正式功效分析；多数人类实验设计组件不适用。整体证据支持其描述性与比较性结论，但若干LLM评估风险报告不足。
