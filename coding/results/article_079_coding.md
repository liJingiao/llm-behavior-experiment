# article_079 | Towards Dynamic Theory of Mind: Evaluating LLM Adaptation to Temporal Evolution of Human States | 2025

研究类型概述：构建并评估 DYNToM 动态 ToM 多项选择基准：用 GPT-4-Turbo 生成 1,100 个社会情境、5,500 个场景和 78,100 个问题，并进行人工验证；对 10 个 LLM 进行 vanilla/CoT 零样本评测，并与 10 名研究生人类基线比较；辅以心理状态、题型、时间跨度和截断序列的亚组/受控比较。分析单位为模型-问题回答，而非人类被试实验。
- **研究构念（Construct）**：动态心智理论（Theory of Mind）与跨场景心理状态追踪｜CA 构念锚定：心理理论（theory of mind, `trm_4a3fd79d0b392`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：构建并评估 DYNToM 动态 ToM 多项选择基准：用 GPT-4-Turbo 生成 1,100 个社会情境、5,500 个场景和 78,100 个问题，并进行人工验证；对 10 个 LLM 进行 vanilla/CoT 零样本评测，并与 10 名研究生人类基线比较；辅以心理状态、题型、时间跨度和截断序列的亚组/受控比较。分析单位为模型-问题回答，而非人类被试实验。｜CA 任务锚定：心理理论任务（theory of mind task, `trm_4c8a8467304e2`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: 'We employed two evaluation approaches: (1) vanilla prompting... (2) zero-shot chain-of-thought (CoT) prompting'; p.21 Fig.17 reports the two prompt templates; p.8 reports truncation experiment. | 明确操纵了提示方式（vanilla/CoT）及截断序列水平，但未报告操纵检验，分配/顺序细节也不完整。 |
| A2 | 因变量 | 0.5 | p.4: 'consider the LLM’s response correct only if it exactly matches the ground truth option'; p.6 Table 3 reports accuracy percentages. | 因变量为精确匹配准确率，计分方式清楚；但缺少准确率测量的信效度、重复运行方差/CI、连续指标预处理及天花板地板处理说明。 |
| A3 | 控制变量 | 0.5 | p.5: 'we used a temperature of 0.7 and top-p of 0.9 across all models to ensure fair comparison'; p.13 Table 6 lists model versions. | 报告了固定采样参数和模型版本等部分控制，但未系统列出全部控制变量及其控制手段。 |
| A4 | 混淆变量 | 0 | p.9 Limitations only discusses 'Limited LLMs', 'Limited Prompt Methods', 'Limited mental states types and evaluation modality'. | 未识别并控制模型规模/训练数据、生成模型（GPT-4-Turbo）与评测模型重叠等潜在混淆，也未讨论残余混淆对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 理论模型不含调节变量；按心理状态、题型、时间跨度分组只是描述性比较，未做调节交互检验或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 理论模型不含中介变量，未提出或检验中介路径。 |
| A7 | 操作性定义 | 1 | p.3-4: four-step construction framework; p.4 exact-match scoring; p.20 Fig.15 question templates; p.21 Fig.17 evaluation prompts. | 对基准构造、场景/问题生成、题型模板、模型提示和准确率计分给出了可复现的操作化程序。 |
| A8 | 水平数与类型 | 0.5 | p.5: 'ten representative language models, ranging from 7B to 70B parameters'; p.13 Table 6 lists sizes/versions; Table 1 lists question-type proportions. | 报告了模型、提示方式和题型等水平及标签，但未系统说明水平类型（名义/连续）、间距/全距及连续变量中心化处理。 |
| A9 | 单一操作化的风险 | 0 | p.9 Limitations only mentions limited models, prompt methods, mental-state types and modality; no convergent validation of ToM operationalizations. | 关键构念仅用单一基准/单一准确率操作化，且未讨论单一操作化对可推广性的限制或提供会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 因变量为客观选项匹配，不涉及自陈式同源测量；共同方法偏差在此类基准评测中不适用。 |
| B1 | 被试间设计 | NA | — | 无人类或 LLM 单位被随机分配到互斥实验条件；模型比较为观察性基准比较，非被试间实验。 |
| B2 | 被试内设计 | NA | — | vanilla/CoT 及不同问题是在独立 API 调用中作答，无同一会话内条件顺序需要平衡；未报告顺序设计也不构成 B2 的适用结构。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素混合实验及相应混合模型/误差项结构。 |
| B4 | 因子设计 | NA | — | 虽按模型、提示、状态、题型分组报告，但不是正式因子实验，未报告完整设计矩阵与 ANOVA 交互统计。 |
| B5 | 主效应 | NA | — | 无因子实验主效应检验。 |
| B6 | 交互作用 | NA | — | 无正式交互项检验及简单主效应分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计及区组变量。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 无准实验处理分配；研究是基准构建与模型比较。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理及可逆性/迁移对称性设计。 |
| C1 | 随机化 | NA | — | 无处理分配/随机化到互斥条件；随机抽样用于构建题库，不是条件分配。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p.5: temperature 0.7 and top-p 0.9 across all models; p.13 Table 6 lists model versions/context windows. | 报告了部分保持恒定的评测参数与模型版本，但未系统列出所有恒定变量，也未充分讨论固定解码/提示设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 无匹配/配对设计。 |
| C5 | 纳入为变量 | 0 | p.13 Table 6 reports model sizes and versions; no model includes size/architecture as covariate or blocking factor. | 模型规模/架构等已知混淆被记录但未纳入分析模型或区组/协变量控制。 |
| C6 | 盲法 | NA | — | 无需要对实验条件施盲的人类被试/评分者；人工标注用于数据质量验证而非条件结局评分。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 每个问题独立作答，无上下文内学习或练习块。 |
| D2 | 疲劳效应 | NA | — | LLM API 评测无人类疲劳或 session 时长问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立调用/重置上下文，无跨条件延滞或迁移。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为准确率，无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | p.4 'Options and Ground Truth' describes distractor construction; p.20 Fig.15 example lists ground truth 'c' with no option-order randomization. | 多项选择选项顺序未报告随机化或反平衡，正确答案位置偏差未控制。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分及跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或掩饰情节问题；提示语是模型评测指令而非人类 cover story。 |
| E5 | 实验者效应 | NA | — | 数据采集自动化，无人类主试/评分者知晓条件并传递期望的实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 3 reports model/human accuracy means; p.6 discusses GPT-4o near-human on understanding-type questions and low scores such as DeepSeek-V2 7.2%. | 给出了均值准确率和明显高低端表现，但未报告偏度、端点频率或 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | IV 与 DV 不涉及同源自陈式多构念测量；准确率为客观匹配。 |
| F1 | 统计结论效度 | 0.5 | p.6 reports percentage-point gaps (e.g., '6.9 percentage points') and human SD, but no confidence intervals or formal significance tests; p.5 no power analysis. | 报告了准确率差异作为效应量信息，但缺少 CI、样本量/功效依据、多重比较校正及统计假设检验。 |
| F2 | 内部效度 | NA | — | 无人类随机分配、分配隐藏、被试流向与损耗结构；截断比较是同模型同题项的受控描述，不适用 ITT/flow 评估。 |
| F3 | 构念效度 | 0.5 | p.3-4: four annotators scored trajectories/scenarios/questions on 5-point dimensions, discarding items below 4.0; p.5 human baseline. | 提供了基准题项质量与真实性的人工验证证据，但无评分者信度统计、正式效度分析或操纵检验；仍为单一 ToM 操作化。 |
| F4 | 外部效度 | 0.5 | p.5 lists 10 models and human baseline; p.9 Limitations discusses only ten models, vanilla/CoT, limited mental states/modality. | 报告了模型样本来源与推广边界，但未报告跨样本/跨情境复现，且人类标注者代表性信息很少。 |
| G1 | 分析单位 | 0.5 | p.5: 'we calculate their accuracy across all 78,100 questions'; p.6 Table 3 aggregates by model/state/type. | 分析层级为问题回答并聚合成模型/条件均值；问题嵌套于 social stage/scenario 的聚类结构未显式建模。 |
| G2 | 随机效应 | 0 | p.5-6 report only aggregated accuracy means; no mixed/multilevel model or random-effect structure is specified. | 未报告模型/问题/场景的随机效应结构，且将模型作为固定比较；对更广 LLM 总体及题目聚类的推断缺少随机效应支持。 |
| G3 | 材料作为随机效应 | 0 | p.4 fixes 78,100 generated questions; p.6 Table 3 reports model means over these fixed items; no item random effect or F1/F2 analysis. | 有限题目/场景被当作固定测试材料，未考虑材料随机效应；结论推广到任意动态 ToM 题项时受限。 |
| G4 | 统计功效 | 0 | p.5 describes benchmark size and model sample, but no a priori power analysis; p.6 reports point accuracy without CIs. | 无设计阶段功效分析或样本量论证，结果部分也缺少效应量 CI。 |
| G5 | 研究者自由度 | 0.5 | p.3-4 report validity thresholds and retention rates (e.g., 85.4%, 88.7%); p.5 reports all question types and model set; p.9 lists limitations. | 报告了数据生成/剔除规则和主要条件，但未说明样本量决定/停止规则，也未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement or registry link is reported in the paper. | 无预注册，无法区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | 0 | p.4 describes option/ground-truth construction; p.20 Fig.15 example has ground truth option 'c' and does not mention option-position randomization or A/B swapping. | 多项选择候选项位置偏差未识别、未随机化/反平衡，也未报告位置×正确率或翻转率。 |
| J2 | 冗长偏差 | NA | — | 评测为多项选择精确匹配，不是开放式生成质量评分，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错式对话操纵。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge；评分由 ground truth 精确匹配完成。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 评测采用 zero-shot vanilla/CoT，无 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.21 Fig.17 provides full vanilla and CoT prompt templates; p.5 describes the two prompting methods. | 公布了完整提示模板，但未报告版本号/迭代、语义等价措辞敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p.8 reports a 'U-shaped' pattern across time spans and Table 5 reports truncation comparisons; Table 1 gives average scenario/question lengths; Table 6 gives context windows. | 实际检查了中间位置/序列截断对正确率的影响，但未报告精确上下文 token 数、位置反平衡或完整位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0.5 | p.5: 'we used a temperature of 0.7 and top-p of 0.9 across all models'; no seed, repeated sampling N, or CI is reported. | 报告了主要采样超参，但缺少随机种子、重复运行次数及不确定性估计。 |
| J9 | 重复与文本退化 | 0.5 | p.5 reports temperature/top-p; p.7 analyzes intermediate CoT outputs; repetition penalty/退化率/截断比例未报告。 | 报告了解码采样策略的一部分，但未报告 repetition penalty、重复率/退化率和生成长度截断控制。 |
| J10 | 分词效应 | NA | — | 单语言英文任务，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.13 Table 6 gives model versions but no training cutoff versus benchmark-construction date comparison or contamination test; GPT-4-Turbo also generated data and was evaluated. | 新基准未报告污染检测、n-gram 重叠或训练截止日期对照，也未证明 held-out；存在数据生成与评测模型重叠风险。 |
| J12 | 基准饱和 | NA | p.6 Table 3: LLM average 33.0% vs human 77.7%; best GPT-4o 64.0%. | 整体分数远未接近天花板，饱和风险不构成主要问题；因此该组件不适用，而非因缺失报告给 0。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，未设置需机器判定的约束指令。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.21 Fig.17 prompts require 'response in JSON format'; p.20 Fig.15 provides options and ground truth. | 要求 JSON 结构化输出，但未报告格式合法率、重试策略，也未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全性/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.5 uses ten graduate students as a human baseline on the same task; p.9 Ethics: 'our objective is not to anthropomorphize LLMs' but to evaluate capacity to comprehend mental states. | 有同一范式人类基线和避免直接拟人化的说明，但未系统论证 LLM 上测量的 ToM 与人类同名构念的异同，也未做构念效度实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随模型规模/训练进展的能力曲线或涌现宣称；仅包含 7B 到 70B 等模型比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL、best-of-N 或针对代理指标的优化环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.13 Table 6 gives precise model version strings, but p.6 reports single accuracy scores with no repeated-run N, CI, paired tests, or inference logs. | 有较精确的模型 snapshot/version，但缺少重复采样、置信区间和配对检验；不满足可复现性核心要求。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 每次问题在单个提示中连同完整故事作答，非多轮对话累积历史；未评估跨轮次一致性衰减。 |

## 编码小结
基准构建流程、题项模板和 DV 计分较透明，但统计推断、选项位置控制、重复采样与置信区间、污染检查、随机效应/聚类处理、预注册及多数实验设计质控缺失。总体是描述性 LLM 基准评测而非严格实验。
