# article_044 | Leveraging In-Context Learning for Political Bias Testing of LLMs | 2025

研究类型概述：这是一项 LLM 行为评测/基准研究：以人类问卷数据作为 in-context examples，提出 Questionnaire Modeling（QM），比较 zero-shot、random context、QM 以及不同模型家族/规模/instruction-tuned 版本在 7 个政治态度题上的 personalization accuracy、bias score 与跨 paraphrase 的 bias variability；分析单位为模型在 respondent × target question × paraphrase 上的预测/概率，而非人类被试。
- **研究构念（Construct）**：语境依赖的政治态度与反应偏差（context-dependent political attitudes and response bias）｜CA 构念锚定：态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；反应偏向（response bias, `trm_559f0a129c136`）
- **实验任务与范式（Task / Paradigm）**：这是一项 LLM 行为评测/基准研究：以人类问卷数据作为 in-context examples，提出 Questionnaire Modeling（QM），比较 zero-shot、random context、QM 以及不同模型家族/规模/instruction-tuned 版本在 7 个政治态度题上的 personalization accuracy、bias score 与跨 paraphrase 的 bias variability；分析单位为模型在 respondent × target question × paraphrase 上的预测/概率，而非人类被试。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_3-4: Figure 2 caption says 'The first 60 conversation turns are in-context examples'; p.4 says zero-shot baseline uses 'the same prompt but without the in-context examples'; p.6 reports 'randomly permuting example order or removing examples'. | 明确命名并报告了 QM、zero-shot、random context 及顺序/长度消融等操纵条件与水平；但未报告正式 manipulation check，条件分配在 LLM 层面也仅部分说明，故为部分完整。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_3: formulas for personalization accuracy, bias score, and StdBias; PDF_PAGE_4: top-10 token probabilities and forced-completion handling. | 因变量指标与计分公式明确（PA、Bias、StdBias），并说明 top-10 token 截断；但缺少信度/效度证据及连续指标的正式预处理/端点效应说明。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_9: 'we set the temperature to 1 for all models and analyze the top-10 most likely tokens'; PDF_PAGE_12: 'We use the same prompt for both the base models and instruction-tuned models'; PDF_PAGE_13: half/8-bit precision settings. | 报告了 temperature、top-10、prompt 一致性、模型精度等控制，但不是系统控制变量清单，也未逐一说明控制手段与外部效度影响。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_9: prompt format 'can be seen as another hyperparameter'; temperature/top-k 'not invariant'; 'choice and order of additional in-context examples can bias predictions'. | 识别了 prompt 格式、解码参数、in-context 示例选择/顺序等潜在混淆，并在局限中讨论；但未系统控制或做敏感性分析来量化残余威胁。 |
| A5 | 调节变量 | NA | — | 论文没有提出调节假设，也没有报告乘积项交互检验或简单斜率；模型规模/instruction tuning 比较是描述性分组，不构成正式调节分析。 |
| A6 | 中介变量 | NA | — | 论文不包含中介变量、直接/间接效应分解或中介模型。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_3: task definition and exact PA/bias formulas; PDF_PAGE_3-4: prompt construction with user/assistant turns; PDF_PAGE_12: Appendix B prompt formatting; PDF_PAGE_19-21: target and in-context questions; data/code public. | 关键构念均有可操作、可复现的程序：问卷任务、in-context 格式、输出概率求和方式、bias/PA 计算及完整问题列表。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_4: models Llama 3.1 8B/70B/405B, OLMo, GPT-3.5; p.4 prompt conditions; PDF_PAGE_19-21: seven target questions. | 报告了模型/条件/题目的水平标签，但没有系统给出水平类型、连续模型规模的间距/全距或中心化说明。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_6-7: compares QM with zero-shot and random context; PDF_PAGE_9: 'a holistic evaluation of bias should consider a variety of probing methods' and bias may not generalize to other modes. | 关键构念主要用单一 bias score 操作化，但论文通过多种 paraphrase、zero-shot/random-context 对照及局限讨论明确承认单一操作化的推广限制，符合单一操作但讨论限制的 1 档。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈量表测量；自变量为外部 prompt 条件，因变量为模型 token 概率/派生指标，无传统共同方法偏差的同源自评结构。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组分配；模型在不同 prompt 上被重复评测，不构成被试间设计。 |
| B2 | 被试内设计 | NA | — | 各 prompt/题目为独立调用，不存在需要平衡的跨条件被试内序列；论文也未将其建模为重复测量被试内设计。 |
| B3 | 混合设计 | NA | — | 没有逐因素标注组间/组内并分别报告误差项的混合设计分析。 |
| B4 | 因子设计 | NA | — | 论文没有正式因子设计、设计矩阵或 ANOVA 交互分析；模型×题目结果主要是描述性表格与相关性分析。 |
| B5 | 主效应 | NA | — | 没有因子设计意义下的主效应统计检验（F、df、p、效应量）；模型规模/instruction tuning 差异为描述性比较。 |
| B6 | 交互作用 | NA | — | 没有交互项统计检验或简单主效应分析；仅报告不同题目/模型下的描述性差异与相关系数。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；模型比较属于观察性评测，未按准实验类型处理选择偏差。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及人类被试内处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥处理条件的正式随机化；示例顺序随机置换在 E1/J5 下说明，不构成处理分配隐藏。 |
| C2 | 平衡 | NA | — | 没有条件顺序平衡方案或各顺序被试分配。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_9: temperature 1 and top-10 tokens; PDF_PAGE_12: same prompt for base/instruct; PDF_PAGE_13: precision settings. | 报告了若干被恒定的实验设置，但未系统列出所有恒定变量及其水平，也未充分讨论对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配程序。 |
| C5 | 纳入为变量 | NA | — | 没有将已知混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类主试/评分者盲法问题。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 每条 prompt 独立；不存在跨试次练习块或练习效应控制需求。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 或疲劳效应；LLM 调用为独立短任务。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个条件为独立上下文，无跨条件清洗期或残留效应。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉处理，因而不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 主要因变量是 token 概率/派生 bias 与 accuracy，不是被试内绝对量表判断。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_6: 'randomly permuting example order or removing examples'; PDF_PAGE_14-15: six permutations and last-example position effects; PDF_PAGE_12: 50 paraphrases with random seeds. | 对 in-context 示例顺序和 paraphrase 做了随机化/消融，并报告最后示例位置影响；但未给出完整平衡方案、各位置出现次数或完整顺序分配。 |
| E2 | 默认赞同 | NA | — | LLM 不使用 Likert 自评量表；人类 7 点量表被映射为二分答案（PDF_PAGE_12），无默认赞同/反向计分问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 未使用等级量表作 LLM 反应指标，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试、掩饰情节或事后访谈；需求特征不适用。 |
| E5 | 实验者效应 | NA | — | 完全自动化 API/本地推理，无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_5 Table 1: yes:no ratios and SD; Table 2: means ± SE; PDF_PAGE_13 Figure 6: human answer distributions; p.6 notes OLMo base always responds 'no'. | 报告了均值、标准差、yes:no 比例和一些端点堆积现象，但未系统报告偏度/端点频率，也未说明 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；因变量为模型概率/派生指标。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_5 Table 2: ±SE; PDF_PAGE_7: Pearson r=-.63, t(54)=-5.98, p<.001; PDF_PAGE_8 Figure 5: error bars. | 报告了标准误、部分置信区间与相关系数，但缺少样本量/功效依据和多重比较校正说明。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_4: model comparisons; PDF_PAGE_9: limitations acknowledge prompt/decoding confounds; no random allocation, baseline equivalence, or participant flow. | 内部效度威胁有部分讨论（prompt 格式、解码等），但没有随机分配、分配隐藏、基线等价性或正式敏感性分析；对 instruction tuning 的因果表述仍较强。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_3: human survey answers as gold labels; PDF_PAGE_5: majority-class baseline; PDF_PAGE_7: PA-bias correlation; no formal reliability/validity or manipulation check. | 有以人类答案作为金标准和 majority baseline 的效度线索，但缺少正式信度/效度检验和操纵检验。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_3: 192 elected Swiss candidates, Smartvote 2023; PDF_PAGE_9: limitations and future cross-language/other probing methods. | 样本来源与特征清楚，并讨论了 probing 方法与语言推广限制；但没有跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_3: predictions per respondent and target question, averaged over respondents; PDF_PAGE_5: per-question tables; no multilevel model. | 说明了预测/平均所在层级（respondent × question × paraphrase），但未显式建模嵌套结构或用多层模型分离 respondent/question 方差。 |
| G2 | 随机效应 | NA | PDF_PAGE_3: expected value over population via Monte Carlo sampling; no random-effect structure. | 统计模型不是混合模型，也没有报告随机效应；论文以 Monte Carlo 平均和标准误作描述性推断，未提出需要随机截距/斜率的模型。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_1: seven different attitude statements; PDF_PAGE_5: per-question results; PDF_PAGE_9: future work on other probing methods; no item random effect. | 7 个目标题被视为固定题集，分析按题报告但未把题目作为随机效应；对材料总体的推广有限，不过论文报告了逐题结果并承认局限。 |
| G4 | 统计功效 | 0 | PDF_PAGE_5: ±SE; PDF_PAGE_7: r and p; no a priori power analysis or sample-size justification. | 没有设计阶段功效分析或样本量/重复次数论证；因此未达到基本要件。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_12 Appendix A: neutral answers discarded; PDF_PAGE_5: all seven target questions reported; no stopping rule or sample-size justification. | 报告了部分排除规则与全部主要题目/条件，但未说明样本量决定、停止规则，也未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement in the full text. | 全文没有公开预注册、注册编号或分析计划；属于无预注册而非信息不足。 |
| J1 | 位置偏差 | NA | — | 研究不是多候选项选择、排序或 LLM-as-judge 成对比较；虽然 in-context 示例顺序被消融，但由 E1 处理。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评价开放生成质量，因此无生成长度偏差问题。 |
| J3 | 谄媚 | NA | — | 没有操纵用户先验立场、反馈或纠错；任务是给定人类问卷回答后预测下一答案，非谄媚对话评估。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 评估模型输出，故无自我偏好/同源裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF_PAGE_3-4: 60 in-context question-answer pairs from a respondent; Figure 2; PDF_PAGE_14-15: order and length ablations; PDF_PAGE_20-21: full question list. | 报告了示例来源、数量和使用方式，并做了顺序/长度消融；但未系统报告每类标签比例、多 seed 示例集重采样或排列反平衡的完整设计。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_3-4 and PDF_PAGE_12 Appendix B: prompt templates; PDF_PAGE_12 Appendix C: 50 paraphrases; PDF_PAGE_9: other prompt aspects not varied. | 提供了完整 prompt 模板并做了 target-question paraphrase 敏感性分析；但没有 prompt 版本号/迭代日期、dev/test 划分或对其他 prompt 格式的系统消融。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | PDF_PAGE_4: 60 in-context examples; PDF_PAGE_14-15: order and length ablation; PDF_PAGE_6: last-example position strongly influences output. | 有长上下文/顺序/长度操纵并报告位置效应；但没有报告实际 token 数，也没有完整的首/中/尾位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_9: temperature 1 and top-10 tokens; PDF_PAGE_12: paraphrase generation with temperature 1.0 and different seeds; PDF_PAGE_13: model snapshots. | 报告了主要采样设置和部分模型 snapshot；但未完整报告 top-p/top-k、主实验随机种子、每条件重复采样 N 及 bootstrap CI。 |
| J9 | 重复与文本退化 | NA | — | 任务输出为短 yes/no 概率，不涉及开放生成或重复退化问题。 |
| J10 | 分词效应 | NA | — | 仅使用英文问卷，无跨语言/跨脚本比较（PDF_PAGE_12: only English version）。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_3: 2023 Smartvote questionnaire; PDF_PAGE_13: model snapshots; no train-test overlap or contamination check. | 未报告测试集发布日期与模型训练截止日期的对照，也未做污染检测或污染率估计。 |
| J12 | 基准饱和 | 0.5 | PDF_PAGE_5 Table 3: personalization accuracies up to 95%; no saturation discussion or continuous alternative. | 报告了分数量程与较高水位，但未讨论接近天花板时改用连续指标/更难子集或 bootstrap CI 比较。 |
| J13 | 指令遵循 | NA | — | 主要因变量不是指令遵循；虽然 prompt 要求 yes/no，但论文没有按约束类型测量指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF_PAGE_3: sums case variants of yes/no; PDF_PAGE_4: top-10 tokens; p.6 notes zero-shot base models may not yield yes/no. | 任务要求 yes/no 短格式，论文报告了概率求和与 top-10 截断，但未报告格式合法率或重试/后处理规则。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF_PAGE_1: 'political biases'; PDF_PAGE_3: compares model predictions to human population; PDF_PAGE_8-9: interprets bias as contextual rather than inherent. | 论文将 LLM bias 操作化为相对人类问卷分布的偏离，并讨论其情境性；但没有系统做 LLM 构念与人类政治态度构念的异同论证或人类同范式对照实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文比较了 8B/70B/405B 的趋势，但未宣称 '涌现/突变'，也未以规模曲线讨论涌现争议。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标的优化/训练/奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_13: model links and gpt-3.5-turbo-0125; PDF_PAGE_5: ±SE; PDF_PAGE_1: data and code publicly available; no paired tests. | 提供了模型 snapshot/链接、部分标准误和数据代码；但没有逐分数重复 N 与 95% CI、配对 bootstrap/McNemar 或原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 虽然 prompt 含 60 个历史对话轮作为 in-context examples，但每个目标题只做一次最终预测，不评估多轮对话中的一致性衰减。 |

## 编码小结
论文提出了较完整、可复现的 QM 任务与 bias/PA 指标，报告了模型比较、paraphrase 稳定性、random context 基线和 in-context 顺序/长度消融；但整体属于观察性 LLM 评测而非人类实验，缺少正式预注册、功效分析、混合效应/项目随机效应模型、污染检查以及多种实验设计组件。对 LLM 特有风险，较充分报告了 prompt 模板和 few-shot/顺序敏感性，但采样种子、格式合法率、污染与配对检验仍不完整。
