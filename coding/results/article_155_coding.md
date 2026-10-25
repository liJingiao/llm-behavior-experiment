# article_155 | Minerva: A Programmable Memory Test Benchmark for Language Models | 2025

研究类型概述：该文提出并评估一个可编程的 LLM 记忆/上下文使用能力基准。研究单位为 9 个具体语言模型在 1110 个自动生成测试样本上的输出；主要设计是模型 × 任务类别/任务参数 × 测试样本的基准评测，而非人类被试实验。因变量为 exact match、ROUGE-L 与 Jaccard 等自动指标，另含上下文长度和提示措辞的扩展比较。
- **研究构念（Construct）**：上下文记忆的检索、回忆、编辑、结构组织、状态维持与复合操作能力｜CA 构念锚定：回忆（recall, `trm_4a3fd79d0b95b`）；记忆提取（memory retrieval, `trm_4a3fd79d0ba01`）；长时记忆（long-term memory, `trm_4a3fd79d0a833`）
- **实验任务与范式（Task / Paradigm）**：用参数化程序随机生成1110个文本记忆测试，让九种现成模型完成搜索、回忆编辑、集合与列表操作、状态跟踪及复合数据块任务。（操纵记忆操作类型、查询难度、上下文长度、正负样本、操作步数以及原子任务与复合任务。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_2: 'We design multiple atomic tests...'; PDF_PAGE_3: 'fixed snapshot of 1110 randomly generated test samples... context length to 4k tokens'. | 研究通过任务类别、任务超参数、上下文长度和提示变体形成比较条件，至少有任务/参数水平；但未报告传统操纵检验，且各模型均接受同一套条件而非随机分配，故为部分满足。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_3: 'exact match accuracy... ROUGE-L... Jaccard similarity'; PDF_PAGE_18: 给出 Exact Match、ROUGE-L-recall 与 Jaccard 公式。 | 因变量指标和计分方式明确，但未报告测量信度、效标/构念效度证据，也未系统说明连续指标预处理或天花板/地板效应处理。 |
| A3 | 控制变量 | 1 | PDF_PAGE_3: 'fixed the context length to 4k tokens'; 'max output token to 4096, temperature to 0, and top p to 1'; PDF_PAGE_9 讨论主要聚焦短上下文。 | 明确列出若干关键恒定控制及其水平（上下文长度、最大输出、temperature、top-p），并在讨论中说明短上下文设定的外部效度限制。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_7: 'GPT-4 model outperformed GPT-4o... optimization trade-offs'; PDF_PAGE_8: prompt variation 比较；PDF_PAGE_5: gibberish context ablation。 | 识别并部分控制了提示措辞、语义干扰、模型架构/训练差异等潜在混淆，但未系统报告残余混淆或敏感性分析对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量假设，也没有对调节变量做交互检验；模型/任务差异属于比较条件而非理论调节模型。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解设计。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_4 Table 1 给出每类任务定义；PDF_PAGE_12-16 Appendix A 给出完整 prompt 模板；PDF_PAGE_18 给出指标公式。 | 各任务的操作化程序、输入模板、可配置超参数与评分指标均较完整，可据此复现。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_16-17 Table 10: 列出 query depth、sequence length、batch size、repetition、number of groups 等水平与样本数。 | 报告了各任务超参数的水平数与具体取值，但未系统说明水平类型、间距/全距及连续变量中心化/标准化。 |
| A9 | 单一操作化的风险 | 0.5 | PDF_PAGE_2: 'We design multiple atomic tests...'; PDF_PAGE_4 Table 1 将同一记忆能力拆为多个测试。 | 关键构念采用多个任务/指标操作化，但未报告各操作之间的会聚证据，也未系统讨论单一操作化的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 自变量为任务/提示条件，因变量为模型在客观任务上的自动评分；不存在人类自陈式同源测量意义上的共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配；研究比较的是固定的一组 LLM，而非被试间条件分配。 |
| B2 | 被试内设计 | NA | — | 同一模型虽评估多个任务，但每个 prompt/测试样本为独立调用，无被试内条件顺序平衡或随机化设计。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内混合设计及相应误差项。 |
| B4 | 因子设计 | NA | — | 研究不是因子实验设计；模型 × 任务的结果以描述性表格/图呈现，未做完整设计矩阵与交互统计。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 无准实验分组或因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理顺序设计，故不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 测试样本由程序随机生成，但模型/条件没有随机分配与分配隐藏机制；对 LLM 基准而言分配问题不适用。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序或跨条件平衡方案。 |
| C3 | 恒定 | 1 | PDF_PAGE_3: 'context length to 4k tokens'; 'temperature to 0, and top p to 1'; 'max output token to 4096'。 | 关键运行条件被恒定并给出具体水平，且在讨论中承认短上下文设置限制。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为协变量或区组纳入统计模型。 |
| C6 | 盲法 | NA | — | 全自动评分，无人类被试、主试或评分者盲法需求。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级。 |
| D1 | 练习效应 | NA | — | 每个测试 prompt 独立调用模型，无上下文内学习或练习阶段。 |
| D2 | 疲劳效应 | NA | — | 无人类 session、休息或疲劳累积设计；LLM 调用为独立推理。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立 API/推理调用，无跨条件延滞或残留迁移。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为 exact match、ROUGE-L、Jaccard 等客观指标，无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选项顺序或被试内处理顺序；query depth 与上下文位置是任务生成参数，非选项/刺激呈现顺序平衡问题。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert 或态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 不存在人类被试需求特征；LLM 不会被 cover story 影响。 |
| E5 | 实验者效应 | NA | — | 数据采集与评分完全自动化，无人类实验者/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0 | PDF_PAGE_3-7 表 2-6 主要给出准确率/相似度点估计；未见 SD、偏度或端点频率统计。 | 存在明显端点堆积（如多个 1.00 与 0.0），但论文未报告分布形态或端点频率，也未系统讨论天花板/地板对内部效度的损害。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念测量，不涉及共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_9 与 PDF_PAGE_19 的 prompt variation 表报告 95% CI；PDF_PAGE_3 报告 1110 样本快照。 | 部分比较报告了置信区间，但多数主结果仅有准确率点估计；无功效分析、无系统效应量、无多重性校正说明。 |
| F2 | 内部效度 | NA | — | 研究为基准评测，非随机分配实验，也不作因果推断。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_1-2 强调 atomic tests 隔离记忆能力并避免 reasoning 混淆；PDF_PAGE_9 以人类认知测试作类比。 | 有任务内容效度与构念隔离的论证，但未报告信度、统计效度证据或 manipulation check，也未讨论单一操作化局限。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_3 列出 9 个模型及版本；PDF_PAGE_9 讨论主要聚焦短上下文且基准可扩展到长上下文。 | 报告了模型样本来源与部分推广边界，但无跨样本/跨情境复现，也未精确界定外部效度边界。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_3: 'fixed snapshot of 1110 randomly generated test samples'; PDF_PAGE_16-18 报告每任务样本数。 | 说明了评估在模型-任务-样本层聚合，但未用多层模型处理样本嵌套于任务/超参数的结构；主要分析为描述性平均。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；论文比较的是明确列出的具体模型，而非需要随机效应推广到模型总体的抽样设计。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_2: 'generate randomized test cases for each category'; PDF_PAGE_12: 上下文词从英语词典均匀采样。 | 材料/项目确由随机生成，可视为从更大材料总体抽样，但分析中未显式加入项目随机效应或准 F 比。 |
| G4 | 统计功效 | 0 | PDF_PAGE_3: 'fixed snapshot of 1110 randomly generated test samples'；PDF_PAGE_16-18 给出样本数但无功效分析。 | 没有事前功效分析或其他样本量确定依据，主结果也缺少系统效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_3 与 PDF_PAGE_16-18 列出任务、超参数、样本数与指标；未见排除规则或停止规则。 | 报告了全部任务和样本数，但未报告数据/试次剔除规则、样本量决定方式，也未区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未报告预注册平台、编号或分析计划。 | 无公开预注册；按判定口径，未预注册记 0。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较；yes/no 任务无选项位置反平衡需求。 |
| J2 | 冗长偏差 | NA | — | 无 LLM 裁判评分开放性生成质量，长度不作为质量偏好来源比较。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或纠错式对话输入，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge，采用自动 exact match/ROUGE/Jaccard 指标。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 提示模板为 zero-shot 指令，未使用 few-shot in-context 示例；附录中的 FINAL ANSWER 仅为格式示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_12-16 Appendix A 给出完整 prompt 模板；PDF_PAGE_8 与 PDF_PAGE_19 报告 prompt variation 敏感性比较。 | 提供完整模板并做了措辞变体消融，但无模板版本号/迭代日期、dev/test 划分说明或系统 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | PDF_PAGE_3: context 固定 4k，Stateful 约 1.5k；PDF_PAGE_8-9 与 PDF_PAGE_19 报告不同上下文长度结果。 | 报告了实际上下文长度并做长度变化，但未操纵关键信息首/中/尾位置，也未报告位置 × 正确率曲线。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_3: 'temperature to 0, and top p to 1'; 'max output token to 4096'。 | 报告了主要采样超参，但未报告随机种子、每条件重复采样 N 与主结果 CI；主实验基本为单次确定性解码设定。 |
| J9 | 重复与文本退化 | 0.5 | PDF_PAGE_3 报告 temperature/top-p/max output；PDF_PAGE_5 讨论模型在编辑中 'repetitive word loops'。 | 报告了部分解码设置并讨论重复退化，但未报告 repetition penalty、重复率/退化率作为 QC 指标，也未系统分离退化与能力。 |
| J10 | 分词效应 | NA | — | 单语言英文基准，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | PDF_PAGE_2: 'allowing the generation of fresh, randomized test cases'；PDF_PAGE_3 使用自建快照。 | 使用自动生成的新测试可降低污染，但未报告模型训练截止日期对照或污染检测率。 |
| J12 | 基准饱和 | 0.5 | PDF_PAGE_3: 'models are expected to perform perfectly at this length'；PDF_PAGE_8: retrieval-style tasks 'less effective at distinguishing model capabilities'。 | 识别到搜索类任务接近天花板并转向更难任务/更长上下文，但未系统改用连续指标或对模型差异做 bootstrap CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为独立因变量；任务准确率关注记忆操作而非约束遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0 | PDF_PAGE_12-16 模板要求 'yes/no' 或 'FINAL ANSWER' 格式；PDF_PAGE_18 以 exact match/ROUGE 评估，未报告格式合法率。 | 任务确有输出格式要求，但未报告格式约束设置、格式合法率或把格式失败与内容错误分开；单一成功率可能混合二者。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF_PAGE_9: 'Analogies to Human Cognitive Testing... analogous to memory testing in humans'；PDF_PAGE_2 定义 memory-usage capabilities。 | 论文将 LLM 记忆能力与人类认知测试类比并给出任务定义，但未系统比较人类同名构念、未报告人类对照或权重快照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有随模型规模/训练进展的能力曲线，也未宣称涌现或突变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究为纯基准评估，不涉及对代理指标的优化、RL 或 best-of-N 训练环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_3 列出模型名称与版本；PDF_PAGE_16-18 报告每任务样本数；PDF_PAGE_9/19 部分表有 95% CI。 | 报告了样本数与部分 CI，但模型 snapshot 不精确（如仅写 GPT-4o），主结果无重复采样 CI，模型比较也未做配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮作答，无对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
这是一项系统化、可复现性较好的 LLM 基准工程研究：任务族、提示模板、超参数网格、样本数与自动指标报告较清楚，并做了提示变体、上下文长度和 gibberish 消融。主要缺口是缺少统计建模/随机效应、功效论证、污染检测、精确模型 snapshot、格式合法率、信效度与天花板/地板分布的系统报告；多数人类实验专有设计组件不适用。
