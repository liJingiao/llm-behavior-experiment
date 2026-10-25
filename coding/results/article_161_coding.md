# article_161 | Unnatural Languages Are Not Bugs but Features for LLMs | 2025

研究类型概述：这是一项以 LLM 为对象的实证研究：先提出基于梯度的 unnatural language 搜索方法，再在 SynContextQA、SimGSM8K 上比较自然语境、Shuf-InJ 与 unnatural 语境的跨模型/跨任务表现，随后用 LIMA/GSM8K 做 instruction tuning 条件比较，并结合 token importance、embedding inverse similarity、dependency probing 分析模型处理机制。主要分析单位为“模型×数据集/基准×条件/训练变体”，另有 token 级机制分析；无人类被试。
- **研究构念（Construct）**：非自然语言输入中的语义保持、噪声过滤、关键词重排与上下文依赖理解｜CA 构念锚定：认知控制（cognitive control, `trm_4aae62e4ad209`）；注意（attention, `trm_4a3fd79d09902`）；干扰控制（interference control, `trm_551f11bb8f6a8`）
- **实验任务与范式（Task / Paradigm）**：仅依据无需训练的推理单元：把自然上下文转换为保持语义的非自然字符串，让多种现成LLM在SynContextQA和SimGSM8K回答自然语言问题，并分析token重要性和中间表征。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_4: Table 2 labels 'Natural / Shuf-InJ / Unnatural'; PDF_PAGE_3: Algorithm 1 and Eq.(2) describe how unnatural strings are searched; PDF_PAGE_5: training variants Natural/Random/Empty/Unnatural. | 核心自变量（上下文类型、训练集类型、ICL n 等）被命名并给出至少两个水平及创设程序，但未系统报告单位如何分配到水平、随机化/顺序控制或完整操纵检验；语义回译验证只覆盖 unnatural 字符串。基本要件达成，完整性不足。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_4: 'For SynContextQA, we evaluate performance using exact keyword matching, while for SimGSM8K, we use accuracy'; PDF_PAGE_5: 'winrate ... LC AlpacaEval 2.0'. | 因变量指标与计分方式有明确界定（exact match/accuracy/winrate），但未报告信度、效度、连续指标预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_4: 'All answers were generated under zero-shot setting without sampling'; PDF_PAGE_5: 'all models are fine-tuned for 10 epochs using identical hyperparameters'; PDF_PAGE_2: simple questions chosen. | 报告了 zero-shot、无采样、相同训练超参数、简化问题等控制，但未系统列出控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_4: 'LLMs may answer questions based on pre-trained knowledge rather than the provided context' and synthetic non-existing entities are used; PDF_PAGE_4: SimGSM8K prevents 'simply extract keywords'; PDF_PAGE_11: limitation that searched strings inevitably contain original tokens. | 识别并部分控制了常识记忆、关键词抽取等潜在混淆，并设置了 Shuf-InJ/合成实体对照；但未报告残余混淆的敏感性分析或系统内部效度评估。 |
| A5 | 调节变量 | NA | — | 研究没有明确的调节变量理论模型，也未做乘积项交互检验或简单斜率分析；跨模型/跨数据集比较是描述性分组，不构成本编码意义上的调节分析。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量假设，也没有直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_3: Eq.(1)-(3) and sample-and-selection search; PDF_PAGE_11: Algorithm 1 pseudocode; PDF_PAGE_4: exact keyword matching and accuracy; PDF_PAGE_7: token removal importance Eq.(4). | unnatural language、语义等价搜索、理解性指标和 token importance 机制指标均给出了可复现的操作化程序。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_4: Table 2 conditions 'Natural / Shuf-InJ / Unnatural'; PDF_PAGE_5: Table 3 'ICL(n=1) / ICL(n=8)'; PDF_PAGE_6: Table 4 Natural/Random/Empty/Unnatural. | 报告了主要条件水平与标签，但未系统说明水平类型（名义/等级）、间距/全距及连续变量中心化等。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_2: SynContextQA and SimGSM8K; PDF_PAGE_5: LIMA instruction-tuning plus AlpacaEval; PDF_PAGE_6: MixEval; PDF_PAGE_7-8: token importance and embedding analyses; PDF_PAGE_11: limitations on generalizability. | 关键构念采用多个任务、多个模型、多个基准和多种机制指标进行三角验证，并在局限部分讨论了推广限制与失败情形。 |
| A10 | 单一方法的风险 | NA | — | 研究不是自陈式多构念测量；IV 为输入/训练条件，DV 为模型输出正确率或基准分数，不构成传统共同方法偏差检验的适用场景。 |
| B1 | 被试间设计 | NA | — | 无人类被试，也没有把独立被试组分配到不同条件的被试间设计；模型/测试项在不同条件下被比较，不是被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试接受全部条件的重复测量顺序设计；LLM 每次评估为独立 prompt/调用，未构成需要顺序平衡的被试内设计。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素混合的人类实验设计，也没有相应混合模型误差项。 |
| B4 | 因子设计 | NA | — | 虽然表格呈现模型×数据集×条件组合，但没有作为传统因子设计报告设计矩阵并做 ANOVA 交互检验；按规则不把描述性网格当作因子实验。 |
| B5 | 主效应 | NA | — | 没有因子设计下的主效应统计检验（F、df、p、效应量）。 |
| B6 | 交互作用 | NA | — | 没有报告交互项统计检验、简单主效应或带误差棒的交互图。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量及区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 没有被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；无随机分配问题下的准实验类型、选择偏差与因果推断限定框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理可逆性/迁移对称性设计问题；LLM 主评估为独立 prompt。 |
| C1 | 随机化 | NA | — | 研究没有把分析单位随机分配到互斥处理组；条件是对同一基准/模型设置的系统评估，未报告随机分配机制。 |
| C2 | 平衡 | NA | — | 没有条件顺序需要平衡；主评估不是有顺序的重复测量被试内设计。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_4: 'zero-shot setting without sampling'; PDF_PAGE_5: 'identical hyperparameters'; PDF_PAGE_4: fixed model list. | 报告了 zero-shot、无采样和相同训练超参数等恒定设置，但未完整列出所有恒定变量（如精确 API 版本、温度、最大长度）及其外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配/配对分配方法。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型，也未报告协变量分析；该研究不是以协变量调整为核心的设计。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，没有人类被试或人类评分者盲法问题。 |
| C7 | 平衡的层级 | NA | — | 没有人类被试内顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | 主评估为独立 prompt/测试项，不存在跨试次的练习效应或需要练习块/截除的控制。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题；LLM 调用不涉及时长与休息间隔。 |
| D3 | 延滞 / 迁移效应 | NA | — | 主条件下每个评估 prompt 独立，不存在跨条件清洗期或迁移污染；两轮对话在同一测试项内部，不是跨条件残留。 |
| D4 | 不对称迁移 | NA | — | 无被试内顺序设计，故无不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为 exact match/accuracy/winrate 等客观判定，不使用主观量表，无范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 核心 unnatural language 任务为开放式上下文问答，不是选项/刺激顺序操纵；MixEval 中的多项选择子集按现成基准评估，未作为顺序偏差实验处理。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征和事后访谈推断研究假设的问题。 |
| E5 | 实验者效应 | NA | — | 数据采集与评分由自动流程/API 完成，无人类主试或评分者的实验者效应。 |
| E6 | 天花板 / 地板效应 | 0 | PDF_PAGE_4: natural condition accuracies include 0.99, 0.98, 1.00 in Table 2; PDF_PAGE_4: 'most models on natural questions is over 80%, indicating the simplicity of questions'; no SD/skew/endpoint frequencies reported. | 报告了准确率均值且自然条件下明显接近上限，但没有报告分布、端点频率或系统讨论天花板效应对区分度的影响；存在明显端点堆积而未充分讨论。 |
| E7 | 共同方法偏差 | NA | — | IV 为输入/训练条件，DV 为模型输出或基准指标，不是同源自陈式多构念测量，不适用共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_4: Table 2 reports accuracies; PDF_PAGE_5: winrates; PDF_PAGE_6: MixEval scores. | 报告了准确率/winrate 等点估计与比较差异，但无置信区间、正式效应量、统计检验、样本量确定依据或多重性校正；统计结论效度报告不完整。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_5: 'all models are fine-tuned for 10 epochs using identical hyperparameters'; PDF_PAGE_5: Natural/Random/Empty baselines; PDF_PAGE_6: models compared. | 通过同一基础模型、相同超参数和基线条件部分控制内部效度，但未报告随机种子、训练运行方差、分配隐藏或系统内部效度威胁分析。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_12: Table A7 translation verification EM/F1/NLI; PDF_PAGE_7: token importance analysis; PDF_PAGE_8: embedding/keyword reordering analysis. | 有语义回译验证和多种机制证据支持构念效度，但缺少测量信度指标、人类不可读性操纵检验及系统性操纵检查。 |
| F4 | 外部效度 | 1 | PDF_PAGE_4: diverse open-source and commercial models listed; PDF_PAGE_4-6: SynContextQA, SimGSM8K, LIMA, AlpacaEval, MixEval; PDF_PAGE_11: limitations discuss not always generalizable across tasks and search constraints. | 报告了模型与任务来源的多样性，在多个模型/任务上复现主要现象，并讨论推广边界与失败案例。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_4: accuracy aggregated over datasets; PDF_PAGE_5: winrate over benchmarks; PDF_PAGE_7-8: token-level analyses. | 说明了模型/数据集/条件的分析层级，但未系统讨论测试项嵌套于数据集、模型两两比较的聚集结构，也未使用多层模型处理聚类方差。 |
| G2 | 随机效应 | 0 | PDF_PAGE_4: models treated as separate rows/comparisons; PDF_PAGE_5: benchmark comparisons; no mixed-effects or random-effects specification. | 研究声称跨模型泛化，但模型被当作固定比较对象，未说明随机效应结构或可推广总体；推断的可推广性受限。 |
| G3 | 材料作为随机效应 | 0 | PDF_PAGE_4: 100 SynContextQA/SimGSM8K questions; PDF_PAGE_5: LIMA 1000 instructions; no item-level random effects or mixed models. | 材料/题目被视为固定集合，未将题项作为随机抽样总体建模，存在语言/材料固定效应问题。 |
| G4 | 统计功效 | 0 | p.1–16 全文实验设计与结果部分均未报告事前功效分析、目标功效或样本量/重复次数推导依据 | 没有事前功效分析、目标效应量、重复次数推导或结果置信区间；仅报告单次评估点估计。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_6: 'we remove the results of subset GPQA, MBPP, WinoGrande, and HumanEval since the subsets were too small'; many conditions reported in Tables 2-6. | 报告了部分排除规则和多个因变量/条件，但未完整说明样本量决定方式、是否有中途停止/追加、以及验证性与探索性分析的区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–16 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文没有预注册平台、编号、分析计划或验证性/探索性分析区分；按校准规则记 0，而不是 NR。 |
| J1 | 位置偏差 | 0 | PDF_PAGE_5: 'using the official pipeline and the annotation model is GPT-4o'; no A/B swap, position randomization, or flip-rate reporting. | 使用 AlpacaEval 的 LLM 裁判/成对比较，但未报告候选项位置反平衡、交换前后翻转率或位置×正确率曲线；位置偏差风险未识别。 |
| J2 | 冗长偏差 | 0.5 | PDF_PAGE_2: 'Length-controlled (LC) AlpacaEval 2.0'; PDF_PAGE_5: 'LC AlpacaEval 2.0'. | 使用 length-controlled AlpacaEval 对长度偏差有一定控制，但未报告被评回答长度分布与得分相关、裁判 prompt/rubric 或人类评分对照。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场、反馈或纠错框架操纵，不涉及谄媚/附和风险。 |
| J4 | 自我偏好 | 0.5 | PDF_PAGE_5: annotation model is GPT-4o; evaluated models include Llama-3 and Gemma-2 in Figure 2/Table 4. | 报告了裁判模型和被评模型来源，裁判与被评模型非同家族；但未报告匿名化、独立裁判团、各裁判单独结果或与人类金标准一致性。 |
| J5 | 少样本示例选择与排列偏差 | 0 | PDF_PAGE_5: Table 3 'ICL(n=1)' and 'ICL(n=8)'; PDF_PAGE_5: examples in natural language to ensure output formatting. | 使用了 few-shot ICL，但未报告示例来源、标签比例、顺序反平衡、多 seed 重采样或完整模板；仅报告单次模板下结果。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | PDF_PAGE_3: task prompt denoted t; PDF_PAGE_12: only SynContextQA generation prompt provided; no full evaluation prompt/version/sensitivity. | 未提供完整评估 prompt 模板、版本号、语义等价措辞消融或 dev/test 划分；prompt 敏感性控制缺失。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短（SynContextQA 约不超过 40 字符；SimGSM8K 为简单短题），无长上下文/RAG 设置，不涉及中间迷失。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_4: 'All answers were generated under zero-shot setting without sampling'; no temperature/seed/repeated-run CI reported. | 说明无采样评估，但未报告温度、top-p/top-k、seed、API snapshot、重复次数与方差/置信区间；非确定性未被统计建模。 |
| J9 | 重复与文本退化 | 0.5 | PDF_PAGE_4: 'without sampling'; PDF_PAGE_5: GPT-4o annotation pipeline; no repetition penalty/degeneration rate. | 报告了无采样解码策略，但未报告 repetition penalty、n-gram 重复率/退化率、生成长度截断或跨条件解码一致性检查。 |
| J10 | 分词效应 | 0 | PDF_PAGE_3: 'tokenized sequences of x have varying lengths across optimization iterations due to different models employing distinct tokenizers'; no tokenizer names/versions or token-count control in evaluation. | 研究跨模型比较自然与 unnatural 字符串，且方法明确依赖不同 tokenizer，但未报告 tokenizer 版本、token/词数比或在分析中控制 token 数；存在分词/长度混淆风险。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_4: SimGSM8K derived from GSM8K test set; PDF_PAGE_5: LIMA, AlpacaEval; no training-cutoff or contamination check reported. | 使用公开基准和已知数据集，却未报告测试集版本与模型训练截止日期对照、n-gram/DCQ 污染检测或 held-out 私有集。 |
| J12 | 基准饱和 | 0 | PDF_PAGE_4: Table 2 natural scores 0.99/0.98/1.00; 'most models on natural questions is over 80%, indicating the simplicity of questions'; no saturation analysis or CI-based comparison. | 自然条件下已接近天花板，但未识别饱和问题、未改用连续指标/更难子集，也未用 bootstrap CI 比较差异。 |
| J13 | 指令遵循 | 0 | PDF_PAGE_5: instruction-following ability evaluated through AlpacaEval winrate with GPT-4o judge; PDF_PAGE_6: MixEval scores. | 论文声称 instruction-following 能力，但主要依赖 LLM 裁判/基准胜率，没有可机器判定的指令约束集或按约束类型拆分准确率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 实验不要求结构化/JSON/文法约束输出，无格式合法率与内容错误分离问题。 |
| J15 | 越狱稳健性 | NA | — | 研究不是安全性/越狱稳健性评估，没有有害请求集或对抗攻击成功率测量。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文是 ML/NLP 工程与机制分析，不把 LLM 作为心理学/认知科学被试来测量人类同名心理构念；不适用 J16 的心理学范式定位要求。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有随模型规模/训练进展绘制能力曲线，也不宣称涌现/突变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不把 benchmark/奖励模型/LLM-judge 作为优化目标进行 RL 或 best-of-N 优化；unnatural 搜索优化的是重构概率，不是评估代理指标。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | PDF_PAGE_4: model names such as 'GPT-3.5-turbo' and 'GPT-4o'; PDF_PAGE_5: GPT-4o annotation; no repeat N, CI, exact snapshot, or paired tests. | 只报告单点基准分数，未报告重复次数、置信区间、精确 API snapshot/版本字符串或配对检验；评估可复现性报告不足。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF_PAGE_13: 'each QA session consists of two turn'; Table A9 reports two-turn dialogue results. | 确实做了两轮对话评估，但仅报告最终回答准确率，未按轮次独立/累积评分，也未报告上下文截断或跨轮一致性衰减。 |

## 编码小结
论文对 abnormal/unnatural 输入的语义保持、跨模型迁移、噪声过滤与关键词重排提供了较多实证结果，核心操纵与测量程序较清楚；但统计推断、采样重复、置信区间、预注册、随机化/顺序控制、基准污染与饱和等可复现性和有效性报告明显不足。许多人类被试专属设计组件在本研究中不适用；LLM 评估相关组件多数只能部分满足或缺失。整体上结论有价值，但方法学报告不足以支持很强的泛化与可复现性声明。
