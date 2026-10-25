# article_169 | From Tokens to Words: On the Inner Lexicon of LLMs | 2025

研究类型概述：这是一项 LLM 机制可解释性研究：用探测分类、logit lens、Patchscopes、注意力与 FFN 消融、以及无微调词表扩展实验，考察 LLM 是否在内部把子词整合为整词表征。分析单位主要是词/子词 token、层、模型输出与数据集样本；没有人类被试，也没有人类被试分配。
- **研究构念（Construct）**：子词到整词的词汇整合、词形恢复与内部词汇表征｜CA 构念锚定：词汇通达（lexical access, `trm_4a3fd79d0b80f`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）；阅读（reading, `trm_4a3fd79d0aeb6`）
- **实验任务与范式（Task / Paradigm）**：把原本单token词人为拆成2—5个子词，或加入拼写错误，并在四个冻结LLM逐层读取最后子词的隐藏表示，检查其何时恢复原词身份及FFN消融如何改变恢复轨迹。（操纵原词是否被拆分、拆分方式、拼写错误、单词是否在现有词表内、模型和层级，并消融相关FFN更新。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: 'We generate the nonwords by shuffling tokens...'; p.5: 'randomly split each single-token word longer than three characters into 2–5 sub-words'; p.8: identified FFN ablation vs random FFN ablation. | 论文报告了多个受控条件及其构造程序，但没有统一的操纵检验，也没有按心理实验意义上的单位分配方式说明。 |
| A2 | 因变量 | 0.5 | p.4: 'k-nearest neighbors (k-NN) probing classifier' with 80%/20% train/test split; p.5: 'rate of retrieval—the proportion of words...'; p.10: 'token-level top-1 accuracy'. | 因变量指标和计分方式明确，但未报告信度、效度、置信区间或针对连续指标的预处理/防端点效应说明。 |
| A3 | 控制变量 | 0.5 | p.4: nonword construction preserves prefix/suffix positional distributions; p.8: 'as a control... ablate an equal number of random FFN updates'; p.10: Original, Mean Embed., Ours baselines. | 报告了若干控制手段，但未系统列出控制变量清单并逐一说明。 |
| A4 | 混淆变量 | 0.5 | p.4: token co-occurrence explanation tested by using the penultimate token; p.18: false negatives/false positives analysis; p.8: random FFN ablation control. | 识别并控制了若干潜在混淆（如 token 共现、随机消融对照），但未系统讨论残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 研究没有理论上的调节变量假设，也没有相应的交互检验设计。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量或中介效应分解。 |
| A7 | 操作性定义 | 1 | p.4 nonword generation and kNN probing; p.5 logit lens; p.6 Patchscopes prompt; p.8 FFN ablation; p.9 3-step vocabulary expansion; p.1 code release. | 关键构念均给出可重复执行的操作化程序，且公开代码，足以复现。 |
| A8 | 水平数与类型 | 0.5 | p.4: 53% two-token words, 37.3% three-token, rest four-token; p.5: split into 2–5 sub-word tokens; p.8: 2-, 3-, and 4-token word analyses. | 报告了部分水平数与取值，但缺少系统说明水平类型、间距、全距或连续层变量的中心化等。 |
| A9 | 单一操作化的风险 | 1 | p.23: logit lens and cosine similarity produce 'nearly identical patterns'; p.8 random FFN ablation control; p.21 cross-model retrieval results. | 关键构念采用了多种操作化/指标，并报告了会聚证据（logit lens、cosine、Patchscopes、消融、多模型）。 |
| A10 | 单一方法的风险 | NA | — | 研究使用模型内部表征和客观计算指标，不存在人类自评式共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 没有人类被试间分配；同一模型被重复分析，词项也不是按心理实验被试组独立分配。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量及条件顺序平衡设计；层间比较是结构性分析，不是被试内处理顺序。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内混合设计及对应误差项。 |
| B4 | 因子设计 | NA | — | 没有因子设计矩阵、每格样本量和 ANOVA 主效应/交互表；主要是逐层曲线和分组比较。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 没有因子设计交互项检验；层间模式不是实验交互设计。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是需要报告非随机分组的选择偏差与因果局限的准实验研究。 |
| B10 | 被试内设计的适用条件 | NA | — | 不存在人类被试内设计的处理可逆性与迁移对称性问题。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥处理条件；80/20 划分只是探测分类的训练/测试划分，不是处理分配。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件呈现顺序。 |
| C3 | 恒定 | 0.5 | p.5 lists Llama2-7B, Llama3-8B, Mistral-7B, Yi-6B; p.5: last 100 tokens as context; p.6 Patchscopes prompt. | 模型和上下文长度等被固定，但未系统列出所有恒定变量及其水平，也未讨论其外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组因素或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 没有需要盲法的人类被试或人类评分者。 |
| C7 | 平衡的层级 | NA | — | 没有顺序效应平衡层级需要说明。 |
| D1 | 练习效应 | NA | — | 没有人类练习块或跨条件学习效应控制问题；模型推理过程也未按练习阶段设计。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长、休息间隔等疲劳控制设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各分析在独立上下文/输入上进行，没有跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 没有交叉处理顺序，因此不存在不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 研究不使用主观量表或绝对量值判断，不存在范围效应校准问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有选项顺序或多处理呈现顺序的随机化/反平衡；词内 token 顺序是刺激本身的一部分，非可随机化的呈现顺序。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 没有人类被试，因此不存在需求特征或事后假设推断访谈。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试或评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.4: probe peaks at 89%; p.5: 93.2% of split words retrieved in at least one layer; p.8: 95% baseline for country capitals; p.10 token-level accuracy table. | 报告了若干准确率/检索率，但未报告标准差、偏度、端点频率或 pilot 难度校准，端点效应风险未系统评估。 |
| E7 | 共同方法偏差 | NA | — | 没有多构念自陈式同源测量，不存在共同方法偏差检验问题。 |
| F1 | 统计结论效度 | 0.5 | p.20 Table 3 reports per-layer one-sided t-test p-values; p.4 uses 10,000 words; p.8 uses 5,571 words; many retrieval/accuracy rates are reported as percentages. | 报告了效应估计（准确率/检索率）和部分 p 值，但缺少置信区间、样本量功效依据和多重比较校正。 |
| F2 | 内部效度 | 0.5 | p.8: identified FFN ablation vs random FFN ablation control; p.10: Original, Mean Embed., Ours baseline comparison. | 有消融与基线对照，一定程度上评估内部效度，但没有随机分配、分配隐藏、被试流向或损耗处理。 |
| F3 | 构念效度 | 0.5 | p.23: logit lens and cosine similarity yield 'nearly identical patterns'; p.8 random FFN ablation control; p.18 ARC nonword comparison. | 提供了多种操作化与效度会聚证据，但缺少正式信度统计和操纵检验。 |
| F4 | 外部效度 | 0.5 | p.5: four LLMs; p.10: WikiText-103, PubMed, and Arabic Wiki40B; p.21: cross-model retrieval results. | 报告了多个模型和数据集来源并展示跨模型/跨域趋势，但未系统论证样本代表性或明确推广边界。 |
| G1 | 分析单位 | 0.5 | p.4: word-level dataset and kNN probing; p.8: 5,571 two-token words used in layer-wise t-tests; p.9: token-level vocabulary expansion evaluation. | 分析单位在词/token/层层面有描述，但未明确处理词项嵌套、上下文嵌套或多层重复观测的统计层级。 |
| G2 | 随机效应 | NA | — | 没有人类被试随机效应结构；四个模型作为固定比较对象，词项总体推广问题在 G3 中处理。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: 10,000 words sampled from the Gutenberg corpus; p.8: 5,571 two-token words from WikiText-103; analyses aggregate word-level accuracy. | 材料词项确实来自较大语料总体，但分析只报告聚合比例，没有用词项随机效应或混合模型来反映材料抽样不确定性。 |
| G4 | 统计功效 | 0 | p.4: 10,000 words; p.8: 5,571 words; p.20: only p-values for t-tests; no power analysis reported. | 没有事前功效分析或样本量论证，结果也缺少置信区间，仅以点估计和 p 值支持推断。 |
| G5 | 研究者自由度 | 0.5 | p.4 dataset composition and nonword construction; p.5 split/typo procedures; p.10 three evaluation datasets; no explicit exclusion/stopping/exploratory labeling. | 报告了主要条件和因变量，但未完整报告剔除规则、样本量决定方式，也未区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–26 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告数据收集前的公开预注册、分析计划或停止规则。 |
| J1 | 位置偏差 | NA | — | 研究不涉及多候选项选择、排序或 LLM-as-judge 成对比较，因此不存在候选位置偏差。 |
| J2 | 冗长偏差 | NA | — | 研究不使用 LLM 裁判评估开放生成质量，不存在长度被误当质量的冗长偏差。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场、反馈或纠错式对话，不涉及谄媚。 |
| J4 | 自我偏好 | NA | — | 研究不使用 LLM-as-judge 评估模型输出；Patchscopes 是同一模型对隐藏表征的解码，不是裁判偏好比较。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，没有 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.6: Patchscopes prompt 'Repeat this word twice: 1) X 2)'; p.8: 'The capital of [COUNTRY] is'; p.9: expansion template 'x x x x'. | 提供了部分 prompt 模板，但没有版本化、敏感性消融或 dev/test prompt 调参说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文仅约 100 个 token，远非长上下文/RAG 设置，不存在中间迷失或信息位置操纵问题。 |
| J8 | 温度与采样随机性 | 0 | p.5–p.6 describe model runs and Patchscopes; p.10 describes vocabulary expansion training; no temperature, top-p, seed, or repeated sampling statistics are reported. | 未报告解码采样超参、随机种子或重复运行 N 与方差/置信区间；生成式评测的非确定性未被纳入统计设计。 |
| J9 | 重复与文本退化 | NA | — | 任务主要是短词重复、检索和 token 级预测，不是开放长文本生成；重复/退化风险不是核心问题。 |
| J10 | 分词效应 | 0.5 | p.4: 'Llama2 tokenizer'; p.10: Arabic Wiki40B and token-level evaluation; p.25: token reduction rates across WikiText-103, PubMed, Arabic Wiki40B. | 报告了分词器和 token 数/缩减率，但没有精确 tokenizer revision，也未在所有跨语言能力比较中系统控制 token 数。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4: Gutenberg/WikiText data; p.10: WikiText-103, PubMed, Arabic Wiki40B; no model training cutoff or contamination detection reported. | 使用公开语料和预训练模型，但未报告训练截止日期对照、n-gram 重叠或污染率；无法排除预训练暴露对词表扩展评测的影响。 |
| J12 | 基准饱和 | NA | — | 研究不是标准 benchmark SOTA 比较，也未涉及基准饱和后的微小提升宣称。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，没有约束遵循准确率测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 研究不要求 JSON/结构化输出，格式合法率不是指标。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 footnote: 'This process might resemble the mental lexicon in humans'; p.3: 'inner lexicon'; p.7: models 'understand' words. | 论文使用人类心理词典类比和认知化表述，但没有系统比较 LLM 构念与人类同名构念，也没有人类对照数据。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究比较四个固定模型，不报告随规模/训练进展的涌现能力曲线，也不宣称突变式涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对代理指标（奖励模型/LLM-judge/benchmark）的优化和 overoptimization 监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.5 lists Llama2-7B, Llama3-8B, Mistral-7B, Yi-6B; p.10 reports accuracy table; no repeated-run N, confidence intervals, precise model snapshots, or paired tests are reported. | 只报告点估计和模型名称，缺少精确 snapshot、重复次数、置信区间与配对检验，评估可复现性不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究是单轮输入/分析，没有多轮对话历史累积与一致性衰减问题。 |

## 编码小结
论文在内部表征的多种操作化与收敛验证上较充分，方法细节和代码可复现性较好；但它不是心理学意义上的随机实验，许多人类被试设计组件（分配、顺序平衡、盲法、需求特征等）不适用。统计上缺少重复运行/置信区间、功效分析、预注册与部分 LLM 评估可复现性信息，且对分词器版本、数据污染、固定材料推广等问题报告不足。
