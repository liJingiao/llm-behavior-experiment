# article_122 | ToMATO: Verbalizing the Mental States of Role-Playing LLMs for Benchmarking Theory of Mind | 2025

研究类型概述：该文是 LLM 基准构建与评测研究：用 Llama-3-70B-Instruct 进行带信息不对称的双角色 LLM-LLM 多轮对话生成，构造 ToMATO/ToMATO-FB 多项选择心理理论基准，并在九个 LLM 上评测；同时包含 MTurk/LLM 质量验证、人类基线及信息不对称消融。主要分析单位为生成的对话/问题与模型-题目的评测结果，而不是人类被试的实验分配。
- **研究构念（Construct）**：一级/二级心理理论、错误信念与人格条件下的心智推断｜CA 构念锚定：心理理论（theory of mind, `trm_4a3fd79d0b392`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；冲动性（impulsivity, `trm_50070dce14554`）
- **实验任务与范式（Task / Paradigm）**：仅依据九种现成LLM在ToMATO对话问答上的零样本/提示评估，测试其对信念、意图、欲望、情绪和知识的一级及二级推断。（改变心智状态类别、一级/二级目标、真/错误信念、角色人格及模型。）｜CA 任务锚定：心理理论任务（theory of mind task, `trm_4c8a8467304e2`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: 'we investigated the effect of the invisibility of one’s thoughts and system prompts ... on the frequency probability of false belief generation'; p.6 Table 6 lists System Prompt/Thought checkmark conditions. | 信息不对称消融明确操纵两个二值因素并给出各水平组合，但分配/随机化程序与操纵检验未完整报告，因此为部分满足。 |
| A2 | 因变量 | 0.5 | p.4: each instance includes conversation C, question Q, four options O and ground-truth answer A; p.5 Table 3 reports ToM performance (%) with mean±SD over five runs. | 因变量是多项选择正确率，指标与计分清楚；但无正式信效度证据、连续指标预处理或天花板/地板说明，故仅部分满足。 |
| A3 | 控制变量 | 0.5 | p.4: incorrect options were randomly sampled from the thought set 'because intentionally creating incorrect options can introduce spurious correlations'; p.5: mean±SD over five runs; p.7: lexical-overlap baseline and z-statistics. | 报告了若干控制措施（随机错误选项、LO 基线、五次运行、词级相关控制），但未系统列出全部控制变量及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p.4: random incorrect options address spurious correlations; p.7: z-statistics word-level spurious-correlation analysis; p.6: 'it is unfair to compare Llama models with other LLMs' because benchmark was generated with Llama-3-70B-Instruct. | 识别了词级捷径、词汇重叠和生成模型重叠等潜在混淆并做了部分控制，但没有正式敏感性分析或完整残余混淆量化。 |
| A5 | 调节变量 | NA | — | 文中没有明确的调节假设或乘积项交互检验；按心理状态/人格高低拆分子集属于描述性分组比较，不构成调节模型。 |
| A6 | 中介变量 | NA | — | 没有中介变量假设，也没有直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p.4: equations for role-playing LLM generation and inner-speech prompts; p.3 Table 2 gives exact inner-speech prompt prefixes; p.5: false-belief detection by comparing first- and second-order mental states. | 一级/二级心理状态、五类心理状态、IS prompting、选项构造和计分均有可操作描述，但完整 system prompt、QA 模板与裁判指令未在正文全部给出，复现需依赖外部代码。 |
| A8 | 水平数与类型 | 0.5 | p.2 defines five mental-state categories and first-/second-order states; p.6 Table 5 splits each Big Five factor into high/low; p.1 abstract says 15 personality trait patterns, while p.7 analysis mentions 32 = 2^5 patterns. | 主要分类水平与标签基本明确，但人格模式数量在摘要与方法/分析中不一致，且未系统说明水平类型/间距/全距。 |
| A9 | 单一操作化的风险 | 0.5 | p.7: future work includes extending to multi-modal contexts and multi-agent settings; p.6: notes limitations of constructing benchmarks with LLMs. | ToM 主要依赖一个基准/单一测量范式；虽有多类别、第一/第二级和错误信念子集，但会聚证据有限，只在讨论中简要提及边界，因此部分满足。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是自陈式多构念测量，自变量/因变量不是同一份量表来源；生成模型与评测模型重叠问题属基准污染/生成偏差，按 J11 处理，而非共同方法偏差。 |
| B1 | 被试间设计 | NA | — | 基准评测中九个 LLM 均在相同题目上作答，不存在人类或 LLM 被试按互斥条件随机分配；模型间比较不是被试间分配。 |
| B2 | 被试内设计 | NA | — | 虽然同一模型评测全部题目，但没有把条件顺序作为被试内处理并做顺序平衡；属于固定基准评测，不是重复测量实验设计。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内因素混合的实验设计，也没有相应混合模型或误差项。 |
| B4 | 因子设计 | NA | — | 论文有模型、心理状态类别、第一/第二级等分层展示，但这是基准描述性交叉表，不是带完整设计矩阵和主效应/交互检验的因子实验设计。 |
| B5 | 主效应 | NA | — | 没有因子实验中的主效应统计检验；表 3/5 为按类别汇总的正确率。 |
| B6 | 交互作用 | NA | — | 没有实验交互项检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 没有处理分配意义上的区组随机化；场景类别和人格配对的抽样属于基准构成分层，不是区组设计。 |
| B8 | 拉丁方 | NA | — | 无被试内条件顺序设计，不使用拉丁方。 |
| B9 | 准实验设计 | NA | — | 不是无法随机分配的准实验因果设计；模型间比较没有选择偏差/匹配/DiD 等准实验框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理条件，因此不涉及可逆性和迁移对称性论证。 |
| C1 | 随机化 | NA | — | 随机抽样场景、角色和错误选项是刺激/样本构造，不是实验条件分配；无随机分配方法与分配隐藏机制。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，因此无顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.4: 'We employ Llama-3-70B-Instruct'; 'N is set seven because we found longer conversations tended to be redundant'; p.6 notes limitations of LLM-generated benchmark. | 报告了部分恒定设置（生成模型、轮数等）并简要讨论局限，但未系统列出所有恒定变量及其外部效度限制。 |
| C4 | 匹配 | NA | — | 没有对实验单位做匹配后再分配；每个场景采样五对角色属于基准构造中的平衡/控制，不是匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.6 Table 5 splits questions by high/low Big Five personality traits and reports performance by subset. | 人格因素被测量并按子集分析，但未作为协变量/区组纳入正式模型，也未检验斜率齐性或报告调整后效应量。 |
| C6 | 盲法 | 0 | p.5: 'we instruct three human annotators and GPT-4o mini to judge whether B correctly infers A’s mental state or not'; p.5: MTurk annotators validate quality. | 存在人类评分者/标注者，但全文未报告盲法类型、对谁施盲、实施方式或盲法成功检验。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级需要说明。 |
| D1 | 练习效应 | NA | — | LLM 评测题目为独立 QA 调用；多轮对话是输入材料而非被试跨条件学习序列，因此无练习效应控制问题。 |
| D2 | 疲劳效应 | NA | — | 主分析为 LLM 推理，不存在 session 疲劳；人类 MTurk 标注仅用于质量验证/基线，未作为条件时间序列分析。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个问题/对话输入独立，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或顺序平衡，因此不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为客观多项选择正确率，不是量表式绝对判断，无范围效应校准问题。 |
| E1 | 位置 / 顺序偏差 | 0 | p.4: for each question, correct answer A is the thought and three incorrect options are randomly sampled from other thoughts; no statement of shuffling/randomizing option positions. | 多项选择选项位置未报告随机化或反平衡，也未讨论位置效应；这是明确缺失而非不适用。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类实验被试和掩饰情节；MTurk 标注者是编码者而非接受操纵的实验参与者。 |
| E5 | 实验者效应 | NA | — | 数据采集主要由自动化 LLM 评测完成，无人类主试与实验者期望传递；人类标注者问题归入 C6 盲法评估。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5 Table 3 reports accuracy means and standard deviations for all models and humans; p.5 notes random baseline is 25%. | 报告了均值和 SD，但未报告偏度、端点频率或预实验难度校准，不能充分排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；因变量为客观正确率。生成-评测重叠风险在 J11 中处理。 |
| F1 | 统计结论效度 | 0 | p.5 Table 3 reports only mean±SD over five runs; no confidence intervals, formal effect sizes, power analysis, or multiple-comparison correction. | 没有达到报告效应量/CI、样本量依据和多重性校正的基本要求；比较主要依赖描述性均值。 |
| F2 | 内部效度 | 0.5 | p.6 acknowledges Llama benchmark generator overlap as 'unfair' comparison; p.7 reports lexical-overlap baseline and z-statistics to assess shortcut confounds; p.5 reports MTurk validation. | 没有随机分配/分配隐藏或被试流向，但识别并部分控制了若干内部效度威胁，故为部分满足。 |
| F3 | 构念效度 | 0.5 | p.5 describes MTurk and GPT-4o mini validation of conversations/options; p.6 Table 6 reports information-asymmetry ablation; p.7 reports z-statistics on spurious word correlations. | 有较强的构念效度与质量验证证据，但缺正式信度/评分者间一致性统计，且单一基准的操作化局限未充分展开。 |
| F4 | 外部效度 | 0.5 | p.4 samples 160 scenarios uniformly from eight SOTOPIA categories and five role pairs per scenario; p.5 evaluates nine specified LLMs and MTurk human baseline; p.7 discusses future multi-modal/multi-agent extension. | 报告了样本/模型来源和部分推广边界，但未报告标注者代表性、跨情境复现或完整外部效度边界。 |
| G1 | 分析单位 | 0.5 | p.5 Table 4 reports 753 conversations and 5.4k questions; p.5 Table 3 reports scores averaged over five runs; no multilevel/cluster model is reported. | 说明了数据层级（对话/问题）与统计汇总层级，但没有处理问题嵌套于对话、运行嵌套于模型的聚集结构。 |
| G2 | 随机效应 | 0 | p.5 Table 3: 'mean±standard deviations over five runs' but no mixed-effects model, random-effect structure, or fixed/random factor specification. | 统计上未说明任何随机效应；虽然重复运行，但仅做均值/SD 汇总，未把运行/项目/对话等来源方差显式建模。 |
| G3 | 材料作为随机效应 | 0 | p.5 Table 4 treats 753 conversations/5.4k questions as the benchmark material set; p.5 reports aggregated accuracy only; no item random effect or quasi-F. | 没有把材料/问题作为从更大总体抽样的随机因子纳入分析，结论仍基于固定测试集，存在项目推广不足。 |
| G4 | 统计功效 | 0 | No power analysis or a priori sample-size justification is reported; p.5 only states performance mean±SD over five runs. | 无设计阶段功效分析、预期效应量或样本量推导；五次运行也不是统计功效论证。 |
| G5 | 研究者自由度 | 0.5 | p.5: conversations flagged by majority (5.8%) excluded; invalid instances removed; ToMATO final 5.4k questions; all main tables report model/category results. | 报告了部分排除规则与主要结果，但缺少完整剔除数量、所有探索/验证分析区分及样本量决定方式。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or pre-specified analysis plan is reported. | 无公开预注册；也未将验证性与探索性分析明确区分，故记 0 而非 NA。 |
| J1 | 位置偏差 | 0 | p.4 describes creating options as correct answer A plus three randomly sampled incorrect options, but does not report option-position shuffling, A/B swapping, or position-wise accuracy. | 多项选择任务存在选项位置偏差风险，但未做任何位置反平衡/随机化或报告位置偏差结果。 |
| J2 | 冗长偏差 | 0.5 | p.4 notes manually written incorrect options tend to be shorter and therefore randomly samples incorrect options to reduce spurious correlations; p.5 uses GPT-4o mini as a judge/validator. | 识别了选项长度/捷径问题并做了部分控制，但未报告 LLM 裁判的长度-得分相关、盲评长度对照或裁判温度等。 |
| J3 | 谄媚 | NA | — | 任务为客观多项选择/标签判断，无用户先验立场、反馈或纠错对话中的谄媚操纵。 |
| J4 | 自我偏好 | 0.5 | p.5: three human annotators and GPT-4o mini judge false beliefs; GPT-4o mini is also among the evaluated LLMs; both annotators and GPT must agree for inclusion. | 存在被评模型与裁判/标注模型同源风险，但论文使用人类多数作为共同标准，未量化自我偏好、未报告各裁判单独结果或匿名化。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 未报告使用 few-shot in-context examples；Inner Speech 是零样本提示，不是少样本示例集。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.3 Table 2 gives exact inner-speech prompt prefixes; p.4 describes system prompt components; p.1 provides a code/data repository link. | 提供了部分提示模板/版本线索，但正文未给出完整 system prompt，未做语义等价提示敏感性消融，也未说明 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | p.4: conversations use short utterances and N=7 turns; Table 4 average tokens per utterance 41.6. | 上下文远非长文档/RAG 设置，不涉及长上下文中间信息位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | p.5 Table 3 reports mean±standard deviations over five runs; no temperature, top-p, seed, or exact API snapshot is reported. | 有重复运行并估计了运行间变异，但缺少采样超参、种子与置信区间，采样随机性控制不完整。 |
| J9 | 重复与文本退化 | 0 | p.4 describes multi-turn LLM generation and sets N=7 because longer conversations were redundant, but no decoding strategy, repetition penalty, repetition rate, or truncation rate is reported. | 涉及开放生成但未说明/控制解码策略与重复退化，无法把生成质量差异与解码设置区分开。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本输入，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.3 discusses test-set contamination of popular existing tests; p.6 notes Llama-3.1-70B comparison is 'unfair' because ToMATO was generated with Llama-3-70B-Instruct. | 识别到生成模型重叠和污染风险，但没有报告训练截止日期对照、n-gram/DCQ 污染检测或污染率。 |
| J12 | 基准饱和 | NA | p.5 Table 3: human 87.3%, GPT-4o mini 73.5%; p.5 random baseline 25%; p.7 claims benchmark remains challenging. | 该新基准分数未接近天花板，研究也不在饱和基准上宣称微小提升；饱和风险不实际存在。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，未设置可验证约束指令集。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.4: IS prompting specifies output prefix '({thought}) “{utterance}”' and uses regular expressions to delete thoughts. | 报告了格式约束与后处理方式，但未报告格式合法率、重试策略，也未将格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/对齐、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 states the goal is to test 'whether large language models (LLMs) possess human-like ToM'; p.2 defines ToM from human psychology; p.5 includes an MTurk human baseline; p.5 lists model versions. | 明确把 LLM 的 ToM 与人类 ToM 联系并做同范式人类基线，但未系统论证 LLM 构念与人类同名构念的异同，也未给精确 snapshot。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨规模/训练进展的涌现或能力曲线宣称；只是比较若干具体模型。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究为基准构建与评测，不对代理指标做训练/RL/best-of-N 优化，不涉及奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 Table 3 reports mean±SD over five runs; p.5 names model families; p.1 provides code/data repository link. | 报告了重复次数与模型版本，但缺 95% CI、配对检验、精确 API snapshot/commit hash 和逐题敏感性分析。 |
| J20 | 多轮对话中的一致性衰减 | NA | p.4 formulates ToMATO as multiple-choice QA over conversations, with each instance C/Q/O/A; evaluation is per-question, not a multi-turn model interaction with cumulative scoring. | 多轮对话是输入材料，不是让被测模型在多轮对话中逐步作答并评估一致性衰减。 |

## 编码小结
论文对 ToM 构念和基准构造过程说明较充分，提供多类心理状态、一级/二级与错误信念子集，并报告多次运行均值和标准差，还用人类基线、MTurk 验证、词级虚假相关分析和信息不对称消融增强效度。但作为基准论文，仍缺少多项选择选项位置随机化/反平衡、采样超参与精确 snapshot、统计不确定性与配对检验、预注册与功效分析、随机效应/项目推广建模等；LLM 裁判与基准生成模型重叠风险也未系统量化。多数人类实验特有的分配、顺序、盲法与需求特征组件不适用。
