# article_147 | SteerConf: Steering LLMs for Confidence Elicitation | 2025

研究类型概述：方法/基准评测论文：提出 SteerConf，通过不同 steering 提示、置信一致性度量与线性量化来改进 LLM 言语化置信校准；在 7 个基准、多个 LLM（GPT-3.5、LLaMA3、GPT-4，附小模型 Qwen3-1.7b）上做零样本评测、基线比较与消融。无人类被试，分析单位为每个问题上的 LLM 输出及其聚合指标；主要比较方法、模型、数据集与 CoT 条件。
- **研究构念（Construct）**：言语化置信判断、过度自信与元认知校准｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：在七个知识、常识、伦理和推理任务中要求GPT-3.5、LLaMA3和GPT-4同时作答并报告置信度，以保守到乐观的多级steering prompt重复询问，再按回答一致性聚合。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.7: we employ five steering levels: {very cautious, cautious, vanilla, confident, very confident}; p.60-61 give full prompts; p.88 Table 5 reports steering effects. | 自变量被明确命名并给出 5 个水平及提示文本，但未明确说明单位如何分配到水平、是否随机化；steering 效果只是描述性证据，未作为正式 manipulation check 程序报告，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.9: metrics ECE, AUROC, PR-P, PR-N; Appendix A p.59 gives formulas; p.9 tables report point estimates. | 因变量指标与计分方式明确，但未报告信度/效度证据，也没有连续指标的 CI、预处理或防天花板/地板说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.9: LLaMA3 70B with 4-bit quantization; GPT-3.5 and GPT-4; same datasets and CoT conditions used across comparisons. | 报告了部分保持恒定的条件（模型、数据集、CoT/非 CoT、提示模板），但没有系统列出控制变量清单及逐项控制手段，故为 0.5。 |
| A4 | 混淆变量 | 0 | p.48 limitations mention manual prompt design, query cost, and open-ended tasks, but no discussion of confounds or residual confounding. | 未系统识别潜在混淆（如调用次数、提示长度、答案选择规则、模型准确率差异）及其控制方式，也未讨论残余威胁。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量理论模型或交互检验，不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解，不适用。 |
| A7 | 操作性定义 | 1 | p.6-8: equations for mean confidence, confidence consistency, answer consistency, calibrated confidence and linear quantization; p.60-61 full prompts. | 核心构念均有可复现操作化：steering 提示、置信抽取、一致性公式、校准与答案选择规则均写出。 |
| A8 | 水平数与类型 | 0.5 | p.7: l in {-ell,...,ell}, ell=2, five levels from very cautious to very confident; labels and order described. | 报告了水平数与标签，并暗示有序水平，但没有明确说明水平类型、间距/全距或连续处理方式，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.9 uses ECE, AUROC, PR-N, PR-P and accuracy; p.31/p.87 confidence histograms; p.88 Table 5 steering effects. | 对校准/失败预测使用多个指标，但没有报告各指标间的会聚证据；同时对任务范围限制仅在 p.48 讨论，故为 0.5。 |
| A10 | 单一方法的风险 | NA | — | 自变量是提示/方法条件，因变量是基于答案正确性的客观校准指标，不存在人类自陈式同源共同方法偏差问题，不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试组间分配；同一问题在多个 steering 水平/方法下被评估，不是独立被试组设计。 |
| B2 | 被试内设计 | 0.5 | p.6-7: for each question we apply 2ell+1 steering levels and generate 2ell+1 prediction-confidence pairs. | 存在同一问题内的重复提示/重复测量结构，但没有报告条件顺序处理、平衡方案，也未在统计模型中将被试/问题作为随机效应，故为 0.5。 |
| B3 | 混合设计 | NA | — | 没有逐因素标注组间/组内的混合实验设计；模型与数据集是评测分层，不是人类被试混合设计。 |
| B4 | 因子设计 | NA | — | 没有完整因子设计矩阵、每格样本量与交互分析；多模型/多数据集属于基准评测分层而非正式因子实验。 |
| B5 | 主效应 | NA | — | 无因子设计中的主效应检验，不适用。 |
| B6 | 交互作用 | NA | — | 无正式交互项检验与简单主效应分析，不适用。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计及区内随机分配。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 非准实验设计，无不可随机分配的人类被试分组。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，且 LLM 各提示调用无不可逆后效问题，不适用。 |
| C1 | 随机化 | NA | — | 同一问题被所有方法和 steering 水平评估，不存在将独立单位随机分配到互斥条件的程序。 |
| C2 | 平衡 | NA | — | 无需要平衡的人类被试条件顺序；各 steering 提示是独立 LLM 调用，未设计顺序效应平衡。 |
| C3 | 恒定 | 0.5 | p.9 reports model versions and LLaMA3 70B 4-bit quantization; p.60-61 fixes prompt templates and CoT/non-CoT variants. | 列出了一些恒定条件（模型、量化、提示、CoT 条件），但没有完整报告恒定变量水平及其对外部效度的限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人工评分者，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 顺序平衡设计。 |
| D1 | 练习效应 | NA | — | LLM 各提示调用独立，无人类或上下文内练习效应；不适用。 |
| D2 | 疲劳效应 | NA | — | 无人类长 session 或疲劳风险；不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立 LLM 会话/调用，无跨条件残留或清洗期需求。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或不对称迁移检验需求。 |
| D5 | 范围效应 | NA | — | 无人类被试内绝对判断/量表评分任务，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p.9: Law and Ethics are MMLU multiple-choice benchmarks; no report of answer-option order randomization or counterbalancing. | 涉及多项选择选项与固定 steering 提示序列，但未报告选项/刺激顺序的随机化或反平衡，也未讨论顺序效应。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表自陈及跨群体反应风格比较；置信直方图不是该类反应倾向分析。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | 自动调用 LLM 评测，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.4 Figure 1 notes vanilla 100% confidence but only 50% accuracy; p.31 Figure 3 confidence histograms; p.9 accuracy tables. | 报告了置信分布/端点现象与部分准确率，但没有系统报告均值、SD、偏度、端点频率，也未说明 pilot 难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量，不适用。 |
| F1 | 统计结论效度 | 0 | p.54 NeurIPS checklist Q7: Experiment statistical significance Answer: No; tables p.9-10 report only point estimates. | 没有误差棒、置信区间、显著性检验或多重性校正，也没有样本量/功效依据；仅报告点估计并宣称显著优于基线。 |
| F2 | 内部效度 | NA | — | 无人类随机分配、分配隐藏、被试流向与损耗；方法比较在同一基准题目上自动进行，这些内部效度程序不适用。 |
| F3 | 构念效度 | 0.5 | p.88 Table 5 and p.87 Figure 5 show steering effects; p.60-61 prompts and p.59 metric formulas; p.48 acknowledges limited task scope. | 有 steering 效果检查和指标操作化，但没有报告 ECE/AUROC 等测量的信度/效度证据，也几乎没有单一操作化局限的系统讨论，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.9 reports seven benchmarks and three main model families; p.48 limits to numerical/multiple-choice tasks and future open-ended extension. | 报告了评测数据集与模型来源，并给出部分边界条件；但没有代表性抽样框或跨样本/跨情境复现实验，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p.9: metrics computed on benchmark datasets and aggregated per model/dataset; no multi-level model or item clustering correction reported. | 说明了评测层级（问题输出聚合到数据集/模型），但没有讨论题目嵌套于数据集、重复调用嵌套于问题等结构，故为 0.5。 |
| G2 | 随机效应 | NA | — | 未使用含随机效应的统计模型；模型与数据集作为固定评测对象，论文不据此做需随机效应建模的总体推断。 |
| G3 | 材料作为随机效应 | NA | — | 自变量载体是 steering 提示而非有限材料抽样，未做以项目和被试同时为随机因子的分析；不适用。 |
| G4 | 统计功效 | 0 | p.54 checklist Q7 says no statistical significance/error bars; no power analysis reported. | 无事前功效分析，也未报告效应量置信区间；仅有点估计，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p.9-10 and p.88-90 report many benchmarks/metrics and ablations; no explicit trial exclusion rules, stopping rules, or confirmatory/exploratory distinction. | 主要因变量、数据集和消融条件报告较全，但缺少数据排除规则、试次/样本量决定方式及探索性/验证性区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.52-58 NeurIPS checklist contains no preregistration; no registration number or link in the paper. | 无预注册，未登记假设、分析计划、排除规则或停止规则。 |
| J1 | 位置偏差 | 0 | p.9 Law and Ethics are MMLU multiple-choice; no mention of answer-option position randomization or A/B swapping. | 实验涉及多项选择作答，但完全未报告选项位置随机化/反平衡或位置偏差检验，故为 0。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放生成质量，也不比较回答长度与得分，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户立场、反馈或对话式纠错操纵，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 裁判或成对比较评估模型输出，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 提示为零样本 steering prompt，不使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.60-61 publishes full prompt templates; p.89 Table 7 compares original vs brief steering prompts; p.48 notes manual prompt design. | 提供了完整模板并做了一种措辞变体的稳健性检查，但没有版本日期、dev/test 分离或系统 prompt 搜索过程，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG 设置，输入为短基准问题。 |
| J8 | 温度与采样随机性 | 0 | p.9-10 describe multiple samples and M=5 for some baselines, but no temperature, top-p, seed, or API snapshot reported; p.54 Q7 says no error bars. | 未报告采样超参（至少 temperature）与随机种子，也没有重复采样的 CI 或调用日期/snapshot，故为 0。 |
| J9 | 重复与文本退化 | NA | — | 主要输出是短答案加置信分数/简要 CoT，不评估开放文本质量或重复退化，解码退化指标不适用。 |
| J10 | 分词效应 | NA | — | 单语言英文基准，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.9 lists public benchmarks GSM8K, MMLU, BigBench etc. and GPT-3.5/4; no training cutoff comparison or contamination detection. | 使用公开基准和闭源模型，但未报告训练截止日期、测试集版本对照、n-gram/DCQ 污染检测或污染率。 |
| J12 | 基准饱和 | 0.5 | p.9-10 and p.89-90 report metric values on benchmark datasets; main metrics ECE/AUROC are continuous, but no SOTA position or bootstrap CI comparison. | 使用连续校准指标而非仅 accuracy，降低饱和风险；但没有评估基准饱和与 SOTA 位置，也未做 CI 比较，故为 0.5。 |
| J13 | 指令遵循 | NA | — | 指令遵循不是因变量；p.60 only discusses format-following as a prerequisite, not measured by machine-verifiable constraints. |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.60-61 specify fixed answer-confidence output format; p.60 notes formatting failures but reports no legal-format rate or retry policy. | 报告了格式约束设置并承认格式失败，但没有报告格式合法率、重试策略，也未把格式失败与内容错误分列，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 and p.5 frame LLM overconfidence/calibration; p.9 compares models, but no human baseline or systematic human-LLM construct comparison. | 论文把 LLM 的 overconfidence/calibration 当作构念，但没有系统论证其与人类元认知/置信判断的异同，也无人类同范式对照，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随规模/训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标的训练优化、RL 或 best-of-N 过优化监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.54 Q7 says no error bars/statistical tests; p.9 names GPT-3.5, GPT-4, LLaMA3 without precise snapshot/date; no repeated-seed CI. | 未报告重复次数、置信区间、精确 snapshot、配对检验或推理日志，评估可复现性不足，故为 0。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮问题作答，无多轮对话历史累积。 |

## 编码小结
该文不是传统心理实验，人类被试设计组件多数为 NA。方法化的提示操纵与公式定义较完整，但统计推断、采样超参/重复、基准污染、评估可复现性以及部分位置/格式控制报告不足。置信校准是核心因变量，但信效度证据、置信区间与随机效应结构缺失。
