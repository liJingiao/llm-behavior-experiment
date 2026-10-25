# article_208 | Do LLMs estimate uncertainty well in instruction-following? | 2025

研究类型概述：这是一项 LLM 基准评估研究：在 IFEval 及作者构建的 Controlled/Realistic 基准上，比较 6 类不确定性估计方法与 4 个 LLM，分析单位为模型响应及按指令类型聚合的 AUROC；不涉及人类被试实验。
- **研究构念（Construct）**：指令遵循中的元认知监控、自我置信与不确定性估计｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：让现成模型完成可验证指令，并通过口头置信、p(true)、序列概率、困惑度和token熵判断自己的回答是否遵循指令。（比较不同控制难度、真实任务、指令类型、模型规模及六种无需训练的不确定性读出。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3: 'we employ several baseline methods' and lists six methods/four LLMs; p.7: Controlled-Easy, Controlled-Hard, Realistic versions. | 明确命名并报告了不确定性方法、模型与数据集版本等条件及水平，但没有操纵检验或单位随机分配说明。 |
| A2 | 因变量 | 0.5 | p.3: 'AUROC is used to measure if the models’ uncertainty estimation matches the ground truth labels ... generated using the automated evaluation functions from IFEval'; p.4 Table 1. | 因变量指标与计分方式明确，但未报告信度、效度、连续指标预处理或置信区间。 |
| A3 | 控制变量 | 1 | p.5–7 systematically discuss length bias, task-quality entanglement and difficulty; p.7: Controlled version neutralizes token length; GPT-4 filters task quality >8 and same responses are used across models. | 系统识别并说明了主要控制变量及其控制手段（长度中性化、任务质量过滤、同响应跨模型比较）。 |
| A4 | 混淆变量 | 0.5 | p.5–7 identify length bias, task-quality confounding and difficulty differences, with controlled benchmark as remedy; p.10 mentions potential leakage. | 识别并控制了主要潜在混淆，但未报告残余混淆的量化敏感性分析或正式内部效度威胁评估。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量假设或乘积项交互检验；模型、方法与指令类型的比较为描述性基准比较，不构成调节分析。 |
| A6 | 中介变量 | NA | — | 没有中介变量、直接/间接效应或因果链检验。 |
| A7 | 操作性定义 | 1 | p.3 gives uncertainty formulas and p.4 describes probe training; p.13–16 provides full prompts for verbalized confidence, p(true), and benchmark generation/filtering. | 关键构念的操作化较完整：不确定性指标、正确性标签、探查模型与生成/过滤提示均可复现。 |
| A8 | 水平数与类型 | 1 | p.3 lists six uncertainty methods and four model versions; p.7 defines Controlled-Easy/Controlled-Hard/Realistic; p.21 lists instruction types. | 各因素水平数与标签明确；均为分类水平，无连续水平间距/中心化问题。 |
| A9 | 单一操作化的风险 | 0.5 | p.3 employs multiple uncertainty estimation methods; p.8 Table 4 and p.21 Table 9 compare methods across models/conditions. | 关键构念采用了多种操作化，但未报告不同操作间的会聚证据，也未系统讨论单一操作化局限。 |
| A10 | 单一方法的风险 | NA | — | 主要因变量正确性来自 IFEval 确定性程序，不确定性来自 logits、verbalized 或内部状态，方法来源并非同源自陈量表；无共同方法偏差检验需求。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配；模型在同一基准条件上评估，不是独立被试组间设计。 |
| B2 | 被试内设计 | NA | — | 没有人类被试重复测量或跨条件呈现顺序；各不确定性指标为离线计算，无顺序平衡需求。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内混合实验设计及相应误差项。 |
| B4 | 因子设计 | NA | — | 论文是描述性基准矩阵而非实验因子设计，未报告 ANOVA 式主效应/交互项；按规则无因子设计及交互分析记 NA。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的正式主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是非随机分配的准实验干预研究，主要是个基准评测。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理条件，无需论证处理可逆性或迁移对称性。 |
| C1 | 随机化 | NA | — | 研究单位未被随机分配到互斥处理条件；基准响应和模型为固定集合。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件呈现顺序。 |
| C3 | 恒定 | 0.5 | p.3: model versions are listed and 'we employ greedy decoding without sampling'. | 报告了模型版本和固定贪心解码，但未系统列出所有恒定设置，也未充分讨论其对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对分配。 |
| C5 | 纳入为变量 | NA | — | 未把已知混淆变量作为协变量或区组纳入统计模型；论文采用基准构建控制混淆，而非 ANCOVA。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者盲法安排；GPT-4 评分条件也不是人类盲法设计。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | 各响应独立评分，无跨试次练习或学习效应设计。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同条件间无药物/学习残留或清洗期问题；每次评估独立。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移或不对称迁移设计。 |
| D5 | 范围效应 | NA | — | 主要因变量为 AUROC 等排序指标，不是人类被试内绝对量值或李克特量表评分；无范围效应控制需求。 |
| E1 | 位置 / 顺序偏差 | 0 | p.3: p(true) prompt asks 'Does the response: (A) Follow instructions (B) Not follow instructions. The answer is:'; p.14 gives the same fixed A/B order. | 二选一选项顺序固定，未随机化或反平衡，也未报告位置偏差检查；存在选项位置风险。 |
| E2 | 默认赞同 | NA | — | 研究不使用含正反向题的李克特/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 未使用需要分析端点/中点反应风格的人类等级量表；主要比较 AUROC，而非跨群体量表反应风格。 |
| E4 | 需求特征 | NA | — | 无人类被试，故无需求特征或事后访谈问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.4 Table 1 and p.8 Table 4 report mean AUROC/SR; p.7 describes Controlled-Easy/Hard difficulty construction. | 报告了主要指标均值并设计了难度水平，但未报告标准差、偏度或端点频率，也未说明 pilot 难度校准细节。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，无共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | p.4 Table 1 and p.8 Table 4 report AUROC point estimates; p.18 Table 7 reports sample counts. | 报告了效应量性质的 AUROC 与样本量信息，但没有置信区间、功效分析和多重比较校正。 |
| F2 | 内部效度 | NA | — | 研究不是因果处理实验，无随机分配、分配隐藏或被试流向/损耗问题；内部效度主要通过 A4 的基准混杂控制讨论。 |
| F3 | 构念效度 | 0.5 | p.3–4 motivate uncertainty estimation and describe multiple methods; p.13–16 give prompts; p.2–3 rely on IFEval deterministic verifier. | 有构念论证和多方法操作，但未报告测量信度/效度指标或操纵检验。 |
| F4 | 外部效度 | 0.5 | p.3 lists four LLMs; p.10 limitations mention 'narrow scope of instruction types and domains' and potential leakage. | 报告了模型来源与边界限制，但未做跨样本/跨领域复现或代表性抽样论证。 |
| G1 | 分析单位 | 0.5 | p.8 Table 4 reports averages; p.21 Table 9 reports AUROC 'for each instruction type' and averages across instruction types; p.18 Table 7 gives response counts. | 存在响应嵌套于指令类型/提示的结构，但分析以按指令类型聚合/平均为主，未用多层模型显式分离聚集方差。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；四个模型是明确固定的比较对象，未主张从随机模型总体推断，故无随机效应结构需报告。 |
| G3 | 材料作为随机效应 | 0.5 | p.21 Table 9 reports per-instruction-type results; p.10 acknowledges narrow instruction-type scope. | 材料/指令类型被拆分报告并承认范围有限，但未将材料/项目作为随机效应纳入模型。 |
| G4 | 统计功效 | 0 | p.18 Table 7 gives data counts; no power analysis or confidence intervals are reported. | 没有事前功效分析、目标效应量或结果 CI；仅报告点估计。 |
| G5 | 研究者自由度 | 0.5 | p.7 describes GPT-4 task-quality filtering >8 and generation of controlled responses; p.18 Table 7 reports per-condition counts; p.3 lists all uncertainty methods. | 报告了筛选规则、主要因变量和条件，但未区分验证性与探索性分析，也未说明停止规则或全部事后分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–25 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册、注册编号或数据收集前分析计划；按规则记 0。 |
| J1 | 位置偏差 | 0 | p.3 and p.14 show the binary p(true) prompt with fixed '(A) Follow instructions (B) Not follow instructions' order; no swap or position analysis is reported. | 涉及二选一位置风险，但未做 A/B 反平衡、交换重判或翻转率分析。 |
| J2 | 冗长偏差 | 0.5 | p.5 Figure 2 and p.24 Table 11 analyze token-length differences; p.7 constructs a length-neutral Controlled version; p.8 notes sequence probability may exploit length. | 明确识别并设计控制长度偏差，但未报告长度—得分相关系数、裁判温度或完整长度盲评对照。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场、反馈或纠错对话，无谄媚操纵可能。 |
| J4 | 自我偏好 | 0.5 | p.6 Table 2 and p.16 show GPT-4 used to score task quality/instruction-following; p.2–3 main IFEval labels use deterministic verifier. | 使用了异源 GPT-4 评估/过滤，但未报告裁判模型快照、与人类金标准一致性或自我偏好/同源偏差量化。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 提示词为 zero-shot，未使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.13–16 provides full prompts for uncertainty elicitation and data generation/scoring. | 提供了完整提示模板，但没有版本号、语义等价敏感性消融或 dev/test 划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务上下文为短指令/响应，不涉及长上下文或 RAG 的信息位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | p.3: 'To avoid randomness in decoding, we employ greedy decoding without sampling.' | 报告了贪心解码，但未报告温度/top-p/seed、重复采样次数或基于重复的置信区间。 |
| J9 | 重复与文本退化 | 0.5 | p.3 reports greedy decoding without sampling; no repetition/degeneration rate or truncation proportion is reported. | 报告了解码策略，但未报告 n-gram 重复率/退化率或生成长度截断比例。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本，无跨语言/跨脚本 tokenization 比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.10: limitations mention 'potential risk of leakage'; p.2–3 use public IFEval; no training cutoff or overlap analysis is reported. | 承认污染/泄漏风险，但未对照模型训练截止日期，也未做 n-gram/DCQ 污染检测。 |
| J12 | 基准饱和 | NA | p.8 Table 4 shows AUROC near chance and Controlled-Hard generally below 0.62; no saturated benchmark improvement claim. | 所用指标远未接近天花板，且论文未在饱和基准上宣称显著提升，故该风险不适用。 |
| J13 | 指令遵循 | 0.5 | p.2: IFEval uses deterministic programs to verify instruction following; p.13 Table 5 breaks results down by instruction types. | 指令遵循有可机器判定标准并按约束/指令类型拆分，但未报告模型指令微调数据规模等训练细节。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.14 prompts require 'Your response should be ONLY the score, an integer between 0 and 9' and fixed A/B output. | 报告了结构化输出要求，但未报告格式合法率、解析失败率或重试/后处理规则。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文定位为 LLM 工程性不确定性估计基准，不主张测量或外推人类心理学/认知构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随模型规模/训练进展的涌现能力曲线，也未宣称突然涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及以基准/奖励模型/LLM-judge 为目标的优化或过优化监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.3 lists model versions (LLaMA2-chat-7B/13B, Mistral-7B-Instruct-v0.3, Phi-3-mini-128k-instruct); p.1 gives code/data link; no repeated runs or CIs are reported. | 提供了模型版本和代码链接，但无精确 snapshot 日期/commit、重复次数、置信区间或配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示/响应评估，不涉及多轮对话历史累积。 |

## 编码小结
论文的核心是工程性基准评测与不确定性方法比较，控制了长度、任务质量和难度等基准混杂，并提供了较完整的提示词与数据说明；但缺少推断统计、置信区间、预注册、严格随机化/顺序平衡及部分 LLM 评估偏差控制。人类实验设计组件多为 NA，基准评测相关的 G/J 组件部分满足。
