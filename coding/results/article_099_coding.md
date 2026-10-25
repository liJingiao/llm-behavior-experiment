# article_099 | Logical forms complement probability in understanding language model (and human) performance | 2025

研究类型概述：LLM 逻辑推理基准/受控数据集评估，并辅以小型人类行为实验。核心操纵/分层为命题与模态逻辑中的 modality、argument form 及 meaningful/nonsensical 内容，因变量为 soft accuracy、hard accuracy 及人类 Yes/No 正确率与反应时；统计上使用含 LLM 或参与者随机效应的混合模型。
- **研究构念（Construct）**：演绎推理、逻辑形式效应与内容—形式交互｜CA 构念锚定：演绎推理（deductive reasoning, `trm_4a3fd79d0a072`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：LLM 逻辑推理基准/受控数据集评估，并辅以小型人类行为实验。核心操纵/分层为命题与模态逻辑中的 modality、argument form 及 meaningful/nonsensical 内容，因变量为 soft accuracy、hard accuracy 及人类 Yes/No 正确率与反应时；统计上使用含 LLM 或参与者随机效应的混合模型。｜CA 任务锚定：演绎推理任务（deductive reasoning task, `trm_4c898b8c2d071`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: 'Pairing with four rules and theorem–fallacy variations, we have a total of 3 × 4 × 2 = 24 forms'; p.5: 'We evaluate ... with the probability-based protocol'. | modality、argument form、内容有意义/无意义等自变量被命名并给出水平，但各水平如何分配到 LLM/人类单位以及操纵检验报告不完整。 |
| A2 | 因变量 | 0.5 | p.5: soft accuracy 公式 p̂ = ...；p.7: 人类二值正确率 Eq. (6)；p.17: hard accuracy 与 N=10 token 规则。 | 因变量测量与计分方式明确，但未见信效度证据；连续指标预处理与天花板/地板说明有限。 |
| A3 | 控制变量 | 0.5 | p.12 Table 3 列出 Hugging Face commit；p.12 说明 bf16/f32 量化；p.13 给出固定 prompt 与按键反转。 | 报告了若干控制变量及控制手段，但未系统列出完整控制变量清单。 |
| A4 | 混淆变量 | 0.5 | p.3: 'Knowledge bias is a common pitfall... Such bias will complicate logical reasoning... and should be avoided in data curation'; p.7: mirror dataset 与 nonsensical words。 | 识别并控制了知识/内容混淆，但未做敏感性分析或系统量化残余混淆威胁。 |
| A5 | 调节变量 | NA | — | 全文没有把某个变量作为调节变量提出并做中心化/简单斜率分析；附录 C.2 的交互属于额外逻辑形式分析，不构成正式调节模型。 |
| A6 | 中介变量 | NA | — | 无中介变量与直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.3–4 给出逻辑形式到自然语言模板的转换规则；p.13 给出 exact prompt format；p.7 与 p.13 给出人类按键说明。 | 关键构念均有可复现的操作化程序：数据合成、prompt、计分与人类任务说明较完整。 |
| A8 | 水平数与类型 | 0.5 | p.4: '3 × 4 × 2 = 24 forms'；p.6 Table 1 列出 modality 与 argument form 各水平；p.7 mirror dataset 区分 meaningful/nonsensical。 | 水平数与具体标签清楚，但未系统说明水平类型、间距/全距及连续变量中心化。 |
| A9 | 单一操作化的风险 | 1 | p.5 soft accuracy；p.17 Table A4 比较 soft、thresholded soft 与 hard accuracy；p.9 limitations 讨论合成语言与推广限制。 | 采用 soft/hard 等多种指标并报告会聚比较，同时讨论单一合成数据与语言覆盖的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 自变量是材料/逻辑形式属性，因变量是模型概率或人类按键反应，不存在自陈式同源共同方法偏差问题。 |
| B1 | 被试间设计 | NA | p.5 Eq. (4) 将 LLM 作为随机效应并跨全部条件评估；p.7 Eq. (6) 将 ParticipantID 作为随机效应。 | 核心自变量为模型内/被试内条件，未设置互斥的组间实验条件分配。 |
| B2 | 被试内设计 | 0.5 | p.7: 'logit(Acc) ∼ Modality + ArgForm + Rt + (1 + Rt &#124; ParticipantID)'；p.5 Eq. (4) 含 (1 + Perplexity &#124; LLM)。 | 随机效应表明存在重复测量/被试内结构，但条件呈现顺序与平衡方案未报告。 |
| B3 | 混合设计 | NA | — | 没有同时包含组间与组内焦点因素的混合设计；按键反转只是反平衡，不是实验因素。 |
| B4 | 因子设计 | 0.5 | p.4: '3 × 4 × 2 = 24 forms'；p.6 Table 1 给出 modality × argument form 分列结果；p.15 C.2 有 'Modality × ArgForm' 交互模型。 | 存在交叉因子结构，但主分析多为加性模型，未给完整设计矩阵/每格样本量，交互只在附录额外分析。 |
| B5 | 主效应 | 0.5 | p.6: 'likelihood ratio test ... yields a significant result (p < 0.001)'；p.6 Table 2 报告 pairwise hypotheses；p.7 人类模型 χ2(2)=25.6。 | 报告了主效应/系数检验与部分置信区间，但缺完整 F/df/效应量。 |
| B6 | 交互作用 | 0.5 | p.15 C.2: 拟合含 'Modality × ArgForm + Perplexity' 的模型并报告部分交互系数与 p 值。 | 有交互检验，但未报告完整简单主效应、多重比较校正与带误差棒交互图。 |
| B7 | 区组设计 | NA | — | 没有区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡顺序。 |
| B9 | 准实验设计 | NA | — | 没有非随机分组准实验设计或因果组间比较。 |
| B10 | 被试内设计的适用条件 | 0 | p.7 人类模型显示 participant 内重复，但全文未论证逻辑形式条件的可逆性或迁移对称性。 | 若按被试内/重复项目处理，论文未讨论处理可逆性与迁移/学习对称性，也未报告相应检验。 |
| C1 | 随机化 | NA | — | 没有把分析单位分配到互斥实验条件的随机化程序；LLM 与人类均为条件内评估。 |
| C2 | 平衡 | 0 | p.13 仅说明一半参与者反转 F/J 按键；未报告题目/条件顺序平衡方案及每种顺序人数。 | 存在重复呈现条件，但顺序平衡未报告，故核心质控做法缺失。 |
| C3 | 恒定 | 0.5 | p.12 Table 3 列出模型 commit 与量化格式；p.13 给出固定 prompt；p.9 limitations 讨论合语言/英语。 | 列出若干恒定变量及水平，但未系统讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.5 Eq. (4) 将 Perplexity 作为固定效应并设随机斜率；p.7 Eq. (6) 纳入 Rt。 | 已知混淆变量被测量并纳入模型，但未检验协变量斜率齐性等关键假设，调整后效应报告不完整。 |
| C6 | 盲法 | NA | — | 无组间条件可隐藏，且无人类评分者；人类实验为自动化任务，不涉及盲法分配。 |
| C7 | 平衡的层级 | 0 | p.13 只报告按键反转；未说明完全平衡、拉丁方或 ABBA 等平衡层级及构造方法。 | 存在重复条件但未报告任何顺序平衡层级。 |
| D1 | 练习效应 | 0 | p.13 人类指导语仅说明作答按键，无练习块、截除或练习效应控制说明。 | 人类重复作答存在练习效应风险，但未报告控制安排。 |
| D2 | 疲劳效应 | 0 | p.13 未报告 session 时长、休息间隔或条件时间分散；p.12 仅报告 LLM 计算耗时。 | 人类任务疲劳控制未报告。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM 每个 prompt 独立、上下文重置；人类为单次 item-level 任务，无跨条件处理式洗脱期设计。 |
| D4 | 不对称迁移 | NA | — | 没有顺序化处理条件的迁移对称性设计。 |
| D5 | 范围效应 | NA | — | 因变量为正确率/概率与反应时，不是主观量表绝对判断，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.13: 'Half of the participants see ... "F" for Yes, and "J" for No'; 另一半反转按键。 | 对 Yes/No 按键位置做了反平衡，但未报告题目呈现顺序随机化及每顺序分配细节。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中间反应倾向。 |
| E4 | 需求特征 | NA | — | 任务为客观逻辑判断，无掩饰情节需求，也未主张需要事后访谈检查需求特征。 |
| E5 | 实验者效应 | NA | — | 数据采集通过 Prolific 自动化完成，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 1 列出大量均值（部分达 1.000）；p.6 Figure 3 给出 95% CI；p.17 比较 soft/hard accuracy。 | 报告了均值/区间并可见部分接近上限，但未系统报告偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 没有同源自陈式多构念测量，CMB 不适用。 |
| F1 | 统计结论效度 | 0.5 | p.6 报告 marginal R2=0.342、conditional R2=0.543、p<0.001；Figure 3 有 95% CI；p.7 人类模型 χ2 检验。 | 报告了效应量/区间与主要检验，但无样本量确定依据，多重比较校正未说明。 |
| F2 | 内部效度 | 0.5 | p.3: 控制 knowledge bias；p.5 同一组 interpretations 应用于各逻辑形式；p.12 Table 3 固定 checkpoints。 | 通过内容和模型版本控制部分效度威胁，但无随机分配、基线等价、被试流向/损耗处理报告。 |
| F3 | 构念效度 | 0.5 | p.5 定义 soft accuracy；p.17 Table A4 比较 soft 与 hard accuracy；p.4 逻辑形式 ground truth 明确。 | 构念操作化与部分效度证据较清楚，但无内部一致性/重测/评分者信度等正式信度报告。 |
| F4 | 外部效度 | 0.5 | p.7: '710 responses from adults fluent in English through Prolific'；p.9 limitations 指出合成语言、仅英语、人类样本有限。 | 报告样本来源并讨论推广边界，但缺人口学特征与跨样本复现。 |
| G1 | 分析单位 | 1 | p.5 Eq. (4) 使用 (1 + Perplexity &#124; LLM)；p.7 Eq. (6) 使用 (1 + Rt &#124; ParticipantID)。 | 处理/观测层级与混合模型随机效应匹配，明确区分 LLM 与参与者聚集结构；但未处理 interpretation/item 随机效应，另见 G3。 |
| G2 | 随机效应 | 1 | p.5 Eq. (4) 与 p.7 Eq. (6) 明确给出随机截距/随机斜率；p.6 Figure 4 报告 per-model random effects。 | 明确 LLM 与参与者为随机效应，并报告随机效应结构。 |
| G3 | 材料作为随机效应 | 0 | p.5: 'The same set of interpretations is applied to variables p, q'；Eq. (4) 仅含 LLM 随机效应，未含 item/interpretation 随机效应。 | 材料/interpretations 是有限抽样但未作为随机效应建模，存在语言材料固定效应风险。 |
| G4 | 统计功效 | 0 | p.5 报告 24,000 questions；p.7 报告 710 human responses；全文无事前功效分析或样本量推导。 | 无设计阶段功效分析或样本量论证，仅报告检验结果。 |
| G5 | 研究者自由度 | 0.5 | p.17 说明 hard accuracy 使用 N=10 token 与 threshold 0.5；p.5 报告 24,000 题；p.7 报告 710 responses。 | 报告了部分计分/排除规则和条件，但样本量决定方式及验证性/探索性分析区分不足。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册平台、编号或数据收集前分析计划。 | 无预注册；也没有区分预注册验证性与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM-as-judge、排序或成对候选位置比较；Yes/No 概率评估无候选位置偏差。 |
| J2 | 冗长偏差 | NA | — | 不涉及开放式生成长短比较或 LLM 裁判质量评分。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或多轮谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 作为裁判。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.5: 'We use a zero-shot setting'；p.12: zero-shot nature。 | 零样本提示，无 few-shot 示例选择问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.13 给出 exact prompt format：'Consider the following statements... Answer:<eof>'；p.5 零样本设置。 | 提供了完整 prompt 模板，但无版本化、敏感性消融或 dev/test 划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | prompt 很短，无长上下文/RAG/信息位置操纵。 |
| J8 | 温度与采样随机性 | 0 | p.17 footnote: 'due to the non-deterministic nature of GPU parallelism, the soft accuracy results ... differ ... MSE <0.01'；未报告 temperature/seed/重复 N。 | 承认 GPU 非确定性，但采样超参、seed 与重复采样置信区间均未完整报告。 |
| J9 | 重复与文本退化 | NA | — | 任务只输出 Yes/No，不涉及开放生成退化。 |
| J10 | 分词效应 | NA | p.9: 'our material only covers English'。 | 单语言、单脚本，无跨语言/跨脚本分词比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.4–5 新构建 24,000 题合成数据集；p.12 Table 3 给出模型 commit；未报告训练截止日期或污染检测。 | 使用新自建受控数据集且给出模型版本，但未做污染检测/污染率报告。 |
| J12 | 基准饱和 | 0.5 | p.6 Table 1 显示 overall accuracy 约 0.335–0.926，部分子格达 1.000；p.5 使用连续 soft accuracy；未系统讨论饱和。 | 报告了分数量程并采用连续 soft accuracy，但未明确评估饱和或改用更难 held-out 子集。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.17 hard accuracy 规则：最多 N=10 tokens，若无 Yes/No 则记 0；phi-3-mini 'only on 76.3% of the cases it decodes an answer token within the first 10 output tokens'。 | 报告了 Yes/No 输出格式与部分合法率信息，但未使用文法约束，也未把格式失败与内容错误作为独立指标完整报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 1 | p.7 进行人类行为实验并用同一数据比较；p.9 明确讨论 'LLMs as human models... execute such approaches cautiously'；p.12 Table 3 给出权重快照/commit。 | 明确把 LLM 逻辑推理表现与人类同名构念对照，报告模型版本，并警告不宜直接外推人类心理学结论。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的涌现曲线或能力曲线宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无针对代理指标的优化/训练/奖励过优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.12 Table 3 给出精确 Hugging Face commit；p.17 footnote 报告两次 soft accuracy 的 MSE<0.01；但主表分数无重复 N/CI/配对检验。 | snapshot 标识较精确且报告了部分非确定性检查，但缺每分数重复次数、置信区间和模型间配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为严格单轮 Yes/No 回答，无多轮对话历史。 |

## 编码小结
论文较清楚地公开了数据生成、prompt、模型 checkpoint 与主要混合模型，复现基础较好；但人类实验细节、条件呈现顺序平衡、练习/疲劳控制、材料随机效应、功效分析与预注册等报告不足。多个内部效度/可复现性组件只能给部分分，部分不适用组件应记 NA。
