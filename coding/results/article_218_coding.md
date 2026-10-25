# article_218 | Creativity or Brute Force? Using Brainteasers as a Window into the Problem-Solving Abilities of Large Language Models | 2025

研究类型概述：该文构建 BRAINGLE BRAINTEASER 基准，对多个 LLM 在 CoT、Math、Hint、Math+Hint 等提示条件下进行基准评测和描述性比较，并辅以改写题面、informed self-correction、步骤拆分与提示使用分析。分析单位是模型×题目×提示/分析条件下的响应，主要依赖 OpenAI o3 作为自动裁判。
- **研究构念（Construct）**：创造性问题解决、穷举策略、提示利用与错误自我修正｜CA 构念锚定：创造性思维（creative thinking, `trm_4a3fd79d09f42`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：让多个现成推理模型解决专家编写的数学与逻辑brainteaser，并在无提示、结构化提示、反穷举提示、给定官方解和给定错误解等条件下比较。（操纵题目类型与难度、模型、提示/提示摘要、反穷举指令以及真/假参考解。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6 Table 3 compares CoT Prompt, Math Prompt, w Hint, Math Prompt w Hint; p.23-24 Appendix F gives prompt texts. | 提示策略是明确操纵的自变量，至少有四个水平和具体标签，且有 prompt 文本；但未报告操纵检验，分配方式也只是每个模型/题目在条件下调用，未系统说明。 |
| A2 | 因变量 | 0.5 | p.6 reports percent solution correctness judged by o3; p.6 notes 99.3% and 97% raw agreement for correctness and creativity/brute-force; p.7 defines brute-force/creative solutions. | 因变量指标与计分方式基本明确（o3 判定的正确率、brute-force/creative 分类、步骤数等），并有人类一致性证据；但缺少正式信度、效度检验及对连续指标或端点效应的系统预处理说明。 |
| A3 | 控制变量 | 0.5 | p.23 Table E lists model versions, top_p, max tokens, temperature; p.6 states all models evaluated under same prompting approaches. | 报告了模型版本与采样参数等部分控制变量，但没有系统列出控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.22 Limitations acknowledges prompt engineering limits, single-source benchmark, o3 judge bias, macro step-count bias, and possible data contamination. | 识别了若干潜在混淆并给出部分控制/验证（如人类一致性），但对残余混淆及其对内部效度威胁的讨论不系统。 |
| A5 | 调节变量 | NA | — | 研究没有正式界定调节变量并提出交互假设；模型规模和提示类型的比较是描述性分组，未做正式调节/交互检验，因此不适用。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量、直接/间接效应分解或因果链假设，不适用。 |
| A7 | 操作性定义 | 1 | p.7 gives operational definitions of brute-force and creative solutions; p.24 Appendix G gives the counting-steps prompt; p.6 describes correctness scoring by o3 comparison to human solutions. | 关键构念有较详细的、可复现的操作化：提示模板、brute-force/creative 定义、判定方式与计分单位均明确。 |
| A8 | 水平数与类型 | 0.5 | p.6 Table 3 lists four prompt conditions and seven models; p.23 Table E lists model versions. | 报告了主要条件的水平数与标签，但未明确说明水平类型、分类间距/全距，也未对连续模型规模变量作中心化或回归建模说明。 |
| A9 | 单一操作化的风险 | 1 | p.6 and p.22 report o3 judgments validated against human annotators for correctness and creativity/brute-force; p.5/p.9 report manual inspection of step breakdowns. | 关键构念的自动判断与人工标注有一致性会聚证据，步骤拆分也有人工检查，符合多指标/多评分者会聚证据的要求。 |
| A10 | 单一方法的风险 | 0.5 | p.22 Appendix B acknowledges potential bias from using OpenAI o3 as judge; p.6/p.22 report human agreement checks. | 说明了自动裁判这一方法来源并做了部分人工验证，但被评对象包含 o3 且未做系统共同方法偏差统计检验或设计控制，信息不完整。 |
| B1 | 被试间设计 | NA | — | 不是人类被试间实验；同一模型和题目在多个提示条件下被评估，没有独立被试组分配。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量及顺序平衡设计；各提示条件为独立 API 调用，论文未设置需要平衡的条件顺序。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内混合实验设计，也没有对应混合模型或误差项。 |
| B4 | 因子设计 | NA | — | 论文呈现模型×提示×数据集的评测矩阵，但没有正式因子实验设计、设计矩阵、每格样本量或 ANOVA 交互分析，因此不按因子设计适用。 |
| B5 | 主效应 | NA | — | 没有正式因子设计下的主效应统计检验，因此不适用。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验、简单主效应或交互图误差棒，因此不适用。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计及区内随机分配。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验分组研究；没有非随机分配下的因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理设计，因此不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有把独立分析单位随机分配到互斥条件；所有模型/题目在多个提示条件下被调用，不涉及被试随机化。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，无需平衡方案。 |
| C3 | 恒定 | 0.5 | p.23 Table E lists model names, top_p, max tokens, temperature; p.22 Limitations restricts conclusions to a specific set of LLMs and benchmark. | 列出了部分恒定变量及水平，但未系统说明所有环境/版本恒定措施，也没有充分展开外部效度限制。 |
| C4 | 匹配 | NA | — | 无匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入分析模型，因此该组件结构不存在。 |
| C6 | 盲法 | NA | — | 核心评估为自动化 LLM 裁判，无人类被试/评分者盲法设计；人类标注仅用于一致性验证，未构成正式盲法实验。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 各提示条件为独立调用，无练习块或上下文内学习顺序问题。 |
| D2 | 疲劳效应 | NA | — | LLM 调用无人类疲劳效应，也无 session 时长/休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每条件独立会话，无跨条件迁移或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件残留或不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 主要因变量为客观正确率和分类指标，不涉及主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选/序列刺激的选项顺序设计；题目独立呈现，不涉及被试内刺激顺序平衡。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 研究对象为 LLM，不存在人类被试需求特征或事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试传递期望的问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 3 reports accuracy means for full set and top-50 hardest subset; p.4 Table 1/Table 2 provide difficulty and step statistics; no SD/skew/endpoint frequency by item. | 报告了正确率水平与 top-50 更难子集，可部分排查天花板/地板；但未报告主要因变量的标准差、偏度或端点频率，也未系统说明难度预校准。 |
| E7 | 共同方法偏差 | NA | — | 不涉及同源自陈式多构念测量，因此共同方法偏差不按该组件适用。 |
| F1 | 统计结论效度 | 0 | p.6 Table 3 mostly reports point estimates; p.8 rewriting comparison reports p=0.023, p=0.043, p=0.08 but no effect sizes or CIs; p.17 checklist states only single run. | 未系统报告效应量、置信区间、样本量/功效依据或所有分析的多重性校正，基本要件未达成。 |
| F2 | 内部效度 | 0.5 | p.6 compares prompting conditions across models and problems; p.22 Limitations discusses possible biases but no randomization/allocation/baseline equivalence or flow. | 提示条件比较涉及一定的内部效度问题，并部分讨论了裁判、来源和污染风险；但无随机分配、分配隐藏、基线等价性检验或被试流向/损耗处理。 |
| F3 | 构念效度 | 0.5 | p.6 reports o3-human agreement 99.3% and 97%; p.5/p.9 manual inspection of step breakdowns; p.7 gives construct definitions. | 有关键测量的会聚效度和人工检查证据，但缺少正式信度/效度统计、操纵检验及单一操作化局限的系统论证。 |
| F4 | 外部效度 | 0.5 | p.3-4 describes Braingle source and benchmark construction; p.6-7 lists evaluated models; p.22 states findings are specific to BRAINGLE BRAINTEASER and a specific set of LLMs. | 报告了数据集来源、模型列表和部分推广边界，但未报告跨样本/跨情境复现，代表性论证有限。 |
| G1 | 分析单位 | 0.5 | p.6 Table 3 aggregates accuracy by model×prompt×dataset; p.9 step-count analyses aggregate by model; no multilevel model or explicit clustering treatment. | 分析存在题目嵌套于数据集、响应嵌套于模型/题目的结构，但论文主要用聚合百分比呈现，未显式说明分配层级与分析层级匹配或使用多层模型。 |
| G2 | 随机效应 | 0 | p.6-7 model comparisons are descriptive by fixed model set; p.22 Limitations notes conclusions are specific to a set of LLMs; no random-effects structure reported. | 没有混合模型或随机效应说明，模型被当作固定集合比较，却对外泛称 LLMs/模型能力，随机效应结构缺失。 |
| G3 | 材料作为随机效应 | 0 | p.3-4 constructs benchmark from Braingle problems; p.6 reports aggregate accuracy over items; no (1&#124;item) model, F′ or item-level generalization analysis. | 题目材料是从更大题库抽样，但分析未将题目作为随机效应，结论对材料总体的推广缺乏统计处理。 |
| G4 | 统计功效 | 0 | p.17 checklist states single run per setting due to API cost; no a priori power analysis or effect-size/CI plan. | 没有事前功效分析或样本量推导，主要报告点估计，部分比较仅给 p 值，未满足功效与效应量报告要求。 |
| G5 | 研究者自由度 | 0.5 | p.4 reports removing low-quality problems, leaving 242 Math and 236 Logic; p.6 Table 3 reports many model/prompt conditions; p.17 notes single run due budget; no clear confirmatory/exploratory distinction. | 报告了部分数据筛选规则与主要条件，样本量受 API 成本限制也有说明；但未完整区分验证性与探索性分析，也未系统报告所有排除/停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or pre-specified analysis plan is reported in the main text or checklist. | 没有预注册或时间戳早于数据收集的分析计划，按规则记 0。 |
| J1 | 位置偏差 | NA | — | LLM 裁判用于单答案正确性和 brute-force 分类，不是多候选项选择、排序或成对位置比较，因此候选位置偏差不适用。 |
| J2 | 冗长偏差 | 0 | p.6-7 uses OpenAI o3 to judge correctness and brute-force/creative solutions; p.47-48 reports longer step counts for some models but no length-score correlation or length control in judging. | LLM 裁判评估生成解的质量/策略时可能受长度影响，但全文未说明长度控制、未报告回答长度与得分的相关或长度对照盲评。 |
| J3 | 谄媚 | 0.5 | p.8 reports informed self-correction by swapping flawed LLM and correct human solutions; p.49-51 show prompt and false-confession examples; over 60% models often took the bait. | 通过交换正确/错误角色测试模型是否附和给定前提，并报告了 false confession/justified denial 分布；但未系统区分 feedback vs answer sycophancy，且样本仅限手动检查的少量错误例。 |
| J4 | 自我偏好 | 0.5 | p.6/p.22 use OpenAI o3 as the judge while OpenAI o3 is also one of the evaluated models; p.22 acknowledges potential bias and reports human agreement and comparison with other judges. | 识别了 o3 裁判可能偏差并做了人类一致性验证，但仍主要使用同源 o3 作为唯一自动裁判，未匿名化、未报告异源陪审团分别结果或量化自我偏好率。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.7 uses a few-shot prompt with labeled brute-force/non-brute-force examples; p.43 and p.47 show few-shot judge prompts with placeholders, but no source/count/label balance/order randomization/multiple seeds. | 使用了 few-shot 示例，但未报告示例来源、每类数量、排列反平衡、多 seed 重采样或示例未取自测试集的证明；基本报告要求未达成。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.23-24 Appendix F gives full CoT, Math, and Hint prompts; p.6 compares four prompting approaches; p.22 notes prompt engineering effects were limited. | 提供了完整 prompt 模板并比较多个提示版本，但未做语义等价措辞的敏感性消融、未明确 dev/test 划分，也未报告 prompt 搜索/版本迭代过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验没有长上下文、RAG 或关键信息位置操纵，题目上下文相对短，不适用。 |
| J8 | 温度与采样随机性 | 0.5 | p.23 Table E reports top_p, max tokens, temperature; p.17 checklist states a single run per setting due to API cost. | 报告了主要采样超参并明确单次运行，但无随机种子、每条件重复采样 N 与 95% CI，闭源模型 snapshot 日期也不完整。 |
| J9 | 重复与文本退化 | 0.5 | p.23 Table E reports temperature/top_p/max tokens; p.8 mentions DeepSeek R1 distillation models prone to degenerative repetition; no systematic repetition-rate QC. | 报告了部分解码设置，注意到可能退化，但没有报告 repetition penalty、n-gram 重复率/退化率，且不同模型采样温度不完全一致。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言任务，无跨语言/跨脚本或跨格式分词比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.22 Limitations states dataset came from public Braingle and data contamination is a potential concern; initial pilot found frontier-model solutions distinct from human solutions, but this is called anecdotal. | 识别了污染风险并给出轶事性 pilot 观察，但没有报告与模型训练截止日期的系统对照、正式 n-gram/DCQ 污染检测或污染率。 |
| J12 | 基准饱和 | 0.5 | p.6 Table 3 shows top accuracies around 82.8% on Math and 74.4% on Logic; p.3 states results show the benchmark is non-saturated; top-50 subsets are also reported. | 报告了基准分数量程、不同模型水位和更难子集，显示未饱和；但模型间差异未用 bootstrap CI 比较，也未在接近天花板时改用连续指标，因此仅部分满足。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，没有按约束类型测量指令遵守率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.23-24 prompts require responses to finish with the exact format Final answer: followed by the answer; no format-validity rate or retry strategy is reported. | 报告了输出格式约束设置，但未报告格式合法率、重试/后处理规则，也未将格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/对齐、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 abstract frames the work as probing problem-solving and creativity in LLMs; p.7 defines creative/brute-force by analogy to human insight; p.22 limits conclusions to a specific set of models and operational definitions. | 论文对 LLM 上的创造性/brute-force 构念作了操作化，并部分讨论其与人类解的异同和推广限制；但没有系统的人类同范式对照实验或完整构念效度论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究没有报告随模型规模/训练进展的能力曲线，也不宣称涌现或突变现象；仅有不同已发布模型的横断比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及以 benchmark/奖励模型/LLM-judge 为优化目标进行训练、RL 或 best-of-N 优化，因此 overoptimization 不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.17 checklist states single run per setting and no error bars; p.23 Table E gives inference settings; p.1 links code and dataset; some model snapshots have dates but several are vague. | 报告了重复次数为单次及部分模型版本/设置，并公开代码和数据；但无 95% CI、无配对检验、无精确 API snapshot/逐题日志，复现保障不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮提示—响应评估；informed self-correction 也是单轮输入，不存在多轮对话历史累积或跨轮一致性衰减。 |

## 编码小结
整体是 LLM 基准评测与多条件描述性分析，不是人类被试实验。论文对 LLM 特有风险（LLM 裁判、few-shot、prompt 版本、污染、饱和、可复现性）有部分识别，但多数统计推断、随机化、随机效应、预注册和功效分析缺失；人类实验特有的分配、顺序、盲法等组件多不适用。
