# article_047 | Characterizing Similarities and Divergences in Conversational Tones in Humans and LLMs by Sampling with People | 2024

研究类型概述：该研究是混合人类与 GPT-4 的 Sampling with People 心理语言学表征研究：通过迭代生成/标注、质量匹配评分、相似性判断、特征评分及跨域对齐基准，比较人类与 GPT-4 的会话语调表征。分析单位为人类参与者/评分与 GPT-4 查询/采样链，不是传统随机对照实验。
- **研究构念（Construct）**：对话语气、效价与人机心理语言学表征（conversational tone, valence, and cross-human/LLM psycholinguistic representation）｜CA 构念锚定：情绪（emotion, `trm_4a3fd79d0a17f`）；情绪识别（emotion recognition, `trm_4a3fd79d0b665`）；共情（empathy, `trm_4a3fd79d0b67d`）
- **实验任务与范式（Task / Paradigm）**：该研究是混合人类与 GPT-4 的 Sampling with People 心理语言学表征研究：通过迭代生成/标注、质量匹配评分、相似性判断、特征评分及跨域对齐基准，比较人类与 GPT-4 的会话语调表征。分析单位为人类参与者/评分与 GPT-4 查询/采样链，不是传统随机对照实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4 (p.4)： “perform two tasks ... (1) elicit a sentence ... (“S” task), and (2) annotate a conversational tone ... (“T” task)”；p.15 (p.15)： “participants were randomly assigned to either annotate ... or create ...”。 | S/T 任务被明确命名并给出两个水平，且报告了随机分配；但主比较的人类/GPT 不是随机操纵，且无操纵检验，故只部分满足。 |
| A2 | 因变量 | 0.5 | p.4 (p.4)： “Participants rate the strength ... using a Likert scale, resulting in 16,000 rating judgments”；p.5 (p.5)： “split-half reliability ... humans: r = 0.91 ... GPT: r = 0.87”。 | 因变量指标与计分方式清楚，且报告了信度；但缺少系统效度证据及连续指标预处理/天花板地板说明，完整性不足。 |
| A3 | 控制变量 | 0.5 | p.4 (p.4)： “human and GPT-4 experiments were otherwise identical in their design”；p.15 (p.15)： “We always used a temperature of 0.8 ... GPT-4 (the June 13th, 2023 release)”；p.4 还报告人类/GPT 句子各取 40 条形成 balanced corpus。 | 报告了若干控制措施（同流程、同提示、固定温度与版本、平衡语料），但没有系统列出全部控制变量及逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | p.9 (p.9)： “we did not test a wide variety of LLMs and LLM parameters, including varying the prompt and temperature”；p.7 (p.7)： “monotone response that GPT provides in similarity judgments”。 | 识别了模型/参数和 GPT 单调作答等潜在混淆，并在局限中讨论；但未做控制方式或敏感性分析，残余威胁讨论不完整。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量假设，也没有交互检验；特征维度用于解释 MDS 变异，不作为调节变量。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或中介假设。 |
| A7 | 操作性定义 | 1 | p.2-4 (p.2-p.4)：详细定义 conversational tone、S/T 任务、质量控制评分、相似性判断和特征评分；p.15-21 (p.15-p.21) 给出完整说明和 GPT prompts。 | 关键构念均有可观测、可重复执行的操作化程序和提示模板，足以复现。 |
| A8 | 水平数与类型 | 0.5 | p.4 (p.4)： “40 tones and 80 sentences”；p.15 (p.15)： “90 SP sampling chains, each with 100 iterations”；p.20 (p.20) 给出 S/T prompts。 | 报告了任务水平与刺激数量/标签，但没有系统说明水平类型、间距/全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 1 | p.5-7 (p.5-p.7)：同时使用质量匹配评分、直接相似性判断和特征评分；p.7 报告两种相似性矩阵相关 “humans: r = 0.76 ... GPT: r = 0.83”。 | 关键构念采用多种操作化，并报告了会聚证据；满足单一操作化风险控制要求。 |
| A10 | 单一方法的风险 | NA | — | 研究使用生成、质量匹配评分、相似性判断和特征评分等不同任务渠道，没有同源自评多构念的共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 人类与 GPT 是观察性比较组，不是把分析单位随机分配到互斥实验条件；无传统被试间条件分配设计。 |
| B2 | 被试内设计 | NA | — | 参与者完成若干试次但不是接受某个完整被试内因子的全部水平；无完整被试内条件设计和顺序平衡方案可编码。 |
| B3 | 混合设计 | NA | — | 没有逐因素标注组间/组内的混合设计，也没有对应混合模型或两类误差项。 |
| B4 | 因子设计 | NA | — | 研究不是多因素完全交叉因子实验，未呈现设计矩阵和主效应/交互 ANOVA 表。 |
| B5 | 主效应 | NA | — | 无因子设计主效应检验。 |
| B6 | 交互作用 | NA | — | 无因子设计交互项检验。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机分配。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 虽然人类/GPT 非随机分组，但论文未将其作为准实验因果设计，也不作准实验因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有需要论证处理可逆性/迁移对称性的被试内处理条件设计。 |
| C1 | 随机化 | 0.5 | p.15 (p.15)： “each trial, participants were randomly assigned to either annotate ... or create ...”；p.17 (p.17)： “participants are shown a random item from each pool of examples”。 | 报告了随机分配/随机抽取，但未报告随机数生成工具、分配隐藏或随机化后基线检验。 |
| C2 | 平衡 | NA | — | 没有需要对条件顺序做平衡的互斥条件设计；采样链中 S/T 交替是 Gibbs 采样程序本身，不是待平衡的顺序效应设计。 |
| C3 | 恒定 | 1 | p.15 (p.15)： “We always used a temperature of 0.8 ... GPT-4 (the June 13th, 2023 release)”；p.15 还报告 Prolific、英国、英语母语参与者；p.9 讨论未变化 prompt/temperature 与单一模型的外部效度限制。 | 明确列出多项恒定变量及水平，并讨论其外部效度边界，满足完整性要求。 |
| C4 | 匹配 | NA | — | 没有匹配分配；人类/GPT 句子各随机取 40 条是平衡抽样，不是匹配变量设计。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型；句子来源通过平衡抽样处理。 |
| C6 | 盲法 | NA | — | 任务为在线自动化呈现，没有需要施盲的组别条件或人类评分者条件判断。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 等顺序平衡层级可选。 |
| D1 | 练习效应 | 0.5 | p.15 (p.15)： “Each human experiment began with detailed instructions and practice trials”；p.18 (p.18)： “two practice trials”。 | 报告了练习试次，但未报告练习结束标准、前段试次截除依据或试次位置协变量。 |
| D2 | 疲劳效应 | NA | — | 报告的人类实验为短时在线多试次任务（如 SP 每名参与者 10–12 trials），没有长 session 疲劳控制或明显疲劳风险设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 采样链中前一轮输出进入下一轮是目标机制；没有跨条件清洗期或治疗迁移设计，且每名参与者只看到上一轮输出。 |
| D4 | 不对称迁移 | NA | — | 没有交叉处理设计，也不检验迁移对称性；人类/GPT 为独立域。 |
| D5 | 范围效应 | 0 | p.4 (p.4)：质量匹配评分使用 “Likert scale”；p.15 (p.15) 相似性与特征评分也使用 1–5 Likert；p.5-7 跨人类/GPT 比较评分嵌入。 | 使用被试内多次 Likert 评分并跨域比较，但全文未讨论范围效应、未做被试间对照或范围偏差控制。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.15 (p.15)：试次随机指派为 S/T、示例随机抽取；p.17 (p.17)： “participants are shown a random item from each pool of examples”。 | 对示例和任务分配有随机化，但未报告刺激/配对呈现顺序的具体随机化或反平衡方案，也未说明各顺序分配。 |
| E2 | 默认赞同 | NA | — | 使用的是语调强度/相似性单题 Likert 评分，不是含正反向题的态度同意量表，默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | 0 | p.4 (p.4) 使用 1–5 Likert 评分；p.7 (p.7) 仅提到 GPT “monotone response”；未报告各评分分布的偏度或端点/中点使用比例。 | 未报告量表分数分布，也未对跨人类/GPT 的反应风格差异作校正；虽提到 GPT 单调作答，但不构成完整分布证据。 |
| E4 | 需求特征 | 0 | p.15 (p.15)： “Participants first receive instructions explaining what a conversational tone is and example sentences”；未报告掩饰情节或事后访谈。 | 参与者可推断研究关注会话语调，论文未使用 cover story 或 post-experimental inquiry 检查需求特征。 |
| E5 | 实验者效应 | NA | — | 数据收集由 PsyNet/在线平台与 GPT API 自动完成，无人类主试或人类评分者在场传递期望。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5 (p.5)： “all human-originated sentences had at least one conversational tone with an average rating exceeding 2.89, and exceeding a rating of 2 for 95% of GPT-originated sentences”；未报告各评分均值/SD/偏度/端点频率。 | 提供了端点相关的部分证据，但无完整分布或 pilot 难度校准说明。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；研究用多种任务并报告收敛效度，共同方法偏差不按该组件适用。 |
| F1 | 统计结论效度 | 0.5 | p.5 (p.5)：多处报告 “CI = [...] via bootstrapping”；p.9 (p.9)：对齐方法结果报告 r 及 CI。 | 报告了效应量/相关系数与置信区间；但无样本量确定依据/功效分析，也未说明多重比较校正。 |
| F2 | 内部效度 | 0.5 | p.15 (p.15) 报告随机指派 S/T 与随机示例；p.16 (p.16) Table 1 报告各实验样本量；未报告分配隐藏、基线等价检验或被试流向/损耗处理。 | 有部分分配程序与样本量报告，但内部效度威胁评估和流失处理不完整。 |
| F3 | 构念效度 | 0.5 | p.5 (p.5)：split-half reliability humans r = 0.91, GPT r = 0.87；p.7 (p.7)：直接相似性矩阵与质量匹配评分相关 humans r = 0.76, GPT r = 0.83。 | 报告了信度和收敛效度，并采用多操作化；但缺少正式操纵检验与更完整的构念效度论证。 |
| F4 | 外部效度 | 0.5 | p.15 (p.15)：Prolific、英国、英语母语、>18 岁；p.9 (p.9) 局限讨论只测英国参与者、有限模型/参数与有限采样链。 | 报告样本来源与推广边界，但未报告跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.15 (p.15)：90 条采样链，每链 100 iterations；p.5 (p.5)：相似性由 “vector of average ratings of all sentences” 计算。 | 说明了试次/链/参与者层级，但分析主要基于聚合评分和 bootstrap，未用多层模型显式分离嵌套方差。 |
| G2 | 随机效应 | 0.5 | p.5 (p.5)： “bootstrapping occurs with 5000 repetitions”；p.5 报告 split-half reliability；未报告混合模型随机效应结构。 | 通过重采样处理抽样不确定性，但未明确哪些因子为随机效应、哪些为固定效应。 |
| G3 | 材料作为随机效应 | 0.5 | p.4 (p.4)： “40 random sentences from each of the humans and GPT”；p.5 (p.5) 用 bootstrap/split-half 评估评分矩阵可靠性。 | 把句子作为抽样材料并用重采样评估稳健性，但未建立 (1&#124;item) 或准 F 比的材料随机效应模型。 |
| G4 | 统计功效 | 0.5 | p.5 (p.5) 报告 r 与 95% CI；p.9 (p.9) 报告对齐方法 r 与 CI；无事前功效分析。 | 报告效应量和置信区间，但缺少设计阶段功效分析或样本量推导。 |
| G5 | 研究者自由度 | 0.5 | p.18 (p.18) Table 2 列出句子/语调过滤标准；p.16 (p.16) Table 1 列出各实验响应数；未报告停止规则及验证性/探索性区分。 | 报告了排除/过滤规则和主要测量，但研究者自由度披露不完整。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–28 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告公开预注册、注册编号或数据收集前分析计划，也未声明为纯探索性研究。 |
| J1 | 位置偏差 | NA | — | GPT 用于生成/标注/评分，不是多项选择、排序或 LLM-as-judge 成对优劣判断；无候选位置偏差设计。 |
| J2 | 冗长偏差 | NA | — | 没有用 LLM 裁判比较开放生成质量或长度，不涉及冗长偏差。 |
| J3 | 谄媚 | NA | — | 没有用户立场、反馈或纠错式对话操纵，不涉及谄媚偏差。 |
| J4 | 自我偏好 | 0.5 | p.4 (p.4)：GPT-4 用于生成/采样，且 “GPT data underwent the same rating process with GPT agents as raters”；p.5 也由 GPT 评分。 | 同一 GPT-4 既生成又评分，存在自我偏好风险；论文未量化 favor-own-generation，也未报告匿名化/异源裁判分析，仅有部分人类评分对照。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.15 (p.15)： “There is a pool of 50 items for each type of example ... participants are shown a random item from each pool”；p.17 (p.17) 给出生成示例的 prompts。 | 报告了示例来源与随机抽取，但未报告多 seed 重采样、示例排列反平衡或各示例集结果分布。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.17-21 (p.17-p.21) 给出完整 GPT prompts；p.9 (p.9) 承认 “did not ... varying the prompt”。 | 公布了提示模板，但无版本化/敏感性消融/dev-test 划分说明，且承认未变化 prompt。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验上下文很短，无长文档或 RAG 设置，不涉及中间迷失/位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | p.15 (p.15)： “We always used a temperature of 0.8 ... GPT-4 (the June 13th, 2023 release)”；p.5 使用 bootstrap CI。 | 报告了 temperature 与模型版本，但未报告 top-p/top-k/seed，亦未对同一 prompt 重复采样并给出均值/CI。 |
| J9 | 重复与文本退化 | 0.5 | p.15 (p.15) 报告 temperature 0.8 与 chat completion mode；p.7 (p.7) 讨论 GPT 单调作答与句子空间中高重复。 | 部分报告了解码设置并定性讨论退化/重复，但未报告 repetition penalty、n-gram 重复率或截断比例。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本实验，无跨语言/跨脚本 token 数比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 使用自行诱导的全新句子/语调语料，不是公开标准知识基准；未做标准基准污染分析，也不属于该风险类型。 |
| J12 | 基准饱和 | NA | — | 对齐方法基准是自定义相似性恢复指标，不是接近天花板的公开能力基准。 |
| J13 | 指令遵循 | NA | — | 论文不以指令遵循为因变量；提示中的 “Respond only ...” 是输出约束，不是测量指令遵循能力。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.20 (p.20) prompts 要求 “Respond using only an adjective” 或 “Respond with only a number”；未报告格式合法率。 | 有输出格式约束及提示，但未报告格式失败率、重试策略或将格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.3-4 (p.3-p.4) 用同一 SP 范式比较人类与 GPT-4 的 conversational tone；p.15 报告 GPT-4 June 13, 2023 release；p.9 承认只测有限模型。 | 明确把 GPT 作为心理学式被试并做人类同范式对照，但只测一个模型且未系统论证 LLM 构念与人类构念的理论异同。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有随模型规模/训练进展的能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对代理指标进行训练/RL/best-of-N 优化，也不涉及奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4 (p.4)：GPT-4 为 “June 13th, 2023 release”；p.5 (p.5)：bootstrap 5000 次并报告大量 CI；p.25 (p.25) Table 3 注明 “aggregated across 100 seeds”；GitHub 链接公开数据与代码。 | 有模型发布日期、重复/CI 与代码数据链接，但未给精确 API snapshot/commit hash，也未系统报告配对检验或原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 不是多轮对话一致性实验；每次 GPT 提示仅使用上一轮输出，既不累积完整对话历史，也不测量逐轮一致性衰减。 |

## 编码小结
论文方法透明，材料、提示与数据代码公开，信度与收敛效度证据较充分；但核心是观察性比较与表征分析，缺少预注册、事前功效分析、完整顺序平衡/混合模型以及 GPT 采样超参细节，许多实验设计组件只能部分满足或对当前设计不适用。
