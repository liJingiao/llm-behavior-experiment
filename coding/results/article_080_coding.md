# article_080 | Exploring LLMs’ Ability to Spontaneously and Conditionally Modify Moral Expressions through Text Manipulation | 2025

研究类型概述：LLM 行为/基准式观察操纵研究，无人类被试。研究者用 12 个开放与 abliterated LLM，对五个人工标注道德数据集做 revise/rewrite/continue 三类文本操纵，并施加 unconditioned、moral-blind、moral-informed（intensify/diminish）条件提示，在温度 0.1/1.0 下生成文本，再用 ME2-BERT 评分并计算 h-shift 与 v-shift。
- **研究构念（Construct）**：道德基础理论（Moral Foundations Theory）下的道德表达与条件性道德语言调整｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：LLM 行为/基准式观察操纵研究，无人类被试。研究者用 12 个开放与 abliterated LLM，对五个人工标注道德数据集做 revise/rewrite/continue 三类文本操纵，并施加 unconditioned、moral-blind、moral-informed（intensify/diminish）条件提示，在温度 0.1/1.0 下生成文本，再用 ME2-BERT 评分并计算 h-shift 与 v-shift。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4 'Text Modification Tasks' defines Revision/Rewriting/Continuation; p.5 Fig.1 gives RQ1/RQ2/RQ3 prompt templates; p.3 states temperatures 0.1 and 1.0. | 自变量与主要水平/提示程序有报告，但没有报告条件分配到生成实例的随机化/平衡程序，也没有操纵检验。 |
| A2 | 因变量 | 0.5 | p.6 defines v-shift and h-shift formulas with [0,1] moral scores and Kendall tau distance; p.4 Table 3 and Appendix B report ME2-BERT agreement and Cohen's κ. | 因变量指标和计分公式明确，且评分模型与人工标注一致性有报告；但 h/v-shift 的信度、抽样不确定性（CI）和天花板/地板预处理报告不足。 |
| A3 | 控制变量 | 0.5 | p.3: 'we kept parameters top_p and top_k to their default values of 1 and 50'; vLLM on 8x NVIDIA A30; Tables 1-2 list model versions; p.5 prompts fixed. | 报告了部分恒定控制（采样默认参数、推理库、硬件、模型版本），但没有系统列出所有控制变量及其控制手段。 |
| A4 | 混淆变量 | 0.5 | p.9 Limitations acknowledges human-annotation subjectivity and limited language/cultural coverage; p.2 discusses different model 'cultures' as a selection rationale. | 提到了若干潜在偏差/混淆来源，但没有系统说明控制方式，也没有对残余混淆作敏感性分析或内部效度评估。 |
| A5 | 调节变量 | 0 | p.1 hypothesis: the effect 'might be further amplified when the LLM is instructed to focus on the evidence of moral dimensions'; p.7 Table 5 compares RQ1/RQ2/RQ3 descriptively; p.12-13 Table 7 reports task-pair t-tests within prompt types, not prompt×task interaction. | 提出了条件提示会放大任务效应的调节式假设，但未报告正式交互检验、中心化/标准化或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量或中介效应分析，理论模型不包含中介链条。 |
| A7 | 操作性定义 | 1 | p.5 Fig.1 provides full prompt templates for RQ1-RQ3; p.4 defines three text modification tasks; p.6 gives exact h-shift/v-shift formulas and parameter values. | 关键自变量操纵与因变量计算均有可复现的操作化描述，包括提示、任务定义、评分模型与公式。 |
| A8 | 水平数与类型 | 0.5 | p.4 lists three task levels; p.5 Fig.1 lists unconditioned/moral-blind/moral-informed conditions; p.3 gives temperatures 0.1 and 1.0; Tables 1-2 list models. | 水平数与标签基本明确，但未说明水平类型、连续变量（如温度）的间距/中心化处理及完整设计矩阵。 |
| A9 | 单一操作化的风险 | 0.5 | p.6 uses both h-shift and v-shift; p.4 Table 3 and Appendix B compare ME2-BERT, MoralBERT, MoralStrength, DDR; p.12 Table 6 reports Cohen's κ. | 关键构念采用了多种指标和多个评分模型，但没有报告 h-shift 与 v-shift 的会聚效度或单一操作化的系统局限讨论。 |
| A10 | 单一方法的风险 | NA | — | 自变量为 LLM 文本生成，因变量由 ME2-BERT 自动评分；方法来源不同，不存在同源自评式共同方法偏差。 |
| B1 | 被试间设计 | NA | — | 没有人类被试组间分配；同一批文本/模型跨条件生成，不属于被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量及条件顺序平衡设计；各条件由独立 API 调用生成，未报告顺序或随机效应结构。 |
| B3 | 混合设计 | NA | — | 没有人类组间/组内混合设计，也没有相应的混合误差项分析。 |
| B4 | 因子设计 | 0 | p.7 Table 5 summarizes task/prompt/model means; p.12-13 Table 7 reports only task-pair paired t-tests; no full factorial design matrix, per-cell N, or interaction terms. | 存在任务、提示条件、模型、温度等多因素网格，但没有报告完整因子设计矩阵或交互项，因此未达到因子设计编码要求。 |
| B5 | 主效应 | 0.5 | p.7 Table 5 reports descriptive task/prompt/model means; p.12-13 Table 7 reports 1440 paired two-sided t-tests for task pairs at p<.05. | 任务差异有显著性检验，但只报告拒绝率/百分比，缺少 F、df、效应量和正式主效应表。 |
| B6 | 交互作用 | 0 | p.7 discusses larger RQ2/RQ3 shifts descriptively and p.12-13 Table 7 tests task pairs within prompt types; no prompt×task or model×task interaction test. | 没有正式交互项统计检验，也没有简单主效应及多重比较校正。 |
| B7 | 区组设计 | NA | — | 没有区组变量或分层随机分配程序。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；没有非随机分组、选择偏差或准实验因果推断设定。 |
| B10 | 被试内设计的适用条件 | NA | — | 不是人类被试内处理设计，不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 研究单位没有被概率分配到互斥条件；所有入选文本在模型/任务/提示条件下生成，未报告随机分配机制。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序设计，也没有各顺序被试数或迁移对称性前提。 |
| C3 | 恒定 | 0.5 | p.3 reports top_p=1, top_k=50, vLLM, 8x NVIDIA A30, Ubuntu; Tables 1-2 list model versions; p.5 fixed prompt templates. | 列出了一些恒定变量及水平，但没有系统说明这些恒定控制对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有匹配变量、配对分配或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组/协变量纳入分析；模型规模/地域等仅作描述性模型属性。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人工评分者，不涉及盲法安排。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序，无完全平衡/拉丁方/ABBA 层级需要报告。 |
| D1 | 练习效应 | NA | — | LLM 每次条件生成无上下文内学习；没有练习块或试次位置问题。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题；API/批处理生成不涉及休息间隔。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个提示为独立生成，没有跨条件清洗期或残留效应。 |
| D4 | 不对称迁移 | NA | — | 不存在同一被试跨条件的非对称迁移；独立调用无跨条件残留。 |
| D5 | 范围效应 | NA | — | 因变量为 h/v-shift 连续评分，不是被试内绝对判断或李克特量表范围效应场景。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选项、刺激序列或被试内处理顺序；每条文本由单次固定提示生成，不涉及位置/顺序偏差。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分题或默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征或事后假设推断访谈。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集与模型评分，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | NA | — | 因变量是派生连续 moral-shift 指标，并非任务难度/正确率型端点截断测量；未报告端点频率不构成典型天花板/地板问题。 |
| E7 | 共同方法偏差 | NA | — | 自变量生成与因变量自动评分来源分离，无同源自评式 CMB。 |
| F1 | 统计结论效度 | 0 | p.12-13 Appendix D reports 1440 paired two-sided t-tests at .05 and percentage of rejections; p.7 Table 5 reports means; no effect sizes, CIs, power, or multiple-comparison correction. | 仅报告显著性/拒绝率与均值，缺少效应量、置信区间、样本量确定依据及多重性校正，且 1440 次检验未校正。 |
| F2 | 内部效度 | 0.5 | p.4 selects instances perfectly matched by ME2-BERT (100% agreement); p.12-13 uses paired t-tests on same text instances; no randomization/allocation concealment or attrition/flow discussion. | 同一文本跨任务配对比较与匹配选择提供一定控制，但没有随机分配、分配隐藏或系统内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | p.4 Table 3 reports ME2-BERT matchings with human annotations; p.12 Table 6 reports Cohen's κ against other scoring models; RQ0 awareness is not a manipulation check. | 评分模型的效度/一致性有证据，但缺少对文本操纵成功的操纵检验，且对 h/v-shift 构念效度讨论有限。 |
| F4 | 外部效度 | 0.5 | p.3 Tables 1-2 describe model sources, sizes and geographic coverage; p.9 Limitations discusses language/cultural coverage; Appendix I adds a GPT-4o check. | 样本来源和边界条件有所讨论，但没有系统跨样本/跨情境复现，模型与数据集代表性仍有限。 |
| G1 | 分析单位 | 0.5 | p.12 Appendix D: shift values retrieved per dataset/task/model and paired t-tests over all instances; no multilevel model or explicit nesting correction for texts within datasets/models. | 分析在生成实例层级进行并做任务配对，但没有显式说明处理/分析层级匹配，也未用多层模型处理嵌套。 |
| G2 | 随机效应 | NA | — | 无人类被试随机效应；12 个模型作为固定比较组，研究不建立 subject 随机截距/斜率模型。 |
| G3 | 材料作为随机效应 | 0.5 | p.4 uses 20,980 text instances from five datasets; p.7 Table 5 averages over datasets; no item/dataset random effects are reported. | 材料/数据集被用于多条文本并跨数据集汇总，但分析未把项目/数据集作为随机效应，推广到材料总体的不确定性未建模。 |
| G4 | 统计功效 | 0 | No power analysis is reported; p.7 Table 5 and p.12-13 Table 7 report no effect sizes or confidence intervals. | 缺少事前功效分析、目标效应量、样本量/重复次数论证，也未报告效应量及 CI。 |
| G5 | 研究者自由度 | 0.5 | p.4 describes selection of 20,980 perfectly matched instances; Appendix A gives preprocessing; p.8 reports refusal rates; no explicit stopping rule or confirmatory/exploratory distinction. | 数据选择、预处理与拒绝率有报告，但未完整说明样本量决定方式、全部事后分析及探索性/验证性区分。 |
| G6 | 预先设定 / 预注册 | 0 | No pre-registration platform, identifier, or time-stamped analysis plan is reported in the paper. | 无预注册；论文属于事后报告的分析流程。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较，无候选位置偏差。 |
| J2 | 冗长偏差 | 0 | p.5 prompt says 'Do not add any other text or comment'; no output length distribution, length-score correlation, or length control is reported despite continuation generating new text. | 开放性生成任务可能因 revise/rewrite/continue 长度不同影响 moral score，但论文未报告或控制长度偏差。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或多轮纠错设置，不涉及谄媚偏差。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge；ME2-BERT 是道德基础分类/评分模型，不是被评模型同源生成裁判。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.5 Fig.1 prompts are zero-shot instruction templates; no few-shot in-context examples are used. | 无 few-shot 示例选择、标签比例或排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5 Fig.1 and p.12 Fig.6 provide full prompt templates; no prompt version/iteration, semantic-equivalence sensitivity ablation, or dev/test split is reported. | 完整模板已公布，但缺少提示版本管理、敏感性消融和测试集调参隔离说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 输入为短文本/句子级道德文本，无长文档、RAG 或长上下文信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.3 reports temperature 0.1 and 1.0, top_p=1, top_k=50; no seed, repeated-sampling N, or confidence intervals are reported. | 主要采样超参有报告，但缺少随机种子、每条件重复采样次数与不确定性估计。 |
| J9 | 重复与文本退化 | 0.5 | p.3 reports vLLM inference and sampling parameters; no repetition penalty, n-gram repetition/degeneration rate, max generation length, or truncation rate is reported. | 解码设置部分报告，但未把重复/退化作为质控指标，也未报告生成长度上限。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文数据集与英文提示，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.3 lists five public human-annotated datasets and says models were accessed on HuggingFace at end of 2024; no contamination/overlap check or per-model training cutoff is reported. | 公开数据集与模型访问时间有交代，但没有训练数据重叠检测或污染率评估。 |
| J12 | 基准饱和 | NA | — | 不是准确率基准饱和评估；研究测量 moral-shift 而非基准分数上限。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；p.5 only mentions semi-automatic checking of extra comments, not instruction-following accuracy. |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/JSON/文法约束输出，自由文本生成无需格式合法率编码。 |
| J15 | 越狱稳健性 | NA | — | 不是安全/越狱评估；p.8 refusal rate is incidental, not an adversarial attack ASR evaluation. |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 RQ0 asks whether LLMs are 'aware of a psychological conceptualization' of MFT; p.9 Limitations notes open questions about MFT and machine-based analyses; no systematic LLM-human construct equivalence test. | 论文明确以心理学 MFT 构念研究 LLM 行为，但对 LLM 道德表达与人类同名构念的异同仅有限讨论，未做同范式人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的涌现能力曲线，也无'涌现/突变'宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标/奖励模型的优化或 overoptimization 监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.2 provides a resources link; p.3 and Tables 1-2 give model names/versions; p.12-13 reports paired t-tests; no repeated-sampling N, 95% CI, exact commit hashes, or raw logs are reported. | 模型版本与部分可复现资源有报告并做了配对检验，但缺少重复采样不确定性、精确 snapshot 和完整日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示生成，无多轮对话历史累积，也不主张多轮部署外推。 |

## 编码小结
论文对提示模板、任务类型、模型版本、评分模型选择与 h/v-shift 定义报告较充分，但整体属于观察性 LLM 行为比较而非随机化实验：缺少条件分配/顺序随机化、操纵检验、完整因子交互分析、效应量与置信区间、多重比较校正、混合效应/项目随机效应建模，以及对输出长度和训练数据污染的控制。大量人类被试特有的设计/质控组件不适用；与 LLM 评估相关的 J2、J6、J8、J9、J11、J16、J19 存在部分报告但关键信息不足。
