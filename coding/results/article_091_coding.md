# article_091 | SCOP: Evaluating the Comprehension Process of Large Language Models from a Cognitive View | 2025

研究类型概述：LLM基准评测研究：提出五项阅读理解技能（locating, inferring, connecting, organizing, selecting），从12个数据集构造4,682条测试样本，并用document-level accuracy比较GPT-4o、Claude-3.5-sonnet、Llama3.1-70B-Instruct、Qwen2-72B-Instruct等模型。分析单位主要是测试文档/题目与模型输出，不涉及人类被试分配。
- **研究构念（Construct）**：阅读理解过程、局部/全局表征与定位—推断—连接—组织—选择技能｜CA 构念锚定：词汇通达（lexical access, `trm_4a3fd79d0b80f`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）；阅读（reading, `trm_4a3fd79d0aeb6`）
- **实验任务与范式（Task / Paradigm）**：LLM基准评测研究：提出五项阅读理解技能（locating, inferring, connecting, organizing, selecting），从12个数据集构造4,682条测试样本，并用document-level accuracy比较GPT-4o、Claude-3.5-sonnet、Llama3.1-70B-Instruct、Qwen2-72B-Instruct等模型。分析单位主要是测试文档/题目与模型输出，不涉及人类被试分配。｜CA 任务锚定：阅读广度任务（reading span task, `trm_4c40d168898db`）；句图匹配任务（sentence-picture matching task, `trm_4f241e8a01052`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.7: Figure 3 compares 'with SS' vs. 'without SS'; p.6: 'We set the temperature for all LLMs to 0'. | 主要设计是基准评测，无经典实验操纵；但辅助分析明确操纵了是否提供支持句（with/without SS）。两个水平存在，但未说明分配程序、每条件样本构造细节或操纵检验，故为0.5。 |
| A2 | 因变量 | 0.5 | p.6: 'We use document-level accuracy ... exactly match the golden results, divided by the total sample size.'; p.14: validity score 0.81, inter-annotator agreement 73%. | 因变量指标和计分方式明确，且有数据有效性人工核查；但未报告模型输出的信度、重复测量稳定性，也未讨论连续指标预处理或天花板/地板效应，故为0.5。 |
| A3 | 控制变量 | 0.5 | p.6: 'We set the temperature for all LLMs to 0'; p.6: 'The prompts for all tasks are listed in the Appendix D.' | 报告了温度与提示模板等控制，但未系统列出所有控制变量及控制手段，故为0.5。 |
| A4 | 混淆变量 | 1 | p.6: 'we further exclude questions that can be directly answered by advanced LLMs ... without referring to the document'; p.9: 'some data might already be known to LLMs'. | 识别了记忆/污染这一主要混淆，并通过过滤、pilot对照与局限性讨论控制及说明残余威胁，基本达到1。 |
| A5 | 调节变量 | NA | — | 理论模型不包含调节变量，也未做调节效应检验。 |
| A6 | 中介变量 | NA | — | 理论模型不包含中介变量，未做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.3 Table 1 defines five tasks with inputs/outputs; pp.3-6 give data construction rules; p.6 defines accuracy; pp.22-25 give full prompts. | 五个技能的输入输出、数据筛选、评分方式和提示操作化较完整，可供复现。 |
| A8 | 水平数与类型 | 0.5 | p.3 Table 1 lists five skills/tasks; p.7 Figure 3 shows with/without SS; p.6 lists four main LLMs. | 技能/模型/数据类别水平明确，但未系统说明自变量水平类型、间距、全距或连续变量中心化；SS条件也未形式化为完整水平设计，故为0.5。 |
| A9 | 单一操作化的风险 | 1 | pp.3-6 use multiple datasets per skill; p.8 Figure 4 reports inter-task correlations validating the framework. | 关键技能采用多个数据集/任务操作化，并报告任务间相关作为会聚证据，达到1。 |
| A10 | 单一方法的风险 | NA | — | 研究不是自陈式多构念测量，不存在人类研究意义上的共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试或被试组分配；模型在同一测试数据上比较，不是被试间实验。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量和条件顺序平衡；LLM逐题独立调用，不适用经典被试内设计。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内混合实验设计。 |
| B4 | 因子设计 | NA | — | 研究不是全因子实验；模型、技能、文档类型、答案样式只是评测分层/描述变量，没有完整因子设计矩阵。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无实验交互项检验；仅做描述性比较与相关分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；无随机分配失败后的准实验因果推断框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理顺序，不涉及处理可逆性/迁移对称性。 |
| C1 | 随机化 | NA | — | 无处理条件到互斥被试组的随机分配。 |
| C2 | 平衡 | NA | — | 无条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p.6: 'We set the temperature for all LLMs to 0'; p.6: prompts in Appendix D; p.9: results may be sensitive to prompts. | 温度与提示被固定，但未系统列出模型版本、API环境、解码设置等恒定变量及其外部效度限制，故为0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或人类评分者需要盲法。 |
| C7 | 平衡的层级 | NA | — | 无条件顺序平衡层级可编码。 |
| D1 | 练习效应 | NA | — | LLM逐题独立提示，无练习块或上下文内学习。 |
| D2 | 疲劳效应 | NA | — | 无人类session疲劳或休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个测试样本独立，无跨条件清洗期或迁移。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移，不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 因变量为客观accuracy，无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | p.22-25 prompts present fixed option/candidate lists; no randomization or counterbalancing reported. | 多项选择选项、连接任务候选句、组织任务subheadings均按固定顺序呈现，未报告随机化或反平衡，存在位置/顺序偏差风险。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无极端/中间反应倾向。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或掩饰情节。 |
| E5 | 实验者效应 | NA | — | 自动化LLM调用，无人类主试或评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0 | p.6 Table 3 reports aggregate accuracy only; SQuAD scores reach 98.96-99.16 but no distribution/SD/skew/endpoint discussion. | 报告了均值式accuracy，但未报告分布、端点频率或pilot难度校准；且存在接近天花板的SQuAD成绩未讨论。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，无共同方法偏差检验需求。 |
| F1 | 统计结论效度 | 0 | p.6 Table 3 reports accuracy percentages; no confidence intervals, effect sizes, significance tests, or multiplicity correction. | 有描述性准确率与样本量，但未报告效应量/置信区间、推断统计与多重性校正，未达到基本要求。 |
| F2 | 内部效度 | NA | — | 非随机分配实验，不主张实验因果效应；污染等内部效度威胁已在A4处理。 |
| F3 | 构念效度 | 0.5 | p.6: human validity 0.81, inter-annotator agreement 0.73; p.8 Figure 4 inter-task correlations; no manipulation check. | 报告了数据有效性和IAA及任务相关，但无操纵检验，构念效度证据不完整，故为0.5。 |
| F4 | 外部效度 | 0.5 | p.6 Table 2 lists 12 datasets and sizes; p.7 discusses document types and answer styles; no representative sampling. | 报告了数据来源、模型类型与文档/答案边界，但未系统论证样本代表性或跨情境复现，故为0.5。 |
| G1 | 分析单位 | 0.5 | p.6: 'We use document-level accuracy ... divided by the total sample size'; no mixed/hierarchical model for item nesting. | 明确了统计层级为document-level accuracy，但未讨论题目嵌套于数据集/模型重复调用的聚集结构，故为0.5。 |
| G2 | 随机效应 | NA | — | 无人类被试随机效应；模型比较按固定模型处理，项目随机效应在G3单独判断。 |
| G3 | 材料作为随机效应 | 0.5 | p.6 Table 2 uses multiple datasets per skill; pp.7-8 analyze per-dataset accuracy and inter-task correlations; no item random-effect model. | 使用多个数据集/大量项目并在多个材料上比较，但未在统计模型中纳入item random effect或准F比，故为0.5。 |
| G4 | 统计功效 | 0 | p.6 Table 2 reports sample sizes; no a priori power analysis or effect-size/CI justification. | 未做事前功效分析或样本量论证；结果也未报告效应量与CI。 |
| G5 | 研究者自由度 | 0.5 | p.6 reports filtering 33,827 noise samples from 37,023 and all five skills; p.9 limitations; no preregistered analysis plan. | 报告了数据过滤规则、各数据集样本量和全部五个技能结果，但未说明样本量决定方式、optional stopping或验证性/探索性分析区分，故为0.5。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered analysis plan is reported in the paper. | 无预注册；研究不是明确声明的纯探索性研究，故记0。 |
| J1 | 位置偏差 | 0 | p.22-25 prompts show fixed multiple-choice options and candidate orders; no A/B swap or position-randomization report. | 涉及多项选择、候选句排序等位置风险，但完全未报告位置反平衡、随机化或位置×正确率分析。 |
| J2 | 冗长偏差 | NA | — | 不使用LLM裁判或开放式生成质量评分；评估为精确匹配accuracy。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈纠错或多轮对话式评估。 |
| J4 | 自我偏好 | NA | — | 不涉及LLM-as-judge或模型输出成对比较。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.22-25 prompts each include one worked example; no report of example source, sampling, order counterbalancing, or multiple example seeds. | 使用了one-shot/few-shot示例，但未报告示例来源、标签比例、排列反平衡或多seed重采样。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | pp.22-25 provide complete prompts; p.9 says results may be sensitive to prompts; no versioned sensitivity ablation or dev/test split. | 完整prompt模板已给出，但未报告版本化、语义等价措辞消融或dev/test划分，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是长上下文/RAG设置；文档最大约4,583 tokens（p.13 Table 5），远低于现代LLM窗口，未操纵关键信息位置。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'We set the temperature for all LLMs to 0'; no seeds, top-p/top-k, repeated sampling, or CIs reported. | 报告了temperature但未报告seed、其他采样参数、重复次数与置信区间，故为0.5。 |
| J9 | 重复与文本退化 | NA | — | 任务输出为短JSON/列表，非开放式长文本生成，文本退化风险不适用。 |
| J10 | 分词效应 | NA | — | 单语言英文评估，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.6 filters questions answerable without document; p.9: 'some data might already be known to LLMs'; no training-cutoff versus test-date comparison. | 识别并部分控制污染，但未报告模型训练截止日期与测试集发布日期的系统对照或污染率检测，故为0.5。 |
| J12 | 基准饱和 | 0.5 | p.6 Table 3 reports high locating scores (e.g., SQuAD 98.96-99.16) and low other scores; no SOTA/saturation or CI comparison discussion. | 报告了分数量程内的当前结果，但未识别部分数据集接近天花板、未改用连续指标或CI比较，故为0.5。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，不涉及约束型指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | pp.22-25 require JSON/List output only; no format-valid rate or retry/post-processing report. | 报告了结构化输出要求，但未报告格式合法率、重试策略，也未将格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估或有害请求。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 and p.2 frame the work as evaluating LLM comprehension from a cognitive view and compare patterns to experts/humans; model names but no weight snapshots. | 明确将LLM放在认知/阅读理解构念下评估，并引用人类理论，但未系统论证LLM构念与人类同名构念的异同，也无同范式人类对照，故为0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨模型规模/训练进展的能力曲线或涌现能力宣称；仅补充测试Llama-3.1-7B并排除。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 纯基准评估，无训练/RL/best-of-N等对代理指标的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.6 names models but no exact snapshots/API dates, repeat count, confidence intervals, or paired tests are reported. | 只报告单点准确率；无重复次数、CI、精确snapshot标识或配对检验，评估可复现性不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 所有任务为单轮提示，无多轮对话历史累积，也不主张多轮部署。 |

## 编码小结
该文是较完整的LLM阅读理解过程基准，任务与数据构造、评分指标和提示模板报告较充分；但作为基准评测，许多人类实验设计组件不适用。LLM特有风险中，位置偏差、few-shot示例来源、提示敏感性、采样随机性、污染、格式合法率与评估可复现性等报告不完整或缺失。
