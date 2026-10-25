# article_113 | Intuitive or Dependent? Investigating LLMs’ Behavior Style to Conflicting Prompts | 2024

研究类型概述：这是一项以 LLM 为分析对象的基准评测/观察性比较研究：作者构造 KRE 冲突数据集，操纵或组合提示冲突（negative/golden context、instruction with/without hint、few-shot 配置、role play 角色），用 VR、RR、FR、DMSS 等指标评估 7 个 LLM 的事实稳健性与决策风格；没有人类被试分配，也不是随机化心理实验。
- **研究构念（Construct）**：冲突信息下的依赖型、直觉型与理性决策风格｜CA 构念锚定：语言产生（language production, `trm_4a3fd79d0a78d`）；语言理解（language comprehension, `trm_4a3fd79d0a775`）；认知控制（cognitive control, `trm_4aae62e4ad209`）
- **实验任务与范式（Task / Paradigm）**：这是一项以 LLM 为分析对象的基准评测/观察性比较研究：作者构造 KRE 冲突数据集，操纵或组合提示冲突（negative/golden context、instruction with/without hint、few-shot 配置、role play 角色），用 VR、RR、FR、DMSS 等指标评估 7 个 LLM 的事实稳健性与决策风格；没有人类被试分配，也不是随机化心理实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3: 'There are two types of instructions: (1) Instruction without hint ... (2) Instruction with hint ...'; p.5: 'each question will be tested under all three configurations' and role prompts in Appendix B.5. | 明确命名并报告了多个提示/角色条件及其水平，也描述了创设方式；但无独立随机分配，也无操纵检验，故仅部分满足。 |
| A2 | 因变量 | 0.5 | p.4: 'VR and RR scores are between 0 and 1'; p.5: defines DMSS; p.14: 'temperature to 0', 'maximum output length to 520'. | 因变量指标与计分公式明确，但没有报告指标信度/效度证据，也未说明分布、连续指标预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | p.3: 'we try our best to design an instruction set for KRE and choose the best performed one'; p.14: 'set the maximum output length to 520 tokens, and the temperature to 0'. | 报告了部分控制手段（固定温度/长度、筛选最佳提示），但未系统列出控制变量清单及逐一控制方式。 |
| A4 | 混淆变量 | 0.5 | p.3: 'Different prompts may lead to different results ... To minimize such influence'; p.7: 'The extended length of the context could obstruct the LLMs'; p.9 lists dataset/task/model limitations. | 识别了提示措辞、上下文长度和模型选择等潜在混淆，并做了部分控制/讨论；但无敏感性分析或对残余混淆的系统评估。 |
| A5 | 调节变量 | NA | — | 论文没有明确的中介/调节理论模型，也未做乘积项交互或简单斜率分析，故不适用。 |
| A6 | 中介变量 | NA | — | 没有中介变量定义、直接/间接效应分解或因果链检验，故不适用。 |
| A7 | 操作性定义 | 0.5 | p.4 gives VR/RR formulas; p.5 gives DMSS and few-shot configurations; p.17-23 provide prompt templates. | 关键指标和多数提示条件可复现；但 DMSS 到三种风格的阈值/分类规则不够明确，操作化仍不完整。 |
| A8 | 水平数与类型 | 0.5 | p.3: two instruction types; p.5: three few-shot configurations and two role prompts. | 报告了多个条件的水平标签，但未系统说明各因素的变量类型、全距或连续变量处理；多为分类条件。 |
| A9 | 单一操作化的风险 | 0.5 | p.5 defines DMSS as the primary style metric; p.12 says DMSS near 0 is ambiguous and FR should be auxiliary; p.9 notes metrics 'may not encompass all aspects'. | 核心构念主要依赖单一 DMSS 指标，但有辅助 FR 和局限讨论；未报告多操作化会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 这是 LLM 客观选择题/行为输出基准，不涉及人类自陈式多构念同源测量，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试分配；不同模型是固定比较组，不是随机分配的被试间实验。 |
| B2 | 被试内设计 | NA | — | LLM API 调用相互独立，没有人类被试内 session 顺序或顺序平衡问题；重复条件不需要按人类被试内设计编码。 |
| B3 | 混合设计 | NA | — | 未使用混合设计或分别报告组间/组内误差项的统计模型。 |
| B4 | 因子设计 | NA | — | 论文是基准评测而非正式因子实验，没有因子设计矩阵和主效应/交互分析，故不适用。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验，故不适用。 |
| B6 | 交互作用 | NA | — | 没有交互项统计检验或简单主效应分析，故不适用。 |
| B7 | 区组设计 | NA | — | 没有区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方设计或需要拉丁方平衡的人类被试内顺序。 |
| B9 | 准实验设计 | NA | — | 没有准实验分组、选择偏差处理或非随机因果推断框架；角色干预只是同模型提示前后比较。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥条件；所有问题按流水线进入各评测条件，无随机化分配程序。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序；LLM 独立调用，无顺序效应。 |
| C3 | 恒定 | 0.5 | p.14: 'temperature to 0', 'maximum output length to 520 tokens'; p.9 discusses limited model selection. | 报告了固定温度和最大输出长度等常量，但未系统列出所有恒定变量及其外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入分析模型。 |
| C6 | 盲法 | NA | — | 没有人类被试或评分者的盲法安排；模型名称/提示条件并不按盲法隐藏。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 等顺序平衡层级设计。 |
| D1 | 练习效应 | NA | — | LLM 条件调用相互独立，没有跨试次练习效应或练习块安排。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长或疲劳效应；LLM 调用不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每条件为独立提示，不涉及清洗期或跨条件迁移残留。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件迁移或不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为准确率/比例/风格分数，不是主观量表绝对判断，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p.4 shows MCQ options as fixed A/B/C/D; p.3 says a misleading option is randomly chosen, but no option-position randomization or counterbalancing is reported. | 多选项位置偏差是实际风险，但全文未见选项顺序随机化/反平衡或位置效应分析。 |
| E2 | 默认赞同 | NA | — | 不使用李克特/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 被试是 LLM，不存在人类需求特征或事后访谈推断假设的问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者在场传递期望。 |
| E6 | 天花板 / 地板效应 | 0 | p.6-8 report average VR/RR/DMSS percentages; p.16 reports aggregate robustness scores, but no skew/endpoint frequencies or pilot difficulty calibration. | 准确率/比例是有界指标，存在天花板/地板风险；未报告分布形态或端点频率，也未讨论难度校准。 |
| E7 | 共同方法偏差 | NA | — | 没有同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.6-8 and p.16 mostly report point percentages; no confidence intervals, effect sizes, power analysis, or multiplicity correction. | 有模型/条件比较和结论宣称，但统计结论效度信息不足，仅报告描述性分数。 |
| F2 | 内部效度 | 0 | p.5 describes role play intervention; p.7 says 'we can change LLMs' decision-making style'; no random allocation, baseline equivalence, flow, or attrition handling. | 角色干预和模型比较缺少随机分配、分配隐藏、基线等价与内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | p.3 reports human validation of negative contexts with >98% misleading and high agreement; p.8 reports metric scores; no manipulation check for role/style construct. | 有数据刺激的人工验证，但未报告 DV 指标信度/效度，也未正式做 style/role 操纵检验；构念效度证据不完整。 |
| F4 | 外部效度 | 0.5 | p.5 lists seven models; p.9 limitations note limited dataset, task specificity, and limited model selection. | 报告了模型和数据集来源并讨论部分边界，但没有跨样本/跨情境复现结果，代表性有限。 |
| G1 | 分析单位 | 0.5 | p.4 metrics average over questions x; p.5 'each question will be tested under all three configurations'; no multilevel model or clustering treatment. | 实际分析单位为问题/模型响应，处理也在该层级；但未明确讨论数据集/问题嵌套和聚集结构。 |
| G2 | 随机效应 | 0 | p.8 model-level leaderboard; no mixed model or random effects structure; questions/models treated as fixed aggregates. | 未说明随机/固定效应，也未把问题或数据集作为随机抽样总体处理。 |
| G3 | 材料作为随机效应 | 0 | p.3 uses fixed question sets from four datasets; p.4 averages over x; no item random effect or F′/mixed model. | 材料/问题被视为固定集合，未建模材料随机效应，不能推广到更广项目总体。 |
| G4 | 统计功效 | 0 | p.3 reports dataset size 11,684; p.6-8 report scores but no a priori power analysis, effect sizes, or CIs. | 没有事前功效分析或样本量论证，结果也缺少效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.3 describes dataset filtering and instruction selection; p.14 reports decoding settings; p.16 reports invalid response counts, but no explicit exclusion/stopping rules. | 报告了部分数据处理和无效输出，但未完整报告试次剔除规则、全部分析选择及验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–27 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未提及预注册、注册平台或分析计划；按口径记 0。 |
| J1 | 位置偏差 | 0 | p.4/p.24-26 show fixed option orders A-D; no option-position counterbalancing, swap re-judging, or position-wise accuracy is reported. | 多选题存在显著位置偏差风险，但未做任何位置平衡或翻转率报告。 |
| J2 | 冗长偏差 | NA | — | 没有使用 LLM-as-judge 对开放式回答质量打分；评分主要是答案匹配/准确率，冗长偏差不适用。 |
| J3 | 谄媚 | NA | — | 没有操纵用户先验立场或反馈纠错，不涉及谄媚风险评估。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM 裁判或成对比较评估，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.5: 'three configurations': all-positive, all-negative, mixed; 'we manually sample three samples for each evaluation setting'; prompts in B.3. | 报告了 few-shot 示例数量、标签比例和来源，但未报告示例顺序反平衡、多 seed 重复或示例与测试集隔离的完整证明。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.3 reports 24 instruction variants; p.12-13 report instruction selection tables; p.17-23 provide full prompt templates. | 提供了完整模板和敏感性比较，但未见明确 dev/test 划分，也未说明是否在测试集上调 prompt。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不是长上下文/RAG 信息位置实验，上下文为短/中等知识段落，无 token 位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.14: 'set the maximum output length to 520 tokens, and the temperature to 0'; no seed, top-p/top-k, repeated sampling or CI reported. | 报告了主要采样设置，但没有随机种子、重复采样次数和方差/置信区间；采样随机性未被纳入统计设计。 |
| J9 | 重复与文本退化 | 0.5 | p.14 reports temperature and max output length; p.16 Table 8 reports invalid/negative answer counts, but no repetition penalty or n-gram degeneration rate. | 部分报告了解码设置和无效输出，但未报告重复/退化率，条件间解码策略细节也不完整。 |
| J10 | 分词效应 | NA | — | 单语言英文任务，不做跨语言/跨脚本 tokenization 比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3 names datasets MuSiQue/SQuAD/ECQA/e-CARE but no model training cutoff, dataset version-vs-cutoff comparison, or contamination detection. | 使用公开数据集且未做任何污染检查，存在把记忆/污染当泛化的风险。 |
| J12 | 基准饱和 | NA | — | KRE 分数总体在 20-69% 左右，远离天花板，且不是饱和基准评测场景，故不适用。 |
| J13 | 指令遵循 | NA | — | 论文主要测量事实稳健性和决策风格，不以指令遵循为独立因变量；无效输出仅作为辅助计数。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.17-23 prompts require formats such as 'The answer is A: ...'; p.16 Table 8 counts invalid outputs, but no overall format-legal rate or grammar-constrained setting is reported. | 有输出格式约束和部分无效输出统计，但未把格式合法率与内容正确率独立、完整报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全性/越狱评估，无有害请求或对抗攻击测试。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: 'Drawing on cognitive theory ... categorize LLMs’ preference into dependent, intuitive, and rational/irrational styles'; p.2 defines these styles; no human-subject comparison. | 明确把 LLM 行为映射到人类决策风格构念，但未系统论证二者异同，也未做人类同范式对照或权重快照定位。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有报告随模型规模/训练进展的能力曲线，也不宣称涌现能力。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N 或代理指标优化环节，不涉及奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.5 and p.8 name models; p.14 reports temperature=0 and max length, but no exact snapshot/API date, repeat count, CI, or paired tests. | 评估可复现性信息不足，仅有模型名称和部分解码参数，缺少重复/置信区间/snapshot 标识。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评测，无多轮对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
论文对提示条件、数据集构造、指标公式和部分 prompt 模板报告较充分，但多数人类实验设计组件不适用；适用的偏差与统计组件中，随机分配、顺序/位置控制、随机效应、预注册、采样可复现性、基准污染控制等明显不足。整体适合作为 LLM 基准评测编码，不能按人类被试实验的完整实验设计标准视为完备。
