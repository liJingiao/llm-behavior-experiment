# article_202 | Unveiling Causal Reasoning in Large Language Models: Reality or Mirage? | 2024

研究类型概述：LLM 基准评测与方法提出研究：比较 4 个 LLM、4 种提示/推理方法（Vanilla、CoT、RAG、G2-Reasoner）及 4 个因果问答基准（COPA、e-CARE、CausalNet、CausalProbe-E/H），主要指标为 exact match，并构建 CausalProbe 2024。无人类被试实验；人类志愿者仅用于 CausalProbe-H 子集质量核查。
- **研究构念（Construct）**：因果推理的浅层知识依赖与新颖、想象和反事实情境泛化｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：让现成LLM回答旧因果基准和CausalProbe-2024问题，并在常见、新鲜、想象和反事实情境中比较表现。（改变语料新颖度、因果问题层级、情境类型及是否提供通用知识和目标导向提示。）｜CA 任务锚定：演绎推理任务（deductive reasoning task, `trm_4c898b8c2d071`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p8 Table 2: methods Vanilla/CoT/RAG/G2-Reasoner across 4 LLMs; p5 Figure 3 goal-oriented prompt. | 提示/推理方法是被比较的操纵条件，至少 4 个水平已命名；但未报告正式操纵程序、单位分配或操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p8 Table 2: 'The metric is exact match (EM)'; p10 defines exact match and partial match; p22 Table 6 reports SDs. | 因变量指标与计分方式明确；但缺少测量信度/效度证据及分布/天花板地板预处理说明。 |
| A3 | 控制变量 | 0.5 | p17 Appendix C: 'temperature ... 1.0 ... 0 ... maximal new tokens as 128 ... 50'; p10: Ubuntu 20.04 and NVIDIA RTX A6000 GPUs. | 报告了温度、最大 token 数与硬件等部分控制；未系统列出全部控制变量，也未讨论这些固定设置的外部效度限制。 |
| A4 | 混淆变量 | 1 | p6 Table 1 training cut-off dates; p9 uses Min-K% Prob for freshness; p16 Limitations admits CausalProbe 2024 may not be fully unseen; p22 Appendix I.3 discusses model/generation/language bias. | 识别了训练数据污染/语料新鲜度这一关键混淆并进行 Min-K 检测，同时讨论残余不可见性问题与基准生成偏差，符合识别、控制与残余威胁报告。 |
| A5 | 调节变量 | NA | — | 论文无明确调节变量、调节假设或交互检验，故不适用。 |
| A6 | 中介变量 | NA | — | 论文无中介变量、直接/间接效应分解或中介假设，故不适用。 |
| A7 | 操作性定义 | 0.5 | p4 Definitions 1-3 define causal reasoning levels; p9 describes CausalProbe construction stages; p8 uses exact match; p24 Figure 14 gives construction prompts. | 基准构建与 EM 计分较可复现，但 level-1/2 构念主要通过理论定义与语料新鲜度间接操作化，未给出完整的可复现操作化链条。 |
| A8 | 水平数与类型 | 0.5 | p8 Table 2 lists four methods, four LLMs and four benchmarks; p9 describes CausalProbe-E/H/M. | 水平数与标签基本明确；但未说明水平类型、间距/全距，连续变量中心化等也不适用或未报告。 |
| A9 | 单一操作化的风险 | 1 | p8 Table 2 includes COPA, e-CARE, CausalNet, CausalProbe-E and -H; p10 reports exact match and partial match; p10 notes consistent declines as corpora become fresher. | 关键构念采用多个基准与多个模型评测，并报告跨基准的一致模式，具备多操作化会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 研究不使用人类自陈量表或同源自评；IV 为提示/方法与基准，DV 为客观 EM 分数，共同方法偏差问题不适用。 |
| B1 | 被试间设计 | NA | — | 无人类或 LLM 被试被分配到互斥条件；模型/方法是固定评测组合，不适用被试间设计。 |
| B2 | 被试内设计 | NA | — | 无需要顺序平衡的被试内重复测量设计；各方法在同一固定测试集上独立推理，不按 LLM 试次顺序设计。 |
| B3 | 混合设计 | NA | — | 无混合设计及逐因素组间/组内标注，不适用。 |
| B4 | 因子设计 | NA | — | 论文是基准评测与方法比较，无正式因子设计、设计矩阵或交互统计；不适用 B4 因子设计组件。 |
| B5 | 主效应 | NA | — | 无因子设计下的主效应统计检验，不适用。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验与简单效应分析，不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计，不适用。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计，不适用。 |
| B9 | 准实验设计 | NA | — | 无随机分配实验或明确定义的准实验处理分配；论文是既有基准与自建基准的评测比较，不适用准实验设计组件。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理与迁移对称性问题，不适用。 |
| C1 | 随机化 | NA | — | 研究单位未被随机分配到互斥实验条件；同一测试集对多方法固定评测，不适用随机化组件。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件顺序或顺序效应设计，不适用。 |
| C3 | 恒定 | 0.5 | p17 Appendix C reports temperature 1.0 for closed-source and 0 for open-source, max new tokens 128 for CoT and 50 otherwise; p10 reports Ubuntu 20.04 and RTX A6000 GPUs. | 列出了若干被恒定变量及具体水平；但未系统列出全部恒定变量，也未讨论这些设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 无匹配设计或匹配后均衡性检验，不适用。 |
| C5 | 纳入为变量 | NA | — | 未将已知混淆变量作为区组或协变量纳入统计模型，不适用。 |
| C6 | 盲法 | NA | — | 无人类被试/主试盲法实验；LLM 推理自动进行，不适用盲法组件。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级，不适用。 |
| D1 | 练习效应 | NA | — | LLM 各条件独立推理，无跨试次练习效应或练习块安排，不适用。 |
| D2 | 疲劳效应 | NA | — | 无人类或 LLM 长 session 疲劳问题，不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各评测条件独立，无跨条件延滞/迁移或清洗期设计，不适用。 |
| D4 | 不对称迁移 | NA | — | 无交叉条件迁移对称性检验，不适用。 |
| D5 | 范围效应 | NA | — | 因变量为客观 EM 分数，不使用主观量表或范围效应，不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p2 Figure 1(c) shows choice_1 to choice_4 with 'answer': 2; p23 Figure 9 CausalProbe example has 'answer': 3; no option-order randomization or answer-position distribution is reported. | 多选选项按固定生成顺序呈现，未报告选项顺序随机化/反平衡或各位置正确率，故为未控制。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较，不适用。 |
| E4 | 需求特征 | NA | — | 无人类实验参与者的需求特征或掩饰情节设计；人类志愿者仅参与基准质量核查，不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集为自动化 LLM 推理，无人类主试/评分者期望效应，不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p8 Table 2 and p22 Table 6 report means and SDs, e.g. Claude 3 opus on COPA 0.993±0.001 and CausalProbe-H around 0.688; no skew or endpoint frequencies are reported. | 报告了均值与标准差且部分条件接近上限，但未报告偏度、端点频率或 pilot 难度校准，故部分满足。 |
| E7 | 共同方法偏差 | NA | — | IV 和 DV 均来自 LLM 客观任务表现，非自陈式同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p8 Table 2 reports only EM means; p22 Table 6 adds SDs; p27 checklist states no error bars/statistical significance for inference experiments. | 无效应量、置信区间、功效分析或显著性/多重比较校正，仅报告点估计和部分 SD。 |
| F2 | 内部效度 | 0.5 | p6 Table 1 gives training cut-offs; p9 uses Min-K% Prob to check freshness; p16 Limitations discusses inability to fully confirm unseen; no randomization or flow diagram. | 属于非随机基准比较；主要内部效度威胁（训练数据污染）有检测和讨论，但无分配程序、基线等价检验或被试流向。 |
| F3 | 构念效度 | 0.5 | p20 reports human QC with 13 qualified volunteers and 89.2% qualification for CausalProbe-HQ; p9 uses Min-K% Prob; p8 uses exact match. | 有基准质量控制与多基准结果，但无正式信度/效度指标，也无针对理论构念的操纵检验。 |
| F4 | 外部效度 | 0.5 | p6 Table 1 lists four studied LLMs; p8 states corpora from BBC and The Guardian; p16 discusses limitations; no representative sampling or cross-context replication. | 报告了模型与数据来源，但样本代表性有限，推广边界讨论不系统，未做跨情境复现。 |
| G1 | 分析单位 | 0.5 | p8 Table 2 averages exact match over benchmark items; p21 states CausalProbe includes 6,922 Q&A items; no item-level multilevel model is reported. | 分析主要在模型×基准层面汇总；题目嵌套于基准的聚集方差未被显式建模或报告。 |
| G2 | 随机效应 | NA | — | 模型版本是被研究的固定集合，没有按模型/被试抽样总体进行随机效应推断的需求，不适用混合模型随机效应组件。 |
| G3 | 材料作为随机效应 | 0 | p8 Table 2 reports only average EM over items; p21 describes 6,922 Q&A items but no (1&#124;item) random effect or F′ analysis. | 题目/材料被视为固定测试集，未将材料作为随机效应纳入分析，结论未体现对材料总体的推广。 |
| G4 | 统计功效 | 0 | p8 Table 2 and p22 Table 6 report EM and SD; no power analysis, target effect size, CI or sample-size justification appears. | 无设计阶段功效分析或样本量/重复次数依据，结果部分也未报告效应量置信区间。 |
| G5 | 研究者自由度 | 0.5 | p9 reports filtering articles >15,000 chars and unethical questions; p20 reports benchmark QC; p8 Table 2 reports all four methods and benchmarks; no explicit exploratory/confirmatory labels. | 报告了数据过滤/质控与主要条件，但未完整说明样本量决定、所有因变量/条件报告边界及验证性与探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number or analysis plan is mentioned; p16 only discusses limitations. | 无数据收集前预注册或分析计划，按规则记 0。 |
| J1 | 位置偏差 | 0 | p2 Figure 1(c) has choice_1 to choice_4 and 'answer': 2; p23 Figure 9 CausalProbe has 'answer': 3; no position randomization, flip rate or position-wise accuracy is reported. | 多项选择答案位置固定，未报告位置反平衡/随机化、交换前后翻转率或答案位置分布，存在未控制的位置偏差。 |
| J2 | 冗长偏差 | NA | — | 评估使用 exact match 而非 LLM 裁判或开放生成质量评分，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户立场、反馈或多轮纠错输入，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 对被评模型输出评分，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 模型评估为零样本/检索式提示，无 few-shot in-context 示例选择与排列实验，不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p5 Figure 3 shows the goal-oriented prompt; p24 Figure 14 shows construction prompts; no semantic-equivalence sensitivity ablation or dev/test split is reported. | 提供了部分提示模板，但未做提示措辞敏感性消融，也未说明 prompt 是否在测试集上调参。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0 | p5 Figure 3 uses RAG; p9 removes articles exceeding 15,000 characters; actual context token counts and key-information position × accuracy curves are absent. | RAG/上下文实验中未报告实际 token 数，也未操纵关键信息在上下文中的位置或报告中间迷失曲线。 |
| J8 | 温度与采样随机性 | 0.5 | p17 sets temperature 1.0 for closed-source and 0 for open-source, max new tokens 128/50; p19 says closed-source experiments repeated three times with SDs in Table 6. | 报告了主要采样参数和部分重复；但未报告 top-p/top-k、随机种子或置信区间，开源模型重复信息不足。 |
| J9 | 重复与文本退化 | NA | — | 任务输出为多项选择/短答案，不涉及开放生成文本的重复与退化评估，不适用。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文，无跨语言/跨脚本比较，分词效应组件不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p6 Table 1 compares LLM cut-offs with CausalProbe 2024; p9 and p18-p19 use Min-K% Prob; p16 admits CausalProbe may still not be absolutely unseen. | 有训练截止对照和污染检测，但仅在开源模型上做、未报告明确污染率，且残余不可见性限制只能部分缓解。 |
| J12 | 基准饱和 | 0.5 | p8 Table 2 shows COPA scores near ceiling for Claude 3 opus (0.991) and LLaMA 3 (0.937); p10 notes CausalProbe is harder; no saturation analysis or CI comparison. | 报告了基准水位并引入更难基准，但未系统处理 COPA 等接近天花板的指标，也未用连续指标或 CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，且无按约束类型拆分准确率的测量，不适用。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 任务仅要求选择选项 ID，不涉及 JSON/grammar-constrained 等结构化输出设置，不适用。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱或有害请求评估，不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p4 Definitions 2-3 define level-1/level-2 causal reasoning in human-like terms; p1 abstract claims genuine causal reasoning akin to humans; no human same-paradigm comparison is reported. | 论文明确把 LLM 因果推理与人类 level-1/2 构念关联，并报告模型版本；但缺少人类同范式对照实验，构念效度论证不完整。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨模型规模/训练进展的能力曲线，也未宣称涌现或指标诱导假象，不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究未对 benchmark/奖励模型/LLM-judge 代理指标进行训练或 best-of-N 优化，不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p19 says closed-source experiments were repeated three times and p22 Table 6 reports SDs; p8 provides code/data link; model names are given without precise API snapshot dates and no paired tests/CI are reported. | 报告了部分重复次数与 SD/代码，但模型 snapshot 不精确，缺少置信区间和配对检验，开放源模型重复次数未明确。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮问答评测，无多轮对话一致性衰减设计，不适用。 |

## 编码小结
论文核心是基准构建、LLM 评测与 RAG/目标提示方法比较，不是随机化心理实验。其训练数据新鲜度控制与 Min-K 检测较好，但评测统计以均值/标准差为主，缺少推断统计、置信区间、位置平衡、提示敏感性、采样完整报告等。多数人类被试特有的分配与顺序组件不适用（NA）；对 LLM 评测实际存在的风险按 J 组编码。
