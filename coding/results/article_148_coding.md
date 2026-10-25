# article_148 | Beyond Surface Structure: A Causal Assessment of LLMs' Comprehension ability | 2025

研究类型概述：该文是 LLM 能力评估研究，采用因果中介分析框架，将 LLM 对深层语义结构的依赖定义为直接因果效应（ADCE），对表层形式的依赖定义为间接因果效应（AICE）。分析单位主要是“模型×任务×样本”的聚合评估；研究者主动操纵输入干预类型（T=1 同时改变深层与表层结构；T=0 仅改变表层结构），比较 12 个模型在 5 个 benchmark 上的 ADCE、AICE 与 Accuracy，并辅以合成数据验证、SFT 前后比较和 spurious correlation 实验。
- **研究构念（Construct）**：深层语义结构理解与表层形式依赖｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：在乘法、词语重排、GSM8K、逻辑蕴含和常识问答等任务中，对正确样本分别改变深层答案相关结构或仅改变表层形式，计算平均直接与间接因果效应并跨模型比较。（改变深层数字/运算/语义关系或仅改变措辞、掩码、交换形式，并比较任务、模型和规模。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 1 | p4 Eq.2 defines treatment T with levels T=0 (alter s, preserve d) and T=1 (alter both s and d); p6 Sec.3.3 details Mask/Rephrase intervention generation; p20 Alg.1 gives full estimation procedure; p8 reports random-weight baseline with ADCE=0 as a manipulation/validity check. | 自变量明确命名为干预类型 T，两个水平及取值清楚，操纵程序、样本内分配逻辑和操纵检验（random-weight baseline）均有报告，达到 1。 |
| A2 | 因变量 | 0.5 | p6 Eq.5 defines ADCE/AICE via indicator function 1[Y_post≠Y_origin] and reports the range [-1,1]; p8 Fig.5 reports ADCE and accuracy. No internal-consistency/reliability evidence, no repeated-measurement variance, no explicit preprocessing or ceiling/floor handling for the continuous ADCE metric. | 因变量指标与计分方式明确，但信度证据和连续指标预处理/防端点效应说明缺失，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p7–8 states all models are evaluated on the same five benchmarks and with task-specific intervention strategies (Mask for 2-digit Multiplication, GSM8k, Word Unscrambling; Rephrase for Analytic Entailment and CommonsenseQA); p25 gives prompt templates. No systematic control-variable list or per-variable control procedure. | 报告了部分恒定控制（相同任务、相同干预流程、相同 prompt 模板），但未系统列出控制变量及逐一控制手段，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p5 Sec.3.2 explicitly discusses non-estimability due to mutual influences between deep and surface structures and proposes ADCE/AICE approximations; p17–18 Appendix B.1 discusses positivity, consistency, sequential ignorability; p9 Sec.4.5 tests spurious correlation. No formal sensitivity analysis for residual confounding. | 识别了深层/表层结构相互影响及 spurious correlation 等潜在混淆，并说明近似策略和假设，但未报告正式的残余混淆敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 全文没有明确界定调节变量，也没有乘积项交互检验或简单斜率分析；模型规模仅作描述性趋势比较（p8–9 Fig.5/6），不构成调节假设检验，故 NA。 |
| A6 | 中介变量 | 0.5 | p5 Eq.3 decomposes TE into DCE and ICE; p6 Eq.4 defines approximated DCE/AICE; p9 Fig.7 compares δ_ADCE and δ_AICE across models. Effect sizes are reported graphically, but no bootstrap confidence intervals, no explicit a/b path coefficients, and no multiple-mediator specific indirect-effect CIs. | 中介变量（深层/表层结构）被明确界定并做了直接/间接效应分解，但缺少置信区间与路径系数报告，故为 0.5。 |
| A7 | 操作性定义 | 1 | p20 Alg.1 gives full ADCE estimation steps; p22 Alg.2 gives Mask/Rephrase intervention-data generation; p24 Alg.3 gives rephrase-by-agent procedure; p25 Table 4 and p26 Tables 6–7 give prompt templates. Task-specific intervention word pools are described on p22. | 关键构念（深层/表层结构干预、ADCE/AICE）均有可复现的操作化程序、算法、规则与模板，达到 1。 |
| A8 | 水平数与类型 | 0.5 | p4 Eq.2 reports T as binary (0/1) with labels; p7–8 lists 12 models and five tasks as comparison groups. Treatment type is nominal; model scale is ordered/continuous but no centering/standardization is reported for the accuracy-ADCE regression. | 报告了水平数与取值，但缺水平类型（名义/等级/连续）的系统说明、水平间距/全距以及连续变量的中心化说明，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p7–8 evaluates the same deep/surface construct with five benchmarks and two intervention strategies; p8 Fig.5 reports cross-task ADCE patterns. No explicit convergence evidence across operationalizations and no dedicated discussion of single-operation limitation. | 采用了多种任务/干预操作化，但没有系统报告各操作间的会聚证据，也未讨论单一操作化的推广限制，故为 0.5。 |
| A10 | 单一方法的风险 | NA | — | 自变量是研究者构造的输入干预，因变量是模型输出的客观变化（答案是否改变）与准确率，不是同源自陈式测量；共同方法偏差检验不适用于该因果评估设计，故 NA。 |
| B1 | 被试间设计 | NA | — | 研究没有人类被试，也没有将独立被试组随机分配到条件；模型间比较是不同模型评估，不是被试间实验分配，故 NA。 |
| B2 | 被试内设计 | 0.5 | p6 Sec.3.3 and p20 Alg.1: for each correctly answered sample, both T=1 and T=0 intervention data are generated and evaluated, which is a within-item repeated condition. No counterbalancing or order-handling scheme is reported. | 同一原样本接受 T=1 与 T=0 两个条件，属重复测量结构，但未报告条件顺序平衡方案，故为 0.5。 |
| B3 | 混合设计 | NA | — | 论文没有建立明确的组间/组内混合设计分析框架，也没有逐因素标注组间/组内并使用混合模型或分别报告组间/组内误差项，故 NA。 |
| B4 | 因子设计 | 0 | p7–8 has a model × task structure (12 models across five benchmarks) and p8 Fig.5 plots ADCE against accuracy by task. But no complete design matrix, per-cell sample sizes, or ANOVA table with interaction terms is reported. | 存在多因素交叉比较的结构，但未报告完整设计矩阵、每格样本量与交互统计量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p8 Fig.5 reports regression slopes/R² and ADCE values by task, but no F/df/p/effect-size tests for main effects of model or task are reported. | 未报告因子设计意义上的主效应统计检验，故为 0。 |
| B6 | 交互作用 | 0 | p8 Fig.5 and p9 Fig.6/7 present trends by model and task, but no interaction-term statistical test, simple-effects test, or multiple-comparison correction is reported. | 完全未报告交互项统计检验，故为 0。 |
| B7 | 区组设计 | NA | — | 研究未使用区组/分层设计，也未报告区组变量、划分依据或区内随机分配，故 NA。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方顺序安排，故 NA。 |
| B9 | 准实验设计 | NA | — | 研究不是无法随机分配的人类准实验；条件由研究者构造的干预数据定义，故 NA。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM 的每个干预条件在独立推理中评估，不存在人类被试内设计中的处理可逆性/迁移对称性问题；论文也未作此论证，故 NA。 |
| C1 | 随机化 | NA | — | 没有将分析单位随机分配到条件的机制；所有模型在固定 benchmark 和固定干预规则下评估，属于基准评估而非随机分配实验，故 NA。 |
| C2 | 平衡 | 0 | p22 Alg.2 generates T=1 data first and then derives T=0 from it; p20 Alg.1 evaluates both but no condition-order counterbalancing or sequence-allocation scheme is reported. | 条件顺序固定（先构造 T=1，再构造 T=0），未做任何平衡或报告顺序分配，故为 0。 |
| C3 | 恒定 | 0.5 | p7–8 fixes the five benchmarks, task-specific intervention strategies, and model list; p25–27 gives prompt templates. No systematic table of held-constant variables and their levels, and no discussion of external-validity limits of these constants. | 报告了部分恒定控制（任务、干预策略、prompt 模板），但未系统列出恒定变量及其水平并讨论外部效度限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 研究未使用匹配程序，故 NA。 |
| C5 | 纳入为变量 | NA | — | 论文没有将已知混淆变量作为区组或协变量纳入统计模型，也没有 ANCOVA 式调整分析；该组件在本研究的基准评估设计中没有对应结构，故 NA。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，没有人类被试、主试或评分者需要盲法，故 NA。 |
| C7 | 平衡的层级 | 0 | p22 Alg.2 generates T=1 data first and then derives T=0 from it; p20 Alg.1 evaluates both but no condition-order counterbalancing or sequence-allocation scheme is reported. | 研究存在被试内/序列顺序平衡需求（同 C2），但未明确选用完全平衡、拉丁方或 ABBA 层级，亦未报告构造方法与顺序效应形状假设，记 0。 |
| D1 | 练习效应 | NA | — | LLM 每个条件独立推理，不存在跨试次/跨会话的练习效应或上下文内学习；故 NA。 |
| D2 | 疲劳效应 | NA | — | 任务是短时 API/本地推理评估，没有人类 session 时长和休息安排问题，故 NA。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各干预条件在独立推理中评估，无跨条件残留或需要清洗期的设计，故 NA。 |
| D4 | 不对称迁移 | NA | — | 同上，没有跨条件迁移或顺序平衡失效的风险结构，故 NA。 |
| D5 | 范围效应 | NA | — | 因变量为答案是否改变与准确率，不是主观量表评分类任务，无范围效应问题，故 NA。 |
| E1 | 位置 / 顺序偏差 | 0 | p7–8 uses CommonsenseQA as a multiple-choice task, but no option-order randomization or counterbalancing is reported; p25–27 prompt templates also do not mention option shuffling. | 存在多选项任务，但未对选项/刺激呈现顺序做任何随机化或反平衡，也未讨论顺序效应，故为 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，故 NA。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也不涉及跨群体反应风格比较，故 NA。 |
| E4 | 需求特征 | NA | — | 研究对象为 LLM，不存在人类被试可推断研究假设并产生需求特征的问题，故 NA。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者参与，故 NA。 |
| E6 | 天花板 / 地板效应 | 0.5 | p8 Fig.5 and p10 Fig.8 report ADCE/accuracy values and trends, but no skewness, endpoint frequency, or pilot difficulty-calibration analysis is reported. | 报告了主要指标的均值/散点趋势，但未报告偏度、端点频率或任务难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 自变量为研究者构造的干预，因变量为客观答案变化，不是同源自陈式多构念测量，故 NA。 |
| F1 | 统计结论效度 | 0.5 | p8 Fig.5 reports ADCE values, regression slopes β, and R²; p9–10 Fig.6/8 report further effect-size-like comparisons. No confidence intervals, no sample-size/power justification, and no multiple-comparison correction across 12 models × 5 tasks. | 报告了效应量（ADCE、β、R²），但缺置信区间、样本量确定依据和多重性校正，故为 0.5。 |
| F2 | 内部效度 | NA | — | 研究没有人类被试随机分配、分配隐藏、基线等价性或被试流向/损耗问题；其因果推断建立在干预数据构造与模型输出比较上，故该组件 NA。 |
| F3 | 构念效度 | 0.5 | p8 reports a random-weight baseline with ADCE=0; p21 Fig.11 validates ADCE/AICE against synthetic true causal effects. No reliability evidence (e.g., repeated-sampling consistency) is reported. | 有操纵检验和合成数据效度验证，但缺少信度证据与多操作化会聚证据，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p7–8 lists the five benchmark sources and 12 models from four families; p9–10 discusses task complexity and model-type differences. No explicit sampling frame/representativeness statement, no formal cross-sample replication, and no clearly delimited generalization boundaries. | 报告了样本（模型/数据集）来源与特征，但未明确推广边界条件或跨情境复现结果，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p20 Alg.1 aggregates ADCE per model/task over correctly answered samples; p7–8 describes models and tasks as analysis units. No multilevel model explicitly separates sample/task/model variance. | 说明了处理发生在样本级、分析在模型×任务聚合级，但没有显式多层模型处理嵌套结构，故为 0.5。 |
| G2 | 随机效应 | NA | — | 研究推断的是固定的一组具体模型，不使用混合模型，也没有将模型/任务作为随机效应进行总体推广的需求；故 NA。 |
| G3 | 材料作为随机效应 | 0 | p7–8 uses fixed benchmark items and aggregates ADCE over items; p20 Alg.1 does not include item random effects or quasi-F statistics. No item-level random-effect modeling is reported. | 材料/题目被视为固定 benchmark 项目，未在分析中考虑项目随机效应，故为 0。 |
| G4 | 统计功效 | 0 | Full text contains no a priori power analysis, no target effect size justification, and no confidence intervals for ADCE/AICE comparisons. | 无任何事前功效分析或样本量论证，也未报告效应量置信区间，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p20 Alg.1 and p23 Appendix F.1.2 report that only correctly answered samples are used for intervention and give intervention sample counts; no full list of all measured DVs/conditions, no stopping/optional-stopping disclosure, and no confirmatory/exploratory distinction. | 报告了关键数据选择规则（仅正确样本）和部分样本量，但未完整报告全部因变量/条件、样本量决定方式及验证/探索性区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement, registry link, or timestamped analysis plan appears in the paper. | 无预注册，也未区分预注册验证性分析与事后探索性分析，故为 0。 |
| J1 | 位置偏差 | 0 | p7–8 and p25–27: CommonsenseQA is a multiple-choice task, but option position is not randomized or counterbalanced, and no position-flip/accuracy-by-position analysis is reported. | 涉及 LLM 在多选项任务中的选择，但未对候选位置做任何反平衡/随机化，故为 0。 |
| J2 | 冗长偏差 | NA | — | 研究不使用 LLM 作为裁判来比较开放式生成质量，也不涉及答案长度与质量混淆的评估，故 NA。 |
| J3 | 谄媚 | NA | — | 任务为无用户立场输入的单轮客观答题，不存在用户先验立场操纵或谄媚风险，故 NA。 |
| J4 | 自我偏好 | NA | — | 研究不使用 LLM-as-judge 或成对模型输出比较，评估基于可机器判定的答案改变/准确率，故 NA。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p26–27 Appendix G.2 and Tables 7–8 describe ICL/FTICL with two in-context examples, but do not report example source, class proportion, order counterbalancing, or multi-seed resampling. | 附录的 ICL 实验使用了 two-shot 示例，报告了数量但缺示例来源、比例、排列控制与多 seed 重采样，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p25 Table 4 and p26 Tables 6–7 provide prompt templates; p25–27 gives some prompt wording. No prompt version number, iteration date, sensitivity ablation, or dev/test split is reported. | 提供了 prompt 模板，但未做版本化、敏感性消融或说明 dev/test 划分，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验上下文为短题目/短选项，远低于长上下文窗口，且无 RAG 或长文档设置，故 NA。 |
| J8 | 温度与采样随机性 | 0 | Full text reports no temperature, top-p, top-k, repetition penalty, random seed, repeated sampling N, or API snapshot date. | 完全未报告解码采样超参、随机种子或重复运行，故为 0。 |
| J9 | 重复与文本退化 | NA | — | 任务为短答案/选项输出，不涉及开放式长文本生成退化问题，故 NA。 |
| J10 | 分词效应 | NA | — | 研究为单语言（英语）单脚本评估，无跨语言/跨脚本比较，故 NA。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p7–8 uses public benchmarks (2-Digit Multiplication, GSM8k, Word Unscrambling, Analytic Entailment, CommonsenseQA) but does not report test-set version vs. model training cutoff or any contamination detection. | 使用公开基准但未做污染检查或训练截止日期对照，故为 0。 |
| J12 | 基准饱和 | 0 | p8 Fig.5 shows some models/tasks with high accuracy near 1.0, but the paper does not discuss benchmark saturation or switch to continuous indicators for near-ceiling cells. | 未评估基准饱和问题，也未在接近天花板时改用连续指标或更难子集，故为 0。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循，研究没有测量指令约束满足率，故 NA。 |
| J14 | 输出格式约束 / 结构化输出 | 0 | p26 Table 5 shows prompt instructions requiring output in formats such as 'The answer is' and 'The unscrambled word is', but no format-validity rate, retry strategy, or separate format-failure vs. content-error reporting is provided. | 要求了输出格式，但未报告格式约束设置细节与格式合法率，故为 0。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/对齐或越狱评估，故 NA。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p3–4 Sec.2 defines deep/surface structure comprehension for LLMs and relates it to Chomsky's distinction; p7–10 evaluates LLMs but does not systematically compare the measured LLM construct with human same-name constructs or include human comparison data. | 明确界定了 LLM 上测量的深层/表层理解构念，但未系统论证其与人类同名构念的异同，也无人类对照实验，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p8–9 Fig.5 and Fig.6 report that ADCE increases with model scale, using a continuous ADCE metric, but do not report multi-seed curves or confidence intervals to rule out metric-induced discontinuity/emergence artifacts. | 报告了随模型规模变化的连续 ADCE 趋势，但没有多 seed/置信区间检验，也未正式讨论涌现与指标假象，故为 0.5。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对代理指标（benchmark/reward model/LLM-judge）的优化训练，故 NA。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p8 Fig.5 and p10 Fig.8 report single-point scores per model/task; model names are given without precise snapshot/API date, and no repeated-run N, confidence intervals, or paired tests are reported. | 只报告单点分数，缺重复次数、置信区间、精确 snapshot 标识和配对检验，故为 0。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮问答/干预评估，没有多轮对话历史累积，故 NA。 |

## 编码小结
论文提出了有理论意义的因果评估指标，干预生成流程与跨任务/跨模型评估较完整；但多数统计推断停留在描述性比较与回归趋势，缺少置信区间、重复采样、随机化/顺序平衡、基准污染检查和精确模型 snapshot 报告。编码中，凡是标准人类实验设计组件（被试分配、盲法、疲劳/练习等）均按 NA 处理；与 LLM 条件内比较和基准评估实际相关的顺序、采样、可复现性组件则按实际报告情况编码。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）, C7（NA→0）。
