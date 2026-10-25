# article_060 | Stochastic Chameleons: Irrelevant Context Hallucinations Reveal Class-Based (Mis)Generalization in LLMs | 2025

研究类型概述：这是一项以 LLM 为分析对象的受控行为分析与机制可解释性研究：在同一 query 上比较 Q-only 与 C+Q（前置无关上下文）两种条件，使用 ParaRel 的 39 类事实召回关系、多个模型家族，并结合 500 条人工标注、PMI 统计、logit attribution、activation patching 与 attention knockout。没有人类被试分配。
- **研究构念（Construct）**：基于类别的泛化与无关语境诱导的幻觉（class-based generalization and context-induced hallucination）｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：这是一项以 LLM 为分析对象的受控行为分析与机制可解释性研究：在同一 query 上比较 Q-only 与 C+Q（前置无关上下文）两种条件，使用 ParaRel 的 39 类事实召回关系、多个模型家族，并结合 500 条人工标注、PMI 统计、logit attribution、activation patching 与 attention knockout。没有人类被试分配。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: “We compare two conditions: 1) Q-only ... 2) C+Q, where each Q is prepended with context demonstrations ...” | 明确命名并构造了两个水平，且同一 query 在两条件下比较；但没有正式操纵检验或完整分配/随机化说明，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.4: “The model’s top-1 prediction is A_Q”; p.14: “we set the temperature to zero ... perform string matching” | 因变量指标（top-1 prediction、accuracy、ΔRate、PMI、候选组成）与计分方式明确；但未报告信效度证据或连续指标预处理/防天花板地板说明。 |
| A3 | 控制变量 | 0.5 | p.14: “We set the temperature to zero for all models”; p.4: “using their base versions”; “We randomly sample 100 examples per subdatasets” | 提到了温度、base 版本、抽样、词表限制等控制手段，但没有系统清单并逐一说明所有控制变量。 |
| A4 | 混淆变量 | 0.5 | p.1: “we sidestep the data leakage issue”; p.2: “reducing the likelihood of pure pattern matching”; p.10: limitations on controlled setting | 识别了数据泄漏/记忆复现与模式匹配等潜在混淆，并用错误答案分析和受控配对降低威胁；但未做敏感性分析或定量残余混淆评估。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量理论模型或交互调节检验；模型规模、提示模板等只是探索性比较，未作为正式调节变量。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量与直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.4: definitions of Ccand. and Qcand.; p.5: annotation criteria; p.6: PMI computation; p.7: activation patching procedure | 关键构念均有可观测、可复现的操作化：条件构造、候选定义、人工标注步骤、PMI 与机制干预流程均较明确。 |
| A8 | 水平数与类型 | 0.5 | p.4: “We compare two conditions: 1) Q-only ... 2) C+Q”; p.24: 39 relation types and templates | 报告了两个条件水平及标签，属于名义水平；但未系统说明水平类型、间距/全距等（分类变量部分不适用）。 |
| A9 | 单一操作化的风险 | 1 | p.5: 500 annotated context-based candidates; p.6: PMI statistical validation; p.7: logit attribution; p.8: activation patching and knockout | 关键现象通过行为比例、人工标注、PMI、logit attribution、activation patching 和 attention knockout 多操作化，并报告了相互汇聚的证据。 |
| A10 | 单一方法的风险 | NA | — | 不涉及自陈式多构念同源测量；IV 为上下文条件操纵，DV 为模型预测，传统共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组分配；同一 query 在 Q-only 与 C+Q 下比较，不构成被试间设计。 |
| B2 | 被试内设计 | NA | — | LLM 每次前向推理独立，条件顺序不产生学习/残留；论文未设置需要顺序平衡的被试内会话，故该人类被试内设计组件不适用。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素混合设计及对应误差项。 |
| B4 | 因子设计 | NA | — | 核心是 Q-only 与 C+Q 的条件比较，不是完全交叉因子设计；模型规模比较是探索性扩展，未报告设计矩阵和 ANOVA 交互表。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无正式交互项统计检验；机制上的竞争不是 ANOVA 交互。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方设计。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；LLM 条件为确定性构造而非非随机分组实验。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理可逆性/迁移对称性设计问题。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥处理条件；每个 query 同时构造 Q-only 与 C+Q，分配隐藏/ITT 等不适用。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序；LLM 前向独立，Q-only 与 C+Q 不是可交换的会话顺序。 |
| C3 | 恒定 | 0.5 | p.4: base model versions and templates; p.14: “temperature to zero” and vocabulary restriction; p.10: English/model-size limitations | 报告了温度、模型版本、词表等部分恒定条件，但未系统列出全部恒定变量及其水平，也仅部分讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计。 |
| C5 | 纳入为变量 | 0 | p.4: 39 subdatasets; p.5: aggregated proportions; p.9: model-size comparison; no covariate/block model reported | 关系类型、模型家族等已知异质性被分层描述或比较，但未作为区组/协变量纳入模型，也未做协变量调整分析。 |
| C6 | 盲法 | 0 | p.5: “We perform this annotation on a randomly sampled set of 500 ...”; p.15: annotation procedure | 存在人工标注/判断，但未报告标注者盲法、人数、培训或盲法成功检验；可盲却未报告。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 每条件独立前向推理，无练习块或上下文内学习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长/疲劳问题；LLM 推理不涉及休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每条件独立计算，无跨条件残留或清洗期需求。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或顺序平衡问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观 top-1 预测/准确率/PMI，不涉及主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选选项或序列刺激位置平衡；上下文置于 query 前是条件定义本身，不是可反平衡的位置偏差。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中间反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或掩饰情节问题。 |
| E5 | 实验者效应 | NA | — | 数据采集主要由自动化模型推理完成；无人类主试期望传递。 |
| E6 | 天花板 / 地板效应 | 0 | p.5: accuracy 47.2%→43.1% for Llama and 38.2%→35.3% for Mistral; no distribution/skew/endpoint analysis | 因变量 accuracy 有上下界，但论文未报告偏度、端点频率或 pilot 难度校准，无法排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.6: Table 10 reports mean PMI, t-statistic and p-value; p.5: proportions without CI | 报告了 p 值和部分描述统计，但没有效应量/置信区间、样本量确定依据或多重性校正说明。 |
| F2 | 内部效度 | 0.5 | p.1: controlled setting to reduce leakage; p.4: dataset construction and random sampling; p.10: limitations | 讨论了数据泄漏等内部效度威胁并说明受控构造，但无随机分配、分配隐藏、基线等价或损耗流程（LLM 研究中多数不适用）。 |
| F3 | 构念效度 | 0.5 | p.5: 500 annotated candidates with criteria; p.6: PMI validation; p.7: logit attribution; no inter-rater reliability | 有多操作化与行为操纵效果证据，但未报告标注者间信度、测量信度/效度指标或正式 manipulation check。 |
| F4 | 外部效度 | 0.5 | p.4: Llama-3, Mistral, Pythia across 39 subdatasets; p.9: larger-model and prompt-template checks; p.10: English/model-size limitations | 报告了模型/数据集来源并做跨模型与跨模板复现，但模型选择代表性、完整推广边界和自然文本情境仍有限。 |
| G1 | 分析单位 | 0.5 | p.4: 27.6K queries, 3,900 context variations per query, 106M examples; p.5: datapoint-level proportions; p.6: one-sample t-test | 分析在 datapoint/context-query 层级进行，但 query 嵌套于关系类型、context variations 嵌套于 query 的结构未用多层模型显式处理，存在聚合/独立性风险。 |
| G2 | 随机效应 | NA | — | 论文未使用混合模型，也不涉及人类被试随机效应；模型家族主要作为固定比较对象，未主张从模型总体抽样。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: “We randomly sample 100 examples per subdatasets”; p.14: larger-model sampling; analyses aggregate over items | 材料/项目确有随机抽样，但分析未将 item 作为随机效应，也未用准 F 比或混合模型合并被试与项目方差。 |
| G4 | 统计功效 | 0 | p.4: sample sizes chosen by data/compute constraints; p.6: p-values reported without power analysis | 没有事前功效分析或样本量论证；结果也未系统报告效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.4: P264 all 53 examples; random sampling details; p.14: temperature/vocabulary; p.9: prompt sensitivity | 报告了部分抽样与条件选择规则，但未完整报告剔除标准、全部测量因变量以及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.10: limitations section; no preregistration link or analysis plan | 全文未报告公开预注册或数据收集前的分析计划。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较；top-3 候选用于事后分类而非位置偏好判断。 |
| J2 | 冗长偏差 | NA | — | 不评估开放式生成长度/质量，不涉及长度偏差。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | C+Q 中的 context demonstration 是被操纵的无关上下文，不是 few-shot in-context learning 示例；无 few-shot 示例选择/标签比例问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.9: alternative ParaRel templates used for prompt sensitivity; p.24: Table 15 templates; p.25: Table 16 alternative templates | 提供了模板并做措辞敏感性比较，但未报告 prompt 版本号、完整 system/分隔符细节、dev/test 划分或完整 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短，仅一条前置 demonstration，不是长上下文或 RAG 场景。 |
| J8 | 温度与采样随机性 | 0.5 | p.14: “temperature to zero for all models”; p.18: random-layer interventions averaged over three runs | 报告了温度并做部分三次运行，但未报告 top-p/top-k、seed、精确 snapshot 或主实验重复采样 CI。 |
| J9 | 重复与文本退化 | NA | — | 任务为 top-1 短答案预测且限制词表，不涉及开放生成重复/退化问题。 |
| J10 | 分词效应 | NA | — | 仅英文数据（[[PDF_PAGE_10]] limitation），无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.1: discusses data leakage and sidesteps by analyzing incorrect answers; p.2: “sidestep the data leakage issue”; p.4: ParaRel | 识别了基准污染/数据泄漏风险并采用错误答案分析降低影响，但未做 n-gram/DCQ 等污染检测或报告污染率。 |
| J12 | 基准饱和 | NA | p.5: accuracy around 30–47%; p.9: size/prompt comparisons | 不是基准饱和评估；分数远未接近天花板，也未宣称基准 SOTA 提升。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化输出或解析格式。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: “class-based (mis)generalization” and stochastic parrot framing; p.4: base models; p.9: discussion | 明确界定了 LLM 上的 class-based generalization 构念并讨论与 stochastic parrot 的关系，但未与人类同名构念做系统对照或人类实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 仅比较少量模型大小（7/8B、12B、70B），没有训练进展/规模曲线，也未宣称涌现突变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标（benchmark/reward/LLM-judge）的优化或 overoptimization 监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.14: temperature zero; p.4: model families; p.18: three runs for random interventions | 主结果基本为单点分数，无重复次数与置信区间、无精确 snapshot/API 日期、无配对检验；可复现性报告不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为严格单轮输入，不涉及多轮对话一致性或上下文累积。 |

## 编码小结
论文清晰报告了条件构造、候选定义、标注流程和机制干预方法，并用行为、统计与机制证据汇聚支持 class-based (mis)generalization。主要报告缺口在于：缺少正式操纵检验、评分者间信度/盲法、效应量与置信区间、精确模型 snapshot 与重复采样方差；对人类设计层组件多数不适用。
