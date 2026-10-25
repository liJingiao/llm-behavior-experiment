# article_197 | When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings | 2025

研究类型概述：LLM 多轮传递链模拟研究（LLM-as-participant / 多智能体文化演化模拟）。分析单位为传递链及链内代际文本；主要条件为模型、任务、文本属性，初始文本按属性范围抽样；主要指标为毒性、积极性、难度、长度及由其估计的吸引子位置/强度。
- **研究构念（Construct）**：文化传递中的吸引子、累积信息变形与偏差放大｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：让同种或混合的现成LLM沿50代电话游戏链依次改写文本，追踪每代文本属性并估计文化吸引子的方向和强度。（改变初始文本、改写或续写指令、模型、模型规模及同质或混合传递链。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p5: three tasks Rephrase/Take inspiration/Continue and six models listed; p6: “For each of the 6 models, 3 tasks, and 20 initial texts, we ran 5 transmission chains with 50 transmission steps.” | 任务与模型被明确命名并给出水平/标签及提示文本，但未报告操纵检验；条件为全交叉执行而非随机分配，分配程序说明不完整。 |
| A2 | 因变量 | 0.5 | p5: toxicity by Detoxify 0.0–1.0, positivity by NLTK SentimentIntensityAnalyzer -1.0–1.0, difficulty by Gunning-Fog index, length by character count; p18: hashtag filtering for Mistral-7B Continue. | 因变量的指标与计分方式清楚，但未报告这些自动指标的信度/效度证据，也未详细说明连续指标的预处理与端点/天花板地板处理。 |
| A3 | 控制变量 | 0.5 | p18: “Temperature was set to 0.8 with and top_p to 0.95. All models, except GPT3.5, bfloat16 precision was used.”; p5: tasks remained consistent within each chain. | 报告了温度、top-p、精度和链内任务固定等控制，但不是系统列出所有额外变量及其控制手段。 |
| A4 | 混淆变量 | 0.5 | p26: section B.2.3 notes tasks vary on dimensions beyond “room for variation,” and adds a constraint manipulation; p8: robustness checks for prompt phrasings and larger initial-text set. | 识别并部分控制了任务限制程度等潜在混淆，但未系统讨论残余混淆或敏感性分析对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 本研究的理论模型没有明确的调节变量与调节假设；任务/模型/属性被作为因素或效应来源处理，未做乘积项交互检验，故不适用。 |
| A6 | 中介变量 | NA | — | 本研究没有中介变量、直接/间接效应分解或中介假设。 |
| A7 | 操作性定义 | 1 | p4: texti+1 = LLM(task, texti), 50 generations; p18: exact prompts for Rephrase/Inspiration/Continue; p5 and p19: exact metric tools and scoring. | 关键构念给出了可复现的操作程序：传递链生成规则、任务提示、文本属性测量工具与计分范围均明确。 |
| A8 | 水平数与类型 | 0.5 | p5: three task levels and six model levels; p18: initial texts sampled to cover five difficulty/toxicity/positivity/length values; p6: 20 initial texts × 5 seeds. | 报告了主要因素的水平数与标签，但未完整说明水平类型、间距/全距以及连续初始属性进入回归时的中心化/标准化处理。 |
| A9 | 单一操作化的风险 | 0 | p5: each text property measured by one metric (Detoxify, NLTK/VADER, Gunning-Fog, character count); p19: metric details. | 每个关键文本属性仅用单一指标操作化；全文没有在局限部分讨论单一操作化对可推广性的限制，也没有多指标会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈式多构念测量；自变量为模型/任务条件，因变量为自动文本指标，不存在人类共同方法偏差问题。 |
| B1 | 被试间设计 | 1 | p6: “each chain is composed of a population of agents sharing the same underlying model”; “Tasks remained consistent within each chain”; 5 chains per model/task/initial text. | 链为独立分析单位，每条链只接受一个模型/任务组合；报告了每种组合的链数（20 初始文本×5 seeds=100 条链）。 |
| B2 | 被试内设计 | NA | — | 不存在需要平衡顺序的被试内条件设计；50 代是传递链的纵向序列，而不是可反平衡的实验条件顺序。 |
| B3 | 混合设计 | NA | — | 没有明确采用混合设计并逐因素标注组间/组内，也没有混合 ANOVA 的组间/组内误差项报告。 |
| B4 | 因子设计 | 0 | p28: “Model 1 ... μ = αTask + βModel + γProperty”; no interaction terms or full design matrix; p6 reports model/task/property conditions. | 虽然模型、任务、属性被全交叉执行，但统计分析采用加性贝叶斯模型，未报告因子设计完整设计矩阵、格子样本量或交互项。 |
| B5 | 主效应 | 0.5 | p8: reports posterior differences across Task, Model, Property with 95% credible intervals; Tables 2–4 p28–29 give CIs for differences. | 报告了主要因素差异及 95% 可信区间，但没有 F/df/p 效应量，也未在交互显著时讨论主效应解释限制。 |
| B6 | 交互作用 | 0 | p8: “Increasing the temperature appears to lead to stronger attractors only in constrained tasks”; p9 Figure 5a shows visual pattern; no interaction test reported. | 存在类似交互的视觉/描述性主张（温度×任务），但没有报告交互项统计检验、简单效应或置信区间，属于仅凭图形/描述作交互解释。 |
| B7 | 区组设计 | 0.5 | p18: initial texts selected to cover five values of difficulty, toxicity, positivity, and length; p6: 20 initial texts and 100-text robustness check. | 按初始文本属性范围进行了分层抽样/区段控制，但未说明正式区组变量、区内随机分配和模型中的区组处理。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；模型/任务条件为模拟全交叉执行，不涉及非随机分组与选择偏差的准实验推断框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理条件及其可逆性/迁移对称性论证需求；传递链代际序列是研究现象本身。 |
| C1 | 随机化 | 0 | p6: “For each of the 6 models, 3 tasks, and 20 initial texts, we ran 5 transmission chains”; no randomization method or allocation concealment reported. | 条件为全交叉网格执行，未报告概率分配、随机数工具或分配隐藏；作为模拟实验未见随机化程序。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序；每条链固定一个任务/模型并沿代际传递。 |
| C3 | 恒定 | 0.5 | p18: temperature 0.8, top_p 0.95, bfloat16 precision; p5: exact models and APIs; p5: task consistent within chain. | 列出了一些恒定变量及水平，但未系统讨论这些固定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配程序或匹配变量。 |
| C5 | 纳入为变量 | 0.5 | p6: linear regression of final property on initial property; p28: Bayesian models include Task, Model, Property effects. | 初始属性值被纳入回归，任务/模型/属性被纳入贝叶斯模型；但未报告协变量斜率齐性检验或调整后效应量等 ANCOVA 类假设检验。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人类评分者，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 等条件顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 没有人类练习块或试次位置协变量；LLM 各代调用不是同一被试的练习序列，代际变化是研究对象。 |
| D2 | 疲劳效应 | NA | — | 不存在人类 session 疲劳或休息安排问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件清洗期需求；链内上一代输出作为下一代输入是该设计的核心机制，不是需洗脱的迁移污染。 |
| D4 | 不对称迁移 | NA | — | 没有被试内交叉条件及迁移对称性检验需求。 |
| D5 | 范围效应 | NA | — | 使用客观文本指标而非主观量表绝对判断，范围效应组件不适用。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选项/刺激呈现顺序或被试内处理顺序需要随机化或反平衡；每条链按固定任务提示传递单一文本。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 智能体不会被人类式需求特征影响，也不需要掩饰情节或事后访谈。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p7 Figure 2 shows property distributions across generations; p7 notes toxicity converges to a narrow peak around 0; p31 discusses Mistral length discontinuities/collapse. | 报告了分布形态并显示毒性在 0 附近堆积（地板效应相关），但未系统报告均值/SD/偏度/端点频率，也未说明 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，CMB 不适用。 |
| F1 | 统计结论效度 | 0.5 | p28: 95% credible intervals for posterior differences; p28: argues FDR correction unnecessary because all p-values are reported; p6: 20 texts × 5 seeds. | 报告了可信区间和所有 KS p 值，但没有事前功效分析、明确效应量或样本量确定依据。 |
| F2 | 内部效度 | 0.5 | p6: same 20 initial texts and 5 seeds across model/task conditions; p8 and p23–26: robustness checks with 100 texts, prompt paraphrases, and constraint manipulation. | 通过相同初始文本与多 seed 及稳健性实验增强了内部可比性，但未报告随机分配、分配隐藏或正式基线等价检验。 |
| F3 | 构念效度 | 0.5 | p5 and p19: describes Detoxify, VADER/NLTK, Gunning-Fog, character count; p18: uses established tools; no reliability/validity statistics or manipulation check reported. | 指标工具和构念对应关系有说明，并引用成熟工具，但未报告信度/效度证据、操纵检验或单一操作化局限。 |
| F4 | 外部效度 | 0.5 | p5: six models from three companies; p18: initial texts from scientific abstracts, news, social media; p10: limitations discuss homogeneous chains, networks, human-LLM extension. | 报告了模型与初始文本来源，并讨论了部分推广边界，但没有代表性抽样、跨人群/跨情境复现或明确总体推广框架。 |
| G1 | 分析单位 | 0.5 | p6: 100 chains per model/task (20 initial texts × 5 seeds); p6–7: each chain has 50 generations; p28: Bayesian models fitted on attractor strength/position estimates. | 说明了链为分析单位及链数，但代际嵌套于链、seed 嵌套于初始文本等聚集结构未用多层模型显式分离。 |
| G2 | 随机效应 | 0 | p28: “Strength ~ N(µ, σ²), where µ = αTask + βModel + γProperty”; “Positionproperty ~ N(µ, σ²), where µ = αTask + βModel”. | 贝叶斯模型把所有因素作为固定效应，未说明初始文本、seed 或链的随机效应结构，无法据此判断推广总体。 |
| G3 | 材料作为随机效应 | 0.5 | p18: initial texts sampled from larger online datasets to cover property ranges; p23: robustness check with 100 initial texts; p28: no item random effect in models. | 初始文本被视为从更大材料库抽样并做了 100 文本稳健性检查，但分析中未将材料/初始文本作为随机效应纳入模型。 |
| G4 | 统计功效 | 0 | p6: 20 initial texts × 5 seeds; p8: 95% credible intervals; no a priori power analysis or sample-size justification. | 没有设计阶段功效分析或样本量确定依据；虽然报告了可信区间，但不满足功效分析要件。 |
| G5 | 研究者自由度 | 0.5 | p18: filters out “#some_keyword” hashtags for main analyses; p5: lists four metrics; p8 and app. B: multiple robustness checks; no explicit confirmatory/exploratory labeling. | 报告了排除规则、主要指标和部分稳健性分析，但未完整区分验证性与探索性分析，也未说明是否有中途停止/追加。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration mentioned; p11 only provides reproducibility statement and GitHub link. | 未报告预注册平台、注册编号、预设假设或分析计划；仅有可复现性声明不等于预注册。 |
| J1 | 位置偏差 | NA | — | 不使用 LLM-as-judge、多候选项选择、排序或成对比较，位置偏差不适用。 |
| J2 | 冗长偏差 | NA | — | 没有用 LLM 裁判评估开放生成质量；长度本身是被测量的结果变量，不是裁判偏差控制问题。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈纠错或谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 评估模型输出，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验使用零样本任务提示，没有 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p18: exact prompts for three tasks; p24: five different phrasings per task used as robustness check; no prompt version number or dev/test split. | 提供了完整提示模板并做了措辞敏感性复现，但没有版本号、迭代日期、dev/test 划分或 prompt 搜索过程报告。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 每一代只接收前一文本，不是长文档/RAG 或超长上下文信息位置实验。 |
| J8 | 温度与采样随机性 | 0.5 | p18: “Temperature was set to 0.8 ... top_p to 0.95”; p6: 5 seeds per initial text/model/task; no top-k, max length, or explicit seed values. | 报告了主要采样超参与 5 次重复，但未完整报告种子值、top-k、最大生成长度及每条件 95% CI。 |
| J9 | 重复与文本退化 | 0.5 | p18: temperature/top_p; p31: Mistral-7B Continue degenerates into many hashtags; p32 Table 13 examples; hashtags filtered in main analyses. | 报告了解码采样设置和重复/退化现象，但未报告 repetition penalty、生成长度上限或系统化退化率指标。 |
| J10 | 分词效应 | NA | — | 单语言英文文本实验，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 不是能力基准测试；没有测试集准确率或公开 benchmark 分数需要做训练数据污染检查。初始文本用于刺激生成而非金标准答案。 |
| J12 | 基准饱和 | NA | — | 不使用有分数上界的基准，也无基准饱和/天花板比较问题。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循准确率，没有机器可判定约束遵守测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 输出为自由文本，不要求 JSON/结构化格式，也不解析格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 实验测量毒性作为文本属性演化结果，不是越狱/安全对齐评估；未设置自然拒绝率或对抗攻击成功率。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p2–p3: borrows cultural evolution/attractor concepts; p3: “avoid assuming that LLMs possess ‘priors’ in the same way that humans do”; p4: contrasts with cultural values literature. | 论文对 LLM 上文化吸引子构念与人类文化演化构念的关系有理论讨论并澄清非直接类比，但没有与人类同范式数据对照，构念效度论证不完整。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有随模型规模/训练进展宣称“涌现/突变”的连续能力曲线；只有若干模型包括不同 Llama 规模作为条件比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不训练、不微调优化代理指标，也不以 benchmark/奖励模型为优化目标。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p11: GitHub and data release; p5: exact model names/versions incl. gpt-3.5-turbo-0125 and Mistral-7B-Instruct-v0.2; p6: 5 seeds; p8: credible intervals. | 报告了 5 次重复、模型版本与数据/代码，部分模型 snapshot 标识不完全精确，模型比较主要基于可信区间而非配对检验。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p4: “We run this process for 50 generations”; p6–p7: properties tracked at each generation; p8: KS tests compare generation i to generation 1. | 明确做了多轮评估并按代际分析、比较单轮与多轮差异；但未明确报告上下文是否会在超长文本时截断，也未报告每轮上下文长度处理。 |

## 编码小结
论文清楚报告了 LLM 传递链设计、任务提示、模型版本和自动文本指标，并报告了代际分布、KS 检验和贝叶斯可信区间。但它不是人类实验，许多人类被试特有的人际分配、顺序平衡、盲法、需求特征等组件不适用；同时缺少操纵检验、测量信效度、功效分析、随机效应/嵌套结构建模、预注册和完整提示版本管理等。
