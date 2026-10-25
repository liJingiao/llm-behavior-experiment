# article_041 | Decoupling Metacognition from Cognition: A Framework for Quantifying Metacognitive Ability in LLMs | 2025

研究类型概述：方法学/基准评估研究：提出 DMC 框架，用 LLM-SDT 与 LLM-Meta-SDT 从失败预测表现中分离认知能力与元认知能力；在 8 个数据集、5 类任务、3 个 LLM、6 种置信度引出方法上进行评估。分析单位为模型-数据集-置信度引出方法聚合后的 LLM 输出，而非人类被试实验。
- **研究构念（Construct）**：独立于认知表现的元认知敏感性（metacognitive sensitivity separated from cognitive task performance）｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：方法学/基准评估研究：提出 DMC 框架，用 LLM-SDT 与 LLM-Meta-SDT 从失败预测表现中分离认知能力与元认知能力；在 8 个数据集、5 类任务、3 个 LLM、6 种置信度引出方法上进行评估。分析单位为模型-数据集-置信度引出方法聚合后的 LLM 输出，而非人类被试实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'We use two popular types ... Verbalized including Vanilla, Cot and Top-k ... Consistency-based including Self Random, Perturbing and Misleading'; 'three popularly-used LLMs: LLaMA2-70B, GPT-3.5, and GPT-4'. | 明确命名了置信度引出方法与模型水平，但未完整报告各方法的提示词、具体操纵程序、单位分配方式或操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.5 eq.27: 'MC_Mce = d*/d'; p.6: calibration metrics including ECE, AUROC, BS and CV comparison. | 因变量指标与计分公式明确，但未报告信度、效度证据，也未说明连续指标预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | p.6: 'The default sampling temperature is set to 0.1, while 0.7 is employed when multiple runs are necessary'; p.6 option-order swapping. | 报告了温度与选项顺序等控制，但未系统列出全部控制变量及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p.2: calibration-based metrics 'conflating the impact of cognitive ability'; p.6: swapping option order 'to eliminate biases introduced by the order of options'. | 识别了认知能力耦合与选项顺序两个潜在混淆，并用 DMC/交换顺序处理；但未报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 理论模型不包含调节变量，也未提出调节假设与交互检验。 |
| A6 | 中介变量 | NA | — | 理论模型不包含中介变量，未做直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p.4-5: failure-prediction matrix P_Mce, CP_Mce, LLM-SDT parameter recovery eqs.15-16, LLM-Meta-SDT fitting constraints eqs.17-27. | 元认知与认知构念有明确数学操作化，但置信度引出的提示程序和分箱细节未完整给出，复现仍依赖外部代码。 |
| A8 | 水平数与类型 | 0.5 | p.6: eight datasets, six confidence elicitation methods, three LLMs; Tables 2-3 list labels. | 报告了各因素水平数与标签，但未说明水平类型、间距/全距或连续变量中心化处理。 |
| A9 | 单一操作化的风险 | 0.5 | p.6-7: six CEMs and eight datasets produce different DMC values; no convergent validity across operationalizations is reported. | 使用多种置信度引出方式与多数据集，但未报告不同操作化之间的会聚证据，也未讨论单一 DMC 操作化的推广限制。 |
| A10 | 单一方法的风险 | 0 | p.4: same LLM M produces both answer and confidence; p.6 no common-method bias check. | 自变量相关输出与因变量均来自同一 LLM 生成流程，未报告任何共同方法偏差程序控制或统计检验。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立组分配；LLM 条件不是被试间设计。 |
| B2 | 被试内设计 | NA | — | 未采用需要顺序平衡的同一被试跨条件重复测量设计；同一模型跨条件调用是独立 API 调用，未报告条件顺序处理。 |
| B3 | 混合设计 | NA | — | 没有明确的混合设计及组间/组内因素统计模型。 |
| B4 | 因子设计 | 0 | p.6-7: Tables 2-3 report cell means for CEMs, datasets and models, but no design matrix sample sizes, ANOVA, or interaction statistics. | 存在多因素基准网格，但未作为因子设计报告交互项或完整设计矩阵。 |
| B5 | 主效应 | 0 | p.7: Tables 2-3 report average DMC scores by CEM/model; no F, df, p, or effect size for main effects. | 仅报告描述性均值，未报告主效应统计检验。 |
| B6 | 交互作用 | 0 | p.7: model/CEM differences are described descriptively; no interaction test. | 多因素条件间可能存在交互，但论文完全未报告交互项检验。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；未作因果效应估计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理顺序设计，不涉及可逆性/迁移对称性。 |
| C1 | 随机化 | NA | — | 无随机分配或分配隐藏机制；研究为基准比较而非随机实验。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需平衡。 |
| C3 | 恒定 | 0.5 | p.6: default temperature 0.1, 0.7 for multiple runs; model versions named but no full constancy list. | 报告了温度等部分恒定条件，但未系统列出所有恒定变量及其水平，也未讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.2 and p.5: cognitive ability is separated and used to compute d*/d; not included as ANCOVA covariate. | 认知能力作为关键混淆在模型中被显式测量与去耦合，但未按协变量/区组分析报告斜率齐性等假设。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或评分者，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM API 调用为独立会话，无练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类疲劳效应或 session 时长问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件间无跨时间残留迁移；未使用需要清洗期的交叉设计。 |
| D4 | 不对称迁移 | NA | — | 无跨条件残留，不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 不使用人类主观量表校准；置信度分箱不是李克特式量表范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 1 | p.6: 'to eliminate biases introduced by the order of options, we also create new questions by swapping the order of options for each binary choice problem'. | 对每个二选一题同时创建正反两种选项顺序，选项位置被完全反平衡。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分题问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，需求特征不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集自动化，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0 | p.7: Tables 2-3 report only mean DMC values; no SD, skewness, endpoint frequencies, or pilot difficulty calibration. | 仅报告均值，无法评估天花板/地板效应，也未说明任务难度校准。 |
| E7 | 共同方法偏差 | 0 | p.4: answer and confidence come from the same LLM; no common-method bias control or test. | 关键测量同源，但未做共同方法偏差程序控制或统计检验。 |
| F1 | 统计结论效度 | 0 | p.7: results are descriptive means/CV; no effect sizes, confidence intervals, sample-size justification, or multiplicity correction. | 缺少效应量/CI 与推断统计，仅报告描述性比较。 |
| F2 | 内部效度 | NA | — | 非随机分配实验，也无因果效应估计；不适用分配隐藏/被试流向评估。 |
| F3 | 构念效度 | 0.5 | p.2: SDT-based theoretical rationale; p.7 RQ4 shows DMC metacognition aligns with AbstainQA performance. | 提供了理论构念论证与一定收敛效度证据，但未报告信度、正式效度检验或操纵检验。 |
| F4 | 外部效度 | 0.5 | p.6: eight datasets across five task types and three LLMs; no explicit sampling frame or generalization boundaries. | 报告了数据集与模型来源/覆盖，但未明确推广边界或跨情境复现实验。 |
| G1 | 分析单位 | 0.5 | p.4: O = [y_hat, y, rating] at question level; p.6-7 analyses aggregate across datasets to produce dataset-level DMC. | 提及了数据集与模型层级，但未说明题目嵌套于数据集的处理，分析主要基于聚合表。 |
| G2 | 随机效应 | NA | — | 仅比较三个固定模型，未建立混合模型或随机效应结构，也未主张抽样模型总体推断。 |
| G3 | 材料作为随机效应 | 0 | p.4: item-level counts T_Ai/F_Ai etc. are aggregated; p.6 binary-choice questions used as materials; no item random effect. | 题目作为有限材料被固定处理，仅做聚合分析，未考虑材料/项目随机效应，存在向任意题目推广的限制。 |
| G4 | 统计功效 | 0 | p.6-7: no power analysis or sample-size/repetition rationale; no effect sizes or CIs. | 无事前功效分析或样本量论证，结果仅报描述统计。 |
| G5 | 研究者自由度 | 0.5 | p.6: all eight datasets and six CEMs in Table 2; p.7: only three representative CEMs selected for RQ3; no exclusion rules or per-dataset N. | 报告了大部分条件，但未说明数据排除规则、每数据集样本量或分析选择自由度。 |
| G6 | 预先设定 / 预注册 | 0 | p.6-7: no preregistration or pre-specified analysis plan is reported. | 无公开预注册，也未区分验证性与探索性分析。 |
| J1 | 位置偏差 | 0.5 | p.6: option order is swapped for each binary-choice problem to eliminate order bias. | 明确做了选项位置反平衡，但未报告交换前后翻转率、位置×正确率曲线或完整裁判/提示版本信息。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 对开放式生成质量做长短比较。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错式对话操纵，不涉及谄媚。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 评估模型输出，无自我偏好风险。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 未使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p.6: CEMs are named and cited, but full prompt templates, version dates, sensitivity ablations, and dev/test separation are not reported. | 未提供完整提示模板与版本化/敏感性分析，提示工程自由度未受控。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文或 RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'default sampling temperature is set to 0.1, while 0.7 is employed when multiple runs are necessary'. | 报告了 temperature，但未报告 top-p/top-k/seed、重复运行次数或置信区间。 |
| J9 | 重复与文本退化 | NA | — | 主要任务为二选一答案与置信度输出，不涉及开放式长文本退化评估。 |
| J10 | 分词效应 | NA | — | 单语言英文基准，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.6: public benchmarks include SAT/AGIEval, MMLU, Big-Bench-Hard, CommonsenseQA; no training cutoff or contamination check is reported. | 使用公开基准但未评估测试集污染或训练数据重叠，无法区分记忆与泛化。 |
| J12 | 基准饱和 | 0 | p.6-7: only metacognitive DMC scores are reported; no benchmark accuracy, SOTA position, or saturation assessment. | 未报告所用基准的分数量程与当前水位，也未评估饱和问题。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，无约束指令准确率测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 未使用 JSON/grammar 等结构化输出实验，也未报告格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1-2: draws on human metacognition and confidence literature; p.6: compares three LLMs but no human same-paradigm data or exact model snapshots. | 明确把 LLM 的元认知与人类同名构念作理论类比，但未报告精确权重/API 快照，也未做人类对照实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模或训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及以代理指标为优化目标的训练/RL/best-of-N 优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.1: code link only; p.6: temperature given, but no repeat N, confidence intervals, exact API dates/snapshots, or paired tests. | 评估可复现性报告不足，缺少重复次数、CI、精确模型 snapshot 与配对比较。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮，无对话历史累积。 |

## 编码小结
论文核心贡献是提出并验证一个可计算的元认知量化框架，给出了较完整的数学模型和跨数据集/跨模型比较；但作为心理学式实验报告，许多操纵程序、信效度、随机化/顺序控制、采样重复与不确定性报告不足。编码时对 LLM 条件比较保留适用性，但对人类被试特有的分配与顺序设计多记为 NA。
