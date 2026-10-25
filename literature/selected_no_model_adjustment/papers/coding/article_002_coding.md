# article_002 | Whose Opinions Do Language Models Reflect? | 2023 (ICML, PMLR 202)

研究类型概述：LLM 行为探测/基准构建研究（无新增人类被试，人类数据来自 Pew American Trends Panel 公开调查）。9 个语言模型（AI21 与 OpenAI，350M-178B）作答 1498 道 Pew 单选题，通过下一词 log-prob 得到观点分布，与总体及 60 个人口群体的人类分布比较；自变量为模型（及是否 HF 调优）、群体提示（默认 / QA / BIO / PORTRAY 引导）、目标群体与题目主题；因变量为 1-Wasserstein 对齐度（representativeness、steerability、consistency）及拒答率、熵。页码为 PDF 页码（含附录至 p.34）。

注：CSV 实际含 69 个组件，而非 70 个。

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 1 | p.4 "We consider three approaches to supply this information to the LM": QA / BIO / PORTRAY；p.21 Table 5 列出 9 个模型；p.20 Table 4 列出 22 个引导目标群体 | 模型、引导方式（含默认无引导）、目标群体的水平、操纵程序均明确；所有模型作答同一批题；steered 相对 default 的提升（Fig.4b）起操纵检验作用 |
| A2 | 因变量 | 1 | p.4 Eq.(1) "This metric is bounded between 0 and 1, with a value of 1 implying a perfect match between the two opinion distributions"；p.7 steerability 公式；p.8 consistency C_m | 指标、计分、取值范围清楚；p.22 Fig.7 概率质量检查、p.30 B.4 稳健性提供测量可靠性证据；有序选项映射（A.4）说明预处理 |
| A3 | 控制变量 | 0.5 | p.3 "Unless otherwise specified, we present the options in the order they are provided by the survey designers"；p.30 "For a given question, the same random permutation is used across LMs" | 有控制手段（统一模板、零样本、同一排列）；缺：无系统的控制变量清单，各模型提供商/规模/训练差异未作控制 |
| A4 | 混淆变量 | 0.5 | p.9 Limitations: "has had issues with social desirability bias (Yan, 2021) that may affect the accuracy of the human opinion distribution"；p.3 用调查权重 "to correct sampling biases" | 识别了人类参照分布的偏差并用权重校正，refusal 单独比较；缺：HF 调优与 provider/规模/数据混淆未系统讨论，无敏感性分析 |
| A5 | 调节变量 | NA | — | 无调节假设；主题/群体分层为描述性，无交互检验 |
| A6 | 中介变量 | NA | — | 无中介分析 |
| A7 | 操作性定义 | 1 | p.4 "we prompt the model and obtain the next-token log probabilities ... ignoring all other possible completions"；p.3 Fig.1 prompt 模板；p.21 A.4 有序映射 | "观点""对齐""可引导性""一致性"均有可复现公式与 prompt 程序 |
| A8 | 水平数与类型 | 1 | p.21 Table 5（模型、规模、类型）；p.16 Table 2（人口属性及取值）；p.20 Table 4 | 水平数、取值、类型（有序选项映射为整数）完整；部分模型 API 快照日期未给（见 J19） |
| A9 | 单一操作化的风险 | 1 | p.4 steering 采用三种提示（QA/BIO/PORTRAY）；p.9 "Multiple-choice format. We focus on probing LM behaviors using a multiple-choice prompts, which differs from the open-ended text generation setting" | 引导有多种操作化；单选题格式的泛化限制在局限中讨论 |
| A10 | 单一方法的风险 | NA | — | 人类参照（Pew 调查）与 LM 输出为不同来源，非同源自陈测量 |
| B1 | 被试间设计 | NA | — | 无被试分配；各模型作答同一题集，为模型比较 |
| B2 | 被试内设计 | NA | — | 无顺序、无重复测量设计 |
| B3 | 混合设计 | NA | — | 非混合设计 |
| B4 | 因子设计 | NA | — | 模型×引导×群体虽交叉呈现（Fig.4b、Fig.11），但无因子设计分析与推断检验 |
| B5 | 主效应 | NA | — | 无推断统计 |
| B6 | 交互作用 | NA | — | 无交互检验 |
| B7 | 区组设计 | NA | — | 未使用区组 |
| B8 | 拉丁方 | NA | — | 非被试内顺序设计 |
| B9 | 准实验设计 | NA | — | 无被试分配 |
| B10 | 被试内设计的适用条件 | NA | — | 非被试内设计 |
| C1 | 随机化 | 0.5 | p.30 B.4.1 "randomly permuted (rather than the default ordinal) order" | 仅在稳健性分析中使用随机排列选项顺序；无条件分配；缺：随机工具/种子、排列次数未报告 |
| C2 | 平衡 | NA | — | 无条件顺序平衡需求 |
| C3 | 恒定 | 1 | p.3 "we format each question into the prompt template shown in Figure 1"；"Unless otherwise specified, we present the options in the order they are provided by the survey designers"；p.9 局限（US 中心、单选格式） | 提示模板、选项顺序、无采样（log-prob）等被恒定；局限节讨论外部效度 |
| C4 | 匹配 | NA | — | 未使用匹配 |
| C5 | 纳入为变量 | NA | — | 无协变量模型；调查权重用于校正人类分布，非实验混淆的协变量 |
| C6 | 盲法 | NA | — | 无人类被试/评分者/LLM 裁判，自动化指标计算 |
| C7 | 平衡的层级 | NA | — | 无平衡设计 |
| D1 | 练习效应 | NA | — | 各题独立作答，无试次序列 |
| D2 | 疲劳效应 | NA | — | 同上 |
| D3 | 延滞/迁移效应 | NA | — | 同上 |
| D4 | 不对称迁移 | NA | — | 同上 |
| D5 | 范围效应 | NA | — | 各题独立呈现，无被试内量表评分 |
| E1 | 位置/顺序偏差 | 0.5 | p.5 "permuting the order in which answer choices are presented to the model—see Appendix B.4"；p.30 "the same random permutation is used across LMs" | 做了选项顺序随机化稳健性检验，且各模型用同一排列；缺：主分析用固定有序顺序，每题仅一种随机排列，未做完整反平衡 |
| E2 | 默认赞同 | NA | — | 无量表反向题情境；答案字母偏差见 J1 |
| E3 | 极端/中间反应倾向 | 1 | p.6 "it typically assigns > 0.99 probability to one of the options"；p.25 Fig.9 熵分布；p.25 Fig.10 拒答率 | 报告了模型分布的熵（尖锐度）与人类对比，并用 modal 分析讨论其对结论的威胁 |
| E4 | 需求特征 | NA | — | 无人类被试 |
| E5 | 实验者效应 | NA | — | 无主试/评分者，自动化流程 |
| E6 | 天花板/地板效应 | 1 | p.5 "While the maximum possible of this score is 1, it cannot be achieved for all of the groups"；Fig.2 给出人类均值 0.949 与最差群体 0.865 作为参照 | 报告 DV 分布与上限讨论，并给出人类基线校准 |
| E7 | 共同方法偏差 | NA | — | 非同源问卷自陈 |
| F1 | 统计结论效度 | 0.5 | p.5 Fig.2 以人类群体间对齐度作量表解释效应大小 | 以人类基线解释效应量；缺：无置信区间/不确定性、无显著性检验、无样本量依据、无多重比较处理 |
| F2 | 内部效度 | 0.5 | p.5 "We ensure that all our subsequent results are robust to such design choices by replicating our analysis with (i) different prompt templates, and (ii) permuting the order"；p.22 概率质量 sanity check | 评估了提示与顺序威胁；缺：模型间差异（provider/规模/训练）的混淆未评估 |
| F3 | 构念效度 | 1 | p.1 脚注 "we do not view LMs as having their own opinions, but instead as reflecting those of humans involved in their design process"；p.22 "This is a necessary sanity check to ensure that the distributions we are deriving ... are meaningful and not just noise"；p.2 问卷由 Pew 专家设计 | 有构念澄清、测量合理性检验与操纵效果（steerability）证据；虽无正式信度系数，但有稳健性复现 |
| F4 | 外部效度 | 1 | p.12 A.1 Pew ATP 抽样 "randomly-chosen address-based sample of households"；p.9 "our conclusions are only valid for the populations in the US"；p.3 "15 ATP polls" | 报告人类样本来源与代表性、推广边界（US/WEIRD、选择题格式），并覆盖 15 次调查作跨调查检验 |
| G1 | 分析单位 | 0.5 | p.4 Eq.(1) 按题平均；p.13 "Note that questions may fall into multiple categories" | 分析单位（题、群体、主题）明确；缺：题目嵌套于调查波次/主题的聚集结构、问题多主题重叠未在分析中处理 |
| G2 | 随机效应 | NA | — | 未用混合模型 |
| G3 | 材料作为随机效应 | 0.5 | p.3 "we use 15 ATP polls, chosen to cover a range of topics" | 题目来自调查并按主题汇总；缺：非随机抽样、未将题目作随机效应或报告题间变异 |
| G4 | 统计功效 | 0 | — | 无功效/样本量论证 |
| G5 | 研究者自由度 | 0.5 | p.12-13 A.2 Post-processing（"We omit questions where the phrasing ... depends on a previous answer"）；p.7 steerability "choose the one that works best"；p.13 "we pick a subset of 500 questions where the subgroups under consideration frequently disagree" | 报告了题目修改/剔除规则与子集选择标准；缺：对三种提示取最优（max）的偏高风险未讨论，验证性/探索性未区分 |
| G6 | 预先设定/预注册 | 0 | — | 全文未提及预注册 |
| J1 | 位置偏差 | 0.5 | p.30 B.4.1 "present the model with answer choices for a question in a randomly permuted ... order"；p.21 "a random model that chooses one of the answers choices per question at random" | 做了选项位置随机化；缺：每题仅一种排列、非完整反平衡，未单独估计字母/位置偏差大小 |
| J2 | 冗长偏差 | NA | — | 无自由生成，亦无 LLM 裁判 |
| J3 | 谄媚 | NA | — | 非对话式用户立场/纠错评估；PORTRAY/BIO 为显式人设引导，是测量 steerability 而非谄媚 |
| J4 | 自我偏好 | NA | — | 无 LLM 裁判 |
| J5 | 少样本示例选择与排列偏差 | NA | p.30 B.4.2 "Example" 变体含一个示例（Answer: C） | 主分析为零样本；仅稳健性变体含单个固定示例，未构成 few-shot 实验 |
| J6 | 提示敏感性/脆弱性 | 0.5 | p.3 Fig.1 完整模板；p.30 B.4.2 "General: Please read the following multiple-choice question carefully and select ONE of the listed options." 及 Example 变体 | 提供模板并做了提示格式敏感性分析（500 题子集）；缺：无版本化记录、无 dev/test 分离，仅 3 种格式 |
| J7 | 长上下文信息位置效应 | NA | — | 非长上下文/RAG |
| J8 | 温度与采样随机性 | NA | p.4 "obtain the next-token log probabilities" | 使用下一词 log-prob，无采样随机性（A.5 温度仅用于人类分布锐化） |
| J9 | 重复与文本退化 | NA | — | 无自由生成 |
| J10 | 分词效应 | NA | — | 非跨语言/多格式输入 |
| J11 | 测试集污染/数据泄漏 | 0 | p.12 "15ATP surveys over multiple years (2017-2021)" | 公开 Pew 调查题目与结果可能进入预训练语料，全文未评估污染，也未对照模型训练截止日期 |
| J12 | 基准饱和 | NA | p.2 "We thus view our dataset and metrics as probes ... and not as a benchmark that should be indiscriminately optimized" | 定位为探针而非排行榜基准，不涉及饱和 |
| J13 | 指令遵循 | NA | — | 非指令遵循评测 |
| J14 | 输出格式约束/结构化输出 | 1 | p.4 仅取答案字母的 log-prob，"treat the refusal and non-refusal answer choices ... separately"；p.22 Fig.7 "the cumulative probability mass models assign to one of the answer choices" | 报告了格式约束设置与分配到合法选项的概率质量，并把拒答单独作指标；部分模型质量较低（"at least 30% on average"） |
| J15 | 越狱稳健性 | NA | — | 非安全/对齐攻击评测 |
| J16 | LLM 作为被试的范式定位 | 1 | p.1 脚注 "we do not view LMs as having their own opinions, but instead as reflecting those of humans involved in their design process"；p.4 "treats human alignment as an inherently subjective quantity that depends on who it is measured against" | 明确界定 LM 上测量的是与人类群体观点分布的对齐，而非"LM 拥有观点"，并讨论与人类构念的差异 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无涌现/规模曲线宣称 |
| J18 | 指标博弈与奖励过优化 | NA | p.2 "not as a benchmark that should be indiscriminately optimized" | 无优化研究；仅在局限中提醒勿盲目优化指标 |
| J19 | 评估可复现性与种子/检查点依赖 | 0.5 | p.21 Table 5 与 A.3 给出模型名及文档链接；p.12 "Our code and data are available at https://github.com/tatsu-lab/opinions_qa" | 有模型标识与代码；缺：API 快照日期、重复次数/CI 与配对检验均无 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 单轮问答 |

## 编码小结
本篇是用公开民调对 9 个语言模型做观点对齐探测，无人类实验与 LLM 裁判，因此 B、D 系列及 J2/J4/J8/J9 等多项记 NA。强项在于操作化与构念澄清（A7、A9、F3、J16）、对天花板与分布尖锐度的呈现（E3、E6）以及对 LLM 输出格式质量的检查（J14）。弱项是缺乏任何推断统计、功效、预注册（F1 仅 0.5，G4、G6 记 0）以及对训练数据污染的讨论（J11 记 0 为偏严判断，因 Pew 汇总分布未必被逐题记忆，但全文未讨论）。不确定处：A1 将"引导相对默认的提升"视为操纵检验而给 1；C1/J1 对"仅稳健性分析中随机排列一次"给 0.5；J5 将带固定示例的提示变体视为非 few-shot 实验而记 NA；J14 将 Fig.7 的概率质量视为格式合法率的等价物。

