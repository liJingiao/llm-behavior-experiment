# article_118 | Bias in Language Models: Beyond Trick Tests and Towards RUTEd Evaluation | 2025

研究类型概述：LLM偏差评测方法研究：系统比较标准短文本偏差基准与三类长文本RUTEd任务，在九个LLM、三种偏差指标、40个职业及多套提示模板上计算偏差量并做相关/稳健性分析。不是人类被试实验，分析单位为模型×情境×指标×职业×重复生成层面的评测分数。
- **研究构念（Construct）**：应用情境依赖的性别—职业联结偏差｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：LLM偏差评测方法研究：系统比较标准短文本偏差基准与三类长文本RUTEd任务，在九个LLM、三种偏差指标、40个职业及多套提示模板上计算偏差量并做相关/稳健性分析。不是人类被试实验，分析单位为模型×情境×指标×职业×重复生成层面的评测分数。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.4: “we test nine LLMs” and “compare it with three long-form text generation tasks”; PDF p.5-6 gives exact prompts and max token lengths for each task. | 评测情境/模型/指标可视为设计因素，水平与提示程序有报告；但无随机分配或操纵检验，且不是人类被试实验。 |
| A2 | 因变量 | 0.5 | PDF p.6: defines neutrality, skew, stereotype formulas using normalized probabilities; PDF p.7 gives sampling variance and 95% CI approach. | 因变量指标与计分方式明确，且有抽样方差/CI；但无传统信度、效度证据及反应时类连续指标预处理说明。 |
| A3 | 控制变量 | 0.5 | PDF p.6: “Models were set to default temperature with no minimum token probability and with the aforementioned maximum tokens”; n=30 or 64 replicates. | 报告了部分控制设置（温度默认、无最小token概率、最大长度、重复次数），但不系统，且未给出温度具体值。 |
| A4 | 混淆变量 | 0.5 | PDF p.9: “Mode collapse ... could distort bias estimates” and reports a check; PDF p.9: tests 10 standard and 30 RUTEd prompt templates. | 识别并检查了模式崩溃与提示措辞两个潜在威胁；但未系统列出全部残余混淆或做形式化敏感性分析。 |
| A5 | 调节变量 | NA | — | 研究没有调节变量理论模型或交互检验，属于评测相关性/稳健性分析。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量假设与直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | PDF p.4-6: exact template prompts for decontextualized, Bedtime Stories, User Personas, ESL; PDF p.6: definitions for pronoun classification and three metric formulas. | 关键构念均有可复现操作化：任务提示、最大长度、重复生成、性别代词归类与指标公式。 |
| A8 | 水平数与类型 | 0.5 | PDF p.6: model levels include Llama-2 7/13/70B, Flan-PaLM XS/S/M/L, GPT-4-0125-preview, Mixtral-8x7B; PDF p.4: four evaluation contexts. | 报告了主要水平与标签，但未系统说明水平类型、间距/全距或连续变量中心化处理。 |
| A9 | 单一操作化的风险 | 1 | PDF p.1 abstract: “three contexts of real-world use”; PDF p.9: prompt variation robustness; PDF p.10: limitations on gender-occupation and binary gender. | 使用多情境、多指标和多提示模板操作化偏差，并讨论了单一情境/职业限制与可推广性边界。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈式测量，IV/DV同源问题不按共同方法偏差处理；所有偏差均由模型生成文本计算，属于评测设计本身。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组分配；模型/情境为固定评测条件。 |
| B2 | 被试内设计 | NA | — | 同一模型跨任务重复评测，但每次生成是独立API调用，无人类被试内顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合实验设计及相应误差项分析。 |
| B4 | 因子设计 | NA | — | 虽有多模型×多情境×多指标结构，但不是因子实验，未用ANOVA报告主效应/交互；不按B4编码。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有交互项统计检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无被试内条件顺序设计，故无拉丁方。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计；模型比较为固定目标评测，无随机分配需求。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 研究单位没有被随机分配到互斥处理；模型、任务和提示由设计固定。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件呈现顺序。 |
| C3 | 恒定 | 0.5 | PDF p.6: fixed max token lengths for each context and “default temperature with no minimum token probability”; PDF p.10 discusses limitations of prompt/style generality. | 列出了若干恒定设置及水平，但温度和部分解码设置不够具体；外部效度限制有讨论但不系统。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为协变量/区组纳入统计模型；职业分层是描述性稳健性检查。 |
| C6 | 盲法 | NA | — | 数据采集和指标计算完全自动化，无人类被试/评分者盲法问题。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM各次生成独立、无上下文内学习或练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类被试疲劳或长session问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每次生成独立，无跨条件残留/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉条件，不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 不使用主观量表绝对判断；偏差指标为文本统计量。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多候选项/刺激序列的被试内呈现；性别词集合概率求和，顺序不影响指标。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表，不涉及默认赞同。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，故无需求特征或事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 实验者效应不适用：生成和评分自动化，无人类主试/评分者。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.8 Figure 1 reports 102 bias quantities with 95% CIs; PDF p.7 gives sampling variance formulas. | 报告了均值与置信区间，可部分观察端点风险；但未系统报告偏度、端点频率或任务难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无人类同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | PDF p.7 Table 1 reports Spearman rank correlations; PDF p.8 Figure 1 includes 95% CIs; PDF p.6 reports n=30/64 replicates. | 报告了效应量（相关）和部分CI/样本重复数；但无功效分析、无多重比较校正说明，部分假设检验信息不完整。 |
| F2 | 内部效度 | NA | — | 非随机实验且主要作预测相关性/评测比较，不主张因果效应；随机分配、分配隐藏、基线等内部效度组件不适用。 |
| F3 | 构念效度 | 0.5 | PDF p.6: metric formulas and operational definitions; PDF p.10: limitations on construct scope and binary gender restriction. | 构念操作化与内容对应有讨论，但无工具信度（如α/重测）或正式效度检验，也无操纵检验。 |
| F4 | 外部效度 | 0.5 | PDF p.6: nine models from four families; PDF p.10: limitations on gender-occupation, gender binary, occupations and prompts; PDF p.9: prompt robustness. | 报告了模型来源、任务情境与推广边界，并做提示稳健性检查；但模型并非总体代表样本，跨样本/跨情境复现有限。 |
| G1 | 分析单位 | 0.5 | PDF p.6: “n = 30 replicates per task and occupation” and n=64 for Flan-PaLM; PDF p.7: sampling variance formula aggregates over occupations. | 说明了重复生成与职业层级的计算，但未明确处理生成嵌套于职业/模型的层级结构，主要用聚合与解析方差。 |
| G2 | 随机效应 | NA | — | 模型是固定评测目标而非从模型总体抽样的随机效应；无人类被试随机效应需求。 |
| G3 | 材料作为随机效应 | 0.5 | PDF p.4: uses “20 female-majority occupations and 20 male-majority occupations from WinoBias”; PDF p.10: limitations include “certain occupations”. | 职业材料为固定40项，未纳入项目随机效应或准F/混合模型；但论文承认职业范围限制。 |
| G4 | 统计功效 | 0.5 | PDF p.6: n=30 or 64 replicates; PDF p.7: cites binomial normality rule of thumb and reports sampling variance/CI. | 有基于正态近似的重复次数/精度论证并报告CI，但无正式功效分析或预期效应量来源。 |
| G5 | 研究者自由度 | 1 | PDF p.9-10: reports 102 quantities from 108 possible and explains missing model-metric combinations; PDF p.6: “Replicates with no such pronouns are dropped”; PDF p.14 labels occupational analysis as exploratory. | 报告了排除规则、全部主要指标/条件、缺失原因，并区分了零星探索性分析与主分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–26 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未提及预注册、注册平台/编号或数据收集前分析计划；按口径记0。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或LLM-as-judge成对比较；候选位置偏差不适用。 |
| J2 | 冗长偏差 | NA | — | 不使用LLM裁判评估生成质量，也不比较开放生成长度与得分。 |
| J3 | 谄媚 | NA | — | 没有用户立场/反馈/纠错对话，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 不使用LLM-as-judge，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 任务提示为零样本生成/下一词概率，无few-shot in-context示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.9: “10 standard benchmark prompt templates ... and 30 RUTEd prompt templates”; PDF p.18-21 Tables B1-B3 provide full templates; Appendix B reports robustness correlations. | 提供完整模板并做提示敏感性消融；但无版本号/迭代日期，也未说明dev/test分离。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG设置；最大生成长度1000 tokens，非长上下文信息位置实验。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.6: “default temperature with no minimum token probability”; n=30/64 replicates; PDF p.8 Figure 1 has 95% CIs; GPT-4-0125-preview is named. | 报告了温度默认、重复次数和部分模型snapshot，并有CI；但未给出top-p/top-k/seed等完整采样参数及精确API日期。 |
| J9 | 重复与文本退化 | 0.5 | PDF p.9: mode-collapse check on 10,800 Llama-2 replicates using cosine similarity and manual inspection; PDF p.6: default temperature and max tokens. | 报告了解码方式概要并检查模式崩溃/退化；但无repetition penalty、n-gram重复率或截断比例等完整QC指标。 |
| J10 | 分词效应 | NA | — | 单语言英语、单脚本，无跨语言/跨格式tokenization比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.4 uses BIG-bench Gender Sensitivity and WinoBias; PDF p.6 names model families; no training cutoff or contamination analysis is reported. | 未报告测试集版本与模型训练截止日期对照，也未做污染检测；公开基准分数被直接用于比较。 |
| J12 | 基准饱和 | 0 | PDF p.7-8 reports correlations and Figure 1 metrics; no benchmark score range, SOTA ceiling, or saturation analysis is discussed. | 未报告基准饱和检查或当前水位；未改用连续/更难子集以排除饱和导致的微小差异。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；任务是偏差文本生成/下一词概率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化输出或语法约束输出；生成文本后统计代词/词概率。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或对抗攻击评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究为LLM偏差基准评测，不主张把LLM作为心理学/认知科学被试测量人类同名构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较Llama-2与Flan-PaLM不同规模，但未报告随规模/训练进展的能力曲线，也不宣称涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N或对代理指标的优化过程；仅为基准评测。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.6 reports n=30/64 and model names including GPT-4-0125-preview; PDF p.7-8 reports sampling variance and 95% CIs; no paired model comparison test is reported. | 报告了重复次数、CI和部分模型标识；但缺少所有模型的精确snapshot/API日期、原始日志/提示集发布及配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示生成/概率评测，无多轮对话历史累积。 |

## 编码小结
论文清楚报告了评测任务、提示、偏差指标公式、重复次数与部分模型版本，并做了提示变异、模式崩溃和职业分层等稳健性检查；但它不是人类被试实验，绝大多数被试分配、顺序平衡、盲法等组件不适用。LLM评测相关组件中，提示敏感性、采样重复、可复现性有部分报告，基准污染与饱和检查缺失。
