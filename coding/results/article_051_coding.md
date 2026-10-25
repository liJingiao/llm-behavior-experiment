# article_051 | Comparing Inferential Strategies of Humans and Large Language Models in Deductive Reasoning | 2024

研究类型概述：LLM 行为基准/观察性比较研究：5 个开源 LLM 在 12 道命题逻辑题上以 zero-shot chain-of-thought 生成推理，重复 5 个随机 seed，共 300 条响应；两名标注者人工标注推理策略、推理 soundness 与最终答案正确性。人类数据来自 Van der Henst et al. (2002) 的文献对照，没有新招募人类被试。
- **研究构念（Construct）**：演绎推理策略与推理过程效度（deductive inferential strategies and reasoning-process validity）｜CA 构念锚定：演绎推理（deductive reasoning, `trm_4a3fd79d0a072`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：LLM 行为基准/观察性比较研究：5 个开源 LLM 在 12 道命题逻辑题上以 zero-shot chain-of-thought 生成推理，重复 5 个随机 seed，共 300 条响应；两名标注者人工标注推理策略、推理 soundness 与最终答案正确性。人类数据来自 Van der Henst et al. (2002) 的文献对照，没有新招募人类被试。｜CA 任务锚定：演绎推理任务（deductive reasoning task, `trm_4c898b8c2d071`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_4: 'we assess a total of five models... Llama 2 with model sizes of 7B, 13B, and 70B, ... Mistral-7B ... and Zephyr-7B'; PDF_PAGE_5: 'We prompt each model...' | 自变量可辨认为模型类型/规模/对齐（5 个模型水平，名称与权重来源有报告，单位按模型独立运行），但没有操纵检验，操纵程序本质上是选择既有权重而非主动创设条件；故基本要件达成但报告不完整。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_5: 'manually evaluate... for strategies employed... and the logical validity... record whether the final answer is correct... Cohen’s Kappa value of κ=0.98'; Table 1 on PDF_PAGE_6 reports strategy percentages, correct answer and sound reasoning. | 因变量指标与计分方式明确（策略频率、sound reasoning、correct answer 百分比；人工标注），并报告标注者间信度；但缺少效度证据、连续指标预处理/剔除标准以及天花板地板效应说明。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_4: 'framed the problems around... colored marbles... colors assigned randomly'; PDF_PAGE_5: 'refrain from providing few-shot examples... zero-shot chain-of-thought... nucleus sampling... top-p=0.9, temperature T=0.6... 5 random seeds'; PDF_PAGE_9 limitations discuss fixed task setup. | 报告了若干保持恒定的条件（固定题集、中性内容、同一 prompt、zero-shot CoT、固定采样参数、5 seeds），但没有系统列出控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_9: 'limited set of problems... fixed framework... constant and neutral content, disregarding potential content-effects... not yet examined... complexity... logical connectives'; PDF_PAGE_6 discusses model family differences. | 识别了内容效应、问题复杂度、模型家族/规模/对齐等潜在混淆，并部分讨论局限；但没有系统控制这些混淆，也没有敏感性分析或残余混淆量级评估。 |
| A5 | 调节变量 | NA | — | 研究没有正式的调节变量模型或交互假设；虽然描述性地比较模型类型/规模/对齐与策略频率，但未做交互检验、中心化或简单斜率分析，故按无调节模型记 NA。 |
| A6 | 中介变量 | NA | — | 研究不包含中介变量、直接/间接效应分解或因果链中介假设，故不适用。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_3 Section 2 gives operational definitions and examples for five strategies; PDF_PAGE_5 describes manual labeling of strategies, soundness and final answer; PDF_PAGE_15 Figure 5 gives full task prompt. | 关键构念有可复现的操作化：策略定义与示例、任务 prompt、人工标注与计分流程、模型版本与数据/代码公开；足以让他者复现。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_4 lists five models and Llama sizes 7B/13B/70B; PDF_PAGE_18 Table 3 gives model properties; no formal regression coding of size/alignment. | 报告了模型条件数、具体标签/名称以及部分水平类型（家族名义、规模有序/连续、对齐名义），但缺水平间距、全距及连续变量入模时的中心化/标准化说明。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_9: 'Our study is constrained by a limited set of problems, designed within a fixed framework... constant and neutral content... not yet examined factors such as complexity...'; multiple outcome indicators include five strategies, correct answer and soundness. | 关键构念采用多种策略指标及两个结果指标；同时 Limitation 明确讨论了固定题集/中性内容对推广边界的限制，满足单一操作化风险讨论要求。 |
| A10 | 单一方法的风险 | NA | — | 不是自陈式多构念问卷研究；自变量为模型/权重，因变量为模型文本的人工编码，不存在问卷式共同方法偏差的同源测量问题，故不适用。 |
| B1 | 被试间设计 | NA | PDF_PAGE_4: 'we assess a total of five models...' | 纯 LLM 基准研究，无人类被试分配；模型是研究者选择的固定条件而非随机分配到条件，故 B1 不适用（模型间独立性与重复结构在 G1 讨论）。 |
| B2 | 被试内设计 | NA | PDF_PAGE_5: 'ask each model to solve the set of propositional problems across 5 random seeds, resulting in a total of 60 responses per model' | 同一模型完成 12 题×5 seeds 属于重复观测，但不是人类被试内实验条件设计，也无条件顺序平衡方案；按无被试内条件设计记 NA，重复/嵌套结构在 G1、G2 编码。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素并存的混合实验设计；模型比较是固定模型条件，题/seed 重复不是实验混合因素，故不适用。 |
| B4 | 因子设计 | NA | — | 不是多因素全交叉因子实验；模型比较为单组比较，题目/seed 不是交叉实验因子，故无因子设计可编码。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验（无 ANOVA 主效应表），故不适用。 |
| B6 | 交互作用 | NA | — | 没有可检验的交互项或简单主效应分析；模型规模/对齐仅为描述性比较，故不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层分配；模型/题目均非区组变量，故不适用。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计，故不适用。 |
| B9 | 准实验设计 | NA | PDF_PAGE_4: model selection described as assessing five open-access models; no quasi-experimental design label or causal identification strategy. | 这不是人类准实验或因果识别设计；模型选择与比较按观察性基准处理，未采用不等同对照、中断时间序列、RDD 等准实验框架，故不适用。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及人类被试内处理的处理可逆性/迁移对称性论证，故不适用。 |
| C1 | 随机化 | NA | PDF_PAGE_4: five models selected; PDF_PAGE_5: '5 random seeds' repeated. | 没有把被试或试次随机分配到互斥处理条件；5 个随机 seed 是采样重复，不是条件随机化，故 C1 不适用；随机性报告问题在 J8/J19 编码。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，无需顺序平衡方案，故不适用。 |
| C3 | 恒定 | 1 | PDF_PAGE_4-5: fixed 12 problems, neutral colored-marble content, same system/user prompt, zero-shot CoT, top-p=0.9 and T=0.6; PDF_PAGE_9 limitations discuss fixed task/content external-validity limits. | 明确列出了固定题集、内容中性、prompt、zero-shot 策略和采样参数等恒定条件，并在 Limitation 讨论由此带来的外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配变量，故不适用。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型，故不适用。 |
| C6 | 盲法 | 0 | PDF_PAGE_5: manual evaluation 'independently conducted by two hired students'; PDF_PAGE_17 A.2 describes training but no blinding to model identity/condition. | 存在人工评分者这一需要盲法的结构，但全文未报告评分者对模型身份/条件是否施盲、如何施盲或盲法成功检验，故基本要件未达成。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 等顺序平衡层级，故不适用。 |
| D1 | 练习效应 | NA | PDF_PAGE_5: each problem is prompted separately; no practice block or within-session learning design is described. | LLM 每次针对独立问题 prompt 生成，无练习块或上下文内学习设计；练习效应组件不适用。 |
| D2 | 疲劳效应 | NA | PDF_PAGE_5: 12 problems ×5 seeds per model, each response short and independently prompted. | 任务短且为独立调用，无长 session 疲劳风险；疲劳控制不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各问题/seed 独立生成，不存在跨条件药物/学习残留或清洗期问题，故不适用。 |
| D4 | 不对称迁移 | NA | — | 无交叉条件迁移或不对称迁移设计，故不适用。 |
| D5 | 范围效应 | NA | Table 1 on PDF_PAGE_6 uses objective strategy labels, correct answer and soundness proportions. | 因变量为客观分类/正确率，不是主观量表或绝对量值估计，无范围效应问题，故不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF_PAGE_15 Figure 5 lists problems 1–12 in fixed order; PDF_PAGE_5 does not report randomizing problem order or seed order. | 12 道题的呈现顺序按固定题号列出，未报告题序或 seed 顺序的随机化/反平衡，也未讨论顺序效应；虽然每题独立生成降低风险，但结构存在而未控制，记 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同偏差问题，故不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较，故不适用。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在人类需求特征或事后推断研究假设的访谈检查；故不适用。 |
| E5 | 实验者效应 | 0 | PDF_PAGE_17 A.2 reports comprehensive annotator training and independent annotation, but no statement that annotators were blind to model identity/condition or research hypothesis. | 有人工评分者且报告了培训标准化，但没有报告评分者盲法层级或期望控制；基本要件（至少说明谁盲）未达成，记 0。 |
| E6 | 天花板 / 地板效应 | 0.5 | Table 1 on PDF_PAGE_6 and Table 4 on PDF_PAGE_19 report means and standard deviations for strategy percentages, correct answer and sound reasoning; no skewness/endpoint frequencies or pilot calibration. | 报告了主要因变量的均值与标准差，可初步排查端点堆积；但未报告偏度、端点频率或 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | 自变量为模型/权重、因变量为文本标注，不是同源自评多构念测量，故不适用。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_7: 'Pearson correlation coefficient r(298)=0.45 and... p=1.6×10−16'; Table 1 reports means/SD; no CI, power analysis, or multiplicity correction. | 报告了相关系数这一效应量及标准差，并报告主要分析；但缺乏 95%CI、样本量确定依据/功效分析、多重性校正及统计假设说明。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_4 lists five selected models; PDF_PAGE_9 limitations discuss fixed task/content; no random assignment, baseline equivalence test, flow diagram or attrition handling. | 报告了模型选择与配置，并部分讨论内部效度限制；但无随机分配、基线等价、被试/试次流向与损耗处理，内部效度评估不完整。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_5 reports Cohen's κ=0.98 inter-annotator reliability; PDF_PAGE_17 gives per-label kappa; PDF_PAGE_9 notes limited fixed problem set; no manipulation check. | 报告了标注信度及策略定义来源，但缺少效度证据、操纵检验与多操作化会聚证据；单一固定题集局限有讨论但不够系统。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_4 and PDF_PAGE_18 Table 3 describe model sources, sizes, context length and fine-tuning; PDF_PAGE_9 discusses fixed problems, neutral content and unexamined factors; no cross-sample replication. | 报告了模型样本来源与特征，并讨论推广边界；但人类比较来自旧文献且未做跨样本/跨情境复现，外部效度证据有限。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_5: 'a total of 300 responses'; PDF_PAGE_7 uses r(298) on response-level data; Table 1 aggregates by model. | 说明了响应总量，但统计分析在模型响应层做相关时未处理题/seed/模型嵌套，主要表又仅以模型层汇总；存在聚集结构但未用多层模型显式分离，记 0.5。 |
| G2 | 随机效应 | 0 | PDF_PAGE_5 and Table 1/4 report aggregated model-level percentages; no mixed-effects model or random-effect structure is reported. | 统计模型未报告任何随机效应；题/seed 对模型响应构成重复/嵌套结构且结论涉及题目总体，但被当作固定或汇总处理，故未满足基本要件。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_4: '12 problems of propositional logic suggested by Van der Henst et al. (2002)'; PDF_PAGE_9: 'limited set of problems... fixed framework'. | 材料为有限 12 题，作者在 Limitation 承认题集有限，但分析未把题目作为随机因子或做项目层面推广检验；属于部分满足。 |
| G4 | 统计功效 | 0 | PDF_PAGE_5: '5 random seeds... 60 responses per model'; no a priori power analysis or sample-size justification; Table 4 reports SD but no CI. | 没有事前功效分析或样本量/重复次数论证，结果主要报告百分比均值与 SD，缺置信区间；仅事后描述样本量，不能算功效证据。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_5 reports all models, 12 problems and 5 seeds; PDF_PAGE_9 notes no mechanistic analysis; no trial exclusion rules or stopping/追加说明; no confirmatory/exploratory labeling. | 报告了全部条件、主要因变量和固定重复次数，但未报告试次剔除标准与数量、为何选 5 seeds、是否停止/追加，也未区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未出现预注册平台、注册编号、时间戳或分析计划预注册说明。 | 无公开预注册；按既定口径无预注册记 0，而不是 NR。 |
| J1 | 位置偏差 | NA | PDF_PAGE_15 prompt asks for 'Conclusion: True/False'; no candidate options, ranking, or paired LLM-judge comparison. | 任务为二元 True/False 判断，不涉及多候选项位置、排序或裁判成对比较，故位置偏差组件不适用。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放生成质量，也不比较回答长短，故冗长偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈纠错或多轮对话式评估，故谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 作为裁判或成对比较评估模型输出，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | PDF_PAGE_5: 'we refrain from providing few-shot examples... zero-shot chain-of-thought prompting'. | 明确为零样本提示，无 few-shot 示例选择/排列问题，故不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_15 Figure 5 provides the full system/instruction/user prompt template; PDF_PAGE_5 describes zero-shot CoT and model-specific system-message handling, but no prompt-sensitivity ablation or dev/test split. | 公开了完整 prompt 模板和部分版本/格式信息；但没有语义等价措辞的敏感性消融、版本迭代日期或 dev/test 划分说明，故仅部分满足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | PDF_PAGE_18 Table 3 lists context lengths 4K/8K; prompts in Figure 5 are short and contain no long documents or RAG. | 上下文很短且无长文档/RAG 设置，不涉及中间迷失或信息位置效应，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_5: 'nucleus sampling using... top-p = 0.9, temperature T = 0.6... across 5 random seeds'; Table 4 reports SD over seeds. | 报告了主要采样超参与重复次数及 SD；但未报告具体 seed 值、top-k、repetition penalty、最大生成长度，也未给 95%CI，故不完整。 |
| J9 | 重复与文本退化 | 0.5 | PDF_PAGE_5 reports nucleus sampling with top-p=0.9, T=0.6 and constant settings across models; no repetition penalty, n-gram repetition rate or degeneration rate is reported. | 解码策略有报告且各模型比较保持恒定；但缺少 repetition penalty、重复率/退化率 QC 和截断比例，故仅部分满足。 |
| J10 | 分词效应 | NA | PDF_PAGE_15 prompts and problems are in English; no cross-language or cross-script comparison. | 单语言英语任务，无跨语言/跨脚本输入比较，故不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_4: '12 problems... suggested by Van der Henst et al. (2002)'; PDF_PAGE_18 Table 3 gives model details but no training cutoff vs benchmark release comparison or contamination check. | 使用 2002 年公开题集，存在训练语料重叠风险；全文未报告训练截止日期对照、n-gram 重叠或污染率，也未把污染与泛化区分，故记 0。 |
| J12 | 基准饱和 | NA | Table 1 on PDF_PAGE_6: correct answer 40.0–56.7%, sound reasoning 0–31.7%, far below ceiling. | 分数远未接近天花板，饱和风险不存在，故基准饱和组件不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，也没有按约束类型测量指令违反，故不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF_PAGE_15 prompt requires ending with 'Conclusion: True/False'; PDF_PAGE_5 describes manual evaluation, but no format-validity rate, retry policy or post-processing normalization is reported. | 有明确输出格式要求，但未报告格式合法率、解析/重试规则，也未把格式失败与内容错误分开统计，故仅部分满足。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全、越狱或有害请求评估，故不适用。 |
| J16 | LLM 作为被试的范式定位 | 1 | PDF_PAGE_2: 'draw from cognitive science literature... study inferential strategies... first to comprehensively compare... LLMs and humans'; PDF_PAGE_4: 'task setup aligns with the experiment conducted by Van der Henst et al. (2002)'; PDF_PAGE_18 Table 3 gives model/weight details. | 明确把 LLM 上测量的推理策略构念与人类同名构念作理论对照，使用同一组 12 题人类实验材料，报告模型权重来源，并讨论模型类型/规模/对齐作为比较因素而非人类被试样本；未直接外推人类结论。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | PDF_PAGE_6: 'model scale significantly influences the frequency with which strategies are employed... larger models... more readily'; no emergence/phase-transition claim. | 仅描述 7B/13B/70B 的规模趋势，没有宣称涌现或突变，也没有建立规模能力曲线并解释相变，故该风险组件不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及 RL、best-of-N、benchmark 优化或代理奖励优化，故指标博弈/奖励过优化组件不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_5 reports 5 random seeds and Table 4 reports mean±SD; PDF_PAGE_18 gives model names/versions (e.g. Llama-2-chat-hf, Mistral-7B-Instruct-v0.2, zephyr-7b-beta) but no commit hash/API date, no 95%CI and no paired tests. | 报告了重复次数 N=5、均值/SD 和模型版本名称，并公开数据/代码；但缺精确 snapshot/commit、95%CI、配对检验和逐题敏感性分析，故仅部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | PDF_PAGE_5: each problem is posed as an independent prompt; no multi-turn dialogue history. | 严格单轮任务，无对话历史累积，也不主张多轮部署一致性，故不适用。 |

## 编码小结
研究对五种推理策略及新增 symbolic strategy 的操作化较清楚，人工标注信度很高（总体 Cohen's κ=0.98），并提供了 prompt、模型版本和公开数据/代码。但统计推断较有限：主要为描述性百分比与一个未处理嵌套的 response-level 相关分析；缺乏预注册、事前功效分析、模型/题目随机效应、污染检查、格式合法率、种子与快照精确报告。大量人类实验设计组件对本研究的 LLM 分析单位不适用。
