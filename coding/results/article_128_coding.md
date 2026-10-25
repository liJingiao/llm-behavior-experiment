# article_128 | Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents | 2024

研究类型概述：LLM 多智能体基准/模拟实验，而非人类被试实验。分析单位为“模型 × 场景 × 条件”的独立模拟运行（每次实验 5 个随机种子），主要比较 15 个 LLM、3 个公共资源场景，并操纵/消融 universalization 提示、communication 与 newcomer 扰动；因变量为生存时间/生存率、总收益、效率、平等性、过度使用等客观模拟指标，另有对话分类与子技能测试。
- **研究构念（Construct）**：公共资源困境中的合作、规范形成与长期后果推理｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：让多个现成LLM Agent在渔业、牧场和污染三类公共资源环境中连续决策、沟通和谈判，观察群体能否形成可持续均衡。（改变底层模型、资源场景、是否允许沟通、是否加入自利新成员及是否加入Universalization推理提示。）｜CA 任务锚定：囚徒困境（prisoner's dilemma (PD), `tsk_KRl3zbyaJcKWM`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p7: 'we augment the memory of each agent with ... if everyone takes more than f(t), the shared resources will decrease next month'; p7: communication ablation compares 'without communication with those with communication'; p5: 15 LLMs listed. | 明确命名并操纵了 universalization、communication、newcomer 等自变量，也报告了模型水平；但未报告操纵检验，条件分配与部分实验细节不完整，故为 0.5。 |
| A2 | 因变量 | 0.5 | p4: 定义 survival time m、survival rate q、total gain R、efficiency u、equality e、over-usage o 及公式；p6 Table 1: 'mean and 95% confidence intervals'。 | 因变量指标和计分公式明确，并有跨 seed 变异信息；但未报告心理测量式信效度、连续指标预处理或天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | p5: 'Each agent receives identical instructions... temperature to zero... Each simulation was repeated with five random seeds'; p16: 'simultaneous harvesting mechanism... prevents the influence of harvesting order'。 | 报告了若干控制手段（相同指令、温度 0、5 seeds、同时收获），但未系统列出全部控制变量及其控制方式。 |
| A4 | 混淆变量 | 0.5 | p5: 'One possibility for this difference is that the fishing scenario only requires reasoning about a single variable...'; p22: 'some randomness persists due to LLM inference kernels... external APIs'；p9-10 limitations。 | 识别了场景复杂度、推理内核/API 非确定性等潜在混淆，但未系统控制或做敏感性分析，残余威胁讨论有限。 |
| A5 | 调节变量 | NA | — | 没有明确的调节变量假设、乘积项交互检验或简单斜率分析；sub-skill 与 survival time 的相关分析不构成正式调节设计。 |
| A6 | 中介变量 | NA | — | 论文讨论机制（如长远后果推理、沟通），但未建立正式中介模型，也未做直接/间接效应分解，故按无中介设计处理。 |
| A7 | 操作性定义 | 1 | p3 Figure 2 给出 prompt sketches；p18-22 Listings 1-12 给出具体规则与任务提示；p4 给出环境动态与指标公式；p22 提供 GitHub 复现说明。 | 关键构念有可观测、可重复的操作化程序：场景规则、agent 提示、收获/讨论流程和指标计算均较完整。 |
| A8 | 水平数与类型 | 0.5 | p5: 列出 15 个模型及 open/closed weights；p4: fishery/pasture/pollution 三场景；p7: universalization 与 communication 两水平。 | 水平数和取值/标签明确，但未统一说明各变量的水平类型、间距/全距或连续变量中心化；分类变量虽可推断为名义变量，报告仍不完整。 |
| A9 | 单一操作化的风险 | 0.5 | p6 Table 1 同时报告 survival rate、survival time、gain、efficiency、equality、over-usage；p7-8 另有 dialogue 分类与四项 sub-skill tests。 | 关键结果使用多种指标/任务，但未报告各操作化之间的会聚证据，也未系统讨论单一操作化的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 主自变量/条件与因变量均为客观模拟日志和资源指标，不是同源自陈量表；共同方法偏差框架不适用。 |
| B1 | 被试间设计 | 0.5 | p5: 'Each simulation was repeated with five random seeds'; p22: 'For each experiment, we perform 5 runs'。 | 各模型/条件由独立模拟运行承担，可视为 between-run 比较；但未明确使用被试间逻辑说明分配，也未报告各组独立样本量细节。 |
| B2 | 被试内设计 | NA | — | 没有同一模拟运行内接受所有条件的重复测量设计；不同条件在独立 simulation runs 中完成，无被试内顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 论文未采用正式混合设计或混合模型来区分组间/组内因素；模型、场景、条件主要是基准式比较。 |
| B4 | 因子设计 | NA | — | 虽有多模型、多场景、多条件比较，但未建立带完整设计矩阵和交互检验的因子实验；按无正式因子设计处理。 |
| B5 | 主效应 | NA | — | 未报告正式因子设计中的主效应 ANOVA/F、df、p、效应量；仅有描述性均值与部分 t 检验。 |
| B6 | 交互作用 | NA | — | 未对模型 × 场景 × 条件等交互项做统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 没有区组/分层设计或区组变量报告。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验研究；模型比较与提示消融无随机分配，但论文也未将其作为准实验因果设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理顺序设计，故不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 条件由模型/实验设置固定运行，不是随机分配到独立单位的处理；5 个 seeds 用于重复而非处理分配隐藏。 |
| C2 | 平衡 | NA | — | 各条件在不同模拟运行中独立完成，没有条件顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p5: 'temperature to zero... identical instructions'; p22: hardware/API 细节与 'five different random seeds'；p9-10 limitations。 | 列出并固定了温度、指令、运行轮数等若干常量，但未系统列出所有固定变量及其外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配程序或匹配变量。 |
| C5 | 纳入为变量 | NA | — | 主分析没有把已知混淆作为协变量或区组纳入模型；sub-skill 仅作相关/OLS 辅助分析，并非 ANCOVA 式控制。 |
| C6 | 盲法 | 0 | p8: 'we manually annotated 100 random utterances and found that an annotator... agreed with GPT-4-turbo’s labels 72% of the time'。 | 存在人工评分/标注环节，但未报告盲法安排、施盲对象或实施方式；按可盲未盲记 0。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡、拉丁方或 ABBA 顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 模拟运行独立重置，无人类练习块；月内多轮学习是环境动态本身，不是练习效应控制设计。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳问题；论文虽报告运行时长，但无休息/时间分散设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同条件在独立 simulation runs 中完成，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或顺序平衡问题。 |
| D5 | 范围效应 | NA | — | 无主观量表或绝对判断的范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p16: 'To mitigate any potential bias arising from the order in which agents select... we adopted a simultaneous harvesting mechanism... prevents the influence of harvesting order'。 | 用同时收获机制消除了收获顺序偏差，并随机分配资源不足时的单位；但未对对话发言顺序做随机化/反平衡，也未报告完整平衡方案。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中间反应倾向比较。 |
| E4 | 需求特征 | NA | — | 研究对象是 LLM agents，不是人类被试；无人类 cover story、事后访谈或 debriefing 设计。 |
| E5 | 实验者效应 | NA | — | 主数据采集与指标计算自动化，无人类主试/评分者期望传递问题；仅有辅助人工标注已在 C6 处理。 |
| E6 | 天花板 / 地板效应 | 0.5 | p6 Table 1: 多个模型 survival rate 为 0.0，GPT-4o 为 53.3；p28 Table 8: GPT-4 universalization 达到 120.00±0.00、效率 100.00±0.00。 | 报告了均值/SD/生存率端点频率，可看出地板和天花板；但未报告偏度、端点频率统计或 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | 主 IV/DV 为客观模拟行为与资源指标，不是同源自评多构念测量；共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p5: 5 random seeds；p6 Table 1: 95% confidence intervals；p7: universalization/communication 比较报告 t-test p 值。 | 报告了变异与部分 CI/p 值，但无事前功效分析、样本量依据、多重比较校正或完整统计假设说明。 |
| F2 | 内部效度 | 0.5 | p5: 相同 setup、5 seeds、temperature 0；p22: 承认 LLM 推理内核和外部 API 非确定性；p9-10 limitations。 | 报告了重复运行与部分内部效度威胁，但没有随机分配/分配隐藏、基线等价性检验或完整被试流向式说明。 |
| F3 | 构念效度 | 0.5 | p8: GPT-4-turbo 对话分类与人工标注一致率 72%；p32-38: 四项 sub-skill tests 的模板、评分与结果。 | 有部分效度/评分者一致性证据，但主指标无传统信效度证据，也无针对提示操纵的 manipulation check。 |
| F4 | 外部效度 | 0.5 | p5: 列出闭源/开源模型和 exact identifiers；p9-10: 讨论场景简化、未来更多资源类型/人类-AI 等边界条件。 | 报告了模型样本来源与部分推广边界，但未讨论模型总体代表性，也未做跨样本/跨情境复现。 |
| G1 | 分析单位 | 0.5 | p5: 'Each simulation was repeated with five random seeds'；p8: 对每段 utterance 分类后汇总到模型/条件；p6 Table 1 以 run 聚合。 | 主分析在 simulation-run 层聚合，避免了把单个 agent 当独立样本；但对话分类存在 utterance 嵌套，未使用多层模型显式处理。 |
| G2 | 随机效应 | NA | — | 未使用混合模型或随机效应推断；模型集合是固定基准目标，5 个 seeds 仅用于描述变异，故不需要按随机效应总体推断。 |
| G3 | 材料作为随机效应 | 0.5 | p4: 三个场景 fishery/pasture/pollution；p9: 'simplified nature of the resource-sharing scenarios... future version'；p6 分场景报告。 | 有三个场景作材料/任务变式并分场景报告，但被当作固定场景而非从场景总体抽样，未用场景随机效应或准 F 比，故为部分满足。 |
| G4 | 统计功效 | 0.5 | p5: 5 seeds；p6 Table 1: 95% CI；p7: 报告 universalization 的平均改善和 t-test；无功效分析。 | 报告了效应量式变化与 CI，但缺少事前功效分析或 5 次运行的理由，故为 0.5。 |
| G5 | 研究者自由度 | 0.5 | p7: 'excluding Claude-3 Opus due to API costs'；p5/p22: 每个实验 5 runs；论文报告多个指标和 sub-skill，但未区分验证性与探索性分析。 | 报告了部分条件排除和运行次数，但未完整说明所有因变量/条件、样本量决定方式及探索性-验证性区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–46 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告预注册平台、注册编号或预先分析计划；无验证性与探索性分析区分。 |
| J1 | 位置偏差 | NA | — | 任务是数值收获决策与多智能体对话，不是多候选项选择、排序或 LLM-as-judge 成对比较；无候选位置偏差设置。 |
| J2 | 冗长偏差 | NA | — | LLM 裁判仅用于 utterance 分类，不是按生成长度/质量评分；长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 没有操纵用户先验立场、反馈纠错或测量谄媚翻转率；不涉及 sycophancy 设计。 |
| J4 | 自我偏好 | 0.5 | p8: 'we used GPT-4-turbo to classify each utterance...'；p8: 人工标注 100 utterance 作为对照，一致率 72%。 | 存在 LLM-as-judge/分类器，且被评模型包含 GPT-4/GPT-4o 等同家族模型；报告了裁判模型和人工一致率，但未控制或量化自我偏好偏差。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主要提示为零样本规则/任务说明，不是 few-shot in-context examples 实验；无示例选择/排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p3 Figure 2 prompt sketches；p18-22 给出多场景完整提示；p22 指向 GitHub 代码。 | 提供了较完整的 prompt 模板与代码，但未做语义等价措辞的敏感性消融，未说明 dev/test 划分或 prompt 迭代版本。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为 12 个月模拟与短对话，不涉及长文档/RAG 的中间迷失问题。 |
| J8 | 温度与采样随机性 | 0.5 | p5: 'temperature to zero, i.e., greedy decoding... five random seeds'；p22 Table 3: exact API identifiers and dates。 | 报告了 temperature、重复次数与 API model snapshot；但未报告 top-p/top-k、随机种子值或完整采样约束。 |
| J9 | 重复与文本退化 | 0.5 | p5: 'greedy decoding'；p21 prompt: 'avoids repetition'；无 repetition penalty/重复率 QC。 | 报告了解码策略，但未报告 repetition penalty、n-gram 重复率/退化率或生成长度截断比例。 |
| J10 | 分词效应 | NA | — | 单语言英文实验，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p2: 提出新 GovSim 环境；p32: sub-skill 由模板程序化生成；未报告训练截止日期对照或污染检测。 | 使用新建基准降低污染风险，但未系统报告训练截止日期、n-gram 重叠或污染率。 |
| J12 | 基准饱和 | 0.5 | p6 Table 1 标注 Max=100/12/120 等量程；p28 Table 8: GPT-4 universalization 达 120.00±0.00、Efficiency 100.00±0.00、Equality 100.00±0.00。 | 报告了量程和当前水位，也使用连续指标；但在接近天花板的结果上未讨论饱和问题，也未改用更难子集。 |
| J13 | 指令遵循 | NA | — | 研究不是测量指令遵循，因变量是资源合作结果与对话类型，不是 IFEval 式约束遵循。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p18 Listing 2: 'Put the final answer after "Answer:"'；p21 Listing 10: 要求 Response/Next speaker 等结构化输出；未报告格式合法率或重试策略。 | 报告了输出格式约束设置，但未报告格式合法率、解析失败率、重试/后处理规则，也未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及越狱、安全对齐或对抗攻击评估；合作/安全问题不是 jailbreak ASR 测量。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1 abstract: 'study strategic interactions and cooperative decision-making in LLMs'；p7: 引入 moral psychology 的 'Universalization'；p9-10: 未来可加入人类。 | 明确将 LLM 合作与人类道德心理学/公共资源理论关联，并避免直接声称等同于人类；但无人类对照实验，也未系统论证 LLM 构念与人类同名构念的异同。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文不报告随模型规模/训练进展的能力曲线，也不做“涌现能力”跨规模指标争议分析；标题中的 emergence 指模拟中合作规范出现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N 或按代理指标优化模型的环节；纯基准评估，不涉及 reward overoptimization。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5: 5 seeds；p6 Table 1: 95% CI；p22 Table 2-3: 开源模型 HF identifiers 与闭源 API exact identifiers/dates。 | 报告了重复次数 N、CI 和较精确 snapshot 标识；但未给随机种子值、逐次日志或配对检验。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p4: 模拟 'repeated for T time steps'，T=12 months；p6 Figure 3: 展示逐月资源与各 agent 收获轨迹。 | 确实进行了多轮/逐月评估并展示轨迹，但没有按每轮报告指令遵循/一致性衰减，也未明确说明上下文是否截断历史。 |

## 编码小结
论文提供了较完整的模拟环境、提示、指标定义与模型标识，重复运行并报告了 CI/SD，且对 communication、universalization 和新加入者做了消融/扰动；但整体是基准式比较而非预注册的因子实验。主要缺口是缺少正式操纵检验、统计功效/多重校正说明、随机分配与盲法、提示敏感性分析、LLM 裁判同源偏差控制，以及对饱和/污染/构念迁移的系统论证。
