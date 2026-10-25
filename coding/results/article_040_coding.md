# article_040 | How Well Can LLMs Negotiate? NegotiationArena Platform and Analysis | 2024

研究类型概述：LLM 多智能体谈判基准与行为评估研究；分析单位是单局谈判（game/trial），主要操纵或系统比较模型配对与先后手、游戏场景、社会行为提示、游戏参数与金额尺度；因变量为解析后的胜率、平均收益、接受概率、最终价格等。不是人类被试实验，而是基于 LLM API 的零样本多轮对话模拟与描述性/部分推断性比较。
- **研究构念（Construct）**：谈判策略、锚定、让步与社会决策（negotiation strategy, anchoring, concession, and social decision-making）｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：LLM 多智能体谈判基准与行为评估研究；分析单位是单局谈判（game/trial），主要操纵或系统比较模型配对与先后手、游戏场景、社会行为提示、游戏参数与金额尺度；因变量为解析后的胜率、平均收益、接受概率、最终价格等。不是人类被试实验，而是基于 LLM API 的零样本多轮对话模拟与描述性/部分推断性比较。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3: 'We compare both permutations of agents'; p.6: 'We prompt GPT4 with the additional personas: ... (Cunning) and ... (Desperate)'; p.16 Appendix F gives exact social prompts. | 核心自变量被命名并给出至少两个水平及取值/标签，操纵程序也有提示词；但未报告随机分配方式或操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.3: 'We report two main metrics: win rate and average payoff'; p.15 Tables 4-5 report payoffs with confidence intervals. | 因变量指标和计分方式清楚，并报告了部分均值/CI；但无信度、效度证据，也无连续指标预处理/天花板地板说明。 |
| A3 | 控制变量 | 0.5 | p.12 Appendix A: 'Both GPT and Claude are using a temperature of 0.7 and ... a maximum of 400 tokens'; p.3 gives model versions; p.6 fixes Player 1 as GPT-4. | 报告了温度、最大长度、模型版本和部分角色固定等控制手段，但不是系统控制变量清单，也未逐一说明控制方式。 |
| A4 | 混淆变量 | 0.5 | p.5: 'the order in which an agent goes and its role matters'; p.12: 'our prompts are slightly biased towards Claude'. | 识别了先后手/角色和 prompt 偏向等潜在混淆，并用双方排列部分控制；但未系统报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有提出并检验调节假设；社会行为跨游戏比较是分组描述，不是正式调节/交互模型。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p.2 Tables 1-3 describe game structures; p.3 specifies XML-like communication tags; p.17 Figure 21 gives a complete system prompt; p.7 operationalizes anchoring via initial-final price correlation. | 主要游戏规则、提示格式、社会提示和指标操作化较清楚，但未逐构念给出完整、统一的操纵与计分程序，部分构念仍是描述性。 |
| A8 | 水平数与类型 | 0.5 | p.3 lists four models and both role permutations; p.6 gives three social-behavior levels; p.7 describes buyer valuation manipulation and p.8 describes 2-turn vs 3-turn ultimatum. | 报告了多个自变量的水平数和标签，但缺少水平类型、间距/全距及连续变量中心化/标准化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.3-p.4 use win rate and payoff across three scenarios；p.6 social behavior each used one persona prompt; p.7 uses multiple dependent measures. | 谈判能力通过多场景、多指标部分多操作化，但社会行为只用了单一提示版本，且未讨论单一操作化对可推广性的限制。 |
| A10 | 单一方法的风险 | NA | — | IV 是提示/模型条件，DV 是解析后的博弈结果，不是自陈量表同源测量；共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立组分配；同一模型在多个对局和条件下被重复评估，不属于经典被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有参与者层面的被试内条件序列与顺序平衡；每一局是独立多轮会话，角色先后手由双方排列处理。 |
| B3 | 混合设计 | NA | — | 未使用组间/组内混合设计及相应混合模型或重复测量 ANOVA。 |
| B4 | 因子设计 | 0 | p.3-p.4 report multi-model pair matrices and p.6 reports a three-level social-behavior manipulation, but no ANOVA/design matrix with interaction statistics. | 存在多因素交叉比较，但未报告正式交互项、完整设计矩阵或 ANOVA 表；按因子设计完整性标准判为 0。 |
| B5 | 主效应 | 0.5 | p.4 reports model/role comparisons descriptively and p.15 gives payoff confidence intervals; p.7 gives one binomial p-value for over-valued buyer. | 报告了模型、角色等主效应的描述性结果和部分 CI，但没有正式 F/df/p/效应量，故不完整。 |
| B6 | 交互作用 | 0 | p.4 Fig.3 and p.6 Fig.8 present matrices/panels but no interaction F/df/p or simple-effects tests. | 没有对交互项做统计检验，也没有系统简单效应或多重比较校正。 |
| B7 | 区组设计 | NA | — | 无区组或分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 无人类准实验分组；模型比较不是非随机分组的选择偏差设计，未按准实验类型报告。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理条件设计，因此不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | 0 | p.3: 'We run 60 negotiations for each ordered pair of agents in each scenario'; p.6: 'We run 80 games for each pair'; no random assignment method or random seed reported. | 条件分配按固定局数运行，未报告概率随机分配方法、随机数工具或分配隐藏。 |
| C2 | 平衡 | 0.5 | p.3: 'Since being either the first or the second agent has an impact ... we compare both permutations of agents'; 60 negotiations per ordered pair. | 用双方角色排列平衡先后手，并给出每排列局数；但没有迁移对称性前提论证。 |
| C3 | 恒定 | 0.5 | p.12 Appendix A: temperature 0.7 and max 400 tokens; p.3 gives gpt-4-1106-preview and gpt-3.5-turbo-1106; p.6 fixes Player 1 as GPT-4 in social-behavior experiments. | 列出多个恒定条件与水平，但未系统讨论这些恒定所带来的外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未将已知混淆变量作为协变量或区组纳入模型；角色/先后手主要靠排列比较，而非 ANCOVA。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人类评分者，盲法不适用。 |
| C7 | 平衡的层级 | 0.5 | p.3 reports both permutations for first/second agent and 60 games per ordered pair, but does not name a formal balancing level or construction method. | 实际上做了双方角色完整排列，但未明确报告平衡层级、构造方法或顺序效应形状假设。 |
| D1 | 练习效应 | NA | — | 每局是独立 LLM 会话，跨局无练习块或试次阶段；练习效应不适用。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳，且任务为短时 API 调用，不涉及休息间隔或 session 疲劳控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同条件为独立对局，未报告跨条件残留或清洗期问题，迁移效应不适用。 |
| D4 | 不对称迁移 | NA | — | 无跨条件处理顺序，因此无不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观支付/价格/接受概率，不是被试内绝对判断或李克特量表。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.3: 'we compare both permutations of agents ... We run 60 negotiations for each ordered pair'; p.5 discusses first/second agent and anchoring. | 对先/后手做了双方排列并给出每排列局数，但没有报告随机化方案类型、完整位置×结果曲线或逐位置分配细节。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 全自动 LLM API 调用，无人类主试或评分者，实验者效应不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.4 Fig.3 shows win rates including 1.00; p.15 Tables 4-5 give payoffs with CIs; p.8 Fig.11 acceptance probability ≈1.0; no pilot difficulty calibration reported. | 报告了均值/CI 及部分端点概率，可观察到天花板现象，但未报告偏度、端点频率统计或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 没有多构念自陈式同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.15 Tables 4-5 report payoffs with confidence intervals; p.7 reports p-value < 0.05 for one comparison; no power analysis or multiplicity correction reported. | 报告了部分效应量/CI 与个别 p 值，但缺样本量确定依据、全部分析报告和多重性校正。 |
| F2 | 内部效度 | 0.5 | p.3 reports both permutations and fixed number of games; p.12 discusses prompt bias and limitations; no allocation concealment, baseline equivalence, or participant flow. | 报告了基本条件安排并评估了部分内部效度威胁，但缺随机分配、分配隐藏、基线等价性和损耗/中断流程。 |
| F3 | 构念效度 | 0.5 | p.7 anchors analysis to known game-theoretic rationality and human findings; p.12 notes prompt bias and instruction-following failures; no formal reliability or manipulation check. | 用已知博弈理性基准和人类文献提供一定效度参照，但无信度指标、操纵检验或系统构念效度论证。 |
| F4 | 外部效度 | 0.5 | p.3 lists model versions and scenarios; p.12 discusses prompt bias and model instruction-following limitations; no representative sampling or cross-context replication. | 报告了模型来源/版本与场景边界，但未系统说明推广边界或跨样本/跨情境复现。 |
| G1 | 分析单位 | 0.5 | p.3: 60 negotiations per ordered pair; outcomes aggregated per model pair/game; p.15 CI computed over games. No explicit nested model for games within model-pair. | 明确分析单位是单局并按模型对聚合，但未显式处理局嵌套于模型对/场景的聚集结构。 |
| G2 | 随机效应 | NA | — | 主要分析为游戏层聚合，模型被视为固定比较对象而非从模型总体随机抽样；无混合模型需求。 |
| G3 | 材料作为随机效应 | NA | — | 游戏场景与规则是固定的平台材料，不把具体材料作为从材料总体抽样的随机因子。 |
| G4 | 统计功效 | 0 | p.3, p.6, p.7 give 60/80/100/20 games per condition but no a priori power analysis or sample-size rationale. | 无事前功效分析或其他样本量论证；仅报告了局数。 |
| G5 | 研究者自由度 | 0.5 | p.3 says win rate ignores ties; p.12 notes some games break because models use wrong tags; no count of broken games or clear exploratory/confirmatory distinction. | 报告了平局排除和格式中断规则，但未报告中断数量、样本量决定方式，也未系统区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement or registry link found in the article. | 无预注册或时间戳早于数据收集的分析计划。 |
| J1 | 位置偏差 | NA | — | 不涉及候选选项选择、排序或 LLM-as-judge 成对比较；先后手问题已在 E1/C2 处理。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估生成质量，无长度偏差评分问题。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错式对话；多智能体谈判不测量谄媚。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 作为裁判或评估者。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，无 few-shot in-context 示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.17 Figure 21 provides a complete system prompt; p.12 admits prompts can bias and were adapted for Claude; no sensitivity ablation or dev/test split reported. | 公布了完整 prompt 示例并讨论 prompt 偏向，但无版本化、语义等价措辞敏感性消融或 dev/test 分离。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短多轮游戏，无长文档、RAG 或中间迷失实验。 |
| J8 | 温度与采样随机性 | 0.5 | p.12 Appendix A: temperature 0.7, maximum 400 tokens; p.3 gives model snapshots; p.15 gives payoff CIs; no seed/top-p details. | 报告了主要采样参数、模型版本和部分 CI，但缺随机种子、top-p/top-k 以及所有条件下的重复采样 CI 说明。 |
| J9 | 重复与文本退化 | 0.5 | p.12 gives temperature 0.7 and max 400 tokens; p.3 says strict parser interrupts games on format failure; no repetition penalty or degeneration rate reported. | 报告了基本解码设置和长度上限，但未报告 repetition penalty、n-gram 重复率/退化率。 |
| J10 | 分词效应 | NA | — | 单语言英语实验，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.8: 'Considering the game’s popularity, it is likely that the model has seen instances ... during training'; no formal contamination test rate. | 识别了 Ultimatum 游戏可能被训练语料见过并讨论记忆/泛化，但没有做污染检测或报告污染率。 |
| J12 | 基准饱和 | 0.5 | p.4 Fig.3 contains win rates of 1.00; p.8 Fig.11 acceptance probability ≈1.0; p.4 and p.15 also use continuous payoff/CIs. | 报告了接近天花板的结果并使用连续 payoff 作为补充，但未正式进行饱和诊断或模型间 CI 比较。 |
| J13 | 指令遵循 | NA | — | 论文不以指令遵循为因变量；仅把 GPT-3.5 等指令错误作为行为/混淆讨论。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.3 describes XML-like tags and: 'games are interrupted if one of the agents does not behave as expected'; no format-valid rate or retry policy reported. | 有强制结构化输出格式与严格解析，但未报告格式合法率、重试次数或格式失败与内容错误的分离指标。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 cites theory of mind and irrationality; p.8 says analysis assesses 'to what extent LLM agents mirror human irrationalities'; p.9 compares with human negotiation literature; no new human comparison experiment. | 将 LLM 谈判/非理性与人类同名构念作了类比并报告模型版本，但没有系统人类对照或完整构念效度论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无 RL、best-of-N 或对代理指标的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.3 gives model versions and 60/80 games; p.15 gives CIs; p.17 gives prompts; no random seeds, paired tests or raw logs reported. | 报告了部分重复次数、模型版本、CI 和 prompt，但缺精确 snapshot 日期/种子、配对检验和原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.2 says 8 or 10 rounds of interaction; p.8 compares classical 2-turn vs 3-turn ultimatum and analyzes acceptance at the penultimate turn; p.15 analyzes sequential proposals. | 确实做了多轮谈判并分析轮次动态，但未系统按每轮独立/累积评分、报告上下文截断或固定每轮评分协议。 |

## 编码小结
论文提出了可复现的 NegotiationArena 平台，系统比较多个 LLM 在多类多轮谈判游戏中的行为，并公开部分 prompt 与结果，具有较强的方法描述价值。主要不足是推断性设计与报告不完整：缺少随机分配、功效分析、预注册、正式交互/混合模型分析、采样种子和多重性校正，部分构念只靠单一提示操作且未做操纵检验或信效度论证。
