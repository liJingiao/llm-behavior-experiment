# article_018 | FEEDBACK FRICTION: LLMs Struggle to Fully Incorporate External Feedback | 2025

研究类型概述：LLM 行为/能力评测研究：在受控迭代反馈框架中，让 solver LLM 对数学、知识、科学和多领域基准作答，由 F1 二值正确性反馈、F2 自生成反思反馈或 F3 强模型反思反馈生成反馈，最多迭代 10 轮；比较多个模型与任务，并分析错误类别、采样干预、置信度与数据熟悉度等。分析单位为问题/轨迹及模型×任务×反馈条件，不是人类被试。
- **研究构念（Construct）**：外部反馈采纳与纠错摩擦（feedback incorporation and correction resistance）｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：LLM 行为/能力评测研究：在受控迭代反馈框架中，让 solver LLM 对数学、知识、科学和多领域基准作答，由 F1 二值正确性反馈、F2 自生成反思反馈或 F3 强模型反思反馈生成反馈，最多迭代 10 轮；比较多个模型与任务，并分析错误类别、采样干预、置信度与数据熟悉度等。分析单位为问题/轨迹及模型×任务×反馈条件，不是人类被试。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4 定义 F1binary、F2self、F3strong 三种反馈机制及各自 prompt/公式；p.5 报告 Llama 温度 0、Claude 3.7 温度 0、Claude 3.7 Thinking 温度 1，F3 使用 GPT-4.1 mini；p.8 报告温度递增 0.0/0.15/0.3…。未见操纵检验或明确的单位随机分配。 | 自变量（反馈机制/采样策略）及水平明确，操纵程序大体可复现，但分配方式和操纵检验缺失，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.5：'objective tasks with clear ground-truth answers'，并使用 'same prompts, few-shot demonstrations, answer parsing mechanism, and metrics from lm-evaluation-harness'；p.15：PopQA 使用 LLM-as-a-judge 判定答案正确性。未报告测量信效度或连续指标预处理。 | 因变量指标与计分方式明确，但信效度证据、天花板/地板预处理等缺失，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.4：'same prompts, few-shot demonstrations, answer parsing mechanism, and metrics'；p.5：Llama 使用 vLLM、temperature 0，Claude 经 Anthropic API，单台 H100；p.17：反馈中答案 masking。未形成系统控制变量清单并逐一说明控制手段。 | 报告了若干控制手段，但不系统，且未覆盖所有潜在额外变量，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.4：合成乘法任务用于 'remove potential confounding variables from semantic context'；p.9-10：检验并排除 model confidence、data familiarity、reasoning complexity 等解释；p.10 承认缺乏机制性解释。 | 识别并控制了若干潜在混淆且做了探索，但未系统报告残余混淆或敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 理论模型未提出正式调节假设；模型、任务、反馈类型只是分组比较，未做乘积项交互检验、中心化或简单斜率分析，故不适用。 |
| A6 | 中介变量 | NA | — | 未界定或检验中介变量，也无直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | p.3：pk+1(xi)=concat(xi, historyk)，historyk 含此前所有 answer-feedback 对；p.4：F1/F2/F3 的操作化公式与 prompt；p.4-5：九个任务及 exact/metric 评分；p.17：masking 规则。 | 关键构念（反馈条件、迭代过程、正确率、错误类别）均有可观测、可重复执行的操作化描述。 |
| A8 | 水平数与类型 | 0.5 | p.4：F1/F2/F3 三种反馈水平；p.8：温度递增为 0.0、0.15、0.3…；p.5：五个 solver 模型。明确水平数与标签，但未系统说明水平类型、间距/全距或连续变量的中心化。 | 基本水平信息完整，但缺水平类型及连续变量处理说明，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.7：'manually examine cases... identifies three main categories'，并用 o4-mini 自动分类，Table 1 报告 FR/FQ/OTH；p.1 图 1 底部报告未解决问题类别分布。 | 对反馈抵抗使用了正确率与错误分类等多种指标，但未正式报告各操作化之间的会聚证据或单一操作局限，故为 0.5。 |
| A10 | 单一方法的风险 | NA | — | 主要自变量是实验操纵的反馈机制，因变量为基准答案正确率/错误分类，不是同源自陈量表；PopQA 的 LLM 判分是评估工具，不是 CMB 意义上的同源测量，故不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或被试组的随机条件分配；solver 模型版本是固定比较对象，同一基准问题在条件中被重复评估，不符合被试间设计，故不适用。 |
| B2 | 被试内设计 | 0.5 | p.3：'For iteration k ≥ 1... historyk contains all previous answers and feedback pairs... repeats for up to k = 10 iterations'；p.8：采样干预按迭代改变温度。 | 存在同一问题轨迹上的重复迭代测量，但迭代顺序固定且未报告顺序平衡方案；作为 LLM 重复测量仅部分满足。 |
| B3 | 混合设计 | NA | — | 未将各因素明确标注为组间/组内，也未采用混合模型或分别报告组间/组内误差项；模型、任务、反馈为固定比较网格，故不适用。 |
| B4 | 因子设计 | 0 | p.6 Figure 4 比较不同反馈机制，p.5 列出多模型与多任务；但 Claude 未完整跑 F1/F2/F3，未给完整设计矩阵、每格样本量，也无 ANOVA 主效应/交互统计。 | 多因素比较网格未完全交叉且未报告交互项，未达到因子设计基本要件，故为 0。 |
| B5 | 主效应 | 0 | p.6：'Strong-Model Reflective Feedback (F3) outperforms binary feedback by significant margins... improvements of +26.7% and +10.6%'，但未报告 F、df、p、效应量或正式主效应检验。 | 有描述性主效应比较，但缺统计检验和效应量，故为 0。 |
| B6 | 交互作用 | 0 | p.6 与 Figure 4 仅按模型和任务展示反馈机制差异；全文未见交互项统计检验、简单主效应或多重比较校正。 | 未报告交互项检验，故为 0。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机分配，故不适用。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方平衡条件顺序，故不适用。 |
| B9 | 准实验设计 | NA | — | 研究不是准实验设计，不存在因无法随机分配而产生的选择偏差论证问题，故不适用。 |
| B10 | 被试内设计的适用条件 | 0 | p.3：反馈迭代固定按 k=1…10 顺序进行，history 累积此前全部答反馈；全文未论证处理可逆性或迁移对称性。 | 迭代反馈本质上依赖历史且顺序不可交换，但论文未讨论被试内/重复处理适用条件，故为 0。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥条件；同一基准问题在各反馈条件下重复评估，且无随机化/分配隐藏程序，故不适用。 |
| C2 | 平衡 | NA | — | 没有可采用完全/拉丁方/ABBA 平衡的条件顺序设计；迭代顺序由反馈历史决定，故不适用。 |
| C3 | 恒定 | 0.5 | p.4：'same prompts, few-shot demonstrations, answer parsing mechanism, and metrics'；p.5：Llama 使用 vLLM、temperature 0，Claude API，单台 H100；p.17：masking。未讨论这些恒定设置对外部效度的限制。 | 列出了若干恒定设置，但未系统化并讨论外部效度限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配程序，故不适用。 |
| C5 | 纳入为变量 | 0.5 | p.9：检验 initial confidence 与 accuracy/improvement 的关系；p.9-10：用 PopQA popularity 指标分析 data familiarity；但这些是探索性分组分析，未作为主模型协变量或区组因素。 | 已知潜在混淆被测量并分析，但未检验协变量斜率齐性或报告调整后效应量，故为 0.5。 |
| C6 | 盲法 | NA | — | 主要数据采集与评分自动化，无人类被试/主试盲法设计；人类标注仅用于验证错误分类，且未作为实验条件盲法处理，故不适用。 |
| C7 | 平衡的层级 | NA | — | 未选择完全平衡/拉丁方/ABBA 等顺序平衡层级，故不适用。 |
| D1 | 练习效应 | 0 | p.3：同一问题最多迭代 10 轮，且每轮 history 包含此前所有回答与反馈；未设置无反馈的重复尝试基线或练习/重复效应控制。 | 重复反馈带来的历史/练习效应未被独立控制，可能混淆反馈整合增益，故为 0。 |
| D2 | 疲劳效应 | NA | — | LLM 推理不受人类疲劳效应影响，且实验不是人类长 session 设计，故不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同反馈机制在独立运行中比较，不存在人类交叉设计所需的跨条件清洗期；迭代历史是处理的一部分而非跨条件残留，故不适用。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移/不对称迁移问题，故不适用。 |
| D5 | 范围效应 | NA | — | 不使用主观 Likert/绝对量值评定量表，无范围效应问题，故不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p.4：'MMLU and MMLU Pro... multiple-choice format raises concerns... models... remain anchored to their initial selections'；p.15：多选按 A-D/A-J 标签格式化。未对选项顺序随机化或反平衡。 | 多选题选项位置固定，未做顺序控制且未讨论位置效应控制，故为 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，故不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较，故不适用。 |
| E4 | 需求特征 | NA | — | LLM 实验不存在人类被试可推断研究假设并配合的需求特征问题，故不适用。 |
| E5 | 实验者效应 | NA | — | 主要数据采集完全自动化，无人类主试/评分者参与主要评估，故不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6：'In the standard 5-Digit Multiplication task, both Claude models reach near-perfect accuracy'；Figure 3 多任务准确率曲线显示部分任务接近上限；但未报告 SD、偏度、端点频率或 pilot 难度校准。 | 报告了准确率曲线并识别部分接近上限/下限，但缺少完整分布和任务难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 自变量为实验操纵的反馈机制，因变量为客观答案正确率，不是同源自陈式多构念测量，故不适用。 |
| F1 | 统计结论效度 | 0.5 | p.8-9：'we provide error bars... standard error of a binomial proportion'；p.5 报告任务与评测指标；但无样本量功效依据、主分数 95%CI、多重性校正，且多数比较为描述性。 | 报告了部分误差指标和效应方向，但统计推断完整性与多重校正不足，故为 0.5。 |
| F2 | 内部效度 | 0.5 | p.4-5：受控的环境、统一 prompt、温度与评测流程；p.9-10：对 confidence、familiarity、complexity 等内部效度威胁做探索；但无随机分配、分配隐藏、基线等价性检验或被试流向/损耗处理。 | 有内部效度威胁的评估与控制，但缺少正式分配程序与基线等价报告，故为 0.5。 |
| F3 | 构念效度 | 0.5 | p.7：自动错误分类与人工验证，'96% agreement between human annotators and o4-mini'；p.5：使用 lm-evaluation-harness 指标。未报告反馈机制操纵检验或正确率测量的信效度。 | 有错误分类评分者一致性证据，但缺关键测量的信效度、反馈操纵检验和多操作化讨论，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.5：列出 5 个 solver 模型和 9 个任务；p.4：部分数据集只取 10% 样本；p.10 局限主要讨论机制与缓解策略，未系统界定模型/任务/情境推广边界。 | 报告了模型和任务来源，但未论证代表性或跨样本/跨情境复现，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p.3：准确率按 m 个问题聚合，Acc_k = (1/m)Σ1[f(ak(xi),yi)=1]；p.5：按模型和数据集运行；p.7：按数据集/模型报告错误类别。未说明问题嵌套于数据集及迭代重复的分析层级处理。 | 说明了分析落在问题/条件层面，但未显式处理问题嵌套和迭代重复依赖，故为 0.5。 |
| G2 | 随机效应 | 0 | p.3 仅给出按问题聚合的准确率公式；p.5 列模型；全文无混合模型、随机截距/随机斜率或随机效应结构说明。 | 模型、任务、问题被当作固定比较对象，未报告随机效应结构，故为 0。 |
| G3 | 材料作为随机效应 | 0 | p.4：使用固定基准题目与 10% 抽样；p.5：任务指标来自固定数据集；未将题目/材料作为从更大材料总体抽样的随机因子。 | 未使用材料/项目随机效应或 F′/min F′，结论可推广到任意题目的推断不足，故为 0。 |
| G4 | 统计功效 | 0 | p.4：'we sample 10% of the total data points... preliminary experiments confirmed that this subset yields performance metrics nearly identical'；全文无事前功效分析、目标效应量来源或主分数置信区间。 | 无设计阶段功效分析或系统样本量论证，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p.4：说明 MMLU/MMLU Pro/PopQA/TriviaQA 抽样 10%；p.5：列模型；p.9-10：多种探索性分析。未完整报告全部测量因变量、停止规则及验证性/探索性分析区分。 | 部分报告了抽样与主要分析，但研究者自由度披露不完整，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未见预注册平台、注册编号或数据收集前分析计划；p.4 的抽样与 p.9-10 的分析均为事后描述。 | 无预注册，按判定记 0。 |
| J1 | 位置偏差 | 0 | p.4：'MMLU and MMLU Pro... multiple-choice format raises concerns... models... often remain anchored to their initial selections'；p.15 多选按 A-D/A-J 标签格式化。未报告选项位置随机化、A/B 交换重判或偏好翻转率。 | 识别了多选选择黏着/位置风险，但没有位置反平衡或翻转率控制，故为 0。 |
| J2 | 冗长偏差 | NA | — | 主要指标为客观答案正确率和错误类别；未以 LLM 裁判对开放生成质量按长度/篇幅打分，故不适用。 |
| J3 | 谄媚 | NA | — | 研究不操纵用户先验立场，也不涉及对话式用户反馈导致的谄媚；研究的是外部反馈整合，故不适用。 |
| J4 | 自我偏好 | 0.5 | p.7：'we used OpenAI o4-mini as an automated annotator'，并报告 '96% agreement between human annotators and o4-mini'，对比 GPT-4.1 mini 的 78%；p.15：PopQA 使用 LLM-as-a-judge。未报告裁判匿名化、同源自我偏好量化或各裁判单独结果。 | 报告了裁判模型与人工一致性，但自我偏好风险控制不完整，故为 0.5。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.15：'We employ few-shot prompting across all tasks... For TriviaQA and PopQA, we randomly sample 5 questions without replacement... For MMLU and MMLU Pro... sample 5 questions from the corresponding question category'。未报告每类标签比例、多 seed 重采样或示例顺序反平衡。 | 报告了 few-shot 来源与数量，但缺标签比例/顺序/多 seed 稳健性，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.15-17：Figure 8-10 给出 solver、反馈生成和 masking 的 prompt 模板；但未给 prompt 版本号、迭代日期、敏感性消融或 dev/test 划分。 | 已公布主要 prompt 模板，但无版本管理和敏感性分析，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不是长上下文/RAG 实验，虽包含迭代历史，但未操纵关键信息首/中/尾位置或报告位置×正确率曲线，故不适用。 |
| J8 | 温度与采样随机性 | 0.5 | p.5：Llama 与 Claude 3.7 使用 temperature 0，Claude 3.7 Thinking 使用 temperature 1；p.8：温度递增策略 0.0、0.15、0.3…。未报告 top-p/top-k、seed、重复采样次数与主分数置信区间。 | 报告了主要温度设置但采样随机性控制不完整，故为 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.5：使用 vLLM、temperature 0，Claude API；p.8：'increased temperature successfully diversified model outputs'。未报告 repetition penalty、n-gram 重复率/退化率或条件间解码策略恒定性。 | 报告了解码温度但未做重复/退化质控，故为 0.5。 |
| J10 | 分词效应 | NA | — | 研究为单语言/单脚本？题目均为英文基准，无跨语言或跨脚本比较，故不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4：使用 AIME 2024、MATH-500、TriviaQA、PopQA、MMLU、MMLU Pro、GPQA 等公开基准；p.5：给出模型名称但未报告训练截止日期，也未做 n-gram/DCQ 污染检测。 | 未识别或评估预训练/微调数据与测试基准污染，故为 0。 |
| J12 | 基准饱和 | 0.5 | p.6：'In the standard 5-Digit Multiplication task, both Claude models reach near-perfect accuracy'；Figure 3 中 MMLU 等任务准确率约 95%。未报告当前 SOTA 位置、连续指标或 bootstrap CI 比较。 | 报告了部分接近饱和的分数并仍作比较，但未系统处理饱和问题，故为 0.5。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；答案格式仅用于解析正确性，故不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.15：要求数学答案用 \\boxed{}、多选以 'The answer is (X)' 输出，并使用 lm-evaluation-harness 的 answer parsing；未报告格式合法率、重试策略或将格式失败与内容错误分开。 | 报告了格式约束与解析方式，但缺格式合法率和失败分类，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估，无有害请求或对抗攻击设置，故不适用。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究是 LLM 能力/基准评估，测量反馈整合能力而非把 LLM 当作人类心理学被试并论证同名构念迁移，故不适用。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随模型规模/训练进展的能力曲线或涌现能力宣称，故不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不针对代理指标进行训练/RL/best-of-N 优化，也无 overoptimization 双曲线设置，故不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 给出模型名称与版本（Llama-3.3、Llama-4、Claude 3.7 等）；p.2 脚注给出代码链接；p.9 部分分析报告二项标准误。未给精确 API snapshot/日期、每个主分数重复次数与 95%CI、配对检验或原始推理日志。 | 有部分版本与误差信息及代码发布，但评估可复现性关键项不完整，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.3：最多 10 轮，每轮把全部历史 answer-feedback 对加入 prompt；准确率按迭代 k 报告并说明因保留正确答而单调不降。未说明上下文截断规则或单轮/多轮部署差异。 | 确实做了多轮迭代评估并按轮次报告，但缺上下文截断和轮次依赖的控制说明，故为 0.5。 |

## 编码小结
论文的迭代反馈协议、反馈机制和答案遮蔽描述较清楚，主要因变量为基准正确率与错误分类。其设计更接近 LLM 基准/行为评测而非人类被试实验，因此许多人类分配、顺序平衡、需求特征和实验者效应组件不适用。LLM 评测相关组件存在部分报告不足：无预注册、无功效分析、无正式随机分配/顺序平衡，主分数缺少系统置信区间与精确 snapshot，未评估基准污染；LLM-as-judge 与 few-shot/prompt 细节部分报告但无敏感性分析。总体证据支持其核心现象，但推断和可复现性报告只能算部分完整。
