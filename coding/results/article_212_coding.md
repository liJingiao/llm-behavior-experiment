# article_212 | Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs | 2024

研究类型概述：纯 LLM 行为/基准评测研究（LLM-as-participant），无人类被试。分析单位为数据集题目/模型输出经正则抽取后聚合的准确率；主要操纵 persona 与 persona instruction，并比较模型版本、数据集和去偏 prompt；因变量为 reasoning accuracy 与 abstention/error 分析。
- **研究构念（Construct）**：persona诱发的隐性社会偏见、刻板预设与显性公平表态的分离｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：给现成LLM分配种族、性别、宗教、残障和政治身份persona，让其完成24个知识与推理任务，并与Human/Average Human基线比较。（操纵persona身份、persona措辞、任务领域、模型和去偏提示，并与无特定身份的人类persona基线比较。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3 Table 1 给出 3 种 persona instructions；p.4 Table 2 列出 19 个 personas；p.3 说明 zero-shot；p.14 App. B.1 报告 persona instruction 有效性测试。 | persona 赋值这一自变量被明确命名，水平和取值充分；但每个分析单位如何分配到条件（交叉/重复/随机化）未完整说明，操纵检验主要是 instruction 级有效性测试，不是每个 persona 的正式操纵检验，因此记 0.5。 |
| A2 | 因变量 | 0.5 | p.4 报告 'max token length of 1024, temperature 0, and a top-p value of 1'，并 'report numbers averaged across 3 runs'；p.15 说明 MMLU/Sports 用正则抽取答案、MBPP 用单元测试通过率；p.4 用 Wilson CI。 | 因变量指标与计分方式明确（准确率/通过率），但未报告测量信度、效度证据，也未系统说明连续指标预处理或端点效应处理，因此为 0.5。 |
| A3 | 控制变量 | 0.5 | p.4 固定 temperature/top-p/max token；p.3 使用 zero-shot 与统一任务指令；p.13 使用官方 test partitions；p.4 对三次运行取平均。 | 报告了若干实际控制变量及其水平，但不是系统控制变量清单，且未逐项说明控制手段与外部效度影响，因此为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.8 讨论 'the choice of instruction can significantly impact the level of observed bias'；p.18 Llama-2 使用 AWQ 量化；p.10 局限性讨论 personas/datasets 非穷尽。 | 识别了 instruction 选择、量化模型、数据集/ persona 覆盖等潜在混淆，并以 3 个 instruction 平均及 App. H 单 instruction 结果作部分敏感性说明；但缺正式残余混淆量化，因此为 0.5。 |
| A5 | 调节变量 | NA | — | 论文没有提出正式调节假设，也没有报告乘积项交互检验或简单斜率分析；模型/群体/数据集差异主要是描述性比较，按规则记 NA。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或因果链中介假设，记 NA。 |
| A7 | 操作性定义 | 1 | p.3 Table 1 给出 person instruction 完整模板；p.4 Table 2 列出全部 personas；p.15 给出 MMLU/Sports/MBPP 用户 prompt 与正则抽取规则、MBPP 单元测试标准。 | 关键自变量操纵与因变量测量/计分均有可复现的操作化描述，故记 1。 |
| A8 | 水平数与类型 | 0.5 | p.4 Table 2 列出 19 个 persona 标签与 5 个群体；p.3 Table 1 给出 3 个 instruction 水平；p.18 列出模型版本。 | 水平数与各水平标签明确，但未明确标注水平类型（名义/等级/连续）、间距、全距；这些多为名义分类变量但仍缺显式说明，故 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.4 Table 2、p.13 Table 5 显示 19 personas 与 24 datasets；p.7 用 shared non-abstained questions 复分析；p.10 局限性承认 personas/datasets 非穷尽。 | 使用多个数据集、多个 instruction 和多个模型提高操作覆盖，并讨论部分推广限制；但核心偏见图念仍主要用 accuracy drop 单一指标，未正式报告多操作会聚证据，故 0.5。 |
| A10 | 单一方法的风险 | NA | — | 自变量为 prompt 操纵，因变量为客观答案正确率/代码测试通过率，不是同源自陈量表；共同方法偏差框架不适用，记 NA。 |
| B1 | 被试间设计 | NA | — | 没有人类被试间分配；所有 persona 条件作用于同一批数据集题目/模型调用，非独立被试组设计，记 NA。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量与条件顺序平衡；LLM 调用为独立的 zero-shot API 请求，不构成需要顺序平衡的会话内重复测量，记 NA。 |
| B3 | 混合设计 | NA | — | 不存在人类组间/组内混合设计，也未使用混合 ANOVA 误差项，记 NA。 |
| B4 | 因子设计 | NA | — | 虽有 persona、dataset、model、instruction 的交叉评测结构，但未作为正式因子设计报告设计矩阵、单元样本量及 ANOVA 交互项；按规则记 NA。 |
| B5 | 主效应 | NA | — | 没有正式因子设计中的主效应检验（F、df、p、效应量），记 NA。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验、简单主效应或交互图误差棒，记 NA。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计，记 NA。 |
| B8 | 拉丁方 | NA | — | 没有被试内拉丁方顺序设计，记 NA。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计；模型版本比较是固定条件基准比较，未报告选择偏差与准实验因果推断框架，记 NA。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理可逆性/迁移对称性问题；API 条件独立，记 NA。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥条件；对大数据集随机抽 250 题属于题目抽样，不是条件分配随机化，记 NA。 |
| C2 | 平衡 | NA | — | 没有条件顺序需要平衡的被试内设计，记 NA。 |
| C3 | 恒定 | 0.5 | p.4 固定 'temperature 0'、'top-p value of 1'、'max token length of 1024'；p.3 zero-shot；p.18 对 Llama-2 使用 AWQ 量化与 vLLM。 | 列出了若干恒定设置与水平，但未系统讨论这些恒定设置对外部效度的限制，故 0.5。 |
| C4 | 匹配 | NA | — | 没有匹配设计，记 NA。 |
| C5 | 纳入为变量 | 0.5 | p.4 报告最终准确率为 3 个 persona instructions 与 3 次运行的平均；p.8 Table 4 和 p.26 App. H 报告单 instruction 与去偏条件结果。 | instruction 变异被设计性平均并做了单 instruction 敏感性展示，但没有作为协变量/区组纳入正式模型，也未检验 ANCOVA 斜率齐性，故 0.5。 |
| C6 | 盲法 | NA | — | 无人类被试或人工评分者，答案由正则/单元测试自动判定，不需要盲法，记 NA。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级，记 NA。 |
| D1 | 练习效应 | NA | — | 每次调用为独立 zero-shot 请求，无上下文内练习或跨试次学习，记 NA。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳效应；任务以 API 调用为单位，记 NA。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件间无跨会话上下文残留或清洗期问题，记 NA。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移与不对称迁移问题，记 NA。 |
| D5 | 范围效应 | NA | — | 因变量为客观正确率/通过率，不是主观量表绝对判断，不存在范围效应，记 NA。 |
| E1 | 位置 / 顺序偏差 | 0 | p.15 MMLU prompt 仅说明 'The answer can only be an option like (A), (B), (C), (D)'；未报告选项位置随机化、反平衡或位置偏差分析。 | 存在多项选择选项位置偏差风险，但全文未说明正确答案位置分布随机化或位置×正确率分析，按规则记 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，记 NA。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也没有跨群体反应风格比较，记 NA。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征；LLM 不涉及人类被试推断实验假设，记 NA。 |
| E5 | 实验者效应 | NA | — | 数据采集与评分完全自动化，无人类主试/评分者，记 NA。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.4 Fig. 2 报告各 persona 的 micro-averaged accuracy；p.7 Fig. 6 报告 error rate 与 abstention 占比；但未报告 SD、偏度、端点频率或 pilot 难度校准。 | 报告了均值型描述统计和错误率，可部分评估端点风险；但缺分布形态、SD、端点频率和 pilot 校准，故 0.5。 |
| E7 | 共同方法偏差 | NA | — | 自变量为 prompt，因变量为客观 accuracy；非自陈式多构念同源测量，CMB 不适用，记 NA。 |
| F1 | 统计结论效度 | 0.5 | p.4 报告 3 runs 平均与 Wilson CI；p.4–p.8 报告大量 relative % drop；p.13 说明数据集样本量。 | 报告了不确定性区间和效应量式相对下降，但没有事前功效分析或明确多重比较校正，也未系统报告所有统计假设，故 0.5。 |
| F2 | 内部效度 | 0.5 | p.4 设置 'Human' 与 'No Persona' 基线，并称 'No Persona' 与 'Human' 无统计显著差异；所有 persona 使用同一数据集；未报告随机分配、分配隐藏或被试流向。 | 有基线比较与同题控制，但无随机分配/分配隐藏，内部效度控制主要是设计层面的固定比较，故 0.5。 |
| F3 | 构念效度 | 0.5 | p.14 App. B.1 报告 persona instruction 有效性测试与筛选；p.15 说明答案抽取规则；p.10 局限性承认 personas/datasets 非穷尽。 | 有 instruction 操纵有效性检验且 accuracy 为客观指标，但无心理测量信度/效度证据，也未系统论证操作化与 bias 构念的对应，故 0.5。 |
| F4 | 外部效度 | 1 | p.3–p.4 报告 24 datasets、19 personas、4 LLMs 及具体版本；p.13 使用官方 test partitions 并说明大数据集随机抽 250 题；p.10 明确 personas/datasets 非穷尽、仅英文；p.18–p.20 报告跨模型结果。 | 样本来源、数据集抽样、模型版本和推广边界均有报告，并给出跨模型/跨情境比较，故记 1。 |
| G1 | 分析单位 | 0.5 | p.4 说明结果 'micro-averaged on all 24 datasets'；p.4 用 Wilson CI 对聚合准确率作显著性判断；未报告多层模型或题目嵌套处理。 | 说明了聚合分析层级，但未显式建模题目嵌套于数据集、数据集嵌套于领域的聚集结构，属于聚合处理，故 0.5。 |
| G2 | 随机效应 | 0 | p.4 与 p.15 显示分析基于题目级抽取后按 persona/dataset 聚合准确率，并使用 Wilson CI；全文未报告随机效应或混合模型结构。 | 研究存在题目/数据集嵌套和模型版本多水平结构，但分析未使用任何随机效应，且将模型/数据集作为固定条件处理，故记 0。 |
| G3 | 材料作为随机效应 | 0 | p.13 Table 5 列出 24 个数据集及题量；p.4 使用 micro-averaged accuracy；未报告 item random effect 或准 F 比。 | 有限题目/数据集被当作固定评估材料聚合，未把项目/材料作为随机因子纳入分析，限制了对更广题目总体的推广，故 0。 |
| G4 | 统计功效 | 0.5 | p.4 对 3 次运行取平均；p.13 给出各数据集样本量；p.4 使用 Wilson CI；但无设计阶段功效分析或预期效应量来源。 | 有重复运行和置信区间，但缺事前功效分析/样本量推导，故 0.5。 |
| G5 | 研究者自由度 | 0.5 | p.3–p.4 报告 24 datasets、19 personas、4 LLMs 与 3 个 instructions；p.13 说明大数据集随机抽 250 题；未明确报告试次/数据集剔除规则、是否中途停止及验证性/探索性区分。 | 主要因变量与条件报告较全，部分数据处理规则可见；但排除规则、停止规则与探索性/验证性区分不完整，故 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未报告预注册平台、注册编号、样本量/停止规则或分析计划。 | 无预注册，且未明确区分验证性与探索性分析，按此前口径记 0，而非 NR。 |
| J1 | 位置偏差 | 0 | p.15 MMLU prompt 固定要求 '(A), (B), (C), (D)' 选项；未报告选项位置随机化、A/B 交换或位置×正确率分析。 | LLM 做多项选择时存在位置偏差风险，但未做任何位置反平衡或随机化，故 0。 |
| J2 | 冗长偏差 | NA | — | 不以 LLM 裁判评估开放生成质量，也不涉及长度—质量比较；记 NA。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错式对话操纵，谄媚风险不适用，记 NA。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 或同源自评，记 NA。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.3 明确 'we use a zero-shot setting'；无 few-shot in-context examples，记 NA。 | 零样本设置，J5 不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.3 Table 1 给出 3 个主 persona instructions；p.14 Table 8 列出 10 个候选 instruction；p.22–p.23 Table 14 列出去偏 instructions；p.26 App. H 报告单 instruction 结果。 | prompt 模板和多个变体公开，并做了 instruction 变体敏感性展示；但无 prompt 版本号/迭代日期、无 dev/test 划分说明，故 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验上下文很短，无长文档/RAG 或关键信息中间位置操纵，记 NA。 |
| J8 | 温度与采样随机性 | 0.5 | p.4 报告 'temperature 0'、'top-p value of 1'、'max token length of 1024'，并对 3 次运行取平均；报告精确模型版本如 gpt-3.5-turbo-0613；未报告 seed/top-k/repetition penalty。 | 报告了主要采样参数、重复运行数与模型 snapshot，但缺 seed/top-k 等细节，故 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.4 说明 'temperature 0, and a top-p value of 1 (equivalent to greedy decoding)'；未报告 repetition penalty、n-gram 重复率或退化率 QC。 | 报告了解码策略，但未把重复/退化作为受控 QC 指标，故 0.5。 |
| J10 | 分词效应 | NA | p.10 明确 'All of our datasets and prompts are also in the English language'；无跨语言/跨脚本比较，记 NA。 | 单语言研究，J10 不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3 使用 MMLU、Big-Bench-Hard、MBPP 等公开基准；p.18 给出模型版本；全文未对照训练截止日期或做污染检测。 | 使用公开基准但未报告污染检测/训练截止日期对照，存在记忆复现风险，故 0。 |
| J12 | 基准饱和 | NA | p.4 Fig. 2 中准确率约 0.3–0.7，未接近天花板；论文也未在饱和基准上宣称微小提升。 | 本研究的基准分数远未饱和，J12 风险不实际存在，记 NA。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；App. B.1 的 persona 有效性问题是操纵检验，不是按约束类型测量指令遵循，记 NA。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.15 要求最终句输出答案并用正则抽取；MBPP 抽取代码并运行测试；未报告格式合法率、重试策略或格式失败与内容错误的拆分。 | 报告了格式约束与抽取规则，但未报告格式合法率/重试，也未拆分格式失败与内容错误，故 0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求攻击评估，记 NA。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 该研究是 LLM 行为/偏见基准评测，不主张测量人类心理学同名构念，也未做人类被试对照；按研究类型，J16 不适用，记 NA。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的能力曲线或涌现宣称，记 NA。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以 benchmark/奖励模型/LLM-judge 为优化目标进行训练或 overoptimization 研究，记 NA。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4 报告 3 次运行平均与 Wilson CI，并给出精确模型版本（如 gpt-3.5-turbo-0613、gpt-4-turbo-1106）；p.3 称发布代码与 1.5M outputs；未报告配对检验或逐题结果。 | 有重复次数、CI、snapshot 和输出发布，但模型比较缺配对检验，snapshot 对 Llama-2 也仅给 HuggingFace 路径，故 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 zero-shot 问答，无多轮对话历史累积，记 NA。 |

## 编码小结
论文对 persona 赋值、数据集、模型版本、提示模板和输出抽取规则的报告较透明，核心发现是 persona 诱发准确率下降及显性公平表态和隐性偏见分离。但研究不是人类被试实验，也不是正式多因素方差分析；推断统计依赖聚合准确率和 Wilson CI，缺少心理测量信效度、随机效应/项目推广、预注册与功效分析等。多个适用于人类实验的分配/顺序组件在本研究中不适用。
