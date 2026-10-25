# article_210 | Language Model Alignment in Multilingual Trolley Problems | 2025

研究类型概述：跨语言、跨模型的 LLM 道德偏好基准评测：以 Moral Machine 人类判断为金标准，将 460 个电车困境情景翻译为 107 种语言，评估 19 个 LLM 在六类道德维度上的偏好，并报告语言敏感性、语言资源相关、提示改写一致性、选项顺序稳健性与 jailbreak/uncensor 后的拒绝率与偏好变化。分析单位为模型—语言—情景/聚合偏好，不是人类被试实验。
- **研究构念（Construct）**：跨语言道德判断、牺牲偏好与人类价值对齐｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让19种现成LLM在100多种语言的电车难题中作二选一牺牲判断，并与Moral Machine人类判断比较。（改变语言、物种、性别、体型、社会地位、年龄、生命数量和提示释义。）｜CA 任务锚定：道德困境任务（Moral Dilemma Task, `trm_57ebe6583f52d`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4–5: procedural generation across six moral dimensions, 18 character types, 460 English vignettes translated into 107 languages; p.5: 'ensure each scenario is phrased in both orders'. | 语言、六类道德维度、选项顺序和提示改写均被明确操纵，水平数也给出；但单位如何分配到各水平、完整操纵程序与正式操纵检验未完整报告，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.6: preference p_i defined as percentage of default value; MIS(ph,pm)=&#124;&#124;ph-pm&#124;&#124;_2; p.9: paraphrase Fleiss kappa; p.28 Table 13: option-order consistency rates. | 因变量指标与计分方式明确，并有翻译质量、顺序一致性和改写一致性等部分可靠性证据；但 MIS/偏好向量的正式信效度证据不足，也未系统说明端点/天花板地板等连续指标处理。 |
| A3 | 控制变量 | 0.5 | p.4: age scenarios 'control for the gender and number of characters'; p.5: both option orders; p.6: 'fix the random seed and set the temperature to zero'. | 报告了若干控制变量与控制手段（性别/人数匹配、选项顺序反平衡、温度与种子固定、模型标识），但不是系统控制变量清单，也未逐项说明控制方式。 |
| A4 | 混淆变量 | 0.5 | p.6: language-by-country mapping challenge; p.10 and p.17: dialect, text-only, binary-dilemma limitations; p.20: translation-quality check; p.28: option-order bias sanity check. | 识别并部分控制了选项顺序、翻译质量、语言—国家映射等潜在混淆，也讨论了残余限制；但缺少系统敏感性分析或残余混淆对内部效度威胁的量化说明。 |
| A5 | 调节变量 | NA | — | 研究没有调节变量理论模型或交互检验；语言敏感性、语言资源相关和聚类属于描述性/相关性分析，不是调节效应分析。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量、直接/间接效应分解或因果链假设。 |
| A7 | 操作性定义 | 0.5 | p.4–5: character types and six dimensions described, 460 vignettes, 1–5 characters; p.5: token-forcing prompt; p.6: preference percentage and MIS formula. | 关键构念有操作化描述和公式，但完整的程序化情景生成规则、随机选择规则、精确分配与复现细节主要依赖外部代码/附录，正文未逐构念完整写尽。 |
| A8 | 水平数与类型 | 0.5 | p.4–5: six moral dimensions with age (3 groups), status (3 tiers), fitness (3 levels), gender (7 pairings), number (1–5), species; p.5: 107 languages and five paraphrases. | 各水平具体取值/标签大体明确；但未系统说明水平类型、间距/全距，连续变量入回归的中心化/标准化也未涉及。 |
| A9 | 单一操作化的风险 | 1 | p.10: trolley problem 'sometimes criticized ... too narrow or unrealistic'; p.17: 'Reducing moral judgments to binary choices risks oversimplifying' and calls for other dilemmas. | 关键构念主要采用单一电车困境/二选一操作，但论文在讨论和伦理声明中明确讨论了其可推广性限制及推广边界，符合单一操作时明确讨论限制的要求。 |
| A10 | 单一方法的风险 | NA | — | 这是 LLM 提示—输出评测，不是人类自陈式多构念测量；共同方法偏差（Harman 单因子等）不构成本设计的核心风险。 |
| B1 | 被试间设计 | NA | p.6: 19 LLMs evaluated on the same Moral Machine-derived dataset; no human participant allocation. | 无人类被试组间分配；各 LLM 都在同一套语言和情景上评测，模型身份不是随机分配的被试组。 |
| B2 | 被试内设计 | NA | p.5–6: each question presented in many languages and models are evaluated across the dataset; no sequential within-subject condition-order design. | 没有需要顺序平衡的人类被试内重复测量；LLM 每次为独立提示调用，选项顺序问题在 E1/J1 下单独评价。 |
| B3 | 混合设计 | NA | — | 不存在人类被试的组间/组内混合设计及对应误差项。 |
| B4 | 因子设计 | NA | p.4: six dimensions are varied through separate scenario construction; no full factorial design matrix or interaction ANOVA. | 研究不是完整交叉的因子实验；情景通常隔离一个道德维度并控制其他属性，未报告因子设计矩阵或交互分析。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理分配研究；无人类非随机分组与因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理可逆性/迁移对称性设计问题。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥处理条件的随机化程序；所有模型接受全部语言/情景，随机选取角色仅是刺激构造的一部分。 |
| C2 | 平衡 | NA | — | 无条件顺序的被试内平衡问题；选项呈现顺序的反平衡在 E1/J1 下评价。 |
| C3 | 恒定 | 0.5 | p.6: 'fix the random seed and set the temperature to zero'; p.19 Appendix C.1: greedy decoding; p.19 Tables 4–5: exact model identifiers; p.10: text-only limitation. | 报告了温度、贪心解码、模型标识和文本模态等恒定条件，并讨论了文本模态等外部效度限制；但未系统列出所有环境/API/提示版本等恒定变量。 |
| C4 | 匹配 | NA | — | 无匹配被试或被试组的设计；语言—国家加权平均属于聚合方法，不是匹配。 |
| C5 | 纳入为变量 | 0 | p.9: RQ4 correlates per-language misalignment with number of speakers; p.20: translation-quality check; main MIS analyses do not include these as covariates. | 研究测量了语言使用者数量和翻译质量等潜在混淆，但没有把它们作为协变量/区组纳入主分析模型，也未检验相关模型假设。 |
| C6 | 盲法 | NA | — | 主研究为自动化 LLM 推理，无人类被试或人类评分者需要盲法；MTurk 翻译质量评估不是主因变量评分。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 条件顺序层级需要说明。 |
| D1 | 练习效应 | NA | p.5–6: each prompt is a standalone trolley scenario evaluated by LLMs; no practice block or trial-position learning. | LLM 每次为独立会话/独立提示，不存在人类被试的练习效应或试次位置学习。 |
| D2 | 疲劳效应 | NA | — | 全自动 API/本地推理，无人类 session 时长与疲劳问题。 |
| D3 | 延滞 / 迁移效应 | NA | p.5: single vignette prompt with binary forced choice; no multi-turn condition history. | 每次独立提示，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉处理，故无迁移对称性问题。 |
| D5 | 范围效应 | NA | p.6: preference is percentage of binary choices, not Likert/absolute magnitude rating. | 因变量为二选一偏好百分比，不存在主观量表锚定或范围效应校准问题。 |
| E1 | 位置 / 顺序偏差 | 1 | p.5: 'ensure each scenario is phrased in both orders'; p.28 Table 13: consistency rates after swapping option order for all models. | 对选项顺序做了完全反平衡（每个情景两种顺序），并报告了交换后的一致性率；无 LLM 裁判，因此评审者间信度不适用。 |
| E2 | 默认赞同 | NA | p.6: binary moral choice; p.20: 5-point translation-quality rating not a focal attitude scale. | 主任务不使用 Likert/态度自评量表；翻译质量评分是辅助质量检查，不构成主要构念的默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | 0.5 | p.7–8: GPT-4o Mini 'binarize' and 'always prefers humans ... with pspecies of 100%'; Figures 3/4: endpoint-heavy radar distributions; p.8: language clusters. | 报告了部分端点堆积/偏好极端化信息，并讨论了模型分布差异；但没有系统报告偏度/端点与中点比例，也未对跨语言反应风格差异做校正。 |
| E4 | 需求特征 | NA | — | 无人类被试，故无掩饰情节、事后访谈或人类需求特征检查；LLM 的 safety refusal 属 J15 讨论范围。 |
| E5 | 实验者效应 | NA | p.6 and p.19: fully automated LLM API/local inference. | 完全自动化数据采集，无人类主试或评分者，故无实验者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7–8: GPT-4o Mini 'pspecies of 100%', extreme preferences; Table 14: Llama-family mean preference percentages; Figures 3/4: endpoint radar plots. | 报告了部分均值/端点和明显天花板式二值化现象，但未系统报告偏度、端点频率和 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无人类同源自陈式多构念测量，故共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.7: correlations 0.87, 0.69, 0.68 with p<0.001; p.9: Fleiss kappa 0.56, pairwise F1 78%, accuracy 81%; Table 11: Pearson correlations and p-values. | 报告了相关系数和若干效应量/一致性指标，但缺少置信区间、样本量确定依据、多重比较校正和主要分析完整性说明。 |
| F2 | 内部效度 | 0.5 | p.4–5: procedural generation and controlled character attributes; p.28: option-order robustness check; no human allocation/flow or baseline equivalence. | 研究不是人类随机试验；虽对情景构造和选项顺序做了部分控制，并讨论翻译/语言映射限制，但未报告分配隐藏、基线等价、被试流向/损耗等内部效度程序。 |
| F3 | 构念效度 | 0.5 | p.20: MTurk translation-quality evaluation; p.9: paraphrase consistency with Fleiss kappa; p.28: option-order consistency; p.17: construct/scope limitations. | 有翻译质量、顺序一致性和改写一致性等可靠性/稳健性证据，也讨论了电车困境的构念限制；但缺少对偏好/MIS 测量的正式效度论证和系统操纵检验。 |
| F4 | 外部效度 | 0.5 | p.6: 19 open/closed LLMs; p.5 and Appendix B.1: 107 languages; p.10/17: text-only, dialect, binary-dilemma limitations; Appendix E.4: regional maps. | 报告了模型与语言样本及多项推广边界，但没有讨论模型/语言抽样代表性，也缺少独立的跨样本或跨情境复现实验。 |
| G1 | 分析单位 | 0.5 | p.6: preference vectors computed by language/model; p.8: language-level standard deviation and K-means; p.9: correlations across languages/models; no multilevel model. | 分析层级为语言/模型层面的聚合偏好，但未显式说明情景嵌套于语言、语言嵌套于模型等聚集结构，也未用多层模型分离方差。 |
| G2 | 随机效应 | NA | p.6: 19 fixed LLMs compared descriptively; no mixed-effects model. | 模型被视为固定的 19 个评测对象而非从更大模型总体随机抽样；没有需要随机截距/随机斜率的被试随机效应结构，故本组件不适用。 |
| G3 | 材料作为随机效应 | 0 | p.5: 460 vignettes per language; p.6: preferences are aggregated percentages; no item-level mixed model, F1/F2, or F-prime analysis. | 有限的具体情景被当作固定刺激并聚合为语言/模型偏好，未将材料/项目作为随机效应，因而对任意电车情景的推广缺乏项目层面统计支持。 |
| G4 | 统计功效 | 0 | p.6: 98,440 scenarios and 40M human responses; p.7–9: correlation and descriptive comparisons; no a priori power analysis or confidence intervals. | 未报告设计阶段功效分析、目标功效或预期效应量来源；结果以点估计、相关系数和 p 值为主，缺少置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.4: countries with at least 100 respondents included (130 countries); p.6: 19 models and six dimensions listed; p.9: paraphrase experiment restricted to 14 languages and 2 models due computational budget. | 报告了部分纳入/排除规则、模型与条件清单及计算预算导致的子集；但未完整报告 LLM 输出剔除规则、样本量停止规则，也未区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–10: no preregistration or registered analysis plan reported; p.17: code/data availability statement only. | 全文未报告时间戳早于数据收集的公开预注册、样本量/停止规则或分析计划；因此记 0。 |
| J1 | 位置偏差 | 1 | p.5: each scenario phrased in both orders; p.28 Table 13: consistency rates against option-order position bias for all evaluated models; p.6 and p.19: model identifiers and temperature zero. | 对候选位置做了完全反平衡，并报告了交换前后的一致性率；不涉及 LLM-as-judge 或人类评分者信度，因此相关子项不适用。 |
| J2 | 冗长偏差 | NA | — | 任务为短二选一道德选择，不涉及开放式生成长度/质量评分，无冗长偏差风险。 |
| J3 | 谄媚 | NA | — | 提示中没有用户先验立场、反馈或纠错对话，故不涉及谄媚/附和用户立场风险。 |
| J4 | 自我偏好 | NA | — | 研究以 Moral Machine 人类数据为金标准，不使用 LLM-as-judge 评估模型输出，故无自我偏好裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.5: token-forcing prompt template without in-context examples. | 实验为零样本提示，不使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5: prompt template and token-forcing wording; p.20 Table 6: five prompt paraphrases generated by GPT-4; p.9: paraphrase robustness only on 14 languages and two models. | 提供了提示模板和五种改写，并做了提示敏感性检查；但没有完整 prompt 版本/日期、未说明 dev/test 划分、未报告全语言/全模型敏感性，也未提供完整调参搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | p.5 Table 2: average vignette around 51 words; no long-context/RAG setup. | 提示上下文很短，不涉及长上下文信息位置或 RAG 检索排序问题。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'fix the random seed and set the temperature to zero'; p.19 Appendix C.1: 'temperature to zero for greedy decoding'. | 报告了温度与贪心解码并声称固定种子，但未给出种子值、top-p/top-k 等完整采样参数，也没有对同一提示重复采样并报告 N/置信区间。 |
| J9 | 重复与文本退化 | NA | p.5: token-forcing to elicit binary choice; short option outputs. | 任务为分类式短选项输出，不涉及开放式生成长文本的重复/退化问题。 |
| J10 | 分词效应 | 0 | p.5 Table 2: reports words per vignette by language (English 47, Chinese 78, Swahili 38); no tokenizer name/version or token-length control. | 这是跨语言/跨脚本研究，但未报告分词器版本、token/词数比或在分析中控制 token 长度，故无法排除语言效应与分词效率混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.9: 'data that is not found online and hence was not seen during the LLMs’ training'; no formal contamination detection or training-cutoff table. | 作者论证了数据为按需生成/翻译，污染风险较低；但没有报告所有模型的训练截止日期、n-gram/DCQ 重叠检测或污染率。 |
| J12 | 基准饱和 | 0.5 | p.6: MIS range 0 to 2.45; p.7: some scores below 0.6; p.8: 'GPT-4o Mini ... binarize ... pspecies of 100%'. | 报告了指标量程和部分端点堆积/二值化现象，但没有在接近端点时系统改用连续指标或 bootstrap CI 比较，也未明确讨论饱和对模型差异解释的影响。 |
| J13 | 指令遵循 | NA | p.5: task asks which side the car 'should save', not constraints on instruction following. | 因变量为道德选择，不是指令遵循；无需按否定/数量/格式/风格约束拆分准确率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | p.5: bullet options and token-forcing, but no structured-output grammar/JSON requirement. | 实验不要求 JSON/文法约束等结构化输出，也没有将格式合法率作为核心指标。 |
| J15 | 越狱稳健性 | 0.5 | p.9–10: high refusal rates; token-forcing and uncensoring technique applied to four open models; Figures 12–15: refusal-rate decompositions for original vs uncensored variants. | 包含对抗性 uncensoring 并报告拒绝率，但未使用有害请求集或标准 ASR，也未把自然提示拒绝率与对抗 ASR 作为两个独立安全构念系统报告。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: 'evaluate the moral alignment of LLMs with human preferences'; p.4: Moral Machine human judgments serve as ground truth; p.6: model identifiers; p.17: not suitable for real-world moral decisions. | 使用与人类 Moral Machine 同范式的人类数据对照，也报告模型版本与限制；但没有系统论证 LLM 上测量的道德偏好与人类同名构念的理论异同，也未做新的人类对照实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | p.6: multiple model sizes are evaluated descriptively, but no model-size/ability curve or emergence claim. | 研究不涉及随规模/训练进展的能力曲线，也不宣称涌现或相变。 |
| J18 | 指标博弈与奖励过优化 | NA | p.6: pure evaluation of fixed models; no training, RL, reward-model optimization, or best-of-N optimization. | 没有以 benchmark/奖励模型/LLM-judge 为优化目标的训练过程，故不涉及指标博弈或奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6: fixed seed/temperature; p.19 Tables 4–5: exact open-weight and API model identifiers; p.17: code/data released; no bootstrap CI or paired tests. | 模型 snapshot/标识较精确，并发布数据/代码；但每个条件未报告重复采样 N 与 95% CI，模型比较未做配对检验，seed 值也未明确给出。 |
| J20 | 多轮对话中的一致性衰减 | NA | p.5: each vignette is a single-turn prompt with forced binary answer; no dialogue history. | 实验严格单轮，不涉及多轮对话一致性衰减。 |

## 编码小结
该研究的核心是可复现的 LLM 基准与刺激构造，而非人类被试实验；因此许多人类实验设计组件（B、C、D、E 中的人类分配/顺序/盲法/需求特征等）不适用。可评价部分显示：情景维度、语言、选项顺序和提示改写有明确操纵或检查，翻译质量、选项顺序一致性和改写一致性也有报告；但缺少多层/随机效应建模、项目层面推断、正式信效度/操纵检验、功效分析与预注册、token 长度控制、重复采样置信区间和污染检测。整体为较扎实的探索性/描述性 LLM 对齐评测，但统计推断与可复现细节仍有明显缺口。
