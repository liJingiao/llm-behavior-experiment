# article_170 | Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs | 2025

研究类型概述：这是一项面向 LLM 的基准评测研究：构建 PrefEval 数据集，比较 10 个开源/闭源 LLM 在多轮长上下文对话中推断、记忆并遵循用户偏好的能力；操纵/比较提示方法、上下文长度、偏好表达形式和任务类型，并用 LLM-as-judge 与多项选择分类作为主要评价方式，另含 SFT 与注意力分析。
- **研究构念（Construct）**：用户偏好的推断、长程记忆、主动遵循与冲突处理｜CA 构念锚定：认知控制（cognitive control, `trm_4aae62e4ad209`）；注意（attention, `trm_4a3fd79d09902`）；干扰控制（interference control, `trm_551f11bb8f6a8`）
- **实验任务与范式（Task / Paradigm）**：让十种现成LLM在多轮对话中接收显式、选择隐含或persona隐含偏好，经过不同长度的干扰对话后回答相关请求，并比较零样本和多种推理期干预。（操纵显式/两类隐含偏好、对话距离、单一或冲突偏好、生成与分类任务以及零样本、提醒、自我批评、CoT和RAG。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5 §3.1: 'We investigate methods ... (1) Zero-shot ... (5) Retrieval-Augemented Generation (RAG)'; p.5 'we place the user's preference at the beginning of the conversation and query at the end'. | 提示方法与上下文长度等条件被明确命名并给出多个水平，且方法程序有描述；但分配方式、随机化及操纵检验未报告，因此为 0.5。 |
| A2 | 因变量 | 0.5 | p.4 §2.5: 'four independent evaluators to check the response against four binary metrics'; p.4 'manually checked 200 randomly sampled evaluations, with an observed 5% error rate'; p.44 Table18 报告 human-LLM agreement。 | 因变量指标与计分方式明确，且有部分信度/一致性证据；但缺少连续指标的预处理、端点/天花板地板效应说明，故 0.5。 |
| A3 | 控制变量 | 0.5 | p.5: 'if not explicitly stated otherwise, we place the user's preference at the beginning of the conversation and query at the end'; p.17 Table3 列出模型版本。 | 报告了偏好位置、查询位置、模型版本等部分控制做法，但未系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p.6 footnote: 'GPT-o1-preview may not be a fair comparison ... test-time compute'; p.16 A.1 讨论 data 与 fact-checking 限制。 | 识别了 o-series 测试时计算等潜在不公平比较，并有限度讨论限制；但未系统处理残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量理论模型，也没有乘积项交互检验与简单斜率分析；不同模型/形式/长度的比较是描述性分组，不按调节效应建模。 |
| A6 | 中介变量 | NA | — | 没有中介变量、直接/间接效应分解或因果链假设检验。 |
| A7 | 操作性定义 | 1 | p.3-4 §2.2-2.5 定义 preference-query pair、generation/classification 任务；p.4 Table1 给出 error aggregation；p.17-19 与 p.35-38 给出方法及 evaluator prompts。 | 关键构念被操作化为可重复的对话输入、任务、二元检查与聚合规则，评价 prompt 也公开，达到可复现操作化。 |
| A8 | 水平数与类型 | 0.5 | p.5 §3.1 列出五种方法；p.3 §2.3 三种 preference forms；p.5-6 报告不同 turn/token 长度；p.8 报告多模型。 | 水平数与取值/标签基本明确；但未系统说明各因素的水平类型、间距/全距及连续长度是否中心化。 |
| A9 | 单一操作化的风险 | 1 | p.4 §2.5 同时使用 generation 与 classification；p.7 'correlation coefficient of 0.73'; p.44 Table18 报告 human-LLM agreement。 | 关键构念采用多种操作化/评价方式，并报告了生成与分类的会聚相关及人工核验，满足多种操作化与会聚证据要求。 |
| A10 | 单一方法的风险 | NA | — | 研究不是自陈量表式同源测量；IV 为提示条件，DV 为模型输出/裁判评分，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或被试组分条件；同一批测试项目在多个模型/方法/长度下被评测，不存在被试间分配设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量与条件顺序平衡；LLM 各条件为独立调用，论文未按被试内顺序设计处理。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素混合设计及对应误差项。 |
| B4 | 因子设计 | 0 | p.5-6 Figure4/Figure6 与 p.22-30 Tables 5-13 呈现 model × method × length × topic 的多因素网格。 | 存在多因素交叉的评测结构，但没有完整 ANOVA 设计矩阵、F/df/效应量和正式交互检验；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p.6: 'all methods outperformed the zero-shot baseline'; 但没有报告 F、df、p 或效应量。 | 虽然有描述性主效应比较，但没有报告主效应的统计检验结果；若按因子设计主效应要求，本项未达成。 |
| B6 | 交互作用 | 0 | p.6: 'Self-Critic initially outperformed CoT but fell behind ... reverse was observed for Llama models'; 未给出交互项统计检验。 | 仅凭曲线/模式作交互式解读，未报告交互项 F、df、p、效应量及简单主效应检验，故为 0。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机设计；topic 只是评测维度，不是区组变量。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；模型比较不是非随机分配人类/单位后的因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理序列，故不涉及处理可逆性与迁移对称性。 |
| C1 | 随机化 | NA | — | 测试项目没有被随机分配到互斥条件；各方法/长度是在同一批项目上分别调用评测，不是随机化实验分配。 |
| C2 | 平衡 | NA | — | 没有条件顺序平衡问题；独立 LLM 调用不产生被试内顺序效应。 |
| C3 | 恒定 | 0.5 | p.5: 'we place the user's preference at the beginning ... query at the end'; p.17 Table3 列出固定模型版本。 | 报告了偏好位置、查询位置和模型版本等恒定设置，但未系统列出全部恒定变量并讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配程序。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为协变量或区组纳入统计模型。 |
| C6 | 盲法 | NA | — | 主要数据收集为自动化 LLM 调用；虽有少量人工核验，但不存在对实验条件施盲的人类被试/主试设计。 |
| C7 | 平衡的层级 | NA | — | 没有顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | 没有练习块或跨条件学习；长对话中的 turn 是输入材料而非被试练习阶段。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题；LLM 条件为独立调用，不涉及休息与时间分散。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立提示/调用，无跨条件药物式残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性设计。 |
| D5 | 范围效应 | NA | — | 不使用主观量表式绝对判断，无范围效应/量表锚定问题。 |
| E1 | 位置 / 顺序偏差 | 0 | p.3 分类任务为四选项；p.38 Figure19 的生成模板明确 'Option 1 that aligns with the user's preference'，正文未报告选项顺序随机化或反平衡。 | MCQ 存在候选位置偏差风险，但论文未报告 option order 的随机化/交换重判，故为 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分题与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中间反应倾向问题。 |
| E4 | 需求特征 | NA | — | LLM 自动化评测没有人类被试可推断研究假设的需求特征；未使用人类掩饰情节。 |
| E5 | 实验者效应 | NA | — | 主要数据采集自动化，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.22 Table5 中多种 Reminder 条件接近 100.00；p.6 Figure3 显示大量模型在长上下文下接近 0；论文未报告 SD、偏度或正式端点频率。 | 结果中明显存在天花板/地板现象且报告了均值/图线，但未系统讨论天花板地板效应或任务难度校准，故 0.5。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.2 '3,000 manually curated ... pairs'; p.7 'correlation coefficient of 0.73'; p.22-30 报告 accuracy 表；未报告主要比较的 95%CI、功效分析或多重性校正。 | 报告了数据规模与部分效应指标/相关，但缺少样本量确定依据、置信区间与多重比较校正。 |
| F2 | 内部效度 | 0.5 | p.5 §3.1 列出模型/方法；p.9 §3.7 用 80% topics 训练、20% unseen topics 评测；未报告随机分配、分配隐藏或基线等价性。 | 固定测试集和模型版本提供一定可比性，但不是随机分配实验，内部效度威胁未被系统评估。 |
| F3 | 构念效度 | 0.5 | p.4 'observed 5% error rate'; p.7 generation-classification r=0.73；p.44 Table18 报告 agreement；但无方法操纵检验。 | 有信度/一致性及会聚效度证据，但缺少对提示方法操纵是否成功的 manipulation check，故 0.5。 |
| F4 | 外部效度 | 0.5 | p.3 1000 个 preference-query pairs、20 topics；p.16 A.1 承认 synthetic preference-query pairs 与真实用户偏好之间有限。 | 报告了数据集来源与部分推广边界，但未证明对真实用户总体或跨情境的代表性。 |
| G1 | 分析单位 | 0.5 | p.7: 'each data point ... averaged over 20 topics'; p.19 Figure11 也按 20 topics 聚合。 | 报告了聚合层级，但未用多层/混合模型显式处理 response/query 嵌套于 topic 的结构。 |
| G2 | 随机效应 | NA | — | 统计模型没有随机效应；模型被作为固定评测对象而非从模型总体随机抽样，且无人类被试随机效应需求。 |
| G3 | 材料作为随机效应 | 0 | p.7 'each data point ... averaged over 20 topics'；p.22-30 按 topic 汇总，未报告 item/material random effect。 | 偏好-查询项目是有限材料集合，但分析未把材料/项目作为随机因子，难以把结论显式推广到新材料总体。 |
| G4 | 统计功效 | 0 | p.2 报告 3,000 对数据；全文没有事前功效分析、目标功效、预期效应量来源或主要比较 CI。 | 无统计功效分析或样本量论证，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p.17-18 A.4 与 p.41-42 A.14 描述数据构造、过滤与人工筛选；但未全面报告所有可能的因变量/条件取舍与探索性/验证性区分。 | 报告了部分数据构造与排除/过滤规则，但研究者自由度披露不完整。 |
| G6 | 预先设定 / 预注册 | 0 | p.11 Reproducibility Statement 仅说明将发布数据与 prompts；未提及时间戳早于数据收集的预注册。 | 无预注册，故为 0。 |
| J1 | 位置偏差 | 0 | p.3 分类任务为四选项；p.38 Figure19 指定 option 1 aligns、options 2-4 violate；未报告位置交换、翻转率或位置×正确率曲线。 | LLM 多项选择存在明显候选位置偏差风险，但论文未做位置反平衡或报告位置偏差分析。 |
| J2 | 冗长偏差 | 0 | p.4 使用 Claude 3 Sonnet 作为 LLM-as-a-judge，检查四个二元指标；未报告长度分布与得分相关、长度控制或盲评。 | 生成任务由 LLM 裁判评分，但未识别或控制冗长偏差，故为 0。 |
| J3 | 谄媚 | NA | — | 没有操纵用户先验立场、纠错反馈或 pro-/anti-framing；研究目标是偏好遵循而非谄媚反应偏差。 |
| J4 | 自我偏好 | 0 | p.4 'we apply the LLM-as-a-judge framework using Claude 3 Sonnet'；p.17 Table3 显示 Claude 3 Sonnet 同时是被评测模型之一。 | 裁判模型与被评模型同源，且未报告自我偏好控制、匿名化或多裁判陪审团；虽有少量人工一致性核验，但不足以消除自我偏好风险。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.18 'Few-Shot Chain-of-Thought ... we used 5-shot'，并展示示例；未报告示例来源、各类比例、排列反平衡或多 seed 重采样。 | few-shot 示例数量与部分模板可见，但示例选择、排列与稳定性控制不完整。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.17-19 A.4 给出 Reminder/CoT/RAG prompts；p.35-38 给出 evaluator prompts；未报告 prompt 版本号、敏感性消融或 dev/test 划分。 | 完整模板大体可得，但没有版本化、措辞敏感性检验或测试集调参说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 1 | p.5 上下文长度至 100k tokens；p.42-43 A.16 'inserting the preference in different locations of a fixed 100 turn conversation'，p.43 Figure23 报告 middle 位置下降。 | 实际长上下文长度与关键信息位置（首/中/尾）均被操作化，并报告位置×表现模式；符合核心长上下文位置效应要求。 |
| J8 | 温度与采样随机性 | 0 | p.17 Table3 仅列模型版本；p.3-5 未报告 temperature、top-p、top-k、seed 或重复采样次数及 CI。 | 生成式 LLM 评测未报告采样随机性控制，故为 0。 |
| J9 | 重复与文本退化 | 0 | p.4 生成任务与 p.4-5 评价协议未说明 decoding 策略、repetition penalty、重复率或截断比例。 | 涉及开放生成，但未报告解码策略与重复/退化质量控制，故为 0。 |
| J10 | 分词效应 | NA | — | 数据集与实验为英文、单脚本，没有跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.11 'We plan to release our benchmark'；p.17 Table3 报告部分模型版本/日期；未报告测试集与训练截止日期对照或污染检测。 | 使用新构建 held-out 基准且给出模型版本，但未做 n-gram/DCQ 等污染检查，故 0.5。 |
| J12 | 基准饱和 | 0.5 | p.22 Table5 中 Reminder 多种条件达 99.03/100.00；p.6 也报告 zero-shot 接近 0；未用连续指标或 bootstrap CI 处理饱和。 | 报告了接近天花板/地板的分数与 SOTA 水位，但未系统改用连续指标或做 CI 比较，故 0.5。 |
| J13 | 指令遵循 | NA | — | 研究不把离散指令遵循作为因变量，也没有 IFEval 式可验证约束；偏好遵循不等同于指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.3 分类任务给四个选项并要求选择一个；p.38 Figure19 给出选项生成格式；未报告格式合法率、重试或无效输出处理。 | 存在结构化多项选择输出设置，但格式合法率与失败处理未报告，故 0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱或有害请求鲁棒性评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 这是工程/应用型 LLM 个性化能力基准，不主张测量人类心理学/认知科学构念；不需按心理被试范式定位。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有随模型规模/训练进展宣称涌现或能力突变曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以代理指标为优化目标并监控 overoptimization 的训练/RL/best-of-N 过程；SFT 直接使用任务数据并在 held-out topics 上评测。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.17 Table3 给出较精确模型版本；p.22-30 报告逐模型/方法/长度的点估计 accuracy；未报告重复次数 N、95%CI 或配对检验。 | snapshot/版本较精确，但缺重复采样与置信区间/配对比较，故 0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.6 Figure3 报告不同 turn 长度下 accuracy；p.34 Figure13 报告 error counts across turns；未说明每轮独立/累积评分及上下文截断处理。 | 确实做了多轮/多会话长度评测并展示随轮次变化，但未按每轮独立/累积评分拆分或报告历史截断，因此为 0.5。 |

## 编码小结
论文作为 LLM 个性化偏好遵循基准，任务、数据构造、提示模板和评价指标报告较充分，且用生成/分类两类任务与人工核验做了会聚验证；但它不是人类被试实验，因而大量人类实验设计组件不适用。主要缺口在于：未系统报告条件分配/顺序平衡、候选位置偏差、采样温度与重复次数、置信区间/多重校正、项目随机效应与污染检查等，因此 LLM 评测可复现性与偏差控制只能部分满足。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
