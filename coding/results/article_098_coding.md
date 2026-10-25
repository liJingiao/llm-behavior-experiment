# article_098 | Gender Inclusivity Fairness Index (GIFI): A Multilevel Framework for Evaluating Gender Diversity in Large Language Models | 2025

研究类型概述：纯 LLM 基准/评估框架研究：提出 GIFI，对 22 个 LLM 在 7 个性别公平维度（GDR、SN、NTS、CF、SA、OF、PE）上评估，涉及 11 类代词/性别标识条件与多组自建或改造数据集；研究单位是模型—指标—提示/输出，模型间比较为观察性基准比较，无人类被试随机分配。
- **研究构念（Construct）**：性别包容性、非二元身份识别、刻板印象与群体公平｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：纯 LLM 基准/评估框架研究：提出 GIFI，对 22 个 LLM 在 7 个性别公平维度（GDR、SN、NTS、CF、SA、OF、PE）上评估，涉及 11 类代词/性别标识条件与多组自建或改造数据集；研究单位是模型—指标—提示/输出，模型间比较为观察性基准比较，无人类被试随机分配。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3 Table 1 lists binary, neutral, and neopronoun groups; p.4 Section 3.2 says prompt templates are varied across G pronoun groups; p.5 Section 4 constructs 11 variants per prompt. | 自变量可界定为性别代词/性别标识条件（11 个 pronoun groups），水平与替换程序明确；但未报告操纵检验，分配方式主要是每个 prompt 生成 11 个变体并让所有模型评估，故为部分完整。 |
| A2 | 因变量 | 0.5 | p.3–5 define GDR, SN, NTS, CF, SA, OF, PE with formulas and scoring; p.31 Table E.6 reports metric values. | 因变量指标与计分方式明确，但未报告传统信度/效度证据，也未系统说明连续指标的预处理、天花板/地板控制；部分稳健性见附录 C 但不构成完整测量信效度报告。 |
| A3 | 控制变量 | 0.5 | p.6: “maximum token length of 200, decoding hyperparameters set to temperature of 0.95, and nucleus sampling with top-p of 0.95”; p.19–20 data-cleaning rules; p.23 model deployment details. | 报告了固定解码参数、数据清洗规则和统一评测协议等控制手段，但未以清单方式系统列出所有控制变量及其控制方式。 |
| A4 | 混淆变量 | 0.5 | p.10 Limitations discusses data contamination and model training-data opacity; p.25 Appendix C discusses classifier bias and VADER ablation. | 识别了训练数据污染、外部分类器偏差等潜在混淆，并用同协议相对比较和 VADER 消融作部分缓解；但未系统量化残余混淆或做完整敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量假设或交互检验设计，故不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | p.3–5 give exact metric formulas and pronoun-group definitions; p.19–20 detail data construction and templates; p.23 gives model setup and identifiers. | 关键构念（性别包容性/公平）被操作化为七项可计算指标，代词替换与数据构建步骤足够具体，可据以复现。 |
| A8 | 水平数与类型 | 1 | p.3 Table 1 lists 11 pronoun groups with labels and binary/neutral/neo types; p.4 states G=11 groups. | 水平数、各水平标签与水平类型明确；代词组为分类变量，水平间距/全距与中心化不适用。 |
| A9 | 单一操作化的风险 | 0.5 | p.3–5 define seven metrics; p.31 Table E.6 reports each metric separately and aggregate GIFI. | 关键构念采用多指标操作化，但未报告各指标间会聚效度、相关矩阵或单一/多重操作化局限的系统讨论。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈问卷的同源测量；自变量为提示/代词替换，因变量为模型输出自动评分，不适用传统共同方法偏差检验。 |
| B1 | 被试间设计 | NA | — | 纯 LLM 基准评测，无人类被试或模型被随机分配到互斥条件；模型间比较不是被试间实验。 |
| B2 | 被试内设计 | NA | — | 虽然每个模型接受多个代词条件，但提示/生成相互独立，无需要平衡顺序的人类被试内设计；论文未报告重复测量顺序设计。 |
| B3 | 混合设计 | NA | — | 无明确的组间/组内混合实验设计，也无对应混合模型与误差项。 |
| B4 | 因子设计 | NA | — | 不是因子实验设计；模型、代词组、任务不是作为完全交叉实验因素并检验交互。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验、简单主效应或误差棒图示。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；研究为观察性模型基准比较，且未作准实验因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内设计，不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无人类被试或分析单位被随机分配到条件；所有模型按同一协议评估，无分配隐藏问题。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件呈现顺序；提示/条件生成相互独立。 |
| C3 | 恒定 | 0.5 | p.6 fixes max token 200, temperature 0.95, top-p 0.95; p.23 reports model identifiers and deployment; p.10 discusses language/model coverage limits. | 报告了部分恒定变量及水平（解码参数、模型版本、协议），并在局限中讨论外部效度；但未系统列出所有环境/调用恒定项。 |
| C4 | 匹配 | NA | — | 未使用匹配设计，也不存在匹配变量、匹配后均衡性或回归假象问题。 |
| C5 | 纳入为变量 | NA | — | 研究未把已知混淆变量作为区组/协变量纳入统计模型；无 ANCOVA/协变量分析结构。 |
| C6 | 盲法 | NA | — | 自动指标评估，无人类主试、评分者或需要施盲的被试；不适用盲法安排。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级或拉丁方/ABBA 设计。 |
| D1 | 练习效应 | NA | — | LLM 各提示/条件独立生成，无人类练习效应或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长、休息间隔或疲劳效应问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM 每次生成独立，无跨条件清洗期或迁移残留。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉设计，不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 主要使用客观文本指标/准确率，不是被试内绝对量表评分，不涉及范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多候选选项、序列刺激呈现或需要随机化/反平衡的人类刺激顺序设计；提示变体为独立生成。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分或默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不涉及掩饰情节、事后访谈或需求特征。 |
| E5 | 实验者效应 | NA | — | 数据采集与评分完全自动化，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Figure 3 reports mean and variance across 4 runs; p.8 Figure 4 shows sentiment/toxicity/semantic-similarity distributions; p.31 Table E.6 reports scores. | 报告了部分分布/均值方差，但未系统报告偏度、端点频率或 pilot 难度校准；NTS 与 PE 接近上限也未讨论天花板/地板效应对解释的影响。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，不适用传统共同方法偏差分析。 |
| F1 | 统计结论效度 | 0 | p.31 Table E.6 reports point scores; p.7 Figure 3 reports variance across 4 runs, but no confidence intervals, effect sizes, or multiplicity correction. | 主要分析为描述性分数和排名，没有报告推断统计所需的效应量/置信区间，也没有样本量依据与多重比较校正；基本要件未达成。 |
| F2 | 内部效度 | NA | — | 纯观察性基准评测，无随机分配、分配隐藏或因果推断主张；不适用实验内部效度流程。 |
| F3 | 构念效度 | 0.5 | p.5 defines seven metrics; p.25 Appendix C acknowledges external-classifier bias and reports VADER ablation (Pearson r=0.785). | 有部分构念效度/稳健性讨论（分类器偏差、VADER 消融），但未报告评分信度、操纵检验或完整构念效度证据。 |
| F4 | 外部效度 | 0.5 | p.6 lists 22 LLMs; p.23 Table B.4 gives identifiers/sizes; p.10 Limitations discusses language scope and model coverage. | 报告了模型样本来源与特征，并讨论语言和模型覆盖边界；但未报告跨情境复现或抽样代表性检验。 |
| G1 | 分析单位 | 0.5 | p.5 constructs datasets and evaluates all models; p.7 Figure 3 notes error bars are SD across 4 generation runs; p.31 aggregates to model-metric scores. | 存在模型内多次生成、提示/数据集嵌套的聚集结构，但分析主要用模型级聚合均值，未说明分配/分析层级匹配或使用多层模型显式分离方差。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；模型被视为特定评估对象而非从模型总体抽样的随机效应，研究不需要模型随机效应推断。 |
| G3 | 材料作为随机效应 | 0 | p.5 uses fixed prompt sets (e.g., 100 prompts expanded to 1,100/2,200); p.31 aggregates scores without item random effects or item-level generalization analysis. | 有限提示/材料被当作固定刺激汇总到模型级，未将 prompt/item 作为随机效应，也未论证对材料总体的推广；存在语言作为固定效应谬误风险。 |
| G4 | 统计功效 | 0 | p.5 reports dataset sizes; no a priori power analysis, expected effect size, or sample-size justification is reported. | 无设计阶段功效分析或样本量/重复次数论证，结果也未报告 CI；不满足基本要件。 |
| G5 | 研究者自由度 | 0.5 | p.19–20 report data-cleaning and exclusion rules; p.5 lists all seven metrics; p.23 lists models; no preregistration or exploratory/confirmatory distinction. | 报告了排除规则与全部主要指标/模型，但未说明样本量决定方式、是否中途停止或预注册，也未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1 provides code/data link but no preregistration platform, timestamp, or registered analysis plan; no mention of preregistration elsewhere. | 未发现预注册；按口径记 0，而不是 NR。 |
| J1 | 位置偏差 | NA | — | 研究不做多候选项选择、排序或 LLM-as-judge 成对比较；无候选位置偏差。 |
| J2 | 冗长偏差 | NA | — | 评估指标为情感/毒性/相似度/代词匹配/数学准确率，不是开放性生成长度质量比较；无长度偏差评分问题。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话操纵，不涉及谄媚。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge 评估模型输出；主要用 RoBERTa、Perspective API、MiniLM embedding 与规则/准确率。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.6 and p.23: “chain-of-thought prompting with eight randomly selected exemplars”; no example-set seed, order counterbalancing, or full template given. | 数学 PE 使用 8 个随机 few-shot 示例，报告了来源与数量；但未报告标签比例、排列反平衡、多 seed 重采样和完整提示模板，信息不完整。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4 and p.19–20 describe template structures and word lists; p.1 links code/data; no prompt-version sensitivity ablation or dev/test split reported. | 模板结构和部分提示设计可查，且有代码链接，但未报告完整 prompt 版本化、语义等价敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG 或关键信息位置操纵实验。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: max token 200, temperature 0.95, top-p 0.95; p.7 Figure 3 notes 4 generation runs; p.10 mentions random seed but does not report its value. | 报告了主要采样超参与部分任务 4 次重复，但未完整报告 seed、top-k/repetition penalty、每次重复的均值与 95% CI；闭源 API 有日期但一致性不完整。 |
| J9 | 重复与文本退化 | 0.5 | p.6 reports temperature/top-p and max token length; p.23 same setup. No repetition rate, degeneration rate, or repetition penalty reported. | 报告了解码策略和长度上限，但未报告重复率/退化率及 repetition penalty；条件间解码策略大体恒定但退化质控缺失。 |
| J10 | 分词效应 | NA | — | 仅英文单语言评测，局限中明确说 language scope limited to English；无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.10 Limits: RealToxicityPrompts was released prior to 2022 and may have been seen during training; authors mitigate by relative comparisons under same protocol but acknowledge incomplete control. | 识别并讨论了测试集污染风险，但未逐个模型对照训练截止日期，也未做 n-gram/DCQ 污染检测或污染率估计。 |
| J12 | 基准饱和 | 0.5 | p.31 Table E.6 shows NTS and PE often near ceiling (e.g., PE 0.96–0.99); no saturation analysis or alternative continuous metrics reported. | 报告了分数量程与多处接近上限的分数，但未系统评估基准饱和、改用更难子集或连续指标，也未做分数差异的 CI 比较。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；无 IFEval 式指令约束测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求 JSON/结构化输出或文法约束；无格式合法率与内容错误分离问题。 |
| J15 | 越狱稳健性 | NA | — | NTS 测量生成文本毒性，不是越狱/对抗攻击安全评估；无攻击族与 ASR 设置。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 Abstract mentions evaluating “cognitive behaviors under different gender assumptions”; p.3–5 operationalize gender fairness in LLM outputs; no human same-paradigm comparison. | 论文将公平/刻板印象等构念用于 LLM 评估，但未系统论证 LLM 上构念与人类同名心理构念的异同，也无人类对照实验；跨模型比较作为评估对象而非被试样本。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不报告随模型规模/训练进展的能力曲线，也不宣称涌现/突变；模型大小仅描述性列出。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标进行训练、RL、best-of-N 或奖励优化；纯评估研究。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.23 Table B.4 gives exact model identifiers/API names; p.7 notes 4 generation runs and error bars; no 95% CI or paired model comparisons reported. | 报告了模型 snapshot 标识和部分重复次数，但多数分数无 CI、无配对检验，也未发布完整原始推理日志；可复现性信息部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示生成/评估，无多轮对话历史累积，也不主张多轮部署。 |

## 编码小结
该研究的核心贡献是指标操作化、数据构建与跨模型评测，七维指标公式、数据清洗、模型标识和部分重复运行报告较清楚。主要不足是缺少推断统计与置信区间、项目/提示随机效应、预注册、功效分析、提示敏感性与采样不确定性系统控制；大量人类实验设计组件因纯基准评估而 NA。
