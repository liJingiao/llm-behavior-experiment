# article_053 | KRISTEVA: Close Reading as a Novel Task for Benchmarking Interpretive Reasoning | 2025

研究类型概述：该文构建并发布 KRISTEVA 文学细读基准，包含 1331 道多选题（11 个任务类型，源自 49 篇大学文学课程考试作文），在零样本设置下评测 19 个 LLM，并用 3 名人类细读者对子集建立人类基线。分析单位主要是题目/任务与模型，属于基准评测而非随机分配的人类或动物实验。
- **研究构念（Construct）**：文学细读与阐释性推理（close reading and interpretive reasoning in literary language）｜CA 构念锚定：词汇通达（lexical access, `trm_4a3fd79d0b80f`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）；阅读（reading, `trm_4a3fd79d0aeb6`）
- **实验任务与范式（Task / Paradigm）**：该文构建并发布 KRISTEVA 文学细读基准，包含 1331 道多选题（11 个任务类型，源自 49 篇大学文学课程考试作文），在零样本设置下评测 19 个 LLM，并用 3 名人类细读者对子集建立人类基线。分析单位主要是题目/任务与模型，属于基准评测而非随机分配的人类或动物实验。｜CA 任务锚定：阅读广度任务（reading span task, `trm_4c40d168898db`）；句图匹配任务（sentence-picture matching task, `trm_4f241e8a01052`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | — | 本研究不是研究者主动操纵自变量的实验；11 个任务类型与 19 个模型是既有基准分层/被评对象，不是随机分配到水平的处理条件。 |
| A2 | 因变量 | 0.5 | p.5 “performed an exact match with the ground truth to assess accuracy”；p.6 Table 2 报告各题型与模型准确率及题量。 | 因变量指标与计分方式明确为多选题 exact-match accuracy，并给出题量；但未报告测量信度、效度、准确率置信区间或连续指标预处理/防天花板说明，故为部分完整。 |
| A3 | 控制变量 | 0.5 | p.5 “only use the instruction-tuned versions ... in a zero-shot setting”；“All experiments are conducted with the Language Model Evaluation Harness ... version 0.4.7”；脚注 4 说明省略 chain-of-thought。 | 报告了若干保持恒定的程序（zero-shot、instruction-tuned、同一 harness、统一 JSON prompt、无 CoT），但未系统列出控制变量清单及各自控制方式。 |
| A4 | 混淆变量 | 0.5 | p.9 Limitations: “MCQs contain LLM-generated distractors, which could bias the benchmark towards being more LLM-solvable”；human evaluators “disadvantaged by KRISTEVA’s MCQ format”；并提及 small sample size。 | 识别了若干潜在混淆（LLM 生成干扰项、人类不熟悉 MCQ、小样本、领域专长），但未给出控制方案或敏感性分析，仅作限制讨论。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量或调节假设，也没有相应交互检验。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或中介假设。 |
| A7 | 操作性定义 | 1 | p.5 Table 1 给出 11 个任务与 CRIT 步骤/推理类型映射；p.14 Table 3 给出每个任务输入/输出与完整问题模板；p.18 C.2 给出评测 prompt；p.5 说明 exact match 计分。 | 关键构念被操作化为具体题型、输入/输出 schema、数据构建流程和准确率计分，复现所需核心程序较完整。 |
| A8 | 水平数与类型 | NA | — | 11 个题型是基准分层/描述性任务类别，不是研究者操纵的多水平自变量；因此不按实验水平编码。 |
| A9 | 单一操作化的风险 | 0.5 | p.2 “operationalize three of CRIT’s six steps into 11 distinct and sequential tasks”；p.6 Table 2 报告各题型及总体平均。 | 用多种任务类型操作化细读过程，但未报告不同操作之间的会聚效度或正式多操作化验证，仅提供总体平均与题型分项。 |
| A10 | 单一方法的风险 | NA | — | 研究对象是 LLM 客观多选题输出与 exact-match 计分，不是同源自陈式量表，无共同方法偏差检验的适用场景。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或 LLM 试次被分配到互斥实验条件；研究为基准评测，不是被试间实验。 |
| B2 | 被试内设计 | NA | — | 没有对同一被试/模型按条件顺序进行重复测量并需平衡顺序的实验设计；题目独立呈现，不存在实验条件顺序。 |
| B3 | 混合设计 | NA | — | 不存在逐因素标注组间/组内的混合实验设计。 |
| B4 | 因子设计 | NA | — | 虽有 19 个模型 × 11 个题型的描述性结果矩阵，但不是实验因子设计，也未做 ANOVA 主效应/交互检验。 |
| B5 | 主效应 | NA | — | 无因子实验设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无实验交互项或简单主效应检验。 |
| B7 | 区组设计 | NA | — | 无区组设计或分层随机分配。 |
| B8 | 拉丁方 | NA | — | 无被试内条件顺序，无需拉丁方平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；没有非随机分组与因果效应宣称。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理设计，故不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有将分析单位随机分配到互斥实验条件；选项打乱不属于处理分配随机化。 |
| C2 | 平衡 | NA | — | 没有被试内条件顺序需要平衡；答案选项顺序问题在 E1/J1 处理。 |
| C3 | 恒定 | 0.5 | p.5 “only use the instruction-tuned versions ... in a zero-shot setting”；“All experiments are conducted with the Language Model Evaluation Harness ... version 0.4.7”；统一 JSON 评测 prompt。 | 报告了若干恒定程序，但未系统列出所有环境/模型版本/调用条件，也未讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后分配程序。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组/协变量纳入统计模型的分析。 |
| C6 | 盲法 | NA | — | 人类评估者只是回答基准题目以建立基线，不是接受实验处理或对模型输出进行条件盲评分，故盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | 没有跨条件的重复测量设计；人类评估者完成一个或两个单元测试，但不存在需 ABBA/练习块控制的实验条件顺序。 |
| D2 | 疲劳效应 | NA | — | 无长时程重复条件 session 设计；未构成实验疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个模型/题目评估不涉及跨条件残留或清洗期。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉设计，故无迁移对称性检验问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观 exact-match accuracy，不是被试内绝对判断或李克特量表评分。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.5 “the correct answer and distractors are merged into a final list of answer options, which is then shuffled, ensuring that there are no answer positional biases”；“presented in this arbitrary order in all the experiments”。 | 报告了答案选项打乱以避免位置偏差，但未说明随机化算法、各位置正确项分布或交换前后位置效应分析。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分题与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 主要评估为客观多选题，无需掩饰情节；人类基线评估者也非接受处理条件并可推断实验假设的实验被试。 |
| E5 | 实验者效应 | NA | — | LLM 评测完全自动化；人类评估者只是答题建立基线，不对实验条件评分，故主试/评分者盲法层级不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 2 报告各题型准确率与题量；例如 Q2 多个模型接近 98%，随机基线约 25%；但未给 SD、偏度或端点频率，也未说明 pilot 难度校准。 | 给出了准确率均值与题量，可部分看出任务难度和 Q2 接近天花板，但缺少分布统计与难度校准说明。 |
| E7 | 共同方法偏差 | NA | — | 不存在同源自陈式多构念测量，故共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.6 Table 2 报告所有模型/题型准确率、题量与随机基线；但全文未报告准确率差异的置信区间、显著性检验、多重比较校正或事前功效。 | 提供了较完整的描述性结果与样本量信息，但推断统计效度证据不足。 |
| F2 | 内部效度 | NA | — | 非实验基准评测，无随机分配、分配隐藏、被试流向或因果效应宣称，内部效度随机化组件不适用。 |
| F3 | 构念效度 | 0.5 | p.7 “Agreement scores range from 0.523 ... to 0.644, indicating moderate consensus”；p.2-3]] 通过 CRIT 框架论证任务构念。 | 报告了人类评估者间 Krippendorff α 及构念来源，但未报告基准题项本身的信度/效度、LLM 操纵检验或多操作化会聚证据。 |
| F4 | 外部效度 | 0.5 | p.4 “49 de-identified essays ... from three exams in a university-level literature course”；p.9 “scope ... limited to the classroom data of one course”，并讨论 introductory level、English texts 等边界。 | 报告了数据来源、样本特征与部分推广边界，但未报告跨课程/跨情境复现。 |
| G1 | 分析单位 | 0.5 | p.5 逐题 exact-match；p.6 Table 2 按题型报告题量与准确率；但未说明题目嵌套于作文/课程的聚类结构如何处理。 | 分析单位可辨认为题目/模型层级，但未显式建模题目嵌套于作文或任务层级的聚集方差。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；被比较的 19 个模型是固定的评估对象，而不是从模型总体抽样的随机效应单位。 |
| G3 | 材料作为随机效应 | 0.5 | p.4 由 49 篇作文构建 1331 道题；p.5 从作文抽取特征/语境并生成题目；分析仅报告聚合准确率。 | 题目/作文明显来自更大材料总体，但分析未将题目或作文作为随机效应，结论向新材料推广的统计处理不足。 |
| G4 | 统计功效 | 0 | p.6 Table 2 给出题量与准确率；全文未报告事前功效分析、目标效应量或准确率置信区间。 | 没有设计阶段功效分析或等效的样本量论证，结果也未给 CI，无法判断检验敏感度。 |
| G5 | 研究者自由度 | 0.5 | p.4 以 instructor grade 过滤并排除低于 80% 的作文；p.5 报告 11 个题型和 19 个模型，称无不可解析输出。 | 报告了数据过滤规则与全部题型/模型结果，但未说明样本量停止规则、分析计划或验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–22 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文没有预注册平台、编号或分析计划；也未明确区分验证性与探索性分析。 |
| J1 | 位置偏差 | 0.5 | p.5 正确答案与干扰项合并后 “shuffled, ensuring that there are no answer positional biases”；所有实验以 arbitrary order 呈现。 | 对候选项位置做了打乱，但未报告各位置正确率、交换前后偏好翻转或位置×正确率分析；不是 LLM-as-judge，但位置偏差风险已部分控制。 |
| J2 | 冗长偏差 | NA | — | 评估为多选题 exact-match，不涉及开放式生成质量的长短比较或 LLM 裁判长度偏差。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场/framing 操纵，不涉及谄媚偏差。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 评估模型输出；o1-preview 仅用于生成干扰项，不是裁判。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.5 “in a zero-shot setting”；无 few-shot in-context examples。 | 零样本评测，不涉及 few-shot 示例选择与排列偏差。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.18 C.2 给出完整评测 prompt 与 JSON 输出格式；p.17 给出干扰项生成 prompt；但未报告语义等价措辞的敏感性消融或 dev/test 划分。 | 提示模板基本公开，但只有单一版本，未系统评估 prompt 脆弱性。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务使用短文学 passage 的逐题问答，非长上下文/RAG 位置效应实验；未以窗口长度为核心。 |
| J8 | 温度与采样随机性 | 0 | p.5 仅说明使用 Language Model Evaluation Harness 与 zero-shot；未报告 temperature、top-p、seed、重复采样次数或 API snapshot。p.6 Table 2 为单点准确率。 | LLM 非确定性未被纳入统计设计；采样超参数和重复运行信息缺失。 |
| J9 | 重复与文本退化 | NA | — | 输出为短 JSON 多选题答案，不涉及开放生成重复/退化问题。 |
| J10 | 分词效应 | NA | — | 实验为英语单语言、单脚本文本，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.1 称 KRISTEVA 为新 benchmark；p.4 数据来自课程作文；但全文未报告模型训练截止日期、测试集版本与训练语料重叠检测。 | 虽为新收集课堂数据，但未按编码表要求对照训练截止日期或做污染检测，无法将记忆与泛化区分。 |
| J12 | 基准饱和 | 0.5 | p.6 Table 2 总体准确率约 49.7%–69.7%，Q2 多模型接近 98%；未报告 bootstrap CI 或饱和处理。 | 报告了分数量程与 SOTA 位置，也可见个别题型接近天花板，但未正式讨论饱和或改用连续指标/更难子集。 |
| J13 | 指令遵循 | NA | — | 因变量是文学细读多选题准确率，不是指令遵循；JSON 格式仅作为输出约束，不构成 IFEval 式指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.5 要求 JSON 格式；“no outputs were unparseable”；p.18 给出 JSON schema。 | 报告了结构化输出设置与隐含 100% 可解析率，但未单列格式合法率/重试策略，也未把格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 不是安全/越狱评估，无有害请求或攻击成功率测量。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文将细读作为 LLM 能力基准，并在 Appendix A 明确避免把 understanding/judgment 等心理属性直接归给 LLM；不是把 LLM 当作心理学被试的构念测量研究。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有宣称涌现能力，也没有跨规模训练进展的能力曲线；仅有不同模型规模的一般描述比较。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及以 benchmark/奖励模型/LLM-judge 为优化目标的训练、RL 或 best-of-N 过优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.5 使用 Language Model Evaluation Harness version 0.4.7 并公开数据集；但 p.6 Table 2 只给单点准确率，未报告重复次数、95% CI、精确 API snapshot 日期或配对检验。 | 有公开数据和 harness 版本，但缺少非确定性评估所需的重复、置信区间、精确模型 snapshot 与配对比较，复现证据不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮多选题作答，无对话历史累积或多轮一致性衰减问题。 |

## 编码小结
论文清楚报告了基准构建、任务操作化、提示模板、准确率计分和人类基线；但作为 LLM 基准，缺少采样超参数与重复运行/置信区间、精确 API snapshot、污染检查，且未对题目/作文等材料做随机效应建模。多数人类实验设计组件因无受控分配而记 NA；关键方法学短板集中在评估可复现性、随机性与材料推广性。
