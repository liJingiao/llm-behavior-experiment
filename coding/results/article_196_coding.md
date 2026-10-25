# article_196 | Large Language Models are Fixated by Red Herrings: Exploring Creative Problem Solving and Einstellung Effect using the Only Connect Wall Dataset | 2023

研究类型概述：论文构建 Only Connect Wall（OCW）基准数据集，并用静态/上下文词嵌入聚类、GPT-3.5-turbo/GPT-4 的零样本与少样本 ICL，在分组（Grouping）和连接（Connections）任务上评测 LLM 的创造性问题解决表现；另生成 OCW-Randomized、OCW-WordNet 两个变体以消融红鲱鱼干扰。属于基准构建与 LLM 行为评测，不是以人类被试为对象的随机实验。
- **研究构念（Construct）**：创造性问题解决中的认知固定和Einstellung效应｜CA 构念锚定：创造性思维（creative thinking, `trm_4a3fd79d09f42`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：让GPT系列和其他预训练模型解决Only Connect Wall词语分组与连接任务，并在保留、削弱或替换红鲱鱼的版本中比较解题表现。（操纵红鲱鱼是否存在及其强度、上下文示例数量、模型和分组或连接任务。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'We experiment with 0, 1, 3, 5, and 10 in-context examples.' p.5-p.6 describe embedding and LLM conditions; p.20 describes OCW-Randomized/WordNet construction. | 明确比较了模型、shot 数、数据集变体等条件及取值，并报告了部分创设程序；但未报告操纵检验，也未像人类实验那样说明单位分配/随机化。 |
| A2 | 因变量 | 0.5 | p.3: 'We evaluate Task 1 (Groupings) via six metrics...' p.4: Task 2 uses exact match, ROUGE-1 F1, BERTScore F1; examples/threshold in Table 1. | 因变量指标与计分方式明确，且给出 BERTScore hashcode 和阈值示例；但缺少正式信效度证据及连续指标的预处理/天花板地板说明。 |
| A3 | 控制变量 | 0.5 | p.6: 'temperature=0 ... snapshots ... max output length is set to 144 tokens ... all other hyperparameters ... defaults'; p.6: same in-context examples across all test inputs; p.5: 16 random sortings for embeddings. | 报告了若干控制变量及控制手段（温度、snapshot、固定示例、最大输出长度、随机排序），但未系统列出完整控制清单或逐项说明。 |
| A4 | 混淆变量 | 0.5 | p.10: 'performance ... can vary significantly depending on the order that clues are provided'; 'we did not evaluate GPT-3.5-turbo and GPT-4's sensitivity to this ordering'; also discusses leakage and UK-centric bias. | 识别了顺序、污染和文化偏差等潜在混淆，并说明部分缓解/局限；但未系统控制或做敏感性分析，残余威胁仍存在。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量假设与交互检验；模型×shot×数据集比较是描述性分组，不是正式调节分析。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量模型或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.3 defines the 16-word/4-group task and connections; p.7 Figure 4 gives task prompts; p.4 defines exact match, ROUGE-1 and BERTScore scoring. | 关键任务、提示结构、分组与连接评分方式均有可复现操作化；红鲱鱼消融也通过 OCW/Randomized/WordNet 构造具体化。 |
| A8 | 水平数与类型 | 0.5 | p.6: shots 0,1,3,5,10; Table 2 lists model names/versions; p.20 defines dataset variants. | 报告了主要条件的水平数和标签，但缺少水平类型、间距/全距及连续变量中心化等说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.3: OCW as 'analogical proxy' for RAT; p.9 and p.20 add OCW-Randomized and OCW-WordNet to reduce red herrings; p.10 discusses UK-centric limitation. | 使用了两个任务、多个指标和红鲱鱼水平不同的数据集变体，具有一定多操作化；但未报告操作间会聚证据，对单一代理局限的讨论也较有限。 |
| A10 | 单一方法的风险 | NA | — | 不存在人类自陈式 IV/DV 同源测量；自变量是任务/数据条件，因变量是模型输出自动指标，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组接受不同条件；LLM 基准评测不是被试间分配设计。 |
| B2 | 被试内设计 | 0.5 | p.6: same test inputs and same in-context examples; p.5: embeddings repeated over 16 random seeds/sortings; p.6: clues 'randomly sorted' for ICL. | 同一测试墙在多个模型/shot 条件下重复评测，具有重复测量/项目内比较结构；但未明确报告条件顺序平衡或把项目作为随机效应，且 GPT 的顺序敏感性未评估。 |
| B3 | 混合设计 | NA | — | 没有逐因素标注的人类被试组间/组内混合设计；模型比较与 shot 比较不是被试层面混合设计。 |
| B4 | 因子设计 | 0 | p.8 Table 4 and p.10 Table 5 report model × shot × dataset results; no full design matrix with cell n and no ANOVA interaction table. | 多因素交叉结构清楚并给出结果表，但缺少完整设计矩阵、每格样本量以及正式交互项统计；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p.8 Table 4 and p.10 Table 5 compare models/shots/datasets descriptively; no F/df/p/effect size for main effects. | 没有报告主效应的统计检验结果；只能视为描述性比较。 |
| B6 | 交互作用 | 0 | p.9: 'Performance for GPT-4 improves monotonically...' but no interaction test; Table 4/5 are descriptive. | 未报告交互项的统计检验、简单效应或误差棒/CI交互图；仅有描述性趋势。 |
| B7 | 区组设计 | NA | — | 没有使用区组/分层变量及区内随机分配。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；没有非随机分组后的因果推断框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理设计，因此不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 基准条件固定，未把测试墙随机分配到条件；嵌入随机种子只用于稳定性重复，不是处理分配随机化。 |
| C2 | 平衡 | NA | — | 没有人类被试内的条件顺序需要平衡；shot/模型条件不是按顺序分配给同一被试。 |
| C3 | 恒定 | 0.5 | p.6: 'temperature=0', GPT snapshots, 'max output length ... 144 tokens', other hyperparameters defaults; p.6 fixed in-context examples. | 列出了若干恒定设置及水平，但未系统列出全部恒定变量，也未充分讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有匹配变量或匹配后分配程序。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入统计模型；也没有 ANCOVA。 |
| C6 | 盲法 | NA | — | 没有人类被试/评分者盲法安排；LLM 自动评测不涉及盲法。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡、拉丁方或 ABBA 等条件顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 调用为独立会话，无练习块或上下文内学习累积；不涉及人类练习效应。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session、休息间隔或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个基准条件可独立调用，无跨条件清洗期或残留迁移问题。 |
| D4 | 不对称迁移 | NA | — | 不存在被试内交叉条件，因此不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为客观任务指标（分组指标、匹配/F1），不是主观量表或绝对量值估计。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.5: 'We randomly shuffle the word order across sixteen different runs for each wall'; p.6: current example's 16 clues are randomly sorted; p.10: GPT order sensitivity not evaluated. | 对词顺序做了随机化/多随机排序，但没有报告每个位置出现次数、顺序组分配，且未评估 GPT 的位置敏感性。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征或事后假设推断访谈。 |
| E5 | 实验者效应 | NA | — | 数据采集完全通过 API/自动脚本完成，无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.8 Table 3/4 report means ± SD and # solved walls/# correct groups; p.10 limitations discuss data properties. | 报告了均值和标准差以及部分端点型计数（solved walls），但未报告偏度/端点频率，也未说明 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不存在自陈式多构念同源测量；IV 为任务材料/条件，DV 为自动指标。 |
| F1 | 统计结论效度 | 0 | p.8 and p.10 report means/SD or point scores; no confidence intervals, no formal effect sizes, no power analysis, no multiplicity correction. | 缺少样本量依据、效应量/CI、多重性校正；文中使用 'significantly' 等措辞但未见相应推断检验。 |
| F2 | 内部效度 | 0.5 | p.10 discusses order sensitivity, possible training-set leakage, and UK-centric bias; no randomized allocation/baseline equivalence or attrition flow. | 对部分内部效度威胁有讨论，但没有随机分配、基线等价性或系统敏感性分析，红鲱鱼消融与任务难度等混淆仍未充分排除。 |
| F3 | 构念效度 | 0.5 | p.4 Table 1 illustrates metric behavior and threshold; p.6-p.7 provide prompts; no formal reliability evidence or manipulation check. | 提供了指标示例、任务定义和实现细节，但缺少信度证据、操纵检验和构念对应关系的系统论证。 |
| F4 | 外部效度 | 0.5 | p.3: 618 walls from 15 seasons scraped from fan sites; p.10: clues are Western/UK-centric and may not extrapolate to other languages/cultures. | 报告了数据来源与明显推广边界，但未提供代表性抽样框架，也未报告跨样本/跨文化复现。 |
| G1 | 分析单位 | 0.5 | p.4: metrics 'could be calculated per wall, per episode, per season, or for the entire test set'; results are reported on entire test set. | 说明了墙/集/季/测试集等分析层级，但最终按整个测试集聚合，未用多层模型处理墙嵌套于剧集/季的结构。 |
| G2 | 随机效应 | NA | — | 没有混合模型或随机效应结构；模型被当作固定基准系统比较，不是从模型总体抽样的随机效应设计。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: split into train 62, validation 62, test 494 walls; p.8 reports aggregate results over test set. | 使用了 held-out 测试墙，材料并非完全穷尽固定刺激；但未把墙/项目作为随机效应纳入模型，推广到任意墙的推断仍有限。 |
| G4 | 统计功效 | 0 | p.1–23 全文实验设计与结果部分均未报告事前功效分析、目标功效或样本量/重复次数推导依据 | 没有事前功效分析或样本量论证；结果也缺少效应量及置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.5: 'for brevity, results are not included' for two clustering variants; p.17: LLaMa results omitted for brevity; many metrics are reported. | 报告了较完整的任务与主要指标，但存在有意的结果省略和大量探索性模型选择，未区分验证性/探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–23 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 未见公开预注册、分析计划或停止规则；论文也未声明为纯探索性研究。 |
| J1 | 位置偏差 | NA | — | 任务不是多项选择/排序/LLM-as-judge 成对比较，不存在候选项位置偏差操纵。 |
| J2 | 冗长偏差 | NA | — | 没有 LLM 裁判或成对生成质量评分；长度偏差框架不适用。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错对话，不存在谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 评估模型输出，因此不涉及自我偏好裁判偏差。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.6: 'In-context examples are randomly selected from the train set; the same examples are used across all test inputs'; 0,1,3,5,10 shots. | 报告了示例来源和数量，但未报告多示例集 seed、标签比例、排列反平衡或多重抽样均值±SD；模板主要见图示。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.6: 'We developed our prompts on the validation set and reported the final performance on the test set'; p.7 Figure 4 gives example prompts. | 有 dev/test 划分并展示提示样式，但未报告 prompt 版本号、语义等价措辞敏感性消融或完整可复现模板。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短，无长文档、RAG 或中间迷失位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'temperature=0' and fixed snapshots; p.5: 16 random seeds for embeddings; LLM results are single runs without CI. | 报告了温度、snapshot 和嵌入重复次数，但未报告 LLM 重复采样 N、随机种子、top-p/top-k 或置信区间。 |
| J9 | 重复与文本退化 | 0.5 | p.6: temperature=0, max output length 144, simple post-processing; no repetition penalty or degeneration rate. | 报告了解码温度和长度上限，但未报告 repetition penalty、n-gram 重复率/退化率以及条件间解码策略的完整一致性。 |
| J10 | 分词效应 | NA | — | 仅英语单脚本实验，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.10: walls are publicly available on fan sites and may be in training sets; low performance makes leakage unlikely; dataset distributed compressed. p.6 gives GPT snapshots. | 识别了污染风险并对照公开数据与模型 snapshot，但未做 n-gram/DCQ 污染检测或报告污染率。 |
| J12 | 基准饱和 | NA | — | OCW 是全新且困难的基准，GPT-4 仅解决 6/494 walls（p.8 Table 4），远未接近天花板；不构成基准饱和风险。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；虽有格式输出要求，但未系统按约束类型测量 IF。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.8: 'misformatted outputs (4.4% of all predicted groups)' and 'hallucinated clues (6.6%)'; p.6 describes padding to 4 predictions and post-processing. | 报告了格式失败率及部分后处理规则，但未使用结构化/文法约束输出，也未把格式合法率作为完整独立指标系统报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/对齐、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: OCW 'makes it an ideal proxy task to explore and study the fixation effect and Einstellung paradigm ... in LLMs'; p.10 discusses UK-centric/cultural limits. | 明确把 LLM 任务作为人类认知构念的类比代理，并报告模型版本；但未系统论证 LLM 构念与人类同名构念的异同，也未做受控人类对照实验（仅引用节目人类表现）。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的能力曲线，也不宣称涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以代理指标为优化目标进行训练、RL 或 best-of-N 优化；仅为基准评估。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6 gives GPT-3.5-turbo-0301 and gpt-4-0314 snapshots and temperature=0; p.8 reports 16-seed mean±SD for embeddings; no LLM CI/paired tests/raw logs. | 提供了较精确的 snapshot 和部分重复次数，但 LLM 结果多为单点分数，缺少 CI、配对检验和逐题日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评测，无多轮对话历史，也不主张多轮部署外推。 |

## 编码小结
论文在数据集、任务、提示和指标上提供了较清楚的基准描述，并报告了多模型、多 shot、多数据集变体的描述性结果；但对认知构念（fixation/Einstellung）的操纵与效度论证较弱，缺少推断统计、效应量/CI、操纵检验、预注册和系统的混淆控制。整体是扎实的基准论文，但按实验心理学编码表看，许多设计/质控组件只达到部分报告或缺失。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
