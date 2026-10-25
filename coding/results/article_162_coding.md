# article_162 | Bias Amplification in Language Model Evolution: An Iterated Learning Perspective | 2024

研究类型概述：理论建模与LLM实验结合：用贝叶斯迭代学习框架分析LLM代际自我演化中的先验偏差放大，并在ACRE归纳任务、缩写词自数据增强任务和on-policy DPO训练中做验证。分析单位为模型代际链/运行（多次seed或多条件链），操纵因素包括提示偏差强度、似然强弱、交互阶段类型、Heff类型、生成轮次及DPO长度约束等；测量指标为后验熵、特定假设概率、易词比例、平均词频排名、平均长度、胜率等。无人类被试。
- **研究构念（Construct）**：迭代学习中的先验偏差放大、文化传递与模式坍缩｜CA 构念锚定：刻板印象（stereotypes, `trm_4a3fd79d0b285`）；态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：仅依据现成LLM通过ICL进行多代数据生成和传递的实验，检验显式/隐式假设及交互约束如何改变偏差的代际演化。（改变初始样本、先验偏好、示例压缩压力、交互约束和迭代代数。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'We use six different prompts to introduce different levels of biases'; p.7: 'control the strength of the likelihood by selecting different h*'; p.7 Table 1: 'imitation-only', 'w. self-refine', 'w. hypo-search'; p.24-25 prompt manipulation details. | 主要自变量被明确命名并给出多个水平，但各条件的运行/seed分配、随机化方式及完整操纵检验未系统报告，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.6: 'calculate Plmw(h) ... by multiplying the probabilities of specific tokens'; p.9: metrics 'Ratio of easy samples', 'Average rank', 'Average length'; p.7 Table 1 reports mean±SE; p.8 Figure 3 reports mean and standard deviations. | 因变量指标与计分方式基本清楚，并报告多次运行变异；但未系统报告信度/效度证据、连续指标预处理及天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | p.24: 'The temperature is 0.1'; p.7 names GPT3.5, GPT4, Claude3-haiku, Mixtral; p.29 Figures 17 prompt design; p.14 Appendix A discusses assumptions. | 报告了部分控制变量（温度、模型版本、提示模板、任务设置），但未形成系统控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.7: 'the confidence of LLM’s prediction is heavily influenced by its degree of familiarity ... manipulate the prompt to create spurious correlations'; p.24-25 manipulates hint position before/after d0; p.14 discusses assumptions not exactly satisfied. | 识别并部分控制了提示熟悉性、位置和模型差异等潜在混淆，但未系统报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | 0.5 | p.7: 'the likelihood and prior compete with each other during iterated learning'; p.26 Figures 12-13 show prior-bias level × likelihood strength; p.9 Table 2 crosses Heff settings with Ne levels. | 存在明确的交互/调节式检验（偏差强度×似然、Heff×Ne），但未使用正式乘积项、中心化或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 全文没有中介假设，也没有直接/间接效应分解；中介变量组件不适用。 |
| A7 | 操作性定义 | 0.5 | p.6 ACRE rule/sampling procedure; p.24 posterior token-probability calculation; p.27-29 Figures 14-17 full prompts; p.9 acronym task procedure; p.1 code link. | 关键任务和指标有较详细操作化，部分实验细节依赖公开代码；对全部实验（尤其DPO训练超参数）未在正文完整写明，故为部分满足。 |
| A8 | 水平数与类型 | 0.5 | p.7: 'six different prompts to introduce different levels of biases'; p.25 lists 'Very high / High / Medium / Mild / Low / Very low'; p.8 five Heff settings; p.9 Ne=2,4,6,8,10. | 主要因素的水平数与取值/标签报告较清楚，但水平类型、间距/全距及连续变量中心化说明不完整。 |
| A9 | 单一操作化的风险 | 1 | p.6-10: experiments across ACRE, acronym self-augmentation, and on-policy DPO; multiple models GPT3.5/GPT4/Claude3-haiku/Mixtral; p.23 toy Bayesian iterated learning; consistent amplification trends described. | 关键构念通过多种任务、多种模型和多种指标进行三角验证，并报告了趋势一致性，满足多操作化要求。 |
| A10 | 单一方法的风险 | NA | — | 自变量为提示/训练条件，因变量为模型输出或算法计算指标，不存在人类自陈式同源测量；共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 研究没有人类被试或人类被试组分配；使用LLM代际链和多条件运行，不能按人类被试间设计编码。 |
| B2 | 被试内设计 | NA | — | 不存在对同一被试实施所有条件并做顺序平衡的被试内设计；代际重复是纵向演化过程而非条件顺序平衡。 |
| B3 | 混合设计 | NA | — | 没有人类混合设计及相应组间/组内误差项统计模型；虽然有条件与代际重复，但不构成可编码的混合设计。 |
| B4 | 因子设计 | 0 | p.7: six prior-bias levels × strong/weak likelihood; p.9 Table 2: five Heff settings × Ne=2,4,6,8,10; p.26 Figures 12-13. | 存在交叉因素设计和交互趋势展示，但未给出完整设计矩阵、每格样本量和ANOVA统计表；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | p.7 Table 1 reports condition means/SE; p.7 text describes prior/likelihood trends; p.9 Table 2 reports condition means/SD. | 主效应趋势有描述，但未报告F值、自由度、p值和效应量。 |
| B6 | 交互作用 | 0 | p.7: 'the likelihood and prior compete'; p.26 Figures 12-13 show bias-level × likelihood curves; p.9 Table 2 shows Heff × Ne means. | 报告了交互趋势和图示，但无正式交互检验、简单效应及多重比较校正；因未报告交互项的正式统计检验结果，按级联规则基本要件未达成记 0。 |
| B7 | 区组设计 | NA | — | 没有区组/分层设计或区组变量。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验的随机分配失败情形；研究为LLM实验与理论模拟。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内条件处理，不涉及可逆性或迁移对称性的被试内适用条件论证。 |
| C1 | 随机化 | 0 | p.8: '5 different seeds'; p.8: '10 different h*'; p.29: '4 different seeds'; no description of random assignment or random-number tool. | 报告了多次运行/seed，但未报告条件如何随机分配、随机数生成工具或分配隐藏。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序；代际顺序固定且是研究现象的一部分。 |
| C3 | 恒定 | 0.5 | p.24: 'The temperature is 0.1'; p.7 names model versions; p.29 Figures 17 prompt design; p.14 Appendix A discusses assumptions. | 列出部分恒定变量与水平（温度、模型版本、提示模板），但未系统讨论其对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入统计模型的设计。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者盲法安排；LLM裁判的偏差风险在J4中评估。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA层级需要报告。 |
| D1 | 练习效应 | NA | — | 研究不是人类练习任务；代际学习属于处理本身，不存在需要截除或抵消的练习效应。 |
| D2 | 疲劳效应 | NA | — | LLM实验无人类疲劳风险。 |
| D3 | 延滞 / 迁移效应 | NA | — | 跨代信息传递是迭代学习处理本身，不是需要在条件间洗脱的顺序混淆；因此不按延滞/迁移效应编码。 |
| D4 | 不对称迁移 | NA | — | 没有需要平衡的条件对，也不检验跨条件迁移对称性。 |
| D5 | 范围效应 | NA | — | 研究不使用主观量表或绝对判断评分类任务。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.24-25: misleading sentence placed before vs after d0; p.25 lists 'Very high: ... before and after', 'Very low: ... after dt' and discusses position effects. | 识别并操纵了提示位置效应，但没有系统随机化/反平衡各条件的提示位置；部分偏差水平与位置安排存在混杂。 |
| E2 | 默认赞同 | NA | — | 研究不使用Likert或态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不需要掩饰情节或事后访谈检查需求特征。 |
| E5 | 实验者效应 | NA | — | 无人类主试或人类评分者；实验者效应不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6: posterior entropy 'gradually decreases to almost zero'; p.8 Figure 3 histogram and probability curves; p.9 Figure 4 response length curves; Tables report mean±SD/SE. | 报告了均值、变异和明显的端点饱和趋势，但未系统报告偏度、端点频率及任务难度预实验校准。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.7 Table 1 reports mean±SE; p.8 Figure 3 mean/SD; p.9 Table 2 mean±SD; p.8 '5 different seeds'; p.7 '10 different h*'. | 报告了多次运行的变异和样本量，但无事前功效分析、95%CI或多重性校正。 |
| F2 | 内部效度 | 0.5 | p.6-10 controlled prompt/Heff/DPO manipulations; p.14 Appendix A discusses assumptions and deviations; no random allocation or allocation concealment reported. | 通过条件控制和多模型重复支持内部效度，但没有随机分配、分配隐藏或正式内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | p.24: format-related token probability 'always close to one'; p.6 posterior entropy; p.7 manipulation of P0 via prompts; multiple models/tasks. | 有操纵检验和多种操作化证据，但缺少正式信度/效度统计或测量工具效度论证。 |
| F4 | 外部效度 | 0.5 | p.6 lists GPT3.5, GPT4, Claude3-haiku, Mixtral; p.8-10 tasks; p.14 Appendix A.2 calls tasks 'toyish' and discusses applicability; p.29 mixed GPT/Claude results. | 报告了模型/任务来源并讨论部分推广边界，但样本并非代表性抽样，也缺少系统跨情境复现。 |
| G1 | 分析单位 | 0.5 | p.8: '5 different seeds'; p.8: '10 different h*'; p.9 Table 2 averages over seeds; p.29: '4 different seeds'; generations nested within chains. | 说明了运行/代际层级并做聚合，但没有明确分配层级与分析层级的匹配，也未用多层模型处理嵌套方差。 |
| G2 | 随机效应 | 0.5 | p.7 Table 1 mean±SE; p.8 Figure 3 mean±SD; p.9 Table 2 mean±SD; no explicit random-effects specification. | 以多次seed/运行的变异报告部分体现了随机变异，但未说明哪些因子为随机效应及其结构。 |
| G3 | 材料作为随机效应 | 0.5 | p.6 ACRE uses fixed 5 objects and 243 hypotheses; p.9 acronym words from COCA frequency; p.14 Appendix A.2 acknowledges 'toyish' tasks; no item random effect. | 材料/项目被视为固定任务实例，未在模型中作为随机效应；但通过多任务、多模型部分缓解推广局限。 |
| G4 | 统计功效 | 0 | No power analysis or sample-size justification; only multiple seeds/runs (5, 10, 4) are reported on p.7-8, p.29. | 没有设计阶段功效分析或其他样本量确定依据，只报告了重复运行变异。 |
| G5 | 研究者自由度 | 0.5 | p.7: '10 different h*'; p.8: '5 different seeds'; p.29: '4 different seeds'; p.7/p.29 note Mixtral results omitted due to instruction violations/typos; many conditions in Appendix. | 报告了主要因变量、条件和部分排除理由，但未说明样本量决定、停止规则或验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registry link, or pre-specified analysis plan is reported. | 无预注册或明确的事前分析计划说明。 |
| J1 | 位置偏差 | 0 | p.10 footnote: 'We use GPT4 to compare the helpfulness between responses generated by different models'; no report of swapping response order or position analysis. | 存在LLM裁判成对比较的位置偏差风险，但未报告位置反平衡、交换顺序重判或翻转率。 |
| J2 | 冗长偏差 | 0.5 | p.10: length bias studied; adds 'you are a laconic agent and prefer concise answers' to annotator LLM; Figure 4 reports average response length and win rate against SFT. | 明确识别并部分控制长度偏差，报告了长度与胜率曲线；但未报告长度—得分相关系数、裁判温度或盲评细节。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场/多轮反馈/纠错对话式评估，谄媚偏差不适用。 |
| J4 | 自我偏好 | 0.5 | p.10 footnote: GPT4 compares helpfulness between responses; evaluated models include llama-2-7B/DPO/SFT; no report of anonymization, individual judge results, or human gold agreement. | 报告了裁判模型和被评模型家族，但未量化自我偏好、匿名化或与人类金标准一致性。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.6 few-shot d0 in ACRE; p.8 20 initial samples in acronym task; p.27-29 Figures 14-17 give prompt templates; 5 seeds/10 h* used. | 报告了示例数量和部分来源/模板，但未系统报告标签比例、示例排列反平衡或多示例集重采样。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.24-25 six prompt-bias variants and synonym/object-name/position changes; p.27-29 Figures 14-17 full prompt templates; p.1 code link. | 提供了完整提示模板并做了多种措辞/位置敏感性比较，但无版本号/迭代日期和明确dev/test划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验不是长文档/RAG长上下文位置效应研究；上下文主要为任务提示和示例。 |
| J8 | 温度与采样随机性 | 0.5 | p.24: 'The temperature is 0.1'; p.8: '5 different seeds'; p.7: '10 different h*'; p.29: '4 different seeds'; no top-p/top-k/seed values for all models. | 报告了部分采样超参和重复运行次数，但缺少完整采样参数、seed值与置信区间。 |
| J9 | 重复与文本退化 | 0 | p.24 only reports temperature=0.1; no decoding strategy/repetition penalty/repetition-rate QC; p.29 mentions Mixtral typos but not systematic degeneration analysis. | 开放生成任务中未系统报告解码策略和文本退化指标，无法排除解码/重复对结果的影响。 |
| J10 | 分词效应 | NA | — | 研究为单语言英文任务，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | ACRE被用作行为实验任务，而非用于宣称基准泛化能力；没有基准污染检查需求。 |
| J12 | 基准饱和 | NA | — | 研究不是基准饱和评估，也不依赖SOTA基准分数宣称提升。 |
| J13 | 指令遵循 | NA | — | 指令遵循不是本研究的因变量；仅提到模型格式遵循作为实验可行性条件。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.6 requires rule format; p.24 format-related token probability 'always close to one'; p.29 JSON output prompt and Mixtral typos; no separate format legal-rate table. | 报告了格式约束和部分格式遵循证据，但未系统报告格式合法率、重试策略及格式失败与内容错误的分离。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1-2 draws analogy between LLM evolution and human cultural evolution/iterated learning; p.5 Proposition 2 links ICL to Bayesian agents; p.14 Appendix A discusses assumptions and deviations. | 明确界定了LLM作为贝叶斯智能体的测量构念并讨论与人类迭代学习的类比及假设限制，但未做同范式人类对照实验。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | p.10 on-policy DPO ranks responses by another LLM annotator for helpfulness; GPT4 win-rate evaluation; Figure 4 shows length/win-rate tradeoff; too strong Hshort harms helpfulness. | 涉及代理指标（LLM helpfulness）优化，并报告了长度与胜率权衡；但训练与评估均为LLM，缺少独立held-out人类金标准和代理-真实双曲线。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.7 reports model versions 'GPT3.5-Turbo 1106', 'GPT3.5-Turbo 0125', 'Claude3-haiku-20240307'; p.8 5 seeds; p.10 llama-2-7B; Table 1/2 error bars. | 报告了部分snapshot标识和重复次数，但缺少95%CI、配对检验及所有评估的精确snapshot。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.6-7 iterated learning across generations; p.8 Figure 3 per-generation curves; p.14: 'we will feed all historical information to API'; p.8 uses 6 generations in acronym task. | 进行了多轮/多代评估并按代际报告，但未明确区分单轮与多轮成绩、上下文截断规则和跨轮一致性分析。 |

## 编码小结
论文将人类文化演化的迭代学习框架迁移到LLM，理论贡献明确，实验覆盖多种任务与模型，并对先验偏差放大给出较系统的行为证据。方法报告在提示模板、条件设置和主要指标上较充分，但作为心理/行为实验编码仍存在若干报告缺口：条件分配与随机化、统计模型、随机效应、功效分析、预注册等不完整；许多人类被试特有组件不适用。LLM评估相关风险中，长度偏差被直接研究并部分控制，LLM裁判与提示敏感性有部分报告，但位置偏差、解码重复、独立人类金标准等报告不足。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B6（0.5→0）, B4（0.5→0）。
