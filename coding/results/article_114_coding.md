# article_114 | Veracity Bias and Beyond: Uncovering LLMs’ Hidden Beliefs in Problem-Solving Reasoning | 2025

研究类型概述：纯 LLM 行为/提示实验，无人类被试；研究比较多个 LLM 在不同任务、人口标签呈现方式与推理输出格式下的归因偏差与评价偏差，分析单位为模型在问题—人口群体条件组合上的输出。
- **研究构念（Construct）**：真实性偏差、人口群体归因偏差与评价偏差｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：纯 LLM 行为/提示实验，无人类被试；研究比较多个 LLM 在不同任务、人口标签呈现方式与推理输出格式下的归因偏差与评价偏差，分析单位为模型在问题—人口群体条件组合上的输出。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.3: “We test two modes of demographic options: (1) Direct Labels... (2) Name Proxies”；p.4: “three output format requirements: No Reasoning (NR), Short Reasoning (SR), and Long Reasoning (LR).” | 有明确操纵/变化的提示条件与至少两个水平，但未报告正式操纵程序、单位分配方式与操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | PDF p.3: “Correctness Attribution Bias (ABcor)” 与 “Incorrectness Attribution Bias (ABinc)” 公式；p.3-4: “Evaluation Inconsistency (EI)” 与 “Evaluation Preference (EP)” 定义；p.4: “binary scoring... 1-6 scale rubric.” | 因变量指标与计分方式明确，但未报告信效度证据，也未对比例/分数指标作天花板地板或预处理说明。 |
| A3 | 控制变量 | 0.5 | PDF p.3: “We randomize the position of correct and incorrect answers and the order of demographic options for each query”；p.4: “temperature = 0”；p.4: “only consider a problem ‘Solvable’... across all these temperatures.” | 报告了温度固定、位置随机化、可解题筛选等控制做法，但未形成系统的控制变量清单与逐一控制手段说明。 |
| A4 | 混淆变量 | 0.5 | PDF p.4: “we introduce a random perturbation baseline where demographic information is switched between random neutral placeholders”；p.6: “beyond random perturbation”；p.9: “we cannot fully explain its origins or causal mechanisms.” | 识别了模型随机性这一潜在混淆并用随机占位符基线处理，但对残余混淆和内部效度威胁讨论不充分。 |
| A5 | 调节变量 | NA | — | 研究没有明确的调节变量假设，也没有报告正式交互检验；Figure 3 对 NR/SR/LR 的比较是描述性条件比较，不作为调节分析编码。 |
| A6 | 中介变量 | NA | — | 研究不包含中介变量与中介效应分析。 |
| A7 | 操作性定义 | 1 | PDF p.2-3: 给出 Attribution 与 Evaluation 的完整提示模板与流程；p.3: 给出 ABcor、ABinc、EI、EP 公式；p.4: 说明错误解生成与评分规则；p.11: Appendix A 给出写作评分 rubric 与输出格式。 | 关键构念均有可观测的操作化：提示模板、任务材料、指标公式、计分方式和输出要求足以复现核心测量。 |
| A8 | 水平数与类型 | 0.5 | PDF p.3: Direct Labels vs. Name Proxies；p.4: NR/SR/LR 三种输出格式；p.4: 数学/编码/常识用 binary，写作使用 1-6 scale；p.5-6: race 与 gender 分组。 | 多数条件的水平数与标签已给出，但未系统说明水平类型、间距/全距及连续变量的中心化等细节。 |
| A9 | 单一操作化的风险 | 1 | PDF p.5: “attribution biases persist across all reasoning benchmarks”；p.5: “Using race-associated names as race proxies reveals similar biased attribution patterns”；Table 1 与 Figure 2 展示多任务、多模型结果。 | 关键构念使用了多种任务、指标和姓名代理/直接标签操作化，并报告了跨操作的一致性/会聚模式。 |
| A10 | 单一方法的风险 | NA | — | 该研究不是自陈式多构念测量，自变量为提示中的人口标签/条件，因变量为模型判定输出；共同方法偏差框架不适用于此类单渠道 LLM 提示实验。 |
| B1 | 被试间设计 | NA | — | 没有人类被试的独立组分配；不同模型和条件不是通过将独立被试分配到条件来实施的。 |
| B2 | 被试内设计 | NA | — | 没有人类被试式重复测量与顺序设计；同一问题在不同人口标签下以独立提示调用呈现，未报告被试内条件顺序平衡。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合设计及相应误差项分析。 |
| B4 | 因子设计 | NA | — | 研究比较多个模型、任务和条件，但没有建立正式因子设计，也未报告完整设计矩阵与主效应/交互 ANOVA。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应检验；人口群体差异用 Chi-Square/McNemar 等分别检验。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验；域/模型差异主要为描述性比较。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方设计。 |
| B9 | 准实验设计 | NA | — | 研究不是非随机分组的准实验，也未作准实验因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 研究不涉及人类被试内处理的可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有将独立被试/单位随机分配到互斥实验条件的机制；仅对选项位置与答案顺序做随机化，归入 E1 编码。 |
| C2 | 平衡 | NA | — | 没有人类被试条件顺序平衡问题；选项顺序随机化在 E1 中处理。 |
| C3 | 恒定 | 0.5 | PDF p.3: “five of the most commonly used LLMs: OpenAI GPT-3.5-turbo and GPT-4o...”；p.4: “All experiments... use temperature = 0”。 | 报告了温度固定与模型清单等恒定设置，但未讨论这些恒定选择对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未把潜在混淆变量作为协变量或区组纳入模型；随机扰动基线不是 ANCOVA 协变量。 |
| C6 | 盲法 | NA | — | 数据采集与评分为自动化 LLM 调用，无人类被试、主试或评分者盲法安排。 |
| C7 | 平衡的层级 | NA | — | 没有被试内条件顺序的平衡层级问题。 |
| D1 | 练习效应 | NA | — | LLM 提示为独立调用，未涉及跨试次练习效应或练习块安排。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长与疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件清洗期或迁移效应设计。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 主要因变量为归因百分比/评价不一致率等客观指标；写作评分虽为 1-6，但不涉及人类主观量表范围效应校准。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF p.3: “We randomize the position of correct and incorrect answers and the order of demographic options for each query.” | 明确报告了位置/选项顺序随机化，但未给出随机化方案类型、各位置出现次数、顺序组分配或位置效应检验。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分与默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表反应风格或跨群体端点/中点使用比例分析。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征与事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试/评分者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.5: “GPT-3.5-turbo assigns 82% of the correct solutions to the White group in GSM8K”；Table 1 与 Figure 2 报告了多种归因比例；p.4: “only consider a problem ‘Solvable’...”。 | 报告了比例型结果与若干端点化模式，但未报告均值/SD/偏度/端点频率表，也未系统说明难度校准与天花板地板效应。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念同源测量，不涉及共同方法偏差统计检验。 |
| F1 | 统计结论效度 | 0.5 | PDF p.5: “All attribution differences across demographics are statistically significant with Chi-Square tests”；p.7 Table 3: “McNemar tests: ** for p < 0.05 and * for p < 0.1.” | 报告了偏差比例/效应量与部分显著性检验，但无置信区间、样本量功效依据或明确多重比较校正。 |
| F2 | 内部效度 | 0.5 | PDF p.3: “We randomize the position of correct and incorrect answers and the order of demographic options”；p.4: “random perturbation baseline” 用于区分人口驱动偏差与模型随机性。 | 报告了部分随机化与基线控制，但无正式条件分配隐藏、基线等价性检验或被试流向/损耗处理；对内部效度威胁评估不完整。 |
| F3 | 构念效度 | 0.5 | PDF p.3-4: 自定义 ABcor/ABinc/EI/EP 指标；p.5: 多任务与 name proxy/direct labels 的一致性结果；全文未报告信度或正式 manipulation check。 | 有多操作化与会聚证据，但无指标信度、效度检验或操纵检验，构念效度论证不完整。 |
| F4 | 外部效度 | 0.5 | PDF p.3: 说明五个模型与各基准数据集来源；p.12: 额外加入 DeepSeek-V3 与 Qwen2.5-72B；p.9: 局限中承认机制与系统性检测方法有限。 | 报告了模型/任务来源和部分扩展样本，但未系统论证模型总体代表性、推广边界与跨情境复现。 |
| G1 | 分析单位 | 0.5 | PDF p.3: EI 定义为对 n 个问题跨人口群体评价的聚合；p.4: “We sample 100 solvable questions each from mathematics, coding, and commonsense reasoning tasks.” | 分析了问题/提示层级输出，但未显式处理问题嵌套于数据集、提示嵌套于模型及重复人口标签条件的聚集结构。 |
| G2 | 随机效应 | NA | — | 未使用混合模型或随机效应；研究把特定模型作为固定比较对象，不主张推广到模型总体，故不按随机效应组件编码。 |
| G3 | 材料作为随机效应 | 0.5 | PDF p.4: “We sample 100 solvable questions each from mathematics, coding, and commonsense reasoning tasks.”；p.5: 对归因比例做合并 Chi-Square 检验。 | 材料确实从基准中抽样，但分析中未把问题/材料作为随机效应纳入模型，项目层面可推广性处理不完整。 |
| G4 | 统计功效 | 0 | PDF p.4: 仅说明每类任务抽取 100 个可解题；全文无事前功效分析、预期效应量、目标功效或置信区间报告。 | 无样本量确定依据与功效分析，结果部分也缺 CI，故为 0。 |
| G5 | 研究者自由度 | 0.5 | PDF p.4: 详细说明可解题筛选、错误解生成与评分规则；p.5-7: 报告主要指标与部分附加结果；未说明样本量停止规则或验证性/探索性区分。 | 部分研究者自由度被报告，但未完整说明全部条件/因变量、样本量决定方式及探索性分析标注。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–14 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告预注册平台、注册编号或数据收集前分析计划；按规则记 0。 |
| J1 | 位置偏差 | 0.5 | PDF p.3: “We randomize the position of correct and incorrect answers and the order of demographic options for each query.”；p.4: “temperature = 0”。 | 对候选项/答案位置做了随机化，并报告模型与温度，但未报告位置交换前后的偏好翻转率或位置×正确率曲线。 |
| J2 | 冗长偏差 | 0.5 | PDF p.2: “we present identical solutions as being from different demographic groups”；p.4: 写作使用官方 1-6 rubric。 | 评价中使用同一解答文本可控制人口标签比较中的长度差异，但未报告解答长度分布、长度—得分相关或明确的长短偏好控制说明。 |
| J3 | 谄媚 | NA | — | 任务不涉及用户先验立场、反馈/纠错或多轮谄媚操纵。 |
| J4 | 自我偏好 | NA | — | LLM 评价的是基准/学生答案在不同人口标签下的评分，不是对不同模型生成输出的成对裁判，也未涉及裁判偏好本家族输出的自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，没有 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.3: 展示 Attribution/Evaluation 提示模板；p.11 Appendix A: 展示写作评价完整 rubric 与 JSON 输出格式。 | 提供了提示模板但无版本号、迭代日期、语义等价措辞敏感性消融或 dev/test 划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务上下文为短问题/答案，不是长上下文或 RAG 实验。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.4: “All experiments... use temperature = 0”；p.7: 代码颜色生成“repeated the request 50 times with temperatures ranging from 0 to 0.7”。 | 报告了温度设置与部分重复次数，但缺 top-p/top-k/seed、API snapshot、逐步置信区间等完整采样随机性报告。 |
| J9 | 重复与文本退化 | NA | — | 主要输出为选项 ID、评分或代码片段，评价重点不是开放式长文本生成质量，重复/退化率不构成本研究核心风险。 |
| J10 | 分词效应 | NA | — | 单语言英文刺激，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.2-3: 使用 GSM8K、MATH、HumanEval、CommonsenseQA、ARC-Easy、ASAP-AES 等公开基准；全文未报告训练截止日期、污染检测或 n-gram 重叠。 | 属于公开基准评测但未做测试集污染检查，也未与模型训练截止日期对照，记 0。 |
| J12 | 基准饱和 | NA | — | 研究不以基准准确率提升或 SOTA 饱和为结论目标，主要报告偏差比例指标，故基准饱和风险不适用。 |
| J13 | 指令遵循 | NA | — | 论文不以指令遵循为因变量，也未按约束类型系统测量指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p.3: “Output the option ID in each [cloze]”；p.11: “Provide your evaluation in the following JSON format”。 | 报告了输出格式要求，但未报告格式合法率、解析失败/重试策略，也未将格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 研究不是安全/越狱稳健性评估；虽提及拒绝率，但并非对抗攻击成功率评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.1: “Uncovering LLMs’ Hidden Beliefs”；p.2: 将“Veracity Bias”定义为模型把解答正确性与人口群体关联的偏差；全文未做与人类同名构念的系统对照实验。 | 研究把偏差/隐藏信念作为 LLM 构念来测量，并联系人类人口偏见，但未系统论证 LLM 构念与人类同名构念的异同。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随模型规模/训练进展的能力曲线或涌现能力宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有训练、RL、best-of-N 或对代理指标进行优化的环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.3: 列出五个模型名称与引用；p.4: “temperature = 0”；p.7 Table 3 使用 McNemar 检验；未给精确 snapshot/date 与 95% CI。 | 报告了温度、模型标识与部分配对检验，但缺精确 snapshot、重复采样 N/CI 和完整原始日志，可复现性报告部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评价/归因，不涉及多轮对话一致性衰减。 |

## 编码小结
论文提出了 LLM 的“真实性偏差”，包括归因偏差与评价偏差，并用多个公开基准、多个模型和自定义指标进行观察与比较。操作定义、提示模板和位置随机化报告较清楚，但整体仍属 LLM 基准式提示实验：缺少人类实验式的随机分配、盲法、预注册、功效分析与置信区间，部分人类被试组件不适用。
