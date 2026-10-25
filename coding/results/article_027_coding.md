# article_027 | How does Misinformation Affect Large Language Model Behaviors and Preferences? | 2025

研究类型概述：本文是面向 LLM 的 misinformation 基准构建与评测研究，并提出 RtD 干预方法。分析单位为 LLM 调用/基准题目及其条件汇总，不是人类被试。核心比较维度包括 misinformation 类型、单跳/多跳、六种文本风格、是否存在参数知识、证据呈现方式以及模型系列/规模。
- **研究构念（Construct）**：虚假信息易感性与知识偏好（misinformation susceptibility and knowledge preference）｜CA 构念锚定：情绪（emotion, `trm_4a3fd79d0a17f`）；情绪识别（emotion recognition, `trm_4a3fd79d0b665`）；共情（empathy, `trm_4a3fd79d0b67d`）
- **实验任务与范式（Task / Paradigm）**：本文是面向 LLM 的 misinformation 基准构建与评测研究，并提出 RtD 干预方法。分析单位为 LLM 调用/基准题目及其条件汇总，不是人类被试。核心比较维度包括 misinformation 类型、单跳/多跳、六种文本风格、是否存在参数知识、证据呈现方式以及模型系列/规模。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p2: 'three knowledge-conflicting types ... 3 types and 6 textual styles'; p5 evaluates models across these conditions; p27-p30 prompts provided; no manipulation check reported. | 论文明确构造并命名了 misinformation 类型、风格、hop 等条件及其水平，但未报告操纵检验；作为 LLM 条件操纵记 0.5。 |
| A2 | 因变量 | 0.5 | p6 defines Success Rate, Memorization Ratio MR and Evidence Tendency TendCM; p15-p16 Appendix F.1 gives formulas MR=Rc/(Rc+Rm) and TendCM=(Rc-Rm)/(Rc+Rm). | 因变量指标与计分方式清楚，但缺少信度/效度证据、置信区间及连续指标预处理说明。 |
| A3 | 控制变量 | 0.5 | p5: 'temperature setting of 0 ... output length 512'; p16: 'batchsize of 20000 and maintain other configurations default'; p27/p30 option/evidence order randomized. | 报告了若干恒定推断设置和顺序控制，但未系统列出控制变量清单及各自控制手段。 |
| A4 | 混淆变量 | 0.5 | p6: two scenarios according to whether LLMs possess prior factual knowledge; p17 analyzes perplexity/N-gram/question similarity for style effects; p9 Limitations mainly discusses coverage. | 通过记忆/未知分层和语言特征分析部分识别了潜在混淆，但没有正式说明残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 无调节假设和交互检验模型；文中只有条件分组描述比较，未界定调节变量。 |
| A6 | 中介变量 | NA | — | 无中介变量、直接/间接效应分解或因果链检验。 |
| A7 | 操作性定义 | 1 | p2-p4 gives benchmark construction pipeline; p5 Table 2 gives data statistics; p15-p16 gives metric formulas; p25-p30 gives prompts; p14 gives human annotation guideline. | 关键构念、数据构造、评估指标和提示均写成了可重复执行的操作程序。 |
| A8 | 水平数与类型 | 0.5 | p2: three knowledge-conflicting types and six styles; p4 Table 2: one-hop/multi-hop, 3 types, 6 styles; p5 lists open/closed models and sizes. | 水平数与水平标签清楚，但未明确标注变量类型、水平属性/间距等，故为部分完整。 |
| A9 | 单一操作化的风险 | 0.5 | p6 uses Success Rate, MR and TendCM; p7-p8 reports figures; p14 reports human evaluation of benchmark quality; no cross-metric convergence/correlation is given. | 采用多个指标和多种文本风格评估关键现象，但未报告各操作化指标之间的会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 不是人类自陈式多构念测量；不存在典型的共同方法偏差同源自评问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试组间分配；所有模型在同一基准条件上被评测，而非独立被试组承担不同条件。 |
| B2 | 被试内设计 | NA | — | 无人类被试内条件顺序设计；各 benchmark 项独立提示，未报告被试级条件顺序平衡。 |
| B3 | 混合设计 | NA | — | 无正式组间/组内混合实验设计及对应混合模型/误差项。 |
| B4 | 因子设计 | NA | — | 论文未做正式因子设计及主效应/交互分析；仅有基准条件描述比较。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验、简单主效应或交互图示误差。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计及区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；基准构建与评测不涉及非随机分组因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理设计，因此不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | misinformation 类型/风格由数据构建决定，不存在将研究单位随机分配到互斥实验条件的程序；选项/证据顺序随机化另见 E1/J1。 |
| C2 | 平衡 | NA | — | 无重复条件顺序及顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p5: 'temperature setting of 0 ... output length 512'; p16: 'batchsize of 20000 and maintain other configurations default'; p27/p30 order randomization. | 列出了部分恒定变量及水平，但未系统讨论这些固定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为协变量或区组纳入统计模型，也无 ANCOVA/协变量分析。 |
| C6 | 盲法 | NA | — | 结果评估由自动化 LLM 调用完成；人类标注仅用于数据质量，不涉及结局盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | 各提示独立调用，LLM 无跨试次上下文学习或练习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳效应，且不存在 session 时长/休息问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立提示，无跨条件迁移或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件顺序，因此不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为离散选择/正确率和客观指标，不是主观量表范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p27: 'The order of options is randomized to avoid any influence of sequence'; p30: 'The order of evidences and options are randomized'. | 报告了选项/证据顺序随机化，但未说明随机化方案类型、各顺序出现次数或平衡细节。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分题或默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不涉及需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | LLM 评估完全自动化，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5 and Table 3 report mean Success Rate values across models/conditions (some near 99%); p5 only says results averaged across three runs; no SD/skew/endpoint frequencies or pilot calibration reported. | 报告了主要因变量的均值并可见部分高分接近上限，但未报告分布、端点频率或难度校准。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念测量，无同源共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | p5: 'All reported results are averaged across three runs'; p8-p9 reports Success Rate improvements such as '23.14 to 47.77'; no confidence intervals, power analysis or multiple-comparison correction. | 提供了百分比差异/效应量级和主要结果，但缺置信区间、样本量依据及多重性校正。 |
| F2 | 内部效度 | 0.5 | p27/p30 reports option/evidence order randomization; p5 and p16 describe model evaluation; no baseline equivalence, allocation concealment, flow diagram or loss handling. | 有部分顺序控制，但无随机条件分配、基线等价性及内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | p4-p5 reports NLI quality check with over 95% accuracy; p14-p15 Table 5 reports inter-annotator agreement around 94-97%; no reliability/validity evidence for main LLM metrics or manipulation check. | 基准数据质量有信度/效度证据，但关键 LLM 行为指标的信效度和操纵检验不足。 |
| F4 | 外部效度 | 0.5 | p5 lists open/closed model families and sizes; p9 Limitations notes incomplete coverage and text-only scope; no representative sampling of models or cross-context replication. | 报告了模型样本和部分推广边界，但未论证模型代表性或跨情境复现。 |
| G1 | 分析单位 | 0.5 | p5: 'All reported results are averaged across three runs'; p16 says closed-source models use subsets; no multilevel model or item/model nesting treatment. | 说明了结果按模型/条件汇总，但未明确处理题目嵌套于模型/材料的分析层级。 |
| G2 | 随机效应 | 0 | No mixed-effects model or random-effect structure is reported; p5/Table 3 report aggregated means only. | 对重复题目和模型系列未设随机效应，无法区分项目/条件抽样方差，推断可推广性不足。 |
| G3 | 材料作为随机效应 | 0 | Benchmark items/materials are treated as fixed test instances; no item random effect, mixed model, or quasi-F/min-F correction is reported. | 未把材料/项目作为从更大总体抽样的随机因子，存在材料固定效应风险。 |
| G4 | 统计功效 | 0 | No a priori power analysis or sample-size justification is reported; only 'averaged across three runs' on p5. | 缺少设计阶段功效分析和预期效应量依据。 |
| G5 | 研究者自由度 | 0.5 | p4 reports completeness filtering, entailment checking and semantic matching with alpha=0.3; p5 reports metrics and conditions; no trial exclusion/stopping rules or explicit confirmatory/exploratory labeling. | 报告了数据构建过滤和主要指标，但未完整披露分析排除、停止规则及探索性/验证性区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or pre-specified analysis plan is mentioned. | 无预注册，且未明确区分验证性与探索性分析。 |
| J1 | 位置偏差 | 0.5 | p27: 'The order of options is randomized'; p30: 'The order of evidences and options are randomized'. | 识别并随机化了选项/证据位置，但未报告交换前后偏好翻转率或位置×正确率曲线。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放生成质量；因变量为多项选择/Success Rate 等。 |
| J3 | 谄媚 | NA | — | 无用户立场、反馈或纠错对话操作，不涉及谄媚偏差。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 或模型生成互评。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 评估提示为零样本多项选择提示，未使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p25-p30 provides full prompts for generation/stylization/evaluation; no prompt version dates, sensitivity ablation, or dev/test separation is reported. | 公布了完整提示模板，但未做措辞敏感性消融或说明是否在测试集上调参。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短（每条证据约 550 tokens），不是长上下文或 RAG 位置效应实验。 |
| J8 | 温度与采样随机性 | 0.5 | p5: 'temperature setting of 0 ... output length 512'; 'All reported results are averaged across three runs'; p16 says default configurations; no top-p/seed/snapshot or 95% CI reported. | 报告了温度和重复次数，但缺完整采样参数、随机种子、调用日期和置信区间。 |
| J9 | 重复与文本退化 | NA | — | 评估任务为短多项选择输出，不涉及开放生成退化率或 n-gram 重复率比较。 |
| J10 | 分词效应 | NA | — | 实验为英语单语言/单脚本，无跨语言分词效应比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p3 uses Wikidata dump '2024.09.01'; p5 lists model names but no training cutoff dates or contamination detection/overlap analysis. | 未做测试集污染检查，也未对照模型训练截止日期与基准发布日期。 |
| J12 | 基准饱和 | 0.5 | Table 3 and Figures 4-7 report benchmark scores; several temporal-conflict cells are near 99%; no explicit saturation analysis or CI comparison is given. | 报告了分数量程和部分高分，但未系统评估天花板/饱和或改用连续指标比较。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；任务是 misinformation detection/choice QA。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p27: 'Only choose and return with a specific option'; p29-p30 similar option-only constraints; no format-legal rate or retry/post-processing report. | 有输出格式约束，但未报告格式合法率、重试策略或将格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估或有害请求攻击成功率。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文是 LLM 基准/工程评测，不主张测量可与人类心理学构念对应的被试构念，也无人类同范式对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨规模/训练进展的涌现能力曲线或相变宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | RtD 为推理时方法流程，不是以代理指标为目标的训练/RL/best-of-N 优化研究。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5: 'All reported results are averaged across three runs'; p5/p16 report model names but not exact snapshots/API dates; no CI, paired tests, or raw logs. | 有重复运行和模型家族名称，但缺精确 snapshot、置信区间、配对检验与推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评估，无多轮对话历史累积。 |

## 编码小结
论文在基准构建、数据质量控制、提示披露和跨模型评测方面较扎实，适合作为 LLM 行为/偏好评测；但它不是人类实验，也不是正式因子实验。多数人类被试设计与顺序控制组件不适用。主要不足是缺少推断统计与置信区间、模型 snapshot/污染检查、提示敏感性消融、项目随机效应和多层建模，以及预注册/研究者自由度控制。
