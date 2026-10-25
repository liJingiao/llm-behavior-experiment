# article_065 | Prompting Language Models for Linguistic Structure | 2023

研究类型概述：该文是计算语言学/LLM 行为评测研究：提出 structured prompting，在零样本与少样本下用自回归 PLM 做 POS、NER、chunking 序列标注，并比较模型规模、k-shot 数、标签形式、BIO 约束、预训练语料污染与标签先验等因素。分析单位是模型在固定评测样本和多次随机 demonstration 抽样上的输出，不含人类被试。
- **研究构念（Construct）**：语言结构知识与超越表面记忆的句法泛化（linguistic structure knowledge and generalization beyond surface memorization）｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）；句法加工（syntactic processing, `trm_4a3fd79d0b34b`）
- **实验任务与范式（Task / Paradigm）**：该文是计算语言学/LLM 行为评测研究：提出 structured prompting，在零样本与少样本下用自回归 PLM 做 POS、NER、chunking 序列标注，并比较模型规模、k-shot 数、标签形式、BIO 约束、预训练语料污染与标签先验等因素。分析单位是模型在固定评测样本和多次随机 demonstration 抽样上的输出，不含人类被试。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_3: “We use k = 10 sentences as demonstrations ... m = 5 runs”；PDF_PAGE_12 Table 6 报告 k=0,1,3,5,7,9；PDF_PAGE_6 报告 original/shuffled/proxy labels；PDF_PAGE_3 报告 125M–175B 多个模型。 | 多个条件及水平被明确命名并给出取值，但缺少形式化的单位分配说明和操纵检验；属于部分满足。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_2–3: POS 用 accuracy，NER/chunking 用 F1；PDF_PAGE_3: “We report the mean and standard error across m runs”；PDF_PAGE_12 Table 6 给出 means ± SE。 | 因变量指标与计分方式明确，但未报告心理测量式信度/效度证据，也未系统给出连续指标预处理或地板/天花板说明。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_3: “The evaluation subset is held fixed across all five runs, and ... fixed across models”；PDF_PAGE_2: prompt delimiter/format differences had little effect；PDF_PAGE_3: BIO constraints used。 | 报告了若干实际控制项和控制方式，但未形成系统控制变量清单，也未逐项说明所有控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_9 Limitations 讨论 data leakage；PDF_PAGE_6 报告搜索 Pile 并以 words/proxy labels 控制标签泄漏；PDF_PAGE_9 明确承认 GPT-3 与不可得预训练数据下无法完全控制污染。 | 识别并部分控制了预训练污染与标签先验等潜在混淆，也讨论了残余威胁，但缺少形式化敏感性分析。 |
| A5 | 调节变量 | NA | — | 本研究没有调节变量理论模型或交互检验；模型规模与 k-shot 的关系是描述性 scaling 分析，不作为调节假设。 |
| A6 | 中介变量 | NA | — | 没有中介变量、直接/间接效应分解或因果链假设。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_2: 逐步描述 structured prompting 算法——给定标签集合 L 与 context c，每步用 P_M(ℓ&#124;c,s_t) 取 argmax 并追加当前词与预测标签，多 token 标签用平均 log-likelihood；PDF_PAGE_3: 任务、标签格式与评测指标明确。 | 关键操纵与测量均有可复现的程序描述，达到操作化定义要求。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_3: 默认 k=10, m=5；PDF_PAGE_12 Table 6 给出 k=0,1,3,5,7,9；PDF_PAGE_3–4 给出模型规模与模型名；PDF_PAGE_6 给出 label sets。 | 大多条件的水平数与取值被报告，但未系统说明每个自变量的水平类型、间距/全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_6: 用 original, shuffled, proxy, words 多种标签操作化；PDF_PAGE_5: 报告 seen/unseen labels；PDF_PAGE_8 Table 3 报告不同标签集在各 class 上的 Spearman 相关。 | 关键构念采用多个任务与多种标签操作化，并报告了跨操作的会聚证据与相关模式。 |
| A10 | 单一方法的风险 | NA | — | 研究不使用人类自评量表，也不存在主观构念的同源自评 IV/DV 结构；prompt 操纵与 benchmark 指标不属于共同方法偏差范式。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或 LLM 被试被随机分配到互斥条件；模型比较是按模型规模/家族排列，不是被试间实验分配。 |
| B2 | 被试内设计 | NA | — | 没有明确的被试内重复测量设计与条件顺序平衡方案；同一模型跨条件评测属于 benchmark 网格，不是被试内实验。 |
| B3 | 混合设计 | NA | — | 没有逐因素标注组间/组内的混合实验设计，也没有对应的混合模型/重复测量 ANOVA。 |
| B4 | 因子设计 | NA | — | 没有完整交叉的因子设计、每格样本量与 ANOVA 交互表；模型、k、任务、标签集是分别分析或部分消融。 |
| B5 | 主效应 | NA | — | 无因子设计中的主效应 ANOVA 报告；文中比较主要是均值/SE 与消融差异。 |
| B6 | 交互作用 | NA | — | 没有交互项统计检验、简单主效应或交互图误差棒。 |
| B7 | 区组设计 | NA | — | 未使用区组设计或分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或对应顺序构造。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计，也没有非随机分组与因果推断限定。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有需要论证处理可逆性与迁移对称性的被试内处理设计。 |
| C1 | 随机化 | NA | PDF_PAGE_3 报告 demonstrations 与 test examples 随机抽样，但无处理条件分配程序。 | 随机抽样用于构造运行集和评测子集，不是把分析单位随机分配到互斥实验条件；分配隐藏/基线均衡不适用。 |
| C2 | 平衡 | NA | — | 无被试间/被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_3: fixed evaluation subset, fixed demonstrations across models, greedy top-1, k=10 default；PDF_PAGE_9 讨论 English-only 与 GPT-3 实验限制。 | 报告了若干恒定控制及其水平/做法，但未系统列出全部恒定变量并逐一讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计；模型评测固定同一评测集不属于心理实验中的被试匹配。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入 ANCOVA/回归模型；污染分析是单独诊断而非协变量控制。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者需要盲法；模型输出由自动指标评分。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡、拉丁方或 ABBA 顺序设计及其层级选择。 |
| D1 | 练习效应 | NA | — | 无人类练习阶段或跨条件学习；LLM 各评测调用不形成传统练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳设计；计算运行时长不属于被试疲劳效应。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留或清洗期；每个 prompt/模型评测独立进行，不训练新参数。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移与不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为 POS accuracy 与 NER/chunking F1，不是主观量表或绝对量值判断任务。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_3: “k demonstrations are sampled from the training dataset at random”；PDF_PAGE_5 报告不同 demonstration sets 会造成性能差异；未报告 demonstration 排列的显式反平衡或位置分析。 | 随机抽样 demonstration 提供了一定顺序随机性，但没有明确报告样例排列方案、位置出现次数或被试/运行分配细节。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，不存在默认赞同或反向计分问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试参与，不存在人类需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | 数据收集完全自动化，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_4 Table 1 报告 Acc./F1 与 SE；PDF_PAGE_12 Table 6 报告各任务及 k 的 means ± SE；PDF_PAGE_5 报告 zero-shot POS 约 17% 且随机约 5.8%。 | 报告了均值与标准误，但未报告偏度、端点频率或 pilot 难度校准；只能算部分满足。 |
| E7 | 共同方法偏差 | NA | — | IV 为 prompt/标签/模型条件，DV 为自动任务指标，不存在自评式同源多构念测量。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_3: mean and standard error across runs；PDF_PAGE_5: Spearman 相关及 p-values；PDF_PAGE_8 Table 3 报告 performance deltas 与 ρ。 | 报告了均值/SE 和部分效应量（delta、ρ），但没有事前功效分析、95% CI 或系统多重性校正。 |
| F2 | 内部效度 | NA | — | 这是非实验性 benchmark/行为探针评估，没有随机分配、分配隐藏、被试流向或损耗，也不作严格因果推断。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_1–2 将 structured prompting 定位为 behavioral probe；PDF_PAGE_5–6 做 seen/unseen labels 与 label ablations；PDF_PAGE_8 报告跨标签集 class-level 相关；PDF_PAGE_9 讨论污染限制。 | 对构念效度有操作化与会聚分析，但缺少人类信效度证据或正式 manipulation check。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_3 报告模型家族、数据集与评测子集；PDF_PAGE_9 明确 English-only 与 GPT-3 实验限制；未报告跨语言或跨样本复现。 | 报告了样本/模型来源并讨论部分边界条件，但没有跨样本或跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_3: “m = 5 runs per experiment”，评测集固定为 1000 examples；PDF_PAGE_12 Table 4 另做评测集重抽样稳定性检查。 | 说明了运行层级与固定评测样本，但没有明确讨论 test items / demonstrations / models 的嵌套结构及分析层级匹配。 |
| G2 | 随机效应 | 0.5 | PDF_PAGE_3 报告多次运行的 mean 和 standard error；PDF_PAGE_5 报告不同 demonstration sets 的变异；全文未建立混合模型或说明随机截距/随机斜率。 | 以运行间变异报告部分随机性，但未明确哪些因子为固定/随机效应，也未用随机效应模型推广到 demonstration 或 item 总体。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_3: 每个任务从 test set 随机抽 1000 个 examples 且在各运行间固定；PDF_PAGE_12 Table 4 对较小模型重抽样评测集检查稳定性；未使用 item random effects。 | 承认并检查了评测样例选择的一定变异性，但主要分析将测试项目视为固定集合，未把材料/项目作为随机效应纳入模型。 |
| G4 | 统计功效 | 0 | PDF_PAGE_3 只说明 m=5 与 1000 examples 的评测安排；PDF_PAGE_4/12 报告 mean ± SE；全文无事前功效分析或样本量推导。 | 没有设计阶段功效分析、预期效应量来源或样本量论证。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_3 报告默认 k=10、m=5、1000 test examples；PDF_PAGE_12 A.1 说明固定评测子集并做重抽样检查；PDF_PAGE_9 讨论 GPT-3 仅做部分实验与未做全面 prompt ablations。 | 报告了部分排除/抽样与运行规则，但未系统区分验证性与探索性分析，也未完整说明所有分析路径选择。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未见预注册平台、注册编号或数据收集前分析计划；PDF_PAGE_9 仅报告事后 limitations。 | 无预注册；也未声明为纯探索性研究并区分验证/探索分析。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM-as-judge、成对比较或多候选项位置选择；标签通过固定标签集合上的 likelihood 评分产生。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放性生成长度，不存在长度偏差评分问题。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈纠错或多轮对话式谄媚风险；任务是闭卷序列标注。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 裁判评估模型输出，无自我偏好/同源裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF_PAGE_3: demonstrations 从训练集随机抽样，尽量覆盖标签空间，默认 k=10、m=5 runs；PDF_PAGE_5 分析 demonstration set 对性能的影响；PDF_PAGE_13 Table 6 给出不同 k 的结果。 | 报告了示例来源、数量和多次抽样运行，但未报告精确标签比例、示例排列反平衡或完整 prompt 模板，故为部分满足。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_2 Figure 1 与 Section 3.1 给出 prompt 结构示意；PDF_PAGE_2 称 preliminary experiments with varied prompt formats had little effect；PDF_PAGE_9 承认 GPT-3 未做全面 prompt ablations。 | 报告了 prompt 结构并做了有限的格式敏感性说明，但未公布完整原始模板、版本号与 dev/test 划分，敏感性消融也不完整。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为少量 demonstrations 与单句序列标注，不是长文档/RAG 信息位置实验。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_3: 大多数模型用 greedy top-1 label；GPT-Davinci 因成本用 “unconstrained top-1 sampling”；PDF_PAGE_3 报告 m=5 runs，但未报告 temperature、seed 或采样快照。 | 报告了解码方式与重复运行，但缺少温度、top-p、seed 与闭源 API snapshot 等关键随机性信息。 |
| J9 | 重复与文本退化 | NA | — | 任务输出为短标签/固定标签集合，不是开放式长文本生成，重复退化风险不适用。 |
| J10 | 分词效应 | NA | — | 实验为 English-only，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | PDF_PAGE_6: 搜索 Pile 中 POS/NER 标签与任务数据，并称 “we find no evidence of test data leakage”；PDF_PAGE_9: 承认 GPT-3 因黑箱和预训练数据不可得无法完全控制泄漏；PDF_PAGE_7 Table 2/7 报告出现频次。 | 做了污染与测试泄漏检查，并区分记忆/泛化讨论，但未给出完整训练截止日期对照或统一污染率，GPT-3 无法核查。 |
| J12 | 基准饱和 | 0.5 | PDF_PAGE_4/13 报告 POS、NER、chunking 的分数与 majority baselines；分数未接近天花板，但未系统给出基准量程、SOTA 位置或饱和子集分析。 | 报告了当前水位与基线，但没有明确讨论基准饱和或必要时改用连续指标/更难子集。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；任务为 POS/NER/chunking 序列标注，不涉及 IFEval 式约束遵循。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF_PAGE_2 使用 constrained decoding over fixed labels；PDF_PAGE_3 对 chunking/NER 强制 BIO 约束，并称通常影响很小；PDF_PAGE_4 报告 GPT-Davinci 的 format errors 及剔除格式错误后的子集分数；PDF_PAGE_12 Table 5 比较有无 BIO constraints。 | 报告了格式约束设置与消融，但未系统给出格式合法率，也未始终把格式失败与内容错误作为两个独立指标报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估，无有害请求集或对抗攻击。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF_PAGE_1–2 将工作定位为测试 PLM 的 linguistic knowledge 与 surface memorization，并使用 behavioral probing 框架；PDF_PAGE_8 与 probing 文献比较；但没有人类同名构念对照实验。 | 有将 PLM 作为行为探针对象并讨论语言知识的定位，但未系统论证与人类语言认知构念的异同，也未报告人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | PDF_PAGE_3–4 与 Figure 2 报告模型规模上的性能变化，但未宣称 “涌现/突变”；因此不触发该风险组件。 | 没有 emergence/sudden transition 宣称，故不按涌现能力争议编码。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究是固定模型上的 prompting/benchmark 评估，不涉及以代理指标为目标的训练、RL、best-of-N 优化或 held-out 人类评估监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_3: m=5 runs，报告 mean and standard error；PDF_PAGE_3 给出模型名与规模（GPT-Neo 系列、GPT-Curie、GPT-Davinci）；但没有精确 snapshot 日期、逐题日志或配对检验。 | 有重复次数与标准误，模型标识也较具体，但缺少精确 snapshot、置信区间/配对比较及原始推理日志，可复现性报告不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮 prompting/序列标注，无多轮对话历史或跨轮一致性评估。 |

## 编码小结
论文对 prompting 与序列标注任务的程序、任务指标和标签消融报告较充分，但对心理实验式分配、随机化、混合效应、信效度、预注册与部分 LLM 评测可复现性报告不完整。多数人类被试设计组件不适用；LLM 评测相关的 few-shot、prompt 敏感性、污染、格式约束、重复运行等只能部分满足评分表。
