# article_241 | OMEGA: Can LLMs Reason Outside the Box in Math? Evaluating Exploratory, Compositional, and Transformative Generalization | 2025

研究类型概述：该文构建并评估 OMEGA 数学推理泛化基准，包含探索性、组合性、变革性三条 OOD 泛化轴；使用程序化模板生成训练/测试题，评估多种前沿 LLM 在各复杂度层级上的 exact-match、Pass@k 与 CoT 行为，并对 Qwen2.5-7B 系列做 GRPO 强化学习前后比较。分析单位为题目/模板层级与模型/检查点层级，无人类被试。
- **研究构念（Construct）**：数学问题解决中的探索性、组合性、变革性泛化与过度思考｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）；计划（planning, `trm_4a3fd79d0acc1`）
- **实验任务与范式（Task / Paradigm）**：让DeepSeek-R1、Claude-3.7-Sonnet、o3-mini和o4-mini直接完成六个数学领域中逐级复杂的OMEGA题目，编码准确率、推理步骤类型和正确答案被改错的轨迹。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p5: “we define a scalar complexity measure δ ... For each generalization axis ... specify a training set ... distinct set of templates and parameter regions ... for testing”; p7: “evaluate four frontier models ... across different complexity levels, measuring exact-match accuracy on a held-out set of 100 samples per complexity level”; p10: RL on 1k training problems and ID/OOD evaluation. | 泛化轴、复杂度层级和 RL 前后条件可视为主要设计变量，且报告了多水平与生成程序；但没有正式操纵检验、分配机制说明或随机化/平衡细节，故为部分满足。 |
| A2 | 因变量 | 0.5 | p7: “measuring exact-match accuracy on a held-out set of 100 samples per complexity level”; p10: “report Pass@k”; p8-p9: 还分析 CoT token 数和错误模式。 | 因变量指标与计分方式明确，但未报告测量信度/效度证据、答案抽取与预处理细节，也未系统报告准确率的置信区间；仅部分满足。 |
| A3 | 控制变量 | 0.5 | p25: 训练/评估设定报告“each training set consists of 1,000 problems”、“same sampling strategy as training”、“temperature 1.0”、“seed 3”；p7: 报告模型版本；p25: 给出 GRPO 关键超参与评估协议。 | 已报告若干控制手段（固定模型版本、采样策略、seed、训练/测试规模、复杂度层级），但未以系统控制变量清单逐一说明控制手段，故为部分满足。 |
| A4 | 混淆变量 | 0.5 | p9: 讨论 lower accuracy 是否只是算术错误，并用 Matrix Rank 的 CoT 分段分析 conjecture/computation；p29-p31: 用 DP solver 与 token 估算检查 context-length 是否限制性能；p8-p9: 讨论 overthinking 与 error spirals。 | 识别并检查了若干潜在混淆（上下文长度、算术错误、overthinking），但未系统报告残余混淆或敏感性分析对内部效度的威胁，故为部分满足。 |
| A5 | 调节变量 | NA | — | 全文没有明确的调节变量理论模型、乘积项交互检验或简单斜率分析；域/模型差异仅作描述性比较，故不适用。 |
| A6 | 中介变量 | NA | — | 全文没有中介变量、直接/间接效应分解或 a/b 路径报告，故不适用。 |
| A7 | 操作性定义 | 1 | p5-p7: 明确说明 40 个模板生成器、6 个数学域、参数化复杂度 δ、训练/测试切分规则；p5: “solutions are programmatically generated ... symbolic, numerical, or graphical methods”；p18-p24: 各模板与复杂度水平表；p25: RL 训练与评估流程；代码链接见摘要。 | 关键构念（三类泛化、复杂度、RL 前后）和因变量（exact-match/Pass@k）均有较可重复的操作化程序与模板示例，满足复现要求。 |
| A8 | 水平数与类型 | 0.5 | p5: “δ: Θτ → Z+ ranks problems by increasing complexity”；p8 Figure 3 展示 1–7 复杂度层级；p18-p20 表 4–6 给出 Lv1–Lv5 及复杂度范围；p10: 训练用 levels 1–2，OOD 用更高层级。 | 报告了轴类别/复杂度层级与大部分层级取值，但未对每条泛化轴统一说明水平类型、水平间距、全距或连续变量的中心化处理，故为部分满足。 |
| A9 | 单一操作化的风险 | 0.5 | p5: “40 templated problem generators spanning six mathematical domains”；p10-p14: 在多个域、多个设置上报告 RL 前后表现；p18-p24: 各模板及组合/变革设置示例。 | 关键构念采用多模板、多域、多设置操作化，并非单一操作；但未报告各操作之间的会聚证据或形式化一致性检验，故为部分满足。 |
| A10 | 单一方法的风险 | NA | — | 自变量为问题模板/复杂度/训练条件，因变量为客观 exact-match/Pass@k；不存在自陈式同源测量或共同方法偏差问题，故不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或被试组分派；同一模型/检查点在多个条件/复杂度层级上被评估，不存在被试间独立组设计，故不适用。 |
| B2 | 被试内设计 | NA | — | 测试题为独立 LLM 调用，没有需要平衡的被试内条件顺序或重复测量顺序设计；报告的是跨题目/跨层级聚合准确率，故不适用。 |
| B3 | 混合设计 | NA | — | 研究并未设置组间/组内混合的人类实验因素，也无对应混合误差项分析，故不适用。 |
| B4 | 因子设计 | NA | — | 虽比较多个模型、域、复杂度与 RL 条件，但没有正式因子设计矩阵、每格样本量与主效应/交互 ANOVA 分析；不属于经典因子实验，故不适用。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验与效应量报告，故不适用。 |
| B6 | 交互作用 | NA | — | 没有交互项统计检验、简单主效应或交互图误差棒，故不适用。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计或区组变量报告，故不适用。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计，故不适用。 |
| B9 | 准实验设计 | NA | — | 这不是人类准实验设计；RL 前后比较虽有非随机训练干预，但全文没有按准实验类型、选择偏差、匹配或 DiD 等框架报告，故不按 B9 编码。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理可逆性/迁移对称性设计，故不适用。 |
| C1 | 随机化 | NA | — | 研究没有把分析单位随机分配到互斥实验条件；题目由模板参数生成，模型按条件评估，未报告随机分配与分配隐藏。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，无顺序平衡方案需要报告。 |
| C3 | 恒定 | 0.5 | p25: “temperature 1.0”、“seed 3”、“same sampling strategy as training”、固定训练/评估规模；p7: 明确 API 模型版本日期；p25: 给出完整 GRPO 关键超参。 | 列出了若干恒定变量及其水平（模型版本、温度、seed、训练/评估协议），但未系统讨论这些恒定设置对外部效度的限制，故为部分满足。 |
| C4 | 匹配 | NA | — | 没有人类被试或评分者的匹配设计；“matched training-test pairs”是任务构造，不是匹配分配，故不适用。 |
| C5 | 纳入为变量 | NA | — | 没有随机分组后把混淆变量作为区组/协变量纳入 ANOVA/ANCOVA 的设计；复杂度、上下文长度等作为分析检查而非协变量建模，故不适用。 |
| C6 | 盲法 | NA | — | 无人类被试/主试/人工评分者需要盲法；评估与主要分析为自动化 exact-match。LLM 标注者并非人类盲法对象。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级需要报告，故不适用。 |
| D1 | 练习效应 | NA | — | 测试题为独立 LLM 调用，无跨试次练习效应或练习块设计；RL 训练不属于被试内练习效应控制。 |
| D2 | 疲劳效应 | NA | — | LLM 评估无人类疲劳效应，亦无 session 休息/时间分散设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每道题/每次评估相互独立，无跨条件残留或清洗期设计。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉设计，故无迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观 exact-match/Pass@k，不是绝对判断或量表评分，无范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 主要是开放式数学作答与自动 exact-match，不涉及多候选项/刺激序列位置平衡；固定题序对独立 LLM 调用不构成选项位置偏差设计。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，使用掩饰情节或事后访谈检查需求特征的逻辑不适用。 |
| E5 | 实验者效应 | NA | — | 主要数据采集与评分自动化，无人类主试/评分者的实验者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p8: “performance begins near ceiling levels but steadily declines as problem complexity increases”；p10: “approaching 100% when the problem complexity is low ... performance drops to zero at complexity level 6”；p5: 设定 δ0 使 base model 在训练数据上低于 50%。 | 报告并讨论了低复杂度近天花板、高复杂度地板效应及难度校准思路，但未给出均值/SD/偏度/端点频率等完整分布统计，故为部分满足。 |
| E7 | 共同方法偏差 | NA | — | 无自评式 IV/DV 同源测量，故无共同方法偏差问题。 |
| F1 | 统计结论效度 | 0 | p7: “100 samples per complexity level”；p25: ID 100 题、组合/变革 20–50 题；p8-p14 主要以 exact-match/Pass@k 图形和点估计呈现，未见效应量、95%CI、多重性校正或正式假设检验。 | 未报告效应量或置信区间，样本量无功效分析依据，多重比较未说明校正，因此未达到基本要件。 |
| F2 | 内部效度 | 0.5 | p7: 说明 held-out 100 samples、模型版本；p25: 报告训练/评估协议、200 次评估取最后 5 checkpoints；p29-p31: 检查 context-length 不构成限制；但无随机分配/分配隐藏或系统基线等价性分析。 | 报告了训练/评估程序和部分内部效度检查，且 RL 前后有基线对照；但缺少正式随机分配、分配隐藏、残余混淆与损耗/敏感性分析，故为部分满足。 |
| F3 | 构念效度 | 0.5 | p5: “solutions are programmatically generated ... validated ... symbolic, numerical, or graphical methods”；p7-p10: 使用 exact-match/Pass@k 与多域多模板；p25: 训练题限制在 base model 低于 50% 的复杂度。 | 提供了答案正确性构造验证（程序化/符号/数值/图形）与多操作化，但未报告评分信度、LLM 标注一致性或正式操纵检验，故为部分满足。 |
| F4 | 外部效度 | 0.5 | p7: 四个 frontier models 与版本；p10: Qwen2.5-7B-Instruct 与 Qwen2.5-Math-7B；p27-p28: 补充 Qwen Math-7B 结果；p5: 六域 40 模板。 | 报告了模型来源、版本、多个领域和部分跨模型复现；但未系统界定结果对模型总体、数学域或真实课堂/竞赛情境的推广边界，故为部分满足。 |
| G1 | 分析单位 | 0.5 | p7: “100 samples per complexity level”；p25: “ID problems: 100 test samples”、“Compositional and Transformational problems: 20–50 test samples per setting”；p10-p14: 按 domain/setting 聚合准确率。 | 说明了样本与聚合评估层级，但题目嵌套于模板/域、模型/检查点重复评估的层级结构未被多层模型显式处理，故为部分满足。 |
| G2 | 随机效应 | 0.5 | p10: 使用 Qwen2.5-7B-Instruct 与 Qwen2.5-Math-7B；p25: 评估 200 次，报告最后 5 个 checkpoints 平均；未见混合模型/随机效应设定。 | 对检查点波动做平均，但未明确哪些因子为随机/固定效应，也未说明模型或检查点抽样的总体推广范围，故为部分满足。 |
| G3 | 材料作为随机效应 | 0 | p5: 使用 40 个模板生成器；p7: 每个复杂度层级 100 个 held-out 样本；p18-p24: 固定模板族与设置列表。分析按模板/域聚合，但未见 item/template 随机效应或准 F 比。 | 有限模板被视为固定材料，结论却推广到数学推理能力/泛化轴，未把材料作为随机因子建模，未达到基本要件。 |
| G4 | 统计功效 | 0 | p7: 100 samples per complexity level；p25: 20–50 test samples per setting；全文未见事前功效分析或准确率置信区间；Figure 3、8–14 主要为点估计/柱状图。 | 没有功效分析、目标效应量或样本量推导，也未系统报告效应量与 CI，故未达到基本要件。 |
| G5 | 研究者自由度 | 0.5 | p25: 报告训练集 1,000 题、ID 100 题、组合/变革 20–50 题、评估 200 次取最后 5 个 checkpoints；p7: held-out 100 samples；p10-p14: 报告多域、多个设置结果。 | 报告了样本量、评估协议和多个结果，但未报告数据/试次剔除规则、是否中途停止或追加、探索性与验证性分析的区分，故为部分满足。 |
| G6 | 预先设定 / 预注册 | 0 | p25 报告训练与评估细节，但全文未见预注册平台、注册编号、预注册分析计划或明确声明为纯探索性研究。 | 没有数据收集前预注册，也未区分验证性与探索性分析；按规则记 0，而非 NR。 |
| J1 | 位置偏差 | NA | — | 主要评估为开放式数学答案 exact-match/Pass@k，非多候选项选择、排序或 LLM-as-judge 成对比较；无候选位置操纵。 |
| J2 | 冗长偏差 | NA | — | LLM 裁判（o4-mini）用于句子分类/计算正确性标注，不是对开放式答案质量按长度打分；不构成长度被误当质量的评估场景。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或纠错对话，不涉及谄媚/附和测量。 |
| J4 | 自我偏好 | 0.5 | p9: “asked O4-mini to label each segment”；p7: O4-mini 本身也是被评估模型之一；p26: 给出分类 prompt；未报告裁判与人类金标准一致性、匿名化或自我偏好量化。 | 用于标注 DeepSeek-R1 CoT 的裁判为 O4-mini，属异源裁判，但未系统报告同源/异源控制、各裁判单独结果或自我偏好偏差率，故为部分满足。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主实验不是 few-shot in-context learning 设计；标注 prompt 为指令式、零样本示例，未使用 few-shot 示例集。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p26: 提供 CoT 分段标注的完整 prompt；p25: 报告 chat template 名称与训练超参；但主要评估 prompt 全文、版本、迭代日期与敏感性消融未报告。 | 提供了部分 prompt 模板，但未做语义等价措辞敏感性分析，也未说明 dev/test 划分与 prompt 调参过程，故为部分满足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不是长上下文/RAG 信息位置实验；Appendix D 只检查题目所需 token 是否在 context window 内，未操纵关键信息首/中/尾位置。 |
| J8 | 温度与采样随机性 | 0.5 | p25: “temperature 1.0”、“seed 3”、“num_samples_per_prompt_rollout 64”，评估 200 次并取最后 5 个 checkpoints 平均；p7 脚注给出 Claude/o3-mini/o4-mini 版本日期；但 frontier API 采样参数、top-p/top-k 与置信区间未完整报告。 | 报告了部分采样超参、seed 和重复评估，但闭源 API 的完整采样设置与多次采样 CI 不完整，故为部分满足。 |
| J9 | 重复与文本退化 | 0.5 | p8-p9: 报告错误回答 token 更多、overthinking、reasoning spirals；p25: 报告 temperature 1.0、max_token_length 8192、response_length 6336；但未报告 n-gram 重复率/退化率/截断比例。 | 报告了解码相关设置并定性分析重复/螺旋退化，但缺少重复率与截断比例等 QC 指标，故为部分满足。 |
| J10 | 分词效应 | NA | — | 实验为英文数学题、单语言单脚本，无跨语言/跨脚本 token 数比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p5-p7: 题目由程序化模板生成并可发布；p7: 报告评估模型版本；但全文未见训练截止日期对照、n-gram/DCQ 污染检测或污染率。 | 虽使用新生成的 held-out 题集，但未证明模板/问题不在预训练语料中，也未报告污染检测；按基准评估适用规则记 0。 |
| J12 | 基准饱和 | 0.5 | p8: “performance begins near ceiling levels but steadily declines”；p10: Pass@k 在低复杂度接近 100%，高复杂度降至 0；p7: 每层级 100 样本，主要用 exact-match。 | 识别了低复杂度近天花板并设计了更高复杂度层级，但未在近饱和区改用连续指标或报告 bootstrap CI，故为部分满足。 |
| J13 | 指令遵循 | NA | — | 因变量是数学答案正确性/exact-match，不是指令遵循；无否定/数量/格式/风格约束准确率测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p26: 要求 o4-mini 以 JSON 格式输出分类结果；p25: 训练设置包含“apply_r1_style_format_reward True”和“apply_verifiable_reward True”；但未报告格式合法率、重试策略或格式失败与内容错误的分开统计。 | 存在结构化/格式约束设置，但缺少格式合法率与格式失败独立指标，故为部分满足。 |
| J15 | 越狱稳健性 | NA | — | 研究为数学能力基准，不涉及有害请求、越狱或安全对齐评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1: 以 Boden 创造力类型学定义探索性/组合性/变革性；p3: “unlike humans who fluidly integrate mastered skills”；p10-p14: 将 LLM 与人类数学家能力作对比；但无人类同范式对照或系统构念效度论证。 | 论文使用认知科学/人类创造力构念解释 LLM 数学泛化，并报告模型版本与跨模型比较，但未系统说明 LLM 构念与人类同名构念的异同，故为部分满足。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究不报告随模型规模/训练进展的涌现曲线，只比较若干固定模型与复杂度层级，故不适用。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | p10-p14: 用 GRPO 在 1k 训练题上优化，并在 ID/OOD 测试集上评估 RL 前后；p13-p14: 讨论 OOD 无提升甚至下降；p27-p28: 做技能配对消融；但未报告优化轮次 vs 代理/gold 双曲线。 | 优化对象（训练题 reward）与 held-out ID/OOD 评估分离，并报告 OOD 不提升；但未绘制 overoptimization 曲线、未报告 LLM-judge 一致性衰减，故为部分满足。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p7 脚注: “Claude (2025-02-19), o3-mini (2025-01-25), o4-mini (2025-04-16)”；p25: seed 3、评估 200 次、最后 5 checkpoints 平均；但未见 95%CI、配对检验或逐题日志/推理日志发布说明。 | 报告了部分重复评估和模型版本标识，但 snapshot 不完全（如 DeepSeek-R1 日期未列）、无 CI 与配对检验，故为部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮数学题求解，无多轮对话历史或轮次一致性评估。 |

## 编码小结
这是一项以程序化基准和 LLM 训练前后评估为核心的研究。优点是问题生成、模板控制、训练/测试分离、多模型多领域比较和 RL 前后对比较系统；不足是推断统计、置信区间、随机效应/材料抽样、污染检测、提示敏感性、采样复现细节与 LLM 裁判验证报告有限，很多经典人类实验组件不适用。
