# article_017 | GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations | 2024

研究类型概述：LLM 游戏论基准评测/多智能体对局观察；以 10 个游戏、多个 LLM、多种推理范式和不同对手进行重复对局，分析单位为模型—游戏—推理方法—对手组合下的 50 场有效 match 的平均 NRA/Elo，并辅以 regret、Pareto 与错误画像分析。
- **研究构念（Construct）**：重复博弈中的策略推理（strategic reasoning in repeated games）｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：LLM 游戏论基准评测/多智能体对局观察；以 10 个游戏、多个 LLM、多种推理范式和不同对手进行重复对局，分析单位为模型—游戏—推理方法—对手组合下的 50 场有效 match 的平均 NRA/Elo，并辅以 regret、Pareto 与错误画像分析。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.5: 'we consider the following reasoning paradigms' Prompt/CoT/SC-CoT/ToT；p.5: '10 different gaming environments'；p.6: temperature 0.2, 50 valid matches, first-player 25 matches. | 明确命名并报告了多个条件水平（游戏、模型、推理方法、对手）及基本操纵程序，但未说明条件分配/随机化逻辑，也未报告真正的操纵检验；任务完成率只算 sanity check。 |
| A2 | 因变量 | 0.5 | PDF p.4: NRA 公式及取值 [-1,1]；p.6: 'For each competition, we run 50 valid matches... averaged NRA'；p.8: error pattern percentages. | 因变量指标 NRA/Elo/regret/error 等计分方式清楚，但未报告信度、效度证据及连续指标预处理/天花板地板处理说明。 |
| A3 | 控制变量 | 0.5 | PDF p.5: MCTS 'number of simulations as 1000'；p.6: 'temperature is set to 0.2', 'max number of generated tokens is 1024', '50 valid matches'；p.6: first-player balanced 25 matches. | 列出了若干控制变量及控制水平，但不是系统控制变量清单，也未逐一说明所有控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF p.6: 'To mitigate the first-player advantage, we have each participant take the first turn in 25 matches'；p.9: limitations 提到 prompt sensitivities、action/state space limited；p.24-25: temperature/CoT prompt sensitivity 实验。 | 识别了先手优势、prompt 敏感性等潜在混淆并做了部分控制/敏感性检查，但未系统报告残余混淆及内部效度威胁的敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量理论模型，也没有交互检验或简单斜率分析；按规则不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或中介假设；不适用。 |
| A7 | 操作性定义 | 1 | PDF p.4: 形式化定义 gameplay 为 (S,A,M,O) 并给出 NRA 计分公式；p.15-22: 逐游戏列出 observation/action 格式、规则和 prompt；p.19-23: system/head/observation/reasoning prompts 全文。 | 关键构念通过游戏规则、观察/动作接口、prompt 模板和 NRA 计分公式高度操作化，可复现性较好。 |
| A8 | 水平数与类型 | 0.5 | PDF p.5: '10 different gaming environments'；p.5: 推理范式 Prompt/CoT/SC-CoT/ToT；p.6: 模型列表与 50 matches。 | 报告了各分类条件的水平与标签，但未明确说明水平类型、间距/全距以及连续变量中心化等；对分类变量这些多为不适用，但论文未显式交代。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p.4: NRA 与 Elo 指标；p.8: error pattern profiles；p.9: regret 与 Pareto Efficiency；p.5: 10 个游戏。 | 对战略推理采用了多游戏、多指标操作化，但没有报告各操作化/指标间的会聚证据；局限部分提到游戏动作/状态空间有限。 |
| A10 | 单一方法的风险 | NA | — | 自变量为模型/推理方法/游戏条件，因变量为客观游戏结果（胜负、收益、Elo 等），不是同源自陈量表，共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试及被试间随机分配；LLM 模型身份是固定评测条件，不是被分配到互斥条件的被试组。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内设计或条件顺序平衡方案；同一 LLM 的多 match 评测不是以被试为单位的重复测量实验。 |
| B3 | 混合设计 | NA | — | 没有明确逐因素标注组间/组内的混合设计及对应误差项分析。 |
| B4 | 因子设计 | NA | — | 虽有多模型×多游戏×多推理方法的评测网格，但没有作为正式因子设计报告设计矩阵、每格样本量和 ANOVA 交互分析。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验与效应量报告；仅描述性比较平均值。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验、简单主效应或带误差棒的交互图示分析。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量及区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；没有非随机分组后的因果识别设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内条件顺序设计，因此不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 模型/游戏/推理范式等条件为固定评测条件，未把研究单位随机分配到互斥实验条件；无随机化分配机制可评。 |
| C2 | 平衡 | 0.5 | PDF p.6: 'To mitigate the first-player advantage, we have each participant take the first turn in 25 matches.' | 报告了先手角色的 25/25 平衡，但未报告平衡层级、完整顺序分配细节及迁移对称性前提。 |
| C3 | 恒定 | 0.5 | PDF p.6: 'temperature is set to 0.2 and the max number of generated tokens is 1024'；p.5: MCTS simulations 1000；p.9: limitations 提到 prompt sensitivity。 | 列出若干恒定控制（温度、最大长度、MCTS 模拟数等），但未系统列出所有环境/模型/设备恒定变量及其外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计，也没有匹配变量或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未把已知混淆变量作为协变量/区组纳入统计模型；先手优势采用平衡而非 ANCOVA 协变量处理。 |
| C6 | 盲法 | NA | — | 主要是自动化 API 评测，无人类被试盲法；人工错误画像不构成本研究的处理效应盲法设计。 |
| C7 | 平衡的层级 | 0.5 | PDF p.6: 'each participant take the first turn in 25 matches'；p.5-6: 50 valid matches 的设定。 | 报告了先手顺序的完全平衡做法及数量，但未明确说明平衡层级选择理由、构造方法及顺序效应形状假设。 |
| D1 | 练习效应 | NA | — | LLM 每场 match 为独立游戏会话，权重不随 match 更新；没有人类式练习效应或试次位置协变量需求。 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳效应；论文也未按人类 session 疲劳控制来设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件清洗期设计；每场游戏在独立环境中运行，不涉及药物/学习残留式迁移。 |
| D4 | 不对称迁移 | NA | — | 没有迁移对称性检验需求；LLM 条件不是同一被试跨条件的连续处理。 |
| D5 | 范围效应 | NA | — | 因变量为客观游戏结果/NRA/Elo，不是主观量表评分，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF p.5: prompt 中包含 'legal actions'；p.21-22: 固定格式的 observation prompt；全文未报告 legal action 列表呈现顺序的随机化或反平衡。 | 游戏每回合有多个合法动作选项，存在选项顺序偏差风险，但论文未对动作/选项顺序做随机化或反平衡，也未讨论该风险。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在人类需求特征或掩饰情节问题。 |
| E5 | 实验者效应 | NA | — | 数据采集主要通过 LLM API 自动化完成，无人类主试/评分者的期望传递问题；人工错误画像不是主要处理效应评分。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.6: 'all the LLM agents... achieve NRA as -1' against MCTS；p.9: limitation 'actions/state space is limited, which may not be well-distinguished for LLMs in the same skill levels'。 | 报告了明显的端点/地板式 NRA=-1 并讨论任务区分度限制，但没有报告偏度、端点频率的系统分布或 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | IV 与 DV 不是同源自评量表；DV 为客观游戏结果，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | PDF p.4: NRA 定义与 [-1,1]；p.6: 50 valid matches；p.6 Fig.3 提到 error bars over different reasoning methods；无 p 值/CI/多重校正表。 | 报告了效应量式的 NRA 与部分变异信息，但缺少样本量功效依据、置信区间、正式显著性检验和多重性校正。 |
| F2 | 内部效度 | 0.5 | PDF p.6: 'For each competition, we run 50 valid matches'、first-player 25/25；p.23: completion rates/sanity check；未报告随机分配或基线等价性检验。 | 报告了评测流程和部分内部效度控制，但非随机分配、无分配隐藏/基线等价检验，对因果推断威胁讨论有限。 |
| F3 | 构念效度 | 0.5 | PDF p.23: sanity check completion rates 'all the LLM agents achieve ≥90% completion rate'；p.5: 10 个任务覆盖多类游戏；p.9: limitations 提到 prompt sensitivity 与游戏区分度。 | 报告了任务完成率作为基本 sanity check 和多游戏内容覆盖，但没有 NRA/Elo 等关键测量的信度/效度证据，也未做正式 manipulation check。 |
| F4 | 外部效度 | 0.5 | PDF p.6: 明确列出 GPT-4-0613、GPT-3.5-turbo-1106、Llama-3-70b-Instruct 等模型；p.9: limitations 提到 prompt 依赖与 action/state space 有限。 | 报告了模型样本来源与部分版本，并讨论部分推广边界，但模型集合不代表 LLM 总体，也未报告跨情境复现实验。 |
| G1 | 分析单位 | 0.5 | PDF p.6: 'For each competition, we run 50 valid matches. The final performance is measured by the averaged NRA over the 50 valid matches.' | 说明了 match 层级汇总到模型—游戏—推理方法组合，但未用多层模型显式处理 match/turn 嵌套，只做平均聚合。 |
| G2 | 随机效应 | 0 | PDF p.6: 结果以 50 场 match 平均 NRA 报告；全文未说明模型、游戏或 match 的随机效应结构。 | 没有随机效应模型或随机截距/斜率；模型/游戏均按固定条件处理，无法区分抽样变异与条件效应。 |
| G3 | 材料作为随机效应 | 0 | PDF p.5: 固定选择 10 个游戏；p.6: 按游戏/条件报告平均 NRA；未把游戏作为项目随机效应建模。 | 10 个游戏被视为固定任务集合，未报告 item/game 随机效应，结论向任意游戏总体的推广缺乏统计处理。 |
| G4 | 统计功效 | 0 | PDF p.6: 仅说明 '50 valid matches'，无功效分析或样本量推导；结果主要为平均 NRA/Elo，无 CI。 | 没有事前功效分析、目标功效、预期效应量来源或置信区间；50 场 match 未给出统计依据。 |
| G5 | 研究者自由度 | 0.5 | PDF p.23: 以 '50 valid matches' 和 completion rates 说明有效 match 标准；p.9: limitations 列出部分限制；未明确区分验证性与探索性分析。 | 报告了有效 match/非法动作的排除逻辑和全部主要游戏，但没有完整说明所有因变量/条件选择、停止规则及探索性/验证性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–36 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 未报告预注册平台、注册编号、预注册假设/分析计划或与预注册偏离；按规则无预注册记 0。 |
| J1 | 位置偏差 | 0 | PDF p.5: prompt 中包含 'legal actions'；p.21-22: 固定 observation 模板；未报告 legal action 顺序随机化/反平衡，也未报告位置×正确率。 | LLM 在多个合法动作中选择时存在选项位置偏差风险；论文只平衡先手，不控制合法动作列表顺序，也未讨论或量化偏差。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放式生成长短质量，无长度偏差问题。 |
| J3 | 谄媚 | NA | — | 任务为无用户先验立场输入的封闭游戏对局，不涉及用户反馈/纠错式谄媚评估。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 裁判或 LLM-as-judge 成对比较；胜负/收益由游戏规则计算。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验使用零样本 prompting，无 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.19-23: 给出 system/head/observation/reasoning prompt 全文；p.24-25: 五种 CoT prompt 的敏感性实验及结果。 | 提供了较完整 prompt 模板并做了 CoT 措辞敏感性检查，但未给 prompt 版本号/迭代日期、dev/test 划分及完整 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是长上下文/RAG 实验，游戏 observation 远低于需要研究中间迷失的上下文长度。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.6: 'temperature is set to 0.2 and the max number of generated tokens is 1024'、'50 valid matches'；p.23-24: 温度 0.4/0.6/0.8 实验。 | 报告了 temperature、最大长度和重复 match 数，并做了温度敏感性；但未报告 top-p/top-k/重复惩罚/随机种子，也未给 95% CI。 |
| J9 | 重复与文本退化 | NA | — | 任务输出为短游戏动作而非开放式长文本生成，n-gram 重复/退化问题不适用。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本英文 prompt，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.15: 游戏环境基于 OpenSpiel；全文未报告测试集版本与模型训练截止日对照、污染检测或污染率。 | 使用经典公开游戏，存在模型预训练已见规则/策略的污染风险；论文未做任何污染评估，也未讨论其对‘战略推理’结论的影响。 |
| J12 | 基准饱和 | 0.5 | PDF p.4: NRA 自然归一化到 [-1,1]；p.6: 对 MCTS 时 'all the LLM agents... achieve NRA as -1'，呈明显地板；p.9: 提到游戏区分度有限。 | 识别到接近下限的分数表现并给出量程，但未改用连续指标/更难 held-out 子集，也未做模型间 bootstrap CI 比较。 |
| J13 | 指令遵循 | 0.5 | PDF p.23: 以 legal moves 和 '50 valid matches' 计算 completion rates；p.19: system prompt 要求 'strictly follows' 指令。 | 有可机器判定的完成/合法动作标准，但未按否定/数量/格式/风格等约束类型拆分准确率，也未报告指令微调细节。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p.22: 要求 'Action: Your action wrapped with <>' 等格式；p.23: completion rates 统计合法动作完成率。 | 报告了格式约束和总体完成率，但未将格式失败与内容错误分开报告，也未报告格式合法率/重试策略与解析归一化规则。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估，无自然拒绝率与对抗 ASR 构念。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.1: 摘要称评估 'strategic and logical reasoning abilities'；p.5: 用游戏论任务操作化战略推理；p.6: 列出模型版本；未报告与人类同范式对照。 | 将 LLM 的战略推理作为认知/能力构念测量并操作化，但未系统论证该构念与人类同名构念的异同，也未做人类对照实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的连续能力曲线或‘涌现/突变’宣称；模型大小差异只作描述性比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标（benchmark/reward model/LLM judge）的训练、RL 或 best-of-N 优化，无奖励过优化监控问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.6: 使用 GPT-4-0613、GPT-3.5-turbo-1106 等版本，每竞争 50 matches；未报告 CI、随机种子、配对检验或原始推理日志。 | 报告了重复 match 数与部分精确模型版本，但开源模型无 commit hash，未给 95% CI/配对 bootstrap/McNemar 等可复现统计细节。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF p.5: 支持多轮游戏；p.9: 讨论 Iterated Prisoner's Dilemma 重复轮次与 Pareto Improvement；p.8: 人工检查 157 turns。 | 确有多次对局和多轮游戏，并分析部分轮次行为；但未系统按轮次独立/累积评分、未报告上下文是否截断，也未量化跨轮一致性衰减。 |

## 编码小结
该文不是人类被试实验，而是 LLM 战略推理能力的基准评测。设计、任务规则、prompt 与部分采样参数报告较充分，但推断统计、随机效应/嵌套结构、预注册、选项位置顺序、污染控制、统计功效与部分可复现性细节不足。
