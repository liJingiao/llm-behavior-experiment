# article_228 | Trans-EnV: A Framework for Evaluating the Linguistic Robustness of LLMs Against English Varieties | 2025

研究类型概述：该文提出并验证一个将标准美式英语（SAE）基准自动转换为多种英语变体的框架，并在6个QA基准、38个英语变体（18种方言+20种ESL变体）和7个LLM上进行基准评测。主要分析单位是基准题项/模型输出，汇总到数据集×变体×模型层面；另用3名人类标注者验证转换质量，并含开放式任务与LLM-as-judge评估。
- **研究构念（Construct）**：英语变体加工、语言距离敏感性与方言公平差异｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：把六个文本benchmark确定性转换为38种英语方言和ESL变体，让七个现成LLM完成原始与变体版本，并按语言特征和语言距离分析表现变化。（操纵英语变体、方言/ESL类型、CEFR水平、句长、语言距离、任务和模型，并与SAE原始版本比较。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4–5: 报告18种方言、CEFR A/B与10种L1构成20种ESL变体；p5: “we randomly shuffle features in Lvi and apply them sequentially”；p6: human evaluation验证转换。 | 自变量“英语变体/原SAE vs 变体”被明确命名并给出多水平及转换程序、部分操纵检验；但未明确说明分析单位如何分配到水平（同一题项同被转换为多变体、独立评测），故为0.5。 |
| A2 | 因变量 | 0.5 | p7: “Tables 4 and 5 report model performances… Orig. denotes the original SAE dataset”；p9: IFEval用指令遵循准确率、AlpacaFarm用win rate、MT-Bench用0–10分；p26: 最大生成2048 tokens并解析“The answer is”。 | 因变量指标与计分方式明确；但未报告基准测量的信效度、连续指标预处理或天花板/地板控制，故为0.5。 |
| A3 | 控制变量 | 0.5 | p26: “maximum number of generated tokens to 2048 and conducted all experiments in a zero-shot setting. The system prompt used was…”；p7脚注列出模型版本；p22: guideline generation用temperature 0.8、top-p 0.95。 | 报告了若干固定控制（zero-shot、最大长度、系统提示、模型版本、转换模型），但未系统列出全部控制变量及控制手段，故为0.5。 |
| A4 | 混淆变量 | 0.5 | p8: 将变体表现差异部分归因于预训练语料可得性，并报告mC4/OSCAR比例；p8–9: 按词数/句数四分位分析sentence length与performance gap；p9: 讨论语义保持与转换限制。 | 识别并探索了长度、预训练数据可得性、转换质量等潜在混淆，但未在模型中正式控制或报告残余混淆敏感性分析，故为0.5。 |
| A5 | 调节变量 | NA | p8仅描述性比较“reasoning-based QA”与“knowledge-based QA”的下降幅度，并称“suggesting that reasoning ability may support robustness”；无正式交互模型。 | 论文没有提出并检验正式调节假设（无variety×task/model交互检验、无简单斜率），理论模型不包含调节变量，故NA。 |
| A6 | 中介变量 | NA | — | 全文无中介变量、直接/间接效应分解或因果链中介假设，故NA。 |
| A7 | 操作性定义 | 1 | p4–5详述eWAVE/CEFR/L1特征抽取、guideline生成、feature transformer与semantic checker的逐步转换；p6给出人工评价Q1/Q2；p26给出QA评测提示与解析规则。 | 关键构念（变体转换、模型表现）均有可复现的操作化程序、计分与评测流程，故为1。 |
| A8 | 水平数与类型 | 0.5 | p4: 18 dialects；p4–5: CEFR A/B与10种L1组成ESL变体；p7: 38 varieties；p9: L1 difficulty categories 1–4。 | 报告了水平数与各水平标签，且区分方言/ESL、CEFR、L1分类；但未系统说明水平类型、间距/全距或连续变量中心化，故为0.5。 |
| A9 | 单一操作化的风险 | 1 | p6–7: human evaluation（多个feature transformer、Q1/Q2、valid rate、S的precision/recall/F1）；p9: IFEval、AlpacaFarm、MT-Bench开放式任务；p7–10: 六个closed-form基准、七个模型。 | 关键构念采用多基准、多任务、多模型与人工验证的多种操作化，并报告会聚性证据，故为1。 |
| A10 | 单一方法的风险 | NA | — | 自变量是转换后的文本变体，因变量是LLM在基准上的客观准确率/分数，非自陈同源测量；无共同方法偏差检验需求，故NA。 |
| B1 | 被试间设计 | NA | — | 无人类被试组间分配；同一基准题项被转换为多个变体并由各模型分别评测，不存在独立被试组承担条件，故NA。 |
| B2 | 被试内设计 | NA | — | 虽同一题项在多个变体上被重复评测，但各评测为独立提示，无被试内呈现顺序或顺序平衡问题；人类被试内设计不适用，故NA。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合的人类实验设计，故NA。 |
| B4 | 因子设计 | 0 | p7–10 Tables 4–6展示model×dataset×variety的多因素结果网格；但全文无factor design的ANOVA表、主效应/交互统计量。 | 多因素交叉网格存在，但未报告因子设计所要求的交互项统计检验与完整ANOVA，故为0。 |
| B5 | 主效应 | 0 | p7–10仅报告各模型/数据集/变体的均值或百分比，并比较“Orig.”与“Mean”；无主效应F、df、p、效应量。 | 未报告因子设计意义上的主效应统计检验，故为0。 |
| B6 | 交互作用 | 0 | p7–10及p28–29仅报告描述性均值、相关系数与L1组单因素ANOVA，无variety×model/dataset交互项检验或简单效应分析。 | 完全未报告交互作用统计检验，故为0。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计，故NA。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计，故NA。 |
| B9 | 准实验设计 | NA | — | 非准实验分组研究；变体转换不是对独立组作非随机分配，且无选择偏差/匹配/DiD等准实验结构，故NA。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，不涉及处理可逆性与迁移对称性论证，故NA。 |
| C1 | 随机化 | NA | p5: “we randomly shuffle features in Lvi and apply them sequentially.” | 该随机化是转换特征应用顺序，不是研究单位到互斥条件的随机分配；无分配隐藏/基线均衡问题，故C1为NA。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，无顺序平衡需求，故NA。 |
| C3 | 恒定 | 0.5 | p26: 固定最大生成2048 tokens、zero-shot、统一system prompt；p7脚注/正文列出模型版本；p22固定guideline generation温度与top-p。 | 明确报告了部分恒定变量及水平，但未系统讨论这些恒定选择对外部效度的限制，故为0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配/配对分配，故NA。 |
| C5 | 纳入为变量 | 0.5 | p8–9: “separated the six datasets based on word count and sentence count using four quantiles”；p27: 对ESL四类L1组作one-way ANOVA。 | 长度作为分层分析变量、L1类别作组间比较，部分将已知混淆纳入分析；但未作为协变量/ANCOVA调整，也未检验斜率齐性，故为0.5。 |
| C6 | 盲法 | 0 | p6: “recruited graduate students… selected three individuals… Each model generated 25 transformed outputs… evaluated on two criteria”；未报告盲法安排。 | 存在人类标注者评价转换质量，但未报告对模型身份/条件的盲法或盲法成功检验，故为0。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级（完全平衡/拉丁方/ABBA）设计，故NA。 |
| D1 | 练习效应 | NA | — | LLM各评测提示独立，无练习/学习阶段；人类被试练习效应不适用，故NA。 |
| D2 | 疲劳效应 | NA | — | 无人类session时长、休息或疲劳控制问题，故NA。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各变体评测相互独立，无跨条件清洗期或迁移残留问题，故NA。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉处理，不涉及不对称迁移，故NA。 |
| D5 | 范围效应 | NA | — | 主因变量为QA准确率/胜率/评分，不涉及人类被试内绝对量值估计或李克特范围效应，故NA。 |
| E1 | 位置 / 顺序偏差 | 0 | p26: “we parsed the output beginning from the phrase ‘The answer is’”；p7–10及p26均未报告随机化或反平衡多项选择选项位置。 | 多选题选项顺序/正确答案位置未见随机化或反平衡，且未讨论位置效应，故为0。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表，故NA。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分与跨群体反应风格比较，故NA。 |
| E4 | 需求特征 | NA | — | 主实验对象为LLM，无人类被试需求特征；人类标注者仅评价转换质量而非实验参与者，故NA。 |
| E5 | 实验者效应 | 0 | p6: 报告标注者招募、grammar pre-test与3人选择、150样本评价界面（Fig.4），但未报告对模型条件/研究假设的盲法。 | 人类标注者评价存在，但未报告盲法层级及评分者是否知晓模型条件；虽有部分标准化，核心盲法安排缺失，故为0。 |
| E6 | 天花板 / 地板效应 | 0.5 | p7–10 Tables 4–6报告各模型/数据集/变体的均值与原始SAE分数；例如ARC原始分接近97.5，但未报告SD、偏度、端点频率或pilot难度校准。 | 报告了均值并显示原始基准接近上限，但未提供分布/端点或难度校准证据，也未讨论天花板/地板，故为0.5。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量，故NA。 |
| F1 | 统计结论效度 | 0.5 | p27–29: Tables 19–20报告Pearson/Spearman/Kendall相关系数与p值及one-way ANOVA F/p；但主要模型比较仅报告均值/百分比，无CI、样本量依据或多重校正说明。 | 报告了部分效应量（相关系数）和检验结果，但缺置信区间、样本量/功效依据及多重性校正，故为0.5。 |
| F2 | 内部效度 | 0.5 | p5: 同一SAE题项转换为所有变体并在各模型上评测，控制了题项身份；p8–9分析长度与数据可得性；但无随机分配/基线等价/损耗流程。 | 以同一题项跨变体比较提供部分内部效度控制，并讨论长度/数据可得性威胁；但无正式分配程序与内部效度威胁评估，故为0.5。 |
| F3 | 构念效度 | 1 | p6–7: human evaluation报告valid rate 132/150 (88%)，semantic checker S precision 83.6%、recall 97.0%、F1 89.8%；p4–5: 专家审阅与特征效度验证。 | 报告了转换操纵检验、人工效度评价与语义保持指标，并对关键操作化提供效度证据，故为1。 |
| F4 | 外部效度 | 0.5 | p7–10: 6个公开基准、38个变体、7个模型及开放式任务；p10 Limitations: “focuses primarily on English varieties… evaluation is currently limited to QA tasks”。 | 报告了样本/任务/模型来源并讨论部分推广边界（仅英语、QA任务），但未报告跨样本/跨情境复现，故为0.5。 |
| G1 | 分析单位 | 0.5 | p7–10以model×dataset×variety汇总均值呈现；p27对L1四组作one-way ANOVA；未说明题项嵌套于数据集/变体的多层结构。 | 说明了转换在题项层面、统计主要在数据集/变体汇总层面，但未显式处理题项嵌套或匹配方差，故为0.5。 |
| G2 | 随机效应 | NA | — | 模型、数据集和变体是被明确选择的固定集合，主要分析为汇总描述与变体层面相关；无混合模型/随机效应需求，故NA。 |
| G3 | 材料作为随机效应 | NA | — | 使用各基准全部题项作为固定材料，未从材料总体抽样，也未主张推广到任意题项总体；无需项目随机效应，故NA。 |
| G4 | 统计功效 | 0 | p7–10报告均值，p28–29报告部分p值；全文无事前功效分析、目标效应量来源或样本量/重复次数论证。 | 无任何功效分析或样本量确定依据，故为0。 |
| G5 | 研究者自由度 | 0.5 | p5: 对无法充分简化词汇的样本“exclude those samples”；p25 Table13报告各数据集转换成功数与比例；但未报告停止规则或验证性/探索性分析区分。 | 报告了部分排除规则与转换/排除数量，以及全部基准/模型结果；但未完整报告样本量决定方式与探索性/验证性区分，故为0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–30 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册平台、编号/链接或数据收集前分析计划；故为0。 |
| J1 | 位置偏差 | 0 | p9: 开放式任务用“LLM-as-a-judge strategy, using GPT-4.1 as evaluator”；p26: 多选题解析“The answer is”；未报告选项/候选位置随机化、交换重判或位置×正确率。 | 涉及多选输出与LLM裁判，但完全未提及位置偏差控制或翻转率，故为0。 |
| J2 | 冗长偏差 | 0 | p9: AlpacaFarm用win rate、MT-Bench让评估LLM给0–10分；未报告长度控制、长度—得分相关或长度匹配。 | 开放式生成由LLM裁判评分，但未对长度/冗长偏差作任何说明或控制，故为0。 |
| J3 | 谄媚 | NA | — | 任务为客观QA/指令跟随/open-ended评分，无用户先验立场或反馈纠错操纵，谄媚风险不存在，故NA。 |
| J4 | 自我偏好 | 0.5 | p9: 裁判为GPT-4.1（p9脚注gpt-4.1-2025-04-14）；被评模型包括GPT-4o-mini与o4-mini等同属OpenAI家族；未报告匿名化、异源陪审团或与人类一致性。 | 报告了裁判模型版本与被评模型，可识别同源风险；但未控制自我偏好或量化偏差，故为0.5。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p22: guideline generation用one-shot prompting；p24 Table15转换提示为one-shot并含示例；p6未报告示例来源/排列/多seed。 | 存在few-shot/one-shot示例并给出模板，但未报告示例选择来源、标签比例、排列反平衡或多seed重采样，故为0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p22 Table9、p24 Table15、p27 Table16、p26 D.1系统提示均给出；但未做语义等价措辞敏感性消融或dev/test划分说明。 | 提供了较完整prompt模板，但缺少版本化敏感性消融与dev/test分离说明，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG设置，故NA。 |
| J8 | 温度与采样随机性 | 0 | p26仅说明zero-shot与最大2048 tokens；未报告评测temperature/top-p/top-k、seed或每条件重复采样N/CI。p22仅对guideline generation报告temperature 0.8、top-p 0.95。 | 主基准评测的采样超参与随机性未报告，且无重复运行/置信区间，故为0。 |
| J9 | 重复与文本退化 | 0 | p9开放式任务生成模型输出；全文未报告解码策略、repetition penalty、重复率/退化率或截断比例。 | 涉及开放生成但未报告解码与退化QC，故为0。 |
| J10 | 分词效应 | NA | — | 研究为英语内部变体，同一拉丁脚本，无跨语言/跨脚本分词比较，故NA。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p5使用MMLU、ARC、TruthfulQA、GSM8K、HellaSwag、WinoGrande等公开基准；p7列出模型版本；未做训练截止日期对照或污染检测。 | 公开基准存在污染风险，但未报告版本/训练截止日期对照或n-gram重叠检测，故为0。 |
| J12 | 基准饱和 | 0.5 | p7–10报告原始SAE分数很高（如ARC 97.5、GSM8K 96.1、HellaSwag 96.1、WinoGrande 91.1），部分接近上限；但未讨论饱和或改用连续指标/CI比较。 | 报告了分数量程与水位，接近天花板却未使用连续指标或CI比较，故为0.5。 |
| J13 | 指令遵循 | 0.5 | p9: IFEval用于开放式任务，“metric is the accuracy of instruction adherence”；Table6仅报告IFEval总准确率，未按约束类型拆分。 | 使用了可机器验证的IFEval，但未按否定/数量/格式等约束类型拆分，也未报告模型指令微调信息，故为0.5。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p26: 系统提示要求“Start your final sentence with ‘The answer is ’”，并据此解析；但未报告格式合法率、重试策略或将格式失败与内容错误分开。 | 有结构化输出/解析约束，但未报告格式合法率与重试/后处理，故为0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估，无有害请求集，故NA。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究为工程/应用型LLM基准评测，不主张将LLM作为心理学/认知科学被试测量人类同名构念，故NA。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随模型规模/训练进展的涌现能力曲线，故NA。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练/RL/best-of-N等对代理指标进行优化的环节，故NA。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p7脚注给出gemini-2.5-pro-exp-03-25、gpt-4o-mini-2024-07-18、o4-mini-2025-04-16等版本并公开代码/数据；但未报告每分数重复N、95%CI或配对检验。 | 提供了部分精确模型版本与公开资源，但缺少重复次数、置信区间和配对检验，故为0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示/单轮评分，无多轮对话历史累积，故NA。 |

## 编码小结
研究属于LLM基准与框架评测，而非人类被试实验。优点是对变体转换流程、提示词、转换有效性和开放式评测有较详细报告；不足是主基准比较多为汇总均值，缺少因子ANOVA/交互检验、重复采样与置信区间、位置/长度偏差控制、污染与饱和讨论，以及若干实验设计与人因质控组件不适用。
