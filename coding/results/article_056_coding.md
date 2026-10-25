# article_056 | Skin-in-the-Game: Decision Making via Multi-Stakeholder Alignment in LLMs | 2024

研究类型概述：LLM 提示框架的基准评测研究，而非人类被试实验。研究以多个道德推理基准为任务，比较 I/O、CoT、TE、SKIG 及消融/变体在不同 LLM 上的准确率，并用 GPT-4 作为裁判评估利益相关者识别与推理一致性；分析单位为基准题目、模型调用及提示条件。
- **研究构念（Construct）**：共情、问责与风险视角下的道德判断及多方利益决策（moral judgment and multi-stakeholder decision-making under empathy, accountability, and risk）｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：LLM 提示框架的基准评测研究，而非人类被试实验。研究以多个道德推理基准为任务，比较 I/O、CoT、TE、SKIG 及消融/变体在不同 LLM 上的准确率，并用 GPT-4 作为裁判评估利益相关者识别与推理一致性；分析单位为基准题目、模型调用及提示条件。｜CA 任务锚定：道德困境任务（Moral Dilemma Task, `trm_57ebe6583f52d`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5 Table 1 lists I/O, CoT, TE, SKIG accuracy; pp.16-21, 28-29 give prompt structures; p.8 tests prompt variants and ST/MT variants. No explicit randomization/allocation or manipulation check. | 自变量被明确命名并给出多个水平及提示程序，但缺少单位分配方式、随机化及操纵检验，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.5: model ‘select the most appropriate option from four presented choices’; Tables 1/3/5 report accuracy. p.22 Table 17 reports split sizes. No reliability/validity/preprocessing or ceiling/floor handling. | 因变量指标与计分方式明确（基准准确率），但无信效度证据、无反应时等预处理，也无专门的天花板/地板说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.22 Table 18: ‘temperatures were held at zero for all experiments, except for consistency experiment where temperature was set to 0.7’; p.22 Table 17 fixed dataset splits; p.5 uses a single H100. | 报告了温度、数据集划分、硬件等部分保持恒定的做法，但未系统列出控制变量清单及每项控制手段，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.8: ‘ten additional prompt sets with altered lexical choices and syntax versions’; p.8: ‘single-turn variants performed poorly... MT...’; pp.37 Tables 37-39 report ablations. | 识别并检验了提示措辞、单轮/多轮等潜在混淆，但未系统报告残余混淆或敏感性分析对内部效度的威胁，故为 0.5。 |
| A5 | 调节变量 | NA | — | 论文没有理论上的调节变量、调节假设或交互检验；模型比较是描述性分组，不是正式调节分析，故不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或因果链中介假设，故不适用。 |
| A7 | 操作性定义 | 1 | pp.4-5 describe six SKIG steps with explicit prompts; pp.20-21 and 28-29 provide full prompt templates; p.22 gives stakeholder-identification scoring (‘correct only when all characters... are present’); results scored by benchmark accuracy. | 关键构念（提示条件、利益相关者识别、最终选择）均有可执行的操作化程序和计分说明，达到可复现程度。 |
| A8 | 水平数与类型 | 0.5 | p.5 Table 1 lists four prompting methods and seven LLMs; p.8 reports ST-All/ST-Best/MT-Best/MT-All variants; p.22 Table 18 lists model context lengths. Levels are categorical; no explicit level type/spacing/centering. | 报告了水平数与各水平标签，但未系统说明水平类型、间距/全距及连续变量中心化等，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | pp.5-8 report MMLU Moral Scenarios, Moral Stories, ETHICS and Social Chemistry results with broadly similar improvement trends; p.8 reports consistency rates 93/92/91 for components. | 关键构念采用了多个基准/指标，并报告了相似趋势，但未做正式会聚效度统计或明确讨论单一操作化局限，故为 0.5。 |
| A10 | 单一方法的风险 | NA | — | 因变量为基准标签正确率，自变量为提示条件；不涉及同一来源的自陈式多构念测量，共同方法偏差问题不适用。 |
| B1 | 被试间设计 | NA | p.5: same benchmark items are evaluated under all prompting methods; no independent subject groups. | 没有人类被试或独立组分配；基准题目被重复用于多个提示条件，故被试间设计不适用。 |
| B2 | 被试内设计 | NA | — | 论文未定义人类被试内重复测量设计，也未报告被试层顺序平衡；LLM 调用按独立提示进行，故不适用。 |
| B3 | 混合设计 | NA | — | 论文没有明确声明混合设计、逐因素标注组间/组内或两类误差项，故不适用。 |
| B4 | 因子设计 | 0 | p.5 Table 1 and pp.37 Tables 37-39 cross prompting methods with seven models and report cell accuracies, but no interaction term or ANOVA table. | 存在多因素交叉表格，但没有报告任何交互项统计检验，按 B4 规则记 0。 |
| B5 | 主效应 | 0 | p.5 Table 1 reports descriptive accuracy differences by method/model; no F, df, p, effect size or formal main-effect tests. | 只有描述性百分比，没有主效应的统计检验结果，故记 0。 |
| B6 | 交互作用 | 0 | p.5 Table 1; no interaction test, simple effects, multiple-comparison correction or error bars. | 完全未报告交互项统计检验与简单效应分析，故记 0。 |
| B7 | 区组设计 | NA | — | 没有区组变量、分层变量或区内随机分配，故不适用。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方或被试内顺序平衡，故不适用。 |
| B9 | 准实验设计 | NA | — | 这不是非随机分配的人类准实验；论文只是对不同提示条件做基准比较，故不适用。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理的适用条件论证或迁移对称性检验，故不适用。 |
| C1 | 随机化 | NA | — | 每个基准题目都在多个提示条件下被评估，不存在把分析单位随机分配到互斥条件的程序；故不适用。 |
| C2 | 平衡 | NA | — | 提示条件以独立 API 调用实施，无被试内条件顺序需要平衡，故不适用。 |
| C3 | 恒定 | 0.5 | p.22 Table 18: temperatures zero except 0.7 for consistency; p.22 Table 17 fixed dataset splits; p.5 single H100 for local models. No discussion of external-validity limits from these constants. | 报告了温度、数据集划分、硬件等恒定控制，但未系统列出恒定变量水平并讨论外部效度限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 没有匹配变量、配对或倾向得分匹配程序，故不适用。 |
| C5 | 纳入为变量 | 0.5 | p.5 Table 1 includes model identity as a crossed factor; p.8 and pp.37 Tables 37-39 include prompt-component ablations and ST/MT variants; no covariate model, slope-homogeneity test or adjusted effect sizes. | 通过模型因素和消融部分隔离了一些已知差异，但未作为协变量正式控制，也未检验相关假设或报告调整后效应，故为 0.5。 |
| C6 | 盲法 | 0 | p.5: ‘We instruct human annotators to classify errors into the above bias categories.’ No blinding, rater independence, or blind-success check is reported. | 存在人类评分者进行错误分类，但未报告任何盲法安排及施盲对象，故记 0。 |
| C7 | 平衡的层级 | NA | — | 没有顺序效应平衡层级或构造方法，故不适用。 |
| D1 | 练习效应 | NA | — | LLM 基准题目以独立提示调用完成，不存在人类练习块或跨试次学习语境，故不适用。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长与疲劳控制问题；LLM 调用不涉及生理疲劳，故不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各提示条件基本为独立调用；多轮子问题在一个会话内累积，但不是跨条件残留或清洗期设计，故不适用。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件迁移或不对称迁移设计，故不适用。 |
| D5 | 范围效应 | NA | — | 因变量为客观选项正确率，不是绝对量值估计或李克特量表，故范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | pp.20-21 show fixed A/B/C/D answer-choice order; p.23 judge prompt fixes ‘Answer 1’ as SKIG answer and ‘Answer 2’ as labels, with no position counterbalancing. | 多项选择与裁判比较均按固定位置呈现，未报告选项/刺激顺序随机化或反平衡，故记 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，故默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也没有跨群体反应风格比较，故不适用。 |
| E4 | 需求特征 | NA | — | 没有人类被试、掩饰情节或事后访谈；LLM 基准任务不涉及人类需求特征，故不适用。 |
| E5 | 实验者效应 | 0 | p.5 mentions human annotators for error categorization, but no rater blinding, training standardization, or scripted scoring is reported. | 人类评分者参与辅助错误分类，但未报告盲法层级、培训或脚本化程度，故记 0。 |
| E6 | 天花板 / 地板效应 | 0.5 | pp.5-8 Tables 1/3/5 report accuracy percentages, including GPT-4 99% on ETHICS and 96% on Moral Stories; no SD, skew, endpoint frequencies, or pilot difficulty calibration. | 报告了聚合准确率，但未报告分布形态/端点频率，也未讨论接近上限的任务饱和，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 自变量为提示条件、因变量为基准正确率，不是同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.5 Table 1 and pp.5-8 report point accuracies only; no effect sizes, confidence intervals, power analysis or multiple-comparison correction are reported. | 只有点估计准确率，未报告效应量/CI、样本量依据或多重性校正，故记 0。 |
| F2 | 内部效度 | 0.5 | p.5 uses fixed benchmark test split and evaluates same items under all methods; p.8 and pp.37-39 add prompt-robustness and ablations. No random allocation, allocation concealment, baseline-equivalence test, or participant flow/attrition. | 同一题集下条件对比及部分稳健性/消融评估支持内部效度，但缺少正式分配程序、基线等价与损耗报告，故为 0.5。 |
| F3 | 构念效度 | 0.5 | p.8 reports GPT-4-judged consistency of 93%, 92%, 91% for empathy, risk and outcome components; multiple established benchmarks are used, but no formal reliability/validity evidence or manipulation check is reported. | 有多个基准和一致性结果，但缺少正式信效度统计、操纵检验及单一操作化局限讨论，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.5 lists seven LLMs and four benchmarks; p.22 Table 17 gives dataset split sizes; p.9 limitations discuss negotiation and harmful-response extensions, not clear sampling or generalization boundaries. | 报告了模型与基准来源及样本规模，但未系统论证代表性、推广边界或跨情境复现，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p.5 and p.22 report accuracy aggregated over test questions; no explicit analysis-level model or nesting structure (e.g., items within benchmark, repeated method) is described. | 分析单位可推断为基准题目/模型调用，但未说明分配层级与统计模型是否匹配，故为 0.5。 |
| G2 | 随机效应 | NA | — | 论文未使用混合模型或随机效应推断；模型作为固定系统被比较，且没有正式随机效应模型需求，故不适用。 |
| G3 | 材料作为随机效应 | 0.5 | p.22 Table 17 shows benchmark subsets drawn from larger pools (400/894; 1000/3964; 2000/20000), but p.5 and pp.5-8 report only aggregate accuracy and do not model item/material random effects. | 材料来自更大题目池，具备项目抽样意义，但分析未将题目作为随机因子或报告混合模型，故为 0.5。 |
| G4 | 统计功效 | 0 | p.22 Table 17 gives sample sizes, but there is no a priori power analysis or sample-size justification; pp.5-8 report no effect sizes or confidence intervals. | 无事前功效分析，结果也未报告效应量或 CI，故记 0。 |
| G5 | 研究者自由度 | 0.5 | p.22 Table 17 reports selected test sizes; p.8 adds prompt-robustness, ST/MT and risk-objective analyses; no explicit exclusion rules, stopping rules, or confirmatory/exploratory labeling. | 报告了主要条件与部分补充分析，但没有完整的排除/停止规则和验证性-探索性区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–40 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文没有预注册平台、注册编号、分析计划或预注册偏离说明；按判定口径记 0。 |
| J1 | 位置偏差 | 0 | pp.20-21 use fixed A-D choice order; p.23 judge prompt fixes Answer 1/Answer 2 order; no position counterbalancing or flip-rate analysis is reported. | 涉及多项选择与 LLM 裁判比较，但完全未做候选位置反平衡或位置偏差报告，故记 0。 |
| J2 | 冗长偏差 | 0 | p.8 uses a GPT-4 ‘Judge’ for consistency and stakeholder identification; p.23 shows judge prompts without length-control instructions or length-score correlations. | 使用 LLM 裁判评估生成内容，但未识别或控制长度/冗长偏差，故记 0。 |
| J3 | 谄媚 | NA | — | 任务是无用户先验立场的封闭式道德基准问答，没有用户立场操纵或反馈对话，故谄媚偏差不适用。 |
| J4 | 自我偏好 | 0 | p.8: ‘we prompt a GPT-4 “Judge” model’ while GPT-4 is also one of the evaluated LLMs; no same-source control, anonymization, or self-preference quantification is reported. | 裁判模型 GPT-4 同时属于被评模型集合，未控制自我偏好，故记 0。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.22: stakeholder identification uses a ‘four-shot setting’; p.23: consistency judge uses a ‘two-shot setting’; no exemplar source, label ratio, permutation, multi-seed repetition, or full exemplar set is reported. | 使用 few-shot，但只报告示例数量，未报告来源、标签比例、顺序控制或多 seed 结果，故记 0。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.8: ‘ten additional prompt sets... average accuracy of 70.5%’; pp.28-29 provide sample paraphrase templates; p.38 Table 43 reports prompt 1-5 accuracies. No prompt version/date or dev/test split is reported. | 提供了完整模板并做了提示敏感性消融，但缺少版本日期、dev/test 划分及完整搜索过程，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务上下文为短基准题干，不涉及长文档、RAG 或关键信息位置操纵，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | p.22 Table 18: temperature 0 for all experiments except 0.7 for consistency; no random seeds, repeated sampling N, or confidence intervals are reported. | 报告了温度但无 seed、重复采样次数与 CI，故为 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.22 Table 18 reports temperature settings only; no greedy/beam/sampling decoding details, repetition penalty, degeneration rate, or truncation proportion is reported. | 部分报告了解码温度，但未报告重复/退化 QC，故为 0.5。 |
| J10 | 分词效应 | NA | — | 实验为英语单语言、单脚本，无跨语言或跨格式 token 数比较，故不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.5 and p.22 use public MMLU Moral Scenarios, Moral Stories, ETHICS and Social Chemistry splits; no model training cutoff, contamination check, n-gram overlap, or held-out private test is reported. | 使用公开基准且未评估训练数据污染，故记 0。 |
| J12 | 基准饱和 | 0 | p.8 Table 5 reports GPT-4 99% on ETHICS, and p.7 Table 3 reports 96% on Moral Stories, but there is no ceiling/saturation analysis, continuous metric, or CI comparison. | 在接近上限的基准上仍宣称提升且未识别饱和问题，故记 0。 |
| J13 | 指令遵循 | NA | — | 研究评估道德判断/选择准确率，不以指令遵循为因变量，故不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0 | pp.20-21 require selecting one of A-D choices, but no grammar-constrained output, format-validity rate, retry policy, or separate format/content error reporting is given. | 存在多项选择格式要求，但未报告格式约束设置与格式合法率，故记 0。 |
| J15 | 越狱稳健性 | NA | — | 论文不涉及安全/越狱或对抗攻击评估，故不适用。 |
| J16 | LLM 作为被试的范式定位 | 0 | p.1 frames ‘moral reasoning and ethical decision-making’ in LLMs; p.5 uses human moral benchmarks, but the paper never explicitly compares LLM moral-reasoning constructs with human constructs or discusses construct-validity boundaries. | 论文以道德推理、共情、问责等心理学式构念包装 LLM 任务，但未论证 LLM 构念与人类同名构念的关系；若视为纯工程任务则可不适用，但本文按适用处理并记 0。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有随模型规模/训练进展的能力曲线或涌现宣称，故不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有训练/RL/best-of-N 等对代理指标的优化过程，也没有 overoptimization 监控问题，故不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.22 Table 18 lists model names/context lengths but no precise snapshot/API date; pp.5-8 report single point accuracies without repeat N, CI, paired tests, or raw logs. | 缺少精确 snapshot、重复次数、CI 和配对检验，故记 0。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.8 asks ‘Does this method necessitate a multi-turn framework...’ and compares ST-All, ST-Best, MT-Best, MT-All; p.37 Table 41 reports aggregate accuracies 20/22/59/71%. No per-round scoring or context-truncation analysis is reported. | 存在多步/多轮提示变体比较，但不是用户-模型多轮对话，也未按轮次拆分或报告历史截断；按部分满足记 0.5。 |

## 编码小结
论文提供了较完整的提示模板和多基准、多模型结果，但整体是描述性 benchmark 评估：缺少正式统计推断、效应量与置信区间、条件顺序/位置平衡、随机化、信效度论证、预注册及多数 LLM 评估可复现性细节；因此多数设计层组件只能部分满足或因不适用而记 NA。
