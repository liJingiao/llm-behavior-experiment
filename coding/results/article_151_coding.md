# article_151 | Large Language Models as Analogical Reasoners | 2024

研究类型概述：这是一项关于 LLM prompting 方法的基准评测与消融研究：比较 analogical prompting 与 0-shot、0-shot CoT、few-shot CoT、retrieved CoT 等方法在 GSM8K、MATH、Codeforces 与 BIG-Bench 上的表现。分析单位为基准问题/测试用例及模型-方法组合，不是人类被试实验；无人类被试分配，也无 LLM-as-judge。
- **研究构念（Construct）**：类比推理、从自生成先例迁移解题策略，以及相关与错误先例对推理的影响｜CA 构念锚定：类比推理（analogical reasoning, `trm_4a3fd79d09810`）；流体智力（fluid intelligence, `trm_4a3fd79d0a375`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：GPT-3.5-turbo、GPT-4及现成开源checkpoint在数学、代码和其他推理任务中，先自行回忆/生成若干相关问题及解法，或生成高层知识后再生成先例，随后用这些先例解决目标问题。｜CA 任务锚定：类比推理任务（analogical reasoning task, `trm_4f244f0286947`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p3-6: 方法部分定义 0-shot、0-shot CoT、few-shot CoT、retrieved CoT、self-generated exemplars、self-generated knowledge+exemplars，并给出若干 prompt 模板；p5-6 给出 K 与基线设置。 | 提示方法被明确命名且有两个以上水平，部分操纵程序可复现；但未报告分配方式（所有测试项通常都在各提示条件下评测）与操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p4-5: 'For each problem, we obtain an output from LLMs using a temperature of 0, and report the accuracy'; Codeforces 报告 Acc@1/Acc@10，并说明 'correctness ... whether it passes all test cases'。 | 因变量指标和计分方式有界定（准确率、Acc@k、全部测试用例通过）；但未报告信度/效度证据，也未说明连续指标预处理或天花板/地板处理。 |
| A3 | 控制变量 | 0.5 | p4-5: 数学与 BIG-Bench 使用 temperature 0，Codeforces 采样 10 个输出且 temperature 0.7；p5 固定使用 GPT-3.5-turbo、GPT-4、PaLM 2-L 等模型版本。 | 报告了温度、模型版本等部分控制变量，但未系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p4: Codeforces 仅取 2023 年 Level-A 题以 'prevent test set contamination'；p10: 'LLM performance can be influenced by specific prompt phrases ... our work is also subject to this prompt sensitivity'。 | 识别了污染与 prompt 敏感性等潜在混淆，但未系统控制或做敏感性分析来量化残余威胁，只作有限讨论。 |
| A5 | 调节变量 | NA | — | 论文没有提出调节变量假设，也没有正式的乘积项交互检验；Table 4/5 的规模与 K 分析属于描述性消融，不作为调节模型编码。 |
| A6 | 中介变量 | NA | — | 论文没有提出中介变量或进行直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p3-6 与附录 p17-26 给出各提示方法的完整/半完整 prompt 模板、输出格式与示例；p4-5 定义 accuracy、Acc@k、Codeforces 全部测试用例通过。 | 关键构念（提示方法）有较可复现的操作化，但因变量计分细节（如数学答案抽取规则）未完整写出，故为部分满足。 |
| A8 | 水平数与类型 | 0.5 | p5-6: 比较方法包括 0-shot、0-shot CoT、few-shot CoT、retrieved CoT、self-generated exemplars、self-generated knowledge+exemplars；K=5 for GSM8K, K=3 for MATH/BIG-Bench/Codeforces。 | 报告了多水平提示方法及 K 取值，但没有明确说明水平类型、水平间距/全距或连续变量的中心化处理（提示方法为类别变量）。 |
| A9 | 单一操作化的风险 | 0.5 | p7-9: 在 GSM8K、MATH、Codeforces、BIG-Bench 及多种模型规模上评测；p9 对 50 个正确和 50 个错误样例做定性分析。 | 多任务、多模型结果可视为一定的会聚证据，但缺少构念层面的多种操作化及会聚统计；也未明确讨论单一提示操作化对可推广性的限制。 |
| A10 | 单一方法的风险 | NA | — | 自变量为文本提示，因变量为模型客观输出/准确率，不涉及人类自陈量表同源测量，共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配到条件；基准问题通常在多个提示方法下被重复评测，不属于被试间设计。 |
| B2 | 被试内设计 | NA | — | 虽然同一基准问题可出现在不同提示条件中，但各条件为独立调用，无人类被试内重复测量顺序或跨条件 session；不按被试内设计编码。 |
| B3 | 混合设计 | NA | — | 无组间/组内人类因素的混合设计及对应误差项。 |
| B4 | 因子设计 | NA | — | 非心理实验的因子设计；论文比较提示方法×模型×数据集，但未报告完整设计矩阵、每格样本量与主效应/交互 ANOVA。不按因子设计编码。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机分配。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 无准实验人类分组或因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理可逆性/迁移对称性设计问题。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥条件的程序；基准项通常在各方法下全量评测。单一条件/无分配问题。 |
| C2 | 平衡 | NA | — | 无人类条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p4: 数学任务 'temperature of 0'；p5: Codeforces 'temperature of 0.7' 并固定模型 GPT-3.5-turbo、GPT-4 0613、PaLM 2-L；p10 讨论模型强弱与 prompt 敏感性限制。 | 列出了部分恒定变量及其水平（温度、模型版本、提示模板），但未系统列出全部恒定变量或逐一讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配程序。 |
| C5 | 纳入为变量 | NA | — | 没有将已知混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 无人类被试/人类评分者需要盲法；准确率由自动测试判定。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 每个问题/条件为独立提示调用，不存在跨试次练习效应或同一上下文内学习序列。 |
| D2 | 疲劳效应 | NA | — | LLM API 评测无人类 session 疲劳问题；未涉及长时被试任务。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各提示条件为独立调用，无跨条件清洗期或迁移效应问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移设计。 |
| D5 | 范围效应 | NA | — | 因变量为客观准确率/代码测试通过，不使用主观量表或绝对量值估计。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选项/刺激序列的被试内位置随机化问题；BIG-Bench 答案选项也未作为位置平衡对象报告。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征或掩饰情节问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期待传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p7 Table 1-3、p8 Table 4、p9 Table 5 报告各任务准确率/Acc@k 的均值或汇总百分比。 | 报告了准确率水位，可部分排查端点；但未报告标准差、偏度、端点频率或 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念测量，无共同方法偏差同源问题。 |
| F1 | 统计结论效度 | 0.5 | p7-9 各表报告准确率百分比及方法间差异；p9 报告部分定性计数（如 6/50、9/50、35/50）。 | 报告了性能指标与方法间差值，但无置信区间、事前功效分析、样本量确定依据或多重比较校正。 |
| F2 | 内部效度 | NA | — | 无人类随机分配、分配隐藏、基线等价性检验或被试流向/损耗问题；不按人类内部效度设计编码。 |
| F3 | 构念效度 | 0.5 | p9: 'We manually analyzed the performance ... random sample of 50 correctly and 50 incorrectly solved problems'，并分类为 exemplars irrelevant/incorrect/relevant and correct。 | 提供了定性错误分析作为部分构念/效度证据，但没有评分者信度、正式效度检验或提示操纵检验。 |
| F4 | 外部效度 | 0.5 | p5 报告模型来源与版本；p4-5 报告 GSM8K、MATH、Codeforces、BIG-Bench；p10 讨论更强/更大模型与 prompt 敏感性等边界。 | 报告了数据集与模型来源及部分推广边界，但未系统说明抽样代表性、纳入排除标准和跨样本/跨情境正式复现。 |
| G1 | 分析单位 | NA | — | 分析单位为基准问题/测试用例，提示方法在分析层级上全量应用；无人类或试次级嵌套随机分配结构需要显式多层建模。 |
| G2 | 随机效应 | NA | — | 模型版本被作为固定比较对象，未使用混合模型；论文不主张把模型视为从更大模型总体抽样的随机效应。 |
| G3 | 材料作为随机效应 | NA | — | 基准问题被视为固定评测集，不涉及有限具体材料作为心理学实验刺激的项目随机效应推广。 |
| G4 | 统计功效 | 0 | p.1–28 全文实验设计与结果部分均未报告事前功效分析、目标功效或样本量/重复次数推导依据 | 全文无设计阶段功效分析、目标功效或预期效应量推导；结果仅报准确率百分比，无 CI。 |
| G5 | 研究者自由度 | 0.5 | p17: Codeforces 保留描述在 2000 tokens 内的问题，得到 50 题，并 'conduct the evaluation twice and then report the average results'；p4-9 报告主要任务与消融。 | 报告了 Codeforces 的筛选和重复，但未完整报告所有排除规则、停止规则及所有可能因变量/条件的验证性与探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–28 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 无预注册、注册编号或先于数据收集的分析计划；论文未区分预注册验证性与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM-as-judge、排序或成对候选位置选择；无位置反平衡问题。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判对开放式生成质量打分；评估为任务准确率/测试用例通过率。 |
| J3 | 谄媚 | NA | — | 无用户先验立场或反馈式谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 评估模型输出，因此无自我偏好裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p6: few-shot CoT 使用 GSM8K/MATH 训练集 K=5 个有标签 exemplars，其他数据集使用 K=3 人工标注 exemplars；retrieved CoT 用 Sentence-BERT top K=5。 | 报告了 few-shot 示例来源与数量，但未报告示例排列反平衡、多 seed 重采样或示例选择偏差分析。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p3-6 及附录 p17-26 提供完整 prompt 模板和示例；p10 承认 'our work is also subject to this prompt sensitivity'。 | 完整 prompt 可复现，但没有版本号/迭代日期、系统语义等价敏感性消融或 dev/test 划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短，非长文档/RAG 设置；retrieved CoT 是示例检索基线而非长上下文利用实验。 |
| J8 | 温度与采样随机性 | 0.5 | p4: 数学任务 temperature 0；p5: Codeforces 每问题采样 10 个输出，temperature 0.7。 | 报告了主要温度和 Codeforces 重复采样次数，但缺 top-p/top-k、随机种子、调用 snapshot 细节和均值置信区间。 |
| J9 | 重复与文本退化 | 0.5 | p4-5: 数学与 BIG-Bench 使用 temperature 0，Codeforces 采样 10 个输出、temperature 0.7；p4 讨论模型可能重复生成相同 exemplars，但无定量 QC。 | 报告了解码温度与采样方式，但未报告 repetition penalty、n-gram 重复率/退化率或生成长度截断比例。 |
| J10 | 分词效应 | NA | — | 单语言英文任务，无跨语言/跨脚本分词效率比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p4: Codeforces 使用 2023 年题 'to prevent test set contamination'；p5: 模型为 GPT-3.5-turbo、GPT-4 0613、PaLM 2-L。 | 对 Codeforces 做了时间污染控制，但未对 GSM8K/MATH/BIG-Bench 做污染检测，也未系统报告模型训练截止日期。 |
| J12 | 基准饱和 | 0.5 | p7-9 表格报告 GSM8K 约 75-82%、MATH 约 30-37%、Codeforces 约 8-19%、BIG-Bench 约 30-75% 的当前水位。 | 报告了当前准确率水位，但未明确给出基准量程/SOTA 位置、饱和判断或 CI 比较；部分任务水位不高，饱和风险有限。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循准确率；提示中的格式要求并非以可验证指令集为测量对象。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p3-4 与附录 prompt 要求 'Q:'/'A:' 格式和 '\boxed{}' 答案；但没有报告格式合法率或格式失败/内容错误分离指标。 | 报告了输出格式约束设置，但未报告格式合法率、重试/后处理规则，属于部分满足。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文借用人类类比推理作为方法灵感，但研究目标是 prompting 工程与任务准确率，不主张把 LLM 作为心理学被试测量同名认知构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | Table 4 比较不同规模/强度模型，但没有宣称 '涌现/突变'，也不是连续指标与多 seed 的涌现曲线分析。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及以 benchmark/奖励模型/LLM-judge 为代理目标的训练或优化；没有 overoptimization 环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5: GPT-4 'version 0613, accessed in June–September 2023'；p17: Codeforces 'conduct the evaluation twice and then report the average results'。 | 报告了模型版本/部分调用日期和 Codeforces 两次评测，但多数分数无重复次数、无 CI、无配对检验，snapshot 信息也不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮提示，无多轮对话历史累积或跨轮一致性评估。 |

## 编码小结
按 LLM 基准评测编码：提示方法是受控比较条件，但因变量为任务准确率/Acc@k，统计以描述性百分比为主；大量人类被试特有的分配、顺序、盲法、需求特征等组件不适用。J 部分主要涉及 few-shot 基线、prompt 敏感性、采样与可复现性；整体报告有一定透明度但缺少置信区间、系统敏感性消融和完整污染检查。
