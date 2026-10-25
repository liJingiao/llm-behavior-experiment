# article_243 | KScope: A Framework for Characterizing the Knowledge Status of Language Models | 2025

研究类型概述：这是一项面向 LLM 的方法/基准评估研究：提出五种知识状态的分类与 KScope 分层统计检验框架，在 9 个 LLM、4 个数据集上重复采样刻画参数性与语境性知识状态；随后用分层 logistic regression/SHAP 分析语境特征重要性，并比较多种语境增强策略对知识更新成功率的影响。分析单位主要是问题×模型×数据集/知识状态，条件多为独立 LLM 调用或同一题项下的重复评估。
- **研究构念（Construct）**：知识状态的一致性与正确性、语境驱动的知识更新、熟悉性和冲突反应｜CA 构念锚定：认知控制（cognitive control, `trm_4aae62e4ad209`）；注意（attention, `trm_4a3fd79d09902`）；干扰控制（interference control, `trm_551f11bb8f6a8`）
- **实验任务与范式（Task / Paradigm）**：对四个问答数据集中的问题生成多种释义，分别在无语境、金标准语境和噪声语境下重复采样九个现成LLM的答案，用分层检验将每题分类为五种知识状态，并比较语境特征和提示增强造成的状态转移。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: 'When supporting context c is available... q = f(· &#124; x, c)'; p.8: augmentation strategies include 'Credibility', 'Naïve Summarization', 'Constrained Summarization', 'Combined'. | 研究确实操纵了有无支持语境及语境增强策略，并给出水平与提示程序；但未系统报告单位如何分配到各水平，也无操纵检验（manipulation check），故为0.5。 |
| A2 | 因变量 | 0.5 | p.3-5: KScope defines modes Yp, five statuses, hierarchical exact tests; p.15: N=100 responses and M=20 paraphrases; p.7: success label for knowledge update. | 因变量指标（知识状态、更新成功率）及计分/统计检验定义清楚；但未报告传统信效度证据，也未系统说明连续指标预处理/端点效应，故为0.5。 |
| A3 | 控制变量 | 0.5 | p.6: 'setting the temperature to 1', 'fix the significance level ... at α = 0.05'; p.15: M=20 and N=100; p.16: L2 regularization and five-fold cross-validation. | 报告了部分控制变量及其固定方式（temperature、α、M/N、正则化、交叉验证），但未系统列出控制变量清单并逐一说明控制手段，故为0.5。 |
| A4 | 混淆变量 | 0.5 | p.6: 'likely due to longer context lengths'; p.7: features include Context Length; p.9: limitations mention underexplored stylistic features and clean supporting-context setting. | 识别了语境长度、领域/数据集差异、特征覆盖面等潜在混淆，并在特征分析中纳入部分变量；但未系统说明全部混淆控制与残余威胁/敏感性分析，故为0.5。 |
| A5 | 调节变量 | 0 | p.7: Figure 6 reports Spearman correlations among feature-importance rankings across statuses; p.8: Figure 7 reports augmentation effects separately for each status; no formal status × strategy interaction test is reported. | 论文按初始知识状态分层比较特征重要性和增强效果，具有调节式研究问题；但未报告正式交互检验、中心化/标准化或简单斜率推断，按编码表判0。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量与中介效应分解，理论模型也不是中介模型。 |
| A7 | 操作性定义 | 1 | p.3-5: precise definitions of modes, five statuses and KScope tests; p.15: M=20 paraphrases, N=100 samples; p.23-25: full prompts for option generation, response sampling, credibility and summarization. | 关键构念与处理均有可执行的操作化说明：状态判定的统计流程、采样参数、特征计算、增强策略提示词均可复现；代码链接也给出。 |
| A8 | 水平数与类型 | 0.5 | p.5: datasets converted to three-option classification; p.8: four augmentation strategies plus original context; p.24: prompts specify Option 1-3 and context/no-context versions. | 报告了主要条件的水平数与标签，但未系统说明水平类型、间距/全距及连续变量中心化处理；故为0.5。 |
| A9 | 单一操作化的风险 | 1 | p.9: 'we restrict our experiments to three-option classification due to computational constraints' and 'input context always includes supporting evidence'; p.15: KScope claimed to generalize to open-ended questions. | 核心构念主要采用单一 KScope 操作化，但作者在局限中明确讨论了三种选项限制、干净支持语境限制及未来推广边界，符合单一操作化需讨论可推广性限制的要求。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是人类自陈式多构念测量，IV 为提示/语境条件，DV 为模型输出与统计判定，不存在传统共同方法偏差检验问题。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立 LLM 组被随机分配到单一条件；模型/数据集比较是观察性分组而非被试间实验分配。 |
| B2 | 被试内设计 | NA | — | 同一模型/题项在不同语境条件下重复评估，但各次为独立 LLM 调用，未构成需要顺序平衡的同一会话内被试内设计。 |
| B3 | 混合设计 | NA | — | 研究没有明确设置组间/组内混合实验设计并采用混合模型；模型与数据集是分层/观察性因素。 |
| B4 | 因子设计 | NA | — | 论文不是以 ANOVA 式因子实验呈现因素、设计矩阵与交互项；模型×数据集×条件比较是基准式分层汇总。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验（F、df、p、效应量），故不适用。 |
| B6 | 交互作用 | NA | — | 没有正式报告交互项统计检验与简单主效应/事后比较，故不属于因子交互设计编码。 |
| B7 | 区组设计 | NA | — | 论文按数据集、LLM、初始知识状态分层分析，但这不是区组随机设计，也无区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；模型/数据集比较是观察性基准比较，且未按准实验类型编码。 |
| B10 | 被试内设计的适用条件 | NA | — | 独立 LLM 调用不存在人类被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 条件不是分配给独立单位；同一题项可接受多条件/重复采样，且无随机分配隐藏机制可编码。 |
| C2 | 平衡 | NA | — | 无跨条件顺序呈现与顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.6: temperature fixed to 1, α = 0.05; p.15: M=20, N=100; p.15: experiments run on four A100 GPUs. | 列出并固定了若干关键参数/环境，但未系统列出所有恒定变量及水平，也未讨论这些恒定选择对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有匹配变量、配对或倾向得分匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.7: analyses are stratified by dataset, LLM and initial parametric knowledge status; p.16: logistic regression with five-fold CV; context length included among features. | 部分混淆/异质性通过分层与特征纳入处理，但未检验协变量斜率齐性或报告调整后效应量，故为0.5。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人工评分者；全自动 LLM 调用与算法评估，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA等顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | LLM 每条件为独立调用，不存在人类被试跨试次练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长/疲劳问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立提示与采样，无跨条件药物/学习残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内顺序迁移设计，故不对称迁移不适用。 |
| D5 | 范围效应 | NA | — | 因变量为选项/判定结果与统计成功率，不是主观量表绝对判断。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.5: 'To reduce positional bias, we permute the order of each regimen–comparator pair' for Hemonc; p.24: choices shown as Option 1-3. | 仅 Hemonc 明确提到置换选项顺序，其他数据集与完整平衡方案细节未报告；且无位置×正确率或翻转率，故为0.5。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，无法推断研究假设或产生需求特征。 |
| E5 | 实验者效应 | NA | — | 无人类主试/评分者参与的数据采集，实验者效应不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.4: Figure 3 shows status proportions, e.g., HotpotQA contextual Consistent Correct as high as 96.4%/98.8%; p.16: class imbalance noted and models not beating dummy baseline excluded. | 报告了状态比例并处理了极端类别不平衡，但未系统报告偏度/端点频率或 pilot 难度校准，故为0.5。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.5: exact binomial/multinomial/likelihood-ratio tests with Bonferroni and BIC; p.7: Spearman correlations with Bonferroni correction; p.8: reports percentage changes. | 报告了效应量性质的比例/百分比变化并做部分多重校正，但无置信区间、无功效分析/样本量依据，故为0.5。 |
| F2 | 内部效度 | 0.5 | p.5: with/without context prompts; p.4: baseline parametric status distributions; p.9: limitations on clean supporting context and computational restriction. | 同一题项在条件间比较并展示基线状态，部分讨论内部效度威胁；但无随机分配/分配隐藏或正式敏感性分析，故为0.5。 |
| F3 | 构念效度 | 0.5 | p.15: hyperparameter search shows status characterization stabilizes at N=100/M=20; p.3-5: taxonomy and operational definitions; no formal reliability/validity statistics. | 提供了稳定性证据与构念定义，但缺少正式信度/效度检验和操纵检验，故为0.5。 |
| F4 | 外部效度 | 1 | p.6: nine instruction-tuned LLMs across Gemma-2, Llama-3, Qwen-2.5; four datasets; p.8: GPT-4o held-out from feature analysis generalizes; p.9: limitations on three-option and clean-context settings. | 报告了模型/数据集来源与特征，明确推广边界，并做了跨模型（含 GPT-4o）泛化验证；外部效度报告较完整。 |
| G1 | 分析单位 | 0.5 | p.7: 'for each combination of dataset, LLM, and initial parametric knowledge status, we formulate a stratified binary classification task'; p.16: five-fold CV and exclusion criteria. | 说明了分析在数据集×LLM×状态组合内进行，但未使用多层模型显式处理题项/模型/数据集嵌套，故为0.5。 |
| G2 | 随机效应 | NA | — | 主要分析为固定分层/汇总与逐组合 logistic regression，未做需随机效应推广的混合模型；模型与数据集被视为固定对象，而非从总体随机抽样。 |
| G3 | 材料作为随机效应 | NA | — | 材料为固定基准题项，论文不做项目总体推广或 item random-effect 推断；各数据集分别分析，故不适用。 |
| G4 | 统计功效 | 0.5 | p.15: hyperparameter search stabilizes at M=20, N=100; p.8: reports percentage changes but no CIs; no formal power analysis. | 有采样数/ paraphrases 的稳定性论证，但不是目标功效分析，且结果缺置信区间，故为0.5。 |
| G5 | 研究者自由度 | 0.5 | p.7: discard cases not exceeding dummy baseline; p.16: exclude combinations with <50 examples or <10 per class; Figure 10 reports full Macro-F1 changes. | 报告了主要排除规则和较多结果，但未完整区分验证性/探索性分析，也未明确所有样本量决定与中途停止规则，故为0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.2: code link exists; no mention of preregistration, registered report, or timestamped analysis plan. | 未报告任何预注册；按编码口径，适用的预注册组件缺失记0。 |
| J1 | 位置偏差 | 0.5 | p.5: Hemonc regimen–comparator pairs are permuted to reduce positional bias; p.24: Option 1-3 format. | 仅对 Hemonc 明确做位置置换，未报告各数据集选项位置分布、A/B交换翻转率或位置×正确率曲线，故为0.5。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放式生成质量；KScope 主评估是选项/状态判定，不涉及长度被误当质量的裁判偏差。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈/纠错或多轮谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 没有 LLM-as-judge 成对比较或自我偏好评分；GPT-4o 仅用于生成干扰项/摘要，不作为裁判。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.23: Figure 17 shows a three-example few-shot prompt for GPT-4o to generate incorrect options; examples and template are shown. | 使用 few-shot 生成干扰项，报告了示例数量与模板，但未说明示例来源、抽样/排列控制或多 seed 稳定性，故为0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.15: M=20 paraphrases to reduce prompt sensitivity; p.23-25: full prompts are provided; no prompt version/date or dev/test separation. | 提供完整提示词并用 paraphrases 降低敏感性，但未报告 prompt 版本、敏感性消融、dev/test 划分，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p.7: Context Length is one of the extracted context features; p.8: constrained summarization reduces length; p.17: normalized feature space. | 涉及长语境/检索语境并分析长度特征与摘要压缩，但未报告实际 token 数、关键信息首/中/尾位置操纵或位置×正确率曲线，故为0.5。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'We keep the LLMs’ sampling distributions unchanged by setting the temperature to 1'; p.15: N=100 responses and M=20 paraphrases; no top-p/top-k or seed details. | 报告了 temperature 与重复采样次数，但缺 top-p/top-k、随机种子、置信区间和闭源 API snapshot 日期，故为0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.6: temperature=1 sampling; p.4: chain-of-thought responses are sampled; no repetition rate or degeneration QC reported. | 报告了采样策略的部分信息，但未报告 repetition penalty、重复率/退化率、截断比例，故为0.5。 |
| J10 | 分词效应 | NA | — | 研究为英文单语、单脚本提示与基准，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.5: public datasets Hemonc, PubMedQA, NQ, HotpotQA; p.6: model families/sizes; no training cutoff or contamination check reported. | 未报告测试集版本与模型训练截止日期对照，也未做 n-gram/DCQ 等污染检测；按适用组件缺失记0。 |
| J12 | 基准饱和 | 0.5 | p.4: Figure 3 shows near-ceiling proportions, e.g., HotpotQA contextual Consistent Correct 96.4%/98.8%; p.16: class imbalance and dummy-baseline filtering. | 报告了分数分布和极端不平衡，但未系统比较 SOTA/天花板位置、未改用连续指标或 bootstrap CI，故为0.5。 |
| J13 | 指令遵循 | NA | — | 论文不以指令遵循为因变量；虽有输出格式要求，但研究目标为知识状态刻画，不是测量 IF。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.24: required output format '<answer>Option [number]</answer>'; p.4: invalid responses (outside support/refusal) are counted in N′. | 提示词要求结构化答案且提及无效回答，但未报告格式合法率、重试策略或把格式失败与内容错误分开，故为0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文将 knowledge status 作为 LLM 内部知识状态/NLP 构念，不主张测量人类心理学构念，也未做人类同名构念外推。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较模型规模，但未宣称涌现/突变，也未报告跨训练进展的涌现能力曲线；不触发 J17。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有通过训练/RL/best-of-N 优化 benchmark、奖励模型或 LLM-judge 的代理目标；增强策略比较不是奖励过优化范式。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.15: N=100 responses per question; p.2: code link; p.6: model families and sizes; p.8: GPT-4o evaluation; no CIs, paired tests, or exact API snapshot dates. | 报告了重复采样 N 与部分模型名称/代码，但缺置信区间、配对检验和精确 snapshot/commit 标识，故为0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 所有评估均为单轮提示/独立采样，无累积对话历史或多轮一致性评估。 |

## 编码小结
论文对知识状态的测量与 KScope 框架给出了较清晰的操作化与可复现代码/提示词，但在实验设计层面主要是描述性/基准式比较，缺少人类实验意义上的随机分配、顺序平衡、盲法与预注册；统计上多为比例、分层回归和 SHAP 汇总，未系统报告置信区间、功效分析、项目随机效应与污染检验。多数 J 类 LLM 风险只得到部分处理。
