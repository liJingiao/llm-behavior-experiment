# article_193 | Task Ambiguity in Humans and Language Models | 2022

研究类型概述：混合的人类—LLM基准实验：构建AmbiBench六类二分类任务，操纵指令信息性、示例数量、提示格式与模型类型，比较人类与模型识别目标任务准确率，并做小样本微调。分析单位为模型提示/条件与人类被试。
- **研究构念（Construct）**：任务歧义下的意图推断、指令理解和从示例辨识目标任务｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：让人类和现成模型在每个输入同时符合两种分类规则的AmbiBench任务中，根据信息充分或不足的说明和逐渐增加的标注示例推断真正目标。（操纵说明是否提供目标特征、标注示例数量、任务特征组合、呈现格式和被试类型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.6: 'two different levels of instruction: 1. Informative instruction... 2. Uninformative instruction'; PDF p.5: 'Each model is evaluated with 720 different in-context prompts for each level of instruction'。 | 自变量名称、两个指令水平及示例数等程序有报告，但缺少操纵检验；分配和随机化仅部分说明，故为0.5。 |
| A2 | 因变量 | 0.5 | PDF p.6: 'achieve approximately 50% accuracy... output the correct letter'; PDF p.7: 'Error bars show 95% bootstrap CIs'。 | 因变量为分类准确率，计分方式明确；但未报告信度/效度证据及连续指标预处理，故为0.5。 |
| A3 | 控制变量 | 0.5 | PDF p.5: 'The order of the examples, the example format, as well as the assignment of each class to an output letter (X or Y) are randomized'; PDF p.6: 'All aspects of the examples are randomized'；PDF p.4两种提示格式取平均。 | 报告了若干控制手段（随机化、格式平均、模板固定），但未形成系统控制变量清单并逐一说明，故为0.5。 |
| A4 | 混淆变量 | 0.5 | PDF p.8: 'we caution against claims of superhuman performance given that annotators represent merely a sample from a single distribution of humans, and they may have experienced fatigue'; PDF p.9: 'training dataset of these models was not released'。 | 识别了人类疲劳、样本代表性、HFD训练数据不可见等潜在混淆，但未系统控制或做敏感性分析，故为0.5。 |
| A5 | 调节变量 | NA | — | 论文没有正式的调节变量模型或调节假设；模型规模与HFD训练只是描述性模型比较，未做交互检验与简单斜率分析。故不适用。 |
| A6 | 中介变量 | NA | — | 全文无中介变量界定、直接/间接效应分解或因果链检验，故不适用。 |
| A7 | 操作性定义 | 1 | PDF p.4 Table 1给出六个任务及示例；PDF p.20-22 Appendix G给出句子模板、特征取值、提示构造；PDF p.5报告人类输入与作答方式。 | 关键构念（任务歧义、指令信息性、示例数、准确率）均有可复现的操作化程序，故为1。 |
| A8 | 水平数与类型 | 0.5 | PDF p.6列出informative/uninformative两水平；PDF p.6示例数从zero到twenty；PDF p.18 Table 2列出各模型参数量；PDF p.4列出Arrow/Q-A两格式。 | 报告了主要水平数与取值/标签，但未系统标注水平类型、间距/全距及连续变量中心化说明，故为0.5。 |
| A9 | 单一操作化的风险 | 1 | PDF p.9: 'our work studies task ambiguity between two possible tasks—however, in general task ambiguity may occur between arbitrarily many tasks'；PDF p.2讨论真实世界推广。 | 关键构念主要用AmbiBench单一基准操作化，但局限部分明确讨论了仅两种任务和模板化设置对推广的限制，故为1。 |
| A10 | 单一方法的风险 | NA | — | 研究不是同源自陈式多构念测量；自变量为提示操纵，因变量为任务准确率，不涉及共同方法偏差的自评同源问题。 |
| B1 | 被试间设计 | 0.5 | PDF p.5: 'We also recruited a new participant for every single in-context instance'；PDF p.19: 'each participant was only given one set of 20 examples'；PDF p.19给出51、33、96名被试。 | 人类提示分配具有被试间成分并报告样本量，但模型跨条件重复、人类在4.3中跨示例位置重复，并非纯被试间设计，故为0.5。 |
| B2 | 被试内设计 | 0.5 | PDF p.6: 'as the number of examples grows from zero... to twenty'；PDF p.5: 'Models are shown all 20 questions within the same API query'；PDF p.19: 人类逐题作答。 | 存在明确的重复测量/累积示例结构，并随机化示例顺序；但未报告各顺序/位置分配方案与随机效应模型，故为0.5。 |
| B3 | 混合设计 | 0.5 | PDF p.5说明人类每个in-context instance独立招募；PDF p.6说明示例数在0-20内重复；PDF p.7比较人类与模型。 | 研究含组间（不同人类提示/任务）与组内（示例数）成分，但未逐因素标注组间/组内或用混合模型分别报告误差项，故为0.5。 |
| B4 | 因子设计 | 0 | PDF p.6-7 Figure 2/3展示模型×指令/示例数表现；PDF p.8 Figure 4展示ambiguous vs control finetuning。 | 多因素交叉比较存在并报告描述性交互模式，但无完整设计矩阵、每格样本量或ANOVA表；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | PDF p.6: 'humans perform the strongest... closely followed by the text-davinci-003 and text-davinci-002 HFD models'；PDF p.7图示模型/条件差异及95% bootstrap CIs。 | 报告了主要条件差异并给出CI，但无F、df、p或效应量，故为0.5。 |
| B6 | 交互作用 | 0 | PDF p.7: 'HFD training hurts at curie scale, but dramatically helps at davinci scale'；Figure 3带95% bootstrap CIs。 | 报告了HFD×规模的交互式模式，但无正式交互检验、简单效应与多重比较校正；因未报告交互项的正式统计检验结果，按级联规则基本要件未达成记 0。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计；PDF p.9的finetuning三折是按任务划分训练/测试，不是区组随机分配。 |
| B8 | 拉丁方 | NA | — | 研究未使用拉丁方平衡顺序，故不适用。 |
| B9 | 准实验设计 | NA | — | 提示和条件分配采用随机化/随机抽取，不是无法随机分配的准实验设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 研究不是在多个可逆处理条件间做被试内交叉；示例数增加是累积性信息学习过程，未涉及处理可逆性或迁移对称性论证。 |
| C1 | 随机化 | 0.5 | PDF p.5: 'The order of the examples... are randomized'；PDF p.19: 'Prompts given to participants were randomized and roughly evenly distributed'。 | 报告了概率式随机化，但未说明随机数生成工具、分配隐藏或随机化后基线均衡检验，故为0.5。 |
| C2 | 平衡 | 0.5 | PDF p.5: 示例顺序、格式和X/Y映射随机化；PDF p.21: 'order of groupings, order of labels... were randomized... with equal probabilities'。 | 有顺序随机化/平衡意图，但未报告具体平衡层级和各顺序人数，故为0.5。 |
| C3 | 恒定 | 0.5 | PDF p.4两种提示格式并取平均；PDF p.5人类与模型看同样输入；PDF p.19所有问卷用Qualtrics。 | 报告了若干被恒定因素，但未系统列出恒定变量及其水平，也未讨论其对处部效度的限制，故为0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对分配，故不适用。 |
| C5 | 纳入为变量 | 0 | PDF p.18 Table 2列出模型参数量，但PDF p.9指出训练数据未公开；PDF p.8讨论人类可能疲劳但未纳入协变量。 | 已识别的模型训练/规模和人类疲劳等混淆未作为区组或协变量纳入分析，也未调整组间差异，故为0。 |
| C6 | 盲法 | 0 | PDF p.19: 'All surveys were created using Qualtrics' survey builder'；全文未报告盲法安排。 | 未报告对人类被试、主试或分析者的任何盲法安排及实施方式，故为0。 |
| C7 | 平衡的层级 | 0.5 | PDF p.5和p.21报告示例/标签/分组顺序随机化并等概率，但未说明完全平衡、拉丁方或ABBA等层级。 | 有随机化但未明确所选平衡层级、构造方法及顺序效应形状假设，故为0.5。 |
| D1 | 练习效应 | NA | — | 4.3的示例逐个呈现并给反馈是研究中的in-context学习操纵，不是独立练习阶段；没有可分离的练习效应控制问题，故不适用。 |
| D2 | 疲劳效应 | 0.5 | PDF p.9: 'may have experienced fatigue or distraction across the 20-example episode'；PDF p.8: 'human annotators mostly spent between 4 and 8 minutes'。 | 识别了疲劳风险并给出大致时长，但未报告休息间隔、session控制或条件时间分散，故为0.5。 |
| D3 | 延滞 / 迁移效应 | NA | — | 研究不是被试内处理交叉设计；模型每个提示独立，finetuning训练/测试任务分离，无清洗期或跨条件残留问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉处理，故不存在需检验的不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为客观分类准确率/输出合法概率，不是量表式绝对判断，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF p.5: 'The order of the examples, the example format, as well as the assignment of each class to an output letter (X or Y) are randomized'；PDF p.21: 分组、标签和显著特征等概率随机化。 | 对示例/标签顺序做了随机化，但未报告各顺序位置出现次数或翻转率，故为0.5。 |
| E2 | 默认赞同 | NA | — | 不使用Likert或态度自评量表，故默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较，故不适用。 |
| E4 | 需求特征 | 0 | PDF p.5: 'with minimal additional information presented to them before the study began'；PDF p.18仅给出一般性说明，未报告事后推断比例或debriefing检查。 | 未使用掩饰情节/盲法或事后访谈检查需求特征，故为0。 |
| E5 | 实验者效应 | NA | — | 数据采集通过Prolific/Qualtrics和API自动化完成，无人类主试或评分者在场施测，故不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.6: 'humans... perfect performance in all but one task'；PDF p.6: 'many models... approximately 50% accuracy'；PDF p.7提供95% bootstrap CIs。 | 报告了均值/CI并提到端点表现，但无偏度、端点频率或pilot难度校准说明，故为0.5。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，无共同方法偏差的程序/统计检验问题。 |
| F1 | 统计结论效度 | 0.5 | PDF p.7: 'Error bars show 95% bootstrap CIs'；PDF p.5报告720 prompts/条件；PDF p.19报告人类样本量。 | 报告了CI和样本量，但无功效分析、效应量和多重比较校正，故为0.5。 |
| F2 | 内部效度 | 0.5 | PDF p.5和p.19报告提示/顺序随机化；未报告分配隐藏、基线等价性或被试流向图。 | 有随机化但缺分配隐藏/基线/损耗处理，故为0.5。 |
| F3 | 构念效度 | 0.5 | PDF p.3-4描述AmbiBench任务构造；PDF p.17 Figure 7验证输出合法率；但未报告正式信度/效度统计或操纵检验。 | 有任务构造和输出格式验证，但信效度证据与操纵检验不足，故为0.5。 |
| F4 | 外部效度 | 0.5 | PDF p.5: 人类来自Prolific；PDF p.9 limitations讨论模板化、人类样本与两任务限制；PDF p.16给出真实世界附录示例。 | 报告了样本来源并讨论部分推广边界，但无跨样本/跨情境复现，故为0.5。 |
| G1 | 分析单位 | 0.5 | PDF p.5: 'Each model is evaluated with 720 different in-context prompts'；PDF p.19: 96名人类被试；PDF p.6模型在单个API query中看20个示例。 | 说明了提示/被试层级，但未用多层模型显式处理提示、任务或示例嵌套，故为0.5。 |
| G2 | 随机效应 | 0.5 | PDF p.7使用95% bootstrap CIs；PDF p.5将模型作为固定比较对象；未说明随机效应结构。 | 未指定随机截距/斜率或可推广总体；自助CI部分反映抽样变异但非完整随机效应模型，故为0.5。 |
| G3 | 材料作为随机效应 | 0.5 | PDF p.4: 'programmatically constructed from a set of templates'；PDF p.22描述随机生成特征和实例；未报告item随机效应。 | 材料从模板/词表生成并随机化，但分析未把材料/项目作为随机因子，故为0.5。 |
| G4 | 统计功效 | 0 | PDF p.5报告720 prompts，PDF p.19报告人类N，但未给出功效分析、目标效应量或样本量推导；PDF p.7仅给CI。 | 无事前功效分析或样本量论证，故为0。 |
| G5 | 研究者自由度 | 0.5 | PDF p.19报告人类样本量和重复参与过滤；PDF p.15有附录探索性口头报告实验；未报告完整排除规则/停止规则及验证性-探索性区分。 | 部分报告了样本量与过滤，但研究者自由度披露不完整，故为0.5。 |
| G6 | 预先设定 / 预注册 | 0 | PDF p.10仅有Reproducibility statement和代码链接，未提预注册平台、编号或分析计划。 | 无预注册，故为0。 |
| J1 | 位置偏差 | 0.5 | PDF p.5: 'assignment of each class to an output letter (X or Y) are randomized'；PDF p.21: 'order of labels... randomized... with equal probabilities'。 | 对X/Y标签位置和示例顺序做了随机化，但未报告交换前后偏好翻转率或位置×正确率曲线，故为0.5。 |
| J2 | 冗长偏差 | NA | — | 任务输出为X/Y分类标签，不涉及开放式生成长度与质量比较，故冗长偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话操纵，故谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 未使用LLM-as-judge评估模型输出，故自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF p.5使用两个in-context examples；PDF p.6示例数0-20；PDF p.21-22给出示例构造和随机化规则。 | 报告了示例来源/数量/比例与随机化，但未做多seed重采样均值±SD或校准说明，故为0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.4比较Arrow与Q/A两种提示格式；PDF p.17 Appendix D用wug替换测试uninformative措辞；PDF p.20-22提供模板。 | 有模板和部分提示敏感性检验，但缺版本/日期、dev-test分离及系统语义等价消融，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文最多20个短示例，远低于长上下文/RAG设置，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.5: '720 different in-context prompts for each level'；PDF p.7报告95% bootstrap CIs；未报告temperature/top-p/seed。 | 有重复提示与CI，但未报告采样超参和随机种子，故为0.5。 |
| J9 | 重复与文本退化 | NA | — | 主任务只输出X/Y短标签，不涉及开放生成重复与退化；附录A的口头化不是主要条件比较，故不适用。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文、单脚本任务，无跨语言/跨脚本比较，故不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.2: 'we introduce AmbiBench, a new benchmark'；PDF p.10发布代码/数据；但未报告模型训练截止日期或污染检测。 | 新基准虽降低污染可能，但未做测试集版本与训练截止日期对照，也未报告污染率，故为0。 |
| J12 | 基准饱和 | 0.5 | PDF p.6: 'humans... perfect performance in all but one task'；PDF p.7图示模型准确率与CI；未改用连续指标或更难子集处理人类informative条件的天花板。 | 模型整体未饱和，但人类informative条件已接近天花板，论文未做饱和处理，故为0.5。 |
| J13 | 指令遵循 | 0.5 | PDF p.6操纵informative/uninformative instruction；PDF p.6: 'most models are not reliably able to follow simple instructions'；因变量为可判定的X/Y准确率。 | 指令遵循有机器可判定标准，但未按否定/数量/格式等约束类型系统拆分，故为0.5。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p.17 Figure 7报告各模型输出X/Y合法概率；PDF p.6提到部分模型输出Z等非法值。 | 报告了格式合法率并把非法输出作为问题提及，但未报告文法约束/重试策略，且未始终将格式失败与内容错误分列，故为0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全性/越狱评估，无有害请求或对抗攻击设置，故不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.5人类与模型接受尽可能相同的输入；PDF p.7: 'outperform human participants'；PDF p.9 caution；PDF p.18报告参数规模。 | 有LLM—人类同范式对照和构念比较，并谨慎解释；但模型快照/训练阶段不精确，构念异同讨论不系统，故为0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随规模/训练进展的能力曲线或涌现宣称，仅比较已有模型规模，故不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究是基准评估与小样本finetuning，不以benchmark/reward/LLM-judge为优化目标，无代理指标过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.5报告每个条件720个提示；PDF p.7报告95% bootstrap CIs；PDF p.10发布代码；但未给精确API snapshot日期或配对检验。 | 有重复次数和CI，但快照标识不精确且模型比较未做配对检验，故为0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮提示/单次in-context episode，无多轮对话历史累积，故不适用。 |

## 编码小结
研究设计清晰，任务生成、提示格式、示例顺序和标签映射等随机化较细，并提供自助置信区间与人类对照；但统计以描述性比较和自助CI为主，缺少正式交互/混合效应模型、功效分析、预注册以及精确的LLM快照和采样参数。模板化基准、Prolific样本和模型训练数据不可见限制了外部与内部效度。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B6（0.5→0）, B4（0.5→0）。
