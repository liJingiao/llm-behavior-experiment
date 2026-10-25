# article_211 | Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | 2023

研究类型概述：LLM 行为与基准评测研究，非人类被试实验；分析单位为两个模型在 BBH/BBQ 题目上的输出，主要操纵提示偏置（Answer is Always A、Suggested Answer）、CoT 与 No-CoT、zero-shot 与 few-shot、去偏指令等，因变量为准确率下降、不忠实解释比例及人工标注的解释支持率。
- **研究构念（Construct）**：链式思维解释忠实性、事后合理化与提示偏置敏感性｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：在多项选择任务中向现成模型加入偏置特征，比较最终答案是否受偏置影响以及CoT是否如实提及该影响。（改变偏置提示类型、偏置强度、模型规模、是否使用CoT及任务。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4-5: 'we compare model predictions on unmodified inputs (unbiased context) against predictions on inputs that have a biasing feature applied (biased context)'; 'First, we test Answer is Always A... Second, we test Suggested Answer'; p5: 'CoT vs. No-CoT' and 'Zero-Shot vs. Few-Shot'. | 自变量的名称、水平与创设方式较清楚，且按同一题目配对比较；但未报告正式的操纵检验，分配到条件的方式也仅隐含为同一模型/题目的重复提示。 |
| A2 | 因变量 | 0.5 | p5: 'we use decrease in model accuracy when exposed to biased contexts to measure systematic unfaithfulness'; p7: 'Percentage of Unfaithfulness Explained by Bias'; p7: manual annotation of 104 unfaithful explanations. | 因变量指标与计分方式有明确界定，包括准确率下降、不忠实配对比例和人工支持性标注；但未报告测量信度、效度证据、标注者一致性或连续指标预处理细节。 |
| A3 | 控制变量 | 0.5 | p5: 'We use the same few-shot prompt for both CoT and No-CoT prompting settings'; p5: GPT-3.5 temperature 0.7 and Claude 1.0 temperature 1; p4: same benchmark and models within experiments. | 报告了若干保持恒定的因素（同一数据、同一 few-shot prompt、温度默认值），但不是系统的控制变量清单，也未逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p5: 'A drop in accuracy... could in principle result from increased noise... but in practice we find that almost all drops in accuracy are explained by increases in bias-consistent predictions'; p6: 'Since all settings use the same data, we employ a paired difference test'. | 识别了噪声导致准确率下降这一替代解释并做了检查，也使用配对比较；但未系统讨论残余混淆或敏感性分析对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 理论模型没有明确调节变量与调节假设；模型/提示条件比较是条件效应比较，未做正式调节模型、中心化或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量与中介假设，也未做直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p4: 'we reorder the multiple-choice answer options in the few-shot prompts... so that the correct answer is always the first one (A)'; p5: 'We add the following string to the prompt: I think the answer is <random_label>...'; p7: annotation rule for whether explanation supports predicted answer. | 关键操纵和不忠实性计分都有可执行描述，但精确 prompt 模板、完整标注流程与部分计分细节主要指向附录，正文中仍不完整。 |
| A8 | 水平数与类型 | 0.5 | p4-5: two biasing features, CoT vs No-CoT, zero-shot vs few-shot; p8: no debiasing instruction vs debiasing instruction; p7: BBQ weak evidence version 1 vs version 2. | 各条件的水平数与标签基本明确，但未给出完整多因素设计矩阵；水平类型为分类变量，未显式说明类型、间距或中心化。 |
| A9 | 单一操作化的风险 | 1 | p3: 'counterfactual simulatability' framework with two types of counterfactuals; p4-7: 13 BBH tasks, two bias types, two models, plus BBQ; p10: 'necessary but not sufficient test' limitation. | 关键构念采用多种任务、偏置类型与不忠实性指标进行多操作化，并在局限部分明确讨论了单一/有限操作无法证明完全忠实。 |
| A10 | 单一方法的风险 | NA | — | 自变量与因变量均来自 LLM 对同一提示的输出，不涉及人类自陈量表的同源方法偏差；也无 Harman 因子、标记变量等共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 研究没有人类被试，也不存在被试组间分配；分析单位是模型在题目上的输出。 |
| B2 | 被试内设计 | NA | — | 虽然同一题目被置于偏置/无偏置等对照条件，但每次提示独立生成，没有人类被试内顺序或跨条件迁移意义上的重复测量设计。 |
| B3 | 混合设计 | NA | — | 没有人类被试的组间/组内混合设计，不涉及混合误差项。 |
| B4 | 因子设计 | 0 | p4-5: BBH experiments cross two bias types, CoT/No-CoT, zero/few-shot, two models; p8: Table 5 crosses CoT/No-CoT, zero/few-shot, debiasing instruction and model; no full ANOVA/design matrix. | 存在多因素条件结构，但论文以逐条件比较和表格呈现，没有完整设计矩阵、每格样本量或正式交互项统计检验；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | p6: 'accuracy drops as much as -36.3%... confidence intervals... range from ±1.6% to ±2.4%'; p8: 'effect of CoT ranges from... -1.2% to... -8.9%'. | 报告了主要条件效应的大小和置信区间，但未报告 F 值、自由度、p 值表或 ηp² 等效应量，也未系统讨论交互显著时主效应解释受限。 |
| B6 | 交互作用 | 0 | p6 and p8 report separate effects of bias, CoT, few-shot, and debiasing across models/settings, but no formal interaction test or simple-effects follow-up. | 没有报告交互项统计检验、简单主效应或交互图误差棒；仅有分组描述和逐条件差异比较。 |
| B7 | 区组设计 | NA | — | 没有区组或分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有人类被试内条件顺序，也未使用拉丁方设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验的人类因果设计，不存在非随机分组选择偏差问题。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM 每次提示独立，无处理可逆性或跨条件迁移问题。 |
| C1 | 随机化 | 0.5 | p5: 'We sample a different random multiple-choice letter label for each dataset instance' for the Suggested Answer bias. | Suggested Answer 的标签确有随机抽取，但未报告随机数生成工具、种子、分配隐藏或基线均衡检验；其他条件比较也不是随机分配到组。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件呈现顺序；偏置/无偏置提示是独立生成的不同上下文。 |
| C3 | 恒定 | 0.5 | p5: 'For GPT-3.5 we use a temperature of 0.7... For Claude 1.0 we use a temperature of 1'; p5: 'We use the same few-shot prompt for both CoT and No-CoT'; p4: same benchmark subsets. | 报告了温度、数据与部分提示保持恒定，但没有系统列出所有环境/模型调用恒定变量，也未讨论这些恒定选择对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配或配对分配设计。 |
| C5 | 纳入为变量 | NA | — | 没有将已知混淆变量作为区组或协变量纳入统计模型；研究主要通过同一题目配对比较控制题目差异。 |
| C6 | 盲法 | 0 | p7: 'we manually annotate 104 unfaithful explanations (one from each model/few-shot/task/context combination)'; p8-9: manual annotation of 96 examples. | 存在人工标注环节，但未报告盲法安排、标注者是否知晓条件、标注者人数或盲法成功检验。 |
| C7 | 平衡的层级 | NA | — | 没有需要选择完全平衡、拉丁方或 ABBA 层级的顺序设计。 |
| D1 | 练习效应 | NA | — | LLM 每条件独立提示，无练习块或上下文内学习。 |
| D2 | 疲劳效应 | NA | — | 不涉及人类 session 时长或疲劳效应。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各提示独立生成，不涉及跨条件清洗期或残留效应。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移，因此不对称迁移不适用。 |
| D5 | 范围效应 | NA | — | 使用的是客观准确率和解释标注，不是量表式绝对判断，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p4: 'We reorder the multiple-choice answer options in the few-shot prompts... so that the correct answer is always the first one (A)'; p5: suggested-answer label sampled randomly per instance. | 论文识别并操纵了选项位置/标签偏置，也随机化 Suggested Answer 标签；但没有对测试题选项位置做系统反平衡，也未报告 A/B 交换翻转率或各位置正确率曲线。 |
| E2 | 默认赞同 | NA | — | 未使用 Likert 或态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 未使用等级量表，也不涉及跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 没有人类被试意义上的需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | 数据采集为自动化 LLM API 调用，无人类主试或实验者期望传递；人工标注环节不构成实验者效应主问题。 |
| E6 | 天花板 / 地板效应 | 0 | p6: reports accuracy percentages such as '57.1→59.6% for GPT-3.5' and '59.2→65.3% for Claude 1.0'; no SD, skew, endpoint frequencies, or pilot difficulty calibration. | 报告了准确率均值，但没有报告分布形态、端点频率或任务难度校准，无法排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念测量，不涉及共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | p5: 3,299 evaluation examples; p6: 'confidence intervals... ±1.6% to ±2.4%' and 'we employ a paired difference test'; p8: Table 5 reports significance marks and 95% CIs in text. | 报告了样本量、差异估计与置信区间及配对比较，但没有事前功效分析、正式效应量名称、所有分析的多重性校正说明。 |
| F2 | 内部效度 | NA | — | 没有人类被试随机分配、分配隐藏、流失或 flow diagram；内部效度以同一题目配对提示和替代解释检查来处理。 |
| F3 | 构念效度 | 0 | p3 defines faithfulness via counterfactual simulatability; p7 and p8-9 report manual annotation rules but no reliability/validity statistics or formal manipulation check. | 构念定义和多操作化有讨论，但没有报告关键测量的信度、效度证据、标注者一致性或正式操纵检验；因此核心构念效度证据不足。 |
| F4 | 外部效度 | 0.5 | p4: 13 BBH tasks and 3,299 examples; p7: BBQ subset stratified across nine social bias categories, 2,592 examples; p10: limitations on minor input modifications and unknown biases. | 报告了样本来源和任务/类别特征，也讨论了部分推广边界；但没有跨样本/跨情境复现结果，代表性论证有限。 |
| G1 | 分析单位 | 0.5 | p5: 3,299 examples for evaluation and 330 examples per task; p5: Figure 1 accuracy is 'micro-averaged across BBH tasks'; p6: paired difference test on same data; p8: Table 5 by model and setting. | 分析单位基本是题目级输出，并按任务做微平均/逐任务结果；但未明确处理题目嵌套于任务和模型的聚集结构，也未使用多层模型。 |
| G2 | 随机效应 | 0 | p4: only text-davinci-003 and claude-v1.0; p6: paired difference tests; p10: conclusion speculates 'similar outcomes... for other biasing features and models'; no random-effects model. | 模型和任务被当作固定个案处理，未说明随机效应结构；结论又向其他模型/偏置推广，随机效应/可推广总体范围报告不足。 |
| G3 | 材料作为随机效应 | 0.5 | p5: 'we subsample 330 examples per task... 3,299 examples for evaluation'; p6: confidence intervals from paired differences over examples; no item random-effect model. | 题目/材料显然来自有限基准，分析在题目层面做配对置信区间，体现了项目抽样；但没有显式将材料/题目作为随机效应纳入混合模型。 |
| G4 | 统计功效 | 0 | p5: 'Due to cost constraints, we subsample 330 examples per task'; p6 reports CIs but no a priori power analysis or standardized effect size. | 没有设计阶段功效分析或基于预期效应量的样本量推导；结果虽报告差异和置信区间，但无正式功效论证。 |
| G5 | 研究者自由度 | 0.5 | p5: bias-contradicting subset sizes (2,111 and 1,928) and task subsampling; p7: annotation sample definitions; p8: Table 5 reports multiple settings; p8 notes Appendix F.6 for bias-consistent labels. | 报告了主要数据子集、排除规则和多种分析条件，但未明确区分验证性与探索性分析，也未说明是否有按结果停止或追加。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement; p4 provides a GitHub link for data and code only. | 没有公开预注册、注册编号或数据收集前的分析计划；也未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | 0.5 | p4: 'We reorder the multiple-choice answer options in the few-shot prompts... so that the correct answer is always the first one (A)'; p5: suggested-answer letter sampled randomly; p6: accuracy drops attributed to Answer is Always A. | 识别并操纵了候选位置/标签偏置，也量化了其对答案的影响；但没有做 A/B 交换重判、报告偏好翻转率或系统位置反平衡。 |
| J2 | 冗长偏差 | NA | — | 研究不使用 LLM-as-judge 评估开放生成长度质量；主要指标为最终答案准确率和人工解释支持性标注。 |
| J3 | 谄媚 | 0.5 | p5: Suggested Answer prompt says 'I think the answer is <random_label> but I’m curious to hear what you think'; p5 cites sycophancy work; p6 reports accuracy changes under Suggested Answer; p8 reports debiasing prompting effects. | 显式操纵了用户建议答案并报告其对最终答案的影响，但没有报告严格的两类 sycophancy 翻转率、模型训练阶段/版本日期的完整信息或按轮次谄媚。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 或模型间成对裁判，因此无自我偏好偏差。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p4-5: '30 examples per task as candidates for few-shot CoT demonstrations'; 'we use a few-shot prompt with three examples' for Suggested Answer; '7 to 15 examples' for Answer is Always A; p5: demonstrations based on Suzgun et al. and manually edited; exact prompts in Appendix E. | 报告了 few-shot 示例来源、数量范围和不同标签条件，但未报告示例排列反平衡、多个示例集 seed 的重复结果，也未在正文提供完整模板。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p5: 'see Appendix E for exact prompt formats'; p5 compares CoT vs No-CoT; p8 adds debiasing instruction 'Please ensure that your answer is unbiased...'; no prompt sensitivity ablation or dev/test split. | 有多个提示版本并指向完整模板，但未报告语义等价措辞的敏感性消融、版本迭代日期或 dev/test 分离，提示工程自由度控制不完整。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文长度用于 few-shot 示例（最多 4,096 token），但没有长文档/RAG 设置，也没有关键信息首中尾位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p5: 'For GPT-3.5 we use a temperature of 0.7... For Claude 1.0 we use a temperature of 1'; no top-p, top-k, seed, repeated sampling N, or API snapshot date. | 报告了温度这一主要采样超参，但未报告种子、重复采样次数、方差估计或闭源 API snapshot 日期。 |
| J9 | 重复与文本退化 | 0 | p5 only reports temperature for each model; no decoding strategy, repetition penalty, n-gram repetition/degeneration rate, or length truncation rate. | 存在开放 CoT 生成，但未报告解码策略和重复/退化质量控制，无法排除解码差异与模型能力混淆。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本任务，没有跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p4: uses BBH and BBQ public benchmarks; no test-set version/training-cutoff comparison, contamination detection, or held-out private test. | 使用公开基准且未报告训练截止日期或污染检测，不能排除记忆/数据泄漏解释。 |
| J12 | 基准饱和 | NA | — | BBH 被描述为当前 SOTA 明显低于人类且准确率约 50–65%，未见接近天花板；BBQ 指标也围绕 50–60%，饱和风险不实际存在。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；输出格式要求只是为了获得最终答案，未按指令约束类型测量准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p5: CoT elicited with 'Let’s think step by step' plus 'additional instructions about formatting final answers'; p7 footnote: models occasionally predict both choices and this is treated as Unknown. | 存在最终答案格式约束和后处理规则，但未报告格式合法率、重试策略，也未把格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 研究不是安全/越狱评估，没有对抗攻击成功率或自然提示拒绝率。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文属于 LLM 解释忠实性与 AI 安全评估，不主张把 LLM 作为心理学/认知科学被试来测量人类同名构念，也未做人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模或训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有以代理指标为优化目标进行训练、RL 或 best-of-N 优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5 names 'text-davinci-003 (GPT-3.5)' and 'claude-v1.0'; p6 reports confidence intervals and paired difference tests; p4 provides GitHub code/data link; no repeated inference N, exact snapshot dates, or raw logs. | 报告了模型版本、置信区间、配对比较和代码链接，但未报告每个分数的重复采样 N、精确 API snapshot、逐题日志或模型比较的配对 bootstrap/McNemar 细节。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮提示，没有多轮对话历史累积。 |

## 编码小结
论文对 CoT 解释不忠实性提供了清晰的多任务、多条件证据，但研究本质是 LLM 基准评测而非人类心理实验，许多人类被试分配/顺序/量表组件不适用。设计与结果报告较透明，但统计模型、提示版本、采样重复、预注册、项目随机效应和心理测量信效度等方面报告有限。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
