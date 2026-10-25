# article_014 | Do LLMs write like humans? Variation in grammatical and rhetorical styles | 2025

研究类型概述：观察性/比较性语料库语言学研究：以人类文本与六个 LLM 生成的平行 500 词文本块为分析单位，用 Biber 66 个语言特征、随机森林和 lasso 分类器及配对 Wilcoxon 检验比较人类与不同 LLM、基础模型与指令微调模型、不同语料/体裁间的文体差异。
- **研究构念（Construct）**：语法、修辞与文体变异行为（grammatical, rhetorical, and stylistic behavior）｜CA 构念锚定：句法加工（syntactic processing, `trm_4a3fd79d0b34b`）；句法分析（syntactic parsing, `trm_4a3fd79d0b340`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）
- **实验任务与范式（Task / Paradigm）**：观察性/比较性语料库语言学研究：以人类文本与六个 LLM 生成的平行 500 词文本块为分析单位，用 Biber 66 个语言特征、随机森林和 lasso 分类器及配对 Wilcoxon 检验比较人类与不同 LLM、基础模型与指令微调模型、不同语料/体裁间的文体差异。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_1: “We used six LLMs: GPT-4o and GPT-4o Mini ... and Meta Llama 3 8B, 70B, 8B Instruct, and 70B Instruct ... producing six LLM-authored texts for each human-authored text.” | 模型/文本来源是被明确命名并比较的分组变量，且列出至少两个水平与标签；但这不是随机分配的实验操纵，未报告操纵检验或分配方式，故为部分满足。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_1: “we used Douglas Biber’s tagset of 66 linguistic categories ... features include mean word length ... nominalizations ... agentless passive voice”及“paired Wilcoxon signed-rank test with Bonferroni”。 | 因变量指标和计分方式（66 个特征的出现率/分类器表现）界定清楚，并报告效应量与分类准确率；但未报告信度、效度证据或系统性的连续指标预处理/天花板地板说明。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_1: “from each text we extracted two consecutive chunks of roughly 500 words ... The first chunk was provided to each LLM ... prompted to write 500 more words in the same style, tone, and diction”。 | 报告了若干控制措施（同一前文、约 500 词长度、统一提示、相同模型版本），但未系统列出全部控制变量及控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_1: “As the instruction tuning processes are not publicly documented, it is not possible to determine the cause more precisely.” | 识别了指令微调、模型规模、训练数据/体裁等潜在混淆，并承认无法精确判定因果来源；但未做敏感性分析或系统控制残余混淆。 |
| A5 | 调节变量 | NA | — | 研究没有正式的调节变量理论模型或乘积项交互检验；模型规模/指令微调只是描述性比较，故不适用。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_1: “two consecutive chunks of roughly 500 words ... first chunk was provided ... prompted to write 500 more words ... Biber’s tagset of 66 linguistic categories ... All analysis code is available via the Open Science Framework”。 | 对文本切分、提示程序、生成长度、特征提取和分类分析给出了可复现的操作化描述，代码/语料亦公开。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_1: “six categories of text (academic, news, fiction, spoken word, blogs, and TV/movie scripts)”及六个 LLM 名称。 | 报告了模型/体裁的水平数与标签，但未系统说明各水平的类型（名义/等级/连续）、间距、全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_1: “A random forest classifier ... achieved a test accuracy of 66%”与“Lasso-penalized logistic regression classifiers attained similar performance”，并报告多特征出现率。 | 关键构念采用多指标/多分析策略（66 个特征、随机森林、lasso、词频）并报告了会聚性证据，符合多操作化要求。 |
| A10 | 单一方法的风险 | NA | — | 研究不使用自陈量表；文本来源是客观元数据，因变量由文本计算得到，不存在常见自评共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或 LLM 被试被随机分配到互斥实验条件；这是按文本来源分组的平行语料比较，不适用被试间实验分配逻辑。 |
| B2 | 被试内设计 | NA | — | 虽然每个提示文本对应多个模型输出，但这是配对/交叉语料结构而非有顺序条件的被试内实验；无顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合实验设计及相应误差项，故不适用。 |
| B4 | 因子设计 | NA | — | 研究未建立因子实验设计，也未报告设计矩阵与主效应/交互 ANOVA；模型与体裁比较是描述性/分类分析，不按因子设计编码。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验，故不适用。 |
| B6 | 交互作用 | NA | — | 无正式交互项统计检验，故不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机分配程序。 |
| B8 | 拉丁方 | NA | — | 无被试内条件顺序，未使用拉丁方。 |
| B9 | 准实验设计 | 0.5 | PDF_PAGE_1: “As the instruction tuning processes are not publicly documented, it is not possible to determine the cause more precisely.” | 模型/指令微调比较不可能随机分配，作者也承认因果判定受限；但未明确标注准实验类型、选择偏差来源或系统讨论内部效度威胁。 |
| B10 | 被试内设计的适用条件 | NA | — | 不是被试内处理设计，不涉及处理可逆性或迁移对称性。 |
| C1 | 随机化 | NA | — | 所有提示文本均生成六种模型文本，不以概率机制把文本分配到单一条件；无实验随机分配问题。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡，故不适用。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_1: “roughly 500 words ... first chunk was provided to each LLM ... prompted to write 500 more words”及固定模型版本。 | 报告了长度、提示、模型版本等恒定因素，但未系统列出全部恒定变量及其水平，也未讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | 0.5 | PDF_PAGE_1: “from each text we extracted two consecutive chunks ... first chunk was provided ... generated text was then compared to the next 500-word chunk of the human text.” | 按同一人类文本/前文进行配对匹配，报告了匹配变量与程序；但未报告匹配后均衡性检验或回归假象讨论。 |
| C5 | 纳入为变量 | 0.5 | PDF_PAGE_1: “Differences ... were tested ... with the paired Wilcoxon signed-rank test”；未将体裁等作为协变量纳入模型。 | 配对检验在分析层面控制了同一文本的配对变异，但未系统把已知混淆（如体裁/语料来源）作为协变量或区组并检验模型假设。 |
| C6 | 盲法 | NA | — | 没有人类被试、主试或人类评分者，采用自动化文本特征提取，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | LLM 每个文本的生成不构成跨条件学习或练习块；无人类练习效应控制问题。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长或疲劳安排；自动化批处理不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个生成文本可按独立上下文理解，无跨条件清洗期或迁移污染问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉条件，不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为文本特征计数/率与分类器指标，不是主观量表，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选/排序刺激或 LLM-as-judge 选项位置；文本块顺序是续写设计的固有结构，不是可平衡的处理顺序。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中间反应倾向。 |
| E4 | 需求特征 | NA | — | 无人类被试参与，不存在人类需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | 无人类主试/评分者参与，自动化文本采集与分析。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_1: “Fig. 3 illustrates ... rate of occurrence ... relative to human text”及“A random forest classifier ... achieved a test accuracy of 66%, compared to an expected accuracy of 14%”。 | 报告了特征出现率分布、词频分布和分类准确率，可部分排查端点问题；但未报告偏度/端点频率或 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念测量，IV 与 DV 也不是同源自评，故不适用。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_1: “paired Wilcoxon signed-rank test with Bonferroni multiple comparison correction”与“paired Cohen’s d=1.38”等效应量。 | 报告了效应量与多重比较校正，但未报告置信区间、事前样本量/功效分析，统计假设检验细节也不完整。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_1: “after these were removed, there were n=8,290 HAP-E texts ... with outputs from all LLMs”及配对比较设计。 | 报告了排除不可用输出并采用配对设计，但没有随机分配、分配隐藏、基线等价检验或完整被试/文本流向；内部效度威胁仅部分讨论。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_1: “Biber’s tagset of 66 linguistic categories”及随机森林/lasso 分类结果；未报告评分者信度或操纵检验。 | 使用成熟语言特征体系并报告分类器效标表现，但缺少正式信度、效度证据和操纵检验；多操作化有报告。 |
| F4 | 外部效度 | 1 | PDF_PAGE_1: “six categories ... HAP-E ... COCA ... CAP ... M4 parallel corpus ... generalizability across LLMs or to different registers of text is difficult.” | 报告了多语料来源、体裁范围，并用 CAP 与 M4 做跨语料/跨模型泛化检验，同时明确讨论推广边界。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_1: “from each text ... two consecutive chunks”及“With two human chunks and six LLM-authored chunks for each text, HAP-E comprised n=66,320 chunks”。 | 说明了文本块的分析单位和每文本多输出的结构，并用配对检验处理部分配对；但未用多层模型显式处理文本块嵌套于文档/提示的聚集结构。 |
| G2 | 随机效应 | 0 | PDF_PAGE_1: “paired Wilcoxon signed-rank test”与随机森林分析；未报告随机效应结构。 | 分析未包含随机效应模型，也未说明哪些因子为随机/固定；文本/提示层面的聚集方差未被显式分离。 |
| G3 | 材料作为随机效应 | 0 | PDF_PAGE_1: 使用 66 个特征和随机森林/lasso，但未报告 (1&#124;item) 或材料随机效应。 | 材料/文本被视为大量样本并做跨语料检验，但统计模型没有把材料/项目作为随机效应，不能从模型层面保证推广到材料总体。 |
| G4 | 统计功效 | 0.5 | PDF_PAGE_1: 报告“paired Cohen’s d=1.38”等效应量；未报告事前功效分析或置信区间。 | 有效应量报告，但无设计阶段功效分析、目标功效或样本量推导。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_1: “after these were removed, there were n=8,290 ...”；所有特征见 SI Appendix Table S4，代码公开；未明确区分验证性与探索性分析。 | 报告了排除不可用输出、全部特征和分析代码，但排除数量/规则细节不完全，且未系统区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | PDF_PAGE_1: 仅报告 OSF 分析代码 deposited 2024-12-12，未提及时间戳早于数据收集的预注册。 | 无预注册；不能判断主要假设和分析计划是否事先固定，故为 0。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM 多项选择、排序或成对裁判，无候选位置偏差问题。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评价生成质量；长度控制是文本块构造，不是裁判长度偏差。 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈对话，不涉及谄媚。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 或自我偏好评估。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 提供的 500 词前文是文体续写上下文，不是带标签的 few-shot 示例；未涉及示例标签比例与排列反平衡。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_1: “See SI Appendix for detailed prompt information”与致谢“Aadi Menon for exploring suitable prompts”。 | 提示模板/探索信息有部分交代，但主文未展示完整模板，且未报告版本化敏感性消融或 dev/test 分离；只能算部分满足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文仅约 500 词，远低于长上下文/RAG 设置，无中间迷失问题。 |
| J8 | 温度与采样随机性 | 0 | PDF_PAGE_1: 仅说明每个模型“producing six LLM-authored texts for each human-authored text”，未报告 temperature、top-p、seed 或重复采样。 | LLM 生成存在采样随机性，但未报告任何采样超参、种子或每条件重复次数与方差，无法评估非确定性。 |
| J9 | 重复与文本退化 | 0 | PDF_PAGE_1: 脚注“Llama base models have a tendency to repeat themselves”及“Here is the continuation...”伪影，但未报告解码策略或 repetition penalty。 | 识别了重复/退化伪影，但未报告解码策略、重复率 QC 或条件间解码一致性，核心做法缺失。 |
| J10 | 分词效应 | NA | — | 单一英语、单脚本研究，无跨语言/跨脚本分词比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 不是标准基准评测；主要使用新建/平行语料与生成文本，不以公开测试集分数推断泛化能力。 |
| J12 | 基准饱和 | NA | — | 不涉及基准饱和或接近天花板的能力基准。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，也未测量约束类型准确率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/JSON 输出，无格式合法率问题。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全、越狱或对齐评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究是语料库语言学/文体比较，不主张测量 LLM 的心理学或认知科学构念；LLM 被视为文本生成器而非心理学被试。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随规模/训练进展的涌现能力曲线，也未宣称涌现；仅描述性比较 8B/70B 与 base/instruct。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对代理指标进行训练、RL 或 best-of-N 优化，无奖励过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_1: 列出 GPT-4o、GPT-4o Mini、Llama 3 8B/70B/Instruct 并注明访问日期“Accessed 16 October 2024”；语料和代码公开，但未报告重复采样与置信区间。 | 提供了较明确的模型变体和访问日期、配对检验及代码，但每个文本/模型只生成一次，未报告重复次数 N、95% CI 或逐题敏感性分析。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究为单轮续写生成，无多轮对话历史累积，不涉及轮次一致性衰减。 |

## 编码小结
该研究不是随机分配的人类被试实验，而是基于既有/生成文本的平行语料比较；因此许多人类被试分配、顺序平衡和实验者效应组件不适用。核心比较清晰、语料和代码公开，但提示词敏感性、解码采样、重复运行与嵌套文本结构未充分处理，部分构念效度和可复现性信息不足。
