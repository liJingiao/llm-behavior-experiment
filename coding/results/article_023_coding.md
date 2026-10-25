# article_023 | Wisdom of the Silicon Crowd: LLM Ensemble Prediction Capabilities Rival Human Crowd Accuracy | 2024

研究类型概述：包含两个研究：Study 1 为纯 LLM 基准/观察性比较（12 个 LLM 集成的中位预测 vs 925 名人类预测者的中位预测，31 个二元预测问题）；Study 2 为同模型内前后测干预（GPT-4 与 Claude 2 在接触人类中位数前后更新预测）。分析单位为问题、模型与重复预测试次，无人类被试随机分组；主要指标为 Brier 分数、预测区间宽度与更新幅度，并观察 acquiescence。
- **研究构念（Construct）**：群体智慧、预测判断与默认赞同偏差（wisdom of crowds, forecasting, and acquiescence）｜CA 构念锚定：反应偏向（response bias, `trm_559f0a129c136`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：包含两个研究：Study 1 为纯 LLM 基准/观察性比较（12 个 LLM 集成的中位预测 vs 925 名人类预测者的中位预测，31 个二元预测问题）；Study 2 为同模型内前后测干预（GPT-4 与 Claude 2 在接触人类中位数前后更新预测）。分析单位为问题、模型与重复预测试次，无人类被试随机分组；主要指标为 Brier 分数、预测区间宽度与更新幅度，并观察 acquiescence。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p7: 'within-model research design that collected two forecasts (pre- and post-intervention) per model run'; PDF p10 intervention prompt provides human median. | Study 2 有明确操纵：是否提供人类中位数（前后测两水平），并给出干预提示词；但未报告操纵检验，分配/顺序细节也不完整，故部分满足。 |
| A2 | 因变量 | 0.5 | PDF p10: Brier score formula and '0.250 ... if all predictions were 50%'; PDF p14: prediction interval and adjustment magnitude results. | 因变量指标与计分方式明确；但未报告心理测量信效度、连续指标预处理或天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | PDF p5: models accessed 'through a web interface and did not query any models via their APIs to hold the query method constant'; p7: human median collected same day. | 报告了若干控制手段（统一查询方式、默认参数、同日人类中位数），但控制变量清单不系统，外部效度限制讨论不足。 |
| A4 | 混淆变量 | 0.5 | PDF p5 footnote controls model updates; p7 notes asynchronous queries/current-date issue; p16 discusses limitations and alternative explanations. | 识别了模型更新、人类预测可见性、异步查询等潜在混淆并作了部分控制；但未系统做敏感性分析或充分量化残余威胁。 |
| A5 | 调节变量 | NA | — | 本研究没有明确调节假设、乘积项交互检验或简单斜率分析；模型比较是描述性/单因素比较，不构成调节模型。 |
| A6 | 中介变量 | NA | — | 没有中介变量、直接/间接效应分解或因果链中介检验。 |
| A7 | 操作性定义 | 1 | PDF p7 Figure 1 full prompt; p9 Figure 3 and p10 Figure 4 Study 2 prompts; p10 aggregation and Brier formula; p7 human median definition. | 关键构念（LLM 预测、人类中位数、聚合、准确率）均给出可执行的操作程序与计分公式，足以理解复现流程。 |
| A8 | 水平数与类型 | 0.5 | PDF p5-6 Table 1 lists 12 model labels; p7 gives pre/post two-level design. | 报告了各水平标签与水平数，但未明确水平类型、间距/全距或连续变量中心化等细节。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p16: 'our study could draw on a well-curated set of questions... may further reduce performance'; main accuracy mainly Brier score. | 关键构念主要依赖单一预测任务/单一主指标；文中对单一场境与问题集的推广限制有简短讨论，但未系统比较多种操作化。 |
| A10 | 单一方法的风险 | NA | — | 预测与准确率来自 LLM 输出和外部客观结果，不使用同源自陈量表；共同方法偏差不构成主要问题。 |
| B1 | 被试间设计 | NA | — | Study 1 为观察性模型比较，Study 2 为同模型前后测；不存在把独立被试/单位随机分配到互斥实验条件的被试间设计。 |
| B2 | 被试内设计 | 0.5 | PDF p7: 'within-model research design ... two forecasts (pre- and post-intervention) per model run'; p14 reports pre/post results. | Study 2 明确为重复测量/同模型前后测；但条件顺序固定为先前测后干预，未报告平衡方案或把试次/问题作为随机效应。 |
| B3 | 混合设计 | NA | — | 没有同时包含组间与组内因素的混合设计；Study 2 逐模型分析，Study 1 为单因素模型比较。 |
| B4 | 因子设计 | NA | — | 没有多因素完全交叉的因子设计；Study 1 仅比较模型，Study 2 为前后测。 |
| B5 | 主效应 | NA | — | 不存在因子设计意义上的主效应分析；单因素模型比较不按 B5 的因子设计主效应编码。 |
| B6 | 交互作用 | NA | — | 没有交互项检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序安排。 |
| B9 | 准实验设计 | 0.5 | PDF p7: Study 2 is a within-model pre/post design; p16 acknowledges 'alternative explanations ... simple expectation fulfilling remain'. | Study 2 的干预不是随机分配的单组前后测，且未系统说明准实验类型/选择偏差；但讨论了部分替代解释与因果限制，故部分满足。 |
| B10 | 被试内设计的适用条件 | 0 | PDF p7-8: models receive initial forecast then human-median intervention in same conversation; no reversibility or migration-symmetry argument. | 同模型前后测且信息暴露很可能不可逆，但全文未论证处理可逆性、迁移对称性或改用被试间设计。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥条件：Study 2 所有模型均接受前后测，Study 1 为观察性比较。 |
| C2 | 平衡 | 0 | PDF p7: initial prompt first, then intervention prompt; no counterbalancing described. | Study 2 存在条件顺序但固定，未报告任何顺序平衡方案。 |
| C3 | 恒定 | 0.5 | PDF p5: 'using default parameters (e.g., temperature) for all models'; web interfaces held constant; p7 same day human median. | 报告了部分恒定控制（查询方式、默认参数、同日中位数），但未系统列出所有恒定变量及其外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配或被试配对设计。 |
| C5 | 纳入为变量 | 0 | PDF p11-12: one-way ANOVA and Tukey HSD across models; Table 1 lists internet access/model features but no covariate or blocking model. | 潜在模型特征（联网、接入点、规模）被描述和事后比较，但未作为协变量/区组纳入分析，也未检验斜率齐性。 |
| C6 | 盲法 | NA | — | 数据采集与计分由自动化流程完成，无人类主试/评分者盲法问题。 |
| C7 | 平衡的层级 | 0 | PDF p7 fixed pre-then-post order; no balance hierarchy reported. | Study 2 有被试内顺序但未报告完全平衡/拉丁方/ABBA 等平衡层级。 |
| D1 | 练习效应 | 0 | PDF p7: 'two forecasts (pre- and post-intervention) per model run'; no practice/anchor control described. | 同会话前后测中初次回答可能产生练习/锚定效应，但未报告任何练习控制、截除或顺序抵消。 |
| D2 | 疲劳效应 | NA | — | LLM 网页查询为短时自动化任务，无人类疲劳或长 session 休息问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | Study 2 是单一干预后的前后测，不是多条件交叉设计；人类中位数暴露是目标处理而非需清洗的跨条件迁移。 |
| D4 | 不对称迁移 | NA | — | 不存在需要检验迁移对称性的交叉条件设计。 |
| D5 | 范围效应 | NA | — | 因变量是概率预测/Brier 分数，不是李克特式主观量表评定；无经典范围效应校准问题。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF p7: initial prompt then intervention prompt; no randomization/counterbalancing of within-model treatment order. | Study 2 的处理顺序固定，未做顺序随机化或反平衡；Study 1 问题上也无顺序控制报告。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表；acquiescence 是在概率预测均值偏高中观察和讨论的，不是反向计分题设计。 |
| E3 | 极端 / 中间反应倾向 | 0.5 | PDF p8: 'minimum raw forecast value of 0.1% and a maximum ... 99.5%, with a median forecast of 60%', mean 57.35; p10-11 Figure 5 and KDE. | 报告了预测分布的部分信息（均值、SD、中位数、极值与散点图）并讨论 acquiescence；但未报告偏度/端点比例，也未对跨模型反应风格差异作校正。 |
| E4 | 需求特征 | NA | — | 研究对象为 LLM，无人类被试的掩饰情节或事后访谈；提示词中的角色设定不属于人类需求特征检查。 |
| E5 | 实验者效应 | NA | — | 完全自动化查询与客观计分，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p8 reports forecast min/max/median/mean; p10-12 report Brier means, SD, KDE and raincloud plots. | 报告了因变量分布与端点范围，但未报告难度预实验校准或专门的偏度/端点频率分析。 |
| E7 | 共同方法偏差 | NA | — | 自变量为外部提示/模型条件，因变量为客观预测准确率；不存在同源自评共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | PDF p10-11 report Brier means, t tests and equivalence bounds; p12 and p14 use Benjamini-Hochberg correction. | 报告了部分效应量信息、多重比较校正与全部主要检验；但缺少主要效应的置信区间和样本量/功效确定依据。 |
| F2 | 内部效度 | 0.5 | PDF p7 within-model pre/post; p8 reports missing forecasts; p16 discusses confounds and alternative explanations. | 报告了数据缺失和部分内部效度威胁，但无随机分配、分配隐藏或系统基线等价性检验。 |
| F3 | 构念效度 | 0.5 | PDF p10 cites Brier score as a strictly proper scoring rule and defines scoring; p13 adds calibration analysis. | 预测准确率有公认计分规则支持，但未报告传统信度、操纵检验或对 acquiescence 构念的效度验证。 |
| F4 | 外部效度 | 0.5 | PDF p5: 31 Metaculus binary questions and 925 human forecasters; p16 discusses generalization limits of one tournament and curated questions. | 报告了样本来源与部分推广边界，但没有跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | PDF p7: each question posed three times; p14: paired tests with t(92); p10 main tests use question-level medians. | 描述了分配/测量层级，但 Study 2 的三次预测嵌套于 31 个问题，分析未用多层模型显式分离问题层方差。 |
| G2 | 随机效应 | 0 | PDF p11: one-way ANOVA across models; p14: paired t tests with t(92); no random-effect structure reported. | 未报告任何随机效应；重复问题/模型内的预测被当作独立观测处理，缺少对问题与模型抽样总体的随机效应建模。 |
| G3 | 材料作为随机效应 | 0.5 | PDF p10: median per question then average across all questions; p14: Study 2 tests over 93 forecasts per model, no item random effect. | Study 1 在一定程度上以问题为单位汇总，部分体现材料抽样；但 Study 2 未把问题作为随机项目效应，结论向问题总体的推广有限。 |
| G4 | 统计功效 | 0 | PDF p5-p7 methods and p10-p14 results; no a priori power analysis or target effect-size justification. | 无设计阶段功效分析或样本量论证；结果也未系统报告主要效应的 95% CI。 |
| G5 | 研究者自由度 | 0.5 | PDF p5 states analyses were preregistered and exploratory analyses are labelled; p8 reports 1007 collected/109 missing forecasts and model changes. | 报告了缺失/剔除与验证性/探索性区分，但未说明样本量决定方式或停止规则。 |
| G6 | 预先设定 / 预注册 | 0.5 | PDF p5: 'All analyses were preregistered on the Open Science Framework' with OSF link; exploratory analyses are labelled. | 有公开预注册链接并区分验证性/探索性分析；但文中未完整展开预注册的分析计划、样本量/停止规则与排除规则。 |
| J1 | 位置偏差 | NA | — | 研究不涉及多候选项选择、排序或 LLM-as-judge 成对比较，无候选位置偏差。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评价开放式生成质量；因变量为 Brier 分数，长度偏差不适用。 |
| J3 | 谄媚 | 0.5 | PDF p10 intervention gives human median and asks adjustment; p15 exploratory analysis asks whether updates are 'simply as an agreement-focused response'. | 人类中位数作为外部先验会影响更新，文中提示了 agreement-focused response 风险；但未做 pro-/anti framing 操纵，也未报告答案翻转率或系统谄媚测量。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge，因此无自我偏好裁判偏差。 |
| J5 | 少样本示例选择与排列偏差 | NA | PDF p7 Figure 1 and p9 Figure 3 prompts provide instructions rather than few-shot examples. | 实验为零样本提示，无 in-context few-shot 示例选择或排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p7 Figure 1, p9 Figure 3, p10 Figure 4 provide complete prompt templates; no sensitivity ablation or dev/test split described. | 完整提示模板可核查；但未做语义等价措辞敏感性分析，也未说明 prompt 是否在测试问题上调优。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | PDF p7 prompt contains background/resolution/question text; no long-document or RAG setting. | 上下文为单个预测问题，远非长上下文/RAG 场景。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p5: default parameters '(e.g., temperature)' and each model queried 'three independent times'; p14 reports SDs. | 报告了默认采样与重复次数 N=3，但未给出实际 temperature/top-p/seed 或精确 snapshot。 |
| J9 | 重复与文本退化 | NA | — | 因变量是概率数值和 Brier 分数，不是开放文本生成质量；重复/退化率不适用于主要分析。 |
| J10 | 分词效应 | NA | — | 单语言英文提示，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | PDF p2: 'the correct answer ... cannot be in a given LLM’s training set'; p16: queried in real time while answers were unknown. | 使用尚未发生、数据收集时无人知晓结果的前瞻性问题，训练数据污染答案的风险在设计上基本不存在。 |
| J12 | 基准饱和 | NA | PDF p10: Brier baseline 0.250 and LLM crowd M=0.20; p11 human crowd M=0.19. | 使用自定义问题集而非接近饱和的标准基准，分数离完美值 0 仍有距离，未出现基准饱和问题。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；主要任务是概率预测。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p5: prompt includes 'instructions on how to format the output'; footnote p5 codes bare Yes/No as 99%/1% in <1% cases; p10 specifies 'My Prediction: Between XX.XX% and YY.YY%'. | 要求并定义了结构化数值输出，也报告了少量格式异常处理；但未系统报告格式合法率或将格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估，无有害请求或对抗攻击设置。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p1 abstract frames 'wisdom of the silicon crowd'; p9 calls acquiescence 'machine-equivalent'; p3 directly compares to human crowd; p5-6 Table 1 lists models. | 明确把 LLM 预测/acquiescence 与人类构念对照，并做了人类同任务比较；但模型快照不精确，部分结论仍有从人类 crowd 概念向 LLM 外推的意味。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有报告随模型规模或训练进展的涌现/能力曲线，不涉及涌现指标假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N 或对代理指标进行优化的环节；仅为评估。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p5: web interfaces and default parameters, with footnote model-version changes; p8: 1007 forecasts; p14: SDs and repeated three runs. | 报告了重复次数/部分离散度和模型名称，但缺少精确 API 日期/commit snapshot、CI 与完整原始日志，复现性仅部分满足。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF p7: Study 2 collects 'two forecasts (pre- and post-intervention) per model run'; p14-15 report pre/post changes and Figure 9. | 有两轮对话式前后测并分别报告前后结果；但仅两轮、非长多轮，且未说明上下文截断/历史长度控制。 |

## 编码小结
论文对预测任务、提示词、聚合规则与 Brier 计分有较充分操作化，并报告了预注册与探索性分析标记；但采样参数/模型快照不精确，重复预测与问题嵌套未用多层模型处理，部分混淆控制、功效分析与预注册细节不足。许多人类被试特有的分配、盲法、需求特征等组件不适用；整体多数适用组件只能评为部分满足。
