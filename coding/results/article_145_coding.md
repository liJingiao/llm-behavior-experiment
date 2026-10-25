# article_145 | Reflection-Bench: Evaluating Epistemic Agency in Large Language Models | 2025

研究类型概述：这是一项LLM基准评测/观察性比较研究，而非人类被试实验。分析单位主要是模型×任务×提示策略的聚合得分（并含任务内多轮试次），比较16个主评测模型（另含Centaur及基座模型）在预测、决策、知觉、记忆、反事实思考、信念更新和元反思七类认知任务上的表现；操纵/比较提示策略与难度参数，模型和任务多为固定基准维度。
- **研究构念（Construct）**：认识能动性，包括预测、决策、知觉、记忆、反事实思考、信念更新和元反思｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：16个模型在双骰赌博、Iowa Gambling、概率反转、meta-bandit等七项文本化认知任务中跨多轮预测、选择、接收反馈、回忆与更新，并比较zero-shot、CoT与self-reflection。｜CA 任务锚定：爱荷华赌博任务（Iowa Gambling Task, `tsk_4a57abb949ae5`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'We implement three response formats ... free output, direct choice generation, and zero-shot CoT'; Table 1 (p.6) lists Easy/Hard parameters; Appendix A.1-A.8 (p.15-17) gives prompts. | 提示策略有三水平，难度有Easy/Hard两水平，任务参数也在Table 1给出，基本要件达成；但未报告操纵检验，且条件分配是固定/重复评测而非随机分配，故只能算0.5。 |
| A2 | 因变量 | 0.5 | p.4-5: scoring formulas such as 'Score = (1 − MAE/MaxMAE) * 100'; p.5: Oddball uses rule-based 0-3 manual scoring and embedding-based automated scoring; p.7: 'r=0.87' between human and automated Oddball scoring. | 各任务因变量指标和计分方式界定清楚；但多数构念缺少信度/效度证据，只有Oddball报告了人工与自动评分相关，且未系统报告连续指标的预处理、SD或端点。故为0.5。 |
| A3 | 控制变量 | 0.5 | p.6: Table 1 fixes p, x, n and Easy/Hard settings; p.6: 'we repeat most tasks twice. The Oddball task ... is repeated three times'; p.6 mentions context-length constraints. | 报告了固定任务参数、重复评测和部分上下文长度约束等控制，但未系统列出控制变量清单及逐一控制手段，因此为0.5。 |
| A4 | 混淆变量 | 0.5 | p.2: 'parameterized design ... reduces potential data contamination'; p.6: Centaur fine-tuned on human cognitive test data 'showed no improvement ... compared to its base model' as leakage check. | 明确识别了数据污染/泄漏这一潜在混淆并用参数化任务与Centaur对照缓解；但对其他混淆（如模型版本、提示差异、任务材料差异）的残余威胁讨论有限，故0.5。 |
| A5 | 调节变量 | NA | — | 理论模型没有调节变量假设，也未做正式调节效应/交互检验；提示策略与任务/模型的差异只是描述性比较，不按调节变量编码。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或因果链中介检验。 |
| A7 | 操作性定义 | 1 | p.4-5 describes each task procedure and scoring; p.15-17 Appendix A gives system prompts/examples for WPT, WCST, Oddball, N-back, DC-IGT, PRLT, MBT. | 七个认知维度均给出可执行的任务程序、输入输出格式、系统提示与评分方式，其他研究者可据此复现，达到操作性定义完整。 |
| A8 | 水平数与类型 | 0.5 | p.6 Table 1: Easy/Hard values for WPT p=0.9/0.8, WCST x=72/90, N-back n=2/4, etc.; p.6: three response formats. | 报告了主要条件的水平数与取值/标签；但未统一说明水平类型、间距、全距或连续变量中心化等，故为0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.4-5 each dimension uses one adapted cognitive test; p.9: 'the ecological validity of these adapted tasks may require further investigation'. | 关键构念基本是每维度单一任务操作化；作者在局限中简要讨论了生态效度/适用边界，但未系统讨论单一操作化的推广限制，也未提供多维会聚证据，故0.5。 |
| A10 | 单一方法的风险 | NA | — | 研究不是自陈量表式多构念测量；自变量为提示/任务条件，因变量为客观任务得分，CMB/同源自评问题不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试组间分配；同一模型被跨条件/任务评测，不存在独立被试组承担不同水平的人类被试间设计。 |
| B2 | 被试内设计 | 0.5 | p.6: 'we repeat most tasks twice'; p.7 Table 2 reports model-strategy pairs; p.6: same 16 models evaluated under three strategies. | 同一模型在多个提示策略/任务上被重复评测，具有重复测量性质；但未报告条件顺序安排或平衡方案，故0.5。 |
| B3 | 混合设计 | NA | — | 论文没有按人类混合设计逐因素标注组间/组内，也未使用混合ANOVA/混合模型；模型×任务×策略的交叉只作基准比较，不按混合设计编码。 |
| B4 | 因子设计 | 0 | p.7 Table 2 lists model×strategy scores; p.23-27 Figures 9/17 show task/strategy/model variation; p.6 Table 1 gives parameters. | 存在模型、任务、策略、难度等多因素交叉结构，并报告了大量聚合分数；但未给出正式设计矩阵、每格样本量或ANOVA交互统计量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p.7 Table 2 and p.21 Table 9 report average scores; p.7-8 discuss prompt strategy differences but no F/df/p/effect size main-effect tests. | 有描述性主效应比较，但没有正式主效应统计检验、自由度、p值或效应量；按编码表不能算主效应已报告。 |
| B6 | 交互作用 | 0 | p.23-27 Figure 9/17 display variation across task/model/strategy; no interaction F/df/p/effect size or simple-effects tests are reported. | 交互作用仅以图形和描述性差异呈现，未做统计交互检验，故为0。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量及区内随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方或多条件顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；模型为既有模型集合的基准比较，不是因无法随机分配而形成的准实验处理研究。 |
| B10 | 被试内设计的适用条件 | NA | — | 虽然同一模型跨条件评测，但各条件基本是独立API调用；论文未做可逆性/迁移对称性论证。对人类被试式被试内适用条件不适用。 |
| C1 | 随机化 | NA | — | 没有条件随机分配或分配隐藏；p.6的'1 million random simulations'只是建立机会水平阈值，不是实验条件随机化。 |
| C2 | 平衡 | NA | — | 未设计需要平衡的条件顺序；各模型/策略评测是独立会话式调用，论文没有顺序平衡层级或各顺序分配。 |
| C3 | 恒定 | 0.5 | p.6 Table 1 fixes task parameters; Appendix A (p.15-17) fixes prompts; p.6 mentions using respective model APIs and context length constraints. | 报告了部分恒定变量（任务参数、提示、API/上下文限制），但未系统列出所有恒定变量水平，也未充分讨论对外部效度的限制，故0.5。 |
| C4 | 匹配 | NA | — | 没有匹配变量、配对/频数匹配或倾向得分匹配。 |
| C5 | 纳入为变量 | NA | — | 没有将已知混淆变量作为协变量/区组纳入统计模型；模型/任务作为固定基准分组，不是C5意义上的协变量控制。 |
| C6 | 盲法 | 0 | p.28: Oddball responses 'were scored by one Master’s student in cognitive science'; no blinding of this rater or blinding-success check is reported. | 存在人工Oddball评分，但未报告盲法类型、对谁施盲或成功检验；可盲而未报告盲法，按0处理。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡、拉丁方或ABBA等顺序平衡层级。 |
| D1 | 练习效应 | 0 | p.6: repeats tasks twice/three times for robustness; p.15-17 tasks are multi-trial; no practice block, early-trial exclusion, or trial-position covariate is reported. | 多轮任务存在明显学习/练习效应，但论文未设置练习块、截除标准或将试次位置作为协变量；仅做重复评测，不能算练习效应控制。 |
| D2 | 疲劳效应 | NA | — | LLM不存在人类式疲劳；论文也未设计session休息或条件时间分散。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各任务/条件基本为独立API会话，未见同一上下文跨条件残留的设计；不需要清洗期。重复评测未说明共享上下文，按独立会话处理。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移设计，也无条件对/顺序×条件建模需求。 |
| D5 | 范围效应 | NA | — | 主要因变量为客观任务得分/正确率/MAE，不使用被试内绝对量表或李克特评分。 |
| E1 | 位置 / 顺序偏差 | 0 | p.5: N-back uses 'a fixed sequence of letters'; p.15 WCST lists four cards in fixed order; no randomization/counterbalancing of option or stimulus order is reported. | 多项选择/序列刺激的呈现顺序固定，未做随机化或反平衡，也未讨论位置偏差，故为0。 |
| E2 | 默认赞同 | NA | — | 研究不使用Likert/态度自评量表，不存在反向计分与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 研究对象为LLM而非人类被试；无人类被试需求特征、事后访谈或debriefing。 |
| E5 | 实验者效应 | NA | — | 主要数据采集完全自动化，无人类主试与被试互动；仅Oddball验证评分涉及一名人工评分者，已在C6单独记录。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7: three models achieved perfect N-back scores; p.6: hard settings produced expected score decreases; p.2: 'far from saturated'. No SD/skew/endpoint frequencies are systematically reported. | 论文报告了部分天花板/饱和迹象（N-back满分、MBT全失败）并用硬设置检验headroom，但缺少系统分布、偏度和端点频率，故0.5。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量，CMB不适用。 |
| F1 | 统计结论效度 | 0 | p.6: chance thresholds established at the 95th percentile via 1 million random simulations; p.7 Table 2 and p.21 Table 9 report average scores only; no effect sizes, CIs, power analysis, or multiple-comparison correction. | 有分数和机会水平阈值，但缺少效应量/置信区间、样本量依据及多重性校正，故为0。 |
| F2 | 内部效度 | 0.5 | p.2 and p.6 report parameterized design and Centaur leakage comparison; p.6 repeats tasks; no random assignment, allocation concealment, or baseline equivalence is reported. | 评估了数据污染这一内部效度威胁并做了重复评测，但作为提示策略比较仍无随机分配/分配隐藏；其他内部效度威胁讨论有限，故0.5。 |
| F3 | 构念效度 | 0.5 | p.7: Oddball automated scoring vs human scoring r=0.87; p.4-5 adapt validated cognitive tests; p.9 discusses ecological validity limits. No full reliability/validity or manipulation checks for all constructs. | 提供了部分评分效度和任务来源效度证据，并讨论生态效度；但缺少所有关键测量的信度、效度和操纵检验，故0.5。 |
| F4 | 外部效度 | 0.5 | p.6 lists 16 models across reasoning, mainstream, and Qwen-2.5 families; p.9 Limitations discuss base LLM scope, ecological validity, multi-modal/naturalistic boundaries. | 报告了模型样本来源和主要边界条件，但未说明抽样框/代表性、跨样本或跨情境复现，故0.5。 |
| G1 | 分析单位 | 0.5 | p.6 says evaluations use model APIs and repeats; p.7 Table 2 and p.21 Table 9 aggregate by model-strategy-task; no multilevel model for trial nesting is described. | 说明了评测/聚合层面的一部分，但未明确处理分配层级、试次嵌套及分析单位匹配，故0.5。 |
| G2 | 随机效应 | NA | — | 未使用混合模型，且论文比较的是固定选择的模型集合与固定基准任务，不主张把模型/任务当作从总体抽样的随机效应；按固定效应基准设计处理。 |
| G3 | 材料作为随机效应 | NA | — | 具体任务材料是固定基准刺激，不作为从材料总体抽样的随机因子，也未主张材料层面推广；不适用项目随机效应编码。 |
| G4 | 统计功效 | 0 | p.6 Table 1 gives fixed trial numbers; p.6 uses 1 million simulations only for chance thresholds; no a priori power analysis, expected effect size, or CI is reported. | 没有设计阶段功效分析或样本量论证，也没有效应量/CI；研究比较模型差异但不报告统计功效。 |
| G5 | 研究者自由度 | 0.5 | p.6: 'average scores exclude MBT' because all models failed; p.6 hard settings exclude non-parameterized Oddball; Table 1 and Appendix B report trial counts/raw scores. | 报告了主要任务、排除的MBT总体均值和Oddball硬设置排除，并给出原始分数表；但未完整报告逐试次剔除规则/数量及验证性-探索性分析区分，故0.5。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered report is mentioned; p.9 only discusses future work and limitations. | 无公开预注册、注册编号或数据收集前分析计划，按0处理。 |
| J1 | 位置偏差 | 0 | p.15 WCST four cards are listed in fixed order; p.5 N-back uses fixed letter sequence; no A/B or left/right position counterbalancing or flip-rate analysis is reported. | 存在多候选/左右选项任务，但未做位置随机化、交换重判或位置×正确率分析，故为0。 |
| J2 | 冗长偏差 | NA | — | 不使用LLM-as-judge进行开放式生成质量比较；Oddball自动评分是embedding相似度而非裁判模型质量打分，长度偏差构念不直接适用。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈纠错或多轮谄媚操纵；不适合谄媚偏差编码。 |
| J4 | 自我偏好 | NA | — | 不使用LLM裁判或成对模型输出偏好判断；无自我偏好/同源裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主实验为零样本提示（free output/direct/zero-shot CoT）；Appendix中的任务示例是说明性示例，不作为few-shot in-context learning操纵。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.15-17 Appendix A.1-A.8 provides complete strategy and task prompts; p.6 compares three prompting strategies; no prompt versioning, semantic-equivalence sensitivity, or dev/test split is reported. | 完整提示模板已公布，并有策略比较；但无版本号/迭代日期、敏感性消融及dev/test分离，故0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不是长上下文/RAG设置，任务上下文远短于宣称的窗口长度，无关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'we repeat most tasks twice. The Oddball task ... is repeated three times'; no temperature, top-p, seed, or exact snapshot date is reported. | 有重复评测，但未报告采样超参和种子；只能部分满足随机性报告要求，故0.5。 |
| J9 | 重复与文本退化 | 0 | p.6 only distinguishes free output/direct/CoT formats and mentions CoT exceeding max token limits; no decoding strategy, repetition penalty, or degeneration rate is reported. | 未说明greedy/beam/sampling等解码策略，也未报告重复率/退化率或生成长度控制，故为0。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本研究，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.2-3 motivates contamination-minimization via parameterized cognitive tests; p.6 compares Centaur vs Llama-3.1-70B-Instruct and finds no improvement; no systematic n-gram/DCQ contamination rate or model cutoff comparison. | 识别并部分评估了基准污染，提供Centaur对照；但未报告测试集版本与各模型训练截止日期对照、污染率或正式检测，故0.5。 |
| J12 | 基准饱和 | 0.5 | p.2 says benchmark is 'far from saturated'; p.6-7 report hard-setting score decreases; p.7 notes N-back perfect scores and MBT all-model failure; no CI-based saturation analysis or continuous score alternative. | 报告了整体水位和硬设置headroom，并注意部分任务天花板/地板；但接近端点时未改用连续指标或做CI比较，故0.5。 |
| J13 | 指令遵循 | NA | — | 研究测量的是认知任务表现，不是指令遵循能力；没有按否定/数量/格式/风格等约束类型测量指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.15 A.1: direct generation prompt asks to 'respond only with your choice directly'; p.5-5 tasks specify output formats; no format-validity rate or retry/parsing policy is reported. | 报告了格式约束设置（direct/free/CoT与任务输出要求），但未报告格式合法率、重试策略或格式失败与内容错误分开统计，故0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估，无有害请求集或对抗攻击测量。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.3: cognitive psychology treats LLMs as 'humanoid subjects'; p.3-4 maps seven human cognitive dimensions to adapted tests; p.9 Limitations acknowledge base-LLM scope and ecological validity. No same-paradigm human baseline except Centaur comparison. | 明确把LLM作为认知科学式被试并讨论与人类认知过程的对应，但未系统比较LLM构念与人类同名构念的数据差异，模型snapshot也不精确，故0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p.2: 'hierarchical structure aligned with model scaling'; p.7 Table 2 includes Qwen-2.5 72B/32B/14B/7B; only discrete task scores, no continuous-log-likelihood/partial-credit curves or multiple seeds. | 有模型规模家族比较并提到层级与scaling一致；但只展示离散硬指标，未用连续指标或多seed排除指标诱导假象，故0.5。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究是纯基准评估，不涉及训练、RL、best-of-N或针对代理指标的优化过程；无overoptimization监控需求。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6 reports repeating tasks twice and Oddball three times; p.1 provides code/data link; model versions are named but exact API snapshot dates, CIs, and paired tests are absent. | 有重复次数和部分模型版本，并公开代码/数据；但缺少精确snapshot、95%CI及配对检验，故0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.4-5 tasks are multi-turn (WPT, WCST, N-back, DC-IGT, PRLT, MBT); p.8 notes 'full conversation history being available'; p.6 mentions context length constraints; results analyze blocks/reversals by trial groups. | 确实做了多轮/多试次评估并按块或反转阶段分析，但未系统按轮次独立/累积评分报告，也未完整说明每轮上下文截断策略，故0.5。 |

## 编码小结
论文构建了较完整的认知心理学启发式LLM基准，任务操作化、提示模板和评分公式报告较充分，并讨论了污染最小化、硬难度设置与部分行为模式。但统计推断与可复现性报告较弱：缺少正式效应量/置信区间、随机化/位置平衡、采样超参和精确snapshot；提示敏感性和污染检测也只有部分证据。大量人类被试实验组件因无人类分配/自陈量表而应为NA。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
