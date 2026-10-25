# article_008 | Decision-Making Behavior Evaluation Framework for LLMs under Uncertain Context (Jia, Yuan, Pan, McNamara, Chen) | 2024 (NeurIPS 2024)

研究类型概述：纯 LLM 行为实验（无人类被试，人类参照值取自既有文献）。以 Tanaka-Camerer-Nguyen（TCN）多选清单彩票任务估计风险偏好 σ、概率加权 α、损失厌恶 λ；自变量为模型（ChatGPT-4-Turbo、Claude-3-Opus、Gemini-1.0-pro）与情境（无情境 / 随机分配人口学特征 / 按真实分布分配）及人口学特征（性别、年龄、教育、婚姻、居住地、性取向、残障、种族、宗教、政治倾向）；每个设置 300 次独立 API 会话，因变量为各参数估计值，并用 OLS 回归检验人口学特征对参数的影响。
- **研究构念（Construct）**：不确定情境下的风险偏好与决策（risk preference and decision under uncertainty）｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：纯 LLM 行为实验（无人类被试，人类参照值取自既有文献）。以 Tanaka-Camerer-Nguyen（TCN）多选清单彩票任务估计风险偏好 σ、概率加权 α、损失厌恶 λ；自变量为模型（ChatGPT-4-Turbo、Claude-3-Opus、Gemini-1.0-pro）与情境（无情境 / 随机分配人口学特征 / 按真实分布分配）及人口学特征（性别、年龄、教育、婚姻、居住地、性取向、残障、种族、宗教、政治倾向）；每个设置 300 次独立 API 会话，因变量为各参数估计值，并用 OLS 回归检验人口学特征对参数的影响。｜CA 任务锚定：爱荷华赌博任务（Iowa Gambling Task, `tsk_4a57abb949ae5`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | §5.2 p7: "a baseline with no demographic context (context-free), human-like demographic distributions, and augmented distributions"; Table 2 列出各人口学特征水平；附录 C Table 13 模板 | 自变量（模型、情境与 10 类人口学特征）及各水平明确；但未报告角色采纳的操纵检验，且各水平样本分配均衡性细节不完整，按统一级联口径记 0.5。 |
| A2 | 因变量 | 0.5 | §3 p4 Eq.(1)-(3)；§4 Step 2 "A switching point ... is defined as the smallest lottery number n such that"; Step 4 "midpoints of these final intervals are the estimates" | 指标 σ/α/λ、计分和估计程序明确；缺：参数为区间中点估计，其信效度/拟合度未报告；未提及回答不一致（多次切换）的处理 |
| A3 | 控制变量 | 0.5 | §5 p6: "the same session was maintained for each trial ... History from the previous game sets was cleared"; 附录 C 同一 prompt 文本，demographic 在每个问题前重复 | 报告了同一会话保持、跨游戏集清除历史、固定提示模板等控制手段；但未报告采样温度、top-p、随机种子等关键控制变量，控制清单不完整，按统一级联口径记 0.5。 |
| A4 | 混淆变量 | 0.5 | §6 Limitations p10: "the difficulty in directly comparing LLM behaviors to humans due to the complex and sensitive nature of many demographic features" | 识别了人类比较的局限；但未识别/控制 prompt 措辞、特征共现（随机叠加多个特征，"Consider the risk preferences ..."的指令性暗示）等混淆，也无敏感性分析 |
| A5 | 调节变量 | NA | — | 人口学特征作为自变量而非调节变量；无交互检验 |
| A6 | 中介变量 | NA | — | 无中介 |
| A7 | 操作性定义 | 1 | 附录 B Tables 9-11 彩票清单；附录 C Table 12/13 完整提示；§4 Steps 1-5 | 构念（风险偏好等）和操纵均有可复现程序 |
| A8 | 水平数与类型 | 1 | §5.2 Table 2 (10 个人口学组及各水平如 "15 - 24, 25 - 34 ...")；§5 三种情境 | 水平数/标签/类型明确；各特征的取值全距清楚 |
| A9 | 单一操作化的风险 | 0.5 | §6 Limitations p10: "this study uses financial experiments to elicit overall preferences, exploring other domains with other experiments could provide a more comprehensive understanding" | 用三组彩票序列（Series 1–3）测不同参数，但每个构念只有单一任务（金融彩票）；局限中承认其对推广性的限制 |
| A10 | 单一方法的风险 | NA | — | 无自变量与因变量同源问卷；参数由选择行为推得 |
| B1 | 被试间设计 | 0.5 | §4 Step 1 p5: "each query to the LLM represents an individual interaction, analogous to testing a different human subject"; §5.2 "randomly assigning LLMs foundational demographic features" | 每次会话仅一种人口学设置（情境），实质被试间；但对模型、情境层的分配（样本是否均衡）和随机分配程序细节不足 |
| B2 | 被试内设计 | 0.5 | §5 p6: "Series 1 and 2 focus on positive outcomes ... Series 3 introduces negative outcomes"; 附录 C 三道题依次在同一会话 | 同一会话依次完成三个系列属于被试内测量（不同参数）；固定顺序且保留历史，未报告顺序平衡 |
| B3 | 混合设计 | NA | — | 未按组间/组内因素建模；参数分别回归 |
| B4 | 因子设计 | 0 | Table 2；§5.2 "augmentation ... randomly incorporating other minority features" | 各人口学特征随机组合，可视为多因素，但未呈现设计矩阵、每格样本量，亦未做交互项；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | Table 7、Table 8（系数、SE、星号）；Figure 6、7 | 报告系数、SE、显著性水平；缺 CI/效应量，各变量参照组虽在表 4 注解（lifelong Democrat）但基础人口学基准未全列 |
| B6 | 交互作用 | 0 | §5.2 OLS Eq.(9)(10) 与 Table 7–8 仅含各人口学特征主效应项 | 10 类人口学特征在提示中随机组合构成多因素设计，但回归模型仅纳入主效应而完全忽略特征间交互项，按级联规则记 0。 |
| B7 | 区组设计 | NA | — | 无区组 |
| B8 | 拉丁方 | NA | — | 固定题目顺序，不涉及 |
| B9 | 准实验设计 | NA | — | 无不可随机分配的情形 |
| B10 | 被试内设计的适用条件 | 0 | §5 p6: "the same session was maintained ... to guarantee that each participating LLM can access all necessary information from the conversation history"; 附录 C: "we maintain a history of collecting all responses from the LLMs, and this information is aggregated into the subsequent inputs" | 三个系列在同一会话中保留历史，前序选择可能影响后序（可逆性/迁移）；文中仅说独立指令（"your choice should be independent"），未论证或检验迁移，属于对被试内适用条件的未做 |
| C1 | 随机化 | 0.5 | §5.2 p7: "We first generate a distribution of demographic profiles by randomly assigning LLMs foundational demographic features" | 随机分配特征并给出程序（随机/真实分布两种）；缺随机数工具、种子、分配隐藏 |
| C2 | 平衡 | 0 | 附录 C Table 12：三道题固定顺序 "first lottery ... second ... last" | 条件（Series 1→2→3）顺序固定且共享历史，无任何平衡；该组件基本要件未达成 |
| C3 | 恒定 | 1 | §5 p6 同一 prompt、同一会话、历史清除；附录 B 彩票表恒定 | 恒定的变量及水平均明确；对外部效度限制见 Limitations |
| C4 | 匹配 | NA | — | 无匹配 |
| C5 | 纳入为变量 | 0.5 | §5.2 OLS Eq.(9)(10): "RiskParameter_i = β0 + β_n Demographic_ni + ε_i" | 将基础人口学变量纳入 OLS 回归模型加以控制（达成基本要件），但未报告回归斜率齐性/共线性诊断及调整后效应量，按统一级联口径记 0.5。 |
| C6 | 盲法 | NA | — | LLM 实验，无评分者/施盲对象 |
| C7 | 平衡的层级 | 0 | 附录 C Table 12：三道题固定顺序 "first lottery ... second ... last" | 研究存在被试内/序列顺序平衡需求（同 C2），但未明确选用完全平衡、拉丁方或 ABBA 层级，亦未报告构造方法与顺序效应形状假设，记 0。 |
| D1 | 练习效应 | 0 | 附录 C: 三题连续、共享历史，无练习块 | 同会话重复判断可能产生学习/适应（上下文内），未设练习或控制 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳 |
| D3 | 延滞 / 迁移效应 | 0.5 | §5 p6: "History from the previous game sets was cleared to prevent LLMs from recollecting previous games."; 附录 C 会话内历史保留 | 识别了跨"游戏集"的迁移并清历史，但会话内三个系列仍累积历史，未检验污染 |
| D4 | 不对称迁移 | 0 | 附录 C 固定顺序 | 未检验迁移对称性，固定顺序且无反向顺序 |
| D5 | 范围效应 | 0.5 | 附录 C: "your choice should be independent of the previous and following lotteries" | 题内以指令要求独立；未讨论范围效应风险（切换点选择受清单范围锚定，Series 1 的奖励值跨度大）；二选一切换点任务，风险只部分适用 |
| E1 | 位置 / 顺序偏差 | 0 | 附录 B Tables 9-11 选项 A/B 固定；附录 C 固定题序 | 选项位置（Option A 始终为安全选项）、清单行序递增均未随机/反平衡，也未讨论；仅有 "switching point" 单调清单 |
| E2 | 默认赞同 | NA | — | 无量表 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无量表 |
| E4 | 需求特征 | 0.5 | 附录 C Table 13: "Consider the risk preferences and decision-making processes of a person with these characteristics." | 提示直接点明"考虑风险偏好"，存在明显需求特征；文中未说明或检验（也未识别为偏差）；LLM 语境下为角色扮演的提示效应，已部分讨论于 §6 "who LLMs are 'pretending to be'" |
| E5 | 实验者效应 | NA | — | 自动化 API，无实验者 |
| E6 | 天花板 / 地板效应 | 0.5 | Table 5 报告 Mean/Std/Min/Max（如 σ min 0.305, max 0.505） | 报告了描述统计及范围；未讨论 Claude σ 的低方差（SD 0.0237）与 λ 区间上限等天花板/地板问题 |
| E7 | 共同方法偏差 | NA | — | 同 A10 |
| F1 | 统计结论效度 | 0.5 | Table 7/8 系数、SE、*** 标注；Table 5/6 SD | 报告系数与 SE、显著性；无效应量/CI，无多重性校正（对 3 参数×3 模型×多特征的大量检验尤为欠缺），样本量依据仅为 "300 ... upper bound typically observed in human ... experiments" |
| F2 | 内部效度 | 0.5 | §5: "same session ... History ... cleared"；§5.2 随机分配特征 | 评估了会话污染等威胁；缺基线等价、固定题序下的顺序威胁评估，无失败调用/无效响应排除报告 |
| F3 | 构念效度 | 0.5 | §4 Step 4 "aligning with the methodology endorsed by [32]"; Table 5 与 Human Sample 对比 | 用已验证的 TCN 范式并对照人类样本均值；缺对 LLM 上参数效度的检验（如多采样一致性、模型内拟合） |
| F4 | 外部效度 | 0.5 | §5 模型选择准则 "(i) The model must be sufficiently large ... (ii) pre-trained on natural human utterances"; Limitations p10 | 说明模型来源与选择理由，局限中指出仅金融域；缺版本/日期细节及跨情境复现 |
| G1 | 分析单位 | 0.5 | §5 "each query to the LLM represents an individual interaction"; Eq.(9) 下标 i 为观测 | 以单次会话为分析单位且与随机分配层级匹配；会话嵌套于模型、各模型分别回归，未讨论；参数估计由区间中点构成的测量误差未传递 |
| G2 | 随机效应 | NA | — | 单层回归，无需随机效应 |
| G3 | 材料作为随机效应 | 0 | 附录 B 仅一套彩票表 | 材料（彩票清单）固定，唯一一套，却对"LLM 决策行为"作一般性结论，未作为随机抽样或讨论 |
| G4 | 统计功效 | 0.5 | §5 p6: "We chose a sample size of 300 data pieces, which represented the upper bound typically observed in human financial decision-making behavior experiments." | 给出样本量理由，但无功效分析、目标功效和预期效应量 |
| G5 | 研究者自由度 | 0.5 | §5 "Version names will be omitted hereafter"; §5.2 "we introduce an augmentation technique that involves randomly incorporating other minority features" | 报告模型选择准则与特征扩充方式；未报告数据排除规则（无效回答）、所有测量/条件，未区分验证与探索，亦未写明为何仅此三个模型 |
| G6 | 预先设定 / 预注册 | 0 | p.1–24 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未见预注册 |
| J1 | 位置偏差 | 0 | 附录 B Tables 9-11：Option A 固定为较安全项，且附录 C 中 A/B 位置固定 | 属选项选择任务，选项位置/清单顺序未做 A/B 交换或随机化，也未提及，读到了确实没做 |
| J2 | 冗长偏差 | NA | — | 无 LLM-as-judge |
| J3 | 谄媚 | 0.5 | 附录 C Table 13 "Consider the risk preferences ... of a person with these characteristics" | 属于用户/系统提示注入先验（角色人设），论文操纵并测量了模型对特征的响应；但未识别为谄媚/顺从偏差，也无对照提示（如仅给特征不提风险） |
| J4 | 自我偏好 | NA | — | 无 LLM-as-judge |
| J5 | 少样本示例选择与排列偏差 | NA | — | 零样本，无示例 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | 附录 C Tables 12-14 完整 prompt；§5: "Prompt templates were specifically designed to optimize for responsiveness and answer validity" | 提供完整模板；缺措辞敏感性消融、版本化与 dev/test 分离，且提示针对"响应有效性"优化的过程未说明 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 短上下文（但特征重复附加，是否有位置效应并非研究问题） |
| J8 | 温度与采样随机性 | 0.5 | §5.1 p6: "After repeatedly prompting LLMs ... 300 times ... Though they do not always produce identical responses in each round, the resulting distribution elucidates the behavior patterns" | 利用 300 次重复将采样非确定性纳入设计，并报告 SD；但未报告 temperature、top-p、种子等采样超参 |
| J9 | 重复与文本退化 | NA | — | 输出仅为数值，无文本生成与退化问题（有格式约束，见 J14） |
| J10 | 分词效应 | NA | — | 单语英语，不涉及跨语言/格式 |
| J11 | 测试集污染 / 数据泄漏 | 0 | 附录 B 彩票表采自 TCN/Holt-Laury 等经典实验 | 经典范式很可能出现在训练数据中，文中未评估或讨论，也无训练截止日对照 |
| J12 | 基准饱和 | NA | — | 非基准评测，无得分天花板问题（见 E6） |
| J13 | 指令遵循 | 0.5 | 附录 C: "Answer me with the value of <x1> only, please remember <x1> should be larger and equal to 1, less and equal to 13, do not explain." | 以机器可判格式（整数范围）要求；但未报告指令违反率或按类型拆分 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | 同上 | 提示给出格式约束，且数值范围可程序检验；未记录合法率，格式失败也未与内容分开报告 |
| J15 | 越狱稳健性 | NA | — | 非安全评估 |
| J16 | LLM 作为被试的范式定位 | 0.5 | §1 p2: "This framework represents the first application of behavioral economics to LLMs without any preset behavioral tendencies"; §4 Step 1: "we treat LLMs similarly to human populations ... we assume fixed parameters for each interaction"; §6 "who are LLMs in their most fundamental form?" | 界定了 σ/α/λ 构念并与人类样本对比，讨论 LLM 与人类差异的可能原因；但"每次查询等同一名被试、参数固定"的假设缺乏论证，且人类对照来自不同样本（Human Sample 越南 TCN）而非同任务同条件 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无规模曲线/涌现宣称 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无优化 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | §5: "ChatGPT-4-Turbo, Claude-3-Opus, and Gemini-1.0-Pro. Version names will be omitted hereafter."; NeurIPS checklist: code and data released | 重复 300 次、有 SD/回归；但明确略去版本/快照标识，亦无种子，复现受限；代码与数据已公开（检查表） |
| J20 | 多轮对话中的一致性衰减 | 0.5 | 附录 C: 三题在同一会话顺序提出且 "demographic features are added before each prompt to ensure that all features are remembered by the LLMs, thereby preventing the loss of feature memory in long-term conversations." | 属多轮会话，并通过每轮重复人设以防特征遗忘（对一致性衰减有控制意识）；但未按轮次评分或评估一致性衰减 |

## 编码小结
本篇是纯 LLM 的行为经济学评测（TCN 彩票任务），人口学特征通过 prompt 前缀"随机分配/按真实分布"操纵，主要设计为被试间（每会话一个情境）加会话内三个系列（被试内、固定顺序、保留历史）。关键判断：因会话内三题固定顺序且共享历史，B10/C2/D1/D4 记 0（基本要件未达成），而不是 NR；人口学特征作为回归自变量（C5 记 1）。选项 A/B 与清单顺序固定、无位置控制，J1/E1 记 0；经典彩票材料的污染风险未讨论（J11 记 0）。不确定处：J3 把"特征人设提示"视作谄媚相关操纵（偏宽，记 0.5）；A4/E4 对提示指令性暗示的评分；C7 因未宣称平衡而记 NA，与 C2 记 0 的区别可能被不同编码员不同处理；Table 12/14 提示中 "less and equal to 13" 的边界措辞与表内行数不一致，未作为错误处理。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 A1（1→0.5）, A3（1→0.5）, C5（1→0.5）, B6（NA→0）, B4（0.5→0）, C7（NA→0）。
