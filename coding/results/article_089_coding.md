# article_089 | The Lawyer That Never Thinks: Consistency and Fairness as Keys to Reliable AI | 2025

研究类型概述：纯 LLM 基准/重复测量评测：六个模型在四类理性任务与 MBE 法律题上各重复 12 次，比较 TRCS、ICC 与 ANOVA；无人类被试、无实验操纵、无 LLM 裁判、无少样本、无安全评估、无多轮对话。
- **研究构念（Construct）**：理性判断、认知偏差、测试—重测一致性与法律判断稳定性｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：纯 LLM 基准/重复测量评测：六个模型在四类理性任务与 MBE 法律题上各重复 12 次，比较 TRCS、ICC 与 ANOVA；无人类被试、无实验操纵、无 LLM 裁判、无少样本、无安全评估、无多轮对话。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | — | 研究为六个固定模型的基准评测，模型与任务类型是观察分组，而非研究者主动操纵的自变量，故无实验自变量。 |
| A2 | 因变量 | 0.5 | p.5-6: 'Test-Retest Consistency Score (TRCS) captures the proportion of identical responses across repeated trials... ICC assesses the reliability... ANOVA to determine whether differences... are statistically significant.' | TRCS、ICC 与 ANOVA 作为因变量指标及计分思路已界定；但未报告这些指标的信效度证据，也未说明连续指标预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | p.4: 'All responses were generated using each model’s official API with default settings; no parameters were modified to ensure consistent testing conditions.' | 报告了至少一个控制手段（固定 API 默认设置、不调参），但没有系统列出所有控制变量及其具体水平（如 temperature、top-p、日期、调用参数）。 |
| A4 | 混淆变量 | NA | — | 无操纵自变量的观察性基准，不涉及实验内部效度意义上的自变量混淆；文中虽提及后端更新/采样随机性，但不属于受控实验混淆变量。 |
| A5 | 调节变量 | NA | — | 理论模型与结果均无调节变量或交互检验假设。 |
| A6 | 中介变量 | NA | — | 理论模型与结果均无中介变量或直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p.4-6: 'four well-established behavioral tasks...' 'TRCS... proportion of identical responses...' 'All code, Python scripts, and data ... publicly available at our GitHub repository' | 关键构念有任务名称、示例和一致性指标定义，且提供代码仓库；但正文未给出完整题目集、完整 prompt 与逐项计分细节，操作化仍不完整。 |
| A8 | 水平数与类型 | NA | — | 无多水平实验自变量；模型与任务仅为观察分组，未报告水平类型、间距或中心化等实验水平信息。 |
| A9 | 单一操作化的风险 | 0.5 | p.7: 'TRCS and ICC capture different dimensions of consistency... relying on TRCS alone may overstate model reliability.' | 使用多个任务与 TRCS/ICC 多指标，但未系统报告各操作化之间的会聚证据；对单一指标局限有讨论但不完整。 |
| A10 | 单一方法的风险 | NA | — | LLM 基准无人类问卷式同源自评，共同方法偏差框架不适用；所有输出来自模型 API，但并非自评量表同源问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试的组间分配；模型比较不是被试间实验分组。 |
| B2 | 被试内设计 | 0.5 | p.4: 'We conducted six trials over 30 days. In each trial, we presented every question twice using identical prompts... This repeated-measures design...' | 确有模型内重复测量（每模型多次重复作答），但未报告试次/题目顺序的随机化或平衡方案及各顺序分配。 |
| B3 | 混合设计 | NA | — | 未构成正式的组间×组内混合实验设计，也未按混合设计分别报告组间/组内误差项；仅是基准任务的重复测量。 |
| B4 | 因子设计 | NA | — | 不是因子实验；无因素完全交叉的设计矩阵、每格样本量与交互统计。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无因子设计交互项及简单效应分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理分配研究。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理的不可逆性或迁移对称性问题；LLM API 各次调用独立。 |
| C1 | 随机化 | NA | — | 无随机分配或分配隐藏；模型为固定选取，不属于随机化实验。 |
| C2 | 平衡 | 0 | p.4: 'Rather than administering all trials consecutively, we deliberately distributed the testing schedule to capture temporal fluctuations in model behavior.' | 存在重复试次顺序/时间安排，但未报告任何条件顺序平衡方案、各顺序数量或迁移对称性论证。 |
| C3 | 恒定 | 0.5 | p.4: 'official API with default settings; no parameters were modified to ensure consistent testing conditions' | 报告了一个恒定控制（API 默认设置），但未具体列出默认参数值或其他环境/时段恒定变量及外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 无将已知混淆变量作为区组或协变量纳入模型的分析；研究也不是受控实验。 |
| C6 | 盲法 | NA | — | 全自动 API 调用，无人类被试、主试或评分者可施盲。 |
| C7 | 平衡的层级 | 0 | p.4: 'deliberately distributed the testing schedule' | 虽有重复试次的时间分散，但未说明完全平衡/拉丁方/ABBA 等平衡层级、构造方法或顺序效应假设。 |
| D1 | 练习效应 | NA | — | 各次 API 调用独立，无对话上下文内学习或练习块；LLM 重复试次不涉及人类练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类被试疲劳问题；调用为自动化短任务，不涉及 session 休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立 API 调用，无跨条件迁移或清洗期问题；文中后端更新是时间漂移风险，不是处理迁移。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件对的迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 无主观量表或绝对判断的范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0 | p.8 Table 5: legal prompt with fixed answer choices '(A)... (B)... (C)... (D)...' and model first/second attempt; no option-order randomization reported. | 使用多项选择选项，但未报告选项位置随机化/反平衡、位置×正确率分析或偏好翻转检查，存在固定选项位置偏差风险。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中点反应倾向。 |
| E4 | 需求特征 | NA | — | 无人类被试，不涉及需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6: 'TRCS analysis reveals substantial response variability... with a standard deviation of 0.23'; Figures 1-3 show score distributions. | 报告了部分描述统计/图形，但未报告偏度、端点频率或 pilot 难度校准，无法充分排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 无自评式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.6: 'ANOVA results (F (3.65), p = 0.0059)' and 'Levene’s test (F (1.38), p = 0.245)'; no effect sizes or CIs. | 只报告了显著性检验，未报告效应量、置信区间、样本量确定依据或多重性校正；统计结论效度信息不足。 |
| F2 | 内部效度 | NA | — | 观察性基准，无随机分配、分配隐藏或被试流向等实验内部效度组件；也不作强因果推断。 |
| F3 | 构念效度 | 0.5 | p.6-7: ICC is used as reliability of model outputs; p.7 discusses TRCS/ICC divergence. | 报告了 ICC 作为信度型指标并讨论指标差异，但缺少效度证据、操纵检验和多操作化会聚证据。 |
| F4 | 外部效度 | 0.5 | p.4 Table 2 lists six models and sizes; p.9 limitations note only 30-day period and only legal/rationality tasks. | 报告了模型样本来源与部分特征及推广边界，但无跨样本/跨情境复现结果，外部效度论证有限。 |
| G1 | 分析单位 | 0.5 | p.4: 'We treat each model as an independent evaluation unit'; p.4 repeated trials per question per model. | 说明了模型为独立评估单位，但未说明题目/试次嵌套于模型的分析层级，也未使用多层模型处理重复观测。 |
| G2 | 随机效应 | 0 | p.6: one-way ANOVA and Levene’s test reported; no random-effects specification. | 重复观测和题目嵌套存在，但未说明哪些因子为随机/固定效应，也未报告混合模型随机截距/斜率结构。 |
| G3 | 材料作为随机效应 | 0 | p.4-5: tasks and MBE questions are used as fixed benchmark items; no item random effect reported. | 有限题目/材料被当作固定测试集，分析中未将题目作为随机效应，无法支持向材料总体的推广。 |
| G4 | 统计功效 | 0 | p.4: 'six trials... twelve responses per question per model'; no power analysis or target effect size. | 未报告事前功效分析、目标功效、预期效应量或样本量/重复次数依据；结果也无效应量与 CI。 |
| G5 | 研究者自由度 | 0.5 | p.4: 'six trials over 30 days... every question twice... twelve responses per question per model'; code/data public. | 报告了重复次数与部分任务/条件，但未报告数据排除规则、题目总数、样本量决定方式或验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–13 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未提及预注册、注册平台/编号或分析计划；按缺失记 0，而非 NR。 |
| J1 | 位置偏差 | 0 | p.8 Table 5: fixed options '(A)...(D)' and first/second attempts; no option-position counterbalancing or flip-rate analysis. | LLM 多项选择任务存在候选位置偏差风险，但未做选项顺序随机化/反平衡，未报告位置×正确率或翻转率。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放式生成质量，无长度被误当质量的比较场景。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话，不涉及谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 或成对模型评判，无自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 未使用 few-shot in-context examples，为零样本问答式评测。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p.4: 'identical prompts'; Table 3/5 give examples but no complete prompt template, versioning or sensitivity ablation. | 使用自定义提示但未提供完整模板、版本号或语义等价措辞敏感性检验，也未说明 dev/test 分离；prompt 自由度未受控。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG 设置；任务输入远低于长窗口。 |
| J8 | 温度与采样随机性 | 0.5 | p.4: 'official API with default settings; no parameters were modified' and 'twelve responses per question per model'. | 报告了重复次数与默认设置，但未给出 temperature、top-p、seed 等具体采样超参，也未报告重复运行的置信区间。 |
| J9 | 重复与文本退化 | NA | — | 任务为多项选择/短答案，不涉及开放式长文本生成的重复与退化问题。 |
| J10 | 分词效应 | NA | — | 单语言英语、单脚本，无跨语言/跨分词器比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4-5: MBE and rationality tasks are public benchmarks; no training-cutoff vs test-version comparison or contamination detection reported. | 使用公开法律/理性基准但未检查训练数据污染，未报告测试集版本与模型训练截止日期对照，污染风险未评估。 |
| J12 | 基准饱和 | 0 | p.7: 'GPT-4 consistently answered specific legal prompts (TRCS = 1.00)...'; no saturation assessment or continuous alternative metric. | 部分 TRCS 已达 1.00，存在天花板风险，但未评估基准饱和或改用连续指标/更难子集。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，无否定/数量/格式等约束遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/JSON/文法约束输出，格式合法性不是独立指标。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱/对抗攻击评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.4-5: 'These tests serve as diagnostic tools for evaluating alignment with normative standards of reasoning, rather than as evidence of human-like cognition'; p.1 compares LLM and human experts. | 明确了 LLM 上理性/一致性构念与人类构念的差异，并列出模型；但无人类同范式对照实验，也未系统论证跨模型/规模作为自变量的构念效度。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告跨规模/训练进展的能力曲线，也未宣称涌现或指标诱导的突变；仅有模型大小与一致性描述性比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不对 benchmark/奖励模型/LLM-judge 作优化，无代理指标过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4: 'twelve responses per question per model'; model names listed, but no exact snapshot/API date, CIs, or paired tests in results. | 报告了重复次数和模型名称，但 snapshot 标识不精确，未报告 95%CI、配对检验或逐题敏感性分析。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮问答/基准调用，无多轮对话历史累积。 |

## 编码小结
研究属于观察性 LLM 一致性基准。报告了 TRCS/ICC 定义与重复测量安排，但统计报告和设计控制较薄弱：缺少 prompt/采样超参细节，且未做选项位置、污染、饱和、功效等检查。大量人类实验组件因设计不适用而记 NA。
