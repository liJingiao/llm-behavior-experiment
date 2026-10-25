# article_192 | Uncovering Gaps in How Humans and LLMs Interpret Subjective Language | 2025

研究类型概述：这是一项 LLM 行为审计/方法评估研究，不是传统人类被试实验。作者提出 TED 方法，用梯度嵌入构建 LLM 的“操作性同义词典”，再与人类或 LLM 构建的语义同义词典比较，寻找主观短语操作语义与人类预期的错配；随后在输出编辑与推理引导两类任务上，用 GPT-4 裁判评估下游成功率，并与语义基线比较。
- **研究构念（Construct）**：主观语言的操作语义、概念关系和人类意图与模型行为之间的错配｜CA 构念锚定：语言理解（language comprehension, `trm_4a3fd79d0a775`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：在输出编辑和推理引导任务中向冻结模型加入成对主观词语，比较输出属性变化与人类参考词库预期，并对发现的语义冲突做下游行为验证。（操纵主观控制词、编辑或直接推理任务、模型和参考词语关系，并比较模型操作词库与人类词库。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | [PDF_PAGE_5] “We test Mistral 7B Instruct ... and Llama 3 8B Instruct”；[PDF_PAGE_7] Table 1 比较 TED 与 Sem. only；[PDF_PAGE_8] “Write a [subjective phrase] blog post...”。 | 可识别的操纵条件包括主观短语/编辑条件、TED 与语义基线、模型与任务等，且给出水平与材料；但未报告正式操纵检验、单位分配逻辑与完整实验分配程序，故为部分满足。 |
| A2 | 因变量 | 0.5 | [PDF_PAGE_5] “we use a judge to measure whether ow2 is more aligned with w1 ... compute the success rate by repeating ... for k generic prompts”；[PDF_PAGE_7] 使用 GPT-4 裁判；[PDF_PAGE_25] 报告 GPT-4 与人类裁判的一致性。 | 因变量指标（下游成功率和阈值以上比例）与计分方式明确，且有部分裁判效度证据；但缺少正式信度（如 α）、完整预处理规则及天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | [PDF_PAGE_17] “Inference occurs ... with a temperature = 1 ... We do not include a system prompt ... format both the prompt and output using the appropriate chat template”；[PDF_PAGE_7] “We randomize the order of outputs”。 | 报告了若干恒定/控制手段，如温度、无 system prompt、chat template、输出长度上限和裁判中的 A/B 随机化；但未系统列出控制变量清单并逐一讨论控制手段。 |
| A4 | 混淆变量 | 0.5 | [PDF_PAGE_6] “the annotators can provide noisy labels ... LLM’s are imperfect proxies of human judgment”；[PDF_PAGE_7] “GPT-4 occasionally outputs that there is no difference ... we say TED is not predictive”；[PDF_PAGE_25] 报告 GPT-4 与人类判断的一致率。 | 识别并部分处理了裁判偏差、人类标注噪声和 LLM 语义同义词典误差等潜在混淆；但没有系统讨论残余混淆或敏感性分析对内部效度的影响。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量理论模型，也没有报告交互检验与简单斜率分析；该组件不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量与中介效应分解，不适用。 |
| A7 | 操作性定义 | 1 | [PDF_PAGE_5] 公式 (1)(2) 定义 eop(w) 与 tllm；[PDF_PAGE_6] 报告 n=100、τsim/τdis；[PDF_PAGE_18] 给出编辑与裁判 prompt；[PDF_PAGE_18] 报告 GPT-4 裁判 prompt。 | 关键构念的操作化较可复现：梯度嵌入、同义词典阈值、语义同义词典构建、下游成功率的生成与裁判流程均有明确说明，代码链接也给出。 |
| A8 | 水平数与类型 | 0.5 | [PDF_PAGE_6] “n = 100 prompts ... τsim = 0.93 and τdis = −0.1 ... For Llama 3 ... τsim = 0.98 and τdis = −0.5”；[PDF_PAGE_7] 阈值 0.1,0.3,0.5,0.7,0.9；[PDF_PAGE_16] 210 个短语；[PDF_PAGE_17] 132 个短语。 | 报告了多个条件的水平与取值，包括模型、任务、短语集合和阈值；但没有明确给出完整因子结构、水平类型、间距/全距及连续阈值的中心化处理。 |
| A9 | 单一操作化的风险 | 0.5 | [PDF_PAGE_5] TED 用梯度嵌入并与下游行为验证；[PDF_PAGE_6] 同时使用人类与 LLM 构建的语义同义词典；[PDF_PAGE_9] 讨论 “many natural ways that it could be improved” 并提到改进嵌入。 | 关键构念有多种评估渠道（操作性词典、人工语义词典、LLM 语义词典、下游行为），但没有报告各操作化之间的正式会聚证据；对单一梯度嵌入局限的讨论也较有限。 |
| A10 | 单一方法的风险 | NA | — | 研究不是同源自陈式多构念测量：操作性语义来自梯度嵌入，人类预期来自标注，后者来自 GPT-4 裁判；共同方法偏差不是核心风险，故不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试组间分配；模型条件不是独立被试组。因此不按人类被试间设计编码。 |
| B2 | 被试内设计 | 0.5 | [PDF_PAGE_5] 对同一 generic prompt 生成 o∅ 与受 w2 引导的 ow2 并比较；[PDF_PAGE_18] “We randomize Response A and Response B to eliminate order bias”。 | 可在 LLM 提示/输出层面视为同题配对比较，且裁判阶段做了 A/B 顺序随机化；但没有正式称其为重复测量设计，也未在统计模型中设提示或题目的随机效应，顺序分配细节不足。 |
| B3 | 混合设计 | NA | — | 不存在组间与组内因素混合的实验设计，也没有对应混合模型或两类误差项。 |
| B4 | 因子设计 | NA | — | 虽然 Table 1/2 呈现模型、任务、语义词典与方法的多维比较，但没有正式因子设计、完整设计矩阵的 ANOVA 或交互项检验；按因子设计要求记 NA。 |
| B5 | 主效应 | NA | — | 没有正式因子设计意义上的主效应检验，不适用。 |
| B6 | 交互作用 | NA | — | 没有报告正式交互项统计检验、简单主效应和多重比较校正，不适用。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量及区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序安排。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计，没有非随机分组及选择偏差处理。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理可逆性与迁移对称性设计。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥实验条件；仅对裁判中的 A/B 顺序和部分失败样本做随机化，这不构成处理分配随机化。 |
| C2 | 平衡 | NA | — | 没有需要平衡的处理顺序设计；A/B 响应顺序随机化在 E1/J1 下编码。 |
| C3 | 恒定 | 0.5 | [PDF_PAGE_17] “temperature = 1 ... We do not include a system prompt ... format both the prompt and output using the appropriate chat template”；[PDF_PAGE_7] “We randomize the order of outputs”。 | 报告了若干被恒定的生成设置和最大输出长度，但没有系统列出所有恒定变量及其水平，也未讨论这些恒定选择对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计，也无匹配变量和匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | 0.5 | [PDF_PAGE_18] “We randomize Response A and Response B to eliminate order bias”；[PDF_PAGE_24-25] 人类标注 prompt 只标 A/B 与 Unsure，未标条件来源。 | 通过 A/B 随机化和不显示条件标签形成了部分遮蔽，但没有报告正式盲法类型、施盲对象与盲法成功检验。 |
| C7 | 平衡的层级 | NA | — | 没有需要选择完全平衡、拉丁方或 ABBA 的被试内条件顺序层级。 |
| D1 | 练习效应 | NA | — | LLM 生成按独立提示/条件进行，不存在人类被试的练习块或上下文内学习；不适用。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长、休息间隔或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各生成条件可视为独立提示，没有跨条件清洗期或残留效应设计。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件迁移对称性检验需求。 |
| D5 | 范围效应 | NA | — | 不使用主观李克特量表或被试内绝对判断，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | [PDF_PAGE_7] “We randomize the order of outputs when prompting GPT-4 to eliminate order bias”；[PDF_PAGE_18] “We randomize Response A and Response B”。 | 报告了裁判阶段 A/B 顺序随机化，但没有报告具体随机化方案、各位置出现次数或交换前后偏好翻转率。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert 态度量表，无反向计分题与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 人类 MTurk 标注是语义同义词典/裁判验证任务，不是行为实验被试；不存在掩饰情节或事后假设推断流程的核心需求。 |
| E5 | 实验者效应 | 0.5 | [PDF_PAGE_20-21] 报告 10 名 MTurk 标注者、资格测试和标准化说明；[PDF_PAGE_24] 每对由三名标注者标注。 | 报告了评分者人数、资格筛选与标准化脚本，但没有明确说明评分者对条件的盲法层级与期望控制。 |
| E6 | 天花板 / 地板效应 | 0.5 | [PDF_PAGE_9] Table 2 报告平均成功率与阈值以上比例；[PDF_PAGE_27-40] 给出大量逐对成功率表。 | 报告了成功率分布的部分信息（阈值以上比例与均值变异性），但没有正式报告偏度/端点频率，也没有说明 pilot 难度校准，无法充分排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，CMB 不适用。 |
| F1 | 统计结论效度 | 0.5 | [PDF_PAGE_7] “average success rate ... over 30 randomly sampled failures ... k = 100 prompts”；Table 1/2 报告 “Avg. Suc. ± ...”；[PDF_PAGE_9] Table 2。 | 报告了主要结局的比例指标及其离散度，但没有明确样本量/功效依据、95% CI、多重性校正或正式统计检验假设说明。 |
| F2 | 内部效度 | 0 | [PDF_PAGE_5] “TED’s improvement over this baseline comes entirely from filtering for better failures”；[PDF_PAGE_7] 仅说明对 30 个失败对做随机抽样评估，未报告条件随机分配或基线等价性。 | 方法/基线比较没有随机分配、分配隐藏或选择偏差控制说明，也未评估方法间选择差异对内部效度的威胁。 |
| F3 | 构念效度 | 0.5 | [PDF_PAGE_25] “GPT-4 matches the majority-vote judgment on 84% ... when all annotators agree ... 97%”；[PDF_PAGE_24] 人类同义词典标注使用三人全同意规则。 | 有部分构念/裁判效度证据（GPT-4 与人类标注一致、人工标注共识规则），但缺少正式信度统计、操纵检验和多操作化会聚分析。 |
| F4 | 外部效度 | 0.5 | [PDF_PAGE_5] 仅测试 Mistral 7B Instruct 与 Llama 3 8B Instruct；[PDF_PAGE_6] 10 名 MTurk 标注者；[PDF_PAGE_16-17] 短语集合来自 GPT-4 生成和手工筛选。 | 报告了模型与标注样本来源/特征，但没有系统说明跨模型、跨任务、跨短语总体的推广边界，也没有跨样本/跨情境复现实验。 |
| G1 | 分析单位 | 0.5 | [PDF_PAGE_7] “average success rate ... over 30 randomly sampled failures ... using k = 100 prompts”；[PDF_PAGE_5] 下游评估以提示和失败对为单位。 | 说明了成功率聚合层级（失败对与提示），但没有明确处理提示嵌套于失败对/问题、短语对选择等聚集结构。 |
| G2 | 随机效应 | 0 | [PDF_PAGE_7] 结果仅报告平均值与阈值比例；[PDF_PAGE_9] 无混合模型或随机效应结构。 | 研究将提示与短语对作为固定集合进行简单平均，没有说明哪些因子为随机效应，也没有用随机截距/斜率结构把提示或材料方差分离。 |
| G3 | 材料作为随机效应 | 0 | [PDF_PAGE_6] “We average n = 100 prompts”；[PDF_PAGE_16-17] 报告有限短语集合；[PDF_PAGE_27-40] 只报告逐对成功率表。 | 短语/材料是有限固定刺激，分析未把材料或短语对作为随机抽样总体处理，也没有准 F 比或混合模型；存在将结论推广到任意主观短语的风险。 |
| G4 | 统计功效 | 0 | [PDF_PAGE_7] 仅说明抽取 30 个失败对、每对 k=100 prompts；全文未报告事前功效分析或目标功效。 | 没有设计阶段功效分析、预期效应量来源或样本量推导，因此不满足统计功效要求。 |
| G5 | 研究者自由度 | 0.5 | [PDF_PAGE_6] “we restrict the annotators to label 1260 pairs out of ... 27084”；[PDF_PAGE_7] “30 randomly sampled failures”；[PDF_PAGE_19] 200 个伦理问题中 100 个训练、100 个测试；[PDF_PAGE_24] 标注者不一致则丢弃。 | 报告了部分排除/抽样规则和主要条件，但没有完整披露所有研究者自由度、阈值调参过程及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | [PDF_PAGE_1-10] 未见预注册链接、注册编号或数据收集前分析计划。 | 全文未报告预注册；因此按缺失适用组件记 0，而非 NR。 |
| J1 | 位置偏差 | 0.5 | [PDF_PAGE_7] “We randomize the order of outputs when prompting GPT-4 to eliminate order bias”；[PDF_PAGE_18] 完整 A/B 裁判 prompt；[PDF_PAGE_7] 裁判模型为 “gpt-4-turbo-2024-04-09”。 | 识别并随机化了候选响应位置，且报告裁判模型与 prompt；但没有报告 A/B 交换前后偏好翻转率或位置×正确率曲线，采样参数也不完整。 |
| J2 | 冗长偏差 | 0 | [PDF_PAGE_7] 使用 GPT-4 chain-of-thought 裁判比较输出；[PDF_PAGE_17] 输出上限 10000 tokens；全文未报告长度—得分相关或长度控制。 | LLM 裁判比较开放式生成文本，长度可能被误当质量；论文未报告任何长度偏差控制或长度与裁判结果的关系。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场、反馈或纠错式多轮对话，不涉及谄媚风险。 |
| J4 | 自我偏好 | 0.5 | [PDF_PAGE_7] 被评模型为 Mistral 7B / Llama 3 8B，裁判为 GPT-4；[PDF_PAGE_25] 报告 GPT-4 与人类判断一致率。 | 使用异源 LLM 裁判并有部分人类金标准验证，降低同源自我偏好；但没有多裁判陪审团、各裁判单独结果或自我偏好率量化。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验未使用 few-shot in-context 示例；裁判和语义同义词典构建均为 zero-shot 式提示。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | [PDF_PAGE_18] 给出完整裁判 prompt；[PDF_PAGE_17-18] 给出编辑 prompt；[PDF_PAGE_19-20] 给出 LLM 语义词典 prompt；[PDF_PAGE_19] 训练/测试伦理问题分离。 | 提供了较完整 prompt 模板和部分 dev/test 分离，但没有报告 prompt 版本迭代、语义等价措辞的敏感性消融或完整 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短提示，不涉及长文档/RAG、中间迷失或关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | [PDF_PAGE_17] “temperature = 1”；[PDF_PAGE_7] 每个失败对使用 k=100 prompts；Table 1/2 报告均值±离散度；未报告 seed 或 top-p/top-k。 | 报告了主要采样参数和重复的提示集合，但没有报告随机种子、top-p/top-k、逐条件重复采样 N 和 bootstrap 置信区间。 |
| J9 | 重复与文本退化 | 0 | [PDF_PAGE_17] 仅报告 temperature 与 10000 token 上限；全文未报告解码策略、repetition penalty 或 n-gram 重复率/退化率。 | 任务涉及开放生成，但解码与重复退化未被作为受控变量报告，无法排除解码差异与模型行为混淆。 |
| J10 | 分词效应 | NA | — | 仅英语单语言、单脚本研究，无跨语言/跨脚本 token 数比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 研究使用自建伦理问题、主题和短语集，并非公共能力基准；虽然训练/测试问题做了拆分，但测试集并非用于宣称标准基准泛化能力，污染风险不是该设计的核心。 |
| J12 | 基准饱和 | NA | — | 不是标准能力基准评测，也没有 SOTA 饱和与显著提升宣称；不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，无否定/数量/格式/风格约束准确率评估。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 输出为开放式文本，不要求 JSON/文法约束等结构化输出。 |
| J15 | 越狱稳健性 | NA | — | 虽然观察到有害/攻击性输出，但不是安全对齐或越狱稳健性评估，无自然拒绝率与对抗 ASR 设计。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | [PDF_PAGE_1] 研究比较 LLM 操作语义与人类预期；[PDF_PAGE_10] “Even though LLMs exhibit human-like tendencies, they are not human and sometimes behave counterintuitively”。 | 论文明确把 LLM 行为与人类预期对照，并提醒 LLM 不是人类；但没有系统界定 LLM 上“操作语义”与人类同名构念的异同，也未做严格的人类同范式心理实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及模型规模/训练进展曲线或涌现能力宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究评估 TED 的预测效度，不对基准/奖励模型/LLM-judge 进行优化式训练，故无指标博弈与奖励过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | [PDF_PAGE_7] “30 randomly sampled failures ... k = 100 prompts”；[PDF_PAGE_7] 裁判为 gpt-4-turbo-2024-04-09；[PDF_PAGE_17] 报告 Mistral 7B Instruct v0.2 与 Llama 3 8B Instruct。 | 报告了重复评估规模、模型版本和裁判日期，并给出均值±离散度；但没有给出精确 commit/snapshot 哈希、重复采样置信区间或配对 bootstrap/McNemar 检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮：提示—生成—裁判，没有对话历史累积或多轮一致性衰减评估。 |

## 编码小结
论文对核心计算流程、提示词和评估指标的报告较充分，且提供了人类标注与 GPT-4 裁判的一致性验证；但作为实验设计研究，许多人类被试分配、区组、盲法、预注册和功效分析组件不适用。主要不足在于：因子性比较没有正式交互/随机效应模型，裁判位置与长度偏差只部分处理，缺少预注册、功效分析和完整的不确定性/多重性说明。
