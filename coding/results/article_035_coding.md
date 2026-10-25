# article_035 | In-Context Impersonation Reveals Large Language Models' Strengths and Biases | 2023

研究类型概述：该文属于 LLM 行为/提示条件评估研究（LLM-as-participant 风格），不是人类被试实验。研究通过给 Vicuna-13B 与 ChatGPT/gpt-3.5-turbo 加人格前缀“If you were a {persona}”，在二臂老虎机、MMLU 推理和基于 CLIP 的细粒度图像分类描述任务中比较年龄、专业、种族、性别等人格条件；分析单位为独立的 LLM 调用/游戏/题目/类别描述，主要比较条件间奖励、准确率与回归系数。
- **研究构念（Construct）**：角色扮演诱导的探索策略与社会角色偏差（persona-induced exploration strategy and social-role bias）｜CA 构念锚定：计划（planning, `trm_4a3fd79d0acc1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：该文属于 LLM 行为/提示条件评估研究（LLM-as-participant 风格），不是人类被试实验。研究通过给 Vicuna-13B 与 ChatGPT/gpt-3.5-turbo 加人格前缀“If you were a {persona}”，在二臂老虎机、MMLU 推理和基于 CLIP 的细粒度图像分类描述任务中比较年龄、专业、种族、性别等人格条件；分析单位为独立的 LLM 调用/游戏/题目/类别描述，主要比较条件间奖励、准确率与回归系数。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.2: 'prefixing the prompt with “If you were a {persona}”'; p.3: ages 2,4,7,13,20; man/woman; black/white; p.3-5 task-specific prompts. | 人格提示被明确操纵并给出多个水平与程序，但未报告操纵检验，条件分配主要是全条件运行而非随机分配，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.4 'average reward per trial'; p.5 'accuracy'; p.5 'repeat them five times. We report the mean performance as well as 95% confidence intervals'; p.5 CLIP classification accuracy. | 因变量指标与计分方式清楚，视觉任务有重复和置信区间；但无信效度证据，也无系统连续指标预处理/天花板地板说明。 |
| A3 | 控制变量 | 0.5 | p.3 Vicuna-13B and gpt-3.5-turbo; p.3 temperatures 0.7/1; p.5 top-k 50 and max 96 tokens; p.5 'We did not tune these values'; p.8 CLIP variants. | 报告了模型版本、解码参数、VLM 选择等控制，但未以系统控制变量清单逐项说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.6 'As LLMs seem sensitive to prompts [69]... six prompt variations'; p.5 class-name removal post-processing; p.8 'language encoder of VLMs potentially being weaker'. | 识别并部分控制了提示敏感性与类名泄漏，也提到 VLM 语言编码器差异，但未系统讨论残余混淆和敏感性分析。 |
| A5 | 调节变量 | NA | — | 没有调节假设或调节效应检验；人格类别是操纵的自变量，不是调节变量。 |
| A6 | 中介变量 | NA | — | 没有中介变量或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.2 persona prefix; p.4 bandit prompt and reward sampling; p.4-5 MMLU answer-token argmax; p.5 vision prompt and CLIP scoring. | 关键构念均给出了可观测、可重复的操作化程序，包括提示、答案选择与计分。 |
| A8 | 水平数与类型 | 0.5 | p.3 '2, 4, 7, 13, or 20-year-old'; p.3 'man or a woman'; 'black person or a white person'; p.6 additional ages 2-60 in steps. | 报告了各人格条件的水平标签和部分年龄间距，但未系统说明变量类型、全距与中心化/标准化。 |
| A9 | 单一操作化的风险 | 0.5 | p.3-5 three tasks; p.8 multiple CLIP variants; p.9 'two very different language models'. | 使用多任务、多模型、多提示变体提供了部分会聚证据，但多为定性比较，未正式量化不同操作化间的会聚。 |
| A10 | 单一方法的风险 | NA | — | 不涉及自陈式多构念测量；自变量是提示操纵，因变量是客观任务奖励/准确率，不是共同方法偏差语境。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配；LLM 调用不是独立被试组，条件为提示全交叉评估。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量及顺序平衡；各提示调用基本独立。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合设计及相应误差项。 |
| B4 | 因子设计 | NA | — | 人格类别分别比较，未形成完整因子设计矩阵与 ANOVA 交互检验。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无因子设计意义上的交互项检验。 |
| B7 | 区组设计 | NA | — | 未使用人类区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无人类被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验或非随机分组的人类干预研究。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理的适用条件论证。 |
| C1 | 随机化 | NA | — | 无人类随机分配与分配隐藏；人格条件由提示全交叉设定。 |
| C2 | 平衡 | NA | — | 无人类条件顺序平衡问题。 |
| C3 | 恒定 | 1 | p.3 Vicuna-13B and gpt-3.5-turbo; p.5 temperature, top-k, max tokens; p.8 CLIP ViT-B/32, ViT-B/16, OpenCLIP; p.10 limited range of personas/tasks. | 明确列出模型、解码与 VLM 选择等恒定设置，并在结论中讨论有限人格与任务范围的外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.6 all Vicuna experiments run with six prompt variations; p.8 Chi2 tests consider 'three CLIP models, five different seeds and the six different impersonation prompt variations'. | 提示变体/模型/种子被作为稳健性因素纳入比较，但未作为区组或协变量建模，也未报告斜率齐性或调整后效应。 |
| C6 | 盲法 | NA | — | 自动评估，无人类被试或人类评分者盲法。 |
| C7 | 平衡的层级 | NA | — | 无人类条件顺序平衡层级。 |
| D1 | 练习效应 | 0.5 | p.4 prompt-chaining across previous trials; p.6 trial number and age entered in regression; β=0.63, p<.001 for trial effect. | 试次位置被建模并报告学习趋势，但无练习块、初期截除标准或跨被试练习控制。 |
| D2 | 疲劳效应 | NA | — | 自动化 LLM 任务，无人类疲劳效应风险。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件使用独立提示/游戏，没有跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为奖励/准确率等客观指标，无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | p.4-5 MMLU prompt lists fixed options A, B, C, D; p.5 predicted option via argmax over A-D; no shuffling or position counterbalancing reported. | 未对选项位置随机化或反平衡，也未讨论多选题位置偏差。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在人类需求特征或掩饰情节。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试/评分者。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 reward curves and regression; p.7 MMLU accuracy with random baseline; p.8 vision accuracy; no endpoint frequencies or skew reported. | 报告均值/部分 CI 和随机基线，并讨论部分任务接近随机；但未报告偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式同源多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.6 regression β and p values; p.5 95% confidence intervals for repeated vision runs; p.8 Chi2 tests p<0.001; no a priori power analysis or multiplicity correction. | 报告了效应量/部分 CI 与显著性，但缺样本量依据、系统多重校正和统计假设说明。 |
| F2 | 内部效度 | 0.5 | p.6 all Vicuna experiments with six prompt variations; p.8 three CLIP models, five seeds, six prompt variations; no human allocation concealment, baseline equivalence, or attrition flow. | LLM 条件全交叉并有提示/模型稳健性检查，但无人类随机分配、分配隐藏、基线等价和损耗处理。 |
| F3 | 构念效度 | 0.5 | p.8 Chi2 tests for expertise/race/gender; p.9 qualitative age-description patterns; no formal manipulation check or reliability/validity evidence. | 有跨任务/模型会聚和定性操纵迹象，但无正式操纵检验或信效度论证。 |
| F4 | 外部效度 | 1 | p.7 CUB and Stanford Cars; p.8 three VLM variants; p.9 Vicuna-13B vs ChatGPT; p.10 limited range of personas and simple tasks. | 报告数据集与模型来源，并在多数据集/多模型/多 VLM 上复制，同时说明有限人格和任务范围的推广边界。 |
| G1 | 分析单位 | 0.5 | p.6 '2k two-armed bandit games of 10 trials'; p.6 'average task accuracy'; p.5 'classification accuracy of the test splits'. | 说明了主要分析层级，但未显式处理试次嵌套于游戏、题目嵌套于任务等聚集结构。 |
| G2 | 随机效应 | NA | — | 无人类被试随机效应；模型版本作为固定比较对象，不涉及从模型总体抽样的随机效应结构。 |
| G3 | 材料作为随机效应 | 0.5 | p.6-7 MMLU all tasks and per-task results; p.7-8 CUB/Stanford Cars classes; p.8 multiple datasets. | 使用多个任务/类别/数据集并报告汇总与部分个案，但未使用项目随机效应或准 F 比，材料仍被当作固定集合分析。 |
| G4 | 统计功效 | 0.5 | p.5 'repeat them five times' and 95% CI; p.6 regression coefficients; p.8 Chi2 tests; no power analysis or sample-size justification. | 报告部分效应量和 CI，但无设计阶段功效分析或样本量推导。 |
| G5 | 研究者自由度 | 0.5 | p.6 six prompt variations; p.8 five seeds; p.9 ChatGPT vision only original prompt for computational reasons; no exclusion rules or stopping rules. | 报告了主要条件与部分计算限制，但缺数据排除规则、样本量决定方式及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No pre-registration platform, number, or link is reported; p.6-9 analyses appear post hoc. | 无预注册，也未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | 0 | p.4-5 MMLU prompt presents answer options A-D; p.5 predicted option is argmax over A-D; no answer-position randomization, swap, or flip-rate analysis. | 未控制或报告候选位置偏差；多选题选项位置固定，未做交换重判或位置×正确率分析。 |
| J2 | 冗长偏差 | NA | — | 使用 CLIP 进行下游视觉分类评估，不是 LLM-as-judge 或 LLM 质量评分，长度偏好风险不属于该组件。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错操纵，不涉及谄媚测量。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 作为裁判；评估由 CLIP/OpenCLIP 完成。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.3 'all experiments are conducted in a zero-shot fashion'; p.5 four examples only for class-name post-processing, not main few-shot condition. | 主实验为零样本；没有 few-shot 示例选择/排列的实验性比较。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.6 'we follow the meta-prompting approach from [26] to vary our impersonation prompts... six prompt variations'; p.4-5 prompt templates; full variations in suppl. A.1. | 有提示变体敏感性消融和模板，但未给出完整版本管理、dev/test 划分及完整主文模板。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短（如 10 试次、单题 MMLU），无长文档/RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.3 temperature 0.7 for sentences and 1 for single token; p.5 Vicuna top-k 50, max 96 tokens; p.5 five repetitions with 95% CI; no seed/top-p/snapshot. | 报告主要采样超参与视觉重复，但缺随机种子、top-p、精确 API snapshot 与所有条件的重复方差。 |
| J9 | 重复与文本退化 | 0.5 | p.5 auto-regressive sampling, default top-k 50, max 96 tokens; no repetition penalty or n-gram degeneration rate. | 报告了解码策略与长度上限，但未报告重复率/退化率 QC，也未系统比较条件间解码退化。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言、单脚本，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4 MMLU dataset; p.7 CUB and Stanford Cars; p.3 model descriptions; no training-cutoff comparison or contamination detection. | 使用公开基准但未报告测试集版本与训练截止日期对照，也未做污染检测；不能排除记忆/污染影响。 |
| J12 | 基准饱和 | NA | — | MMLU 准确率约 0.2-0.4，视觉分类准确率也较低，未接近天花板，基准饱和风险不突出。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，未测量约束违反准确率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 无 JSON/文法约束等结构化输出要求；主要是自由文本描述或单选 token。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/对齐或越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 'recover human-like developmental stages of exploration'; p.6 'in line with psychological literature'; p.9 'LLM's may not faithfully represent the language of children'; p.10 limitations. | 有 LLM 行为与人类构念的类比及部分限制说明，但未系统论证 LLM 测量构念与人类同名构念的异同，也无人类对照实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随模型规模/训练进展的能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及以 benchmark/奖励模型/LLM-judge 为优化目标的训练、RL 或 best-of-N 过优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 five repetitions and 95% CI for vision; p.3 Vicuna-13B and gpt-3.5-turbo; no exact snapshot/API date, seed, or paired tests. | 报告了部分重复次数与 CI，但模型 snapshot 不精确，缺 seed、原始日志和配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究不是多轮对话一致性评估；bandit 的 10 试次是序列决策任务，不是对话式部署测试。 |

## 编码小结
论文以多任务、多模型、多提示变体和多 VLM 变体提供了较丰富的 LLM 人格提示效应证据，并报告了部分重复与置信区间、定性描述和显著性检验。但作为 LLM 行为评估，缺少操纵检验、候选位置/顺序控制、完整解码与 seed/checkpoint 报告、污染检查、功效与预注册；人类被试设计组件大多不适用。整体方法透明度中等，可复现性仍有明显缺口。
