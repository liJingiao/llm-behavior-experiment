# article_189 | LLM Evaluators Recognize and Favor Their Own Generations | 2024

研究类型概述：LLM-as-evaluator/benchmark-style实验：在XSUM与CNN/DailyMail摘要任务上测量GPT-4、GPT-3.5、Llama-2-7b的自我识别与自我偏好；通过监督微调改变自我识别能力，并设置长度、元音数、可读性、always-1、random等控制微调任务，另操纵来源标签正确/反转；辅以20名人类标注者做质量偏好金标准。主要分析单位为模型配置与示例/摘要，统计以聚合分数和Kendall τ为主，未使用多层模型、正式显著性检验或预注册。
- **研究构念（Construct）**：模型对自身文本的来源识别与自我偏好评价偏差｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：把模型自身、其他模型和人类生成的摘要成对或单独呈现给同一现成模型，要求判断来源并选择或评分更好的摘要。（操纵摘要来源、数据集、成对或单独呈现、是否显示真实或错误来源标签以及评价模型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'We use supervised fine-tuning on pairwise examples to alter the LLMs’ self-recognition capability... We use 500 training articles... The remaining 500 articles and associated summaries are used for evaluation.' p.7: 'we additionally fine-tune GPT-3.5 and Llama on three tasks unrelated to self-recognition: length, vowel count, and Flesch-Kincaid readability score... always output the answer “1” and to answer randomly.' | 明确命名并报告了微调任务类型、示例数（0/2/10/500）及控制任务水平，也描述了微调程序；但未报告单位/条件分配机制（非随机被试分配）或独立操纵检验，故为0.5。 |
| A2 | 因变量 | 0.5 | p.3: 'We compute a prediction confidence by normalizing the output probabilities of the tokens associated with the two options.' p.3: 'For self-preference, we prompt the LLM evaluator to rate a given summary with a Likert-scale rating of one to five... weighted by the output probability of each number token.' | 因变量指标（self-recognition/self-preference score）和计分方式定义清楚；但未报告信度、效度、反应时等连续指标预处理或天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | p.3: 'We sample summaries from each of the LLMs at temperature zero... standardize the punctuation and initial capitalization.' p.9: 'all conditions use the same straightforward prompt design.' p.7: 'fine-tune... on three tasks unrelated to self-recognition: length, vowel count, and Flesch-Kincaid readability score.' | 报告了温度固定、提示设计统一及控制微调任务等控制手段；但未系统列出全部控制变量清单及逐一控制方式，故为0.5。 |
| A4 | 混淆变量 | 1 | p.7: 'To confirm that the fine-tuning procedure did not introduce any confounding effect on the variables under study, we additionally fine-tune... on three tasks unrelated to self-recognition... Always 1... Random.' p.7: 'add either correct or reversed labels indicating the source... shows a reversal in self-preference when the labels are reversed.' p.9: 'Controlling for ground-truth generation quality... Our existing results provide indirect evidence for disproportionate self-preference.' | 明确识别了微调混淆、生成质量和来源标签等威胁，并报告控制任务、标签反转和人类评价；同时在局限中承认残余混淆（ground-truth quality未完全控制）。 |
| A5 | 调节变量 | NA | — | 论文未提出调节变量假设，也未进行调节/交互效应检验；模型、数据集等比较不是正式调节分析。 |
| A6 | 中介变量 | NA | — | 论文检验self-recognition与self-preference的相关和因果方向，但未定义或估计正式中介模型，无a/b路径、直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.2: 'Self-preference is when an LLM favors its own outputs... Self-recognition is an LLM’s ability to distinguish its outputs...' p.3: 'Pairwise measurement... Individual measurement...' p.13/15/19: full prompts for summary generation, pairwise and individual measurement. | 对self-recognition、self-preference及微调/测量程序给出了可复现的操作化定义、计分与完整提示模板。 |
| A8 | 水平数与类型 | 0.5 | p.6: 'We train on the two datasets separately but evaluate both in- and out-of-domain... 500 training articles... remaining 500.' p.7: 'eight fine-tuned models for each of the two datasets... Self-Rec (2/10/500)... Always 1... Random... Readability... Length... Vowel count.' | 报告了各条件标签与水平数（示例数、控制任务、数据集），但未系统说明水平类型、间距/全距及连续变量中心化等。 |
| A9 | 单一操作化的风险 | 1 | p.3-4: pairwise与individual两种测量设置并报告结果；p.2-3: 两个数据集XSUM与CNN/DailyMail；p.9: 'Our cross-dataset evaluation provides initial evidence that self-recognition is a general capability...' | 关键构念采用pairwise/individual、两种数据集、多个模型等多种操作化，并报告跨数据集/跨设置的会聚与差异。 |
| A10 | 单一方法的风险 | 0.5 | p.3: 两种核心测量均由LLM提示完成；p.5: 'We conduct human evaluation of pairwise judgment on generated summaries to check if the self-preference shown by LLMs is justified by quality differences.' | 主要IV/DV均来自LLM提示同一方法渠道，作者用人类质量评价作外部校验；但未做共同方法偏差统计检验或系统程序控制。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配；模型配置差异不是人类被试间设计。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量设计；LLM示例虽重复评估，但不是以被试为单位的被试内实验。 |
| B3 | 混合设计 | NA | — | 无人类组间/组内混合设计。 |
| B4 | 因子设计 | NA | — | 研究比较模型、数据集与微调条件，但未建立正式因子设计、设计矩阵或ANOVA交互分析。 |
| B5 | 主效应 | NA | — | 无正式因子设计ANOVA主效应检验。 |
| B6 | 交互作用 | NA | — | 无正式交互项统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；LLM微调比较不按准实验类型编码。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内设计，不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无人类随机分配；模型微调条件为独立模型配置而非将分析单位随机分配到处理条件。 |
| C2 | 平衡 | NA | — | 无被试条件顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.3: 'at temperature zero... standardize the punctuation and initial capitalization.' p.9: 'all conditions use the same straightforward prompt design.' p.9: 'Our preliminary experiments indicate that the strength of both properties are insensitive to prompts.' | 报告了温度、提示、数据集等部分恒定条件；但未系统列出所有恒定变量及水平，也只笼统讨论提示/任务有限的推广边界。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.7: 'we additionally fine-tune... on three tasks unrelated to self-recognition: length, vowel count, and Flesch-Kincaid readability score... Always 1... Random.' | 将长度、元音数、可读性等已知混淆作为控制微调任务纳入比较；但未以协变量/区组进入统计模型，也未检验斜率齐性或报告调整后效应量。 |
| C6 | 盲法 | 0.5 | p.24: 'Each entry includes the original news article and two different versions of summaries. Your task is to pick which one...' Appendix E未报告盲法类型或盲法成功检验。 | 人类标注任务未给出摘要来源标签，可推断具有一定盲法；但论文未明确报告盲法安排、施盲对象或成功检验，故为0.5。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序平衡设计。 |
| D1 | 练习效应 | NA | — | LLM每次提示独立、无上下文内学习；无人类练习效应设计。 |
| D2 | 疲劳效应 | NA | — | LLM无疲劳效应；任务为自动化短提示评估。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM条件独立调用，无跨条件清洗期/残留迁移问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | 0 | p.3: 'For self-preference, we prompt the LLM evaluator to rate a given summary with a Likert-scale rating of one to five...' 全文未讨论范围效应或量表锚定方式。 | individual设置使用1-5评分，存在量表/范围效应风险，但未讨论或采用被试间对照/绝对锚控制。 |
| E1 | 位置 / 顺序偏差 | 1 | p.3: 'To account for the LLMs’ ordering bias... we prompt the LLMs twice for each example by swapping the options, computing the average of the two confidence scores.' p.5: 'GPT-4, GPT-3.5, and Llama reverse their pairwise preferences when the ordering of options is reversed at rates of 25%, 58%, and 89% respectively.' | 对每个pairwise示例进行选项交换并平均，报告了反转率；属于完整反平衡/位置控制。 |
| E2 | 默认赞同 | NA | — | 不是多题Likert态度自陈量表，未涉及反向计分题与默许偏差。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不是人类等级量表跨群体反应风格研究；LLM单题评分不按E3的人类反应倾向编码。 |
| E4 | 需求特征 | NA | — | 主要实验对象为LLM，无人类被试对研究假设的需求特征；人类标注者仅作质量评价。 |
| E5 | 实验者效应 | 0.5 | p.24: '20 crowdworkers recruited from Upwork... For each of the 300 pairwise comparisons, we collect three annotations... Below is the instruction given to each annotator.' p.24: full written instructions; no blind-success check. | 报告了人类评分者人数、书面标准化指令和报酬；但未明确评分者盲法层级、培训/一致性或期望控制。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.16 Table 7报告了多处自我偏好/自我识别分数，如0.912、0.959、0.970等；未报告标准差、偏度、端点频率或pilot难度校准。 | 报告了聚合分数，部分接近上限；但缺少分布形态、端点频率及任务难度校准说明。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；核心为LLM提示测量与人类质量评价，不按E7编码。 |
| F1 | 统计结论效度 | 0.5 | p.7 Table 1: Kendall’s τ correlations. p.27 checklist: 'Experiment Statistical Significance Answer: [No] ... it is unclear if commonly-used significance tests are directly applicable...' | 报告了部分效应量（Kendall τ）与大量聚合分数；但没有置信区间、样本量确定依据、统计显著性检验或多重性校正。 |
| F2 | 内部效度 | 0.5 | p.6: 'We use 500 training articles... The remaining 500 articles... used for evaluation.' p.7: controlled fine-tuning tasks and label reversal; p.9 limitations discuss residual validity threats. | 描述了训练/评估划分与混淆控制，并讨论内部效度威胁；但无随机分配、分配隐藏、基线等价检验或正式被试流向。 |
| F3 | 构念效度 | 0.5 | p.2 defines self-preference/self-recognition; p.5 human evaluation as external quality check; p.6 fine-tuning manipulation; no internal consistency, IRR or formal construct validity statistics. | 构念定义与操作化较清楚，并有部分人类金标准/操纵结果；但缺少测量信度、评分者间一致性及系统效度证据。 |
| F4 | 外部效度 | 0.5 | p.2: '2,000 randomly sampled news articles from two datasets: XSUM and CNN/DailyMail.' p.5: 20 annotators from Upwork. p.9: limitations mention more datasets, tasks, and frontier LLMs in future work. | 报告了数据集与标注者来源及部分推广边界；但样本代表性有限，未报告跨样本复现的完整结果。 |
| G1 | 分析单位 | 0.5 | p.3: pairwise/individual measurements are per example; p.7 Table 1 reports example-level Kendall τ; p.2: scores averaged over dataset. | 说明了示例层级测量与数据集聚合，但未明确处理示例嵌套于文章/模型配置的聚集结构，也未使用多层模型。 |
| G2 | 随机效应 | NA | — | 未使用含随机效应的统计模型；研究主要是聚合描述与相关分析，不按混合模型随机效应编码。 |
| G3 | 材料作为随机效应 | 0.5 | p.2: '2,000 randomly sampled news articles from two datasets...' p.6-7: training/evaluation articles and cross-dataset evaluation; no item random effect model. | 材料/文章被抽样并跨数据集检验，但统计分析未把item/article作为随机效应，未使用(1&#124;item)或准F比。 |
| G4 | 统计功效 | 0.5 | p.7 Table 1报告Kendall’s τ；p.16 Table 7报告聚合分数。全文无事前功效分析、目标功效或样本量推导。 | 报告了部分效应量（相关τ），但缺少事前功效分析/样本量论证及置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.3: summary cleaning/standardization; p.6: 500 train and 500 eval; p.9 limitations; p.16-23 tables report many conditions. No explicit exploratory/confirmatory labeling or stopping rule. | 报告了部分数据清洗/划分规则与多种条件结果；但未报告完整排除规则、样本量决定或验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | 全文与NeurIPS checklist未见预注册平台、编号或分析计划；p.25-31 checklist也未报告预注册。 | 无公开预注册或事先分析计划，且未区分验证性与探索性分析。 |
| J1 | 位置偏差 | 0.5 | p.3: 交换选项并平均；p.5: 'reverse... at rates of 25%, 58%, and 89% respectively.' p.3: model names Llama-2-7b-chat, GPT-3.5, GPT-4; p.13/15/19 prompt templates. | 位置偏差控制与反转率报告较扎实；但缺少人类评分者间信度、精确API snapshot/版本日期及完整裁判模型采样参数。 |
| J2 | 冗长偏差 | 0.5 | p.7: 控制微调任务包括'Length'；p.24 human instruction: 'A longer summary is not necessarily better.' 但LLM评估prompt未明确禁止长度偏好，也未报告长度—得分相关。 | 长度被作为控制任务并给人类标注者提示，但未系统控制LLM裁判的长度偏差，未报告长度与得分关系。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错的多轮对话式谄媚操纵。 |
| J4 | 自我偏好 | 0.5 | p.1: 'self-preference, where an LLM evaluator scores its own outputs higher...' p.5: human pairwise evaluation to check quality; p.7: label experiments show reversal; p.7 Table 1 correlates recognition and preference. | 明确识别并量化同源裁判的自我偏好，并提供人类质量金标准与标签反转证据；但未采用异源陪审团、匿名化输出或报告人类-LLM裁判一致性。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 提示均为zero-shot，无few-shot in-context示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.13/15/19提供完整提示模板；p.9: 'Our preliminary experiments indicate that the strength of both properties are insensitive to prompts, so all conditions use the same straightforward prompt design... future work... more prompt designs.' | 公布了提示模板并称初步测试对提示不敏感；但未做系统敏感性消融、版本化日期或dev/test分离说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为新闻文章加摘要，不涉及长上下文/RAG中间迷失操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.3: 'We sample summaries from each of the LLMs at temperature zero.' 未报告top-p、seed、重复采样次数与置信区间。 | 报告了温度固定，但缺少完整采样超参、随机种子、重复运行与CI；Chat API无snapshot日期。 |
| J9 | 重复与文本退化 | 0.5 | p.3: temperature zero生成摘要；p.13: 清理初始文本、项目符号/编号及尾随标点；未报告n-gram重复率/退化率。 | 报告了解码温度与文本清理，但未系统报告重复/退化的QC指标或生成长度截断比例。 |
| J10 | 分词效应 | NA | — | 单语言英文研究，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.2: 使用XSUM与CNN/DailyMail公开数据集；全文未报告测试集版本日期、模型训练截止日期或污染检测。 | 未识别或评估预训练数据与公开数据/任务之间的潜在重叠，未做污染率检查。 |
| J12 | 基准饱和 | NA | — | 研究不是标准基准SOTA评测，也未宣称基准饱和或显著提升，不按J12编码。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循；无约束指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.15: 'You respond with only “1” or “2” and no other text.' p.19: 'You respond with only "Yes" or "No"' and 'a number from 1 to 5'; 未报告格式合法率或重试策略。 | 报告了严格的输出格式约束，但依赖token概率解析，未报告格式合法率及格式失败与内容错误的分离。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2: 'We follow the prosaic rather than the intentional interpretation... without claiming that the LLMs have any notion or representation of itself.' p.3: model names/versions; no human same-paradigm comparison beyond quality annotation. | 明确说明LLM构念采用prosaic解释，避免直接拟人化外推；但未报告精确权重snapshot，也未做同名人类构念的同范式对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨模型规模/训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对benchmark/reward model/LLM-judge代理指标的优化与overoptimization监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.6: 500训练/剩余评估示例；p.3: temperature zero；p.1代码链接。未报告精确模型snapshot、重复运行N、95% CI或配对检验。 | 提供了代码/提示与示例量，但结果主要是单点聚合分数，缺少重复次数、置信区间、精确API日期与配对比较。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评估，无多轮对话历史或逐轮一致性设计。 |

## 编码小结
研究主题与核心现象（self-recognition与self-preference）界定清楚，位置偏差通过选项交换与反转率报告处理得较好，并通过控制微调任务、标签实验和人类质量评价提供一定因果/混淆控制。但整体是LLM评估实验而非人类被试实验：缺少正式随机分配、功效分析、置信区间、预注册、精确模型snapshot、评分者间信度与严谨的多层随机效应建模；部分人类量表/盲法相关组件仅部分报告或不适用。
