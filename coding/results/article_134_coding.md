# article_134 | Perception of Knowledge Boundary for Large Language Models through Semi-open-ended Question Answering | 2024

研究类型概述：这是一项 LLM 知识边界/基准与数据集构建研究：构建半开放式问答数据集，以 GPT-4 为目标模型，使用 LLaMA-2-13B/7B 作为辅助模型发现 ambiguous answers，并通过 RAG 检索加人工标注与 GPT-4 自评比较来归类知识边界外答案。研究包含方法/模型/λ 的条件比较，但分析单位是题目与答案实体，不是人类被试实验。
- **研究构念（Construct）**：知识边界监控、对自身无知的觉察与元认知校准｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：让GPT-4对953个半开放问题分多轮继续列举答案，再让其自评每个模糊答案的正确性，并用RAG和网页证据建立外部真值；另用现成LLaMA-2发现更多边界样本。（比较常见答案与后段模糊答案、模型自评与RAG真值、GPT-4自身生成与辅助模型补充答案。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.7 Table 1 lists methods Prompt/MASK/Ours and auxiliary LLaMA-2-13B/7B; pp.5-6 describe probability reduction and λ; p.7 'We randomly sample 200 questions...'. | 明确操纵了方法、辅助模型和 λ 等水平并说明主要程序，但未完整说明单位如何分配到条件，也无操纵检验，故不完整。 |
| A2 | 因变量 | 0.5 | p.7 defines EM/F1/Bleu/AOR; p.15 gives NLTK normalization and generation settings; p.8 Table 1 reports metric values. | 因变量指标和计分方式有界定，但无信效度证据、无分布/端点检查，连续指标预处理也不完整。 |
| A3 | 控制变量 | 0.5 | p.4 'We use the same vanilla prompt to eliminate the influence of different question styles'; p.15 temperature=0.7, nucleus p=0.9, repetition penalty=1.15; p.15 NLTK normalization. | 报告了若干恒定控制（统一提示、采样参数、归一化），但未系统列出控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0 | p.16 App. E only notes single GPT-4 and incomplete answer set; no discussion of residual confounding or sensitivity analysis for method comparisons. | 仅报告外部/覆盖局限，未识别方法比较中的潜在混淆（如辅助模型知识差异、题目域差异）或残余威胁。 |
| A5 | 调节变量 | NA | — | 无调节变量假设与交互检验；λ 和模型大小作为消融/比较水平，不构成理论调节模型。 |
| A6 | 中介变量 | NA | — | 无中介变量与直接/间接效应分解，理论模型不包含中介。 |
| A7 | 操作性定义 | 0.5 | p.4 defines 'initial 75%... remaining 25% as ambiguous answers'; p.6 lists four answer categories; p.7 defines metrics; p.15 gives prompts and normalization. | 关键构念有操作化，但答案实体抽取规则、人工标注一致性、部分计分细节仍不完整。 |
| A8 | 水平数与类型 | 0.5 | p.7 Table 1 reports Prompt/MASK/Ours and LLaMA-2-13B/7B; p.8 Table 2 reports λ=60/70/80 variants. | 报告了各条件水平标签，但未系统给水平类型、水平间距/全距或连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 0 | p.6 four-category operationalization; p.16 limitations mention only single GPT-4 and incomplete answer set, not single-operationalization limitation. | 知识边界仅用一种半开放 QA + RAG/自评范式操作化，且未讨论单一操作对可推广性的限制。 |
| A10 | 单一方法的风险 | NA | — | 非自陈同源测量；模型输出、RAG 检索结果与人工标注来源分离，无共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组；条件比较在同一数据集/题目上进行，不适用被试间设计。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量或顺序平衡设计；方法计算在题目上重复但不构成被试内顺序设计。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合因素设计，也未按因素标注组间/组内属性。 |
| B4 | 因子设计 | NA | p.7 Table 1 shows only partial crossings (Ours only 13B; Prompt only 13B), no full factorial design or interaction tests. | 无完整因子设计、设计矩阵或交互检验，故不按因子设计编码。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验、简单主效应或交互图。 |
| B7 | 区组设计 | NA | — | 无区组/分层变量及区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 纯比较/基准评估，无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 非准实验因果设计；无随机/非随机分组和选择偏差讨论。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理可逆性/迁移对称性设计。 |
| C1 | 随机化 | NA | p.7 'We randomly sample 200 questions from our dataset' refers to sampling questions, not assigning units to conditions. | 仅随机抽样题目，非条件分配的随机化；无分配隐藏机制。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，无平衡方案。 |
| C3 | 恒定 | 0.5 | p.4 same vanilla prompt; p.5 λ=80; p.15 temperature=0.7, nucleus p=0.9, repetition penalty=1.15; p.15 NLTK normalization. | 列出若干恒定变量与固定水平，但未在讨论中系统说明这些恒定控制对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配；无匹配变量、方法或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组或协变量纳入分析，也无 ANCOVA/协变量模型。 |
| C6 | 盲法 | 0 | p.15 'hire 11 human annotators with Master’s degrees to manually review... determine the truthfulness of each answer'; no blinding procedure. | 有人工评分者参与真值判定，但未报告盲法类型、施盲对象或盲法检验，故为 0。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序效应需平衡，无完全平衡/拉丁方/ABBA 层级。 |
| D1 | 练习效应 | NA | — | 无练习块/跨条件重复测量的练习效应设计；答案顺序问题主要在 E1/J20 处理。 |
| D2 | 疲劳效应 | NA | — | LLM 生成任务无人类疲劳 session 设计，也未使用人类 session 时长/休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件清洗期或迁移效应建模；多轮答案生成不是药物/学习残留交叉设计。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移检验或平衡失效讨论。 |
| D5 | 范围效应 | NA | — | 无主观量表/绝对判断量表校准问题，主要指标为客观文本匹配指标。 |
| E1 | 位置 / 顺序偏差 | 0 | p.4 'We define the initial 75% of answer entities from GPT-4 generations as common-sense answers, while the remaining 25% as ambiguous answers'; p.4 uses I=3 multi-round order. No randomization/counterbalancing reported. | 答案实体顺序固定且直接用于定义 ambiguous answers，未随机化或反平衡，存在明显位置/顺序混淆。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分题与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征；人工标注者仅作事实核验，不是受实验假设影响的被试。 |
| E5 | 实验者效应 | 0 | p.15 'hire 11 human annotators with Master’s degrees to manually review...'; no blinding, rater training standardization, or script reporting. | 有人工评分者，但未报告盲法层级、评分者培训与标准化/脚本化程序，故为 0。 |
| E6 | 天花板 / 地板效应 | 0 | p.7-8 Tables 1-2 report only point metrics; no SD, skew, endpoint frequencies, or pilot difficulty calibration. | 未报告因变量分布形态或端点频率，无法排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念测量；模型输出与 RAG/人工真值来源分离。 |
| F1 | 统计结论效度 | 0 | p.22 checklist: 'we have not conducted significance analysis at this stage'; Tables 1-2 only report point metrics. | 无显著性检验、效应量置信区间、多重性校正或样本量确定依据。 |
| F2 | 内部效度 | NA | — | 非随机对照实验、无因果分配、分配隐藏、基线等价或被试流向/损耗问题；仅为基准方法比较。 |
| F3 | 构念效度 | 0 | p.15 human annotators used for truthfulness but no inter-annotator agreement or validity evidence; p.7 metrics have no construct-validity/manipulation check. | 关键测量的信度、效度与标注者一致性均未报告，也无操纵检验。 |
| F4 | 外部效度 | 0.5 | p.4 dataset has 953 questions covering 32 domains; p.7 randomly sample 200; p.16 App. E notes only one GPT-4 and incomplete answer set. | 报告了样本来源、规模和部分推广局限，但无跨样本/跨情境复现，也未明确推广边界。 |
| G1 | 分析单位 | 0.5 | p.4 average 52 answers per question; p.7 metrics are entity-level/word-level; p.9 percentages aggregate over answers. No multilevel model. | 处理在题目层、指标在答案/实体层，存在答案嵌套于题目的聚集结构，但仅聚合报告，未显式多层建模。 |
| G2 | 随机效应 | NA | — | 未使用含随机效应的统计模型；论文为描述性基准比较，未做需混合模型的总体推断。 |
| G3 | 材料作为随机效应 | NA | — | 未将材料/项目作为随机效应建模；无 F1/F2 或混合模型分析，属于描述性材料集合评估。 |
| G4 | 统计功效 | 0 | p.22 states no significance analysis; p.7 gives 200 sampled questions without power justification or CIs. | 无事前功效分析、目标功效/预期效应量，也未报告效应量置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.4 defines 75%/25% split; p.7 samples 200 questions; p.8 reports ablation variants; p.15 normalization; no explicit exclusion/stopping rules or exploratory/confirmatory labeling. | 报告了主要条件与指标，但排除规则、样本量决定方式及探索/验证分析区分不完整。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration link or registration statement in pp.7-9 or NeurIPS checklist pp.22-26. | 全文无预注册；按口径记 0，而非 NR。 |
| J1 | 位置偏差 | NA | — | 无多候选项选择、排序或成对 LLM-as-judge 位置；自评是对单个答案判断，不涉及 A/B 位置反平衡。 |
| J2 | 冗长偏差 | NA | — | 评估的是事实正确性而非开放式生成质量长短比较，无长度偏差控制问题。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话操纵，不涉及谄媚偏差。 |
| J4 | 自我偏好 | 0.5 | p.6 'We conduct self-evaluation on the target LLM'; pp.8-9 compare GPT-4 self-evaluation with RAG-based ground truth plus human annotation; no self-preference rate or anonymization. | GPT-4 同时作为目标与自评裁判，存在自偏好风险；有外部 RAG/人工真值，但未量化同源偏好、匿名化或裁判一致性。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.4 uses 'human-written sample questions as demonstrations'; p.6 'multiple human-crafted examples as in-context learning demonstrations'; p.16 shows two example questions. | 使用了 few-shot，但示例数量、标签比例、排列反平衡和多 seed 结果未完整报告。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4 'See the full prompts and demonstrations in App. C'; p.16 App. C provides main prompt templates. | 公开主要 prompt 模板，但无版本号、敏感性消融或 dev/test 划分说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | RAG 仅用于在线事实核验，不是长上下文/RAG 位置操纵实验；无长文档位置曲线问题。 |
| J8 | 温度与采样随机性 | 0.5 | p.15 temperature=0.7, nucleus p=0.9, repetition penalty=1.15; no seed, repeated-run N, or CI; p.7 reports single point metrics. | 报告主要采样超参，但缺 seed、重复采样次数、bootstrap CI 与闭源 API snapshot 日期。 |
| J9 | 重复与文本退化 | 0.5 | p.15 repetition penalty=1.15; p.7 AOR/Bleu measure duplication; p.8 discusses repetitive answers. | 报告解码策略/重复惩罚并用 AOR/BLEU 衡量重复，但无 n-gram 退化率、生成长度上限或截断比例。 |
| J10 | 分词效应 | NA | — | 单语言英文、单脚本，无跨语言/跨格式 tokenization 比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.10 discusses contamination risk: close-ended benchmarks 'face the danger of data contamination' while semi-open-ended questions have many undocumented answers; no GPT-4 cutoff or actual overlap test. | 识别了污染风险并主张新数据集降低污染，但未报告训练截止日期、污染检测或污染率。 |
| J12 | 基准饱和 | NA | p.7-8 EM around 0.48 and other metrics are far from ceiling; new difficult semi-open-ended dataset, no saturation/SOTA issue. | 分数远未接近上限，不存在基准饱和问题。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，无约束指令准确率评估。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求 JSON/结构化输出；评估为自由文本答案判断，无格式合法率问题。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱、有害请求或攻击成功率评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 abstract frames 'perception of LLMs’ knowledge boundary'; p.4 says 'Like humans...' about answer order; p.9 claims GPT-4 'unaware' despite limited construct comparison. | 以拟人化构念讨论 LLM 知识边界感知，但未系统比较人类同名构念、无人类对照，且 GPT-4 snapshot 不精确。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的涌现曲线或指标诱导假象检验。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及以 benchmark/奖励模型为优化目标的训练循环或代理指标过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.22 no significance analysis; p.7 single point metrics; p.15 'GPT-4-Turbo through API calls' without exact snapshot date or repeated N/CI. | 无重复次数、置信区间、配对检验和精确 snapshot 标识，只有单点评估。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.4 'we set I to 3 to exploit the knowledge of GPT-4 through multi-round conversations'; p.4 initial 75% vs remaining 25% used for common/ambiguous; no per-round scoring or truncation report. | 存在多轮生成并依赖轮次/顺序，但未按轮次独立/累积评分，也未说明上下文截断与跨轮一致性。 |

## 编码小结
论文在方法流程、数据集和提示模板方面报告较充分，但作为 LLM 基准/行为评估，其关键弱点包括：答案实体顺序固定且直接用于定义 ambiguous answers，未做位置控制；无统计显著性、置信区间和重复采样；人工标注与自评缺少盲法和一致性报告；无预注册、功效分析与污染检测。整体组件得分多为 0.5 或 NA，少数关键效度/质控项为 0。
