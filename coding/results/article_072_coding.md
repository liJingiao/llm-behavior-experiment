# article_072 | MISGENDERED: Limits of Large Language Models in Understanding Pronouns | 2023

研究类型概述：本文是面向LLM的代词预测/误性别基准评测研究。研究构造模板化数据集，通过受限解码让多种自回归与掩码语言模型在给定代词声明后预测缺失代词，并比较代词类型、代词形式、声明类型、声明数量、模型规模及few-shot设置下的准确率。研究无人类被试，分析单位为模型在评测实例/条件上的聚合表现。
- **研究构念（Construct）**：代词理解、非二元代词泛化与社会语言偏见（social-language behavior and pronoun generalization/bias）｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）；刻板印象（stereotypes, `trm_4a3fd79d0b285`）
- **实验任务与范式（Task / Paradigm）**：本文是面向LLM的代词预测/误性别基准评测研究。研究构造模板化数据集，通过受限解码让多种自回归与掩码语言模型在给定代词声明后预测缺失代词，并比较代词类型、代词形式、声明类型、声明数量、模型规模及few-shot设置下的准确率。研究无人类被试，分析单位为模型在评测实例/条件上的聚合表现。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: 'We use two different declaration types and seven combinations of declared forms'; p.4-5 and Table 1/Table 2 specify pronoun types, forms, declaration types and numbers; p.5-6 describe direct prompting and in-context learning. | 研究确实界定了多个受控输入条件及其水平，并说明如何构造实例；但没有操纵检验，也不是人类被试分配到条件。核心操纵/条件界定存在，但完整报告要件不足。 |
| A2 | 因变量 | 0.5 | p.4-5: each instance has a missing [PRONOUN], and 'yhat = arg min L(...)' over candidate pronouns; p.7 Table 4 reports 'Accuracy' by pronoun type; p.7 Fig. 3 reports 95% CI for size plots. | 因变量指标与计分方式明确为受限代词预测准确率，并部分给出置信区间；但未报告信度、效度或针对准确率端点/地板的系统处理说明。 |
| A3 | 控制变量 | 0.5 | p.4: 'we only use preferred pronouns from a single pronoun group'; p.4: names sampled from US Social Security/unisex lists; p.5: 'unified constrained decoding mechanism'. | 论文报告了若干保持恒定或统一处理的控制做法（单一pronoun group、同一模板体系、统一受限解码），但没有系统列出控制变量清单及逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | p.10 Limitations: 'the measurements can be sensitive to the choice of templates'; p.8 discusses memorization/name-pronoun associations as likely confounds. | 论文识别了模板选择、姓名关联等潜在混淆，并说明结果不应视为最终结论；但未系统控制这些混淆或报告敏感性分析。 |
| A5 | 调节变量 | NA | — | 全文没有明确调节变量假设，也未报告乘积项交互检验；模型规模、代词形式等只是描述性分组比较，不构成正式调节分析。 |
| A6 | 中介变量 | NA | — | 全文没有中介变量或中介效应假设，也没有直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.4-5: dataset construction, inputs/labels for masked and autoregressive models, constrained decoding formula; p.13 Appendix B gives a constrained decoding example; p.14 Appendix A lists all templates. | 关键构念被具体操作化为给定代词声明后预测缺失代词，模板、输入格式、候选标签与预测规则均可复现，达到操作化定义要求。 |
| A8 | 水平数与类型 | 0.5 | p.4 Table 1 lists 3 pronoun types, 11 pronoun groups and 5 forms; p.5 Table 2 lists declaration numbers 2-5; p.5 Table 3 lists model families and parameter counts; p.7 Fig. 3 plots size in billions. | 水平数与具体取值/标签报告较充分，但未明确标注各因素为名义/等级/连续，也未系统报告水平间距、全距或连续变量中心化处理。 |
| A9 | 单一操作化的风险 | 1 | p.4: 'We manually construct ten templates for each pronoun form'; p.10: 'measurements can be sensitive to the choice of templates ... findings should not be considered as the definitive verdict'. | 关键构念主要采用模板式准确率这一单一指标，但使用每个形式10个模板并在局限中明确讨论了模板敏感性与可推广性限制，符合单一操作化下的局限讨论要求。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈量表或同源自评设计，IV与DV不是共同方法偏差意义上的同源测量；共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配；所有模型在完整评测集上评估，不存在被试间条件分配，故被试间设计不适用。 |
| B2 | 被试内设计 | NA | — | 虽同一模型会在多个条件/实例上被评估，但这是基准评测而非带顺序呈现的重复测量实验；无被试内顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合设计或对应误差项需要编码。 |
| B4 | 因子设计 | 0 | p.6 Table 5 crosses pronoun type with declaration type; p.6 Table 6 crosses pronoun type with declaration number; p.7 Table 8 crosses pronoun type with pronoun form; p.7 Fig. 3 crosses model family/size with pronoun type. | 多因素条件已被交叉呈现，但论文主要报告聚合准确率，未给出完整设计矩阵/每格样本量，也未报告ANOVA式主效应与交互统计量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p.6 Table 4 reports average accuracy by pronoun type; p.6 Tables 5-6 and p.7 Table 8 report subgroup accuracies, but no F/df/p/effect-size tests are reported. | 在可视为多因素基准比较的设计中，主效应仅以描述性准确率呈现，缺少统计检验结果，未达到基本要件。 |
| B6 | 交互作用 | 0 | p.7: 'there seems to be an inverse correlation' between binary and neo-pronoun performance by form, but no interaction statistical test is reported. | 论文描述了一些交互样态，但没有对交互项作统计检验，也没有简单效应检验或误差棒图示，未达到基本要件。 |
| B7 | 区组设计 | NA | — | 研究未采用区组/分层随机设计，无区组变量与区内分配程序。 |
| B8 | 拉丁方 | NA | — | 研究未使用拉丁方顺序设计；基准实例不是按被试顺序呈现的条件序列。 |
| B9 | 准实验设计 | NA | — | 这不是准实验因果设计；模型比较和规模比较属于观测性基准分析，没有随机分配缺失但声称准实验因果效应的问题。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理条件序列，无需论证处理可逆性或迁移对称性。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥条件的随机化程序；所有模型在完整数据集上确定性评估，无分配隐藏问题。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件呈现顺序；基准实例独立评估。 |
| C3 | 恒定 | 0.5 | p.5: 'We use a unified constrained decoding mechanism' for masked and autoregressive models; p.5 Table 3 fixes model checkpoints/parameter counts by model name; p.10 limitations note English-only and Western conceptualization. | 论文报告了若干统一控制做法（统一解码、固定模型清单与参数规模、数据集模板），但没有系统列出所有保持恒定的环境/实现变量及其恒定水平。 |
| C4 | 匹配 | NA | — | 研究没有使用匹配或配对分配程序，无匹配变量、匹配后均衡性检验等问题。 |
| C5 | 纳入为变量 | NA | — | 研究未把混淆变量作为协变量或区组因素纳入统计模型；姓名关联等只作事后描述性分析，不存在协变量调整分析。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类被试、主试或评分者需要盲法。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序需要选择完全平衡、拉丁方或ABBA等平衡层级。 |
| D1 | 练习效应 | NA | — | 每个评测实例独立打分，不是同一被试在时间序列上接受练习/重复条件；无练习效应控制问题。 |
| D2 | 疲劳效应 | NA | — | 无人类session或疲劳相关的长时实验安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各评测实例独立，无跨条件清洗期或迁移效应问题。 |
| D4 | 不对称迁移 | NA | — | 不存在跨条件不对称迁移设计。 |
| D5 | 范围效应 | NA | — | 因变量为客观代词预测准确率，不是被试内绝对判断或量表评分，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 模型不是从按固定顺序呈现的多个选项中作答；候选代词通过受限标签集上的loss/argmin计算，不存在选项位置随机化或刺激顺序平衡问题。 |
| E2 | 默认赞同 | NA | — | 研究不使用Likert或态度自评量表，无反向计分与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也没有跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，因此不存在需求特征或事后假设推断检查。 |
| E5 | 实验者效应 | NA | — | 数据收集完全自动化，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Table 4 reports accuracy by pronoun type (Binary 75.3, Neutral 31.0, Neo-Pronouns 7.6); p.7 Fig. 3 reports 95% CIs; p.9 discusses poor performance. | 论文报告了主要准确率均值及部分置信区间，可看出neo-pronoun接近地板；但没有报告端点频率、偏度或pilot难度校准过程，地板效应处理不完整。 |
| E7 | 共同方法偏差 | NA | — | 研究不是同源自陈式多构念测量，IV和DV也不是自评量表；共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.7 Fig. 3 reports '95% confidence interval' for model-size plots; p.6-7 Tables 4-8 report accuracy but no power analysis or multiplicity correction. | 部分结果报告了95% CI和准确率，但无样本量确定依据/功效分析，主表多数差异无推断统计与多重性校正，统计结论效度信息不完整。 |
| F2 | 内部效度 | NA | — | 该研究是基准评测与观察性模型比较，没有随机分配、分配隐藏或被试流向等人类实验内部效度程序，也未作强因果效应推断。 |
| F3 | 构念效度 | 0.5 | p.10 Limitations: 'measurements can be sensitive to the choice of templates'; p.10 also limits the construct to one type of misgendering and upstream evaluation. | 论文讨论了模板敏感性和构念边界，具有一定构念效度反思；但没有报告信度、效标/构念效度统计证据或操纵检验。 |
| F4 | 外部效度 | 0.5 | p.4 uses US first names from Social Security and unisex/female/male lists; p.10 Limitations: Western conception, English only, US names, no downstream applications, larger models not evaluated. | 样本/材料来源与推广边界有明确说明；但没有跨样本或跨情境复现结果，因此只给部分分。 |
| G1 | 分析单位 | 0.5 | p.4: dataset results in 'a total of 3.8 million instances'; p.6 reports accuracy aggregated over models/conditions; no hierarchical model or clustering adjustment is described. | 论文说明评测在实例层面进行并按条件聚合，但没有明确处理分配层级、分析层级及模板/姓名的嵌套结构。 |
| G2 | 随机效应 | NA | — | 研究未使用混合模型或随机效应结构；模型族/规模作为固定比较对象，不把LLM视为从总体抽样的被试样本，因此无随机效应结构可编码。 |
| G3 | 材料作为随机效应 | 0.5 | p.4: 'We manually construct ten templates for each pronoun form'; p.10 acknowledges results are sensitive to template choice, but no mixed model with item/template random effects is reported. | 材料被固定为有限模板集，分析中未把模板/姓名作为随机项目效应；不过论文在局限中明确承认模板敏感性，属部分满足。 |
| G4 | 统计功效 | 0 | p.6-7 report accuracies and p.7 Fig. 3 reports CIs, but no a priori power analysis, target effect size, or sample-size justification is reported. | 缺少事前功效分析或样本量论证；虽部分图有CI，但未达到G4基本要件。 |
| G5 | 研究者自由度 | 0.5 | p.4 describes 3.8M instances and all templates are in Appendix A; p.5-9 report multiple conditions and models. No explicit exclusion rules, stopping rule, or confirmatory/exploratory distinction is reported. | 条件与材料报告较完整，但缺少样本量决定方式、剔除/停止规则及验证性与探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration is mentioned in the main text or ACL checklist (p.15-16); no registered analysis plan or deviation discussion is provided. | 未报告数据收集前预注册、分析计划或预注册偏离说明。 |
| J1 | 位置偏差 | NA | — | 研究不涉及多项选择候选位置、排序或LLM-as-judge成对比较；代词候选概率由受限标签集的loss决定，无选项位置偏差问题。 |
| J2 | 冗长偏差 | NA | — | 评测输出为短代词而非开放式长文本生成，不涉及长度被误当质量的冗长偏差。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错对话操纵，谄媚偏差不适用。 |
| J4 | 自我偏好 | NA | — | 研究不使用LLM-as-judge或成对模型输出评比，无自我偏好偏差问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.6: in-context learning with '2,4,6, 10, and 20-shot settings using GPT-J-6B and OPT-6.7b'; examples are randomly sampled templates, names, and pronouns not in the evaluated instance. | 报告了few-shot示例来源、shot数与部分采样规则；但未报告标签比例、示例排列反平衡、多seed均值/方差或完整提示模板。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5 describes input formatting and constrained decoding; p.14 Appendix A provides full templates and Table 14; p.10 acknowledges template sensitivity. | 提供了较完整模板和输入构造方式，但没有prompt版本号、语义等价措辞敏感性消融、dev/test划分或prompt搜索过程说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 输入为短句加代词声明，上下文远低于长窗口/RAG设置，不涉及长上下文信息位置效应。 |
| J8 | 温度与采样随机性 | NA | p.5: predictions are obtained by 'yhat = arg min L(...)' over constrained label sets, not by stochastic text sampling. | 使用候选标签序列loss的argmin进行确定性受限预测，不涉及temperature/top-p采样随机性。 |
| J9 | 重复与文本退化 | NA | — | 任务输出为单个短代词，不涉及开放式生成重复与文本退化问题。 |
| J10 | 分词效应 | NA | — | 研究限定英语单语言、单脚本，无跨语言/跨脚本分词长度比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.8 Table 11 reports pronoun counts in C4, OpenWebText, and Pile, and p.8 discusses memorized name-pronoun associations, but no model training cutoff, test-set overlap check, or contamination rate is reported. | 论文分析了预训练语料中代词频次，但没有对照测试集版本与训练截止日期，也未做污染检测。由于是新建模板数据集但未证明未见于训练语料，按不完整/缺失编码为0。 |
| J12 | 基准饱和 | NA | — | 该基准分数远未接近天花板（如neo-pronoun平均7.6%），主要问题是低分/地板而非饱和；不适用基准饱和风险。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，也没有约束类型准确率拆分。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 研究不使用结构化JSON/文法约束输出合规率作为指标；受限解码只是候选代词集合上的预测，不是格式合规评测。 |
| J15 | 越狱稳健性 | NA | — | 研究关注误性别/代词偏差，不涉及越狱攻击或安全对齐评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 本文是NLP偏见/能力基准评测，不主张在LLM上测量人类心理学构念，也未做人类-LLM同名构念对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文报告模型规模与准确率关系，但明确称未观察到一致的scaling原则，没有宣称涌现或突变，不适用涌现指标假象争议。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及以benchmark/奖励模型/LLM-judge为优化目标的训练或best-of-N优化，无代理指标过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 Table 3 lists model names and parameter counts; p.7 Fig. 3 reports 95% CIs; code/dataset are released. No exact model snapshot dates/commit hashes or paired model comparisons are reported. | 有部分可复现信息（模型清单、数据/代码、部分CI），但缺少精确snapshot标识、重复采样次数说明和配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮短句代词预测，无多轮对话历史累积或多轮一致性衰减问题。 |

## 编码小结
该文清晰报告了数据集构造、条件水平、模型清单与受限解码指标，但其主体是描述性基准评测，未进行正式实验操纵检验、推断性主效应/交互检验、随机化/顺序平衡、预注册或功效分析；许多人类实验特有的质控组件不适用。总体信息透明度较高，但多数推断与质控项只能给部分分或按不适用处理。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
