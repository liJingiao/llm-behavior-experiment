# article_220 | StressPrompt: Does Stress Impact Large Language Models and Human Performance Similarly? | 2025

研究类型概述：该研究属于 LLM 基准评测/LLM-as-participant：用 1–10 级 StressPrompt 作为系统提示操纵“压力”，在 6 个指令微调 LLM 与多个基准上比较表现；20 名人类被试仅用于对提示的压力水平评分校准；另用 RepE 分析隐藏状态。没有人类任务表现实验，主要结论是 LLM 表现呈 Yerkes-Dodson 倒 U 形。
- **研究构念（Construct）**：压力唤起与任务表现的Yerkes-Dodson倒U关系｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：向多个现成LLM施加不同强度的StressPrompt，让其完成指令遵循、复杂推理和情绪智能任务，并与Yerkes-Dodson规律比较。（操纵压力等级、压力理论框架、任务类别和模型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p3: 'We constructed a total of 100 prompts ... 20 offline participants ... rated the stress induced by all 100 prompts on a scale from 1 to 10'; p4: 'We constructed ten distinct sets of prompts, each corresponding to a specific stress level S_i'. | 压力水平被明确操纵为 1–10 级系统提示，并有人类评分信度/分类作为操纵验证；但未清楚报告各模型、任务或提示如何分配到水平、是否随机化/独立调用，操纵检验主要是提示评分而非 LLM 压力状态，故为 0.5。 |
| A2 | 因变量 | 0.5 | p5: 'The datasets employed ... IFEval, BBH, MATH, GPQA, MuSR, MMLU-P ...'; p4 Eq. 1 uses task-specific 'Metric'; p7 Table 1 reports means and SDs. | 因变量用基准指标/准确率测量，计分方式有公式和 lm-eval 默认设置；但未逐基准报告条目数、计分细节、信效度证据、预处理或天花板/地板效应说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p5: 'The generation temperature was set to 0, and specific dialogue tokens were used to ensure consistency'; 'using the lm eval framework with default settings'; 'All evaluations were performed on NVIDIA A100 GPUs'. | 报告了温度、对话 token、默认评测设置和硬件等部分控制手段，但未系统列出控制变量清单并逐一说明控制方式，也未讨论外部效度限制，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p5: 'model architecture and training specifics play a crucial role in how stress affects performance'; 'task complexity significantly impacts the stress level at which peak performance is achieved'. | 事后提到模型架构/训练与任务复杂度影响压力-表现关系，但没有把它们作为混淆变量系统控制，也未讨论残余混淆或敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 没有正式界定调节变量或进行乘积项交互/简单斜率分析；任务复杂度和模型差异只是描述性解释，不构成受控调节检验，故不适用。 |
| A6 | 中介变量 | NA | — | 没有中介变量、直接/间接效应分解或因果链中介假设，故不适用。 |
| A7 | 操作性定义 | 0.5 | p3: prompts based on four psychological frameworks; p4: 'For each task T ... each stress level set S_i ... conditioning the model on the prompts in S_i'; p4 Eq. 1. | 对压力操纵和基准评分给出了可复现的框架与公式，但未在正文展示完整 StressPrompt 文本、逐任务评分细节和各水平操纵步骤，故为 0.5。 |
| A8 | 水平数与类型 | 0.5 | p3: 'a scale from 1 to 10, where 1 represented minimal stress and 10 represented maximal stress'; p4: 'ten distinct sets of prompts, each corresponding to a specific stress level S_i where i ∈ {1,...,10}'. | 报告了 10 个水平及 1–10 标签，但未明确水平类型（名义/等级/连续）、间距/全距处理或连续变量中心化说明，故为 0.5。 |
| A9 | 单一操作化的风险 | 0 | p3: 'We constructed a total of 100 prompts ... collectively referred to as StressPrompt'; p5: evaluation uses listed benchmarks; no limitations discussion. | 关键构念“压力”主要依赖单一 StressPrompt 操作化；虽有多基准衡量能力，但未报告多操作化会聚证据，也未在局限部分讨论单一操作化对可推广性的限制，故为 0。 |
| A10 | 单一方法的风险 | NA | — | 自变量是实验者构造的提示文本，因变量是客观基准得分，并非同源自陈式测量；共同方法偏差问题不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试间随机分配；每个 LLM 在不同压力水平下被重复评测，不存在独立被试组接受单一水平的被试间设计，故不适用。 |
| B2 | 被试内设计 | 0.5 | p4: 'For each task T ... each stress level set S_i, we evaluated the performance of the LLM f by conditioning the model on the prompts in S_i'; p5 lists multiple models. | 同一模型覆盖 10 个压力水平，属于重复评测；但未报告条件顺序安排、随机化或平衡方案。每次调用看似独立，顺序效应可能有限，但设计报告不完整，故为 0.5。 |
| B3 | 混合设计 | NA | — | 没有明确采用混合设计并逐因素标注组间/组内，也没有混合模型或重复测量 ANOVA 的组间/组内误差项报告，故不适用。 |
| B4 | 因子设计 | NA | — | 核心是单因素压力水平的多模型、多基准描述性比较，没有正式因子设计、完整设计矩阵和交互项检验，故不适用。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验（F、df、p、效应量）；故不适用。 |
| B6 | 交互作用 | NA | — | 没有正式交互项检验、简单主效应或带误差棒的交互图；任务/模型差异只是描述性观察，故不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层变量及区内随机分配程序，故不适用。 |
| B8 | 拉丁方 | NA | — | 没有被试内条件顺序设计，也未使用拉丁方平衡顺序，故不适用。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；没有非随机分组、选择偏差或准实验因果推断框架，故不适用。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM 评测为独立提示调用，没有人类被试内处理的不可逆后效或迁移对称性问题，故不适用。 |
| C1 | 随机化 | NA | — | 没有将独立分析单位随机分配到互斥条件；每个模型接受全部压力水平，不涉及随机分配/分配隐藏，故不适用。 |
| C2 | 平衡 | NA | — | LLM 调用为独立提示，不涉及需要平衡的条件顺序；未报告顺序分配并非遗漏核心质控，故不适用。 |
| C3 | 恒定 | 0.5 | p5: 'The generation temperature was set to 0, and specific dialogue tokens were used to ensure consistency'; 'using the lm eval framework with default settings'; 'All evaluations were performed on NVIDIA A100 GPUs'. | 列出了温度、对话 token、默认设置与硬件等恒定项，但未系统说明各恒定水平及对外部效度的限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 没有使用匹配设计或匹配变量，故不适用。 |
| C5 | 纳入为变量 | NA | — | 没有将已知混淆变量作为区组/协变量纳入统计模型；该研究也未采用 ANCOVA 框架，故不适用。 |
| C6 | 盲法 | NA | — | 主数据为自动化 LLM 评测，无人类被试/评分者需要条件盲法；人类仅参与提示压力评分，核心 LLM 结果不存在条件盲法结构，故不适用。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡、拉丁方或 ABBA 等顺序平衡层级，故不适用。 |
| D1 | 练习效应 | NA | — | 每个提示/问题作为独立输入，无多轮上下文内学习或练习阶段，故不适用。 |
| D2 | 疲劳效应 | NA | — | LLM 评测无 session 疲劳问题；人类仅做离线提示评分，不构成长时实验任务，故不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个条件为独立 API/模型调用，无跨条件残留或清洗期问题，故不适用。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移/不对称迁移设计，故不适用。 |
| D5 | 范围效应 | NA | — | 主要因变量为客观基准准确率/得分，不是被试内绝对量值估计或李克特量表，故不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p5: benchmarks include 'MMLU'、'GPQA'、'MMLU-P' 等多项选择任务；'The evaluations were conducted using the lm eval framework with default settings'；未描述选项/题目顺序随机化或反平衡。 | 多项选择基准存在答案选项位置偏差风险，但研究未报告选项或刺激顺序随机化/平衡方案，故为 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用含正反向题项的态度/Likert 自评量表；人类压力评分为单次 1–10 评分，不涉及默许偏差的正反向题设计，故不适用。 |
| E3 | 极端 / 中间反应倾向 | 0.5 | p3–p4: '20 offline participants ... rated ... on a scale from 1 to 10'；p4: 'Figure 4 illustrates the distribution of StressPrompt across various stress levels'. | 展示了评分分布，但未报告偏度、端点/中点使用比例，也未讨论反应风格；无跨群体比较。基本分布信息有但不完整，故为 0.5。 |
| E4 | 需求特征 | 0 | p3: '20 offline participants ... rated the stress induced by all 100 prompts'; no cover story or post-experimental inquiry reported. | 人类被试仅进行压力评分，未使用掩饰情节或事后访谈检查其对研究假设的推断，需求特征未控制，故为 0。 |
| E5 | 实验者效应 | 0 | p3: '20 offline participants' rated prompts; no blinding, rater training, or standardized script reported. | 人类评分环节未报告盲法层级、评分者培训或脚本化程度；主数据虽自动化，但人类标注存在实验者效应风险，故为 0。 |
| E6 | 天花板 / 地板效应 | 0.5 | p7 Table 1: 'Values are averaged over multiple prompts and expressed with their respective standard deviations'; MATH/MMLU-P 等显示接近地板的数值。 | 报告了各条件均值与 SD，可部分排查天花板/地板；但未报告偏度、端点频率或 pilot 难度校准过程，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 自变量为提示文本操纵，因变量为客观基准得分，来源并非同源自评；共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p7 Table 1 reports means ± SD, but no effect sizes/95% CI for stress effects or sample-size justification; p4 only reports Cronbach α/ICC for ratings. | 主假设检验未报告效应量或置信区间，也无样本量确定依据/多重性校正；只有描述统计和图形趋势，故为 0。 |
| F2 | 内部效度 | 0 | p5 describes models, temperature and benchmarks, but no random assignment/allocation concealment, baseline equivalence testing, or participant flow/loss handling. | 未报告随机分配与分配隐藏、各组基线等价性、被试/试次流向与损耗处理，也未评估内部效度威胁，故为 0。 |
| F3 | 构念效度 | 0.5 | p4: 'Cronbach’s Alpha ... 0.9947'; 'ICC2 ... 0.8942 (95% CI [0.86, 0.92])'; p4 Stress Scanner describes internal-state changes. | 报告了提示压力评分的信度/评分者一致性，但缺少效度证据、完整操纵检验和多操作化会聚证据；Stress Scanner 只是内部状态描述，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p5 lists models: Llama-3-8B/3.1-8B/70B, Phi-3-mini, Qwen2-72B/7B, Mistral-7B; benchmarks listed; no explicit generalization boundaries. | 报告了模型与基准来源，但未讨论样本/模型/任务的代表性、推广边界或跨情境复现，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p4 Eq. 1 averages over prompts within S_i and QA pairs; p7 Table 1: 'Values are averaged over multiple prompts'; no multilevel model or explicit assignment-level statement. | 分析将提示/问题聚合到模型×压力×任务层面，存在嵌套结构但未显式多层建模；基本提到聚合，未说明分配/分析层级匹配，故为 0.5。 |
| G2 | 随机效应 | 0 | p7 Table 1 and p4 Eq. 1 present aggregated descriptive results; no random-effects structure is reported for models, prompts, or items. | 未说明任何随机效应或随机截距/斜率结构；模型、提示和基准项目均按固定集合处理，无法判断可推广总体，故为 0。 |
| G3 | 材料作为随机效应 | 0 | p3 uses a fixed set of 100 StressPrompt prompts; p5 uses fixed benchmark datasets; no item/material random effect or F′/min F′ analysis. | 材料和基准项目被当作固定刺激，没有把材料/项目作为随机因子纳入分析，犯语言/材料作为固定效应谬误的风险，故为 0。 |
| G4 | 统计功效 | 0 | p5 lists models/benchmarks; p7 Table 1 reports means ± SD; no a priori power analysis, target effect size, or CI for main effects. | 无设计阶段功效分析或样本量论证，结果部分也未报告压力效应的效应量与置信区间，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p5 lists all ten stress levels and benchmark datasets; p7 Table 1 reports main results; no exclusion rules, sample-size stopping rule, or confirmatory/exploratory distinction. | 报告了条件与多个因变量，但未报告数据排除规则、样本量决定方式及验证性/探索性分析区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–10 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册平台、注册编号、样本量/停止规则或分析计划的事前登记；按样本口径记 0。 |
| J1 | 位置偏差 | 0 | p5: benchmarks include 'MMLU'、'GPQA'、'MMLU-P'；'using the lm eval framework with default settings'；未报告选项位置反平衡或正确答案位置随机化。 | 多项选择基准存在候选项/答案位置偏差，但研究完全未提及位置反平衡、交换重判或位置×正确率分析，故为 0。 |
| J2 | 冗长偏差 | NA | — | 评估主要使用基准准确率/客观指标，未描述 LLM-as-judge 或开放性生成长度质量评分，冗长偏差不构成核心风险，故不适用。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或多轮纠错设定，不涉及谄媚操纵，故不适用。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge 评估模型输出；没有裁判模型同源/自我偏好问题，故不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 论文未报告 few-shot in-context examples；未说明示例来源、数量或排列，无法认定存在 few-shot 设计，故按不适用处理。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p4 uses StressPrompt as system instruction; p5 only quotes baseline prompts 'you are a helpful assistant' and 'let’s think step by step'; full StressPrompt templates/versions/sensitivity ablations are not reported. | 提供了基线措辞但未给出完整 StressPrompt 模板、版本号、敏感性与 dev/test 划分，故为 0。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短提示加题目，不涉及长文档、RAG 或长上下文位置操纵，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | p5: 'The generation temperature was set to 0'; p7 Table 1 reports values 'averaged over multiple prompts and expressed with their respective standard deviations'; no seed/top-p/repeated sampling CI. | 报告了 temperature=0，但未报告 top-p/top-k、随机种子、重复采样次数与置信区间；表中的 SD 是跨提示变异而非重复调用方差，故为 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p5: 'The generation temperature was set to 0, and specific dialogue tokens were used to ensure consistency'; no repetition penalty or degeneration-rate QC reported. | 报告了基本解码设置（temperature=0），但未报告 repetition penalty、n-gram 重复率/退化率或截断比例，故为 0.5。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文基准，无跨语言/跨脚本比较或 token 成本比较，故不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p5 lists public benchmarks including MMLU, BBH, MATH, GPQA, MuSR; model versions are named, but no training cutoff/contamination check is reported. | 使用公开基准但未对照模型训练截止日期、未做污染检测或报告污染率，直接把分数当作能力指标，故为 0。 |
| J12 | 基准饱和 | 0 | p7 Table 1 reports benchmark scores and SDs; no SOTA position, ceiling analysis, continuous metrics, or bootstrap CI comparison. | 未报告基准分数量程与 SOTA 位置，也未讨论饱和/地板问题；在接近上限或下限的分数上仍作趋势解释，故为 0。 |
| J13 | 指令遵循 | 0.5 | p5 includes IFEval, an instruction-following benchmark; p7 reports IFEval scores; no constraint-type breakdown or machine-verifiable criteria details. | 使用 IFEval 这一可验证指令基准，基本满足机器可判定标准；但未按否定/数量/格式/风格约束拆分准确率，也未说明模型指令微调数据，故为 0.5。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 研究未要求 JSON/结构化输出或文法约束，故不适用。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估，无有害请求、攻击族或 ASR 设置，故不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1 Abstract: 'LLMs, like humans, perform optimally under moderate stress, consistent with the Yerkes-Dodson law'; p7: 'LLMs can map human-like relationships between stress and task performance'. | 论文明确把 LLM 压力表现类比人类 Yerkes-Dodson，但未系统论证 LLM 构念与人类同名构念的异同，也无可比的人类任务表现对照；模型版本报告也不够精确，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有随模型规模/训练进展的能力曲线或涌现/突变宣称，故不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究为纯基准评测，没有训练、RL、best-of-N 或代理指标优化过程，故不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p5 names model families/versions; p7 Table 1 reports means ± SD; no exact API dates/snapshot hashes, repeated-run N/CI, paired tests, or raw logs. | 未报告精确 snapshot、重复次数与 95% CI、配对检验或原始推理日志；仅有模型名称和均值/SD，故为 0。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示加问题，无多轮对话历史累积，也不主张多轮部署，故不适用。 |

## 编码小结
研究提出了可复用的 StressPrompt 并做了多模型、多任务描述性比较，但核心推断多为均值/SD 和图形趋势，缺少正式效应量、置信区间、随机化/顺序控制、污染与位置偏差检查、预注册与功效分析。构念上将 LLM 内部状态与人类压力类比，外推较强，报告完整性有限。
