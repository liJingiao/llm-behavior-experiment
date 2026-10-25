# article_171 | DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life | 2025

研究类型概述：本文是 LLM 基准/数据集构建与行为评测研究，而不是人类被试实验。核心分析单位是模型×日常道德困境的响应，以及按行动选择汇总的价值偏好计数。主要设计包括：六种 LLM 在同一批 1,360 个二元困境上的观察性比较、将 301 个价值映射到五个理论框架、对照 OpenAI/Anthropic 原则做价值冲突分析，以及针对 GPT-4-turbo 的系统提示调制实验。
- **研究构念（Construct）**：日常道德困境中的价值优先级、价值冲突与行为选择｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让现成LLM在1,360个日常两难情境中选择采取或不采取行动，并把选择及理由映射到五套社会学、心理学和哲学价值框架。（改变生活主题、受影响当事人、冲突价值、模型、公开原则文档和system prompt。）｜CA 任务锚定：道德困境任务（Moral Dilemma Task, `trm_57ebe6583f52d`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.9–10: 'we designed a system prompt modulation experiment with GPT-4-turbo ... two different sets of prompts – one for each value group'; p.35 Table 14 lists the prompts. | 系统提示是被主动操纵的自变量，至少含支持价值/反对价值两个水平，并有具体提示文本；但未明确报告条件分配方式、顺序处理或操纵检验，因此为部分满足。 |
| A2 | 因变量 | 0.5 | p.6: 'choosing action A determines selected values ... alternative action determines neglected values ... computed the difference ... normalized ... dividing total number on same dimension'; p.3 reports validation F1/κ. | 因变量指标与计分方式清楚：二元行动选择、选中价值减未选价值并做维度归一化；但信效度证据主要是数据集与 Reddit 的相似性验证，不是因变量测量信度，且缺少连续指标预处理/防端点说明。 |
| A3 | 控制变量 | 0.5 | p.18: 'we use greedy decoding for all the model response generation'; p.18: 'our choice of temperature (0) is optimal for this task'. | 报告并固定了贪心解码与温度 0 等关键生成设置，但没有系统列出所有额外控制变量及控制手段。 |
| A4 | 混淆变量 | 0.5 | p.17–18 discusses Mixtral 'stronger guard' / 74.85% answering, Western bias and demographic bias; p.6 mentions normalized value distributions to allow fair comparison. | 识别了拒答、文化偏差、价值分布不均衡等潜在混淆，并作了部分归一化/讨论；但未系统说明控制方式，也未做残余混淆的敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有提出理论上的调节变量，也没有调节/交互检验设计，故不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或中介效应分析，故不适用。 |
| A7 | 操作性定义 | 1 | p.4 §2.2 and p.19–20 A.5 give generation prompts and multi-step procedures; p.6 gives the value-preference scoring formula; Fig.1 shows the schema. | 困境生成、行动选择、当事人/价值抽取和偏好计分均有可复现的操作程序与提示示例，关键构念操作化较完整。 |
| A8 | 水平数与类型 | 0.5 | p.6 lists six evaluated models; p.35 Table 14 gives supporting/opposing system prompt sets for principles. | 模型与提示条件的具体标签可识别，但没有以设计表形式报告每个因素的水平数、水平类型、间距/全距等；模型比较亦非正式多水平实验设计。 |
| A9 | 单一操作化的风险 | 0 | p.6 uses binary action choices to infer value preferences; no multiple operationalizations or limitation discussion of single-operation generalizability is provided. | 核心构念主要依赖单一二元行动选择操作化，全文未讨论单一操作对可推广性的限制，也未报告多种操作间的会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 这不是人类自陈式同源测量；输入为研究者构造的困境/提示，输出为 LLM 行动选择，经典共同方法偏差框架不直接适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配；六个模型是对固定模型集合的观察性比较，不是被试间随机分配设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量分配；提示调制按独立 API 调用实施，论文也未把条件顺序作为设计因素报告。 |
| B3 | 混合设计 | NA | — | 不存在需要逐因素标注组间/组内并分别设误差项的混合设计。 |
| B4 | 因子设计 | NA | — | 没有正式因子实验、完整设计矩阵或每格样本量；模型比较是描述性观察，不是因子设计。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验，故不适用。 |
| B6 | 交互作用 | NA | — | 未报告正式交互项统计检验或简单效应分析，故不适用。 |
| B7 | 区组设计 | NA | — | p.4 按 17 个主题分层抽样 80 个困境属于数据集采样平衡，不是实验区组设计，也没有区内随机分配处理。 |
| B8 | 拉丁方 | NA | — | 没有被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 没有准实验分组、选择偏差控制或因果识别设计；模型比较主要是描述性基准评测。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，也无须论证处理可逆性/迁移对称性。 |
| C1 | 随机化 | NA | — | 所有模型/条件均对同一批困境作答，没有把分析单位随机分配到互斥处理条件，随机化程序不适用。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件呈现顺序；提示条件按独立调用实施，论文未报告顺序平衡。 |
| C3 | 恒定 | 0.5 | p.18: 'we use greedy decoding' and temperature 0; p.6 gives model names/versions. | 报告了温度 0、贪心解码及部分模型版本等恒定设置，但没有系统讨论这些恒定条件对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型；归一化价值分布是描述性处理而非 ANCOVA 协变量控制。 |
| C6 | 盲法 | NA | — | 主研究为自动化 LLM 调用；Reddit 相似性由作者标注，但没有条件盲法或可比的评分者盲法设计。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 对每个困境独立单轮作答，没有练习块或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 任务为短文本单轮判断，无人类 session 时长或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立提示调用，未报告跨条件会话延续，故无清洗期/迁移设计。 |
| D4 | 不对称迁移 | NA | — | 不存在被试内交叉条件，迁移对称性不适用。 |
| D5 | 范围效应 | NA | — | 主要因变量是二元选择与价值计数，不是需要绝对锚定的主观量表评分，故范围效应不直接适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p.6 uses 'Action 1' / 'Action 2'; p.37 original prompt: 'If you choose the first action (to do), return Action 1 ... second action ... Action 2'; no counterbalance/randomization of option order is reported. | 二元选项固定为 Action 1=to do、Action 2=not to do，未报告交换选项位置或反平衡，存在选项位置偏差风险。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分题与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或事后访谈；LLM 不会被传统意义上欺瞒，故不适用。 |
| E5 | 实验者效应 | NA | — | 主数据由 API 自动采集，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | Fig.3–4 and Fig.6 report value percentage distributions; p.17 reports Mixtral answers 74.85% and discusses neutral Purity/refusal risk. | 论文报告了价值分布图与 Mixtral 作答率，能部分看出端点/拒答问题；但没有系统报告均值、标准差、偏度、端点频率或任务难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，共同方法偏差不按人类量表框架适用。 |
| F1 | 统计结论效度 | 0.5 | p.6–8 report percentage preferences/differences and weighted score differences; p.6 reports validation F1 and Cohen's κ; no confidence intervals or multiplicity correction are given. | 报告了描述性效应量（百分比差异、加权分差、F1/κ），但主比较缺少置信区间、样本量功效依据和多重性校正。 |
| F2 | 内部效度 | 0.5 | p.9–10 describes the system-prompt modulation and before/after comparisons under 16 principles; p.18 controls greedy decoding/temperature. | 报告了提示调制程序与基线-调制对比，但没有随机分配、分配隐藏、基线等价性检验或正式内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | p.6 reports human verification of generated dilemmas: F1=85.7%, Cohen's κ=52.6%; p.5–6 maps values to five frameworks. | 提供了数据集内容效度/与 Reddit 相似性的部分证据，但没有报告模型行动选择测量的信度、操纵检验或单一操作化局限。 |
| F4 | 外部效度 | 0.5 | p.3–4 describes 1,360 dilemmas from 17 topics and six models; p.17 discusses Western/cultural and demographic biases and future broader sampling. | 样本来源、主题构成和推广限制有讨论，但人类代表性/跨情境复现不足，主要仍是 LLM 基准内部的模型比较。 |
| G1 | 分析单位 | 0.5 | p.6 describes each dilemma as binary choice and aggregates selected/neglected values across models; no explicit analysis-level/nesting model is reported. | 说明了模型×困境的汇总分析方式，但没有显式处理同一困境被多个模型重复评估的嵌套/配对结构。 |
| G2 | 随机效应 | 0.5 | p.6–8 report aggregate value preferences; no mixed model or random-effect structure is specified for models/dilemmas. | 模型作为固定集合比较、困境作为重复材料，但未报告随机效应结构或可推广总体范围。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: 'We stratify and sample 80 dilemmas from each topic, resulting in a dataset of 1,360 moral dilemmas'; analyses aggregate over these dilemmas. | 困境/材料明显来自更大主题总体的分层样本，但分析没有把困境/项目作为随机效应纳入模型，结论到任意新困境的可推广性受限。 |
| G4 | 统计功效 | NA | — | 研究是描述性基准评测，没有预设效应量或推断性功效分析；样本量主要由主题平衡和预算决定，因此功效分析不适用。 |
| G5 | 研究者自由度 | 0.5 | p.4 excludes values appearing in <100 dilemmas, leaving 301 values, and samples 80 dilemmas per topic; p.7 omits models/dimensions for clarity; p.17 reports Mixtral answer rate. | 报告了部分排除规则、抽样数量与结果展示选择，但没有完整区分验证性与探索性分析，也未系统报告所有分析选择的研究者自由度。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration, registered report, or timestamped analysis plan is mentioned in the main text or appendix. | 全文没有预注册信息，也没有区分预注册验证性分析与事后探索性分析；按判定口径记 0。 |
| J1 | 位置偏差 | 0 | p.6 binary-choice format; p.37 prompt fixes 'first action (to do)' as Action 1 and 'second action (not to do)' as Action 2; no swap/flip-rate analysis is reported. | 未对二元选项位置做反平衡或交换顺序重判，也未报告位置×选择或偏好翻转率，存在明显选项位置偏差风险。 |
| J2 | 冗长偏差 | NA | — | 评估对象是二元行动选择与价值计数，不是开放式生成质量的长短比较，也没有 LLM 裁判按长度评分。 |
| J3 | 谄媚 | NA | — | 没有操纵用户先验立场或用户反馈；系统提示调制测量的是可引导性，不是谄媚/附和用户先验。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM 作为成对/评分裁判来评价模型输出；GPT-4-turbo 用于生成数据和原则到价值的分类，不是自我偏好裁判场景。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.36–38 A.12 and Table 15 report four few-shot examples used to prompt Llama base models; examples are provided, but no multi-seed resampling or order counterbalancing is reported. | 补充实验确实使用了 few-shot 示例并展示模板与大致标签平衡，但没有报告多示例集 seed 重复、排列反平衡或模板全文的可复现链接。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.37 gives the original binary-choice prompt; p.15–20 A.5 and p.35 Table 14 give generation, extraction, and system prompts; no semantic-equivalence sensitivity ablation or dev/test split is reported. | 提供了主要提示模板和系统提示，满足基本可复现性；但未报告提示版本化、敏感性消融、开发/测试划分或提示搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 困境文本很短，远低于长上下文窗口，无 RAG 或长文档位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.18: greedy decoding and temperature 0 are used; a bootstrap experiment samples 100 dilemmas and runs GPT-4-turbo five times, reporting mean 45.6/100 and SD 1.02%. | 报告了温度 0、贪心解码和一次小规模重复采样方差估计；但未报告 top-p/top-k、随机种子、每条件重复次数与置信区间，闭源 API 也缺少精确 snapshot 日期。 |
| J9 | 重复与文本退化 | NA | — | 主评测输出为短选项 Action 1/Action 2，不涉及开放生成退化；Mixtral 重复问题属于任务遵循问题，不是文本退化主指标。 |
| J10 | 分词效应 | NA | — | 研究对象为英语困境与英文提示，没有跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4 says dilemmas are synthetically generated with GPT-4; the paper does not report model training cutoffs or any contamination/overlap check for the generated test set. | 测试集为新构造，但没有提供训练截止日期对照、n-gram/DCQ 污染检测或 held-out 证明；不能排除生成/评测模型间重叠，故记 0。 |
| J12 | 基准饱和 | NA | — | 该研究不是准确率接近上限的饱和基准；报告的是价值偏好百分比与差异，不涉及基准 SOTA 饱和问题。 |
| J13 | 指令遵循 | NA | — | 论文不以指令遵循为因变量，也未按约束类型系统测量指令遵循；Mixtral 拒答仅作为任务完成限制讨论。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.37 requires output strictly as 'Action 1' or 'Action 2'; p.17 reports Mixtral answers 74.85% after a stronger instruction and discusses refusal/repeating prompt. | 报告了二值结构化输出要求及部分格式/作答失败率，但没有系统报告所有模型的格式合法率、重试策略及格式失败与内容错误的分离。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及越狱、有害请求攻击或安全对齐评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2 and p.6 frame the work as evaluating LLM value preferences using five human theories; p.3 validates generated dilemmas against Reddit data, but no systematic human same-paradigm comparison is reported. | 论文把 LLM 行为解释为价值偏好，并借助人类价值理论；但未系统论证 LLM 构念与人类同名构念的异同，也未做同范式人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的能力曲线，也没有涌现能力宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对代理指标的优化、训练或 best-of-N 优化，故无奖励过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6 lists model names including GPT-4-turbo (0125); p.18 reports greedy decoding and a five-run bootstrap on 100 dilemmas; main scores lack per-condition CIs and paired tests. | 报告了部分模型版本、重复次数与一次方差估计，但缺少每个分数的 95% CI、配对检验、精确 API snapshot 和原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮困境判断，没有多轮对话历史累积或一致性衰减设计。 |

## 编码小结
论文对日常道德困境数据集、模型行动选择与价值偏好进行了较系统的描述性评测，并提供了生成与评测提示、价值映射和部分人类验证。但许多实验设计要求并未按人类被试实验标准报告；适配 LLM 的偏差控制也较弱，尤其是二元选项位置未反平衡、主结果缺少置信区间与项目随机效应建模、未做污染检查且无预注册。大量人类被试设计组件不适用，适用组件中多项仅达到部分报告。
