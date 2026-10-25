# article_135 | Meta-in-context learning in large language models | 2023

研究类型概述：该文是面向 LLM 的计算/行为实验研究，而非人类被试实验。作者以 GPT-3（text-davinci-002）为主要对象，在单维函数学习、二臂老虎机、真实回归基准和 MMLU 上考察“上下文内元学习”：通过在上下文中依次呈现多个任务，检验任务序号/试次数对 MSE、regret、RMSE、accuracy、先验估计与策略参数的影响；分析单位为 LLM 的模拟运行、试次和任务序列。
- **研究构念（Construct）**：元情境学习、先验适应以及跨任务学习策略变化｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：向GPT-3连续呈现多个相关的少样本回归任务或双臂老虎机任务，比较普通in-context与前置多个任务后的学习曲线，并转移到真实回归数据和MMLU。（改变连续任务数量、任务间统计相似性、先验分布、奖励结构和同类示例数量。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3: “We set the temperature parameter to zero... unless otherwise noted”; p.4: “prompts that include data from up to five tasks”; p.10: “k ∈ {0, 1, 2} examples from the same category” | 明确操纵/考察了任务序号、试次数、模型、MMLU few-shot 数量及是否加入跨类别元示例等至少两个水平；但未报告正式分配程序或操纵检验，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.4: “performance as measured by the mean-squared error (MSE)”; p.6: “Performance (measured in terms of regret)”; p.8: “We measured performance by the root-mean-squared error”; p.10: “accuracy of 55.1%” | 因变量指标与计分方式（MSE/regret/RMSE/accuracy）清楚；但缺少信效度证据、连续指标的系统预处理说明与防天花板/地板说明，仅零散报告异常值剔除与归一化，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.3: “TEXT-DAVINCI-002... temperature parameter to zero... retained the default values”; p.6: “randomly sampled two different letters without replacement”; p.8: “normalized both the feature and target spaces to the interval of [−1, 1]” | 报告了模型版本、温度、默认参数、字母随机化、归一化和特征筛选等控制；但未以系统清单逐一说明所有控制手段，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.5: “practical constraint of a finite context window”; p.6: “cancel out biases towards certain letters” and “mitigate recency biases”; p.9: “task similarity” | 识别并处理了字母偏差、近因偏差、上下文长度和任务相似性等潜在混淆，但没有系统的残余混淆或敏感性分析，故为 0.5。 |
| A5 | 调节变量 | 0.5 | p.8: “we furthermore included an interaction effect with task number for each factor”; p.8: “positive interaction effect between task number and Vt” | 将任务序号作为策略效应的调节变量并报告了交互检验；但未说明中心化/标准化，也未报告各调节水平的简单斜率，故为 0.5。 |
| A6 | 中介变量 | 0 | p.5: “performance improves during meta-in-context learning because it adapts its priors”; p.7: “part of this performance boost arises because GPT-3 adapts its priors” | 论文提出了“先验适应驱动表现提升”的机制假设并采集先验，但未做直接/间接效应分解、a/b 路径或 bootstrap CI，提出中介性机制却未进行中介分析，故为 0。 |
| A7 | 操作性定义 | 0.5 | p.3-4: 给出函数生成公式、输入范围、噪声分布与示例 prompt；p.6: 给出二臂老虎机 prompt；p.8: 给出真实回归 prompt；p.10: 说明 MMLU few-shot 设置 | 关键任务和指标有较具体的操作化程序，但 prompt 均以 “[. . .]”省略，未提供完整模板或代码，复现性不完整，故为 0.5。 |
| A8 | 水平数与类型 | 0.5 | p.3: “T = 5 input-target pairs” and “up to five tasks”; p.6: “10 trials”; p.10: “k ∈ {0, 1, 2}” | 报告了主要水平数与取值；但未系统说明水平类型、间距/全距及连续变量入回归时的中心化/标准化，故为 0.5。 |
| A9 | 单一操作化的风险 | 1 | p.1: “two idealized domains... two diverse benchmarks”; p.5: “three distinct settings”; p.10: 报告 MMLU 上元上下文学习收益 | 核心构念在函数学习、二臂老虎机、真实回归和 MMLU 多域、多指标上重复操作化，并报告一致的改善证据，达到多操作化会聚要求。 |
| A10 | 单一方法的风险 | NA | — | 该研究不是多构念同源自陈量表测量；自变量是提示/任务上下文操纵，因变量是模型客观输出，共同方法偏差的人类问卷意义不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类或独立被试组接受不同条件的被试间分配；模型比较是描述性/计算性对比，主设计不是被试间实验。 |
| B2 | 被试内设计 | 0.5 | p.3: “iteratively presented each data-point together with the history of previous observations, starting from the first trial in task one up to the last trial in task five”; p.8: 以 trial 和 task number 预测 RMSE | 同一模拟内重复经历 trial/task 序列，具有重复测量性质；但顺序固定、未报告平衡方案，也未在统计模型中显式使用模拟运行随机效应，故为 0.5。 |
| B3 | 混合设计 | NA | — | 没有逐因素区分的组间/组内混合设计；模型比较与任务序列不构成正式混合设计。 |
| B4 | 因子设计 | 0.5 | p.4: “linear regression model that included the trial and task number as independent variables on the MSE”; p.8: “interaction effect with task number”; p.9: trial and task similarity | 存在 trial、task、策略因子等交叉/回归结构并报告部分交互；但未给出完整设计矩阵、每格样本量与标准 ANOVA 效应量，故为 0.5。 |
| B5 | 主效应 | 0.5 | p.5: “statistically significant effects for both trial number... and task number”; p.8: 报告 Vt、RUt、Vt/TUt 主效应系数 | 报告了主效应系数、标准误、t/z 与 p 值；但无 ηp² 等效应量，且在交互显著时未系统说明主效应解释受限，故为 0.5。 |
| B6 | 交互作用 | 0.5 | p.8: “positive interaction effect between task number and Vt (β = 0.128 ± 0.025, z = 9.633, p < 0.001)” | 报告了任务序号与策略因子的交互检验；但没有简单主效应/多重比较校正细节，图示误差棒不是针对简单效应，故为 0.5。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机分配设计；任务是随机抽样而非按区组变量划分。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计，也没有人类被试内条件顺序需要拉丁方平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；没有非随机处理分配与选择偏差的因果推断框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 任务的累积序列本身就是元上下文学习对象，不是可逆处理的人类被试内设计；未主张或设计可逆性/迁移对称性检验。 |
| C1 | 随机化 | NA | — | LLM 模拟没有把独立分析单位随机分配到互斥处理组的分配问题；任务/输入随机抽样属于刺激抽样，不是处理分配隐藏。 |
| C2 | 平衡 | NA | — | 没有需要平衡的独立条件顺序；任务序号是学习进程本身，不能通过常规被试顺序平衡解决。 |
| C3 | 恒定 | 0.5 | p.3: “TEXT-DAVINCI-002... temperature parameter to zero... default values for all other parameters”; p.6: 固定赌场/机器提示；p.8: 固定五特征与归一化范围 | 报告了模型、温度、默认参数、提示模板和数据处理等恒定设置；但未系统讨论这些恒定选择对外部效度的限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配/配对分配程序；不存在需要匹配后均衡性检验的设计。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入模型；任务相似性是解释变量而非匹配/协变量控制。 |
| C6 | 盲法 | NA | — | 研究为自动化 LLM 调用与客观指标计算，无人类被试、主试或评分者需要盲法。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 等顺序平衡层级；任务序列不按该框架设计。 |
| D1 | 练习效应 | 0.5 | p.5: 回归中 trial number 效应显著；p.6: “Performance... improves over the first four trials and plateaus” | 将试次位置/试次数作为学习效应纳入分析，但没有练习块、截除规则或初期练习效应控制安排，故为 0.5。 |
| D2 | 疲劳效应 | NA | — | LLM 模拟不存在人类疲劳；单次提示/短序列调用，无需休息间隔或 session 时长控制。 |
| D3 | 延滞 / 迁移效应 | 0.5 | p.9: “meta-in-context learning works best if similarity to previously encountered tasks is high”; p.9: 将 task similarity 纳入实验 1、2 分析 | 识别并建模了跨任务迁移/相似性效应，但因上下文累积而无清洗期，也未把条件对作为显式设计因素，故为 0.5。 |
| D4 | 不对称迁移 | 0 | p.9: 仅分析 task similarity，未报告迁移对称性检验；p.3: 任务从 task one 到 task five 固定累积 | 跨任务序列固定且上下文累积，迁移可能是非对称的；论文未检验或讨论迁移对称性及平衡失效，故为 0。 |
| D5 | 范围效应 | NA | — | 没有使用李克特量表、绝对量值估计等需要范围效应控制的被试内主观评分类任务。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.6: “randomly sampled two different letters without replacement” and “randomized the order of these letters in the questions at each trial to mitigate recency biases” | 对二臂老虎机选项字母及题中顺序做了随机化以减少位置/近因偏差；但未报告完整平衡方案、各位置出现次数或翻转率，故为 0.5。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体/跨文化反应风格比较。 |
| E4 | 需求特征 | NA | — | 研究对象为 LLM，无人类被试的需求特征或事后访谈；赌场 cover story 是提示框架，不是人类欺瞒实验程序。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.9: “percentage of predictions outside or equal to the extremes of the squashed target range”; p.4/p.6/p.8: 报告均值与 95% CI | 报告了均值、误差线和真实回归中极端预测比例，但没有系统报告偏度/端点频率，也未说明 pilot 难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 没有多构念同源自陈量表，不存在共同方法偏差的程序控制/统计检验问题。 |
| F1 | 统计结论效度 | 0.5 | p.5: “β = −30.614 ± 3.08, t = −19.514, p < 0.001”; p.4/p.6/p.8: 图注报告 95% confidence intervals；p.4/p.6/p.8: 报告 100、500、42·50 次模拟 | 报告了系数、标准误/置信区间与模拟次数，但无样本量功效依据、无多重性校正说明，统计假设检验说明也不完整，故为 0.5。 |
| F2 | 内部效度 | 0.5 | p.3-4: 函数、输入和任务随机生成；p.8: “randomly selected five different tasks”; p.10: 讨论上下文长度与任务简单性限制 | 有随机抽样和部分内部效度限制讨论；但没有随机分配、分配隐藏、基线等价或试次流向/损耗处理，故为 0.5。 |
| F3 | 构念效度 | 0.5 | p.4-5: 用 MSE 回归确认 in-context/meta-in-context learning；p.9: 用 extreme predictions 与 task similarity 支持解释；p.10: 多基准外推 | 主要指标为客观计算指标，并提供多域会聚与若干机制性检验；但无正式信度、效度证据或完整操纵检验，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.3: “TEXT-DAVINCI-002... GPT-3”; p.8: “60 different real-world datasets... 42 remaining datasets”; p.10: 讨论有限观测、简单任务、上下文窗口等边界 | 报告了模型来源、基准和部分推广边界；但没有跨样本/跨情境系统复现结果，代表性论证有限，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p.4: “100 simulations”; p.5: 以 trial/task 对 MSE 做线性回归；p.6: “500 simulations”; p.8: “42 · 50 simulations” | 说明了模拟次数与分析在 trial/task 层面进行，但未显式说明模拟运行/任务的嵌套聚集结构，也未使用多层模型匹配分析层级，故为 0.5。 |
| G2 | 随机效应 | 0 | p.5: “we fitted a linear regression model that included the trial and task number”; p.8: 使用线性/probit 回归系数报告 | 模型仅报告固定效应回归，未说明哪些因子为随机效应，也未用随机截距/斜率处理模拟运行或任务抽样；对重复测量和任务总体推广不足，故为 0。 |
| G3 | 材料作为随机效应 | 0.5 | p.3-4: 函数参数从 p(T) 抽取、输入从 U(0,100) 抽取；p.8: 随机选五个真实数据集；p.10: MMLU 任务 | 材料/任务明确来自更大分布或基准抽样；但分析中未将任务/项目作为随机效应纳入模型，故为 0.5。 |
| G4 | 统计功效 | 0 | p.4: “100 simulations”; p.6: “500 simulations”; p.8: “42 · 50 simulations” | 没有事前功效分析或样本量/模拟次数确定依据；虽报告了置信区间，但未满足功效论证基本要件，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p.5: “We omitted outlier predictions that had absolute values of 10,000 or larger”; p.8: 少于五特征的数据集被排除、按 F 值保留前五特征；p.6: 排除字母 I/U | 报告了若干排除/预处理规则和主要因变量，但未说明样本量停止规则，也未明确区分验证性与探索性分析，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–14 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告预注册平台、注册编号或数据收集前分析计划；也没有区分预注册验证性分析与事后探索性分析，故为 0。 |
| J1 | 位置偏差 | 0.5 | p.6: “randomly sampled two different letters without replacement” and “randomized the order of these letters... to mitigate recency biases”; p.3: 报告模型与温度 | 对二臂老虎机选项位置/字母顺序做了随机化，并报告模型/温度；但未报告交换前后偏好翻转率或位置×正确率，故为 0.5。 |
| J2 | 冗长偏差 | NA | — | 研究不使用 LLM-as-judge 或开放式生成长短比较；因变量为数值预测/regret/准确率。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错对话，不涉及谄媚偏差操纵。 |
| J4 | 自我偏好 | NA | — | 没有 LLM 裁判或成对比较评估，不存在裁判自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.3: “T = 5 input-target pairs” and “up to five tasks”; p.6: 每任务 10 trials；p.8: 每任务 5 points、5 features；p.10: k ∈ {0,1,2} | 报告了 few-shot 示例数量、来源和多次模拟；但没有系统报告示例排列反平衡、多示例集 seed 均值±SD 或校准/模板全文，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p.3-10: 多个 prompt box 含 “[. . .]”省略；未报告提示版本号、敏感性消融或 dev/test 划分 | 只给出提示模板片段，未提供完整模板与版本，也未做措辞敏感性消融或说明是否在测试集上调参，故为 0。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是长文档/RAG 的关键信息位置效应研究；虽然上下文随任务累积，但未以“中间迷失”或 token 位置×正确率为核心检验。 |
| J8 | 温度与采样随机性 | 0.5 | p.3: “temperature parameter to zero... unless otherwise noted” and “default values for all other parameters”; p.5/p.7: “set the temperature to one” and repeated five times；p.13: API accessed 2023-05-10 | 报告了温度、模型与访问日期及部分重复；但没有 top-p/top-k、随机种子/API snapshot 细节和每条件采样 CI 的完整报告，故为 0.5。 |
| J9 | 重复与文本退化 | NA | — | 任务输出为短数值/字母选择，不涉及开放式长文本生成与重复/退化率评估。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文提示，无跨语言/跨脚本比较，无分词长度混淆问题。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.8: 使用 60 个真实回归数据集；p.10: 使用 MMLU 基准；全文未报告训练截止日期与测试集重叠检测 | 使用了公开基准但未与模型训练数据截止日期对照，也未做污染检测或污染率报告，故为 0。 |
| J12 | 基准饱和 | NA | p.10: MMLU 准确率 55.1%；p.8: RMSE 连续指标；未出现接近天花板的结果 | 所用基准未饱和且采用连续误差指标，不存在需要改用更难子集或连续指标的天花板风险，故为 NA。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，没有按约束类型评估指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.3/p.6/p.8: 提示要求“y = [insert]”“Machine [insert]”等固定短答格式；全文未报告格式合法率或重试策略 | 存在结构化短答格式约束，但未报告文法引导、格式合法率、重试/后处理规则，也未将格式失败与内容错误分开，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全性、越狱或有害请求评估，无自然拒绝率/对抗攻击成功率问题。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2-3: 引用 GPT-3 在二臂老虎机上“exceeded that of human participants”；p.5/p.7: 使用“priors”“Boltzmann exploration”“Thompson sampling”解释 LLM 行为 | 将 LLM 作为学习/认知行为主体，并与人类实验任务和人类启发式算法类比；但没有系统论证 LLM 构念与人类同名构念的异同，也无人类同范式对照，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p.5: “solely text-davinci-002 seems to exhibit meta-in-context learning capabilities”；p.5: 比较 context size 8000 vs 4096 并称“emergent phenomenon” | 报告了模型规模/家族比较并主要使用连续 MSE 指标，但对“涌现”仅作推测，未系统展示多 seed、连续指标与置信区间曲线以排除指标假象，故为 0.5。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究仅做提示评估，无训练、RL、best-of-N 或对代理指标的优化过程，不存在奖励过优化/指标博弈。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.3: “TEXT-DAVINCI-002... OpenAI Python API”; p.13: “Accessed: 2023-05-10”；p.4/p.6/p.8: 报告 100/500/42·50 次模拟与 95% CI | 报告了重复模拟次数、模型名称、访问日期与置信区间；但没有精确 API snapshot/commit、随机种子、配对显著性检验或原始推理日志，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究为单轮提示式评估/序列上下文，不是多轮对话中的一致性衰减研究，也未外推到多轮部署。 |

## 编码小结
论文对核心现象“跨任务序列改善上下文学习”给出了多域证据，并清楚报告了任务生成、提示模板要点、模型版本、温度设置和主要统计结果。但作为 LLM 行为研究，它在随机化/顺序平衡、随机效应与嵌套结构、提示敏感性与完整模板、基准污染、统计功效、预注册等方面报告不足；部分人类被试设计组件不适用。整体属于方法披露中等、核心操作化较清楚但可复现性与偏差控制有限的实证研究。
