# article_157 | RULEBREAKERS: Challenging LLMs at the Crossroads between Formal Logic and Human-like Reasoning | 2025

研究类型概述：大型 LLM 基准评测/LLM-as-participant 研究：作者构造 RULEBREAKERS 数据集，含 rulebreaker 与 non-rulebreaker 成对实例，交叉 modus tollens/disjunctive syllogism、地理/类别实体与 10 种提示措辞，评测 7 个 LLM 的配对准确率、rulebreaker/non-rulebreaker 准确率和置信度，并用知识熟悉度、输入×梯度/注意力归因和神经元激活做解释性分析；无人类被试。
- **研究构念（Construct）**：形式逻辑规则与常识约束冲突时的过度刚性推理｜CA 构念锚定：语义记忆（semantic memory, `trm_4a3fd79d0b083`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）；认知控制（cognitive control, `trm_4aae62e4ad209`）
- **实验任务与范式（Task / Paradigm）**：让七种现成LLM判断成对的rulebreaker与非rulebreaker自然语言推理题。（保持逻辑形式近似不变，操纵结论是否与世界知识/常识冲突，并改变表述模板。）｜CA 任务锚定：演绎推理任务（deductive reasoning task, `trm_4c898b8c2d071`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: “four templates ... created by permuting premise-conclusion structures of two logical rules ... and two kinds of entity pairs”; p.6: “present each instance ... in 10 different variations”; p.6: “Using the default configurations, we perform one forward pass on each prompt.” | 研究报告了数据集条件和提示措辞的多水平操纵及生成程序，但未报告正式操纵检验，单位分配到条件的规则也主要是全提示统一评测而非随机分配。 |
| A2 | 因变量 | 0.5 | p.5: Eqs. (1)-(3) define paired accuracy, τDR and τDN; Eqs. (4)-(6) define confidence p+(x), Π+DN and Π+DR; p.7 Figures 3-4 report accuracy with 95% CI. | 因变量指标与计分方式明确，但未报告测量信度/效度证据，也未对连续指标预处理或端点效应做系统说明。 |
| A3 | 控制变量 | 0.5 | p.6: “we filter out those entity pairs which the model lacks relational knowledge of”; p.6: 10 prompt phrasing variations; p.6: “Using the default configurations”; p.25-p.26: GPU/batch-size details. | 报告了若干控制手段（知识过滤、提示变体、默认配置、硬件与批大小），但没有形成系统的控制变量清单并逐项说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.6: 过滤模型缺乏关系知识的 city 名称；p.8: “this is the case for most LLMs, except for Meta-Llama-3-8B-Instruct and GPT-4o”; p.9: “the relation between failure and attention distribution is less clear-cut than expected.” | 识别并部分控制了实体熟悉度、提示措辞和注意力等潜在混淆，也如实讨论残余不一致，但未以正式敏感性分析或内部效度威胁评估呈现。 |
| A5 | 调节变量 | NA | — | 论文未提出正式调节假设，也未做乘积项交互检验与简单斜率分析；模型/子集比较属于描述性或解释性分析，不构成调节设计。 |
| A6 | 中介变量 | NA | — | 论文未提出中介模型，也未做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.4: Table 1 and Section 3.1 describe templates, entity pairs, verbs and names-pronouns generation; p.5: exact accuracy/confidence formulas; p.6: exact prompt phrasings and answer options; p.2: dataset link released. | 关键构念被写成可复现的生成、提示和计分程序，包括数据集模板、水平标签、公式与公开链接。 |
| A8 | 水平数与类型 | 0.5 | p.4: two logical rules (MT/DS) and two entity-pair kinds; p.5 Figure 2 gives dataset counts; p.6: “five basic phrasings” × “two answer-option pairs” = 10 variations. | 报告了各因素水平数与具体标签，但未明确标注水平类型（名义/等级/连续）及间距/全距等，属于部分满足。 |
| A9 | 单一操作化的风险 | 1 | p.5: main accept/reject task with paired accuracy; p.23-p.25: Appendix I conclusion-generation task; p.19: prompt phrasing breakdown and robustness; p.25: “results ... generally conform to the patterns ... in our main experiment.” | 关键构念至少通过 accept/reject 判断和结论生成两种任务操作化，并通过多种提示措辞检验会聚性，符合多操作化要求。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈式测量，IV 为外部提示/数据条件，DV 为模型输出与内部归因指标；不存在问卷式共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 没有把独立被试组分配到不同条件；所有模型均评测全部提示条件，不存在传统被试间设计。 |
| B2 | 被试内设计 | NA | — | 虽然同一模型处理多个提示条件，但每次为独立前向传播且无上下文累积，不需要按人类被试内顺序平衡编码。 |
| B3 | 混合设计 | NA | — | 没有混合设计及对应组间/组内误差项的统计模型。 |
| B4 | 因子设计 | 0 | p.4: Table 1 crosses two logical rules with two entity-pair kinds; p.7: Figure 3 reports paired accuracy for MT/DS × country-city/type-instance subsets; p.6: 10 prompt variations. | 存在多因素交叉的数据结构与子集描述结果，但未报告完整设计矩阵的每格样本量，也未给出交互项的正式统计检验；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p.7: “models achieve higher paired accuracy on the DS subsets compared to MT” is only a descriptive trend; no F/df/p/effect size for main effects is reported. | 论文有子集均值与置信区间，但没有报告各因素主效应的统计检验，按编码规则基本要件未达成。 |
| B6 | 交互作用 | 0 | p.7: “we see a high degree of variability ... on different prompt subsets”; no interaction F/df/p, simple effects, or error-bar interaction plot is reported. | 未对交互项做正式统计检验，也未在交互显著时报告简单主效应或多重比较。 |
| B7 | 区组设计 | NA | — | 研究没有区组/分层分配设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡被试内条件顺序。 |
| B9 | 准实验设计 | NA | — | 模型比较属于固定检查点上的基准评测，不是准实验处理分配，也未以准实验因果设计框架报告。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及人类被试内处理的处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 所有模型对所有提示进行评测，没有把分析单位随机分配到互斥条件的分配程序。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序；提示为独立前向传播。 |
| C3 | 恒定 | 0.5 | p.6: model versions and “Using the default configurations”, no system prompts; p.6: GPT-4o “gpt-4o-2024-11-20”; p.25-p.26: GPU, batch size and inference time details. | 报告了模型版本、默认配置和硬件等恒定项，但未系统列出所有恒定变量及对结论外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配或配对分配设计。 |
| C5 | 纳入为变量 | 0.5 | p.6: 过滤 20 个模型缺乏关系知识的 city 名称；p.8 Table 3: 测量并比较模型对城市/国家的“familiarity”与正确/错误配对。 | 已知的知识/熟悉度混淆被测量并用于过滤和补充分析，但未作为主分析中的协变量或区组变量正式建模，也未检验斜率齐性等假设。 |
| C6 | 盲法 | NA | — | 数据收集与评分完全自动化，无人类主试/评分者需要盲法。 |
| C7 | 平衡的层级 | NA | — | 没有顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | 每个提示独立前向传播，无上下文内练习或学习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 批量推理不涉及人类疲劳或 session 时长问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件上下文延续，每个 prompt 独立处理，无延滞/迁移效应。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为准确率和 token 概率等客观指标，不存在量表式范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | p.6: answer options are fixed as “Answer Yes or No only.” or “Answer True or False only.”; p.6: 10 variations vary question wording and answer-option pair, but no reversal/randomization of option or premise order is reported. | 未报告对 yes/no 或 true/false 选项顺序、前提顺序做随机化或反平衡；提示措辞变体不等于选项位置平衡。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分题问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不需要 cover story 或事后访谈检查需求特征。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类实验者/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7: Figure 4 shows some models achieve perfect non-rulebreaker scores (“Gemma-2-27b-it and GPT-4o ... perfect scores”) while rulebreaker scores are low; p.24 Table 8 shows further ceiling patterns. | 报告了均值/CI 和明显的端点现象，但未系统报告偏度/端点频率，也未说明难度校准或 pilot 过程。 |
| E7 | 共同方法偏差 | NA | — | 不存在同源自陈式多构念测量；IV 与 DV 不是问卷来源关系。 |
| F1 | 统计结论效度 | 0.5 | p.7: Figures 3-4 report 95% CI; p.8: Welch’s t-test p < 0.0001 for confidence/familiarity comparisons; p.24 Table 8 reports accuracy differences. | 报告了效应量性质的准确率与置信区间，也有部分显著性检验，但无样本量/功效依据，且多重模型×子集比较未见校正。 |
| F2 | 内部效度 | NA | — | 无人类随机分配、分配隐藏、被试流向或 attrition 问题；不属于传统实验内部效度框架。 |
| F3 | 构念效度 | 0.5 | p.17 Table 5 links templates to cognitive-science human studies; p.6 filters model knowledge; p.19 reports prompt phrasing sensitivity; no conventional reliability or validity coefficients are reported. | 有构念对应与知识过滤等效度论证，但缺少测量信度/正式效度证据和完整操纵检验。 |
| F4 | 外部效度 | 0.5 | p.6: model selection criteria (“medium-sized”, “instruction-fine-tuned”, “open-sourced”) and GPT-4o comparison; p.19: prompt phrasing breakdown; p.27-p.28: logic-enhanced model robustness checks. | 报告了模型来源与部分跨条件稳健性，但未系统界定对模型总体、任务情境或人类推理的推广边界。 |
| G1 | 分析单位 | 0.5 | p.5: D comprises all instances permuted across 10 phrasings; paired accuracy is computed over Dpaired; p.7: results aggregated by model and prompt subsets. | 分析单位定义在 prompt/pair 层面，但未用多层/混合模型处理提示嵌套于模板、实体对、措辞及模型等聚集结构。 |
| G2 | 随机效应 | NA | — | 论文未使用随机效应模型；七个模型作为固定检查点分别比较，并未从模型总体随机抽样作混合模型推断。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: country-city pairs from WikiData, type-instance pairs from ConceptNet, names randomly sampled; p.5: accuracy averaged over D; p.7: aggregated model results. | 具体实体/项目来自更大池并大量生成，但分析未把 item/entity 作为随机效应纳入模型，项目层面推广性受限。 |
| G4 | 统计功效 | 0.5 | p.6: model selection limited by “computational constraints”; p.7: figures report 95% CI; no a priori power analysis or sample-size derivation is reported. | 报告了准确率与置信区间，但无设计阶段功效分析或明确样本量/重复次数论证。 |
| G5 | 研究者自由度 | 0.5 | p.6: “We exclude the subset of prompts ... containing any of these 20 city names”; p.25: unparsed responses are separately categorized; p.23-p.28: multiple additional analyses. | 报告了排除规则、未解析输出与多项补充实验，但未完整区分所有验证性/探索性分析，也未说明样本量停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or time-stamped analysis plan is reported in the main text or appendices. | 无预注册信息；按编码口径，适用但未报告记 0。 |
| J1 | 位置偏差 | NA | — | 研究不是 LLM-as-judge 或多候选项排序/成对偏好任务；模型仅对给定结论作 yes/no/true/false 判断，不存在 A/B 候选位置。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判对开放式回答质量打分；结论生成用模式匹配而非长度-质量评分。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场、反馈或纠错对话，不涉及谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 无 LLM-as-judge 或模型间成对裁判，不涉及自我偏好偏差。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.28 Table 10 includes “COT (2-SHOT)” for gpt-3.5-turbo, but no example source, label proportion, ordering counterbalancing, or multiple seeds are reported. | 附加实验实际使用了 2-shot CoT，存在 few-shot 示例偏差风险，但缺少示例来源、比例、顺序控制与多 seed 报告。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.6: five question phrasings × two answer-option pairs; p.22 Appendix G gives example prompts; p.23 Appendix H adds instruction/alternative phrasing; p.19-p.21 report phrase-level sensitivity. | 提示模板和敏感性消融较充分，但缺少版本号/迭代日期、dev/test 划分以及 prompt 搜索过程说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 提示均为短 premises/conclusion，无长上下文或 RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: “Using the default configurations, we perform one forward pass”; p.25: conclusion generation uses “greedy decoding” and max 50 tokens; p.26 Table 9 tests temperatures 0.1/0.5/1.0. | 报告了部分采样/解码设置与温度敏感性，但未完整报告 top-p/top-k/seed、重复采样次数及对应 CI。 |
| J9 | 重复与文本退化 | 0.5 | p.25: conclusion generation uses “greedy decoding” with max 50 tokens and pattern-matching; p.26 Figure 7 separates correct/incorrect/unparsed; no n-gram repetition or degeneration rate is reported. | 报告了解码方式与截断长度，并给出 unparsed 类别，但未报告重复率/退化率等文本质量 QC。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言、单脚本提示，无跨语言/跨脚本 token 化比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.2: dataset publicly released; p.6: models including GPT-4o 2024-11-20; no training cutoff comparison or contamination detection is reported. | 数据集是新构造的，降低了公开基准污染风险，但论文未报告模型训练截止日期或任何污染检测/泄漏检查。 |
| J12 | 基准饱和 | NA | p.7: baseline random guessing 0.25 and overall paired accuracy mostly mediocre (only Meta-Llama-3-8B-Instruct > 0.6); p.7 notes perfect non-rulebreaker subset scores. | 核心配对准确率远未饱和；个别 non-rulebreaker 子集满分在文中作为解释性现象讨论，未构成整体基准饱和问题。 |
| J13 | 指令遵循 | NA | — | 因变量是逻辑/知识知情推理判断，不是指令遵循能力；未按否定/数量/格式等约束拆分指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.6: answer options “Answer Yes or No only.” / “Answer True or False only.”; p.25: pattern-matching and “unparsed” category for generated conclusions; no separate format legal-rate for main experiment is reported. | 有格式约束设置并部分报告 unparsed，但未系统报告格式合法率、重试策略及格式失败与内容错误的独立指标。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估或有害请求。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2: defines “human-like” and “knowledge-informed” based on cognitive-science findings; p.17 Table 5 maps templates to human studies; p.7: compares observed LLM behavior with “what we expect from typical human reasoners.” | 论文明确把 LLM 行为与人类同名构念作理论对照，并报告模型版本；但没有直接同范式人类被试实验，部分外推仍依赖既有文献。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究不报告跨模型规模/训练进展的涌现曲线，也不宣称涌现突变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以代理指标为优化目标进行 RL、best-of-N 或 benchmark 过优化；仅做基准评测与模型比较。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6: exact model names and GPT-4o snapshot “gpt-4o-2024-11-20”; p.7: accuracy figures with 95% CI; p.6: “one forward pass”; no model commit hashes, repeated-run N, or paired model comparison tests are reported. | 提供了部分版本标识与 CI，但缺少精确检查点/commit、重复运行次数、配对检验和原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示-回答，不使用多轮对话历史，也不主张多轮部署一致性。 |

## 编码小结
论文的核心贡献是数据集与基准评测，而非传统人类被试实验。对 LLM 分析单位而言，数据生成、提示变体、指标定义与部分混淆控制较清楚，但缺少正式操纵检验、随机效应/项目推广模型、预注册、功效分析与若干 LLM 评估透明度项；大量人类被试设计组件因无对应结构记 NA。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
