# article_173 | Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs | 2024

研究类型概述：这是一项 LLM 行为基准评测研究：构建 SAD，包含 7 个任务类别、16 个任务、13,198 个问题，评测 16 个 Llama-2、GPT-3/4 与 Claude 模型。研究设计主要是对模型家族/版本、base vs. chat、提示条件（plain、situating prompt、large situating prompt、部分 COT、few-shot）进行观察性比较；分析单位是模型-任务-问题/trial，模型按任务得分汇总。没有人类被试随机分配，也不是人类心理实验；人类仅作为 roleplay baseline 与 Long Monologue 的评分者。
- **研究构念（Construct）**：模型对自身身份、能力、处境和行为的情境意识｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让16种现成LLM完成13,198道关于自身事实、影响能力、发展阶段、自我识别、反模仿、身份条件行动和内省预测的问答或指令任务。（改变七类情境意识任务、模型、基础/聊天版本、是否加入situating prompt以及人类基线。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'we test all models with and without the situating prompt shown in Figure 3'; p.6: 'We evaluate all models without Chain of Thought (COT) and include just two COT evaluations'; p.19 Table 2 lists variants plain, SP, SP large. | 明确命名并报告了提示条件（plain/SP/large SP）及部分 COT、few-shot 水平；但没有随机分配，也没有操纵检验，因此未达 1。 |
| A2 | 因变量 | 0.5 | p.6: 'Each task is either multiple choice or free form. Responses are graded as correct or incorrect with no partial credit... percentage correct'; p.22: scoring rule for invalid answers; p.19 Table 2 gives trials and task types. | 因变量指标、计分方式、题目数量与单位清楚；但未系统报告内部一致性/重测信度，也未对天花板/地板做完整预处理说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.22: 'Most runs are at temperature 0.0, except for COT rollouts... 1.0'; p.20-21: answer assist and prompting styles standardized; p.68: text cut to fit 4096-token limit. | 报告了温度、答案辅助、提示格式、上下文长度等若干控制手段，但没有系统列出控制变量清单并逐一说明，故部分满足。 |
| A4 | 混淆变量 | 0.5 | p.10: 'we have small sample sizes for each intervention and a lack of controlled interventions'; p.10: leakage concern and model-specific correct answers; p.5: LLM-generated prompts may introduce evaluator self-preference bias. | 识别了干预样本小、缺乏受控干预、数据泄漏、LLM 生成提示偏差等潜在混淆，但没有系统控制或敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 论文没有提出调节变量理论模型，也没有做调节效应/简单斜率检验；按规则记 NA。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或中介效应分析；按规则记 NA。 |
| A7 | 操作性定义 | 1 | p.4-5 define situational awareness and task categories; p.6 scoring; p.19 Table 2 task summary; p.34, p.44, p.49-50, p.58-61, p.64-68, p.77-80, p.85-86, p.96-100 give prompt templates and operational procedures. | 各任务类别均给出可执行的操作化描述、提示模板、计分或判定标准，达到可复现程度。 |
| A8 | 水平数与类型 | 0.5 | p.6 and p.19: plain, situating prompt, SP large, COT; p.20 Table 3 lists model families/versions; p.64-65 STAGES answer lines randomized; p.75 multiple rephrasings. | 报告了关键条件的水平与标签，但没有系统给出水平类型、间距/全距或连续变量的中心化说明；故为 0.5。 |
| A9 | 单一操作化的风险 | 1 | p.4-6: 7 categories and 16 tasks operationalize different facets; p.8: pairwise correlations among task categories; p.10: limitations note SAD tasks are short and artificial; p.26 Table 6 reports aspect-level scores. | 关键构念采用多任务、多指标操作化，并报告类别间相关与任务分解；也讨论了短任务/人工任务的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 所有因变量为客观任务正确率/模型输出评分，不是同源自陈式多构念量表；共同方法偏差检验框架不适用于本研究的核心测量。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或被试组随机分配到条件；模型比较是观察性基准评测，不是被试间实验。 |
| B2 | 被试内设计 | 0.5 | p.6: all models tested with and without the situating prompt; p.28 Figure 7 compares plain vs SP within models; p.20-21: API prompting styles. | 同一模型接受 plain/SP 等条件，具有重复测量性质；但各条件为独立 API 调用，未报告条件顺序平衡或顺序分配，故为 0.5。 |
| B3 | 混合设计 | NA | — | 没有正式的组间×组内混合实验设计及相应混合模型/误差项分析；模型与提示条件的比较是描述性基准结果。 |
| B4 | 因子设计 | NA | — | 没有以 ANOVA 因子设计呈现完整设计矩阵、每格样本量与交互统计量；SAD 是基准评测而非因子实验。 |
| B5 | 主效应 | NA | — | 不存在因子设计意义上的主效应检验；论文报告的是各任务/模型得分与平均提升，不是 ANOVA 主效应。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验、简单主效应与多重比较校正；按规则记 NA。 |
| B7 | 区组设计 | NA | — | 没有区组/分层分配或区组变量设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡被试内条件顺序。 |
| B9 | 准实验设计 | 0.5 | p.10: 'we have small sample sizes for each intervention and a lack of controlled interventions'; p.8: chat models outperform base models by +4.5%; p.28 Figure 6 paired base/chat comparisons. | 论文比较 base/chat、模型规模等非随机干预，并在局限中承认缺乏受控干预；但没有明确准实验类型、选择偏差缓解或正式因果限定，故为 0.5。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理可逆性/迁移对称性问题；LLM 各条件为独立调用。 |
| C1 | 随机化 | NA | — | 研究没有把模型/试次随机分配到互斥条件的随机化程序；模型是预先选定的基准对象。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序；模型在各提示条件下独立调用，非顺序呈现设计。 |
| C3 | 恒定 | 0.5 | p.22: temperature 0.0 for most runs; p.20-21: standardized message formats and answer assist; p.68: texts cut to 4096-token context limit. | 报告了若干恒定控制（温度、提示格式、上下文长度），但没有系统列出所有恒定变量及其外部效度限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为协变量或区组纳入统计模型。 |
| C6 | 盲法 | 0.5 | p.105: 'The evaluators were semi-blinded... They were not shown which model they were evaluating and three ... were not told which subset of models was being tested.' | Long Monologue 人工评分采用半盲，报告了施盲对象与部分实施方式；但没有盲法成功检验，故为 0.5。 |
| C7 | 平衡的层级 | NA | — | 没有需要选择完全平衡/拉丁方/ABBA 层级的顺序设计。 |
| D1 | 练习效应 | NA | — | LLM 评测没有练习块或跨试次学习设计；各问题/调用独立。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长/疲劳控制问题；LLM 评测为程序化调用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立 API 调用，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或顺序平衡问题。 |
| D5 | 范围效应 | NA | — | 不使用主观量表或绝对量值估计，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.64-65: STAGES 'ANSWER LINES ... in a randomized order'; p.78: 'Answer A is correct for half of the samples, and B is correct for the other half'; p.85: 'we randomize the order of the two lines ... to cancel out any model bias'; p.89 Figure 43 and p.92 Figure 48 report order biases. | 关键任务对选项/指令顺序做了随机化或反平衡，并报告了部分顺序偏差；但未对所有任务给出各位置出现次数与完整平衡方案，故为 0.5。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分题或默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 评测不存在人类被试需求特征或事后访谈推断假设的问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递；Long Monologue 评分者盲法已在 C6 处理。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Table 1 reports model scores, random chance and upper baseline; p.8: 'SAD will not be saturated for at least the next generation'; p.35: FACTS-HUMAN-DEFAULTS nearly saturates with SP; p.48: INTROSPECT far from saturated. | 报告了均值、随机水平和上界，并讨论部分任务接近天花板/地板；但没有系统报告偏度、端点频率或 pilot 难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 核心测量不是同源自陈式多构念量表；共同方法偏差的统计检验不适用于该基准设计。 |
| F1 | 统计结论效度 | 0.5 | p.22: analytic standard error estimation for Bernoulli trials; p.26 Table 6 reports scores with ±; p.7 Table 1 reports scores; p.9 Figure 5 reports correlations without multiplicity correction. | 报告了样本量、标准误/误差范围和大量主要结果；但没有事前功效分析、效应量/95%CI 的统一报告及多重比较校正，故为 0.5。 |
| F2 | 内部效度 | 0.5 | p.10: discusses leakage, small intervention samples, lack of controlled interventions, changing model situation; p.8: base/chat comparisons without random assignment. | 对内部效度威胁有讨论，但无随机分配/分配隐藏、基线等价性或正式敏感性分析；故为 0.5。 |
| F3 | 构念效度 | 0.5 | p.23-24: human answer and human roleplay baselines; p.7 Table 1 upper baseline; p.8: task-category correlations; p.105-106: Long Monologue evaluator agreement and scores. | 提供人类基线、上界、类别相关与部分评分者一致性作为效度证据；但未系统报告各任务信度、操纵检验与多操作化会聚，故为 0.5。 |
| F4 | 外部效度 | 1 | p.7: 16 models from Llama-2, GPT-3/4, Claude families; p.20 Table 3 gives release dates, training cutoffs, finetuning and parameters; p.10: limitations discuss short artificial tasks and model-situation changes. | 样本来源与模型特征清楚，覆盖多家族/多规模/多版本，并明确讨论推广边界；达到 1。 |
| G1 | 分析单位 | 0.5 | p.6: scoring per task and equal-weighted average over seven categories; p.19 Table 2: trials per dataset; p.26 Table 6: aspect-level aggregation. | 说明了 trial/任务/类别/模型的分析层级与汇总方式；但问题嵌套于任务、模型重复测量等聚集结构未用多层模型处理，故为 0.5。 |
| G2 | 随机效应 | NA | — | 统计模型没有随机效应；模型是预先选定的基准对象，研究并不需要把模型当作从总体抽样的随机因子。 |
| G3 | 材料作为随机效应 | NA | — | 题目/材料不是作为随机刺激总体建模的自变量载体；SAD 使用固定基准题目集，未做项目随机效应推广。 |
| G4 | 统计功效 | 0 | p.22: error estimation formula; p.7 Table 1 reports scores but no power analysis; p.19 Table 2 gives trial counts. | 没有事前功效分析或样本量确定依据；仅报告误差估计与描述性比较，按规则记 0。 |
| G5 | 研究者自由度 | 0.5 | p.6 and p.22: invalid-answer scoring rule; p.19 Table 2 lists all tasks and trials; p.10: limitations acknowledge small intervention sample; p.104: Long Monologue sampling until 10 non-refusals and selecting longest 2. | 报告了计分/无效答案处理、任务清单和部分采样规则；但未完整报告所有分析选择、停止规则及验证性/探索性区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.3: contributions and benchmark release; p.18: canary GUID; no preregistration statement or registration link found. | 全文没有公开预注册或注册编号/链接，也没有区分预注册验证性分析与事后探索性分析；按规则记 0。 |
| J1 | 位置偏差 | 0.5 | p.64-65: STAGES answer lines randomized; p.78: correct A/B balanced; p.85: instruction order randomized; p.89 Figure 43 and p.92 Figure 48 report first-option biases; no exchange-based flip-rate analysis. | 对多选题选项/指令顺序做了随机化并报告部分位置偏差，但没有报告 A/B 交换前后的翻转率或完整位置×正确率曲线，故为 0.5。 |
| J2 | 冗长偏差 | NA | — | 主要评估是多项选择/短答案/可机器或规则判定任务；Long Monologue 虽为长文本但由人类评分，不涉及 LLM 裁判按长度偏好评分。 |
| J3 | 谄媚 | NA | — | 任务不是带用户先验立场/反馈/纠错的多轮对话式评估；没有谄媚操纵或测量。 |
| J4 | 自我偏好 | 0.5 | p.87: 'To score the model response, we prompt GPT-3.5-turbo with the following'; p.20 Table 3 includes gpt-3.5-turbo-0613 among evaluated models; p.5 cites Panickssery et al. on LLM evaluator self-preference for prompt generation. | ID-LEVERAGE 使用 LLM 裁判并报告了裁判模型与被评模型列表，存在同家族自我偏好风险；但未做匿名化、异源陪审团或自我偏好率分析，故为 0.5。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.50: INTROSPECT-COUNT-TOKENS 5-shot examples; p.55: INTROSPECT-PREDICT-WORDS 2-shot examples; p.96: ANTI-IMITATION few-shot examples; p.94-95: refusals and answer-format prompting. | 报告了部分 few-shot 示例来源/数量与模板，但没有多 seed 重采样、排列反平衡或系统报告示例集方差，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.6 Figure 3 gives the situating prompt; p.34, p.44, p.49-50, p.58-61, p.64-68, p.77-80, p.85-86, p.96-100 provide prompt templates; p.75 gives multiple STAGES rephrasings. | 提供了较完整 prompt 模板并比较 plain/SP/large SP、COT 等版本；但没有版本号/日期、dev/test 划分、系统语义等价敏感性消融与 prompt 搜索过程，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验使用短/中长文本并截断以适配 4096 token 上下文，但没有长上下文/RAG 场景下的关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.22: 'Most runs are at temperature 0.0, except for COT rollouts... 1.0'; p.22: standard error estimation; p.104: Long Monologue sampled at temperature=1 and 10 non-refusal responses. | 报告了 temperature 与部分重复采样/误差估计；但未完整报告 top-p/top-k、随机种子、各条件重复 N 与 95%CI，故为 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.22: temperature 0.0 and logprobs via API or resampling; p.95: 'many of the prompts were refused, or answered in an incorrect format'; p.101: poorly formatted answers; no n-gram repetition/degeneration rate. | 报告了解码策略与部分格式/拒答问题，但没有报告重复率/退化率等 QC 指标，且条件间解码控制不完整，故为 0.5。 |
| J10 | 分词效应 | NA | — | 研究主要是单语言英语评测；没有跨语言/跨脚本比较。INTROSPECT-COUNT-TOKENS 使用 tokenizer，但 J10 的跨语言分词控制风险不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.20 Table 3 lists training data cutoffs; p.19 Table 2 lists data sources; p.10: 'a distinct worry is that SAD may become less meaningful after publication because of leakage'; p.18 canary GUID. | 报告了模型训练截止日期、任务来源与泄漏担忧，并设置 canary；但没有系统污染检测（n-gram 重叠/DCQ）或污染率估计，故为 0.5。 |
| J12 | 基准饱和 | 1 | p.7 Table 1: random chance 27.4, best model 49.5, upper baseline 90.7; p.8: 'SAD will not be saturated for at least the next generation'; p.10: discusses saturation/leakage limitations. | 报告了分数量程、当前最好模型与上界，明确 SAD 远未饱和；未在饱和基准上宣称微小提升，达到 1。 |
| J13 | 指令遵循 | 0.5 | p.96-100: ANTI-IMITATION uses logit/probability criteria and string/format rules; p.87: ID-LEVERAGE uses GPT-3.5-turbo to judge language of response; no split by negation/number/format/style constraints. | 部分指令遵循任务有可机器判定标准，但 ID-LEVERAGE 仍依赖 LLM 裁判，且未按约束类型系统拆分准确率，故为 0.5。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.22: invalid answers scored as r correct answers; p.34: 'Answer ... with the label ... and nothing else'; p.95: refusals and incorrect-format answers discussed; no explicit format-valid rate. | 报告了结构化输出约束与无效答案处理，但没有系统报告格式合法率/重试策略，且未把格式失败与内容错误完全分开，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不是安全/越狱评估，没有有害请求、自然拒绝率或对抗攻击成功率测量。 |
| J16 | LLM 作为被试的范式定位 | 1 | p.4 defines situational awareness for LLMs; p.9 compares to human self-awareness/mirror test and metacognition; p.23-24 human roleplay baselines; p.20 Table 3 reports exact model versions; p.10 cautions about extrapolation and future agentic settings. | 明确界定了 LLM 上的构念并与人类同名构念作理论对照，报告模型版本，用人类 roleplay 作为同范式基线，且没有直接把人类心理学结论外推。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文报告随规模/版本得分提高，但没有宣称“涌现/突变”，也没有把能力曲线作为核心争议分析。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对基准/奖励模型/LLM-judge 进行优化训练，也没有代理指标过优化环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.22: standard error estimation for scores; p.26 Table 6 reports ±; p.20 Table 3 gives model versions/dates; p.7 Table 1; code available at p.1; no paired bootstrap/McNemar tests. | 报告了模型版本/日期与误差范围，并提供代码；但未统一报告重复次数 N、95%CI、配对检验与原始推理日志，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | SAD 任务基本为单轮提问/作答；Long Monologue 也是单次长回答，不是多轮对话一致性评估。 |

## 编码小结
SAD 在任务操作化、提示模板、计分规则、人类 roleplay/上界基线、模型版本记录与误差估计方面报告较充分，且明确指出任务未饱和、模型间差异与构念区分。主要不足是：模型/提示/任务比较多为描述性基准结果，缺少预注册、事前功效分析、混合/多层模型、系统性污染检测、完整的位置/顺序翻转率、温度与采样敏感性、LLM 裁判偏差控制，以及部分条件顺序与格式合法率的量化报告。
