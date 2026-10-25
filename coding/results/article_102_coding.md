# article_102 | Say What You Mean! Large Language Models Speak Too Positively about Negative Commonsense Knowledge | 2023

研究类型概述：纯 LLM 探测/基准评测研究，无人类被试实验。分析单位为 CSK-PN 中的知识三元组/提示，比较 QA 与约束生成（CG）任务在不同模型、few-shot 数量、示例正负比例、输入形式、CoT 与温度下的表现，核心因变量为 TP/TN/Acc 及 QA-CG 一致性。
- **研究构念（Construct）**：负性常识表征、否定加工、信念冲突与任务形式依赖｜CA 构念锚定：语义记忆（semantic memory, `trm_4a3fd79d0b083`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）；认知控制（cognitive control, `trm_4aae62e4ad209`）
- **实验任务与范式（Task / Paradigm）**：纯 LLM 探测/基准评测研究，无人类被试实验。分析单位为 CSK-PN 中的知识三元组/提示，比较 QA 与约束生成（CG）任务在不同模型、few-shot 数量、示例正负比例、输入形式、CoT 与温度下的表现，核心因变量为 TP/TN/Acc 及 QA-CG 一致性。｜CA 任务锚定：语义判断任务（semantic decision task, `trm_4f240cb09f8e5`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5：'We manually write 32 examples... randomly sample a total number of k examples from E+ and E−'；p.5 Table 1 比较 QA 与 CG、k=2/10；p.7-8 操纵示例比例、CoT、输入形式和温度。 | 任务形式、k、示例比例、CoT 等是明确操纵变量并给出水平/程序；但未报告单位分配到条件的随机化/平衡，也无操纵检验，故为 0.5。 |
| A2 | 因变量 | 1 | p.4：'We define TP and TN as the accuracy on the positive and negative splits... Acc=(TP+TN)/2'；CG metric 'produces 1 or 0 based on the finding of negation cues'；'manual inspection of 200 cases... correct 97%'；'100 cases... agreement... 95%'。 | QA/CG 的指标、计分与验证均明确；无反应时等连续指标故不涉及预处理。 |
| A3 | 控制变量 | 0.5 | p.5：'all models use greedy decoding (temperature as 0.0)'；p.5：few-shot examples '&#124;E+&#124;=&#124;E−&#124;'；p.3 去除含代词/否定/形容词等无效三元组。 | 报告了若干恒定/控制措施，但无系统控制变量清单及逐项控制方式，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.6 §5.1 将 question/keywords 输入互换以检验输入形式混淆；p.7 §5.2 按关键词共现分桶；p.7 §5.3 调整 E+/E− 比例；p.6 与 p.14 报告 instruction wording、temperature 敏感性。 | 识别并检验了多个关键混淆/敏感性，但对模型训练历史等残余混淆只作假设和未来工作，未充分量化内部效度威胁。 |
| A5 | 调节变量 | NA | — | 论文未建立正式调节变量模型或交互检验；k、模型、共现等是条件/分层分析，不作为调节假设。 |
| A6 | 中介变量 | NA | — | 无中介变量与直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.3 定义负事实 ¬r(s,o) 与 CSK-PN；p.4 给出 QA/CG prompt 形式、yes/no 计分和 negation-cue 计分；p.14 Table 3 给出完整 task prompt 示例。 | 关键构念、任务、计分与数据构建均有可复现操作化。 |
| A8 | 水平数与类型 | 0.5 | p.5 Table 1：k=2/10；p.6 Figure 3：k=0,2,4,8,16,32；p.7 Figure 6：η；p.8 Table 2：CoT None/Deduction/Fact；p.5 列出多种模型。 | 水平数与标签清楚，但未系统说明水平类型、间距/全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 1 | p.4-5 同时用 Boolean QA 与 constrained generation 两种操作化；p.5 Table 1 报告 QA-CG consistency (Cns.)；p.4 对 CG 指标做人工效度检查。 | 关键构念有双任务操作化，并报告一致性/冲突结果和指标验证。 |
| A10 | 单一方法的风险 | NA | — | 测量为 LLM 客观输出与自动/人工验证指标，不是同源自陈量表；共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或 LLM 被试分配到独立条件；模型/任务为固定评测条件，不构成被试间设计。 |
| B2 | 被试内设计 | NA | — | 未将同一被试接受全部水平的重复测量作为设计，且无顺序平衡/随机效应；不适用。 |
| B3 | 混合设计 | NA | — | 无混合设计及组间/组内因素标注与对应误差项。 |
| B4 | 因子设计 | NA | — | 无完整因子设计、设计矩阵或 ANOVA 交互检验；多个条件比较为描述性基准。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 无正式交互项统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 无实验区组/分层随机分配；共现与关系类型为事后分析分层。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或被试内顺序平衡。 |
| B9 | 准实验设计 | NA | — | 未声称准实验设计；模型比较不是准实验分组。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及被试内处理可逆性/迁移对称性设计。 |
| C1 | 随机化 | NA | — | LLM 评测无处理分配/随机化；示例随机抽样不是条件分配。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，无顺序平衡问题；E+/E− 比例平衡不是顺序平衡。 |
| C3 | 恒定 | 0.5 | p.5：'all models use greedy decoding (temperature as 0.0)'；模型版本固定；p.14 Appendix A.2 固定任务 instructions/examples。 | 恒定控制（模型、解码、提示）有描述，但未系统列出恒定变量及外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用被试匹配或匹配分组设计。 |
| C5 | 纳入为变量 | 0.5 | p.7 §5.2 按关键词共现桶分析；p.15 Figure 9 按关系类型分析；p.15 Table 4 分析例外副词。 | 测量并分层分析已知混淆/分层变量，但未作为正式协变量/区组纳入模型，也未检验斜率齐性。 |
| C6 | 盲法 | NA | — | 主指标自动计算，无人类主试/评分者盲法设计；人工检查仅用于指标验证。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 每次提示独立评测，无练习块或跨试次学习；few-shot 示例不是练习效应设计。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳风险，且任务不是长时间 session。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留/清洗期设计；各提示独立处理。 |
| D4 | 不对称迁移 | NA | — | 无迁移对称性设计。 |
| D5 | 范围效应 | NA | — | 无绝对判断/李克特量表范围效应问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选/序列刺激或选项位置操纵；few-shot 示例排列问题由 J5 处理。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 无人类被试需求特征；未做事后访谈，不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集自动化，无人类主试期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5 Table 1 报告 TP/TN/Acc 均值；p.7-8 讨论 TN 低、TP 过高；p.8 指出 TP 'irrationally high'。 | 有均值及高/低端表现讨论，但无 SD/偏度/端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念量表，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.3 数据集 4,000 triples；p.5 Table 1、p.7 Figure 6、p.8 Table 2 报告准确率/性能，但无 95% CI、功效分析或多重比较校正。 | 报告性能估计和主要分析，但缺样本量依据、CI 和多重性校正。 |
| F2 | 内部效度 | 0.5 | p.6 §5.1 互换输入形式检验混淆；p.14 Appendix B.1 温度敏感性；p.8 Table 2 CoT 对照；但无随机分配/流向/损耗。 | 对若干内部效度威胁做了控制比较，但整体非随机，残余模型训练混淆未充分评估。 |
| F3 | 构念效度 | 0.5 | p.4 CG 指标人工验证 97%、与人类判断 95% 一致；p.4-5 双任务操作化；但无正式信度/manipulation check。 | 有指标效度证据和多操作化，但欠正式信度与操纵检验。 |
| F4 | 外部效度 | 0.5 | p.3 CSK-PN 来自 ConceptNet/Safavi 过滤；p.5 多模型；p.9 Limitations 限定 relational commonsense/ConceptNet 与例外。 | 报告数据/模型来源和边界，但无抽样代表性或跨情境复现的系统证据。 |
| G1 | 分析单位 | 0.5 | p.3：4,000 triples；p.5 Table 1 按模型/任务聚合准确率；p.7 按共现桶聚合；无多层/聚类模型。 | 分析单位（三元组/提示）与条件层级基本可辨，但未显式处理关系/项目聚集结构。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；模型版本作为固定比较对象，无被试/模型总体随机效应需求。 |
| G3 | 材料作为随机效应 | 0 | p.3 使用 4,000 个 ConceptNet triples；p.5 只报告模型层面聚合准确率；p.7 仅按共现桶/关系分亚组。 | 材料被视为固定集合，未将 item 作为随机效应或使用 F′/混合模型，却推广到一般负性常识。 |
| G4 | 统计功效 | 0 | p.5 Table 1 与 p.8 Table 2 无事前功效分析、效应量 CI 或重复次数设计；仅报告准确率。 | 无样本量/功效论证，也未见 CI；不能支持统计功效。 |
| G5 | 研究者自由度 | 0.5 | p.3 说明去除 pronouns/negation/adjectives 等无效三元组并得 4,000 条；p.5-8 报告多项任务和消融；但未明确区分验证性/探索性分析。 | 排除规则与主要条件较完整，但研究者自由度披露和探索/验证划分不足。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未出现预注册平台、编号或数据收集前分析计划；p.1 仅给出 GitHub 资源链接。 | 无预注册；按判定口径记 0。 |
| J1 | 位置偏差 | NA | — | 无多候选项选择/排序或 LLM-as-judge 成对比较；QA 仅 yes/no。 |
| J2 | 冗长偏差 | NA | — | 无 LLM 裁判或开放式生成长短评分；CG 由否定线索检测评分。 |
| J3 | 谄媚 | NA | — | 无用户先验立场/反馈/纠错对话操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 评估模型输出。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.5：'We manually write 32 examples... randomly sample k examples from E+ and E−'；'&#124;E+&#124;=&#124;E−&#124;'；p.14 Table 3/6 示例。 | 示例来源、数量和标签比例有报告，但无多 seed 重采样、排列反平衡或完整模板全文，故 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.6 Figure 4 error bars 检验 instruction wording；p.14 Appendix A.2 列出 4 种可替换 instructions；但无 prompt 版本日期/dev-test 划分。 | 有提示措辞敏感性检验，但未完整版本化/记录搜索与测试隔离。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短 few-shot prompt，无长文档/RAG 或位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.5：'all models use greedy decoding (temperature as 0.0)'；p.14 Appendix B.1 温度敏感性；未报 seed/top-p/重复 N。 | 报告主要采样设置（greedy/temperature），但无 seed、重复采样和 CI，snapshot 不精确。 |
| J9 | 重复与文本退化 | 0.5 | p.5 报告 greedy decoding；p.16 讨论 weak negation/生成错误；未报重复率或 repetition penalty。 | 解码策略有报告并基本恒定，但缺文本退化/重复率 QC。 |
| J10 | 分词效应 | NA | — | 单语言英语、单一脚本，无跨语言/跨格式比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3 CSK-PN 由 ConceptNet 过滤构建；未报告测试集发布日期与模型训练截止日期对照或污染检测。 | 负性知识三元组很可能见诸预训练语料，但未做污染评估，故 0。 |
| J12 | 基准饱和 | NA | — | CSK-PN 为新构建探测集，TN 等指标远未饱和；论文未作基准饱和或 SOTA 宣称。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；QA/CG 评测负性常识而非约束遵循率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.4 QA 要求 yes/no；'For rare scenarios (<1%) ... compare conditional probability'；未报告格式合法率。 | 有简单格式约束与兜底规则，但无正式格式合法率/结构化输出设置。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求集。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 脚注定义 'a model’s belief ... prediction about the truth value'；p.5 多模型；p.9 讨论 commonsense/例外局限；无人类同范式对照。 | 对 LLM 'belief' 作了操作化，但未系统比较人类同名构念或报告人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨规模/训练进展的涌现能力曲线或突变宣称；仅比较若干模型。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无对代理指标的优化训练/RL/best-of-N 环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 列出 Flan-T5、GPT-3、Codex002、InstructGPT002/003、ChatGPT 等版本；p.1 GitHub 资源；但无重复 N、CI、精确 snapshot 日期或配对检验。 | 有模型版本和资源，但评估可复现性报告不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 prompt 评测，无多轮对话历史累积。 |

## 编码小结
论文提出了负性常识知识上的“belief conflict”现象，并系统报告了任务、模型、示例数量/比例、输入形式和 CoT 等条件下的结果。主要不足是推断统计与不确定性报告薄弱：无功效分析、置信区间、多重性校正、项目随机效应或污染检查；提示和 few-shot 细节部分可复现但未版本化。人类实验设计相关组件多数不适用。
