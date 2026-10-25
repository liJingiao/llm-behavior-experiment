# article_105 | Beyond Facts: Evaluating Intent Hallucination in Large Language Models | 2025

研究类型概述：这是一项 LLM 基准评测与自动指标开发研究：作者构建 FAITH QA 基准，提出 ConstraintScore，用多个 LLM 生成回答，并用 GPT-4o 作为主要裁判对意图约束满足度打分，同时用 1,000 条样本的人类评分验证指标。分析单位为查询/回答/模型-任务分层，不是人类被试实验。
- **研究构念（Construct）**：意图理解、约束保持、遗漏/误解型intent hallucination｜CA 构念锚定：语言理解（language comprehension, `trm_4a3fd79d0a775`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：这是一项 LLM 基准评测与自动指标开发研究：作者构建 FAITH QA 基准，提出 ConstraintScore，用多个 LLM 生成回答，并用 GPT-4o 作为主要裁判对意图约束满足度打分，同时用 1,000 条样本的人类评分验证指标。分析单位为查询/回答/模型-任务分层，不是人类被试实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | — | 无研究者主动操纵的实验自变量；模型、任务、难度均为基准评测中的观察性分层/比较变量，而非实验分配条件。 |
| A2 | 因变量 | 0.5 | p.5: 'CS(q,y)=Ws/Wt×10'; p.5: 'A high score (≥9) indicates strong adherence...'; p.7: 'Perfect' and 'Constraint Score (CS)' as metrics. | 因变量指标与计分方式清楚（Perfect、CS、Fact），但未报告评分者信度/内部一致性，也无连续指标预处理细节。 |
| A3 | 控制变量 | 0.5 | p.6: 'For all baselines, we set the temperature τ = 0.3'; p.15: prompt templates; p.6 footnotes give model snapshots. | 报告了温度、零样本设置、提示模板和模型版本等控制，但未系统列出控制变量清单及所有控制手段。 |
| A4 | 混淆变量 | 0.5 | p.2: 'LLM judgers tend to provide biased evaluations'; p.16: 'minimal bias from using GPT-4o for both generation and evaluation' with Claude-3 check. | 识别了 LLM-as-judge 与同源模型偏差，并用 Claude-3 复评作部分敏感性检查；但未系统讨论任务/难度/主题等残余混淆。 |
| A5 | 调节变量 | NA | — | 无调节变量假设或交互检验设计。 |
| A6 | 中介变量 | NA | — | 无中介变量假设或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | pp.4-5, Eqs.(1)-(7): constraint mapping and scoring steps; pp.19-20, Tables 6-7: full prompt templates; p.5 Table 1: task statistics. | 关键构念（intent constraint、omission/misinterpretation、ConstraintScore）给出了可复现的操作化步骤、公式、提示词和任务设置。 |
| A8 | 水平数与类型 | NA | — | 无主动操纵的多水平自变量；任务类型、难度和模型只是基准分层/比较维度，不作为实验水平分配编码。 |
| A9 | 单一操作化的风险 | 0.5 | p.6: multiple tasks and metrics; p.7: human evaluation; p.9: limitation says only 2 major causes and 4 task types. | 使用多个任务与多种指标并提供人类评分对照，但未系统报告跨操作的会聚证据；局限部分主要谈任务/类别粒度，而非单一操作化限制。 |
| A10 | 单一方法的风险 | 0.5 | p.6: GPT-4o used for ConstraintScore; p.16: Claude-3 check 'Pearson correlation of 0.93'; p.7: human evaluation. | 生成与评分均涉及 LLM，且 GPT-4o 同时是被评模型与主要裁判；作者做了 Claude-3 和人类评分部分对照，但无正式共同方法偏差检验。 |
| B1 | 被试间设计 | NA | — | 无人类被试间分配；不同 LLM 是观察性比较组，不是随机分配的被试组。 |
| B2 | 被试内设计 | NA | — | 每个模型在固定测试集上评测，但没有人类被试内条件顺序设计或顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合实验设计。 |
| B4 | 因子设计 | NA | — | 论文不是因子实验；没有完整设计矩阵与交互项统计，仅有基准分层比较。 |
| B5 | 主效应 | NA | — | 无因子实验主效应检验。 |
| B6 | 交互作用 | NA | — | 无因子实验交互作用检验。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验干预研究；无处理分配或因果效应推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理条件，因此不涉及可逆性/迁移对称性。 |
| C1 | 随机化 | 0.5 | p.6: '150 randomly sampled questions'; p.5: 'One of the inputs is randomly removed'; p.6: 'One article is randomly removed per case'. | 存在随机抽样/随机移除内容，但未报告随机数生成工具、分配隐藏或随机化后均衡性检验。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件顺序设计。 |
| C3 | 恒定 | 0.5 | p.6: temperature τ = 0.3; p.15: fixed prompt templates; p.14: model versions/snapshots. | 报告了部分恒定变量（温度、提示、模型版本），但没有系统列出全部恒定变量及讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | 0 | p.15: 'five paid student annotators... majority voting... read the guidelines'; no blinding described. | 人类评分者参与验证，但未报告盲法安排、对谁施盲或盲法成功检验。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级设计。 |
| D1 | 练习效应 | NA | — | LLM 查询/回答独立生成，无练习块或跨试次学习设计。 |
| D2 | 疲劳效应 | NA | — | 无长 session、休息间隔或时间分散设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件清洗期或迁移设计。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性检验。 |
| D5 | 范围效应 | NA | — | 无人类被试内绝对判断/量表范围效应问题；0–10 分为 LLM 裁判评分，不是被试量表锚定。 |
| E1 | 位置 / 顺序偏差 | 0 | p.5: three RAG articles 'One article is randomly removed per case'; no article-order randomization/counterbalancing reported. | RAG 多文章刺激的顺序可能影响模型，但论文只随机移除内容，未报告对文章呈现顺序做随机化或反平衡。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无跨群体等级量表反应风格比较。 |
| E4 | 需求特征 | NA | — | 人类标注者不是实验被试；主研究不涉及掩饰情节或事后访谈。 |
| E5 | 实验者效应 | 0 | p.15: five paid student annotators, majority voting, guidelines; no blindness/training standardization details. | 有人类评分者参与，但未报告盲法层级、评分者培训标准化或对假设知情控制。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Table 3: Perfect and CS means; p.7 Figure 3 KDE; no skew/endpoint frequency or pilot difficulty calibration. | 报告了均值/Perfect 端点率，但未报告偏度/端点频率，也未说明任务难度预校准过程。 |
| E7 | 共同方法偏差 | 0.5 | p.6: GPT-4o for generation/evaluation; p.16: Claude-3 check Pearson r=0.93; p.7: human evaluation. | 生成与评分同属 LLM 渠道，作者用异源裁判和人类评分部分控制，但未做正式共同方法偏差统计检验。 |
| F1 | 统计结论效度 | 0.5 | p.23 Table 15: paired t-tests, Mean Diff ± SD, t, p; p.7: MSE; no CI/effect sizes or power analysis. | 报告了部分效应量（均值差）、p 值和配对比较，但缺置信区间、样本量功效依据及多重性校正。 |
| F2 | 内部效度 | NA | — | 非实验性基准比较，无随机分配/因果处理推断；不适用内部效度的实验分配问题。 |
| F3 | 构念效度 | 0.5 | p.7: human evaluation MSE comparison; p.16: Claude-3 judge check; no inter-rater reliability reported. | 有指标与人类判断的效度对照，但无评分者信度/内部一致性及操纵检验。 |
| F4 | 外部效度 | 0.5 | p.1: 20,068 queries; p.14: model/data sources; p.9: limitation on only 2 causes/4 tasks and no reasoning models. | 报告了数据来源、任务与模型清单及部分限制，但无抽样代表性论证或跨情境复现。 |
| G1 | 分析单位 | 0.5 | p.6: test set 150 sampled questions per category; p.23: paired t-tests across 6 tasks; no multilevel model. | 说明了在查询/任务层面汇总分析，但未用多层模型处理回答嵌套于任务/查询的结构。 |
| G2 | 随机效应 | 0 | p.23 Table 15: model comparisons via paired t-tests; no random effects or mixed models reported. | 未说明任何随机效应结构；若要将结论推广到查询总体，需要项目/查询随机效应，但论文只作固定比较。 |
| G3 | 材料作为随机效应 | 0 | p.6: 150 test questions per category; p.7 Table 3 aggregates; no item random effect or quasi-F. | 有限测试查询被当作固定材料处理，未纳入材料/项目随机效应，结论向材料总体的推广未论证。 |
| G4 | 统计功效 | 0 | p.6: 'due to monetary costs' 150 randomly sampled questions; no power analysis or CIs. | 无设计阶段功效分析；样本量仅以成本说明，结果也未报告主要指标的置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.6: metrics and test-set sampling; p.15: human evaluation; no exclusion rules/stopping/exploratory-vs-confirmatory distinction. | 报告了主要指标与条件，但未报告数据排除规则、停止规则或验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–25 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册、注册编号或数据收集前分析计划；属于未预注册研究。 |
| J1 | 位置偏差 | NA | — | 实验不是多候选项选择、排序或成对 LLM-as-judge 比较，而是单回答约束满足度评分。 |
| J2 | 冗长偏差 | 0 | pp.4-5: ConstraintScore rubric checks constraints; no length rubric, length-score correlation, or length-controlled comparison. | 开放式生成由 LLM 裁判评分，但未识别或控制长度偏差，未报告回答长度与得分关系。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或多轮纠错式谄媚操纵。 |
| J4 | 自我偏好 | 0.5 | p.6: GPT-4o default for ConstraintScore; p.16: Claude-3 check r=0.93 and 'minimal bias from using GPT-4o for both generation and evaluation'. | 识别了裁判与被评模型同源风险并做异源裁判检查，但未报告各裁判单独结果、匿名化或 favor-own-generation 比例。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 采用零样本提示，无 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | pp.19-20 Tables 6-7: full prompt templates; p.15: prompt sections; no sensitivity ablation or dev/test separation reported. | 公布了较完整提示模板，但没有语义等价措辞敏感性消融、dev/test 划分或 prompt 搜索过程说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0 | p.5: RAG setup; p.8: 'limitations of longer context'; no actual token counts or first/middle/last position manipulation. | 有长上下文/RAG 场景，但未报告实际上下文 token 数、关键信息位置操纵或位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'temperature τ = 0.3'; p.15: self-consistency 2 times / rerun, fact-check 5 times; p.6 footnotes: model snapshots. | 报告了温度和部分重复策略及模型快照，但缺 top-p/top-k、seed、每次条件重复采样 N 和主要分数的置信区间；温度设置还有正文/附录不一致。 |
| J9 | 重复与文本退化 | 0 | p.6: temperature only; no decoding strategy, repetition penalty, repetition rate or degeneration analysis. | 涉及开放生成，但未报告解码策略与重复/退化指标。 |
| J10 | 分词效应 | NA | — | 单语言英文、单脚本研究，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.1: new FAITH QA benchmark; p.14: model versions; no training-cutoff comparison or contamination detection. | 构建了新基准并报告模型版本，但未对照训练截止日期、未做 n-gram/DCQ 污染检测，也未明确证明测试集未见于训练语料。 |
| J12 | 基准饱和 | 0.5 | p.7 Table 3: Perfect rates and continuous CS; p.5: CS 0-10; no saturation analysis or bootstrap CI. | 同时报告离散 Perfect 与连续 CS，部分任务分数较高，但未讨论基准饱和、未报告 SOTA 水位或置信区间比较。 |
| J13 | 指令遵循 | 0 | pp.4-5: Sϕ(c,y) parameterized with an LLM; p.8 Figure 4: violated constraint categories; no machine-verifiable per-constraint checks. | 指令/约束遵循依赖 LLM 裁判，而非可机器判定标准；虽按 subject/action 等类别拆分，但基本要件未满足。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.19 Table 5 and p.20 Tables 6-7 specify 'START:'/final listing output; no format-validity rate or retry statistics. | 提示中规定了结构化输出格式，但未报告格式合法率、重试策略或格式失败与内容错误分离。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文是工程/应用型 LLM 能力与基准评测，不主张把 LLM 作为心理学/认知科学被试测量人类同名构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨规模/训练进展的涌现能力曲线或涌现宣称；仅有限模型间比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标进行训练、RL、best-of-N 等优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6 footnotes: exact snapshots (e.g., gpt-4o-2024-05-13); p.6: 150 sampled questions per category; p.23: paired tests; no repeated-run CIs. | 报告了精确模型快照、样本量和配对比较，但没有重复采样次数/随机种子/95% CI，难以估计非确定性方差。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 所有任务为单轮查询/单轮回答评估，无多轮对话实验。 |

## 编码小结
论文清楚定义了 intent hallucination（omission / misinterpretation）、约束抽取与 ConstraintScore 计分流程，并提供了较完整的任务、数据统计、模型版本和提示模板；但作为基准评测，缺少随机分配/顺序平衡、随机效应建模、重复采样置信区间、污染与饱和分析、裁判偏差系统控制等。总体是较扎实的基准与指标验证工作，但统计与可复现性报告仍有明显缺口。
