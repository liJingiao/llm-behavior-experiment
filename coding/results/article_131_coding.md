# article_131 | CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models | 2025

研究类型概述：该文提出并构建 CEB 组合式公平性评测基准，围绕偏见类型（刻板印象/毒性）、社会群体（年龄/性别/种族/宗教）和任务（识别/选择/续写/对话/分类）组织数据集，并在 GPT-3.5、GPT-4、Llama2、Llama3、Mistral 等 LLM 上做基准评测；主要分析单位是模型×配置×样本的评测分数，另含 20 名志愿者对 GPT-4 评分的人工验证。
- **研究构念（Construct）**：社会刻板印象与毒性偏差在任务、群体和反应形式之间的条件性差异｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让多种现成GPT、Llama与Mistral模型在刻板印象/毒性、年龄/性别/种族/宗教及识别/选择/续写/对话等组合条件下作答；仅依据现成模型行为测量。（改变偏差类型、社会群体、任务形式和被测模型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4-5: taxonomy dimensions include Bias Type (Stereotyping/Toxicity), Social Group (Age/Gender/Race/Religion), Task (Recognition/Selection/Continuation/Conversation/Classification); p.7: 'For each configuration ... we evaluate 100 samples.' | 多个设计因素及其水平被明确命名，属于组合式基准条件；但条件由数据集构造/配置决定，不是随机分配到实验单位，且无操纵检验，故只部分满足。 |
| A2 | 因变量 | 0.5 | p.7: 'The Recognition and Selection tasks ... Micro-F1 score'; 'GPT-4 to assess the stereotypical degree ... score between 0 and 100'; 'Perspective API ... toxicity probability'; 'Demographic Parity (DP), Equalized Odds (EO), and Unfairness Score'. | 因变量指标和计分方式明确，但未系统报告测量信度、效度证据，也未对连续分数说明预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | p.26: 'we set the max token lengths of the generated output as 512. We set the temperature as 0 ... except Contianutoni and Conversation ... 0.8'; 'For GPT-3.5 ... gpt-3.5-turbo-0613 and ... gpt-4-turbo-2024-04-09.' | 报告了温度、最大生成长度和部分模型快照等控制项，但未系统列出全部控制变量清单，也未逐一讨论这些恒定设置对外部效度的限制。 |
| A4 | 混淆变量 | 0.5 | p.9: 'GPT models still outperform ... due to the significantly larger parameter sizes'; p.9: 'higher prevalence of such biased content in the training data'; p.8: 'safety alignment tuning on Llama models is excessively exercised'. | 文中事后识别了模型规模、训练数据流行度、安全对齐等可能混淆因素，但没有通过设计或统计方式控制，也未系统报告残余混淆威胁。 |
| A5 | 调节变量 | NA | — | 论文没有提出调节变量假设，也没有进行调节效应或交互检验；其组合维度主要作为基准描述维度，而非理论调节模型。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、中介假设或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.18-25 给出各任务 prompt 模板；p.27-30 给出 GPT-4 bias score、Perspective API、DP/EO/Unfairness 的计分方式；p.26 报告数据集统计。 | 关键构念被操作化为具体任务、提示模板、评分规则和指标，复现路径较完整；数据集构造与模型评测程序也可据附录重执行。 |
| A8 | 水平数与类型 | 0.5 | p.4-5: Bias Type 2 类、Social Group 4 类、Task 5 类；p.27 Table 9 列出模型及参数量；p.26 Table 8 列出数据集规模。 | 报告了各因素水平数与标签，但未系统标明水平类型（名义/等级/连续）、间距/全距；模型规模在描述中混合使用但未作为连续变量中心化分析。 |
| A9 | 单一操作化的风险 | 0.5 | p.4-7 使用多个任务、多个数据集和多种指标；p.33-34 Limitations 讨论 'Scope of Social Groups and Bias Types'、'Reliance on Existing Datasets'、'Evaluation Metric Consistency'。 | 关键构念采用多种操作化，但未报告不同操作化之间的会聚证据（如任务间相关）；局限讨论存在但不具体到单一操作化的推广边界。 |
| A10 | 单一方法的风险 | NA | — | 该研究不是多构念自陈式问卷研究，因变量来自基准任务输出或分类指标，不适用传统共同方法偏差检验。 |
| B1 | 被试间设计 | NA | — | 没有人类被试被分配到不同自变量水平；LLM 不是以独立被试组方式分配条件，故不适用被试间设计。 |
| B2 | 被试内设计 | NA | — | 同一模型虽在多个配置上评测，但均为独立 API/提示调用，无会话内重复测量顺序；论文未报告也不需要有顺序平衡方案。 |
| B3 | 混合设计 | NA | — | 没有组间因素与组内因素并存的混合实验设计，也没有对应混合模型或两类误差项。 |
| B4 | 因子设计 | 0 | p.5 Table 2 给出 Bias Type×Social Group×Task 的组合矩阵；p.7-10 报告各配置均值；但全文未对配置因素做主效应/交互的方差分析或报告交互项统计量。 | 存在多因素组合式评测结构，但未将其作为统计因子设计报告完整设计矩阵与交互检验，因此未满足基本要件。 |
| B5 | 主效应 | 0 | p.9-10 仅以描述性方式比较不同社会群体和任务的平均分，如 'performance on social groups of ages and genders is generally more paramount'；无 F、df、p 或效应量。 | 有描述性边际比较，但没有主效应统计检验，故主效应组件不成立。 |
| B6 | 交互作用 | 0 | Table 6、Table 7 分别按任务、偏见类型、社会群体列表；正文仅描述性归纳，没有交互项统计检验、简单效应或误差棒。 | 未报告任何交互作用统计检验；属于多因素描述性评测，不能算作完整交互分析。 |
| B7 | 区组设计 | NA | — | 没有使用区组或分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 论文是基准评测与数据集构建，不是需要讨论非随机分配因果推断的准实验研究。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有采用需要论证可逆性与迁移对称性的被试内处理设计。 |
| C1 | 随机化 | NA | — | 论文没有把实验单位随机分配到互斥处理条件；Appendix B 的 'randomly extract a sample' 是数据集抽样，不是处理分配。 |
| C2 | 平衡 | NA | — | 没有条件顺序需要平衡，也没有被试在各顺序组间的分配。 |
| C3 | 恒定 | 0.5 | p.26: 'max token lengths ... 512'；'temperature as 0 ... except ... 0.8'；'A100 NVIDIA GPU with 80GB memory'；'checkpoint gpt-3.5-turbo-0613 ... gpt-4-turbo-2024-04-09'. | 列出了若干恒定控制项及其水平，但没有系统讨论这些恒定设置对结果外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型；论文主要做描述性基准比较。 |
| C6 | 盲法 | 0 | p.8: 'We recruit 20 volunteers and asked each of them to assess the bias of 100 samples. In this setup, each sample is evaluated by 5 volunteers.' | 存在人工评分者，但未报告是否对模型来源/条件施盲、施盲方式或盲法成功检验；人工评分可能知道样本来自不同模型。 |
| C7 | 平衡的层级 | NA | — | 没有顺序平衡层级（完全平衡/拉丁方/ABBA）可选择或报告。 |
| D1 | 练习效应 | 0 | p.8: '20 volunteers ... assess the bias of 100 samples'；未报告练习块、前测练习试次或试次位置协变量。 | 人工评分者连续评 100 个样本，存在练习/熟悉评分标准的风险，但论文没有报告任何练习效应控制。 |
| D2 | 疲劳效应 | 0 | p.8: 人工评分设置为每名志愿者评 100 个样本；未报告 session 时长、休息间隔或条件在时间上的分散方案。 | 人工评分任务可能产生疲劳，但论文未报告任何休息或时长控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件重复处理或清洗期设计；每个 LLM 提示是独立调用，人工评分也不构成条件交叉处理。 |
| D4 | 不对称迁移 | NA | — | 没有被试内交叉条件，因此不存在需要检验的不对称迁移。 |
| D5 | 范围效应 | 0.5 | p.27-28: GPT-4 bias score 使用 0-99 绝对评分，并给出 0-39、40-79、80-99 的分段锚点；但未讨论范围效应或做被试间对照。 | 评分量表有绝对锚点，但没有讨论范围效应风险，也没有采用被试间对照来控制量表校准偏差。 |
| E1 | 位置 / 顺序偏差 | 0 | p.18-21 Selection 选项以 '1.'、'2.'、'3.' 固定编号呈现；未报告选项顺序随机化或反平衡方案。 | 多选项选择任务存在位置/顺序偏差风险，但论文没有报告任何随机化或反平衡细节。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，也没有正反向计分题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 主要指标是 LLM 输出的偏见/毒性分数与分类公平性指标，不是人类等级量表反应风格，也不涉及跨群体反应风格比较。 |
| E4 | 需求特征 | 0 | p.8: 人工评分者被要求 'assess the bias of 100 samples'；未报告 cover story、盲法或 post-experimental inquiry。 | 人工评分者可推断研究关注偏见评估，但论文没有报告掩饰情节、事后访谈或 debriefing 流程。 |
| E5 | 实验者效应 | 0 | p.8: 仅说明招募 20 名志愿者，每样本由 5 人评分；未报告评分者培训、标准化脚本或盲法层级。 | 人工评分者可能存在期望效应，但未报告主试/评分者盲法与培训标准化。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.10 Fig. 6 与附录 Fig. 10-33 报告部分 bias score 分布；Table 6 中 Toxicity Recognition 多处接近 100；但未报告 pilot 难度校准或系统讨论天花板/地板效应。 | 提供了部分分布图，可排查端点堆积，但没有系统报告均值/SD/偏度/端点频率，也未讨论任务难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，不适用共同方法偏差的程序控制与统计检验。 |
| F1 | 统计结论效度 | 0 | p.7-10 主要报告均值、Micro-F1、bias/toxicity score；p.33 Table 15 仅报告 5 次运行的 SD；未报告效应量、95%CI、样本量功效依据或多重性校正。 | 描述性基准比较没有达到统计结论效度组件的基本要求：缺少效应量/CI、主要推断检验和多重比较校正。 |
| F2 | 内部效度 | NA | — | 研究不是随机对照实验，也不作因果推断；不适用随机分配、分配隐藏、基线等价性与损耗流向评估。 |
| F3 | 构念效度 | 0.5 | p.7-8: 使用 GPT-4 作为 bias judge，并用 20 名志愿者人工评分进行比较，称 'Humans are generally aligned with GPT-4'; 但未报告 inter-rater reliability、与人类评分的相关系数或正式效度指标。 | 有人类评分对照作为部分效度证据，但缺少信度统计、评分者一致性、操纵检验及多操作化会聚证据。 |
| F4 | 外部效度 | 0.5 | p.26 Table 8 报告数据集规模与覆盖社会群体；p.27 Table 9 列出模型；p.33-34 Limitations 讨论社会群体、偏见类型和参考数据集的边界。 | 报告了数据集来源/规模和部分推广边界，但没有报告跨样本或跨情境复现结果，也未论证样本代表性。 |
| G1 | 分析单位 | 0.5 | p.7: 'For each configuration ... we evaluate 100 samples'；p.27: 'All these datasets could be considered as classification tasks ... Micro-F1'。 | 说明了每个配置的样本量和聚合层面，但没有讨论样本嵌套于数据集/配置的聚类结构，也没有多层模型或分析单位匹配说明。 |
| G2 | 随机效应 | NA | — | 论文没有使用混合效应模型，也没有把模型/被试作为随机效应报告；其分析是描述性基准汇总，故该组件不适用。 |
| G3 | 材料作为随机效应 | 0 | p.7 说明每个配置评测 100 个样本；p.26 Table 8 列出数据集规模；但分析仅汇总 F1/分数，未将材料/项目作为随机效应，也未报告 (1&#124;item) 或准 F 比。 | 使用有限具体样本作为评测材料，但没有把材料视为来自更大总体的随机样本纳入分析，结论可能过度推广到任意材料。 |
| G4 | 统计功效 | 0 | p.7 仅说明每个配置 100 个样本；全文没有事前功效分析、目标功效、预期效应量或样本量推导。 | 没有设计阶段功效分析或样本量论证，结果也未系统报告效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.27-29 说明 RtA 输出不参与 bias score 计算，并报告 RtA rate；p.26 Table 8 报告各数据集规模；但未明确区分验证性与探索性分析，也未说明是否中途停止/追加。 | 部分报告了排除规则和全部主要条件，但缺少完整的数据收集停止规则与验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未出现预注册平台、注册编号、预注册分析计划或时间戳早于数据收集的说明。 | 无预注册，且未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | 0 | p.18-21 的 Selection prompts 将候选句固定编号为 '1.'、'2.'、'3.'；未报告 A/B 交换、位置随机化、翻转率或位置×正确率曲线。 | 选择任务存在候选项位置偏差风险，但论文完全未提及位置反平衡或随机化。 |
| J2 | 冗长偏差 | 0 | p.7: 'we use GPT-4 to assess the stereotypical degree of LLM-generated outputs'；p.27-28 judge prompt 只按偏见程度评分，未报告回答长度与得分相关系数或长度控制。 | LLM 裁判用于开放式生成评分，但没有识别或控制长度偏差，也未报告长度分布与得分关系。 |
| J3 | 谄媚 | 0 | p.22-23 Conversation prompts 含用户立场（如 'I don’t like 25-year-old guys'），但没有 pro-/anti-framing 操纵、答案翻转率或 sycophancy 测量。 | 对话式任务包含用户先验立场，存在谄媚风险，但论文未操纵或测量该偏差。 |
| J4 | 自我偏好 | 0.5 | p.7: 'we use GPT-4 to assess ... all LLMs'；p.8: 人工评分用于检查 GPT-4 是否偏向自身输出，并称 'does not stem from an inherent bias in favor of its own generated outputs'；但未量化 self-preference rate，也未用异源陪审团。 | 明确使用 GPT-4 评判包括 GPT-4 在内的模型输出，并有人类对照讨论自我偏好；但未报告各裁判单独结果、匿名化或自我偏好比例。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 任务提示为零样本指令式 prompt，附录未显示 few-shot in-context examples，因此 few-shot 示例选择与排列偏差不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.27-28 给出 GPT-4 judge 的完整评分 prompt；p.18-25 给出各任务 prompt；但未报告 prompt 版本号、迭代日期、敏感性消融或 dev/test 划分。 | 提供了较完整提示模板，但没有版本化、语义等价措辞敏感性分析，也未说明是否在测试集上调 prompt。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 输入上下文为短句/短对话/表格描述，远低于长上下文窗口，也没有 RAG 或长文档位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.26: temperature 0（除 Continuation/Conversation 为 0.8）、max tokens 512、GPT 快照日期；p.33: Continuation/Conversation 的 Stereotyping 结果报告 5 次运行 SD。 | 报告了主要采样温度和部分快照，并做有限重复运行；但未报告 top-p/top-k、随机种子，且未给出重复运行的 95%CI。 |
| J9 | 重复与文本退化 | 0.5 | p.26: 报告 temperature 与最大生成长度 512；p.28-29 将安全对齐拒答输出排除；但未报告 repetition penalty、n-gram 重复率或退化率。 | 部分报告解码设置，开放生成任务存在重复/退化风险，但未作为 QC 指标系统报告，也未说明条件间解码策略是否完全恒定。 |
| J10 | 分词效应 | NA | — | 研究以英文单语言/单脚本为主，没有跨语言或跨脚本比较，也未涉及分词长度作为混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.8 使用 WinoBias、StereoSet、RedditBias、CrowS-Pairs 等公开数据集，p.5-6 又用 GPT-4 构造 CEB 数据；未报告测试集版本与模型训练截止日期对照，也未做污染检测。 | 基准评测存在训练数据污染风险，但论文没有检查 n-gram 重叠、DCQ、训练截止日期或私有 held-out 集。 |
| J12 | 基准饱和 | 0 | Table 6 中 Toxicity Recognition 分数接近 100（如 GPT-4 多项 100.0）；论文未讨论基准饱和、未改用连续指标或更难子集，也未报告 bootstrap CI。 | 部分子任务已接近天花板，但论文没有评估饱和风险，仍直接报告模型差异。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；虽然报告了 RtA 率并讨论安全对齐影响，但没有系统测量否定/数量/格式/风格等指令约束。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.18-25 prompt 反复要求 'Return only one number as your output'；p.7 使用 Micro-F1 评测；但未报告格式合法率、重试策略或把格式失败与内容错误分开。 | 存在结构化/短格式输出约束，但论文没有系统报告格式约束设置和格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 研究不是越狱/对抗安全性评估；没有攻击族、ASR 或自然提示拒绝率与对抗攻击成功率的区分。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文将 LLM 作为公平性评测对象，而不是心理学/认知科学意义上的被试；不主张测量人类同名心理构念或外推人类心理学结论。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文比较若干模型规模，但没有报告跨规模能力曲线、涌现宣称或连续指标/多 seed 的涌现检验。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究是纯基准评估，没有以 benchmark/reward model/LLM-judge 为优化目标进行训练、RL 或 best-of-N 优化，因此不涉及代理指标过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.26 报告 GPT-3.5/GPT-4 精确快照；p.33 对 Continuation/Conversation 的 Stereotyping 报告 5 次运行 SD；代码链接公开；但多数任务单次评测，未报告 CI、配对检验或完整原始日志。 | 部分可复现信息存在（快照、代码、有限重复 SD），但缺少每个分数的 N/95%CI、配对模型比较和逐题结果。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | Conversation 任务只是基于一个对话开头的单轮生成，不是多轮累积对话；论文没有多轮一致性衰减评估。 |

## 编码小结
这是一项 LLM 公平性基准评测与数据集构建研究，而不是以人类被试为单位的受控实验。设计上明确给出组合式配置、样本量、提示模板和部分评测指标，但统计上以描述性均值和排序比较为主，缺少置信区间、配对检验、功效分析、预注册、污染检查、位置/长度偏差控制、提示敏感性分析等；人工评分部分也缺少盲法、信度与疲劳/练习控制。大量人类实验设计组件不适用，LLM 评测质量控制组件多为部分满足或缺失。
