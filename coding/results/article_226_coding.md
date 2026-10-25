# article_226 | Leveraging Large Language Models for Multiple Choice Question Answering | 2023

研究类型概述：LLM 基准评测与提示策略比较研究：在 20 个多项选择问答数据集上比较 cloze prompting（CP）与 multiple choice prompting（MCP），并考察不同 CP 归一化、zero/one/few-shot、答案顺序扰动以及多模型的多项选择符号绑定（MCSB/PPA）。分析单位为题目/模型调用，而非人类被试。
- **研究构念（Construct）**：多项选择符号绑定、选项顺序不变性与反应映射｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：在多个现成LLM和20余个数据集上重排答案选项与符号，测量符号绑定，并比较cloze prompting和显式multiple-choice prompting。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5 §5.1: 'We evaluate 5-shot model performance...'; p.7 §5.4: 'Our prompt phrasing is consistent across tasks'; p.8 Table 2 lists CP/MCP × zero/one/few. | 自变量被明确命名：CP vs MCP、Raw/LN/UN、zero/one/few-shot；但未报告正式操纵检验，分配/顺序处理也不完整，因此为部分满足。 |
| A2 | 因变量 | 0.5 | p.8 Table 2 reports 'accuracy'; p.4 defines PPA as 'the proportion of orderings that chose the plurality answer among all orderings'. | 因变量指标与计分方式明确（accuracy、PPA），但未报告信度/效度证据，也未说明连续指标预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | p.7 §5.4: 'Our prompt phrasing is consistent across tasks'; 'K is always chosen to be as high as possible while respecting Codex’s 4,000 token context limit'; p.10 mentions 'the single random seed'. | 报告了若干控制做法（统一提示格式、模型、随机种子、尽量不调 K），但未系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p.7 §5.3 discusses dataset leakage and says 'we were not able to acquire the GPT-3 training data to perform a manual collision check'; shuffling checks are in Appendix C. | 识别并讨论了数据泄漏、答案顺序等潜在混淆，给出若干间接控制与残余不确定性；但未做系统敏感性分析或量化残留混淆。 |
| A5 | 调节变量 | 0 | p.1 Abstract: MCSB ability 'varies greatly by model'; p.5 §5.1 asks whether higher MCSB leads to higher accuracy; Table 1 compares models descriptively. | 论文有类似调节/边界条件的理论主张（MCSB 能力影响 MCP 收益），但未做正式交互检验，只分别比较模型表现；按编码规则记 0。 |
| A6 | 中介变量 | NA | — | 研究不包含中介变量或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | p.3 defines CP and MCP; p.4 defines PPA; p.16–p.21 give prompt examples; p.10 gives code link. | 关键构念的操作化程序清楚：提示如何构造、答案如何评分、PPA 如何计算，且提供代码与示例，足以复现。 |
| A8 | 水平数与类型 | 0.5 | p.8 Table 2 reports N (answer options) and K (exemplars); p.3 names Raw/LN/UN; p.5 describes 5-shot setting. | 报告了水平数与各水平标签；但未系统说明水平类型、间距/全距或连续变量的中心化/标准化，K 也随数据集变化。 |
| A9 | 单一操作化的风险 | 0.5 | p.4 defines PPA as MCSB measure; p.8 reports downstream accuracy across 20 datasets. | MCSB 主要用 PPA 单一指标操作化，accuracy 是下游任务表现而非 MCSB 的正式会聚指标；论文未报告会聚证据，也未在局限中充分讨论单一操作化限制。 |
| A10 | 单一方法的风险 | NA | — | 这是客观 LLM 任务评测，不涉及人类自评/同源自陈量表，共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试组间分配；同一模型/题目在多个提示条件下评估，不属于人类被试间设计。 |
| B2 | 被试内设计 | NA | — | 虽对同一批题目比较不同提示条件，但为独立 API 调用，没有人类被试内顺序设计或顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合的人类被试设计。 |
| B4 | 因子设计 | 0 | p.8 Table 2 presents CP/MCP × zero/one/few across datasets, but no interaction term or factorial statistical model is reported. | 存在多因素交叉的评测矩阵，但完全未报告交互项检验或相应统计量，不满足因子设计基本要件。 |
| B5 | 主效应 | 0 | p.8 §6 reports mean gaps (e.g., '8.3, 12.2, and 9.7 percentage points') but no formal main-effect F/df/p. | 仅报告描述性均值差异，未报告主效应的统计检验结果。 |
| B6 | 交互作用 | 0 | p.8 Table 2 and §6 compare conditions descriptively; no interaction F/df/p or simple-effects tests. | 未对交互作用做统计检验，也未报告简单主效应或图示误差棒。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有采用拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；模型比较也不是非随机分组因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理的可逆性/迁移对称性设计。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥条件的程序；同一题目在多个条件上评估，主要随机化出现在答案顺序扰动与示例抽样。 |
| C2 | 平衡 | NA | — | 无人类被试条件顺序，无需条件顺序平衡。 |
| C3 | 恒定 | 0.5 | p.7 §5.4: 'Our prompt phrasing is consistent across tasks'; p.10: 'single random seed'; model choice constrained to Codex. | 报告了一些恒定控制（提示格式、模型、随机种子），但未系统列出恒定变量水平及外部效度限制。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未把混淆变量作为协变量/区组纳入统计模型；本题不适用。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者盲法需求；评测自动完成。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 每个提示是独立 API 调用，无跨试次学习/练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题；任务是自动评测。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM 调用独立、无跨条件上下文累积，迁移/清洗期不适用。 |
| D4 | 不对称迁移 | NA | — | 无跨条件残留迁移。 |
| D5 | 范围效应 | NA | — | 因变量为客观 accuracy/PPA，不是量表式绝对判断，无范围效应。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.4 PPA uses all n! answer orderings; p.23 Table 4 reports 'Strong shuffle'; p.10 mentions a single random seed. | 对答案顺序做了系统考察/强随机化并报告 shuffle 结果，但未报告主表中每位置出现次数、顺序分配细节，主实验也以数据集原顺序为主。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，需求特征不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0 | p.8 Table 2 reports only accuracy means (e.g., COPA 100.0, StoryCloze 98.5), with no SD, skew, endpoint frequencies, or ceiling/floor discussion. | accuracy 是有界指标且部分数据集接近上限，但未报告分布形态或端点频率，也未讨论天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | IV 为提示条件、DV 为客观任务 accuracy/PPA，不属于同源自评共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | p.8 §6 reports average gaps ('9.7 percentage points') but no confidence intervals, power analysis, or multiple-comparison correction. | 报告了描述性差异，可作为粗略效应量；但缺少 CI、样本量依据、正式统计检验与多重性校正。 |
| F2 | 内部效度 | 0.5 | p.7 §5.3 addresses dataset leakage; p.10 gives code and a single random seed; no formal allocation/concealment or baseline equivalence. | 对数据泄漏和提示公平性做了内部效度讨论，但无人类随机分配/分配隐藏/基线等价性检验。 |
| F3 | 构念效度 | 0.5 | p.4 defines PPA as order-invariance measure; p.5 compares PPA across models; no reliability or formal validity evidence is reported. | 对 MCSB 构念与 PPA 指标关系有论证，但缺少信度、正式效度证据或操纵检验统计。 |
| F4 | 外部效度 | 0.5 | p.6–p.7 describe 20 diverse datasets; p.9 concludes broad promise for foundation models. | 样本/数据集来源与多样性有报告，但未明确抽样代表性、推广边界及跨样本复现结果。 |
| G1 | 分析单位 | 0.5 | p.5: 'We randomly sample 100 instances' / '500 instances'; p.8 Table 2 aggregates accuracy by dataset; no multilevel model. | 题目/数据集层级可推断，但未明确说明分配层级、分析层级匹配或嵌套结构处理。 |
| G2 | 随机效应 | NA | — | 无人类被试随机效应；模型作为固定评测对象比较，未使用混合模型，且不涉及把模型样本推广到随机模型总体。 |
| G3 | 材料作为随机效应 | 0.5 | p.5 random sampling of OpenBookQA/StoryCloze/RACE-m; p.6 20 datasets; no item-level random effect or mixed model. | 使用了多个数据集与题目抽样，具备材料抽样的意味，但分析未把题目/材料作为随机效应，结论仍按固定材料报告。 |
| G4 | 统计功效 | 0 | p.8 reports point accuracy and mean gaps; no a priori power analysis or confidence intervals. | 无设计阶段功效分析或样本量论证，结果亦无 CI；按规则记 0。 |
| G5 | 研究者自由度 | 0.5 | p.5 reports downsampling to 100/500; p.8 Table 2 notes some values not computed; p.10 gives code/seed. | 多数数据集、条件和缺失值有报告，但缺少完整排除规则、样本量决定方式及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No pre-registration statement appears in the paper; only a reproducibility statement with code and a single seed is given on p.10. | 无公开预注册或分析计划登记。 |
| J1 | 位置偏差 | 0.5 | p.4 PPA enumerates all n! orderings; p.23 Table 4 reports strong-shuffle results; p.10 mentions a single random seed. | 识别并系统测量了答案顺序敏感性，也做了强 shuffle；但未报告交换前后偏好翻转率/各位置正确率，也未报告采样参数与评分 prompt 版本。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放生成质量，不存在长度冗长偏差。 |
| J3 | 谄媚 | NA | — | 无用户先验立场/反馈式对话操纵，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 的自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.7: 'K is always chosen to be as high as possible'; p.10: 'single random seed we use for selection of few-shot exemplars'; Appendix A gives prompt examples. | 报告了 few-shot 数量与随机抽样种子，但未报告各类标签比例、示例排列反平衡、多 seed 重采样或完整 few-shot 模板。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.7 §5.4 describes consistent prompt phrasing; p.16–p.21 provide examples; p.10 links code. | 提供了提示示例与可复现代码，但未给出版本号、敏感性消融、dev/test 划分或 prompt 调优过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文受 4000 token 限制，未研究长上下文/RAG 信息位置效应。 |
| J8 | 温度与采样随机性 | 0 | p.10 reports only a single random seed for exemplars/shuffling/corruptions; no temperature, top-p, or repeated sampling details. | 未报告解码采样超参、模型采样种子、重复运行次数或方差估计。 |
| J9 | 重复与文本退化 | NA | — | 任务为从符号 token 概率中选择答案，不涉及开放生成退化/重复率。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文基准，未做跨语言/跨脚本比较；tokenization 只作为 CP 归一化问题讨论，不适用该组件。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.7 §5.3 explicitly discusses dataset leakage, Codex being fine-tuned from GPT-3 on Python, and says manual collision check was not possible for other datasets. | 识别并间接评估了污染风险，但未报告正式污染检测率、精确训练截止日期或 held-out 污染检验。 |
| J12 | 基准饱和 | 0.5 | p.8 Table 2 includes SOTA columns and high scores (COPA 100.0, StoryCloze 98.5); p.9 claims new SOTA on 9 datasets. | 报告了基准分数量程与 SOTA 位置，但接近上限的数据集未改用连续指标或更难子集，也未讨论饱和问题。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，无约束指令遵循准确率测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 模型输出通过符号 token 概率直接读取，不涉及解析生成文本的结构化输出合法率。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究定位为 LLM 工程/基准评测，不主张测量人类心理学构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告跨规模/训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标/奖励模型的优化，只做基准评估。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.8 reports single point accuracies; p.10 gives code/endpoints and one seed, but no repeated runs, CIs, paired tests, or exact snapshot date. | 评估仅报告单点分数，缺少重复次数、置信区间、配对检验和精确模型 snapshot 信息。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评测，无多轮对话历史或一致性衰减测试。 |

## 编码小结
论文对 MCP 与 CP 的核心比较清楚，覆盖多数据集、多示例设置，并显式讨论答案顺序与数据泄漏风险；但统计推断较薄弱，缺少置信区间、重复采样、正式交互检验、精确 snapshot 与更完整的提示敏感性/可复现性报告。
