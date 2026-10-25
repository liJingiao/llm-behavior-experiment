# article_032 | Evaluating Cognitive Maps and Planning in Large Language Models with CogEval | 2023

研究类型概述：系统基准/行为评测：研究者构造6种图结构×3个域×15类任务条件×3个温度，对8–9个LLM进行重复提示评测，并用逻辑回归比较规划表现；无人类被试、无人类基线。分析单位为各模型/提示组合下的生成响应与成功/失败计数。
- **研究构念（Construct）**：认知地图与空间/图结构规划（cognitive maps and planning）｜CA 构念锚定：计划（planning, `trm_4a3fd79d0acc1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：系统基准/行为评测：研究者构造6种图结构×3个域×15类任务条件×3个温度，对8–9个LLM进行重复提示评测，并用逻辑回归比较规划表现；无人类被试、无人类基线。分析单位为各模型/提示组合下的生成响应与成功/失败计数。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4 (p.4): 'created with 3 factors of graph structure (6 graphs), domain (3 domains), and tasks (15 tasks) over 3 temperatures (0, 0.5, 1)'; p.4: '30 times for OpenAI models ... and once for the remaining models'. | 明确命名并给出多个因子与水平，含温度操纵和重复采样；但未报告操纵检验，分配/重复逻辑也仅部分说明，模型差异更接近观察性比较。 |
| A2 | 因变量 | 0.5 | p.8 (p.8): Table 2 caption 'number of successes out of max possible successes in dialog'; Table 3 'Mean and standard errors for planning performance across all task conditions'. | 因变量指标和成功/失败计分基本明确，但未报告评分者信度、效度、连续指标预处理、天花板/地板处理细节。 |
| A3 | 控制变量 | 0.5 | p.4 (p.4): 'we implemented measures to mitigate such effects ... prompt, temperature, experimental conditions ... domain ... graph'; p.5: 'included model version and temperature as separate independent variables'. | 提到了多个控制因素及其纳入分析方式，但不是系统化控制变量清单，也未逐一说明恒定/平衡/协变量控制手段。 |
| A4 | 混淆变量 | 1 | p.2–3 (p.2–p.3): 'To prevent any possible contamination, we avoided BIG-bench ... and a planning benchmark for GPT-3'; p.10 (p.10): Limitations discuss unknown architecture/training and no human baseline. | 识别了训练集污染、任务/图结构/温度/模型架构等潜在混淆，并说明控制方式与残余威胁；虽无正式敏感性分析，但内部效度威胁讨论较完整。 |
| A5 | 调节变量 | NA | — | 理论模型不包含调节变量；文中虽有图×域×条件等交互检验，但属于因子设计交互，按设计矩阵在B6编码，不作为调节假设。 |
| A6 | 中介变量 | NA | — | 未提出中介假设，也未进行直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p.3 (p.3) Figure 1 gives an example task prompt; p.5 (p.5): 'All prompts are available in the supplementary material and on https://github.com/cogeval/cogmaps'; p.7 Table 1 lists task conditions. | 对规划/认知地图通过具体任务提示和成功标准进行了操作化，并给出示例与材料链接；但正文未完整给出所有提示、评分细节和逐构念操作流程。 |
| A8 | 水平数与类型 | 0.5 | p.4 (p.4): '3 factors of graph structure (6 graphs), domain (3 domains), and tasks (15 tasks) ... 3 temperatures'; p.7 (p.7) Table 1 lists 15 condition labels. | 报告了因子及水平标签；但未完整说明水平类型、间距/全距和连续变量中心化，且域数量/标签在p.2与p.4之间略有不一致。 |
| A9 | 单一操作化的风险 | 0.5 | p.4 (p.4): 'multiple tasks and multiple response generations'; p.2 (p.2): operationalized latent ability 'with a number of tasks'. | 关键构念采用多任务、多图、多域操作化，但未报告各操作化之间的正式会聚证据或会聚统计。 |
| A10 | 单一方法的风险 | NA | — | 自变量是外部构造的任务提示/图结构，因变量是模型回答的客观正确性；不是同源自陈式测量，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试的区组/条件分配；同一模型接受多个任务提示，API调用之间也无被试间随机分配，故人类被试间设计不适用。 |
| B2 | 被试内设计 | NA | — | 虽有重复生成，但每次API调用独立，无人类被试内顺序呈现及顺序平衡设计。 |
| B3 | 混合设计 | NA | — | 没有人类被试组间/组内混合因素设计，也未按两类误差项分析。 |
| B4 | 因子设计 | 0.5 | p.4 (p.4): factors graph structure, domain, tasks, temperature; p.6 (p.6): significant graph×domain, graph×condition, domain×condition, and three-way interactions. | 因素水平交叉并报告了交互检验（逻辑回归χ²）；但未给出完整设计矩阵、每格样本量和ANOVA式效应量/自由度表。 |
| B5 | 主效应 | 0.5 | p.6 (p.6): 'LLM (χ2 ...), graph ..., condition ..., and domain ... each yielded significant chi-squared statistics'; p.8 Table 2 reports chi-square, df, p. | 报告了各主效应统计量，但缺效应量与置信区间；交互显著时也未明确声明主效应解释受限。 |
| B6 | 交互作用 | 0.5 | p.6 (p.6): 'graph-domain ... graph-condition ... domain-condition ... graph-domain-condition ... all significant'; p.7 Figure 2 shows means with standard errors but not interaction simple effects. | 报告了交互项χ²和p，但未进行简单主效应/多重比较校正；交互图不是针对交互的误差棒图。 |
| B7 | 区组设计 | NA | — | 没有使用区组或分层随机设计，也无区组变量及区内分配程序。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方或需要被试内顺序平衡的实验设计。 |
| B9 | 准实验设计 | NA | — | 不是非随机分组的准实验因果研究；研究为LLM基准评测，无人类处理分配。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理序列，不涉及处理可逆性或迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有把独立单位随机分配到互斥条件；所有模型/提示组合按计划直接评测，无随机化或分配隐藏。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，故无顺序平衡方案可报告。 |
| C3 | 恒定 | 0.5 | p.4 (p.4): lists LLMs and APIs; p.4: temperatures '0, 0.5, and 1'; p.5: prompts available online. | 报告了模型/API与温度设置，并保持部分提示材料固定；但未系统列出所有恒定变量及其水平，也未充分讨论由此造成的外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对设计。 |
| C5 | 纳入为变量 | 0.5 | p.5 (p.5): 'included model version and temperature as separate independent variables that account for technical variation'; p.6 reports LLM×temperature interaction. | 将模型版本和温度作为回归模型中的独立变量处理；但未检验协变量斜率齐性、未报告调整后效应量。 |
| C6 | 盲法 | NA | — | 数据采集主要经由API自动完成，无人类被试或人类评分者的盲法安排可报告。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序效应，故不涉及完全平衡/拉丁方/ABBA层级选择。 |
| D1 | 练习效应 | NA | — | 各次生成为独立API调用，无上下文内练习或学习累计，练习效应不适用。 |
| D2 | 疲劳效应 | NA | — | 无人类session时长、疲劳或休息安排；LLM调用不受人类疲劳机制影响。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每次生成独立重置上下文，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或不对称迁移风险。 |
| D5 | 范围效应 | NA | — | 因变量为任务成功/失败，不是主观量表评分，无范围效应或量表锚定问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无人类被试内刺激序列，也无明确的多选项列表顺序操纵；LLM候选位置偏差在J1单独编码。 |
| E2 | 默认赞同 | NA | — | 未使用Likert或态度自评量表，无默认赞同/反向计分问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 未使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在人类需求特征或事后假设推断访谈。 |
| E5 | 实验者效应 | NA | — | 完全通过API自动采集，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.8 (p.8) Table 3 reports means and standard errors; e.g., nonteleShortcutCoT shows '1.00, 0.00' for gpt-4 and gpt-35. | 报告了均值/SE并可见若干端点值（1.00或0.00），但未系统报告偏度、端点频率或pilot难度校准，也未讨论天花板/地板对区分度的影响。 |
| E7 | 共同方法偏差 | NA | — | 自变量为外部任务操纵，因变量为客观正确性；不同源自评构念，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.6 (p.6) reports χ², df and p values; p.8 Table 3 reports means/SE but no effect sizes/95% CI; p.4 does not report power analysis. | 仅报告χ²和p，未报告标准化效应量或置信区间，也无样本量功效依据和多重性校正说明；未达到基本要件。 |
| F2 | 内部效度 | NA | — | 无人类随机分配、分配隐藏、被试流向或损耗；研究不是因果干预实验，内部效度随机化框架不适用；污染等威胁已在A4讨论。 |
| F3 | 构念效度 | 0.5 | p.4 (p.4): 'operationalize planning ability by generating unique variations of established experimental tasks'; p.2: human experiments 'offer both established construct validity'. | 借助既有人类任务和多任务操作化提供一定构念效度依据；但未报告测量信度、评分者信度或操纵检验，也未系统论证LLM构念与人类构念的对应。 |
| F4 | 外部效度 | 0.5 | p.4 (p.4) lists LLMs and APIs; p.10 (p.10): 'we do not have a human baseline' and discusses application caution. | 报告了模型样本来源与任务范围，并讨论应用边界；但无跨情境复现或人类基线，外部效度证据有限。 |
| G1 | 分析单位 | 0.5 | p.5 (p.5): 'we fit a logistic regression analysis ... We made sure that each combination ... had several replicates'; p.8 Table 2 counts successes 'in dialog'. | 说明了分析使用生成成功/失败并在组合内有重复，但未明确分配层级与统计层级的匹配，也未对生成嵌套于提示/模型的聚集结构建模。 |
| G2 | 随机效应 | 0 | p.5 (p.5): logistic regression with domain, condition, graph, model version and temperature as regressors; no random effects reported. | 重复生成嵌套于提示/模型，且研究对更广LLM/任务总体作概括；但模型完全按固定效应处理，未报告随机截距/斜率或可推广总体。应报告随机效应而未报告。 |
| G3 | 材料作为随机效应 | 0 | p.4 (p.4) uses six specific graphs and fixed task prompts; p.5 logistic regression treats graph/condition as fixed categorical regressors. | 有限图结构/任务材料被当作固定刺激，未将材料/项目作为随机效应纳入分析；对任意图结构或任务的推广缺少统计基础。 |
| G4 | 统计功效 | 0 | p.4 (p.4): 30 generations for OpenAI and once for others 'for which we had API access'; no a priori power analysis; p.6 only χ²/p. | 无设计阶段功效分析或样本量依据，也未报告效应量与置信区间；重复次数由API访问决定而非功效推导。 |
| G5 | 研究者自由度 | 0.5 | p.4 (p.4): 30 repeats for OpenAI, once for others; p.7 Table 1 and p.8 Table 3 list many/all task conditions; no exclusion rules or exploratory/confirmatory distinction reported. | 报告了重复次数决定方式和较完整的任务条件，但未报告试次/提示排除规则，也未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.4–5 (p.4–p.5) methods and全文未见预注册平台、注册编号或分析计划；无验证性/探索性偏离说明。 | 没有公开预注册或时间戳早于数据收集的分析计划，按规则记0。 |
| J1 | 位置偏差 | 0 | p.5 (p.5) example prompt fixes candidate order: 'From the lobby you have two choices, room 1 and room 2'; no position counterbalancing or flip-rate report. | LLM需要在房间/路径中做选择，但未报告候选位置随机化/反平衡、交换顺序重判或位置×正确率分析。 |
| J2 | 冗长偏差 | NA | — | 不使用LLM裁判评估开放生成质量；答案是房间/路径选择，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话操纵，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 不使用LLM-as-judge或成对模型输出评估，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实际任务提示为零样本直接提问；未使用few-shot in-context示例，示例选择/排列偏差不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5 (p.5): 'All prompts are available in the supplementary material and on https://github.com/cogeval/cogmaps'; p.3 Figure 1 gives an example prompt. | 提供了提示示例和材料链接，但正文未给出版本号、迭代日期、语义等价敏感性消融或dev/test划分；无法排除提示工程自由度。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务提示为短图/房间描述，远低于长上下文窗口，也无RAG或关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.4 (p.4): temperatures '0, 0.5, and 1'; '30 times for OpenAI ... once for the remaining models'; p.5 notes temperature 0 is not entirely deterministic. | 报告了温度和重复次数；但未报告top-p/top-k、随机种子、每条件均值与95%CI，闭源模型也缺精确snapshot日期。 |
| J9 | 重复与文本退化 | 0.5 | p.4 (p.4) discusses temperature 0 as deterministic/greedy vs higher-temperature diversity; p.6 failure modes include loops and longer trajectories. | 部分说明了解码/温度策略，但未报告repetition penalty、n-gram重复率/退化率等QC指标，也未将解码策略作为受控变量系统比较。 |
| J10 | 分词效应 | NA | — | 单语言英文任务，无跨语言/跨脚本比较，分词长度控制不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.2–3 (p.2–p.3): 'To prevent any possible contamination, we avoided BIG-bench ... and a planning benchmark for GPT-3'; p.5: novel prompts and GPT-4 failed to recall figure details. | 明确识别污染风险并采用新提示规避已知污染；但未报告训练截止日期、n-gram重叠/DCQ等正式污染检测率。 |
| J12 | 基准饱和 | NA | — | 使用新构造任务而非既有公开基准，也未在SOTA提升语境中解释分数；虽然个别条件出现1.00，但整体并非饱和基准评估。 |
| J13 | 指令遵循 | NA | — | 因变量是规划正确性，不是指令遵循；无按约束类型拆分的指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 输出为自由文本房间选择，不要求JSON/结构化输出，也无格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2 (p.2): 'our goal is not a comparison with human performance nor any assumptions of LLMs being human-like'; p.4 operationalizes cognitive maps/planning functionally. | 明确讨论功能主义、多重可实现性，并避免直接把人类结论套到LLM；但无人类同范式基线，模型权重快照信息不精确。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随模型规模/训练进展的能力曲线；模型间比较不是受控scaling curve，也未用该曲线声称涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N或对代理指标的优化环节，代理指标过优化不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4 (p.4): '30 times for OpenAI ... once for remaining models'; model labels include GPT-4-*, GPT-3.5-turbo-175B, davinci-003, Bard-*, etc.; p.8 Table 3 means/SE but no CI/paired tests. | 报告了重复次数和部分模型版本，但snapshot/日期不精确，缺bootstrap CI与配对检验，原始日志/逐题结果也未在正文完整提供。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 任务为单轮提示-回答评测，没有对话历史累积或多轮一致性评估。 |

## 编码小结
这是一项LLM认知能力基准评测而非人类被试实验，故大量人类实验设计组件不适用。论文对因子结构、重复生成、部分温度和模型信息有报告，也讨论了污染与构念效度；但缺少操纵检验、信效度、效应量与CI、随机效应/聚类处理、精确快照、prompt敏感性消融等关键报告。
