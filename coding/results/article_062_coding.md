# article_062 | GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers | 2024

研究类型概述：基准构建与LLM评测研究：以GSM8K为基础，用GPT-4生成并由人工修订八类数学题扰动，构建GSM-Plus（10,552题），在25个LLM与4类提示方法上比较原始题与扰动题准确率，并用PDR、ASP衡量稳健性。分析单位为模型—题目/题目变体对的评测结果，不是人类被试实验。
- **研究构念（Construct）**：稳健数学推理与捷径/启发式依赖（robust mathematical reasoning versus shortcut/heuristic reliance）｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：基准构建与LLM评测研究：以GSM8K为基础，用GPT-4生成并由人工修订八类数学题扰动，构建GSM-Plus（10,552题），在25个LLM与4类提示方法上比较原始题与扰动题准确率，并用PDR、ASP衡量稳健性。分析单位为模型—题目/题目变体对的评测结果，不是人类被试实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.2: 'we identify 5 perspectives... eight variations for each question'; p.3 Table 2 lists eight perturbation types; p.4: 'all question variations and answers produced by GPT-4 are further refined by human annotators'. | 扰动类型作为核心自变量被明确命名，并给出五个视角与八个水平/取值及生成修订程序；但缺少正式的单位分配说明与操纵检验（仅有题项通过率/人工校验），故为部分满足。 |
| A2 | 因变量 | 0.5 | p.4: PDR and ASP formulas; p.5: accuracy table with GSM8K vs GSM-Plus; p.15: human baseline accuracy. | 因变量指标（准确率、PDR、ASP）与计分方式有明确定义，准确率为百分比；但未报告测量信度、效度证据或连续指标预处理/天花板地板控制，故为部分满足。 |
| A3 | 控制变量 | 0.5 | p.5: 'The decoding temperature is set to 0 for deterministic predictions. Open-source base models are inferred using 8 demonstrations.' | 报告了温度=0与开源基础模型8-shot等控制手段，但没有系统列出控制变量清单并逐一说明控制方式，故为部分满足。 |
| A4 | 混淆变量 | 0.5 | p.4: 'we further analyze the potential preference bias that may be introduced towards question variations' and Table 3 compares GPT-4 on self-generated vs human-corrected questions. | 识别并检验了GPT-4自生成题目可能带来的偏好偏差；但没有系统讨论其他残余混淆（如数据污染、提示选择）及内部效度威胁，故为部分满足。 |
| A5 | 调节变量 | NA | — | 全文没有正式的调节变量假设或交互项检验；模型规模、SFT类型与扰动类型的比较是描述性分组，不构成调节分析。 |
| A6 | 中介变量 | NA | — | 全文没有中介变量、直接/间接效应分解或因果链中介假设。 |
| A7 | 操作性定义 | 1 | p.3-4: eight perturbation definitions and GPT-4 rewriting plus human correction; p.4: PDR/ASP equations; p.5: exact-answer accuracy and human baseline; p.21: critical-thinking answer extraction expressions. | 关键构念（稳健数学推理）与八类扰动的操作化、题目生成/修订流程、准确率与PDR/ASP计分均有可复现描述。 |
| A8 | 水平数与类型 | 0.5 | p.2: 'we create eight variations'; p.3 Table 2 and p.14 Table 6 list eight named perturbation categories. | 报告了核心自变量的水平数与各水平标签/定义；扰动类型为名义分类变量，但未明确写出类型、水平间距与全距，故为部分满足。 |
| A9 | 单一操作化的风险 | 0.5 | p.2: eight perturbations from five perspectives; p.9 Limitations: 'we do not investigate the accuracy of solution chains' and 'does not investigate the underlying reasons'. | 用多种扰动与两个稳健性指标考察构念，但核心测量仍主要是最终答案准确率；局限部分仅简要提到未研究解题链和失败原因，未充分展开单一操作化的推广边界。 |
| A10 | 单一方法的风险 | NA | — | 自变量为题目扰动/模型/提示方法，因变量为客观答案正确率；不存在自陈式同源测量或共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 研究不是人类被试间实验；每个模型对同一批题目/变体进行评测，没有把人类或LLM单位分配到互斥实验组。 |
| B2 | 被试内设计 | NA | — | 同一模型回答所有题目变体属于基准评测的题目内重复，但各题独立作答、无人类被试重复测量顺序问题；不按被试内设计编码。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合实验设计，也没有对应混合模型或两类误差项。 |
| B4 | 因子设计 | NA | — | 不是完整交叉的因子实验；模型、扰动、提示方式仅作基准评测比较，未报告设计矩阵、每格样本量与交互ANOVA。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有交互项统计检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 没有区组变量、划分依据或区内随机分配。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 属于基准构建/评测，不是准实验因果设计；未声称随机分配或准实验因果效应。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及人类被试内处理的适用条件论证。 |
| C1 | 随机化 | NA | — | 没有把单位随机分配到处理条件的程序；所有模型均在同一基准题目上评测，属于基准观察性比较。 |
| C2 | 平衡 | NA | — | 无人类条件顺序需要平衡；各题目/变体独立评测。 |
| C3 | 恒定 | 0.5 | p.5: 'The decoding temperature is set to 0 for deterministic predictions. Open-source base models are inferred using 8 demonstrations.' | 报告了温度与shot数等恒定设置，但未列出完整恒定变量清单，也未讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配程序或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计分析。 |
| C6 | 盲法 | NA | — | 没有人类被试/评分者条件盲法设计；人工标注用于数据校验而非实验条件比较。 |
| C7 | 平衡的层级 | NA | — | 没有顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | LLM各题独立作答，且无跨条件上下文内学习设计；不涉及人类练习效应。 |
| D2 | 疲劳效应 | NA | — | LLM评测不涉及人类session疲劳；论文也未以人类被试进行长时重复测量。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各题目/变体评测相互独立，无跨条件清洗期或残留效应问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件迁移或迁移对称性检验。 |
| D5 | 范围效应 | NA | — | 因变量为客观答案正确率，不是量表式绝对判断，无范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 任务不是多选项选择、排序或序列刺激呈现；题目变体顺序不影响独立作答结果。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 不是人类被试实验，不涉及掩饰情节或事后推断研究假设；人工标注任务不是需求特征敏感的实验参与。 |
| E5 | 实验者效应 | NA | — | LLM评测为自动化流程，不涉及人类主试/评分者期望传递；人工标注主要用于数据质量校验。 |
| E6 | 天花板 / 地板效应 | 0 | p.5 Table 4 reports only accuracy percentages for models/human; p.1 mentions GSM8K scores >90%/>80% but no main-DV SD, skew, or endpoint frequencies are reported. | 准确率是有界因变量，存在天花板/地板风险；论文仅报告均值表，未报告标准差、偏度或端点频率，也未说明难度校准，故核心报告缺失。 |
| E7 | 共同方法偏差 | NA | — | 自变量为题目扰动、因变量为客观答案正确率，不存在自评式同源测量与共同方法偏差。 |
| F1 | 统计结论效度 | 0.5 | p.4: PDR/ASP definitions; p.5 Table 4 reports accuracy and PDR/ASP for all models; no confidence intervals or significance tests are reported. | 报告了PDR、ASP等效应型指标与所有主要模型结果，但没有样本量确定依据、置信区间、多重性校正或推断统计检验，故为部分满足。 |
| F2 | 内部效度 | NA | — | 这是基准评测而非随机分配因果实验；论文未主张随机分配因果效应，内部效度实验组件不适用。 |
| F3 | 构念效度 | 0.5 | p.4: 10% variations cross-annotated with '90.02%' inter-annotation consistency; p.14 Table 7 reports human pass rates and Krippendorff alpha 0.567; p.5 human baseline. | 报告了人工标注一致性和扰动通过率，提供了一定的构念/数据质量证据；但缺少正式的测量效度论证与操纵检验体系，故为部分满足。 |
| F4 | 外部效度 | 0.5 | p.5: 25 LLMs and human annotators; p.9 Limitations: only elementary school math, not other education levels, and not solution-chain accuracy. | 报告了模型样本与人类基线来源，并在局限中说明只覆盖小学水平；但未系统讨论模型/题目样本代表性和跨情境复现，故为部分满足。 |
| G1 | 分析单位 | 0.5 | p.2: 1,319 GSM8K questions with eight variations; p.4 metrics over datasets; p.5 model-level accuracy aggregated across questions. | 说明了题目/变体与模型评测的分析单位，但未处理八类变体嵌套于种子题目的聚集结构，也未用多层模型；为部分满足。 |
| G2 | 随机效应 | NA | — | 没有人类被试或跨材料混合模型的随机效应结构；模型为固定基准列表，不是从模型总体随机抽样的被试样本。 |
| G3 | 材料作为随机效应 | 0 | p.2: 'the 1,319 test questions from GSM8K' and eight variations each; p.4: metrics aggregated over fixed dataset; no item random effect or F′/mixed model. | 数学题目作为固定测试材料处理，未把题目/材料视为从更大材料总体抽样并纳入随机效应；结论容易从固定题集外推到一般数学推理，故核心做法缺失。 |
| G4 | 统计功效 | 0 | p.5 and p.9 report model comparisons and limitations but no a priori power analysis, target effect size, or confidence intervals. | 无设计阶段功效分析或样本量/重复次数论证，结果也未报告置信区间，仅报告点估计。 |
| G5 | 研究者自由度 | 0.5 | p.5 lists 25 models and 4 prompting techniques; p.8 uses a random subset of 120 seed questions and 960 variations; p.9 limitations acknowledge scope limits. | 报告了大部分模型、条件与子集选择，但未完整说明样本量决定、所有可能的排除/停止规则，也未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | 全文（pp.1–24）未报告预注册平台、注册编号、预注册假设或分析计划。 | 没有公开预注册，也未区分预注册验证性分析与事后探索性分析，故为0。 |
| J1 | 位置偏差 | NA | — | 研究不做多候选项选择、排序或LLM-as-judge成对比较；正确答案是开放式最终数值/表达式，无候选位置偏差。 |
| J2 | 冗长偏差 | NA | — | 评估依据最终答案正确率，不是对开放生成文本作LLM裁判或长短质量比较；不存在长度被误当质量的评分环节。 |
| J3 | 谄媚 | NA | — | 任务输入不含用户先验立场或反馈纠错对话；未操纵pro-/anti-framing，不涉及谄媚测量。 |
| J4 | 自我偏好 | NA | — | 没有使用LLM-as-judge评估模型输出；GPT-4用于题目生成而非裁判，故J4不直接适用。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.5: 'Open-source base models are inferred using 8 demonstrations'; p.8: 'Complexity-based CoT and LTM use 8 and 1 in-context examples, respectively.' | 仅报告了few-shot数量，未说明示例来源、类别比例、排列反平衡、多seed重采样或完整示例模板；属于单次模板下信息不足。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.8: 'The full prompts are listed in Appendix C.4'; p.18-21 Examples C.9–C.14 give exact COMP prompts. | 公布了所提COMP方法的完整提示模板，但未报告prompt版本迭代、语义等价敏感性消融、dev/test划分或对标准CoT等提示的完整版本控制。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务输入为短篇小学数学题，不是长上下文/RAG实验，无中间迷失或信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.5: 'The decoding temperature is set to 0 for deterministic predictions'; p.9: 'COT + SC aggregates each answer by sampling 5 predictions'; p.9 Table 5 reports ensemble results. | 报告了温度=0与部分自洽采样N=5，但未报告top-p/top-k、随机种子、重复运行的置信区间或闭源API snapshot日期。 |
| J9 | 重复与文本退化 | 0.5 | p.5: temperature 0 for deterministic predictions; p.9: self-consistency samples 5 predictions; no repetition-penalty or degeneration-rate report. | 部分报告了解码策略（贪心/采样与SC），但未报告repetition penalty、n-gram重复率/退化率或截断比例，故为部分满足。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言、单脚本数学评测，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.1 mentions the debate about models possibly performing due to 'training data leakage'; p.5 lists model names and evaluation setup but reports no training cutoff comparison or contamination detection. | 虽在引言提到数据泄漏风险，但没有做测试集与训练截止日期对照、n-gram重叠/DCQ等污染检测，也未报告污染率，故核心检查缺失。 |
| J12 | 基准饱和 | 0.5 | p.1: 'GPT-4 and cutting-edge open-source models have reported accuracy rates exceeding 90% and 80%' on GSM8K; p.2: GSM-Plus has 10,552 harder variations. | 识别到GSM8K接近饱和并构建更难扰动集，报告了当前水位与量程；但未使用连续指标、bootstrap CI或更难held-out子集作饱和后的统计比较。 |
| J13 | 指令遵循 | NA | — | 因变量是数学答案正确率，不是指令遵循测量；无否定/数量/格式/风格约束的指令遵循指标。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.13 Example B.2: 'Use the format #### [value]'; p.21: critical-thinking answer extraction uses a list of acceptable expressions. | 报告了最终答案格式要求与部分提取规则，但未报告格式合法率、重试策略，也未将格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 研究是数学能力基准，不涉及有害请求、越狱或安全对齐评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文定位为NLP数学推理能力基准，不主张把LLM作为心理学/认知科学被试来测量人类同名心理构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文比较不同规模模型的表现，但没有报告训练进展/规模能力曲线，也没有宣称涌现或相变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 纯基准评估，没有以benchmark/reward model/LLM-judge为优化目标进行训练、RL或best-of-N优化，故不涉及奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.5 lists model names and temperature 0; p.4-5 report single aggregate accuracy scores without confidence intervals, repeated runs, exact snapshot/commit hash, or paired tests. | 缺少重复次数、95%置信区间、精确模型snapshot标识和配对检验；仅报告单点分数，故评估可复现性报告不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮题目作答，没有多轮对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
该文是较完整的LLM数学推理稳健性基准与评测论文，清楚定义了八类扰动、数据构建流程、准确率/PDR/ASP指标与人工校验；但作为基准评测，缺少统计不确定性报告、基准污染检测、精确模型快照/重复运行信息、few-shot示例来源与顺序控制等。A-G中的许多人类实验设计组件不适用于该研究；LLM评测相关的J组件中，J11、J19明显不足，J5、J8、J9、J14等仅有部分信息。
