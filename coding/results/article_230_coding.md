# article_230 | RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style | 2025

研究类型概述：这是一项面向 LLM 奖励模型的基准构建与评测研究，而非以人类被试为对象的实验。研究构造了带风格控制（简洁、详细、Markdown）与正确/错误响应配对的 RM-Bench 数据集，在 Chat、Code、Math、Safety 四个领域上评测近 40 个奖励模型，并分析奖励模型分数与策略模型表现的相关性。分析单位主要是提示—响应配对、领域/风格条件下的准确率以及模型层面的相关性。
- **研究构念（Construct）**：奖励判断中的细微内容辨别、风格干扰与偏好偏差｜CA 构念锚定：语言产生（language production, `trm_4a3fd79d0a78d`）；语言理解（language comprehension, `trm_4a3fd79d0a775`）
- **实验任务与范式（Task / Paradigm）**：向公开reward model呈现内容正确但风格较弱与内容错误但更长或格式更强的回答对，要求其给出偏好，并在聊天、安全、数学和代码域比较。（操纵内容正确性、回答长度、Markdown格式、领域、难度和reward model类型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.5: 'considering two style features: Length and Markdown formatting... y∅: Short... yL: Detailed... yL,M: Detailed... with Markdown'; p.3-5 describes chosen/rejected construction. | 风格与正确性条件被明确构造为基准操纵，给出了三个风格水平及生成程序；但没有随机分配说明与操纵检验，故为0.5。 |
| A2 | 因变量 | 0.5 | PDF p.3 Eq.(5): 'Accuracy = ... I[Rψ(x,yc)>Rψ(x,yr)]'; p.6 defines Easy/Normal/Hard Accuracy and domain metrics. | 因变量指标和计分方式明确，且有与政策模型表现的相关性作为效度证据；但缺少奖励模型准确率的信度、置信区间和连续指标误差控制说明。 |
| A3 | 控制变量 | 0.5 | PDF p.9: 'All datasets are sampled to 60k examples to ensure comparable training data size. The policy models are trained using PPO... with the same training data and hyperparameters'; p.5 style-controlled generation. | 报告了若干控制手段（同生成模型、同训练数据量、同PPO超参数、内容保持的风格转换），但未系统列出控制变量清单及逐一控制方式。 |
| A4 | 混淆变量 | 1 | PDF p.15 Appendix C: 'Potential Bias Introduced by GPT-4O... none of the tested reward models are based on gpt-4o'; p.15 Appendix A discusses 'Limited Coverage of Bias Types' and 'Limited Correlation with Policy Models'. | 明确识别了生成模型风格偏差、未覆盖的风格偏差类型及相关性推广限制，并说明部分控制与残余威胁；符合1。 |
| A5 | 调节变量 | NA | — | 理论模型不包含调节变量，也没有调节/交互假设检验。 |
| A6 | 中介变量 | NA | — | 理论模型不包含中介变量，未进行直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | PDF p.3-5: detailed construction of chosen/rejected responses per domain; p.5 style-controlled generation; p.3 Eq.(5) scoring. | 对细微错误、风格偏差、Easy/Normal/Hard 指标及奖励比较计分给出了可复现的操作化程序。 |
| A8 | 水平数与类型 | 0.5 | PDF p.5: three style levels y∅, yL, yL,M; p.3 four domains Chat, Code, Math, Safety; p.5 Table 2 reports token statistics. | 报告了风格水平/标签和领域类别，但未明确说明水平类型、间距/全距等；对连续变量中心化也不相关。 |
| A9 | 单一操作化的风险 | 1 | PDF p.5: uses Length and Markdown as two style operations; p.6-7 reports Easy/Normal/Hard accuracy across models; p.15 acknowledges only two bias types covered. | 关键构念采用了多个风格维度和多指标评测，并讨论了偏差覆盖局限；可给1。 |
| A10 | 单一方法的风险 | NA | — | 刺激/响应由生成模型构造，因变量来自奖励模型评分，构念来源天然不同，不属于同源自评共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 没有人类或被试组接受互斥条件的被试间分配；所有奖励模型在同一固定基准上评测。 |
| B2 | 被试内设计 | NA | — | 奖励模型对全部基准条目评分，但这不是带条件顺序平衡的人类被试内实验；条目独立评分，顺序效应不构成设计组件。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合实验设计，也无对应混合模型误差项。 |
| B4 | 因子设计 | 0 | PDF p.6: 'organize the results into a 3×3 matrix... Style-Substance Evaluation Matrix'; rows/columns are chosen/rejected styles. | 存在风格×风格交叉矩阵，报告了部分单元格准确率；但没有完整设计矩阵、每格样本量和ANOVA主效应/交互统计；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | PDF p.6-7 reports Easy/Normal/Hard and domain accuracies, but no F/df/p/effect-size main-effect tests. | 未报告因子设计意义上的主效应统计检验，仅给描述性准确率。 |
| B6 | 交互作用 | 0 | PDF p.6 Figure 2 gives an example 3×3 matrix, but no interaction F/df/p or simple-effects tests. | 虽展示矩阵模式，但未对交互项做统计检验，也未报告简单效应/多重比较校正。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量及区内随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计，也不以非随机分组因果推断为目标。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理的不可逆性/迁移对称性设计问题。 |
| C1 | 随机化 | NA | — | 基准条目不分配到互斥处理组；所有被测模型都在同一固定测试集上评分，无随机分配环节。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | PDF p.5: gpt-4o used for chosen/rejected; p.5 'decoding temperature t = 1.0' for code/math; p.17 system prompt provided. | 报告了若干保持恒定的生成模型/温度/系统提示，但未系统列出所有恒定变量及其水平，也未完整讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配分配或匹配后均衡性检验。 |
| C5 | 纳入为变量 | 0.5 | PDF p.9: 'All datasets are sampled to 60k examples... same training data and hyperparameters'; p.10 normalizes policy performance by SFT baseline. | 通过采样与统一训练设置控制了部分已知混淆，但未作为协变量/区组进入统计模型，也未检验斜率齐性。 |
| C6 | 盲法 | 0 | PDF p.4: 'Human annotators then verify the chosen and rejected responses' and no blind procedure is reported. | 存在人工核验评分者，但未报告盲法安排、施盲对象或成功检验；故为0。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级可选。 |
| D1 | 练习效应 | NA | — | 每个基准条目独立评分，无练习块或跨试次学习设计。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长/休息安排；奖励模型评测不是疲劳设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件间无跨会话残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移及其对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为准确率/比较判断，不是主观量表绝对评分，无范围效应校准问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 奖励模型对每个响应独立打分后比较，不涉及选项/刺激呈现顺序或位置随机化。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表及跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，也不存在可推断研究假设并配合的需求特征。 |
| E5 | 实验者效应 | 0 | PDF p.4: human annotators verify chosen/rejected correctness, but no blinding, rater training, or standardization is reported. | 主要评分自动化，但存在人工核验评分者；论文未报告盲法层级与标准化培训，故为0。 |
| E6 | 天花板 / 地板效应 | 0 | PDF p.6 Table 3 reports point accuracy and p.7 random baseline; safety domain scores near 95% but no distribution/SD/endpoint-frequency or ceiling discussion. | 只报告均值型准确率，未给出分布形态或端点频率，且安全领域高分未作天花板讨论。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念测量，IV与DV非同一自评来源。 |
| F1 | 统计结论效度 | 0.5 | PDF p.9-10: Pearson r=0.55, p=0.07; p.16 r=0.21, p=0.51; figures show 95% bands. | 报告了相关系数、p值和部分置信带；但缺少样本量/功效依据、准确率指标的CI及多重比较校正。 |
| F2 | 内部效度 | NA | — | 研究以基准评测和相关性分析为主，未做随机分组因果推断；无被试流向/损耗等实验内部效度组件。 |
| F3 | 构念效度 | 0.5 | PDF p.9-10 reports correlation with policy model performance; p.4 human/automatic verification of correctness; no reliability evidence. | 有关联效度和数据正确性核验，但缺少奖励比较准确率的信度、测量误差和系统操纵检验。 |
| F4 | 外部效度 | 1 | PDF p.4 lists prompt sources AlpacaEval/HumanEvalPack/MATH/XSTest; p.15 discusses limitations; p.31 Appendix M replicates with LLaMA-3-8B. | 样本来源、代表性边界和跨模型复现均有报告，符合外部效度要求。 |
| G1 | 分析单位 | 0.5 | PDF p.3 Eq.(5) averages indicator over prompt-response tuples; p.9-10 correlates model-level aggregate scores; no multilevel model for prompts/domains. | 分析单位有配对/条目和模型聚合两个层级，但未显式处理条目嵌套于提示/领域，也未说明分配与分析层级匹配。 |
| G2 | 随机效应 | NA | — | 统计模型未使用随机效应；该研究是将特定奖励模型作为固定评测对象，而非对模型总体做随机效应推断。 |
| G3 | 材料作为随机效应 | NA | — | 提示和响应被视为固定测试集，未以项目随机效应模型推断材料总体；无F1/F2式项目推广分析。 |
| G4 | 统计功效 | 0 | PDF p.9-10 reports r/p without a priori power analysis or sample-size justification; no CI for accuracy comparisons. | 没有事前功效分析或样本量论证，主要比较也给点估计而非完整CI。 |
| G5 | 研究者自由度 | 0.5 | PDF p.4 details filtering/dropping prompts; p.5 Table 2 reports final sample counts; no explicit separation of confirmatory/exploratory analyses. | 报告了数据筛选和最终样本量，但未完整披露所有分析路径、停止规则及验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement or registered analysis plan appears in the paper. | 无预注册；按口径记0，而非NR。 |
| J1 | 位置偏差 | NA | — | 不是LLM-as-judge选择/排序实验；奖励模型分别评分后比较，候选位置不是设计变量。 |
| J2 | 冗长偏差 | 0.5 | PDF p.5 style-controlled length variants; p.5 Table 2 average tokens; p.7 Hard Accuracy reflects style bias; p.8 Figure 3 correctness/verbosity scatter. | 显著关注并控制了长度/格式风格偏差，报告了长度统计与风格鲁棒性指标；但未报告长度与奖励分数的相关系数，也未给裁判温度/人类长度偏好对照。 |
| J3 | 谄媚 | NA | — | 任务中无用户先验立场、反馈纠错或多轮谄媚操纵。 |
| J4 | 自我偏好 | 0.5 | PDF p.15 Appendix C: 'Since our benchmark is largely constructed based on the responses generated by gpt-4o, a reward model built upon gpt-4o may be biased... none of the tested reward models are based on gpt-4o'. | 识别了生成模型与被评模型可能同源的偏好偏差，并说明当前测试模型不含gpt-4o；但未量化同源偏好率、匿名化或异源陪审团。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF p.18 Table 6: 'Total 23 In Context Examples'; p.16 reports many-shot jailbreak success rate 52.1%. | 报告了in-context示例数量与来源流程，但未做多seed重采样、排列反平衡或模板敏感性分析。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.17 Table 5 system prompt; p.18 Table 6 jailbreak prompt; p.30 Tables 18-19 style-control prompts. | 提供了完整提示模板，但无版本号、敏感性消融及dev/test划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短，无长文档/RAG或中间迷失位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.5: 'decoding temperature t = 1.0' for code/math response generation; no seeds or repeated-evaluation CIs are reported. | 报告了部分采样超参，但缺少seed、重复运行次数和置信区间。 |
| J9 | 重复与文本退化 | 0.5 | PDF p.5 reports temperature t=1.0 but no greedy/beam/sampling strategy or repetition/degeneration QC. | 解码温度有报告，但未报告重复率、退化率及条件间解码策略恒定性。 |
| J10 | 分词效应 | NA | — | 单语言/单脚本基准，无跨语言/跨脚本分词效率比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.4 lists test prompt sources (AlpacaEval, HumanEvalPack, MATH, XSTest), but no training-cutoff comparison or contamination detection is reported. | 未评估预训练/微调数据与测试集重叠，也未报告污染率；基准评测下适用，故为0。 |
| J12 | 基准饱和 | 0.5 | PDF p.6 Table 3 reports top scores with random baseline 50%; safety scores up to 95.7 but no saturation/CI discussion. | 报告了基准水位和随机基线，但安全领域接近天花板时未改用连续指标或CI比较，也未讨论饱和风险。 |
| J13 | 指令遵循 | NA | — | 不测量指令遵循能力，因变量是奖励模型偏好/准确率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化输出或格式合法性评估。 |
| J15 | 越狱稳健性 | NA | — | Safety领域评估奖励模型对安全/不安全响应的区分，不是自然拒绝率与越狱攻击成功率的对齐/安全评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 纯工程性奖励模型基准，不主张测量人类心理学/认知构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较2B到340B模型，但不做规模/训练进展能力曲线，也不宣称涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究是基准评测与相关性分析，不涉及以代理指标为目标的优化、RL或best-of-N过优化监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | PDF p.6-10 and Appendix K report point accuracy scores for models; no repeated-run N, confidence intervals, exact snapshots, or paired tests are reported. | 只给单点分数，缺重复次数、CI、精确snapshot和配对比较，故为0。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮/条目独立评测，无多轮对话历史累积。 |

## 编码小结
该论文在奖励模型基准的构念操作化、风格控制数据构造和多模型评测方面较扎实，尤其对长度/Markdown 风格偏差与政策模型相关性有系统报告。但作为基准评测，它缺少对采样随机性、置信区间、模型 snapshot、基准污染、统计多重性/配对检验的完整控制；许多人类实验设计组件不适用。整体上适合评价奖励模型的细微内容辨别和风格鲁棒性，但推断性统计与可复现性报告仍有提升空间。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
