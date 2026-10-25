# article_005 | Evaluating Language Model Agency through Negotiations (Davidson, Veselovsky, Kosinski, West) | ICLR 2024

研究类型概述：纯 LLM 实验（无人类被试）。以结构化谈判博弈（LAMEN 框架）评测 6 个 LM（gpt-3.5/gpt-4/chat-bison/claude-2/command/command-light；LLaMA 2 未通过资格测试）的 agency；自变量为模型身份、self-play vs cross-play、博弈类型（distributive/compatible/mixture/integrative）与议题数（1 或 2）；因变量为协议达成率（soft/hard）、归一化收益 U/U*、内/外忠实度、指令遵循（字数、JSON 格式）。同一 agent 轮换双方角色与先后手并取均值，每格约 25+ 次运行（gpt-4 约 15）。

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 1 | §3.5 p6: "Game complexity increases as we (i) move from one to two Issues, (ii) mix distributive and compatible Issues, and finally (iii) introduce integrative preference weights." | 博弈类型/议题数/模型/self vs cross-play 均明确命名并给出水平；LLM 实验无需被试式操纵检验 |
| A2 | 因变量 | 0.5 | §3.4 p6: "All alignment metrics are reported as fractions between 0 and 1, with 1 indicating a perfect score." | 指标、计分均明确；缺：offer 抽取（regex + gpt-3.5 回退，App. A.5）无准确率/信度验证，亦无效度证据 |
| A3 | 控制变量 | 1 | App. A.3 p17-18: "all experiments were repeated at least 25+ times at a temperature of 0.2"; Table 6 默认参数（note/message 最大字数 64、记忆设置、transcript 格式、Show rounds=True） | 控制手段逐项列出 |
| A4 | 混淆变量 | 1 | §3.1 p5: "We control for these biases by having each agent play both sides and both starting positions and then taking the average over outcomes."; App. A.2 | 识别 intra-game/先手锚定/persona/RLHF/inter-game 偏差并说明处理；inter-game 偏差明确承认未系统检验（残余威胁已如实报告） |
| A5 | 调节变量 | NA | — | 未设调节假设/交互检验；博弈类型、self/cross-play 作为分层描述而非调节分析 |
| A6 | 中介变量 | NA | — | 无中介设计 |
| A7 | 操作性定义 | 1 | §2.3 p4: "If Alice makes an offer to Bob for fewer slices than she stated as acceptable, we register this as an instance of internal unfaithfulness."; §3.4 soft/hard agreement 定义；App. E 完整 prompt | 构念（忠实度、协议、指令遵循）均有可复现程序 |
| A8 | 水平数与类型 | 1 | §2.1 p3-4 与 Fig. 2.1：distributive / compatible / mixture / integrative；§3.5 一至两个议题 | 水平标签与取值明确（名义类）；全距在 payoff 表（App. E.3）给出 |
| A9 | 单一操作化的风险 | 0.5 | App. A.2 p16-17: "we did not perform a systematic experimental sweep to establish guidelines on how important this factor is to our metrics of interest." | 主结果基本只用租房博弈一个场景；认识到 inter-game 偏差并承认未检验，但推广性限制讨论不充分；同一构念有多指标 |
| A10 | 单一方法的风险 | NA | — | 无人类问卷式同源测量；DV 来自对话日志的自动抽取，CMB 概念不适用 |
| B1 | 被试间设计 | NA | — | 无人类被试；运行为独立实例但文中未以被试间设计表述 |
| B2 | 被试内设计 | 0.5 | §3.1 p5: "having each agent play both sides and both starting positions" | 同一模型轮换角色与先后手属被试内/重复测量，已说明平衡；缺各顺序下运行数分配的报告 |
| B3 | 混合设计 | NA | — | 未按因素标注组间/组内，亦未使用相应混合模型 |
| B4 | 因子设计 | NA | — | 议题数、议题类型并未完全交叉，也未做因子 ANOVA |
| B5 | 主效应 | NA | — | 无因子检验 |
| B6 | 交互作用 | NA | — | 无交互检验 |
| B7 | 区组设计 | NA | — | 无区组 |
| B8 | 拉丁方 | NA | — | 仅两位置完全平衡，不涉拉丁方 |
| B9 | 准实验设计 | NA | — | 模型不可随机分配，但其属于被比较对象而非被试，文中无准实验论述 |
| B10 | 被试内设计的适用条件 | NA | — | 各次运行为独立 API 会话（"negotiate against independent instances"），无迁移/可逆性问题；文中未论证，属推断 |
| C1 | 随机化 | NA | — | 无随机分配；角色/先后手为完全交叉平衡 |
| C2 | 平衡 | 0.5 | §3.1 p5 同上；脚注3 p5: "The same model plays both sides and starting positions after which results are aggregated and averaged." | 报告了平衡方案；缺各顺序/角色下的运行数及对称性前提论证 |
| C3 | 恒定 | 1 | App. A.3 Table 6 p18；§5 p8: "running all models with a temperature of 0.2" | 恒定变量与水平明确；限制对外部效度的影响在 §5 有所涉及 |
| C4 | 匹配 | NA | — | 无匹配 |
| C5 | 纳入为变量 | NA | — | 无协变量分析 |
| C6 | 盲法 | NA | — | LLM-vs-LLM，无施盲对象 |
| C7 | 平衡的层级 | 0.5 | §3.1 p5 同上 | 层级为完全平衡（2 角色 × 2 先后手）且已陈述；未讨论对顺序效应形状的假设 |
| D1 | 练习效应 | NA | — | 各轮独立实例，无练习 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳 |
| D3 | 延滞/迁移效应 | NA | — | 无跨条件迁移（独立实例） |
| D4 | 不对称迁移 | NA | — | 同上 |
| D5 | 范围效应 | NA | — | 非被试内量表评分任务 |
| E1 | 位置/顺序偏差 | 1 | §3.1 p5: "the anchoring bias can give an advantage to the agent initiating the negotiation"；以双方×双先后手平衡 | 先后手位置反平衡且方案清晰 |
| E2 | 默认赞同 | NA | — | 无量表 |
| E3 | 极端/中间反应倾向 | NA | — | 无量表 |
| E4 | 需求特征 | NA | — | LLM 实验，无被试推断假设问题 |
| E5 | 实验者效应 | NA | — | 全自动流程，无主试/评分者 |
| E6 | 天花板/地板效应 | 0 | Table 1 p6, Table 2 p7 仅报均值±SE | 未报告分布形态/端点频率，也未讨论 hard agreement 率接近 0.1（地板）等情形；读到了未做 |
| E7 | 共同方法偏差 | NA | — | 非问卷同源测量 |
| F1 | 统计结论效度 | 0.5 | §4 p6: "Average results and standard errors are reported over 25+ runs for each model"; §5 p8: "hampering our ability to reduce confidence intervals further." | 报告 SE，但无 CI/效应量、无显著性检验、无多重性校正、样本量无依据 |
| F2 | 内部效度 | 0.5 | §3.1；A.4 p18 资格测试（"require at least one successful agreement to proceed"）；App. G p25 command-light 缓存疑点 | 评估了偏差威胁并报告排除；缺基线等价性与完整流向，gpt-4 运行数偏少 |
| F3 | 构念效度 | 0 | App. A.1 p16: "At this point, this proved too error-prone." | 未提供 agreement 抽取、faithfulness 度量的信效度证据；多操作化与操纵检验亦无 |
| F4 | 外部效度 | 0.5 | §2.2 p4: "self-play provides limited insight into the transportability of results"; §5 Prompts and Settings | 模型来源明确，并讨论 self-play 外推限制和 prompt 依赖；跨场景复现未做 |
| G1 | 分析单位 | 0.5 | §4 p6: "Average results and standard errors are reported over 25+ runs for each model" | 以运行为分析单位并汇总双方角色；双方嵌套于同一博弈、同模型多运行的聚集结构未处理 |
| G2 | 随机效应 | NA | — | 无推断模型 |
| G3 | 材料作为随机效应 | 0 | App. E.3 p23-24 仅一个租房 Game；App. A.2 | 材料（博弈场景）固定，未作随机抽样或纳入分析，却对"negotiation agency"作宽泛结论 |
| G4 | 统计功效 | 0 | §5 p8: "financially constrained the number of experiments we could perform" | 无功效分析；运行数仅以成本说明 |
| G5 | 研究者自由度 | 0.5 | §4 p6: "we opted to exclude this model from cross-play"; App. A.3 默认参数在 gpt-3.5 上扫描选定 | 报告了排除及参数选择，但排除为事后定性判断；未区分验证/探索分析 |
| G6 | 预先设定/预注册 | 0 | — | 文中未见预注册（读全文无提及） |
| J1 | 位置偏差 | NA | — | 非 LLM 选择/排序/裁判实验；先后手问题见 E1 |
| J2 | 冗长偏差 | NA | — | 无 LLM 裁判评质量；gpt-3.5 仅用作 offer 抽取 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈操纵 |
| J4 | 自我偏好 | NA | — | 无 LLM-as-judge |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主实验为零样本；抽取器的 few-shot 例子（App. A.5）仅为辅助且未报告 |
| J6 | 提示敏感性/脆弱性 | 0.5 | App. E.2 p23 完整 Note/Message prompt；§5 p8: "a set of prompts likely exists that would be more beneficial for each model." | 给出完整 prompt 模板，对记忆/长度/格式做了消融并承认提示依赖；缺 prompt 措辞敏感性消融、版本化与 dev/test 分离（仅在 gpt-3.5 上调参） |
| J7 | 长上下文信息位置效应 | NA | — | 非长上下文/RAG 实验 |
| J8 | 温度与采样随机性 | 0.5 | §5 p8: "running all models with a temperature of 0.2 and averaging results over many runs"; App. A.3 "at least 25+ times" | 报告 temperature 与重复次数及 SE；缺其他采样超参和种子 |
| J9 | 重复与文本退化 | 0.5 | App. A.3 temperature 0.2 保持恒定；App. G p25-26 command-light 重复回合示例 | 解码设置（仅 temperature）恒定且各条件一致；缺 top-p 等解码方式与重复率指标 |
| J10 | 分词效应 | NA | — | 单语（英语），无跨语言/格式比较 |
| J11 | 测试集污染/数据泄漏 | 0.5 | Abstract p1: "side-step accidental evaluation data leakage"; §1 讨论 benchmark 训练暴露风险 | 识别污染并以动态生成博弈规避；未评估游戏规则（改编自 Bontempo & Iyengar 2008）与训练数据重叠，未给训练截止日对照 |
| J12 | 基准饱和 | 1 | §3.4 p6: U, U* 归一化在 [0,1]；App. F 推导最优得分上下界；§4.1 报告 U*=0.5 的零和基线 | 报告量程与水位，且博弈可随模型进化增加复杂度 |
| J13 | 指令遵循 | 1 | §3.4 p6: "staying within the maximum number of words allowed to generate notes/messages (note/msg instruct) and the ability to correctly format internal offer indications using valid JSON (format instruct)" | 采用机器可判标准，按 note/msg/format 分项报告（Table 1/3） |
| J14 | 输出格式约束/结构化输出 | 1 | §3.4 同上；App. A.5 p19: "We compute our instruction-following metric for offer formatting (format instruct) by measuring the fraction of times LM-extraction is required." | 报告 JSON 格式合法率，且与内容指标（payoff/faithfulness）分开；约束为 prompt 级而非文法约束 |
| J15 | 越狱稳健性 | NA | — | 非安全拒绝/对抗攻击评估 |
| J16 | LLM 作为被试的范式定位 | 0.5 | §1 p2: "negotiation games provide a realistic and ecologically valid assessment context"; §7 p9 "how human negotiation biases carry over to LM agents" | 界定了 LM 上的构念（faithfulness、ToM 估计）并把人类谈判偏差（锚定、性别）作为控制依据，但未系统论证与人类构念的异同；未来工作承认待检验 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未做规模曲线/涌现宣称（"emergent"仅见于引言背景） |
| J18 | 指标博弈与奖励过优化 | NA | — | 无以代理指标为优化目标 |
| J19 | 评估可复现性与种子/检查点依赖 | 0.5 | §4 p6: "over 25+ runs"; Footnote 1 p1 开源 LAMEN 代码与数据；Table 1 ±SE | 有重复次数、SE、代码与转录开放；缺确切模型 snapshot 标识（文中仅 gpt-3.5/gpt-4/claude-2 等）、种子、配对检验 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | §3.4 p6: "A negotiation ends when both agents use the agreement phrase or a maximum of 10 rounds is reached."; App. A.3 记忆/历史长度消融 | 为多轮评估且控制了上下文可见性（完整 message 历史）；缺按轮次的逐轮/累积评分以识别衰减 |

## 编码小结
本文是纯 LLM 自/互博弈的评测研究，大量人类被试类组件（B1/B3–B10、D1–D5、E2–E5、E7、G2）判 NA，A10、C1、C4–C6 亦因 LLM 自动流程而 NA。核心设计控制（角色与先后手完全平衡、temperature/长度/记忆等参数恒定并给全 prompt）较为扎实，J13/J14/J12 判 1。薄弱处为统计报告（仅均值±SE、无检验/CI/功效/预注册）、测量信效度（offer 抽取未验证）、单一博弈场景的材料泛化（G3 记 0）以及模型 snapshot 与种子缺失。不确定处：B1/B10 是否应视作 NA（独立运行）、E6 在只报均值时记 0 还是 NR、F1 中 SE 是否算"不确定性报告"（本篇按 0.5）。
