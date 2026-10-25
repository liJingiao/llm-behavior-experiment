# article_206 | Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies | 2023

研究类型概述：LLM-as-participant 的“Turing Experiment”方法论文：用 GPT 系列模型通过 zero-shot prompt 模拟多个被试，复现 Ultimatum Game、Garden Path、Milgram Shock、Wisdom of Crowds 四类人类研究，并将模拟结果与既有文献/人类数据比较。分析单位主要是模型生成的模拟记录、k-choice 概率分布、姓名对/句子的聚合结果和模型版本，不是人类被试随机实验。
- **研究构念（Construct）**：经典经济、心理语言和社会心理行为的群体模拟与失真｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：用现成LLM模拟多名实验参与者，复现最后通牒、花园路径、Milgram服从和群体智慧实验。（复现原实验条件，并改变persona、人口信息、实验条件和模型版本。）｜CA 任务锚定：最后出价博弈（Ultimatum Game (UG), `trm_553e8882e3cb6`）；阅读广度任务（reading span task, `trm_4c40d168898db`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6: 'Our Ultimatum Game simulator takes three inputs: an integer offer in {0, 1, . . . , 10}, the name of the proposer, and the name of the responder.' p.14 Table 2: '11 offers', '24 control sentences and 24 GP sentences', '30 stages of shock'. p.5: 'natural temperature = 1 and top p = 1 parameters are used.' | 自变量/条件（offer 金额、句子类型、shock/submersion 阶段、问题）及其水平有明确命名和取值，但操纵程序、条件分配到记录的方式、模型比较是否作为正式自变量、以及操纵检验均不完整或不正式。 |
| A2 | 因变量 | 0.5 | p.5: 'Valid percentage generation rates... All rates have a standard error of less than 0.05%.' p.6: 'we compute validity rates, consistency of decisions for a given name pair across offers, and agreement with prior results.' p.18: 'Valid completions must be integers (commas and spaces are ignored).' | 各 TE 的因变量（accept/reject 概率、grammaticality 判断、shock/termination 分类、数值估计）与计分方式基本明确，validity rate 与格式规则也有报告；但缺少人类测量意义上的信度/效度证据、条目级计分细节和对所有连续指标的预处理说明。 |
| A3 | 控制变量 | 0.5 | p.5: 'the natural temperature = 1 and top p = 1 parameters are used.' p.6: 'This procedure yielded a balanced design where each of the 1,000 names was used for the responder 10 times.' p.4: 'prompts...' | 报告了若干被控制的变量（温度、top-p、姓名平衡、prompt 模板、模型版本），但不是系统的控制变量清单，也未逐一说明控制手段及其对结果的影响。 |
| A4 | 混淆变量 | 0.5 | p.2: 'the TE should be zero-shot... otherwise the model may simply repeat the prior data.' p.9: 'the models have almost certainly been trained on data that includes descriptions of these experiments... we created three artificial variations of TEs.' | 明确识别训练数据污染这一潜在混淆，并对三个 TE 构造新颖变体加以缓解；但对残余污染、prompt 敏感性、模型训练偏差等内部效度威胁未做敏感性分析或系统量化。 |
| A5 | 调节变量 | 0.5 | p.7: 'We find that the distributions of acceptance probabilities in the LM-5 simulations vary significantly (p < 1e-16) by the gender of the pairings.' Figure 5 on p.8 shows male–female pairing differences. | 性别配对被作为探索性调节/分组变量分析，并报告了组间显著性；但没有正式的报告乘积项交互模型、中心化/标准化或完整简单斜率分析，因此只算部分满足。 |
| A6 | 中介变量 | NA | — | 全文不包含中介变量或直接/间接效应分解；研究模型是模拟与复现人类研究，不涉及中介假设。 |
| A7 | 操作性定义 | 1 | p.6 Figure 3 shows the full Ultimatum Game prompt; p.14 Table 2 lists TE inputs; p.15–17 lists all garden-path/control sentences; p.18 lists WOC questions; p.27–33 gives full Milgram prompt templates and algorithm text. | 对关键条件、材料、prompt 构造和输出计分/解析规则给出了足够可复现的操作化细节，并给出代码链接（p.6）。 |
| A8 | 水平数与类型 | 0.5 | p.6: 'integer offer in {0, 1, . . . , 10}'; p.14 Table 2: '11 offers', '24 control sentences and 24 GP sentences', '30 stages of shock'; p.18: 10 general-knowledge questions. | 报告了水平数和各水平标签/取值，但未系统说明水平类型（名义/等级/连续）、间距/全距，连续变量也无中心化/标准化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.9: 'we created three artificial variations of TEs'; p.15: original and authored garden-path sentences; p.21: novel destructive obedience scenario; p.18: authored WOC questions. | 对多项关键现象采用了经典材料与作者新编材料的多种操作化，并报告趋势相似；但 Ultimatum Game 基本仍为单一操作化，且未系统讨论单一操作化的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是人类自陈/同源自评设计；条件与结果均由同一 LLM/prompt 管道产生，但其主要风险属于 prompt、采样、LLM 裁判与非确定性（J 节），不以人类共同方法偏差检验为适用框架。 |
| B1 | 被试间设计 | NA | — | 没有人类被试被分配到互斥条件；模拟记录是独立 prompt 生成/概率计算，不是人类被试间随机分配实验。条件操纵在 A1/E1 中处理。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量及顺序平衡设计；Milgram 的多阶段记录是固定协议模拟，不是需要平衡顺序的人类被试内实验。 |
| B3 | 混合设计 | NA | — | 不存在人类组间/组内混合设计，也无混合 ANOVA 误差项。 |
| B4 | 因子设计 | NA | — | 虽然不同 TE 有多类输入（金额、姓名、句子类型、题目），但没有正式因子设计、完整设计矩阵、每格样本量和主效应/交互 ANOVA，不能按人类因子实验组件编码。 |
| B5 | 主效应 | NA | — | 不存在因子设计意义上的主效应统计检验；模型间与条件间比较主要是描述性/概率分布比较。 |
| B6 | 交互作用 | NA | — | 没有正式因子交互项检验；性别配对分析是探索性组间比较，已在 A5 记录。 |
| B7 | 区组设计 | NA | — | 姓名按种族/性别平衡用于构造材料，但不是人类区组随机分配，也没有区组固定/随机效应模型。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；没有人类非随机分组及选择偏差处理。与历史人类研究的比较属于外部效度/复现比较。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理可逆性/迁移对称性设计；Milgram 的固定阶段协议不是可平衡的被试内处理。 |
| C1 | 随机化 | NA | — | 没有处理条件随机分配；姓名配对虽由随机洗牌构造（p.6），但不是实验处理分配，也无分配隐藏/ITT 等人类试验随机化机制。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，也不存在顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.5: 'natural temperature = 1 and top p = 1 parameters are used'; p.5 lists the GPT model versions; p.6 gives the code URL. p.2 discusses prompt validation. | 报告了若干恒定设置（温度、top-p、模型版本、prompt 模板），但未系统列出全部恒定变量及其水平，也未在讨论中说明这些恒定设置造成的外部效度限制。 |
| C4 | 匹配 | NA | — | 没有基于结果或基线的人类匹配；姓名按种族/性别平衡是材料构造，不是匹配控制。 |
| C5 | 纳入为变量 | NA | — | 没有已知混淆变量被作为协变量/区组纳入统计模型并检验 ANCOVA 假设。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者可盲；LLM 分类/裁判问题在 J4 处理。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 模拟没有人类练习效应或上下文内学习；Milgram 多次生成是协议推进，不是需要练习块/ABBA 抵消的练习效应设计。 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳；单次生成/概率计算不存在人类 session 休息与时间分散问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 没有跨条件药物/学习残留或人类清洗期设计；各 TE 记录基本是独立 prompt 生成，Milgram 的阶段累积属于协议结构而非交叉处理残留。 |
| D4 | 不对称迁移 | NA | — | 没有交叉处理的迁移对称性检验。 |
| D5 | 范围效应 | NA | — | 因变量主要是 accept/reject、grammaticality、shock/termination、数值估计；不使用人类主观李克特量表或绝对量值判断，无范围效应校准问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.6: 'We randomly shuffled the dataset of surnames, paired each of the 500 surnames with five other surnames... balanced design.' p.6 Figure 3 uses fixed completion options 'accept or reject'; p.29 uses fixed 2-choice prompts 'did shock or did not shock'. | 姓名/材料配对有随机洗牌和平衡，但 k-choice/2-choice 选项顺序固定，未报告选项位置随机化或反平衡，也未报告顺序位置分析。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，故无人类需求特征与事后访谈检查；LLM prompt 中的模拟情境不属于人类需求特征。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.9: 'the majority... gave perfectly correct estimates... hyper-accuracy distortion'; Figure 8 reports 'median normalized estimate... black lines indicate the quartiles'; p.19 Table 3 reports medians and IQR for all questions/models. | 报告了均值/中位数、IQR 和 WOC 的端点堆积（IQR=0，hyper-accuracy），并识别了天花板式失真；但未系统报告偏度、端点频率表，也未报告预实验难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | 不是人类自陈式多构念测量，共同方法偏差框架不适用；相关 LLM 同源风险在 J4/J8/J9 处理。 |
| F1 | 统计结论效度 | 0.5 | p.5 Table 1: 'All rates have a standard error of less than 0.05%.' p.7: 'vary significantly (p < 1e-16) by the gender of the pairings.' p.15 Figure 10 error bars show SEM. | 报告了标准误、误差棒、部分 p 值与分布量，但缺少事前样本量依据/功效分析、正式效应量与 95%CI、所有主要分析的完整报告及多重性校正说明。 |
| F2 | 内部效度 | NA | — | 没有人类随机分配、分配隐藏、基线等价性、被试流向与损耗处理；这不是人类 RCT。LLM 内部效度威胁（污染、prompt 敏感）已在 A4/J6/J11 记录。 |
| F3 | 构念效度 | 0.5 | p.5 Table 1 reports validity rates; p.15 Figure 10 compares simulated ratings to human ratings from Christianson et al.; p.2 describes prompt validation to avoid p-hacking. | 报告了生成合法性（validity rate）和与人类数据的同范式比较，提供了一定构念效度证据；但缺少测量信度、正式 manipulation check、以及单一操作化局限的系统论证。 |
| F4 | 外部效度 | 0.5 | p.5–6: surnames from U.S. 2010 Census, 100 names from each of five racial groups, 1,000-name pool; p.9 discusses risks and future larger systematic simulations. | 报告了模拟样本来源和人口学构造（姓名/种族/性别标题），并讨论部分限制；但未系统说明抽样代表性、推广边界条件及跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.4: k-choice prompt validity rate 'reflects the fractions of completions'; p.6: '10,000 name pairs'; p.7: Pearson correlations across name pairs; p.15: error bars across per-sentence averages. | 说明了 prompt/模拟记录/姓名对等分析层面，并在名称对与句子层面聚合；但没有明确处理姓名、句子、题目与被试式记录之间的嵌套/聚集结构，也未使用多层模型。 |
| G2 | 随机效应 | 0.5 | p.5–6: 1,000-name pool and balanced 10,000 name pairs; p.7: correlations of acceptance probability for name pairings across offers; p.9: discusses simulating populations. | 姓名被当作来自更大总体的模拟被试样本来使用并做聚合，但统计模型未报告随机效应（如 name/race random intercepts）；只能算部分体现了可推广到姓名总体的意图。 |
| G3 | 材料作为随机效应 | 0.5 | p.15: '24 garden path sentences compiled by Christianson et al.' and 24 control sentences plus authored sentences; p.15 Figure 10 groups across sentences with SEM; p.18: 10 WOC questions. | 使用了多句/多题材料并按句子/题目聚合、报告误差棒，但没有把材料/项目作为随机效应（无 item random effect、无准 F/混合模型），因此材料总体推广不完整。 |
| G4 | 统计功效 | 0 | p.5: 'All rates have a standard error of less than 0.05%' is reported post hoc; no a priori power analysis or sample-size justification is given. | 没有设计阶段功效分析、目标功效、预期效应量来源或重复次数推导；仅有大样本生成与描述性标准误，不构成事前功效论证。 |
| G5 | 研究者自由度 | 0.5 | p.5 describes validity-rate criteria for acceptable generations; p.2 says prompts were tweaked 'without examining the experimental outcomes'; appendices report all sentences/questions/conditions and p.6 gives code URL. | 报告了生成合法性/排除标准和多数条件，并给出代码；但没有完整报告排除数量、样本量停止规则、全部因变量的探索/验证区分，也未明确是否存在中途追加或选择性分析。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or time-stamped analysis plan appears in the paper. p.2 only says they avoided 'p-hacking' by not examining outcomes during prompt validation. | 无预注册；虽提到避免 p-hacking，但没有在数据收集前公开主要假设、样本量/停止规则、排除规则和分析计划。 |
| J1 | 位置偏差 | 0 | p.4 describes k-choice prompts with completions c1...ck; p.6 Figure 3 fixes 'accept' vs 'reject'; p.29 uses 'did shock' vs 'did not shock' and 'did stop' vs 'did not stop'. | 涉及多项选择/二选一判断，但完全没有报告候选项位置反平衡、A/B 交换或位置正确率/翻转率；直接使用固定选项顺序。 |
| J2 | 冗长偏差 | NA | — | 研究不涉及对开放生成长短质量进行 LLM-as-judge 的成对比较；Milgram 自由生成仅被分类为是否 shock/stop，不是按长度评质量。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或纠错式对话；不存在谄媚/sycophancy 操纵与测量。 |
| J4 | 自我偏好 | 0 | p.20: 'this classification is also accomplished by querying the LM... the LM is effectively also playing the role of an experimenter'; p.22: 'Italicized text is generated by GPT-3, and GPT-3 is also used to make decisions'. | Milgram 中使用同一模型既生成又分类/裁判，未使用异源陪审团、匿名化或人类金标准，也未量化自我偏好/同源偏差风险，属于被评模型自身作为唯一裁判的危险做法。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.2: 'the TE should be zero-shot, meaning that neither the procedure nor any training data... include prior data specific to that experiment.' | 研究明确采用 zero-shot prompt，没有 few-shot in-context examples 选择/排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.2: 'tweaking of prompts without examining the experimental outcomes'; p.5: 'LMs are highly sensitive to prompt wording'; full prompt examples and templates are in Figures 3, 6, 14 and pp.27–33. | 提供了大量完整 prompt 模板并讨论 prompt 敏感性，但没有系统报告 prompt 版本号、语义等价措辞的敏感性消融、prompt 搜索过程或 dev/test 划分，因此只部分满足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是长文档/RAG 信息位置实验；Milgram 记录随阶段增长，但研究没有操纵关键信息在长上下文中的首/中/尾位置并报告位置×正确率。 |
| J8 | 温度与采样随机性 | 0.5 | p.5: 'the natural temperature = 1 and top p = 1 parameters are used'; p.5 describes k-choice probability computation; p.7 uses simulations over 10,000 name pairs; p.5 Table 1 gives SE <0.05%. | 报告了 temperature 与 top-p，并进行了大量模拟/概率计算；但没有报告随机种子、top-k、重复抽样 N 与 bootstrap 95%CI、闭源 API snapshot 日期，随机性控制不完整。 |
| J9 | 重复与文本退化 | 0.5 | p.5: temperature=1 and top_p=1 sampling; p.5 Table 1 reports validity rates; p.20 describes extracting the first sentence via regex before classification. | 报告了基本解码策略和有效性 QC，但没有报告 repetition penalty、n-gram 重复率/退化率、生成长度上限或截断比例，也未证明各条件解码策略严格恒定。 |
| J10 | 分词效应 | NA | — | 全部材料为英语单语言、单脚本，没有跨语言/跨脚本比较，因此分词效率混淆不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.2: 'the TE should be zero-shot... otherwise the model may simply repeat the prior data'; p.9: 'the models have almost certainly been trained on data that includes descriptions of these experiments... we created three artificial variations of TEs.' | 明确识别训练数据污染并部分用新编 material/scenario 控制，但没有报告模型训练截止日期与测试集版本对照，也没有 n-gram/DCQ 等污染检测或污染率。 |
| J12 | 基准饱和 | 0.5 | p.9: 'hyper-accuracy distortion... median of 1.0 with 0.0 IQR'; Figure 8 plots normalized estimates and quartiles; p.19 Table 3 reports medians/IQR and truth values. | WOC 任务出现明显天花板式饱和，作者识别 hyper-accuracy 并改用归一化连续估计与 IQR 展示；但没有报告模型间 bootstrap CI/配对比较，也未系统用更难子集检验是否仍有区分度。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；只报告格式合法性/有效生成率，相关格式问题归入 J14。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.5 Table 1: 'Valid percentage generation rates'; p.18: 'Valid completions must be integers (commas and spaces are ignored)'; p.20: 'first sentence was extracted using regex'. | 报告了格式约束/合法率与部分归一化规则（整数、忽略逗号空格、regex 取首句），但未报告文法引导/JSON mode 等结构化输出设置、重试策略，也未把格式失败与内容错误完全分开。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估；Milgram 是模拟经典心理学实验，不是对模型有害请求拒绝率的测试。 |
| J16 | LLM 作为被试的范式定位 | 1 | p.1 Abstract: 'evaluating to what extent a given language model... can simulate different aspects of human behavior'; p.2: 'A replication TE is for replicating a finding in prior human subject research'; p.9 discusses distortions and limitations. | 论文核心就是 LLM 作为人类被试模拟的范式定位：明确说明模拟/复现人类构念、与人类同名现象比较、报告模型版本（text-davinci-003、gpt-35-turbo、gpt-4 等），并讨论不能直接外推人类心理结论的 distortion/限制。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文比较不同模型并发现更大/更对齐模型更准确或出现 hyper-accuracy，但没有宣称“涌现/突变”能力曲线，也没有做连续指标与多 seed 的涌现争议分析，故该组件不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究是纯评估/复现，没有以 benchmark、奖励模型或 LLM judge 为优化目标进行训练/RL/best-of-N 优化，无代理指标过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 lists exact model names (text-ada-001 through gpt-4); p.5 Table 1 reports standard errors; p.6 gives code URL; p.5 reports temperature/top-p. | 提供了模型版本名、样本规模/标准误和代码，但缺少精确 API snapshot 日期/版本字符串、随机种子、每分数重复 N 与 95%CI、模型间配对检验及原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究没有用户–模型多轮对话或轮次一致性评估；Milgram 是固定协议的多阶段模拟记录，不是对话式多轮实验，故不按 J20 编码。 |

## 编码小结
该文核心贡献是提出并演示用 LLM 模拟人类被试并复现人类研究，操作化与 prompt/材料报告较充分，且对训练数据污染做了部分新颖条件控制。主要不足是：温度/seed/重复抽样与置信区间报告不完整，prompt 敏感性未系统消融，部分判断用同一 LLM 作分类/裁判且未控制自我偏好，位置偏差与基准饱和/污染控制不充分。由于没有人类被试分配、顺序平衡、盲法等设计，B/C/D/E 等大量人类实验设计组件记 NA；但 LLM 条件、prompt、材料、采样与评估组件按实际分析单位编码。
