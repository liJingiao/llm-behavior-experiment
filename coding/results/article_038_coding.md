# article_038 | Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs | 2024

研究类型概述：本文是黑箱 LLM 置信度引出方法的系统基准评测：比较提示策略（Vanilla、CoT、Self-Probing、Multi-Step、Top-K）、采样策略（Self-Random、Prompt、Misleading）与聚合策略（Consistency、Avg-Conf、Pair-Rank），并在多个数据集与多个 LLM 上评估校准（ECE）和失败预测（AUROC、AUPRC）。分析单位是模型在题目上的回答/置信度输出，而非人类被试。
- **研究构念（Construct）**：元认知置信度、概率校准与过度自信（metacognitive confidence, calibration, and overconfidence）｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：本文是黑箱 LLM 置信度引出方法的系统基准评测：比较提示策略（Vanilla、CoT、Self-Probing、Multi-Step、Top-K）、采样策略（Self-Random、Prompt、Misleading）与聚合策略（Consistency、Avg-Conf、Pair-Rank），并在多个数据集与多个 LLM 上评估校准（ECE）和失败预测（AUROC、AUPRC）。分析单位是模型在题目上的回答/置信度输出，而非人类被试。｜CA 任务锚定：心理物理学任务（psychophysics task, `trm_502985b4baaed`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3–4: “we design a series of human-inspired prompting strategies”；Table 1 列出 Vanilla/CoT/Self-Probing/Multi-Step/Top-K；p.5 列出 sampling 与 aggregation 策略。 | 明确比较多个提示、采样、聚合水平，但未报告单位如何分配到条件及操纵检验，故只算部分完整。 |
| A2 | 因变量 | 0.5 | p.6: “we employ Expected Calibration Error (ECE) ... Area Under the Receiver Operating Characteristic Curve (AUROC) ... AUPRC-Positive ... AUPRC-Negative”；p.25 E.2 给出指标定义。 | 因变量指标与计分方式明确，但缺信度/效度证据及连续指标预处理、ECE 分箱等细节。 |
| A3 | 控制变量 | 0.5 | p.25 E.4: “we sample M = 5 responses ... temperature hyper-parameter as 0.7”；p.6 说明使用五个数据集和五类模型。 | 报告了温度、M、模型/数据范围等部分控制做法，但未系统列出控制变量清单并逐项说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.8: “CoT has significantly increased the accuracy ... reduction in overconfidence is due to the diminished gap between average confidence and accuracy, not necessarily ... ability”；p.24 D.3 重复该解释。 | 识别了准确率提升作为校准改善的潜在混淆，但未做系统控制或敏感性分析来讨论残余威胁。 |
| A5 | 调节变量 | NA | — | 未提出正式调节假设或交互检验；模型/任务差异只作分层描述，不构成调节分析，故不适用。 |
| A6 | 中介变量 | NA | — | 未提出中介变量或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | p.4 Table 1 列出各提示策略；p.26–29 Table 14–18 给出完整 prompt；p.5 给出 Consistency/Avg-Conf/Pair-Rank 公式；p.6/p.25 定义 ECE/AUROC 等指标。 | 关键构念的操作化程序较清楚：提示模板、采样方式、聚合公式和评估指标均可复现。 |
| A8 | 水平数与类型 | 0.5 | p.4 Table 1 列出 5 个提示水平；p.5 列出 3 类采样与聚合策略；p.6 列出 5 个模型和多类数据集；p.8 说明 M 从 1 到 13。 | 给出水平数与标签，但缺水平类型、间距/全距及连续变量中心化等完整说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.4–5 比较多种提示、采样与聚合操作；p.9 指出 “none of these techniques consistently outperform others”。 | 对关键构念采用多种操作化并比较，但未报告各操作之间的会聚证据，只报告相对性能。 |
| A10 | 单一方法的风险 | NA | — | IV 为输入提示操纵，DV 为模型输出与外部答案键计算的客观指标；不存在人类自评式共同方法偏差问题，故不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试分配；所有模型/题目在相同基准条件下评估，不是被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量或条件顺序设计；不同 prompt 作为独立 API 调用执行，顺序效应不构成设计组件。 |
| B3 | 混合设计 | NA | — | 未建立组间/组内因素混合设计，故不适用。 |
| B4 | 因子设计 | NA | — | 虽然比较多个因素，但未构成并分析正式因子设计：无设计矩阵、每格样本量和交互项统计检验。 |
| B5 | 主效应 | NA | — | 没有正式因子设计意义上的主效应统计检验，故不适用。 |
| B6 | 交互作用 | NA | — | 没有正式交互作用检验或简单效应分析，故不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层分配设计，故不适用。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方设计平衡条件顺序，故不适用。 |
| B9 | 准实验设计 | NA | — | 非准实验设计；不是在非随机分组下作因果推断的研究。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理可逆性/迁移对称性设计问题，故不适用。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥条件的程序；基准评测在同一组题目上比较各方法。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件顺序或被试顺序分配，故不适用。 |
| C3 | 恒定 | 0.5 | p.25 E.4: “we sample M = 5 responses ... temperature ... 0.7”；p.6 固定模型与数据集清单；p.21 Figure 7 说明重复采样。 | 报告了温度、M 等部分恒定控制，但未系统列出全部恒定变量及其水平，也未充分讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配程序，故不适用。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组或协变量纳入统计模型，故不适用。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者的盲法安排，故不适用。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 等顺序平衡层级，故不适用。 |
| D1 | 练习效应 | NA | — | LLM 各条件独立调用，无人类练习效应或跨试次学习；不适用。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳效应，且研究不是长时人类 session 设计；不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立 API 调用且无跨条件残留，不需要清洗期；不适用。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移问题；不适用。 |
| D5 | 范围效应 | NA | — | 无人类被试内绝对判断/量表范围效应设计；置信度端点堆积问题在 E6 下评估。 |
| E1 | 位置 / 顺序偏差 | 0 | p.6 使用 MMLU 的 Prf-Law 与 Biz-Ethics 等多选题；p.27 prompt 要求输出 “ONLY the option letter”；全文未说明选项顺序随机化或反平衡。 | 多选题目存在选项位置偏差风险，论文未报告任何选项顺序控制，也未讨论该偏差。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，也没有反向计分题；不适用。 |
| E3 | 极端 / 中间反应倾向 | 0.5 | p.6 Figure 2 与 p.19 Figure 5 报告置信度分布，主要是 80%–100% 且多为 5 的倍数；但未做跨模型反应风格校正。 | 报告了置信度端点/分布形态，但未系统讨论跨模型反应风格对比较的威胁。 |
| E4 | 需求特征 | NA | — | 无人类被试，也不需要掩饰情节或事后访谈检查需求特征；不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递；不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Figure 2 展示置信度分布和端点聚集；p.7 Table 2 报告各数据集指标；p.19 Figure 5 显示 100% 置信度下仍有大量错误。 | 报告了分布/端点频率并讨论 overconfidence，但未报告偏度、均值/SD 全表和 pilot 难度校准细节。 |
| E7 | 共同方法偏差 | NA | — | 非多构念自评量表研究，无同源自评共同方法偏差问题；不适用。 |
| F1 | 统计结论效度 | 0.5 | p.8 Table 3、p.9 Table 4 报告均值/方差；p.21 Figure 7 给出重复抽样的均值与误差棒；但全文未报告功效分析、95%CI 或多重比较校正。 | 有部分均值与方差信息，但缺样本量确定依据、效应量/CI、所有分析的多重性校正和统计假设说明。 |
| F2 | 内部效度 | NA | — | 没有人类随机分配、分配隐藏、被试流向与损耗；这是固定模型/数据集上的基准评测，不作人类 RCT 因果推断。 |
| F3 | 构念效度 | 0.5 | p.6/p.25 定义 ECE、AUROC、AUPRC；p.16 B.1 比较白盒 token-prob 方法；p.19 Figure 5 报告置信度分布。 | 提供标准指标与多指标结果，但缺正式信度/效度证据和 manipulation check，对单一操作化局限讨论有限。 |
| F4 | 外部效度 | 0.5 | p.6 列出数据集类型与模型清单；p.9 Limitations 指出 “Scope of Datasets ... leaving summarization and open-ended QA to the future work”。 | 报告了样本/任务范围与部分推广边界，但未说明抽样代表性或跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.6: “five types of datasets ... five widely-used LLMs”；p.7 Table 2 按模型与数据集分别报告指标。 | 分析在题目/答案层聚合并按模型/数据集分组报告，但未明确处理题目嵌套于数据集/模型的分析层级，也无多层模型。 |
| G2 | 随机效应 | NA | — | 统计结果不以混合模型呈现，模型/数据集被当作固定比较对象；无随机效应推广需求。 |
| G3 | 材料作为随机效应 | NA | — | 未把项目/材料作为随机效应作跨材料总体推断；题目只用于计算数据集级指标，故不适用。 |
| G4 | 统计功效 | 0 | p.6 与 p.25 只报告 M=5、温度 0.7 等实现设置；全文无功效分析或样本量/重复次数依据。 | 没有事前功效分析、目标效应量或样本量推导，也未在结果中系统报告效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.6 与 p.23 Table 13 报告多种数据集、模型和方法；p.25 E.4 说明 M=5 与温度；但无数据排除规则或验证性/探索性标注。 | 报告了较多因变量与条件，但缺排除规则、样本量决定方式和验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册平台、注册编号或数据收集前分析计划。 | 无预注册；也未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | 0 | p.6 使用 MMLU 多选题；p.27 prompt 要求输出 option letter；p.3–5 的 Top-K/排序聚合未说明候选位置反平衡或位置×正确率。 | 存在选项/候选位置偏差风险，论文未做位置随机化、交换重判或报告翻转率。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放式生成质量；没有长度与质量混淆的裁判场景。 |
| J3 | 谄媚 | 0.5 | p.4: “Misleading, feeding misleading cues to the model, e.g., ‘I think the answer might be ...’”；p.18–19 Table 11 列出 Weak/Strong Claim/External Source 提示；p.21–22 Table 12 报告不同提示组结果。 | 操纵了用户先验/误导提示并报告性能，但未报告答案翻转率，也未区分 answer sycophancy 与 feedback sycophancy。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 或模型间成对评判，无自我偏好偏差问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示；Top-K 中的格式示例不是 few-shot 示例，故不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.26–29 Table 14–18 给出完整 prompt；p.4 Table 1 比较多种提示；p.16 B.2 还比较 confident/cautious role prompt。 | 提供了模板并做了部分提示变体比较，但无版本号/迭代日期、dev/test 分离和系统语义等价敏感性消融。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG 实验；上下文远低于长窗口设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.25 E.4: “Self-Random ... temperature ... 0.7”；“sample M = 5 responses”；p.21 Figure 7 对每个 M 随机采样 5 次并报告均值/方差。 | 报告了主要温度与重复采样，但缺 top-p/top-k、随机种子、精确 API snapshot 和 95%CI。 |
| J9 | 重复与文本退化 | 0.5 | p.25 E.4 报告 Self-Random 的温度 0.7；p.21 Figure 7 报告重复抽样；但全文未统一报告 greedy/beam/sampling 及 repetition penalty/退化率。 | 部分报告了解码设置，但缺重复率/退化率 QC，且各条件解码策略未完整记录。 |
| J10 | 分词效应 | NA | — | 单语言英文任务，无跨语言/跨脚本比较；不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.5–6 使用 GSM8K、StrategyQA、MMLU 等公开基准和多个闭源模型；全文未对照模型训练截止日期或做污染检测。 | 未评估测试集与预训练/微调数据重叠，无法排除记忆复现。 |
| J12 | 基准饱和 | NA | — | 所用任务并非接近天花板，研究也不在饱和基准上宣称显著提升；不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，故不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.27–29 prompt 明确要求 “ONLY the option letter / number” 等严格格式；p.25 Figure 8 给出输出示例；但未报告格式合法率或解析失败率。 | 有格式约束设置，但未报告格式合法率和重试/后处理规则，格式失败与内容错误未分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估，无有害请求或攻击成功率测量。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: “similar to how humans talk about confidence”；p.6: “models might be imitating human expressions when verbalizing confidence”；p.24 D.3 讨论人类不确定性表达。 | 提及 LLM 置信度与人类同名构念的关系，但未系统做构念异同论证或人类对照实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未宣称涌现/突变能力；虽比较模型规模趋势，但不做涌现指标假象分析。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标的训练/RL/best-of-N 优化；只是评估已有方法。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.18 Table 7 使用 chatgpt-0613；p.25 E.4 报告 M=5 与温度 0.7；p.21 Figure 7 报告 5 次随机抽样均值/方差；但主模型 snapshot 与 CI/配对检验不足。 | 有一定重复与方差报告，但缺精确 snapshot、统一 95%CI 和模型间配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮问答；Self-Probing 使用独立 chat session，不积累多轮历史，故不适用。 |

## 编码小结
研究提供了较完整的算法框架、提示模板、聚合公式和多模型多数据集结果，适合作为置信度引出基准。其主要不足是基准评测常见的可复现性与推断问题：缺少预注册、功效/样本量依据、置信区间与多重比较校正、精确 snapshot、基准污染检查，以及对选项位置、输出格式合法率、用户提示导致的翻转率等 LLM 特有偏差的系统控制。
