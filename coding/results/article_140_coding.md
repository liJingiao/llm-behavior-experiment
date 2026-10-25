# article_140 | Uncertainty of Thoughts: Uncertainty-Aware Planning Enhances Information Seeking in LLMs | 2024

研究类型概述：这是一项 LLM 算法与基准评测研究：提出 UoT 规划方法来改善 LLM 的主动信息寻求提问，在 20 Questions、医学诊断和故障排查三类任务、五个数据集上比较 UoT 与 Direct Prompting、CoT、ToT 等方法；分析单位是任务案例/对话，指标为成功率 SR、成功案例平均对话轮数 MSC 和平均对话轮数 MCL。无人类被试，不测量心理学构念。
- **研究构念（Construct）**：不确定情境中的主动信息寻求与问题选择效率｜CA 构念锚定：计划（planning, `trm_4a3fd79d0acc1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：在医疗诊断、故障排查和20 Questions中，让现成LLM生成候选问题与未来回答，依据剩余候选不确定性计算奖励并树搜索选择下一问，与直接提示、CoT和ToT比较。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p7 §3.1: 'We test various LLMs... Baselines Direct Prompting (DP)... UoT...'; p8 Table 1 reports methods/models/datasets/open-closed settings. | 明确命名并报告了方法自变量及多个水平/标签，也详细描述了 UoT 操作流程；但未报告随机分配到条件、分配隐藏或操纵检验，故为 0.5。 |
| A2 | 因变量 | 0.5 | p7: 'Success Rate (%): SR = S/T... Mean Conversation Length... MSC = Rs/S... MCL = R/T'; p8 Table 1 uses SR/MSC/MCL. | 因变量指标与计分公式明确；但无信度/效度证据，也未说明连续指标预处理或端点/天花板地板效应处理，故 0.5。 |
| A3 | 控制变量 | 0.5 | p7: answerer 'simulated by GPT-4'; maximal turns set to 20/5; p19: temperature 0.7 for ToT/CoT-SC; p21: simulation steps=3, m=3, λ=0.4. | 报告了若干被恒定的设置（答案者、最大轮数、部分超参），但没有系统列出控制变量清单并逐一说明控制手段，故 0.5。 |
| A4 | 混淆变量 | 0.5 | p9 §3.3.1 compares at equal token cost by Pruned UoT and Adapted-ToT D=4; p10 limitation: 'simplified scenario' and overlapping possibility sets. | 识别了计算成本与场景简化等潜在混淆并做了部分控制，但未系统说明残余混淆或敏感性分析，故 0.5。 |
| A5 | 调节变量 | NA | — | 论文理论模型不含调节变量，也未做调节/交互假设检验；不适用。 |
| A6 | 中介变量 | NA | — | 论文理论模型不含中介变量，也未做直接/间接效应分解；不适用。 |
| A7 | 操作性定义 | 1 | p2-6 §2.1-2.6: possibility space Ω, question generation, simulation tree, entropy reward Eq.10, reward propagation; p7 metrics formulas; p22-27 full prompts. | 关键构念（信息寻求方法、成功率与效率）给出了可复现的算法步骤、指标公式和完整提示词模板。 |
| A8 | 水平数与类型 | 0.5 | p7 §3.1 lists DP, PP, CoT, CoT-SC, Reflexion, Original/Adapted-ToT, UoT, open/closed; p8 Table 1. | 各方法水平数与标签明确，但未说明水平类型、间距或全距；连续入回归的中心化问题不适用，故 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p7-9: three scenarios and five datasets; p8 Table 1 and p9 Figure 3/4 report consistent comparisons. | 在多个任务/数据集上评估，具有跨任务一致性证据；但未正式报告多操作化会聚统计，单一操作化局限讨论有限，故 0.5。 |
| A10 | 单一方法的风险 | NA | — | 自变量为提示/算法，因变量为客观成功率/轮数，不存在自陈量表同源问题；共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试，也不是将被试独立分配到组间条件的实验；任务案例层面为基准评测，不适用被试间设计。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量设计；多轮对话内的条件顺序不是被试内实验顺序，也无被试顺序平衡。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素混合的人类实验设计，故不适用。 |
| B4 | 因子设计 | 0 | p8 Table 1 reports model × method × dataset comparisons; p18 Tables 7-8 only report DP vs UoT t-tests, without full design matrix or interaction terms. | 存在多因素比较，但非完整交叉设计，未报告交互项和完整设计矩阵/每格样本量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | p8 Table 1 reports method main comparisons; p18 Tables 7-8 report DP vs UoT t-tests and p-values. | 报告了主要方法比较及 t 检验，但无 F/df/效应量，也未在交互显著时说明主效应解释限制，故 0.5。 |
| B6 | 交互作用 | 0 | p8-9 and p18 report no interaction tests; only pairwise DP vs UoT comparisons appear. | 跨模型/数据集比较却完全未报告交互项统计检验，多因素下忽略交互，故为 0。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计，故不适用。 |
| B8 | 拉丁方 | NA | — | 无人类被试内拉丁方顺序安排，故不适用。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；属于 LLM 算法基准评测。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理可逆性/迁移对称性设计，故不适用。 |
| C1 | 随机化 | NA | — | 研究单位未随机分配到互斥条件；各方法是在同一基准案例上独立运行/比较，无随机分配与分配隐藏。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，因此无顺序平衡方案；不适用。 |
| C3 | 恒定 | 0.5 | p7: answerer 'simulated by GPT-4', max turns 20/5; p21: simulation steps=3, m=3, λ=0.4; p10 discusses simplified scenarios. | 列出了若干恒定设置并简要讨论场景简化限制，但未系统列出所有恒定变量及水平、也未充分讨论外部效度限制，故 0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配设计；不适用。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组/协变量纳入分析模型；模型/数据集仅做分层展示，不构成 ANCOVA 或协变量控制。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者盲法安排；GPT-4 作为答案者模拟器不是盲法实验对象。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级，故不适用。 |
| D1 | 练习效应 | NA | — | 无人类练习效应或跨条件学习问题；每段对话为独立 LLM 交互。 |
| D2 | 疲劳效应 | NA | — | 无人类疲劳效应；不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无药物/学习残留式跨条件迁移；各案例/方法为独立运行，无需清洗期。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移检验需求；不适用。 |
| D5 | 范围效应 | NA | — | 因变量为客观成功率/轮数，不是主观量表绝对判断，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选项/刺激顺序的被试内呈现实验；候选问题由期望奖励选择，未做位置顺序实验。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表或跨群体反应风格比较；不适用。 |
| E4 | 需求特征 | NA | — | 无人类被试，故无人类需求特征/事后访谈检查；不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集主要由 LLM/API 自动完成，无人类主试或评分者期望效应；不适用。 |
| E6 | 天花板 / 地板效应 | 0 | p8 Table 1 reports only SR/MSC/MCL percentages; e.g., DX UoT 97.0/92.1. No SD, endpoint frequencies, or pilot difficulty calibration are reported. | 成功率有上界且部分结果接近天花板，但仅报告均值/百分比，无分布、端点频率或任务难度校准，故为 0。 |
| E7 | 共同方法偏差 | NA | — | 自变量/因变量不是同源自评多构念测量，共同方法偏差问题不适用。 |
| F1 | 统计结论效度 | 0 | p8 Table 1 reports SR/MSC/MCL means; p18 Tables 7-8 report t and p values, but no effect sizes or confidence intervals; no multiplicity correction. | 统计结论主要基于均值和 p 值，未报告效应量/CI、多重性校正或样本量功效依据，故为 0。 |
| F2 | 内部效度 | 0.5 | p7 uses same datasets, GPT-4 answerer and fixed max turns; p18 reports t-tests. No randomization/allocation concealment, baseline equivalence, or attrition/flow reporting. | 比较使用同一数据集与答案者有基本控制，但无随机分配、分配隐藏、基线等价检验或损耗处理说明，故 0.5。 |
| F3 | 构念效度 | 0.5 | p9: 'GPT-4’s accuracy as answerer is evaluated by analyzing 10% of interactions'; p17 Table 6 reports Judgment 100 and IF 92.9-94.4. | 报告了 GPT-4 答案者的可靠性检查；但主要成功指标本身无信效度证据，也无方法操纵检验，故 0.5。 |
| F4 | 外部效度 | 0.5 | p7-8 reports dataset sources and sizes (Common 111, Things 1854, MedDG 500, FloDial 153 faults); p10 discusses simplified scenarios as limitation. | 报告了数据集来源、规模和部分推广边界；但未报告跨样本/跨情境复现或代表性抽样，故 0.5。 |
| G1 | 分析单位 | 0.5 | p7 defines SR=S/T, MSC, MCL; p8 Table 1 aggregates per dataset/model/method. Multi-turn dialogue is nested within cases, but no explicit analysis-level discussion. | 分析单位为案例/对话，处理也在案例层；但未明确讨论轮次嵌套对话、案例嵌套数据集的聚类结构及相应分析层级，故 0.5。 |
| G2 | 随机效应 | NA | — | 未使用混合模型或随机效应；模型和数据集被作为固定基准单位，不涉及随机效应推广。 |
| G3 | 材料作为随机效应 | NA | — | 材料/项目不是作为自变量的有限刺激集；研究为案例级方法评测，不涉及把材料作为随机效应推广到材料总体的设计。 |
| G4 | 统计功效 | 0 | p7-8 report dataset sizes but no power analysis; p18 reports p-values without effect sizes or confidence intervals. | 无事前功效分析或样本量论证，结果未报告效应量/CI，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p7-8 reports main datasets and metrics; p20 describes MedDG selection of 500; p21 reports hyperparameters. No full trial exclusion counts, stopping rules, or confirmatory/exploratory labels. | 报告了数据集构建与主要指标，但未完整报告试次剔除、停止规则、样本量追加/停止方式及验证性与探索性分析区分，故 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p1 and p28-35 checklist contain no preregistration or analysis-plan registration. | 无公开预注册或分析计划，故为 0。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM-as-judge 的多候选项排序/成对比较；候选问题由期望奖励选择，未做位置反平衡实验。 |
| J2 | 冗长偏差 | NA | — | 评估指标为成功率/轮数，不使用 LLM 裁判给开放生成质量打分；长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 任务中没有用户先验立场、反馈或纠错式对话操纵，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | GPT-4 用作答案者/环境模拟器，不是 LLM-as-judge 评估生成质量；不涉及裁判自我偏好。 |
| J5 | 少样本示例选择与排列偏差 | NA | p22-27 提示词均为 zero-shot 指令，无 few-shot 示例。 | 实验为零样本提示，无 in-context few-shot 示例选择或排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p22-27 provide full prompt templates for DP, Planning, UoT, CoT, ToT, answerer; no prompt versioning, sensitivity ablation, or dev/test split is reported. | 提供了完整提示词模板，但无版本号、语义等价措辞敏感性消融或 dev/test 划分，故 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG 设置；不适用。 |
| J8 | 温度与采样随机性 | 0.5 | p19: temperature 0.7 for CoT-SC/ToT; p21: simulation steps=3, m=3, λ=0.4; no random seeds or repeated-sample CIs are reported. | 报告了部分采样超参与重复/计算设置，但无 seed、每条件重复 N 与 95% CI，故 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p19 reports temperature settings for some baselines; p21 reports implementation hyperparameters. No decoding strategy, repetition rate, or degeneration QC is reported. | 有部分温度/实现设置，但未系统报告解码策略、重复率/退化率，也未证明各条件解码策略严格恒定，故 0.5。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言任务，无跨语言/跨脚本分词比较；不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p7-8 use public benchmarks such as Things, DX, MedDG, and FloDial; no training cutoff or contamination check is reported. | 使用公开基准且未报告模型训练截止日期、数据重叠或污染检测，无法排除记忆复现，故为 0。 |
| J12 | 基准饱和 | 0.5 | p8 Table 1 reports benchmark scores and SOTA-like comparisons; DX reaches 97.0/92.1. No continuous metric, held-out harder subset, or saturation discussion is provided. | 报告了分数量程和当前水位，但接近天花板时未改用连续指标或更难子集，也未做 CI 比较，故 0.5。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循准确率；任务为信息寻求成功率与效率，不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p22-27 prompts impose output forms such as 'Question 1: Is X ...? YES: ... Count of YES: ...'; no format-validity rate or separate format-failure reporting is given. | 存在格式约束与解析需求，报告了模板，但未报告格式合法率，也未将格式失败与内容错误分开报告，故 0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/对齐、越狱或有害请求评估；不适用。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究为纯工程/应用能力评测，不主张测量人类心理学构念；不适用 LLM 心理学被试定位。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随模型规模/训练进展的涌现能力曲线；不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及以 benchmark/奖励模型/LLM-judge 为优化目标的训练或 best-of-N 过优化监控；不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p1 provides code link; p7 names models (GPT-4, Gemini-1.5-Pro, Claude-3-Opus, Llama-3-70B-Instruct, Mistral-Large); p18 reports t-tests but no precise snapshots, repeated-run CIs, or paired tests. | 提供代码/数据并报告部分检验，但模型 snapshot 不精确、无重复 N/CI/配对检验细节，故 0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p2-3 formulate multi-turn Questioner-Answerer interaction; p7 sets max turns 20/5; p8 reports MSC/MCL final success and conversation length. | 确实进行了多轮任务并报告最终成功率与轮数，但未按轮次拆分一致性/衰减，也未说明上下文截断处理，故 0.5。 |

## 编码小结
论文对 UoT 算法、提示词、任务和主要指标的界定较清楚，也提供了代码与部分显著性检验；但统计推断以成功率均值与 t 检验为主，缺少效应量、置信区间、预注册、功效分析、模型 snapshot 与污染/饱和/项目泛化等系统报告。大量人类被试实验设计组件不适用于该 LLM 基准评测。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
