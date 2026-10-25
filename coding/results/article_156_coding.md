# article_156 | EvaLearn: Quantifying the Learning Capability and Efficiency of LLMs via Sequential Problem Solving | 2025

研究类型概述：该文是面向大语言模型的基准评测研究：构建648题、182个7题序列、6类任务的EvaLearn，比较zero-shot、few-shot、demonstration learning、feedback learning等求解范式，并用GPT-4o作为评委、结合实例级rubric进行自动判定，报告多个学习能力/效率指标。文中称评测九个前沿模型，但表2、表4、表5又包含Gemini-2.5-Pro/Flash，存在模型数量口径不一致。
- **研究构念（Construct）**：序列问题解决中的经验学习、学习效率、稳定性、反馈利用与负迁移｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让九种现成LLM按顺序解决182组、每组7个相关问题，在零样本、少样本、历史示例和教师反馈条件下比较后续题目的行为变化。（操纵问题位置、任务类型、是否保留先前问题与标准答案、是否提供逐题rubric反馈以及思考型与非思考型模型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5-6: 'two sequential learning paradigms: (I) Demonstration learning... (II) Feedback learning'; p.5-6 also defines zero-shot and few-shot, with prompts in Fig. 19-22. | 明确命名并报告了至少四种求解范式的水平与提示程序，但未见操纵检验、正式的单位分配说明或条件顺序随机化。 |
| A2 | 因变量 | 0.5 | p.4-5: five metrics defined by formulas (Acc, slope k, Pfirst, Poffset, Nconsec, Accpw-K); p.4: rubric + 'LLM-as-a-judge'; p.4: human verification 'exceeds 95%'. | 因变量指标与计分方式明确，并报告了评委人工核验准确率；但无连续指标预处理、无置信区间/分布、效度证据不足。 |
| A3 | 控制变量 | 0.5 | p.4: 'we use GPT-4o as the judging model'; p.29: 'temperature is set to 0.2' for non-thinking models; 'input and output lengths are set to the maximum supported by each model'. | 报告了部分控制变量（评委模型、温度、最大长度、提示模板），但未系统列出控制变量清单及控制手段。 |
| A4 | 混淆变量 | 0.5 | p.1/p.7-p.9: discusses 'stronger static abilities do not show a clear advantage in learning capability' and task/model differences; p.9: 'static model capability, task type, and reasoning approach all influence learning efficiency'. | 识别了静态能力与任务类型等潜在混淆，并作描述性比较；但未系统控制或报告残余混淆/敏感性分析。 |
| A5 | 调节变量 | NA | — | 理论模型未设定正式调节变量；虽有任务类型、模型类型分组比较，但无调节假设、乘积项交互检验或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 无中介变量与直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.4-5: task definitions, five metric formulas, Eq.1-8; p.5-6: four solving paradigms; p.48-50: full judge and solving prompts; p.51-54: example instances with rubrics and canonical answers. | 关键构念（学习能力/效率）通过任务、提示、评分规则和指标公式被高度操作化，足以复现实验流程。 |
| A8 | 水平数与类型 | 0.5 | p.3: six task types; p.5-6: zero-shot, few-shot, demonstration learning, feedback learning; p.29: model list; p.28 Table 3: published dates. | 报告了任务类型、求解范式和模型水平标签，但未说明水平类型、间距/全距，连续变量也无中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.2: 'a suite of five metrics'; p.4-5: Acc, k, Pfirst, Poffset, Nconsec, Accpw-K; p.9: metrics 'capture different aspects'. | 对学习能力采用多种指标，具备多操作化；但未报告各指标间会聚效度或相关性矩阵，仅作概念性说明。 |
| A10 | 单一方法的风险 | NA | — | 自变量为提示/求解范式，因变量为模型答案经LLM rubric评委判定；非自陈式同源测量。LLM评委与部分被评模型同源的风险在J4单独编码。 |
| B1 | 被试间设计 | NA | — | 同一模型在多种求解范式和全部任务上被重复评测，不存在独立被试组随机分配到互斥条件的被试间设计。 |
| B2 | 被试内设计 | 0.5 | p.5: 'models are required to sequentially solve all problems within a sequence'; p.28: 'the order of problems within each sequence is randomized'. | 存在明显的模型内重复测量/序列设计，并随机化题序；但未报告求解范式顺序的平衡方案、各顺序分配或随机效应模型。 |
| B3 | 混合设计 | NA | — | 未定义或分析正式混合设计（如模型组间×任务/范式组内），也无混合模型/重复测量ANOVA。 |
| B4 | 因子设计 | NA | — | 文中呈现模型×任务×求解范式的描述性矩阵（如p.6 Table2、p.30 Table5），但未作为正式因子设计报告交互项或完整设计矩阵/每格样本量。 |
| B5 | 主效应 | NA | — | 无正式因子设计的主效应统计检验；仅报告均值差和描述性比较。 |
| B6 | 交互作用 | NA | — | 无正式交互项统计检验和简单效应分析；任务差异以描述性方式讨论。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计；模型间比较为观察性基准比较，未声称随机分配。 |
| B10 | 被试内设计的适用条件 | NA | — | 序列学习中的累积经验是研究目标，不是可逆处理的被试内条件顺序设计；无经典可逆性/迁移对称性适用结构。 |
| C1 | 随机化 | 0.5 | p.28: 'the order of problems within each sequence is randomized'. | 报告了题序随机化，但未说明随机数生成工具、分配隐藏与基线均衡；模型/范式条件也非随机分配。 |
| C2 | 平衡 | 0.5 | p.28: 'the order of problems within each sequence is randomized'; p.5: sequence positions defined. | 有题序随机化，但未报告平衡层级、各顺序数量或迁移对称性前提论证。 |
| C3 | 恒定 | 0.5 | p.29: 'temperature is set to 0.2'; 'input and output lengths are set to the maximum'; p.4: 'GPT-4o as judging model'. | 报告了部分恒定条件，但未系统列出所有恒定变量及对推广边界的限制。 |
| C4 | 匹配 | NA | — | 无匹配/配对设计。 |
| C5 | 纳入为变量 | 0.5 | p.5: Poffset uses zero-shot correctness to discount 'pre-existing knowledge' (Eq.5); p.9: discusses static ability. | 以zero-shot基线控制先验知识/静态能力，类似纳入基线变量；但未用协变量模型、斜率齐性检验或报告调整后效应量。 |
| C6 | 盲法 | NA | — | 无人类被试或人工评分者盲法；主要评分为自动化LLM评委。 |
| C7 | 平衡的层级 | 0 | p.28: 'the order of problems within each sequence is randomized'; p.5: sequence positions defined. | 研究存在被试内/序列顺序平衡需求（同 C2），但未明确选用完全平衡、拉丁方或 ABBA 层级，亦未报告构造方法与顺序效应形状假设，记 0。 |
| D1 | 练习效应 | 0.5 | p.5 Eq.8: Accpw-K excludes first K problems; p.7/p.44-45: post-warmup accuracy discussed. | 用warm-up截除分析练习效应，并报告不同K；但无练习结束标准、渐近平台、试次位置协变量或ABBA抵消。 |
| D2 | 疲劳效应 | NA | — | LLM API评测不存在人类疲劳效应；任务分多次API调用，疲劳不适用。 |
| D3 | 延滞 / 迁移效应 | 0.5 | p.1/p.6: 'negative transfer' discussed; p.2/p.5: sequential setting lets models use experience from previous solutions. | 识别了正/负迁移和跨题经验累积，但未使用清洗期，也未把条件对显式建模。 |
| D4 | 不对称迁移 | 0.5 | p.1: 'negative transfer'; p.6-p.9: positive/negative task-specific transfer discussed. | 承认迁移可正可负，但未系统检验迁移对称性或量化残留偏差方向/大小。 |
| D5 | 范围效应 | NA | — | 因变量为客观正确率类指标，不涉及主观量表锚定或范围效应。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.28: 'the order of problems within each sequence is randomized'; p.5: position m=1...7 used. | 对题序做了随机化，但未报告随机化方案、各位置出现次数或跨序列平衡细节。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征； prompts虽可影响模型，但不属于人类实验需求特征。 |
| E5 | 实验者效应 | NA | — | 完全自动化API采集，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table2 and p.37-39 heatmaps report mean accuracies; some task cells are high (e.g., summarization/classification/MR around 85%-90%). | 报告了单元均值，可观察部分高分任务；但未报告SD、偏度或端点频率，也未讨论天花板/地板效应对区分度的影响。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；主要风险为LLM评委同源，已在J4处理。 |
| F1 | 统计结论效度 | 0.5 | p.4: N=182 sequences, M=7; p.6 Table2: percentage-point differences; p.37-39: slope k heatmaps. | 报告了样本结构与多处效应量式差异/斜率，但无置信区间、无功效分析、无多重性校正，且'显著'多为叙述性。 |
| F2 | 内部效度 | 0.5 | p.5-6: solving paradigms and prompts described; p.28: problem order randomized; p.29: API models/temperature. | 报告了条件程序与题序随机化，但无分配隐藏、基线等价检验、API失败/损耗处理或系统内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | p.4: human verification of judge outputs 'exceeds 95% for all tasks'; p.28: rubric validation process; p.4-5: five metrics. | 报告了评分可靠性/人工核验，但效度证据与操纵检验不足，且单方法/单评分框架限制未系统讨论。 |
| F4 | 外部效度 | 0.5 | p.3: six task types and 648 problems; p.29: model list and API evaluation; p.26: limitations. | 报告了任务与模型样本来源，但未说明代表性抽样、纳入排除标准、跨情境复现或明确推广边界。 |
| G1 | 分析单位 | 0.5 | p.4: 'N=182... M=7'; metrics average over sequences and problems; p.5: per-sequence/per-position formulas. | 说明了分析单位为序列/问题/模型，但存在问题嵌套序列、序列嵌套任务的聚集结构，未用多层模型显式处理。 |
| G2 | 随机效应 | 0 | p.4-5: metrics average across sequences and positions; p.6: model-level comparisons; no random-effects model reported. | 未报告随机效应结构；模型被作为固定比较组，序列/问题方差未从误差项分离。 |
| G3 | 材料作为随机效应 | 0 | p.3-4: fixed 648-problem benchmark; p.4: N=182 sequences; no item random effect or F1/F2 modeling. | 题目被视为固定基准材料，未将材料/题目作为随机效应；结论向任意题目总体的推广缺乏建模支持。 |
| G4 | 统计功效 | 0 | p.4: fixed 648 problems/182 sequences; p.6 and Appendix results report point estimates; no power analysis or CIs. | 无事前功效分析、无置信区间；样本量由基准构建决定，不是由功效推导。 |
| G5 | 研究者自由度 | 0.5 | p.3-4: all six task types and 648 problems described; p.6 Table2/p.30 Table5 report multiple paradigms; p.29: nine models listed, but tables also include Gemini models. | 报告了全部任务/主要条件与指标，但未报告API失败/试次剔除规则或样本停止规则；且模型数量口径不一致，增加选择性报告疑虑。 |
| G6 | 预先设定 / 预注册 | 0 | p.1-10 and Appendix A: no preregistration platform/ID or pre-analysis plan reported. | 未见公开预注册；按口径无预注册记0，而非NR。 |
| J1 | 位置偏差 | NA | — | LLM评委不是做候选A/B成对选择或排序，而是按rubric对单个答案判分；无候选项位置偏差结构。 |
| J2 | 冗长偏差 | 0 | p.4: GPT-4o judge with instance-level rubric; p.48 Fig.18: grading prompt emphasizes requirements but not length control. | 评估开放式生成，但未说明长度偏差、未报告长度-得分相关或盲评/长度对照。 |
| J3 | 谄媚 | NA | — | 无用户先验立场/pro-anti framing操纵；feedback learning中的反馈来自评分规则/教师模型，不是用户立场纠错。 |
| J4 | 自我偏好 | 0 | p.4: 'In all experiments, we use GPT-4o as the judging model'; p.6 Table2 includes GPT-4o among evaluated models. | 评委与被评模型存在同源（GPT-4o既评又评GPT-4o输出），未使用异源陪审团、匿名化或报告自我偏好偏差率。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.5: few-shot uses 'three demonstrations from the same task'; 'The demonstrations are identical for all problems within each task type'; p.49-50 Fig.20. | 报告了示例数量和同一任务来源及固定模板，但未报告标签比例、示例抽样/排列反平衡、多seed重复或示例未取自测试集的证明。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.48-50: full judge prompt and full zero-shot/few-shot/demonstration/feedback prompts in Fig.18-22. | 提供了完整提示模板，但无版本迭代日期、语义等价敏感性消融、dev/test分离说明或prompt搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 序列上下文包含前序题目/答案/反馈，但并非长上下文或RAG基准；未设置长文档关键信息位置操纵，也无RAG chunk排序。 |
| J8 | 温度与采样随机性 | 0.5 | p.29: 'temperature is set to 0.2' for non-thinking models; 'thinking-based models do not support temperature adjustment'; input/output max lengths set. | 报告了主要采样温度（部分模型）与最大长度，但无top-p/top-k、seed、重复采样N、置信区间或API snapshot日期。 |
| J9 | 重复与文本退化 | 0 | p.29: temperature and max lengths only; no decoding method, repetition penalty, repetition/degeneration rate reported. | 涉及开放式生成，但未报告greedy/beam/sampling等解码策略，也未把重复率/退化率作为质控指标。 |
| J10 | 分词效应 | NA | — | 主要为单语言英文任务，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3: problems 'carefully constructed from scratch'; p.28 Table3 lists model published dates, but no training cutoff/contamination detection. | 自建基准降低但未排除污染；未报告测试集版本与训练截止日期对照、n-gram重叠/DCQ等污染检测或污染率。 |
| J12 | 基准饱和 | NA | p.6 Table2: overall accuracies roughly 28%-68%; p.3: benchmark described as challenging. | 这是新构建且总体分数未接近天花板，J12不构成主要风险；个别任务高分未改变总体判断。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；少量格式要求属于答题模板，不是系统性IF评测。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.48 Fig.18 judge output requires 'JSON' format; p.49-50 Fig.20-22 require answer formats; p.51-54 examples specify list-of-moves format. | 报告了格式约束/提示模板，但未报告格式合法率、结构化输出/grammar约束、重试策略，也未将格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估，无有害请求集或对抗攻击。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: claims to evaluate 'learning capability' and 'gap between models and human capabilities'; p.3: cites humans gaining experience from sequential problems. | 将LLM序列性能称为学习能力并类比人类学习潜力，但未系统界定LLM构念与人类同名构念的异同，也无人类同范式对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无随模型规模/训练进展的涌现能力曲线，也未宣称规模涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无对benchmark/奖励模型/LLM-judge的优化训练或best-of-N优化环节；属于纯评测。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.6/p.30 tables report single point percentages; p.29 lists API models and temperature/max length but no repeat N, CIs, seeds or precise snapshots (except case study p.31 uses Claude-3-7-sonnet-20250219). | 大多为单次运行点估计，无重复次数/置信区间/配对检验，模型snapshot标识不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | EvaLearn是序列解题，不是多轮对话；虽按位置评分，但不测试对话历史中的指令遵循/一致性衰减。 |

## 编码小结
EvaLearn提供了较完整的数据集、任务、提示模板、评分规则与多项学习指标，操作化与可复现材料较强；但统计推断较薄弱：缺少重复采样、置信区间、正式主效应/交互检验、随机效应建模与功效分析，且LLM评委GPT-4o同时是被评模型之一，未控制自我偏好；污染、饱和、提示敏感性、采样随机性等LLM评测风险报告不足。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 C7（NA→0）。
