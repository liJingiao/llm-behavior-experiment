# article_179 | Measuring And Improving Persuasiveness Of Large Language Models | 2025

研究类型概述：该文构建 PersuasionBench 与 PersuasionArena，利用企业社交媒体自然实验构造 transsuasion 配对数据，评测多种 LLM 的行为模拟、内容模拟、生成式 transsuasion、transcreation、人类作为判官与跨域迁移能力，并用指令微调比较不同训练条件。分析单位主要是 tweet/pair、模型生成结果与 LLM/人类评估结果，而非人类被试条件分配实验。
- **研究构念（Construct）**：说服性语言、受众适配与传播效果预测｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；态度（attitude, `trm_4a3fd79d09947`）
- **实验任务与范式（Task / Paradigm）**：让现成GPT、Llama等模型判断、预测、改写和生成不同受众与传播条件下的说服文本，并通过PersuasionArena由人类比较模型与人类文本。（改变模型、内容、受众、时间、低高互动文本配对、生成或判断任务和人类评价条件。）｜CA 任务锚定：类比推理任务（analogical reasoning task, `trm_4f244f0286947`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.9 “We start with Vicuna-1.5 13B ... instruction fine-tune it with instructions created using 3 million unique tweets under the following settings”；p.19 Table 2/3 列出不同模型、训练配置与 0/5/10-shot 条件。 | 训练组合与模型/设置比较可视为受控自变量，水平与标签有报告；但未报告操纵检验，且 LLM 条件的“分配”并非随机被试分配，故只算部分完整。 |
| A2 | 因变量 | 0.5 | p.7 “we use accuracy to report the results”；“BLEU-1, BLEU-2, ROUGE-1, ROUGE-L, and BERTScore”；p.7 Oracle-as-a-judge 与 Elo 评分；p.30 人类偏好任务报告 accuracy 与 cumulative probability。 | 因变量指标与计分方式基本明确，但未系统报告测量信度/效度、连续指标预处理或防天花板/地板说明。 |
| A3 | 控制变量 | 1 | p.5 “tweets within the pair do not differ by more than 45 days ... content similarity”；p.23 描述用户名过滤、新闻过滤、<100 tweets 或 >10 tweets/day 排除、人工过滤等步骤。 | 系统报告了同一账号、时间窗、语义/编辑相似度、账户类型、发帖频率等控制变量及其过滤手段。 |
| A4 | 混淆变量 | 1 | p.16 FAQ “To mitigate confounds, we applied multiple filtering steps ... ensuring high semantic similarity and temporal nearness ... manually verifying”；p.25 D.4.1 分析时间特征并对品牌分层；p.26 Table 7 显示过滤后时间解释力 R2=0.013。 | 识别并控制了品牌、时间、内容相似度等潜在混淆，并报告时间残余影响的敏感性分析；仍有未控制外部因素，但编码要求的核心项已达成。 |
| A5 | 调节变量 | NA | — | 论文没有明确设定调节变量及相应交互假设/交互检验；模型规模与训练方式的比较是描述性/推断性比较，不构成正式调节模型。 |
| A6 | 中介变量 | NA | — | 论文未提出或检验中介变量与直接/间接效应分解，不适合按中介分析编码。 |
| A7 | 操作性定义 | 1 | p.3 定义 transsuasion 为保持 sender/receiver/time/channel 不变而改变行为结果；p.7 说明各类任务输入输出及评估；p.46-p.50 提供完整 prompt listings。 | 关键构念、任务输入输出、评估指标与生成 prompt 均有可复现操作化，足以供他人复现主要流程。 |
| A8 | 水平数与类型 | 0.5 | p.10 §4 列出 CS+BS、CS+BS+TS、Ours-Instruct、DPO、7B/13B 等训练条件；p.19 Table 2 列出 0/5/10-shot；Table 3 列出多种 transsuasion 任务与迭代次数。 | 各分类水平取值与标签有报告；但未集中说明水平类型、水平间距/全距，连续变量中心化等亦不适用或未报告。 |
| A9 | 单一操作化的风险 | 1 | p.10 “PersuasionArena exhibits a strong rank correlation (0.69 Kendall’s Tau) across these tasks”；p.30 人类研究结果与基准排序一致性比较。 | 关键构念“persuasiveness”采用 NLP 指标、Oracle Elo、人类判官、跨域迁移等多种操作化，并报告会聚证据。 |
| A10 | 单一方法的风险 | 1 | p.4 列出四类测试机制：conventional metrics、Oracle-LLM-as-a-judge、Human-as-a-judge、domain-shift tasks；p.10 报告跨任务排序相关。 | 研究明确采用多种方法来源评估不同构念，并报告跨方法/跨任务一致性，因此不存在单一方法同源问题。 |
| B1 | 被试间设计 | NA | — | 不存在人类被试被分配到独立条件的人类被试间实验；LLM 模型/训练条件比较不是人类被试分配设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试重复接受所有条件的被试内设计；同一测试集被多个模型评估不等于被试内条件顺序设计。 |
| B3 | 混合设计 | NA | — | 论文没有逐因素标注组间/组内的混合实验设计，也没有对应混合 ANOVA 分析。 |
| B4 | 因子设计 | NA | — | 论文进行多模型、多任务、多 shot 的基准比较，但没有构建完全交叉的因子实验设计矩阵，也未报告因子交互项；因此不按 B4 的因子实验编码。 |
| B5 | 主效应 | NA | — | 不存在按 B4 定义的因子设计主效应检验，故无适用主效应统计量。 |
| B6 | 交互作用 | NA | — | 不存在正式因子设计中的交互项检验与简单主效应分析。 |
| B7 | 区组设计 | NA | — | company-stratified/time-stratified 抽样用于测试集构造，不是实验处理分配的区组设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡被试内条件顺序的设计。 |
| B9 | 准实验设计 | 0.5 | p.3 “perfect controlled experiments are impractical at scale ... natural experiments”；p.5 同账号、45 天窗口、相似度阈值配对；p.25 分析时间残余影响。 | 明确采用自然实验/非随机设计并做了匹配和残余时间分析，但未系统讨论因果推断局限与所有内部效度威胁，故为部分满足。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理顺序设计，不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥处理条件；虽然测试集按账号/时间抽样，但这不是处理随机化与分配隐藏。 |
| C2 | 平衡 | NA | — | 没有条件顺序需要平衡，不属于顺序平衡设计。 |
| C3 | 恒定 | 0.5 | p.5 控制同一账号、45 天内发帖、内容相似度；p.55 局限中说明仅英语、单次说服、未研究受众依赖。 | 报告了若干被恒定/限制的变量及外部效度限制，但未以统一控制变量清单逐一列出所有实验环境/模型调用条件。 |
| C4 | 匹配 | 0.5 | p.5 “same username ... do not differ by more than 45 days ... content similarity thresholds”；p.6 Table 1 给出 cosine/edit/image similarity 阈值。 | 报告了匹配变量与阈值/程序，但无正式匹配后均衡性检验，也未讨论回归假象风险。 |
| C5 | 纳入为变量 | 0.5 | p.25 将 hour/day、brand 纳入时间影响分析；p.25 Table 5/6 报告 like difference 与 time difference 的相关。 | 已知混淆时间被测量并作补充分析，但未在主要模型比较中作为协变量/区组纳入调整，也未报告斜率齐性等假设检验。 |
| C6 | 盲法 | NA | — | 人类用户在产品中自然反馈，未进行比较条件盲法；LLM Oracle 不是需要人类盲法的主试/评分者场景。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 等顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 每条件生成任务没有传统练习块或跨试次学习设计；multi-iteration 是生成改进迭代，不是练习效应控制。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长、休息间隔或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件残留/清洗期问题；跨域任务用于迁移验证，不是同一被试的条件间残留。 |
| D4 | 不对称迁移 | NA | — | 不存在被试内条件顺序或不对称迁移检验。 |
| D5 | 范围效应 | NA | — | 主要因变量为客观准确率、Elo、NLP 指标与人类行为结果，不涉及量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.6 “To eliminate positional bias ... we compute results on both pairs (T1,T2) and (T2,T1).” | 对成对比较做了位置反平衡，是核心做法；但未报告翻转率、各位置正确率或更完整的顺序分配细节。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表；人类反馈是 upvote/downvote 与原因选择，不是正反向计分量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表跨群体比较或反应风格分析。 |
| E4 | 需求特征 | 0 | p.8 描述与 Fortune 500 公司合作，让 20,000+ 用户使用应用并给出 upvote/downvote/评论；p.20 Figure 4 展示反馈流程。 | 存在人类用户反馈数据，但全文未报告掩饰情节、单盲程序或事后访谈检查需求特征。 |
| E5 | 实验者效应 | NA | — | 人类反馈通过产品自动采集，无人类主试/评分者面对面施测；LLM 评估亦无实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.19 Table 2/3 报告准确率与 Elo；p.30 Table 9 报告部分均值±误差；但未报告偏度或端点频率。 | 报告了主要指标均值/部分离散度，但没有系统报告分布形态、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不属于同源自陈式多构念测量，IV/DV 来源并非自评量表同源结构。 |
| F1 | 统计结论效度 | 0.5 | p.19 Table 3 报告 Elo 与胜率换算；p.10 “38 elo ... 160 elo ... win rates 55.45% and 71%”；p.30 Table 9 有 ±。 | 报告了效应量/胜率与部分不确定性，但缺少样本量确定依据、统一 95%CI 与多重比较校正说明。 |
| F2 | 内部效度 | 0.5 | p.3 明确自然实验近似受控条件；p.5 给出配对流程；p.23 给出数据过滤与样本量变化；p.25 分析时间混淆。 | 报告了分配/配对程序与部分内部效度分析，但没有随机分配、分配隐藏、基线等价性或完整 flow/损耗处理。 |
| F3 | 构念效度 | 0.5 | p.10 报告跨任务 Kendall’s Tau=0.69；p.30 人类判官与基准结果一致性；p.34 用 NER/factuality/metrics match 做额外效度检查。 | 有多操作化与部分会聚/效度证据，但缺少正式信度统计、manipulation check 与传统构念效度分析。 |
| F4 | 外部效度 | 1 | p.5 说明数据来自 Wikipedia 企业账号与 Twitter 企业推文；p.30 报告跨域迁移结果；p.55 限制部分讨论英语、单次说服、未研究受众依赖。 | 报告了样本来源、跨情境迁移与明确推广边界，符合外部效度核心要求。 |
| G1 | 分析单位 | 0.5 | p.4 测试集按 randomly chosen accounts（company-stratified）和时间分层；p.6 以 tweet pairs 计算 accuracy；p.19 以模型为单位汇总准确率/Elo。 | 说明了数据/测试划分层级，但统计分析按 tweet/pair 独立汇总，未说明品牌/账号/时间聚类或嵌套结构如何进入模型。 |
| G2 | 随机效应 | 0 | p.19 Table 2/3 只报告 accuracy/Elo；p.30 Table 9 报告均值±误差；全文无混合模型随机效应结构说明。 | 若需将结论推广到推文/品牌/时间总体，应处理这些抽样层级；但论文只做固定模型间描述性比较，未报告任何随机效应模型。 |
| G3 | 材料作为随机效应 | 0 | p.6 使用具体 tweet pairs 作为测试材料并报告 accuracy；p.19 结果未同时考虑 item 随机效应或准 F 比。 | 有限具体推文被当作固定测试材料，结论欲推广到材料总体，但分析中未将材料/项目作为随机因子。 |
| G4 | 统计功效 | 0.5 | p.10 报告 Elo 差值与胜率换算；p.19 Table 2/3 报告准确率/Elo；未报告事前功效分析或样本量推导。 | 报告了部分效应量，但缺少设计阶段功效分析和依据；符合“有效应量但缺事前功效分析”的部分满足。 |
| G5 | 研究者自由度 | 0.5 | p.5 详细列出推文过滤与样本量变化；p.9 列出训练配置；p.21 说明人类反馈过滤；但未明确区分验证性与探索性分析。 | 报告了主要排除规则、任务和条件，但未完整说明所有分析的事前/探索性质与停止规则，部分研究者自由度仍不清楚。 |
| G6 | 预先设定 / 预注册 | 0 | p.1-p.56 全文未见预注册平台、注册编号或分析计划。 | 无预注册，也未说明实际分析与预注册偏离；按口径记 0，而非 NR。 |
| J1 | 位置偏差 | 0.5 | p.6 “To eliminate positional bias ... compute results on both pairs (T1,T2) and (T2,T1).”；p.7 Oracle-as-a-judge 与 arena Elo。 | 成对比较做了位置反平衡，但未报告交换前后偏好翻转率、各位置正确率；裁判模型版本有部分报告，采样参数与 prompt 版本信息不完整。 |
| J2 | 冗长偏差 | 0.5 | p.7 Oracle LLM 评估生成内容；p.17 FAQ 称 “Linguistic features like emojis, hashtags, and length have minimal correlation with persuasiveness”。 | 使用 LLM 裁判评估开放生成，并提到长度等表面特征影响小，但未见裁判 rubric 的长度控制，也未报告长度—得分相关系数或长度对照。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场操纵或多轮纠错反馈；人类 upvote/downvote 是自然反馈，不构成 sycophancy 评估。 |
| J4 | 自我偏好 | 0 | p.7 “We train an Oracle LLM (Vicuna-1.5-13B) ... Oracle is then asked to rate ...”；p.9 被评模型包括 Vicuna-1.5-13B 及基于 Vicuna 的 Ours。 | Oracle 与被评模型同源/同家族，存在自我偏好风险；未采用异源裁判陪审、匿名化或自我偏好偏差量化，直接用同源 Oracle 作主要裁判，故记 0。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.7 “5-shot ICL using randomly sampled high-liked tweets”；p.9 Blog 任务给 10 个同作者 ICL 样本；p.48 Listing 11 给出模板。 | 报告了示例来源与数量并公开模板，但未报告标签比例、排列反平衡、多 seed 重采样或示例未取自测试集的系统证明。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.46-p.50 Listings 3-14 公布 Behavior/Content/Transsuasion 等 prompt 模板；p.47 Listing 3 system prompt。 | 提供了完整模板，但未报告 prompt 版本号、敏感性消融、dev/test 划分或 prompt 调优过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务上下文为短推文、图片描述和有限 ICL 示例，不涉及长文档/RAG 与中间迷失风险。 |
| J8 | 温度与采样随机性 | 0 | p.9-p.10 报告模型名称与训练设置，但全文未见 temperature、top-p、top-k、seed、重复采样次数或置信区间说明。 | LLM 非确定性采样参数与重复运行基本未报告，无法判断采样随机性对结果的影响。 |
| J9 | 重复与文本退化 | 0 | p.48 Listing 11 为开放生成 transsuasion prompt，但全文未说明 greedy/beam/sampling、repetition penalty、重复/退化率。 | 开放生成任务存在重复与文本退化风险，但未报告解码策略或退化 QC 指标。 |
| J10 | 分词效应 | NA | p.55 “We focus on the English language in the current work”；无跨语言/跨脚本比较。 | 单语言英语研究，无分词器跨语言 token 长度混淆风险，故不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.17 FAQ “Our dataset consists of recent tweets, ensuring they are outside the pretraining knowledge cutoff for models like LLaMA-2 ... no instances ... in Vicuna’s supervised fine-tuning datasets.” | 报告了对训练截止期和 Vicuna SFT 重叠的初步检查，但未系统做 n-gram/DCQ 污染检测或报告污染率。 |
| J12 | 基准饱和 | NA | p.19 Table 2/3 给出 random/baseline/topline，最佳分数未接近 100%（如 BS 最高约 68.5，TS-CT 最高约 82.3）。 | 这是新构建基准，分数未接近上限，无饱和风险；虽然报告了量程/水位，按规则可记 NA。 |
| J13 | 指令遵循 | NA | — | 研究不以通用指令遵循能力为因变量；生成任务有格式/约束，但由本章 J14 处理，不能算指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.47 Behavior Simulation prompt “Give me the label only and nothing else”；p.48 Comparative Transsuasion “Answer with A or B only”。 | 报告了严格格式约束的 prompt，但未报告格式合法率、重试策略，也未将格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 论文讨论说服的伦理风险，但没有安全/越狱评估或有害请求攻击成功率设置。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.6 设 simulative capabilities，要求模型模拟人类行为；p.30 与人类作为 judges 的转移结果比较；p.55 讨论推广限制。 | 论文确实把 LLM 用于模拟人类说服行为并与人类研究对照，但没有系统论证 LLM 上构念与人类同名构念的异同与构念效度边界。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文比较不同规模模型的说服力，但没有报告连续规模/训练进展曲线，也未宣称突然涌现；不构成绩效曲线与指标诱导假象评估。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | p.7 Oracle 在包括 train/test 的完整数据上训练；p.10 用人类研究与跨域任务验证；p.17 FAQ 承认 Oracle 包含测试数据。 | 优化目标涉及 likes/engagement 代理与 Oracle 评分，评估侧有人类/跨域验证，但未画代理分数与真实 gold 分数的 overoptimization 双曲线，且 Oracle 与测试数据重叠，独立性不足。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.19 Table 2/3 报告准确率/Elo；p.30 Table 9 报告 ±；p.10 用 Bayes-Elo 换算胜率。 | 有部分重复/变异性信息与模型版本名，但多数主结果无重复次数 N、95%CI、精确 API snapshot/日期与配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 多轮迭代是同一推文的生成改进，不是带对话历史的多轮交互评估；论文也未主张多轮部署一致性。 |

## 编码小结
论文是大型 LLM 基准、自然实验数据构建与模型训练评估研究。对构念操作化、多方法评估和跨域验证报告较充分，但多数实验设计、随机化、功效分析、预注册、采样随机性、LLM 裁判偏差控制等未完整报告；对自然实验内部效度有一定控制与敏感性分析，但因果推断与现实推广边界仍有限。
