# article_077 | In-Context Analogical Reasoning with Pre-Trained Language Models | 2023

研究类型概述：零样本基准评测：将 RAVEN 瑞文推理矩阵的视觉特征转写为语言提示，比较不同提示抽象层级、模型规模与子任务下预训练语言模型的答案选择准确率；无人类被试，分析单位为模型-条件-测试样例的聚合准确率。
- **研究构念（Construct）**：心理测量矩阵任务中的类比/关系推理与抽象（analogical/relational reasoning and abstraction in a psychometric matrix task）｜CA 构念锚定：类比推理（analogical reasoning, `trm_4a3fd79d09810`）；流体智力（fluid intelligence, `trm_4a3fd79d0a375`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：零样本基准评测：将 RAVEN 瑞文推理矩阵的视觉特征转写为语言提示，比较不同提示抽象层级、模型规模与子任务下预训练语言模型的答案选择准确率；无人类被试，分析单位为模型-条件-测试样例的聚合准确率。｜CA 任务锚定：瑞文高级推理测验（Raven's Advanced Progressive Matrices, `trm_4f24211a03b07`）；类比推理任务（analogical reasoning task, `trm_4f244f0286947`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4-6: 'three levels of abstraction' and 'OPT 125M, 1.3B, 13B ... GPT-3'; p15 Table 3 crosses model size with abstraction. | 自变量（抽象层级、模型规模）及水平有界定，操纵程序有描述；但无操纵检验，分配/评分方式亦非传统实验分配。 |
| A2 | 因变量 | 0.5 | p5: 'arg max ... log Pr (L (m11:32 , y))'; p5: 'random subset of 500 testing examples'; p15 Table 3 reports accuracies. | 因变量为候选答案选择准确率，计分方式明确；但无信度、效度证据，也未报告连续指标的预处理或天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | p5: token-length normalized log-probabilities; p7: orientation excluded 'to avoid unnecessarily increasing prompt lengths'; p10: 500-example subset to reduce computation. | 提到若干控制措施（长度归一化、排除 orientation、固定测试子集），但未系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 1 | p8: row-ablation tests in-context learning versus prior knowledge; p13 Appendix B uses I-RAVEN to address distributional bias; p10 limitations discuss human-comparison and text-conversion threats. | 识别了预训练先验、RAVEN 负选项分布偏差、人类对照不可直接比较等潜在混淆，并报告相应控制/补充分析及残余威胁。 |
| A5 | 调节变量 | NA | — | 未提出调节假设或调节模型；模型规模/子任务是设计因素而非被界定的调节变量，未做交互检验与简单斜率。 |
| A6 | 中介变量 | NA | — | 无中介变量、中介假设或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p4-5: entity/layout naming and decomposition definitions; p5 token-normalized log-prob scoring equation; p14 Figure 14 example prompts; p2 code link. | 关键构念被操作化为可复现的提示生成规则与候选概率选择规则，步骤、示例和代码可支持复现。 |
| A8 | 水平数与类型 | 0.5 | p5: OPT 125M, 1.3B, 13B, GPT-3 175B; p4-5 three abstraction levels; p8 rows 1/2/3; p7 orientation distractor. | 报告了主要因素水平数与标签；但水平类型、连续变量间距/全距及中心化说明不完整。 |
| A9 | 单一操作化的风险 | 1 | p6: quasi-image and random-naming baselines; p13 I-RAVEN supplementary analysis; p15 Tables 3-4 across subtasks. | 关键构念采用多种提示抽象、多个 RAVEN 子任务及 I-RAVEN 变体进行多操作化比较，并讨论文本化/分解假设的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 自变量为提示条件，因变量为客观答案准确率；无自评量表同源测量问题，共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配；模型评测不是被试间实验。 |
| B2 | 被试内设计 | NA | — | 同一模型在多个提示条件下评测，但每个提示彼此独立，无被试内顺序/学习设计。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合设计。 |
| B4 | 因子设计 | 0 | p15 Table 3: crossed model-size × abstraction × sub-task grid; p6-8 describe performance patterns. | 存在完全交叉的多因素描述性网格，但未报告 ANOVA/交互项、df、p 或效应量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p6: 'monotonically increase with model size'; p8: 'further improvement'; no F/df/p/effect size. | 只有描述性比较，未报告任何主效应的正式统计检验。 |
| B6 | 交互作用 | 0 | p6: 'much sharper improvement ... in smaller models'; no interaction test or simple-effects analysis. | 以曲线/数字描述交互样态，但无统计交互检验、简单主效应或多重比较。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 提示条件为独立评测，无处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 无处理分配到互斥条件的随机化；500 例随机子集是抽样而非实验分配。 |
| C2 | 平衡 | NA | — | 无条件顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p5 token-length normalization; p7 orientation excluded; p10 500-example subset; p16 compute across several platforms. | 报告了若干恒定/控制设置，但未系统列出恒定变量及其水平，也未充分讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 无将混淆变量作为区组/协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 主要评测由模型自动完成，无人类评分者盲法安排。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 无跨试次练习阶段；每个提示独立评分，不涉及练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类被试疲劳/休息安排；模型评测不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件清洗期或迁移残留问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观答案准确率，无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 候选答案作为缺失槽补全逐一评分，非有序选项列表；无被试内刺激/选项顺序设计。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，需求特征不适用。 |
| E5 | 实验者效应 | NA | — | 完全自动化评测，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p6-8 and p15 Table 3 report accuracies; p8 Table 2 reports human accuracies; no SD/endpoint frequencies or pilot calibration. | 报告了各条件准确率与人类参考，便于观察高值；但未报告分布/端点频率，也未说明难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无同源自陈式多构念测量。 |
| F1 | 统计结论效度 | 0 | p5: 500 examples per sub-task; p15 Table 3 point accuracies; p16 checklist C3 says greedy setting and no summary statistics/CI. | 无样本量功效依据、无效应量/置信区间、无多重比较校正或统计假设检验，仅报告单点准确率。 |
| F2 | 内部效度 | 0.5 | p5: evaluations on same random 500-example subset; p10 limitations; no allocation concealment/baseline equivalence. | 评测程序与若干威胁在局限中讨论，但无随机分配/分配隐藏/基线等价性报告；对内部效度威胁仅部分评估。 |
| F3 | 构念效度 | 0.5 | p2 RPM as psychometric relational reasoning test; p4-5 abstraction operationalization; p10 limitations; p13 I-RAVEN. | 有构念界定、多操作化与局限讨论，但无信度/manipulation check，且准确率本身不提供传统信效度统计。 |
| F4 | 外部效度 | 0.5 | p5 random 500 examples per sub-task; p13 I-RAVEN; p10 limitations on text conversion and need for future human studies. | 报告了数据来源、模型范围与部分边界条件，并做 I-RAVEN 补充；但无跨样本人类复现或系统代表性论证。 |
| G1 | 分析单位 | 0.5 | p5: 500 testing examples per sub-task; p15 aggregate accuracy tables; no multilevel/mixed model. | 分析发生在模型-条件-子任务聚合层，说明了评测单位；但未显式处理样例嵌套或分析层级匹配问题。 |
| G2 | 随机效应 | NA | — | 未使用混合模型或随机效应；模型规模作为固定设计水平比较，无被试抽样随机效应需求。 |
| G3 | 材料作为随机效应 | 0.5 | p5: 'random subset of 500 testing examples'; p15 aggregated accuracies; no item-level random effect. | 材料/题目被视为从 RAVEN 测试集抽样，但分析仅聚合准确率，未将题目作为随机效应建模。 |
| G4 | 统计功效 | 0 | p5: 500 examples used partly for computation; p15 point accuracies; no power analysis or CI. | 无设计阶段功效分析或样本量论证，结果仅单点准确率，无效应量/CI。 |
| G5 | 研究者自由度 | 0.5 | p5: 500-example subset; p10 computational reduction explanation; p16 code link; no explicit exclusion/validation-exploratory split. | 报告了部分抽样与计算限制，并提供代码；但未系统报告剔除规则、全部条件及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–18 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 无预注册或时间戳早于数据收集的公开分析计划。 |
| J1 | 位置偏差 | NA | p5: choice is 'arg max ... log Pr (L (m11:32 , y))' over candidates. | 候选作为同一缺失槽的补全逐一评分，不是有序 A/B 选项列表或 LLM-as-judge 成对比较；位置偏差结构上不存在。 |
| J2 | 冗长偏差 | NA | — | 不涉及 LLM 裁判或开放性生成长短质量比较。 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈对话式评估。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge，因变量为客观候选准确率。 |
| J5 | 少样本示例选择与排列偏差 | NA | p5: 'We apply PLMs to RAVEN in a zero-shot setting.' | 为零样本任务，不使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p14 Figure 14 example prompts; p3 code link; no semantic-equivalence ablation or dev/test split described. | 提供了多类提示示例与代码，基本可还原模板；但未做提示敏感性消融，也未说明是否在测试集上调提示。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG 设置；RPM 提示长度远低于长窗口操纵场景。 |
| J8 | 温度与采样随机性 | NA | p16 checklist C3: 'All evaluations occur in a greedy setting where PLMs choose the most probable answer.' | 候选由条件概率 argmax 选择，未使用随机采样；不涉及温度采样随机性。 |
| J9 | 重复与文本退化 | NA | — | 不涉及开放式生成长文本或重复退化问题。 |
| J10 | 分词效应 | NA | — | 单语言/单脚本评测，无跨语言或跨格式比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p10: generated text 'impossible to appear directly in PLM pre-training'; p5 text-davinci-002; no training cutoff or contamination detection. | 论文论证了文本提示的新颖性，但未报告测试集版本与模型训练截止日期对照，也未做污染检测/报告污染率。 |
| J12 | 基准饱和 | 0.5 | p6-8 compare to human and supervised baselines; p15 Table 3 accuracies; no CI or continuous metrics. | 报告了基准准确率与参考水位，但未讨论饱和问题、未报告 CI/连续指标。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 无结构化输出/格式合法率评估。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1-2 discuss analogy and human cognition; p5 human baseline; p10 limitations note human results come from different setting and call for future human studies. | 将 RPM 类比推理构念用于 PLM 并有构念讨论，但未做同范式人类对照，且明确人类比较不可直接类比。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p6-8 and p15 Table 3 plot accuracy across model sizes; only discrete accuracy, no continuous metrics or multi-seed curves. | 报告了规模-准确率曲线，但仅用离散准确率，无连续指标、多 seed 或置信区间，未排除指标诱导的突变假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练/RL/best-of-N 等对代理指标的优化过程，纯零样本评测。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5 lists model versions/sizes; p15 single point accuracies; p16 greedy setting and no summary statistics; no repeated runs/CI. | 报告了模型名称/规模与部分评测设置，但无重复次数、置信区间、精确 snapshot 或配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮独立提示，无多轮对话一致性衰减问题。 |

## 编码小结
论文是 LLM 零样本能力评测而非人类被试实验，核心操纵为语言抽象层级与模型规模，因变量为 8 选 1 准确率。方法描述与提示示例较充分，但统计推断、置信区间、重复采样、污染检查和预注册等报告不足；多数人类实验设计组件不适用。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
