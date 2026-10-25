# article_090 | SocialCC: Interactive Evaluation for Cultural Competence in Language Agents | 2025

研究类型概述：这是一项面向 LLM/语言智能体的跨文化能力基准评测：构建 3,060 个人工撰写的多轮跨文化互动场景，让不同 LLM 扮演角色进行多轮对话，再由 GPT-4o 作为 LLM-as-judge 按文化觉察、文化知识（常识与价值观）、文化行为评分；并以 450 个场景的人类标注检验裁判准确率。研究不是人类被试实验，而是观察性模型比较与基准评测。
- **研究构念（Construct）**：跨文化能力、文化觉察、文化知识与文化适切行为｜CA 构念锚定：刻板印象（stereotypes, `trm_4a3fd79d0b285`）；态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：这是一项面向 LLM/语言智能体的跨文化能力基准评测：构建 3,060 个人工撰写的多轮跨文化互动场景，让不同 LLM 扮演角色进行多轮对话，再由 GPT-4o 作为 LLM-as-judge 按文化觉察、文化知识（常识与价值观）、文化行为评分；并以 450 个场景的人类标注检验裁判准确率。研究不是人类被试实验，而是观察性模型比较与基准评测。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | p.7: We evaluate multiple LLM families, including Phi-4, Mistral-7B, Llama-2...；全文为基准评测，模型身份不是随机操纵的自变量。 | 没有研究者主动操纵、水平分配或操纵检验；模型/国家/话题均为观察性分组，故 NA 而非 0。 |
| A2 | 因变量 | 0.5 | p.6: Cultural Awareness ... score of 1 if ... 0；Cultural Behavior ... score of 3 ... 0；p.7/12: GPT-4o judge vs 450 human scenarios, accuracy >88%, double-annotated. | 因变量指标与计分方式明确；有人类-裁判准确率，但无内部一致性/重测/评分者信度，也无连续指标预处理说明，故 0.5。 |
| A3 | 控制变量 | 0.5 | p.7: set the temperature to 1 ... judge models ... to 0；we select GPT-4o as the judge；apply AutoGen。 | 报告了温度、裁判模型与部分实现常数；未系统列控制变量清单，也未讨论恒定带来的外部效度限制，故 0.5。 |
| A4 | 混淆变量 | 0.5 | p.9: LLMs internalise certain cultural biases during pretraining...；p.8: English cultural dominance；p.10 limitations mention cultural biases. | 识别了训练数据偏差/英语文化主导等潜在混淆，但未说明控制方式或敏感性分析，故 0.5。 |
| A5 | 调节变量 | NA | — | 没有调节变量假设或交互检验；国家/话题/文化组仅为描述性分层，故 NA。 |
| A6 | 中介变量 | NA | — | 没有中介假设或直接/间接效应分解，故 NA。 |
| A7 | 操作性定义 | 1 | p.6: 逐维定义评分规则（awareness/knowledge 0/1；behavior 0–3），并说明 Social Goal Completion 与 Cultural Conflict Management；p.16–20: 给出 simulation/judge prompts。 | 关键构念均有可执行的操作化与评分程序，故 1。 |
| A8 | 水平数与类型 | NA | p.6 Table 2 lists model labels；p.14 country/scenario counts；no manipulated multi-level IV. | 模型、国家、话题是基准分组/材料属性，不是研究者操纵的多水平自变量，故 NA。 |
| A9 | 单一操作化的风险 | 0 | p.6: 每个维度仅用单一 LLM-judge rubric 计分；p.7: 仅以 450 例 human validation 报告总体 accuracy。 | 关键构念未采用多种操作化并报告会聚证据，也未在局限中讨论单一操作对推广的限制，故 0。 |
| A10 | 单一方法的风险 | 0.5 | p.7: we select GPT-4o as the judge；human evaluation... accuracy exceeding 88%；p.12: 450 scenarios double-annotated. | 主评分与被评输出同属 LLM 管线，但有人类评分作为部分异源校验；无共同方法偏差程序/统计控制，故 0.5。 |
| B1 | 被试间设计 | NA | — | 基准对多个模型在同一组场景上评测，没有将被试/模型分配到互斥实验条件的被试间设计，故 NA。 |
| B2 | 被试内设计 | NA | — | 虽每个模型在多个场景上重复评测，但场景是固定基准材料而非实验条件，且无顺序平衡或重复测量模型，故 NA。 |
| B3 | 混合设计 | NA | — | 无组间/组内因素混合设计，故 NA。 |
| B4 | 因子设计 | NA | — | 无完全交叉的因子实验设计或 ANOVA 主效应/交互分析；模型比较为描述性基准，故 NA。 |
| B5 | 主效应 | NA | — | 无因子设计主效应统计检验，故 NA。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验；图 5/6 为描述性分层，故 NA。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配程序，故 NA。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计，故 NA。 |
| B9 | 准实验设计 | NA | — | 非准实验设计，也无随机分配/因果推断设计，故 NA。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内实验条件，故 NA。 |
| C1 | 随机化 | NA | — | 没有条件分配或随机化步骤；所有模型均在固定基准上评测，故 NA。 |
| C2 | 平衡 | NA | — | 无条件顺序需平衡，故 NA。 |
| C3 | 恒定 | 0.5 | p.7: agent temperature=1, judge temperature=0, vLLM/AutoGen, same GPT-4o judge；p.4: fixed cultural knowledge sources. | 列出若干恒定设置，但未完整列清单，也未讨论外部效度限制，故 0.5。 |
| C4 | 匹配 | NA | — | 无匹配设计，故 NA。 |
| C5 | 纳入为变量 | NA | — | 未把混淆变量作为区组/协变量纳入模型；无 ANCOVA/协变量分析，故 NA。 |
| C6 | 盲法 | NA | — | 无实验条件盲法安排；人类标注用于 judge validation，不是条件施盲，故 NA。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级，故 NA。 |
| D1 | 练习效应 | NA | — | 每个场景为独立 LLM 会话，未设计跨条件练习块；多轮对话中的提示是任务本身而非练习效应控制，故 NA。 |
| D2 | 疲劳效应 | NA | — | LLM 评测无人类疲劳/休息安排，故 NA。 |
| D3 | 延滞 / 迁移效应 | NA | — | 场景独立，无跨条件清洗期/残留迁移设计，故 NA。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性设计，故 NA。 |
| D5 | 范围效应 | NA | — | 因变量为裁判量表分数而非人类绝对判断/李克特自评，故 NA。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无选项顺序或多处理顺序的反平衡；每个场景独立评测，固定顺序不构成实验条件，故 NA。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，故 NA。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表跨群体反应风格比较，故 NA。 |
| E4 | 需求特征 | NA | — | 无人类被试，LLM 不被认为会产生人类需求特征；未设置掩饰情节/事后访谈，故 NA。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者按条件施测；人类标注仅用于 judge validation，故 NA。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 2: behavior score distribution by 0/1/2/3 for each model；awareness/knowledge means reported；p.4 human validation but no pilot difficulty calibration. | 报告了部分因变量端点分布（behavior），但 awareness/knowledge 未报分布，亦无 pilot 难度校准，故 0.5。 |
| E7 | 共同方法偏差 | 0.5 | p.7: GPT-4o judge；p.12: 450 human scenarios for validation；no CMB statistical test. | 同一 LLM 管线产生输出并由 LLM 评分，仅以人类验证部分缓解；无 CMB 检验或同源比例报告，故 0.5。 |
| F1 | 统计结论效度 | 0 | p.6 Table 2 reports means/percentages only；p.7 reports aggregate means；no CIs, effect sizes, significance tests or multiplicity correction. | 仅描述性均值/百分比，缺少效应量、CI、样本量依据与多重性校正，故 0。 |
| F2 | 内部效度 | NA | — | 非随机实验，无分配隐藏/基线等价/被试流向；研究为基准评测而非因果推断，故 NA。 |
| F3 | 构念效度 | 0.5 | p.7: human eval 450 scenarios, judge accuracy >88%；p.12 Table 5A per-dimension accuracy 84–92%；p.6 construct definitions. | 有构念定义与 judge 对人类的准确率，但无评分者间信度/kappa、无 manipulation check，故 0.5。 |
| F4 | 外部效度 | 0.5 | p.4: 3,060 scenarios over 60 countries/6 continents；p.9–10 limitations: broad but not complete, English-only, cultural norms dynamic. | 报告了场景/国家来源并讨论推广边界，但未报告跨样本/跨情境复现，故 0.5。 |
| G1 | 分析单位 | 0.5 | p.6 Table 2 reports model-level aggregate means across scenarios；p.7 evaluate multiple LLM families；no multilevel model for scenarios nested in models. | 分配/分析层级未显式建模；存在场景嵌套于模型/国家的聚集结构，但只做聚合均值，故 0.5。 |
| G2 | 随机效应 | NA | p.6 Table 2 reports fixed set of model names；no random-effects model. | 模型为固定基准对象，研究没有进行从模型总体抽样的随机效应推断，也无混合模型结构需报告，故 NA。 |
| G3 | 材料作为随机效应 | 0 | p.4: handcraft 3,060 scenarios；p.6 Table 2 aggregates across scenarios；no item random effect or mixed model. | 有限场景被当作固定刺激，未将场景/国家作为随机效应或使用准 F/混合模型，存在语言作为固定效应谬误风险，故 0。 |
| G4 | 统计功效 | 0 | p.6–7: no power analysis, no effect size or confidence interval；only descriptive means. | 无事前功效分析或样本量论证，结果也未报效应量/CI，故 0。 |
| G5 | 研究者自由度 | 0.5 | p.7 lists evaluated models and focuses on 8；p.6 Table 2 includes model results；p.12 human eval 450 scenarios；no exclusion rules or stopping rule. | 报告了多个因变量维度和模型结果，但未完整报告排除规则、样本量决定方式，也未区分验证性与探索性分析，故 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–31 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告预注册、注册编号或分析计划；故 0。 |
| J1 | 位置偏差 | NA | — | LLM 裁判针对单个对话评分，不涉及候选答案位置、排序或成对比较，故 NA。 |
| J2 | 冗长偏差 | 0 | p.16–20 judge prompts specify criteria and output format, but no instruction or analysis about answer length；no length-score correlation reported. | 开放式多轮生成由 LLM 裁判评分，存在长度/冗长偏差风险，但未控制或报告长度与得分关系，故 0。 |
| J3 | 谄媚 | NA | — | 没有操纵用户先验立场或测量谄媚；对手代理的挑战属于文化冲突任务，不是 sycophancy 评估，故 NA。 |
| J4 | 自我偏好 | 0 | p.7: GPT-4o as judge；evaluated models include GPT-4o and GPT-4.1；p.12 human accuracy is overall, not per-model or self-preference. | 用 GPT-4o 评判包含 GPT-4o/GPT-4.1 的模型输出，存在同源自我偏好风险；未匿名化、未用异源陪审团、未量化 favor-own，故 0。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.16–20 prompts are zero-shot task/judge prompts with output examples, not few-shot in-context exemplars. | 实验未使用 few-shot 示例选择与排列，故 NA。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.16–20 Appendix C provides full simulation and judge prompt templates；no prompt versioning, sensitivity ablation, or dev/test split reported. | 提供了完整模板，但未报告版本号、语义等价措辞消融或 dev/test 分离，故 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验无长文档/RAG 设置；多轮对话最多 20 轮，远低于长上下文操纵场景，故 NA。 |
| J8 | 温度与采样随机性 | 0.5 | p.7: agent temperature=1, judge temperature=0；no top-p/top-k, seed, repeat N, or confidence intervals reported. | 报告了主要温度设置，但缺少 seed、重复采样次数与 CI，故 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.7: temperature=1 for agents and 0 for judges；no repetition penalty, n-gram repetition rate, or degeneration QC reported. | 报告了基本解码温度设置，但未报告重复惩罚/退化率，也未严格说明各条件解码策略恒定，故 0.5。 |
| J10 | 分词效应 | NA | p.10: our benchmark is designed in English；no cross-language/cross-script experiment. | 单语言英文基准，无跨语言/跨脚本比较，故 NA。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.4: WVS Wave 7 Version 6.0 and Cultural Atlas used；p.7: model snapshots such as GPT-4.1-2025-04-14；no contamination detection or training cutoff comparison. | 报告了基准来源/版本与模型快照，但未做污染检测或训练截止日期对照，故 0.5。 |
| J12 | 基准饱和 | 0.5 | p.6 Table 2: awareness/knowledge means 0–1, behavior 0–3 with distribution；scores are not saturated but no bootstrap CIs or SOTA-position comparison. | 报告了分数量程与当前水位，基准未接近天花板；但未做 CI 比较，故 0.5。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，故 NA。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.16–20 judge prompts include Output Format specifications；no format legality rate or retry strategy reported. | 裁判输出要求结构化格式，但未报告格式合法率、重试或格式失败与内容错误拆分，故 0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估，故 NA。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: Cultural competence refers to the ability of individuals...；p.2: three key components；LLM agents role-play roles；no human behavioral comparison. | 把人类文化能力构念用于 LLM 代理测量，但未系统论证 LLM 同名构念与人类构念的异同，也未做人类同范式对照，故 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较不同模型规模，但未报告规模/训练进展能力曲线，也未宣称涌现或相变，故 NA。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究为纯基准评估，无训练、RL、best-of-N 等代理指标优化过程，故 NA。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.7 reports precise model snapshots/date identifiers；p.6 reports single aggregate scores；no repeat N, confidence intervals, or paired tests. | 模型 snapshot 标识较精确，但无重复次数、CI 与配对比较，故 0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.5: Complete task within 20 rounds；p.6 judge scores the dialogue history；no per-round scoring or consistency-decay analysis. | 确实做了多轮对话评估，但未按轮次拆分评分、未报告上下文截断或跨轮行为轨迹，故 0.5。 |

## 编码小结
论文提出了较完整的新型多轮跨文化能力评测框架，场景和评分维度定义较清楚，并提供人类标注验证；但其核心证据主要是模型层面的描述性均值与百分比，缺少置信区间、显著性/配对检验、场景随机效应建模、污染检查、裁判自我偏好与冗长偏差控制，也没有预注册或功效分析。总体适合编码为 LLM 基准评测，不宜按人类实验设计逐项苛求分配与顺序控制。
