# article_163 | LLM Agents Can Be Choice-Supportive Biased Evaluators: An Empirical Study | 2025

研究类型概述：这是一项以 LLM agents 为分析单位的实证/基准式研究：比较多个 LLM 模型在记忆版与评价版选择支持偏差任务中的表现，并加入提示词“perceived control”操纵和 284 名人类被试的对照。研究不是传统随机分组的人类被试实验，分析单元主要是个别模型/迭代输出。
- **研究构念（Construct）**：选择支持偏差、后决策评价扭曲与控制感｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让19种现成LLM在五类情境中先选择选项，再执行记忆式或评价式任务，比较对已选和未选项目的后续归因。（改变已选/被拒选项、第一/第三人称、记忆保留、情境类型以及是否让代理感到选择由自己控制。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3：“We perform minimalist modification to prompts to alter the LLM’s perception of control”；p.6：“changing ‘was chosen’ to ‘was chosen by you’”；p.5：“50 iterations ... randomizing the assignment” | 明确报告了 perceived control 提示这一操纵及两个水平，并描述了局部操纵程序；但没有报告条件分配逻辑，也没有操纵检验，故只算部分满足。 |
| A2 | 因变量 | 0.5 | p.3：记忆任务“measure hits and false alarms... Responses are collected in a structured JSON format”；p.4：评价分数“scoring system ranging from -5 to 5... Tendency Score”，并有 pilot n>100 的人工校验。 | 因变量指标与计分方式已明确，但缺少正式信度/效度证据、连续指标预处理或端点效应说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.3：“The given features for options, the order for the features, and the order for the options are randomly chosen and shuffled before each interaction”；p.4：“the temperature is set to zero”。 | 报告了刺激顺序随机化、选项/特征随机分配和 temperature=0 等控制手段，但未系统列出全部控制变量及其控制方式。 |
| A4 | 混淆变量 | 0.5 | p.3：“to control for potential content-specific biases”；p.5：“not all models are tested on all variations”；p.7：limitations 提到只使用一个代表性 human scenario。 | 识别并用随机化控制了内容特异性偏差，也承认部分模型未覆盖全部变体；但没有系统讨论残余混淆或敏感性分析。 |
| A5 | 调节变量 | 0.5 | p.4：ANOVA 报告“interaction between choice of LLM and option (F = 18.78, p < 0.001)”；p.6：比较“was chosen”与“was chosen by you”条件；p.5：提到较小模型偏差更大，但细节见 appendix。 | 有模型/选项交互检验和 perceived control 条件比较，具备部分调节检验；但未报告中心化/标准化（二元变量可免）和简单斜率/正式交互分解，模型规模效应也主要引用附录。 |
| A6 | 中介变量 | NA | — | 研究模型不包含中介变量，也没有直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p.3：描述 2AFC 选择任务、五个选项对、十个特征、回忆任务；p.4：描述 GPT-4o 评价、-5 到 5 Tendency Score 与人工 pilot。 | 关键构念有任务层面的操作化，但缺少完整提示词、评分 rubric 与可复现的计分细节，故不完整。 |
| A8 | 水平数与类型 | 0.5 | p.5：17 个模型来自 5 个 LLM families；p.5：评价实验 19 个模型并做 50 iterations；p.6：四个额外 scenarios 及 perceived control 两个 prompt 版本。 | 报告了部分水平数与标签，但未在正文完整列出所有模型具体版本/情景水平，也未系统给出水平类型、间距与全距。 |
| A9 | 单一操作化的风险 | 0.5 | p.1-p.2：同时使用 memory-based 与 evaluation-based 两类任务；p.3：评价版用于排除记忆/contextual hallucination；p.7：limitations 讨论任务简化和 human 仅一个 scenario。 | 关键构念采用了多种操作化，并显示两类范式均出现偏差；但没有正式报告不同操作化之间的会聚证据或相关。 |
| A10 | 单一方法的风险 | NA | — | 自变量是提示/选择条件，因变量为模型输出或人类文本经 LLM 评分，不属于同源自陈式多构念测量；LLM 裁判同源风险在 J4 处理。 |
| B1 | 被试间设计 | NA | — | 没有传统人类被试随机分配到互斥条件的被试间设计；LLM 模型也不是被随机分配的独立被试组。 |
| B2 | 被试内设计 | NA | — | 未明确报告重复测量/被试内设计及条件顺序平衡；记忆任务的前后阶段是任务结构，不是被试内条件设计。 |
| B3 | 混合设计 | NA | — | 没有明确混合设计，也没有逐因素标注组间/组内属性。 |
| B4 | 因子设计 | 0.5 | p.4：报告“two-factor ANOVA test, accounting for model type and selection difference”；p.4：记忆实验报告 choice of LLM、option 及其 interaction。 | 有多因素 ANOVA 结构并报告了部分交互，但缺完整设计矩阵、每格样本量、自由度和效应量。 |
| B5 | 主效应 | 0.5 | p.4：“significant effects for choice of LLM (F = 29.63, p < 0.001) and option (F = 3454.61, p < 0.001).” | 报告了主效应 F 与 p，但没有给自由度、效应量，也未在交互显著时说明主效应解释受限。 |
| B6 | 交互作用 | 0.5 | p.4：“A significant interaction between choice of LLM and option is also observed (F = 18.78, p < 0.001)”；p.6 图 6 有 SE 误差棒。 | 报告了交互显著性并图示误差棒，但没有做简单主效应/多重比较校正，缺完整交互统计量。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方或需要拉丁方平衡的多条件顺序设计。 |
| B9 | 准实验设计 | NA | — | 研究以模型/情景比较和提示词变体为主，未报告准实验类型、非随机原因或选择偏差缓解措施。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有采用传统被试内处理设计，因此不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 分析单位没有被概率分配到互斥实验条件；仅有特征/选项顺序随机化，已归入 E1，分配隐藏也不适用。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序设计。 |
| C3 | 恒定 | 0.5 | p.4：“the temperature is set to zero to ensure reproducibility”；p.3：prompts 被描述为 carefully crafted 以保持模型间一致性。 | 列出了 temperature=0 和提示构造一致性等恒定控制，但没有系统列出设备、模型版本、时段等恒定水平，也未讨论其外部效度限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配或配对设计。 |
| C5 | 纳入为变量 | NA | — | 没有将已知混淆变量作为区组或协变量纳入分析；模型/情景被当作研究因素而非协变量控制。 |
| C6 | 盲法 | NA | — | 人类参与者的选择条件本身无法对其隐藏，且研究没有人类评分者盲法安排；LLM 裁判知晓条件的风险在 J4 处理。 |
| C7 | 平衡的层级 | NA | — | 没有采用完全平衡/拉丁方/ABBA 等条件顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 没有人类练习块或需要控制初期练习效应的顺序设计；记忆任务的回忆阶段是研究构念的一部分，不是练习效应控制问题。 |
| D2 | 疲劳效应 | NA | — | LLM 调用不存在人类疲劳；人类问卷也未报告长 session，因此疲劳控制不构成实际设计问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件清洗期或残留迁移设计；评价任务每次交互独立，记忆任务的前后语境是操纵目标本身。 |
| D4 | 不对称迁移 | NA | — | 没有被试内交叉处理，因此不存在不对称迁移检验问题。 |
| D5 | 范围效应 | NA | — | 主要因变量是归因准确性或 LLM-judge 生成的 Tendency Score，不是人类被试内绝对量值估计/Likert 量表校准。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.3：“the order for the features, and the order for the options are randomly chosen and shuffled before each interaction”；p.5：“randomizing the assignment of positive features, negative features, and neutral features to the two options”。 | 明确报告了选项/特征顺序随机化，但没有说明随机化方案细节、各位置出现次数或位置 × 选择分析。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，没有反向计分题与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表分布或跨群体反应风格比较；Tendency Score 是裁判评分而非被试自评等级。 |
| E4 | 需求特征 | 0 | p.4：人类实验仅说明“presented with the same decision-making scenarios... through an online questionnaire platform”，未报告 cover story、单盲或事后访谈。 | 人类被试可能推断选择-评价任务的目的，但全文没有需求特征掩饰或 post-experimental inquiry，故为 0。 |
| E5 | 实验者效应 | NA | — | 主数据收集为在线自动化问卷与自动 LLM 评分，没有人类主试/评分者在场传递期望；pilot 人工校验不是正式实验者效应设计。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5 图 5 报告各模型 chosen/rejected 的 mean 与 SE；p.4 提到对评分做 n>100 的 pilot 人工校验。 | 报告了均值和标准误，但没有偏度、端点频率或任务难度校准，无法充分排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 没有同源自陈式多构念测量；人类选择与解释文本不是多量表自评，LLM 输出评分也不是传统 CMB 场景。 |
| F1 | 统计结论效度 | 0 | p.4/p.6：主要结果以 F、p 值报告，如“F = 18.78, p < 0.001”“F = 33.37, p < 0.001”；未报告效应量或 95% CI，也无功效分析。 | 仅报显著性和部分均值/SE，没有效应量、置信区间、样本量确定依据或多重性校正，故为 0。 |
| F2 | 内部效度 | 0.5 | p.3：特征/选项顺序随机化以控制内容偏差；p.5：随机分配正/负/中性特征；p.7：301 人经筛选后 284 人有效。 | 报告了刺激随机分配与部分筛选/损耗信息，但没有条件分配隐藏、基线等价性检验、完整被试流向或内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | p.4：GPT-4o 评分前用 n>100 pilot，三位作者人工校验并达成共识；p.1-p.3：同一构念用记忆版和评价版两种范式。 | 有 pilot 人工校验和多操作化，但没有正式信度/效度统计、操纵检验，单一操作化局限讨论也有限。 |
| F4 | 外部效度 | 0.5 | p.7：人类样本来源包括 mailing lists、forums、chatrooms，301 人筛选后 284 人，教育背景详细；p.6：扩展到 life choices、public policy、healthcare 等情景。 | 报告了人类样本特征和部分情景推广结果，但样本非代表性抽样，未报告跨样本复现，且局限性部分承认复杂应用仍是开放问题。 |
| G1 | 分析单位 | 0.5 | p.5：“We conducted 50 iterations of the experiment for each model... two-factor ANOVA test”；p.4：实验按每个模型/每次迭代输出进行分析。 | 说明了模型与迭代层级，但未明确处理分配层级与统计模型是否匹配，也未显式建模迭代嵌套于模型的结构。 |
| G2 | 随机效应 | 0 | p.5：统计分析为“two-factor ANOVA test, accounting for model type and selection difference”，未报告任何随机效应；p.5 又声称结论具有 universal applicability。 | 模型被当作固定因素处理，且未讨论对 LLM 总体推广的随机效应；在声称跨模型普适时构成过度推广风险，故为 0。 |
| G3 | 材料作为随机效应 | 0.5 | p.5：每次迭代随机分配 positive/negative/neutral features 到两个选项，并运行 50 iterations；p.3：选项与特征顺序随机化。 | 材料有随机抽样/随机分配并重复多次，但分析中未显式加入 item/feature 随机效应，不能充分推广到任意材料总体。 |
| G4 | 统计功效 | 0 | p.5：“The resulting p-values were consistently below 0.01”；p.5：50 iterations；未报告先验功效分析或效应量/CI。 | 没有设计阶段功效分析，也没有系统报告效应量和置信区间，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p.7：301 名参与者经 age、degree status、attention checks、completion time 筛选后剩 284；p.5：每个模型 50 iterations；但未完整列出所有提示变体与分析路径。 | 报告了部分排除规则和迭代数，但未清楚说明全部因变量/条件、样本量决定方式及探索性与验证性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–10 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告预注册平台、注册编号、分析计划或停止规则。 |
| J1 | 位置偏差 | 0.5 | p.3：“the order for the features, and the order for the options are randomly chosen and shuffled”；p.5：50 iterations 中随机分配特征到两个选项。 | 识别并随机化了选项/特征位置，但没有做 A/B 交换重判、报告偏好翻转率或位置 × 正确率/得分曲线。 |
| J2 | 冗长偏差 | 0 | p.4：评价由“GPT-4o agent”按 -5 到 5 Tendency Score 进行；未报告回答长度分布、长度-得分相关或反长度偏好 rubric。 | 使用 LLM 裁判评价开放式解释，却未控制或报告冗长偏差。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场、反馈纠错或多轮谄媚操纵；perceived control 提示不是 sycophancy 操纵。 |
| J4 | 自我偏好 | 0 | p.4：“The analysis is conducted by a GPT-4o agent”；p.5：被评模型包含 GPT 家族共 19 个模型；未报告匿名化、异源陪审团或自我偏好偏差率。 | 使用 GPT-4o 作为唯一裁判且被评模型可能同源，未识别或控制自我偏好偏差，故为 0。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 研究未使用 few-shot in-context examples；任务是零样本提示式选择/评价。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p.3：prompts 被描述为 based on prior studies 并 carefully crafted；p.6：只说明“was chosen”改为“was chosen by you”并提到其他 prompt variations；未给完整模板、版本号或敏感性消融表。 | 有提示变体比较，但未提供完整 prompt 模板、版本化、dev/test 划分或系统敏感性消融，故为 0。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验上下文很短，不涉及长文档、长上下文或 RAG 信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.4：“temperature is set to zero”；p.5：每个模型 50 iterations 并报告 mean 与 SE；未报告 top-p/top-k、seed、API snapshot 日期。 | 报告了 temperature=0 与重复次数，但采样超参、随机种子和闭源 API 快照不完整，故为 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.4：“temperature is set to zero”；p.3-p.4：要求模型生成解释或 JSON；未报告 repetition penalty、n-gram 重复率或退化率。 | 报告了基本解码设置（temperature=0 近似贪心），但没有重复/退化质控指标，也未系统比较条件间解码策略。 |
| J10 | 分词效应 | NA | — | 研究为单一英语/单脚本任务，没有跨语言或跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3：任务改编自 Henkel and Mather (2007) 等已发表人类研究；全文未报告测试集版本、模型训练截止日期或污染检测。 | 虽非标准公开基准，但使用了已发表范式与情景，存在训练语料污染风险；未做任何污染检查，故为 0。 |
| J12 | 基准饱和 | NA | — | 研究使用新构建的选择支持偏差任务，不涉及接近天花板的标准基准或 SOTA 饱和比较。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循；研究不测量格式/数量/否定等约束遵循率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.3：“Responses are collected in a structured JSON format”；p.3：由 separate agent 格式化 JSON；未报告 JSON 合法率、重试策略或格式失败率。 | 报告了结构化输出要求，但没有把格式失败与内容错误分开报告，也未给格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/对齐评估、越狱攻击或有害请求拒绝率。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1：将研究定位为“AI psychology”，并把人类 choice-supportive bias 范式迁移到 LLM agents；p.7：与 284 名人类作同范式比较。 | 明确讨论了 LLM 构念与人类同名构念的关系，并有人类对照；但未系统论证二者异同，也未报告精确权重快照/版本。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究没有报告随模型规模或训练进展的能力曲线，也没有宣称涌现/突变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有以 benchmark、奖励模型或 LLM-judge 为优化目标进行训练/RL/best-of-N 优化，因此不涉及代理指标过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5：每个模型 50 iterations 并报告 mean 与 SE；p.5：列出 19 个模型名称/家族；p.2/p.5 未给精确 API snapshot、commit hash 或逐题日志。 | 有重复次数和标准误，但模型 snapshot 标识不精确，未报告 bootstrap CI、配对检验或原始推理日志，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.3：记忆版实验包含 choice task 后“the agent continue the previous conversation”执行 recall task。 | 存在两阶段多轮上下文，但没有按轮次独立/累积评分、上下文截断说明或跨轮次行为轨迹分析，故为 0.5。 |

## 编码小结
研究问题具有探索价值，且使用了多种任务范式、多个模型和人类对照；但按方法学编码标准看，统计报告、操纵检验、模型快照、提示词全文、盲法与混淆控制等关键信息普遍不完整，因此多数适用组件只能给 0.5，部分关键质控组件缺失给 0；大量传统被试设计组件因设计单元不适用而记 NA。
