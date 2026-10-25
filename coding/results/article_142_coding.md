# article_142 | StackEval: Benchmarking LLMs in Coding Assistance | 2024

研究类型概述：基准构建与基准评测研究：构建StackEval/StackUnseen代码问答基准，并用LLM-as-a-Judge评估答案可接受性；另以136个问题做裁判准确率与自我偏好分析。分析单位主要是问题-答案对、裁判模型运行与模型聚合分数，不是人类被试实验。
- **研究构念（Construct）**：评价判断中的自我偏好偏差及参考答案的锚定作用｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：六个LLM judge对同一组编码答案评分，每个模型同时评价自身和他人生成结果，并分别在无参考与提供Stack Overflow参考答案加CoT两种条件下运行Wilcoxon配对检验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5–6: 'We compared several evaluation methodologies... Question and Answer Only... Question, Answer, and Reference... Chain-of-Thought...'; p.6 Table 2 reports four prompt configurations. | 提示配置（4水平）被命名并描述了如何构造，但未报告单位分配细节与操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.5–6: 'acceptance score metric... accuracy, completeness, relevance'; 'accuracy against human labelers’ acceptance scores (binarized)'; 'acceptance rate... scores of 2 or 3'. | 因变量指标与计分方式明确；但未报告信度/效度证据及连续指标预处理/端点效应说明。 |
| A3 | 控制变量 | 0.5 | p.6: 'T = 0.01) and fixed seed (s = 42)'; p.7: 'outputs limited to 2048 tokens'; p.6: 'mean evaluation accuracy across 10 runs'. | 报告了温度、种子、输出长度和重复运行等控制，但未系统列出全部控制变量及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p.6: 'judges... exhibit biases from their training'; p.8–9: self-preference and reference-answer anchor; p.9: 'biases towards certain response styles... harder to detect'. | 识别了训练偏差、自我偏好、参考答案锚定与残余风格偏差，但未系统报告控制方式或敏感性分析。 |
| A5 | 调节变量 | 0 | p.8: 'in the presence and absence of reference answers'; p.8 Table 4: Baseline vs CoT + Ref. Answer self-preference p-values. | 将参考答条件作为潜在调节情境并分别报告，但未做正式交互检验、中心化说明或简单斜率分析；因提出条件/调节性比较却未报告乘积项交互统计检验，按级联规则基本要件未达成记 0。 |
| A6 | 中介变量 | NA | — | 全文无中介变量或中介效应分解；研究模型不包含中介假设。 |
| A7 | 操作性定义 | 0.5 | p.5 Table 1 rubric; p.16 Figure 8 full judge prompt; p.7 direct question presentation; p.4 dataset sampling/annotation. | 关键构念有操作化描述，但部分基线/CoT/Ref提示与自偏好聚合细节不完整，复现信息不全面。 |
| A8 | 水平数与类型 | 0.5 | p.5–6 lists four prompt configurations; p.8 Table 4 compares Baseline vs CoT + Ref. Answer; Table 2 has six judge models. | 报告了水平数与标签；未明确标注水平类型、间距等，且模型比较更接近观察分组而非完整实验因子。 |
| A9 | 单一操作化的风险 | 0.5 | p.9: 'evaluation criteria primarily assess correctness and relevance... may not fully capture... efficiency, maintainability'; p.9 static snapshot/one-shot. | 关键构念基本用单一rubric操作化，但在局限中讨论了推广边界；未提供多操作化会聚证据。 |
| A10 | 单一方法的风险 | 0.5 | p.4–6: human expert annotations and LLM judges; p.8 self-preference same-model judgments; p.9 judge-bias limitations. | 同时使用人类金标准与LLM裁判，但自我偏好分析存在同源评分风险，未报告共同方法偏差统计检验。 |
| B1 | 被试间设计 | NA | — | 无人类被试间分配；模型/问题比较不是独立被试组设计。 |
| B2 | 被试内设计 | NA | — | 虽同一裁判模型跨多个提示配置被比较，但这是自动化独立调用的条件比较，不是人类被试内重复测量设计，无需被试顺序平衡。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合实验设计，也无被试层混合模型。 |
| B4 | 因子设计 | NA | — | 没有报告经典因子设计及ANOVA交互分析；表2/表3是基准比较表而非完整设计矩阵与推断统计。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 没有正式交互项检验和简单主效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无被试内设计，无拉丁方顺序安排。 |
| B9 | 准实验设计 | NA | — | 不是非随机分配的准实验；论文未作准实验因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内设计，不涉及处理可逆性与迁移对称性。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥条件的程序；提示配置是同一模型上全部运行。 |
| C2 | 平衡 | NA | — | 无人类被试内条件顺序，因此无顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.6: 'T = 0.01) and fixed seed (s = 42)'; p.7: 'outputs limited to 2048 tokens'; p.9: static snapshot/one-shot limitations. | 列出了温度、种子和输出长度等恒定控制，但对这些恒定水平的外部效度限制讨论不系统。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组/协变量纳入统计模型的分析结构。 |
| C6 | 盲法 | 0 | p.4: 'human domain experts, who compare it... A third domain expert then verified these annotations'; p.6 human-annotated ratings. | 存在人类评分者，但未报告盲法类型、施盲对象或实施方式；可盲而未报告。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM API调用为独立条件运行，没有人类被试练习效应或试次内学习。 |
| D2 | 疲劳效应 | NA | — | 无人类session疲劳问题；LLM评估为自动化运行。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各提示配置/模型调用可视为独立重置，无跨条件药物或学习残留清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性检验需求。 |
| D5 | 范围效应 | NA | — | 无人类被试内绝对量表判断；LLM rubric评分不涉及人类范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 评估为单答案逐项打分，不是多候选项选择/排序，无选项位置随机化问题。 |
| E2 | 默认赞同 | NA | — | 不使用Likert或态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试参与实验，不存在掩饰情节或需求特征检查。 |
| E5 | 实验者效应 | 0 | p.4: human domain experts annotate; p.6: human-annotated ratings; no blinding/training details reported. | 有人类评分者参与，但未报告评分者盲法层级、培训标准化或脚本化程度。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 2: mean accuracy ± 95% CI; p.7 Table 3: acceptance rates, including O1 Preview 95.5% on StackEval. | 报告了均值/置信区间和接受率，但未报告偏度、端点频率或pilot难度校准；高接受率未讨论天花板。 |
| E7 | 共同方法偏差 | NA | — | 没有同源自陈式多构念量表，不适用共同方法偏差量表分析。 |
| F1 | 统计结论效度 | 0.5 | p.6 Table 2 reports mean accuracy ± 95% CI across 10 runs; p.8 Table 4 reports Wilcoxon p-values. | 报告了置信区间和部分检验，但无样本量确定依据、正式效应量体系与多重比较校正说明。 |
| F2 | 内部效度 | NA | — | 不是随机对照实验，也无因果处理分配；论文主要做基准评估而非内部效度因果推断。 |
| F3 | 构念效度 | 0.5 | p.4 human expert annotation and third expert verification; p.5 rubric；p.9 limitations. | 有专家标注与rubric，但未报告评分者间信度、效度证据或操纵检验。 |
| F4 | 外部效度 | 0.5 | p.2 Figure 1/p.4: 925 questions, 25 languages, sampled by Stack Overflow survey popularity; p.7 StackUnseen; p.9 Stack Overflow bias limitations. | 报告了样本来源、抽样与推广边界；但未报告跨样本复现或更系统的代表性检验。 |
| G1 | 分析单位 | 0.5 | p.6: 'mean evaluation accuracy across 10 runs'; p.7 Table 3 reports model-level acceptance rates; p.14 Table 5 full results. | 说明了聚合层级，但未显式处理问题/运行嵌套结构，也无多层模型。 |
| G2 | 随机效应 | 0 | p.6 Table 2 and p.7 Table 3 use aggregate means; no mixed-model random effects are reported. | 模型与问题被作为固定比较对象，未报告随机截距/随机斜率；若要对问题总体推广则不足。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: 925 curated Stack Overflow questions; p.7 Figures 3/5/7 report subsets by question type/language; no item random effects. | 材料来自更大题库并做子集分析，但未把问题/项目作为随机效应纳入模型。 |
| G4 | 统计功效 | 0.5 | p.6 Table 2: mean ± 95% CI across 10 runs; p.8 Wilcoxon p-values. | 报告了重复运行的不确定性，但无事前功效分析或样本量推导。 |
| G5 | 研究者自由度 | 0.5 | p.3 dataset filtration criteria; p.4 136-question judge subset; p.14 Table 5 full model results. | 报告了部分纳入/排除与全部结果，但未完整说明所有运行剔除规则、停止规则及探索/验证分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered analysis plan is reported; only code/data release at https://github.com/ProsusAI/stack-eval. | 无预注册；公开数据/代码不等同于时间戳早于数据收集的预注册。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或成对LLM-as-judge位置比较；评分为单答案逐项打分。 |
| J2 | 冗长偏差 | 0 | p.3 mentions 'pairwise comparisons are susceptible to position and verbosity biases'; p.16 Figure 8 rubric/prompt contains no length-control instruction or length-score analysis. | 使用LLM裁判评估开放式代码/答案，但未控制或报告长度偏差，也未报告长度—得分相关。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或纠错对话，不适用谄媚分析。 |
| J4 | 自我偏好 | 0.5 | p.1: 'whether they favor their own generated solutions'; p.8 Table 4: self-preference Wilcoxon p-values; p.6 human annotations. | 明确研究同源裁判的自我偏好并有统计检验，但未报告匿名化、各裁判单独结果和favor-own比例效应量。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 提示配置未使用few-shot示例；属于zero-shot/直接提示评估。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.16 Figure 8 gives full CoT + Ref. Answer judge prompt; p.5–6 describes other prompt variants. | 提供了主要提示模板并比较了提示组件，但无版本/日期、语义等价措辞消融及dev/test划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长文档/RAG或关键信息位置操纵实验；问题长度有限制但未做长上下文位置效应研究。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'T = 0.01) and fixed seed (s = 42)'; 'mean evaluation accuracy across 10 runs'; p.7 same generation settings and 2048-token limit. | 报告了温度和种子并有10次重复；但未完整报告top-p/top-k、精确API snapshot等。 |
| J9 | 重复与文本退化 | 0.5 | p.7: 'T = 0.01) and fixed seed (s = 42)'; 'outputs limited to 2048 tokens'; no repetition/degeneration QC reported. | 报告了部分解码设置与长度上限，但未报告解码策略细节、repetition penalty或退化率。 |
| J10 | 分词效应 | NA | — | 未做自然语言/脚本跨语言比较；编程语言是任务类别，不是分词长度控制实验。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.1: 'risk of benchmark leakage'; p.3–4: StackUnseen uses recent Sep 2023–Mar 2024 and later data to prevent leakage; p.4 StackEval dates. | 识别污染风险并用近期数据构建StackUnseen，但未报告训练截止日期对照、污染检测率或held-out私有测试。 |
| J12 | 基准饱和 | 0.5 | p.7 Table 3: O1 Preview 95.5% on StackEval; StackUnseen used to evaluate recent harder content; no explicit ceiling analysis. | 报告了量程上的高水位并用更难子集，但未明确讨论饱和、连续指标或CI比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；没有约束型指令遵循评分。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.16 Figure 8 requires output as JSON object with specified keys; no format-validity rate or retry policy reported. | 裁判提示要求结构化JSON输出，但未报告格式合法率、重试/后处理规则；部分满足。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 纯工程/应用基准评估，不主张测量LLM的心理学/认知构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨规模/训练进展的能力曲线或涌现能力宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标的优化过程（无训练/RL/best-of-N优化监控）。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6: mean accuracy ± 95% CI across 10 runs; p.7 Table 3 reports acceptance rates; GitHub repository shared. | 报告了重复次数与部分CI，但精确模型snapshot/API日期和配对检验不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 评估为单轮问答/单轮裁判，无多轮对话历史累积，也不主张多轮部署结论。 |

## 编码小结
论文报告了较完整的数据集构建、提示配置比较、重复运行与自偏好检验，并提供了公开代码与数据；但它不是传统心理实验，许多人类被试分配、顺序平衡、量表与预注册组件不适用。适用组件中，提示配置操纵、伦理/质量控制与可复现性信息部分完整但常缺关键细节（如操纵检验、盲法、长度偏差控制、精确snapshot、功效分析、随机/混合效应建模），因此多为0.5。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 A5（0.5→0）。
