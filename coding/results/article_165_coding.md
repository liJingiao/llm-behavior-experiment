# article_165 | Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book? | 2025

研究类型概述：NLP benchmark/ablation study：用长上下文 LLM、Llama、NLLB 比较语法书整体/平行例子/解释文本/类型学提示/少样本等条件，在 Kalamang、Nepali、Guarani 翻译、语法判断和 IGT 预测任务上评测。无人类被试，分析单位为 prompt 设置、模型、语言/任务和测试集分数，不是心理学被试实验。
- **研究构念（Construct）**：显式语法知识利用、示例学习与规则学习差异、跨语言泛化及任务—知识形式匹配｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）；句法加工（syntactic processing, `trm_4a3fd79d0b34b`）
- **实验任务与范式（Task / Paradigm）**：只依据冻结的Gemini与Llama-Instruct长上下文提示实验：分别向模型提供完整语法书、仅平行例句、仅语法解释、词表或类型学特征提示，并在翻译、语法可接受性判断和gloss预测中比较行为；NLLB与LoRA微调结果仅作外部基线，不作为纳入依据。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5 p.5: 'We prompt with the entire grammar, BOOKall, in-context...'；p.6 p.6 Table 2 列出 0-shot、WORDLIST、5*-SHOT、PARAbook、BOOKall、BOOKpara、BOOKnon-para、TYP 等条件。 | 有明确的条件操纵与水平标签，但未报告随机分配、分配隐藏或操纵检验；对 LLM benchmark 而言属于条件比较，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.5 p.5: 'We evaluate translation automatically with CHRF++'；p.9 p.9 Table 5 报告 Morpheme Acc./Word Acc./Stem F1/Gram F1/CHRF++；p.8 p.8 Figure 1 报告 grammaticality accuracy。 | 因变量指标和计分方式基本明确，但无信度/效度证据；仅说明截断首行等预处理，缺少完整分布与防天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | p.5 p.5: 使用 'Gemini-1.5-Flash-001'、'Llama-3.1-8B base and instruction-tuned'、'NLLB-1.3B-Distilled'；p.5 p.5: 'scores for trimmed responses after the first newline character'。 | 报告了部分保持恒定的模型、评价指标和输出截断规则，但没有系统列出控制变量清单及逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | p.9 p.9: 'We fit univariate least squares regression models to CHRF++ scores with test set type coverage as the independent variable'；同页还用 prompt tokens 检验长度混淆；p.10 p.10 讨论 needle-in-a-haystack。 | 识别并统计建模了 test type coverage 和 prompt length 等潜在混淆，但对残余混淆与内部效度威胁未做系统敏感性分析。 |
| A5 | 调节变量 | NA | — | 研究没有调节变量假设或乘积项交互检验；语言/模型差异只是描述性分组或重复实验，不构成正式调节分析。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量或直接/间接效应分解；test type coverage 用作回归自变量解释分数，不是中介模型。 |
| A7 | 操作性定义 | 1 | p.3-4 p.3 p.4 描述语法书过滤、BOOKpara/BOOKnon-para、PARAbook、PARAtrain、WORDLIST、TYP 构造；p.4 p.4 描述 SWAPadj/SWAPran/SHUFFLE 语法判断；p.4-5 p.4 p.5 描述 IGT 训练/测试与 NLLB/LoRA 微调参数。 | 关键操纵与任务的操作化程序较具体，含数据来源、prompt 类型、模型、微调参数和评价指标，可据以复现。 |
| A8 | 水平数与类型 | 0.5 | p.5 p.5 Table 1 给出 BOOKpara/BOOKnon-para 的行数与 token 数；p.6 p.6 Table 2 给出各 prompt 设置的 CHRF++ 与 token 数；p.20 p.20 Table 8 给出 prompt 示例。 | 条件水平与标签、部分取值/token 数明确，但未系统说明水平类型、间距/全距，连续变量（token、type coverage）入回归时也未报告中心化/标准化。 |
| A9 | 单一操作化的风险 | 1 | p.3 p.3 脚注称 'We omit human evaluation... given the infeasibility of engaging proficient Kalamang speakers'；p.21-22 p.21 p.22 讨论 CHRF++ 小差异与定性分析必要性；p.8-9 p.8 p.9 用翻译、语法判断和 IGT 多任务会聚。 | 关键构念通过多任务/多语言/多模型操作化，并对翻译仅用自动指标及人类评价不可行的局限作了明确讨论。 |
| A10 | 单一方法的风险 | NA | — | 自变量为 prompt/数据条件，因变量为自动 CHRF++/accuracy 等，非自陈同源测量；无共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试或被试组分配；不同 prompt/模型是 benchmark 条件，不是独立被试组。 |
| B2 | 被试内设计 | NA | — | 虽同一测试集在多条件下重复评测，但无人类被试内重复测量与条件顺序安排；不按被试内设计编码。 |
| B3 | 混合设计 | NA | — | 没有组间/组内人类因素混合设计，也无混合 ANOVA 误差项结构。 |
| B4 | 因子设计 | NA | — | 存在多条件评测网格，但不是正式因子实验；全文未做折因 ANOVA/主效应与交互项统计，按规则该组件不适用。 |
| B5 | 主效应 | NA | — | 无正式因子设计的主效应检验。 |
| B6 | 交互作用 | NA | — | 无正式交互项统计检验或简单效应分析；仅描述不同模型/语言下的分数模式。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；没有非随机分组后的因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | benchmark 条件比较，无研究单位被随机分配到互斥条件的程序；单次/独立 prompt 调用不涉及分配隐藏。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件呈现顺序；不同 prompt 设置分别独立运行。 |
| C3 | 恒定 | 0.5 | p.5 p.5: 固定使用 'Gemini-1.5-Flash-001'、'Llama-3.1-8B base and instruction-tuned' 和 'NLLB-1.3B-Distilled'；p.5 p.5: 'trimmed responses after the first newline character'；p.22 p.22 讨论 API-only 模型限制。 | 报告了部分恒定因素（模型版本、输出截断、评价指标），但未系统列出全部恒定变量及水平，也未充分讨论其外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.9 p.9 将 test set type coverage 作为自变量回归 CHRF++，并检验 prompt token 与分数关系；p.9-10 p.9 p.10 用覆盖率解释语法解释文本的虚假优势。 | 已知混淆被测量并纳入回归分析，但未做 ANCOVA 式调整、斜率齐性检验或调整后效应量报告。 |
| C6 | 盲法 | NA | — | 全自动 API/模型评测，无人类被试、主试或评分者可施盲。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | LLM 各 prompt 条件独立调用，无试次内练习效应；人类练习效应不适用。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题；模型长上下文调用不按疲劳效应编码。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立运行，无跨条件学习/残留迁移的清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉条件，无不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 主要因变量为 CHRF++、accuracy、morpheme accuracy 等客观指标，不是李克特/绝对量值判断。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无人类被试内刺激序列或多选项顺序平衡；LLM 选择/候选位置偏差在 J1 中评估。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，无需求特征或事后访谈问题。 |
| E5 | 实验者效应 | NA | — | 完全自动化 API 评测，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.8 p.8 Figure 1 报告 grammaticality accuracy；p.9 p.9 Table 5 报告各指标分数；p.18 p.18 Table 6 报告高资源语言上界并说明 kgv 测试集偏弱。 | 报告了均值/分数和部分上界校准，但未报告标准差、偏度或端点频率；对天花板/地板风险只有间接讨论。 |
| E7 | 共同方法偏差 | NA | — | IV 与 DV 来源天然分离（prompt/数据条件 vs 自动指标），无共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | p.18 p.18 Appendix B 报告 F、R2、p 与 Pearson r；p.21 p.21 提到 CHRF 差异需 3.05 才具实践意义；p.5 p.5 无样本量功效分析。 | 报告了部分效应量（R2、r）和显著性，但无置信区间、无事前功效分析，也未系统说明多重比较校正。 |
| F2 | 内部效度 | 0.5 | p.9 p.9 用覆盖率/长度回归评估混淆；p.21-22 p.21 p.22 讨论小测试集、API-only 模型和定性分析限制；无随机分配或被试流向。 | 对部分内部效度威胁（词汇覆盖、长度、测试集规模）作了评估，但不是随机实验，也无分配隐藏/基线等价/损耗流程。 |
| F3 | 构念效度 | 0.5 | p.5 p.5 使用 CHRF++ 并引用 Popović；p.9 p.9 Table 5 使用既有 IGT 指标；p.8-10 p.8 p.9 p.10 用语法判断/IGT/翻译多任务论证构念。 | 使用了既有指标和多任务证据，但没有报告信度/效度统计或操纵检验；构念与任务对应关系有讨论但不够系统。 |
| F4 | 外部效度 | 1 | p.4-5 p.4 p.5 报告 kgv、npi、gug 数据来源与 FLORES/ Dictionaria 测试集；p.7 p.7 报告跨语言结果；p.21-22 p.21 p.22 明确讨论测试集规模、模型可及性和推广边界。 | 报告了多语言/多模型复现与样本来源，并在限制中明确推广边界，外部效度报告较完整。 |
| G1 | 分析单位 | 0.5 | p.10 p.10 Figure 2 以各 prompt 设置为回归点建模 CHRF++ 与 coverage；p.6 p.6 Table 2 为聚合测试集分数；全文未显式讨论测试句/设置嵌套。 | 说明了分析在 prompt 设置/测试集聚合层进行，但未说明处理分配层级与项目嵌套结构，也未使用多层模型分离测试句方差。 |
| G2 | 随机效应 | NA | — | 无人类被试随机效应；模型/设置被视为固定比较对象，不存在被试抽样总体推断。 |
| G3 | 材料作为随机效应 | 0.5 | p.5 p.5 报告 kgv 100 例、npi/gug FLORES 1012 例、IGT 97 例测试集；p.6 p.6 与 p.9 p.9 仅报告聚合指标；未报告 item random effects 或混合模型。 | 承认测试集是有限样本并跨语言/任务复现，但分析未把测试句/材料作为随机效应，仍有语言作为固定材料集的推广风险。 |
| G4 | 统计功效 | 0 | p.5-6 p.5 p.6 无事前功效分析；p.18 p.18 仅报告显著性与 R2；p.21 p.21 提到测试集小但无功效推导。 | 无目标功效、预期效应量与样本量推导，也无置信区间；仅报告点估计和显著性。 |
| G5 | 研究者自由度 | 0.5 | p.5 p.5 报告数据/代码可用及首行截断规则；p.6 p.6 Table 2 列出多数条件，并用 '–' 标出上下文长度不允许的设置；p.8-9 p.8 p.9 报告多任务结果。 | 报告了大部分条件和排除/截断规则，但未明确区分验证性与探索性分析，也未说明样本量决定和中途停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | p.5 p.5 仅称 'Data (including grammar book splits) and code are made available'；全文未见预注册平台、编号或分析计划。 | 无预注册；研究含明确假设与多条件比较，故记 0 而非 NA。 |
| J1 | 位置偏差 | 0 | p.4 p.4: 'We ask the model to choose the original Kalamang test sentence against a modified example'；未报告 original/modified 位置交换、随机化或翻转率。 | 语法判断是 LLM 选择任务，存在候选位置偏差风险，但论文完全未提及位置反平衡或交换前后比较。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放生成质量；翻译用 CHRF++，语法判断/IGT 用自动准确率。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话，不涉及谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 裁判或成对 LLM 偏好评估，无自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.4 p.4 说明 5*-SHOT 基于最长公共子序列检索 5 个例子；p.5 p.5 说明 5*-SHOT 使用 PARAbook、npi/gug 用 FLORES dev；p.20 p.20 Table 8 给出示例格式。 | 报告了 few-shot 示例来源和数量，但未做多 seed 重采样、排列反平衡，也未报告标签比例/模板全文等完整控制。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.3-5 p.3 p.4 p.5 描述 0-shot、WORDLIST、PARAbook、BOOK、TYP 等 prompt；p.20 p.20 Table 8 给出各设置 excerpt；p.19 p.19 Table 7 给出 TYP prompt extract。 | 提供了较详细的 prompt 示例和可复现代码链接，但未给完整模板版本号、未做语义等价措辞敏感性消融、未说明 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p.6 p.6 Table 2 报告 BOOKall 约 99.6k tokens、BOOKnon-para 约 81.3k tokens；p.10 p.10 讨论 needle-in-a-haystack 和相关信息比例。 | 报告了实际上下文 token 数并讨论长上下文检索困难，但没有操纵关键信息首/中/尾位置或报告位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0 | p.5 p.5 仅报告 API 模型和 Llama/NLLB 版本；全文未报告 temperature、top-p、seed、重复采样次数或方差。 | 未报告采样超参、随机种子或重复运行，所有分数为单次点估计。 |
| J9 | 重复与文本退化 | 0 | p.5 p.5 仅说明截断首行以区分翻译与 overgeneration/chat explanations；未报告 decoding strategy、repetition penalty 或退化率。 | 有输出截断与定性观察，但未报告解码策略和重复退化 QC，基本要件未达成。 |
| J10 | 分词效应 | 0.5 | p.6 p.6 Table 2 注明 'prompt tokens counted with NLTK's tokenizer'；跨 kgv/npi/gug 与英/目标语言评测；未报告模型 tokenizer 版本或 token/词数比控制。 | 跨语言实验报告了 NLTK 计数工具和 token 数，但未报告模型分词器 revision，也未在跨语言分析中控制 token 长度差异。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.22 p.22: 'test set examples have been available online from Dictionaria ... since November 2020'，并论证 0-shot 极低使污染相关性降低；未报告训练截止日期或污染率检测。 | 识别并讨论了测试集公开可得的污染风险，但未做正式污染检测或与训练截止日期系统对照。 |
| J12 | 基准饱和 | NA | — | kgv 分数远未接近天花板（0-shot 约 11-12 CHRF++，最佳约 43-46），且使用新/困难 XLR 任务；饱和问题不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；虽有首行格式要求，但没有按约束类型测量指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.5 p.5: 'trimmed responses after the first newline character ... forceful prompt'；p.7 p.7 提到 Llama-I 在 BOOK 设置中 'often fails to output translations on the first line'；未报告格式合法率。 | 有首行输出格式约束和部分失败观察，但未把格式失败与内容错误分开报告，也无格式合法率/重试策略。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/对齐、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 这是纯 NLP/应用任务评测，不主张测量心理学/认知科学构念；讨论中的人类学习类比不构成 LLM 心理学被试范式。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的涌现能力曲线；仅比较少量具体模型。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不对 benchmark/奖励模型/LLM-judge 代理指标做优化；微调是在平行数据上，不是奖励过优化研究。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.6 p.6 Table 2、p.9 p.9 Table 5 仅报告单点分数；p.5 p.5 给出模型版本/名称，但无重复次数、置信区间或配对检验。 | 有模型 snapshot 名称但无重复运行、无 CI、无配对 bootstrap/McNemar，评估可复现性报告不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 翻译、语法判断和 IGT 均为单轮 prompt 任务，无多轮对话历史累积。 |

## 编码小结
研究对数据子集、prompt 类型、模型和评价指标报告较充分，并用回归分析检验 test type coverage 与 prompt token 等混淆；但推断统计、采样随机性、重复运行/置信区间、prompt 敏感性、候选位置控制、污染检测与项目随机效应报告不足。多数人类被试设计组件不适用。
