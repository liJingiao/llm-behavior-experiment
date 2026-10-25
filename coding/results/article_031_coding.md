# article_031 | We Understand Elliptical Sentences, and Language Models should Too: A New Dataset for Studying Ellipsis and its Interaction with Thematic Fit | 2023

研究类型概述：NLP 数据集构建与语言模型基准评估。作者构建 ELLie（575 个椭圆句，按语义角色和典型性条件组织），评估 GPT-2 large 与 BERT-base-cased 在句子概率、填充词概率和省略动词/宾语检索上的表现；无人类被试，分析单位为句子/试次与模型条件。
- **研究构念（Construct）**：省略消解与题元适合度交互（ellipsis resolution and thematic fit）｜CA 构念锚定：句法加工（syntactic processing, `trm_4a3fd79d0b34b`）；句法分析（syntactic parsing, `trm_4a3fd79d0b340`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）
- **实验任务与范式（Task / Paradigm）**：NLP 数据集构建与语言模型基准评估。作者构建 ELLie（575 个椭圆句，按语义角色和典型性条件组织），评估 GPT-2 large 与 BERT-base-cased 在句子概率、填充词概率和省略动词/宾语检索上的表现；无人类被试，分析单位为句子/试次与模型条件。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: five alternatives T, AT, SP_v; p.5 Table 1 lists T-T, T-AT, AT-T, AT-AT, T-SP_v; p.5 Table 2 lists semantic roles. | 典型性条件、语义角色和模型被明确命名并给出水平/标签，但条件由数据集固定构造，未报告操纵检验或单位分配程序。 |
| A2 | 因变量 | 0.5 | p.5: sentence probability computed with chain rule for GPT-2 and PLL for BERT; p.6: verb retrieval accuracy via regular expressions; direct object accuracy for GPT-2. | 因变量指标与计分方式明确，并做 token 数归一化；但无信效度证据、无置信区间或连续指标防端点说明。 |
| A3 | 控制变量 | 0.5 | p.5: normalization based on number of tokens to ensure results not affected by sentence length; p.4 fixed GPT-2 large and BERT-base-cased. | 报告了 token 长度归一化和固定模型版本等控制，但未系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p.8: models tend to rely on frequent verb-argument co-occurrences; p.9: behavior guided more by lexical cues than genuine linguistic structure. | 识别了词频/共现等潜在混淆并作解释，但未在设计或分析中系统控制，也未做敏感性分析。 |
| A5 | 调节变量 | NA | — | 研究无调节变量假设；语义角色、模型和条件均作为比较因子而非调节变量处理。 |
| A6 | 中介变量 | NA | — | 无中介变量假设，也未做直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p.3: quintuplets differ only in candidate fillers and typicality conditions; p.5: sentence probability/PLL computation; p.6: prompt and regular-expression accuracy. | 关键构念有较具体操作化，但 thematic fit 依赖 DTFit 评分、SP_v 为手动检查，未给出完整可复现阈值或完整 prompt 集。 |
| A8 | 水平数与类型 | 0.5 | p.4: five conditions T, AT, SP_v; p.5 Table 2: five semantic roles; p.6: GPT-2 top-p vs greedy. | 报告了水平数和各水平标签，但未说明水平类型、间距/全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 0.5 | p.5-p.8: three tasks (sentence typicality, filler typicality, elided verb retrieval); p.8 discusses convergence/differences across tasks. | 对椭圆句理解采用多任务/多指标，但未系统报告各操作间会聚效度。 |
| A10 | 单一方法的风险 | NA | — | 研究不是自陈式多构念测量，全部指标来自模型输出，共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试，也没有被试间条件分配；句子/模型试次不是人类被试组。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量设计；模型对句子独立评分。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合设计。 |
| B4 | 因子设计 | 0 | p.6: Kruskal-Wallis and pairwise Wilcoxon across conditions; p.7 Table 4 role-condition means; no interaction test reported. | 典型性条件与语义角色可交叉，但未报告完整设计矩阵、每格样本量或交互项统计；按因子设计核心要件未达成。 |
| B5 | 主效应 | 0.5 | p.6: models assign significantly higher scores to T-T than atypical/anomalous conditions; Kruskal-Wallis and pairwise Wilcoxon; no H/F/df/p/effect size reported. | 报告了条件主效应的显著性和方向，但缺完整统计量、效应量，且未讨论交互受限。 |
| B6 | 交互作用 | 0 | p.6-p.8: only condition-wise comparisons and role descriptions; no interaction term statistics. | 未报告任何交互项检验，也未做简单主效应/多重比较校正的完整报告。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无被试内条件顺序设计，未使用拉丁方。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；无人类非随机分组。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理，不涉及处理可逆性/迁移对称性。 |
| C1 | 随机化 | NA | — | 无人类被试随机分配；数据集条件为固定构造，模型调用也不存在条件随机分配。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，因此无顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.4: GPT-2 large (36 layers, 1024 embedding) and BERT-base-cased (12 layers, 768 embedding); Minicons/Transformers library. | 报告了模型版本和库等恒定条件，但未系统列出全部恒定变量/水平，外部效度限制仅在局限中部分讨论。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.5: normalization based on number of tokens; no ANCOVA or covariate model reported. | 测量并归一化了 token 数这一潜在混淆，但未作为协变量/区组纳入统计模型，也未检验相关假设。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 每条件独立调用，无上下文内学习或练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类疲劳问题，任务为模型推理调用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立评分/生成，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或不对称迁移风险。 |
| D5 | 范围效应 | NA | — | 因变量为概率和检索准确率等客观指标，无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多候选项选择、排序或序列刺激顺序操纵；句子独立评分。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不涉及需求特征/掩饰情节。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Figures 1-4: boxplots of sentence/filler probability distributions; p.8 Table 5: low retrieval accuracy (0.15-0.63). | 报告了分布图和准确率以显示低端表现，但未系统报告偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.6: Kruskal-Wallis followed by pairwise Wilcoxon; p.8 Table 5 accuracy; no effect sizes, CIs, or correction details. | 统计结论仅以显著性描述和准确率呈现，未报告效应量/置信区间，样本量无功效依据，多重比较校正未说明。 |
| F2 | 内部效度 | NA | — | 非人类随机实验，无因果推断主张；无分配隐藏、基线或被试流向问题。 |
| F3 | 构念效度 | 0 | p.3: DTFit human ratings mentioned as source; p.9: limitations note ELLie still needs human judgments; no reliability/manipulation check. | 未报告模型测量的信效度证据或操纵检验，构念与指标对应关系主要靠论证而非实证验证。 |
| F4 | 外部效度 | 0.5 | p.4: two pretrained models; p.9: limitations on English-only, only two models, small dataset, future cross-linguistic/more models. | 报告了数据集/模型来源并讨论部分推广边界，但无跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.5-p.6: analyses at sentence/model condition level; no multilevel model or explicit assignment-analysis hierarchy discussion. | 分析单位为句子/模型条件，条件由数据集构造；未明确说明分配层级与统计层级匹配，也未用多层模型处理句子嵌套于角色/条件。 |
| G2 | 随机效应 | 0 | p.4: only two pretrained models; p.9: only two models tested; no random-effect structure reported. | 模型被当作两个固定比较对象，未设随机效应；结论讨论 LMs 泛化时未提供随机效应结构，推断可推广性受限。 |
| G3 | 材料作为随机效应 | 0 | p.5 Table 2: 575 constructed sentences; analyses aggregate over sentences; no item random effect or F1/F2 combined model. | 材料是固定构造的有限句子，未将项目作为随机因子或做准 F/混合模型分析。 |
| G4 | 统计功效 | 0 | p.4-p.8: no power analysis or sample-size justification; accuracy table only. | 无事前功效分析或样本量论证，结果未报告效应量/CI。 |
| G5 | 研究者自由度 | 0.5 | p.4: dataset structure all conditions; p.9: limitations acknowledge small dataset and two models; no exclusion rules or confirmatory/exploratory labels. | 报告了全部条件与主要因变量及数据集规模，但缺数据排除规则、停止规则和验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–13 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册或注册链接，也未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较；模型概率/检索准确率无候选位置反平衡问题。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放生成质量，无长度偏差风险。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge，因此无裁判自我偏好风险。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本 prompting，无 few-shot in-context examples；未来 few-shot 仅为展望。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5-p.6 prompt templates (2); p.8 pilot prompts (4) and note that minimum prompt changes can change results. | 给出 prompt 模板示例并做了小规模 prompt pilot，但无版本化、系统敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为单句/短句，远低于长上下文窗口，无 RAG 或长文档位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: top-p=0.92, seed set, top-3 generated sentences, greedy search configuration; no temperature/CI/snapshot details. | 报告了主要采样参数、seed 和重复生成数，但未报告 temperature、完整超参、置信区间或精确 API snapshot。 |
| J9 | 重复与文本退化 | 0.5 | p.6: GPT-2 tested with top-p nucleus sampling and greedy search; no repetition rate/degeneration QC reported. | 报告了解码策略，但未报告 repetition penalty、n-gram 重复率/退化率、生成长度上限或截断比例。 |
| J10 | 分词效应 | NA | — | 单语言英文、单脚本研究，无跨语言/跨脚本比较；虽处理了两个 tokenizer 的位置差异，但不属于 J10 核心跨语言比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4: GPT-2 trained on WebText, BERT on Wikipedia/BooksCorpus; p.3: new ELLie dataset, partly based on DTFit; no contamination check or cutoff comparison. | 未报告训练截止日期与测试集版本对照，也未做 n-gram 重叠/污染检测；部分材料来自已有 DTFit，污染风险未评估。 |
| J12 | 基准饱和 | NA | — | ELLie 为新难题且检索准确率很低（0.15-0.63），远未接近天花板，饱和问题不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，无约束指令测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/JSON 输出，无格式合法率问题。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估或有害请求。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究为 NLP 语言模型能力评估，分析单位为模型概率/检索准确率，不主张把 LLM 作为心理学被试测量人类同名构念；心理语言学仅作背景。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 仅两个模型/时点，无跨规模或训练进展的能力曲线，不涉及涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL 或 best-of-N 代理指标优化环节，代理指标博弈/过优化不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6: GPT-2 top-3 generation with seed; GPT-2 large and BERT-base-cased specified; p.8 Table 5 scores; no CIs or paired tests. | 报告了部分重复次数和模型版本，但无置信区间、精确 snapshot/commit、逐题敏感性分析或模型配对检验；BERT 为单次评估。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮 prompting，无多轮对话历史累积。 |

## 编码小结
研究核心是数据集与 LLM 行为评估，而非人类实验。A–G 中大量人类被试设计组件不适用；A 层条件操纵与测量指标有报告但不完整，J6/J8/J9/J19 等 LLM 评估风险有部分报告，但缺少统计不确定性、精确 snapshot、系统提示消融与污染检测。
