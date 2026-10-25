# article_190 | Open Models, Closed Minds? On Agents Capabilities in Mimicking Human Personalities through Open Large Language Models | 2025

研究类型概述：LLM-as-participant 的人格测评基准/观察性实验：以 12 个开源 LLM 为分析单位，使用 MBTI 与 BFI 测量其人格表达，并比较无条件、人格条件化、角色+人格条件化提示及温度设置下的结果。
- **研究构念（Construct）**：人格特质、人格条件化和社会角色对人格表达的影响｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；冲动性（impulsivity, `trm_50070dce14554`）；内部动机（intrinsic motivation, `trm_4a3fd79d0a6e8`）
- **实验任务与范式（Task / Paradigm）**：让12个现成开放模型回答MBTI和BFI问卷，随后加入特定人格或职业角色提示，比较测得人格是否按目标方向改变。（比较模型家族、无条件基线、目标人格提示、职业角色提示和角色加人格联合提示。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3 'we devised three prompting strategies... system prompts designed to condition them to specific personalities'; p.4 'N = 30 independent repetitions... 12 × 2 × 16 × 30' | 人格/角色条件化及温度被明确操纵，水平数和提示程序有报告；但无操纵检验，条件分配与重复细节仅部分说明。 |
| A2 | 因变量 | 0.5 | p.2 MBTI 'set QMBTI of 60 questions' and options; p.3 BFI '44 questions' and options; p.6 Table 3 reports accuracy ± SD | 因变量指标与计分基本界定；但未报告信度、效度、连续指标预处理或天花板/地板控制。 |
| A3 | 控制变量 | 0.5 | p.4 'we kept the top p and top k parameters at their default values of 50 and 1'; 'all our experiments locally... text-generation-webui' | 报告了部分恒定参数与部署环境，但未系统列出所有控制变量及其控制手段。 |
| A4 | 混淆变量 | 0.5 | p.3 'To mitigate potential biases due to the ordering of prompts... administered the questions individually and in a random order'; p.7 'Limited explainability' | 识别了提示顺序偏差并随机化问题顺序，但未系统讨论残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 理论模型与结果部分均无调节假设或交互检验，故不适用。 |
| A6 | 中介变量 | NA | — | 无中介假设、直接/间接效应分解或因果链检验，故不适用。 |
| A7 | 操作性定义 | 0.5 | p.3 Figures 1-3 give prompt templates; p.2 MBTI/BFI scoring references | 关键构念有操作化描述，但完整人格特质文本、角色标签和部分计分规则放在扩展版，正文不足以完全复现。 |
| A8 | 水平数与类型 | 0.5 | p.3 'P MBTI the set of 16 MBTI personality types' and 'P BFI the set of 5 BFI personality factors'; temperatures τ = {0.01, 0.7} | 报告了主要水平数与标签；未明确水平类型、间距/全距或连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p.2 uses both MBTI and BFI; p.5 Figure 5 and p.6 Table 3 | 使用两种人格测评作为多操作化，但未报告两者会聚证据；也未充分讨论单一测评局限。 |
| A10 | 单一方法的风险 | 0 | p.3 prompts elicit LLM questionnaire answers; no common-method-bias test | 自变量（提示条件）与因变量（自评式问卷回答）同源自同一 LLM 文本生成渠道，未做共同方法偏差程序控制或统计检验。 |
| B1 | 被试间设计 | NA | — | 无人类被试间分配；同一模型接受所有温度/人格条件，应按 LLM 重复测量而非被试间设计理解。 |
| B2 | 被试内设计 | 0.5 | p.3 'administered the questions individually and in a random order'; p.4 N=30 per model/condition | 同一模型重复接受各条件，但未报告条件顺序平衡方案，也未在模型中把模型/试次作随机效应。 |
| B3 | 混合设计 | 0 | p.4 '12 × 2 × 16 × 30' and '12 × 2 × 5 × 30' | 实际存在模型（组间）与温度/人格条件（组内）的交叉，但未逐因素标注组间/组内，也未使用混合模型或分别报告误差项。 |
| B4 | 因子设计 | 0 | p.4 full crossing formula; p.6 Table 3 reports model × temperature / factor summaries | 多因素完全交叉，但未给完整设计矩阵/每格样本量，也未报告交互项统计量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p.6 Table 3 reports per-model accuracy and percentage increases, no F/df/p/effect size | 未报告因子设计中的主效应统计检验。 |
| B6 | 交互作用 | 0 | p.6 discussion of temperature/model differences, no interaction test | 仅描述不同模型/温度下差异，未报告交互项统计检验或简单效应。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计，也无区组变量与区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或类似顺序平衡结构。 |
| B9 | 准实验设计 | NA | — | 研究不是准实验干预设计，未比较非随机处理组与对照组并作因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，且 LLM 各次施测为独立会话/独立重复，不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有把独立单位随机分配到互斥条件；每个模型接受所有条件，问题顺序随机化不属于处理分配随机化。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡；重复施测按独立重复处理，未形成条件顺序设计。 |
| C3 | 恒定 | 0.5 | p.4 top p/top k fixed at 50/1; experiments run locally with text-generation-webui on specified hardware | 报告了部分恒定参数和运行环境，但未讨论这些恒定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对分配程序。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组或协变量纳入统计分析；模型规模仅作描述性列出。 |
| C6 | 盲法 | NA | — | 全自动 LLM 测评，无人类被试、主试或评分者盲法安排。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | LLM 每次施测为独立重复，无练习块或跨试次学习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 不产生人类式疲劳；任务按独立重复运行，无 session 疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立调用/重复，未涉及跨条件残留或清洗期。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或不对称迁移设计。 |
| D5 | 范围效应 | NA | — | 研究不是人类被试内绝对判断/量值估计范式；虽然使用 Likert 选项，但核心不是范围效应校准设计。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.3 'administered the questions individually and in a random order' | 问题顺序做了随机化，但未说明随机方案类型、各位置出现次数或选项顺序平衡；仅部分满足。 |
| E2 | 默认赞同 | 0 | p.2 BFI 44 questions with five Likert options; no reverse-scoring or acquiescence discussion in main text | 使用 Likert 自评量表，但正文未报告反向计分题、正反向一致性或默许偏差控制。 |
| E3 | 极端 / 中间反应倾向 | 0 | p.5 Figure 5 reports average BFI scores; no skew or endpoint/midpoint usage reported | 报告了均值/平均分，但未报告分数分布形态或极端/中间反应倾向，也未在跨模型比较中校正反应风格。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或事后假设推断访谈；LLM 提示施测不按人类掩饰情节编码。 |
| E5 | 实验者效应 | NA | — | 完全自动化 LLM 数据采集，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 3 reports mean ± SD accuracy; p.6 notes 'perfect outcome... maximum score of 5.0' | 报告了均值/SD 和个别满分端点案例，但未系统报告偏度/端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | 0 | p.3 prompt-conditioned LLM questionnaire responses; no common-method-bias control | IV 与 DV 同源自 LLM 自评式回答，未做 CMB 程序控制或统计检验。 |
| F1 | 统计结论效度 | 0.5 | p.4 N=30 repetitions; p.6 Table 3 reports mean ± SD and percentage increases | 报告了重复次数、均值和标准差/百分比变化，但无事前功效分析、置信区间、多重比较校正或正式假设检验。 |
| F2 | 内部效度 | 0.5 | p.3 'we treated all models equally in terms of prompting'; p.7 limitations on deployment and explainability | 有标准化提示与同条件重复，但无随机分配、基线等价性检验或损耗处理；内部效度威胁仅零散讨论。 |
| F3 | 构念效度 | 0.5 | p.2 established MBTI/BFI tests and scoring; p.4 RQ0 expert-description similarity | 使用成熟测评并做了一定专家描述相似性检查，但未报告信度/效度指标或人格条件化操纵检验。 |
| F4 | 外部效度 | 0.5 | p.4 Table 2 lists 12 open models varying by size/architecture; p.7 limitations discuss deployment and larger models | 报告了模型样本特征和部分推广限制，但未系统界定抽样代表性或跨情境复现边界。 |
| G1 | 分析单位 | 0.5 | p.4 N=30 repetitions per model/condition; analyses average over repetitions | 说明了重复施测与模型-条件层级，但未使用多层/混合模型显式分离嵌套方差。 |
| G2 | 随机效应 | 0.5 | p.4 12 models and N=30 repetitions; no random-effect specification | 存在重复试次嵌套于模型/条件的结构，但论文把模型当固定集合、聚合重复，未报告随机效应结构。 |
| G3 | 材料作为随机效应 | NA | — | 问卷题目是标准化 MBTI/BFI 固定测量工具，不作为从更大材料总体抽样的实验材料因子。 |
| G4 | 统计功效 | 0 | p.4 N=30 chosen for 'statistically meaningful' assessments; no power analysis | 没有事前功效分析或预期效应量推导，结果也未报告置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.4 N=30 per model/condition and listed conditions; no exclusion/stopping rules | 报告了主要条件和重复次数，但未报告试次/模型排除规则、样本量决定依据或验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement in the paper | 正文未报告预注册、注册编号或分析计划。 |
| J1 | 位置偏差 | 0 | p.2 answer options are fixed ordered Likert/MBTI sets; p.3 only questions are randomized | 涉及多选项选择，但未对选项位置做随机化或反平衡，也未报告位置偏差检验。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评价开放式生成长度或质量。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或纠错式对话操纵。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM 裁判或成对输出比较。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，无 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.3 Figures 1-3 provide prompt templates; no prompt versioning or sensitivity ablation | 给出了主要提示模板，但未报告版本号、语义等价敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文或 RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.4 temperature τ={0.01, 0.7}, top p=50, top k=1, N=30 repetitions | 报告了主要采样超参和重复次数，但未报告随机种子、每次采样置信区间或 API/后端 snapshot。 |
| J9 | 重复与文本退化 | NA | — | 任务为选项选择/短回答评分，不涉及开放文本重复退化分析。 |
| J10 | 分词效应 | NA | — | 单语言英语、单脚本，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4 models obtained from HuggingFace 'as of early 2024'; no training-cutoff/overlap analysis | 使用公开人格问卷且 RQ0 检查模型对测试的了解，但未做训练数据截止日期对照或污染检测。 |
| J12 | 基准饱和 | 0.5 | p.6 Table 3 reports accuracy and BFI scores; notes 'maximum score of 5.0' cases | 报告了分数量程与部分满分端点案例，但未系统评估基准饱和或改用连续指标/更难子集。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；问卷作答不涉及按约束类型拆分准确率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求 JSON/文法约束等结构化输出。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.3 human MBTI/BFI administered to LLM agents; p.1 'mimicking human personalities' | 明确把人类人格测验用于 LLM，并讨论“human-like personalities”，但未系统论证 LLM 构念与人类同名构念的异同，也无人类对照数据。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨规模/训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对代理指标进行训练、RL 或 best-of-N 优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4 N=30 repetitions and model names/versions listed; no exact snapshot/CI/paired tests | 报告了重复次数与模型版本，但未给精确 commit/API snapshot、置信区间或配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 问卷逐题独立施测，未进行多轮对话或上下文累积评估。 |

## 编码小结
本研究将开源 LLM 作为“被试”施测人格问卷，操纵人格/角色条件化提示与温度，并报告多次重复下的准确率、频次或平均分。优点是指示模板、测评来源和部分重复次数较清楚；主要不足是缺少操纵检验、测量信效度、随机效应与多重比较处理、采样种子/置信区间、预注册、污染与饱和分析。大量人类被试分配、顺序平衡、需求特征与实验者效应组件不适用。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
