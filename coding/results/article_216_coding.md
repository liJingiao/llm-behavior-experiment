# article_216 | Evaluating the Inductive Abilities of Large Language Models: Why Chain-of-Thought Reasoning Sometimes Hurts More Than Helps | 2025

研究类型概述：纯 LLM 基准评测与提示干预研究：作者构造四类隐藏规则游戏任务，比较 8 个非推理/推理 LLM 的规则归纳准确率，并用 GPT-4o 作语义裁判；另做理论误差分析与人类标注的错误类型分类。分析单位为规则/案例级准确率及其在模型、游戏、规则类型和干预条件下的聚合，无人类被试分配。
- **研究构念（Construct）**：归纳规则发现、表面先验干扰与链式推理错误传播｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：让八个现成模型从棋类、扑克、骰子和二十一点的短游戏轨迹中归纳未明示的正常或特殊规则，并比较CoT阶段与约束干预。（操纵游戏领域、正常/特殊规则、模型类型、推理阶段和分解/示例/长度约束。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3: models are presented with gameplay transcripts; p.8–9: decomposition/solving/summarization/combined interventions; p.25–26: intervention prompt templates. No manipulation check or full allocation procedure is reported. | 隐藏规则类型（NR/SR）、游戏与提示干预构成可识别自变量且有水平标签和部分操纵程序，但未报告分配方式与操纵检验，故为0.5。 |
| A2 | 因变量 | 0.5 | p.3: “Rule-level accuracy is computed as the proportion of cases judged as consistent.” p.13: GPT-4o judge prompt and examples. | 因变量指标和计分方式明确，但无信度/效度证据、无连续指标预处理或天花板/地板处理说明。 |
| A3 | 控制变量 | 0.5 | p.4: “We randomize the board size (ranging from 8 to 15), shuffle rule assignments across games, and ensure each piece appears at least three times per episode.” | 报告了部分控制变量及手段，但未系统列出完整控制清单。 |
| A4 | 混淆变量 | 0 | p.3 lists model versions and GPT-4o judge; p.4 describes game construction, but no confound identification or sensitivity analysis appears. | 模型规模/训练数据、API差异、提示差异、裁判同源等明显潜在混淆未被识别或讨论，故为0。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量假设与交互检验/简单斜率分析；模型类型与规则类型的比较只是描述性分组。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或中介效应分解。 |
| A7 | 操作性定义 | 1 | p.3–4: game rules and transcript fields; p.13: judge prompt; p.15: induction prompt; p.25–26: intervention prompts. | 关键构念的操作化较完整：隐藏规则、输入transcript、诱导输出格式、GPT-4o判分和三阶段干预均有可复现描述。 |
| A8 | 水平数与类型 | 0.5 | p.3: eight models and versions; p.4: chess 225 transcripts, Texas Hold’em 100 combinations, etc.; p.5 Fig.2: rule-wise SR/NR levels; p.9 Fig.3: intervention levels. | 报告了水平数与取值/标签，但未系统说明水平类型、间距/全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 0.5 | p.3–4: four game tasks and multiple rule variants are used to operationalize inductive reasoning; p.9: per-game and per-intervention results. | 使用多游戏/多规则进行多操作化，但未报告各操作间会聚证据，也未讨论推广限制。 |
| A10 | 单一方法的风险 | 0 | p.3: “We therefore use GPT-4o (gpt-4o-2024-08-06) as a reference judge”; GPT-4o is also one of the evaluated models. | DV完全来自LLM裁判，且裁判模型与被评模型同源；未报告共同方法偏差控制或统计检验。 |
| B1 | 被试间设计 | NA | — | 无人类被试或被试组随机分配；模型比较是观察性分组，不是被试间实验设计。 |
| B2 | 被试内设计 | NA | — | 同一模型跨任务/条件被重复评测，但每次为独立prompt调用，论文未构造需要顺序平衡的被试内会话设计。 |
| B3 | 混合设计 | NA | — | 没有明确的混合设计、组间/组内因素标注或混合误差项模型。 |
| B4 | 因子设计 | 0 | p.5 Fig.2 and p.9 Fig.3 display crossed game/rule/intervention conditions, but no full design matrix, cell sizes, ANOVA table or interaction statistics are reported. | 存在多因素比较结构，但未报告完整因子设计统计与交互项。 |
| B5 | 主效应 | 0 | p.4: “reasoning models consistently perform worse … on special rules”; p.5 Fig.2 shows descriptive bars only. | 只有描述性主效应模式，未报告F/df/p/效应量等主效应检验。 |
| B6 | 交互作用 | 0 | p.4–5: group × rule-type pattern is described as “observed across all domains,” but no interaction test or simple-effects analysis is reported. | 未对交互项做统计检验，也无多重比较或图示误差棒。 |
| B7 | 区组设计 | NA | — | 无区组/分层变量与区内随机分配设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计。 |
| B9 | 准实验设计 | 0 | p.1: “CoT reasoning can degrade inductive performance”; p.3 lists naturally different existing models, with no random assignment to reasoning/non-reasoning condition. | 非随机模型比较被用于支持因果性“reasoning hurts”结论，但未讨论选择偏差或内部效度限制。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM prompt条件为独立调用，无处理残留或可逆性/迁移对称性问题需要论证。 |
| C1 | 随机化 | NA | — | 无人类或模型单位到条件的随机分配；p.4的随机化属于刺激/规则构造，不是实验单位分配。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件顺序；评测为独立prompt调用，未报告顺序设计。 |
| C3 | 恒定 | 0.5 | p.3: exact model version strings; p.9: “strict token budget of 1000 tokens”; p.26: stop sequences and prompt template. | 列出了部分恒定变量（模型版本、token预算、裁判模型），但未系统说明外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配程序。 |
| C5 | 纳入为变量 | 0 | p.3–4: model versions and randomized rule assignments are described, but no known confounds are measured and entered as covariates/blocks. | 未将模型规模、训练数据、API差异等已知混淆变量纳入协变量或区组分析。 |
| C6 | 盲法 | 0 | p.7: “each failure trace was independently reviewed by two annotators using shared labeling criteria”; no blinding or formal agreement statistic is reported. | 错误类型人工标注涉及评分者，但未报告盲法安排；LLM裁判亦无盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级或顺序效应设计。 |
| D1 | 练习效应 | NA | — | LLM独立prompt调用，无练习块或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 无人类session时长或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立prompt/API调用，未报告跨条件残留或清洗期需求。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性设计。 |
| D5 | 范围效应 | NA | — | 无主观量表或绝对判断的范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.4: “We randomize the board size …, shuffle rule assignments across games, and ensure each piece appears at least three times per episode.” | 报告了部分刺激/规则随机化，但未说明呈现顺序、选项顺序或各位置平衡细节。 |
| E2 | 默认赞同 | NA | — | 研究不使用Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，因此无需求特征与事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 主数据采集为自动化LLM调用，无人类主试期望传递问题；人工标注问题见C6。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.4: “most models exceed 90% accuracy” on normal rules; p.9: “Performance on NR rules remains saturated under all settings.” No SD, skew, endpoint frequency or pilot calibration is reported. | 识别到NR饱和，但未报告完整分布/端点频率或任务难度校准。 |
| E7 | 共同方法偏差 | NA | — | IV与DV并非同源自陈式量表，无共同方法偏差的同源测量问题。 |
| F1 | 统计结论效度 | 0 | p.5 Fig.2 and p.9 Fig.3 show accuracy bars; no confidence intervals, effect sizes, sample-size rationale or multiplicity correction are reported. | 统计结论效度报告不足：仅有描述性比较，缺少效应量与CI。 |
| F2 | 内部效度 | 0 | p.3–4 describe model evaluation and task construction, but no random assignment, allocation concealment, baseline equivalence, or participant flow/attrition handling. | 无内部效度保障程序；模型比较的选择偏差未评估。 |
| F3 | 构念效度 | 0 | p.3: GPT-4o is used as reference judge; p.7: annotator agreement described qualitatively; no reliability/validity statistics or manipulation check. | 未报告关键测量的信度、效度、裁判与人类一致性或操纵检验。 |
| F4 | 外部效度 | 0.5 | p.3: eight model names/versions and API/local access are listed; p.4: four games. No sampling frame, representativeness, or boundary-condition discussion. | 报告了模型来源与任务范围，但未论证对外部总体/情境的推广边界或跨样本复现。 |
| G1 | 分析单位 | 0.5 | p.3: “Rule-level accuracy is computed as the proportion of cases judged as consistent”; p.5 Fig.2 aggregates model × game × rule accuracy. No multilevel/aggregation model is reported. | 说明了规则级分析指标，但未说明案例嵌套于模型/游戏/规则的结构如何处理，存在分析单位与独立性隐患。 |
| G2 | 随机效应 | 0 | p.3 lists specific models; p.5/p.9 report model-level comparisons without mixed models or random effects. | 模型被当作固定组别处理，未报告随机效应结构或可推广的模型总体范围。 |
| G3 | 材料作为随机效应 | 0 | p.4: “We construct 225 distinct transcripts by enumerating all combinations of four NRs and four SRs across the six available options”; materials are fixed rather than modeled as random samples. | 有限规则/transcript被当作固定材料，未使用item随机效应或准F/混合模型，存在材料固定效应问题。 |
| G4 | 统计功效 | 0 | p.3–5: no power analysis, expected effect size, sample-size derivation or confidence intervals are reported. | 无设计阶段功效分析或样本量论证，结果亦未报告效应量/CI。 |
| G5 | 研究者自由度 | 0.5 | p.4 and p.7–8 report all rule categories and two annotators, but no trial exclusion rules, stopping decisions, or confirmatory/exploratory distinction. | 部分研究者自由度有报告，但关键排除规则、样本量决定与探索/验证区分缺失。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or pre-specified analysis plan appears in the paper. | 无预注册；不能区分验证性与事后探索性分析。 |
| J1 | 位置偏差 | 0 | p.13 judge prompt fixes the order: “Ground-truth rule: [INSERT TRUE RULE]” followed by “Model-induced rule: [INSERT MODEL RULE]”; p.3 says GPT-4o is queried three times with majority vote but no order swap. | LLM裁判存在固定候选顺序但未做位置反平衡、交换重判或翻转率报告，故为0。 |
| J2 | 冗长偏差 | 0 | p.13 judge prompt contains no length-control instruction; p.15 induction prompt says “Be precise and concise,” but no length–score correlation or length distribution is reported. | LLM裁判评价自然语言规则，存在长度/冗长偏差风险，但完全未说明或控制。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或纠错对话，不涉及谄媚操纵。 |
| J4 | 自我偏好 | 0 | p.3: “We therefore use GPT-4o … as a reference judge”; the same GPT-4o is listed among evaluated non-reasoning models. | 裁判模型与被评模型同源且未匿名化、未用异源陪审团或报告自我偏好偏差率，故为0。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主任务为零样本归纳，输入是待归纳的游戏transcript而非带标签的few-shot示例；J.2是风格提示而非有标签示例集。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.13 judge prompt, p.15 induction prompt, p.25–26 intervention prompts are provided; no prompt versions, sensitivity ablations, or dev/test separation are reported. | 提供了完整模板，但未做措辞敏感性消融、版本化或dev/test划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | transcript通常仅10–12步，不是长上下文/RAG实验，无中间迷失问题。 |
| J8 | 温度与采样随机性 | 0 | p.3 reports model version strings and that GPT-4o judge is queried three times; no temperature, top-p, seed, repetition count for main outputs, or confidence intervals are reported. | 采样超参与主要重复运行未报告，无法把LLM非确定性纳入统计设计。 |
| J9 | 重复与文本退化 | 0 | p.26: “1000-token generation limit using stop sequences”; no decoding strategy, repetition penalty, n-gram repetition rate, or degeneration QC is reported. | 涉及开放式CoT/规则生成，但未报告解码与退化控制。 |
| J10 | 分词效应 | NA | — | 单语言英文、单脚本任务，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3–4 describe self-constructed game tasks but do not compare test-set release dates with model training cutoffs or perform contamination detection. | 未做任何训练数据/测试集污染检查，不能排除记忆或公开数据重叠。 |
| J12 | 基准饱和 | 0.5 | p.4: “most models exceed 90% accuracy” on NRs; p.9: “NR rules remains saturated”; no continuous metrics or bootstrap CIs are used. | 识别到NR饱和并转向SR分析，但未改用连续指标或报告CI比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；虽然有输出格式指导，但不测量约束遵循率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.15 output format: “Induced Rule: <your concise natural language description>”; p.26 token/format constraints. No format-validity rate or retry policy is reported. | 报告了简单结构化输出要求，但未报告格式合法率，也未将格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | NA | — | 研究为能力评测，不涉及有害请求、越狱或安全对齐评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.3: “This more closely mirrors human induction, which relies on observing outcomes…” and model snapshots are largely reported; no human baseline or systematic LLM-vs-human construct comparison. | 将“inductive reasoning”作为类认知构念测量，并简要联系人类归纳，但未系统论证构念等价性或报告人类同范式对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨模型规模/训练进展的能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL、best-of-N或对代理指标的迭代优化环节；提示干预只是被评测条件。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.3 reports exact model versions for most models, but p.5/p.9 figures report no repeated-run N, confidence intervals, paired tests, or raw logs. | 有部分snapshot标识，但缺少主要分数的重复次数、CI和配对比较，故未达基本要件。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮transcript到规则归纳，无多轮对话历史累积。 |

## 编码小结
该研究属于 LLM 能力评测加提示干预，不是人类被试实验。A–G 中许多人类被试分配、顺序平衡、疲劳/练习等组件不适用；但基准评测相关风险（LLM 裁判同源、位置/长度偏差、采样与重现性、污染、饱和、结构化输出、LLM 构念定位）实际存在且大多未充分控制。整体证据以描述性柱状图和示例为主，缺少统计检验、置信区间、裁判信效度与采样细节。
