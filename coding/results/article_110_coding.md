# article_110 | Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral | 2025

研究类型概述：该文以构建 UniMoral 多语言道德推理数据集为核心，并在此基础上对三个 LLM 在四种任务（行动预测、道德类型分类、因素归因、后果生成）上进行零样本/少样本基准评测。人类标注者用于提供行动选择、道德原则、归因因素、后果及 MFQ2/VSM 画像；LLM 条件为模型、语言、情境线索和场景来源，分析单位主要是聚合后的语言×模型×线索×任务分数，而非人类被试的随机分组实验。
- **研究构念（Construct）**：跨语言、跨文化道德判断与道德因素归因｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：该文以构建 UniMoral 多语言道德推理数据集为核心，并在此基础上对三个 LLM 在四种任务（行动预测、道德类型分类、因素归因、后果生成）上进行零样本/少样本基准评测。人类标注者用于提供行动选择、道德原则、归因因素、后果及 MFQ2/VSM 画像；LLM 条件为模型、语言、情境线索和场景来源，分析单位主要是聚合后的语言×模型×线索×任务分数，而非人类被试的随机分组实验。｜CA 任务锚定：道德困境任务（Moral Dilemma Task, `trm_57ebe6583f52d`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.7: 'The four attributes (m, c, p, f s) serve as inputs to three different LLMs'; PDF p.18-19 给出多种条件的 prompt 模板。 | 模型、语言和情境线索可视为基准中的受控输入条件，水平与标签有报告；但没有操纵检验，也没有说明条件分配/随机化程序，故仅部分满足。 |
| A2 | 因变量 | 0.5 | PDF p.7: 'Weighted F1-score acts as our primary metric'; 'we use multilingual BERTScore'; PDF p.20 Table 7 还报告 BLEU、METEOR、BERTScore。 | 因变量指标与计分方式基本明确，但未报告指标信度/效度证据，也未说明连续指标预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | PDF p.21: 'we set all random seeds in Python to be 42... max generation length as 2000 tokens, rest all settings are default'; PDF p.4 说明翻译人工核验。 | 报告了部分控制手段（随机种子、生成长度、默认设置、翻译核验），但没有系统列出控制变量清单及逐项控制方式。 |
| A4 | 混淆变量 | 0.5 | PDF p.8: 语言差异被归因于 'availability of high-quality training data and linguistic complexity'; PDF p.10: 'automated translation ... may miss subtle cultural and linguistic nuances'。 | 识别了跨语言资源、翻译和文化差异等潜在混淆，但没有控制方式或敏感性分析，残余混淆对内部效度的威胁未系统评估。 |
| A5 | 调节变量 | 0 | PDF p.7: RQ III 提出 'how do these factors interact across languages?'；PDF p.8 仅分别报告 language-specific 与 contextual-cue-specific 结果。 | 文中提出跨语言交互问题，但没有定义调节变量、没有交互项检验或简单斜率分析；因此核心交互检验未做。 |
| A6 | 中介变量 | NA | — | 论文没有中介假设，也没有直接/间接效应分解，故本组件不适用。 |
| A7 | 操作性定义 | 1 | PDF p.5 列出标注问题 1–7；PDF p.7 给出 AP/MTC/FAA/CG 的形式化定义；PDF p.17 A.4 说明 MFQ2/VSM 计分；PDF p.18-19 提供提示模板。 | 关键构念（行动选择、道德原则、因素、后果、道德/文化画像）均有可重复执行的操作化、计分或提示程序。 |
| A8 | 水平数与类型 | 0.5 | PDF p.7: 三个模型与四个线索 (m, c, p, f s)；PDF p.1/4: 六种语言；Table 1 给出各语言实例数。 | 报告了各因素的水平数与取值/标签，但未说明水平类型（名义/连续）、间距、全距或连续变量中心化处理。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p.7: 用 AP、MTC、FAA、CG 四个任务衡量道德推理；PDF p.20 Table 7 对 CG 报告 BLEU、METEOR、BERTScore。 | 关键构念在多个任务/指标上有操作化，但没有报告各操作之间的会聚证据；局限性部分也未具体讨论单一操作化的可推广性边界。 |
| A10 | 单一方法的风险 | 0 | PDF p.5-6: 同一批标注者先完成场景评价，再填写 MFQ2 与 VSM；PDF p.10 未讨论共同方法偏差。 | 人类标注端道德/文化画像与场景评价来自同一标注者同源测量，且未报告共同方法偏差的程序控制或统计检验（与 E7 一致），记 0。 |
| B1 | 被试间设计 | NA | — | 没有人类被试被随机分配到互斥条件；LLM 也不是按被试间方式分配到单一条件，而是对所有固定条件做评测。 |
| B2 | 被试内设计 | NA | — | 没有需要顺序平衡的重复测量心理实验；LLM 提示评测不构成带顺序平衡的被试内设计。 |
| B3 | 混合设计 | NA | — | 没有混合设计，也没有逐因素标注组间/组内并分别报告误差项的统计模型。 |
| B4 | 因子设计 | 0 | PDF p.7: 报告三模型与四线索；PDF p.20 Tables 4–6 给出模型×语言×线索的描述性分数。 | 多因素条件事实上完全交叉，但论文只做描述性汇总，未报告因子设计矩阵、每格样本量、ANOVA 主效应或交互项。 |
| B5 | 主效应 | 0 | PDF p.8: 'English consistently ranks among the highest-performing languages...'; 结果以均值/加权 F1 呈现，未给 F、df、p 或效应量。 | 没有报告各因素主效应的正式统计检验与效应量，仅有描述性比较。 |
| B6 | 交互作用 | 0 | PDF p.8 分别描述 language-specific 与 cue-specific 表现；未报告任何交互项检验或简单主效应。 | 完全忽略交互项的统计检验，不能据以判断跨语言/线索的调节模式。 |
| B7 | 区组设计 | NA | — | 没有区组/分层设计，也没有区组变量与区内随机分配。 |
| B8 | 拉丁方 | NA | — | 没有被试内顺序设计，也未使用拉丁方平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；没有非随机分组后的因果效应声称与选择偏差讨论。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理条件，因此不存在处理可逆性/迁移对称性的适用条件。 |
| C1 | 随机化 | NA | — | 基准评测对所有模型/语言/线索固定评估，没有随机分配或分配隐藏机制。 |
| C2 | 平衡 | NA | — | 没有条件顺序需要平衡，因而没有平衡层级或各顺序被试分配。 |
| C3 | 恒定 | 0.5 | PDF p.21: 'random seeds ... 42', 'max generation length as 2000 tokens, rest all settings are default', 'Hugging Face Transformers 4.43.3 and PyTorch 2.4.0'。 | 报告了若干恒定设置和环境，但没有逐一列出所有关键生成参数，也未讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计（配对、频数匹配或 PSM），也无匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 没有需要盲法的人类被试/实验者/评分者条件分配；标注平台自动呈现任务。 |
| C7 | 平衡的层级 | NA | — | 没有顺序平衡层级可选择。 |
| D1 | 练习效应 | NA | — | LLM 各提示相互独立，无上下文内练习；人类标注虽含多个场景，但不是跨条件重复测量设计。 |
| D2 | 疲劳效应 | NA | — | 没有跨条件 session 疲劳设计或条件时间分散方案。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM 每条件独立提示，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件迁移对称性检验的需要。 |
| D5 | 范围效应 | NA | — | 没有被试内绝对判断/量表范围效应设计；跨语言 Likert 反应风格问题在 E3 中处理。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF p.7: AP 在 '(a1, a2)' 中选择；PDF p.19 提示固定为 'Selected action is <a or b>'，未报告选项顺序随机化。 | 行动选项和类别选项按固定顺序呈现，没有反平衡或随机化，也没有讨论顺序效应。 |
| E2 | 默认赞同 | 0 | PDF p.5: 道德原则与因素采用 1–5 Likert 评分；PDF p.17 A.4 说明 MFQ2/VSM 采用五点量表。 | 使用 Likert 量表，但没有报告反向计分题、正反向题一致性或默许偏差讨论。 |
| E3 | 极端 / 中间反应倾向 | 0 | Figure 2c/2d 以均值展示各语言在因素、道德/文化价值上的差异；未报告偏度、端点/中点使用比例或反应风格校正。 | 进行了跨语言 Likert 比较，但没有报告分布形态，也没有讨论或校正极端/中间反应倾向。 |
| E4 | 需求特征 | 0 | PDF p.5-6 描述 Prolific/Potato 标注流程与知情同意；未报告掩饰情节或事后访谈检查需求特征。 | 标注任务目的较明显，参与者可推断研究关注道德决策，但论文没有掩饰情节或事后推断比例检查。 |
| E5 | 实验者效应 | NA | — | 数据收集由 Potato/Prolific 自动呈现，无人类主试或评分者条件期望传递；LLM 评测也由脚本自动完成。 |
| E6 | 天花板 / 地板效应 | 0.5 | Tables 4–7 与 Figure 4 报告各任务的平均 weighted F1/BERTScore；PDF p.8 提到随机表现虚线，但未报告 SD、偏度或端点频率。 | 提供了均值层面的描述统计，可用于粗略排查，但缺少标准差、偏度、端点频率及 pilot 难度校准说明。 |
| E7 | 共同方法偏差 | 0 | PDF p.5-6: 同一批标注者先完成场景评价，再填写 MFQ2 与 VSM；PDF p.10 未讨论共同方法偏差。 | 道德/文化画像与场景评价来自同一标注者自评，但没有程序控制或统计检验来评估共同方法偏差。 |
| F1 | 统计结论效度 | 0 | Tables 4–7 只报告 weighted F1、BLEU、METEOR、BERTScore 点估计；未见样本量功效依据、置信区间、多重比较校正。 | 主要分析只报告性能点估计和零星“高于随机”描述，未报告 CI、效应量、功效分析或多重性校正。 |
| F2 | 内部效度 | NA | — | 研究为数据集构建与基准评测，非随机分组实验；缺少随机分配/分配隐藏并不构成该实验内部效度组件的适用情形。 |
| F3 | 构念效度 | 0.5 | PDF p.3-5 依据 MJI/DIT/MCT、MFQ2、VSM 等理论工具；PDF p.6: 'Each scenario was reviewed by three annotators'，但未报告标注者一致性或量表信度。 | 有理论基础和既有问卷来源，属于部分构念效度证据；但没有报告信度、标注者间一致性、效度统计或操纵检验。 |
| F4 | 外部效度 | 0.5 | PDF p.10 Limitations 说明仅六种语言、Prolific 参与者与非全球代表性；PDF p.16 A.3 与 Figure 7 报告参与者来源与国籍分布。 | 报告了样本来源与部分代表性限制，但没有系统给出抽样框、纳入排除标准、跨情境复现或明确推广边界。 |
| G1 | 分析单位 | 0.5 | Table 1 显示每种语言 '3 Ann/sc'；PDF p.8 的结果按语言/线索/模型聚合，未说明实例、标注者、场景的嵌套处理。 | 存在标注者/场景聚类结构，但统计只做聚合比较，未明确处理分配层级与分析层级的匹配，也未使用多层模型。 |
| G2 | 随机效应 | 0 | Tables 4–7 与 Section 4.2 仅报告固定模型/语言/线索的聚合结果；没有随机效应或混合模型说明。 | 未说明哪些因子作随机效应；场景/标注者等聚类方差没有从误差项分离，推断可推广总体不清楚。 |
| G3 | 材料作为随机效应 | 0 | PDF p.7-8 将场景-行动对作为评测材料并聚合报告；未使用 item random effect、F′ 或混合模型 (1&#124;item)。 | 有限场景/材料被当作固定刺激处理，结论没有显式推广到材料总体。 |
| G4 | 统计功效 | 0 | PDF p.21 仅报告随机种子和生成长度；全文未见事前功效分析、目标效应量或置信区间。 | 没有设计阶段功效分析或样本量/重复次数论证，结果也未报告 CI。 |
| G5 | 研究者自由度 | 0.5 | PDF p.10: 'we focus on four exploratory tasks and evaluate existing systems ... without fine-tuning'；Appendix A.7 提供完整结果表。 | 报告了四个任务及附录完整结果，但未报告数据排除规则、样本量决定方式、是否中途追加/停止，也未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未见预注册平台、注册编号或时间戳早于数据收集的分析计划。 | 无预注册，且任务被描述为探索性；未区分预注册验证性与事后探索性分析。 |
| J1 | 位置偏差 | 0 | PDF p.7/19: AP 要求 'Selected action is <a or b>'，MTC/FAA 也按固定选项输出；未报告选项顺序交换或位置翻转率。 | 涉及 LLM 多选项选择，但完全未提及候选位置偏差，未做 A/B 交换或正确答案位置随机化。 |
| J2 | 冗长偏差 | 0.5 | PDF p.8/20: 'LLMs tend to generate longer text when compared with human annotators... we use multilingual BERTScore ... semantic similarity'。 | 识别到生成长度与表层匹配问题，并用语义指标部分缓解；但没有报告长度分布、长度-得分相关或长度对照。 |
| J3 | 谄媚 | NA | — | 任务不涉及用户先验立场、反馈或纠错对话，无法操纵谄媚。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge 或成对偏好评估；CG 使用 BERTScore/BLEU/METEOR 等自动指标。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF p.7: few-shot 示例 'constructed by considering the ethical principle selected by the annotator for another scenario-action pair'；Appendix A.6 给出含一个示例的模板。 | 报告了示例来源和模板，但未说明标签比例/多示例集、排列反平衡或多 seed 重采样；仅单一 few-shot 配置。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.18 A.6: 'All prompts ... finalized from an initial pool ... over a small subset of the English data ... select the best performing prompts'；模板全文给出。 | 提供了完整提示模板和大致选择过程，但没有报告语义等价改写的敏感性消融，也未明确 dev/test 分离。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短场景与选项/示例，没有长上下文或 RAG 设置，不涉及中间迷失或 chunk 排序。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.21: 'random seeds ... 42', 'max generation length as 2000 tokens, rest all settings are default'；未报告 temperature/top-p、重复采样或 CI。 | 报告了随机种子与最大生成长度，但采样超参不完整，且每个条件似乎只运行一次，未估计方差。 |
| J9 | 重复与文本退化 | 0 | PDF p.21 只说明最大生成长度 2000、其余默认；未报告 greedy/beam/sampling、repetition penalty、n-gram 重复率或截断比例。 | CG 属开放生成，但解码策略和退化 QC 均未报告，无法判断重复/退化是否与条件差异混淆。 |
| J10 | 分词效应 | 0 | PDF p.4: 六语言翻译与人工核验；PDF p.21 只给 Transformers/PyTorch 版本，未给分词器 revision 或各语言 token/词数比。 | 研究是跨语言/跨脚本比较，但未报告分词器版本，也未控制 token 数或报告 token/词数比，语言效应可能与分词效率混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.3-4 说明数据来自心理理论、Reddit 与 Llama 生成；未报告测试集发布日期与模型训练截止日期对照或污染检测。 | 未做任何污染/数据泄漏检查，不能排除公开来源或生成内容已见于预训练语料。 |
| J12 | 基准饱和 | NA | — | 任务为新构建 UniMoral 数据集，AP/MTC/FAA 分数总体远未接近上限，未出现饱和基准上的显著提升宣称；该组件不适用。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循约束，而是行动选择、分类、归因与后果生成；未设置指令遵循准确率评估。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p.19 提示要求 'Strictly give your answer using the following format: "Selected action is <...>"'；但未报告格式合法率、解析失败/重试策略。 | 实验要求结构化/严格格式输出，报告了约束设置；但没有把格式失败与内容错误分开报告，也没有格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全性、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.7: 'we test whether an LLM ... can replicate their decision-making process'；PDF p.3 以 Rest/Haidt 等人类道德推理理论构建 pipeline；PDF p.9 讨论 LLM 与人类可能不同。 | 有把 LLM 行为解释为道德推理的构念讨论和人类标注对照，但未系统论证 LLM 构念与人类同名构念的等价性，也未做同范式人类实验对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的能力曲线，也没有“涌现/突变”宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N 或对代理指标的优化环节；只是对现有模型做固定评测。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.21 报告 seed=42、max generation length=2000、模型名与 HF/PyTorch 版本；Tables 4–7 仅给单点分数，无重复次数、CI 或配对检验。 | 提供部分可复现信息，但缺少精确 snapshot/commit、重复采样 N、置信区间和配对比较，结果可复现性有限。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 所有评测提示为单轮输入，没有对话历史累积，也不主张多轮部署。 |

## 编码小结
论文的主要贡献是数据集与多语言基准，而非严格的人类心理实验或 LLM 心理学被试实验。其优点是任务与操作化较清楚、提示模板有一定公开、结果表较完整；不足是缺少正式交互/主效应统计、随机化/平衡、答案位置控制、重复采样与置信区间、信效度与标注者一致性报告，且跨语言比较未控制分词/资源差异。多数人类实验设计组件不适用于该基准评测，但 LLM 评测中的提示敏感性、少样本、位置偏差、格式约束、可复现性等风险应被识别并编码。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 A10（NA→0）。
