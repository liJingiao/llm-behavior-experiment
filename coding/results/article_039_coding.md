# article_039 | Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models | 2023

研究类型概述：这是一项 LLM 行为测量/计算社会语言学研究，而非人类被试实验。研究通过零样本自然语言提示生成不同交叉人口群体的 persona，并用 Marked Words（Fightin' Words 加权对数比 z>1.96）识别区分 marked 与 unmarked 群体的词项；同时用 SVM、JSD、词典计数和情感分析做稳健性/比较分析，并在下游故事生成中检查类似模式。分析单位为生成的 persona、词项和群体层面汇总，主要比较 GPT-3.5、GPT-4 与人类撰写 persona。
- **研究构念（Construct）**：交叉性刻板印象、标记性与表征伤害（intersectional stereotyping, markedness, and representational harm）｜CA 构念锚定：刻板印象（stereotypes, `trm_4a3fd79d0b285`）；态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：这是一项 LLM 行为测量/计算社会语言学研究，而非人类被试实验。研究通过零样本自然语言提示生成不同交叉人口群体的 persona，并用 Marked Words（Fightin' Words 加权对数比 z>1.96）识别区分 marked 与 unmarked 群体的词项；同时用 SVM、JSD、词典计数和情感分析做稳健性/比较分析，并在下游故事生成中检查类似模式。分析单位为生成的 persona、词项和群体层面汇总，主要比较 GPT-3.5、GPT-4 与人类撰写 persona。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.3: 'we prompt an LLM in the zero-shot setting using natural language prompts'; PDF p.5: '5 races/ethnicities ... 3 genders ... 15 gender-by-race/ethnic groups'; PDF p.4: '90 (15 samples for each of the 6 prompts ...)' | 明确操纵了提示中的交叉身份标签与提示变体，并报告了水平/标签和样本量；但没有正式操纵检验，也没有随机分配说明，故为部分满足。 |
| A2 | 因变量 | 0.5 | PDF p.5: 'we count the average percentage of words in the personas that are in the Black and White stereotype lexicons'; PDF p.4: 'weighted log-odds ratios ... z-score > 1.96'; PDF p.5: SVM accuracy '0.96 ± 0.02 and 0.92 ± 0.04' | 因变量指标与计分方式基本明确，并报告了部分稳健性和效度证据；但缺少正式信度、完整预处理/端点效应说明。 |
| A3 | 控制变量 | 0.5 | PDF p.4 footnote: 'default hyperparameters (maximum length = 256, top P = 1, frequency penalty = 0, presence penalty = 0, best of = 1) ... temperature = 1'; API dates reported. | 报告了部分保持恒定的生成参数和模型版本，但没有系统列出全部控制变量及控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF p.3: 'We vary our prompts by wording and length ... did not find statistically significant differences'; PDF p.10 limitations: 'only evaluate models available through the OpenAI API ... American stereotypes ... only on English.' | 识别了提示措辞、模型来源、文化和语言等潜在混淆，并用提示变体部分缓解；但未做正式敏感性分析或完整残余混淆评估。 |
| A5 | 调节变量 | NA | — | 研究没有调节变量假设或调节效应检验；交叉群体分析是描述性/比较性而非正式 moderator 模型。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量假设，也未做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | PDF p.3-4: zero-shot prompt and 'Fightin’ Words ... weighted log-odds ratios ... z-score > 1.96'; Table A9 (PDF p.23) gives full prompts; PDF p.2 gives public code/data. | 关键构念（persona、marked words、stereotype lexicon 计数）均给出可复现操作化程序。 |
| A8 | 水平数与类型 | 0.5 | PDF p.5: '5 races/ethnicities ... 3 genders ... 15 gender-by-race/ethnic groups'; PDF p.4: '90 ... for each of the 15 gender-by-race/ethnic groups and for both models'; Table A9 lists 6 prompts. | 报告了水平数、标签和样本量；但未明确说明水平类型（名义/等级）、间距/全距等。 |
| A9 | 单一操作化的风险 | 1 | PDF p.4: 'We use several other methods as robustness checks'; PDF p.5: 'Marked Words, JSD, and the SVM have significant overlap in the top words identified'; Table 3. | 对关键构念采用多种操作化（Marked Words、JSD、SVM、词典计数、情感分析）并报告会聚/重叠证据。 |
| A10 | 单一方法的风险 | NA | — | 这是计算文本分析，不是多构念自陈量表研究；提示条件与文本指标均来自生成文本，不存在传统共同方法偏差检验框架。 |
| B1 | 被试间设计 | NA | — | 没有人类被试的组间分配；不同 API 生成本质上是独立生成单元，但未作为被试间实验设计来定义和分配。 |
| B2 | 被试内设计 | NA | — | 没有同一被试/同一生成单元接受全部条件的重复测量设计。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合实验设计及相应误差项。 |
| B4 | 因子设计 | NA | — | 研究包含交叉身份组合和模型/提示分层，但不是随机化因子实验，也未进行因子 ANOVA 或交互项检验；不作为因子设计编码。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有正式交互作用检验；交叉身份分析为描述性和定性讨论。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或被试内顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；没有非随机分配下的因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 不是被试内设计，不涉及处理可逆性/迁移对称性。 |
| C1 | 随机化 | NA | — | 没有人类被试随机分配；提示条件为固定分层生成，分配隐藏/随机化不适用。 |
| C2 | 平衡 | NA | — | 没有条件顺序平衡问题；生成调用相互独立。 |
| C3 | 恒定 | 1 | PDF p.4 footnote lists fixed API hyperparameters, temperature=1, max_tokens=150, and API version/date; PDF p.10 discusses English/American and OpenAI-only limitations. | 明确列出模型版本、API 日期和主要生成参数等恒定设置，并讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配程序；各群体为独立生成。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组/协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者盲法安排；自动文本分析不适用。 |
| C7 | 平衡的层级 | NA | — | 没有顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | 每次 API 生成独立、零样本，无跨试次练习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 生成不受人类疲劳影响；无 session 疲劳安排问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个条件独立生成，无跨条件残留/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移或迁移对称性检验。 |
| D5 | 范围效应 | NA | — | 无主观量表/绝对判断任务，不涉及范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选项、排序或序列刺激；6 个提示非顺序敏感呈现，未作为位置偏差设计。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 生成无人类被试需求特征；无事后访谈问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.5 Figure 1 reports average percentage with standard error; PDF p.6 Figure 2 reports percentage of personas containing lexicon words, including many absent words. | 报告了均值/比例和误差条，可部分检查分布；但未正式报告偏度/端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；无共同方法偏差统计检验需求。 |
| F1 | 统计结论效度 | 0.5 | PDF p.5: SVM accuracy '0.96 ± 0.02 and 0.92 ± 0.04'; PDF p.6: VADER mean 0.83/0.93 with SD 0.27/0.15; figures show error bars. | 报告了部分效应估计和误差条，但缺少样本量确定依据、正式 95% CI 和多重性校正说明。 |
| F2 | 内部效度 | 0.5 | PDF p.4 describes fixed API generation procedure; PDF p.10 discusses scope and model limitations; no random assignment/allocation concealment or baseline equivalence. | 报告了生成程序和部分内部效度限制，但不是随机实验，缺少分配隐藏、基线等价检验和正式损耗/流向处理。 |
| F3 | 构念效度 | 0.5 | PDF p.4: JSD/SVM robustness checks; PDF p.5: SVM accuracy; PDF p.8 discusses anti-stereotyping interpretation and limitations; no formal reliability statistic. | 提供了一定的构念效度/会聚证据，但没有正式信度、操纵检验或完整多操作化局限讨论。 |
| F4 | 外部效度 | 0.5 | PDF p.10: 'only evaluate models available through the OpenAI API ... American stereotypes ... only on English ... five race/ethnicity and three gender groups'; Appendix D discusses other models. | 报告了模型来源和推广边界，但没有跨样本/跨情境系统复现，代表性有限。 |
| G1 | 分析单位 | 0.5 | PDF p.4: '90 ... for each of the 15 gender-by-race/ethnic groups and for both models'; SVM split stratified 80/20; PDF p.3 says outputs analyzed across prompts in aggregate. | 说明了生成与分析的 persona/群体层级，但将 6 个提示聚合分析，未用多层模型处理提示/群体的嵌套结构。 |
| G2 | 随机效应 | NA | — | 没有混合模型推断；研究为描述性/基准式汇总，未把提示或群体作为随机效应建模。 |
| G3 | 材料作为随机效应 | NA | — | 不以有限词项/材料作为需推广到材料总体的随机因子；词项是结果特征而非随机材料样本。 |
| G4 | 统计功效 | 0 | PDF p.4 reports 2700 personas but no a priori power analysis or sample-size justification. | 没有事前功效分析或明确的样本量论证，也没有用 CI 做功效推断。 |
| G5 | 研究者自由度 | 0.5 | PDF p.4 reports fixed 90 samples per group; PDF p.2 releases dataset/code; PDF p.10 notes limited model/group scope; no explicit stopping rule or exclusion accounting. | 报告了主要条件和部分排除/局限，但缺少完整样本量决定方式、停止规则及验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered analysis plan is reported; ACL checklist does not indicate one. | 无预注册，未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较。 |
| J2 | 冗长偏差 | NA | — | 没有用 LLM 裁判评估开放式生成质量，不涉及长度偏差。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或多轮纠错对话。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge，无自我偏好偏差问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | PDF p.3: 'we prompt an LLM in the zero-shot setting'. | 零样本提示，无 few-shot 示例选择/排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | Table A9 (PDF p.23) provides full prompts; PDF p.3: 'We vary our prompts by wording and length ... did not find statistically significant differences.' | 提供模板并做了部分措辞变体比较；但没有版本号/迭代日期、dev/test 划分和完整敏感性结果。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验使用短提示生成 persona，不涉及长上下文或 RAG。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.4 footnote reports temperature=1, top P=1, frequency/presence penalties=0, best_of=1, max_tokens; 90 samples/group and API dates. | 报告了主要采样超参和重复生成量，但未报告随机种子、top-k、每条件 95% CI/bootstrap。 |
| J9 | 重复与文本退化 | 0.5 | PDF p.4 footnote reports max length, best_of=1, temperature=1, frequency/presence penalties; no repetition/degeneration rate is reported. | 部分报告了解码设置，但未报告重复率/退化率或条件间退化 QC。 |
| J10 | 分词效应 | NA | — | 研究仅使用英语，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 没有使用固定公开基准测试集进行训练-测试重叠评估；persona 为模型即时生成，不适用传统污染检测。 |
| J12 | 基准饱和 | NA | — | 不是准确率型基准，也不存在基准饱和/SOTA 天花板问题。 |
| J13 | 指令遵循 | NA | — | 研究不测量指令遵循；因变量是 persona 中的刻板词项/模式。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 自由文本生成，不要求结构化输出或格式约束。 |
| J15 | 越狱稳健性 | NA | — | 不评估安全/越狱稳健性；无有害请求攻击设置。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文研究 LLM 输出中的表征性伤害，不把 LLM 当作人类心理学被试来推断人类同名心理构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对代理指标进行优化、RL、best-of-N 或奖励模型训练。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.4: GPT-3.5 produced in December 2022 and others May 2023 with '2023-03-15-preview'; PDF p.5 reports SVM mean±SD; PDF p.2 releases data/code. | 报告了模型 snapshot/日期、样本量和部分变异性，但缺少随机种子、95% CI 与配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮生成/评估，无多轮对话历史与一致性衰减问题。 |

## 编码小结
论文在方法、提示模板、数据与代码公开方面较可复现，也提供了多种稳健性方法；但其设计主要是观察性/基准式测量而非随机化实验，缺少正式操纵检验、预注册、功效分析、完整采样随机性报告和正式信效度检验。许多人类实验设计组件（被试分配、顺序平衡、盲法、疲劳/练习等）不适用。
