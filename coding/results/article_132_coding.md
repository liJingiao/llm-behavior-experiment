# article_132 | Weak-eval-Strong: Evaluating and Eliciting Lateral Thinking of LLMs with Situation Puzzles | 2024

研究类型概述：LLM 基准评测与多轮 player-judge 交互评估研究。分析单位主要是 975 个情境谜题上的模型输出/多轮对话，以及人类对 judge 判断的一致性评分；主要比较不同玩家模型、不同难度层级和提示增强条件，不是人类被试实验。
- **研究构念（Construct）**：横向思维、创造性问题解决、主动提问与信息搜寻、假设检验和情景重建｜CA 构念锚定：创造性思维（creative thinking, `trm_4a3fd79d09f42`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）；计划（planning, `trm_4a3fd79d0acc1`）
- **实验任务与范式（Task / Paradigm）**：现成LLM作为player读取不完整情境并逐轮提出yes/no问题或给出完整解释，现成WizardLM-2等作为judge依参考情境回答；975道题按Easy/Medium/Hard分级，并以固定最大轮数、重复运行和人类判断核验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.9: 'we treat the question-answer pairs generated during the benchmark as auxiliary prompts'; p.10 Table 6 compares base, data-only, and data+reasoning conditions. | 可将提示增强条件视为被操纵变量，报告了至少两个水平及其标签；但未报告分配方式、完整操纵程序或操纵检验，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.8: 'Accuracy (Acc, %), which measures the correctness ... Average Round (Rnd) ... O/A = ...'; Eq. 5 defines O/A. | 因变量指标与计分方式明确；但缺少信效度证据、连续指标预处理和不确定性报告，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.8: 'We set R = 1 and the max round is 15'; 'use WizardLM-2 (8x22B) as a judge in all these performance comparison experiments'; p.9: 'same auxiliary prompts are used across different LLMs'. | 报告了固定 judge、最大轮数和相同辅助提示等控制手段，但未系统列出全部控制变量，也未报告温度、模型版本等，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.9: 'Performance Bias. ... concerns about bias when a model like WizardLM-2 (8x22B) evaluates its own performance are mitigated through several key design elements.' | 识别了 judge 自偏好这一潜在混淆并作辩护，但未报告残余混淆、敏感性分析或系统控制，故为 0.5。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量理论模型，也没有调节效应或交互检验；难度层级只是描述性分层，不作为调节变量检验。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或中介效应分析，故不适用。 |
| A7 | 操作性定义 | 0.5 | p.3: task definition specifies player asks yes-or-no questions and judge answers yes/no/irrelevant; p.8 defines Acc/Rnd/O/A; p.14 gives player/judge guidelines. | 给出了可执行的交互流程与计分指标，但 'lateral thinking' 构念本身主要靠 SPLAT 成绩间接操作化，缺少独立操作化说明，故为 0.5。 |
| A8 | 水平数与类型 | 0.5 | p.9 Table 4 lists seven player models; p.10 Table 6 lists base/data/data+reasoning; p.4 defines Easy/Medium/Hard as 1–3, 4–6, 7–9. | 报告了多个水平标签，但未系统说明水平类型、间距/全距或连续变量中心化，故为 0.5。 |
| A9 | 单一操作化的风险 | 0 | p.3 and p.4 present SPLAT as the main lateral-thinking measure; p.9-p.10 transfer to RiddleSense/BrainTeaser is elicitation, not convergent validation. | 关键构念 'lateral thinking' 仅用 SPLAT 单一操作化，且全文未讨论单一操作化对可推广性的限制，故为 0。 |
| A10 | 单一方法的风险 | NA | — | 研究不使用自陈式多构念量表，所有测量均为任务文本输出/LLM 判断/人类一致性评分；共同方法偏差框架不适用。相关 judge-player 同源问题在 J4 编码。 |
| B1 | 被试间设计 | NA | — | 没有人类被试被分配到互斥条件；模型比较不是人类被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量设计或条件顺序平衡。 |
| B3 | 混合设计 | NA | — | 没有人类混合设计，也没有逐因素标注组间/组内属性。 |
| B4 | 因子设计 | NA | — | Table 4 按模型和难度列出成绩，但这是描述性分层，不是有完整设计矩阵与交互检验的因子实验。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有报告模型×难度或其他因素的交互项统计检验。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡顺序。 |
| B9 | 准实验设计 | NA | — | 没有准实验设计、非随机分组或因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内设计，因此不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | [[PDF_PAGE_7]] 和 [[PDF_PAGE_9]] 的随机选择是抽取谜题/辅助提示，不是把分析单位随机分配到实验条件；无分配隐藏或条件随机化结构。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序或被试内顺序设计。 |
| C3 | 恒定 | 0.5 | p.8: 'R = 1 and the max round is 15'; judge fixed as WizardLM-2; p.9: same auxiliary prompts across LLMs. | 报告了部分固定控制（judge、轮数、辅助提示），但未报告温度、模型 snapshot 等，也未讨论恒定控制的外部效度限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后分配程序。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入分析模型；难度层级只是描述性分层，未做 ANCOVA 或斜率齐性检验。 |
| C6 | 盲法 | 0 | p.7: 'For each puzzle, we ask three different individuals to assess the final answer agreement and the reasoning process agreement'; no blinding description. | 使用了人类评分者，但未报告盲法安排、施盲对象或成功检验；存在可盲未盲风险，故为 0。 |
| C7 | 平衡的层级 | NA | — | 没有被试内条件顺序，也没有完全平衡/拉丁方/ABBA 层级需要报告。 |
| D1 | 练习效应 | NA | — | 每个谜题作为独立会话评估，没有跨条件练习块或上下文内学习设计；不涉及人类练习效应控制。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长或疲劳控制问题；LLM API 调用不涉及疲劳效应。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件残留或清洗期设计；辅助提示的跨基准迁移是研究操纵本身，不是被试内 carryover。 |
| D4 | 不对称迁移 | NA | — | 没有被试内条件迁移或迁移对称性检验。 |
| D5 | 范围效应 | NA | — | 任务为客观正确性/语义匹配，不使用主观量表或绝对量值估计，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选项/刺激顺序随机化或反平衡；多轮提问顺序是任务本身而非可平衡的选项位置。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 没有人类实验被试；人类仅作为标注者/一致性评分者，不存在掩饰情节或事后推断研究假设的需求特征检查。 |
| E5 | 实验者效应 | 0 | p.7 and p.15: three human assessors are used; no report of blinding, rater training, or script standardization. | 存在人类评分者，但未报告评分者是否知晓条件/模型、盲法层级、培训或标准化脚本，故为 0。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.9 Table 4 reports Acc by Easy/Medium/Hard; p.5 Figure 2 reports difficulty/token distributions; no SD, skew, or endpoint frequencies. | 报告了均值层面的成绩和难度分布，可看出高分未接近 100%，但缺少 SD/偏度/端点频率与 pilot 校准说明，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 不使用同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.9 Table 4 reports Acc/Rnd/O/A percentages only; p.21 checklist Q7 answers 'No' for statistical significance/error bars. | 没有效应量、置信区间、样本量依据或多重比较校正，仅报告点估计，故为 0。 |
| F2 | 内部效度 | 0 | p.8-p.9 compare fixed models/prompt conditions; no random allocation, baseline equivalence, flow, or internal-validity threat assessment beyond performance-bias argument. | 无随机分配与内部效度威胁评估，且以比较性语言报告提示增强效果，故为 0。 |
| F3 | 构念效度 | 0.5 | p.7-p.8 Tables 2–3 report human agreement with judge models (>80% for WizardLM-2); p.9 discusses performance bias. | 有人类一致性作为效度证据，但缺少指标信度、操纵检验和单一操作化局限讨论，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.4: puzzles gathered from public websites and human-reviewed; p.9-p.10 applies prompts to RiddleSense/BrainTeaser. | 报告了谜题来源和跨基准应用，但未系统讨论样本代表性、推广边界和跨情境复现，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p.8: metrics are computed over N samples; p.9 Table 4 aggregates model performance across puzzles and difficulty levels; no multilevel model. | 说明了分析在谜题/模型层面聚合，但未显式处理谜题嵌套或轮次嵌套结构，故为 0.5。 |
| G2 | 随机效应 | 0 | p.8-p.9 analyses aggregate over puzzles and compare model means; no random effects are reported for puzzles or models. | 没有报告随机效应结构，且需要将谜题视为抽样总体以支持推广；把材料/谜题当固定集处理，故为 0。 |
| G3 | 材料作为随机效应 | 0 | p.4: 975 unique puzzles treated as benchmark; p.8-p.9 aggregate across these fixed puzzles; no (1&#124;item) or quasi-F. | 有限谜题被当作固定材料，仅做模型层面汇总，未把材料作为随机效应，限制对谜题总体的推广，故为 0。 |
| G4 | 统计功效 | 0 | p.8-p.9 no power analysis; Table 4 has no CIs; p.21 checklist Q7 'No'. | 无事前功效分析、预期效应量来源或置信区间，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p.8: 'R = 1 and the max round is 15'; p.7: 60 puzzles selected for agreement evaluation; p.10 ablation reported. | 报告了部分条件与消融，但缺少数据排除规则、样本量决定方式和验证/探索分析区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, identifier, or analysis plan is mentioned in the paper or checklist. | 未预注册，也未区分预注册验证性分析与事后探索性分析，故为 0。 |
| J1 | 位置偏差 | NA | — | 评估不是多项选择、排序或成对 LLM-as-judge 比较，而是开放式最终答案的语义匹配，无候选位置操纵。 |
| J2 | 冗长偏差 | 0 | p.8 uses WizardLM-2 as judge; p.14 judge guidelines only say to evaluate correctness, with no length control; p.4 Table 1 reports Avg. A = 45.53 but no length-score correlation. | 开放式答案由 LLM judge 评估，存在长度偏差风险但未说明/控制，未报告长度与得分相关，故为 0。 |
| J3 | 谄媚 | NA | — | 任务中没有用户先验立场或 pro/anti framing 操纵；judge 依据参考场景回答 yes/no/irrelevant，不是谄媚评估范式。 |
| J4 | 自我偏好 | 0.5 | p.9: 'Performance Bias. ... concerns about bias when a model like WizardLM-2 (8x22B) evaluates its own performance are mitigated...'; Table 4 also uses WizardLM-2 as a player. | 识别了裁判与被评模型同源的风险并作辩护，但仍用同源模型作 judge，未报告独立裁判团、匿名化或 self-preference 比例，故为 0.5。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.9-p.10: 'randomly select m situation puzzles (m = 1) ... gather the first 5 question-answer pairs ... same auxiliary prompts are used across different LLMs'. | 报告了 few-shot 式辅助示例的来源与数量，但未做多 seed 重采样、排列反平衡或提供完整模板，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.14 Appendix A.2 gives player/judge guidelines; p.7 Figure 3 shows prompt skeleton with placeholders; no versioned prompt or sensitivity ablation. | 提供了较实质的 prompt 指南，但缺少版本号、完整模板、dev/test 划分和措辞敏感性消融，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 情境谜题文本很短，且无长文档/RAG 设置；不涉及长上下文信息位置效应。 |
| J8 | 温度与采样随机性 | 0 | p.8: 'We set R = 1 and the max round is 15'; no temperature, top-p, seed, or repeated-sampling CI reported. | 只报告 R=1，未报告采样超参、随机种子或重复采样方差，故为 0。 |
| J9 | 重复与文本退化 | 0 | p.8-p.9 involve open-ended final answer generation, but no decoding strategy, repetition penalty, repetition rate, or truncation report. | 任务涉及开放式生成，但未报告解码与重复退化控制，故为 0。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本输入，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4: puzzles are gathered 'from various public websites using web crawlers'; no contamination check against model training data or training cutoff. | 公开网站来源的谜题可能已被预训练数据覆盖，但未做任何污染检测或训练截止日期对照，故为 0。 |
| J12 | 基准饱和 | NA | — | SPLAT 是新建基准，Table 4 中最高平均准确率约 41.70%，Hard 约 17.27%，远未接近天花板；饱和问题不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，也未按约束类型测量指令违反率；不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.3: judge answers are constrained to {yes, no, irrelevant}; p.14 judge guidelines repeat this; no format-legal rate or retry policy reported. | 报告了分类输出约束，但未报告格式合法率、解析失败处理或重试策略，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1-p.3 frame lateral thinking as a human cognitive style and apply situation puzzles to LLMs; p.7-p.8 use human agreement, but no systematic human-player same-paradigm comparison. | 有构念界定和人类一致性验证，但未系统论证 LLM 上 lateral thinking 与人类同名构念的异同，也未报告人类玩家同范式准确率，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的涌现能力曲线或指标诱导假象分析。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及以代理指标为优化目标的训练、RL 或 best-of-N 优化，不适用 overoptimization 监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.8-p.9 report model names and R=1, but no exact API snapshot/date, no confidence intervals, no paired tests, and no raw logs. | 评估可复现性所需重复次数、snapshot 标识、CI 和配对检验均缺失，故为 0。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.8: 'max round is 15'; Table 4 reports Rnd; p.9-p.10 use first 5 QA pairs from multi-turn interaction, but no per-round trajectory or truncation analysis. | 确实做了多轮评估并报告平均轮数，但未按轮次拆分评分或分析一致性衰减，也未说明上下文截断处理，故为 0.5。 |

## 编码小结
论文提出 SPLAT 情境谜题基准与多轮 player-judge 框架，核心贡献在基准构建、LLM 交互评估和提示增强。方法层面报告了任务流程、主要指标和部分人类一致性验证，但统计不确定性、采样参数、模型 snapshot、污染检查、随机效应、提示敏感性、长度/位置偏差和预注册等关键可复现性与效度信息明显不足。由于研究不是人类被试实验，B1–B10、D1–D5 等分配/顺序组件多为不适用；对 LLM 评测相关的 J 组件则按实际风险编码。
