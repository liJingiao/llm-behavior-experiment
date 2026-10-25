# article_225 | Investigating Non-Transitivity in LLM-as-a-Judge | 2025

研究类型概述：实证型 LLM-as-a-Judge / 基准评测研究，无人类被试；分析单位为 AlpacaEval 与 Arena-Hard-Auto 指令层面的模型两两比较，并聚合到 20 个模型的胜率矩阵与排行榜。研究操纵/比较判官模型、位置切换与随机分配、提示策略及 round-robin/Bradley-Terry/SWIM 排名方法；主要指标为 PNT、SNTD、胜率、Elo 及与 Chatbot Arena 的 Spearman/Kendall 相关。
- **研究构念（Construct）**：偏好传递性、循环判断、位置偏差与评判一致性｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让LLM judge对多个模型输出进行成对比较，按模型三元组和指令计算循环偏好与传递性偏离，并操纵输出位置和评判提示。（比较judge、被评模型能力差、输出顺序、位置交换、CoT、结构化清单和允许平局等条件。）｜CA 任务锚定：语义判断任务（semantic decision task, `trm_4f240cb09f8e5`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: “we examine non-transitivity in judgments using two models: GPT-4-Turbo and GPT-3.5-Turbo, both with the temperature set to 0.”；p.4–5: “each comparison is evaluated with responses in both orders”；p.21: 六种 prompting strategies。 | 判官模型、位置处理与提示策略等操纵/比较条件被命名并给出水平，但未报告操纵检验，部分条件分配与程序细节不完整，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.3: PNT 与 SNTD 公式及判定阈值；p.4: Bradley-Terry/Elo 评分公式；p.8: Table 2 报告 Spearman/Kendall 相关。 | 因变量指标与计分方式界定清楚；但缺少对 PNT/SNTD 的信度证据与完整预处理/天花板地板说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.4: “For consistency with AlpacaEval, we maintain the judge configuration and prompt templates”；“both with the temperature set to 0”；p.5: “invoke the judge function twice for each order configuration”；p.8: length-controlled winrate。 | 报告了若干控制变量及控制手段，但未系统列出完整控制清单，故为 0.5。 |
| A4 | 混淆变量 | 1 | p.6–7: “position bias is indeed a contributing factor”；“non-transitivity still occurs within consistent instructions... position bias is not the sole cause”；p.7: Position Difference（PD）与 Figure 6。 | 明确识别位置偏差与判官推理能力等潜在混淆，实施位置切换/随机分配控制，并讨论残余非传递性来源，符合 1。 |
| A5 | 调节变量 | NA | — | 论文没有显式调节变量、调节假设或乘积项交互检验；性能差距分析属于描述性关系/分层比较，不按调节模型编码。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解，不涉及中介模型。 |
| A7 | 操作性定义 | 1 | p.3: PNT、SNTD、Jensen–Shannon divergence 与判官函数定义；p.4: Bradley-Terry 与 Elo 公式；p.24–30: 完整 judge prompts。 | 关键构念（非传递性、判官偏好、BT/Elo 排名）均给出可复现的操作化程序与公式，提示模板也公开，符合 1。 |
| A8 | 水平数与类型 | 0.5 | p.4: 判官模型 GPT-4-Turbo、GPT-3.5-Turbo；四类场景 LL/LM/ML/MM；p.21: 六种 prompting strategies。 | 报告了主要条件的水平数与标签，但未系统给出各变量的水平类型、间距/全距或连续变量中心化说明，故为 0.5。 |
| A9 | 单一操作化的风险 | 1 | p.3: 同时定义 PNT 与 SNTD；p.5–6: 讨论 PNT 对连续偏好不敏感，SNTD 补足；p.13–14: 多判官、多数据集复现；p.17–18: 偏好分布。 | 关键构念使用多种操作化/指标，并报告不同指标差异与跨判官/数据集结果，符合 1。 |
| A10 | 单一方法的风险 | 0.5 | p.4–5: 主要结果均来自 LLM 判官同一 API/方法；p.5: position switching 与每顺序两次调用；p.8: 以 Chatbot Arena 作外部参照；p.15: 讨论 verbosity/token bias。 | 研究清楚说明判官方法与部分程序控制，但未做正式共同方法偏差检验；同源 LLM 评判风险主要通过位置切换缓解，故为 0.5。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配；研究单位是指令层面的模型比较，不是被试间实验设计。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量设计；位置顺序切换属于比较内的反平衡，已在 E1/J1 编码。 |
| B3 | 混合设计 | NA | — | 不存在人类被试的组间/组内混合设计；判官与场景比较不是混合 ANOVA 设计。 |
| B4 | 因子设计 | NA | — | 没有采用因子设计及完整设计矩阵/ANOVA 交互分析；多判官、多场景、多提示策略为描述性比较，不按因子设计编码。 |
| B5 | 主效应 | NA | — | 无因子设计主效应检验；不适用。 |
| B6 | 交互作用 | NA | — | 无因子设计交互项统计检验与简单主效应分析；不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计；不适用。 |
| B8 | 拉丁方 | NA | — | 无人类被试内拉丁方顺序设计；不适用。 |
| B9 | 准实验设计 | NA | — | 不是准实验或非随机人类分组研究；方法比较不按准实验设计编码。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理的适用条件论证；不适用。 |
| C1 | 随机化 | NA | — | 研究单位没有被分配到互斥处理条件；p.5 的位置随机分配仅用于消融比较，已在 E1/J1 处理，不按随机化质控组件编码。 |
| C2 | 平衡 | NA | — | 无人类被试内条件顺序设计；位置顺序反平衡在 E1/J1 编码。 |
| C3 | 恒定 | 0.5 | p.4: 保持 judge configuration 与 prompt templates；temperature set to 0；p.8: 讨论判官模型与数据集的推广限制。 | 报告了若干恒定条件（判官、提示、温度），但未完整列出所有采样与环境常量，外部效度讨论也有限，故为 0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配设计；不适用。 |
| C5 | 纳入为变量 | 0.5 | p.8: “Length-Controlled Winrate... generalized linear model with the same weights as Length-Controlled AlpacaEval”；Table 2 报告 length-controlled 相关。 | 将长度/verbosity 作为已知混淆在排名分析中调整；但未报告斜率齐性检验或完整协变量模型细节，故为 0.5。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者施盲需求；LLM 判官仅使用匿名标识符，不按人类盲法组件编码。 |
| C7 | 平衡的层级 | NA | — | 无人类被试内顺序平衡层级设计；不适用。 |
| D1 | 练习效应 | NA | — | 每次判官调用为独立提示，无人类练习阶段或上下文内学习；不适用。 |
| D2 | 疲劳效应 | NA | — | 无人类长 session 疲劳风险；API 评估任务短且无疲劳安排，不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各判官调用使用独立上下文，无跨条件清洗期需求；不适用。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移不对称的人类重复测量设计；不适用。 |
| D5 | 范围效应 | NA | — | 无主观量表自陈的范围效应问题；判官偏好为连续概率输出，不按该组件编码。 |
| E1 | 位置 / 顺序偏差 | 1 | p.4–5: “each comparison is evaluated with responses in both orders. The final preference score is calculated as the mean... invoke the judge function twice for each order configuration”；p.5: random assignment ablation；p.7: Figure 6 Position Difference。 | 对候选项位置做了系统反平衡（双顺序均值）并报告一致性/位置差异及随机分配对照，符合 1。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表；不适用。 |
| E3 | 极端 / 中间反应倾向 | 0.5 | p.15–18: Figures 8–9 报告不同判官在 random assignment 与 position switching 下的偏好分布；p.15: GPT-3.5 呈 U-shaped，position switching 后集中于 0.5；p.18: GPT-4 在 MM 中仍有 38% 分布于全范围。 | 报告了端点/中点使用和跨判官分布差异，但未做正式反应风格校正或完整偏度分析，故为 0.5。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或事后访谈检查；LLM 判官任务不按该组件编码。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递；不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5: Table 1 报告 PNT/SNTD；p.8: Table 2 报告 Spearman/Kendall（95.0%→96.4% 等）；p.17–18: 偏好分布。 | 报告了主要指标数值和部分分布，但未做 pilot 难度校准，也未讨论高相关接近上限及 PNT 接近 0 的天花板/地板风险，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；LLM 判官共同方法问题在 A10/J4 处理，不适用 E7。 |
| F1 | 统计结论效度 | 0.5 | p.8: Table 2 报告 Spearman/Kendall 相关系数；p.8 Figure 6-Right: 2000 trials、mean 与 95% CI；p.20: Table 6 报告 50 次重复的 SNTD 均值与 SD。 | 报告了效应量/相关与部分置信区间，但无事前样本量论证、无系统多重性校正或统计假设说明，故为 0.5。 |
| F2 | 内部效度 | NA | — | 不是随机化人类实验，无 allocation concealment、被试流向或损耗处理；不按内部效度实验质控编码。 |
| F3 | 构念效度 | 0.5 | p.3–4: 关键指标公式；p.8: 与 Chatbot Arena 人类排名相关作为外部效度证据；p.13–14: 跨判官、跨数据集复现；p.17–18: 偏好分布。 | 提供外部排名效度与稳健性证据，但无正式信度系数、无 manipulation check，且对指标构念效度论证有限，故为 0.5。 |
| F4 | 外部效度 | 1 | p.4: 20 个模型来自 AlpacaEval 与 Chatbot Arena；p.4/13: 另在 Arena-Hard-Auto 的 200 prompts 上复现；p.8: 讨论 AlpacaEval 领域、判官模型与人类偏好偏差等边界。 | 报告样本来源与跨数据集复现，并讨论推广边界，符合 1。 |
| G1 | 分析单位 | 0.5 | p.3: PNT 在 instruction set 上定义；p.4: round-robin 与 Bradley-Terry；p.5: 模型级 win rate 与聚合非传递性。 | 区分了 instruction 层与 model 层分析，但未使用多层/混合模型显式处理观测嵌套与聚集方差，故为 0.5。 |
| G2 | 随机效应 | NA | — | 无混合模型或随机效应结构；研究对象是固定的 20 模型池与数据集，描述性排名不要求把模型/指令作为随机效应推广，故不适用。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: 使用 AlpacaEval 指令集；p.13: 在 Arena-Hard-Auto 上抽样 200 prompts 复现；但分析中未将 instruction 作为随机效应建模。 | 通过多数据集部分回应材料/题目抽样推广，但无显式 item random effect 或准 F/混合模型，故为 0.5。 |
| G4 | 统计功效 | 0 | 全文未见事前功效分析或样本量确定依据；p.8/p.20 仅报告重复试验与部分 CI。 | 无设计阶段功效分析或样本量论证，按编码记 0；虽报告部分效应量与 CI，但不足以满足 G4 基本要件。 |
| G5 | 研究者自由度 | 0.5 | p.4–8: 报告主要指标、场景、判官、提示与排名方法；p.20–21: 额外消融与六种 prompting strategies；p.9: 提供代码与数据链接。 | 报告较全面并公开代码/数据，但未明确区分验证性与探索性分析，也未完整说明所有分析选择与停止规则，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册平台、注册编号或时间戳；仅有代码/数据链接（p.9）。 | 无预注册，按既定口径记 0。 |
| J1 | 位置偏差 | 1 | p.4–5: 每个比较双顺序评估并取均值，每顺序调用两次；p.6–7: 报告 preference consistency、Position Difference，并比较 position switching 与 random assignment；p.24–25: 评分 prompt。 | 明确识别并控制候选项位置偏差，报告交换前后一致性/位置差异，且给出判官版本、温度与 prompt，符合 1。 |
| J2 | 冗长偏差 | 0.5 | p.8: “To mitigate verbosity bias... length-controlled preferences... generalized linear model with the same weights as Length-Controlled AlpacaEval”；Table 2 报告 LC 相关；p.15: 提及 GPT-3.5 受 verbosity/token bias 影响。 | 对长度/verbosity 偏差作了控制并报告 length-controlled 结果，但未报告被评回答长度分布、长度—得分相关或盲评细节，故为 0.5。 |
| J3 | 谄媚 | NA | — | 任务为无用户立场输入的两两质量比较，没有 pro/anti framing、反馈或多轮谄媚操纵，故不适用。 |
| J4 | 自我偏好 | 0 | p.4: 判官为 GPT-4-Turbo 与 GPT-3.5-Turbo，脚注说明 GPT-4-Turbo 指 gpt-4-1106-preview；p.12: gpt-4-1106-preview 又属于 20 个被评模型；p.3: 仅用 unique token identifier 隐藏模型名。 | 裁判模型与被评模型存在同源/重叠风险，但全文未报告或控制自我偏好，也未量化同源裁判结果，故为 0。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 判官评估为零样本 pairwise prompt，无 few-shot in-context examples；checklist 生成虽可能含示例，但不是被评估判官的 few-shot 条件，故不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.24–30: 完整 judge/checklist prompts；p.7: 讨论多种 prompting strategies；p.21: Table 7 比较 Direct、CoT、Checklist、Tie 等策略。 | 提供完整模板并做多种提示策略敏感性比较，但无版本号/日期、无语义等价改写消融、未说明 dev/test 划分，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不涉及长上下文、RAG 或关键信息位置操纵；不适用。 |
| J8 | 温度与采样随机性 | 0.5 | p.4: 判官 temperature set to 0；p.5: 每顺序调用两次；p.20: 随机分配消融重复 50 次并报告均值/SD；p.8: 2000 trials 的 95% CI。 | 报告 temperature 与重复次数，并有部分方差/CI 信息；但未报告 top-p、top-k、seed，部分 API snapshot 不完整，故为 0.5。 |
| J9 | 重复与文本退化 | NA | — | 判官主要输出短模型标识符，不涉及长开放式生成；CoT 解释虽存在但不是重复/退化主分析，故不按开放生成退化编码。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本评估；无跨语言/跨格式输入比较，不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4: 使用公开 AlpacaEval 数据集与预生成输出；p.12: 20 个模型来自公开 leaderboard；全文未报告训练截止日期与测试集重叠检查。 | 存在公开基准污染风险，但未做任何污染检测或训练截止日期对照，故为 0。 |
| J12 | 基准饱和 | 0.5 | p.8: Table 2 中 AlpacaEval Spearman 95.0%、round-robin 96.4%，Kendall 82.1%→86.3%；作者宣称提升但未讨论接近上限的饱和风险。 | 报告了基准相关及当前水位，但未在接近天花板时改用连续指标/更难子集或做饱和讨论，故为 0.5。 |
| J13 | 指令遵循 | NA | — | 研究重点是 LLM 判官偏好的非传递性，而非按可机器判定约束测量指令遵循准确率；AlpacaEval 的开放式指令遵循不作 J13 的约束遵循准确率编码。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.24–25: prompt 要求只输出模型标识符；p.26: CoT 版本用最后一个字符解析；但未报告格式合法率或重试策略。 | 报告了输出格式约束设置，但无格式合法率/失败与内容错误拆分，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/对齐、越狱或有害请求评估；不适用。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究为纯工程/评测方法研究，不主张把 LLM 作为心理学/认知科学被试测量人类同名构念，故不适用。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随模型规模或训练进展的能力曲线，也没有涌现能力宣称；不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不训练/优化代理指标；round-robin/BT/SWIM 是排名方法，非对代理分数的过优化实验，故不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5: 每顺序两次调用；p.20: 消融重复 50 次并报告均值/SD；p.8: 相关比较报告 2000 trials 与 95% CI；p.9: 代码/数据链接。 | 有一定重复与不确定性报告及可复现材料；但并非每个分数都报告 N/CI，部分判官 snapshot 不精确，模型比较未普遍做配对检验，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 pairwise 判官提示，无对话历史累积，也不主张多轮部署，故不适用。 |

## 编码小结
论文对 LLM 判官的非传递性、位置偏差及排名稳健性做了系统实证分析，提示模板、判官版本和位置切换等报告较清楚，并提供代码与数据链接。主要不足包括：无预注册与事前功效分析，部分采样超参与快照信息不完整，自偏好、基准污染与饱和风险未充分处理，部分统计不确定性与多重比较报告不足。大量人类心理实验组件因无人类被试分配/顺序设计而记为 NA；与 LLM 判官直接相关的 J1、J2、J4、J6、J8、J11、J12、J14、J19 等已按实际风险编码。
