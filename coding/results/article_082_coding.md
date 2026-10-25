# article_082 | Investigating and Extending Homans’ Social Exchange Theory with Large Language Model based Agents | 2025

研究类型概述：多智能体 LLM 模拟研究：构建 3 个 LLM 智能体的虚拟社会，观察并验证 Homans 社会交换理论六命题；进一步通过提示设定比较理性/经验认知风格与亲自我/亲社会价值取向，并考察信任违约后的系统韧性；另含 3 名人类与 LLM 智能体的小样本对照。分析单位主要是模拟运行、智能体角色与轮次，而非经典随机对照人类被试实验。
- **研究构念（Construct）**：Homans社会交换理论下的交换价值、互惠、信任违约与亲社会/自利行为｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：多智能体 LLM 模拟研究：构建 3 个 LLM 智能体的虚拟社会，观察并验证 Homans 社会交换理论六命题；进一步通过提示设定比较理性/经验认知风格与亲自我/亲社会价值取向，并考察信任违约后的系统韧性；另含 3 名人类与 LLM 智能体的小样本对照。分析单位主要是模拟运行、智能体角色与轮次，而非经典随机对照人类被试实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.6: 'we first set the agents to operate in either a completely rational or a completely experiential manner and then systematically compare their behaviors'; PDF p.7: 'setting the agents to be Proself and Prosocial, respectively'; PDF p.4: 'each experiment is repeated for five times'. | 认知风格与 SVO 被明确命名并给出至少两个水平，属于研究者设定的条件；但未完整说明条件分配到模拟单位的具体逻辑、随机化方式及操纵检验，故为核心达成但报告不全。 |
| A2 | 因变量 | 0.5 | PDF p.4: 'We measure exchange behaviors through "exchange value," which represents the total value of resources involved in each transaction (sum of incoming and outgoing resources)'; PDF p.4: 'The value coefficients r1, r2 and r3 are set as 1, 4 and 9'; PDF p.3: affinity scores 'ranging from 1 to 5'. | 因变量指标与计分方式有明确界定，包括交换价值、资源价值和 1–5 亲和分数；但未报告信度、效度、条目/评分者一致性及连续指标预处理或天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | PDF p.4: 'M = N = 3'; 'I = 5'; 'S = 15'; 'We use Claude-3.5-sonnet as the base LLM'; PDF p.12: 'Temperature: 0.5', 'Maximum tokens: 8192', 'Top-p: 0.9'. | 报告了多项固定设置与恒定参数，但未以系统控制变量清单形式逐一说明控制手段、控制效果或基线检查，因此只算部分满足。 |
| A4 | 混淆变量 | 0 | PDF p.9: limitations mention 'simplified' environment, 'LLM API cost constraints', 'cultural factors' and English-only conduct; no explicit confound identification/control discussion. | 局限部分讨论的是外部效度与成本，不足以构成对潜在混淆变量的识别、控制方式和残余混淆威胁的说明；全文未系统处理内部效度混淆。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节假设或调节分析；认知风格与 SVO 是操纵/比较条件，而非被界定的调节变量并做交互检验，故不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介假设、a/b 路径或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 0.5 | PDF p.4: exchange value defined as 'sum of incoming and outgoing resources'; PDF p.3: REI scores '1 to 5', SVO implemented 'through pre-defined LLM prompting templates'; PDF p.13-15: Appendix C gives several agent prompts. | 核心指标和部分智能体构念有操作化说明，且附录给出提示模板；但理性/经验与亲自我/亲社会的完整提示文本、参数化和评分实现未完全逐构念复现，因此操作化不完整。 |
| A8 | 水平数与类型 | 0.5 | PDF p.6: rational vs experiential; PDF p.7: Proself vs Prosocial; PDF p.5: breach categories '0-5 breach value', '5-10', '10-15'; PDF p.4: resource values r1=1, r2=4, r3=9. | 报告了主要条件的水平数与取值/标签；但未系统说明水平类型、间距/全距及连续变量中心化等，信任违约严重度还更像观察分组而非严格操纵水平。 |
| A9 | 单一操作化的风险 | 0 | PDF p.6-8: key outcomes mainly single exchange-value/affinity/breach metrics; PDF p.9 limitations discuss simplification/cost/culture but not single-operationalization generalizability. | 关键构念基本依赖单一操作性指标，且全文未讨论单一操作化对可推广性的具体限制，也未报告多操作会聚证据。 |
| A10 | 单一方法的风险 | 0 | PDF p.6-8: agent profile conditions and behavioral outcomes are generated within the same LLM interaction pipeline; no common-method bias procedure or statistical test reported. | 自变量由 LLM 提示设定、因变量也来自同一 LLM 交互输出，方法来源同源；论文未报告 Harman、ULMC、marker variable 等共同方法偏差检验或程序控制。 |
| B1 | 被试间设计 | 0.5 | PDF p.6: 'set the agents to operate in either a completely rational or a completely experiential manner'; PDF p.7: 'setting the agents to be Proself and Prosocial, respectively'; PDF p.4: 'each experiment is repeated for five times'. | 可推断不同条件通过独立模拟运行比较，每个条件重复五次；但未明确写出被试间/运行间分配逻辑、各组样本量与随机分配程序。按 LLM 分析单位，属部分报告。 |
| B2 | 被试内设计 | NA | — | 主要条件为不同模拟/智能体配置间的比较，不存在同一智能体接受所有实验条件并需平衡顺序的被试内设计；轮次变化属于纵向观察而非条件平衡。 |
| B3 | 混合设计 | NA | — | 论文没有同时包含组间与组内因素的正式混合设计，也没有相应混合模型/误差项。 |
| B4 | 因子设计 | NA | — | 认知风格、SVO 与信任违约并非完全交叉的因子设计，未给出设计矩阵或交互项，故不适用。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应检验；认知风格/SVO 比较主要是描述性结果，缺少正式 ANOVA/模型统计量。 |
| B6 | 交互作用 | NA | — | 无正式交互项检验，也不存在可编码的因子交互设计。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计，也没有区组变量与区内分配程序。 |
| B8 | 拉丁方 | NA | — | 无被试内条件顺序设计，未使用拉丁方。 |
| B9 | 准实验设计 | NA | — | 3 名人类与 LLM 的对照是小样本模式一致性比较，未作为准实验因果设计报告，也未提出因果处理效应；因此不按准实验设计编码。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内条件设计，不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | 0 | PDF p.6-7: conditions are created by 'setting the agents' to rational/experiential and Proself/Prosocial; PDF p.4 only says 'each experiment is repeated for five times'. | 条件由预定义提示固定设定，未报告概率随机分配方法、随机数工具或分配隐藏；对多条件模拟而言随机化质量未报告。 |
| C2 | 平衡 | NA | — | 主要条件为不同模拟运行间的比较，不存在需要 ABBA/拉丁方平衡的条件顺序。 |
| C3 | 恒定 | 1 | PDF p.4: 'M = N = 3'; resource values 'r1, r2 and r3 are set as 1, 4 and 9'; 'I = 5'; 'S = 15'; 'Claude-3.5-sonnet'; PDF p.12: temperature, max tokens, top-p; PDF p.9 discusses simplified environment and cultural/linguistic limitations. | 明确列出多个恒定变量及其水平，并报告模型与采样参数；局限部分也讨论了简化情境和文化/语言外部效度限制，满足恒定控制要求。 |
| C4 | 匹配 | NA | — | 未使用匹配设计，也没有匹配变量、匹配方法或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 论文没有将已知混淆变量作为协变量或区组纳入分析；资源丰度和违约严重度是结果分组/观察变量，不是协变量控制。 |
| C6 | 盲法 | NA | — | 主分析为自动化 LLM 多智能体模拟，无人类条件分配需盲法；辅助 3 人研究也未设置人类被试条件组，故不按盲法设计编码。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡，不涉及完全平衡、拉丁方或 ABBA 层级选择。 |
| D1 | 练习效应 | NA | — | 研究没有练习块或前段试次截除设计；轮次中的学习/策略变化本身是观察对象，而非需要抵消的练习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 模拟不受人类疲劳影响；无 session 时长、休息间隔等疲劳控制需求。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同条件在不共享上下文的独立模拟中运行；没有跨条件清洗期或迁移污染问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件重复测量/交叉设计，不涉及不对称迁移检验。 |
| D5 | 范围效应 | NA | — | 主要因变量为交换价值、资源价值、接受率等客观模拟指标；虽含 LLM 生成的 1–5 亲和评分，但不属于人类被试内绝对量表判断的范围效应设计。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF p.3-4: negotiation proceeds with 'up to three rounds of discussions' and a 'structured format as presented in Figure 2'; no randomization or counterbalancing of agent/proposal order is reported; PDF p.12 lists only model parameters. | 多智能体协商涉及固定顺序的发言/提案与多个可选回应，但论文未报告对智能体顺序、提案顺序或刺激顺序做随机化/反平衡，也未讨论顺序效应。 |
| E2 | 默认赞同 | NA | — | 研究不使用人类 Likert/态度自评量表；亲和分是 LLM 依据规则更新的 1–5 评分，不涉及默认赞同的正反向题设计。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有跨群体/跨文化的人类等级量表得分分布比较，不需要极端/中间反应倾向校正。 |
| E4 | 需求特征 | 0 | PDF p.11: human participants receive 'the manual, signed informed consent forms' and 'a guided walkthrough'; no cover story or post-experimental hypothesis-inference check is reported. | 辅助人类研究未报告掩饰情节/盲法，也未做事后访谈检查参与者是否推断出研究假设；任务目标较透明，需求特征风险未被控制。 |
| E5 | 实验者效应 | 0 | PDF p.11: manual and 'guided walkthrough of the trading interface' are described for human participants; no experimenter/rater blinding, training standardization, or rater count is reported. | 虽提供了统一手册与练习，但未报告主试/评分者盲法层级、主试人数、培训标准化或脚本化程度，无法满足实验者效应控制要求。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.16 Tables 1–3 report mean exchange values and percentage changes; PDF p.7 reports Proself/Prosocial 'µ = 300.3, σ = 108.8' vs 'µ = 343.0, σ = 84.1'; no skew/endpoint frequency or pilot difficulty calibration. | 报告了均值、标准差或标准误，可用于初步检查量程；但未报告偏度、端点频率或预实验难度校准，无法充分排除天花板/地板效应。 |
| E7 | 共同方法偏差 | 0 | PDF p.6-8: independent variables are prompt-set agent profiles and dependent variables are modeled behaviors from the same LLM interaction; no common-method bias program control or statistical test is reported. | 自变量与因变量同源于 LLM 交互与模型输出，且未报告共同方法偏差的程序控制或统计检验，也未讨论同源比例。 |
| F1 | 统计结论效度 | 0 | PDF p.4: 'each experiment is repeated for five times, and we report the average results and their standard errors'; PDF p.16 reports means and percentage changes but no inferential tests, effect sizes, or confidence intervals. | 仅有五重复均值和标准误，没有样本量确定依据、正式效应量/95%CI、统计检验或多重性校正；不满足统计结论效度核心要求。 |
| F2 | 内部效度 | 0 | PDF p.6-7: conditions are set by prompts; PDF p.4 reports only five repetitions; PDF p.9 limitations mention simplification/cost but not allocation concealment, baseline equivalence, or attrition. | 没有随机分配程序、分配隐藏、基线等价性检验或被试/运行流向与损耗处理；内部效度威胁未被系统评估。 |
| F3 | 构念效度 | 0 | PDF p.4 defines exchange value and resource scoring; PDF p.6-8 compare behaviors descriptively; no reliability, validity, manipulation check, or multi-operationalization evidence is reported. | 关键测量虽有一定定义，但缺少信度、效度、操纵检验和多操作化会聚证据，构念与指标对应关系未充分论证。 |
| F4 | 外部效度 | 0.5 | PDF p.7: 'We recruited three human participants'; PDF p.9 discusses simplified environment, cost, cultural/linguistic limitations and future larger-scale work; PDF p.16 reports additional GPT-4o and OLMo-2 validation. | 报告了人类样本来源和模型来源，并做了跨模型补充验证与推广边界讨论；但人类样本仅 3 名研究生、代表性不足，跨情境复现有限。 |
| G1 | 分析单位 | 0.5 | PDF p.4: 'each experiment is repeated for five times, and we report the average results and their standard errors'; PDF p.5 and p.8 plot per-round and per-agent outcomes. | 存在轮次嵌套于智能体、智能体嵌套于模拟社会的聚集结构；论文以五重复均值/标准误和逐轮聚合呈现，未明确说明分析层级或使用多层模型分离聚集方差。 |
| G2 | 随机效应 | NA | — | 论文没有混合模型或随机效应推断；3 个智能体是固定角色实例而非从智能体总体抽样，主要结论为描述性模拟模式，故不按随机效应模型要求编码。 |
| G3 | 材料作为随机效应 | NA | — | 资源类型 A/B/C 是固定的 3 类资源，不是从材料总体抽样的语言项目；没有项目随机效应或 F1/F2 推广问题。 |
| G4 | 统计功效 | 0 | PDF p.4: five repetitions are used but no power analysis is reported; PDF p.16 reports means without effect sizes or confidence intervals. | 无设计阶段功效分析、目标功效、预期效应量来源或样本量推导；结果也未系统报告效应量与 CI。 |
| G5 | 研究者自由度 | 0 | PDF p.4 and p.9 mention five repetitions and API cost constraints but do not report exclusion rules, all measured DVs/conditions, stopping rules, or confirmatory/exploratory separation. | 未完整报告试次/模拟剔除标准、全部因变量与条件、样本量决定方式或是否中途停止；验证性与探索性分析也没有明确标注。 |
| G6 | 预先设定 / 预注册 | 0 | PDF p.1-9: no pre-registration platform, registration number, or pre-specified analysis plan is reported. | 全文没有公开预注册或时间戳早于数据收集的分析计划；不满足预注册要求。 |
| J1 | 位置偏差 | NA | — | 研究不是 LLM-as-judge、成对比较或候选答案位置实验；虽有多智能体提案顺序问题，但已在 E1 编码，J1 的候选位置/裁判偏差结构不适用。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放生成质量，也不比较回答长度与质量，故不适用。 |
| J3 | 谄媚 | NA | — | 实验不涉及用户先验立场、反馈纠错或多轮谄媚操纵；智能体协商不是 user-stance sycophancy 评估。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 对被评模型输出做评分或成对比较，因此不存在自我偏好裁判偏差编码对象。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 智能体提示不是 few-shot in-context learning 示例集；论文未使用 few-shot 示例选择与排列实验。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.13-15: Appendix C provides several full agent prompts ('Update BDI', 'Make Deal', 'Update Affinity', 'Determine to Continue', 'Reply'); PDF p.12 gives model parameters; no prompt version, sensitivity ablation, or dev/test split is reported. | 提供了较多提示模板与采样参数，但缺少版本号/迭代日期、语义等价措辞敏感性检验和 dev/test 划分；profile-specific 提示细节也未完全展开，故为部分满足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为 10–20 轮、3 个智能体的短交互，远非长文档/RAG 场景，未声称长上下文位置效应，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.12: 'Model: claude-3-5-sonnet-20240620', 'Temperature: 0.5', 'Maximum tokens: 8192', 'Top-p: 0.9'; PDF p.4: 'each experiment is repeated for five times' and average/standard errors reported. | 报告了主要采样超参、模型 snapshot 和五重复运行；但未报告随机种子、top-k、repetition penalty、95%CI（仅有标准误）等，完整性不足。 |
| J9 | 重复与文本退化 | 0.5 | PDF p.12 reports temperature/top-p/max tokens but no explicit decoding strategy statement, repetition penalty, repetition rate, or truncation rate; PDF p.13-15 prompts require structured actions. | 采样参数有所报告，但未明确解码策略、重复惩罚/退化率、生成长度截断比例或条件间解码一致性，故只算部分满足。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文实验，没有跨语言/跨脚本输入比较，故分词器效应不适用。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 研究使用自建社会交换模拟任务，不是公开基准测试集；没有可评估的训练/测试重叠或基准污染问题。 |
| J12 | 基准饱和 | NA | — | 没有使用标准基准分数或接近天花板的基准水位，故基准饱和问题不适用。 |
| J13 | 指令遵循 | NA | — | 论文不以指令遵循为因变量，也不评估模型对约束指令的遵循准确率；提及 Claude 的 instruction-following 仅是选型理由。 |
| J14 | 输出格式约束 / 结构化输出 | 0 | PDF p.3-4: negotiation follows a 'structured format as presented in Figure 2' with actions such as PROPOSE/ACCEPT/REJECT/PASS; PDF p.15 prompt says 'Return empty "actions": [] if no action needed'; no format-validity rate or retry strategy is reported. | 实验要求结构化动作/JSON 样式输出，但未报告文法引导、格式合法率、重试策略，也未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全对齐、有害请求或越狱评估，故不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.1: 'demonstrating the consistency between the agent and human behaviors'; PDF p.7: human participants interact with two LLM agents 'under the same conditions'; PDF p.4 and p.16 report Claude/GPT-4o/OLMo models; PDF p.9 discusses cultural/linguistic bias. | 论文明确把 LLM 行为与人类社会交换构念作类比，并做了同范式人类对照与跨模型补充；但未系统论证 LLM 构念与人类同名构念的异同，仍有从智能体结果推及人类社会的表述，故为部分满足。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文不报告随模型规模/训练进展的能力曲线，也未宣称涌现能力，故不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不针对 benchmark、奖励模型或 LLM-judge 代理指标进行优化，无代理指标过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.4: 'each experiment is repeated for five times' and standard errors; PDF p.12: 'claude-3-5-sonnet-20240620'; PDF p.16 reports GPT-4o and OLMo-2 results but without explicit snapshot identifiers for all models. | 有重复次数、标准误和 Claude 精确 snapshot，但缺少种子、95%CI、配对检验、原始日志/提示集公开，GPT-4o 与 OLMo 的精确版本信息也不完整。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF p.3: society runs 'round-by-round' and negotiation has 'up to three rounds of discussions'; PDF p.5 and p.8 plot per-round exchange value/affinity over 10–20 rounds; PDF p.12 max tokens 8192; no context truncation report. | 确实进行了多轮交互并按轮次展示结果，但未系统区分单轮与多轮成绩、未报告历史是否被截断及每轮上下文长度，轮次轨迹的统计控制也不完整。 |

## 编码小结
论文把 LLM 智能体作为社会交换行为的模拟被试，提供了可复现的智能体框架、提示与基本实验参数，并报告了五重复均值/标准误及跨模型补充验证。但整体以描述性观察和模式解释为主，缺少正式统计检验、效应量与置信区间、随机化/分配隐藏、操纵检验、功效分析、预注册和多种效度证据；提示顺序、模型采样和嵌套结构报告不完整。
