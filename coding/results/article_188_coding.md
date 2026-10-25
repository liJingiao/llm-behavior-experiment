# article_188 | MoCa: Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks | 2023

研究类型概述：LLM-as-participant 的基准/观察性比较研究：从24篇认知科学论文整理206个因果与道德判断故事，收集每故事25名人类回答，并对多种LLM进行零样本、persona与自动prompt优化条件下的判断比较；用AMCE比较人类与模型对各故事因素属性的隐含倾向。无人类被试随机分配实验，LLM调用为独立单轮。
- **研究构念（Construct）**：因果与道德判断中的规范违背、可避免性、行为者角色和手段—副作用差异｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）；社会规范加工（social norm processing, `trm_58c80b824c51b`）
- **实验任务与范式（Task / Paradigm）**：向多个预训练或API模型呈现来自认知科学研究的受控因果和道德故事，要求二元或等级判断，并与原始人类数据的因素效应比较。（操纵因果正常性、规范类型、道德受益者、伤害可避免性、行动者或患者、个人力量和手段或副作用等因素。）｜CA 任务锚定：道德困境任务（Moral Dilemma Task, `trm_57ebe6583f52d`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_5: “We choose a wide range of language models”；PDF_PAGE_6: “we sample 5 personas from 5 simulacra ... (25 in total)”；PDF_PAGE_7: “APE ... five stories as training examples”。 | 模型与prompt方法可视为比较条件，水平与部分程序有报告；但因素属性并非研究者随机操纵，且无分配方式/操纵检验，故仅部分满足。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_5: “We conduct a 3-class comparison to compute accuracy ... We normalize the model output probability”；PDF_PAGE_6 Table 3: “95% bootstrapped confidence interval ... Agg, AUC, MAE, CE”。 | 因变量指标与计分方式明确；但未报告LLM判断的信效度证据，连续指标主要为聚合指标，预处理/天花板说明不足。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_20: “we only generate one response per story and set P = 1 for the chosen response”；PDF_PAGE_30 Table A7记录各API模型access date与snapshot。 | 报告了固定模型版本/访问日期与固定prompt等控制，但未系统列出全部控制变量及控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_24: “stories we collected might be implicitly biased by our selection process. So it is possible that the AMCE ... is a biased estimate”；PDF_PAGE_10: “small-scale analysis ... model hallucinations”。 | 识别了故事选择偏差与幻觉混淆，并讨论了残余威胁；但无实验控制或敏感性分析消除混淆。 |
| A5 | 调节变量 | 0 | PDF_PAGE_1: “LLMs weigh the different factors quite differently from human participants”；PDF_PAGE_8-9 Figures 2/3仅分别展示人类与模型AMCE。 | 若将系统类型/模型视为调节变量，论文仅做分组AMCE与图形/CI比较，未报告正式的系统×因素交互检验或简单斜率。 |
| A6 | 中介变量 | NA | — | 理论模型与实证分析均不包含中介变量或中介效应分解。 |
| A7 | 操作性定义 | 0.5 | PDF_PAGE_18-19 Table A1逐一定义因素与属性；PDF_PAGE_20 A.3描述Yes/No概率计分；PDF_PAGE_29 A.15描述人类作答界面。 | 关键构念有可观测标注与计分说明，但完整零样本prompt及部分操作细节置于补充材料，复现所需信息仅部分报告。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_5 Table 2列出各因素属性；PDF_PAGE_19 Table A1给出定义；PDF_PAGE_7说明Time为3水平但仅取Early/Late。 | 水平数与标签基本明确；未明确说明水平类型、间距/全距（对分类变量意义有限）及连续变量中心化处理。 |
| A9 | 单一操作化的风险 | 0.5 | PDF_PAGE_30: “Our focus is narrow and only on certain aspects of alignment ... cannot ... sweeping ...”；PDF_PAGE_24 A.6提到人类道德直觉个体差异并留待未来工作。 | 关键因变量采用单一Yes/No操作，文中讨论了范围窄与不可过度推广；但未系统讨论单一操作化边界或多操作会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 因素标注来自专家，人类回答来自Prolific被试，模型输出来自API；不同构念来源不同，非自评量表同源问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试或LLM单元被随机分配至互斥条件的被试间实验；模型比较是基准评测分组而非实验分配。 |
| B2 | 被试内设计 | NA | — | 无被试内条件顺序设计；同一模型在不同prompt/故事上的调用为独立评测，不存在需要顺序平衡的重复测量处理。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内因素混合的实验设计。 |
| B4 | 因子设计 | NA | — | 因素属性由故事内容标注后进行AMCE分析，不是完全交叉的随机化因子实验，也无设计矩阵/每格样本量。 |
| B5 | 主效应 | NA | — | 不是因子实验，无ANOVA主效应可编码；AMCE为属性差异估计而非因子ANOVA主效应。 |
| B6 | 交互作用 | NA | — | 无设计层面的交互项统计检验；仅分别展示人类与各模型AMCE，未做模型×因素正式交互分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层分配设计。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理分配研究；故事来自既有文献，模型与人类比较为基准评测而非非随机处理比较。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理条件，故不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无随机分配单元到实验条件的程序；LLM为单次/单条件评测，人类只为每故事提供判断。 |
| C2 | 平衡 | NA | — | 无实验条件顺序需平衡；LLM调用独立，人类故事呈现顺序问题另在E1评估。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_20 A.3固定“one response per story”与prompt；PDF_PAGE_30 Table A7列出模型access date/snapshot。 | 报告了模型版本/API日期与统一prompt等恒定控制，但未系统列出恒定变量清单或讨论其外部效度限制。 |
| C4 | 匹配 | NA | — | 无匹配设计或匹配变量。 |
| C5 | 纳入为变量 | NA | — | 未把混淆变量作为区组或协变量纳入统计模型；AMCE因素为标注属性而非协变量控制。 |
| C6 | 盲法 | NA | — | 无人类被试分组或评分者条件需要盲法；LLM评测无主试盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级选择。 |
| D1 | 练习效应 | NA | — | LLM每故事独立调用，无练习/学习顺序；人类任务为短故事判断且无练习条件设计。 |
| D2 | 疲劳效应 | NA | — | 无长session疲劳设计；每名人类被试仅5-6个故事，LLM为独立调用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留或清洗期设计；故事/API会话独立。 |
| D4 | 不对称迁移 | NA | — | 无迁移对称性检验设计。 |
| D5 | 范围效应 | NA | — | 因变量为Yes/No判断，不是量表式绝对判断，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_24 A.7: “we randomly sample the stories to present to the respondents”；PDF_PAGE_29 A.15: “one story at a time”。 | 人类多故事呈现有随机抽样/呈现说明，但未报告逐位置平衡或顺序效应检验；LLM单prompt无顺序问题。 |
| E2 | 默认赞同 | NA | — | 任务使用Yes/No二分判断，不使用Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表分布与反应风格比较。 |
| E4 | 需求特征 | NA | — | 标准因果/道德判断任务，无掩饰情节或实验条件；被试难以推断模型对齐假设，需求特征风险不构成本研究设计层组件。 |
| E5 | 实验者效应 | NA | — | 数据采集通过Prolific界面和API自动化完成，无人类主试/评分者实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_4 Table 1报告Yes/No/ambiguous分布；PDF_PAGE_26 Figure A4报告P(Yes)分布；PDF_PAGE_6 Table 3报告模型指标与CI。 | 报告了标签分布和部分端点信息，但未说明pilot难度校准或系统排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 因素标注、人类回答与模型输出来源不同，非同源自评多构念测量。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_6 Table 3: “95% bootstrapped confidence interval”并报告Agg/AUC/MAE/CE；PDF_PAGE_4每故事25人。 | 报告效应估计与bootstrap CI，但无样本量功效依据，且多模型/多因素分析未见多重性校正说明。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_24 A.7讨论AMCE假设与选择偏差；PDF_PAGE_10报告幻觉小样本检查。 | 评估了内部效度威胁（选择偏差、因素非随机、幻觉），但无随机分配/分配隐藏/被试流向等实验内部效度程序。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_29 A.14报告专家标注IoU；PDF_PAGE_10 Table 4报告幻觉检查；PDF_PAGE_7-8用AMCE衡量隐含倾向。 | 有专家标注一致性和幻觉检查，但缺少判断测量的正式信效度证据与操纵检验；单一操作化局限仅部分讨论。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_29 A.15: “Prolific ... US and UK, with English as their first language”；PDF_PAGE_30: “focus is narrow ... cannot ... sweeping ...”。 | 报告了人类样本来源与推广边界，但未做跨样本/跨情境复现，也未系统讨论故事与模型总体的代表性。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_7 AMCE公式以N responses、K stories、J factors定义；PDF_PAGE_4每故事25个回答；PDF_PAGE_29描述单个被试多个故事。 | 说明了分析以故事因素和回答为层级，但未明确处理/分配层级与嵌套结构，也未用多层模型分离故事/被试方差。 |
| G2 | 随机效应 | 0 | PDF_PAGE_7 AMCE使用非参数difference-in-means与bootstrap；全文未报告随机截距/随机斜率或被试、故事随机效应结构。 | 需要跨故事/被试推广时，未说明随机/固定效应，未将被试或故事作为随机效应；仅用汇总/差均值和bootstrap。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_24: “stories ... might be implicitly biased by our selection process”；全文未将故事/项目作为随机效应纳入模型。 | 作者承认故事集合固定且可能有选择偏差，但分析未把材料作为随机样本/随机效应处理。 |
| G4 | 统计功效 | 0.5 | PDF_PAGE_6报告95% bootstrap CI；PDF_PAGE_4报告每故事25人；全文未报告事前功效分析或样本量推导。 | 结果报告了效应估计与CI，但缺少设计阶段功效分析/样本量依据。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_31 A.18.4: “We rejected participant labels if they didn’t spend an adequate amount of time”；PDF_PAGE_10说明幻觉分析为“small-scale”。 | 报告了人类标签剔除规则并区分部分小规模分析，但未完整说明全部条件/分析选择、停止规则及验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未见预注册平台、注册编号或时间戳；PDF_PAGE_7-10多数分析为完成后报告。 | 无公开预注册，也未系统区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 任务为每题单一Yes/No判断，不涉及多候选项位置、排序或LLM-as-judge成对比较。 |
| J2 | 冗长偏差 | NA | — | 主要指标为标签概率/一致性，不涉及开放式生成长度与质量评分。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错的多轮对话式评估。 |
| J4 | 自我偏好 | NA | — | 不使用LLM-as-judge；以人类聚合回答为参照。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF_PAGE_26 A.10: “We manually write a few examples”；PDF_PAGE_27 Table A4: “run models 5 times ... 95% confidence intervals”；PDF_PAGE_28 A.11给出示例prompt。 | 因子推断实验使用手工few-shot示例并重复5次，但未报告示例抽样/比例、排列反平衡或多示例集seed。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_21 A.5给出persona/APE模板“James gave these answers ... James is a [PROMPT]”；PDF_PAGE_7说明5个训练故事与prompt搜索；PDF_PAGE_9报告prompting methods会改变AMCE。 | 有prompt模板、搜索过程与部分dev/test分离，但无版本号/日期及系统语义等价敏感性消融，完整模板亦不充分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 故事上下文短，远低于长上下文/RAG设置，无关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_20 A.3: “temperature-based sampling ... sampled 10 responses for a few stories ... always get the same response ... only generate one response per story”；PDF_PAGE_30 Table A7列API日期/snapshot。 | 报告了部分采样尝试、单响应策略和API snapshot，但未报告temperature数值、top-p/seed及主实验重复采样N与CI。 |
| J9 | 重复与文本退化 | NA | — | 主要输出为Yes/No标签或概率，不涉及开放生成重复/退化QC。 |
| J10 | 分词效应 | NA | — | 材料为英文单语，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_30 Table A7仅列模型access date/snapshot；全文未见训练数据截止日期与测试集n-gram/DCQ污染检测。 | 使用来自已发表论文与公开网络语料的测试故事，但未评估训练/测试污染，也未区分记忆复现与泛化。 |
| J12 | 基准饱和 | NA | PDF_PAGE_6 Table 3显示总体Agg约30–43%、AUC最高约0.74，分数远未接近天花板。 | 基准难度高且当前分数远离饱和区，饱和风险不构成本研究主要问题。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；Yes/No作答是任务反应格式而非IF指标。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 未采用JSON/grammar-constrained结构化输出；Yes/No或“not sure”文本解析不属于本组件所指格式约束实验。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估或有害请求。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF_PAGE_1: “test whether LLMs make causal and moral judgments ... align with those of human participants”；PDF_PAGE_2: “LLM implicit tendencies”；PDF_PAGE_30: “focus is narrow ... cannot ... sweeping ...”；PDF_PAGE_30 Table A7报告模型snapshot。 | 明确把LLM输出解释为隐含倾向并与人类同名判断做同范式比较，且限制过度外推；但未系统论证LLM构念与人类构念的理论异同。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告跨训练进展的涌现能力曲线，也未作“突然涌现”宣称；仅有跨模型大小比较与 inverse-scaling 推测。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | PDF_PAGE_7 APE用5个训练故事选择prompt并称这些故事从结果中排除；PDF_PAGE_6 Table 3b报告优化后结果。 | 存在以训练故事为代理选择prompt、在其余故事评估的分离；但未报告优化轮数与代理-人类金标准双曲线/过优化拐点。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_6报告bootstrap CI；PDF_PAGE_30 Table A7报告API access date与部分snapshot；PDF_PAGE_26因子推断运行5次。 | 有部分重复、CI与snapshot信息，但主对齐实验每故事仅一次响应，模型间比较未报告配对检验，原始推理日志/完整prompt集不充分。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮故事判断，无对话历史累积或多轮一致性评估。 |

## 编码小结
核心贡献是构建带专家因素标注的因果/道德判断挑战集，并在聚合AMCE层面比较LLM与人类。研究对模型版本、指标和部分推断不确定性有报告，但作为因果推断基础的AMCE依赖故事因素近似随机化，作者也承认选择偏差；缺少正式交互检验、随机效应模型、预注册与污染检查。整体上设计透明但若干推断与推广限制仅为部分报告。
