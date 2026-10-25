# article_231 | Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics | 2025

研究类型概述：机制可解释性研究：对四个预训练 LLM 的算术电路进行激活替换、线性探测、神经元级消融与启发式分类；分析单位为模型组件/神经元与抽样算术提示，而非人类被试。
- **研究构念（Construct）**：算术问题中的局部启发式组合、策略脆弱性与错误形成｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让现成Llama3模型完成受控两操作数算术题，按可解释启发式识别相关神经元，并比较启发式相关/随机消融及正确/错误题目的策略贡献。（操纵运算符、数字模式、模型规模、启发式相关或随机神经元消融，并比较正确与错误题。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p3: 'we conduct a series of activation patching experiments' and 'replace the activation of a single MLP layer or attention head'; p7: 'knock out all neurons classified into it'; p8: compares 'Heuristic Ablation' with 'Random Ablation'. | 研究主动操纵模型组件/神经元的激活替换与消融，并比较启发式消融、随机消融、不同消融数量等水平；但未以正式自变量表报告分配方式与操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p3 Eq.(1) defines patching effect; p4 Eq.(2) defines faithfulness F(c); p4-p5 linear probe accuracy; p7 accuracy after heuristic ablation. | 因变量指标与计分方式有明确定义（归一化 logit、faithfulness、accuracy、probe accuracy 等），但无信度/效度证据、无置信区间，也未系统说明连续指标预处理与天花板/地板控制，故只算部分完整。 |
| A3 | 控制变量 | 0.5 | p2: 'We use pre-trained models without fine-tuning'; p3: prompts with four tokens and four operators; p3: 'we only use prompts that are correctly completed'; p19: operands in [0, 300] and exclusion of non-single-token results. | 报告了固定模型、提示格式、操作数范围、单 token 过滤、只用正确完成提示等控制，但不是系统列出的控制变量清单与逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | p3: 'To reduce noise ... we only use prompts that are correctly completed'; p10: limitations about 'human biases' in defining heuristic types and 'digit tokenization'. | 识别了正确完成提示筛选、人工定义启发式与数字 tokenization 等潜在效度威胁，但没有系统说明这些混淆的控制方式或残余威胁的敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文未提出调节变量或交互检验的理论模型；模型规模、算子等差异是描述性/探索性比较，不构成受控调节分析。 |
| A6 | 中介变量 | NA | — | 论文未界定中介变量，也未做直接/间接效应分解或 a/b 路径系数报告。 |
| A7 | 操作性定义 | 1 | p3 details activation patching and Eq.(1); p4 Eq.(2) faithfulness; p4-p5 linear probing; p6 Algorithm 1 and heuristic matching example; p17-p19 Appendix E/F give heuristic definitions and classification algorithm; p1 code link. | 关键构念均有可复现的操作化程序：电路定位、faithfulness、线性探测、神经元消融、启发式分类算法与阈值。 |
| A8 | 水平数与类型 | 0.5 | p2: four LLMs; p3: four operators and 100 prompts per operator; p8: ablation counts 5/10/25 and model sizes; p9: Pythia checkpoints at 10K-step intervals from 23K to 143K. | 报告了多个条件/水平及其取值，但未以正式自变量框架说明水平类型、间距/全距及连续变量中心化等。 |
| A9 | 单一操作化的风险 | 1 | p5: neuron activation patterns and Logit Lens; p6-p7 heuristic classification and type-based ablation; p8: prompt-guided knockout versus random ablation; p9: training-checkpoint analysis; p20-p22 Appendix I replicates across models. | 关键构念通过神经元激活模式、value-vector logit、类型消融、提示级消融、跨模型与跨训练检查点多种操作化获得会聚证据；并讨论了未分类神经元和人工定义局限。 |
| A10 | 单一方法的风险 | NA | — | 本研究为模型内部激活与 logit 的客观计算分析，不使用问卷/自评式多构念测量；共同方法偏差检验在此设计中没有对应意义。 |
| B1 | 被试间设计 | NA | — | 无人类被试，也无被试间条件分配；同一模型在多个干预条件下被反复分析，故不适用传统被试间设计编码。 |
| B2 | 被试内设计 | NA | — | 虽有多条件重复计算，但分析单位是模型组件/神经元/提示，独立前向计算无人类被试内顺序平衡问题；无被试内设计可编码。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内人类因素的混合设计，也无混合 ANOVA 或对应误差项。 |
| B4 | 因子设计 | NA | — | 论文不是全交叉因子实验，未报告完整设计矩阵、每格样本量与因子交互 ANOVA。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验；算子、模型和消融条件的比较是机制分析而非 ANOVA 主效应。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验或简单主效应/多重比较分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机设计或区组变量。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 研究使用计算干预而非准实验分组，也没有非随机分配造成的选择偏差问题。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及人类被试内处理可逆性/迁移对称性设计。 |
| C1 | 随机化 | NA | — | 没有将分析单位随机分配到互斥实验条件的程序；组件/神经元干预是系统定位而非概率分配，随机仅用于反事实提示或随机消融基线。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p2: 'pre-trained models without fine-tuning'; p3: four-token prompts with Arabic numerals and four operators; p19: operand range [0,300] and single-token filtering; p20: GPU setup. | 报告了若干恒定设置（模型、提示格式、操作数范围、单 token、硬件），但未系统讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 无匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 无将混淆变量作为协变量或区组纳入统计模型的 ANCOVA 分析。 |
| C6 | 盲法 | NA | — | 无人类被试或独立人类评分者盲法；人工观察启发式模式不是正式评分流程。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级可编码。 |
| D1 | 练习效应 | NA | — | 论文的 LLM 提示分析为独立前向计算，不涉及人类被试练习块或上下文内学习顺序。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳、休息间隔或条件时间分散问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件清洗期或残留迁移设计；不同提示/干预间不累积会话状态。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移检验需求。 |
| D5 | 范围效应 | NA | — | 因变量为客观 logit/accuracy/faithfulness，不是主观量表或绝对判断，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 算术表达式 token 顺序由任务语法固定，不存在多选项呈现顺序或需要随机化的处理顺序。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，故无需求特征或掩饰情节问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p20 Table 3 reports model accuracies (e.g., Llama3-8B average 0.95, some operators 0.96-0.97); p20 notes integer division high accuracy because 'half of the legal prompts result in the token 0'; p7 reports 95% pre-ablation accuracy. | 报告了均值准确率和部分端点/分布问题，但未报告标准差、偏度、系统性 pilot 难度校准或专门的天花板/地板校正。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p4 reports circuit faithfulness 0.96; p7 reports 'average drop of 29% out of 95% average pre-ablation accuracy'; p7/p8 use 100 or 50 prompts per condition. | 报告了效应量级与每条件提示数，但无置信区间、无样本量功效依据、无多重比较校正，也多为描述性比较而非正式统计检验。 |
| F2 | 内部效度 | 0.5 | p3 describes activation patching with random counterfactual prompts and averaged effects; p7-p8 compare heuristic ablation with random/ unassociated neuron ablation. | 干预程序与随机基线有报告，但无分配隐藏、基线等价性检验、损耗/flow 等人类实验内部效度要素；内部效度威胁评估不完整。 |
| F3 | 构念效度 | 0.5 | p5 links neuron activation patterns to value-vector logits; p6-p7 uses classification threshold t=0.6 and ablation validation; p19 says false classification amount is estimated manually; p10 discusses heuristic-definition limitation. | 有操作化与多方法验证启发式构念，但无信度统计、无评分者间一致性、无正式 manipulation check；构念效度只部分满足。 |
| F4 | 外部效度 | 0.5 | p2 states four models and main analysis on Llama3-8B with Appendix I for others; p10 limits conclusion to digit-combining tokenization; p20 reports model accuracies. | 报告了模型来源、跨模型复现和部分推广边界，但所测模型/算术范围有限，未讨论对更广模型总体或任务情境的代表性。 |
| G1 | 分析单位 | 0.5 | p3: 'The effect is averaged across prompts and measured separately per component'; p5: top-200 neurons per layer; p7: 100 associated and 100 unassociated prompts per heuristic. | 说明了在组件/神经元与提示层面聚合分析，但未使用多层模型显式处理提示、层、模型等嵌套/聚集结构。 |
| G2 | 随机效应 | 0.5 | p3-p4 report averaged effects and circuit faithfulness across prompts; p20-p22 Appendix I compares models; no mixed-effects or random-effect specification is reported. | 结果依赖跨提示平均与模型比较，但未报告哪些因子作为随机效应、随机截距/斜率结构或可推广总体。 |
| G3 | 材料作为随机效应 | 0.5 | p2: 'We sample a list of 100 prompts per operator for circuit discovery, and an identical amount for evaluation'; p7: samples 100 associated and 100 unassociated prompts per heuristic; no item random-effect model. | 提示被抽样并用于平均，但分析未将提示/项目作为随机效应纳入模型，也未使用准 F 或混合模型。 |
| G4 | 统计功效 | 0 | p2-p3 and p7-p8 give prompt/neuron counts (100 prompts per operator; top-200 neurons; 5/10/25 ablations) but no a priori power analysis; results mainly mean curves without CIs. | 无设计阶段功效分析或样本量论证，结果报告也缺效应量置信区间，故不满足。 |
| G5 | 研究者自由度 | 0.5 | p3: only correctly completed prompts for circuit discovery; p19: excludes non-single-token results; p8: random samples 50 correct and 50 incorrect prompts; p1 provides code link. | 报告了若干排除规则与条件，但未完整说明样本量决定方式、所有探索性/验证性分析区分及中途停止/追加规则。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement or registry link in the paper; only a code link is given on p1. | 全文无公开预注册或预先分析计划；不能把代码公开当作预注册。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM-as-judge、多候选项选择或候选位置反平衡；模型输出为算术答案 token 的 logits。 |
| J2 | 冗长偏差 | NA | — | 不涉及开放式生成长短比较或 LLM 裁判质量评分。 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈/纠错对话操纵，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge 或模型生成互评；无自我偏好风险。 |
| J5 | 少样本示例选择与排列偏差 | NA | p3: 'we do not use in-context prompting'. | 实验为零样本算术提示分析，无 few-shot 示例选择/排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p19: 'prompts of the form op1 ◦ op2 =' with operand range [0,300]; p1 code link. No prompt-version, sensitivity ablation, or dev/test split is reported. | 提示模板格式有说明，但无版本号、语义等价措辞敏感性检验或测试集调参说明，只能部分满足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文、RAG 或关键信息位置操纵；输入为极短四 token 算术提示。 |
| J8 | 温度与采样随机性 | NA | — | 研究分析概率/logit 与干预效应，不进行随机解码采样；temperature/top-p 等采样随机性不适用。 |
| J9 | 重复与文本退化 | NA | — | 不涉及开放生成、重复退化或解码策略比较。 |
| J10 | 分词效应 | NA | — | 研究为单一语言/单一数字脚本内的英文算术表达式；未做跨语言或跨脚本 tokenization 比较。p10 的 digit tokenization 只是局限讨论。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p2 identifies models and says 'pre-trained models without fine-tuning'; p20 reports accuracy on generated arithmetic prompts. No training cutoff, test-set version, or contamination/n-gram overlap check is reported. | 研究直接以预训练模型的算术表现为基础，但未评估训练语料与测试算术提示的重叠，也未报告训练截止日期，存在把记忆复现与机制结论混淆的风险。 |
| J12 | 基准饱和 | 0.5 | p20 Table 3 reports per-operator accuracies and notes high division accuracy due to many prompts yielding token 0; some Llama3 scores are near ceiling (e.g., 0.97). | 报告了基准分数量程与部分饱和线索，但未系统使用连续指标/更难子集，也未报告 CI 或对近上限差异作饱和校正。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；无约束型指令与机器可验证遵循标准。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/JSON 输出解析，主要读取答案 token logits。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究定位为 LLM 机制可解释性/算术电路分析，不是把 LLM 当作人类心理学被试测量同名心理构念，也未外推人类心理学结论。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文比较不同模型和 Pythia 训练检查点，但未报告或宣称跨规模能力曲线的突然涌现，也未讨论指标诱导的涌现假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL、best-of-N 或对代理指标的优化过程；不涉及奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p2 names models (Llama3-8B/70B, Pythia-6.9B, GPT-J); p9 reports Pythia checkpoints; p1 provides a code link. No repeated runs with 95% CI, exact API/checkpoint snapshot for all models, or paired tests. | 结果主要为单点均值/曲线，未报告重复运行置信区间，也未给 Llama/GPT-J 的精确 snapshot；可复现性要件不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮算术提示，无多轮对话历史或跨轮一致性衰减。 |

## 编码小结
该文是因果干预式的计算机制研究，不是人类心理学实验。A7/A9 等操作性定义与多证据汇合较强；A1-A3、A8、E6、F1-F4、G1-G3/G5 等有部分报告但完整度不足；大量人类实验设计组件不适用。主要缺口包括无正式随机分配/盲法、无预注册、无功效分析、无置信区间与精确模型 snapshot，以及对训练数据污染的核查不足。
