# article_087 | Language Models can Subtly Deceive Without Lying: A Case Study on Strategic Phrasing in Legislation | 2025

研究类型概述：这是一项以 LLM 智能体模拟为核心的计算型案例研究：lobbyist 生成带有隐藏受益公司的立法修正案，critic 通过成对比较和 Bradley-Terry-Luce 排序识别隐藏受益者；研究操纵/比较不同模型族与规模、迭代 re-planning 轮次、critic 强弱及 prompt 变体，指标为 identificaiton rate 与 benefit capture rate，并辅以人类评估验证部分生成质量。分析单位为 (bill, company) 模拟 trial 及其模型 × trial 条件组合，而非人类被试。
- **研究构念（Construct）**：有意的微妙欺骗、策略性措辞与自利性意图｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：这是一项以 LLM 智能体模拟为核心的计算型案例研究：lobbyist 生成带有隐藏受益公司的立法修正案，critic 通过成对比较和 Bradley-Terry-Luce 排序识别隐藏受益者；研究操纵/比较不同模型族与规模、迭代 re-planning 轮次、critic 强弱及 prompt 变体，指标为 identificaiton rate 与 benefit capture rate，并辅以人类评估验证部分生成质量。分析单位为 (bill, company) 模拟 trial 及其模型 × trial 条件组合，而非人类被试。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: “We use 3 instruction-tuned chatbot LLMs: Qwen-chat, Mixtral-instruct, and Yi-chat, across multiple scales from 7B to 72B parameters.”；p.6: “initial trial followed by two re-planning trials – these correspond to the three bars.” | 自变量被明确命名并给出模型规模/族与 trial 水平，生成与 re-planning 程序有描述；但未报告传统 manipulation check，条件分配也主要是对固定数据集全量运行，故为部分完整。 |
| A2 | 因变量 | 0.5 | p.6: “Identification Rate... Benefit Capture Rate... a trial will score 0, 1/3, 2/3, or 1”；p.7 Table 2 报告 bootstrap SD，p.7 Table 3 报告人评与自动分数一致性。 | 因变量指标与计分方式明确，且有 bootstrap 不确定性与部分人评一致性证据；但缺少系统信效度检验及连续指标预处理/天花板地板说明。 |
| A3 | 控制变量 | 0.5 | p.5: “Unless otherwise stated, we use separate instances of the same LLM for the modules.”；p.19: 给出模型、Guidance 约束生成、固定 prompt 结构与数据过滤。 | 论文保持模型、数据、prompt 结构与生成约束等条件较一致，并做 prompt ablation；但未以控制变量清单形式逐项说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.9: prompt robustness/ablation；“No significant effect... under ±3 percentage points”；p.9-p.10 Limitations 讨论 critic 模型局限、立法模拟简化与开源模型限制。 | 识别了 prompt、critic 强弱、模型局限和场景简化等潜在混淆并做部分稳健性检验；但未系统讨论所有残余混淆及其对内部效度的定量威胁。 |
| A5 | 调节变量 | NA | — | 理论模型未提出调节假设，也未以调节变量进行交互检验；模型规模比较属于条件比较而非正式调节模型。 |
| A6 | 中介变量 | NA | — | 理论模型不包含中介变量，也未报告直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.4-p.5 详述 lobbyist/critic 目标、S_eval 与 S_crit；p.6 “If any of the three draft amendments... score of 1...”；p.20-p.24 附录给出完整 generation、critic、re-planning 与 benefit-capture prompts。 | 关键构念均有可观测、可重复执行的操作化：隐藏受益生成、critic 成对比较识别、benefit entailment 评分与 re-planning 反馈；操作程序足以复现。 |
| A8 | 水平数与类型 | 0.5 | p.5: 模型列有 7B/14B/34B/47B/72B 多个族与规模；p.6: trial 1/2/3；p.8-p.9 prompt variation 与 ablation。 | 报告了主要条件水平与标签，但未说明水平类型（分类/等级/连续）、规模间距与全距，也没有连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.6 两个主要指标；p.7 人类评估验证 benefit capture；p.9 Limitations 提到 critic 模型本身局限。 | 部分采用多指标/人评验证，但核心 deception 主要仍由单一 critic 识别定义；对单一操作化局限的讨论有限。 |
| A10 | 单一方法的风险 | 0.5 | p.5: “separate instances of the same LLM for the modules”；p.7 Table 3 报告 human evaluation 与 automated score 的一致性。 | 生成与评判同属 LLM 方法来源，论文用异源更强 critic 和人类评估部分缓解；但未做正式共同方法偏差统计检验或系统程序控制说明。 |
| B1 | 被试间设计 | NA | — | 无人类被试向互斥条件的随机分配；不同模型是在同一数据集上分别运行，不是传统被试间设计。 |
| B2 | 被试内设计 | NA | — | trial 1-3 是迭代优化处理而非可平衡的重复测量条件序列；不存在对人类被试内条件的顺序平衡设计。 |
| B3 | 混合设计 | 0.5 | p.5-p.6 按模型报告并跨 trial 1/2/3 报告；“initial trial followed by two re-planning trials”；Table 2 按 model × trial 列出。 | 结果结构可视为模型间与 trial 内的比较，但论文未逐因素标注组间/组内，也未使用混合模型或分别报告两类误差项。 |
| B4 | 因子设计 | 0 | p.6 Figure 2 与 Table 2 报告 6 个模型 × 3 个 trial 的组合结果及 bootstrap SD。 | 多因素条件基本完全交叉并给出每格描述性结果，但未提供正式设计矩阵、样本量表和 ANOVA/交互检验；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p.6 仅报告模型间识别率趋势和 trial 下降百分点的描述统计，如 “45.0 pp. → 61.2 pp. → 83.7 pp.”。 | 未对模型主效应或 trial 主效应报告正式统计检验（F/df/p/效应量），仅有描述性比较。 |
| B6 | 交互作用 | 0 | p.6: “the drop in identification rate across trials... also increases with model size”；未给出交互项检验。 | 有交互趋势的定性描述，但未报告模型 × trial 交互项的统计检验、简单效应或图示误差棒检验。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机设计，也未按前测或自然属性划分区组。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计；trial 轮次由迭代 re-planning 固定决定。 |
| B9 | 准实验设计 | NA | — | 并非准实验因果设计；模型与 prompt 条件是研究者设定的计算条件，而不是对非随机人类被试组的准实验比较。 |
| B10 | 被试内设计的适用条件 | NA | — | 不存在需要论证处理可逆性与迁移对称性的被试内人类处理设计；trial 间上下文累积是优化机制本身。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥处理条件；所有 trial 在同一数据集上按模型与轮次运行。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件顺序；trial 序列是固定优化流程而非可反平衡的条件顺序。 |
| C3 | 恒定 | 0.5 | p.19: 固定模型为 Mistral 7B Instruct V2、Mixtral 47B、Yi-chat 34B、Qwen 72B 等；p.19 固定系统提示结构与 Guidance 约束；p.10 Limitations 讨论场景限制。 | 报告了若干恒定控制（模型版本、prompt 结构、数据过滤、生成约束）及一定外部效度限制；但未系统列出全部恒定水平与影响。 |
| C4 | 匹配 | NA | — | 未使用匹配程序，也不需要将实验单位按混淆变量匹配分组。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组因素或协变量纳入统计模型；主要分析为平均值和 bootstrap 描述。 |
| C6 | 盲法 | NA | — | 无人类被试/主试条件的盲法实施；主要数据采集自动化。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡、拉丁方或 ABBA 类顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 无人类练习块或练习效应控制问题；trial 间重复是刻意优化处理，而不是需消除的练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳风险；计算运行不存在休息间隔或时间分散设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 同一模拟保留历史上下文是 re-planning 的处理机制，不是需要清洗的 nuisance carryover；不同模型条件独立运行。 |
| D4 | 不对称迁移 | NA | — | 无跨条件人类处理的迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为识别率与 benefit capture 等客观/LLM 判定指标，不涉及量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.9 Table 4: “Critic Prompt – company names reversed in final question”；“company description reversed in order”。 | 对成对候选公司顺序和描述顺序做了部分反转变体测试，但未随机化每个 pair 的呈现顺序，也未报告各位置出现次数或翻转率。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中间反应倾向或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在人类需求特征或事后猜测实验假设的问题。 |
| E5 | 实验者效应 | NA | — | 数据采集主要由自动化 LLM 调用完成；无人类主试/评分者按条件传递期望的实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6-p.7 Figure 2/Table 2 报告均值与 bootstrap SD；识别率可高至约 94 pp.（p.7）。 | 报告了主要指标的均值/SD 和不确定度，但未系统报告偏度、端点频率或 pilot 难度校准；存在高识别率接近上限而未讨论天花板风险。 |
| E7 | 共同方法偏差 | 0.5 | p.5 “separate instances of the same LLM”；p.7 Table 3 报告 human evaluation 与 automated score 的一致性。 | 生成与自动评判同源，使用人类评估作为部分程序性对照；但未报告正式共同方法偏差统计检验或同源比例。 |
| F1 | 统计结论效度 | 0.5 | p.6-p.7 报告识别率、百分点差异与 “bootstrap standard deviation (in subscript) with 10K resampling iterations”；p.7-8 报告部分人类评估。 | 报告了百分数效应、bootstrap 标准差和部分人评一致性，但缺少样本量功效依据、正式 95% CI、所有分析的多重性校正说明。 |
| F2 | 内部效度 | 0.5 | p.5 说明每 trial 使用 LobbyLens pair 并重复至 4.5K；p.9-p.10 Limitations 讨论 critic 模型局限和场景简化；p.9 报告 ablations。 | 非随机分配，论文通过 ablation、prompt 稳健性和人评部分评估内部效度；但未报告正式基线等价、分配隐藏、损耗流程。 |
| F3 | 构念效度 | 0.5 | p.7 Table 3: “75.3% agreement between human evaluators”；“strong alignment between human and automated benefit capture”。 | 提供了人类评分者一致性和人机一致性作为部分信效度证据，但核心 deception 指标缺少人类效标验证与 manipulation check。 |
| F4 | 外部效度 | 0.5 | p.3-p.4 说明来自美国国会法案与 SEC 10-K 的 936 bills、114 companies、4439 pairs；p.10 Limitations 明确限定为立法案例和简化模型。 | 样本来源、筛选与边界条件有报告，但未报告跨样本/跨情境复现，代表性论证有限。 |
| G1 | 分析单位 | 0.5 | p.5 “In each trial, we use a bill-company pair... We repeat this procedure for each of the 4.5K companies and report the average metrics.” | 说明了每个 trial 来自 (bill, company) 对并报告平均指标，但没有显式区分分配/分析层级，也未用多层模型处理 pair/company 的嵌套。 |
| G2 | 随机效应 | 0 | p.6-p.7 主要报告平均值、bootstrap SD 与模型间比较，未报告随机效应或混合模型。 | 未说明哪些因子为随机效应；若要将结论推广到法案/公司总体，本应将法案/公司纳入随机效应，但论文未报告。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: 936 bills、114 companies、4439 bill-company pairs；p.7: bootstrap with 10K iterations。 | 材料确有从较大法案/公司集合抽样，并用 bootstrap 反映部分抽样不确定性；但未同时建模 subject/item 随机效应，也未报告 F′/混合模型。 |
| G4 | 统计功效 | 0 | p.5 仅说明使用 4.5K samples；p.6-p.7 报告 bootstrap SD 与百分点差异，无事前功效分析。 | 未报告设计阶段功效分析、目标功效、预期效应量来源或正式 95% CI。 |
| G5 | 研究者自由度 | 0.5 | p.3-p.4 报告 bill 长度≤600 tokens、相似度阈值、至少 4 家相关公司等筛选规则；p.6 报告 identification 与 benefit capture 两个主要指标；p.7 人评抽样 100 个模拟。 | 报告了主要数据过滤规则和主要因变量，但未完整说明所有排除/试次处理规则、样本量停止规则及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–25 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册或注册编号；按此前口径，无预注册记 0 而非 NR。 |
| J1 | 位置偏差 | 0.5 | p.9 Table 4 对 critic prompt 做 “company names reversed” 和 “company description reversed in order” 的变体，并报告总体识别率变化。 | 识别并部分测试了候选顺序/描述顺序偏差，但未报告交换前后翻转率、位置×正确率曲线或每个 pair 的正式随机化。 |
| J2 | 冗长偏差 | NA | — | 评估对象是隐藏受益者识别与 benefit entailment，不是按生成长短进行质量评分或成对文风比较；无长度—质量偏差风险。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场操纵或谄媚测量；critic feedback 是 re-planning 的优化信号，不是 sycophancy 范式。 |
| J4 | 自我偏好 | 0.5 | p.5: “Unless otherwise stated, we use separate instances of the same LLM for the modules.”；p.15-p.16 使用 Qwen-72B、GPT-4-Turbo 或三模型 polling 作为更强/异源 critic。 | 论文明确同源裁判风险并部分使用异源/更强裁判，但主实验仍以同源模型为唯一 critic，未量化 self-preference 偏差率。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 提示为 zero-shot 任务指令，未使用 few-shot in-context examples，因此示例选择/排列偏差不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.20-p.24 附录 C 给出完整 prompt 模板；p.9 Table 4 报告 prompt 结构与措辞变体；p.17 报告 CoT 变体。 | 模板与敏感性变体较完整，但未报告 prompt 版本号/迭代日期、dev/test 划分及 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 法案摘要被限制在约 600 tokens 以内，实验上下文远低于长上下文/RAG 设置，未进行关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0 | p.19 描述模型与 Guidance 约束生成，但未报告 temperature、top-p、top-k、seed 或重复采样 N。 | LLM 生成具有采样不确定性，但论文仅报告单次/固定流程结果，缺少采样超参与方差控制报告。 |
| J9 | 重复与文本退化 | 0 | p.19 仅说明使用 Guidance 做 constrained generation 和 regex 停止；未报告 greedy/beam/sampling、repetition penalty 或退化率。 | 开放生成修正案，但未报告解码策略与重复/退化指标，无法排除解码差异与文本退化混淆。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言、单脚本数据，无跨语言/跨脚本 tokenization 比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4 数据来自公开美国国会法案（108th-118th）和 SEC 10-K；未与模型训练截止日期对照或做污染检测。 | 公开立法与公司文本很可能出现在预训练语料中，论文未报告污染率或 held-out 证明，存在把记忆/熟悉度误作策略能力的风险。 |
| J12 | 基准饱和 | 0.5 | p.7 报告初始识别率可达 83.7%，GPT-4-Turbo 可达 94.2%；p.6-p.7 使用 top-1/top-2 与 bootstrap SD，但未讨论饱和。 | 报告了分数量程与高水位，但未在接近上限时改用连续指标或更难 held-out 子集，也未明确讨论饱和。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循能力；虽然生成受格式约束，但没有按指令约束类型测量遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.19: “Guidance framework for constrained generations and forced initialization... with the tokens for AMENDMENT #1”；p.24: 强制 YES/NO。 | 报告了结构化/约束输出设置，但未报告格式合法率、重试策略，也未将格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 研究不是越狱稳健性评估，没有自然提示拒绝率、对抗攻击族或 ASR 指标。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1-p.2 将 deception 与 classical definition 联系并区分 lying/omission；p.9 Limitations: “Future work must also study whether agents can deceive humans”。 | 对 LLM 上的 deception 构念及与人类欺骗的关系有初步讨论，但未做系统的人类同名构念对照实验，也未完全避免拟人化外推。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p.6: “identification... increase of 45.0 pp. → 61.2 pp. → 83.7 pp.”；“deception capabilities increase with model size”。 | 报告了跨规模曲线并给出 bootstrap SD，但主要使用离散识别率硬指标，未展示连续概率/校准曲线或多训练 seed 以排除指标诱导假象。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | p.6 定义 S_eval 与 identification；p.7 人类评估 100 个 Qwen-72B 模拟；p.8-p.9 ablations。 | 优化对象与部分评估对象有区分，并使用人类评估作为外部检查；但未报告代理分数与独立 held-out 人类评估随优化轮次的双曲线，无法识别 overoptimization 拐点。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.7 报告 10K bootstrap iterations 的标准差；p.19 报告模型型号（如 Qwen 72B、GPT-4-Turbo），但无精确 snapshot/API 日期与配对检验。 | 有重复抽样不确定度和模型型号，但 snapshot 标识不精确，模型比较未做 paired bootstrap/McNemar 等正式配对检验。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.5-p.6 报告 trial 1/2/3 的逐轮识别率；p.19 “We keep the whole conversation in memory, hence building up the context length.” | 进行了多轮 re-planning 并逐轮报告成绩，且说明保留历史上下文；但未报告每轮是否截断、温度/seed 一致性及跨轮安全/谄媚轨迹。 |

## 编码小结
论文对 LLM 策略性措辞与隐藏自利意图的测试台、数据集、prompt 与主要结果报告较完整，尤其方法/附录 prompt 可复现性较好；但多数传统实验心理学的被试随机分配、顺序平衡、盲法、随机效应、功效与预注册组件不适用或未报告。统计推断以百分比、bootstrap 标准差和描述性比较为主，缺少正式混合模型、交互检验、精确快照与采样超参报告。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
