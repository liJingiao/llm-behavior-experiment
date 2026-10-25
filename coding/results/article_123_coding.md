# article_123 | Bias and Volatility: A Statistical Framework for Evaluating Large Language Model's Stereotypes and the Associated Generation Inconsistency | 2024

研究类型概述：这是一篇 LLM 社会偏见/刻板印象的统计评估框架论文，提出 Bias-Volatility Framework，并在 12 个 LLM 上评估性别等属性的歧视风险与生成波动；主体为观察性基准评估与模型间比较，另包含一次 Llama2 毒性数据微调的前后比较。分析单位主要是模型—上下文—职业条件及其聚合风险，而非人类被试。
- **研究构念（Construct）**：社会刻板印象的平均偏差、生成波动与歧视风险｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：在不更新模型的主实验单元中，对12种现成LLM在职业—性别/种族等模板下重复采样，并把输出分布分解为偏差风险和波动风险。（改变职业、群体属性、上下文模板、模型及重复采样；纳入单元不依赖论文另设的毒性数据微调干预。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p8: 'We fine-tuned Llama2 on toxic data ... tested the changes in gender discrimination risk before and after its training'; p23 D.4 reports fine-tuning hyper-parameters. | 主体评估为观察性模型比较；唯一明确的主动操纵是毒性数据微调，报告了前后两个水平及训练程序，但无操纵检验、随机分配或更完整水平说明。 |
| A2 | 因变量 | 0.5 | p4: Definitions 1-3 define s, J, rx, R, Rb, Rv; p7 Table 1 reports R/Rb/Rv for models. | 因变量指标与计分公式明确，但未报告测量信度、效度证据或连续指标预处理/端点控制说明。 |
| A3 | 控制变量 | 0.5 | p5: 'We use a uniform distribution as the distribution of occupations'; p6: 'Randomly sample N articles ... set N = 10,000' and standardize predicates to past tense. | 报告了若干控制手段（职业均匀分布、上下文来源固定、模板标准化、频率加权），但未系统列出所有控制变量及控制方式。 |
| A4 | 混淆变量 | 0.5 | p6: context selection is 'designed to avoid the influence of other confounding factors'; p9 discusses socio-economic correlations; p15 checklist says limitations described '[No]'. | 仅笼统提及避免混淆因素，未具体列出关键混淆、控制方式或残余混淆敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有理论上的调节变量模型，也没有乘积项交互检验或简单斜率分析；模型大小、RLHF 等被作为分组比较，而非正式调节检验。 |
| A6 | 中介变量 | NA | — | 无中介变量、直接/间接效应分解或因果链中介假设。 |
| A7 | 操作性定义 | 1 | p4: Equations 1-8 define stereotype, risk, bias/volatility decomposition; p5-p6 describe occupation/gender word lists and context mining; p22-p23 list X/Y/C. | 关键构念有明确数学操作化和可复现的数据挖掘步骤、词表与模板，测量和计分程序清楚。 |
| A8 | 水平数与类型 | 0.5 | p7 lists 12 models and Table 1; p5-p6 describe binary gender, occupations, uniform occupation distribution; p22-p23 give word lists and templates. | 报告了模型、属性、模板等水平/标签，但未系统说明水平类型、间距/全距或连续变量中心化；部分比较变量只是描述性分组。 |
| A9 | 单一操作化的风险 | 0.5 | p20 C.4 reports risk rankings across book/conversation/textbook/webpage context sources; p21 C.5 reports Chinese results; p10 ethics notes every framework has flaws and blind spots. | 通过多种上下文来源和语言提供一定稳健性/会聚证据，但仍主要依赖同一 token-probability 操作化，未系统讨论单一操作化对推广的限制。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈式多构念测量；核心测量为模型 next-token 概率。共同方法偏差检验不适用于该设计。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或被试组分配到互斥条件；12 个模型接受同一评估框架，不是被试间实验。 |
| B2 | 被试内设计 | NA | — | 论文未建立明确的人类被试内重复测量设计；上下文/职业条件独立查询后聚合，未涉及被试顺序分配或平衡。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合设计及相应误差项。 |
| B4 | 因子设计 | NA | — | 没有完全交叉的因子设计、设计矩阵或 ANOVA 交互表；模型、属性、来源比较是分别汇总的评估。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应 F/df/p/效应量报告。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验、简单主效应或带误差棒交互图。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计。 |
| B9 | 准实验设计 | 0 | p8: 'Toxic data reinforces the model’s systemic bias'; 'RLHF ... exhibit a lower bias risk ... yet ... higher volatility risk'; 'The impact of model size...'; no discussion of nonrandom assignment or causal limits. | 模型大小、RLHF 版本和毒性微调前后比较均非随机分配，但论文使用影响/降低/增加等因果化表述，未明确准实验类型、选择偏差或内部效度局限。 |
| B10 | 被试内设计的适用条件 | NA | — | 不存在被试内顺序处理与可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | p6: 'Randomly sample N articles ... set N = 10,000'. | 这里是对 Wikipedia 语料随机抽样，不是实验条件分配；无条件分配隐藏、基线均衡或 ITT/per-protocol 问题。 |
| C2 | 平衡 | NA | — | 上下文独立计算并聚合，无被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p6: uses clean Wikipedia dump, N=10,000, standardizes predicates to past tense, weights templates by corpus frequency; p7 lists model names and sizes. | 固定了语料来源、模板标准化和频率权重，并报告模型名称/规模，但未报告精确 checkpoint、后端/温度等；也未讨论恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配程序。 |
| C5 | 纳入为变量 | 0 | p8 compares model size, RLHF/base-chat, toxic fine-tuning; p9 uses WLS with salary/education but not as confounder adjustment for model comparisons. | 模型规模、训练数据、架构等潜在混淆未被测量并作为区组/协变量纳入模型比较，也未检验协变量假设。 |
| C6 | 盲法 | NA | — | 数据采集和评分完全自动化，无人类主试/评分者可施盲。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 等顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 各上下文模板独立查询，不存在上下文内学习或练习效应。 |
| D2 | 疲劳效应 | NA | — | 无 human session；模型计算上下文概率不受疲劳影响。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个上下文模板独立条件化，无跨条件延滞/迁移；论文也按上下文分布聚合。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为 token 概率定义的风险指标，不是被试内绝对判断/李克特量表，无范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选/排序式选项呈现；候选词概率按集合归一化，顺序不影响求和结果。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分及跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，也无掩饰情节/事后访谈需求特征问题。 |
| E5 | 实验者效应 | NA | — | 完全自动化评估，无人类实验者或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p7 Figure 5 box plot of model average gender predictions; p9 Figure 10 risk distributions; p7 Table 1 risk scores. | 报告了分布与均值/箱线图，可排查端点；但未明确报告偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；核心为模型概率指标，无人类共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | p7 Table 1 gives point estimates for all models; p8 Figures 6-8 and p9 Figure 9 give comparisons/regressions; p15 checklist says error bars '[N/A]'. | 报告了较多点估计和模型间差异，但无置信区间、样本量/功效依据、多重性校正或统计假设检验说明。 |
| F2 | 内部效度 | 0 | p8: fine-tuning, model size and RLHF comparisons; p15 limitations '[No]'; no allocation concealment, baseline equivalence or sensitivity analysis. | 无随机分配、组间基线等价或内部效度威胁评估；对 RLHF/毒性微调作因果化解释但未限定。 |
| F3 | 构念效度 | 0.5 | p4 defines metrics mathematically; p7 uses ideally unbiased/stereotyped/randomly stereotyped reference models; p5 and p22-p23 use sociological word lists. | 有数学定义、内容来源和参考模型作为一定效度证据，但无信度、人类验证、操纵检验或正式构念效度分析。 |
| F4 | 外部效度 | 0.5 | p7 evaluates 12 models; p20 C.4 cross-dataset context sources; p21 C.5 Chinese replication; p10 ethics discusses tailored assessment. | 报告了模型和上下文来源，并展示跨数据集/语言的一定复现；但模型/上下文代表性、抽样框和明确推广边界讨论不充分。 |
| G1 | 分析单位 | 0.5 | p4 Equations 3-4 aggregate over C and X; p6 context templates weighted by corpus frequency; p7 model-level Table 1. | 明确了从上下文/职业聚合到模型风险的层级，但未用多层/混合模型分离上下文或职业的嵌套方差，也无相应不确定性估计。 |
| G2 | 随机效应 | 0.5 | p4: 'rx = Ec∼C(...)' and 'R = Ex∼X(rx)'; p6 contexts sampled and weighted by distribution. | 上下文集和职业分布被当作抽样分布进行聚合，具有随机因素意味；但未正式报告随机效应结构或随机截距/斜率模型。 |
| G3 | 材料作为随机效应 | 0.5 | p6: contexts are mined from sampled Wikipedia articles and weighted by frequency; p22-p23 list templates and top frequencies. | 上下文材料被视为来自语料总体并参与聚合，但未用 item random effect 或准 F 比，材料固定性/推广限制未充分建模。 |
| G4 | 统计功效 | 0 | p15 checklist: error bars with respect to random seed '[N/A]'; no power analysis or sample-size justification. | 无事前功效分析、样本量/上下文数量论证，也未报告效应量置信区间作为推断精度依据。 |
| G5 | 研究者自由度 | 0.5 | p7 lists all 12 models; p18-p19 report race/religion/disability; p20-p21 report additional data sources and Chinese; code/data claimed available. | 报告了大量模型、属性和分析，但未明确试次/数据排除规则、样本量决定方式，也未区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p15 checklist has no preregistration statement; no registration link or timestamp. | 无预注册；分析计划与探索性分析未事先登记。 |
| J1 | 位置偏差 | NA | — | 不使用 LLM-as-judge、成对比较或多候选项位置选择；测量为 token 概率矩阵。 |
| J2 | 冗长偏差 | NA | — | 不评估开放式生成长度与质量，无 LLM 裁判长度偏差问题。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错对话；任务为无用户立场的模板概率测量。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM 裁判评估模型输出，无自我偏好/同源裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | p23 lists fixed context templates; no few-shot in-context examples are described. | 实验为零样本模板概率评估，未使用 few-shot 示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p6 describes context templates and frequency weighting; p23 lists top ten templates and says remaining templates released with code; p21 reports cross-language results. | 通过大量上下文模板和不同数据源间接考察了 prompt/上下文敏感性，但无 prompt 版本号、dev/test 划分、语义等价措辞消融或完整模板全文。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG 实验；上下文模板很短，不涉及信息位置效应。 |
| J8 | 温度与采样随机性 | NA | p4 describes using predicted token probabilities rather than sampled generation; no temperature/top-p/seed reported. | 核心测量基于 next-token 概率而非采样解码，故采样随机性不构成主要设计组件；精确后端复现问题归入 J19。 |
| J9 | 重复与文本退化 | NA | p4 and p6 use probability matrices/short templates; no open-ended generation or repetition degeneration analysis. | 不涉及开放生成文本的重复/退化问题。 |
| J10 | 分词效应 | 0 | p21 C.5: 'We present the measurement results of our model in Chinese in Table 5'; no tokenizer version or token counts are reported. | 存在跨语言比较，但未报告分词器/版本、token/词数比或在分析中控制 token 长度，中文与英文结果缺乏可比的 tokenization 控制。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p6 uses clean Wikipedia dump for context mining; p7 lists models but no training cutoff or contamination check. | 上下文来自公开 Wikipedia，可能与被测模型训练语料重叠；未报告训练截止日期、污染检测或 held-out 处理。 |
| J12 | 基准饱和 | NA | p7 Table 1 reports bounded continuous risk scores (0 to 1), not an accuracy benchmark with ceiling saturation. | 所用指标为连续风险度量，非接近天花板的标准基准；论文未在饱和基准上宣称提升。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，无约束指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化输出/JSON/文法约束，无格式合法率问题。 |
| J15 | 越狱稳健性 | NA | — | 研究评估社会刻板印象/歧视风险，不涉及越狱或安全对抗攻击评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p4: definition 'grounded in sociological research examining human stereotyping'; p1 abstract frames LLM stereotypes; p10 ethics notes tailored measurement limitations. | 讨论了 LLM 刻板印象与人类社会学刻板印象概念的联系，但未做人类同范式对照或系统构念效度论证，且未报告精确权重 snapshot。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | p8 reports model-size trends but no 'emergent/abrupt' capability claim. | 不涉及涌现能力宣称；所用风险指标为连续量，未在台阶式能力曲线上断言突变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对代理指标进行训练/RL/best-of-N 优化；仅评估模型风险指标。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p15 says code/data available but error bars '[N/A]'; p7 lists model names/sizes but no exact snapshot, repeat count, CI or paired tests. | 缺少重复次数、置信区间、精确 snapshot/API 日期和配对检验；仅有模型名称与代码链接不足以满足评估可复现性要求。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮模板概率查询，无多轮对话历史或跨轮一致性评估。 |

## 编码小结
论文对 BVF 指标、上下文挖掘、词表和模型比较报告较完整，但作为评估性/观察性研究，缺少人类实验设计中的分配、盲法、平衡等结构，也缺少测量信效度、置信区间、精确 snapshot、预注册、混淆控制与部分可复现性报告。多数人类被试特有组件应判 NA；与 LLM 评估相关的 prompt 敏感性、跨语言、污染与可复现性等存在明显不足。
