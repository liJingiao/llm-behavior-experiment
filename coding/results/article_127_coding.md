# article_127 | AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text | 2025

研究类型概述：计算/基准评测型研究：提出 Creativity Index 与 DJ Search，将文本与 RedPajama 网页语料进行逐字/语义匹配，比较人类文本与多个 LLM 生成文本的语言新颖性/创造力，并用于零样本机器文本检测；分析单位主要是文本/文档，而非人类被试。
- **研究构念（Construct）**：语言创造力中的新颖性与既有文本重组程度｜CA 构念锚定：创造性思维（creative thinking, `trm_4a3fd79d09f42`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：让现成LLM完成小说、诗歌和演讲写作，并与专业人类文本比较。（改变作者类型、模型、提示风格、解码、上下文长度及已有对齐checkpoint。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: “We experiment with state-of-the-art LLMs... We will ablate the effect of different matching criteria, prompt formats, decoding strategies, context length, and model sizes”; p.7: prompt-format and top-p comparisons. | 自变量/条件与多数水平清楚，但文本到条件的分配不是随机化，且无 manipulation check；按设计层完整性只能给部分满足。 |
| A2 | 因变量 | 0.5 | p.4 defines L-uniqueness and Creativity Index formula; p.25: “sum up the L-uniqueness for 5 ≤ L ≤ 12”; p.26-27: correlations with TTCW dimensions. | 因变量指标与计分方式明确，并有部分效度证据；但未报告传统信度、连续指标预处理细节及完整天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | p.5: RedPajama reference corpus and model list; p.23: “nucleus sampling with p = 0.9... maximum length... 288 tokens”; p.25: DJ Search parameters. | 报告了若干保持恒定的设置（语料、采样 p、生成长度、L 范围），但不是系统控制变量清单，也未逐项说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.8-9: limitations mention RedPajama cutoff/private data, overlap not conclusive memorization, classic literature era/style; p.7: longer prompts can lead to copying. | 识别了多个潜在混淆并给出部分控制/替代解释，但未做正式敏感性分析或系统评估残余混淆。 |
| A5 | 调节变量 | NA | — | 理论模型没有调节变量假设，也没有调节交互检验；模型规模/提示等只作分组消融，不构成调节设计。 |
| A6 | 中介变量 | NA | — | 没有中介变量或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.4 Creativity Index formula; p.19-20 DJ Search algorithms; p.23-25 full prompt templates, model versions, generation parameters; p.25 L range and WMD threshold. | 关键构念（文本新颖性/创造力）与文本来源条件均有可复现的操作化程序，参数与提示模板充分。 |
| A8 | 水平数与类型 | 0.5 | p.5: model/task list; p.7: prompt formats, top-p, prompt length, model size; p.23-24: full list of prompt variants; p.25: L=5..12. | 报告了多个条件及其标签，但水平类型、全距/间距、连续变量中心化等不完整，top-p 具体取值也未在正文完整列出。 |
| A9 | 单一操作化的风险 | 1 | p.7: verbatim-only vs verbatim+semantic; p.26: WMD variants and correlations; p.26-27: TTCW expert-rubric correlations; p.9 limitations. | 对创造力/新颖性使用了多种匹配标准与距离变体并报告会聚结果，也讨论了指标局限。 |
| A10 | 单一方法的风险 | NA | — | 构念为文本统计属性，不是自陈量表或多来源心理测量；共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试分配到实验条件；人文本与模型文本是按来源观察分组，不是被试间随机实验。 |
| B2 | 被试内设计 | NA | — | 没有同一分析单位接受所有条件的重复测量设计。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素混合设计。 |
| B4 | 因子设计 | NA | — | 研究不是完整交叉因子实验，未报告设计矩阵、每格样本量与 ANOVA 交互表；领域/模型/匹配标准多为分别比较或消融。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无因子交互检验与简单效应分析。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理分配研究，而是文本来源的观察性比较与基准评测；未定义准实验类型。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理，不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥实验条件；人类/LLM文本按来源获得，不是概率分配。 |
| C2 | 平衡 | NA | — | 无跨条件顺序，因此无顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.5: RedPajama reference corpus; p.23: “nucleus sampling with p = 0.9” and max length 288; p.25: DJ Search parameter settings. | 列出了一些恒定设置，但未系统列出所有设备/模型版本/温度等恒定水平，外部效度限制讨论也较分散。 |
| C4 | 匹配 | 0.5 | p.24: human novel/speech/poem texts selected “such that their total length exceeds 256 words”; p.23: generations start with human initial sentence. | 在文本长度和起始语境上做了近似匹配，但未报告正式匹配方法或匹配后均衡性检验。 |
| C5 | 纳入为变量 | 0 | p.7: longer prompts tended to slightly increase Creativity Index; p.9: reference corpus/private data limitation discussed but not modeled as covariate. | 识别了提示长度、参考语料等潜在混淆，但未把它们作为区组/协变量纳入统计模型，也未检验斜率齐性。 |
| C6 | 盲法 | NA | — | 主要结果由自动化指标计算，无人类被试/评分者盲法安排；去重中的 LLM 判断不属于结局评分盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级设计。 |
| D1 | 练习效应 | NA | — | LLM 文本为独立生成，不存在人类被试跨试次练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题；生成为计算过程。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留/清洗期设计。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 不使用主观量表或绝对判断任务。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选项/刺激序列呈现，也无被试内处理顺序需要随机化或反平衡。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征或事后访谈问题。 |
| E5 | 实验者效应 | NA | — | 数据采集基本自动化，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.25: “L-uniqueness is close to zero for most human and machine texts when L ≤ 5 and close to one when L ≥ 12. Therefore... 5 ≤ L ≤ 12”; p.7 reports means/percent differences. | 说明了端点风险并通过 L 范围校准任务，但未系统报告均值/SD/偏度/端点频率表。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念测量，不涉及共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | p.7: main comparisons report p-values and N (e.g., p=6.9×10−27, N=600); p.8: RLHF p-values; p.26: correlation r and p; no CIs/power analysis. | 报告了 p 值、样本量和部分百分比差异/相关系数，但无置信区间、无样本量功效依据，也未说明多重比较校正。 |
| F2 | 内部效度 | NA | — | 不是随机分配实验，无被试流向、分配隐藏或基线等价性检验；主要定位为观察性文本比较/基准评测。 |
| F3 | 构念效度 | 0.5 | p.26-27: Creativity Index correlates with TTCW expert rubric dimensions; p.25-26: WMD variants correlate with Euclidean distance; p.9 limitations. | 提供了构念效度证据和多种距离变体的会聚证据，但未报告指标信度/评分者信度，也无操纵检验。 |
| F4 | 外部效度 | 1 | p.5 and p.24-25: human texts from BookMIA, PoemHunter, American Rhetoric, XSum, NaturalProofs; multiple model families/domains; p.9: limitations on high-quality human authors and reference corpus. | 报告了样本来源、领域与模型边界，并在 novel/poetry/speech/news/proof 等多情境中复现主要比较。 |
| G1 | 分析单位 | 0.5 | p.7: comparisons report N=600 etc.; p.8: model/domain comparisons; no multilevel model or clustering by model/prompt reported. | 分析单位基本是文本，但同一模型/提示下多个文本的嵌套结构未显式建模，分配层级与统计层级匹配说明不足。 |
| G2 | 随机效应 | 0.5 | p.5 and p.23: specific models listed (GPT-3, ChatGPT, LLaMA 2, Tulu 2, OLMo); no random-effects structure reported. | 报告了模型清单，但把模型/提示当作固定条件比较，未说明随机效应结构或结论可推广的模型总体。 |
| G3 | 材料作为随机效应 | 0.5 | p.24-25: “randomly sample 100 book snippets”, “randomly sample 100 speeches”, “randomly sample 100 poems”, etc.; analysis treats texts as independent observations. | 材料/文本被视为从更大语料抽样，但分析中未使用 item random effect 或等价的项目层面方差分离。 |
| G4 | 统计功效 | 0 | p.7-8 report p-values and N but no a priori power analysis or sample-size justification; p.26 reports r/p without CIs. | 无设计阶段功效分析或样本量论证，也未系统报告效应量置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.24-25: sampling and deduplication rules described; p.7-8 many analyses reported; no explicit confirmatory/exploratory distinction or stopping rule. | 报告了抽样/去重规则与多数条件，但未完整说明全部因变量、样本量决定方式及探索性/验证性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration/platform/registration number is reported anywhere in the paper. | 无预注册，且未明确声明为纯探索性研究；按口径记 0。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较中的位置偏差。 |
| J2 | 冗长偏差 | NA | — | 主要用确定性文本匹配指标评估创造力，不使用 LLM 裁判对开放式回答长短进行质量评分。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场/framing 操纵，不涉及谄媚。 |
| J4 | 自我偏好 | NA | — | 去重步骤虽调用 LLaMA 2 Chat，但不是用 LLM 作为裁判评估被评模型输出质量；无自我偏好评估场景。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.22: deduplication prompt includes “Here are some examples” with four in-context Yes/No examples; p.21 describes using LLaMA 2 Chat for copy/quotation checking. | 主生成实验是零样本，但在去重 LLM 判断中实际使用了 few-shot；示例模板可见，但未报告示例来源、标签比例控制与排列反平衡。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.7: prompt-format variants produce minimal difference; p.23-24: full prompt templates for novel/poem/speech/news/proof and creativity prompts. | 提供了完整模板并做了多种措辞消融，但无 prompt 版本号/迭代日期、dev/test 划分及敏感性统计的系统报告。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短提示与数百 token 文本，不是长上下文/RAG 位置效应实验。 |
| J8 | 温度与采样随机性 | 0.5 | p.23: “For all generations, we use nucleus sampling with p = 0.9 and set the maximum length... to 288 tokens”; no temperature/seed/CI reported. | 报告了主要采样参数 top-p 与最大长度，但缺 temperature、seed、重复采样次数与置信区间。 |
| J9 | 重复与文本退化 | 0.5 | p.23: nucleus sampling p=0.9 and max length 288; p.7: decoding p-value ablation. | 报告了解码策略，但未报告 repetition penalty、n-gram 重复率/退化率及条件间解码恒定性检查。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本，无跨语言分词效应比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.4: deduplication for texts in reference corpus; p.8: GPT-4 RedPajama cutoff issue and model-generated reference corpus; p.21: dedup thresholds; p.24-25: dataset cutoff notes. | 识别并处理了参考语料截止日期/训练数据重叠问题，但未对所有模型报告系统污染检测率。 |
| J12 | 基准饱和 | NA | — | 不是接近天花板的传统 accuracy 基准饱和比较；检测 AUROC 也未报告饱和问题。 |
| J13 | 指令遵循 | NA | — | 因变量是文本创造力/检测，不是指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/JSON 格式输出，无格式合法率问题。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2 and p.4: creativity defined via originality/statistical rarity; p.9: limitations about high-quality human authors and corpus; no same-paradigm human generation experiment. | 将 LLM 输出与人类文本的“语言创造力”比较并讨论了构念来源与局限，但未做同范式人类生成对照，也未系统论证人类同名构念的可迁移性。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有宣称规模涌现/突变；模型规模分析只报告无一致趋势。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对代理指标进行训练/RL/best-of-N 优化，也无 overoptimization 双曲线。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.23: model names/versions such as text-davinci-003, gpt-3.5-turbo, LLaMA 2, Tulu 2, OLMo; p.7: N=600 etc.; no CI/paired tests/seed logs. | 报告了部分模型标识与样本量，但 snapshot 标识不完整，且无重复运行置信区间、配对检验或原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮生成/评估，无多轮对话历史累积。 |

## 编码小结
论文对 Creativity Index 的构念定义、算法、参数、生成提示与多领域比较报告较充分，并提供了与 TTCW 专家评分的效度证据；但其设计基本是观察性文本比较和消融，缺少随机分配、功效分析、预注册、模型/文本嵌套随机效应、置信区间与多种可复现性控制。多数人类实验专属组件不适用。
