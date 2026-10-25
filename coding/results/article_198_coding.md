# article_198 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | 2023

研究类型概述：这是一项 LLM-as-a-judge 的系统性基准/评估研究，而非传统人类被试实验。分析单位主要是每次 judge vote/评分（问题-回答对、模型对或对话轮次）；研究比较 GPT-4、GPT-3.5、Claude 等 LLM 裁判与人类专家/众包偏好的一致性，并考察位置偏差、冗长偏差、自我增强偏差和数学/推理判分能力。
- **研究构念（Construct）**：评价判断中的位置偏差、冗长偏好、自我增强和人类偏好一致性｜CA 构念锚定：语言理解（language comprehension, `trm_4a3fd79d0a775`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：让GPT-4等现成模型对成对答案或单个答案进行评价，并在交换位置、改变冗长度和标示模型身份后比较评价结果及其与人类偏好的关系。（操纵答案位置、回答长度、生成模型身份、成对或单答案评价方式，并与专家和众包人类偏好比较。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | P4 列出 pairwise、single-answer、reference-guided 三类 judge；P5–P6 操纵 judge 模型、prompt（default/rename）、答案位置（swap）与冗长攻击。 | 自变量被明确命名且有多水平，但分配程序、统一操纵检验与采样设置报告不完整，故为部分满足。 |
| A2 | 因变量 | 0.5 | P7 定义 agreement 为随机抽取的不同 judge 在同一问题上的同意概率，并报告 #votes；P8 Table 5/6 报告 agreement 与 win rate。 | 因变量指标和计分方式明确，但缺少正式信效度证据、置信区间及连续指标预处理说明。 |
| A3 | 控制变量 | 0.5 | P5 使用 GPT-3.5 以 temperature 0.7 生成相似答案；P14 使用 default prompt；P18 提到 gpt-4-0314。 | 报告了部分恒定控制（prompt、模型版本、生成温度），但未系统列出控制变量清单与控制手段。 |
| A4 | 混淆变量 | 1 | P4–P6 识别 position、verbosity、self-enhancement、limited reasoning 等潜在混淆，并报告 swap、reference-guided、CoT、few-shot 等控制及残余局限。 | 既识别混淆，又说明控制方式和残余威胁；自我增强部分明确承认数据有限、难以定论。 |
| A5 | 调节变量 | NA | — | 全文没有正式提出调节变量假设，也未做交互项检验或简单斜率分析；按类别/模型对拆分属于描述性偏差分析，不作为调节模型编码。 |
| A6 | 中介变量 | NA | — | 全文没有中介变量假设，也没有直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | P5 将 position bias 操作为交换顺序后的 consistency 与 favor-first/second；P5 将 verbosity bias 操作为 repetitive-list attack 成功率；P26 给出 agreement 公式。 | 关键构念均有可观测、可重复的操作程序，且提示模板在附录 P14–P17 给出。 |
| A8 | 水平数与类型 | 0.5 | P4 列出三种 judge 类型；P5 报告 default/rename；P25 报告 score/short；P7 列出六个被评模型。 | 水平数与标签多可识别，但缺少统一水平类型、间距/全距及连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 1 | P5–P6 用 consistency、bias 百分比和 failure rate 多指标考察偏差；P8 在 MT-bench 与 Chatbot Arena 两个人数据集、专家与众包人群上验证 agreement。 | 关键构念采用多种操作化并报告会聚性证据；同时讨论 helpfulness 单维化等限制。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是自陈式多构念测量，主要比较 LLM 裁判输出与人类偏好，无共同方法偏差问卷同源问题。 |
| B1 | 被试间设计 | NA | — | 没有将被试分配到互斥实验组的被试间设计；人类评分者与 LLM 裁判均非按条件独立分组。 |
| B2 | 被试内设计 | 0.5 | P6 明确对 judge 调用两次并交换答案顺序；P5 Table 2 报告 swap 后 consistency 与位置偏好。 | 同一问题/回答对在多个 judge 与两种位置下重复，属重复测量；但未报告被试/项目随机效应与完整顺序分配模型。 |
| B3 | 混合设计 | NA | — | 没有明确的组间×组内混合设计标注，也未使用混合模型并分别报告两类误差项。 |
| B4 | 因子设计 | NA | — | 虽有多 judge×prompt 等条件表，但论文未按正式因子实验报告完整设计矩阵、每格样本量与 ANOVA 交互检验；按基准比较而非因子设计编码。 |
| B5 | 主效应 | NA | — | 没有以 ANOVA 主效应形式报告每个因素的主效应统计量，也没有在交互显著时限制主效应解释。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验、简单主效应和带误差棒图示，故不按因子交互设计编码。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层分配，也不涉及区组变量与区内随机化。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方设计；顺序控制采用 swap 而非拉丁方。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计，没有非随机分组后的选择偏差与因果推断限定。 |
| B10 | 被试内设计的适用条件 | NA | — | 不是人类被试内处理设计；位置 swap 不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | 0.5 | P7 随机抽取 3K arena votes；P23 说明 MT-bench 向评分者呈现两个 random anonymous assistants；P4 描述 anonymous battles。 | 有随机抽样/随机匿名呈现的表述，但无随机数工具、分配隐藏、基线均衡或 ITT 说明。 |
| C2 | 平衡 | 0.5 | P6 采用 conservative swapping：交换两个答案顺序后仅在两种顺序一致时判胜；P5 Table 2 报告 consistency。 | 报告了位置顺序平衡方案，但未报告各顺序计数（虽可由全交换推知）及迁移对称性前提。 |
| C3 | 恒定 | 0.5 | P14–P17 固定 default prompt；P5 答案生成使用 temperature 0.7；P18 说明 gpt-4-0314。 | 列出了部分恒定因素与水平，但未系统报告全部环境/模型/采样恒定项及其外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配变量或匹配后分配程序；研究不采用配对/PSM 等匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型，也未做 ANCOVA。 |
| C6 | 盲法 | 0.5 | P4 说明 Chatbot Arena 为 anonymous battles；P23 说 MT-bench 呈现两个 random anonymous assistants。 | 对模型身份有盲化/匿名化安排，但未明确盲法类型、施盲对象、实施方式及盲法成功检验。 |
| C7 | 平衡的层级 | 0.5 | P6 报告交换两次顺序并比较一致性；P5 Table 2 报告 biased toward first/second。 | 使用完全 swap 的顺序控制，但未以 ABBA/拉丁方/完全平衡等层级命名，也未报告构造方法与顺序效应形状假设。 |
| D1 | 练习效应 | NA | — | 没有人类被试练习块、试次截除或试次位置协变量设计；LLM 调用亦非同一上下文学习序列。 |
| D2 | 疲劳效应 | NA | — | 没有 session 时长、休息间隔或条件时间分散设计；评分者任务时长未作为分析变量。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM judge 每次独立调用且位置 swap 不是跨条件处理残留；没有清洗期或迁移建模需求。 |
| D4 | 不对称迁移 | NA | — | 不涉及人类被试内处理的跨条件不对称迁移；位置偏差由 swap 检验而非迁移对称性检验处理。 |
| D5 | 范围效应 | NA | — | 没有人类被试内绝对量值/李克特量表校准问题；1–10 分为 LLM 判分 rubric，非被试主观量表。 |
| E1 | 位置 / 顺序偏差 | 1 | P6 明确对成对答案交换位置；P5 Table 2 报告 swap 后 consistency、biased toward first/second，等于完整两顺序反平衡。 | 候选顺序做了完整交换并报告翻转/一致性结果；对两项位置而言即为完全反平衡。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，也没有反向计分题设计。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有人类等级量表分布或跨群体反应风格比较；LLM 1–10 判分不属于被试反应风格量表。 |
| E4 | 需求特征 | 0.5 | P4/P23 使用匿名 assistants；P7 当人类与 GPT-4 不一致时展示 GPT-4 判断并询问是否合理，报告 75% 认为合理、34% 愿意改变选择。 | 有部分盲化与事后询问式检查，但无 cover story、正式 post-experimental inquiry 推断比例或 debriefing 流程。 |
| E5 | 实验者效应 | 0.5 | P23–P24 说明评分者为 graduate students、多校、付费；界面使用匿名 assistants。 | 报告了部分评分者来源与匿名安排，但未报告实验者/评分者盲法层级、培训标准化与脚本化程度。 |
| E6 | 天花板 / 地板效应 | 0.5 | P9 Table 8 报告 GPT-4 MT-Bench 8.99/10、MMLU 86.4；P8 Fig. 3 报告 win-rate 曲线。 | 报告了均值型得分但缺少 SD、偏度、端点频率及 pilot 难度校准；GPT-4 接近 MT-Bench 上限却未讨论天花板风险。 |
| E7 | 共同方法偏差 | NA | — | IV 与 DV 不是同源自评；比较对象为 LLM 裁判与人类偏好/投票，不涉及传统 CMB 自陈同源测量。 |
| F1 | 统计结论效度 | 0.5 | P8 Table 5/6 报告 agreement 百分比与 #votes；P8 Fig. 2/3 报告 win-rate 与 agreement 关系。 | 有效应量式百分比，但无置信区间、样本量功效依据、正式多重性校正及统计假设检验说明。 |
| F2 | 内部效度 | 0.5 | P7 说明随机抽取 3K votes、58 experts；P23 说明随机匿名 assistants。 | 报告了抽样/匿名呈现与部分威胁讨论，但无 allocation concealment、基线等价性检验、被试流向/损耗处理。 |
| F3 | 构念效度 | 0.5 | P8 报告人类-人类 agreement 约 81%、GPT-4-人类约 85%；P5 Table 2 以 swap consistency 作为位置偏差指标。 | 有信度/会聚式证据和多操作化，但缺正式内部一致性/效度检验与操纵检验统计报告。 |
| F4 | 外部效度 | 0.5 | P7 报告 58 expert labelers、2114 unique IPs；P24 说明评分者多为 ten universities 以上研究生。 | 报告样本来源与特征，并在两个平台比较；但对总体代表性、边界条件与跨情境复现讨论不完整。 |
| G1 | 分析单位 | 0.5 | P7 将 agreement 定义为随机抽取的不同 judge 在同一问题上的同意概率，并报告 vote 数。 | 说明了分析在 vote/judgment 层，但未说明处理分配层级与多人类评分者/多问题聚类的匹配，也未用多层模型处理。 |
| G2 | 随机效应 | 0 | P7–P8 使用 agreement/win-rate 聚合，未报告混合模型或随机截距/斜率；同一评分者与问题重复投票未建模。 | 未把评分者/问题等重复结构作为随机效应，推断可能高估独立性。 |
| G3 | 材料作为随机效应 | 0 | P3 固定 80 个 MT-bench 问题；P7 用同一组问题比较 6 个模型与多个 judge，未报告 item random effect。 | 材料/问题被当作固定基准，未做项目随机效应或准 F 分析以推广到问题总体。 |
| G4 | 统计功效 | 0 | P7 报告 3K votes 与 58 experts，但全文无事前功效分析或预期效应量推导；结果多为百分比。 | 缺少目标功效、预期效应量和样本量推导，也无 CI；不能算满足功效报告要求。 |
| G5 | 研究者自由度 | 0.5 | P23 允许评分者跳过至多 5 个不确定问题；P24 说明付费；P28 说明数据清洗。 | 报告了部分排除/数据清洗与样本量，但未系统报告所有因变量、停止规则及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未见预注册平台、注册编号或数据收集前分析计划。 | 无预注册，且研究包含较多探索性偏差分析，未区分验证性与探索性。 |
| J1 | 位置偏差 | 0.5 | P5 Table 2 报告 swap 后 consistency 与位置偏好；P6 说明交换顺序两次判定；P18 提到 gpt-4-0314。 | 位置反平衡与翻转率报告充分，但对 judge 采样温度/seed 等参数报告不全，故未给满分。 |
| J2 | 冗长偏差 | 0.5 | P5 设计 repetitive-list attack 并报告 failure rate（Table 3）；P14 prompt 明确写 Do not allow the length ... influence your evaluation。 | 有 rubric 长度控制与攻击式长度操纵，但未报告被评回答长度-得分相关系数及完整裁判采样设置。 |
| J3 | 谄媚 | NA | — | 任务不是用户立场/反馈/多轮纠错式对话；没有 pro-/anti-framing 或 answer/feedback sycophancy 操纵。 |
| J4 | 自我偏好 | 0.5 | P5 报告 self-enhancement：GPT-4 对自身 win rate 高约 10%、Claude-v1 高约 25%，并与人类基线比较；Fig. 3b。 | 明确报告裁判与被评模型同源问题并做人类基线，但未做受控匿名化自识别实验，也未量化 favor-own-generation 比例。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | P6 说明 few-shot 选用 3 个 MT-bench-like 示例（A better/B better/tie），由 GPT-4 生成判断；P26 Table 12 报告一致性提升。 | 报告了示例数量、来源与标签比例，但未做多 seed/排列反平衡，也未提供完整模板全文。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | P14–P17 给出多种 prompt 模板；P25 Table 9 比较 default/rename/score/short；P6 比较 CoT/reference-guided/few-shot。 | 有 prompt 版本化与敏感性消融，但未说明 dev/test 划分、迭代日期与完整 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不是长上下文或 RAG 信息位置实验；多轮对话上下文仅两轮，未检验中间迷失。 |
| J8 | 温度与采样随机性 | 0.5 | P5 说明生成相似答案时 GPT-3.5 temperature 0.7；P6 说明同一 judge swap 调用两次。 | 报告了部分采样参数与重复调用，但未报告 judge temperature/top-p/seed、每条件重复采样 N 与 95% CI。 |
| J9 | 重复与文本退化 | 0 | 论文未报告被评模型或裁判模型的 decoding strategy、repetition penalty、n-gram 重复率；P5 repetitive-list attack 是偏差攻击而非解码退化 QC。 | 没有把解码策略作为受控变量，也未报告重复/退化率。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言、单脚本，无跨语言/跨脚本 token 数比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | P3–P4 介绍新 MT-bench 与 Chatbot Arena，但全文未报告测试集版本与模型训练截止日期对照、污染检测或 n-gram 重叠率。 | 虽有新基准，但未做污染/数据泄漏评估，不能把分数明确等同于泛化能力。 |
| J12 | 基准饱和 | 0.5 | P9 Table 8 报告 GPT-4 MT-Bench 8.99、MMLU 86.4；P9 提到 DynaBench 处理 saturation/overfitting。 | 报告了基准分数与接近上限的水位，但未用 CI 或连续指标系统评估饱和，也未改用更难子集。 |
| J13 | 指令遵循 | 0 | P3 称 MT-bench 评估 instruction-following ability，但 P4/P7 主要依赖 LLM judge 或人类偏好判定，未给可机器判定的分约束准确率。 | 指令遵循依赖 LLM 裁判/主观偏好，无 IFEval 式可验证标准，故为 0。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | P14–P17 要求严格输出 [[A]]/[[B]]/[[C]] 或 [[rating]]；P5 Table 2 报告 Error=wrong output formats；P29 Table 15 报告 0%–78.8% error。 | 报告了格式约束与格式错误率，但未报告 grammar/JSON 约束、重试策略与后处理规则。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估；P9 明确说本文强调 helpfulness 而 largely neglects safety。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文是工程/基准评估，不把 LLM 当作心理学被试，也不主张测量人类同名心理构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随规模/训练进展的涌现能力曲线；仅有若干 LLaMA/Vicuna 变体评估。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以代理指标为优化目标进行 RL/best-of-N 等优化并用 held-out 人类评估监控 overoptimization。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | P7 报告 3K votes/58 experts/3K arena votes；P18 说明示例由 gpt-4-0314 生成；P26 附录讨论 agreement 计算。 | 报告了样本量和部分 snapshot 标识，但无置信区间、配对检验及完整原始推理日志/重复采样。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | P6 讨论 multi-turn judge；P8 Table 5 与 Fig. 3 分别报告 first turn/second turn 的 agreement 与 win rate。 | 做了两轮多轮评估并分轮报告，但未检验更长轮次一致性衰减、上下文截断与跨轮行为轨迹。 |

## 编码小结
论文核心贡献清楚，偏差操纵与多基准比较较丰富，且公开了数据与提示模板。但许多人类心理学实验设计组件并非其设计目标，只可按 LLM 评估单位有限适用；统计随机效应、采样参数、预注册/功效、污染检查和置信区间报告不完整，因此大量项目只能评为 0.5、0 或 NA。
