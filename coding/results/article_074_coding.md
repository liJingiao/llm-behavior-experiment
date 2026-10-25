# article_074 | MultiPICo: Multilingual Perspectivist Irony Corpus | 2024

研究类型概述：资源论文：构建多语言、多社会人口群体标注的反讽语料库，并进行探索性标注分歧分析；随后把语料库用作 LLM 反讽识别与视角提示（base/trait/data）的基准评测。分析单位包括标注实例、标注者社会人口群体、语言/变体以及 LLM 输出；不是传统人类被试随机分组实验。
- **研究构念（Construct）**：跨人口与文化群体的反讽感知及语用视角采择（irony perception and pragmatic perspective-taking across groups）｜CA 构念锚定：心理理论（theory of mind, `trm_4a3fd79d0b392`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；刻板印象（stereotypes, `trm_4a3fd79d0b285`）
- **实验任务与范式（Task / Paradigm）**：资源论文：构建多语言、多社会人口群体标注的反讽语料库，并进行探索性标注分歧分析；随后把语料库用作 LLM 反讽识别与视角提示（base/trait/data）的基准评测。分析单位包括标注实例、标注者社会人口群体、语言/变体以及 LLM 输出；不是传统人类被试随机分组实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p7: 'we construct perspective-based datasets per language... base... trait-based... data-driven' and p8 Table 7 reports base/trait/data conditions. | LLM 部分主动操纵了提示条件（base、trait、data）这一自变量，并报告了条件标签与部分操纵程序；但缺少操纵检验，分配/重复调用方式也未系统说明，故为 0.5。 |
| A2 | 因变量 | 0.5 | p4 Table 1 reports label rates and annotation counts; p6 Table 5 and p8 Table 7 report F1 for positive class; p7 uses Pearson correlation for positionality. | 因变量指标与计分方式明确（二分类反讽标签、F1、相关、P-index），但缺少信效度证据、置信区间及连续指标预处理/端点效应说明。 |
| A3 | 控制变量 | 0.5 | p3: annotators selected by 'completion rate at least 99%', native speakers, balanced gender/nationality; attention checks with '50% correct answers' threshold. | 报告了若干控制/质量措施（注意检查、母语筛选、性别与国籍平衡、LangID 过滤），但并非系统控制变量清单，LLM 评测侧的采样与提示控制也不完整。 |
| A4 | 混淆变量 | 0.5 | p9-10 Limitations: 'ethnicity... substantial unbalance', 'some conversational context might be missing', paid crowdsourcing limitations. | 识别了人群不平衡、上下文缺失等潜在混淆，并用随机 P-index 作参照；但未系统控制或量化残余混淆对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量理论模型和交互检验；社会人口维度主要用于分组描述 P-index，而非正式调节分析。 |
| A6 | 中介变量 | NA | — | 无中介变量、直接/间接效应分解或因果链假设。 |
| A7 | 操作性定义 | 0.5 | p12 Appendix A.1 gives annotation instructions and example; p3 describes interface asking 'Ironic or Not ironic'; p12-14 gives prompt examples. | 反讽标注任务与提示条件有可复现操作化描述，但多语言完整提示模板、所有视角提示细节及输出映射规则未完整公开。 |
| A8 | 水平数与类型 | 0.5 | p7 lists three prompting conditions; p13 Table 9 defines demographic cohorts; p3 lists 9 languages and 25 varieties. | 报告了主要条件/分组水平与标签，但未系统说明水平类型（名义/等级/连续）、间距/全距及连续变量中心化等。 |
| A9 | 单一操作化的风险 | 0 | p3-4 and p7: irony measured with single binary annotation/classification task; no discussion of single-operationalization limitation. | 关键构念主要依赖单一操作化（二分类反讽标签），全文未讨论单一指标对可推广性的限制。 |
| A10 | 单一方法的风险 | NA | — | 研究不是同源自评式 IV-DV 结构：社会人口信息与反讽判断虽来自同一标注者，但属于分组元数据与任务判断；LLM 输出与人类标签来源不同。 |
| B1 | 被试间设计 | NA | — | 没有把人类被试分配到互斥实验条件的被试间设计；标注者对所有实例进行重复标注。 |
| B2 | 被试内设计 | NA | — | LLM 条件在同一测试实例上比较，但属于分离的 API 调用，没有被试内条件顺序设计或顺序平衡需要。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内因素混合设计及相应误差项。 |
| B4 | 因子设计 | NA | — | 没有正式因子实验设计、完整设计矩阵或交互项统计检验；模型/语言/提示条件是描述性比较。 |
| B5 | 主效应 | NA | — | 未报告因子设计意义上的主效应检验（F、df、p、效应量）。 |
| B6 | 交互作用 | NA | — | 未报告交互项统计检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配程序。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验干预研究；社会人口分组为观察性分组，无随机分配因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理条件，故不涉及处理可逆性与迁移对称性论证。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到实验条件；随机 P-index 仅用于构造零分布参照，不是处理分配随机化。 |
| C2 | 平衡 | NA | — | 没有条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p3: annotations on Prolific via 'integrated custom-built annotation interface'; p12 Appendix A.1 gives fixed instructions. | 报告了部分恒定设置（平台、界面、说明），但未系统列出所有恒定变量及其水平，也未讨论恒定带来的外部效度限制。 |
| C4 | 匹配 | 0.5 | p3: annotator set 'needed to be balanced both across genders... and nationality'; p4 Table 1 reports realized counts. | 采用按性别/国籍平衡招募（近似分层/配额），但未报告匹配方法、匹配后均衡性检验或回归假象讨论。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为协变量/区组纳入实验效应模型并检验 ANCOVA 假设。 |
| C6 | 盲法 | NA | — | 没有需要盲法的人类实验条件或评分者条件分配；标注任务本身不涉及条件隐藏。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级需要说明。 |
| D1 | 练习效应 | NA | — | 没有跨条件的重复测量或练习阶段设计；标注任务中的项目序列未被作为实验条件分析。 |
| D2 | 疲劳效应 | 0 | p12: 'This annotation consists of 200 small conversations... will take more or less 2 hours.' No rest/break schedule reported. | 报告了较长单次标注时长，但未报告休息间隔、时长限制或条件时间分散方案，疲劳控制缺失。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件迁移/清洗期设计；LLM 条件为独立调用，无上下文残留。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件顺序，不涉及不对称迁移检验。 |
| D5 | 范围效应 | NA | — | 使用二分类标签而非绝对判断/量表评分，无范围效应校准问题。 |
| E1 | 位置 / 顺序偏差 | 0 | p12: '200 small conversations' presented in annotation task; no statement of randomizing item order. p13-14 few-shot examples appear in fixed order. | 未报告对刺激/项目顺序或 few-shot 示例顺序做随机化或反平衡；存在固定顺序风险且未讨论。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表；反讽为二分类判断。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格量表比较。 |
| E4 | 需求特征 | NA | — | 标注任务明确要求判断反讽，无需隐瞒实验假设；没有可合理推断的受控条件假设。 |
| E5 | 实验者效应 | NA | — | 众包远程标注，无人类主试逐场施测；不涉及主试期望传递或评分者盲法条件。 |
| E6 | 天花板 / 地板效应 | 0.5 | p4 Table 1 reports %not/%iro label rates; p6 Table 5 and p8 Table 7 report model F1 scores; no pilot difficulty calibration reported. | 报告了标签比例和模型分数，可排查端点堆积；但未报告偏度/端点频率细节或 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量，不存在共同方法偏差检验需求。 |
| F1 | 统计结论效度 | 0.5 | p5 Table 2, p6 Table 4-5, p8 Table 7 report P-index differences, F1 and correlations as point estimates; no CIs or multiplicity correction. | 报告了效应量类指标和样本量，但缺少置信区间、样本量确定依据、多重性校正及统计假设说明。 |
| F2 | 内部效度 | NA | — | 观察性语料与基准评测，无随机分配因果实验；未主张需要随机分配的内部效度推断。 |
| F3 | 构念效度 | 0.5 | p3 attention checks and 50% threshold; p4 defines P-index; p12 annotation instructions; no conventional reliability/validity coefficients. | 报告了标注质量检查与 P-index，但缺少标准信度（如 α/κ）、效度证据及操纵检验。 |
| F4 | 外部效度 | 0.5 | p3-4 and p13 Table 8/10 report languages, varieties, annotator demographics; p9-10 limitations discuss limited/arbitrary language choice and unbalanced ethnicity. | 样本来源、语言变体和人口特征报告较充分并讨论边界；但无跨样本/跨情境复现设计。 |
| G1 | 分析单位 | 0.5 | p3-4 annotations per instance/annotator; p4 P-index computed over annotator groups; p6-8 model evaluation at instance level. No multilevel model. | 说明了标注与实例层级及分组聚合，但未显式处理标注嵌套于标注者、文本嵌套于语言变体的聚集结构。 |
| G2 | 随机效应 | NA | — | 分析为描述性/聚合性 P-index 与基准 F1，未使用混合模型或随机效应推断；无随机效应结构需要报告。 |
| G3 | 材料作为随机效应 | NA | — | 文本项目不是实验自变量的材料载体；未进行项目随机效应建模，且研究不是以材料抽样推断为核心的实验。 |
| G4 | 统计功效 | NA | — | 探索性语料分析与基准评测，无预设效应量或事前功效分析。 |
| G5 | 研究者自由度 | 0.5 | p3-4 reports 13 annotators excluded after attention-check threshold; p4 Table 1 reports all languages and sample sizes; p7-8 reports base/trait/data conditions. | 报告了部分排除规则、样本量与条件；但未完整说明所有分析选择、停止规则及验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered analysis plan mentioned in the paper. | 未报告预注册平台、编号或分析计划；符合缺失适用组件记 0 的口径。 |
| J1 | 位置偏差 | NA | — | 不是多候选项选择、排序或成对 LLM-as-judge 实验；输出为单一 irony/not irony 标签。 |
| J2 | 冗长偏差 | NA | — | 不是用 LLM 评判开放式生成质量；长度不是评分维度。 |
| J3 | 谄媚 | NA | — | 没有用户立场/反馈/纠错对话，不存在谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 评估模型输出；LLM 本身是被评测分类器。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p7: 'select the top 3 ironic and not ironic instances according to the target group annotation' and prompt with extracted examples; p13-14 example few-shot prompt. | few-shot 示例来源、数量和标签比例有说明，但未报告示例顺序反平衡、多 seed 重采样或完整模板。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p12-14 Appendix B.1 provides English base/trait/data prompt examples; no prompt versioning or sensitivity ablation. | 提供了部分完整提示示例，但未系统提供全部语言模板、版本号、敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务上下文为短 Post-Reply 对，不是长上下文/RAG 实验。 |
| J8 | 温度与采样随机性 | 0 | p6 and p14 mention models and computational resources but no temperature, top-p, seed or repeated sampling. | 未报告采样超参、随机种子或重复运行；LLM 输出非确定性未被纳入统计设计。 |
| J9 | 重复与文本退化 | 0 | p6 notes models output non-standard labels and BLOOM tends to generate long outputs, but no decoding strategy/repetition rate is reported. | 未报告解码策略、重复惩罚或退化率；仅描述了非标准输出及映射。 |
| J10 | 分词效应 | 0 | p3 and p6 compare 9 languages/25 varieties, but no tokenizer version or token counts are reported. | 跨语言比较未控制分词器版本与 token 数，语言效应可能与分词效率混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p3: Reddit data from Jan 2020 to Jun 2021 and Twitter stream data; no training cutoff or contamination check reported. | 测试材料来自公开社交媒体，未报告模型训练截止日期或污染检测，不能排除记忆复现。 |
| J12 | 基准饱和 | NA | p6 Table 5 and p8 Table 7 show F1 scores often low (e.g., 0 to .56), far from ceiling. | 基准分数明显未饱和，不是饱和基准上的微小提升宣称。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；主要评估反讽分类性能。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p12 prompt asks for 'a single label "irony" or "not irony"'; p6 reports non-standard labels and semi-automatic mapping; no formal format-valid rate. | 有格式约束和输出映射讨论，但未报告格式合法率、重试策略或把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文将 LLM 作为反讽识别与视角提示的工程基准，而非心理学/认知科学被试；未主张测量 LLM 的人类同名心理构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随模型规模/训练进展的涌现能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有训练、RL、best-of-N 或对代理指标的优化环节，纯评测。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p6 names ChatGPT (gpt-3.5-turbo), PolyLM-13B and mT0/Bloom, but no snapshots, repeated runs, CIs or paired tests. | 缺少精确 snapshot/日期、重复次数、置信区间和配对检验，评估可复现性报告不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮，无多轮对话历史累积。 |

## 编码小结
研究核心是语料库构建、标注者分歧描述和 LLM 基准评测，而非受控心理学实验。多数实验设计组件（被试间/被试内、随机分配、顺序平衡、盲法等）不适用。适用的测量与偏差组件中，论文提供了较丰富的语料与提示示例、标注者元数据和模型结果，但普遍缺少信效度检验、置信区间、预注册、采样超参、重复运行与污染控制等完整报告。
