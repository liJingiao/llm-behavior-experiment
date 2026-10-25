# article_104 | Comparing LLM-generated and human-authored news text using formal syntactic theory | 2025

研究类型概述：计算语言学/语料库观察性比较研究：复用已有NYT与LLM生成语料，使用HPSG/ERG形式语法解析，比较人类与6个LLM文本的句法构式、词汇类型、形态规则分布、余弦相似度与多样性指数。分析单位为数据集/语料层级（并辅以作者层级描述），来源分组是观察变量，不是作者操纵的实验条件；无人类被试随机分配。
- **研究构念（Construct）**：句法行为、语法多样性与生成语言的结构扁平化｜CA 构念锚定：句法加工（syntactic processing, `trm_4a3fd79d0b34b`）；句法分析（syntactic parsing, `trm_4a3fd79d0b340`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）
- **实验任务与范式（Task / Paradigm）**：计算语言学/语料库观察性比较研究：复用已有NYT与LLM生成语料，使用HPSG/ERG形式语法解析，比较人类与6个LLM文本的句法构式、词汇类型、形态规则分布、余弦相似度与多样性指数。分析单位为数据集/语料层级（并辅以作者层级描述），来源分组是观察变量，不是作者操纵的实验条件；无人类被试随机分配。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | — | 作者没有主动操纵自变量；LLM文本与人类NYT文本均为复用既有语料，来源（human/NYT vs 6个LLM vs WSJ/Wikipedia）是观察性分组，不是实验操纵。 |
| A2 | 因变量 | 0.5 | PDF p.3/9043：“counting the occurrences of phrasal constructions, lexical (inflectional and derivational) rules, and lexical types... through cosine similarity and diversity metrics”；PDF p.7/9047：“Shannon entropy H and the Gini–Simpson index 1 − λ”。 | 因变量指标（HPSG类型频次、余弦相似度、Shannon与Gini–Simpson指数）与计分方式基本明确；但未报告测量信度、评分者/解析一致性、连续指标预处理或置信区间等完整性证据。 |
| A3 | 控制变量 | 0.5 | PDF p.3/9043：“We parsed the data with the latest version of the ERG... and ACE”；同页“We use the dataset created by Muñoz-Ortiz et al. (2024)”；PDF p.10/9050：“we only look at one genre (NYT-style news)... This is why our study is only about English.” | 提到固定语料来源、语法/解析器版本、语体与语言等常量，但没有系统列出控制变量清单及逐一控制手段；属于部分控制。 |
| A4 | 混淆变量 | NA | — | 该研究是观察性语料比较，无作者操纵的自变量与内部效度意义上的实验混淆控制结构；文中虽提到采样、提示与语体限制，但不按实验混淆变量编码。 |
| A5 | 调节变量 | NA | — | 理论模型不包含调节变量，也未进行交互检验或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 理论模型不包含中介变量，也未做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | PDF p.3/9043：“counting the occurrences...”；“We release the ERG-parsed LLM-generated data through GitHub”；PDF p.7/9047：说明Shannon H与Gini–Simpson 1−λ。 | 对语料来源、解析工具、计数单位、余弦相似度与多样性指标给出了可重复执行的操作化流程，并公开解析数据；虽无实验操纵，但测量操作化完整。 |
| A8 | 水平数与类型 | NA | — | Table 1虽列出模型规模与语料来源，但这是观察性分组，不是作者操纵的多水平自变量；按A8规则记NA。 |
| A9 | 单一操作化的风险 | 1 | PDF p.4/9044：Figure 2–4分别比较syntactic types、lexical types、lexical rules的余弦相似度；PDF p.7/9047：使用Shannon与Gini–Simpson两种多样性指数并报告排序一致。 | 关键构念（句法/词汇结构分布）采用多种操作化与多个指标，并报告了跨指标的模式一致性与差异，属于多操作化策略。 |
| A10 | 单一方法的风险 | NA | — | 测量对象是文本的客观语法特征计数，不是自评量表或同源主观构念测量；共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 无人类或LLM被试的条件分配；语料按来源独立分组，不存在被试间随机分配设计。 |
| B2 | 被试内设计 | NA | — | 无重复测量/被试内条件顺序设计。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合设计，也无混合模型误差项。 |
| B4 | 因子设计 | NA | — | 无实验因子设计；模型/语料比较是观察性分组，未做完全交叉的因子设计及交互检验。 |
| B5 | 主效应 | NA | — | 无因子设计中的主效应检验。 |
| B6 | 交互作用 | NA | — | 无实验交互项、简单主效应或交互图误差棒。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不是干预性准实验研究；作者未声称因果处理效应，也无准实验类型、选择偏差缓解或因果推断结构。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内设计，不涉及处理可逆性与迁移对称性。 |
| C1 | 随机化 | NA | — | 研究单位没有被分配到互斥处理条件；语料来源为既有分组，无随机化或分配隐藏问题。 |
| C2 | 平衡 | NA | — | 无条件顺序需要平衡。 |
| C3 | 恒定 | 1 | PDF p.3/9043：ERG release与ACE版本明确；PDF p.3/9043：“the latest version of the ERG... and ACE”；PDF p.10/9050：讨论“only one genre (NYT-style news)”与“only about English”的外部效度限制。 | 明确固定了语法/解析器版本、语料语体与语言，并在局限中说明外部效度边界；恒定变量及水平有报告。 |
| C4 | 匹配 | NA | — | 未使用匹配设计；无匹配变量、匹配方法或匹配后均衡性检验。 |
| C5 | 纳入为变量 | 0 | PDF p.3/9043：“LLM-generated datasets have more sentences, but the sentences written by humans are longer”；此后分析未将句长/文档长度作为协变量或区组纳入模型。 | 已提及句长差异这一已知混淆，但没有测量后纳入分析模型、做区组/协变量控制或报告调整后效应；按规则记0。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者需要盲法；解析与计数为自动化流程。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序，因此无平衡层级选择问题。 |
| D1 | 练习效应 | NA | — | 不是重复试次的学习/练习实验；语料分析无练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类session、休息间隔或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨时间/跨条件交叉处理，不存在清洗期或迁移效应。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件顺序，不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 无主观量表绝对判断或范围效应校准问题；因变量为文本计数/多样性指数。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无刺激/选项/处理顺序操纵；文本顺序不作为随机化或反平衡的实验因素。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试、指导语或需求特征；LLM生成语料为既有数据。 |
| E5 | 实验者效应 | NA | — | 数据采集与解析完全自动化，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | NA | — | 主要因变量为余弦相似度和多样性指数，不是有明确端点正确率/任务难度的测量；无天花板/地板校准需求。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念量表测量，无共同方法偏差的同源自评问题。 |
| F1 | 统计结论效度 | 0.5 | PDF p.5/9045：“We have run the Mann-Whitney U-test... when we apply FDR correction... none... significant”；PDF p.7/9047：报告H值（如human 3.342 vs LLM 3.221–3.284）及“permutation test with 10,000 resamples... p < 0.01”。 | 报告了部分效应/描述性指数、p值与FDR校正，但无置信区间、无样本量/功效依据，也未系统报告所有分析假设检验；统计结论效度报告不完整。 |
| F2 | 内部效度 | NA | — | 非实验、无随机分配与因果推断主张；内部效度意义上的分配隐藏、基线等价与被试流向不适用。 |
| F3 | 构念效度 | 0.5 | PDF p.2/9042：ERG为“broad coverage precision grammar... parse 94% of reasonably well-edited English text”；PDF p.3/9043 Table 2报告NYT数据对ERG类型/规则的覆盖率；PDF p.4/9044报告多类HPSG分布。 | 有形式语法效度论证、覆盖率和多指标证据，但未报告解析/编码信度（如一致性检验），无实验操纵检验；构念效度证据不完整。 |
| F4 | 外部效度 | 1 | PDF p.3/9043 Table 1列出NYT、LLaMA/Falcon/Mistral数据来源、模型规模与训练token；同页说明NYT日期范围；PDF p.4/9044与p.9/9049比较WSJ、Wikipedia以检验跨语体/跨体裁持续性；PDF p.10/9050讨论仅英语、仅NYT-style的推广边界。 | 报告了样本来源、语料特征、跨语体/跨体裁比较与明确推广边界，外部效度报告较完整。 |
| G1 | 分析单位 | 0.5 | PDF p.5/9045：“we only have 9 datasets to compare”；PDF p.6/9046：对“12 authors that have more than 100 sentences”做作者层级比较。 | 统计分析主要在数据集/作者聚合层级进行，但未明确说明句子嵌套于文档/作者/模型的多层结构，也未使用多层模型；属于只用聚合处理的聚类结构。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；6个LLM与人类语料被视为固定比较组，无随机截距/随机斜率结构，也不以模型总体随机抽样为推断目标。 |
| G3 | 材料作为随机效应 | NA | — | 材料是ERG形式语法提供的穷尽类型/构式清单，不是从更大材料总体抽样的刺激项目；项目随机效应不适用。 |
| G4 | 统计功效 | 0 | 全文无事前功效分析或样本量/重复次数推导；结果主要报告p值与描述性指数，未见效应量置信区间。 | 无设计阶段功效分析，也无基于预期效应量的样本量论证；仅有事后描述性比较。 |
| G5 | 研究者自由度 | 0.5 | PDF p.5/9045：“we perform a large number of comparisons... FDR correction... none... significant”；PDF p.7/9047：“we focus on the most salient differences”；PDF p.8/9048：“We have selected such constructions based on the statistical significance”；Appendix D只列p≤0.05结果。 | 报告了主要语料/条件与部分排除/选择逻辑，但存在按显著性和“最显著差异”选择展示的自由度；未报告解析失败/剔除规则及全部因变量结果。 |
| G6 | 预先设定 / 预注册 | 0 | 全文无预注册声明、注册平台或分析计划；作者未区分验证性与探索性分析。 | 无时间戳早于数据收集的公开预注册，也未说明预注册偏离。 |
| J1 | 位置偏差 | NA | — | 不涉及LLM-as-judge、候选项选择/排序或成对比较位置偏差。 |
| J2 | 冗长偏差 | NA | — | 没有用LLM裁判评估生成质量，也没有把长度当作质量评分的LLM-judge设置。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或多轮纠错，不涉及谄媚偏差。 |
| J4 | 自我偏好 | NA | — | 未使用LLM-as-judge，不存在裁判自我偏好/同源偏差。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | LLM文本由既有数据生成，论文未使用few-shot in-context示例，也无示例选择/排列实验。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | PDF p.3/9043：“prompting them with the headlines together with the first 3 words of the lead paragraph”；PDF p.10/9050：“a lot depends on the prompt”。 | 仅描述提示内容，未提供完整prompt模板/版本、未做语义等价措辞敏感性消融，也未说明dev/test划分；按规则记0。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG设置，上下文远低于长窗口操控需求。 |
| J8 | 温度与采样随机性 | 0 | PDF p.10/9050：“An LLM will generate a different text every time”；全文未报告temperature、top-p、seed、重复采样次数或置信区间。 | 识别了LLM非确定性，但没有记录采样超参、种子或多次重复运行；LLM采样方差未纳入统计设计。 |
| J9 | 重复与文本退化 | 0 | PDF p.10/9050仅泛泛承认生成文本每次不同；全文未报告解码策略、repetition penalty、n-gram重复率或退化率。 | 虽涉及开放生成文本，但未报告解码策略与重复/退化QC，无法排除解码退化与语法分布差异混淆。 |
| J10 | 分词效应 | NA | — | 研究仅限英语单脚本，无跨语言/跨脚本或跨格式输入比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | PDF p.3/9043：“The LLMs they used were all released prior to October 1, 2023”；human NYT data为“between October 1, 2023, and January 24, 2024”；同页称可“make sure the LLMs did not have access”。 | 对NYT主数据做了训练截止与文章日期对照，但未做n-gram重叠/DCQ等污染检测；WSJ/Wikipedia等旧语料仍可能有训练重叠，污染率未报告。 |
| J12 | 基准饱和 | NA | — | 不是准确率基准接近饱和的评测；主要指标为分布相似度与多样性指数，无基准天花板问题。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，也无约束指令准确率测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/格式约束输出，无格式合法率与内容错误分离问题。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/对齐、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文是计算语言学/形式语法比较，不主张测量心理学或认知科学构念；不按LLM心理学被试范式编码。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 仅将LLaMA规模作为描述性分组，未报告能力随规模变化的曲线，也未宣称涌现/突变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对benchmark、奖励模型或LLM-judge等代理指标的优化训练，无overoptimization监控问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | PDF p.3/9043 Table 1给出模型名称/规模并发布解析数据，但未报告重复运行次数、置信区间、精确snapshot日期或配对检验；多数比较为单次语料分析。 | 可复现材料有部分公开，但缺少重复次数、CI、精确模型snapshot与配对统计；按J19基本要件未达成记0。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮生成文本分析，无多轮对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
论文核心贡献是方法学与描述性比较：形式语法解析流程清楚、数据与工具版本较可复现，并报告了多类HPSG指标与部分显著性检验。但作为观察性语料比较，随机分配、实验控制、因果推断与多层级统计均不适用或未做；对提示、采样、长度、模型/语料选择等混淆的控制有限，统计报告主要为描述性指数与p值，缺少置信区间与系统的稳健性分析。
