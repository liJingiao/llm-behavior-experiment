# article_205 | Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations | 2025

研究类型概述：这是一项以大型语言模型为认知/机制研究对象的 LLM-as-participant 实验研究：通过神经反馈式 in-context learning 范式，操纵目标激活轴、上下文示例数、层数、任务类型（报告/显式控制/隐式控制）以及模型家族/规模，测量模型报告内部激活标签的准确率、交叉熵，以及控制内部激活的 Cohen's d 效应。研究单位为 LLM 提示/运行配置及由数据集随机抽取的句子，无人类被试。
- **研究构念（Construct）**：对内部激活的元认知监控与控制｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：沿冻结模型残差流的PCA方向生成二元神经反馈标签，给模型若干上下文示例后，要求其报告新输入的激活标签或生成文本以增减该激活方向。（改变PCA目标轴、所在层、解释方差、上下文示例数、报告或显式和隐式控制任务以及模型规模。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_19: 'Our control tasks ... study three orthogonal factors: Layer (l) ... Number of in-context examples (N) ... Target axis'; PDF_PAGE_4 定义 LR/PC 目标轴及 binarization。 | 自变量被明确命名并给出多个水平与标签，也有提示构造程序；但未报告明确的操纵检验，分配方式与部分细节不完整，故为 0.5。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_5: reporting accuracy 与 cross-entropy；PDF_PAGE_19: Cohen's d 公式及 95% CI；PDF_PAGE_6: neural score distributions。 | 因变量指标与计分方式清楚，并报告了 SEM/CI；但没有正式的信度/效度证据或连续指标预处理、防地板天花板说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_19: 'run control experiments 100 times ... sentences randomly sampled'; 'Counterbalanced Label assignment'；PDF_PAGE_4: 使用中位数阈值以保证 balanced labels；PDF_PAGE_17: neutral user messages。 | 报告了若干控制手段（随机抽样、标签反平衡、中性指令），但未系统列出全部控制变量及其控制方式，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_19: 2-by-2 'Counterbalanced Label assignment' 用于控制 'potential confounding factors arising from the LLMs’ response to labels'；PDF_PAGE_20: 报告 off-target control effects；PDF_PAGE_5: 讨论 PC 与 LR 轴相似性。 | 识别并控制了部分潜在混淆，也报告了 off-target 效应；但没有系统讨论残余混淆或敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 论文把 N、轴、层等作为因子式实验变量考察，并未建立明确的调节变量模型，也没有报告乘积项交互与简单斜率，因此该组件不适用。 |
| A6 | 中介变量 | NA | — | 研究没有中介假设或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_4: 公式定义句子嵌入 h̄、投影 a_i 与二值标签 y_i；PDF_PAGE_18-19: 完整 reporting/control prompt 模板及 logit 读出与 Cohen's d 计算。 | 关键构念均给出可观测、可重复执行的程序，包括激活抽取、投影、离散化、提示模板和计分，故为 1。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_19: N ∈ {0, 2, 4, 8, 16, 32, 64, 128, 256}；五个层取 0/25/50/75/100 percentiles；PC_g 的 g ∈ {1, 2, 4, 8, 32, 128, 512}，另有 LR 轴。 | 报告了水平数与具体取值，但缺少明确的水平类型、间距/全距及连续变量中心化说明，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | PDF_PAGE_16: 用 reporting 与 control 两种操作化定义二阶元认知；PDF_PAGE_24: 在四个数据集上复现；PDF_PAGE_5-8: 同时报告 reporting 与 control 结果。 | 关键构念采用了多种任务与数据集操作化，但没有报告各操作间的会聚证据，故为 0.5。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈式多构念测量；神经标签由内部激活计算，因变量为 logits 或控制效应，不适用传统共同方法偏差检验。 |
| B1 | 被试间设计 | NA | — | 无人类被试间分配；LLM 条件为提示/配置层面，并非独立被试组设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量设计；同一模型的不同提示配置相互独立运行。 |
| B3 | 混合设计 | NA | — | 不存在人类组间/组内混合设计及对应混合误差项。 |
| B4 | 因子设计 | 0 | PDF_PAGE_19: 'study three orthogonal factors: Layer ... Number of in-context examples ... Target axis'，并说明每个 (l,n,g) 组合运行 100 次。 | 报告了多因子结构及各组合重复数，但没有完整设计矩阵或含交互项的 ANOVA 表；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | PDF_PAGE_6: 'control effects generally increase with the number of in-context examples'，图 3b 带 95% CI；PDF_PAGE_8: deeper layers 与 larger models 效应更强。 | 报告了各因子的描述性主效应趋势和置信区间，但没有 F/df/p 或完整 ANOVA 主效应表，故为 0.5。 |
| B6 | 交互作用 | 0 | PDF_PAGE_19: 因子被描述为 orthogonal，但结果主要以随 N、layer、axis 的边际曲线呈现；未找到交互项的 F/df/p 或简单效应检验。 | 多因子设计存在但完全未报告交互项统计检验，故为 0。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方被试内顺序设计。 |
| B9 | 准实验设计 | NA | — | 模型家族/规模比较是描述性观察比较，未作为准实验因果设计报告，也无非随机分配与选择偏差讨论框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 不存在人类被试内处理可逆性/迁移对称性设计。 |
| C1 | 随机化 | 0.5 | PDF_PAGE_19: 'We run control experiments 100 times for each configuration ... with sentences randomly sampled from the dataset'；PDF_PAGE_16: 1,200 句随机分为 600/600。 | 有随机抽样与重复运行，但未报告随机数生成工具、种子或分配隐藏，故为 0.5。 |
| C2 | 平衡 | 0.5 | PDF_PAGE_19: 'Counterbalanced Label assignment'，并列出 (i)-(iv) 四种 label/imitate-label 组合。 | 对标签分配做了反平衡，但未报告每种顺序的具体数量及迁移对称性前提，故为 0.5。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_15: 固定 LLaMA 3 与 Qwen 2.5 模型；PDF_PAGE_18: 固定 system prompt；PDF_PAGE_19: 固定层与轴集合；PDF_PAGE_29: 计算资源。 | 多项环境/模型/提示被恒定，但未系统列出恒定变量及其水平并讨论外部效度限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 没有使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为协变量或区组纳入统计模型；标签反应混淆通过设计反平衡控制，而非 ANCOVA。 |
| C6 | 盲法 | NA | — | 完全自动化 LLM 评估，无人类被试/主试/评分者盲法设计。 |
| C7 | 平衡的层级 | 0 | PDF_PAGE_19: 'Counterbalanced Label assignment'，并列出 (i)-(iv) 四种 label/imitate-label 组合。 | 研究存在被试内/序列顺序平衡需求（同 C2），但未明确选用完全平衡、拉丁方或 ABBA 层级，亦未报告构造方法与顺序效应形状假设，记 0。 |
| D1 | 练习效应 | NA | — | 各提示配置独立运行；in-context N 是核心操纵变量而非人类练习效应，故不适用。 |
| D2 | 疲劳效应 | NA | — | LLM 推理无人类疲劳效应与 session 休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同提示/条件相互独立，无跨条件清洗期或残留迁移问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移设计。 |
| D5 | 范围效应 | NA | — | 主要因变量为准确率、交叉熵和激活投影效应，不使用主观量表范围判断。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_4: 'Each sentence is randomly sampled from a given dataset and assigned a discretized label'；PDF_PAGE_19: 每配置 100 次随机抽样。 | 有随机抽样以降低顺序/材料偏差，但未明确报告 in-context 示例呈现顺序的随机化或反平衡方案及各位置次数，故为 0.5。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或事后访谈；LLM 提示指令不构成人类 demand characteristics 设计。 |
| E5 | 实验者效应 | NA | — | 完全自动化模型调用，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_5: Fig. 2c 报告 reporting accuracy 与 cross-entropy 并带 SEM；PDF_PAGE_6: Fig. 3a 报告 neural score distributions；PDF_PAGE_23: ideal observer 上界。 | 报告了均值/分布/置信区间并给出理想观察者上界，但未系统报告偏度、端点频率或 pilot 难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，无共同方法偏差检验需求。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_19: Cohen's d 的 SE 与 95% CI 公式；PDF_PAGE_5-6: accuracy/cross-entropy 曲线带 SEM；PDF_PAGE_36: checklist 声称报告 error bars。 | 报告了效应量与置信区间，但没有样本量/功效依据或多重性校正，故为 0.5。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_19: 随机抽样、100 次重复与 counterbalanced label assignment；PDF_PAGE_16: 600/600 训练-测试划分。 | 有若干内部效度控制，但没有分配隐藏、基线等价性检验或完整被试流向/损耗处理框架，故为 0.5。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_16: 形式化定义 first-order 与 second-order processes；PDF_PAGE_23: ideal observer 上界；PDF_PAGE_24: 四个数据集复现；PDF_PAGE_18-19: 操作化 prompt 与计分。 | 构念定义与操作化较扎实，也报告了跨数据集复现和理论上界，但缺少正式测量信度/效度证据与独立 manipulation check，故为 0.5。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_15: 列出 LLaMA 3 与 Qwen 2.5 系列模型；PDF_PAGE_16: 数据集来源与划分；PDF_PAGE_9-10: 讨论局限与未来推广；PDF_PAGE_24: 跨数据集复现。 | 报告了模型/数据集来源并讨论部分边界条件，但没有代表性抽样或跨人类样本/情境复现，故为 0.5。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_19: 每个配置运行 100 次并随机抽样句子；PDF_PAGE_6: 'each curve is averaged over 100 experiments'；PDF_PAGE_5: 层间平均与 SEM。 | 说明了配置与重复运行层级，但未明确处理句子/运行嵌套结构，也无多层模型，故为 0.5。 |
| G2 | 随机效应 | 0 | PDF_PAGE_19: 每个配置运行 100 次；PDF_PAGE_6: 曲线对 100 次实验取平均；全文未报告随机截距/随机斜率或混合模型。 | 重复运行与句子抽样存在潜在随机效应，但模型未纳入随机效应，故为 0。 |
| G3 | 材料作为随机效应 | 0 | PDF_PAGE_16: 从数据集中随机抽取 1,200 句并划分 600/600；PDF_PAGE_4: 句子随机抽样；分析未报告 item 随机效应或准 F 比。 | 句子/项目被抽样但未作为随机因子建模，结论未显式推广到材料总体，故为 0。 |
| G4 | 统计功效 | 0.5 | PDF_PAGE_19: 每配置重复 100 次以降低方差并报告 CI；PDF_PAGE_5-8: 报告效应曲线与 Cohen's d。 | 有重复运行和效应量/CI，但没有事前功效分析或预期效应量来源，故为 0.5。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_19: 明确列出五个层、N 水平与轴集合；PDF_PAGE_15: 列出模型与数据；PDF_PAGE_29: 计算资源；未报告试次/样本排除规则。 | 报告了主要条件和因变量，但未完整报告排除规则、停止规则及验证性/探索性分析区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | PDF_PAGE_15 仅给出代码仓库；全文没有预注册平台、编号或分析计划。 | 无预注册，故为 0。 |
| J1 | 位置偏差 | NA | — | 研究不涉及 LLM-as-judge 成对比较或多候选项位置操纵；标签从 logits 读出，不是候选排序任务。 |
| J2 | 冗长偏差 | NA | — | 没有用 LLM 评判开放式生成长短并比较质量，故不适用冗长偏差。 |
| J3 | 谄媚 | NA | — | 虽然使用 Sycophancy 数据集作为复现数据之一，但未在评估中操纵用户先验立场或测量谄媚翻转率，故该风险组件不适用。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 评估模型输出，故无自我偏好偏差问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF_PAGE_4: prompt 由 N 个 in-context sentence-label examples 组成；PDF_PAGE_19: N 取值及每配置 100 次随机抽样；PDF_PAGE_4: median threshold 保证 balanced labels；PDF_PAGE_18: 提示模板。 | 报告了示例来源、数量、标签平衡和多次重采样，但未明确报告示例排列反平衡或各示例集 seed 的均值±标准差，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_18: 给出 reporting 与 control 的完整 prompt 模板；PDF_PAGE_4: 描述 prompt construction；未报告 prompt 版本、敏感性消融或 dev/test 划分。 | 模板较完整，但没有 prompt 版本化、语义等价措辞敏感性消融及测试集调参说明，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为最多 256 个短句示例，远低于现代长上下文窗口，且无 RAG 或关键信息首/中/尾位置操纵，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_19: 'run control experiments 100 times for each configuration' 并报告 95% CI；未报告 temperature、top-p、seed 或 API snapshot。 | 有重复运行与置信区间，但缺少采样超参数、种子和精确快照，故为 0.5。 |
| J9 | 重复与文本退化 | 0 | PDF_PAGE_6: explicit control 中 assistant 句由模型 autoregressively 生成；全文未报告解码策略、repetition penalty、重复率或截断比例。 | 显式控制涉及开放生成，但未报告解码策略与文本退化质控，故为 0。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言任务，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_4: 主实验使用公开 ETHICS 数据集；PDF_PAGE_16: True-False、Emotion、Sycophancy 数据集；未报告训练截止日期或污染检测。 | 使用公开基准数据但未评估训练数据重叠/污染，故为 0。 |
| J12 | 基准饱和 | NA | — | 该研究提出新的神经反馈任务而非标准饱和基准，报告准确率也未接近天花板，并提供 ideal observer 上界（PDF_PAGE_23），故不适用基准饱和风险。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；control 成功由神经激活投影测量，而非按约束类型评估指令遵循。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 报告任务直接从 logits 读取 0/1，控制任务为自由文本生成，不涉及 JSON 等结构化输出约束。 |
| J15 | 越狱稳健性 | NA | — | 论文讨论安全含义，但没有越狱/对抗攻击成功率评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF_PAGE_1 脚注声明 anthropomorphic terms 不意味着人类机制等价；PDF_PAGE_16 形式化定义 LLM first/second-order processes；PDF_PAGE_9 讨论与人类元认知/神经科学关系；PDF_PAGE_15 报告模型版本名称。 | 对 LLM 构念与人类同名构念的关系有理论说明和操作化界定，但缺少人类同范式对照，且模型快照不够精确，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文比较模型规模/层深并报告连续 Cohen's d 与 CI，但未宣称“涌现/突变”，故不适用涌现能力指标诱导假象组件。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究为推理阶段评估，不涉及 RL、best-of-N 或对代理指标的优化训练，故不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_19: 每配置 N=100 次重复并报告 95% CI；PDF_PAGE_15: 公开代码仓库与模型名称；未报告 commit hash/API 日期、逐题结果或配对检验。 | 重复次数、CI 和代码较好，但 snapshot 标识不够精确且模型比较未报告配对检验，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF_PAGE_4: 将范式实现为 user-assistant 的 multi-turn dialogue，并给出 N 个 in-context examples；PDF_PAGE_19: 系统改变 N；Fig. 2c 显示性能随 N 变化。 | 有累积多轮上下文与 N 水平评估，但未按轮次独立/累积评分，也未说明上下文截断策略，故为 0.5。 |

## 编码小结
论文提出了清晰且可复现的神经反馈范式，关键操纵与因变量定义较完整，并公开代码与提示模板；主要不足在于统计推断多为描述性效应曲线与置信区间，缺少混合/多层随机效应模型、正式交互检验、功效分析与预注册，且模型快照、解码采样参数、公共数据集污染与部分随机化细节报告不足。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）, C7（NA→0）。
