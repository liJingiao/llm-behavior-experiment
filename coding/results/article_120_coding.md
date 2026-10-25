# article_120 | Episodic Memories Generation and Evaluation Benchmark for Large Language Models | 2025

研究类型概述：本文属于LLM基准构建与评估研究：作者用LLM生成受控的合成叙事书（事件、时间、空间、实体、内容与问答），再在in-context、RAG和fine-tuning等记忆配置下评测多个LLM，并用LLM-as-a-judge计算F1与Kendall τ。没有人类被试；主要分析单位是问题/回答，比较不同模型与记忆配置在问题分层（匹配事件数、cue/trace类型、书长等）上的表现。
- **研究构念（Construct）**：情景记忆中的线索依赖回忆、熟悉性监控、跨事件整合与干扰｜CA 构念锚定：情景记忆（episodic memory, `trm_4a3fd79d0a1f4`）；回忆（recall, `trm_4a3fd79d0b95b`）；记忆提取（memory retrieval, `trm_4a3fd79d0ba01`）
- **实验任务与范式（Task / Paradigm）**：仅依据现成模型的in-context与RAG单元：向模型提供含时间、地点、人物和事件变化的长篇经历，再用不同线索、匹配事件数和单/多事件问题测试回忆。排除作者的微调条件。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p8：'We evaluate several LLMs ... under different configurations: in-context learning, retrieval-augmented generation and fine-tuning'；p8方法段报告in-context前插全文、RAG分段落检索、fine-tuning设30 epochs/batch 64。 | 自变量（记忆配置/模型）被命名并有至少两个水平，操纵程序部分报告；但无传统操纵检验，分配方式也不适用于被试，故0.5。 |
| A2 | 因变量 | 0.5 | p7：'LLM-as-a-judge ... compute an optimistic F1-score ... Kendall’s τ'；p9 Table 3报告F1均值±SD。 | 因变量指标与计分方式明确，但缺评分信度/效度证据与连续指标预处理/端点效应说明。 |
| A3 | 控制变量 | 0.5 | p6：'event meta-data ... number of paragraphs and positions of key information'；p22：'additional seed parameter is used for reproducibility'；p31：每id/bin选Ntarget=5。 | 报告了若干控制手段（元数据定位、固定seed、问题配额），但未系统列出全部恒定变量与控制手段。 |
| A4 | 混淆变量 | 0.5 | p3列出data leakage/shortcuts等威胁；p43做ordered vs unordered与realistic vs non-realistic消融；p48扩展world news/sci-fi。 | 识别并部分控制潜在混淆（污染、时间顺序、真实性），但未系统量化残余混淆或做敏感性分析。 |
| A5 | 调节变量 | NA | — | 全文未提出调节假设、乘积项交互检验或简单斜率分析；按规则NA。 |
| A6 | 中介变量 | NA | — | 全文无中介变量与直接/间接效应分解；按规则NA。 |
| A7 | 操作性定义 | 1 | p4-5：事件元组(t,s,ent,c)、cue(*,s,*,*)与trace类型；p23-25 Listing 7章节生成prompt；p32 F1计分规则。 | 关键构念均有可重复执行的操作化：事件生成、cue/trace模板、QA生成、LLM judge与F1计算。 |
| A8 | 水平数与类型 | 0.5 | p7 Table 2给short/long与QA bin数量；p8列出6模型与3类memory；p31 Table 12给cue/bin水平。 | 报告了水平数与取值/标签，但水平类型、间距/全距及连续变量处理未系统说明。 |
| A9 | 单一操作化的风险 | 0.5 | p4 Table 1与p30 Table 10列出多种cue/trace；p48多universe/benchmark；p10讨论explicit temporal markers等局限。 | 采用多种任务操作化并显示跨任务一致趋势，但未报告正式会聚效度检验。 |
| A10 | 单一方法的风险 | NA | — | 无人类自陈/同源量表设计；IV为模型/记忆配置，DV为QA指标，不属共同方法偏差框架。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配；模型/记忆配置不是被试间分组。 |
| B2 | 被试内设计 | NA | — | 无被试内条件顺序设计；各问题对模型独立调用，未设顺序平衡。 |
| B3 | 混合设计 | NA | — | 无混合设计及组间/组内因素区分。 |
| B4 | 因子设计 | 0.5 | p9 Table 3按model/memory × 事件数bin给出均值±SD；p9 Fig 4按cue type × 事件数分格；未见完整设计矩阵与ANOVA交互统计。 | 存在多因素分格报告，但不是完整因子设计，也缺交互统计量。 |
| B5 | 主效应 | 0.5 | p8 Fig 3用Wilcoxon signed-rank + Holm对模型/记忆组合总体排序；p9 Table 3按bin汇总。 | 有总体模型/记忆比较与显著性排序，但未报告主效应F/df/效应量，也未在交互显著时限定解释。 |
| B6 | 交互作用 | 0.5 | p9仅描述cue type与事件数的梯度，p43有序/无序消融用Mann-Whitney，但未对cue×bin或model×bin交互项作统计检验。 | 有交互式分格描述，但核心交互统计检验缺失，只能给0.5。 |
| B7 | 区组设计 | 0.5 | p31：'Ntarget=5 questions for each of the 36 question ids and for each of the 5 bins'；p31 Table 12报告各cue/bin选中数。 | 有按事件数分层的平衡抽样，但未说明区内随机分配或模型中的区组效应。 |
| B8 | 拉丁方 | NA | — | 无拉丁方或序贯条件顺序设计。 |
| B9 | 准实验设计 | NA | — | 无准实验分组与因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 无被试/试次随机分配；问题选择按固定配额而非概率分配。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需平衡。 |
| C3 | 恒定 | 0.5 | p23：'we used both Claude 3.5 Sonnet (2024-06-20) and GPT-4o... Only the book built from Claude...'；p8 RAG固定text-embedding-3-small；p22 fixed seed。 | 有若干恒定控制，但未给完整恒定清单与外部效度限制讨论。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p31按0/1/2/3-5/6+ bins配额选问；p9 Table 3分bin报告F1。 | 将匹配事件数作为分层/区组变量纳入描述分析，但未做ANCOVA/斜率齐性等协变量检验。 |
| C6 | 盲法 | NA | — | 无人类被试/主试/评分者盲法；LLM judge也不属于人类盲法安排。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级需说明。 |
| D1 | 练习效应 | NA | — | LLM每题独立调用，无上下文内跨试次练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类session疲劳或长时程休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立调用，无跨条件残留/清洗期设计。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为F1/τ等客观指标，不是主观量表范围效应问题；端点问题归E6。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p6 chapters concatenated；p43 ordered vs unordered ablation；p28 Fig 5报告cue在book/chapter/paragraph的相对位置。 | 分析了书/章/段内信息位置并有ordered vs unordered对比，但未随机化问题顺序或说明完整平衡方案。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或事后访谈；LLM提示不作为人类掩饰情节。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p9 Table 3、p39 Table 13报告F1均值±SD，短书多格接近1；未报告偏度/端点频率或pilot难度校准。 | 报告了均值与标准差可部分排查端点，但缺显式天花板/地板分析。 |
| E7 | 共同方法偏差 | NA | — | 无IV/DV同源自评；共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p8：'Wilcoxon signed-rank ... adjusted by Holm’s method'；p9 mean±SD；p46 Fig 8给出bootstrapped paired mean differences。 | 有样本量、配对检验与多重校正，但主分析缺效应量/95%CI与功效依据。 |
| F2 | 内部效度 | NA | — | 非随机实验、无人类因果分配；污染控制更属基准偏差而非F2的被试流向/分配隐藏。 |
| F3 | 构念效度 | 0.5 | p6与p24章节生成有exact verification + LLM-as-a-judge；p7多任务QA；未报告评分者信度/人类效标。 | 有内容与生成验证，但缺测量信度、人类构念效标或正式操纵检验。 |
| F4 | 外部效度 | 0.5 | p8列出6模型；p7 Table 2与p48 Table 28多书/多universe；p10讨论limited domain/explicit temporal markers。 | 报告了模型与基准来源并讨论边界，但缺精确抽样框、模型快照与跨人类样本复现。 |
| G1 | 分析单位 | 0.5 | p8以问题为单位比较模型并做Wilcoxon；p9 Table 3按问题bin汇总；未说明问题嵌套章节/书的层级或混合模型。 | 分析单位基本为问题，但未显式处理问题嵌套于章节/书及跨模型重复测量的聚集结构。 |
| G2 | 随机效应 | 0 | p8仅报告模型间Wilcoxon与均值，未报告任何随机效应；问题/章节被视为固定集合。 | 研究需推广到题目/章节总体，但模型未含随机截距/斜率，随机效应结构缺失。 |
| G3 | 材料作为随机效应 | 0.5 | p48生成11个benchmark/多universe；p8-9汇总仍以固定题集比较，无(1&#124;item)/(1&#124;book)或准F。 | 承认并扩展了多材料/多书，但分析未把材料/题目作为随机效应。 |
| G4 | 统计功效 | 0.5 | p31以评估成本为由每id/bin取Ntarget=5；p9报均值±SD；无事前功效分析/效应量CI。 | 有样本量选择理由但非功效分析，结果缺CI。 |
| G5 | 研究者自由度 | 0.5 | p27 Table 7报告生成失败与丢弃；p31报告问题过滤与配额；p48 Table 28列11 benchmark。 | 报告了部分排除/筛选规则，但未完整区分验证性与探索性分析或停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | 全文无预注册平台/编号或时间戳；无验证性与探索性分析区分。 | 按校准口径，未报告预注册记0，而不是NR。 |
| J1 | 位置偏差 | NA | — | 无多候选项选择、排序或成对LLM-judge位置比较。 |
| J2 | 冗长偏差 | 0.5 | p32：'#pred = min(#iditems, #gt)'以控制多余预测；p35 Listing 13展示冗长答案被截断；未报告长度-得分相关或judge rubric长度控制。 | 对答案冗长/多报有部分控制，但未直接识别LLM裁判的长度偏差。 |
| J3 | 谄媚 | NA | — | 无用户先验立场/反馈操纵；任务为闭卷QA。 |
| J4 | 自我偏好 | 0 | p7：'LLM-as-a-judge'用于语义匹配，但未说明裁判模型版本，也未报告与被评模型是否同源、匿名化或自我偏好率。 | LLM裁判风险实际存在，但核心同源/自我偏好报告缺失。 |
| J5 | 少样本示例选择与排列偏差 | NA | p36 Listings 15-17为zero-shot/整书in-context或fine-tune，无few-shot in-context示例。 | 按规则零样本/纯微调不适用J5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p23 Listing 7章节生成prompt；p32 Listing 12 judge prompt；p36-38 Listings 15-17回答prompt。 | 提供完整prompt模板，但无版本号/敏感性消融/dev-test划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p7报告10k/100k tokens；p28 Fig 5报告cue在book/chapter/paragraph的位置分布；未报告位置×正确率曲线或位置反平衡。 | 长上下文实际token数与位置分布有报告，但关键信息首/中/尾操纵及U形曲线缺失。 |
| J8 | 温度与采样随机性 | 0 | p8仅说明模型与fine-tuning超参；未报告temperature/top-p/seed或重复采样N/CI。 | LLM采样随机性未被纳入统计设计。 |
| J9 | 重复与文本退化 | 0 | p46 Appendix F报告Claude 3.5产生342/685次spurious长重复文本；未报告解码策略/repetition penalty/条件间解码恒定。 | 报告了退化现象但未报告或控制解码策略，不能排除退化与模型能力混淆。 |
| J10 | 分词效应 | NA | — | 英文单语言/单脚本，无跨语言或跨格式比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p1：'synthesize a unique episodic memory benchmark, free from contamination'；p3讨论data leakage；未报告训练截止日期对照或n-gram/DCQ污染检测。 | 设计上宣称污染free并公开数据，但无正式污染率检查。 |
| J12 | 基准饱和 | 0.5 | p9短书多数高分、长书多事件格仍低；p7 Table 2给规模；未明确讨论饱和/改用连续指标或CI。 | 报告了分数量程与SOTA水位，并使用了更难长书，但饱和分析和CI不足。 |
| J13 | 指令遵循 | NA | — | 不测量指令遵循，因变量为QA F1/Kendall τ。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p24-25章节验证要求JSON；p32 judge要求JSON。未报告格式合法率/重试策略或格式失败与内容错误分开。 | 结构化输出设置存在，但格式合法率等关键QC缺失。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1-3用认知科学episodic memory定义并引AMI/Autobiographical Interview；p10讨论局限；未做人类同范式对照或系统构念效度检验。 | 明确把LLM输出解释为情景记忆能力并讨论人类对应，但缺人类对照与系统构念效度论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨规模/训练进展能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无对benchmark/奖励代理的优化循环；fine-tuning仅作记忆基线而非代理指标优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p8列出模型名；p8 Wilcoxon/Holm配对比较；p48发布code/data。未给精确snapshot/API日期、重复采样N、95%CI或逐题日志。 | 有一定可复现资源与配对检验，但种子/检查点依赖与区间估计报告不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | p36 Listing 15为单轮question；无多轮对话评估。 | 实验严格单轮，不主张多轮部署一致性。 |

## 编码小结
该文在基准生成、事件元数据控制、污染规避与多任务操作性定义上较完整，并公开数据/代码；但对LLM评估方法学报告不够充分：缺乏解码采样参数、重复采样与置信区间、精确模型snapshot、LLM裁判的同源/长度偏差控制、题目/章节随机效应或嵌套建模，提示敏感性与预注册也基本缺失。因此多数设计与偏差识别项只能给0.5，若干纯人类被试或序贯设计项判NA。
