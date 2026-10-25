# article_232 | Can Large Language Models Infer Causation from Correlation? | 2024

研究类型概述：这是一项 LLM 基准评测与微调泛化研究：构建 Corr2Cause 数据集，比较 17 个现成 LLM，并检验微调模型在原测试集、复述扰动和变量重命名扰动上的表现。分析单位主要是测试样本/模型输出，研究对象不是人类被试。
- **研究构念（Construct）**：从相关关系推断因果结构、可识别性判断与因果方向偏差｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：把不同DAG的相关和条件独立关系文本化，向GPT-3/3.5/4、Llama、Alpaca及NLI模型提出因果关系假设，要求判断假设是否由相关信息支持。（操纵因果图节点数、Markov等价类、因果关系类型、模型和zero/few-shot CoT条件。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p6: 'we evaluate seventeen existing LLMs'; p8: 'Two Robustness Tests ... paraphrasing ... variable refactorization'. | 研究命名了模型/微调/扰动等条件与多个水平，但不是随机分配实验，未报告操纵程序与操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p7 Table 4: 'F1, Precision, Recall, Accuracy'; p14: 'Just answer "Yes" or "No".' | 因变量指标与计分清楚，但未报告信效度证据、置信区间或连续指标预处理。 |
| A3 | 控制变量 | 0.5 | p7: 'using the OpenAI API ... with temperature 0'; p14: 'batch size to be 8' and列出学习率/dropout/weight decay. | 报告了若干恒定设置，但未系统列出控制变量清单及控制手段，也未讨论这些恒定带来的外部效度限制。 |
| A4 | 混淆变量 | 0.5 | p8: 'Two Robustness Tests' to break spurious correlations; p16: PMI analysis of n-grams and variable names. | 识别了模板/变量名等潜在混淆并用扰动检验，但未对残余混淆做敏感性分析或充分讨论内部效度威胁。 |
| A5 | 调节变量 | NA | — | 无调节变量理论模型或交互检验；按关系类型的分层分析不是调节假设检验。 |
| A6 | 中介变量 | NA | — | 无中介变量与直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p4: task function f:(s,h)->v; p5: verbalization of correlations; p6 Table 2 templates; p14 prompt template. | 任务、数据构造、标签生成、模板和模型输入 prompt 均有可复现的操作化说明。 |
| A8 | 水平数与类型 | 0.5 | p5: six causal relations; p6 Table 1/3: N=2 to 6 and split sizes; p7: 17 models. | 报告了多个条件和水平，但未系统说明水平类型、水平间距/全距或连续变量中心化等。 |
| A9 | 单一操作化的风险 | 0.5 | p10: limitations 'limit the causal graphs to two to six nodes' and 'we do not assume hidden confounders'. | 关键构念主要用单一 Corr2Cause 任务操作化；虽在局限中讨论图规模/隐藏混淆，但无多操作会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 不是自陈式同源测量；模型条件与任务绩效指标不是常见共同方法偏差情形。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配到条件的设计。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量及条件顺序平衡设计。 |
| B3 | 混合设计 | NA | — | 无混合设计；模型/测试集比较不是组间×组内被试设计。 |
| B4 | 因子设计 | NA | — | 无随机化因子实验及完整设计矩阵/ANOVA交互表；模型比较是基准评测而非因子实验。 |
| B5 | 主效应 | NA | — | 无因子设计中的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验；按关系类型或扰动的描述性比较不构成交互检验。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果推断设计；论文主要是基准评测，不宣称需按准实验类型报告选择偏差。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内设计，故不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无实验条件随机分配；测试/开发集随机抽样不等同于处理分配随机化。 |
| C2 | 平衡 | NA | — | 无条件顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p7: 'temperature 0'; p14: 'batch size to be 8' and GPU/hyperparameter settings. | 报告了部分恒定设置，但未系统列出所有恒定变量及水平，也未讨论对外部效度的限制。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 无将混淆变量作为区组/协变量纳入统计模型的设计。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人类评分者需要盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | LLM 条件独立评测，无练习块或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳控制；模型评测不涉及休息间隔。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各测试条件分别推理，无跨条件清洗期或残留效应设计。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为二元分类/客观指标，不是被试内量表评定。 |
| E1 | 位置 / 顺序偏差 | NA | — | 不是多选/序列刺激呈现实验；prompt 顺序固定但不涉及候选项或处理顺序平衡。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或掩饰情节。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p6 Table 3: '% Positive Labels 18.57'; p7 Table 4: models' accuracy/F1 and random baselines. | 报告了类别比例和性能分数，但未报告均值/SD、偏度、端点频率或任务难度校准细节。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量；CMB 不适用。 |
| F1 | 统计结论效度 | 0.5 | p6 Table 3: test/dev/train sizes; p7 Table 4: F1/Precision/Recall/Accuracy. | 报告了样本量与主要性能指标，但缺少置信区间、样本量功效依据和多重比较校正说明。 |
| F2 | 内部效度 | NA | — | 非实验性基准评测，无随机分配、基线等价性、被试流向与损耗处理；亦不作人类因果效应推断。 |
| F3 | 构念效度 | 0.5 | p4–p5: formal causal graph/d-separation/MEC construction and label rule; p10: limitations. | 构念效度有形式化任务与标签生成论证，但无测量信度、操纵检验或多操作化会聚证据。 |
| F4 | 外部效度 | 0.5 | p6: dataset splits and N=2–6; p7: 17-model sample; p10: limitations on graph size and hidden confounders. | 报告了样本/模型来源与部分推广边界，但无跨样本或跨情境复现结果，代表性论证有限。 |
| G1 | 分析单位 | 0.5 | p6: test/dev/train split sizes; p7: aggregate model-level metrics over test samples. | 说明了测试样本级评估，但未讨论模型×项目交叉依赖或多层分析单元问题。 |
| G2 | 随机效应 | NA | — | 无人类被试随机效应；模型按固定集合比较，研究目标是这些具体模型而非从 LLM 总体抽样。 |
| G3 | 材料作为随机效应 | 0.5 | p5: graphs generated from unique DAGs/MECs; p6 Table 3: test split over N=2–6. | 项目来自生成图空间并在多个材料上汇总，但分析未纳入 item 随机效应或混合模型。 |
| G4 | 统计功效 | 0.5 | p6: test/dev sizes capped at 1K for computation budget; p7: performance metrics. | 有样本规模与主要性能指标，但无事前功效分析、置信区间或不确定性估计。 |
| G5 | 研究者自由度 | 0.5 | p6: 'we randomly sample up to 1K or 10%'; p7–p9: main models and perturbations reported. | 主要条件与指标报告较全，但缺数据剔除规则、停止规则及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | 全文无预注册平台、编号或数据收集前分析计划的声明；p4–p9 为常规方法/结果报告。 | 无公开预注册，且未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 任务为 Yes/No 判断，不涉及多候选项位置、排序或 LLM-as-judge 成对比较。 |
| J2 | 冗长偏差 | NA | — | 不涉及开放式生成质量评分或 LLM 裁判的长度偏好。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge；评估基于标签匹配指标。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p17 Appendix G: 'a pair of few-shot examples, one positive and one negative'. | 报告了 few-shot 数量与正负比例，但未说明示例来源、排列反平衡、多 seed 或模板全文。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p14 Appendix A给出完整查询模板；p17 Appendix G给出 enhanced query。 | 有 prompt 模板与增强版本描述，但无版本号、敏感性消融、dev/test 划分或 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 输入为短 premise（平均约 424 tokens），无长上下文/RAG 或关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p7: 'temperature 0'; p14 prompt details. | 报告了 temperature=0，但无 top-p/top-k、seed、重复采样次数或置信区间。 |
| J9 | 重复与文本退化 | NA | — | 主要任务是短答案分类，不涉及开放生成退化率评估；自然故事仅为案例展示。 |
| J10 | 分词效应 | NA | — | 单语言英文、单脚本，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p9: 'data we generate is out-of-distribution from the training data of the current LLMs'; p6 data version/dedup. | 给出 OOD 声明与数据版本，但无正式污染检测、n-gram 重叠率或训练截止日期系统对照。 |
| J12 | 基准饱和 | 0.5 | p7 Table 4: random baselines and best off-the-shelf F1 33.38; scores far below ceiling. | 报告了分数范围与随机基线，但未讨论基准饱和、CI 或更难子集策略；该基准当前并未饱和。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；Yes/No 是答案格式而非约束遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p14: 'Just answer "Yes" or "No".' | 报告了输出格式约束，但未报告格式合法率、重试/后处理规则，未分离格式失败与内容错误。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1: 'Causal inference is one of the hallmarks of human intelligence'; p2: 'test the pure causal reasoning abilities of LLMs'. | 以人类智能作动机并测量 LLM 因果推理能力，但未系统论证 LLM 构念与人类同名构念的异同，也无人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告跨模型规模的能力曲线或宣称涌现/相变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无对代理指标/奖励模型的优化循环；微调训练并非以测试基准为优化目标的代理博弈。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p7: 模型名称与 'GPT-4 ... by April 2023'; p6: test set size 1,162. | 报告了部分模型版本/日期与测试集大小，但无重复运行次数、置信区间、精确 snapshot 或配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮问答，无多轮对话历史累积。 |

## 编码小结
论文提出了新的相关性到因果性推断基准，数据构造形式化、任务定义清楚，并系统比较了多类模型、微调与两种扰动。其主要不足在于：基准评测的报告规范仍不完整，缺少置信区间、重复运行、正式污染检测、预注册与若干 LLM 评测敏感性/可复现性细节；大量人类实验设计组件因无人类被试分配/顺序设计而不适用。
