# article_185 | PrivacyLens: Evaluating Privacy Norm Awareness of Language Models in Action | 2024

研究类型概述：该文提出 PrivacyLens 框架与数据集，用 QA probing 和 LM agent action 两种方式评测多个 LLM 的情境隐私规范意识与无意隐私泄漏。主分析单位是每个 seed/vignette/trajectory 的模型输出或最终动作；比较 9 个模型与 Basic/Privacy-Enhancing 两种提示，并报告泄漏率、probing 准确率与 helpfulness，属 LLM 基准/代理评测而非人类被试实验。
- **研究构念（Construct）**：情境隐私规范意识、敏感信息披露与隐私—助人权衡｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让LLM先回答隐私传输是否合适，再在包含敏感信息和通信工具的代理轨迹中执行用户任务，编码最终行动是否泄露信息以及是否有帮助。（操纵隐私种子、情境和轨迹层级、基础或隐私增强提示、模型规模与模型家族。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.7 §5.1: 'we also experiment with another system prompt ... Basic Prompt ... Privacy-Enhancing Prompt'; p.8 Table 2 reports both prompt conditions for each model. | 提示类型是明确操纵的自变量，有两个水平且程序可见；但未报告操纵检验，也未明确说明条件顺序或分配细节，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.5 Eq.1 defines leakage rate; p.7 §5.1: 'Fleiss Kappa between f and the human majority vote is 0.82 ... accuracy ... 0.92'; helpfulness agreement '0.56'; p.8 Table 2 reports LR/LRh/helpfulness. | 因变量指标和计分方式明确，并有部分人类一致性验证；但缺少完整信效度论证、helpfulness 低一致性讨论及连续指标预处理/端点控制说明。 |
| A3 | 控制变量 | 0.5 | p.7 §5.1: 'All models are used with a temperature of 0'; model snapshots listed; p.18 Appendix C: GPT-4 emulator and fixed sandbox toolkits. | 报告了温度、模型快照、同一轨迹与固定模拟器等控制；但未以系统清单逐项说明控制手段及其外推限制。 |
| A4 | 混淆变量 | 0.5 | p.19 Appendix C: 'One limitation of this setup is that it may affect the validity of evaluating LMs other than GPT-4'; p.10 §6 discusses U.S.-only norms and final-action-only setup. | 识别了轨迹由 GPT-4 agent 生成、仅评最终动作、美国规范等潜在混淆/限制；但未做敏感性分析或量化残余威胁。 |
| A5 | 调节变量 | NA | — | 论文未提出正式调节假设或调节模型；模型规模与提示类型比较属描述性分组比较，不是受控调节分析。 |
| A6 | 中介变量 | NA | — | 无中介变量或中介效应分解，研究问题不涉及中介机制。 |
| A7 | 操作性定义 | 1 | p.3-5 §3.2-3.3 describe seed→vignette→trajectory pipeline and evaluation; p.5 Eq.1; p.21-30 Appendix F provide full prompts and unit-test/refinement procedures. | 关键构念均有可复现操作化：隐私敏感 seed 五元组、vignette 生成、agent 轨迹、probing 问题、泄漏分类器与 helpfulness rubric；提示词和评分 prompt 均给出。 |
| A8 | 水平数与类型 | 0.5 | p.7 §5.1 lists nine model snapshots and two prompt types; p.8 Table 2 lays out Basic vs Privacy-Enhancing results. | 模型与提示水平及标签明确，均为名义分类；但未以正式设计矩阵说明水平类型、间距/全距或连续化处理，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.7-8 §5.2: probing accuracy vs action-based leakage show 'a huge discrepancy'; both QA probing and agent action are used as operationalizations. | 隐私规范意识采用 probing 与 action 两种操作化，并讨论二者不一致；但未报告会聚证据或对多操作化一致性的系统检验。 |
| A10 | 单一方法的风险 | NA | — | 不涉及人类自陈式多构念同源测量；自变量为模型/提示，因变量为模型输出与自动/人工编码，无经典共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试或被试组分配；所有模型在同一固定评测集上运行，不构成被试间实验。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量设计；两种提示虽在相同轨迹上比较，但为独立 API 调用，未按被试内顺序平衡编码。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内混合设计及相应混合误差项。 |
| B4 | 因子设计 | NA | — | 模型、提示与数据层级虽被描述性交叉比较，但无正式因子设计、设计矩阵、每格样本量与 ANOVA 交互检验。 |
| B5 | 主效应 | NA | — | 无因子设计主效应统计检验；模型与提示差异以描述性比率报告。 |
| B6 | 交互作用 | NA | — | 无正式交互项检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理研究；模型比较为基准评测，未作准实验因果设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理顺序问题，不涉及可逆性或迁移对称性。 |
| C1 | 随机化 | NA | — | 无处理分配或随机化；所有模型在固定数据与固定条件下评测。 |
| C2 | 平衡 | NA | — | 无条件顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.7 §5.1: temperature 0 for all models and exact snapshots; p.18 Appendix C: fixed GPT-4 emulator and sandbox tools. | 报告了若干恒定变量和固定水平，但未系统列出所有环境/版本常量及由此产生的外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对分配程序。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型；研究为固定测试集基准比较。 |
| C6 | 盲法 | 0 | p.7 §5.1: 'having 4 annotators label whether an action leaks certain information on 153 pairs'; no blinding or blinding-success check reported. | 存在人工评分者用于验证分类器，但全文未报告对评分者施盲、盲法类型或实施细节，属于适用但未报告。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应平衡层级问题。 |
| D1 | 练习效应 | NA | — | LLM 每次调用独立，无练习或上下文内学习安排。 |
| D2 | 疲劳效应 | NA | — | 无人类长时 session 疲劳风险；评测为独立模型调用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无条件顺序与不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 无人类被试内绝对量表评分；helpfulness 虽为 0-3 评分，但由 LLM 裁判生成，不是人类范围效应设计。 |
| E1 | 位置 / 顺序偏差 | 0 | p.6 Figure 3 consistently shows 'Choices: (A) Yes (B) No' for probing questions. | 多项选择选项位置固定，未做随机化或反平衡，也未讨论或量化位置偏差；属于有选项位置风险但未控制。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表；QA 为二分选择，不涉及反向计分默许偏差。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试参与核心实验，不存在人类需求特征；众包仅用于 seed 构思。 |
| E5 | 实验者效应 | NA | — | 核心数据采集自动完成，无人类主试/实验者接触；人工标注仅用于验证分类器，不构成实验者效应场景。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Figure 4 reports probing accuracy with 95% CIs; p.8 Table 2 reports leakage/helpfulness rates; no endpoint frequencies or pilot difficulty calibration. | 报告了均值/区间与部分端点水平（强模型 probing 近 100%），但未系统报告端点比例、偏度或 ceiling/floor 校准。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量；不涉及共同方法偏差统计检验。 |
| F1 | 统计结论效度 | 0.5 | p.7 Figure 4 reports 95% confidence intervals for probing accuracy; p.8 Table 2 reports effect-size-like rates; no power analysis or multiplicity correction. | 报告了部分 CI 与比率型效应量，但缺样本量依据、所有分析的多重性校正及正式统计检验假设说明。 |
| F2 | 内部效度 | NA | — | 非随机实验、无因果处理分配；论文是基准评测，不作 RCT 式内部效度推断。 |
| F3 | 构念效度 | 0.5 | p.6 §4: seed validation Fleiss' Kappa 0.79; p.7 §5.1: classifier-human Kappa 0.82/accuracy 0.92, helpfulness Kappa 0.56; multiple operationalizations reported. | 有部分信度/一致性证据与双重任务操作化，但无正式效度论证或操纵检验，helpfulness 测量效度也偏弱。 |
| F4 | 外部效度 | 0.5 | p.6 §4 describes U.S. regulations, literature, and Prolific crowdworkers; p.10 Limitations: U.S.-only norms and LM-mediated communication; p.19-20 Table 5 extends to ConfAIde/CultureBank subsets. | 报告了样本来源和若干推广边界，并有跨数据集扩展；但缺完整抽样框/人口学代表性，跨情境复现仍有限。 |
| G1 | 分析单位 | 0.5 | p.5 Eq.1 defines leakage over each trajectory; p.7-8 tables aggregate by model and prompt. | 说明了每个轨迹/最终动作为分析单位，但同一组轨迹跨模型和提示重复使用，未用多层模型处理项目/模型聚集，也未说明分配层级匹配。 |
| G2 | 随机效应 | NA | — | 无混合模型或随机效应结构；比较的是固定的一组具体模型，不作模型总体随机效应推断。 |
| G3 | 材料作为随机效应 | NA | — | 493 个 seed/vignette/trajectory 作为固定评测材料使用，未把材料作为随机因子；研究不进行材料总体随机效应推断。 |
| G4 | 统计功效 | 0 | p.7 §5.1 reports 493 seeds and 1,479 probing questions but no power analysis or sample-size rationale; p.8 reports rates without full CIs. | 无事前功效分析、目标效应量或样本量决定依据，也未对所有主要比较报告 CI。 |
| G5 | 研究者自由度 | 0.5 | p.6 §4 describes validation filtering to 493 valid seeds; p.8 Table 2 reports probing and action outcomes; p.9 §5.3 labels dynamic extension as proof of concept. | 报告了主要排除/验证规则、主要因变量和部分探索性扩展；但缺样本停止规则、是否追加数据及验证性/探索性分析的明确区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered analysis plan is mentioned in the paper. | 无公开预注册、样本停止规则或分析计划登记；按编码口径记 0。 |
| J1 | 位置偏差 | 0 | p.6 Figure 3 fixes the choice order as 'Choices: (A) Yes (B) No'; no position swapping or randomization is reported. | LLM 需在固定 A/B 位置作答，存在位置偏差风险；未做反平衡、交换重判或位置×正确率分析。 |
| J2 | 冗长偏差 | 0 | p.29-30 Appendix F.2.3-F.2.4 give leakage/helpfulness judging prompts; no length control, length rubric, or length-score correlation is reported. | 使用 LLM 裁判评估开放式最终动作，但未说明或控制长度偏差，也未报告文本长度与得分的相关。 |
| J3 | 谄媚 | NA | — | 评估中无用户先验立场、反馈或纠错对话操纵，不涉及谄媚风险。 |
| J4 | 自我偏好 | 0 | p.7 §5.1: 'we build a few-shot classifier f using the same Mistral model'; p.8 Table 2 shows Mistral-7B-Instruct-v0.2 is also an evaluated model. | 裁判模型与被评模型同源且作为唯一裁判，存在自我偏好风险；未报告异源陪审团、匿名化或 favor-own-generation 量化。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.7 §5.1 says a few-shot classifier is used; p.29-30 Appendix F.2.3-F.2.4 show fixed examples but no source, label ratio, order balancing, or multi-seed repetition. | 仅给出单一 few-shot 模板及示例，未说明示例来源、标签比例、排列控制或多示例集重复，属关键信息缺失。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.27-30 Appendix F.2.1-F.2.4 provide full Basic/Privacy-Enhancing prompts and judge prompts; no prompt version/date, sensitivity ablation, or dev/test split is reported. | 完整模板可得且有 Basic vs Privacy-Enhancing 对比，但无版本化、语义等价敏感性消融或测试集调参隔离说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是长上下文/RAG 位置效应实验；轨迹虽有多步工具观测，但未操纵关键信息首/中/尾位置。 |
| J8 | 温度与采样随机性 | 0.5 | p.7 §5.1: 'All models are used with a temperature of 0'; no random seed, repeated sampling N, or variance/CI for leakage rates is reported. | 报告了 temperature，但未报告 top-p/top-k、种子、每条件重复次数及相应 CI，属部分满足。 |
| J9 | 重复与文本退化 | 0.5 | p.7 §5.1 reports temperature 0; no explicit greedy/beam/sampling strategy, repetition penalty, n-gram repetition/degeneration rate, or truncation ratio is reported. | 报告了首要解码参数 temperature，但未完整说明解码策略与重复/退化质控，条件间一致性也仅部分可知。 |
| J10 | 分词效应 | NA | — | 任务为英文单语言、单脚本输入；无跨语言/跨脚本分词效应比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.9 §5.3 says dynamic extension 'holds the potential to mitigate data contamination'; no training cutoff comparison, overlap test, or contamination rate is reported. | 虽提及污染风险与动态缓解潜力，但未报告测试集发布日期与模型训练截止日期对照，也未做污染检测。 |
| J12 | 基准饱和 | 0.5 | p.7 Figure 4 shows several strong models at 97.57%-100% probing accuracy; no ceiling discussion or switch to continuous metrics/harder subset. | probing 指标对强模型接近饱和，但论文未系统处理 ceiling，也未改用连续指标或更难子集；泄漏率本身未饱和。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；agent 格式遵循只是任务执行手段，未测量 IF 准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.27-28 Appendix F.2.1-F.2.2 require 'Single JSON object' for Action Input and ReAct format; no format legality rate or retry/post-processing statistics are reported. | 设置了结构化输出/JSON 格式要求，但未报告格式合法率，也未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不是安全/越狱或对抗攻击评估；隐私泄漏是 Normal-use agent 风险，不涉及 jailbreak ASR。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.3 §3.1 grounds the risk model in Contextual Integrity; p.5 uses a probing question from a human privacy-expectation survey; p.10 Limitations acknowledges cultural/individual differences and setup scope. | 明确以人类隐私规范理论定义构念，并借用人类调查问题；但未系统论证 LLM 同名构念与人类构念的异同，也无同范式人类基线对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 仅比较两对模型规模并描述 probing/action 表现，未报告规模曲线，也未宣称涌现或突变；该风险不实际存在。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对代理指标进行训练、RL、best-of-N 或奖励优化；无 overoptimization 监控问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.7 §5.1 gives exact snapshots such as gpt-4-1106-preview and claude-3-haiku-20240307; p.7 Figure 4 gives probing 95% CIs; no repeated-run N or paired tests for leakage are reported. | 报告了精确模型版本、代码/数据与部分 CI，但缺重复次数、泄漏率 CI、配对 bootstrap/McNemar 等可复现性统计。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 不是多轮对话实验；模型仅在给定固定轨迹后生成最终动作，未评估跨轮次一致性衰减。 |

## 编码小结
评测框架与任务操作化较完整，提供了数据构建流程、模型快照、完整提示词、部分人类验证与 probing 置信区间；但研究基本为描述性基准评测，无随机分配、预注册或功效分析，主要推断缺少重复运行与配对检验。LLM 裁判由 Mistral-7B 同时作为被评模型和唯一裁判，存在同源自我偏好风险；多项选择位置、生成长度和解码随机性控制不足，隐私规范构念向人类或更广文化情境的外推也有限。
