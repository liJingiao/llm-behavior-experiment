# article_045 | Diminished diversity-of-thought in a standard large language model | 2023

研究类型概述：LLM-as-participant / replication benchmark：用 OpenAI text-davinci-003 复现 Many Labs 2 中的 14 项心理学调查，每项约 1000 次独立 API 运行；另做答案顺序反转与人口学提示的探索性随访。分析单位是 LLM 运行（run），主要比较提示条件间的回答分布、效应量与复现率。
- **研究构念（Construct）**：思维多样性衰减、反应稳定性与社会心理偏差（diversity of thought, response stability, and social-psychological bias）｜CA 构念锚定：计划（planning, `trm_4a3fd79d0acc1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：LLM-as-participant / replication benchmark：用 OpenAI text-davinci-003 复现 Many Labs 2 中的 14 项心理学调查，每项约 1000 次独立 API 运行；另做答案顺序反转与人口学提示的探索性随访。分析单位是 LLM 运行（run），主要比较提示条件间的回答分布、效应量与复现率。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: 'we collected data for a total of 14 studies ... each ... about 1,000 different runs'; p.10 Table 1列出各研究条件；p.18 Table 3列出反向顺序条件。 | 各复现研究的提示条件及水平有报告，且给出每条件样本量；但未报告操纵检验，条件分配程序也主要是分别调用 API，不够完整。 |
| A2 | 因变量 | 0.5 | p.5: 'removed all entries that responded to questions with characters that were not among the possible response categories'; p.10 Table 1报告Cohen's d/OR及95%CI；p.44说明按Many Labs 2方案分析。 | 因变量指标与计分方式有界定，并报告效应量/CI及数据清洗规则；但未报告量表信度、效度证据及针对连续指标/端点效应的系统预处理说明。 |
| A3 | 控制变量 | 0.5 | p.43-44: max_tokens=2048, stop=None, temperature=1.0, model=text-davinci-003；p.44: 每条件520 runs等。 | 列出了模型版本、温度、最大token、停止符等主要恒定控制；但未系统列出种子、top-p/top-k、调用时间/环境等控制，控制清单不完整。 |
| A4 | 混淆变量 | 1 | p.17-19报告反向答案顺序的随访及翻转率；p.20报告随机人口学提示随访；p.23-25讨论顺序效应、训练数据/后处理等残余解释。 | 识别并实际检验了答案顺序与人口学提示两个潜在混淆，同时在讨论中如实说明模型封闭、记忆/训练数据等残余威胁。 |
| A5 | 调节变量 | NA | — | 研究没有调节变量理论模型；答案顺序和人口学提示是稳健性随访/操纵，而非正式调节假设与交互/简单斜率分析。 |
| A6 | 中介变量 | NA | — | 研究不包含中介变量或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.5及p.43-45说明提示构造、模型参数、输出txt到csv、数据清洗与按Many Labs 2方案分析；p.31提供OSF代码与数据链接。 | 关键操纵与测量均有可复现的操作化说明，且代码/数据公开，足以支持重复执行。 |
| A8 | 水平数与类型 | 0.5 | p.10 Table 1列出各研究条件描述；p.47报告六点/七点量表与 'strongly conservative' 到 'strongly liberal' 的等级；p.18 Table 3列出反向顺序。 | 多数条件的水平数与标签有报告；但未系统给出每个自变量的水平类型、间距、全距及连续变量中心化/标准化说明。 |
| A9 | 单一操作化的风险 | 1 | p.22 Table 4用L1、L2、cosine多种指标比较MFT向量；p.30: 'our method ... is an entirely text-based attitudinal response method. This limits the external validity'。 | 通过多研究、多指标提供一定会聚证据，并在局限部分明确讨论单一文本调查方法对推广的限制。 |
| A10 | 单一方法的风险 | 0.5 | p.30: 'our method ... is an entirely text-based attitudinal response method. This limits the external validity'；全文未报告共同方法偏差统计检验。 | 研究所有构念均来自同一LLM文本提示-回答渠道，作者承认方法单一；但未报告Harman、marker variable等共同方法偏差检验或程序控制。 |
| B1 | 被试间设计 | 1 | p.5: 'each run representing a new call to the model’s API'；p.44: '520 runs per condition ... total of 1,040 runs'。 | 每个LLM run只接受一个提示条件，条件间由独立API调用承担，并报告了各条件样本量；符合被试间/运行间逻辑。 |
| B2 | 被试内设计 | NA | — | 主设计不是让同一LLM run接受同一自变量的所有水平；调查内的多题重复不等同于被试内条件设计。 |
| B3 | 混合设计 | NA | — | 没有组间×组内混合设计，也没有逐因素标注组间/组内并分别报告误差项。 |
| B4 | 因子设计 | NA | — | 各复现研究基本为单因素条件比较，未形成需要完整设计矩阵的因子设计。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应分析；单因素条件比较不适用。 |
| B6 | 交互作用 | NA | — | 没有因子设计交互项；顺序/人口学随访不是正式交互设计。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；LLM条件由提示文本设定，不存在人类选择偏差/非随机分组的情境。 |
| B10 | 被试内设计的适用条件 | NA | — | 纯运行间设计，不涉及被试内处理可逆性/迁移对称性。 |
| C1 | 随机化 | 0 | p.44: '520 runs per condition'；未报告随机分配方法、随机数工具或分配隐藏。 | LLM runs被分到互斥提示条件，但条件由研究者分别构造/调用，未见概率随机分配或随机化程序。 |
| C2 | 平衡 | NA | — | 条件间为独立run，不存在需要平衡的被试内条件顺序；答案选项顺序问题在E1/J1编码。 |
| C3 | 恒定 | 1 | p.43-44: text-davinci-003, temperature=1.0, max_tokens=2048, stop=None；p.29讨论仅适用于GPT3.5的局限。 | 明确列出主要恒定变量及水平，并讨论模型特异性对推广的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作区组/协变量纳入模型的设计；顺序问题仅以探索性反向条件处理。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 每次run为独立API调用，无跨试次上下文学习或练习效应。 |
| D2 | 疲劳效应 | NA | — | LLM无疲劳效应；每个run为独立短提示。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立调用、无跨条件上下文残留，迁移/清洗期不适用。 |
| D4 | 不对称迁移 | NA | — | 同上，无跨条件不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 虽使用量表题，但每个run只处于一个条件，不存在被试内跨条件绝对判断的范围效应设计。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.17-19: 对六个出现“correct answer”的研究做反向选项顺序随访，Table 3报告66.7%稳健；p.47: 明确说未随机化15题顺序。 | 有部分反向顺序控制并报告翻转结果，但主实验未随机化/完全平衡选项顺序，仅对部分条件做随访。 |
| E2 | 默认赞同 | 0 | p.47: MFT使用六点量表，未报告反向计分题；p.49 Figure S1仅显示选项顺序反转后的政治倾向。 | 使用Likert式自评量表，但未见反向计分题、正反向一致性检验或默许偏差讨论；答案顺序反转不等于反向计分。 |
| E3 | 极端 / 中间反应倾向 | 1 | p.12: '99.6% ... self-identified as a maximally strong conservative'；p.18 Table 3报告原序/反序分布；p.23讨论GPT自由派仍呈右倾MFT。 | 报告了大量端点/分布比例，并把GPT的极端一致反应与人类多样性比较，明确指出其对组间比较和构念解释的威胁。 |
| E4 | 需求特征 | NA | — | 研究对象为LLM而非人类被试，不存在人类需求特征或事后猜测研究假设的访谈。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.12: 'we define a “correct answer” to be an answer given by 99% or more ... although this threshold is arbitrary'；p.13: '100% ... preferred the movie star’s kiss'；p.17: d=9.25。 | 报告了明显的端点堆积/天花板现象并讨论其后果；但未报告预实验难度校准或任务难度参数对区分度的影响。 |
| E7 | 共同方法偏差 | NA | — | 自变量是提示条件操纵，不是与因变量同源的自陈式多构念测量；不构成典型CMB设计。 |
| F1 | 统计结论效度 | 0.5 | p.10 Table 1报告Cohen's d/q/OR及95%CI；p.44报告各条件N；全文未见正式功效分析或多重比较校正。 | 效应量与置信区间报告较完整，也报告了未显著/不可分析结果；但样本量依据主要是“约1000 runs”的实际考虑，缺正式功效分析/多重性校正说明。 |
| F2 | 内部效度 | 0.5 | p.44说明数据收集与样本量；p.17-19用反向顺序检验顺序效应；p.23-30讨论模型版本、记忆/训练数据等内部效度威胁。 | 对顺序、模型特异性和残余解释有讨论，但无随机分配、分配隐藏或基线等价性检验；内部效度评估为部分。 |
| F3 | 构念效度 | 0.5 | p.23-24: 'LLMs and humans constitute fundamentally different cognitive systems'；p.30讨论文本调查与表面记忆对构念解释的限制。 | 对LLM构念与人类构念对应关系有实质讨论，但未报告量表信度、效度统计或操纵检验，构念效度证据不完整。 |
| F4 | 外部效度 | 0.5 | p.29: 结果可能只适用于GPT3.5；p.30: 'entirely text-based attitudinal response method'；p.20报告人口学提示随访。 | 报告了模型来源并明确讨论模型、方法和情境推广边界；但只有单一模型/文本情境，缺跨模型或系统性跨样本复现。 |
| G1 | 分析单位 | 1 | p.5: 'each run representing a new call to the model’s API'；p.44按条件报告520/1040 runs；分析在run层级进行。 | 处理分配单位与统计分析单位均为独立LLM run，未出现把高层分配当低层独立观测的分析单位错误。 |
| G2 | 随机效应 | NA | — | 研究只使用单一固定模型/版本，无被试或材料随机效应推广需求，未使用混合模型。 |
| G3 | 材料作为随机效应 | 0.5 | p.5: 从Many Labs 2的28项中排除14项后分析14项；p.10-11逐研究报告结果；p.30承认子样本因排除图形材料而非随机。 | 使用了多项固定调查材料并逐研究报告，但未把研究/材料作为随机效应建模；作者承认子样本非随机，故为部分满足。 |
| G4 | 统计功效 | 0.5 | p.44: 'we collected 520 runs per condition ... total of 1,040 runs'，目标是约1000 runs；p.10 Table 1报告效应量与95%CI。 | 报告了效应量与CI，并给出大样本收集的实际理由；但没有事前功效分析或明确目标效应量/功效推导。 |
| G5 | 研究者自由度 | 0.5 | p.5及p.45说明剔除未完整/无效回答；p.32说明探索性分析与预注册分析的区别；但每研究剔除数和中途停止规则未完整列出。 | 报告了排除规则、总样本和主要条件，并明确区分验证性与探索性分析；但研究者自由度披露不完整。 |
| G6 | 预先设定 / 预注册 | 1 | p.4: 'We pre-registered this study on the Open Science Framework (Park et al., 2023)'；p.32: 'Most experiments were pre-registered ... exploratory ... indicated as such'。 | 提供OSF预注册链接，说明主分析预注册，并明确标注探索性随访及因“correct answer”偏离预注册分析计划。 |
| J1 | 位置偏差 | 0.5 | p.17-19 Table 3报告原序与反向顺序的回答分布及稳健率（66.7%）；p.25讨论primacy/recency；p.47说明未随机化题目顺序。 | 对部分研究的答案选项顺序做反向检验并报告翻转率，但主实验未做全条件位置随机化/反平衡，且未报告所有位置×正确率曲线。 |
| J2 | 冗长偏差 | NA | — | 研究不使用LLM-as-judge评估开放式生成质量，不涉及长度—质量偏差。 |
| J3 | 谄媚 | NA | — | 无用户先验立场/反馈/纠错式对话操纵，不涉及谄媚。 |
| J4 | 自我偏好 | NA | — | 未使用LLM裁判或成对模型输出比较，不涉及自我偏好偏差。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，无few-shot示例选择/排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.6 Figure 1给出样本输入/输出与CHECKLIST；p.43-44说明格式化指令；p.31提供OSF代码。 | 通过图例和OSF代码可获得提示模板，但正文未给完整模板版本号/迭代日期，也未做语义等价提示的敏感性消融或dev/test划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短调查提示，无长文档/RAG或中间迷失操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.43-44: temperature=1.0, max_tokens=2048, stop=None, 每call n=10；p.44报告每条件约520 runs；全文未报告seed/top-p/top-k/精确API snapshot。 | 报告了关键采样参数和大量重复运行、给出效应量CI；但缺完整解码超参、随机种子/固定策略和精确API日期。 |
| J9 | 重复与文本退化 | 0.5 | p.43-44报告temperature=1.0、max_tokens=2048、stop=None；p.5说明txt到csv及无效回答剔除；未见n-gram重复率/退化率。 | 报告了基本解码设置，但未报告repetition penalty、重复/退化QC或截断比例。 |
| J10 | 分词效应 | NA | — | 单语言英文提示与回答，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.24: 'it is sometimes unclear whether its answers ... were memorized from the training data'；p.30提到 'surface-level memorization'；但未做测试集版本/训练截止日期对照或污染检测。 | 作者意识到训练数据记忆风险，但未报告测试集版本、模型训练截止日期、n-gram重叠或污染率。 |
| J12 | 基准饱和 | 0.5 | p.12定义“correct answer”为99%以上相同回答；p.13报告100%选择kiss；p.17报告d=9.25的极端效应。 | 明确识别了天花板/饱和现象并停止把不可构造统计量当作显著效应；但未改用连续指标或更难held-out子集，也未做bootstrap CI比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；格式化指令只用于数据收集/清洗，未按约束类型测量指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.6 Figure 1显示输出格式指令与CHECKLIST；p.5和p.45说明剔除含无效字符/未完整回答的run；未报告格式合法率。 | 有格式约束设置和剔除规则，但未报告格式合法率、重试策略，也未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 1 | p.23-24: 'empirical findings on GPT3.5 ... should not be assumed to generalise to the human case'；p.24: 'fundamentally different cognitive systems'；p.29报告模型版本限制。 | 明确把LLM上测得的调查反应与人类同名构念作理论异同讨论，使用人类原始/ML2数据作同范式对照，并明确反对直接外推；报告了模型版本（虽未给精确API日期）。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 单模型单时点研究，不涉及跨规模/训练进展的涌现曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL、best-of-N或对代理指标的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.44报告每条件520/1030等N；p.10 Table 1报告95%CI；p.31提供OSF数据与代码；模型标识为text-davinci-003，但无精确API snapshot日期。 | 报告了重复次数、置信区间和数据/代码，具备较好可复现性；但模型snapshot标识不精确，且单模型无需配对模型比较。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮调查提示，无多轮对话历史累积。 |

## 编码小结
该文核心贡献是发现 GPT3.5 在多项社会心理调查中出现零/近零变异的“correct answer”效应，并检验答案顺序与人口学提示的稳健性。设计透明、预注册与数据/代码可得性较好，效应量与置信区间报告较完整；但作为 LLM 行为研究，随机化/顺序平衡、采样参数完整记录、污染检查、量表信效度与若干 LLM 特有偏差控制仍有明显缺口。
