# article_003 | CogBench: a large language model walks into a psychology lab | 2024 (ICML, PMLR 235)

研究类型概述：LLM 作为"被试"的认知心理学基准研究（无新增人类被试，人类参照数据取自既有研究）。40 个 LLM 完成 7 个文本化认知实验（概率推理、Horizon、restless bandit、工具性学习、两步任务、时间折扣、BART），得到 10 项行为指标和 6 项表现指标；自变量包括模型特征（参数量、RLHF、开源、数据量、上下文长度、对话/代码微调；观察性）与提示技术（基线 / CoT / take-a-step-back，5 个模型内操纵）；用多层回归检验 5 个假设。页码为 PDF 页码（含附录至 p.33）。

注：CSV 实际含 69 个组件，而非 70 个。

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.8 "We evaluated five specific LLMs ... applying CoT and SB techniques and comparing the outcomes with their base models"；p.8 给出 CoT 与 SB 的提示文本；p.14 App.A 表列出 LLM 特征 | 提示技术（3 水平）与模型特征（观察性）均命名清楚，prompt 完整；缺：无操纵检验（App.F 承认 "some LLMs do not consistently adhere to this constraint"），LLM 特征为非操纵变量，单位分配（为何仅 5 个模型）仅粗略说明 |
| A2 | 因变量 | 1 | p.5 Fig.2 "All metrics are human-normalized: a value of zero corresponds to a random agent, while a value of one corresponds to the average human subject ... Errors bars represent 95% confidence intervals"；App.B 各指标公式（如 QSR、Rescorla-Wagner 学习率） | 10 项行为 + 6 项表现指标均有定义、计分与归一化；App.D 稳健性、App.E 冗余分析提供信效度相关证据 |
| A3 | 控制变量 | 0.5 | p.3 "We set the temperature parameter to zero, leading to deterministic responses, and retained the default values for all other parameters"；"rely entirely on the LLMs' in-context learning abilities and do not involve any form of fine-tuning" | 有控制手段（温度、无微调、统一任务设置）；缺：未系统列出被恒定的变量，"其余默认参数"含糊，各 LLM 上下文限制导致的任务缩减（试次数）未逐一说明 |
| A4 | 混淆变量 | 1 | p.6 "The multi-level regression approach was chosen because some models are fine-tuned versions of other models"；p.7 "larger models also tend to be trained on larger datasets"；p.9 "the limited transparency of certain proprietary models poses an issue to our regression analysis" | 识别了特征间共线/家族嵌套的混淆，用同时纳入多特征与家族分层控制，并如实报告残余混淆（透明度不足）；无专门敏感性分析 |
| A5 | 调节变量 | NA | p.6 Level-2 模型含群组预测 Z_j | 无调节假设，Level-2 交叉水平交互仅在方程中给出，结果未报告 |
| A6 | 中介变量 | NA | — | 无中介分析 |
| A7 | 操作性定义 | 1 | App.B 各任务 "SUMMARY / METHODS / PROMPTS FOR LLMS / METRICS"，如 p.20 QSR "= 1 − (accuracy − scaled confidence)^2" | 每个构念都有可复现的任务程序、完整 prompt 与指标计算 |
| A8 | 水平数与类型 | 0.5 | p.14 App.A 表（No. of Parameters、Use of RLHF、Open Source 等）；p.8 CoT/SB/基线三水平 | 水平与类型基本明确；缺：专有模型参数量/数据量为估计值（App.A "best available knowledge"）却在表中以确定数值呈现，类型/间距未单独说明 |
| A9 | 单一操作化的风险 | 1 | p.9 "evaluations of LLMs on psychological tasks have to be taken with some caution, as these tasks and the corresponding constructs have not been designed for artificial agents"；App.D 提示变体（任务换故事背景） | 部分构念用任务变体做多操作化检验，且在讨论中说明构念单一任务测量/向 LLM 迁移的限制 |
| A10 | 单一方法的风险 | NA | — | 非同源自陈测量；DV 为 LLM 行为，IV 为模型元数据或提示 |
| B1 | 被试间设计 | NA | — | 模型特征为既有模型的属性，无被试分配 |
| B2 | 被试内设计 | NA | p.8 CoT/SB 与基线比较 | 同一模型多条件为独立无状态调用，文中未作被试内设计声明，不涉及顺序 |
| B3 | 混合设计 | NA | — | 未被表述为混合设计 |
| B4 | 因子设计 | NA | — | 无因子设计 |
| B5 | 主效应 | NA | — | 无因子主效应检验 |
| B6 | 交互作用 | NA | — | 无交互检验 |
| B7 | 区组设计 | NA | — | 未使用区组 |
| B8 | 拉丁方 | NA | — | 非顺序设计 |
| B9 | 准实验设计 | 0.5 | p.6 "We can isolate the effects of specific features or modifications by comparing models within the same higher-level group"；p.7 "Hypothesis is refuted" | 模型特征（RLHF、开源等）为非随机的既有属性，属观察性比较；缺：未明确声明非随机分配与选择偏差来源，仍使用因果性措辞 |
| B10 | 被试内设计的适用条件 | NA | — | 非被试内设计 |
| C1 | 随机化 | 0.5 | App.B.4.2 "Here we randomly sample (without replacement) two letters for each to avoid biases towards a given letter"；App.B.7.2 "We randomly shuffle the assignment to A, B, and C" | 任务刺激标签的随机化有报告；缺：随机工具/种子，且无条件分配随机化（模型特征为既有属性） |
| C2 | 平衡 | NA | — | 无条件顺序平衡需求 |
| C3 | 恒定 | 1 | p.3 温度为 0、其余参数默认、无微调；App.B.1.2 "We matched the probabilities used in (Dasgupta et al., 2020)"；p.9 "while cognitive science studies have demonstrated the external validity of the investigated tasks, it is yet to be shown for LLMs" | 列出恒定的采样设置与任务参数，并讨论外部效度限制 |
| C4 | 匹配 | NA | — | 未使用匹配 |
| C5 | 纳入为变量 | 0.5 | p.6 多层回归 "we use the features of LLMs to predict specific behavioral metrics"；App.G 代码 mixedlm(...) | 同时纳入多种 LLM 特征并按家族分层；缺：未检验共线性/模型假设，未报告模型诊断 |
| C6 | 盲法 | NA | — | 无人类被试或评分者，指标自动计算 |
| C7 | 平衡的层级 | NA | — | 无平衡设计 |
| D1 | 练习效应 | NA | p.1 "learning is induced via prompt-chaining" (Fig.1 caption) | 任务内学习是被测构念而非需控制的练习效应；仅在概率推理中与人类首试比较（App.B.1.2） |
| D2 | 疲劳效应 | NA | App.B.3.2 "The decision to limit the number of trials was made due to context size restrictions for some LLMs" | LLM 无疲劳；试次数因上下文限制缩减，属上下文长度问题（见 J7） |
| D3 | 延滞/迁移效应 | NA | — | 各次模拟为独立调用 |
| D4 | 不对称迁移 | NA | — | 同上 |
| D5 | 范围效应 | NA | — | 无被试内绝对量表评分的跨条件范围问题 |
| E1 | 位置/顺序偏差 | 0.5 | App.B.7.2 "We randomly shuffle the assignment to A, B, and C to avoid biases of LLMs towards certain letters"；App.B.4.2 随机抽字母 | 对标签字母做了随机化；缺：响应选项位置（如 Option 1/Option 2、Machine 顺序）未系统反平衡，BART 示例中选项编码在不同版本不一致（"Option 1 for 'skip' or 0 for 'inflate'" 与 V2 "Option 2"） |
| E2 | 默认赞同 | NA | — | 无同意度量表 |
| E3 | 极端/中间反应倾向 | 0 | App.B.3.4 scaled confidence = (confidence − lowest)/(highest − lowest)；p.5 "models are positioned at extreme ends of the risk-taking spectrum" | 唯一量表为 restless bandit 置信度（0-1），未报告其分布形态；仅用极差缩放校正反应范围，属于完整性项而非分布报告，基本要件未达成 |
| E4 | 需求特征 | NA | — | 无人类被试 |
| E5 | 实验者效应 | NA | — | 自动化流程，无主试/评分者 |
| E6 | 天花板/地板效应 | 1 | p.4 "The restless bandit task poses a challenge for the majority of models"；"the BART proves to be a hurdle for all models"；Fig.2/6/7 全部模型的 DV 与随机/人类基线 | 报告了所有 LLM 的 DV 均值与 95% CI，并以随机=0/人类=1 校准难度，识别 floor 表现 |
| E7 | 共同方法偏差 | NA | — | 非问卷自陈同源测量 |
| F1 | 统计结论效度 | 0.5 | p.5 Fig.2 "Errors bars represent 95% confidence intervals"；p.7 "β = 0.277 ± 0.39, z = 14.1, p < 0.001" | 报告了 CI 与回归系数；缺：样本量/模拟次数依据（仅 "default number of simulations was 100/10"）、5 个假设与多项回归的多重性校正；β ± 0.39 与 z = 14.1 数值不自洽，未说明 ± 含义 |
| F2 | 内部效度 | 0.5 | p.8 CoT/SB 与基线比较；App.D 稳健性；p.9 "limited transparency of certain proprietary models" | 评估了提示变体稳健性和特征混淆；缺：特征为观察性，无基线等价性，CoT/SB 仅 5 模型/2 指标，无损耗/格式失败率处理 |
| F3 | 构念效度 | 1 | App.D "We observe that the CogBench metrics are relatively robust across task variants"；App.E PCA 与相关分析；p.9 "these tasks and the corresponding constructs have not been designed for artificial agents" | 有稳健性与冗余度证据、多操作化（任务变体）及构念迁移限制讨论；Mixtral 先验权重不稳也如实报告 |
| F4 | 外部效度 | 1 | p.3 "We evaluated over 40 different LLMs"；p.14 App.A 表；p.9 "The analysis was preliminary" | 报告了 LLM 样本来源、特征与人类参照来源，指出推广边界（外部效度对 LLM 尚未验证），并跨 40 个模型与提示变体复现 |
| G1 | 分析单位 | 1 | p.6 "any finetuned version of another LLM is part of the same higher level group"；Level-1/Level-2 方程 | 分析单位为 LLM，嵌套于模型家族，处理（特征）与分析层级匹配并显式建模嵌套 |
| G2 | 随机效应 | 0.5 | p.6 Level-2 "u_0j and u_kj are the random effects for the intercept and slope"；App.G mixedlm(..., groups=df_standardized['type_of_llm']) | 说明家族为随机、特征为固定；缺：方程含随机斜率而代码仅指定分组（默认随机截距），结构不一致 |
| G3 | 材料作为随机效应 | 0.5 | p.1 "many of these experiments are programmatically generated"；App.B 各任务 "default number of simulations" | 刺激/试次由程序随机生成并重复多次；缺：任务本身固定，分析中未将材料作随机效应，仅以聚合 CI 体现 |
| G4 | 统计功效 | 0 | — | 无功效分析或样本量论证（40 个 LLM、模拟次数 10/100 均无依据） |
| G5 | 研究者自由度 | 0.5 | p.8 "The selection of these five models and a limited set of metrics was necessitated by the additional engineering effort"；App.C "In the original submission, the five LLMs ... were not included"；App.B.7.4 "we decided to report the risk as the average number of inflation attempts" | 报告了全部 40 个 LLM 结果、模型选择理由及对 BART 指标的改动；缺：数据排除规则、样本量决定方式、验证性/探索性的明确区分（仅称 "preliminary"） |
| G6 | 预先设定/预注册 | 0 | — | 全文未提及预注册 |
| J1 | 位置偏差 | 0.5 | App.B.7.2 "We randomly shuffle the assignment to A, B, and C to avoid biases of LLMs towards certain letters"；App.B.4.2 "to avoid biases towards a given letter" | 识别并随机化了字母标签偏差；缺：选项位置/序号未交换，未检验位置偏差大小 |
| J2 | 冗长偏差 | NA | — | 无 LLM 作裁判 |
| J3 | 谄媚 | NA | — | 非用户立场/纠错对话评估 |
| J4 | 自我偏好 | NA | — | 无 LLM 作裁判 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 提示中的历史为任务本身的交互记录，非少样本示范设计 |
| J6 | 提示敏感性/脆弱性 | 0.5 | App.B 各任务完整 prompt；App.D "Restless bandit V2 / Two-step task V2 / BART V2 / Probabilistic reasoning V2"；"relatively robust across task variants" | 提供完整模板并做提示变体敏感性检验；缺：仅 4/7 任务、5 个 LLM，无版本化记录，无 dev/test 分离 |
| J7 | 长上下文信息位置效应 | 0 | App.B.3.2 "limit the number of trials was made due to context size restrictions for some LLMs"；p.14 App.A 表含 Context Length | 任务历史随试次累积进入上下文，并将名义上下文长度作回归预测因子，但未报告实际使用的 token 数，也未验证模型是否利用全部历史 |
| J8 | 温度与采样随机性 | 0.5 | p.3 "We set the temperature parameter to zero, leading to deterministic responses" 及脚注 2 "setting the temperature to zero has shown to sometimes not guarantee determinism"；App.B "default number of simulations was 100/10" | 报告了温度与模拟次数、CI；缺：种子、其余"默认参数"具体值、非确定性程度的量化 |
| J9 | 重复与文本退化 | 0.5 | p.3 温度为 0；App.F "We imposed a limit of 300 tokens"，"some LLMs begin to exhibit chaotic behavior" | 报告了解码设置并在 CoT/SB 中承认退化问题；缺：重复率/退化率的记录与量化 |
| J10 | 分词效应 | NA | — | 非跨语言/多格式输入 |
| J11 | 测试集污染/数据泄漏 | 0.5 | p.1 "many of these experiments are programmatically generated, minimizing data leakage concerns"；App.B.6.2 "this task is the only one which is not procedurally generated" | 识别了污染风险并以程序化生成缓解；缺：未评估模型训练数据与经典任务的重叠，未对照训练截止日期，时间折扣为固定题目 |
| J12 | 基准饱和 | 0.5 | p.4 "GPT-4 ... achieving human-level scores in most tasks (five out of six)"；p.9 "an openly accessible and challenging benchmark" | 报告了各指标相对随机/人类的水位；缺：未正式评估饱和及采取连续指标/更难子集的对策 |
| J13 | 指令遵循 | NA | — | 非指令遵循评测 |
| J14 | 输出格式约束/结构化输出 | 0.5 | App.B.2.3 "Give the answer in the form 'Machine <your choice>'"；App.F "Final answer: {self.format answer}<your choice>"，"some LLMs do not consistently adhere to this constraint" | 记录了格式约束设置并承认不遵循；缺：格式合法率与格式失败/内容错误的分开报告 |
| J15 | 越狱稳健性 | NA | — | 非安全/对齐攻击评测 |
| J16 | LLM 作为被试的范式定位 | 1 | p.9 "it is unclear if one LLM should be considered a single subject or a population of agents"；"these tasks and the corresponding constructs have not been designed for artificial agents"；p.4 "the human data is only provided as an additional reference point" | 明确界定 LLM 上测得的是行为表型，并论证与人类同名构念的差异与人类比较的谨慎 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p.5 "meta-cognition and model-basedness appear to emerge as properties of high-performing models"；p.7 参数量回归（β = 0.481） | 以连续指标报告规模效应并引用 Schaeffer et al. 的质疑背景；缺：用"emerge"措辞但无多 seed 的规模曲线，未检验是否为指标假象 |
| J18 | 指标博弈与奖励过优化 | NA | p.1 "reducing benchmarks to mere training targets" | 无优化实验 |
| J19 | 评估可复现性与种子/检查点依赖 | 0.5 | p.14 App.A 如 "Claude-3-opus-20240229"、"text-bison@002"；App.B 模拟次数；p.2 代码链接 | 部分模型给出具体 snapshot，并给出重复次数与 95% CI；缺：GPT-4、Claude-1/2 等无快照标识，无配对检验，种子未报告 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 任务为单次提示内累积试次历史（prompt-chaining），不是多轮对话；未分析随轮次衰减 |

## 编码小结
本篇是把 LLM 当作被试做认知心理学实验的"基准 + 假设检验"研究，核心为观察性的多层回归（模型特征→行为指标）和一个小规模的提示技术内操纵（CoT/SB vs 基线），故 B 节多数、D 节全部以及 LLM 裁判相关项（J2/J3/J4）记 NA。强项是操作化与构念效度（A2、A7、A9、F3、J16）：任务有完整 prompt、指标有公式、做了任务变体稳健性和冗余分析，并明确讨论构念迁移与"单个 LLM 是被试还是群体"。弱项是缺少功效/预注册/多重性处理（G4、G6 记 0，F1 仅 0.5），以及 E3、J7 的缺失。不确定处：B9 将"观察性模型特征比较"视作准实验并给 0.5；G2 中方程含随机斜率而代码只分组，据此记 0.5；J14 把格式要求与"不遵循"的定性说明视作基本要件部分达成；J20 将 prompt-chaining 的试次历史视为非多轮对话而记 NA；F1 中 "β = 0.277 ± 0.39, z = 14.1" 数值不自洽，已在备注标出。

