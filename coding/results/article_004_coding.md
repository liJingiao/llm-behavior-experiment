# article_004 | How Humans and LLMs Organize Conceptual Knowledge: Exploring Subordinate Categories in Italian | 2025

研究类型概述：混合型研究：Study 1 为意大利语人类常模收集（365名Prolific被试对187个基本层具体类别的下位样例生成任务）；Study 2 为LLM/vLM基准/观察性比较，使用少量示例生成、基于困惑度的类别归纳与典型性判断，比较8个模型在12个上位类别和187个基本类别上的表现。分析单位为人类被试/类别/样例与模型/类别/提示/重复运行，而非随机分配的经典实验条件。
- **研究构念（Construct）**：概念组织、下位范畴化与典型性（conceptual organization, categorization, and typicality）｜CA 构念锚定：语义记忆（semantic memory, `trm_4a3fd79d0b083`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）
- **实验任务与范式（Task / Paradigm）**：混合型研究：Study 1 为意大利语人类常模收集（365名Prolific被试对187个基本层具体类别的下位样例生成任务）；Study 2 为LLM/vLM基准/观察性比较，使用少量示例生成、基于困惑度的类别归纳与典型性判断，比较8个模型在12个上位类别和187个基本类别上的表现。分析单位为人类被试/类别/样例与模型/类别/提示/重复运行，而非随机分配的经典实验条件。｜CA 任务锚定：语义判断任务（semantic decision task, `trm_4f240cb09f8e5`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5 §4 Setup: 'We use two LLMs families... LLaMA... Mistral... vLMs LLaVA and Idefics2'; p.7: '(i) one of the 187 basic-level categories... (ii) one of the 12 superordinate categories'. | 模型、任务和类别被作为比较因素且水平有报告，但无主动操纵程序、单位分配方式及操纵检验，故为0.5。 |
| A2 | 因变量 | 0.5 | p.3: 'produce as many exemplars as possible'; p.4: 'dominance, availability, and first occurrence... mean rank order'; p.13 Appendix A Eq.1–4; p.5 Table1 valid exemplars. | 因变量指标与计分方式明确，但未见信度/效度证据、连续指标预处理或天花板/地板控制说明，故为0.5。 |
| A3 | 控制变量 | 0.5 | p.3: '365 Italian L1 speakers... no language or attentional disorders'; p.5: 'five runs for each basic-level category'; p.15: 'top-p to 0.75... frequency and repetition penalty are set to 0'. | 报告了部分固定条件，但未系统列出控制变量清单并逐一说明控制手段，故为0.5。 |
| A4 | 混淆变量 | 0.5 | p.10 Limitations: 'Cultural Biases: Model are trained on English and/or multilingual corpora...'; 'simple string matching'; 'Exclude GPT... cannot access perplexity'. | 识别了训练语料/语言、字符串匹配和模型可得性等潜在混淆，但未系统控制或量化残余威胁，故为0.5。 |
| A5 | 调节变量 | NA | — | 无调节假设、乘积项交互检验或简单斜率分析；覆盖度和可用性差异分组是描述性分层，不构成正式调节模型。 |
| A6 | 中介变量 | NA | — | 本研究理论模型不包含中介变量，也无直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.3 Study1 exemplar generation task; p.4 metrics; p.13 Eq.1–4; p.14 Italian/English prompt; p.7 category induction and typicality sentence templates. | 关键构念均有可复现的操作程序、提示模板或计分公式，故为1。 |
| A8 | 水平数与类型 | 0.5 | p.5 lists eight models and sizes; p.3 lists 12 superordinate and 187 basic categories; p.8 defines low/medium/high productivity and &#124;Δ&#124;<0.2/0.2–0.4/>0.4. | 水平数和标签较清楚，但水平类型、连续间距/全距及中心化说明不完整，故为0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.4–8 use generation, category induction, typicality detection and multiple metrics; p.9 discussion qualitatively compares findings across tasks. | 采用多任务/多指标操作化，但未系统报告操作间会聚证据，故为0.5。 |
| A10 | 单一方法的风险 | NA | — | 主比较为人类生成范数与LLM输出/困惑度，来源不同；不存在同源自评多构念的共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 无人类或模型的随机条件分配；模型与人类分组不是实验被试间分配。 |
| B2 | 被试内设计 | NA | — | 重复类别/试次不是处理条件；未见条件顺序平衡方案，且LLM按类别独立调用。 |
| B3 | 混合设计 | NA | — | 未构成组间×组内混合实验，也未分别建立两类误差项。 |
| B4 | 因子设计 | NA | — | 非全交叉因子实验；未报告设计矩阵、每格样本量或交互统计。 |
| B5 | 主效应 | NA | — | 无因子设计主效应推断模型。 |
| B6 | 交互作用 | NA | — | 无正式交互项统计检验。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 非准实验因果设计；人类-LLM比较为观察性比较，未作因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理条件的可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无处理分配或随机化；LLM亦无随机分派条件。 |
| C2 | 平衡 | NA | — | 无条件顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.15: 'top-p to 0.75... frequency and repetition penalty are set to 0'; p.14 gives fixed prompt; p.5 same 187 categories. | 固定了部分提示与解码设置，但未系统列出全部恒定变量及外部效度限制，故为0.5。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未将已知混淆变量作为区组或协变量纳入模型。 |
| C6 | 盲法 | NA | — | 无实验条件盲法或评分者盲法安排。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA顺序层级。 |
| D1 | 练习效应 | NA | — | 无练习块或处理条件顺序设计；LLM每类别独立调用。 |
| D2 | 疲劳效应 | NA | — | 无跨条件时序处理；人类任务约15分钟单session，未构成处理效应混淆。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件清洗期或迁移效应设计。 |
| D4 | 不对称迁移 | NA | — | 无迁移对称性检验需求。 |
| D5 | 范围效应 | NA | — | 无主观量表式绝对判断或范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0 | p.3: 'Each participant is presented with a list of 15-16 categories'; no randomization/counterbalancing of category or item order is reported. | 存在人类被试内多类别呈现与生成序列，但全文未报告类别/项目顺序随机化或反平衡，故为0。 |
| E2 | 默认赞同 | NA | — | 不使用Likert或态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 任务为客观样例生成，无明显掩饰情节或假设推断空间。 |
| E5 | 实验者效应 | NA | — | 数据在线自动采集，无人类主试/评分者直接接触。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5 Table1 reports valid-exemplar percentages; p.7/p.19 report category-induction accuracy up to 0.98; no SD/skew/endpoint frequency or pilot calibration. | 报告了均值/百分比并能看到部分端点，但未报告SD、偏度、端点频率或难度校准，故为0.5。 |
| E7 | 共同方法偏差 | NA | — | 无同源自评多构念测量，不涉及共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | p.4 reports correlations 'rs = 0.95, 0.75, 0.89'; p.5/p.7 report accuracy tables; no confidence intervals, power analysis, or multiplicity correction. | 报告了相关系数与描述性效应量，但缺样本量依据、置信区间、多重性校正和统计假设检验说明，故为0.5。 |
| F2 | 内部效度 | NA | — | 观察性/基准比较设计，无随机分配与因果推断主张。 |
| F3 | 构念效度 | 0.5 | p.4 reports correlations among norm metrics; p.5–8 use multiple tasks; p.9 discusses limitations, but no formal reliability/validity or manipulation check. | 提供部分构念指标间关联与多任务证据，但缺正式信效度与操纵检验，故为0.5。 |
| F4 | 外部效度 | 0.5 | p.10 gives Prolific sample demographics and limitations ('Cultural Biases...'); no cross-sample/cross-language replication. | 报告了样本来源与特征并讨论文化边界，但未报告跨样本/跨情境复现，故为0.5。 |
| G1 | 分析单位 | 0.5 | p.3 describes 365 participants; p.5 describes five runs per model/category; p.4/p.5 analyses aggregate to category/model level. | 描述了数据层级，但分析按类别/模型汇总，未显式处理样例、类别、重复运行与被试的嵌套结构，故为0.5。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；特定模型被视为固定比较对象，人类数据被汇总为常模，无被试随机效应推断需求。 |
| G3 | 材料作为随机效应 | 0 | p.3 uses 187 basic-level concrete categories; p.5 models receive 'the same 187 basic-level concepts'; p.7 selects up to 10 most available exemplars; analyses average by category. | 材料/类别作为有限固定刺激集合，未将项目作为随机效应或使用准F/混合模型，存在语言作为固定效应问题，故为0。 |
| G4 | 统计功效 | 0 | p.3 reports 365 participants; p.5 reports five runs; no a priori power analysis or sample-size justification is reported. | 无事前功效分析或样本量依据，且主要比较缺CI，故为0。 |
| G5 | 研究者自由度 | 0.5 | p.3 reports 24,659 exemplars after typo cleanup; p.4 applies dominance≥0.1 yielding 1,696 exemplars; p.5 describes duplicate removal and valid-exemplar cleaning. | 报告了部分排除/清洗规则和多数测量，但未明确区分验证性与探索性分析，也未说明停止/追加规则，故为0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1 footnote only states 'Data and code is available on GitHub and OSF'; no preregistration or registered analysis plan is reported. | 无预注册，无法区分预注册验证性分析与事后探索性分析，故为0。 |
| J1 | 位置偏差 | NA | — | 候选类别通过分别计算困惑度选择，不涉及候选在提示中的位置顺序或成对呈现位置；无LLM-as-judge位置偏差。 |
| J2 | 冗长偏差 | NA | — | 评估基于有效样例、匹配率和困惑度，不使用LLM裁判对开放生成长度/质量评分。 |
| J3 | 谄媚 | NA | — | 无用户立场、反馈或纠错的对话式评估。 |
| J4 | 自我偏好 | NA | — | 不涉及LLM-as-judge或成对比较中的自我偏好。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.5: 'The instruction is followed by a question-answer example'; p.14 full prompt includes one 'elettrodomestico' example with four exemplars; p.5 five runs per category. | 报告了单一固定few-shot示例与模板，但未报告示例抽样、排列反平衡、多seed或示例来源控制，故为0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.14 provides the complete Italian prompt and English translation; p.15 gives top-p/penalty settings; no prompt-version ablation or dev/test split is reported. | 公布完整模板，但无版本化、敏感性消融和dev/test划分说明，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务提示很短，无长文档或RAG设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.15: 'top-p to 0.75... frequency and repetition penalty are set to 0'; p.5: 'five runs for each basic-level category'; temperature, seed and CI are not reported. | 报告了部分采样超参与重复次数，但缺温度、种子及重复采样置信区间，故为0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.5 describes removing duplicate exemplars and keeping first occurrences; p.15 reports sampling penalties; no n-gram repetition/degeneration rate is reported. | 报告了部分解码/清洗策略，但未报告重复率或退化率，故为0.5。 |
| J10 | 分词效应 | NA | — | 研究为单语言意大利语，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | p.10: 'Since the human data were collected in 2023 and never released, all LLMs have not been exposed to these stimuli'. | 使用自建且未公开的人类数据作为held-out测试材料，并明确说明未被模型接触，故污染风险按NA处理。 |
| J12 | 基准饱和 | 0.5 | p.7 Table3 basic-level category induction accuracy reaches 0.98; p.19 Table9 basic-level average up to 0.98; no saturation discussion or continuous metric. | 报告了准确率并可见近天花板表现，但未识别饱和问题或改用连续指标/CI比较，故为0.5。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；任务输出评估的是样例有效性与类别结构。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.5: generated responses are 'a list of exemplars separated by newlines'; duplicate removal described; p.14 prompt asks for entity names; no format-legal rate. | 有格式约束与清洗，但未报告格式合法率、重试策略或把格式失败与内容错误分开，故为0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或对齐评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1–2 frames LLMs as models of human cognition and category organization; p.9 cautions about extrapolation; p.13 reports model versions/links. | 明确比较LLM与人类构念并使用同一范式，但权重快照/构念效度论证仍不完整，故为0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较不同规模LLaMA模型，但未报告跨规模/训练进展的涌现曲线，也未作涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL、best-of-N或针对代理指标的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5: 'For each model, we perform five runs for each basic-level category'; p.13 provides HuggingFace links/model names; no CIs, paired tests or exact snapshot/commit identifiers. | 报告了重复次数和模型名称链接，但缺置信区间、配对检验和精确snapshot，故为0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮提示/单类别调用，不涉及多轮对话历史累积。 |

## 编码小结
论文提供了较完整的人类下位类别样例数据集、任务定义和提示模板，并将人类与多个LLM/vLM在相同范式下比较；但其设计本质上是常模收集加基准评测/观察性比较，缺少随机分配、正式因子交互检验、项目随机效应、置信区间、预注册与功效分析等实验心理学质控要素。多个人类实验设计组件不适用，LLM评测组件部分适用但报告不完整，因此总体证据强度偏描述性。
