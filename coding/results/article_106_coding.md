# article_106 | Temperature-scaling surprisal estimates improve fit to human reading times – but does it do so for the “right reasons”? | 2024

研究类型概述：计算心理语言学/语料库建模研究，不招募新的人类被试；使用三个既有英语阅读时间语料库（Dundee、Natural Stories、Brown），把不同规模 GPT-2 的 surprisal 以及温度缩放后的 surprisal 作为预测变量，用线性混合效应模型拟合阅读时间。分析单位为词/词元观测，嵌套于被试与文章；主要比较温度条件、模型规模及词类/命名实体/多 subword token 等语言属性。
- **研究构念（Construct）**：语言预测、surprisal与人类阅读加工难度｜CA 构念锚定：词汇通达（lexical access, `trm_4a3fd79d0b80f`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）；阅读（reading, `trm_4a3fd79d0aeb6`）
- **实验任务与范式（Task / Paradigm）**：计算心理语言学/语料库建模研究，不招募新的人类被试；使用三个既有英语阅读时间语料库（Dundee、Natural Stories、Brown），把不同规模 GPT-2 的 surprisal 以及温度缩放后的 surprisal 作为预测变量，用线性混合效应模型拟合阅读时间。分析单位为词/词元观测，嵌套于被试与文章；主要比较温度条件、模型规模及词类/命名实体/多 subword token 等语言属性。｜CA 任务锚定：阅读广度任务（reading span task, `trm_4c40d168898db`）；句图匹配任务（sentence-picture matching task, `trm_4f241e8a01052`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.4: We take four variants of pretrained GPT-2 (small, medium, large, xl); We scale T in the range of [1, 10]; p.3 Eq.5 gives the temperature-scaling formula. | 温度与模型规模有明确条件和水平，但无被试/单位分配或随机化说明，也无操纵检验；按计算条件比较判0.5。 |
| A2 | 因变量 | 0.5 | PDF p.4 Eq.7 defines Δllh as llh(target)-llh(base); p.3 Eq.2-4 define ECE/CECE/HCE; p.14 Appendix C gives RT exclusion rules. | 因变量指标与计分方式清楚，并报告了部分 RT 预处理；但未报告测量信效度，连续指标分布/端点处理也有限，判0.5。 |
| A3 | 控制变量 | 1 | PDF p.14 Eq.30-31 explicitly include freq, length, freq_prev_1, length_prev_1 and random intercepts (1&#124;article)+(1&#124;subj_id); Appendix C details corpus exclusions. | 方法/公式中系统列出了主要控制变量及其进入模型的方式，包含词频、词长、前词变量和随机截距，满足控制变量报告要求。 |
| A4 | 混淆变量 | 1 | PDF p.8 says the beneficial effect might be an artifact of subword tokenization; p.16 Appendix I removes interactions/adds random slopes and examines predictor correlations. | 识别并分析了多个潜在混淆/替代解释（词类、命名实体、subword tokenization、预测变量相关），并报告了残余不确定性（需重训词表才能完全检验），判1。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量理论模型，也未做正式交互项检验和简单斜率分析；词类/NE/多token属机制性亚组分析，不作为调节模型编码。 |
| A6 | 中介变量 | NA | — | 无中介假设、中介变量或直接/间接效应分解，不适用。 |
| A7 | 操作性定义 | 1 | PDF p.2 Eq.1 defines surprisal; p.3 Eq.5-6 define temperature-scaled surprisal; p.4 Eq.7 defines Δllh and p.14 Eq.30-31 give the LME models. | 关键构念均有可复现的公式和计算程序，包括 surprisal、温度缩放、拟合指标和混合模型，判1。 |
| A8 | 水平数与类型 | 0.5 | PDF p.4 lists GPT-2 small/medium/large/xl; p.14 Appendix D lists T values from [1.0,1.1,...,10.0]; corpora are Dundee, Natural Stories and Brown. | 报告了模型规模、温度网格和语料水平/取值，但未系统说明所有变量的类型（连续/等级/名义）、间距/全距及中心化处理，判0.5。 |
| A9 | 单一操作化的风险 | 1 | PDF p.4 uses four GPT-2 variants; p.1/p.5 analyze 3 corpora × 4 LMs; p.5 Table 1 and p.16 Appendix I compare multiple metrics and analyses. | 关键构念采用多种模型、多个语料和多种指标（Δllh、ΔMSE、ECE/CECE/HCE）进行会聚性检验，满足多操作化要求。 |
| A10 | 单一方法的风险 | NA | — | 自变量为模型概率/温度条件，因变量为人类阅读时间与校准指标，来源天然不同；无自陈式共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试分组，也无独立被试组承担不同条件；计算条件比较不适用被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试重复测量或条件顺序设计；模型/温度比较是确定性计算，不适用被试内顺序平衡。 |
| B3 | 混合设计 | NA | — | 没有组间/组内人类因素的混合设计，不适用。 |
| B4 | 因子设计 | NA | — | 虽交叉 3 语料 × 4 模型 × 温度网格，但不是随机分配的人类因子实验，也未做 ANOVA 主效应/交互，不能按实验因子设计编码。 |
| B5 | 主效应 | NA | — | 无因子实验中的主效应检验，不适用。 |
| B6 | 交互作用 | NA | — | 无正式交互项检验、简单主效应或交互图误差棒，不适用实验因子设计编码。 |
| B7 | 区组设计 | NA | — | 没有实验区组/分层分配程序；随机效应文章/被试不等同于实验区组设计。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计，不适用。 |
| B9 | 准实验设计 | NA | — | 无人类准实验分组或非随机分配处理；不适用准实验设计组件。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理条件，不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 单一观察/计算评估，无被试或分析单位的随机分配问题。 |
| C2 | 平衡 | NA | — | 无实验条件顺序需要平衡，不适用。 |
| C3 | 恒定 | 0.5 | PDF p.4 uses four variants of pretrained GPT-2 and three fixed corpora; p.9 Limitations discusses only manual T tuning and nonlinearity, not external-validity boundaries of model/corpus choice. | 模型族、语料和预处理相对固定，但未系统列出所有恒定变量及其水平，也未讨论其对模型/语言外部效度的限制，判0.5。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后分配程序，不适用。 |
| C5 | 纳入为变量 | 0.5 | PDF p.14 Eq.30-31 include baseline covariates freq/length and random intercepts; p.16 Appendix I examines predictor correlations and random slopes. | 已知混淆/协变量被纳入 LME，但未报告回归斜率齐性检验或调整后效应量，判0.5。 |
| C6 | 盲法 | NA | — | 没有人类被试、主试或人工评分者的盲法安排；自动化计算不适用。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级需要报告，不适用。 |
| D1 | 练习效应 | NA | — | 无新人类学习/练习阶段；模型计算不受练习效应影响。 |
| D2 | 疲劳效应 | NA | — | 无人类 session、休息或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件人类残留/清洗期；同一词在不同 T 下的计算相互独立。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件迁移或不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为阅读时间/模型拟合指标，不是主观量表评分，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 自然语料词序固定，无实验刺激顺序随机化/反平衡，也不是多选项单次作答设计；前文词通过 surprisal_prev 等建模。不适用。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分或跨群体反应风格比较，不适用。 |
| E4 | 需求特征 | NA | — | 无新人类被试、指导语或需求特征；不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.14 Appendix C removes reading times <100ms or >3000ms; Tables 1-2 report fit/calibration values but not skew or endpoint frequencies. | 对 RT 端点做了剔除规则，部分处理了地板/天花板风险；但未报告主要因变量分布形态、偏度或端点频率，判0.5。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量；自变量与因变量来源不同，不适用共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | PDF p.5 Table 1 reports Δllh and percent improvement; p.17 Table 8 reports p<0.001 for GPT2 small; no confidence intervals or power analysis appear. | 报告了效应量型指标（Δllh）和部分显著性，但缺样本量依据/功效分析、置信区间及多重性校正，判0.5。 |
| F2 | 内部效度 | NA | — | 无人类随机分配、分配隐藏、基线等价或被试损耗；研究是语料库/模型拟合比较，不适用内部效度分配组件。 |
| F3 | 构念效度 | 0.5 | PDF p.2-3 define surprisal and calibration metrics; p.5/p.16 compare multiple metrics, corpora and model variants; no formal reliability coefficients are reported. | 构念定义和多操作化论证较充分，但未报告测量信度/效度统计或操纵检验，判0.5。 |
| F4 | 外部效度 | 0.5 | PDF p.4 names Dundee, Natural Stories and Brown as three English corpora; p.5/p.8 discuss cross-corpus consistency but not detailed sample representativeness or broad boundary conditions. | 报告了语料来源并做了跨语料重复，但未系统说明被试人口学/代表性及向其他语言、文本类型推广的边界，判0.5。 |
| G1 | 分析单位 | 0.5 | PDF p.14 Eq.30-31 model word-level RT with random intercepts (1&#124;article)+(1&#124;subj_id); p.16 Appendix I adds a random slope for subject. | 分析层级为词观测并嵌套于被试/文章，LME 已分离部分聚集方差；但无处理分配层级（本身无分配）且未明确讨论 assignment-analysis 匹配，判0.5。 |
| G2 | 随机效应 | 1 | PDF p.14 Eq.30-31 explicitly report random intercepts for article and subject; p.16 Eq.33 reports (surprisal&#124;subj_id) random slope. | 明确报告了随机效应因子与随机截距/随机斜率结构，固定效应也有列出，判1。 |
| G3 | 材料作为随机效应 | 0.5 | PDF p.14 Eq.30-31 include (1&#124;article)+(1&#124;subj_id) but no (1&#124;word/item) or word-level random effect. | 文章作为材料随机截距被纳入，但词项/项目未作为随机效应，结论向材料/词项总体推广只部分体现，判0.5。 |
| G4 | 统计功效 | 0 | PDF p.4-p.5 describe corpora and analyses but report no a priori power analysis or sample-size rationale; Table 1/Table 8 give Δllh and p-values without CIs. | 无事前功效分析、无样本量/重复次数推导，结果也缺置信区间，判0。 |
| G5 | 研究者自由度 | 0.5 | PDF p.14 Appendix C reports RT exclusions; p.5 reports all 12 corpus-by-model settings and Appendix I/L add many analyses; p.9 admits T was manually tuned. | 报告了剔除规则、主要语料/模型和多项补充分析，但手动调 T、未区分验证性与探索性分析，也无停止/样本量决定披露，判0.5。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or pre-specified analysis plan appears in the paper; only a code link is given on p.1. | 无预注册，按编码口径记0。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM 多候选项选择、排序或 LLM-as-judge 成对比较，无位置偏差风险。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估生成质量，不涉及生成答案长度与质量混淆。 |
| J3 | 谄媚 | NA | — | 无用户立场、反馈或纠错对话，不涉及谄媚/附和偏差。 |
| J4 | 自我偏好 | NA | — | 没有 LLM 裁判或被评模型间的自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 方法为零样本概率估计，无 few-shot in-context examples，不适用。 |
| J6 | 提示敏感性 / 脆弱性 | NA | — | 没有自定义 prompt 模板或提示工程；直接计算语料中目标词在上下文下的模型概率，不适用 prompt 敏感性组件。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 使用常规阅读语料的短上下文概率估计，无长上下文/RAG 或关键信息位置操纵。 |
| J8 | 温度与采样随机性 | NA | — | 这里的 temperature 是校准/softmax 缩放参数，不是生成解码采样温度；无随机采样、seed 或重复采样问题。 |
| J9 | 重复与文本退化 | NA | — | 不涉及开放文本生成或解码重复/退化，只计算词概率，不适用。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本英语研究，不涉及跨语言/跨脚本 token 数混淆；subword tokenization 是本文实质分析对象（Section 6.3），不是 J10 的跨语言风险。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.4 says four variants of pretrained GPT-2 were used; p.4 lists public reading corpora including Brown/Natural Stories/Dundee; no training cutoff or overlap/contamination analysis is reported. | 公开阅读语料可能存在于预训练数据中，且未报告 GPT-2 训练数据截止日期或污染检测；测试材料污染风险实际存在，判0。 |
| J12 | 基准饱和 | NA | — | 不是准确率型基准且未接近上限；主要指标为连续 Δllh/ΔMSE，无基准饱和问题。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，无约束指令或可机器判定遵循标准。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化输出或 JSON/文法约束，不适用。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全性、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | LLM 未被当作心理学被试；它是估计词概率的模型工具，研究比较模型 surprisal 与人类阅读时间，不主张在 LLM 上测量人类同名心理构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未宣称涌现能力或突变；模型规模曲线用连续 Δllh 描述，且无多 seed 涌现检验，不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无奖励模型/LLM-judge/基准代理优化流程；T 手动调参属于研究者自由度问题，而不是对代理指标的奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | PDF p.5 Table 1 and p.17 Table 8 report single Δllh values and p-values; p.4 only names GPT-2 small/medium/large/xl without exact snapshot; no N, CI, or paired test is reported. | 只有单点模型评估，无重复次数、置信区间、精确 snapshot 或配对比较；虽提供代码，仍未满足可复现评估报告要件，判0。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究为单轮/静态语料概率估计，无多轮对话历史或一致性衰减问题。 |

## 编码小结
论文对 surprisal、温度缩放、校准误差和阅读时间拟合指标的操作化较清楚，预处理与 LME 公式也有报告；主要不足是：无预注册、无事前功效分析、多数结果为单点估计且缺置信区间，模型 snapshot/训练截止日期与测试材料污染未报告，材料/词项随机效应不足，最优温度在评估语料上手动调参。大量人类实验设计组件因无新人类被试分配而记 NA。
