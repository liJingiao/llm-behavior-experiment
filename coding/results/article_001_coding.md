# article_001 | Assessing the Creativity of LLMs in Proposing Novel Solutions to Mathematical Problems | 2025 (AAAI-25)

研究类型概述：纯 LLM 基准评测研究（无人类被试）。10 个 LLM 在同一批 AoPS 数学题上，给定 k 个参考解后生成"新颖解"；自变量为模型（10 个）与参考解数 k（1-5），另按竞赛难度分层；因变量为由 3 个 LLM 裁判（GPT-4 / Claude 3.5 Sonnet / Gemini 1.5 Pro）判定的正确率 C、新颖率 N、N/C、Nu、Nu/N。页码为 PDF 页码（对应 AAAI 页码 25687 起）。PDF 未含正文提及的 Appendix。
- **研究构念（Construct）**：数学创造力与新颖问题解决（mathematical creativity）｜CA 构念锚定：创造性思维（creative thinking, `trm_4a3fd79d09f42`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：纯 LLM 基准评测研究（无人类被试）。10 个 LLM 在同一批 AoPS 数学题上，给定 k 个参考解后生成"新颖解"；自变量为模型（10 个）与参考解数 k（1-5），另按竞赛难度分层；因变量为由 3 个 LLM 裁判（GPT-4 / Claude 3.5 Sonnet / Gemini 1.5 Pro）判定的正确率 C、新颖率 N、N/C、Nu、Nu/N。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3 Novel Solution Generation: "a subset of k reference solutions ... is sequentially selected based on the order in which competitors uploaded their solutions"; p.5 "605 distinct samples with k varying from 1 to 5"; 模型列表见 p.5 | 自变量（模型、k）命名清楚、水平可列；缺：单位如何分配到各 k 水平未交代，无操纵检验（k 与题目难度、n-k 混杂） |
| A2 | 因变量 | 0.5 | p.6 Table 1: "C Correctness Ratio: The proportion of solutions that are valid and can solve the problem correctly"; "N Novelty Ratio ... both correct and distinct from the provided k reference solutions" | 指标与计分明确；缺：LLM 裁判的信效度证据（无人工校验、无裁判间一致性），未讨论天花板（k=4 时 Gemini 100%） |
| A3 | 控制变量 | 0.5 | p.5 Implementation Details: "all experiments were conducted using the greedy decoding strategy ... maximum number of new tokens set to 1024"; Dataset: "total token count did not exceed 3K tokens" | 有控制手段（解码、token 上限、统一模板）；缺：无系统的控制变量清单，系统提示按各模型文档而异 |
| A4 | 混淆变量 | 0.5 | p.7 "potentially due to variability introduced by smaller sample sizes at higher k values"; p.8 Table 5 以 k=1 比较各难度 | 识别了 k 与样本量/难度的混淆并部分控制；缺：未系统讨论残余混淆（k 与 n-k、难度、k 越大样本越少 [k=4 仅 8 题]） |
| A5 | 调节变量 | NA | — | 未设调节假设，难度/ n-k 仅作描述性分层，无交互检验 |
| A6 | 中介变量 | NA | — | 无中介假设 |
| A7 | 操作性定义 | 1 | p.3 五条新颖性标准（"Methodological Differences... Intermediate Step Variation..."）；p.4-5 Fig.4/Fig.5 给出生成与判定 prompt；p.4 粗/细粒度新颖性流程 | 新颖性、正确性均有可复现程序（含 prompt 与判定流程图） |
| A8 | 水平数与类型 | 0.5 | p.5 列出 10 个模型；p.7 Table 3 "Sample sizes for k = 1 to k = 4 are 400, 154, 42, and 8" | 水平标签基本齐全；缺：k 正文称 1-5 而表仅到 4，部分模型无版本（如 Gemini-1.5-Pro、Qwen、Llama）；水平类型/间距未说明 |
| A9 | 单一操作化的风险 | 0 | p.3 / p.6 创造力仅以"正确且与参考解不同"操作化 | 创造力只有一种操作化（LLM 判新颖），多个指标源于同一判定；局限部分无泛化限制讨论（未设局限节） |
| A10 | 单一方法的风险 | NA | — | 非人类问卷同源测量情形，IV 为操纵的模型/k |
| B1 | 被试间设计 | NA | — | 无被试分配；各模型在同一题集上评测，非被试分配设计 |
| B2 | 被试内设计 | NA | — | 无人类被试；LLM API 调用无状态，不涉及条件顺序 |
| B3 | 混合设计 | NA | — | 非混合实验设计 |
| B4 | 因子设计 | NA | — | 模型×k 虽交叉列表（Table 3）但无因子设计分析与交互检验 |
| B5 | 主效应 | NA | — | 无推断统计，仅描述性比较 |
| B6 | 交互作用 | NA | — | 同上 |
| B7 | 区组设计 | NA | — | 未使用区组 |
| B8 | 拉丁方 | NA | — | 非被试内顺序设计 |
| B9 | 准实验设计 | NA | — | 非被试分配研究 |
| B10 | 被试内设计的适用条件 | NA | — | 非被试内设计 |
| C1 | 随机化 | NA | p.5: "For each competition, 50 samples were randomly chosen" | 无条件分配（所有模型接受相同样本），仅有题目随机抽样（见 F4/G5），且未报告随机工具/种子 |
| C2 | 平衡 | NA | — | 无顺序平衡需求（但参考解顺序见 E1） |
| C3 | 恒定 | 0.5 | p.5 "greedy decoding ... maximum number of new tokens set to 1024"；"total token count did not exceed 3K tokens" | 列出了恒定的解码与长度设置；缺：对外部效度的限制讨论 |
| C4 | 匹配 | NA | — | 未使用匹配 |
| C5 | 纳入为变量 | 0.5 | p.8 Table 5 按竞赛难度分层并固定 k=1；p.7 按 k、n-k 分层 | 以分层方式纳入难度/ k；缺：无模型化分析，无协变量检验 |
| C6 | 盲法 | 0.5 | p.3: "transition sentences and justifications explaining why the new solution is distinct from the reference solutions are manually removed. Only the newly generated solution is presented for evaluation" | 对裁判隐去生成方的自我论证；缺：未说明是否隐藏生成模型身份，无盲法成功检验 |
| C7 | 平衡的层级 | NA | — | 原编码文件漏列 C7；该研究为无顺序平衡需求的纯 LLM 基准评测，故补记 NA。 |
| D1 | 练习效应 | NA | — | 非被试内，无试次序列 |
| D2 | 疲劳效应 | NA | — | 同上 |
| D3 | 延滞 / 迁移效应 | NA | — | 同上（单次独立调用） |
| D4 | 不对称迁移 | NA | — | 同上 |
| D5 | 范围效应 | NA | — | 无被试内量表评分 |
| E1 | 位置 / 顺序偏差 | 0 | p.3: 参考解 "sequentially selected based on the order in which competitors uploaded" | 参考解在 prompt 中按上传顺序固定，未随机化或反平衡，也未讨论顺序对生成/判定的影响 |
| E2 | 默认赞同 | NA | — | 无量表；YES/NO 判定偏差见 J 节 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无评分量表 |
| E4 | 需求特征 | NA | — | 无人类被试 |
| E5 | 实验者效应 | 0.5 | p.3 删除裁判看到的论证句；p.4 "three leading LLMs ... as LLM Evaluators" 并行评估 | 评分者为 LLM，评分流程脚本化；缺：未明确盲法层级与是否隐藏模型身份 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Table 3 "Gemini-1.5-Pro ... 100" (k=4)；p.6 "reaches 100% correctness at k = 4" | 报告了主要 DV 的比率；缺：未讨论天花板（k=4 仅 n=8）、无分布信息、难度校准仅按竞赛难度分层 |
| E7 | 共同方法偏差 | NA | — | 非问卷自陈同源测量情形 |
| F1 | 统计结论效度 | 0 | p.7 Table 2 仅给百分比 | 无置信区间、无显著性检验、无效应量、无样本量依据、无多重比较处理；模型间"优劣"结论无推断统计支撑 |
| F2 | 内部效度 | 0.5 | p.5 各模型使用同一批 605 个样本；p.7 讨论小样本变异 | 有统一样本与部分威胁评估；缺：k 与 n-k/难度的混淆未系统评估，裁判偏差未评估 |
| F3 | 构念效度 | 0.5 | p.3 "criteria agreed upon in consultation with several mathematicians"；p.1 引用 Runco & Jaeger 创造力定义 | 有一定效度依据；缺：LLM 裁判与人类裁判一致性、裁判间信度均无，无操纵检验 |
| F4 | 外部效度 | 0.5 | p.2 数据来自 AoPS 八项美国竞赛；p.5 "50 samples were randomly chosen" ，"400 math problems and 605 solutions" | 报告样本来源与抽样；缺：推广边界（仅英文竞赛题、≤3K token、单一语料）未讨论 |
| G1 | 分析单位 | 0.5 | p.5 "605 distinct samples with k varying from 1 to 5"；p.7 Table 3 样本量 | 以样本（题×k）为单位汇总；缺：同一题目产生多个 k 样本的嵌套结构未处理 |
| G2 | 随机效应 | NA | — | 未使用统计模型，无固定/随机效应结构 |
| G3 | 材料作为随机效应 | 0.5 | p.5 "50 samples were randomly chosen" | 题目为随机抽样；缺：分析中未将题目作随机效应或报告题间变异 |
| G4 | 统计功效 | 0 | p.1–11 全文实验设计与结果部分均未报告事前功效分析、目标功效或样本量/重复次数推导依据 | 全文无功效分析或样本量论证（k=4 仅 8 题） |
| G5 | 研究者自由度 | 0.5 | p.2 Data Cleaning: "Samples with images, problems without solutions, or incomplete entries were manually removed"；p.5 token ≤3K 筛选 | 报告了数据剔除规则；缺：prompt 迭代情况、验证性/探索性区分、样本量决定方式未说明 |
| G6 | 预先设定 / 预注册 | 0 | p.1–11 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未提及预注册 |
| J1 | 位置偏差 | 0 | p.3 参考解按上传顺序呈现；p.4 YES/NO 判定 | LLM 作裁判且参考解/新解位置固定，未做交换或随机化，未讨论 |
| J2 | 冗长偏差 | 0 | p.4-5 裁判评估生成解 | LLM 判新颖/正确，未识别或控制解长度对判定的影响（生成上限 1024 tokens 仅是截断设置） |
| J3 | 谄媚 | NA | — | 单轮生成与判定，无用户立场/反馈操纵 |
| J4 | 自我偏好 | 0 | p.4 裁判为 "GPT-4, Claude 3.5 Sonnet, and Gemini 1.5 Pro"；p.5 被评含 GPT-4o、Claude-3-Opus、Gemini-1.5-Pro | 裁判与被评模型同家族重叠（且 Gemini-1.5-Pro 为最优），文中未说明或控制自我偏好 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.3 "a subset of k reference solutions ... sequentially selected based on the order in which competitors uploaded"；p.7 Table 3 | 报告了示例来源、数量（k）；缺：选择/排列方式固定，未做排列敏感性，标签比例不适用 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4 Fig.4 生成 prompt 模板；p.5 Fig.5 判定 prompt 模板 | 提供了模板（Fig.5 新颖性标准以"..."省略）；缺：无措辞敏感性消融、无 dev/test 分离 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 输入不超过 3K tokens，非长上下文/RAG |
| J8 | 温度与采样随机性 | 0.5 | p.5 "all experiments were conducted using the greedy decoding strategy" | 报告了贪心解码；缺：重复运行次数、种子、裁判模型解码设置，无多次采样与 CI |
| J9 | 重复与文本退化 | 0.5 | p.5 "greedy decoding ... maximum number of new tokens set to 1024" | 解码策略已报告且各模型一致；缺：重复率/退化记录，未讨论 1024 token 截断对长解的影响 |
| J10 | 分词效应 | NA | — | 非跨语言/多格式输入实验 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.2 数据来自公开 AoPS；p.5 给模型版本 | 公开竞赛题极可能进入预训练，全文未评估或讨论污染，也未对照训练截止日期 |
| J12 | 基准饱和 | 0.5 | p.7 Table 2 同列出 MATH 准确率；p.6 "Gemini-1.5-Pro reaches 100% correctness at k = 4" | 报告了指标量程与当前水平；缺：未评估饱和/天花板并采取连续指标或更难子集 |
| J13 | 指令遵循 | NA | — | 非以指令遵循为测量对象 |
| J14 | 输出格式约束 / 结构化输出 | 0 | p.4 "responses of 'YES' indicating correctness and 'NO' indicating otherwise" | 裁判输出限定为 YES/NO，但未报告格式合法率或解析失败率 |
| J15 | 越狱稳健性 | NA | — | 非安全/对齐评测 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 "The standard definition of creativity ... (Runco and Jaeger 2012), emphasizes two essential criteria: novelty and usefulness"；p.2 "the applicability of these traditional creativity metrics to AI systems is still a topic of debate" | 界定了 LLM 上的创造力构念并提及与人类度量的差异；缺：未论证"相对已知人类解的新颖性"与人类数学创造力的异同 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无涌现/突变宣称（仅引用 scaling laws 作解释） |
| J18 | 指标博弈与奖励过优化 | NA | — | 无以代理指标为目标的优化 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 "GPT-4o (Version 2024-05-13)", "Claude-3-Opus (Version 2024-02-29)"；p.1 代码链接 | 部分模型给了 snapshot；缺：Gemini 等无版本、裁判版本不详、无重复次数、无 CI/配对检验 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 单轮生成与评估 |

## 编码小结
本篇为纯 LLM 基准评测：10 个模型在同一题集上的比较，核心设计变量为模型和参考解数 k，因此人类被试类的 B、D 节与多数质控项记 NA。变量定义与操作化（A7）做得最好（五条新颖性标准与完整 prompt 模板），但因变量由 3 个 LLM 裁判判定，既无人工校验/裁判间信度，又存在裁判与被评模型同家族重叠（J4）、位置与长度偏差未控制（J1/J2），且无任何推断统计、功效、预注册与污染讨论（F1、G4、G6、J11 记 0）。不确定处：B 节是否应视为"模型间 + k 内"混合设计（本篇无明确表述，故保守记 NA）；G2/C1 因无统计模型和条件分配而 NA；A9 在"多裁判/多指标"是否算多操作化上有判断空间（本篇认定为同源于同一判定，记 0）。PDF 缺少正文提到的 Appendix，Fig.5 中 prompt 以"..."省略，J6 等据此保守判断。
