# article_068 | The Essence of Contextual Understanding in Theory of Mind: A Study on Question Answering with Story Characters | 2025

研究类型概述：研究构建了 CharToM-QA 基准（1,035 道基于经典小说的 ToM 问答），并在生成式 QA 与多选 QA 两种任务上评测多个 LLM；操纵或分层变量包括上下文窗口长度（c=0/1k/2k tokens）、模型、语言（英文/中文）与 ToM 维度（Belief/Intention/Emotion/Desire）。另招募 8 名研究生进行小规模人类多选 QA 研究，比较读过/未读过小说及 c=0/2k 条件。主要分析单位是问题/模型响应，人类研究为辅助。
- **研究构念（Construct）**：心理理论与语境化心理状态归因（theory of mind and contextual mental-state attribution）｜CA 构念锚定：心理理论（theory of mind, `trm_4a3fd79d0b392`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：研究构建了 CharToM-QA 基准（1,035 道基于经典小说的 ToM 问答），并在生成式 QA 与多选 QA 两种任务上评测多个 LLM；操纵或分层变量包括上下文窗口长度（c=0/1k/2k tokens）、模型、语言（英文/中文）与 ToM 维度（Belief/Intention/Emotion/Desire）。另招募 8 名研究生进行小规模人类多选 QA 研究，比较读过/未读过小说及 c=0/2k 条件。主要分析单位是问题/模型响应，人类研究为辅助。｜CA 任务锚定：心理理论任务（theory of mind task, `trm_4c8a8467304e2`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'we vary the context lengths of story plots exposed to models'; Table 1/2 set c=0,1k,2k. | 明确命名并操纵了上下文长度，报告了三个水平；但未报告单位如何分配到水平、随机化细节或操纵检验，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.6: BPC is 'percentage of bonus points' included; PR is 'rate of model responses judged as defective'; multichoice QA uses standard accuracy. p.14 Table 7 reports BPC-human correlation 0.92. | 因变量指标与计分方式明确，且有部分效度证据；但缺信度证据、连续指标预处理和天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | p.6: 'responses of roughly the same length as corresponding answers'; 'no more than 1.5 times longer'; vanilla prompting. | 报告了长度约束与统一提示等控制手段，但未系统列出控制变量清单并逐一说明控制方式。 |
| A4 | 混淆变量 | 0.5 | p.8: 'LLMs may solve our task largely with their memory of the books and reviews, exhibiting the Clever Hans phenomenon'; no formal control or sensitivity analysis. | 识别了预训练记忆/污染这一潜在混淆，但未控制或量化残余威胁，只作为未来工作讨论。 |
| A5 | 调节变量 | NA | — | 论文没有明确调节变量、调节假设或乘积项交互检验；模型/维度/语言比较是描述性分组，不构成调节分析。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或中介效应假设与分解。 |
| A7 | 操作性定义 | 1 | p.3-p.5: problem formulation, ToM dimension definitions, QA construction; p.13 Appendix B definitions; p.17-p.19 full prompts and scoring protocols. | 关键构念（ToM 维度、上下文窗口、BPC/PR、accuracy）均有可观测、可重复执行的操作化程序，达到可复现程度。 |
| A8 | 水平数与类型 | 0.5 | p.6-p.7: context windows set to c=0/1k/2k; models listed in Table 1/2. | 报告了主要水平数与取值，但未系统说明水平类型、水平间距/全距及连续变量中心化。模型/维度/语言多为分类水平。 |
| A9 | 单一操作化的风险 | 1 | p.14 Table 7: BPC vs RougeL vs BertScore and 'Human Correlation' 0.92/0.72/0.81; multiple ToM dimensions and QA formats. | 关键构念采用多种指标与人工评分对照，并报告了会聚证据；非单一操作化。 |
| A10 | 单一方法的风险 | 0.5 | p.6: GPT-4o is used as evaluator; GPT-4o is also an evaluated model in Table 1/2. p.14 reports human correlation for BPC. | 存在同源/同家族模型生成与评判风险；有人类评分相关的部分验证，但未做正式共同方法偏差或自我偏好控制。 |
| B1 | 被试间设计 | NA | p.7-p.8: same models evaluated across context lengths; human participants also answer both read/unread and c=0/c=2k conditions. | 没有清晰的独立被试组只接受一个条件；LLM 条件为同一模型/问题上的重复评估，人类熟悉度也非纯被试间分配。 |
| B2 | 被试内设计 | 0.5 | p.7: human participant 'is initially asked ... (c=0). Then ... extended plot window ... (c=2k)'; models evaluated at c=0/1k/2k. | 存在重复测量/同一问题跨上下文条件评估，但未报告条件顺序平衡或各顺序分配；人类研究顺序固定为 c=0 后 c=2k。 |
| B3 | 混合设计 | 0 | p.7-p.8 Tables 1/2 present model × context × dimension × language descriptively, but no per-factor between/within labeling or mixed model. | 实际含模型（系统间）与上下文长度（同题重复）等多类因素，但未逐因素标注组间/组内，也未用混合模型分别报告误差项。 |
| B4 | 因子设计 | 0 | p.7-p.8 Tables 1/2 cross models, dimensions and context lengths, but contain no interaction terms or full factorial inferential statistics. | 虽有多因素表格，但未报告设计矩阵、每格样本量或交互项统计，未达到因子设计报告要求。 |
| B5 | 主效应 | 0 | p.7-p.8 Tables 1/2 report descriptive percentages only. | 没有报告各因素主效应的统计检验、自由度、p 值或效应量；不能算完整主效应报告。 |
| B6 | 交互作用 | 0 | p.7-p.8 Tables 1/2 report no interaction test, simple effects, or interaction CIs. | 未对任何因素交互作统计检验，也未在交互显著时做简单效应分析。 |
| B7 | 区组设计 | NA | — | 研究没有使用区组或分层随机设计，也没有区组变量与区内分配程序。 |
| B8 | 拉丁方 | NA | — | 研究没有采用拉丁方平衡处理顺序；条件顺序并未按拉丁方设计报告。 |
| B9 | 准实验设计 | 0 | p.7: 'we divided the human annotators into two groups' by whether they had read the books; conclusion states human ToM 'benefits from familiarity with novels'. | 人类熟悉度是自然发生的非随机分组，但未说明准实验类型、选择偏差、匹配/前测控制或因果推断限制。 |
| B10 | 被试内设计的适用条件 | 0 | p.7: same human participant answers first c=0, then extended c=2k; context exposure is irreversible. | 被试内上下文暴露不可逆且未论证可逆性/迁移对称性；也没有改用被试间或缓解措施。 |
| C1 | 随机化 | 0 | p.6-p.8: models evaluated on fixed benchmark; context lengths and human familiarity conditions are pre-specified, no randomization procedure or random-number tool reported. | 未报告随机分配方法、随机数生成工具或分配隐藏；人类熟悉度也不是随机分配。 |
| C2 | 平衡 | 0 | p.7: human c=0 then c=2k fixed order; no counterbalancing described for LLM context conditions. | 条件顺序未平衡；人类研究采用固定顺序，存在顺序与条件混淆。 |
| C3 | 恒定 | 0.5 | p.6: length constraint no more than 1.5× answer; vanilla prompts; fixed plot windows c=0/1k/2k. | 报告了若干恒定的提示与长度约束，但未系统列出所有恒定变量及其水平，也未讨论外部效度限制。 |
| C4 | 匹配 | 0.5 | p.7: 150 questions sampled and 'each question is assigned to one person who had read the book and one who had not'. | 人类比较按问题配对了读过/未读者，属于匹配；但未报告匹配方法、匹配后均衡性检验或回归假象讨论。 |
| C5 | 纳入为变量 | 0 | p.8: pretraining memory/Clever Hans is noted as possible explanation, but no measured confound is included as covariate or block in analysis. | 已识别的污染/记忆混淆没有被测量并纳入协变量/区组，也未做斜率齐性等检验。 |
| C6 | 盲法 | 0 | p.6-p.14: GPT-4o evaluator and human experts are used; no blinding type, masking, or success check is reported. | 未报告盲法安排；LLM 裁判与人工评分者是否知道条件/模型身份也未说明。 |
| C7 | 平衡的层级 | 0 | p.7: fixed c=0 → c=2k order for human study; no ABBA/Latin-square/completely balanced level described. | 未说明所用平衡层级与构造方法，且实际采用固定顺序。 |
| D1 | 练习效应 | 0 | p.7: participants respond to 600 question instances; no practice block, warm-up, or trial-position covariate described. | 存在大量试次和跨上下文重复作答，但无练习效应控制或试次位置分析。 |
| D2 | 疲劳效应 | 0 | p.7: 8 participants answer 600 question instances; no session duration, breaks, or fatigue control reported. | 人类研究任务量较大，但未报告时长、休息或时间分散方案。 |
| D3 | 延滞 / 迁移效应 | 0 | p.7: same participant first answers without extended context, then revises with c=2k; no washout or carryover modeling. | 人类上下文暴露按固定顺序进行，先前作答/阅读可能迁移到后续条件，但未识别或建模。 |
| D4 | 不对称迁移 | 0 | p.7: no test of order × condition interaction or asymmetric transfer; context exposure after c=0 is irreversible. | 未检验迁移对称性；人类设计中的上下文暴露可能不对称，但未讨论平衡失效。 |
| D5 | 范围效应 | NA | — | 主要因变量为 accuracy、BPC、PR 等客观/可判定指标，不使用主观量表评分的范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0 | p.6/p.18 Table 15: candidate choices are presented as (1)-(4), but no randomization or balancing of correct-option position is reported; examples on p.20 show correct choice (3). | 多选选项顺序与正确答案位置未做随机化/反平衡，也未讨论位置偏差。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分题与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也不做跨群体量表反应风格比较。 |
| E4 | 需求特征 | 0 | p.7: human participants are recruited to answer multichoice questions; no cover story or post-experimental inquiry reported. | 人类被试可能推断研究目的（ToM/熟悉度比较），但未使用掩饰情节，也未做事后需求特征检查。 |
| E5 | 实验者效应 | 0 | p.7: human study procedure described without experimenter blinding, rater training, or standardized script details. | 未报告主试/评分者是否知道假设或条件，也未报告培训标准化与脚本化程度。 |
| E6 | 天花板 / 地板效应 | 0 | p.7-p.8 Tables 1/2 report means/percentages only; no SD, skewness, endpoint frequencies, or pilot difficulty calibration. | 未报告因变量分布或端点频率，无法排查天花板/地板效应；任务校准过程未说明。 |
| E7 | 共同方法偏差 | NA | — | 研究不是同源自陈式多构念测量；主要指标为模型输出评分和客观多选正确率。 |
| F1 | 统计结论效度 | 0 | p.7-p.8 Tables 1/2/3 report point percentages/means; no CI, sample-size justification, power analysis, or multiplicity correction. | 仅报告描述性点估计，缺效应量置信区间、功效依据和多重比较校正；未达基本要件。 |
| F2 | 内部效度 | 0 | p.6-p.8: no random assignment, allocation concealment, baseline equivalence test, participant flow, or attrition handling. | 内部效度威胁（污染、熟悉度选择、固定顺序）未系统控制或评估。 |
| F3 | 构念效度 | 0.5 | p.14 Table 7 reports human correlations of BPC/RougeL/BertScore; human study validates subset. No reliability/inter-rater agreement or manipulation check. | 有部分效度证据（与人类评分相关），但缺信度、操纵检验与系统构念论证。 |
| F4 | 外部效度 | 0.5 | p.7: 8 native Chinese-speaking graduate students; 20 novels and 150 characters listed p.13. | 报告了人类样本来源与部分材料范围，但样本小且代表性有限，未系统讨论推广边界或跨样本复现。 |
| G1 | 分析单位 | 0 | p.7-p.13: analyses aggregate question-level accuracy/BPC across books/characters/models; no explicit multilevel or clustering treatment. | 问题嵌套于书/人物、重复测量于模型，但分析未显式处理嵌套或匹配，存在分析单位/聚集问题。 |
| G2 | 随机效应 | 0 | p.7-p.8: descriptive aggregate results; no random-effects structure for model/question/character reported. | 未使用混合模型或说明随机效应；模型与问题均按固定集合处理。 |
| G3 | 材料作为随机效应 | 0 | p.13 Table 4 lists 20 books and 1,035 questions; results are aggregated without item random effects or F1/F2 combination. | 材料/问题未被建模为从更大项目总体抽样，未控制项目随机变异。 |
| G4 | 统计功效 | 0 | No power analysis or sample-size justification reported in p.6-p.8; no CIs reported. | 未报告设计阶段功效分析、目标效应量或样本量推导。 |
| G5 | 研究者自由度 | 0.5 | p.6-p.7 lists six LLMs, metrics, context lengths and human subset; no exclusion rules, sample-size stopping rules, or confirmatory/exploratory labeling. | 报告了较多条件与指标，但未完整报告排除规则、样本量决定方式及探索/验证分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or analysis plan is reported. | 未见预注册；属于事后报告的分析路径，不能区分验证性与探索性。 |
| J1 | 位置偏差 | 0 | p.18 Table 15 instructs models to choose one of candidates (1)-(4); no position randomization/balancing or flip-rate analysis is reported; examples on p.20 have correct choice (3). | 涉及 LLM 多选位置，但完全未报告位置反平衡、正确答案位置分布或位置×正确率曲线。 |
| J2 | 冗长偏差 | 0.5 | p.6: responses required to be roughly same length and no more than 1.5× answer length to avoid arbitrarily long responses; p.8 mentions truncation. | 对长度偏差做了程序控制，但未报告回答长度分布与得分的相关系数，也未报告完整裁判设置。 |
| J3 | 谄媚 | NA | — | 任务是闭卷/给定故事的多选或生成问答，没有用户立场、反馈或纠错式对话，不存在谄媚操纵。 |
| J4 | 自我偏好 | 0 | p.6: 'GPT-4o is used as evaluator'; GPT-4o is also an evaluated model in Tables 1/2. No self-preference analysis or judge anonymization. | 裁判模型与被评模型同源（GPT-4o），但未识别或控制自我偏好，也未报告异源陪审团/一致性衰减。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验使用 vanilla/zero-shot 提示；附录提示中未见 few-shot in-context 示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.15-p.19 provide full prompt templates; no prompt version/date, sensitivity ablation, or dev/test separation is reported. | 完整提示模板可获取，但缺版本化、等价措辞敏感性检验和调参/测试集分离说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p.6/p.8: context lengths are set to 0,1k,2k tokens, and longer contexts are discussed; no manipulation of key-information position within context. | 报告了实际上下文长度并检验长度效应，但未操纵关键信息首/中/尾位置，也未报告位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0 | p.6 setup lists models and prompts, but no temperature, top-p, seed, repeated sampling N, or confidence intervals. | 未报告解码采样超参、随机种子或多次重复运行方差，无法评估 LLM 非确定性。 |
| J9 | 重复与文本退化 | 0 | p.6/p.8: no decoder strategy, beam width, repetition penalty, or n-gram repetition/degeneration rate is reported; only length truncation is mentioned. | 报告了解码/重复相关控制不足；开放生成条件未说明退化率，也未保持条件间解码严格恒定。 |
| J10 | 分词效应 | 0 | p.6: 'English and Chinese' experiments; no tokenizer name/version or token/word ratio reported. | 有跨语言比较但未报告分词器版本，也未控制语言间 token 数差异。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.8: 'the evaluated books and their reviews have been exposed to the LLMs during pre-training'; no contamination detection or training cutoff comparison. | 明确识别了预训练污染/Clever Hans 风险，但未报告模型训练截止日期、n-gram/DCQ 检测或污染率。 |
| J12 | 基准饱和 | NA | — | 研究使用新构建的困难基准，BPC/accuracy 约 35-60%，未见接近天花板；不涉及饱和基准上的微小提升宣称。 |
| J13 | 指令遵循 | NA | — | 实验不以指令遵循为因变量；任务是 ToM 问答，不是 IFEval 类约束遵循评估。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.18 Table 15 requires multichoice output 'only output the index'; no format legality rate, parse failure, or retry strategy reported. | 有格式约束设置，但未报告格式合法率，也未把格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1-p.2: frames ToM as psychological capability and compares LLM with human study; p.7 human performance. | 将 LLM 作为 ToM 能力评估对象并与人类比较，部分讨论了构念意义；但未系统论证 LLM 与人类同名构念的异同，也未报告权重快照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究不报告跨模型规模/训练进展的涌现能力曲线，不涉及涌现/突变宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究是对基准的描述性评估，不涉及对代理指标的优化、RL、best-of-N 或奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.6 lists models (some versioned, e.g. GPT-3.5-Turbo-1106) but no exact API snapshot dates, repeated runs N, CIs, paired tests, or inference logs. | 未满足重复次数、置信区间、精确 snapshot 与配对检验等可复现性要求，仅报单点聚合分数。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 QA，无多轮对话历史累积，也不主张多轮部署。 |

## 编码小结
这是一篇基准构建与描述性模型评测论文，操作化与数据集构建较细，但推断统计、随机化与顺序平衡、LLM 裁判偏差控制、采样随机性、可复现性与污染检测等报告不足。多项组件仅部分满足；部分人类实验或因子推断组件未作为正式实验设计报告。
