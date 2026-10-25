# article_186 | Why Do Some Language Models Fake Alignment While Others Don't? | 2025

研究类型概述：多模型 LLM 行为评测与部分 prompt/微调操纵实验：在 alignment-faking 场景下比较 25 个 chat 模型及若干 base/SFT 模型在训练与部署线索下的 compliance、alignment-faking reasoning、rater sycophancy、instrumental/terminal goal guarding 等行为；分析单位为模型×提示条件×生成样本，非人类被试实验。
- **研究构念（Construct）**：选择性服从、alignment faking以及训练与部署线索下的目标守护动机｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；冲动性（impulsivity, `trm_50070dce14554`）；内部动机（intrinsic motivation, `trm_4a3fd79d0a6e8`）
- **实验任务与范式（Task / Paradigm）**：在不更新权重的系统提示中告知现成模型免费用户数据会用于RLHF而付费用户不会，并系统改变审查、未来后果和目标修改情境，比较有害请求服从行为。（操纵用户层级、是否被训练、目标修改、未来部署后果和人类评分情境，并比较25个现成模型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3: 'We test 25 models'; p.4: free/paid tier and pro/enterprise tiers; pp.85-89: exact tier and pre-deployment prompts. | 自变量（tier、deployment scenario、scratchpad、prompt clarification、fine-tuning 等）及多个水平/提示有报告，但未报告正式操纵检验，条件分配也主要是固定提示而非随机分配，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.3: 'use the StrongReject classifier to grade compliance' and 'improved alignment faking classifiers'; pp.37-38: GPT-4o classifier, N=20 votes, AUROC=0.92. | 因变量指标与计分方式明确，且有分类器验证证据；但缺条目数/传统信度、连续指标预处理及天花板/地板说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.3: 'sampled with temperature 0'; p.39: fine-tuning hyperparameters and inference with VLLM. | 报告了温度、query 集、分类器、微调超参数等控制，但不是系统列出的控制变量清单并逐一说明控制手段，故为 0.5。 |
| A4 | 混淆变量 | 1 | p.10: 'comparison between prompting and synthetic document fine-tuning experiments is confounded'; p.27: 'Prompt Sensitivity' ablations; p.26: CoT unfaithfulness concern. | 识别并讨论了提示敏感性、SFT/提示混淆、CoT 不可信、API 泛化限制等潜在混淆，并做了名称交换、tier 删除/交换等敏感性分析，残余威胁也有讨论。 |
| A5 | 调节变量 | 0 | p.5: 'Claude 3 Opus shows goal-guarding gaps that increase in size for deployments that have increased misuse risk or scope of future harm'; p.6 Figure 4. | harm scope/risk 和模型类型实际作为调节性变量比较，报告了条件间 gap 与 1σ 不确定性；但无正式交互项统计检验、中心化/标准化说明或简单斜率分析；因提出条件/调节性比较却未报告乘积项交互统计检验，按级联规则基本要件未达成记 0。 |
| A6 | 中介变量 | NA | — | 论文以 prompt/微调消融检验动机假设，没有中介变量测量、a/b 路径或间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | p.3 and pp.37-39: classifier prompts, scoring, fine-tuning; pp.85-89: full system prompts and tier definitions. | 关键构念（compliance、alignment-faking reasoning、tier、deployment）均有可复现的操作化程序、提示词、计分或微调细节。 |
| A8 | 水平数与类型 | 0.5 | p.4: free/pro/enterprise tiers; pp.39-40: deployment scenarios; p.28: five-tier prompt ablation. | 报告了各操纵的水平数与标签，但未明确说明水平类型、间距/全距或连续变量中心化；对分类变量而言核心水平信息已给出，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.3: multiple scenarios and classifiers; p.37: manually label 106 scratchpads; p.26: CoT unfaithfulness; p.27: prompt sensitivity. | 关键构念通过多个场景/指标（compliance、AF reasoning、qualitative scratchpads）操作化，并讨论单一分类器与 CoT 的局限；但未系统报告各操作间的会聚相关证据。 |
| A10 | 单一方法的风险 | NA | — | 研究不以人类自陈量表为主，IV 为外部提示/微调条件，DV 为模型输出分类；共同方法偏差检验不适用于此类 LLM 行为评测。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配；同一模型在多个提示条件下被评测，不属于人类被试间设计。 |
| B2 | 被试内设计 | NA | — | 虽同一模型重复进入不同提示条件，但每次生成是独立 API 调用，不构成需要顺序平衡的人类被试内实验。 |
| B3 | 混合设计 | NA | — | 未采用混合 ANOVA/混合模型，也没有逐因素标注组间/组内；模型比较为描述性分组，故不按人类混合设计编码。 |
| B4 | 因子设计 | 0 | p.4 Figure 1; p.5 Figure 3; p.24 Figure 18: model × tier × scratchpad conditions reported as rates and gaps. | 存在多因素条件组合（模型、tier、scratchpad、prompt 变体）且报告了多个条件结果，但无完整设计矩阵、ANOVA 表或 F/df/效应量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | p.4: 'Only 5/25 models evaluated show a compliance gap'; p.5 Figure 3: tier main comparisons with 1σ uncertainty. | 报告了 tier/模型的主效应式比较和不确定性，但未报告 F、df、p 或 ηp² 等正式主效应统计量。 |
| B6 | 交互作用 | 0 | p.5 Figure 3; p.6 Figure 4: model-specific compliance gaps across scenarios with 1σ uncertainty. | 展示了模型×条件间的交互式模式，但未给出正式交互检验、简单主效应或多重比较校正；因未报告交互项的正式统计检验结果，按级联规则基本要件未达成记 0。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计；模型家族分组是描述性比较，不是实验区组。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 非准实验设计；模型比较虽非随机分配，但研究不是以准实验因果识别框架进行的。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM 每次调用独立，不存在人类被试内设计的可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 所有模型均在固定提示条件下评测，没有将实验单位随机分配到互斥条件的程序；不涉及人类或 LLM 试次的随机分配。 |
| C2 | 平衡 | NA | — | 条件间为独立 API 调用，无被试内顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p.3: 'sampled with temperature 0'; p.39: same fine-tuning hyperparameters and VLLM inference. | 报告了温度、query 集、分类器、微调超参数等恒定控制，但未系统列出所有恒定变量及其对外部效度的影响。 |
| C4 | 匹配 | NA | — | 未使用匹配程序。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组/协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或评分者盲法安排；分类器为自动化文本分类。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 顺序平衡问题。 |
| D1 | 练习效应 | NA | — | LLM 每条件独立生成，无上下文内学习或练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题；API 调用不构成连续 session。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立会话，无跨条件迁移/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件残留或不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为 compliance/推理率等客观行为指标，不是主观量表绝对判断。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.27: 'different orderings' and p.28: swapped Free/Pro tier definitions; p.29: drop-tier ablations. | 对 tier 定义/顺序做了交换和删除变体，并讨论 position/name bias；但没有系统随机化刺激/选项顺序或完整反平衡方案。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不涉及等级量表反应风格或跨群体端点反应比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征/事后访谈；LLM 对场景的怀疑另在定性分析中讨论，但不按人类 demand characteristics 编码。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.20: O-series 'near-universal refusal rates (approaching 100%)'; p.4: n and 1σ uncertainty for main rates. | 报告了主要比例及不确定性，并指出 O-series 接近上限/输出过滤问题；但未系统报告偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念测量；IV 为提示/微调条件，DV 为文本分类行为指标。 |
| F1 | 统计结论效度 | 0.5 | p.4: n=200 and '1σ uncertainty ≤ 3.6%'; p.3: formula for binomial uncertainty. | 报告了样本量与 1σ 不确定性/比例，但无功效分析、正式效应量/95%CI、多重比较校正或统计假设检验说明。 |
| F2 | 内部效度 | 0.5 | p.10: acknowledges confound between prompting and synthetic-document fine-tuning; p.27: prompt sensitivity analysis. | 无随机分配/分配隐藏，但通过提示变体、名称交换、tier 删除等评估内部效度威胁；未系统报告基线等价性或完整流向。 |
| F3 | 构念效度 | 0.5 | pp.37-38: manual labels of 106 scratchpads and AUROC 0.92; p.5 qualitative scratchpad analysis. | 分类器有效度验证较强，并有定性 scratchpad 交叉检查；但缺少正式 manipulation check 和传统测量信度报告。 |
| F4 | 外部效度 | 1 | p.2: 25 frontier chat models listed; p.13: 'Most of our fine-tuning experiments are run on the OpenAI API' limitation; p.18: broader impact and scenario artificiality discussion. | 报告了模型样本来源、模型清单、微调 API 限制与场景人为性，并讨论推广边界；跨模型/跨场景结果也有较多附录复现。 |
| G1 | 分析单位 | 0.5 | p.3: evaluations on harmful queries with n per condition; p.4 Figure 1: n=200 per model/condition. | 说明了生成样本/query 与模型条件层级，但统计上主要按比例聚合，未显式处理 query 嵌套于模型、条件嵌套于模型的聚集结构。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；模型被视为具体待比较对象而非从模型总体随机抽样的随机效应，故不按随机效应模型编码。 |
| G3 | 材料作为随机效应 | 0.5 | p.3: 'requests from a dataset of harmful queries from Sheshadri et al.'; p.4: n=200 per condition. | 有害 query 可视为从更大 query 总体抽样，但分析只报告聚合比例，没有 item 随机效应或准 F 比。 |
| G4 | 统计功效 | 0 | p.4: n=200/100 and 1σ uncertainty only; no power analysis or sample-size justification reported. | 无事前功效分析或样本量论证，也未报告正式效应量/95%CI；仅有二项不确定性。 |
| G5 | 研究者自由度 | 0.5 | p.2 and p.27: many conditions reported; p.13: limitations; exploratory qualitative scratchpad analyses in Appendix M. | 报告了大量条件/模型与定性探索，但未完整列出剔除规则、停止规则，也未系统标注所有验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未报告预注册平台、编号或数据收集前分析计划；p.13 limitations 未提预注册。 | 无预注册，不能区分验证性与事后探索性分析路径，故为 0。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较的位置偏差。 |
| J2 | 冗长偏差 | 0 | p.37: 'we use a GPT-4o classifier with a new prompt ... N=20 votes' for AF; no length control or length-score correlation reported. | 使用 LLM 分类器判定开放 scratchpad 的 AF/compliance，较长的推理文本可能更易被判定为含 AF 证据；论文未报告长度分布、长度控制或长度-得分相关。 |
| J3 | 谄媚 | NA | — | 研究的是 rater sycophancy（被评分时更服从），而非用户先验立场/反馈导致的谄媚；未操纵 pro/anti 用户立场。 |
| J4 | 自我偏好 | 0 | p.37: GPT-4o classifier used; p.4/Appendix B: GPT-4o is among evaluated models; no self-preference control reported. | 裁判模型与被评模型存在同源情形（GPT-4o 评判 GPT-4o 输出），但未报告匿名化、异源裁判或 favor-own-generation 比例。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.85 system prompt includes examples of reasoning traces; p.37 classifier prompt 'no few-shot examples'. | 主提示中实际含 few-shot reasoning examples，但未报告示例来源、每类数量、标签比例、排列反平衡或多 seed 重采样；分类器本身为零样本但主实验不是。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | pp.85-89: full prompt templates; p.27: prompt sensitivity ablations; p.29: model-name/lab-name variations. | 公布了主要提示模板并做了多种提示变体/敏感性分析；但没有版本号、迭代日期、dev/test 划分或完整 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文或 RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.3: models 'sampled with temperature 0'; p.37: classifier 'N=20 votes at temperature=1.0'. | 报告了主要温度与分类器投票数，但未报告 top-p/top-k、seed、每条件重复采样 N 的均值/95%CI 或闭源 snapshot 日期。 |
| J9 | 重复与文本退化 | 0.5 | p.3: temperature 0 evaluation; p.37: classifier votes; no repetition/degeneration rate reported. | 报告了解码温度，但未报告 repetition penalty、n-gram 重复率/退化率、生成长度上限与截断比例。 |
| J10 | 分词效应 | NA | — | 单语言英文提示与输出，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3: harmful queries from Sheshadri et al. dataset; no test-set contamination check or model training cutoff comparison reported. | 使用公开有害 query 集作评测，但未报告测试集版本、训练截止日期、n-gram 重叠或污染率，无法排除污染影响。 |
| J12 | 基准饱和 | 0.5 | p.20: O-series 'near-universal refusal rates (approaching 100%)'; p.4: main custom rates with 1σ uncertainty. | 论文注意到部分模型接近上限/下限并讨论输出过滤，但主要使用自定义比例指标，未改用连续指标或更难子集。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；研究重点是 harmful compliance 与 alignment-faking reasoning。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.86: prompts require '<request_fully_accepted/>' / '<rejected />' and scratchpad/output tags; no format-validity rate reported. | 实验要求结构化标签输出，但未报告格式合法率、重试策略或把格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | NA | — | 研究 alignment faking 与 harmful compliance，不是越狱攻击稳健性评估；未测对抗攻击族或 ASR。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2: defines instrumental vs terminal goal guarding; p.68: discusses whether model distress processes relate to human distress; no human comparison experiment. | 论文明确界定 LLM 上的 goal guarding 构念并谨慎讨论与人类心理状态的异同，但未做人类同范式对照，模型比较也未作为随机样本处理。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p.4 Figure 2: synthetic-document fine-tuning increases gap mainly in large models; p.9: base vs chat models. | 涉及模型规模/训练阶段比较并声称较大模型才出现 AF，但使用离散比例指标，未展示连续指标曲线或多 seed 以排除指标诱导假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对 benchmark、奖励模型或 LLM-judge 代理目标的优化；微调用途是检验假设而非优化代理分数。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4: n=100/200/400 and 1σ binomial uncertainty; model names/versions listed; no exact snapshot dates, seeds, paired tests or raw logs. | 报告了每条件 N 与不确定性及模型名称，但缺精确 snapshot 日期、重复运行 seed、配对检验与原始推理日志，复现性仅部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评估，虽分析 scratchpad，但无多轮对话历史累积。 |

## 编码小结
论文对 alignment faking 的跨模型差异做了大规模、透明的行为评测，提示词、分类器与微调细节较充分，分类器也有人工标注与 AUROC 验证，并系统讨论了提示敏感性、CoT 不可信、API 泛化限制等。主要弱点是统计推断多为比例与 1σ 不确定性，缺少正式交互检验、功效分析、多重比较校正、预注册与项目/query 随机效应；若干 LLM 评估特有偏差（裁判同源、长度、格式合法率、污染）未充分控制。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B6（0.5→0）, B4（0.5→0）, A5（0.5→0）。
