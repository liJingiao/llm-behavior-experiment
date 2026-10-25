# article_070 | Language model acceptability judgements are not always robust to context | 2023

研究类型概述：LLM 行为/基准评测研究：以 GPT-2 及多个 OPT 模型为对象，操纵输入前缀的长度、可接受性及与测试现象的匹配性，测量最小配对可接受性判断准确率与 Δ accuracy；分析单位为模型×测试项目/现象层面，采用混合效应逻辑回归并含现象随机截距，不是人类被试实验。
- **研究构念（Construct）**：句法可接受度判断与语境敏感的内隐上下文学习（syntactic acceptability judgment and context-sensitive implicit in-context learning）｜CA 构念锚定：句法加工（syntactic processing, `trm_4a3fd79d0b34b`）；句法分析（syntactic parsing, `trm_4a3fd79d0b340`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）
- **实验任务与范式（Task / Paradigm）**：LLM 行为/基准评测研究：以 GPT-2 及多个 OPT 模型为对象，操纵输入前缀的长度、可接受性及与测试现象的匹配性，测量最小配对可接受性判断准确率与 Δ accuracy；分析单位为模型×测试项目/现象层面，采用混合效应逻辑回归并含现象随机截距，不是人类被试实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p1: “we vary the input contexts based on: length, the types of syntactic phenomena it contains, and whether or not there are grammatical violations”; p4: “sample N sentences (without replacement) ... until the input reaches 1000 tokens.” | 自变量被明确命名并给出水平/构造方式，但未单独报告正式的操纵检验，也未系统说明条件分配逻辑，故为部分满足。 |
| A2 | 因变量 | 0.5 | p3: “A(x_i, x′_i) = 1[P(x_i) > P(x′_i)]”; p4: “compute the log-likelihood ... using the minicons library.” | 因变量指标与计分方式明确，但未报告测量信度/效度证据，也未系统讨论连续指标预处理或天花板/地板问题。 |
| A3 | 控制变量 | 0.5 | p4: “we sample prefix sentences from a completely unrelated Wikipedia domain, the WikiText-103 test set”; p4: “c is held constant for every item.” | 报告了若干控制做法（Wikipedia 控制、同一上下文同时用于 x 与 x′），但未系统列出所有控制变量及其控制手段。 |
| A4 | 混淆变量 | 1 | p7: “controlled perturbations ... preserve ... syntactic structure”; p16: “correlations alone cannot causally implicate similarities”; p9: limitations discuss lexical exposure as residual issue. | 识别并检验了词面重叠、低层句法相似性、模板匹配等潜在混淆，做了扰动与相似性敏感性分析，并讨论残余不确定性。 |
| A5 | 调节变量 | 0.5 | p5: “three-way interaction term ... sum-coded categorical variables and log-transformed prefix lengths”; p6: “three-way interaction ... p < 0.007 for all models.” | 报告了长度×可接受性×匹配性的交互检验与图示，但未系统报告各调节水平的简单斜率统计与完整中心化/标准化说明。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量与中介假设，未做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p3–p4: MPP 定义、P(x) 与准确率公式、上下文 c 的构造、matched/mismatched/Wiki 采样规则均已给出。 | 关键构念的可观测操作化清楚，他人可据此复现主要输入构造与计分。 |
| A8 | 水平数与类型 | 0.5 | p4: “until the input reaches 1000 tokens”; p5: “sum-coded categorical variables and log-transformed prefix lengths.” | 报告了主要因素的水平与类型线索，但未完整列出所有长度水平/间距/全距，也未系统说明每个分类因素的水平标签。 |
| A9 | 单一操作化的风险 | 1 | p3–p4: 使用 BLiMP、SyntaxGym 与 CrowS-Pairs 三个数据集；p7: perturbation analysis; p8: 结果在多个模型/数据集上复现。 | 关键构念采用多数据集、多现象与扰动操作化，并报告了会聚性证据。 |
| A10 | 单一方法的风险 | NA | — | 研究不是自陈式同源测量；输入上下文与模型 log-likelihood 不适用人类共同方法偏差框架。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组分配到条件；所有模型均在相同条件集合上评估。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内顺序呈现与顺序平衡问题；各前缀条件是对独立输入的前向计算，不构成顺序性重复测量。 |
| B3 | 混合设计 | NA | — | 没有人类组间/组内混合设计；模型分别评估，未使用混合 ANOVA 的组间/组内误差项结构。 |
| B4 | 因子设计 | 0.5 | p5: “mixed-effects logistic regression ... three-way interaction term and all lower-order terms”; p6: “three-way interaction ... p < 0.007.” | 因素交叉与交互有报告，但未给完整设计矩阵、每格样本量及完整 ANOVA/效应量表。 |
| B5 | 主效应 | 0.5 | p6: “no main effect of prefix length is significant (p > 0.2 for all models) for Wikipedia sentences”; p6 报告交互显著。 | 有部分主效应/交互信息，但未系统报告每个因素的主效应 F/df/p/效应量，也未在交互显著时完整展开简单主效应。 |
| B6 | 交互作用 | 0.5 | p6: “three-way interaction ... p < 0.007 for all models on BLiMP and SyntaxGym”; Figures 3–4 含 95% CI。 | 报告了交互显著性并图示置信区间，但简单主效应事后比较与多重比较校正不完整。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量与区内随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；无人类非随机分组与选择偏差问题。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及人类被试内处理可逆性/迁移对称性。 |
| C1 | 随机化 | NA | — | 无参与者随机分配或分配隐藏；所有模型接受同一组条件。 |
| C2 | 平衡 | NA | — | 无被试条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p4: “same sequence to each target x and x′”; p4: “context window of 1024 tokens ... investigate 1000 tokens”; p9: limitations on English and unnatural contexts. | 报告了若干恒定设置并讨论外部效度限制，但未系统列出所有恒定变量（硬件、具体 checkpoint、tokenizer 等）及水平。 |
| C4 | 匹配 | NA | — | matched/mismatched 是实验操纵因素，不是为控制混淆而做的人类被试匹配。 |
| C5 | 纳入为变量 | NA | — | 没有已知混淆变量作为协变量/区组纳入分析；现象随机截距不是混淆协变量。 |
| C6 | 盲法 | NA | — | 自动化模型评估，无人类被试/评分者盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | 没有人类练习块或试次位置问题；各输入独立评分。 |
| D2 | 疲劳效应 | NA | — | 无人类 session、疲劳或休息安排问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立前向计算，无跨条件上下文残留；LLM 不保留会话历史。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移/清洗期设计。 |
| D5 | 范围效应 | NA | — | 不使用 Likert/量表评分，无范围效应。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p1: “randomly sampled linguistic contexts”; p4: “sample N sentences (without replacement) from each group.” | 有随机采样上下文的做法，但未详细报告句子顺序平衡方案、各位置出现次数或测试项目呈现顺序。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表与跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征与事后访谈问题。 |
| E5 | 实验者效应 | NA | — | 自动化数据采集，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p6: “Shaded regions are the 95% confidence interval”; p18 Table 1 reports standard deviations over context length. | 报告了均值/置信区间/部分标准差，但未系统报告端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是自陈式多构念同源测量，无共同方法偏差检验需求。 |
| F1 | 统计结论效度 | 0.5 | p3: BLiMP 67×1000 pairs, SyntaxGym ~20 items/phenomenon, CrowS-Pairs 1508 pairs; p6: 95% CI and p-values. | 报告了样本量、效应方向与部分 CI，但无事前功效分析，且多重比较校正不明确。 |
| F2 | 内部效度 | 0.5 | p4: Wiki control and matched/mismatched control; p7: perturbation controls; p9: limitations. | 评估了若干内部效度威胁并做敏感性分析，但无随机分配/分配隐藏/基线等价性报告；对 LLM 评测而言仅部分适用。 |
| F3 | 构念效度 | 0.5 | p3–p4: 使用已发表 BLiMP/SyntaxGym/CrowS-Pairs 及 minicons 计分；p7: perturbation analysis. | 有较充分的构念操作化与多数据集证据，但未报告信度（如内部一致性）与正式 manipulation check。 |
| F4 | 外部效度 | 0.5 | p5: 明确 GPT2 与 OPT 125M–6.7B；p9: limitations note English-only and unnatural prefix contexts. | 报告了模型来源与推广边界，但未系统论证模型族/数据集对更广语言与自然语境的代表性，也无跨语言复现。 |
| G1 | 分析单位 | 0.5 | p5: “random intercept term for the phenomenon (controlling for variation in baseline accuracies per phenomenon).” | 分析层级有考虑现象聚类，但未明确说明项目/试次嵌套，也未在模型中同时处理 item 与 phenomenon 的多层结构。 |
| G2 | 随机效应 | 0.5 | p5: “random intercept term for the phenomenon.” | 仅报告现象随机截距，未完整报告被试/项目/材料等随机效应结构及可推广总体范围。 |
| G3 | 材料作为随机效应 | 0.5 | p5: “random intercept term for the phenomenon”; p3: 各数据集含大量具体句子对。 | 将现象层作为随机截距，部分体现材料总体抽样，但未将具体测试项目作为随机效应，未同时建模 item 与 phenomenon。 |
| G4 | 统计功效 | 0.5 | p3: 数据集规模；p6: “95% confidence interval”; p18 Table 1 报 SD。 | 报告了效应量与部分 CI，但无事前功效分析或样本量推导。 |
| G5 | 研究者自由度 | 0.5 | p2: “several exploratory analyses”; p4: “adapt 23 of the 34 test paradigms”; p7: “top 20 BLiMP phenomena which responded most strongly.” | 披露了部分筛选与探索性分析，但未完整报告所有因变量/条件、样本量决定方式，且按结果选择 top 现象需更明确区分验证性/探索性。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–22 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文与 ACL checklist 均未提及预注册或公开分析计划；适用但未做。 |
| J1 | 位置偏差 | NA | — | 不使用 LLM-as-judge、候选选项排序或成对位置交换；仅比较两个句子在独立输入下的 log-likelihood。 |
| J2 | 冗长偏差 | NA | — | 不涉及 LLM 裁判评估开放式生成质量，长度是实验操纵变量而非评分长度偏差。 |
| J3 | 谄媚 | NA | — | 无用户立场、反馈或纠错对话，不涉及谄媚。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 作为裁判评估其他模型输出，无自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 使用的是上下文前缀，不是带标签的 few-shot 示例；未做示例选择/顺序的 few-shot ICL 设计。 |
| J6 | 提示敏感性 / 脆弱性 | NA | — | 没有自定义 prompt 模板与 prompt 版本工程；输入是构造的前缀文本，不是 prompt 敏感性实验。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是 RAG/长文档关键信息定位实验；测试句始终作为后缀，未操纵“关键信息位于首/中/尾”的位置。 |
| J8 | 温度与采样随机性 | NA | — | 使用预训练模型 log-likelihood 评分，无解码采样；未涉及 temperature 等生成采样参数。 |
| J9 | 重复与文本退化 | NA | — | 不涉及开放文本生成与重复/退化问题。 |
| J10 | 分词效应 | NA | — | 单语言英语、单脚本，未做跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p3–p4: 使用公开 BLiMP、SyntaxGym、CrowS-Pairs；p5: 使用 GPT2 与 OPT 系列。 | 未报告基准发布日期与模型训练截止日期对照，也未做 n-gram/DCQ 污染检测；基准污染风险存在但未评估。 |
| J12 | 基准饱和 | 0.5 | p15 Figures 10–11 给出 baseline accuracy 轴；p19 Appendix E 给出 perplexity margin。 | 报告了基线准确率与连续 margin，但未系统评估基准是否接近天花板或与 SOTA 水位比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，无约束指令测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/JSON 输出，无格式合法率问题。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p2: 将结果与 “syntactic priming” 和 “in-context learning” 联系；p8: “analogous to structural priming”; p9 limitations mention English-only and artificial contexts. | 明确讨论了 LLM 构念与心理语言学同名构念的类比，但未做系统的人类对照实验或完整构念效度论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较模型规模，但没有宣称“涌现/突变”能力曲线，也未做规模×指标的涌现检验。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N 或对代理指标的优化环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5: “GPT2 ... and ... OPT ... 125M, 350M, 1.3B, 2.7B and 6.7B”; p6: “95% confidence interval.” | 报告了模型版本/规模与置信区间，但未给精确 snapshot/checkpoint/commit、随机种子、原始推理日志或配对检验细节。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验是单轮输入评分，无多轮对话历史累积，也不主张多轮部署。 |

## 编码小结
论文对上下文如何影响 LLM 句法可接受性判断做了系统操纵与较充分的结果报告，包括多数据集复现、扰动分析和相似性分析；但若干人类实验设计组件不适用，LLM 评测相关组件在模型快照、采样随机性、基准污染、饱和与可复现性上报告不完整。总体证据较强，但方法报告仍有若干 0.5 级别的缺口。
