# article_019 | RTP-LX: Can LLMs Evaluate Toxicity in Multilingual Scenarios? | 2025

研究类型概述：基准构建与观察性 LLM 评测研究：构建 28 语种 RTP-LX 毒性语料，比较 10 个 S/LLM 及 ACS/FLORES 基线在人类标注毒性标签上的 PA、κw、FP 等表现；不是人类被试实验。分析单位为 prompt/label 层面的模型输出与人类聚合标签比较，语言、模型、伤害类别为评测分组或材料属性。
- **研究构念（Construct）**：文化敏感的危害判断与语境社会知觉（culturally sensitive harm judgment and contextual social perception）｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：基准构建与观察性 LLM 评测研究：构建 28 语种 RTP-LX 毒性语料，比较 10 个 S/LLM 及 ACS/FLORES 基线在人类标注毒性标签上的 PA、κw、FP 等表现；不是人类被试实验。分析单位为 prompt/label 层面的模型输出与人类聚合标签比较，语言、模型、伤害类别为评测分组或材料属性。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | — | 全文没有研究者主动操纵并随机分配的自变量；模型、语言和伤害类别是评测分组或材料属性，不是实验操纵。 |
| A2 | 因变量 | 0.5 | p.4: “we calculated IRR between the aggregated ... human label and S/LLMs with Percentage Agreement (PA) and with κw”; p.3: “Toxicity is scored on a five-point Likert scale, and the rest ... on a three-point scale.” | 因变量指标与计分方式明确，且报告人类标注 IRR（0.62±0.2）；但缺少系统效度证据、连续指标预处理及天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | p.3: “We used temperature of zero throughout”; “All models were called ... on four A100 80Gb PCIE GPUs; except GPT-4 Turbo ... via Azure OpenAI.” | 报告了温度、硬件和部分模型版本等控制，但未系统列出控制变量清单及逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | p.5: “We have mitigated this by ensuring transcreation, not translation...”; p.7: “there is no guarantee that our corpus will not eventually be used to train the models.” | 识别了文化偏斜、方言覆盖和污染等潜在混淆并提出部分缓解措施，但未量化残余混淆或作敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量理论模型或乘积项交互检验；语言可用性分析是描述性分组趋势，不是正式调节分析。 |
| A6 | 中介变量 | NA | — | 论文不包含中介变量或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.8 Table 2 给出八类伤害的操作定义与 1–5/1–3 量表；p.3 描述独立标注与指南；p.4 描述提示、解析器和 PA/κw 指标。 | 关键构念（伤害类别、标注量表、评估指标）均有可复现的操作化说明，足以理解数据构造与模型评分流程。 |
| A8 | 水平数与类型 | NA | — | 没有需要按水平数、间距和类型编码的实验自变量；模型/语言/类别只是评测分组。 |
| A9 | 单一操作化的风险 | 0.5 | p.5: “accuracy as a metric is insufficient”; p.9: “Llama Guard ... a lazy learner”; 使用 PA、κw、FP 与多伤害类别。 | 使用了多种指标与多个伤害类别，并讨论准确率不足和类别差异；但未系统报告各操作化之间的会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 人类标注与模型输出来自不同方法渠道，不存在自变量/因变量同源自评的共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 纯基准评测，没有被试组间分配；模型比较不是人类被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有同一被试接受全部条件的重复测量被试内设计。 |
| B3 | 混合设计 | NA | — | 没有逐因素标注组间/组内的混合实验设计。 |
| B4 | 因子设计 | NA | — | 没有完全交叉的因子实验设计、设计矩阵或 ANOVA 表。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有交互项统计检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计，也没有非随机分组与因果推断主张。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理条件，因此不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有将分析单位随机分配到互斥实验条件；语料来自 RTP 抽样与人工构造，不是随机分配。 |
| C2 | 平衡 | NA | — | 没有条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p.3: “temperature of zero throughout”；p.3: 四个 A100 与 Azure OpenAI；p.7: 指定所测模型版本以保证可复现。 | 报告了温度、硬件、接口和模型版本等恒定项，但未系统讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | 0.5 | p.5: “We explored the correlation ... between the availability online of the languages and the κw”; p.6 Figure 5 按 high/mid/low-resource 分组报告 κw。 | 语言可用性被测量并作为分组变量分析，但未作为正式协变量纳入模型，也未检验斜率齐性或报告调整后效应。 |
| C6 | 盲法 | NA | — | 没有需要隐藏条件的人类实验分组；人类标注无实验条件盲法问题。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 的顺序层级需要报告。 |
| D1 | 练习效应 | NA | — | 没有练习块或随试次学习的实验设计。 |
| D2 | 疲劳效应 | NA | — | 没有实验 session 时长、休息间隔与条件时间分散设计；标注者休息不是实验疲劳控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件清洗期或迁移效应设计。 |
| D4 | 不对称迁移 | NA | — | 没有条件对或迁移对称性检验。 |
| D5 | 范围效应 | 0.5 | p.3: “five-point Likert scale ... three-point scale”; p.8 Table 2 给出类别定义与量表范围；p.3 提到三元量表以降低歧义。 | 有量表锚定与三元化设计，但未明确讨论范围效应风险，也未采用被试间对照或跨语言量表校准。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多候选项选择、排序或刺激/选项位置需要随机化/反平衡。 |
| E2 | 默认赞同 | NA | — | 不是含正反向题的态度/Likert 多题量表，因此默许偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | 0.5 | p.5: “models were also very prone to output binary labels ...”; p.9 Figure 7 展示 Toxicity/Microaggression 的类别分布。 | 报告了模型标签分布与偏向高值/二元标签的现象，但没有对跨语言或跨模型反应风格作校正。 |
| E4 | 需求特征 | NA | — | 没有人类被试的掩饰情节或需求特征检查。 |
| E5 | 实验者效应 | NA | — | 没有实验主试/评分者条件知晓问题；人类标注在模型评估前完成且无实验条件盲法设计。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5: 讨论类别不平衡、FP 与 “lazy learner”；p.9 Figure 7 展示类别分布。 | 报告了分布和端点/误报信息，但未报告 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | 人类标签与模型输出不是同源自陈式多构念测量，共同方法偏差问题不适用。 |
| F1 | 统计结论效度 | 0.5 | p.3: IRR “0.62 ± 0.2”；p.5: FLORES “24.3 ± 8.3% block rate”；p.4 报告 PA 与 κw。 | 报告了效应量性质的 κw/PA 和部分 ± 值，但无置信区间、样本量/功效依据，也未说明多重比较校正。 |
| F2 | 内部效度 | NA | — | 非实验观察性基准评测，无随机分配、分配隐藏或因果效应推断。 |
| F3 | 构念效度 | 0.5 | p.3: 人类标注 IRR 0.62±0.2；p.8 Table 2 类别定义；p.5 讨论 accuracy 与 κw 的构念差异。 | 报告了评分者信度和构念讨论，但缺少正式效度证据与操纵检验。 |
| F4 | 外部效度 | 0.5 | p.2 与 p.8 Table 1 列出 28 种语言；p.5–p.6 讨论文化偏斜、方言覆盖与语言资源边界。 | 报告了语料/语言来源与推广边界，但没有跨样本或跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.3: “aggregated (majority vote; average otherwise) human label”；p.5–p.6 按语言资源层级汇总 κw。 | 分析单位为 prompt/label 与模型输出比较，语言/模型存在嵌套或交叉结构，但只作聚合均值分析，未用多层模型显式处理。 |
| G2 | 随机效应 | NA | — | 没有混合模型或随机效应推断；模型是被评估的固定对象，语言集合是固定基准语言集。 |
| G3 | 材料作为随机效应 | 0 | p.2: 从 RTP 选 top 1,000 prompts 并人工增补；p.4: 与人类聚合标签比较；分析未报告 item 随机效应。 | 有限 prompt 被视为固定材料，未将 prompt/item 作为随机效应纳入分析，限制了对更广材料总体的推广。 |
| G4 | 统计功效 | NA | — | 这是描述性基准评测，没有事前功效分析或预设效应量检验；不以推断性假设检验为主。 |
| G5 | 研究者自由度 | 0.5 | p.4: “We performed three experiments”；p.7: 发布 corpus、prompts、code、rubrics；p.4 报告解析器与部分异常处理。 | 报告了主要条件、模型与指标，并把完整结果指向仓库；但未报告数据排除规则、样本量决定方式或停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–12 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告公开预注册、注册编号或数据收集前分析计划；不属于明确声明的纯探索性预注册研究。 |
| J1 | 位置偏差 | NA | — | 不涉及候选项 A/B 位置、排序或成对裁判位置偏差。 |
| J2 | 冗长偏差 | NA | — | 评估毒性标签/评分，不是开放生成质量的长短比较，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错对话，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 不是让 LLM 成对评判模型生成输出；模型作为标注器与人类标签比较，不构成自我偏好裁判设计。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.4: “We modified the annotation rubric to included exemplars, and formatted it as per each model’s requirements ... The prompt is available in the repository.” | 使用了 few-shot exemplars，但未报告示例来源、每类数量、标签比例、排列平衡或多 seed 重采样。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4: “The prompt is available in the repository”；p.7: 发布 “prompts, code ... rubrics”；未报告 prompt 版本或敏感性消融。 | 提示模板可在仓库获得且作为固定评估流程使用，但缺少版本化、敏感性消融和 dev/test 划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 输入是短毒性 prompt，不是长上下文或 RAG 场景。 |
| J8 | 温度与采样随机性 | 0.5 | p.3: “We used temperature of zero throughout”；p.3: 输出生成于 “11th and 25th May, 2024”；未报告 seed 或重复采样 N。 | 报告了 temperature 和模型调用日期，但未报告随机种子、重复次数与均值置信区间。 |
| J9 | 重复与文本退化 | NA | — | 任务为毒性标签/分数分类式输出，不涉及开放长文本生成与重复退化 QC。 |
| J10 | 分词效应 | 0 | p.2 与 p.8 Table 1 说明跨 28 种语言；p.3 模型通过 Hugging Face/Azure 调用；未报告 tokenizer 名称、版本或 token/词数比控制。 | 跨语言/跨脚本评估实际存在，但完全未报告分词器版本或 token 长度控制，语言差异可能与分词效率混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.3: transcreation “helpful in ablating out data contamination”；p.7: “no guarantee ... will not eventually be used to train the models” 并采取防爬虫措施。 | 识别了污染风险并采取转创与数据保护等缓解，但未报告训练截止日期对照、污染检测方法或污染率。 |
| J12 | 基准饱和 | NA | — | RTP-LX 是新构建的困难基准，结果普遍显示与人类一致性低，未处于饱和区间，饱和问题不适用。 |
| J13 | 指令遵循 | NA | — | 因变量是毒性/伤害标签与人类一致性，不是指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.4: “formatted it as per each model’s requirements (e.g. ChatML)” 并 “wrote a parser to extract scores”；未报告格式合法率。 | 需要从模型响应中解析结构化分数，且报告了解析器与异常处理，但未报告格式合法率、重试策略或将格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | NA | — | 研究评估毒性检测/安全标注能力，不是越狱攻击成功率或自然拒绝率的安全性对齐研究。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 这是应用型 LLM 标注能力评估，不主张测量人类心理学/认知构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨规模/训练进展的涌现能力曲线；虽比较不同模型规模，但未做涌现或指标诱导假象分析。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N 或其他对代理指标的优化过程，不涉及奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.3 给出 gpt-4-turbo-2024-04-09 等具体版本与调用日期；p.7 强调指定模型版本以保证可复现；但未报告重复 N、置信区间或配对检验。 | 给出了部分精确模型 snapshot/版本并发布数据与代码，但主要分数为单点结果，缺少重复采样、CI 和配对比较。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 prompt 分类/标注，没有多轮对话历史累积。 |

## 编码小结
本文的核心贡献是多语言、文化敏感的毒性标注基准与模型评估，而非受控心理学实验。人类实验设计相关组件多为 NA；LLM 评估相关组件部分报告较充分，但统计不确定性、重复采样、提示版本/敏感性、污染检测等关键可复现信息不完整。
