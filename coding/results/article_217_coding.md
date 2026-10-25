# article_217 | Advancing Spatial Reasoning in Large Language Models: An In-Depth Evaluation and Enhancement Using the StepGame Benchmark | 2024

研究类型概述：该文是面向 StepGame 基准的 LLM 空间推理评测与基准修正研究：先识别并修正 StepGame 模板错误，再比较不同 GPT 模型在 base、CoT、ToT、不同 few-shot 集与不同测试集规模下的准确率，并提出模板映射+ASP 的规则化解法。研究对象是 LLM 输出与测试样例，不是人类被试；分析单位主要是模型-条件-测试样例层面的准确率。
- **研究构念（Construct）**：空间关系表征、多跳关系组合与干扰下的推理负荷｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：在修正模板错误的StepGame上，让现成GPT模型从自然语言空间关系链推断两个实体的方向，并比较跳数、噪声、few-shot、CoT和ToT。（操纵跳数、噪声、模型、示例数量和基础/CoT/ToT提示。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5 p.5: Different Few-Shot Sets: clean 5shot(1,3,5,7,10), clean 10shot, clean 5shot separate; p.7 p.7 Table 4: base/CoT/ToT conditions. | 提示策略与 few-shot 设置被明确命名并给出水平/取值，但未报告操纵检验、正式分配或随机化程序，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.7 p.7 Table 4: Accuracy comparison of GPT models on revised StepGame using different methods; accuracy scores with higher values better. | 因变量为准确率/错误数，指标与计分方式基本明确；但无信度、效度、连续指标预处理或天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | p.5 p.5: temperature to 0 in CoT experiments; ToT temperature 0.7; remaining parameters left at standard configurations for these models. | 报告了温度与标准参数等控制手段，但未系统列出全部控制变量清单及对应控制方式。 |
| A4 | 混淆变量 | 0.5 | p.1 p.1: template errors in the benchmark has an impact on the evaluation results; p.6 p.6: limited number of test examples could introduce biases or inaccurate estimations. | 识别了基准模板错误与测试集规模偏差等潜在混淆，并通过修正数据和增大测试集缓解；但未系统讨论残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量假设与乘积项交互检验；模型、hop、few-shot 等差异仅为描述性比较，故不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或因果链中介假设，故不适用。 |
| A7 | 操作性定义 | 0.5 | p.4-5 p.4 p.5: template-to-relation mapping + ASP rules; CoT thought types clink/camap/ccalcu; ToT Algorithm 1 with state generation and evaluation prompts. | 关键任务与提示策略给出了较具体的操作程序，但完整 prompt 模板主要指向附录/代码，正文复现信息不完整。 |
| A8 | 水平数与类型 | 0.5 | p.5-7 p.5 p.6 p.7: k ∈ [1,10]; test examples 30, 100, 1000; three few-shot sets; base/CoT/ToT in Table 4. | 报告了条件水平数与具体标签/取值，但未系统说明水平类型、间距、全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 1 | p.7 p.7: This paper focuses on StepGame; future studies could extend our findings to other benchmarks... controlled natural language... more naturalistic problem statements would therefore be highly desirable. | 关键构念主要用单一 StepGame 基准操作化，但结论部分明确讨论了基准受控语言与跨基准推广的限制，符合单一操作化下讨论推广边界的要求。 |
| A10 | 单一方法的风险 | NA | — | 研究不是多构念自陈问卷；自变量为提示/方法条件，因变量为客观任务准确率，经典共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组；模型/提示条件不是通过被试间随机分配得到，故被试间设计不适用。 |
| B2 | 被试内设计 | NA | — | 没有以人类被试或 LLM 单元为受试者的重复测量顺序设计；测试样例视为独立评估样例，未设置条件顺序平衡。 |
| B3 | 混合设计 | NA | — | 无组间/组内因素混合设计及对应误差项分析，故不适用。 |
| B4 | 因子设计 | NA | — | 论文不是完整交叉因子实验，未用 ANOVA/交互项呈现因子结构；虽比较多模型、多方法与多 hop，但属于基准评测分层描述，不足以按因子设计编码。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应统计检验，故不适用。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验与简单主效应分析，故不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计，也未报告区组变量与区内分配程序。 |
| B8 | 拉丁方 | NA | — | 无被试内条件顺序，未使用拉丁方平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计；没有非随机分组与选择偏差的因果推断问题。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理设计，故不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥实验条件；测试样例与模型条件不是概率分配得到。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，因此不存在顺序平衡方案需要报告。 |
| C3 | 恒定 | 0.5 | p.5 p.5: temperature 0 in CoT; 0.7 in ToT; remaining parameters standard; models Azure OpenAI ChatGPT 3.5-Turbo, Davinci, GPT-4. | 列出了模型版本、温度等恒定设置，但未讨论这些恒定选择对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对分配，故不适用。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组/协变量纳入统计模型，也无 ANCOVA 分析。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者，盲法安排不适用。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级，故不适用。 |
| D1 | 练习效应 | NA | — | LLM 测试样例独立，无练习块或试次内学习；few-shot 示例不是练习效应设计。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题，且任务时长/休息安排不适用于 API 评测。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立 API 调用/独立评估，无跨条件清洗期或残留迁移问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移设计，故不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为客观准确率，不是绝对判断/量表评分，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | NA | — | StepGame 为空间关系问答，无多选选项位置或需平衡的刺激序列；few-shot 示例顺序问题在 J5 下考虑。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，故默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 无人类被试需求特征或事后访谈假设推断，故不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集为 API 自动评测，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 p.7 Table 4: Map+ASP and Davinci+ASP reach 100 on many k; GPT-4 base is 100 at k=1 and dips to 25 at k=10; no SD/skew/endpoint-frequency or pilot calibration. | 报告了准确率均值与部分满分端点，但未报告分布形态、端点频率或 pilot 难度校准说明。 |
| E7 | 共同方法偏差 | NA | — | 非多构念同源自陈测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.6-7 p.6 p.7: test sets of 30, 100, 1000 examples and Table 4 accuracy values; no effect sizes, confidence intervals, or multiplicity correction. | 报告了测试样例数与准确率，但没有效应量、置信区间、主要分析全报告或多重性校正，也未做功效分析。 |
| F2 | 内部效度 | 0.5 | p.1 p.1: template errors distort evaluations; p.6 p.6: limited test examples could introduce biases; p.4 Table 1 corrections. | 对基准模板错误与测试集规模等内部效度威胁有识别和修正，但无随机分配、分配隐藏、基线等价性或正式内部效度分析。 |
| F3 | 构念效度 | 0.5 | p.3-4 p.3 p.4: Table 1/Table 2 incorrect templates; relation-to-sentence mapping corrected; p.4 ASP+template mapping solution. | 通过模板错误审计与修正提供了部分内容效度/构念效度论证，但无信度指标、操纵检验或多操作化会聚证据。 |
| F4 | 外部效度 | 0.5 | p.7 p.7: This paper focuses on StepGame; future studies could extend to other benchmarks; controlled natural language and more naturalistic problem statements desirable. | 报告了样本来源为 StepGame 基准并讨论跨基准/自然语言推广边界，但无跨样本或跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.6 p.6: Tests were carried out on 30, 100, and 1000 test examples; p.7 p.7 Table 4 reports accuracy by model/method/k. | 分析单位可理解为测试样例准确率并按 k 汇总，但未明确说明分配层级、嵌套结构或分析层级匹配问题。 |
| G2 | 随机效应 | NA | — | 无混合模型/随机效应结构；所比较模型是固定具体版本而非从模型总体抽样，随机效应不适用。 |
| G3 | 材料作为随机效应 | NA | — | 材料是固定 StepGame 基准测试集，而非作为自变量载体的抽样材料；不要求被试×项目随机效应模型。 |
| G4 | 统计功效 | 0 | p.6 p.6: tests on 30, 100, and 1000 examples to assess impact; no a priori power analysis, effect sizes, or CIs. | 无设计阶段功效分析或正式样本量论证；仅说明较大测试集更稳定，且结果未附效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.6 p.6: different test subsets and three few-shot sets; p.7 p.7 Table 4 includes base/CoT/ToT results; template removal described p.3-4. | 报告了多项条件与部分数据处理（移除不可修复模板），但未完整报告所有排除规则、样本量决定方式和验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–9 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文没有预注册平台、注册编号或预先分析计划；也未声明纯探索性，故适用但未做。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较；StepGame 为开放关系问答。 |
| J2 | 冗长偏差 | NA | — | 无 LLM 裁判评估开放式生成质量或长度偏好比较，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈纠错或多轮对话设置，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge；准确率由基准答案匹配得到，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.6 p.6: clean 5shot(1,3,5,7,10), clean 10shot, clean 5shot separate; examples from corresponding k-hop training set. | 报告了 few-shot 示例数量与来源/组成，但未做多 seed 重采样、排列反平衡或完整示例集控制。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4-5 p.4 p.5: prompt fragments for clink/camap/ccalcu and ToT; full details said to be in Appendix; no sensitivity ablation or dev/test split. | 提供了部分提示措辞与策略说明，但正文未给出完整模板版本、未做语义等价提示敏感性消融，也未说明 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | StepGame 上下文为短故事/至多 10-hop，远低于长上下文窗口，且无 RAG 或长文档设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.5 p.5: temperature 0 in CoT; ToT temperature 0.7; remaining parameters standard. No seeds or repeated-sampling CIs reported. | 报告了主要温度设置，但缺少 top-p/top-k、随机种子、重复运行次数、置信区间和精确 API snapshot。 |
| J9 | 重复与文本退化 | NA | — | 任务最终输出为空间关系答案/短推理链，不评估开放式长文本生成质量，重复与文本退化不是主要混淆。 |
| J10 | 分词效应 | NA | — | 单语言英文、单脚本任务，无跨语言/跨脚本 token 数比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3 p.3: StepGame benchmark story-question pairs; no model training cutoff or contamination check reported. | 使用公开 StepGame 基准，但未对照训练截止日期，也未做 n-gram/DCQ 等污染检测，不能区分记忆与泛化。 |
| J12 | 基准饱和 | 0.5 | p.7 p.7 Table 4: Map+ASP and Davinci+ASP reach 100%; conclusion: effective resolution prompts a need for more challenging versions. | 识别到规则化解法已接近/达到满分并呼吁更难版本，但未改用连续指标、校准误差或 bootstrap CI 进行饱和分析。 |
| J13 | 指令遵循 | NA | — | 因变量是空间关系推理准确率，不是指令遵循；无否定/数量/格式等约束遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 研究不要求 JSON/文法约束等结构化输出，也没有把格式合法率与内容错误分开评估。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/对齐、有害请求或越狱攻击评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2 p.2 footnote: not thoughts in the human sense; p.7 p.7: Humans would probably find this challenging too. | 对 LLM 的“thoughts”做了去拟人化限定，并偶尔类比人类难度；但未系统论证 LLM 空间推理与人类同名构念的异同，也无人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随规模/训练进展的涌现曲线，也未宣称突变式涌现；模型间差异为描述性比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL、best-of-N 或针对基准的代理指标优化过程，奖励过优化不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.5-7 p.5 p.6 p.7: model names ChatGPT 3.5-Turbo, Davinci, GPT-4 and test sizes; Table 4 gives single accuracy points without CIs, seeds, or exact snapshots. | 只报告单次/单点准确率，无重复次数、95% CI、精确 snapshot 标识或配对检验，评估可复现性不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮问答/单次提示评测，无多轮对话历史累积或多轮一致性衰减评估。 |

## 编码小结
研究核心是基准纠错与 LLM 条件评测，对空间关系抽取与多跳推理负荷有直接比较；但统计推断、置信区间、重复采样、精确模型快照与完整 prompt 报告不足。大量人类实验设计组件（被试分配、顺序平衡、需求特征、实验者效应等）不适用于该 LLM 基准评测。
