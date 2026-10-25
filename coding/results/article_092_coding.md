# article_092 | Can Large Language Models Interpret Noun-Noun Compounds? A Linguistically-Motivated Study on Lexicalized and Novel Compounds | 2024

研究类型概述：LLM 基准/行为评测：用 surprisal 与提示选择两类任务，在词化复合词与自建新异复合词数据上比较 base/instruct 模型；分析单位为复合词或模型-条件，不是人类被试实验。
- **研究构念（Construct）**：名词复合词语义解释、词汇化、类比组合与具体性｜CA 构念锚定：类比推理（analogical reasoning, `trm_4a3fd79d09810`）；流体智力（fluid intelligence, `trm_4a3fd79d0a375`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：LLM 基准/行为评测：用 surprisal 与提示选择两类任务，在词化复合词与自建新异复合词数据上比较 base/instruct 模型；分析单位为复合词或模型-条件，不是人类被试实验。｜CA 任务锚定：类比推理任务（analogical reasoning task, `trm_4f244f0286947`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p5: “We ran three different versions of prompting strategies: zero-shot..., one-shot, and three-shot learning”; p7: NNC 数据用 sameHead/sameMod 替换构造。 | 报告了提示策略、模型版本与替换位置等多水平条件，但未把这些条件作为统一操纵程序报告分配方式，也无操纵检验；仅达基本要件。 |
| A2 | 因变量 | 0.5 | p5: “two different performance metrics: i.) Accuracy... and ii.) Mean Reciprocal Rank (MRR)”；p4 给出 surprisal 公式与计分。 | 因变量指标与计分方式明确，但未报告信效度证据，也未说明连续指标预处理或天花板/地板效应控制。 |
| A3 | 控制变量 | 0.5 | p5 脚注：“Temperature: 0, do_sample: False, top-k: 10, top-p: 5, max-tokens: 50, frequency and presence penalty: 0”；p5 “used the same hyperparameters for all models”。 | 报告了部分固定超参与同一化控制，但未系统列出所有控制变量及逐一控制手段，控制说明不完整。 |
| A4 | 混淆变量 | 0.5 | p9 局限：“The examples presented in one- and few-shot settings are the same independently of whether the target question has the same semantic relation as the prompt. This could... affect the final results.”；p6 讨论 concreteness 与关系难度。 | 识别了提示示例、关系类型/具体性等潜在混淆，并部分讨论影响，但未系统说明控制方式或残余混淆的定量威胁。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量模型或交互检验；concreteness 只作为准确率的预测变量进入 GLMM，不是调节分析。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或因果链中介假设。 |
| A7 | 操作性定义 | 1 | p4-5 描述 surprisal 计算与准确率/MRR 计分；p5 与 p12 附录给出提示模板与选项；p7 描述用 WordNet hypernym 与频率标准构造新异复合词。 | 关键任务、计分、提示和材料构造均有可复现的操作化说明，达到逐构念操作化要求。 |
| A8 | 水平数与类型 | 0.5 | p5 Table 4 列出 BERT、GPT2-xl、Llama-2、Falcon、Mistral 的 Base/Instruct；p7 Table 5-6 列出 1-shot/3-shot；p8 Table 7 列出 sameHead/sameMod。 | 报告了多个条件的水平数与标签，但未系统说明水平类型、间距/全距或连续变量的中心化处理，完整性不足。 |
| A9 | 单一操作化的风险 | 1 | p6: “The results of the prompting experiment are in line with Surprisal scores.”；p3 使用 LNC 与 Nakov 两个数据集。 | 关键构念采用 surprisal 与提示选择、多个数据集和多个模型的操作化，并报告了会聚性证据。 |
| A10 | 单一方法的风险 | NA | — | 这是纯计算评测，不涉及人类自陈式同源测量，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试，也无将被试分配到独立条件的被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内的重复测量设计及顺序平衡方案。 |
| B3 | 混合设计 | NA | — | 没有按被试逐因素标注组间/组内的混合设计。 |
| B4 | 因子设计 | 0 | p5 Table 4、p7 Table 5-6、p8 Table 7 呈现模型、提示设置、数据集/替换位置的条件均值，但无交互项或 ANOVA 表。 | 存在多因素并列比较，但未作为完全交叉因子设计报告设计矩阵、每格样本量与交互统计；按规则多因素但完全未报告交互项记 0。 |
| B5 | 主效应 | 0.5 | p5: “Llama-2 Instruct reaches a statistical significance of the improvement over the Base model... Falcon... statistically worse”；p5 脚注说明用 McNemar 检验。 | 对模型/指令微调差异做了成对统计检验，但未报告正式主效应 F/df/效应量，完整性不足。 |
| B6 | 交互作用 | 0 | p8: “changing the head or modifier affects the ability of the model... differently”，但无交互项统计检验或简单效应分析。 | 仅描述性讨论替换位置与模型表现的差异，未报告交互项统计量、简单效应或图示误差棒。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或被试内顺序安排。 |
| B9 | 准实验设计 | NA | — | 无准实验设计、非随机分组或因果推断处理。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理条件，故不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有将分析单位随机分配到互斥条件的程序；模型/条件均为固定评测设置。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序或各顺序被试分配。 |
| C3 | 恒定 | 1 | p5 脚注列出 temperature、do_sample、top-k、top-p、max-tokens、penalty；p5 “All experiments were run on Colab TPU and A100”；p9 讨论低温度设定对创造性的外部效度限制。 | 明确列出了主要固定超参与运行环境，并在局限中讨论设定对外部效度的影响，核心要求满足。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对分配程序。 |
| C5 | 纳入为变量 | 0.5 | p6: “binomial generalized linear mixed model... Accuracy... concreteness... coefficient=0.703, SE=0.133, p<0.001”。 | 将 concreteness 测量并纳入 GLMM 作为预测/协变量，但未报告斜率齐性、调整后组间效应量或随机效应结构，控制不完整。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类主试、评分者或可施盲的参与者。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡、拉丁方或 ABBA 等顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 评测按独立提示/项目进行，无人类练习块或上下文内学习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳效应，且任务不是长时人类 session。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留或清洗期问题；各提示/项目为独立评测。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉处理，故不涉及不对称迁移检验。 |
| D5 | 范围效应 | NA | — | 因变量为准确率/MRR/surprisal，不是绝对判断或李克特量表，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p5 与 p12 附录给出固定编号选项列表（1-9），未报告选项顺序随机化或反平衡。 | 多选项选择任务存在位置/顺序偏差风险，但论文完全未控制选项呈现顺序，也未讨论顺序效应。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不涉及需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5 Table 4 报告各模型 Accuracy/MRR；p6 Figure 1 与 p8 Table 7 报告分关系/替换位置的准确率，部分关系接近 96%；但无 SD、偏度、端点频率或 pilot 难度校准。 | 报告了总体与分关系准确率，可部分观察天花板倾向，但缺少分布形态与任务难度校准说明。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p6 报告 GLMM 系数、SE、p 与 AIC/BIC；p5 脚注报告 McNemar 检验；p5 Table 4 报告 Accuracy/MRR。 | 报告了统计检验与部分效应相关量，但无置信区间、样本量/功效依据，也未说明多重比较校正。 |
| F2 | 内部效度 | NA | — | 无人类随机分配、分配隐藏、基线等价或被试流向；研究不是因果实验设计。 |
| F3 | 构念效度 | 0.5 | p6 以 surprisal 与提示结果相互印证；p9 讨论 Tratz 标注聚合导致无法确定标注者一致性及单一正确关系假设。 | 有多操作化与部分构念效度讨论，但未报告正式信度/效度统计、评分者一致性或操纵检验。 |
| F4 | 外部效度 | 0.5 | p3 说明数据来自 Tratz、Muraki、Nakov；p9 局限明确“The work focuses only on English”并讨论 7B 模型与提示设定的推广限制。 | 报告了材料来源与部分推广边界，但未报告跨语言/跨情境复现，也未系统说明模型总体代表性。 |
| G1 | 分析单位 | 0.5 | p6 使用 binomial GLMM 分析 compound-level accuracy，但未报告随机效应结构；模型/条件比较对同一批复合词重复观测。 | 说明了统计模型但未明确处理分配层级与复合词/模型重复观测的嵌套结构，分析单位匹配性报告不完整。 |
| G2 | 随机效应 | 0 | p6 仅称“binomial generalized linear mixed model”，未报告哪些因子为随机效应或随机截距/斜率结构。 | 虽使用混合模型，但未说明随机效应因子与结构，读者无法判断推断可推广的总体范围。 |
| G3 | 材料作为随机效应 | 0 | p3 说明使用 668 个 LNC compound 与 250 个 Nakov compound；p6 GLMM 未报告 item/compound 随机效应，也未做 F1/F2 或准 F。 | 具体复合词材料被当作固定项目分析，未把材料作为从更大材料总体抽样的随机因子，限制了对任意材料的推广。 |
| G4 | 统计功效 | 0 | 全文未报告事前功效分析、目标功效、预期效应量或样本量推导；结果无 CI。 | 无设计阶段功效分析或样本量论证，也未报告效应量置信区间。 |
| G5 | 研究者自由度 | 0.5 | p4 说明只保留 clear map 的 compound、忽略 ambiguous compounds 与 odd paraphrases，最终 668；p5 说明 zero-shot 因输出不一致未报告。 | 报告了部分材料筛选与任务排除规则，但未完整报告排除数量、全部因变量/条件及样本量决定方式，也未区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | 全文无预注册平台、注册编号或数据收集前分析计划的说明。 | 无公开预注册，也未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | 0 | p5 与 p12 附录显示固定编号选项（1-9）；未报告选项位置随机化、A/B 交换重判或位置×正确率。 | LLM 从候选项中选择，存在明显位置偏差风险，但完全未做位置反平衡/随机化，也未报告翻转率。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放式生成长短；准确率由 surprisal 或选项匹配计算，冗长偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话操纵，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 裁判或模型输出成对比较，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p5: “one-shot, and three-shot learning (one and three examples are provided, respectively)”；p9 局限说明示例不随目标关系变化。 | 报告了 few-shot 示例数量与部分示例内容，但未报告示例来源/标签比例、排列反平衡、多 seed 重采样与示例未取自测试集的证明。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p5 与 p12 附录给出提示示例；p9 局限：“we did not test whether other questions could improve... nor... different examples within the prompt”。 | 提供了提示模板示例，但无版本号、完整模板集、敏感性消融或 dev/test 划分；作者也承认提示未系统验证。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 提示很短，远低于长上下文窗口，也无 RAG/长文档设置。 |
| J8 | 温度与采样随机性 | 0.5 | p5 脚注报告 temperature=0、do_sample=False、top-k=10、top-p=5、max-tokens=50、penalty=0；全文未见每条件重复采样、随机种子或 CI。 | 报告了主要采样超参，但为单次确定性运行，未报告 seed、重复次数、均值/CI 或精确 API snapshot。 |
| J9 | 重复与文本退化 | NA | — | 主要任务是选项选择与 surprisal 评分，不评估开放式长文本生成退化；重复率 QC 不适用。 |
| J10 | 分词效应 | NA | — | 研究仅限英语单语言单脚本，无跨语言/跨脚本 tokenization 比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p3 提到 Coil and Shwartz 用 n-gram overlap 发现 GPT-3 可能 parroting，但本文未报告 LNC/Nakov 测试集版本、模型训练截止日期或污染检测。 | 使用公开数据集与开放模型，却未做自身测试集污染检查或训练截止日期对照，不能区分记忆与泛化。 |
| J12 | 基准饱和 | 0.5 | p5 Table 4 报告总体 Accuracy 约 0.26-0.65，p6 Figure 1 报告分关系准确率，部分关系接近满分；未报告 SOTA 位置或 bootstrap CI。 | 报告了基准分数量程与部分高位关系，但未系统评估饱和或用连续指标/更难子集处理局部天花板。 |
| J13 | 指令遵循 | NA | — | 因变量是复合词语义关系选择，不是指令遵循测量；不涉及按约束类型拆分指令准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p5 与 p12 附录要求从编号列表中选择最可能描述；未报告文法约束、JSON/结构化输出设置、格式合法率或重试策略。 | 存在编号选项的格式约束，但未把格式失败与内容错误分开报告，也未报告格式合法率；部分满足。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估，无有害请求或对抗攻击设置。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1 明确以人类复合词抽象/类比能力为参照；p6 以 concreteness effect 解释 LLM 表现；但无人类同范式对照实验。 | 讨论了 LLM 构念与人类同名构念的关系，并报告模型版本，但未系统做人类对照或完整构念效度论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告跨模型规模或训练进展的能力曲线，不涉及涌现/指标诱导假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不对代理指标进行训练、RL 或 best-of-N 优化，仅做评测。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5 报告模型名与超参，p10 提供 OSF 数据/代码链接，p5 脚注用 McNemar 做模型比较；但无重复 N、CI、精确 snapshot 或推理日志。 | 具备部分可复现信息与配对检验，但单点分数、无重复/CI，模型 snapshot 标识不精确。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮提示，无多轮对话历史或一致性衰减问题。 |

## 编码小结
研究问题与任务材料描述较具体，并比较了多个开放模型、提示设置与数据集；但缺乏人类被试设计、随机化/顺序控制、预注册、功效分析与置信区间，材料随机效应与提示敏感性报告不足。多数人类实验设计组件不适用；LLM 评测特有的位置偏差、污染、可复现性等存在明显缺口。
