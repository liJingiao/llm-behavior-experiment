# article_204 | ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs | 2025

研究类型概述：该文提出 ReCogLab 生成式基准框架，用可配置图结构与文本模板自动生成关系推理题，并在多个开源/闭源 LLM 上做零样本评测与认知科学启发式探针（容量、符号距离、顺序、一致性/不确定性等）。分析单位主要是自动生成题目/配置与被评测模型，不涉及人类被试分配。
- **研究构念（Construct）**：关系推理、符号距离、关系记忆和元推理偏差｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：用ReCogLab生成文本关系图问题，让多种现成LLM回答路径、比较、家族、社会网络及一致性和不确定性问题。（改变实体数、图规模、符号距离、无关上下文、表述顺序、先验一致性以及矛盾或信息不足。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.4: 'control the core difficulty ... increasing the number of nodes, the number of relationships, and even the structure of the graph'; p.18 lists task parameters such as 'num entities', 'congruence', 'randomize relations', 'do reverse comps'. | 研究确实操纵任务/生成参数并给出多个水平或标签，但未系统报告每个操纵的完整创设程序、单位分配方式与操纵检验，故为0.5。 |
| A2 | 因变量 | 0.5 | PDF p.5: 'we generate 50 validation examples and report on 250-1000 test examples'; p.7 Fig.4: 'Each box reports the accuracy and number of test examples'; p.20: 'we check against all of them for determining correctness'. | 因变量为解析后的答案正确率/准确率，计分与样本量有报告；但未报告测量信效度、连续指标预处理或天花板/地板处理细节。 |
| A3 | 控制变量 | 0.5 | PDF p.5: 'validating on 50 examples before selecting the best prompt and parser'; p.16 provides prompt templates; p.18: 'Jax’s PRNG Keys ... fully reproducible'. | 报告了若干控制手段（固定/验证选择提示与解析器、固定数据种子、PRNG），但没有系统列出所有控制变量及其恒定/控制方式。 |
| A4 | 混淆变量 | 0.5 | PDF p.7: 'we separate out these two effects' for graph complexity vs context length; p.8: 'Random Name ablation removes any connection to the graph problem and real world priors as a control'; p.7 notes Exact Path may benefit from 'number of decoded tokens'. | 识别并部分控制了图复杂度/上下文长度、真实世界先验等混淆，但残余混淆（如生成长度）未系统做敏感性分析或内部效度威胁评估。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量理论模型、乘积项交互检验或简单斜率分析；模型/任务比较是描述性基准比较，不构成调节设计。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或因果链中介假设。 |
| A7 | 操作性定义 | 1 | PDF p.18 lists task parameters; p.19-20 describes domain-specific generation; p.20: 'if there are multiple possible answers, we check against all of them for determining correctness'; p.24-30 gives generated examples; p.1 releases code. | 关键构念有可复现的操作化：任务生成配置、关系/图结构、问题与答案构造、正确性判定及示例均较明确。 |
| A8 | 水平数与类型 | 0.5 | PDF p.18: 'Task Parameters' includes 'num entities', 'congruence', 'randomize relations', 'do reverse comps', 'num families'; p.5 describes configuration sweeps; p.7 varies graph size and symbolic distance. | 报告了多水平的取值/标签，但未完整说明每个因素的水平类型、间距、全距及连续变量中心化/标准化。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p.2-4 presents Comparison, Social Network, Syllogisms and JSON Families as multiple relational-reasoning tasks; p.4: 'include a spectrum of problems in relational reasoning'; p.21-23 provides additional probes. | 关键构念采用多种任务/操作化，但没有报告各操作之间的会聚证据或正式多操作效度分析。 |
| A10 | 单一方法的风险 | NA | — | 自变量是生成任务/配置，因变量是模型答案正确率，均为客观文本任务指标，不存在自陈量表式共同方法偏差的同源问题。 |
| B1 | 被试间设计 | NA | — | 没有人类或 LLM 被试被独立分配到互斥条件组；所有被评测模型在多个基准配置上被评估，不构成被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有以被试为单位、按条件顺序施测的重复测量设计；不同条件是独立生成的评测题集/配置。 |
| B3 | 混合设计 | NA | — | 没有人类或 LLM 被试的组间/组内混合因素设计及相应混合误差项。 |
| B4 | 因子设计 | 0.5 | PDF p.5: 'we generate sweeps of different configurations'; p.7 Fig.4 heatmaps by graph size × symbolic distance with per-cell n; p.7 Fig.5 compares task and flavor-text perturbations. | 存在多因素参数扫掠和分格描述，但未报告完整因子设计矩阵、ANOVA 或正式交互统计量/效应量。 |
| B5 | 主效应 | 0.5 | PDF p.6-7 reports capacity and symbolic-distance patterns; p.8 reports ordering effects; p.9 reports congruence effects across models. | 主效应式模式有描述性报告，但没有报告 F、df、p、效应量或交互显著时的解释限制。 |
| B6 | 交互作用 | 0.5 | PDF p.7 Fig.4 slices accuracy jointly by symbolic distance and graph size; p.8-9 compares order and congruence conditions across models. | 有交互式热图/分条件比较，但没有正式的交互项统计检验、简单主效应检验或带误差棒的交互图。 |
| B7 | 区组设计 | NA | — | 没有以区组/分层变量进行被试或题目分配的设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡条件顺序的被试内设计。 |
| B9 | 准实验设计 | NA | — | 研究不是准实验；没有非随机分组、选择偏差或准实验因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理条件及可逆性/迁移对称性适用条件问题。 |
| C1 | 随机化 | NA | — | 研究没有把实验单位随机分配到处理条件的程序；模型均在相同基准配置上评测，随机种子用于数据生成而非条件分配。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件呈现顺序；各评测题集独立生成并一次性评估。 |
| C3 | 恒定 | 0.5 | PDF p.5: fixed seeds and 'single chain-of-thought prompt'; p.16 provides prompt templates; p.18: 'Jax v0.4.33 randomization implementation'. | 报告了部分恒定因素（提示模板、数据种子、PRNG 版本），但未系统列出模型 snapshot、解码温度、环境等全部恒定条件。 |
| C4 | 匹配 | NA | — | 没有使用匹配/配对分配或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为协变量或区组因素纳入统计模型。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类被试、主试或评分者盲法安排。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡、拉丁方或 ABBA 等条件顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 评测题目独立生成与调用，无跨试次练习或学习累积；不涉及人类练习效应控制。 |
| D2 | 疲劳效应 | NA | — | LLM 评估不存在人类 session 疲劳或休息间隔问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立生成的题集/独立调用，无跨条件延滞或迁移清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件残留或不对称迁移的被试内设计。 |
| D5 | 范围效应 | NA | — | 因变量为答案正确率等客观任务指标，不涉及主观量表绝对判断的范围效应。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF p.19: 'Random simply randomizes the ordering'; p.18 lists 'randomize relations' and 'do reverse comps'; p.8 reports context-ordering experiments. | 对陈述顺序做了随机化或作为顺序条件操纵，但没有完整报告选项位置反平衡、各位置出现次数或被试/题项分配细节。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表；虽然讨论了 Yes/No/Unknown 中的默许偏差，但不是正反向题计分量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 作为基准评测对象，不涉及人类被试需求特征、掩饰情节或事后访谈。 |
| E5 | 实验者效应 | NA | — | 评测自动化，无人类主试/评分者期望效应或盲法问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.7 Fig.4 reports per-cell accuracy and n; p.6 Fig.3 shows capacity curves; p.9 notes some models are 'worse-than-chance (0.5)' on incongruent comparisons. | 报告了准确率均值、分格样本量与难度扫掠，但未系统报告 SD、偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 自变量为任务/配置，因变量为客观答案正确率，不是同源自陈式多构念测量。 |
| F1 | 统计结论效度 | 0 | PDF p.5-6 reports re-seeded accuracy distributions; p.6 Fig.2 is a boxplot; no effect sizes, confidence intervals, or formal inferential tests are reported. | 基本要件未达成：仅报告准确率/分布图与样本数，没有效应量或 CI，也没有多重比较校正说明。 |
| F2 | 内部效度 | 0.5 | PDF p.5: validation on 50 examples before selecting prompt/parser; p.16 prompt validation; p.4 discusses leak safeguards; no random allocation, baseline equivalence, or attrition/flow reporting. | 有一些内部效度控制（验证/测试分离、固定种子、泄漏缓解论述），但缺少分配隐藏、基线等价性和正式内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | PDF p.16: prompt templates and validation; p.2-4 multiple cognitive tasks; p.10 cautions about human-LLM similarity; no reliability/validity statistics or manipulation check. | 通过多任务与验证集提供部分构念效度支持，但没有报告信度、效标/构念效度或操纵检验。 |
| F4 | 外部效度 | 0.5 | PDF p.5 lists evaluated model families (Gemma, Mixtral, Gemini, GPT-4o); p.10 discusses caution about human-LLM comparisons; no exact model versions, sampling frame, or cross-sample replication beyond re-seeding. | 报告了模型来源与部分推广讨论，但未明确外部效度边界、具体 snapshot 或跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | PDF p.5: '50 validation examples and report on 250-1000 test examples'; p.5: '30 different seeded datasets of 200 examples each'; p.6 Fig.2 aggregates by config/seed. | 说明了题目/配置与模型的分析层级，但未使用多层模型显式分离题目嵌套于配置、配置嵌套于任务的方差。 |
| G2 | 随机效应 | NA | — | 没有人类被试随机效应；模型被当作固定评测目标而非从模型总体随机抽样，且未构建混合模型。题目/材料抽样问题在 G3 处理。 |
| G3 | 材料作为随机效应 | 0.5 | PDF p.5 re-seeding: '30 different seeded datasets of 200 examples each'; p.20 rejection sampling to balance rare properties; p.6 Fig.2 shows seed-to-seed variability; no item random effect or mixed model. | 承认并评估了生成数据集的抽样方差，但分析仍以聚合准确率为主，没有把题目/材料作为随机效应纳入模型。 |
| G4 | 统计功效 | 0 | PDF p.5: 'We generate 50 validation examples and report on 250-1000 test examples. Here the important thing is not the specific number of examples'; no power analysis or effect-size/CI report. | 没有事前功效分析或其他系统的样本量论证，也没有报告效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | PDF p.5 gives validation/test sizes and prompt selection; p.20 describes rejection sampling; no explicit trial/subject exclusion rules, stopping rules, or clear confirmatory/exploratory separation. | 部分报告了样本量、验证流程与重采样策略，但未完整报告排除规则、全部测量条件及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | PDF p.1-10 and appendices report no preregistration platform, registration number, or time-stamped analysis plan. | 没有预注册；按判定口径，无预注册且未区分预注册验证性分析记 0。 |
| J1 | 位置偏差 | 0 | PDF p.19: syllogism options are presented as 'All A are Z,' 'No A are Z,' 'Some A are Z,' and 'Some A are not Z'; p.30 examples show fixed option order. No A/B swap, position randomization, or position-accuracy reporting. | 任务含多项选择/排序式选项，但完全未提及候选位置偏差，未做位置反平衡或随机化。 |
| J2 | 冗长偏差 | NA | — | 研究不使用 LLM-as-judge 评估开放式生成质量；因变量主要是可机器判定的答案正确率，不涉及长度被误当质量的裁判问题。 |
| J3 | 谄媚 | NA | — | 任务为无用户立场输入、无反馈/纠错对话的客观闭卷式评测，不存在谄媚操纵情境。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM 裁判或成对模型输出评审；评估基于自动答案匹配。 |
| J5 | 少样本示例选择与排列偏差 | NA | PDF p.16: 'we only consider “0-turn” and “0-trained” prompt strategies'. | 实验为零样本提示，不使用 few-shot in-context examples，故不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.16 provides prompt templates and states validation; p.5: 'validating on 50 examples before selecting the best prompt and parser'; no prompt version/date or sensitivity ablation results. | 公布了较多提示模板并做了验证集选择，但未报告版本化、系统敏感性消融、prompt 长度/分隔符细节及所有版本结果。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | PDF p.8: 'accuracy as a function of the number of input tokens'; p.19 describes ordering (inorder/reverse/random); p.21 rejection sampling for symbolic distance; no first/middle/tail key-information position curve. | 报告了输入 token/上下文长度并操纵陈述顺序，但未系统操纵关键信息首/中/尾位置并报告 U 形位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0 | PDF p.5 re-seeds datasets ('30 different seeded datasets') but does not report temperature, top-p, top-k, model sampling seed, or repeated model samples with CIs. | 只报告了数据生成种子的重采样，未报告解码采样超参或模型调用随机性控制，无法判断 LLM 非确定性。 |
| J9 | 重复与文本退化 | NA | — | 任务以短答案、正确率/选项匹配为主，不评价开放式长文本退化；n-gram 重复率或文本退化不是本研究因变量。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文任务，无跨语言/跨脚本比较或分词效率混淆问题。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.4: 'Safeguards against leaks ... different test seed'; p.5 fixed seeds; no test-set version vs model training cutoff comparison or empirical contamination detection. | 识别了泄漏风险并提出重种子缓解，但未报告模型训练截止日期、测试集版本对照或污染率检测。 |
| J12 | 基准饱和 | 0.5 | PDF p.6-7 reports accuracy across graph sizes; p.7 notes strong performance at low graph size; p.8 uses harder filler/context conditions; no CI or continuous-metric comparison. | 报告了基准分数范围并尝试用难度扩展避免饱和，但未系统评估天花板，也未用连续指标/CI 比较模型差异。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；答案格式是指令的一部分，但主要测量的是关系推理正确率而非指令遵循能力。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p.7: 'instructions to format list answers as a Python code block'; p.16 answer-format templates such as 'Use only one word'; p.5 parser selected on validation; no format-valid rate. | 存在结构化/格式约束和解析器，但未报告格式合法率、重试策略或把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估，无对抗攻击或有害请求集。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.10: 'Many of the effects we observe in LLMs mirror effects observed in humans ... we should as always be careful about drawing too many conclusions about the similarities'; p.2-3 frames tasks from cognitive science. | 有 LLM 构念与人类同名构念关系的讨论和谨慎声明，但未报告模型权重快照，也未做同范式人类对照实验，故为0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究没有宣称规模/训练进展上的“涌现/突变”，也未报告跨规模能力曲线的指标假象问题。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究为纯评测与探针，不涉及对 benchmark、奖励模型或 LLM-judge 的优化训练，不存在代理指标过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.5: '30 different seeded datasets of 200 examples each'; p.6 Fig.2 shows re-seeded score distributions; p.5 lists model families but no exact API snapshot or CIs. | 报告了数据重采样次数和模型家族，但缺少精确 snapshot 标识、逐项/配对检验与 95% CI。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮提示评测，没有多轮对话历史累积，也未主张多轮部署一致性。 |

## 编码小结
作为 LLM 基准与框架论文，任务生成、评测与部分认知探针报告较充分，但并非人类被试实验；许多人类实验设计组件不适用。LLM 评估层面存在提示版本、采样随机性、模型快照、污染检查、选项位置控制等报告不足；总体上可复现工程细节较好，但推断统计与偏差控制不完整。
