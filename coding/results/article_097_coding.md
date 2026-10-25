# article_097 | Rolling the DICE on Idiomaticity: How LLMs Fail to Grasp Context | 2025

研究类型概述：这是一项 LLM 基准构建与评测研究：作者构建了 DICE 对比数据集，用同一习语形式在字面义与比喻义语境中出现，评测 13 个 LLM 在零样本/单样本、三种 prompt 变体下的习语义消歧表现，并分析词频与句子似然对准确率的影响。分析单位主要是句子/表达层面与模型层面，不是人类被试实验。
- **研究构念（Construct）**：习语加工、语境消歧与组合/非组合意义选择｜CA 构念锚定：词汇通达（lexical access, `trm_4a3fd79d0b80f`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）；阅读（reading, `trm_4a3fd79d0aeb6`）
- **实验任务与范式（Task / Paradigm）**：这是一项 LLM 基准构建与评测研究：作者构建了 DICE 对比数据集，用同一习语形式在字面义与比喻义语境中出现，评测 13 个 LLM 在零样本/单样本、三种 prompt 变体下的习语义消歧表现，并分析词频与句子似然对准确率的影响。分析单位主要是句子/表达层面与模型层面，不是人类被试实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5 'We evalute 13 models...'; 'We used three prompt variations'; p.17 Table 5 specifies zero-shot and one-shot prompts. | 自变量包括模型、零/单样本设置和 prompt 变体，水平明确；但未报告操纵检验，分配与评估程序只部分说明，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.5 defines Accuracy_fig/lit equations (1)-(2) and Lenient/Strict Consistency (3)-(7); p.6 Table 2 reports mean ± SD. | 因变量指标与计分方式明确；但未报告模型评分信效度，也未说明连续/端点指标预处理或天花板地板控制，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.2 DICE 'holding surface form constant'; p.4 'same number of variants is matched'; p.15-p.16 hyper-parameters are listed. | 控制了表达形式、字面/比喻变体数、prompt 变体和解码参数，但未系统列出控制变量清单及逐项控制手段，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.1-p.2 notes existing datasets allow surface-level cues as shortcuts; p.6 GPT-4 generated DICE and is not considered revealing; p.9 notes selected idiom sample and English only. | 识别了形式捷径、记忆化和 GPT-4 生成等潜在混淆并部分控制；但对残余生成偏差和选择偏差的内部效度威胁讨论有限，故为 0.5。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量或交互假设；词频和句子似然被作为预测变量分析，不是调节检验。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或中介效应分析。 |
| A7 | 操作性定义 | 1 | p.3-p.5 describe idiom selection, GPT-4 literal sentence generation, expert annotation, task prompts and metric equations; p.17 Table 5 gives full prompts. | 关键构念的操作化较完整：数据构造、标注、prompt、输出标签与计分公式均可复现。 |
| A8 | 水平数与类型 | 0.5 | p.5 lists 13 models and three prompt variations; p.6 Table 2 separates zero-shot and one-shot; p.17 Table 5 gives prompt labels. | 报告了水平数与各水平标签；但未说明水平类型、间距/全距或连续变量的中心化/标准化，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.5 uses three prompt variants and three evaluation levels; p.9 discusses selected idioms and English-only limitations. | 对同一构念采用了多种 prompt 和多种一致性指标，但未报告会聚效度；单一任务限制仅部分讨论，故为 0.5。 |
| A10 | 单一方法的风险 | NA | — | 该研究不是自陈式多构念测量；模型输出与人工标注金标准比较，不存在心理测量意义上的同源共同方法偏差。 |
| B1 | 被试间设计 | NA | — | 没有人类被试组间分配；所有模型在固定测试集上评测，不属于被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量或顺序平衡设计；LLM 各 prompt 调用独立，不构成受试者内顺序设计。 |
| B3 | 混合设计 | NA | — | 没有人类组间/组内混合实验设计。 |
| B4 | 因子设计 | 0 | p.6 Table 2 crosses 13 models with zero/one-shot and three prompt variants descriptively; no interaction test is reported. | 多因素水平虽有交叉展示，但未报告交互项、设计矩阵或每格样本量；核心因子分析要件未达成，故为 0。 |
| B5 | 主效应 | 0 | p.6 Table 2 reports model/prompt means and SDs; no F, df, p or effect size for main effects. | 未对模型、prompt 或 shot 的主效应作统计检验，故为 0。 |
| B6 | 交互作用 | 0 | p.6 Table 2 presents descriptive comparisons; no interaction test, simple effects or error-bar inferential analysis is reported. | 未检验交互作用或简单主效应，故为 0。 |
| B7 | 区组设计 | NA | — | 没有区组或分层设计，也未报告区组变量。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方或受试者内条件顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计；模型比较是固定基准评测，不是非随机分组实验。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理，不涉及处理可逆性或迁移对称性。 |
| C1 | 随机化 | NA | — | 基准评测没有将独立分析单位随机分配到条件的机制；所有模型在同一测试集上评测。 |
| C2 | 平衡 | NA | — | 没有需要对条件顺序进行平衡的人类或 LLM 被试内顺序设计。 |
| C3 | 恒定 | 0.5 | p.15-p.16 give exact GPT snapshots and Table 6 lists temperature/top_p/max_tokens; p.9 limitations discuss language and idiom selection, not decoding settings. | 报告了模型版本和主要解码常量，但未系统讨论这些恒定设置对外部效度的限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 没有匹配程序。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入主分析；词频/似然是单独的研究预测变量，不是 ANCOVA 协变量。 |
| C6 | 盲法 | NA | — | 全自动 LLM 评测，没有人类被试、主试或评分者盲法安排。 |
| C7 | 平衡的层级 | NA | — | 没有顺序平衡层级可报告。 |
| D1 | 练习效应 | NA | — | LLM prompt 独立调用，不存在跨试次练习效应或练习块设计。 |
| D2 | 疲劳效应 | NA | — | 无人类被试 session 疲劳风险；LLM API 评测不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各 prompt 独立调用、无跨条件上下文残留，不需要清洗期或迁移建模。 |
| D4 | 不对称迁移 | NA | — | 不存在跨条件不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量是分类准确率/一致性等客观指标，不是绝对判断或量表评分。 |
| E1 | 位置 / 顺序偏差 | 0 | p.17 Table 5 fixes the response mapping 'i' for figurative and 'l' for literal and fixes the same one-shot example order across prompts; no counterbalancing is reported. | 二元标签映射和示例顺序固定，未做位置/标签反平衡，也未讨论其潜在偏差；故为 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert 或态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 没有人类被试，不存在需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | 全自动 LLM 评测，没有人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 2 reports means and SDs, with clear endpoint patterns such as Flan-T5-Small literal 66.72 vs figurative 0.51 and Flan-T5-Large literal 3.45; no endpoint-frequency or pilot difficulty calibration is reported. | 报告了均值/SD 且可见端点堆积，但未系统报告偏度、端点频率或任务难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 不涉及自评量表或多构念同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.6 Table 2 reports mean ± SD but no confidence intervals or effect sizes; p.8 describes regression analyses without coefficients/CIs; no power analysis or multiplicity correction is reported. | 缺少效应量/置信区间、样本量确定依据和多重性校正，仅报告描述性均值/SD；故为 0。 |
| F2 | 内部效度 | 0.5 | p.2-p.4 describe DICE controlling surface form, matching literal/figurative variant counts and expert annotations; p.6 excludes GPT-4 from interpretation; p.9 notes selected idioms and English-only. | 对形式捷径和记忆化等内部效度威胁有控制，但没有随机分配/流向/损耗等实验报告；残余生成偏差未系统评估，故为 0.5。 |
| F3 | 构念效度 | 0.5 | p.4 reports expert annotation with Cohen's kappa 0.95; p.3-p.4 detail curation; p.5 gives metrics; no manipulation check or human validation is reported. | 有标注者信度和一定构念控制，但缺操纵检验或效标/人类对照效度证据，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.4 reports 402 expressions and 2,066 sentences; p.9 states 'we only consider English idioms' and that DICE contains a selected sample. | 报告了材料来源与推广边界，但没有跨样本或跨语言复现，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p.5 metrics aggregate over sentences and expressions; p.8 fits linear regression of accuracy on frequency/likelihood; no multilevel/nesting handling is described. | 分析在句子/表达和模型层面混合进行，未明确处理句子嵌套于表达、同一表达跨条件重复的聚集结构，故为 0.5。 |
| G2 | 随机效应 | NA | — | 没有人类被试随机效应；13 个模型被作为固定入选集合进行比较，没有混合模型或模型总体随机效应推断。 |
| G3 | 材料作为随机效应 | 0 | p.8 regression uses frequency/likelihood and accuracy without item random effects; p.9 acknowledges selected idiom sample but does not model materials as random. | 402 个表达被视为固定材料，未使用 (1&#124;item)、F′ 或混合模型；结论推广到材料总体时缺少项目随机效应，故为 0。 |
| G4 | 统计功效 | 0 | p.5-p.6 no a priori power analysis or sample-size rationale is reported; p.6 Table 2 gives mean ± SD but no effect sizes/CI. | 无事前功效分析或样本量论证，也未给出常规效应量与置信区间，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p.4 reports additional annotation/exclusion categories; p.7 limits frequency analysis to <200,000 counts; p.5 reports 13 models and three prompts but no stopping rule or confirmatory/exploratory labeling. | 报告了部分排除标准和全部主要条件，但样本量决定、停止规则和探索性/验证性区分不完整，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1-p.9 and appendices contain no pre-registration platform, ID, or pre-specified analysis plan. | 未报告预注册或事前分析计划；0。 |
| J1 | 位置偏差 | 0 | p.17 Table 5 fixes 'i' for figurative and 'l' for literal across prompts; p.6 reports a 'Preference towards figurative' but no label/position counterbalancing or flip-rate analysis. | 二元选项标签位置未交换或随机化，也未报告位置偏差分析；故为 0。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放生成质量，不存在长度与得分关系问题。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错式对话，无法产生谄媚偏差。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM 裁判或成对比较评估模型输出。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.5 'an annotated example ... is prepended to each prompt'; p.17 Table 5 shows one fixed example containing figurative and literal demonstrations; no multi-seed or order counterbalancing is reported. | few-shot 示例数量、标签比例和模板有报告，但示例来源、排列反平衡和多示例集重采样不足，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5 uses 'three prompt variations ... semantically equivalent'; p.17 Table 5 gives full prompt templates, but no version/date, dev/test split, or prompt-search process is reported. | 提供了完整模板并做了三种措辞的敏感性比较；但缺版本化、dev/test 分离和系统消融记录，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 输入是单句语境，平均长度约 15.4/28.1 词，远低于长上下文/RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.15-p.16 give exact GPT snapshots and Table 6 lists temperature/top_p/max_tokens; p.6 reports mean ± SD over three prompts but no seed or repeated-sampling CI. | 报告了主要采样超参和部分模型 snapshot，但没有随机种子、每条件重复采样 N 与 bootstrap CI，故为 0.5。 |
| J9 | 重复与文本退化 | NA | — | 任务输出是短标签 i/l，不涉及开放生成文本退化。 |
| J10 | 分词效应 | NA | — | 单语言英语、单脚本，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3-p.4 DICE draws figurative items from MAGPIE/SLIDE/NCTTI/AStitch and literal items from GPT-4; p.15 gives model versions, but no training-cutoff comparison or contamination detection is reported. | 测试材料部分来自既有数据和生成数据，未做 n-gram/DCQ 等污染检测，也未与训练截止日期对照；故为 0。 |
| J12 | 基准饱和 | NA | — | DICE 是新构建的困难基准，strict consistency 多低于 65%，未接近天花板；不适用饱和风险。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；i/l 是任务输出，不是指令约束遵循评估。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.17 Table 5 requires output 'i' or 'l'; p.5 evaluation treats these as labels; no format-validity rate, retry policy or separation of format failure from content error is reported. | 存在结构化输出要求，但未报告格式合法率与格式/内容错误分离，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 motivates by 'Human processing of idioms'; p.7 'we investigate whether similar effects hold for language models'; p.9 concludes LLMs fail contextual understanding, but no human comparison is run. | 论文将 LLM 表现与人类习语加工构念相联系，但未系统论证同名构念异同或提供人类对照，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有报告跨规模/训练进展的连续能力曲线，也未宣称涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以代理指标为优化目标进行训练、RL 或 best-of-N 优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.15 gives exact GPT snapshots; p.5 uses three prompt variants; p.6 reports mean ± SD; GitHub link is provided, but no bootstrap CI or paired model tests are reported. | 有重复 prompt 条件和部分 snapshot，但缺置信区间、配对检验和逐题日志说明，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮，无多轮对话历史累积。 |

## 编码小结
DICE 的数据构造与对比设计较扎实，明确控制了表达形式并报告专家标注一致性；同时比较多种模型、prompt 变体与零/单样本设置，并分析词频和似然。但推断统计、随机效应、污染检验、位置/标签反平衡、预注册与功效分析等报告不足；多数人类被试实验设计组件不适用。
