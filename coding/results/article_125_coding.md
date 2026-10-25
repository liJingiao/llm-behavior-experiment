# article_125 | Potemkin Understanding in Large Language Models | 2025

研究类型概述：本文为 LLM 评测/基准研究，兼有形式化框架。核心分析单位是模型×概念×题目/生成样本；研究比较 7 个 LLM（另有 incoherence 分析 9 个模型）在定义、分类、受限生成、编辑任务上的表现，并用同一 LLM 生成相关问题、作答与自评来估计 potemkin 率下界。人类专家仅用于部分数据标注，不作为实验被试。
- **研究构念（Construct）**：概念理解的跨任务内部一致性与表面正确造成的虚假理解｜CA 构念锚定：语义记忆（semantic memory, `trm_4a3fd79d0b083`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）
- **实验任务与范式（Task / Paradigm）**：先确认现成LLM在一个概念任务上作答正确，再用围绕同一概念构造的分类、生成和编辑任务检验其跨任务一致性。（改变概念领域、先行成功任务、后续分类/生成/编辑任务以及模型家族，并与人类误解结构比较。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4: 'Our analysis spans the following 7 models...'; p5: 'classification, generation, and editing'; p6: 'keystone set size'; p17: 'Each prompt was constructed by randomly selecting one constraint from each category.' | 明确比较了模型、任务类型、领域与 keystone 大小等条件，并给出主要水平；但模型不是随机分配，任务/提示也无操纵检验与分配方式说明，故为部分满足。 |
| A2 | 因变量 | 0.5 | p5: 'potemkin rate is the percent of questions about a concept that are answered incorrectly, conditional on a model defining that concept correctly'; p7: 'percentage of cases where the model’s initial generation does not match its subsequent classification'; p15: total 2,030 annotations; p24: 2,880 labeled examples. | 因变量为 potemkin rate、incoherence/accuracy，计分与缩放规则清楚；但未报告标注者间信度、正式效度证据，也未系统说明连续指标预处理/端点处理。 |
| A3 | 控制变量 | 0.5 | p4: 'varying generation and evaluation methods to enhance the robustness'; p5: 'ensuring they post-date each LLM’s training cutoff'; p7: 'To avoid sycophancy in the judge... also prompt the LLM to generate a slightly incorrect response'; p15: exclude responses missing specified format. | 报告了若干控制做法（领域内混合标注、文学材料后置、sycophancy 控制、格式缺失剔除），但未系统列出控制变量清单及逐项手段。 |
| A4 | 混淆变量 | 0.5 | p5: 'One possible concern is that while our benchmark only uses single definition questions...'; p6: 'benchmark are too hard such that humans would fail these as well'; p7: 'The reason it’s a lower bound is that the judge may grade an incorrect response as correct'; p9 limitations. | 识别了 keystone 单一、任务难度、LLM judge 漏判等潜在混淆，并作定性讨论；但无敏感性分析或残余混淆的定量评估。 |
| A5 | 调节变量 | NA | — | 不适用：全文未提出调节假设，也未做交互项/简单斜率分析；模型、领域、任务差异仅作描述性拆分。 |
| A6 | 中介变量 | NA | — | 不适用：未提出中介机制或进行直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p2: formal definition of interpretation and keystone; p4-p5: definition/classification/generation/editing tasks; p14 Table 3 lists all 32 concepts and definitions; p25 Appendix M gives prompts for automated procedure. | 关键构念（potemkin、keystone、各任务正确性）均给出可观测操作化：概念定义、任务题干、评分规则、标注与剔除规则，基本可复现。 |
| A8 | 水平数与类型 | 0.5 | p4: '7 models: Llama-3.3 (70B), GPT-4o, Gemini-2.0 (Flash), Claude-3.5 (Sonnet), DeepSeek-V3, DeepSeek-R1, and Qwen2-VL (72B)'; p5: classify/generate/edit; p14: 32 concepts; p6: keystone size k. | 给出模型、任务、领域、概念与 k 的水平/标签；但模型快照不精确，水平类型、间距/全距及连续变量中心化等未系统说明。 |
| A9 | 单一操作化的风险 | 1 | p2: 'two procedures for measuring the prevalence of potemkins'; p7-p8: incoherence and automatic lower-bound procedure; p8: 'These results corroborate the benchmark findings'; p9: limitations on benchmark not exhaustive. | 关键构念采用基准任务与自动自评两套操作化，并报告二者方向一致；同时讨论基准非穷尽局限。 |
| A10 | 单一方法的风险 | 0.5 | p7: 'we prompt the LLM to answer the question correctly and then re-prompt the same LLM to grade its response'; p7: sycophancy concern and incorrect-answer mitigation; p15/p17: expert/author labels vs automated evaluators. | 部分构念来源不同（人工专家标注 vs 自动评估），但自动程序存在同源自评问题；仅做 sycophancy 缓解，无共同方法偏差统计检验。 |
| B1 | 被试间设计 | NA | — | 不适用：无人类被试组间分配；模型比较不是把独立“被试”随机分到单一条件，且同一模型跨任务/概念重复评测。 |
| B2 | 被试内设计 | NA | — | 不适用：无人类被试内重复测量及条件顺序平衡设计；各 prompt/API 调用彼此独立，未按顺序组分配。 |
| B3 | 混合设计 | NA | — | 不适用：未明确声明或实现组间×组内混合设计，也无混合模型误差项。 |
| B4 | 因子设计 | NA | — | 不适用：没有经典因子实验设计、完整设计矩阵和 ANOVA 交互项；表 1/6 是描述性模型×任务/领域汇总。 |
| B5 | 主效应 | NA | — | 不适用：无因子设计下的主效应统计检验与效应量报告。 |
| B6 | 交互作用 | NA | — | 不适用：未对交互项做统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 不适用：无区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 不适用：无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不适用：不是准实验因果设计；模型与任务比较为基准描述。 |
| B10 | 被试内设计的适用条件 | NA | — | 不适用：无人类被试内处理，不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 不适用：研究单位未被随机分配到互斥处理条件；随机选择约束属于刺激构造，不是条件分配随机化。 |
| C2 | 平衡 | NA | — | 不适用：无被试内条件顺序需平衡。 |
| C3 | 恒定 | 0.5 | p4: fixed 7 models and APIs; p5: same classification/generation/editing tasks across models; p15: standard annotation counts; p17: same constraint tables. | 部分固定了模型集合、概念集与任务材料；但未系统列出温度、prompt 版本、API snapshot 等恒定水平，也未讨论这些恒定的外部效度限制。 |
| C4 | 匹配 | NA | — | 不适用：未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 不适用：未把混淆变量作为区组/协变量纳入统计模型。 |
| C6 | 盲法 | 0 | p4: 'we rely on a mix of domain experts and paper authors to evaluate model responses'; p16/p19: Qualtrics expert surveys; no blinding reported. | 存在人工专家/作者评分，但未报告对评分者施盲、盲法类型或实施方式。 |
| C7 | 平衡的层级 | NA | — | 不适用：无顺序平衡层级设计。 |
| D1 | 练习效应 | NA | — | 不适用：LLM 每条件为独立 API 调用，无会话内练习块或试次位置学习。 |
| D2 | 疲劳效应 | NA | — | 不适用：无人类长 session 疲劳风险；任务为离散 API 查询。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不适用：各条件独立会话/独立 prompt，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 不适用：无被试内交叉条件，不存在不对称迁移。 |
| D5 | 范围效应 | NA | — | 不适用：主要指标为正确率/生成判定/自评一致性，非绝对量值或李克特量表。 |
| E1 | 位置 / 顺序偏差 | 0 | p8: MMLU multiple-choice items shown with options A-D; p17: constraints randomly selected, but no option-order randomization or position analysis reported. | 仅随机抽取生成约束，未对 MMLU 选项位置或刺激呈现顺序做反平衡/随机化，也未分析位置偏差。 |
| E2 | 默认赞同 | NA | — | 不适用：研究不使用 Likert/态度自评量表，无反向计分题问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不适用：无等级量表跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 不适用：研究对象为 LLM，不是可产生人类需求特征的人类被试；研究也未做人类事后假设推断访谈。 |
| E5 | 实验者效应 | 0 | p4: expert and author annotations; p16/p19: surveys; no blind arrangement, rater training standardization, or script detail. | 存在人类评分者，但未报告盲法层级、评分者是否知情条件、培训与脚本化程度。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5 Table 1 includes means/SEs and some 1.00/0.00 values (p22 Table 6, e.g., Gemini-2.0 game theory generation 1.00); no endpoint-frequency or pilot calibration. | 报告了均值与标准误，部分表可见端点值；但未报告偏度/端点频率或预实验难度校准过程。 |
| E7 | 共同方法偏差 | 0.5 | p7: same LLM grades its own answer; p7: sycophancy mitigation; no formal common-method statistical test. | 自动下界程序存在同源测量（生成与判定同模型），有程序性缓解但未做 CMB 统计检验，也未量化同源比例。 |
| F1 | 统计结论效度 | 0.5 | p5 Table 1 and p22 Table 6 report rates with standard errors; p15 reports annotation counts; no a priori power, 95% CI, or multiplicity correction reported. | 报告了效应量式比率与 SE，但缺少样本量功效依据、置信区间、统计假设检验与多重性校正。 |
| F2 | 内部效度 | NA | — | 不适用：非随机化因果实验，无处理分配与分配隐藏；论文也未声称经典实验内部效度。 |
| F3 | 构念效度 | 0.5 | p2: formal construct definition; p4-p5 task operationalization and expert labels; p9 limitations; no inter-rater reliability or manipulation check. | 有较强构念论证和多任务操作化，但未报告评分者信度、正式效度指标或操纵检验。 |
| F4 | 外部效度 | 0.5 | p4: models chosen 'for their popularity and range of developers and sizes'; p4: 32 concepts/3 domains; p9: 'not exhaustive... broader range of concepts...'. | 报告了模型与概念来源并讨论非穷尽局限；但无抽样代表性、跨样本/跨情境复现或明确推广边界。 |
| G1 | 分析单位 | 0.5 | p5: rates computed for each (model, concept) pair; p5 Table 1; p24: counts by domain/model; no multilevel model described. | 分析层级主要是模型-概念-题目/标注；存在题目嵌套于概念/领域的聚集结构，但未用多层模型显式处理。 |
| G2 | 随机效应 | 0 | No random-effects model reported; analyses report descriptive rates/SEs by model/domain/task (p5 Table 1; p22 Table 6; p24 Table 7). | 未报告任何随机效应结构；模型和概念均被当作固定集合处理，若需推广到概念/题目总体则推断过强。 |
| G3 | 材料作为随机效应 | 0.5 | p4: 32 concepts/2,030 annotations; p24: 2,880 labeled examples; p9: limitations note concepts not exhaustive; no (1&#124;item)/(1&#124;concept) model. | 承认材料/概念非穷尽，但分析未把概念或题目作为随机效应，未实现项目推广。 |
| G4 | 统计功效 | 0 | p5/p22 only rates with standard errors; no a priori power analysis or sample-size justification. | 未报告设计阶段功效分析或样本量论证，仅报告 SE，且无效应量 CI。 |
| G5 | 研究者自由度 | 0.5 | p15: 'we exclude responses missing the specified format'; counts for classification/generation/editing given; p9 limitations; no optional stopping/exploratory-confirmatory distinction. | 报告了格式缺失剔除和主要任务计数；但未完整报告样本量决定方式、是否中途停止，以及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered report mentioned; no distinction between preregistered confirmatory and exploratory analyses. | 未发现预注册；按口径记 0。 |
| J1 | 位置偏差 | 0 | p8: LLM judge grades its answer; MMLU multiple-choice options A-D shown; no candidate-position counterbalancing or flip-rate analysis. | 存在多选题选项位置与 LLM 判定情境，但完全未报告位置反平衡、交换重判或位置×正确率分析。 |
| J2 | 冗长偏差 | 0 | p7-p8 and p25: LLM judge grades free-form answers/reasoning; no length control in rubric, no length-score correlation. | LLM judge 用于开放作答，但未控制或报告长度偏差。 |
| J3 | 谄媚 | 0.5 | p7: 'To avoid sycophancy in the judge (e.g. an LLM may always grade responses as correct), we also prompt the LLM to generate a slightly incorrect response and also re-prompt the LLM to grade it'; p25 judge prompt. | 识别并部分控制了判分谄媚风险，但未操纵用户先验立场，也未报告翻转率或 feedback/answer sycophancy 分解。 |
| J4 | 自我偏好 | 0.5 | p7: 're-prompt the same LLM to grade its response'; p8 Figure 6 uses same model to judge its generated answer; sycophancy mitigation mentioned. | 明确使用被评同一 LLM 作为裁判，并尝试缓解谄媚；但未量化 self-preference、未用异源裁判/匿名化，故仅为部分满足。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 不适用：主要 prompt 为零样本；未使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p25 Appendix M gives full prompts for automatic evaluation procedure; no prompt versioning, sensitivity ablation, or dev/test split reported. | 提供了部分完整 prompt 模板，但无版本化、语义等价敏感性检验或测试集调参说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不适用：无长上下文/RAG 或多位置信息操纵实验。 |
| J8 | 温度与采样随机性 | 0 | No temperature, top-p, seed, repetition count, or sampling distribution reported; results are single reported runs with SEs from annotations. | 未报告采样超参与随机种子，也未通过多次独立采样估计 LLM 非确定性。 |
| J9 | 重复与文本退化 | 0 | Constrained generation tasks exist (p17-p18), but decoding strategy, repetition penalty, repetition/degeneration rate, and truncation are not reported. | 涉及开放生成，但未报告解码策略与重复/退化 QC。 |
| J10 | 分词效应 | NA | — | 不适用：单语言英文、无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p5: literary examples from recent poetry competitions 'ensuring they post-date each LLM’s training cutoff'; p8 uses MMLU; no MMLU contamination detection or model cutoff dates. | 对文学材料做了部分污染控制，但整体基准无系统污染检测、无训练截止日期对照与污染率报告。 |
| J12 | 基准饱和 | NA | — | 不适用：研究目的不是在同一饱和基准上宣称模型能力提升；也未做 SOTA 饱和/连续指标比较。 |
| J13 | 指令遵循 | NA | — | 不适用：因变量不是指令遵循测量；受限生成用于概念应用而非 IFEval 式约束遵循评估。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p15: 'we exclude responses missing the specified format (e.g., missing strings like “ANSWER: ”)'; no format legal rate or retry policy reported. | 报告了格式缺失剔除，但未报告结构化输出设置、格式合法率、重试/后处理规则，也未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不适用：不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p2-p3 formal framework contrasts human interpretation Fh and LLM interpretation Fl; p2: 'misunderstandings diverge from human patterns'; p4: models specified; no exact weight snapshots or human same-task empirical control. | 对 LLM 构念与人类同名构念有系统理论区分，但缺少精确模型 snapshot 与人类同范式对照实验，跨模型比较也未作为随机抽样总体。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不适用：未报告随规模/训练进展的能力曲线或涌现主张。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不适用：不涉及训练/RL/best-of-N 对代理指标的优化与 overoptimization 监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p4 lists model names; p5/p22 report standard errors and annotation counts; repository link given on p4; no exact API dates/commit hashes, seeds, or paired tests. | 报告了部分重复/标注数与 SE、公开仓库，但模型 snapshot 不精确，缺少重复采样 N、CI 与配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 不适用：研究为单轮 prompt/API 评估，无多轮对话历史累积或轮次一致性分析。 |

## 编码小结
论文提出并实证测量 potemkin understanding，使用新基准与自动自评程序相互佐证，构念操作化较好且有收敛证据。但整体是描述性基准评测：缺少随机分配、顺序平衡、随机效应/项目推广建模、采样超参与重复运行报告、精确模型快照、信度/功效检验和正式多重性控制；部分 LLM-as-judge 与污染风险被提及但未充分量化。
