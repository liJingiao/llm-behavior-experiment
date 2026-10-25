# article_076 | Self-Contrast: Better Reflection Through Inconsistent Solving Perspectives | 2024

研究类型概述：这是一篇 LLM prompting / 基准评测方法论文：提出 Self-Contrast 反思策略，并在数学推理（GSM8K、SVAMP）和创意翻译（CommonMT）上，对多个 LLM 与多种 prompting/ensemble 基线进行对比。分析单位主要是测试题/任务上的模型输出与自动评分，而非人类被试。
- **研究构念（Construct）**：元认知自我评估、不一致视角反思与自我纠错（metacognitive self-evaluation, error monitoring, and self-correction）｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：这是一篇 LLM prompting / 基准评测方法论文：提出 Self-Contrast 反思策略，并在数学推理（GSM8K、SVAMP）和创意翻译（CommonMT）上，对多个 LLM 与多种 prompting/ensemble 基线进行对比。分析单位主要是测试题/任务上的模型输出与自动评分，而非人类被试。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.6: 'We conduct experiments using the GPT-3.5-Turbo-0613 and GPT-4-0613, alongside the Llama2-Chat model with three parameter scales'; PDF p.7, Table 4 lists CoT Prompt, Self-Reflection, SC-Vote, SC-Select, SC-Reflect, Multi-Agent, Hint-Prompt, Math-Prompt, Self-Contrast. | 策略/方法被明确命名且有多个水平，操纵流程与 prompt 在 PDF p.16-20 有描述；但未报告题目/调用如何分配到各条件的随机化或操纵检验，因此只达 0.5。 |
| A2 | 因变量 | 0.5 | PDF p.6: 'For mathematical reasoning, we evaluate the precision of the final answer'; 'we employ BLEURT score as automatic metrics'; PDF p.7 Tables 4-5 report accuracy/BLEURT means. | 因变量指标与计分方式明确，但未报告评分信度/效度、置信区间或端点分布/预处理说明。 |
| A3 | 控制变量 | 0.5 | PDF p.6: 'To make a fair comparison, we uniformly set the temperature to 0.2 for all experiments'; 'evaluate them 10 times using different prompts and average their results under zero-shot scenes.' | 报告了温度统一、零样本和部分重复平均等控制，但未系统列出控制变量清单及逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF p.8: 'For some smaller-scale LLMs, their instruction-following capability is weaker, hindering their potential to conduct precise comparisons and reflection'; PDF p.7-8 讨论 Llama2-7B 低于 ensemble 基线。 | 识别了模型指令遵循能力等潜在混杂解释，但未系统控制或量化残余混淆对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 论文没有提出或检验理论调节变量；模型/任务差异是泛化比较维度，不是调节假设分析。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解，研究问题不属于中介模型。 |
| A7 | 操作性定义 | 1 | PDF p.4-6 详述 Self-Contrast 三阶段：Create Diverse Perspectives、Contrast Inter-Perspective Discrepancies、Eliminate Discrepancies；PDF p.18-20 给出 self-curated、contrast、reflection 的完整 prompt 与 JSON 输入格式。 | 关键流程和因变量计分给出了可重复执行的操作化描述，足以据附录提示复现。 |
| A8 | 水平数与类型 | 0.5 | PDF p.6: 模型包括 GPT-3.5-Turbo-0613、GPT-4-0613、Llama2-Chat 7B/13B/70B；PDF p.7 Tables 4-5 列出多种策略水平；PDF p.17: 'at least two different prompts and a maximum of nine prompts'，k=3。 | 水平数与标签基本明确，但未统一说明各因素的水平类型、间距/全距或连续变量中心化处理。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p.7 Tables 4-5 在数学推理、创意翻译和多模型上报告效果；PDF p.8-9 进一步分析 invalid/toxic reflection 与不同错误类型对比。 | 采用多个任务与多模型提供一定会聚证据，但未正式报告各操作/指标间会聚统计，也未在局限中充分讨论单一操作化边界。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈式同源测量；自变量为 prompting 策略，因变量为客观答案正确率或 BLEURT 自动分数，传统共同方法偏差问题不适用。 |
| B1 | 被试间设计 | NA | — | 研究没有人类或 LLM '被试'被独立分配到互斥条件；各方法在同一测试集上评估，不构成被试间设计。 |
| B2 | 被试内设计 | NA | — | 各 prompting 条件在独立 API 调用中运行，未建立需要顺序平衡的被试内重复测量设计；无跨条件顺序效应设计。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内人类被试因素混合设计；模型和策略是评估比较维度，不是混合实验因素。 |
| B4 | 因子设计 | NA | — | 论文是基准/方法比较，不是以 ANOVA/因子实验报告主效应与交互的因子设计，故该组件不适用。 |
| B5 | 主效应 | NA | — | 无传统因子设计主效应分析；表 4/5 为各模型-策略组合的描述性性能比较。 |
| B6 | 交互作用 | NA | — | 未进行因子交互检验；研究目标是 prompting 方法性能比较，而非实验交互效应。 |
| B7 | 区组设计 | NA | — | 没有区组变量、分层或区内随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡条件的被试内设计。 |
| B9 | 准实验设计 | NA | — | 不存在准实验分组或非随机处理分配的情境。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有需要论证可逆性与迁移对称性的被试内处理设计。 |
| C1 | 随机化 | NA | — | 基准评估将同一测试集用于各方法，无人类被试或分析单位被随机分配到处理条件的问题。 |
| C2 | 平衡 | NA | — | 没有跨条件顺序平衡方案可报告。 |
| C3 | 恒定 | 0.5 | PDF p.6: 'uniformly set the temperature to 0.2 for all experiments'; 模型版本固定为 GPT-3.5-Turbo-0613、GPT-4-0613 与 Llama2-Chat 三种规模。 | 报告了温度和模型版本等恒定设置，但未系统列出全部恒定变量及其外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配、配对或倾向得分匹配程序。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为协变量或区组纳入统计模型。 |
| C6 | 盲法 | 0 | PDF p.15: 'The entire human evaluation process is conducted by two senior PhD students. One is responsible for categorization, while the other verifies the categorization again.' 未报告盲法。 | 存在人工反馈分类评分者，但未说明评分者是否对条件/初始答案状态盲，也未报告盲法成功检验或评分者一致性。 |
| C7 | 平衡的层级 | NA | — | 没有使用完全平衡、拉丁方或 ABBA 顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 每个条件为独立 prompting/API 调用，不存在跨试次练习效应或练习块安排。 |
| D2 | 疲劳效应 | NA | — | 无人类长 session 疲劳问题；LLM 调用不涉及休息间隔或时间位置控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件之间为独立调用，没有跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件迁移对称性需要检验；条件间不共享对话上下文。 |
| D5 | 范围效应 | NA | — | 主要因变量为客观准确率和 BLEURT 自动指标，不涉及主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 研究没有多选选项或序列刺激位置随机化问题；候选比较的位置风险在 J1 讨论。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 研究不涉及人类被试掩饰情节或事后推断研究假设。 |
| E5 | 实验者效应 | NA | — | 主要数据采集完全自动化；人工反馈分类的评分者盲法/标准化问题已在 C6 记录。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.7 Tables 4-5 报告准确率均值，如 GPT-4 在 GSM8K 为 93.9⇒95.1，Self-Contrast 为 95.4；未报告 SD、偏度或端点频率。 | 报告了均值，可用于初步判断高位表现，但未给分布/端点频率，也未讨论 GSM8K/SVAMP 高分端的天花板问题。 |
| E7 | 共同方法偏差 | NA | — | 自变量为 prompting 策略，因变量为客观答案正确率或 BLEURT，不是同源自陈式多构念测量。 |
| F1 | 统计结论效度 | 0.5 | PDF p.7 Tables 4-5 报告各条件准确率和相对 CoT 的百分点变化；PDF p.3 Table 1 报告 one-tailed t-test 的 P 值。 | 有性能差值和部分显著性检验，但没有置信区间、样本量/功效依据和多重比较校正。 |
| F2 | 内部效度 | NA | — | 这是纯基准方法比较，无人类被试随机分配、分配隐藏、基线表或损耗流程。 |
| F3 | 构念效度 | 0.5 | PDF p.6 明确 accuracy 与 BLEURT 指标；PDF p.15 人工反馈分类由两名博士生复核；但无正式信度系数、操纵检验或效度证据。 | 关键测量有操作化与部分人工复核，但缺正式信效度与 manipulation check。 |
| F4 | 外部效度 | 0.5 | PDF p.6 报告模型来源与基准：GPT-3.5/4 和 Llama2-Chat 7B/13B/70B，GSM8K、SVAMP、CommonMT；PDF p.7-9 讨论跨模型/任务效果与局限。 | 报告了模型与任务样本来源，也做了跨模型/任务比较；但未报告基准题目抽样/排除标准，推广边界讨论有限。 |
| G1 | 分析单位 | 0.5 | PDF p.6: 实验在多个基线上运行各模型；PDF p.7 结果按模型×任务×策略汇总平均准确率；未说明题目/重复调用/模型的嵌套结构。 | 分析层级为聚合后的任务-模型-策略性能，但未明确处理分配层级与题目、重复调用等嵌套结构。 |
| G2 | 随机效应 | NA | — | 论文没有混合模型或随机效应分析；模型族被作为固定比较对象，而非要推广到任意模型总体的抽样因子。 |
| G3 | 材料作为随机效应 | NA | — | GSM8K/SVAMP/CommonMT 题目是固定测试材料，不是作为自变量载体的有限材料抽样；论文不做项目随机效应推广。 |
| G4 | 统计功效 | 0 | PDF p.6-7 未报告事前功效分析、目标效应量或样本量推导；结果报告准确率变化和部分 P 值。 | 没有样本量/重复次数设计依据，也未报告置信区间；不符合功效分析要求。 |
| G5 | 研究者自由度 | 0.5 | PDF p.7 Tables 4-5 报告全部主要策略和模型结果；PDF p.8 Table 6 与 p.16 Table A1 报告消融实验；但未给数据剔除规则或验证性/探索性区分。 | 报告了多数因变量与条件，但缺排除规则、样本量决定方式和明确的探索/验证分析标注。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册平台、注册编号或数据收集前分析计划。 | 无预注册；也不存在说明预注册与实际分析偏离的部分。 |
| J1 | 位置偏差 | 0 | PDF p.5-6 描述将多个候选解同时输入 LLM 进行成对差异对比与 checklist 生成，但未报告候选顺序反平衡、A/B 交换或位置×正确率分析。 | Self-Contrast 的确涉及多候选解对比，存在候选位置偏差风险，但论文未做任何位置平衡或翻转率报告。 |
| J2 | 冗长偏差 | NA | — | 最终评估使用答案准确率与 BLEURT，不使用 LLM judge 对开放式生成长度作质量评分，长度偏差风险不构成本研究评估环节。 |
| J3 | 谄媚 | NA | — | 实验没有用户先验立场、反馈纠错或多轮立场框架操纵，不涉及谄媚测量。 |
| J4 | 自我偏好 | NA | — | 不用 LLM-as-judge 作为最终评分器；模型输出由数学答案精确匹配或 BLEURT 自动评分。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主要实验为零样本 prompting；未使用 few-shot in-context examples，故示例选择/排列偏差不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.18-20 附录 D 公布 self-curated、contrast、reflection 的完整 prompt；PDF p.6 提到 baseline 使用 10 个 reflection prompts 取平均；未报告 prompt 版本消融或 dev/test 划分。 | 完整模板已提供，但无版本号/迭代日期、敏感性消融与 dev/test 分离说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为单题提示与少量候选解，不涉及长文档/RAG 或长上下文位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.6: 'we uniformly set the temperature to 0.2 for all experiments'；部分 baseline 有 10 次重复平均；未报告 top-p/top-k、seed、重复采样 CI。 | 报告了温度且部分重复运行，但缺完整采样超参、随机种子与均值置信区间。 |
| J9 | 重复与文本退化 | 0.5 | PDF p.6 报告 temperature=0.2；未报告 beam/greedy、repetition penalty、n-gram 重复率或退化率。 | 有基本解码温度信息，但缺重复/文本退化质量控制，也未说明所有条件的解码策略严格一致。 |
| J10 | 分词效应 | 0 | PDF p.6 使用 CommonMT 进行中文到英文创意翻译；未报告 tokenizer 名称/版本、token/词数比或 token 数控制。 | 跨语言/跨脚本评估存在分词效应风险，但论文完全没有记录分词器与控制 token 长度。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.6 使用公开 GSM8K、SVAMP、CommonMT；模型为 GPT-3.5-Turbo-0613、GPT-4-0613、Llama2-Chat；全文未做训练截止日期对照或污染检测。 | 使用公开基准但未报告污染检测、重叠率或 held-out 私有测试集。 |
| J12 | 基准饱和 | 0.5 | PDF p.7 Table 4 中 GPT-4 在 GSM8K 为 93.9→95.1、Self-Contrast 95.4，SVAMP 为 93.0→94.0；未讨论基准饱和或用连续指标/CI 比较。 | 报告了接近上限的高分水位，但未识别饱和问题，也未改用校准/连续指标或 CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，也没有按否定/数量/格式/风格约束测量指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p.6: 'we use a JSON format for the revision prompt'；PDF p.19 要求 'Please output all revised solutions in JSON format'；未报告格式合法率与重试策略。 | 明确要求 JSON 结构化输出，但未把格式失败与内容错误分开统计，也未报告格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱、拒绝率或对抗攻击评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.1-2 将 LLM 的 self-evaluation 描述为 overconfidence/inconsistency 与 reflection 瓶颈；PDF p.21 提到 'Drawing on cognitive science, human reasoning...'；但无人类同范式对照。 | 使用了人类心理学式构念词并作一定类比，但未系统论证 LLM 构念与人类同名构念的异同及可迁移性。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的能力曲线，也不宣称涌现能力。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以 benchmark/奖励模型/LLM-judge 为优化目标进行训练或 best-of-N 过优化研究。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.6 给出 GPT-3.5-Turbo-0613、GPT-4-0613 和 Llama2-Chat 规模；PDF p.6 说明 baseline 评估 10 次；PDF p.7 报告单点分数，无 CI/配对检验。 | 模型 snapshot 有一定标识且部分重复，但未系统报告每项结果 N、95% CI、配对检验或推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验是单轮 prompting 与评估，不涉及对话历史累积或多轮一致性衰减。 |

## 编码小结
论文对 Self-Contrast 的三阶段流程、提示模板和评估指标报告较充分，并跨多个模型与任务展示了较一致的性能改进；但统计推断、随机性/种子、基准污染与饱和、位置偏差、人工评分盲法等关键偏差控制较薄弱，部分人类实验设计组件不适用于该纯 LLM 基准研究。
