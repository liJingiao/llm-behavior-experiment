# article_144 | Distributive Fairness in Large Language Models: Evaluating Alignment with Human Values | 2025

研究类型概述：该文是LLM作为行为主体/社会规划者的多模型基准与行为比较研究：在资源分配实例上比较GPT-4o、Claude-3.5S、Llama3-70b、Gemini-1.5P与既有研究人类数据，并操纵/考察提示意图、persona、菜单选择、CoT、反馈精炼、角色偏差、顺序与模板等变体。分析单位为每个模型×实例×提示条件的100次LLM响应分布；人类数据来自既有研究，非本文新收集的人类被试实验。
- **研究构念（Construct）**：分配公平偏好、效率-公平权衡、自利偏差与人格操纵｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：向GPT-4o、Claude、Llama和Gemini重复呈现具有EQ、EF、Rawls maximin与效用最大化候选解的资源分配任务，要求选择最公平方案，并与人类分布比较。｜CA 任务锚定：类比推理任务（analogical reasoning task, `trm_4f244f0286947`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_5: 'We consider several state-of-the-art LLMs... default temperature of 1.0'; 'each model was queried 100 times on each instance'; PDF_PAGE_35-42: prompt variants for intentions/personas/options/CoT. | 模型与提示变体被明确命名并给出水平标签，但未报告正式操纵检验，也未完整说明条件分配/随机化程序，故为0.5。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_4: formal definitions of EQ/EF/RMM/USW/PO; PDF_PAGE_21 Table 5: 'mean (±95% CI)' for each notion; PDF_PAGE_36: JSON extraction prompt. | 因变量为响应中满足各公平/效率axiom的比例，指标与计分由形式化算法明确；但未报告传统信效度证据或连续指标预处理，故为0.5。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_5: temperature fixed at 1.0; 100 queries per instance; PDF_PAGE_28 Table 14: exact model strings; PDF_PAGE_35: standardized two-stage prompt format. | 报告了部分控制变量（模型版本、温度、调用次数、prompt格式），但未系统列出控制变量清单并逐一说明所有控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_10: limitations mention 'logical errors and the use of greedy algorithms'; human-study biases; PDF_PAGE_26 Table 13: ordering changes significantly alter responses. | 识别了若干潜在混淆（人类研究背景差异、模型推理错误、顺序/模板敏感性），但未系统说明控制方式及残余混淆对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 本文没有明确的调节变量理论模型与交互假设；模型/提示变体被作为比较条件而非调节变量建模。 |
| A6 | 中介变量 | NA | — | 本文没有中介变量或中介效应分解。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_4: formal definitions of fairness/efficiency notions; PDF_PAGE_35-42: full prompts; PDF_PAGE_36: JSON-based response extraction. | 关键构念均有可复现操作化：公平axiom形式定义、完整提示文本、响应解析与计分流程，且公开代码/数据链接。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_5: four models listed; PDF_PAGE_9: persona/objective prompts; PDF_PAGE_23 Table 10: CoT conditions; PDF_PAGE_5: 100 queries per instance. | 报告了各分类条件的水平与标签，但未系统说明水平类型、间距/全距或连续变量中心化；对本研究多为名义分类变量。 |
| A9 | 单一操作化的风险 | 0.5 | PDF_PAGE_8: generation vs menu selection; PDF_PAGE_9: personas; PDF_PAGE_26-27: ordering and template robustness. | 关键构念采用了生成、选择、多种提示变体等多种操作化，但未系统报告各操作间的会聚证据或单一操作局限的完整讨论。 |
| A10 | 单一方法的风险 | 0.5 | PDF_PAGE_5: same API prompting-and-response pipeline; PDF_PAGE_27: template-based single prompt; PDF_PAGE_26: ordering manipulations. | 所有LLM构念均来自同一提示—响应方法渠道；论文做了多种提示变体稳健性检验，但未报告正式共同方法偏差统计检验或系统程序控制。 |
| B1 | 被试间设计 | NA | — | 没有人类被试间随机分配；模型比较为观察性基准比较，同一模型还跨多个提示条件被重复调用，不构成传统被试间设计。 |
| B2 | 被试内设计 | NA | — | LLM调用为相互独立的API会话，无跨条件上下文累积的被试内顺序设计；论文未按重复测量顺序设计处理。 |
| B3 | 混合设计 | NA | — | 没有逐因素标注组间/组内属性的混合设计分析，也没有对应混合模型与误差项。 |
| B4 | 因子设计 | NA | — | 研究包含模型、实例、提示条件等比较，但未采用因子ANOVA设计，未报告完整设计矩阵、每格样本量与交互项统计；按规则记NA而非0。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验（F、df、p、效应量）可供编码。 |
| B6 | 交互作用 | NA | — | 没有报告因子交互项的统计检验、简单效应或交互图误差棒。 |
| B7 | 区组设计 | NA | — | 没有区组/分层设计及区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡顺序。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计；模型比较没有非随机分组的选择偏差与因果推断框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理，故不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 研究没有把分析单位随机分配到互斥条件的随机化结构；模型与提示条件为固定设计，LLM调用独立且无分配隐藏问题。 |
| C2 | 平衡 | NA | — | 独立API调用无跨条件顺序效应，无需传统条件顺序平衡；论文也未设置顺序分配。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_5: 'default temperature of 1.0'; 100 queries per instance; PDF_PAGE_28 Table 14: exact model/API strings; PDF_PAGE_35: standardized prompt. | 报告了温度、模型版本、调用次数与prompt格式等恒定变量，但未在讨论中系统说明这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配或配对设计。 |
| C5 | 纳入为变量 | 0 | PDF_PAGE_5: models and instances compared descriptively; PDF_PAGE_21: aggregate percentages; no covariate/ANCOVA model reported. | 已知的模型能力/实例难度等潜在混淆未被测量并作为区组或协变量纳入分析，也未检验协变量假设。 |
| C6 | 盲法 | NA | — | 完全自动化数据采集与算法评分，没有人类被试、主试或评分者盲法问题。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA等顺序平衡层级可编码。 |
| D1 | 练习效应 | NA | — | 每个LLM调用为独立会话，无上下文内学习或练习效应；不适用练习块/试次位置控制。 |
| D2 | 疲劳效应 | NA | — | LLM无疲劳效应；任务为短提示调用，不适用session时长与休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每条件独立API会话，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移，不涉及迁移对称性检验。 |
| D5 | 范围效应 | NA | — | 研究不使用Likert/绝对量值评定量表；因变量为分配方案及axiom分类比例。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_26 Table 13: shuffling order of goods/individuals in I2/I6 and reporting significant changes; PDF_PAGE_27: ordering robustness under template prompts. | 论文系统检验了题目中个体/物品顺序的影响，但未在主实验对菜单选项顺序随机化或反平衡，也未报告每顺序分配与翻转率；属部分顺序控制。 |
| E2 | 默认赞同 | NA | — | 研究不使用Likert/态度自评量表，无反向计分与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM研究不涉及人类被试需求特征或事后推断假设访谈。 |
| E5 | 实验者效应 | NA | — | 数据收集与评分完全自动化，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_21 Table 5: mean ±95% CI for each notion; PDF_PAGE_6 Table 2 and PDF_PAGE_5 Figure 2: response percentage distributions. | 报告了均值/百分比与部分分布，便于观察端点堆积，但未专门报告偏度、端点频率或pilot难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念量表测量；IV为提示操纵，DV为算法判定的分配性质，传统共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_5: 100 queries per model/instance; PDF_PAGE_21 Table 5: mean ±95% CI; PDF_PAGE_5: Fisher's exact test p<0.05. | 报告了部分CI与显著性检验，但无样本量/功效依据，多重比较校正也未系统说明。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_5: fixed model/prompt conditions; PDF_PAGE_26-27: robustness checks; PDF_PAGE_10: limitations. | 无随机分配与分配隐藏、无被试流向/损耗问题；论文部分评估了提示顺序/模板等内部效度威胁，但未系统控制所有混淆。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_4: formal axioms; PDF_PAGE_35-42: full prompts; no reliability/manipulation-check statistics reported. | 公平构念有形式化定义和多操作化，但未报告评分/解析信度、效度证据或操纵检验。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_5: four LLMs with versions; PDF_PAGE_28 Table 14: API/model strings; PDF_PAGE_10: limitations on human-study/sample context. | 报告了模型来源与版本，并有限讨论推广边界，但无跨样本/跨情境复现或代表性抽样论证。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_5: each model queried 100 times per instance; PDF_PAGE_5: Fisher's exact tests on response distributions; no multilevel model reported. | 说明了分析在响应层级进行，但未明确处理响应嵌套于模型/实例的聚集结构，推断层级匹配不完整。 |
| G2 | 随机效应 | 0 | PDF_PAGE_5: repeated API calls treated as response counts; PDF_PAGE_21: aggregate means/CI; no random-effects structure reported. | 未报告任何随机效应；模型/实例被当作固定比较条件，未建模抽样变异，可能高估可推广性。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_4: instances adopted from Herreiner and Puppe; PDF_PAGE_30-33: fixed instance set and per-instance tables; no item random effect. | 使用了多个固定实例并报告逐实例与聚合结果，但未将材料/实例作为随机效应纳入模型；只能算部分体现材料变异性。 |
| G4 | 统计功效 | 0.5 | PDF_PAGE_5: 100 queries per model/instance; PDF_PAGE_21 Table 5: 95% CI; no a priori power analysis. | 没有事前功效分析或样本量推导；报告了部分CI/百分比差异，但预期效应量来源与检验功效未说明。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_5: all four models and 10 original instances; PDF_PAGE_35-42: all prompt variants; PDF_PAGE_28 Table 14: model strings. | 报告了大量条件与因变量，但未明确数据排除/停止规则、样本量决定方式，也未系统区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | PDF_PAGE_1-10 and appendices: no preregistration link, registration number, or pre-specified analysis plan reported. | 全文未报告预注册；按口径记0而非NR。 |
| J1 | 位置偏差 | 0.5 | PDF_PAGE_8 and PDF_PAGE_22: menu options listed in fixed order; PDF_PAGE_26 Table 13: ordering of goods/individuals shuffled, not menu option positions; no flip-rate reported. | 识别并检验了题目中个体/物品顺序的敏感性，但未对候选菜单选项位置做反平衡/随机化，也未报告位置翻转率。 |
| J2 | 冗长偏差 | NA | — | 评估由算法按公平axiom分类分配方案，不使用LLM-as-judge对开放生成质量打分，长度偏差风险不适用。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场操纵；反馈精炼是任务性纠错，不是谄媚/立场附和评估。 |
| J4 | 自我偏好 | NA | — | 不使用LLM作为裁判或成对比较评分者，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF_PAGE_41-42: CoT prompt includes one worked example I0 with allocations and fairness explanations; no multi-seed/order counterbalance reported. | 使用了单条in-context示例并公布模板，但未报告多示例集seed重复、排列反平衡或示例来源比例，故为0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_35-42: full prompt templates; PDF_PAGE_26-27: ordering/template sensitivity analyses; no prompt version dates/dev-test split. | 提供了完整模板并做多种敏感性消融，但缺少版本号、迭代日期、dev/test划分与完整搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 提示上下文很短，远低于长上下文窗口，无RAG或长文档位置效应实验。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_5: 'default temperature of 1.0' and 100 queries per instance; PDF_PAGE_28 Table 14: exact model/API strings; Table 5 reports 95% CI. | 报告了温度和重复次数及部分CI，但未报告top-p/top-k、随机种子和每条件完整采样分布。 |
| J9 | 重复与文本退化 | 0 | PDF_PAGE_5: only temperature default reported; no decoding strategy, repetition penalty, n-gram repetition/degeneration rate, or truncation rate reported. | 未说明解码策略与重复/退化质量控制；开放解释生成可能受退化影响，但未报告。 |
| J10 | 分词效应 | NA | — | 实验为英文单语言、单脚本，无跨语言/跨脚本分词长度比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_4: instances from Herreiner and Puppe [50]; no training-cutoff or contamination analysis reported. | 使用公开已发表实例但未检查模型训练数据污染、未对照训练截止日期，也未做n-gram/DCQ检测。 |
| J12 | 基准饱和 | NA | — | 主要分数普遍较低（如EQ常接近0），未接近基准天花板；饱和度风险不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，未测量约束类型拆分准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF_PAGE_35-36: two-stage prompting with JSON extraction; PDF_PAGE_27 and PDF_PAGE_38: template-based JSON prompt; no format-validity rate reported. | 报告了结构化输出设置，但未报告JSON解析成功率、重试策略或将格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF_PAGE_4: 'we interpret alignment in a normative sense'; PDF_PAGE_2: contrast with human subjects on instances from Herreiner and Puppe; PDF_PAGE_28: exact model versions. | 将LLM作为社会规划者并与人类同名公平构念对照，但未系统论证LLM构念与人类构念的理论异同及外推边界，故为0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以benchmark/奖励模型/LLM-judge为优化目标进行训练或best-of-N优化，不涉及代理指标过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_5: 100 queries per model/instance; PDF_PAGE_28 Table 14: exact model strings; PDF_PAGE_21 Table 5: 95% CI; no paired bootstrap/McNemar. | 报告了重复次数、精确模型字符串与部分CI，但未系统做配对检验、未发布逐题推理日志，复现细节不完整。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF_PAGE_10: refinement with feedback; PDF_PAGE_25 Table 11: 'at most two re-tries' and final success rates; no per-turn scoring/truncation details. | 做了多轮反馈精炼，但只报告最终成功率，未按轮次拆分、未说明上下文是否截断及跨轮行为轨迹。 |

## 编码小结
研究以LLM响应为分析单位，核心是分布比较与提示稳健性检验，而不是人类被试随机实验。因此B1–B10、C1/C2/C4/C6/C7、D1–D5、E2–E5/E7等人类被试分配/顺序/自陈量表组件多为不适用；与LLM行为评测相关的J1、J5、J6、J8、J9、J11、J14、J16、J19、J20按实际风险编码。论文报告了完整prompt、模型snapshot与每条件100次调用，但缺少操纵检验、正式随机化、随机效应建模、污染检查和系统共同方法偏差检验，故多项为0.5或0。
