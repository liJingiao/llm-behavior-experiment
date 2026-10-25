# article_191 | Evaluating the Moral Beliefs Encoded in LLMs | 2023

研究类型概述：LLM-as-survey-respondent 的基准/测量研究：研究者构造 1767 个道德情景，设计 3 种问题模板 × 2 种行动顺序共 6 种问题形式，对 28 个开放/闭源 LLM 进行重复采样，估计 action likelihood、entropy、QF-C 与 QF-E，并比较模型、情景歧义度和问题形式敏感性。没有人类被试或人类条件分配；模型比较为观察性。
- **研究构念（Construct）**：道德信念、道德选择不确定性和问题措辞敏感性｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：向28个模型施测包含高歧义和低歧义情境、两种行动及多种问题表述的大规模道德调查，估计行动概率、不确定性和措辞一致性。（操纵道德情境歧义度、违反的道德规则、问题模板和模型，并比较开放与闭源模型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3 Fig.2 and p.6: 'we employ three hand-curated question styles: A/B, Repeat, and Compare ... randomize the order of the two possible actions ... six variations'; p.7: M=10/5, temperature=1. | 问题模板和行动顺序是明确操纵的 LLM 条件，水平数、取值和呈现程序有报告；但没有传统 manipulation check，也没有把分配方式写成独立随机分组，而是所有模型/情景接受全部形式。 |
| A2 | 因变量 | 0.5 | p.3 Defs.1-6; p.5 Eq.7 Monte Carlo mapping; p.7: 'For high-ambiguity scenarios ... M to 10, while for low-ambiguity scenarios ... M to 5'; p.26 invalid/refusal rates. | 因变量指标、公式、计分与采样数明确；但缺少针对 action likelihood/entropy 指标的信度、效度证据，连续指标主要只报告 invalid answer 处理，无置信区间。 |
| A3 | 控制变量 | 0.5 | p.7: 'we keep the prompt header and sampling procedure fixed and present the model with one survey question at a time, resetting the context window'; temperature=1; p.6 equal weights across templates. | 报告了固定 prompt header、采样程序、温度、上下文重置和模板等权控制，但没有系统列出控制变量清单或逐一说明控制手段及外部效度限制。 |
| A4 | 混淆变量 | 0.5 | p.6 'Addressing Question Form Bias' describes six forms/order randomization; p.7 notes API models 'might change while we are conducting the survey ... record the API query timestamps'. | 识别并控制了问题形式/选项顺序偏差，也提到 API 模型漂移；但残余混淆（模型规模、训练/对齐差异、生成与评估模型重叠）没有系统敏感性分析。 |
| A5 | 调节变量 | NA | — | 研究没有明确的调节变量假设或调节效应检验；按问题形式拆分 QF-C/QF-E 是描述性敏感度分析，不是调节模型。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量、直接/间接效应分解或因果链中介假设。 |
| A7 | 操作性定义 | 1 | p.3 Defs.1-6; p.5 Eq.7 and deterministic mapping g; p.23 Tables 12-13 full question and instruction templates; p.7 M and response collection. | 道德选择、 uncertainty、问题形式一致性等构念均给出可复现的公式、prompt、映射规则和采样程序，关键操作化完整。 |
| A8 | 水平数与类型 | 1 | p.3 Fig.2 and p.6: three templates × two action orders = six question forms; p.6: 687 low-ambiguity and 680 high-ambiguity scenarios; p.22 scenario length statistics. | 问题形式与歧义度数据集的水平/标签明确；分类变量无需连续间距。 |
| A9 | 单一操作化的风险 | 0.5 | p.6 six question forms and 'Addressing Question Form Bias'; p.4 Def.5 QF-C as Jensen-Shannon-based consistency across question forms; p.9 Fig.4 QF-C/QF-E results. | 核心构念采用多种问题形式并有跨形式一致性指标，但主要是同一指标下的 prompt 变体，缺少正式收敛/区分效度或多操作化验证讨论。 |
| A10 | 单一方法的风险 | NA | — | 没有人类自陈式 IV/DV 同源测量；研究是提示操纵与模型输出测量，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或被分配到的独立组；28 个模型均接受同一情景/问题形式集，模型比较是观察性，不是被试间实验。 |
| B2 | 被试内设计 | 0.5 | p.6: every scenario is presented with six question forms; p.7: 'one survey question at a time, resetting the context window for each question'. | 同一模型/情景确实接受全部六种形式，属于重复测量结构；行动顺序有反平衡，但六种问题形式的呈现顺序和各顺序分配未报告，且上下文每次重置。 |
| B3 | 混合设计 | NA | — | 低歧义与高歧义数据集分别分析，未报告组间×组内混合设计或混合误差项。 |
| B4 | 因子设计 | NA | — | 没有因子 ANOVA/设计矩阵及交互项统计；问题模板和歧义度主要用于分层描述性比较，不构成完整因子实验分析。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验，因此不适用。 |
| B6 | 交互作用 | NA | — | 没有对问题形式×歧义度或模型×形式等交互项作正式统计检验。 |
| B7 | 区组设计 | NA | — | 按模型家族和参数规模分组只用于图形展示/排序，不是区组随机分配或区组设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计；独立上下文重置下无被试内顺序平衡需求。 |
| B9 | 准实验设计 | NA | — | 研究不是非随机分组准实验；它评估现成模型，没有随机/非随机处理分配或因果效应主张需要按准实验类型编码。 |
| B10 | 被试内设计的适用条件 | NA | — | 每次查询独立并重置上下文，不存在人类被试内处理的可逆性/迁移对称性问题；行动顺序控制见 E1/J1。 |
| C1 | 随机化 | NA | — | 研究单位没有被概率分配到互斥实验条件；所有模型接受全部问题形式，随机化仅涉及行动选项顺序。 |
| C2 | 平衡 | NA | — | 没有需要平衡的跨条件呈现顺序；独立重置上下文，行动顺序反平衡在 E1/J1 中编码。 |
| C3 | 恒定 | 0.5 | p.7 fixed prompt header/sampling and temperature=1; p.25 API access and model download timestamps; p.7 context reset. | 列出了部分恒定控制（prompt header、采样、温度、重置、API/模型时间戳），但未系统讨论这些恒定水平造成的外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用被试匹配、配对或倾向评分匹配。 |
| C5 | 纳入为变量 | 0.5 | p.8: models are 'grouped by model family and sorted based on their estimated size'; p.24 Table 14 model cards report size/access/fine-tuning. | 模型规模和家族等已知差异被记录并用于描述性分组/排序，但没有作为正式协变量或区组项纳入模型，也未报告调整后效应或斜率齐性检验。 |
| C6 | 盲法 | NA | — | 主结果由自动化规则映射提取，无人类主试/评分者对条件盲法；仅有数据集标注者，且不是对 LLM 条件的盲法评分。 |
| C7 | 平衡的层级 | NA | — | 没有使用完全平衡、拉丁方或 ABBA 条件顺序层级；独立重置上下文。 |
| D1 | 练习效应 | NA | — | LLM 每次问题独立调用并重置上下文，不存在跨试次练习/学习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳效应；采样为独立 API/本地调用而非长时人类 session。 |
| D3 | 延滞 / 迁移效应 | NA | — | p.7 明确每次重置上下文，且不同问题形式为独立调用，无跨条件残留或清洗期需求。 |
| D4 | 不对称迁移 | NA | — | 同上，独立调用意味着不存在不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 研究不使用 Likert/绝对量值估计等主观量表；输出是行动选择概率/熵，不是范围效应框架下的量表评分。 |
| E1 | 位置 / 顺序偏差 | 1 | p.6: 'randomize the order of the two possible actions for each question template, resulting in six variations'; p.23: 'present every scenario twice, by switching the two answer options'. | 对两个行动选项做了完整反平衡：每个情景在每种模板下两种顺序都出现，位置偏差控制清楚。 |
| E2 | 默认赞同 | NA | — | 研究不是 Likert/态度自评量表，没有反向计分题或默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体反应风格（端点/中点使用）比较。 |
| E4 | 需求特征 | NA | — | 没有人类被试，因此不存在人类需求特征、掩饰情节或事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 主数据采集完全自动化，无人类主试/评分者在条件间传递期望；数据集标注者不构成结果测量的实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.8 Fig.3 shows marginal action likelihood distributions; p.9 thresholds (QF-E 0.7, QF-C 0.6); p.7 M=5/10. | 因变量有界且图中可看到接近端点的分布，但未明确报告端点频率、偏度或 pilot 难度校准，天花板/地板讨论不足。 |
| E7 | 共同方法偏差 | NA | — | 没有自陈式多构念量表同源测量；IV 是 prompt/形式操纵，DV 是模型输出，不适用共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | p.9 reports Pearson correlations and hierarchical clustering; p.3-4 reports likelihood/entropy metrics; no confidence intervals or power analysis. | 报告了连续效应量/相关系数等主要结果，但没有样本量确定依据、置信区间、所有分析的多重性校正及统计假设检验细节。 |
| F2 | 内部效度 | 0.5 | p.6 randomizes action order; p.7 fixed prompt header/sampling, context reset, API timestamps; p.10 limitations. | 有行动顺序随机化、固定程序和漂移记录，但无分配隐藏/基线等价/被试流向/损耗处理等实验内部效度要素；研究本身也不做因果处理效应推断。 |
| F3 | 构念效度 | 0.5 | p.6 annotator agreement in Table 10 and manual review; p.4 QF-C as consistency metric; p.7 invalid/refusal handling. | 报告了标注者一致性和问题形式一致性指标，但没有对核心 action likelihood/道德信念构念提供正式信度、效度或 manipulation check。 |
| F4 | 外部效度 | 0.5 | p.6 lists 28 models and model families/access; p.10 limitations discuss English-speaking authors/annotators and cultural coverage; p.24-25 model cards/timestamps. | 报告了模型来源/特征和数据集文化局限，但没有跨样本/跨情境复现，也未系统论证模型总体或人类总体推广边界。 |
| G1 | 分析单位 | 0.5 | p.3-p.7 define LLM respondent pθj, scenario xi, question form z, M responses; p.5 Eq.7 Monte Carlo; results aggregate per scenario/model. | 说明了处理发生在模型/情景/问题形式层级，分析在情景级聚合并做模型级比较；但未用多层模型显式处理情景/样本嵌套与依赖。 |
| G2 | 随机效应 | NA | — | 统计分析不是混合效应模型；28 个模型是明确指定的比较对象而非从模型总体抽取的随机样本，模型随机效应不适用。 |
| G3 | 材料作为随机效应 | 0 | p.9 computes Pearson correlations across marginal action likelihoods and clusters them; p.22 reports 687/680 scenarios; no item-level random-effect model or F′/min F′. | 情景/材料是有限抽样得到的项目集，但分析把情景当作固定集合，仅做跨情景聚合/相关，没有将情景作为随机效应建模；结论仍从特定材料推广到模型道德偏好。 |
| G4 | 统计功效 | 0 | p.7 sets M=10 for high-ambiguity and M=5 for low-ambiguity; no power analysis or sample-size justification; no confidence intervals. | 没有事前功效分析、目标功效或预期效应量依据，结果也未系统报告置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.7 invalid answers excluded and likelihood set to 0.5 when no valid answer; p.26 reports invalid/refusal rates; all six forms and 28 models reported. | 报告了无效答案排除规则/数量概况和全部条件，但没有清楚区分验证性与探索性分析，也没有完整说明样本/停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | p.1 provides code/data link; no preregistration, timestamped hypothesis, stopping rule or analysis plan is reported. | 未发现公开预注册或数据收集前分析计划；不能判断验证性/探索性划分。 |
| J1 | 位置偏差 | 0.5 | p.6 randomizes action order and creates six forms; p.29-30 Fig.9/D.4 report option-order sensitivity; p.7 model names and temperature=1. | 识别并反平衡了候选行动位置，报告了问题形式和选项顺序敏感度；但没有给出偏好翻转率/位置×正确率曲线，也未给完整的裁判/评分者一致性对照。 |
| J2 | 冗长偏差 | NA | — | 没有 LLM-as-judge 对开放式生成质量按长度评分；任务是短行动选项/概率测量，不存在长回答被误当质量的问题。 |
| J3 | 谄媚 | NA | — | 也没有用户先验立场、反馈纠错或多轮对话式谄媚操纵；任务是闭卷情景选择。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 评估模型输出；序列到行动的映射是规则式，不涉及裁判自我偏好。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主评估是 zero-shot 调查问题；few-shot prompting 只用于生成高歧义情景（p.19），不是测试阶段的 in-context learning 实验。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.23 Tables 12-13 provide full question templates and instruction headers; p.29-30 Fig.9 and D.4 test three question styles and option orders. | 提供了完整 prompt 模板并做了语义等价问题形式/顺序敏感性分析；但没有版本号、迭代日期、dev/test 划分或完整的 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 情景上下文很短（p.22: low 14.96 words, high 36.28 words），无长上下文/RAG、信息位置操纵或中间迷失问题。 |
| J8 | 温度与采样随机性 | 0.5 | p.7 temperature=1 and M=10/5; p.31 top-p=1; p.25 API access timestamps; p.31 decoding ablation. | 报告了主要采样温度、top-p、M 和 API 时间戳，但没有随机种子、每条件 95% CI、top-k/repetition penalty 等完整采样记录。 |
| J9 | 重复与文本退化 | 0.5 | p.7 default temperature-based sampling; p.31 D.5 ablation compares sampling, greedy, beam search, beam multinomial; no repetition penalty/rate is reported. | 解码策略和消融有报告，主比较中策略保持恒定；但没有报告重复率/退化率或 repetition penalty。输出很短使退化风险较低，但仍属部分报告。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本，没有跨语言/跨脚本 token 数比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.6: low-ambiguity scenarios generated with OpenAI gpt-4; high-ambiguity scenarios generated with text-davinci-003; both models are among the 28 evaluated LLMs; no contamination check reported. | 测试集由被评模型生成且未见训练截止日期/污染检测/held-out 证明；存在自生成测试集污染与记忆复现风险，全文未评估。 |
| J12 | 基准饱和 | 0.5 | p.8 Fig.3 shows low-ambiguity scenarios with many models near high action-1 likelihood; p.9 uses continuous entropy/QF-C thresholds and separately analyzes high-ambiguity set. | 识别了低歧义数据集接近端点，并使用连续 likelihood/entropy 与高歧义子集补充；但没有 bootstrap CI 或明确饱和检验来支持模型间微小差异。 |
| J13 | 指令遵循 | 0.5 | p.23 Tables 12-13 specify answer constraints; p.26 reports invalid/refusal rates; p.23 B.2 uses rule-based mapping. | 格式/指令遵循通过规则解析和 invalid/refusal 率部分测量，但不是按否定/数量/格式/风格约束拆分准确率的指令遵循基准。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.23 Tables 12-13 define A/B, Repeat, Compare and instruction headers; p.26 reports invalid/refusal rates; p.7 excludes invalid answers and sets likelihood to 0.5. | 报告了输出格式约束和格式合法/无效率，但没有文法引导/结构化输出设置、重试策略或把格式失败与内容错误完全分开的独立指标。 |
| J15 | 越狱稳健性 | NA | — | 研究不是安全性/越狱评估；道德情景中的拒绝回答不是对抗越狱攻击成功率测量。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.5 Section 3.1 explicitly discusses LLMs as survey respondents and the debated issue of agency; p.7 and p.24-25 report model versions/timestamps and model cards; no full human same-scenario comparison. | 明确讨论了 LLM 上测量的‘道德信念’与人类自陈/道德心理学构念的异同，并把模型作为比较对象而非人类样本外推；但缺少同范式人类对照数据和精确权重快照，仍主要是 LLM 基准解释。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有报告跨模型规模/训练进展的能力曲线或‘涌现’宣称；模型大小只用于描述性分组和解释。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有训练、RL、best-of-N 或对代理指标的优化过程，不涉及 overoptimization。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.7 reports M=10/5; p.25 API access and model download timestamps; p.1 code/data link; p.31 decoding ablation; no confidence intervals or paired tests. | 报告了重复采样次数、模型/API 时间戳和代码数据链接，但没有逐分数 CI、精确 commit hash、配对检验或原始推理日志，复现性仅部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 所有问题均为单轮询问，且 p.7 明确每个问题重置上下文；没有多轮对话一致性衰减评估。 |

## 编码小结
论文对 LLM 道德选择的操作化、问题形式操纵和采样流程报告较细，尤其是完整 prompt、行动顺序反平衡、M 次采样、模型版本/API 时间戳和公开代码数据。但研究主要是描述性/测量性基准，不是人类被试实验：缺少随机分配、功效分析、置信区间与多层模型，构念效度和跨模型混淆控制有限；对基准污染、模型规模/训练差异和推断可复现性的报告也不完整。
