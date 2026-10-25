# article_061 | Focus on Your Question! Interpreting and Mitigating Toxic CoT Problems in Commonsense Reasoning | 2024

研究类型概述：这是一篇LLM机制解释与缓解方法论文：作者定义并统计Toxic CoT（含Rationale Drift与Answer Drift），用归因追踪和因果追踪分析Llama2-13B/Baichuan2-13B内部信息流，提出RIDERS（Residual Decoding + Serial-Position Swap），并在五个常识推理基准及两个逻辑推理任务上进行多模型、多基线比较。分析单位为问题/数据集层面的LLM输出；无人类被试随机分配，也无LLM-as-judge评估。
- **研究构念（Construct）**：思维链诱导的答案偏离与常识推理退化（reasoning-induced answer/rationale drift in commonsense reasoning）｜CA 构念锚定：语义记忆（semantic memory, `trm_4a3fd79d0b083`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）
- **实验任务与范式（Task / Paradigm）**：这是一篇LLM机制解释与缓解方法论文：作者定义并统计Toxic CoT（含Rationale Drift与Answer Drift），用归因追踪和因果追踪分析Llama2-13B/Baichuan2-13B内部信息流，提出RIDERS（Residual Decoding + Serial-Position Swap），并在五个常识推理基准及两个逻辑推理任务上进行多模型、多基线比较。分析单位为问题/数据集层面的LLM输出；无人类被试随机分配，也无LLM-as-judge评估。｜CA 任务锚定：演绎推理任务（deductive reasoning task, `trm_4c898b8c2d071`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.7: 'Few-shot Answer, Chain-of-Thought, Self-Consistency, Self-Refine, Least-to-Most, Contrasive CoT, RD Only, SPS Only, RIDERS'; p.14 gives RD candidate_num n and weight ω. | prompt/方法条件被明确命名并给出多个水平，基本要件达成；但未报告操纵检验，也未说明单位如何分配到条件，故为0.5。 |
| A2 | 因变量 | 0.5 | PDF p.7: 'Accuracy (ACC)... Toxic Rate (TR)' and Eq.(8); p.3 Eq.(1) defines attribution score. | 准确率、Toxic Rate及归因分数的指标与计分方式有界定；但无信效度证据，也未说明连续指标的预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | PDF p.7: 'For all methods, we employ a 5-shot prompt'; p.14: 'both CoT prompting and our two methods utilize the same prompt'. | 报告了固定5-shot、同一prompt、固定模型/数据集等部分控制手段，但未系统列出控制变量清单及逐一控制方式。 |
| A4 | 混淆变量 | 0.5 | PDF p.4: 'To eliminate the influence of this additional factor... supplementary experiment'. | 识别了用golden label生成正确CoT可能引入的额外因素，并设计补充实验控制；但未系统讨论残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量假设或交互检验设计；模型/数据集比较是描述性分组，不是调节模型。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或因果链中介假设。 |
| A7 | 操作性定义 | 1 | PDF p.2 Def.2.1-2.3; p.6 Algorithm 1; p.7 Eq.(8); p.3 Eq.(1); pp.21-25 prompt templates. | Toxic CoT、Rationale Drift、Answer Drift、TR、归因分数和RIDERS均有可复现的公式或算法描述，关键操作化较完整。 |
| A8 | 水平数与类型 | 0.5 | PDF p.7 lists method levels; p.14 gives RD n/ω values; p.13 Table 5 gives dataset option numbers. | 多个条件/方法的水平数与标签清楚，部分数值参数也报告；但未说明水平类型、间距/全距或连续变量的中心化/标准化。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p.7 Table 1 reports ACC and TR; p.8 Table 2 separates Type1/Type2; p.13 Table 7 reports manual error classification. | 关键构念有多个指标和多种数据集/模型证据，但未正式报告各操作化之间的会聚统计，也未在局限中充分讨论单一操作化边界。 |
| A10 | 单一方法的风险 | 0 | PDF p.7 methods and metrics derive from the same LLM outputs; no common-method-bias test or procedural control is reported. | 自变量（prompt/方法条件）与因变量（同一模型输出上的ACC/TR）同源，全文未报告共同方法偏差的程序控制或统计检验。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配；所有方法在同一批问题/数据集上评测，不存在被试间条件分配。 |
| B2 | 被试内设计 | NA | — | 无人类重复测量设计；LLM各条件的生成为独立调用，未设置被试内顺序平衡或顺序效应问题。 |
| B3 | 混合设计 | NA | — | 研究没有人类被试的组间/组内混合设计，也没有对应的混合ANOVA或混合模型。 |
| B4 | 因子设计 | NA | — | 论文比较多个方法、模型和数据集，但不是形式化的因子实验设计，未报告完整设计矩阵、每格样本量与ANOVA交互表。 |
| B5 | 主效应 | NA | — | 没有因子设计意义下的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有正式交互项检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 研究不是准实验设计；无随机分配问题的人类/现场因果比较。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内设计，因此不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无被试或分析单位被随机分配到互斥条件；LLM实验只是对固定基准执行不同方法。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件顺序；各方法为独立生成/评测。 |
| C3 | 恒定 | 0.5 | PDF p.7: 'For all methods, we employ a 5-shot prompt'; p.14: 'both CoT prompting and our two methods utilize the same prompt'; models/datasets fixed. | 固定了模型、prompt和数据集等若干条件，但未系统列恒定变量及水平，也未充分讨论其外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入统计分析。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类被试、主试或评分者需要盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | LLM每条件独立生成，无上下文内学习或试次位置练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类session疲劳或长时任务休息安排问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立调用/重置上下文，无跨条件延滞或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观正确率/Toxic Rate，不使用主观量表或绝对量值判断，无范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF pp.21-25 prompt templates present fixed option orders such as '(1)...(5)'; no option-order randomization or counterbalancing is reported. | 任务为多项选择，选项位置/呈现顺序偏差风险实际存在；论文未做任何位置随机化或反平衡，也未讨论顺序效应。 |
| E2 | 默认赞同 | NA | — | 不使用Likert或态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中间反应倾向或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不涉及掩饰情节或事后需求特征访谈。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集与指标计算，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0 | PDF p.7 Table 1 and p.15 Table 8 report mean ACC/TR only; no SD, skew, endpoint frequencies, or pilot difficulty calibration are reported. | 准确率和Toxic Rate有上下界且可能受端点堆积影响，但论文只报均值，未做分布或难度校准检查，基本要件未达成。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，无共同方法偏差检验的典型适用场景。 |
| F1 | 统计结论效度 | 0 | PDF p.7 Table 1 reports point ACC/TR without confidence intervals, effect sizes, or p-values; p.13 Table 5 gives dataset sizes but no power rationale. | 未报告效应量/置信区间、样本量确定依据或多重性校正；仅有描述性点估计，统计结论效度报告不足。 |
| F2 | 内部效度 | 0.5 | PDF p.7 uses the same five benchmarks and baselines; p.14 states CoT and proposed methods use same prompt; no formal baseline equivalence, attrition, or contamination assessment. | 报告了部分比较控制（同一数据/模型/prompt），但无正式分配程序、基线等价性检验或内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | PDF p.2 Def.2.1-2.3; p.13 Table 7 manual error classification; p.7 ACC/TR metrics. | 有构念定义、人工错误分类和多数据集证据，但未报告评分者信度、测量效度统计或操纵检验。 |
| F4 | 外部效度 | 0.5 | PDF p.13 Table 5 dataset split/sample/option numbers; p.9 limitations on multi-choice and math; p.15 Tables 8-9 other models. | 报告了样本来源、数据规模和跨模型/任务复现，但代表性论证与明确推广边界仍不充分。 |
| G1 | 分析单位 | 0.5 | PDF p.7 metrics are computed over questions and averaged across datasets; p.13 Table 5 gives sample sizes; no multilevel model is reported. | 分析层级为问题/数据集层面的LLM输出，并做了聚合；但未说明分配层级与统计层级的匹配，也未处理嵌套/聚集结构。 |
| G2 | 随机效应 | NA | — | 论文未使用混合模型或随机效应推断；主要报告固定基准上的描述性点估计，故随机效应结构不适用。 |
| G3 | 材料作为随机效应 | NA | — | 未将材料/项目作为随机效应进行推断；论文不主张对任意材料总体的混合模型推广。 |
| G4 | 统计功效 | 0 | PDF p.13 Table 5 gives fixed dataset sizes; p.7 Table 1 reports point estimates only; no power analysis or confidence intervals. | 无设计阶段功效分析、预期效应量来源或CI报告，基本要件未达成。 |
| G5 | 研究者自由度 | 0.5 | PDF p.13 HellaSwag 2000-instance subset; p.14 'manually filter out the wrong CoT'; no full exclusion counts or explicit exploratory/confirmatory distinction. | 报告了部分抽样和排除做法，但未完整报告所有排除数量、全部条件及样本量决定过程，未区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | No pre-registration or registered analysis plan is mentioned in PDF pp.1-25. | 全文未报告预注册平台、编号或分析计划；按口径记0而非NR。 |
| J1 | 位置偏差 | 0 | PDF pp.21-25 prompts list fixed option orders such as '(1)...(5)'; no A/B swap, position randomization, or flip-rate reporting. | 研究涉及多项选择候选位置，存在位置偏差风险；论文完全未做位置反平衡/随机化，也未报告位置与正确率关系。 |
| J2 | 冗长偏差 | NA | — | 评估为多项选择准确率与Toxic Rate，不是开放性生成长短质量评分，长度偏差风险不适用。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 未使用LLM-as-judge或成对成对比较评分；评估基于可机器判定的选项正确率。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF p.7: 'For all methods, we employ a 5-shot prompt'; Figures 18-22 provide five-shot examples. | 报告了示例数量和完整模板，标签比例可从示例看出；但未说明示例来源/抽样seed、未做顺序反平衡，也未证明示例未取自测试集。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF pp.21-25 provide full prompt templates; p.14 states 'both CoT prompting and our two methods utilize the same prompt'. | 完整prompt模板已公布，但无版本号、迭代日期、语义等价措辞敏感性消融或dev/test分离说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验上下文很短，无长文档/RAG设置，不涉及中间迷失或关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0 | PDF p.14 gives RD candidate_num n and weight ω only; no temperature, top-p, seed, or repeated-sampling N/CI are reported. | LLM生成采样随机性未能作为受控随机源报告；仅单次运行点估计，基本要件未达成。 |
| J9 | 重复与文本退化 | 0.5 | PDF p.6 Algorithm 1 describes RD decoding; p.14 gives RD implementation details; no repetition/degeneration rate or repetition penalty is reported. | 报告了自定义解码策略，但未报告n-gram重复率/退化率，也未充分说明各比较条件解码策略是否严格恒定。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言、单脚本任务，无跨语言/跨脚本或跨格式输入比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.7 uses public benchmarks Winogrande, CSQA, HellaSwag, SIQA, PIQA; no benchmark version, model training cutoff, or contamination test is reported. | 使用公开基准但未做训练截止日期对照、n-gram重叠/DCQ等污染检测，存在记忆复现误判风险。 |
| J12 | 基准饱和 | 0.5 | PDF p.7 Table 1 reports ACC around 60-70 and TR; no SOTA position, confidence intervals, continuous metrics, or saturation discussion. | 报告了基准准确率量程与当前水位（约 60%–70%，未触及天花板），达成基本要件；但未深入评估各子集饱和度或提供连续校准指标与 CI 比较，记 0.5。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；任务是常识/逻辑多项选择，不是约束指令遵循评测。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF pp.21-25 prompts require output format like '{reason} So the answer is: ({option}) {answer}'; no format-valid rate or retry policy is reported. | 有明确格式约束且模板可复现，但未报告格式合法率、重试策略，也未将格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱、有害请求或对抗攻击评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文是LLM机制解释与工程方法评测，不主张把LLM作为人类心理学/认知科学被试来测量同名构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告跨模型规模/训练进展的能力曲线，也未宣称涌现能力。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对代理指标的训练/RL/best-of-N优化或奖励过优化监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | PDF p.7/p.14 report model names including 'gpt-3.5-turbo-1106', but no repeated runs, confidence intervals, or paired significance tests are reported. | 模型标识部分可查，但缺少重复次数、CI、配对检验和日志/逐题结果，评估可复现性报告不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮问答/生成，无多轮对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
论文的核心贡献在于现象定义、机制探测和方法提出，实验以基准准确率与Toxic Rate为主要指标，并辅以归因/因果追踪图形证据。方法描述和prompt附录较完整，但统计推断、信效度、采样随机性、测试集污染与位置/选项偏差控制等报告不足。多数人类被试设计组件（分配、顺序平衡、需求特征、实验者效应等）因研究无人类被试而不适用；与LLM评测直接相关的J1、J5、J6、J8、J9、J11、J12、J14、J19等存在不同程度的报告缺口。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 J12（0→0.5）。
