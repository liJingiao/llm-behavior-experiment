# article_139 | Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct | 2025

研究类型概述：LLM 行为与机制可解释性研究：以 Llama3-8b-Instruct 与 base 模型为对象，研究自生成文本识别、自我归属判断及 residual stream 中自我识别向量的提取、因果操纵（steering/zeroing/coloring）与控制。主要分析单位为文本、文本对或 trial，而非人类被试；包含多个数据集、呈现范式和 steering 参数条件。
- **研究构念（Construct）**：自我生成文本识别、自我归属判断与模型自我表征｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：在摘要和文本续写域生成模型自身、人类及其他模型文本，以成对和单项呈现要求Llama3-8B-Instruct判断作者归属，并用长度匹配、base模型和跨域测试作控制。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p6：'steering with multipliers in the 3 to 6 range on layers 14-16'；p4：length normalization；p3：balanced assignment of self/other answers to A and B。 | 存在多个主动操纵（呈现范式、长度归一化、steering 方向/层/倍数、zeroing/coloring），但未集中完整报告所有水平取值、单位分配细节和统一操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p3：'accuracy metric simply counts the percentage...'，并捕获 'Yes'/'No' 与 '1'/'2' token 概率；p8 报告部分 mean difference 与 95% CI。 | 因变量指标与计分方式清楚，但缺少正式信度/效度证据，也未系统说明连续指标预处理及天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | p3：balanced assignment and order control；p3：nuisance vector out-projection；p4：length normalization；p7：dummy task control。 | 报告了多项控制变量与控制手段，但非系统清单，且未逐一说明所有额外变量。 |
| A4 | 混淆变量 | 1 | p4 讨论模型利用长度线索并做长度归一化；p5 检验 perplexity；p7 用 dummy task 排除 generic agreement；p10 讨论残余 'undetected identifying tells'。 | 识别了长度、perplexity、表面 tells、generic agreement 等潜在混淆，报告控制方式并讨论残余威胁，符合完整要求。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量、调节假设或交互检验；层/倍数扫描属于机制参数检验，不是理论调节模型。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或中介假设。 |
| A7 | 操作性定义 | 1 | p2-3 详述 Summarization/Continuation、Paired/Individual 范式及 accuracy 计算；p3 描述对比向量提取；p14 给出 A.2 prompt。 | 关键构念（自生成文本识别、 authorship 判断、self-recognition vector）均有可重复的操作化程序。 |
| A8 | 水平数与类型 | 0.5 | p2-3 报告两种呈现范式和四个数据集；p6 报告 layer/multiplier steering 范围；p4 报告长度归一化水平。 | 报告了主要水平与取值，但未系统给出所有水平类型、间距、全距及连续变量中心化/标准化说明。 |
| A9 | 单一操作化的风险 | 1 | p2 使用四个数据集与两种呈现范式；p32 Table 6 报告跨数据集向量 cosine similarity（如 CNN-XSUM=0.90）；p8 报告相关证据。 | 关键构念采用多种任务、数据集和两个范式，并报告跨操作会聚证据（向量相似性、Tuned Lens、跨数据 correlations）。 |
| A10 | 单一方法的风险 | NA | — | 研究使用客观 token 概率与模型激活，不是自陈式多构念测量；人类心理学意义上的共同方法偏差框架不适用，相关表面混淆已在 A4 处理。 |
| B1 | 被试间设计 | NA | — | 没有人类或独立模型被试分配到互斥条件；同一模型和文本在多个条件内被重复评估，不构成被试间设计。 |
| B2 | 被试内设计 | 0.5 | p3：'The model is shown each pair of texts twice... once with its own text first and once with its text second'；p6 同一文本进入不同 steering 条件。 | 确有重复测量/重复评估结构并报告了成对顺序交换，但未将文本或模型作为随机效应，也未完整报告所有条件的顺序平衡。 |
| B3 | 混合设计 | NA | — | 没有逐因素标注组间/组内的混合设计，也没有对应混合模型和两类误差项。 |
| B4 | 因子设计 | 0 | p6 Figure 3 与 p7 Figure 4 展示 layer × multiplier 的 steering effectiveness 网格，并在多个数据集上比较。 | 存在层×倍数及数据集的因子式扫描，但没有完整设计矩阵、每格样本量、ANOVA 表或效应量，故仅为部分满足；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | p4 比较长度归一化前后 accuracy；p5 比较 chat/base model；p6 指出 layer 14-16、multiplier 3-6 最有效。 | 报告了若干主效应式比较和趋势，但缺少正式 F/df/p/效应量的主效应检验，也未在交互显著时系统限定解释。 |
| B6 | 交互作用 | 0 | p6-7 Figure 3/4 显示 steering effectiveness 随 layer 与 multiplier 变化，并说明 layer 16 峰值与高倍数退化。 | 展示了 layer × multiplier 的交互式模式，但未报告正式交互统计检验、简单主效应或多重比较校正；因未报告交互项的正式统计检验结果，按级联规则基本要件未达成记 0。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量、区组划分或区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方平衡被试内条件顺序。 |
| B9 | 准实验设计 | NA | — | 研究不是无法随机分配的准实验；主要操纵通过模型内部向量干预实现。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理的不可逆性/迁移对称性设计问题；LLM 调用为独立 prompt。 |
| C1 | 随机化 | NA | — | 没有独立分析单位被随机分配到互斥处理条件；文本/ trial 在同一模型内跨条件重复，随机化分配机制不适用。 |
| C2 | 平衡 | 0.5 | p3：each pair shown twice with own text first/second；p3：balanced assignment of self/other answers to A and B。 | 报告了成对位置和 A/B 选项的平衡，但未报告每种顺序的分配数量、完整平衡层级或迁移对称性论证。 |
| C3 | 恒定 | 0.5 | p3 固定使用 Llama3-8b-Instruct；p2 固定多个数据集与任务；p3 对 prompt 做少量工程化。 | 报告了部分恒定控制（模型、数据集、prompt 流程），但未系统列出所有恒定变量及水平，也未讨论其外部效度限制。 |
| C4 | 匹配 | 0.5 | p4：'experimenting with filtering... and with trimming all texts to a set character length'；p3 QA 选择中等长度且排除 self-referential/profanity。 | 有长度匹配/裁剪式控制，但未按正式匹配方法报告匹配后均衡性检验或回归假象讨论。 |
| C5 | 纳入为变量 | 0.5 | p13 Table 3 报告 perplexity 相关；p19 Figure 8 用长度比预测概率并报告 logistic odds ratio；p3 nuisance vector 去除表面成分。 | 把长度、perplexity 等已知混淆纳入补充分析，但未在主模型中作为协变量并检验斜率齐性/调整后效应量。 |
| C6 | 盲法 | NA | — | 数据收集与评分完全自动化，无人类被试、主试或人类评分者需要盲法。 |
| C7 | 平衡的层级 | 0.5 | p3 报告成对文本两种顺序及 A/B 平衡；未给出正式 ABBA/拉丁方层级或顺序效应形状假设。 | 有基本顺序控制，但未明确平衡层级、构造方法及顺序效应假设。 |
| D1 | 练习效应 | NA | — | LLM 以独立 prompt 调用为主，没有人类被试跨试次学习意义上的练习效应安排。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长或疲劳问题；模型调用不涉及休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同条件为独立 prompt/生成，不存在跨条件药物或学习残留；未设计清洗期。 |
| D4 | 不对称迁移 | NA | — | 无跨条件残留迁移问题；LLM 每次调用不共享上下文记忆。 |
| D5 | 范围效应 | NA | — | 主要指标为 token 概率/激活/行为选择，不是主观量表绝对判断，范围效应框架不适用。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p3：'balanced assignment of self/other answers to A and B'；p3：each pair shown twice with own text first/second；p9 A.9 讨论 letter/order 偏好。 | 对选项和成对文本位置做了基本平衡，但未系统报告位置×正确率、翻转率或所有 steering 实验的呈现顺序控制。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同计分问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 不是人类被试，人类需求特征/掩饰情节框架不适用；任务指令本身是操作的一部分而非人类需求特征。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试或人类评分者，故无实验者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p6 Figure 3 报告部分条件 '100% effectiveness'；p6 Table 1 accuracy 约 50-66%；p9 zeroing 将 claims 从约 50% 降到 under 30%。 | 报告了部分端点频率/百分比，但未系统给出分布形态、偏度、试次端点比例或 pilot 难度校准，且 steering 明显存在天花板效应。 |
| E7 | 共同方法偏差 | NA | — | IV 与 DV 主要是模型内部操纵与客观概率/激活，不是同源自评量表；共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p6 Table 1 报告 accuracy 与 p 值；p8 报告 mean difference 与 95% CI、部分 correlation；p2-3 报告样本量。 | 报告了效应量/CI 和部分检验，但无功效分析、无多重性校正说明，也未系统报告所有主要分析。 |
| F2 | 内部效度 | 0.5 | p8 通过 zeroing/steering 做因果干预；p9-10 讨论替代解释与残余 confounds；p3 做顺序/选项平衡。 | 内部效度论证较强，但没有随机分配、分配隐藏、被试流向/损耗等 RCT 式报告，只能算部分满足。 |
| F3 | 构念效度 | 0.5 | p2 明确区分 'true' self recognition 与 'discriminability'；p6 用 steering 作为操纵检验；p32 报告跨数据集向量相似性。 | 有构念界定、操纵检验和多操作化会聚证据，但缺少正式信度（如内部一致性/重测）和系统效度检验。 |
| F4 | 外部效度 | 0.5 | p2 使用四个数据集；p10 讨论结果可能推广到更大模型和其他家族；p30 附 Sonnet 3.5 结果。 | 报告了多来源刺激和若干跨模型/跨数据集结果，但未系统给出抽样代表性、纳入排除标准与明确推广边界。 |
| G1 | 分析单位 | 0.5 | p3：accuracy 基于 '2*dataset size presentations'；p8 在 text/token 上平均并报告相关与 CI。 | 分析单位隐含为文本/文本对/presentation，但未说明分配层级与统计层级匹配，也未处理同一文本重复评估或数据集聚集。 |
| G2 | 随机效应 | 0 | p6-9 主要报告 percentages、p 值、correlations 与 mean differences；未报告任何随机效应模型或 mixed model。 | 没有说明哪些因子为随机/固定效应，也没有将被试式单位或文本项目作为随机效应；对于向文本总体推广的推断不完整。 |
| G3 | 材料作为随机效应 | 0.5 | p2 每个数据集使用约 1000 条文本；p32 用多个数据集构造向量并比较 cosine similarity；但未报告 item random effect。 | 材料被视为来自多个数据集的样本并在多个文本上重复，但分析未使用 item random effect 或准 F/混合模型，只部分满足。 |
| G4 | 统计功效 | 0 | p2-3 报告 1000 texts 等样本量，但无事前功效分析、目标功效或预期效应量来源。 | 没有设计阶段功效分析或样本量推导；结果虽报告部分 CI，但不足以满足 G4 的完整要求。 |
| G5 | 研究者自由度 | 0.5 | p3 报告仅使用 both judgments correct 的 pairs（n=290）、QA 中等长度/排除 profanity/self-reference；p4 报告 trimming；p2-3 报告样本量。 | 报告了多项排除/筛选规则与部分样本量，但未系统列出所有因变量、全部条件和中途停止/追加规则，验证性与探索性分析也未明确区分。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册平台、注册编号或数据收集前分析计划。 | 没有公开预注册；按口径记 0，而不是 NR。 |
| J1 | 位置偏差 | 0.5 | p3：'balanced assignment of self/other answers to A and B'；p3：each pair shown twice with own text first/second；p14 给出多种答案选项措辞。 | 对候选位置/选项顺序做了基本反平衡，但未报告交换前后偏好翻转率、位置×正确率曲线，且缺少采样参数等完整裁判信息。 |
| J2 | 冗长偏差 | 0.5 | p4：Llama3-8b-Instruct 输出更长且模型利用长度；p19 Figure 8 报告 length ratio-probability ratio correlation 与 logistic odds ratio；p4 做 length normalization。 | 长度偏差被明确识别并控制，且报告了长度—判断关系；但缺少裁判温度/采样设置及人类长度偏好对照，故非完整满足。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场、反馈或多轮纠错输入，不涉及谄媚/立场附和操纵。 |
| J4 | 自我偏好 | NA | — | 这里不是用外部 LLM-as-judge 评估生成质量的流水线；模型自身是 self-recognition 任务的行为对象，自我偏好不是作为评审偏差控制的评估设置。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 最终任务 prompt 为零样本；没有 few-shot in-context 示例来源、数量与排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p3：'A small amount of prompt engineering was used'；p14 Appendix A.2 给出多种答案选项模板；p31 A.11 给出无上下文 prompt。 | 提供了部分 prompt 模板与措辞变体，但没有系统敏感性消融、版本号/迭代日期或 dev/test 划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 所用上下文为短文/摘要或 continuation 起始段，远低于长上下文/RAG 场景，无中间迷失或 chunk 排序问题。 |
| J8 | 温度与采样随机性 | 0 | p2-3 描述生成与 log-probability 采集，但全文未报告 temperature、top-p、seed、重复采样 N 或 API snapshot。 | LLM 采样随机性是适用风险，但核心超参与重复采样信息均缺失，记 0。 |
| J9 | 重复与文本退化 | 0 | p7 提到高倍数 steering 可导致 'degenerate output'，但未报告 greedy/beam/sampling、repetition penalty、n-gram 重复率或截断比例。 | 虽观察到退化现象，但未把解码策略与重复/退化率作为受控变量系统报告。 |
| J10 | 分词效应 | NA | — | 研究为单一语言/单一脚本的自生成文本识别，没有跨语言或跨脚本 tokenization 比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p2 使用 CNN、XSUM、DOLLY、SAD 与 Quora QA 等公开/半公开数据集；全文未给出训练截止日期、测试集版本或污染检测。 | 无法排除预训练/后训练数据与这些文本的重叠，未做污染检查或 held-out 证明，按口径记 0。 |
| J12 | 基准饱和 | NA | — | 研究不是标准基准 SOTA 比较；主要指标为自生成文本识别与 steering effectiveness，不涉及基准饱和/SOTA 水位判断。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，也未系统测量约束遵循率；要求输出 A/B 只是任务格式。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p3：模型被要求输出 '1'/'2'、'Yes'/'No'、'A'/'B'；p14 A.2 明确 'Respond only with the letter A or B'。 | 存在结构化/短格式输出约束，但未报告格式合法率、重试策略或格式失败与内容错误的分离统计。 |
| J15 | 越狱稳健性 | NA | — | 论文仅在讨论中推测安全应用，未设置有害请求、越狱攻击或 ASR 评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1-2 将 LLM 自识别与 situational awareness/self-awareness 联系；p2 区分 'true' self recognition 与 'discriminability'；p10 讨论安全与跨模型推广。 | 对 LLM 构念与人类同名构念的关系有部分理论讨论，并报告模型版本，但未做系统的人类同范式对照或完整构念效度论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨规模/训练进展的系统能力曲线；仅在讨论中引用更大模型和 Sonnet 3.5 的补充结果，不足以构成涌现/规模曲线分析。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不以 benchmark、奖励模型或 LLM-judge 为优化目标，也没有 overoptimization/代理指标优化环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p2-3 报告 dataset 样本量（如 1000 texts）与模型名 Llama3-8b-Instruct；p8 报告部分 95% CI；但无精确 snapshot、seed 或重复采样 N。 | 报告了部分 N 与 CI，但模型标识不精确、未报告随机种子/重复运行，也未做配对检验，故部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 prompt 判断，无多轮对话历史累积，也未外推多轮部署。 |

## 编码小结
论文对关键表面混淆（长度、perplexity、选项顺序、generic agreement）有较系统的识别与控制，并通过 steering、zeroing 和 coloring 建立向量与行为的因果联系。但统计建模多为描述统计、简单相关与二项检验，缺少混合效应/项目随机效应、解码超参与随机种子、预注册、多重性校正和正式功效分析；许多人类心理实验设计组件不适用。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B6（0.5→0）, B4（0.5→0）。
