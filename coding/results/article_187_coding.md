# article_187 | Large Language Models Assume People are More Rational than We Really are | 2025

研究类型概述：该文属于 LLM-as-participant / 认知科学基准比较研究，而非新招募人类被试的实验。它使用已有的人类风险选择数据集 choices13k 和 Jern et al. (2017) 的逆向偏好推断数据集，比较多种 LLM 在零样本与思维链（CoT）提示、不同任务/情境下的输出与人类行为及理性模型（如最大期望值、绝对/相对效用模型）的一致性。主要设计变量是提示类型、任务类型、情境（收益/损失）和模型家族；分析单位是选择问题/成对比较及模型输出，不是人类被试分配单元。
- **研究构念（Construct）**：风险决策中的理性偏差、对他人选择的预测与逆向偏好推断｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：向模型呈现概率和收益不同的赌博选项，要求其自己选择或预测人类选择，并在另一任务中根据观察到的选择判断行动者偏好。（比较自我选择、预测他人和逆向推断任务，操纵赌博概率收益、提示方式和模型，并与人类及理性模型比较。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: 'we designed three forward modeling tasks'; 'zero-shot and CoT prompting across the three different tasks'; p.8: 'prompted using both zero-shot and chain-of-thought prompting'. 未报告操纵检验结果。 | 明确操纵了提示类型（zero-shot/CoT）及任务/情境水平，但缺少操纵检验与部分分配细节，完整性不足。 |
| A2 | 因变量 | 0.5 | p.5: 'computed correlations and mean-squared errors (MSE)'; p.8: 成对比较后按 pairwise wins 聚合为 ranking；p.19: behavioral-model MSE。 | 因变量指标与计分方式明确；但未报告信效度证据，也未说明连续相关/MSE 指标的预处理或端点效应。 |
| A3 | 控制变量 | 0.5 | p.4: 'To minimize any positional biases ... we shuffled the order of the options'; p.8: 'shuffled ... order that decisions appear in the pair, ... options within decisions, and ... items within each option'; p.4: temperature set to 0.7. | 报告了若干控制手段（选项/决策/项目顺序随机化、温度、模板），但未系统列出控制变量清单并逐项说明。 |
| A4 | 混淆变量 | 1 | p.8: 'Though LLMs may have been trained on data from the original experiment, our setup with pairwise decisions, extensive shuffling, and prompt adaptations ensure ... do not help it cheat'; p.10: 讨论 prompt sensitivity、sampling bias 与抽象情境局限；p.20: temperature ablation。 | 识别了训练数据污染、位置/情境偏差与提示敏感性等潜在混淆，并用 shuffling、提示变体和温度消融作控制/敏感性讨论，局限部分说明残余威胁。 |
| A5 | 调节变量 | NA | — | 论文没有提出或检验调节假设；模型能力与提示类型差异只作描述性比较，不构成正式调节设计。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.17-18 Tables 5-6 给出 forward modeling 的完整 prompt 模板；p.25-26 Tables 16-17 给出 inverse modeling prompt；p.8 描述 rule-based 解析、失败重问与 pairwise wins 聚合。 | 关键操纵（提示模板）与因变量（解析规则、排序聚合）均写出可重复执行的操作化程序。 |
| A8 | 水平数与类型 | 0.5 | p.4: 三个任务与五个模型；p.8: positive/negative 两个情境及 zero-shot/CoT；p.20: temperature 取 0.0, 0.5, 1.0, 1.5, 2.0 的消融。 | 各水平标签基本清楚，但未系统说明水平类型、间距/全距及连续温度变量是否中心化/标准化。 |
| A9 | 单一操作化的风险 | 1 | p.5: 'results were similar across the three tasks'; p.8-9: 两种情境与多个模型；p.10: 局限中讨论抽象、受控情境的推广边界。 | 关键构念用多种任务、情境、模型和指标操作化，并报告跨操作的一致模式；同时讨论单一情境/抽象任务的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 研究不是自陈式同源测量；LLM 行为输出与外部人类数据集及理性模型比较，共同方法偏差框架不适用于该设计。 |
| B1 | 被试间设计 | NA | — | 无人类被试组分配；不同 LLM 是固定系统比较对象，不是承担单一条件的独立被试组。 |
| B2 | 被试内设计 | NA | — | 同一模型虽在多个提示/任务下被评估，但每次 API 调用独立、无跨条件 session 顺序或人类被试内顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合设计及对应误差项。 |
| B4 | 因子设计 | NA | — | 研究是模型×提示×任务/情境的基准网格，但未按因子实验报告设计矩阵、每格样本量或 ANOVA 交互统计。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无正式交互项检验与简单主效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或被试内顺序平衡。 |
| B9 | 准实验设计 | NA | — | 非准实验设计；无不可随机分配的人类处理组比较。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理及可逆性/迁移对称性适用条件。 |
| C1 | 随机化 | NA | — | 没有将人类被试或模型单位随机分配到互斥条件；prompt 条件固定，选项 shuffling 属于刺激顺序控制（见 E1），不是处理分配随机化。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件顺序或顺序组分配。 |
| C3 | 恒定 | 1 | p.4: 列出 Llama-3-8B、Llama-3-70B、Claude 3 Opus、GPT-4-Turbo (0125-preview)、GPT-4o 并说明 temperature；p.8: 'temperature = 1 across all models' 及实验日期；p.10: 讨论受控/抽象情境的外部效度限制。 | 明确列出模型版本、温度、数据集与提示模板等恒定条件，并在局限中讨论外部效度。 |
| C4 | 匹配 | NA | — | 未使用匹配程序，无匹配变量或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未使用区组或 ANCOVA 式协变量纳入；对偏差主要作提示/顺序消融与定性讨论。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类被试/主试/评分者盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 调用相互独立，无跨试次上下文学习或练习阶段。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每条件独立提示、无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为选择/排序相关，不使用被试内绝对量表评分，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.4: 'To minimize any positional biases ... we shuffled the order of the options'; p.8: 'shuffled ... order that decisions appear in the pair, ... options within decisions, ... items within each option'. | 报告了随机化/打乱位置，但未说明随机化方案、各位置出现次数或种子细节。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分题与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试可推断研究假设并产生需求特征的问题。 |
| E5 | 实验者效应 | NA | — | 无人类主试/评分者，完全自动化数据采集。 |
| E6 | 天花板 / 地板效应 | NA | — | 主要因变量是相关/MSE/排序相关，不是有端点截断的任务正确率；经典天花板/地板效应不适用于该指标。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；LLM 输出与人类数据/理性模型比较，不涉及共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | p.5 Tables 1-2 与 p.9 Table 4 报告 Spearman/Pearson 相关与 MSE；p.4 使用 9,831 个问题；p.8 样本量 43/42。未见 95% CI、功效分析或多重性校正。 | 报告了效应量（相关、MSE）与样本量，但缺置信区间、事前功效依据和多重比较校正说明。 |
| F2 | 内部效度 | NA | — | 非随机化人类实验，无被试流向、损耗或分配隐藏；研究为 LLM 基准比较，不作随机分配因果推断。 |
| F3 | 构念效度 | 0.5 | p.5-9 Tables 1-4 将 LLM 输出与人类数据和理性模型比较，可视为构念/效标关联证据；p.8 报告解析与聚合；但无内部一致性、评分者信度或 manipulation check。 | 提供了与外部人类数据和理论模型比较的效度证据，但缺传统信度与操纵检验，构念效度报告不完整。 |
| F4 | 外部效度 | 0.5 | p.4: choices13k 数据集及 9,831 问题子集；p.8: Jern et al. (2017) 的 47 个决策及正/负情境；p.10: 讨论抽象受控情境、人类数据采样偏差与推广边界。 | 报告了数据来源与模型集合，并讨论推广边界；但没有代表性抽样或跨独立样本复现，外部效度证据有限。 |
| G1 | 分析单位 | 0.5 | p.4: 'Each completion involved predicting or simulating a single human participant’s decision'; p.5: correlations computed across proportions; p.8: 43/42 samples each make 47 choose-2 comparisons. | 说明了输出在问题/成对比较层面聚合并分析，但未显式处理 completion 嵌套于问题、问题嵌套于数据集的层级结构。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；模型是固定比较对象而非抽样被试，无需被试随机效应；材料/项目推广问题在 G3 讨论。 |
| G3 | 材料作为随机效应 | 0.5 | p.10: 'subset ... carefully selected to be representative ... could be expanded'; p.7: 47 decisions 被描述为覆盖主要决策结构；但分析未加入 item 随机效应或准 F 比。 | 承认所用问题/决策集有限且可扩展，但分析未把材料作为随机效应建模，不能正式推广到任意材料总体。 |
| G4 | 统计功效 | 0.5 | p.4: zero-shot n completions 等于 choices13k 参与者数；p.8: inverse 样本量 43/42 等于原人类实验，Claude 3 Opus 因成本设为 5；结果报告相关/MSE。无功效分析。 | 样本量有实际依据（匹配人类样本、成本限制），并报告效应量；但无事前功效分析或置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.4: 分析子集为 9,831 个非 ambiguous/有反馈问题；p.8: 报告 43/42 与 Claude 5 的样本量；p.17-27 附录列出任务与模板。未明确区分验证性与探索性分析。 | 报告了主要排除规则、样本量选择和大部分因变量/条件；但未系统说明所有分析的事前/探索性质。 |
| G6 | 预先设定 / 预注册 | 0 | p.4-10 方法与局限未见预注册平台、注册编号或时间戳，也无预注册分析计划。 | 无公开预注册；按编码口径记 0，而非 NR。 |
| J1 | 位置偏差 | 0.5 | p.4: 'To minimize any positional biases ... we shuffled the order of the options'; p.8: 打乱 decision pair 顺序、选项内项目顺序；p.4 报告模型版本与采样温度。未报告翻转率或位置×正确率曲线。 | 采取了位置反平衡/打乱并报告模型版本，但未量化位置偏差（交换前后偏好翻转率或各位置正确率）。 |
| J2 | 冗长偏差 | NA | — | 不涉及 LLM-as-judge 评估开放式生成长短或质量。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或纠错式多轮对话，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 作为裁判评估模型输出。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本（zero-shot）或 CoT 提示，不使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.17-18 Tables 5-6 与 p.25-26 Tables 16-17 给出提示模板；p.10 讨论 prompt sensitivity；p.20-21 报告温度、人口学与 monkey 消融。未见 prompt 版本号、迭代日期或 dev/test 划分。 | 提供了模板并做若干提示变体消融，但缺版本化、完整敏感性消融与训练/测试分离说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文或 RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.4: 'temperature set to 0.7'; p.5: CoT/proportion 任务 '1 completion with temperature 0.0'; p.8: 'temperature = 1 across all models'；p.4/p.8 给出模型版本和实验日期。未报告 top-p/top-k、随机种子或 bootstrap CI。 | 报告了主要温度与重复样本量，但采样超参、种子和方差估计不完整。 |
| J9 | 重复与文本退化 | 0.5 | p.4: 'responses were completely deterministic at temperature 0.7 ... thus prompted for 1 completion with temperature 0.0'; p.8: 输出限制为 {stronger, weaker, tie} 并用 rule-based classifier 解析。未报告 repetition penalty 或退化率。 | 报告了温度/确定性处理与短结构化输出，但未报告解码策略细节、重复惩罚和退化率；因任务输出较短，风险有限。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本实验，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.8: 'Though LLMs may have been trained on data from the original experiment, our setup ... ensure ... do not help it cheat'; p.8 报告模型实验日期为 2024 年 4/5 月，使用公开 choices13k 与 Jern 数据。未做 n-gram/DCQ 污染检测或报告训练截止日期。 | 识别并论证了潜在训练数据重叠，但无正式污染检测率和训练截止日期对照。 |
| J12 | 基准饱和 | 0.5 | p.9 Table 4 报告 Spearman 相关（如 GPT-4o CoT 与人类 0.97、与 rational model 0.95/0.94），采用连续相关指标；未讨论接近上限问题或报告 bootstrap CI。 | 使用连续指标而非仅准确率，且报告了当前分数水平；但高相关接近上限时未作饱和讨论或 CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，无约束指令遵循评估。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.17: distribution 任务要求 'json format'；p.6: 'GPT-4 Turbo could not provide a valid output ranking 47 choices at once'；p.8: 用 handmade rule-based classifier 解析，CoT 失败时 re-prompt。未报告格式合法率。 | 报告了输出格式约束、解析与重试策略，但未将格式失败率与内容错误分离报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 1 | p.1 摘要: 'implicit internal models of human decision-making in LLMs'; 'comparing LLM behavior and predictions to a large dataset of human decisions'; p.3: 'inverse decision-making can be considered a specific form of Theory of Mind'; p.8: 使用 Jern et al. 人类数据；p.10 讨论外推限制；p.4/p.8 报告模型版本与日期。 | 论文明确把 LLM 输出定位为隐含的人类决策模型/认知构念，与人类同名构念作同范式比较，并把模型作为固定系统比较而非被试样本；也讨论了外推边界。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨规模/训练进展的能力曲线或涌现能力宣称；仅有模型间描述性比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 纯评估研究，不涉及对代理指标的训练/RL/best-of-N 优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.8: inverse 样本量 43/42；p.4: forward 的 n completions 及模型版本；p.8: 实验日期 2024 年 4/5 月。未报告每个分数的 95% CI、配对检验或原始推理日志。 | 报告了重复次数与部分 snapshot/日期信息，但缺置信区间、精确 snapshot 和配对比较，可复现性报告不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮，无对话历史累积或多轮一致性评估。 |

## 编码小结
论文对 LLM 的提示条件、任务变体、模型版本与主要相关指标报告较清楚，操作化与 prompt 模板也较可复现；但统计推断以点估计相关/MSE 为主，缺少置信区间、功效分析、项目/模型随机效应建模与正式污染检测；部分位置/格式控制和消融有报告但不够系统。总体适合作为 LLM 行为基准比较来编码，许多人类实验特有的分配、盲法、疲劳、需求特征等组件不适用。
