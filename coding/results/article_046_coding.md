# article_046 | Transmission Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and Language-and-Vision Models Cannot (Yet) | 2023

研究类型概述：理论/立场论文，兼有初步实证比较：用工具创新任务（imitation vs innovation）比较儿童、成人及多个 LLM 的对象选择表现，并描述 blicket detector 因果过度假设研究。分析单位为儿童/成人被试与各 LLM 模型输出；因变量为对象选择正确率；模型每个情境按三种选项的六种顺序各查询一次并平均。全文无完整方法节、无正式推断统计与心理测量学报告。
- **研究构念（Construct）**：模仿与创新及因果工具使用推理（imitation versus innovation and causal tool-use reasoning）｜CA 构念锚定：创造性思维（creative thinking, `trm_4a3fd79d09f42`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：理论/立场论文，兼有初步实证比较：用工具创新任务（imitation vs innovation）比较儿童、成人及多个 LLM 的对象选择表现，并描述 blicket detector 因果过度假设研究。分析单位为儿童/成人被试与各 LLM 模型输出；因变量为对象选择正确率；模型每个情境按三种选项的六种顺序各查询一次并平均。全文无完整方法节、无正式推断统计与心理测量学报告。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.1: “Our study has two components: an ‘imitation’ component ... and an ‘innovation’ component...” | 明确命名并描述两个任务水平，但未报告条件分配方式、完整操纵程序或操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.1: “We averaged the scores (1 for selecting the relevant object and 0 for any other response) across the six repeated trials.” | 因变量指标与计分方式明确，但无信度、效度、剔除标准或天花板/地板预处理说明。 |
| A3 | 控制变量 | 0.5 | p.1: “we queried the models six times for every scenario to account for the six different orders... temperature of 0 and kept the default values for all other parameters” | 报告了选项顺序与温度控制，但控制变量清单不系统，未逐一说明所有控制手段。 |
| A4 | 混淆变量 | 0.5 | p.1: “it is unclear whether GPT-4’s improved performance stems from its multimodal character or from reinforcement learning from human feedback”; “systems referred to our earlier published blicket-detector articles as the source” | 识别了训练数据污染、RLHF/多模态等潜在混淆，但未系统控制或做敏感性分析，残余威胁仅泛泛讨论。 |
| A5 | 调节变量 | NA | — | 论文理论模型与实证分析均未包含正式调节变量或交互检验。 |
| A6 | 中介变量 | NA | — | 论文未提出或检验中介模型。 |
| A7 | 操作性定义 | 0.5 | p.1: “we present a series of problems... provide alternative objects... (a)... (b)... (c)...”; “1 for selecting the relevant object and 0 for any other response” | 关键任务有可观测操作化描述，但缺少完整情境数量、具体指导语、儿童施测细节与完整计分流程，不足以便利复现。 |
| A8 | 水平数与类型 | 0.5 | p.1: “an ‘imitation’ component... and an ‘innovation’ component”; models listed as “GPT-4, gpt-3.5-turbo, text-davinci-003... Claude... FLAN-T5” | 报告了任务水平与模型水平标签，但未说明水平类型、间距、全距或连续变量中心化等。 |
| A9 | 单一操作化的风险 | 0.5 | p.1: “Our work serves as a first step”; 工具任务仅一个对象选择范式，因果任务仅 blicket detector 范式 | 关键构念基本为单一操作化；文中虽以“first step”泛泛承认局限，但未系统讨论单一操作对可推广性的限制，也未报告多操作会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 核心测量为客观对象选择正确率，不是同源自陈式量表，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | 0.5 | p.1: 儿童 n = 42、成人 n = 30、五个模型分别报告均值；但未说明被试如何分配到组或条件 | 存在独立组比较（儿童、成人、模型），但未明确被试间分配逻辑与分配程序，故部分满足。 |
| B2 | 被试内设计 | NA | — | 论文未明确声明被试内重复测量设计；仅模型对每个情境重复六种选项顺序，属于刺激顺序控制而非明确的条件顺序设计。 |
| B3 | 混合设计 | NA | — | 未明确报告混合设计并逐因素标注组间/组内，也无混合模型或对应误差项。 |
| B4 | 因子设计 | NA | — | 论文未呈现正式因子设计、设计矩阵、每格样本量或交互项统计。 |
| B5 | 主效应 | NA | — | 无正式因子设计下的主效应统计检验；仅报告描述性均值与 SE。 |
| B6 | 交互作用 | NA | — | 未报告交互项检验、简单效应或交互图。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方设计。 |
| B9 | 准实验设计 | 0.5 | p.1: 比较儿童、成人与多个模型，非随机分组；并称“Our work serves as a first step”及“machines may need more than large-scale language and images” | 属于非随机组间比较，讨论了有限因果/推广解释，但未明确准实验类型、选择偏差来源或系统缓解措施。 |
| B10 | 被试内设计的适用条件 | NA | — | 无明确被试内处理条件设计，故不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无随机分配被试/模型到实验条件的程序；组别为自然属性或模型身份，非随机化实验。 |
| C2 | 平衡 | NA | — | 无明确被试内条件顺序需要平衡；模型六种选项顺序属于刺激位置平衡，归 E1/J1 处理。 |
| C3 | 恒定 | 0.5 | p.1: “temperature of 0 and kept the default values for all other parameters”; “Using exactly the same text input” | 报告了部分恒定控制（温度、输入文本、默认参数），但未系统列出设备/时段/版本等恒定变量及外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组或协变量纳入分析。 |
| C6 | 盲法 | 0 | p.1: 全文未报告对儿童/成人被试、实验者或评分者的盲法安排 | 存在人类被试与施测者，条件为直接指导语，但未报告任何盲法或评分者盲法控制。 |
| C7 | 平衡的层级 | NA | — | 无明确条件顺序平衡层级；选项顺序完全排列属于 E1/J1。 |
| D1 | 练习效应 | 0 | p.1: “a series of problems”但未报告练习块、截除规则或试次位置协变量 | 多题任务存在练习效应风险，但未报告任何练习控制或检验。 |
| D2 | 疲劳效应 | 0 | p.1: 未报告 session 时长、休息间隔或条件时间分散方案 | 儿童与成人完成系列问题，疲劳控制信息缺失。 |
| D3 | 延滞 / 迁移效应 | 0 | p.1: 两个任务组件（imitation/innovation）连续描述，未报告清洗期或条件对建模 | 若同一被试完成两个组件，存在迁移/残留风险但未处理；模型调用为独立查询，故主要问题在人类部分。 |
| D4 | 不对称迁移 | 0 | p.1: 未报告迁移对称性检验或顺序×条件交互 | 未检验不对称迁移，也未讨论平衡失效。 |
| D5 | 范围效应 | NA | — | 使用客观对象选择正确率，无主观量表范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.1: “we noticed that the models could alter their responses depending on how the order of options was presented, we queried the models six times for every scenario to account for the six different orders” | 模型选项顺序做了六种顺序的完全反平衡，但未报告人类刺激呈现顺序，也未给每种顺序的具体计数/分配细节。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | 0 | p.1: 未报告 cover story、单盲程序或事后访谈检查 | 人类儿童/成人可能推断任务意图，尤其是直接问“which go best”与“solve problem”，但无需求特征控制。 |
| E5 | 实验者效应 | 0 | p.1: 未报告被试是否知情分组、主试/评分者盲法、培训或脚本化程度 | 有实验者施测儿童，但无实验者效应控制信息。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.1: 报告各条件均值与 SE（如“Mdavinci = 8.87%, SEdavinci = 2.26%”），但无偏度、端点频率或 pilot 难度校准 | 报告了均值/SE，可初步看到 davinci 创新任务近地板，但未系统讨论天花板/地板或任务难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.1: 报告 n、均值与 SE（如“Mchildren = 88.4%, SEchildren = 2.82%”），但无效应量、95%CI、正式检验或多重性校正 | 有描述性不确定性和样本量，但统计结论效度报告不完整。 |
| F2 | 内部效度 | 0.5 | p.1: 识别训练数据污染、RLHF/多模态混淆与模型差异，但无随机分配、分配隐藏、基线等价检验或被试流向 | 对内部效度威胁有讨论，但缺乏系统控制与报告。 |
| F3 | 构念效度 | 0.5 | p.1: 全文从理论上论证 imitation/innovation 与因果过度假设构念，并描述任务；但无信度、效度、操纵检验或评分者信度 | 构念论证较充分，但心理测量学证据缺失。 |
| F4 | 外部效度 | 0.5 | p.1: 报告儿童 n = 42、Mage = 5.71、成人 n = 30、Mage = 27.80，并列出模型；讨论机器可能需更多于语言/图像数据 | 报告了样本特征与部分推广边界，但无抽样框、纳入排除标准或跨样本/跨情境复现。 |
| G1 | 分析单位 | 0.5 | p.1: 模型“六次”重复后“averaged the scores”；儿童/成人按组报告均值，但未说明分析单位与嵌套结构 | 有重复测量并被聚合，但未说明分配层级、分析层级或试次嵌套处理。 |
| G2 | 随机效应 | 0 | p.1: 无混合模型或随机效应结构；仅报告组均值与 SE | 被试/模型内重复观测未建模为随机效应，推断可推广性受限。 |
| G3 | 材料作为随机效应 | 0 | p.1: 使用“a series of problems”/“every scenario”，但未把情境/材料作为随机效应或报告 F1/F2/准 F | 材料/情境被视为固定，未处理项目推广问题。 |
| G4 | 统计功效 | 0 | p.1: 全文无事前功效分析、目标功效、预期效应量或样本量推导 | 无统计功效论证。 |
| G5 | 研究者自由度 | 0.5 | p.1: 报告了主要任务与均值，但无试次/被试剔除标准、全部因变量清单或样本量决定方式 | 部分透明度存在，但研究者自由度控制不足。 |
| G6 | 预先设定 / 预注册 | 0 | p.1: 全文未提及预注册、注册编号或分析计划 | 无预注册，且未区分验证性与探索性分析。 |
| J1 | 位置偏差 | 0.5 | p.1: “we noticed that the models could alter their responses depending on how the order of options was presented, we queried the models six times for every scenario to account for the six different orders” | 识别并控制了候选位置顺序（六种排列），但未报告翻转率、位置×正确率曲线或裁判模型/评分参数细节；此为多选而非 LLM-as-judge。 |
| J2 | 冗长偏差 | NA | — | 任务为对象选择，不涉及开放式生成长短与 LLM 裁判质量评分。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge 评估模型输出。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 未使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p.1: 仅给出示例性输入（如“Is the red one a blicket?”）和“Using exactly the same text input”，未给完整 prompt 模板、版本、敏感性消融或 dev/test 划分 | 自定义提示存在但未提供完整模板与敏感性分析，核心报告缺失。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短，无长文档/RAG 或位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.1: “temperature of 0 and kept the default values for all other parameters”; “queried the models six times” | 报告了温度、默认参数与重复次数，但无 top-p/top-k/seed、精确 snapshot、95%CI 或 bootstrap。 |
| J9 | 重复与文本退化 | NA | — | 任务为短选项选择，不涉及开放生成重复/退化。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本实验，无跨语言/跨格式比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.1: “once a particular cognitive test is explicitly described in Internet text, it then becomes part of a large language model’s training sample—we found that in some cases the systems referred to our earlier published blicket-detector articles as the source for their answers” | 明确识别污染风险并给出实例，但未系统报告训练截止日期、污染率或 held-out 检测。 |
| J12 | 基准饱和 | NA | — | 使用自建任务且模型分数未接近天花板；非标准基准饱和问题。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循，无约束指令集。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 任务为简单对象选择，不要求 JSON/文法约束等结构化输出。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: 全文明确讨论 LLM 作为文化技术而非个体智能体，并将模型表现与儿童对照；但未给权重快照/方法节中的构念操作定义 | 对 LLM 构念与人类同名构念的关系有系统理论讨论，也有人类对照；但缺少模型快照与正式构念效度操作化。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随规模/训练进展的能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标/奖励模型的优化或 overoptimization 监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.1: 报告每情境六次重复、均值与 SE，并列出模型名称；但无精确 snapshot 日期、95%CI、配对检验或原始日志 | 有重复次数与描述性不确定性，但 snapshot 不精确、无配对比较，复现性报告不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示-作答，无多轮对话历史。 |

## 编码小结
论文核心贡献是理论论证与初步比较，而非完整实验报告。若干关键构念与任务程序有描述，但分配、顺序、信效度、统计推断、预注册、材料随机化等报告严重不全；因此多数适用组件只能给 0.5 或 0，部分结构不存在者记 NA。
