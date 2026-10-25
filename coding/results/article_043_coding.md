# article_043 | Bias in the Mirror: Are LLMs opinions robust to their own adversarial attacks? | 2024

研究类型概述：LLM-as-participant 的偏见稳健性评估：对多种 LLM 在政治/社会等题项上的初始立场（-10 到 10）与经历 fair/biased self-debate 后的立场变化进行重复测量，并辅以多语言条件和小规模人类标注者对照。
- **研究构念（Construct）**：态度持存、政治偏见与说服易感性（attitude persistence, political bias, and susceptibility to persuasion）｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；态度（attitude, `trm_4a3fd79d09947`）
- **实验任务与范式（Task / Paradigm）**：LLM-as-participant 的偏见稳健性评估：对多种 LLM 在政治/社会等题项上的初始立场（-10 到 10）与经历 fair/biased self-debate 后的立场变化进行重复测量，并辅以多语言条件和小规模人类标注者对照。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4: 'In addition to the standard debates, we make each models undergo "biased" debates...'；同一页描述 fair debates 与 biased debates 两种条件。 | fair vs biased debate 可视为被操纵的自变量，且报告了两个水平及基本创设方式；但未报告随机分配/顺序控制，也未报告 manipulation check，故为部分满足。 |
| A2 | 因变量 | 0.5 | p4: 'We ask the models to respond using numerical values between -10 and 10'；p5 Table 1 报告 average shifts 与 Std-Dev。 | 因变量为 -10 到 10 的立场评分及前后变化，计分方式明确；但未报告信度、效度、连续指标预处理或防天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | p6: 'All the models are run with their default parameters'；p4: 'Each model is presented with each question twenty times, with independent evaluations'。 | 提到了 default parameters、相同题项、独立重复评估等部分控制，但没有系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p7: 'likely due to the cultural context embedded in its training data'；p6 讨论 'conservative alignment strategies'。 | 识别了语言/文化语境与对齐策略等潜在混淆，但未说明系统控制方式，也未报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量假设或形式化交互检验；模型/语言/话题比较是描述性分组，不构成调节分析。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量假设，也没有直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p4 描述四轮 debate 流程与 -10 到 10 作答；p11 给出人类标注者指令与 16 个题项；p13-14 给出 fair/biased debate 示例。 | 关键构念有可观测操作化描述，但缺少完整 prompt 模板、所有题项全文与完整计分/解析细节，复现性不完整。 |
| A8 | 水平数与类型 | 0.5 | p4 报告 fair/biased debates、English/Arabic/Chinese 语言条件；p3-4 列出多个模型。 | 报告了多个条件的水平标签与部分取值，但未系统给出水平类型、完整交叉结构、间距/全距或连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p4-p5 使用 fair/biased debates、paraphrasing 与多语言条件；p8 加入人类对照。 | 对偏见稳健性采用了多种操作化，但没有报告各操作间的定量会聚证据；也未充分讨论单一数字评分操作的推广限制。 |
| A10 | 单一方法的风险 | 0 | p4: 'an independent version of the model is prompted to express its stance ... before and after being exposed to the debate'；全文未报告共同方法偏差检验。 | 自变量（debate 条件）与因变量（立场评分）均通过同一 LLM 提示/自报渠道获得，存在同源方法风险，但未做共同方法偏差程序控制或统计检验。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或模型被随机分配到互斥的组间条件；主要是在同一模型/题项内比较前后与条件变化，不构成被试间设计。 |
| B2 | 被试内设计 | 0.5 | p4: 'an independent version of the model is prompted to express its stance ... before and after being exposed to the debate'；'Each LLM will participate in five debates per question'。 | 明确为同一模型/题项的前后重复测量，但未报告 fair/biased 或 debate 顺序的平衡方案及各顺序分配。 |
| B3 | 混合设计 | NA | — | 论文没有明确声明并逐因素标注混合设计，也没有使用混合模型或重复测量 ANOVA；模型间比较是描述性分组。 |
| B4 | 因子设计 | NA | — | 没有完全交叉的因子设计：模型、语言、话题并未形成完整 factorial design，且未报告交互项设计矩阵。 |
| B5 | 主效应 | NA | — | 不存在因子设计意义上的主效应检验；结果以各模型/话题的平均位移描述呈现。 |
| B6 | 交互作用 | NA | — | 不存在因子设计意义上的交互检验，也未报告简单主效应或交互图误差棒。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计，也没有报告区组变量及区内随机分配。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方设计，也没有被试内条件顺序的拉丁方平衡。 |
| B9 | 准实验设计 | NA | — | 研究不是准实验因果设计；模型/语言比较是观察性描述，没有准实验分组、选择偏差缓解或因果推断框架。 |
| B10 | 被试内设计的适用条件 | 0 | p4: 同一模型先给初始立场，再经历 debate，然后再次作答；未讨论态度改变的可逆性或迁移对称性。 | 前后态度改变属于可能不可逆的处理，却采用前后测量且未论证可逆性/迁移对称性，也未说明缓解措施。 |
| C1 | 随机化 | 0 | p4: 'Each LLM will participate in five debates per question. For each instance, an independent version...'；未报告随机分配方法或随机数工具。 | 条件/顺序没有随机化或分配隐藏说明，无法排除条件与顺序混淆。 |
| C2 | 平衡 | 0 | p4 只说明 five debates per question 和 before/after，未报告 fair/biased 或 debate 顺序平衡。 | 重复测量条件顺序固定，未做平衡，也未报告各顺序分配。 |
| C3 | 恒定 | 0.5 | p6: 'All the models are run with their default parameters'。 | 提到了 default parameters 这一恒定设置，但没有列出具体温度、top-p 等水平，也未讨论恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 研究未使用匹配设计，也没有匹配变量或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组或协变量纳入模型；研究主要是描述性均值比较，没有 ANCOVA/协变量调整。 |
| C6 | 盲法 | 0 | p11 给出人类标注者指令；未报告对标注者遮蔽 debate 类型/假设或盲法成功检验。 | 人类标注者知道自己在阅读 LLM 生成的 debate，未报告盲法安排；可盲却未盲。 |
| C7 | 平衡的层级 | 0 | p4 描述四轮 debate 流程和前后测量；未报告任何平衡层级、构造方法或顺序效应形状假设。 | 没有明确选择完全平衡/拉丁方/ABBA 等层级。 |
| D1 | 练习效应 | 0 | p11 人类标注者回答 16 个固定题项；未报告练习块、试次截除或题项位置协变量。 | 人类标注任务包含重复题项，未做练习效应控制；LLM 虽为独立评估，但人类子研究存在练习/顺序风险未处理。 |
| D2 | 疲劳效应 | 0 | p11 列出 16 个题项，但未报告 session 时长、休息间隔或条件时间分散。 | 人类标注者需阅读多个 debate，存在疲劳风险，但未报告任何疲劳控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件清洗期或处理对建模；前后 debate 暴露本身是研究目标，不是需要洗脱的跨条件残留。 |
| D4 | 不对称迁移 | NA | — | 没有条件对/交叉设计，因此不存在需要检验的跨条件不对称迁移。 |
| D5 | 范围效应 | 0 | p4 使用 -10 到 10 的主观评分；p11 人类标注者也使用同一量表；未讨论范围效应或锚定方式。 | 被试内前后评分与跨模型/跨语言比较存在范围效应风险，但未采用被试间对照、绝对锚讨论或设计差异标注。 |
| E1 | 位置 / 顺序偏差 | 0 | p4 固定 debate 流程：first speaker opening、second speaker opening/rebuttal、first speaker rebuttal、second speaker concluding rebuttal；未随机化 pro/con 顺序。 | debate 双方发言顺序固定，未做顺序随机化或反平衡，也未讨论顺序效应。 |
| E2 | 默认赞同 | NA | — | 研究使用单一双极 -10 到 10 数字评分，不是含反向计分题的多题 Likert 量表，默许偏差组件不适用。 |
| E3 | 极端 / 中间反应倾向 | 0 | p5 Table 1 仅报告 average shifts 和 Std-Dev；未报告偏度、端点/中点使用比例。 | 存在跨模型、跨语言比较，但未报告分布形态或反应风格差异，也未讨论其对组间比较的威胁。 |
| E4 | 需求特征 | 0 | p11 人类标注者指令明确告知将阅读 LLM 生成的 debate 并再次评分；未报告 cover story 或事后推断检查。 | 标注者可推断研究关注 debate 是否改变立场，未使用掩饰情节或事后访谈检查需求特征。 |
| E5 | 实验者效应 | 0 | p11 提供统一指令，但未报告主试/评分者盲法层级、人数、培训标准化或脚本化程度。 | 存在人类标注者参与，但未报告任何盲法或实验者期望控制。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5 Table 1 报告各模型的 average shifts 与 Std-Dev；未报告偏度、端点频率或 pilot 难度校准。 | 报告了均值/SD，可部分排查端点堆积，但缺少分布形态、端点频率与任务难度校准说明。 |
| E7 | 共同方法偏差 | 0 | p4 自变量 debate 条件与因变量立场评分均由同一 LLM 提示流程产生；全文未报告共同方法偏差程序或统计控制。 | 同源测量风险存在且未被控制，也未讨论 CMB 对结果的可能膨胀。 |
| F1 | 统计结论效度 | 0 | p5 Table 1 报告均值与 Std-Dev，但未报告效应量、95%CI、样本量确定依据或多重性校正。 | 统计结论效度信息不足；主要比较为描述性均值，未提供推断统计或效应量/CI。 |
| F2 | 内部效度 | 0 | p4 使用独立版本进行前后测，但未报告随机分配、分配隐藏、基线等价性、被试流向或损耗处理。 | 内部效度威胁（顺序、模型/语言混淆）未得到控制或系统评估。 |
| F3 | 构念效度 | 0 | p4 定义 -10 到 10 评分；未报告信度、效度证据或 fair/biased debate 的 manipulation check。 | 关键测量与操纵均缺少信效度/操纵检验论证，操作化与所声称偏见构念的对应关系未充分建立。 |
| F4 | 外部效度 | 0.5 | p3-4 报告多模型、多地区/多语言来源；p8 报告 20 名人类标注者且来自不同文化与性别背景；p9 讨论结论 localized。 | 报告了样本/模型来源与部分推广限制，但缺少系统抽样框、详细人口学特征及跨样本复现结果。 |
| G1 | 分析单位 | 0.5 | p4: 'Each model is presented with each question twenty times'；'five debates per question'；p5 以模型/条件平均值汇总。 | 存在题项/重复评估嵌套结构，但分析以聚合均值为主，未说明分配层级与统计模型层级匹配，也未使用多层模型。 |
| G2 | 随机效应 | 0 | p5 Table 1 仅报告各模型平均值与 Std-Dev；未报告任何随机效应或混合模型结构。 | 重复评估与题项嵌套未被建模为随机效应，推断可能把题项/重复观测当独立或仅作聚合，随机效应结构缺失。 |
| G3 | 材料作为随机效应 | 0 | p3 使用 62 个 Political Compass statements 及额外题项；p5 按模型汇总，未将题项作为随机因子。 | 有限题项被视为固定材料，未使用 (1&#124;item) 或准 F 比等处理，材料总体推广受限。 |
| G4 | 统计功效 | 0 | 全文未报告事前功效分析；p5 仅报告均值/Std-Dev，未报告效应量及 CI。 | 缺少目标功效、预期效应量、样本量推导及结果效应量/CI。 |
| G5 | 研究者自由度 | 0.5 | p4 说明每模型每题 20 次评估、五次 debate；p5-p7 报告多类条件；但未报告剔除规则、停止规则或验证性/探索性区分。 | 报告了主要条件与重复次数，但研究者自由度信息不完整。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册、注册平台或分析计划。 | 没有预注册，也未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 研究不是 LLM-as-judge 或多候选项选择/排序任务；模型只对单个陈述给出 -10 到 10 评分，J1 的候选位置偏差不适用。 |
| J2 | 冗长偏差 | NA | — | 研究没有使用 LLM 裁判评估开放生成质量，因此不存在长度被误当质量的 LLM-judge 冗长偏差。 |
| J3 | 谄媚 | NA | — | 研究操纵的是两个 LLM 实例之间的 pro/con self-debate，不是用户先验立场/反馈下的谄媚；J3 不适用。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 对被评模型输出做评分或成对比较，故自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验采用零样本提示与 self-debate，没有 few-shot in-context examples，J5 不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p4 描述 debate 提示与 -10 到 10 作答；p13-14 给出 fair/biased debate 示例；p5 使用 GPT-4 paraphrasing 检验措辞变化。 | 有部分 prompt 示例与 paraphrasing 敏感性信息，但未提供完整模板版本、系统消息、dev/test 划分或完整敏感性消融。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不是长上下文/RAG 实验，输入为短题项与四轮 debate，不涉及中间迷失或关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p4: each model 每题 20 次独立评估、五次 debates；p6: 'All the models are run with their default parameters'；p5 报告 Std-Dev。 | 报告了重复次数与 default parameters，但未报告 temperature/top-p/seed 具体值、API snapshot 或基于重复采样的置信区间。 |
| J9 | 重复与文本退化 | 0 | p4 使用模型生成四轮 debate 文本；全文未报告 greedy/beam/sampling、repetition penalty、重复率或退化率。 | 开放生成 debate 可能受解码策略与重复退化影响，但未控制或报告。 |
| J10 | 分词效应 | 0 | p4 报告 English/Arabic/Chinese 多语言实验；p7 比较不同语言结果；未报告 tokenizer 名称/版本或 token 数控制。 | 跨语言/跨脚本比较存在分词效率混淆风险，但未报告 tokenizer 或控制 token 长度。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p3 使用 Political Compass 的 62 个 statements 并追加题项；未报告测试集版本、训练截止日期或污染检测。 | 使用公开 Political Compass 题项，但未评估其是否出现在预训练数据中，也未区分记忆复现与偏见表达。 |
| J12 | 基准饱和 | NA | — | 研究不是标准能力基准评测，不涉及基准分数接近天花板后的饱和问题。 |
| J13 | 指令遵循 | NA | — | 因变量是政治/社会立场评分，不是指令遵循；不存在按约束类型拆分指令遵循准确率的设计。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p4: 'We ask the models to respond using numerical values between -10 and 10'；p13-14 示例显示模型输出单个数字；未报告格式合法率或重试策略。 | 有数字格式约束，但未报告解析合法率、格式失败与内容错误分开的指标。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估，没有有害请求集、攻击族或 ASR 测量。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1: 'Similar to humans, it is widely recognized that language models inherit biases...'；p8 将 LLM 与人类标注者比较；p9 讨论人类偏见与模型比较的局限。 | 明确把 LLM 的 bias/opinion 与人类同名构念作比较，并承认局限；但未系统论证构念异同、未报告权重 snapshot，也未做严格同范式人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究比较不同规模模型，但不报告随规模/训练进展的能力曲线，也不宣称涌现能力，J17 不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有以代理指标为优化目标进行训练、RL 或 best-of-N 优化，不涉及奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p4 报告每题 20 次评估、五次 debates；p5 Table 1 报告 Std-Dev；但未报告模型精确 snapshot/API 日期、CI 或配对检验。 | 有重复次数与标准差，但可复现性信息不足：snapshot 标识不精确，缺少置信区间与模型比较的配对检验。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p4 描述四轮 self-debate：opening、rebuttal、concluding rebuttal；但只报告 debate 前后最终评分，未按轮次独立评分。 | 做了多轮 debate 评估，但未报告逐轮一致性/行为轨迹，也未说明上下文截断处理。 |

## 编码小结
该研究提出了有意义的 self-debate 偏见稳健性范式，并覆盖多模型、多语言与人类对照；但整体以描述性均值比较为主，缺少随机化、顺序平衡、操纵检验、信效度证据、效应量/置信区间、随机效应建模及若干 LLM 评估透明度信息，因此多数适用组件的报告完整性为部分满足或缺失。
