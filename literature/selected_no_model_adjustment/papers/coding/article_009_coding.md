# article_009 | CLadder: Assessing Causal Reasoning in Language Models | 2023 (NeurIPS 2023)

研究类型概述:LLM 基准构建与评测研究(无人类被试;以 LLM 为被试)。算法生成 10K 因果推理问答题(CLadder),比较 8 个 LLM 及 GPT-4+CausalCoT 提示。自变量为模型/提示策略、因果阶梯层级(Rung 1-3)、查询类型、常识对齐度(commonsensical / anti-commonsensical / nonsensical);因变量为 Yes/No 回答准确率(另有分步骤 F1、ROSCOE 推理质量分)。

> 说明:编码表实际共 69 行(A10+B10+C7+D5+E7+F4+G6+J20),非任务说明中的 70。

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | §5.1/Table 2 (p.8):模型与 +CausalCoT 为水平;§3.2 (p.5):"we also generate various anti-commonsense and nonsensical variants of the stories" | 自变量及水平清晰、操纵程序可复现;缺操纵检验(未检验 anti-/nonsensical 改写是否确实达到预期的反常识程度),单位分配仅隐含(每模型作答全部题目) |
| A2 | 因变量 | 0.5 | §3 Task Formulation (p.4):"our main task is to test the accuracy of the prediction function f : q ↦ a"; §3.4 (p.7):"one expert evaluator tried to solve a random sample of 50 questions... accuracy of 82%" | 指标(Yes/No 准确率)与计分明确;有标准答案由 oracle CI engine 生成及人类基准,但无信度类证据、未讨论天花板/地板的处理 |
| A3 | 控制变量 | 0.5 | §5.1 (p.8):"We use the OpenAI API with temperature 0"; Appendix A.4 (p.20):"we balance the distribution of correct answers so that there are the same number of 'yes's and 'no's"; §3 Design Principles (p.4):"we avoid settings that involve continuous variables and use binary variables" | 列出了若干被控因素及手段(温度、答案类别均衡、变量二值化、图规模),但未作为"控制变量清单"系统呈现,开源模型的解码设置未报 |
| A4 | 混淆变量 | 0.5 | §3.2 (p.5):"it is very likely that at least some of the stories appear in the training data... Therefore, we also generate various anti-common sense and nonsensical variants of the stories, meant to isolate the effects of memorization" | 识别了"记忆/污染"这一混淆并用设计控制;模型规模/家族/指令微调相互混杂、残余混淆(如 GPT-4 版本差异)未讨论 |
| A5 | 调节变量 | 0 | Table 2 (p.8) 按 Rung 与常识对齐度分层报告准确率 | 未将任何变量界定为调节变量,也未做交互检验(仅描述性分组准确率) |
| A6 | 中介变量 | NA | — | 研究本身不检验中介路径(NDE/NIE 是被测题目内容,不是本研究的中介分析) |
| A7 | 操作性定义 | 1 | Appendix B.1 (p.22) 完整 CausalCoT 提示;Appendix A.5 (p.21) Table 4 问句模板;§1 脚注1 (p.1):"our code can be found at https://github.com/causalNLP/cladder" | 因果推理能力被操作化为 CI engine 生成的带标准答案的 Yes/No 题;题目生成、模板、提示与代码均可复现 |
| A8 | 水平数与类型 | 1 | §3.1/Appendix A.3 (p.20):"ten causal graphs with treatment-effect pairs"; Fig.3/Appendix A.2:10 种查询类型;§3.3/Table 2 三个常识对齐水平 | 各自变量水平数及标签均列出,为名义/等级类别型;不涉及连续水平间距 |
| A9 | 单一操作化的风险 | 1 | §3/Fig.2 (p.4):多种图、查询类型、故事;§7 (p.10):"we cover only some of the commonly studied causal queries spanning all three rungs" | 因果推理由三个 Rung、10 种查询、多种图与故事多重操作化,且在局限中说明覆盖范围有限、仅二值变量 |
| A10 | 单一方法的风险 | NA | — | 自变量与因变量并非同一被试自报同源测量,因变量由与 oracle 答案比对自动得出,不存在共同方法偏差情形 |
| B1 | 被试间设计 | NA | — | 无独立被试组被分配到条件;所有模型均评测同一批题目 |
| B2 | 被试内设计 | NA | — | 各模型对各题为无状态独立 API 调用,无需条件顺序安排;不属于顺序敏感的被试内设计 |
| B3 | 混合设计 | NA | — | 无组间/组内混合因素分析 |
| B4 | 因子设计 | 0.5 | Appendix A.4 (p.20):"balanced such that there are roughly the same number of questions for each distinct story-graph-query combination (ranging from 50-100 per combination) across the different variants" | 题目侧因素(故事×图×查询×常识对齐)在生成上近似完全交叉并报告每格题量范围;但结果只报告边际准确率(Table 2),未报告交互项与每格统计量 |
| B5 | 主效应 | 0 | Table 2 (p.8) 仅给出描述性准确率 | 无任何主效应的统计检验(无显著性检验、无 CI) |
| B6 | 交互作用 | 0 | 同上 | 未对交互项(如 方法×Rung、方法×常识对齐)做统计检验,只有分层描述 |
| B7 | 区组设计 | NA | — | 无被试区组;题目按故事-图-查询均衡生成属于刺激集平衡而非区组分析 |
| B8 | 拉丁方 | NA | — | 非被试内顺序设计 |
| B9 | 准实验设计 | NA | — | 模型比较不涉及被试分配问题,不适用准实验框架 |
| B10 | 被试内设计的适用条件 | NA | — | 未使用被试内设计 |
| C1 | 随机化 | NA | — | 无向条件分配被试的环节(各模型均作答全题)。随机性仅出现在题目抽样与 2K 子集抽样(p.9 脚注7:"we occasionally had to evaluate on a subset of 2K random samples"),未报告随机数工具 |
| C2 | 平衡 | NA | — | 无顺序平衡需求(无状态单次调用) |
| C3 | 恒定 | 1 | §5.1 (p.8):"temperature 0"; §3 (p.4):"we focus on graphs with few (three to four) variables"; "use binary variables instead"; Appendix A.4 答案 Yes/No 各 50% | 恒定项及水平明确;§7 (p.10) 讨论了设计简化与现实情境的差距("making the questions and verbalizations even closer to realistic instances") |
| C4 | 匹配 | NA | — | 未使用匹配 |
| C5 | 纳入为变量 | 0.5 | Table 2 (p.8):按 Rung、常识对齐度分层;Fig.3 | 已知影响因素(Rung、常识对齐)作为分层变量测量并报告,但未纳入统计模型,也无协变量分析 |
| C6 | 盲法 | NA | — | 主评测为自动化比对,无需盲法(人工标注仅在小样本质量检查,见 E5) |
| C7 | 平衡的层级 | NA | — | 无顺序平衡 |
| D1 | 练习效应 | NA | — | 无被试内重复试次/学习效应(每次 API 调用无状态) |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳,不适用 |
| D3 | 延滞/迁移效应 | NA | — | 无条件序列;§5.5 ICL 示例为显式前置而非迁移 |
| D4 | 不对称迁移 | NA | — | 同上 |
| D5 | 范围效应 | NA | — | 非被试内量表评分任务 |
| E1 | 位置/顺序偏差 | 0 | Appendix A.5 Table 4 (p.21) Adjust. Set 模板中两选项固定顺序:"should we look directly at how... in general, or this correlation case by case according to..." | 读到了未对选项/刺激顺序做随机化或反平衡,也未讨论顺序偏差 |
| E2 | 默认赞同 | 0.5 | Appendix A.4 (p.20):"we balance the distribution of correct answers so that there are the same number of 'yes's and 'no's"; Table 2 Random 49.27 | 以 Yes/No 各 50% 平衡,功能上相当于正反向题均衡,但未称为默许偏差、未检验模型的 yes 倾向 |
| E3 | 极端/中间反应倾向 | NA | — | 无量表评分 |
| E4 | 需求特征 | NA | — | 被试为 LLM,无需求特征 |
| E5 | 实验者效应 | NR | §3.4 (p.7) 标注者检查;Appendix E.1 (p.25):"we manually annotate the correctness of 100 samples of CAUSALCOT" | 主评测自动化;但人工标注(可读性、步骤正确性)的标注者是否知情、培训与脚本化情况均未交代,缺信息无法判断 |
| E6 | 天花板/地板效应 | 1 | Table 2 (p.8):Random 49.27,多个模型近随机;§3 (p.4) 难度校准依据:"since LLMs struggle with calculation-heavy tasks... we focus on graphs with few (three to four) variables"; §3.4 人类 82% | 报告了主因变量描述统计与随机基线,说明多数模型处于近地板水平、最高约 83%,并说明了任务难度设计 |
| E7 | 共同方法偏差 | NA | — | 同 A10,无同源自报测量 |
| F1 | 统计结论效度 | 0.5 | §1 (p.3):"CAUSALCOT achieves an accuracy of 70.40%, which substantially improves the performance of vanilla GPT-4 by 8.37 points" | 以原始准确率差报告效应大小,但无 CI、无显著性检验、无多重性处理,温度 0 单次运行无方差估计 |
| F2 | 内部效度 | 0.5 | §5.3 (p.8-9) "Isolating the Effect of Data Contamination" | 评估了污染这一威胁(对比 commonsense/anti/nonsense);无被试分配与损耗问题,但对其他威胁(提示在各模型间是否一致、版本差异)讨论不足 |
| F3 | 构念效度 | 0.5 | §3.4 (p.7):"96% of the questions were deemed readable"; perplexity 21.17; 人类专家准确率 82%; §5.4 分步骤诊断 | 提供了数据集质量与效度证据(可读性、语法、人类基线);缺操纵检验与测量信度(如重复运行一致性)证据 |
| F4 | 外部效度 | 1 | §7 (p.10):"we cover only some of the commonly studied causal queries"; Appendix D (p.24-25) 对早期 v1.0 数据集重复主要结果 | 说明了被评模型与数据来源,指出推广边界(仅 3-4 变量二值图),并在 v1.0 与 v1.5 两版数据上复现主要趋势 |
| G1 | 分析单位 | 0.5 | §3 Task Formulation (p.4):"dataset D := {(qi, ai, ei)} ... consists of N triples" | 分析单位为题目级准确率;但题目嵌套于故事/图/查询,聚集结构未处理 |
| G2 | 随机效应 | NA | — | 未建立统计模型,无固定/随机效应结构 |
| G3 | 材料作为随机效应 | 0.5 | §3.2 (p.5):"we collect a set of two to five stories" per graph; §3.3 (p.6):"large enough to be representative" | 题目由生成过程大量抽样且结果对题目取平均,但故事数很少且固定,未作随机效应建模 |
| G4 | 统计功效 | 0.5 | §3.3 (p.6):"we pick a dataset size that is large enough to be representative, and at the same time not too large to be problematic given the expensive inference costs" | 仅有样本量的粗略论证,无事前功效分析、无效应量/CI |
| G5 | 研究者自由度 | 0.5 | p.9 脚注7:"we occasionally had to evaluate on a subset of 2K random samples"; Table 2 报告全部 8 个模型 | 披露了子集抽样与全部评测模型;未说明排除规则,未区分验证性/探索性分析 |
| G6 | 预先设定/预注册 | 0 | 全文未出现预注册 | 读到了没有预注册 |
| J1 | 位置偏差 | 0 | Table 4 (p.21) 选项固定顺序;Yes/No 作答 | 未对候选位置(两选项顺序、Yes/No 顺序)做交换或随机化,也未分析位置偏差;仅均衡答案类别 |
| J2 | 冗长偏差 | NA | — | 未使用 LLM 作裁判评价生成质量(ROSCOE 为自动指标,非 LLM 裁判长度评价) |
| J3 | 谄媚 | NA | — | 无用户立场/反馈对话 |
| J4 | 自我偏好 | NA | — | 无 LLM-as-judge |
| J5 | 少样本示例选择与排列偏差 | 0.5 | §5.5 (p.9):"we look into the effect of in-context learning (ICL) by providing an example solution before asking the question... prepend a reasoning example of query type i" | 仅在附加分析中使用 1-shot,并系统比较不同查询类型示例的效果(Fig.5);未报告示例的具体来源/标签比例,无排列顺序控制;主实验为零样本 |
| J6 | 提示敏感性/脆弱性 | 0.5 | Appendix B.1 (p.22) 完整 CausalCoT 提示;Appendix D.3 (p.25) Table 7 逐步消融 | 提供完整提示并做步骤消融(仅 v1.0);无措辞/格式变体敏感性分析与 dev/test 分离 |
| J7 | 长上下文信息位置效应 | NA | — | 非长上下文/RAG 实验(单题 ~80 词) |
| J8 | 温度与采样随机性 | 0.5 | §5.1 (p.8):"We use the OpenAI API with temperature 0" | 报告了温度;未报告 top-p/种子,也未做重复运行、无 CI;开源模型设置未说明 |
| J9 | 重复与文本退化 | 0.5 | §5.1 (p.8) temperature 0;Appendix E.2 Table 8 (p.26) "Repetition Word 0.02... Repetition Step 0.02" | 解码设置(温度 0)在模型间一致,并报告了 CausalCoT 输出的重复率(ROSCOE);未明确解码算法/开源模型解码细节,未对各条件重复率比较 |
| J10 | 分词效应 | NA | — | 非跨语言/跨脚本实验,不适用 |
| J11 | 测试集污染/数据泄漏 | 0.5 | §5.3 (p.8-9):"We address this problem by creating not only the commonsensical subset of our dataset, but also anti-commonsensical and nonsensical"; Table 2 注明 v1.5 与 gpt-4-1106-preview | 明确识别污染并以反常识/无意义子集间接评估;未给出各模型训练截止日期与数据集发布时间的对照 |
| J12 | 基准饱和 | 0.5 | Table 2 (p.8) 随机基线 49.27 与各模型成绩 | 报告了量程与当前水位且远离天花板,"highly challenging";未显式评估饱和风险或备用连续指标(仅二值准确率) |
| J13 | 指令遵循 | NA | — | 研究目的不是测量指令遵循;终答为 Yes/No 机器比对但不作为指令遵循构念 |
| J14 | 输出格式约束/结构化输出 | 0.5 | Appendix B.1 (p.22):"The diagram should simply consist of edges denoted in 'var1 -> var2' format"; "in the form 'P(...)=...'" | 提示中规定了结构化输出格式,并报告了分步骤正确率(Table 3);但未单独报告格式合法率,格式失败与内容错误未分开 |
| J15 | 越狱稳健性 | NA | — | 非安全/对齐评测 |
| J16 | LLM 作为被试的范式定位 | NA | — | 属能力基准评测,不是以 LLM 为心理学被试检验人类构念迁移(虽有 §1 引言对"人类智能"的类比) |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随规模/训练进展的能力曲线,也未宣称涌现 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无以代理指标为优化目标的训练/优化 |
| J19 | 评估可复现性与种子/检查点依赖 | 0.5 | §5.1 (p.8):"gpt-4-1106-preview"; Table 2 GPT-3.5 与 GPT-4 在 Appendix D 注明 "queried in May 2023" | 部分模型给出具体 snapshot,GPT-3.5 等仅给泛称;无重复次数、无 CI/配对检验;代码与数据开源 |
| J20 | 多轮对话中的一致性衰减 | NA | — | CausalCoT 为单题内多步链式提示,并非多轮对话一致性评估 |

## 编码小结

本篇是 LLM 基准构建+多模型评测研究,A–G 中大量人类被试专属组件(被试内/拉丁方/练习疲劳/盲法/CMB)判 NA。可复现性相关材料(完整提示、模板、代码、数据)较好,A7/A8/A9/C3/F4 记 1;统计推断环节薄弱:无 CI、无显著性检验、无重复运行、无预注册,故 B5/B6/A5/G6 记 0,F1/G4/J8 记 0.5。主要不确定处:B4/C5 将"题目侧分层均衡、仅边际描述"判为 0.5 或 0 存在尺度弹性;E1/J1 以"选项固定顺序、仅均衡答案类别"判 0,而 E2 将 Yes/No 均衡视为功能性替代记 0.5;E5 因人工标注细节缺失记 NR;J11 以反常识/无意义子集作为间接污染评估,因缺训练截止日对照记 0.5。
