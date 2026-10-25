# article_067 | NewsInterview: a Dataset and a Playground to Evaluate LLMs’ Grounding Gap via Informational Interviews | 2025

研究类型概述：该文是数据集构建、人类—LLM 话语比较与 LLM 多智能体模拟基准的混合研究，不是人类随机对照实验。主要分析单位为生成的问题/对话轮次以及模拟访谈，另有小规模人类被试用于验证 source persuasion。
- **研究构念（Construct）**：信息访谈中的对话共同基础、问题调整与说服性信息搜寻（grounding dialogue, question adaptation, and persuasive information-seeking）｜CA 构念锚定：计划（planning, `trm_4a3fd79d0acc1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：该文是数据集构建、人类—LLM 话语比较与 LLM 多智能体模拟基准的混合研究，不是人类随机对照实验。主要分析单位为生成的问题/对话轮次以及模拟访谈，另有小规模人类被试用于验证 source persuasion。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.3: 'We experiment with different variations: (1) Baseline... (2) Chain-of-Thought... (3) Outline'；p.4 Table 1 另列 Outline-CoT。 | 提示策略作为自变量被命名并列出多个水平，但分配方式、运行顺序与操纵检验未报告。 |
| A2 | 因变量 | 0.5 | PDF p.4 Table 1: 'Exact Match / Info. / Motivation / Style / Discourse / Context'；p.8 Table 2: 'Reward percentage'。 | 因变量指标与百分比计分有界定，话语标注也有部分信度证据；但主指标缺少系统信效度、CI 与连续指标预处理说明。 |
| A3 | 控制变量 | 0.5 | PDF p.3: 'All question-generation experiments are conducted using Llama-3.1-70b'；p.7: 'gpt-4o for the source-LLM'。 | 固定了部分模型与游戏组件，但未系统列出全部控制变量（温度、top-p、运行日期等）及控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF p.8: 'removing the source’s ability to withhold information... drastically increases the reward'；同页提到 'inferring which information the source has withheld' 也是挑战。 | 通过 ablations 识别了 persuasion/withholding 等潜在混淆并作条件比较，但未说明残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 研究未提出正式调节假设，也未报告调节变量的交互检验、中心化或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 研究未提出中介模型，也未进行直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | PDF p.5 Algorithm 1；p.24 Table 11 personas；p.31 Table 13 discourse definitions；p.21-30 prompt templates。 | 游戏、persona、话语类别与多项提示词操作化较详细；但 Section 3 的问题生成变体提示及六维比对计分细节未完整呈现。 |
| A8 | 水平数与类型 | 0.5 | PDF p.3 列出 4 种 prompt 变体；p.7 列出 8 种 persona；p.8 Table 2 为 4 个模型 × 3 条件。 | 水平数与各水平标签基本清楚，但未明确水平类型、间距/全距或连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p.4 Table 1 使用六个对齐维度；p.31 Table 13 使用多种 discourse roles；p.8 使用 reward 指标。 | 关键构念有多个指标，但未报告各操作之间的会聚证据；局限部分主要讨论模拟环境而非测量推广边界。 |
| A10 | 单一方法的风险 | NA | — | 研究主要不是自陈式同源测量；IV 为提示/条件操纵，DV 为 LLM 文本行为、LLM 判定或模拟 reward，不适用传统共同方法偏差框架。 |
| B1 | 被试间设计 | NA | — | 没有人类被试间分配；LLM 条件比较不是独立被试组设计。 |
| B2 | 被试内设计 | NA | — | Section 3 的提示变体为离线独立生成/比较，未形成带条件顺序平衡需求的人类或 LLM 重复测量被试内设计。 |
| B3 | 混合设计 | NA | — | 没有明确的组间/组内混合设计及对应误差项。 |
| B4 | 因子设计 | 0 | PDF p.8 Table 2 为 4 个 interviewer 模型 × 3 个游戏条件的均值表，但未报告交互项检验。 | 存在多因素比较结构，却没有因子设计统计量、完整设计矩阵或交互检验，按规则记 0。 |
| B5 | 主效应 | 0 | PDF p.8 Table 2 仅报告 reward 百分比；正文作描述性比较。 | 未报告主效应的 F、df、p、效应量等统计检验。 |
| B6 | 交互作用 | 0 | PDF p.8 Table 2 与正文按模型/条件描述差异，但无交互项 F、df、p 或简单效应分析。 | 勉强有多因素比较结构，但完全未报告交互统计检验。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量及区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理分配研究；主要为数据集/benchmark 与模拟评估。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理设计，因而不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 研究单位未被随机分配到互斥处理条件；条件为固定 benchmark/独立模拟设置，没有可编码的随机分配机制。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序设计；Section 3 的提示变体为独立离线生成比较。 |
| C3 | 恒定 | 0.5 | PDF p.3 固定 Llama-3.1-70b；p.7 固定 gpt-4o 作为 source；p.10 8.2 承认闭源模型可能变动。 | 列出部分恒定变量，但未系统报告温度、解码设置、API 日期/版本等恒定水平。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为协变量/区组纳入统计模型。 |
| C6 | 盲法 | NA | — | 主要条件无需人类被试/评分者盲法；人类标注的盲法属于 F3/E5 而非处理盲法。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡、拉丁方或 ABBA 等顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 每条件独立生成/模拟，无跨条件练习块或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳设计；LLM 模拟也没有需要休息间隔的连续被试任务。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件间无跨条件残留或清洗期设计；每个模拟访谈独立重置。 |
| D4 | 不对称迁移 | NA | — | 不存在被试内条件迁移对称性问题。 |
| D5 | 范围效应 | 0 | PDF p.7: 'Five participants... rating their own persuasion levels turn-by-turn on a five-point scale across 72 trials'。 | 人类验证使用 5 点量表反复自评，存在范围效应/锚定风险，但未讨论或采用被试间对照、绝对锚。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选项或刺激序列的位置/顺序随机化设计；few-shot 排列问题归入 J5。 |
| E2 | 默认赞同 | NA | — | 未使用多题项 Likert/态度自评量表；persuasion 为单一 5 点评分，不适用反向题一致性检查。 |
| E3 | 极端 / 中间反应倾向 | 0 | PDF p.7 仅报告 5 点评分的相关 r=.43 等，未报告分布、偏度或端点/中点使用比例。 | 使用了等级评分但未报告反应分布形态，也未讨论极端/中间反应倾向。 |
| E4 | 需求特征 | 0 | PDF p.7 人类被试直接进行 persuasion 自评；未报告 cover story、盲法或事后假设推断访谈。 | 人类验证参与者可推测研究关注 persuasion，但论文未检查需求特征或 debriefing。 |
| E5 | 实验者效应 | 0.5 | PDF p.3: 'blindly annotated ten interviews, achieving a κ = .6'；p.7 人类 trials 未报告主试盲法/培训。 | 标注环节有部分盲法，但人类 persuasion trials 的施盲、评分者培训与脚本化程度未充分报告。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.4 Table 1 exact match 3.6%-8.2%，acknowledgement 接近 0；p.8 easy 条件 reward 达 84.7%。 | 可见低端/高端端点堆积迹象，但未报告 SD/偏度/端点频率，也未说明 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | IV 与 DV 不是同源自陈量表；不适用共同方法偏差程序/统计控制。 |
| F1 | 统计结论效度 | 0.5 | PDF p.7 报告 r=.43, p<.0001 并提及 power analysis；p.4/p.8 主要结果为百分比，无 CI 或多重校正。 | 部分效应量与验证性功效分析存在，但主比较缺置信区间、系统多重性校正与所有分析假设检验。 |
| F2 | 内部效度 | 0 | PDF p.8 Table 2 的 ablations 为条件比较，但未报告随机分配、分配隐藏、基线等价或试次流向。 | 模拟/消融比较没有随机化或内部效度威胁控制，按适用设计记 0。 |
| F3 | 构念效度 | 0.5 | PDF p.3 κ=.6、LLM 标注 f1=.8；p.7 source persuasion 与人类评分 r=.43；p.3 人工角色识别验证 >98%。 | 报告了部分信度/验证证据，但缺少提示变体操纵检验与完整构念效度论证。 |
| F4 | 外部效度 | 0.5 | PDF p.2-3 数据集来自 NPR/CNN 的 45,848 个访谈；p.10 8.3 讨论模拟环境简化与风险。 | 样本来源与限制有报告，但没有代表性抽样、明确推广边界或跨情境复现。 |
| G1 | 分析单位 | 0 | PDF p.3 每个样本由同一访谈前 t−1 轮生成下一问；p.4 Table 1 以问题为单位聚合，未建模问题嵌套于访谈。 | 分析层级与数据生成层级不匹配，未处理同一访谈多轮/多问题造成的聚集。 |
| G2 | 随机效应 | 0 | PDF p.4 Table 1 与 p.8 Table 2 仅报告聚合百分比；全文无混合模型或随机效应结构。 | 未说明访谈/问题/模型等因子何为随机效应，存在把聚类当独立观测的风险。 |
| G3 | 材料作为随机效应 | 0 | PDF p.3 使用具体访谈作为上下文材料，p.4 汇总问题对齐百分比；未将材料/访谈作随机效应。 | 材料被当作固定集合，未用 item random effect 或准 F 比来支持对材料总体的推广。 |
| G4 | 统计功效 | 0.5 | PDF p.7: 'a power analysis following guidelines from Card et al. (2020) showed our sample size was adequate'；但无目标功效/预期效应量细节。 | 仅人类验证有笼统功效说明，主 LLM 实验无事前功效分析或 CI。 |
| G5 | 研究者自由度 | 0.5 | PDF p.15 B.3 报告关键词过滤、长度过滤和最终样本量；p.7 报告 450 interviews、72 trials；未区分全部探索性/验证性分析。 | 报告了部分排除与样本决定，但未完整覆盖所有因变量、条件与可选停止/分析选择自由度。 |
| G6 | 预先设定 / 预注册 | 0 | PDF 全文未出现预注册平台、编号或数据收集前分析计划。 | 无预注册；按规则适用时缺失记 0，而非 NA。 |
| J1 | 位置偏差 | NA | — | LLM 判定用于相似性/话语分类，不是候选位置下的选择、排序或成对偏好比较，不涉及位置偏差。 |
| J2 | 冗长偏差 | NA | — | LLM 判定对象是问题对齐/话语分类，不是开放性生成质量评分或长短回答优劣比较。 |
| J3 | 谄媚 | NA | — | 未操纵用户先验立场或纠错反馈来测量谄媚；persuasion 任务不等于 sycophancy 评估。 |
| J4 | 自我偏好 | 0.5 | PDF p.3: 'We ask an LLM, GPT-4o, to perform this assessment'；p.31 使用 Llama-3.1-70b 标注 discourse，而 Section 3 生成也使用 Llama-3.1-70b。 | 关键一致性判定使用异源 GPT-4o，但话语标注存在生成模型与裁判同源风险；未量化 self-preference 或匿名化检验。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF p.21-25 source prompt 包含 persona_few_shot_examples 与固定示例；p.29 也使用 few_shot 块。 | few-shot 示例与模板有展示，但未报告示例抽样、多 seed 重采样、排列反平衡或与测试集隔离。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.15 B.5、p.21-30 提供大量处理与游戏提示模板；未报告版本号、敏感性消融或 dev/test 划分。 | 完整模板部分可得，但提示工程自由度控制不足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短访谈历史；虽有信息项检索，但没有长文档/RAG 关键信息位置操纵或窗口长度断言。 |
| J8 | 温度与采样随机性 | 0 | PDF p.7 列出模型名（gpt-4o、gpt-4o-mini、Llama-3.1-70b、Llama-3.1-8b），但未报告 temperature、top-p、seed 或重复采样方差。 | 未记录 LLM 采样随机性；stochastic Beta 信息返回机制不等于 LLM 解码采样报告。 |
| J9 | 重复与文本退化 | 0 | PDF p.7 仅提及 minimal self-reflection 与 hallucinations，未报告解码策略、repetition penalty、重复率或退化 QC。 | 开放生成任务但未控制或报告重复/文本退化。 |
| J10 | 分词效应 | NA | — | 单语言英语研究，无跨语言/跨脚本比较，不适用分词器效应编码。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.2-3 使用公开 NPR/CNN 访谈构建数据集；未报告模型训练截止日期、污染检测或 n-gram 重叠。 | 材料来自公开新闻文本，污染风险实际存在但未评估。 |
| J12 | 基准饱和 | 0.5 | PDF p.4 Table 1 exact match 约 3.6%-8.2%；p.8 Table 2 full game 约 42%-50%，easy 80%以上；无 SOTA 或 CI 比较。 | 报告了当前分数量级，但未系统评估饱和风险或采用连续指标/置信区间比较。 |
| J13 | 指令遵循 | NA | — | 指令遵循不是因变量；论文未以约束型指令遵循准确率为主要评估目标。 |
| J14 | 输出格式约束 / 结构化输出 | 0 | PDF p.15-19 多处要求把最终回答放入方括号；未报告格式合法率、重试策略或格式失败独立指标。 | 存在结构化输出约束，但格式合法率与内容错误未分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文将 LLM 作为对话 agent/NLP benchmark 评估，不主张测量人类心理学构念或把模型当心理学被试。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随规模/训练进展的涌现曲线，也不宣称突然涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对代理指标进行训练/RL/best-of-N 优化并监控 overoptimization。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.3/p.7 报告模型名和 450 次模拟、72 trials；p.10 8.2 承认闭源模型不可复现；无精确 snapshot/date、无主结果 CI 或配对检验。 | 有重复/样本量信息，但 checkpoint/snapshot 与不确定性报告不足。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF p.8 Figure 5 报告 reward across turns 与 total reward；游戏为 K 轮多轮对话。 | 进行了多轮评估并按轮次展示 reward，但未报告上下文截断策略或指令一致性随轮次衰减的独立/累积评分。 |

## 编码小结
论文提供了较丰富的数据、提示词与模拟环境描述，但多数人类实验设计组件（随机分配、平衡、盲法、功效、预注册等）不适用于其主要 LLM benchmark 结构；同时 LLM 评估关键再现信息（采样参数、snapshot、重复与置信区间、随机效应/聚类处理、污染检查）报告不足。多数适用组件只能给 0.5 或 0。
