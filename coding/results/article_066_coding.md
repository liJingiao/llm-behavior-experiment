# article_066 | Benchmarking Chinese Commonsense Reasoning of LLMs: From Chinese-Specifics to Reasoning-Memorization Correlations | 2024

研究类型概述：该文是 LLM 基准评测与观察性比较研究，而非人类被试实验。分析单位为 19 个 LLM × 5 种 prompt 策略 × 7 个推理任务（另含 4 个记忆任务）；主要指标为 accuracy，并辅以人工错误类型分析、记忆-推理相关分析及预训练 checkpoint 曲线。
- **研究构念（Construct）**：中文与跨文化常识推理及推理—记忆关联（commonsense reasoning versus memorization in Chinese and global contexts）｜CA 构念锚定：语义记忆（semantic memory, `trm_4a3fd79d0b083`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）；刻板印象（stereotypes, `trm_4a3fd79d0b285`）
- **实验任务与范式（Task / Paradigm）**：该文是 LLM 基准评测与观察性比较研究，而非人类被试实验。分析单位为 19 个 LLM × 5 种 prompt 策略 × 7 个推理任务（另含 4 个记忆任务）；主要指标为 accuracy，并辅以人工错误类型分析、记忆-推理相关分析及预训练 checkpoint 曲线。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_6: ‘We selected 5 commonly used prompt strategies’ and ‘For all prompt strategies, we use the 3-shot setting’; Figure 8 gives prompt examples. | 明确命名并报告了 5 种 prompt 策略及其含义/示例，但未报告操纵检验，也未系统说明模型与策略的分配/顺序逻辑；作为 LLM 基准的受控 prompt 因素只部分满足。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_4: ‘used accuracy as the metric’; PDF_PAGE_5: memorization MMR用rule-based matching，其余3个任务用GPT-3.5 judgement. | 因变量指标与计分方式明确（accuracy、正则抽取、规则匹配/GPT-3.5判断），但未报告信度、效度、连续指标预处理或天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_6: maximum output length 512; open-source models temperature 1.0, do_sample=False, bf16; closed-source GPT-3.5/GPT-4 temperature 0.7. | 报告了若干保持恒定的评测设置，但不是系统控制变量清单，未逐一说明控制手段及对外部效度的影响。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_5: translated questions were ‘manually screen[ed]’ for translation errors; PDF_PAGE_10 Limitations note many LLMs/prompt strategies untested. | 识别了翻译错误等潜在问题并做了人工筛查，也承认模型/prompt覆盖有限；但未系统讨论模型训练数据、语言导向、题目来源等残余混淆，也未做敏感性分析。 |
| A5 | 调节变量 | 0 | PDF_PAGE_7: ‘prompt strategies’ effectiveness depends on the LLMs’ orientation and the benchmark task’s domain’; Table 6 reports subgroup averages only. | 论文实际提出/暗示了模型导向与任务领域对 prompt 效果的调节性结论，但只报告描述性分组均值，未做乘积项交互检验、中心化或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量或中介效应分析；记忆-推理相关分析不是中介模型。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_3-5: task definitions, construction methods [T]/[S]/[H], examples, QA process; PDF_PAGE_5: scoring and judgement; PDF_PAGE_21 Figure 8 prompt examples. | 对推理任务、记忆任务、prompt 策略、计分与质量保证给出了较可复现的操作化描述和例子。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_6: five prompt strategies named (Direct, ZH-CoT, EN-CoT, Translate-EN, XLT); PDF_PAGE_5 Table 2: task types and option numbers. | 报告了 prompt 策略的水平数与标签，以及任务/选项类型；但未说明水平类型（名义/等级/连续）、间距、全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 0.5 | PDF_PAGE_5 Table 2: 7 reasoning tasks across multiple Chinese aspects and global domain; PDF_PAGE_10: limitations mention manual construction limits range of knowledge pieces. | 关键构念采用多个任务/多个常识方面测量，但未报告各任务/各操作之间的会聚证据；对单一操作局限的讨论主要停留在数据覆盖限制。 |
| A10 | 单一方法的风险 | 0 | PDF_PAGE_4-6: all measures are derived from LLM outputs and the same evaluation pipeline (accuracy/regex; memorization judged by GPT-3.5/rule-based); no common-method bias check. | 自变量条件与因变量均来自同一模型生成/评测流程，未报告共同方法偏差的程序控制或统计检验，也未讨论其对结论的威胁。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配；所有目标 LLM 均在同一基准上评测，不存在被试间条件分配。 |
| B2 | 被试内设计 | NA | — | 虽同一模型接受多种 prompt 条件，但研究不是人类被试内实验；未按 LLM 重复测量设计报告顺序平衡，且每个 prompt 调用独立。 |
| B3 | 混合设计 | NA | — | 不存在人类被试的组间/组内混合设计及相应误差项。 |
| B4 | 因子设计 | NA | — | 研究是基准评测网格（模型 × prompt × 任务），未作为推断性因子实验报告设计矩阵、每格样本量与 ANOVA 交互项。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验（F、df、p、效应量）。 |
| B6 | 交互作用 | NA | — | 没有报告交互项统计检验、简单主效应或带误差棒的交互图；仅有描述性分组比较。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；不存在非随机分组与因果推断的准实验框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有将分析单位随机分配到互斥条件的程序；所有模型在所有 prompt 条件下被完整评测。 |
| C2 | 平衡 | NA | — | 无条件顺序平衡问题；不同 prompt 是独立调用，不构成需要平衡的顺序设计。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_6: maximum output length 512; opencompass defaults; temperature 1.0/0.7; do_sample=False; bf16. | 报告了部分恒定设置（生成长度、解码默认值、数值精度），但未系统列出所有恒定变量及其水平，也未讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0 | PDF_PAGE_6 Table 4 reports model size and primary language; results do not include model size/language as covariates or blocking factors. | 模型规模、语言导向等已知混淆变量虽被描述，但未作为协变量或区组因素纳入分析，也未检验相关模型假设。 |
| C6 | 盲法 | NA | — | 研究使用自动化 API/开源模型评测，不存在对实验条件施盲的人类被试/主试；人工标注用于基准构建而非实验条件评分。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序，无需选择完全平衡/拉丁方/ABBA 层级。 |
| D1 | 练习效应 | NA | — | 每个 prompt/题目调用独立，无同一会话内的练习或学习阶段。 |
| D2 | 疲劳效应 | NA | — | 无人类被试 session，不存在疲劳效应。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件间为独立 LLM 调用，无跨条件迁移/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件残留，不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为 accuracy，不是主观量表绝对判断，无范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF_PAGE_19 Figure 6 and PDF_PAGE_18 Figure 5 show multiple-choice questions with fixed option order; no mention of option-order randomization/counterbalancing. | 多项选择题的选项位置固定，未报告选项/刺激顺序随机化或反平衡，存在位置偏差风险且未讨论。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表分数分布，不涉及极端/中间反应倾向。 |
| E4 | 需求特征 | NA | — | LLM 评测不存在人类被试需求特征或事后访谈推断假设的问题。 |
| E5 | 实验者效应 | NA | — | 数据收集主要是自动化 LLM 调用；不存在人类主试/评分者期望传递的实验者效应。 |
| E6 | 天花板 / 地板效应 | 0 | PDF_PAGE_7 Table 5 reports task accuracy means, with some tasks near ceiling (e.g. AJ 98.00) and some very low (e.g. RC 8.0); no SD/skew/endpoint frequencies or pilot difficulty calibration. | 报告了各任务 accuracy 均值，但未报告分布形态、端点频率或预实验难度校准；对明显的高/低端点成绩未讨论天花板/地板威胁。 |
| E7 | 共同方法偏差 | NA | — | 研究不使用同源自陈式多构念测量，无共同方法偏差的自评量表问题。 |
| F1 | 统计结论效度 | 0 | PDF_PAGE_7 Table 5 and Table 6 report only accuracy means; no confidence intervals, effect sizes, power analysis, or multiple-comparison correction. | 统计结论效度不足：未报告效应量/CI、样本量确定依据或多重性校正，主要结果以点估计呈现。 |
| F2 | 内部效度 | NA | — | 非实验性基准评测，无随机分配、分配隐藏、被试流向或损耗；论文没有做因果内部效度推断。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_5-6 and PDF_PAGE_12-13 Appendix D describe two independent annotator reviews, failure rates (reasoning 0.19; memorization 0.04), and correction ratios; no formal reliability coefficient or validity evidence. | 有较详细的质量保证和双人独立审核，构成部分信效度证据；但未报告评分者一致性统计、构念效度证据或操纵检验。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_6 Table 4 lists 19 LLMs with size/language; PDF_PAGE_10 Limitations discusses untested LLMs/prompt strategies and dynamic best-prompt issue. | 报告了模型样本来源/特征并讨论了部分推广边界，但未报告跨样本/跨情境复现结果，代表性仍限于选定模型集。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_7 Table 5/6 aggregate accuracy at model-prompt-task level; no mixed/multilevel model or item-level nesting treatment. | 说明了分析在模型-prompt-任务层级进行，但未显式处理题目嵌套于任务、模型嵌套于语言导向等聚集结构，也未将题目作为随机抽样单位建模。 |
| G2 | 随机效应 | NA | — | 研究比较的是固定选定的一组模型，而非从模型总体随机抽样；未使用混合模型，且无需把模型作为随机效应推广到模型总体。 |
| G3 | 材料作为随机效应 | 0 | PDF_PAGE_5 Table 2: finite question sets per task (reasoning 1800; memorization 759); results are aggregated accuracy with no item random effect or mixed model. | 题目被视为固定材料，仅报告聚合 accuracy，未将项目/题目作为随机效应，存在把有限材料当穷尽刺激并过度推广到任意常识题目的风险。 |
| G4 | 统计功效 | 0 | No power analysis or sample-size justification; results report accuracy without confidence intervals (e.g. PDF_PAGE_7 Table 5). | 未报告事前功效分析、样本量/题目量依据，也未在结果中报告效应量及置信区间。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_7-9 report all 7 reasoning tasks and 5 prompt strategies; PDF_PAGE_9 selects only 3 representative LLMs for error-type analysis; no explicit exclusion/optional-stopping rules. | 主要因变量与条件报告较完整，但错误类型分析只选 3 个模型，未明确说明样本量决定方式、排除规则，也未系统区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registry number, or time-stamped analysis plan is reported. | 全文未见预注册；不属于明确声明的纯探索性研究，但也没有预注册或分析计划偏离说明。 |
| J1 | 位置偏差 | 0 | PDF_PAGE_19 Figure 6 shows fixed answer-option positions; no report of A/B exchange, correct-answer position randomization, or position × accuracy analysis. | 使用多项选择但未做选项位置反平衡/正确答案位置随机化，也未报告位置偏差检查；存在系统性位置偏差风险。 |
| J2 | 冗长偏差 | 0 | PDF_PAGE_5: ‘for the other three tasks, we used GPT-3.5 for judgement’; no length-control instruction, length-score correlation, or length distribution reported. | 记忆任务使用 LLM 裁判评估自由文本答案，但未识别或控制冗长偏差，也未报告答案长度与得分关系。 |
| J3 | 谄媚 | NA | — | 任务为闭卷常识问答，无用户先验立场/反馈/纠错式对话，不涉及谄媚操纵。 |
| J4 | 自我偏好 | 0 | PDF_PAGE_5: GPT-3.5 used as judge for memorization tasks; no report of judge vs evaluated model family overlap, anonymization, or self-preference analysis. | 使用 GPT-3.5 作为 LLM 裁判，但未说明裁判与被评模型是否同源，也未做匿名化、异源陪审团或自我偏好偏差量化。 |
| J5 | 少样本示例选择与排列偏差 | 0 | PDF_PAGE_6: ‘For all prompt strategies, we use the 3-shot setting’ only; no example source, class/label ratio, order counterbalancing, or multi-seed resampling reported. | 仅报告了 3-shot 数量，未报告示例来源、每类比例、排列顺序控制或多示例集重复，few-shot 选择偏差控制不足。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_6 and PDF_PAGE_21 Figure 8 provide prompt strategy templates/examples; no prompt versioning, semantic-equivalence sensitivity ablation, or dev/test separation. | 提供了 prompt 策略定义与示例模板，但未给出完整版本管理、敏感性消融或测试集调参说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不是长上下文/RAG 实验，问题通常远短于上下文窗口，无中间迷失/信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_6: open-source temperature=1.0, do_sample=False; closed-source temperature=0.7; no seed, repeated sampling N, or confidence intervals. | 报告了主要采样温度/解码方式，但未报告随机种子、每条件重复采样次数或 95% CI，未把 LLM 非确定性纳入统计设计。 |
| J9 | 重复与文本退化 | 0.5 | PDF_PAGE_6: max output length 512; do_sample=False; temperature settings; no repetition penalty, n-gram repetition rate, or degeneration QC reported. | 报告了解码策略与最大长度，但未报告重复率/退化率，也未说明条件间是否严格保持解码策略恒定（除默认设置外）。 |
| J10 | 分词效应 | 0 | PDF_PAGE_6: comparison includes EN-CoT and Translate-EN across Chinese questions; no tokenizer name/version or token-count control reported. | 涉及中文题目的英文推理/翻译条件，存在跨语言 tokenization 差异风险，但未报告分词器版本、token/词数比或 token 数控制。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_3-5 introduce a new CHARM benchmark and use LogiQA/CLUE/translated BIG-bench items; no training cutoff vs benchmark release comparison or contamination detection is reported. | 虽为新构建基准，但未报告模型训练截止日期与测试集发布日期对照，也未做 n-gram/DCQ 污染检测；不能排除公开来源题目的记忆污染。 |
| J12 | 基准饱和 | 0.5 | PDF_PAGE_7 Table 5 reports model scores and random baselines (overall averages roughly 31.69–84.33); no saturation analysis or continuous metrics for near-ceiling tasks. | 报告了分数量程和当前水位，部分子任务接近天花板；但未系统评估饱和、未改用连续指标或更难 held-out 子集，也未做 bootstrap CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；任务是常识问答/多项选择，无否定/数量/格式等约束指令的遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0 | PDF_PAGE_4: ‘We used regular expressions to extract the preferred choice’; no format-validity rate, retry policy, or separation of format failure from content error reported. | 依赖正则抽取答案格式，但未报告格式合法率、重试策略或把格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/对齐或越狱评估，无有害请求与对抗攻击设置。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 该文为工程/能力基准评测，不主张用人类心理学构念解释 LLM，也未做人类同名构念对照。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | PDF_PAGE_22 Figure 10 reports checkpoint curves for Baichuan2/DeepSeek across training tokens using accuracy only; no continuous metrics or multi-seed intervals. | 报告了随训练进展的 accuracy 曲线，但仅用离散硬指标，未展示 log-likelihood/partial credit 等连续指标或多 seed 曲线；论文未明确宣称‘涌现’，但曲线解释存在指标诱导风险。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及以 benchmark/奖励模型/LLM-judge 为优化目标的训练或 best-of-N 优化，只是离线基准评测。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | PDF_PAGE_6 reports model snapshots (gpt-3.5-turbo-1106, gpt-4-1106-preview) and opencompass settings, but no repeated-run N, CI, paired tests, or seed/checkpoint sensitivity analysis. | 评估可复现性不足：仅有单次点分数和部分 snapshot 标识，无重复次数、置信区间、配对检验或原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮问答，无多轮对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
论文构建并公开了 CHARM 中文常识推理基准，系统报告了数据构造、质量保证、19 个模型与 5 种 prompt 策略的评测结果，以及记忆-推理关联和错误类型。作为基准论文，其任务定义、数据来源与评测流程较清楚，但在统计推断、位置/选项平衡、few-shot 示例控制、LLM 裁判同源偏差、污染检测、重复采样与置信区间、项目随机效应等方面报告不足；多数人类实验设计组件不适用。
