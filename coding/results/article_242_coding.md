# article_242 | Beyond Prompts: Dynamic Conversational Benchmarking of Large Language Models | 2024

研究类型概述：LLM 基准评测研究：以单段长对话将 11 个任务场景交错呈现，比较多种专有/开源 LLM 及 LTM 代理在 isolated 与 2k/32k/120k/200k/500k memory span 下的得分；分析单位为 agent 配置、memory span 与测试重复，属描述性 benchmark 评估，无人类被试。
- **研究构念（Construct）**：长程对话中的回忆、冲突信息处理、情景与前瞻记忆、任务切换和信息整合｜CA 构念锚定：回忆（recall, `trm_4a3fd79d0b95b`）；记忆提取（memory retrieval, `trm_4a3fd79d0ba01`）；长时记忆（long-term memory, `trm_4a3fd79d0a833`）
- **实验任务与范式（Task / Paradigm）**：让多个现成开源和商业LLM及其固定外部记忆配置在一段连续书面对话中并行执行多种记忆任务，改变任务是否交错和信息跨越的记忆跨度，并多次更新或撤销先前信息。（比较隔离与任务交错、2k至500k记忆跨度、不同现成模型、仅LLM与LLM加固定外部记忆，以及包含回忆、冲突、情景记忆、空间记忆、前瞻记忆、理论心智和信息整合的场景。）｜CA 任务锚定：数字广度任务（digit span task, `tsk_4a57abb949a0d`）；记忆广度测验（memory span test, `trm_4da869e68b5c4`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.7: 'We run the same benchmark with a number of different memory spans: 2k, 32k, 120k, 200k, and 500k tokens'; p.27: copied definition files and changed target memory span. | memory span（以及 agent 配置）被明确设置并有水平取值/程序，但无操纵检验、无随机分配说明，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.7: 'All scores are normalized to [0, 1] and scores from the same scenario are averaged together, which makes for a maximum of 11 points'; pp.14–25 detail per-test scoring (regex, string match, ROUGE-L, GPT-4 judge, manual). | 因变量指标和计分方式明确，但未报告信度/效度证据或连续指标预处理/天花板地板处理。 |
| A3 | 控制变量 | 0.5 | p.27: 'we simply copied the definition files and changed the target memory span'; p.26: 'all generation and scheduling processes use seeded random number generators'; p.7: LTM context kept around 16k tokens. | 报告了若干控制手段（固定测试定义、固定 seed、固定上下文上限），但不是系统控制变量清单。 |
| A4 | 混淆变量 | 0.5 | p.8: 'longer input sizes allow for both the tackling of longer tasks and the presence of more distractors'; p.9: automated evaluation can fail in edge cases; p.3: reply length affects filler tokens and later replies. | 识别了若干潜在混淆与内部效度威胁，但未系统控制残余混淆或做敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量假设，也没有报告调节变量的交互检验与简单斜率分析。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量假设，也未做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | pp.14–25: Appendix A gives per-scenario generation and scoring, e.g. Name List JSON score Eq.1, Jokes string match plus GPT-4 checker, ChapterBreak single-integer comparison. | 关键任务构念、数据生成步骤、评分指标与计分规则均有较可复现的操作化程序。 |
| A8 | 水平数与类型 | 0.5 | p.7: memory spans 2k/32k/120k/200k/500k plus isolated; Table 1 lists context sizes and span levels. | 报告了水平数与各水平标签，但未说明水平类型、间距/全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 0.5 | pp.4–5: multiple scenarios per skill (e.g. Recall: Colours and Name List; Integration: Locations, Spy Meeting, Shopping); pp.31–32 discuss task-specific failures but no convergent-evidence analysis. | 关键能力采用多种场景操作化，但未报告各操作间会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 因变量均为客观 benchmark 任务得分，不是同源自陈式多构念量表；共同方法偏差检验在此类 objective benchmark 中不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试的独立组分配；同一 agent 配置跨多个 memory span 运行，不是纯被试间设计。 |
| B2 | 被试内设计 | 0.5 | p.7: same benchmark run across memory spans; Table 1 reports each model across multiple memory spans; no condition-order balancing described. | 存在同一模型跨 span 的重复测量结构，但未报告平衡方案、各顺序分配或随机效应模型。 |
| B3 | 混合设计 | 0.5 | p.7: Table 1 crosses agent configurations with memory spans; no mixed-model or separate error-term reporting. | 设计上隐含组间 agent 配置 × 组内 memory span 的混合结构，但未逐因素标注或使用混合模型。 |
| B4 | 因子设计 | 0 | p.7: Table 1 reports complete model × memory-span score matrix with std; no ANOVA/interaction table. | 因素网格完整呈现，但未报告交互项统计检验、设计矩阵细节或效应量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p.7–8: Table 1 and Figure 5 show mean scores by model/span; no F, df, p, or effect-size tests. | 只有描述性均值/标准差与目视比较，未报告正式主效应检验。 |
| B6 | 交互作用 | 0 | p.8: interleaving is discussed as a key factor, but no formal interaction test; Figure 5 is descriptive. | 虽讨论交错任务的影响，但未对交互项做统计检验、简单主效应或校正。 |
| B7 | 区组设计 | NA | — | 没有区组/分层设计及区内随机分配。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡顺序。 |
| B9 | 准实验设计 | NA | — | 这是 benchmark 评测，不是非随机准实验因果设计，未声称或实施准实验分配。 |
| B10 | 被试内设计的适用条件 | NA | — | 各 memory span 配置为独立运行且上下文重置，不存在同一序列内的处理后效/迁移适用条件论证。 |
| C1 | 随机化 | NA | — | 无随机分配或分配隐藏机制；agent 配置与 memory span 为预设 benchmark 条件。 |
| C2 | 平衡 | NA | — | 各 memory span 为独立基准运行，没有条件顺序平衡设计。 |
| C3 | 恒定 | 0.5 | p.7: LTM context limit kept to 16k tokens; p.26: seeded generation; p.35: exact benchmark version v3.5. | 部分额外变量被恒定（代码版本、上下文上限、seed），但未系统列出恒定变量及外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未把混淆变量作为区组因素或协变量纳入分析；论文中的混淆讨论见 A4。 |
| C6 | 盲法 | NA | — | 无人类被试/评分者盲法设计；评分主要为自动化，少量人工校正未按盲法实验编码。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 等顺序平衡层级。 |
| D1 | 练习效应 | 0.5 | p.5: scenarios are tested multiple times and the agent is instructed to forget/disregard previous test information; p.8: 'early responses heavily influencing later ones'. | 有 reset/forget 安排并讨论模式补全，但无练习块、截除标准或试次位置协变量。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳风险；长对话带来的上下文效应不等于疲劳效应。 |
| D3 | 延滞 / 迁移效应 | 0.5 | p.5: repeated scenarios with 'forget or disregard' instructions; p.8: mixing information from different repetitions; p.31: reset statements pose a challenge. | 识别了跨重复的迁移/干扰风险并使用 reset，但未报告清洗期长度或将条件对显式建模。 |
| D4 | 不对称迁移 | 0.5 | p.8: 'early responses heavily influencing later ones'; p.32: 'overall performance is strongly biased by the first repetition'; no formal symmetry test. | 讨论了可能的不对称迁移/首轮偏差，但未做条件对检验或量化残留偏差。 |
| D5 | 范围效应 | NA | — | 因变量为客观任务得分，不是被试内绝对判断/量表评分，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p.24: ChapterBreak shows six continuations sequentially as options; p.5: scheduling is deterministic; no option-order randomization/counterbalancing reported. | 存在多选项和固定调度顺序，但未做刺激/选项顺序随机化或反平衡，也未讨论位置效应。 |
| E2 | 默认赞同 | NA | — | 未使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 未使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征操纵或事后访谈；此为自动化 LLM benchmark。 |
| E5 | 实验者效应 | NA | — | 数据采集与评分基本自动化，无人类主试/评分者期望传递设计。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Table 1 reports means/std; Figures 25–30 heatmaps show many 0/1 endpoint scores; p.9 acknowledges limited repetitions. | 报告了均值和标准差且端点频率可从热图观察，但未报告偏度、正式 pilot 难度校准或明确天花板/地板威胁分析。 |
| E7 | 共同方法偏差 | NA | — | 因变量为客观 benchmark 得分，不是同源自陈式多构念测量，CMB 不适用。 |
| F1 | 统计结论效度 | 0.5 | p.7: Table 1 reports mean and std; 'we generate 1,000 possible outcomes by repeatedly sampling one result from each scenario'; no confidence intervals/effect sizes or multiplicity correction. | 有描述性效应估计与离散度，但缺正式效应量/95%CI、样本量依据和多重性校正。 |
| F2 | 内部效度 | 0.5 | p.3: generation and scheduling deterministic; p.27: same definition files across spans; p.8–9 discuss interleaving and evaluation caveats; no random assignment/allocation concealment. | 报告了部分设计控制并讨论内部效度威胁，但无随机分配、分配隐藏或基线等价性检验。 |
| F3 | 构念效度 | 0 | p.9: 'automatic evaluation systems can perform poorly in some edge cases, requiring manual checking'; no reliability/validity evidence or manipulation check. | 未报告关键测量信度、效度证据或操纵检验；评分器失败由人工校正但未系统评估信度。 |
| F4 | 外部效度 | 0.5 | p.7: benchmarks executed via Google/OpenAI/Anthropic/TogetherAI APIs; p.9 limitations; p.10 future work. | 报告了模型/API 来源与部分推广边界，但无跨样本或跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.7: 'A benchmark run consists of 33 tests (11 scenarios and 3 repetitions each)'; scores averaged by scenario and summed; no multilevel model. | 说明了测试层级和汇总方式，但把嵌套测试聚合成总分，未显式分离测试/重复的聚集方差。 |
| G2 | 随机效应 | NA | — | 模型未使用混合模型/随机效应；benchmark 将 agent 配置视为固定比较对象，无随机效应推广需求。 |
| G3 | 材料作为随机效应 | 0 | p.7: 11 scenarios × 3 repetitions; p.24–25: only four ChapterBreak samples selected; no item random effect. | 具体测试材料被视为固定 benchmark 项目，未将材料/项目作为随机效应，限制了对新项目总体的推广。 |
| G4 | 统计功效 | 0 | p.9: 'only three repetitions, which is not very reliable'; no a priori power analysis or effect-size/CI reporting. | 无设计阶段功效分析或样本量/重复次数依据，仅事后承认重复少。 |
| G5 | 研究者自由度 | 0.5 | p.7: ChapterBreak excluded from 2k; additional runs with different seed marked by underscores; p.25: manual evaluation adjustments; no full confirmatory/exploratory distinction. | 报告了部分排除规则、额外运行与人工校正，但未完整区分验证性/探索性分析及全部样本量决定规则。 |
| G6 | 预先设定 / 预注册 | 0 | p.35: reproducibility checklist and version v3.5 given; no preregistration record or analysis plan. | 无时间戳早于数据收集的公开预注册，也未区分预注册验证性与事后探索性分析。 |
| J1 | 位置偏差 | 0 | p.24: ChapterBreak presents six options in sequence; no position randomization, A/B exchange, flip-rate, or position × accuracy reporting. | 多项选择存在位置偏差风险，但未做反平衡/随机化，也未报告位置效应。 |
| J2 | 冗长偏差 | NA | — | GPT-4 裁判主要用于内容存在性检查、结构化抽取与分阶段判定，不是开放式生成质量的长度比较，长度被误当质量的风险不作为核心评估设计存在。 |
| J3 | 谄媚 | NA | — | 任务为客观闭卷/记忆任务，无用户先验立场 framing 或纠错反馈的谄媚操纵。 |
| J4 | 自我偏好 | 0 | p.15/17/19/21/22: GPT-4 turbo used as evaluator in Jokes, Locations, Restaurant, Trigger; Table 1 includes GPT-4 turbo as evaluated model; no anonymization or self-preference control. | 裁判与被评模型存在同源（GPT-4 turbo）风险，未报告匿名化、异源陪审团或自我偏好偏差量化。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主要评估为零样本/任务指令式 prompt，未使用 few-shot in-context examples 作为实验条件。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | pp.15–24: several prompt templates shown in figures; p.35: benchmark version v3.5 and open repository; no sensitivity ablation or dev/test split. | 公开了部分 prompt 与版本，但未做语义等价措辞敏感性消融，也未说明 prompt 是否在测试集上调参。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p.3: test messages are 'uniformly distributed across a previously-delimited area'; p.7: memory spans 2k–500k and context ballooning; no first/middle/end manipulation or position × accuracy curve. | 报告了 memory span/token 规模并做区间分散，但未操纵关键信息首中尾位置，也未报告位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0 | p.5: 'zero-temperature LLM calls' only for dynamic data synthesis; p.7: three repetitions but no agent temperature/top-p/seed or variance CI details. | 未报告被评 agent 的采样超参、随机种子与多次采样置信区间，仅有少量重复运行。 |
| J9 | 重复与文本退化 | 0 | No decoding strategy (greedy/beam/sampling), repetition penalty, degeneration rate, or truncation ratio reported for agent outputs. | 任务涉及开放生成，但未报告解码策略和重复/退化 QC 指标。 |
| J10 | 分词效应 | NA | — | 单语言英文基准，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.9: notes that public test data may be in pretraining sets; p.24–25 use ChapterBreak/TriviaQA/ToMI-derived data; no model cutoff or overlap/contamination check reported. | 使用公开数据集和生成任务，但未与模型训练截止日期对照，也未做 n-gram/DCQ 等污染检测。 |
| J12 | 基准饱和 | 0.5 | p.7 Table 1 reports scores out of 11 with std; Figures 25–30 heatmaps; no continuous metrics or bootstrap CI for model comparisons. | 报告了分数量程与当前水位，部分任务接近端点但未改用连续指标或 CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为独立因变量，也没有按约束类型拆分 IF 准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.16: Name List parse failure gives zero; p.18: Shopping requires JSON; p.25 B.3 discusses JSON-format failures; no format-validity rate reported. | 报告了结构化输出要求与部分格式失败案例，但未报告格式合法率，也未使用 grammar constraint 设置。 |
| J15 | 越狱稳健性 | NA | — | 不是安全/越狱评估，未设置有害请求或对抗攻击。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文为工程性 LLM benchmark，不主张在心理学意义上测量与人类同名构念；未做人类对照或构念等价论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随模型规模/训练进展的能力曲线或 emergent ability 宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无对代理指标进行训练/RL/best-of-N 优化，也未报告 overoptimization 监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.7: three repetitions and some additional runs with different seed; Table 1 std; p.35: version v3.5; no exact API snapshot dates or paired tests. | 报告了重复次数、标准差与 benchmark 版本，但 API 模型 snapshot 不精确，模型比较未做配对检验，未发布完整推理日志/CI。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.3: single lengthy conversation with multiple interleaved tasks; p.7: 33 tests; p.8: interleaving degrades performance; p.31–32: turn/repetition-specific failures (e.g. trigger third instance). | 确实进行多轮长对话评估，并讨论部分轮次/重复失败，但未按轮次独立/累积评分，也未报告一致性随轮次衰减曲线。 |

## 编码小结
论文提出了有操作化细节和可复现资源的长对话 benchmark，任务生成、评分和调度描述较充分；但统计上以描述性均值和标准差为主，缺少正式效应量/置信区间、随机化与顺序平衡、信效度、基准污染检查、LLM 裁判偏差控制，且 3 次重复被作者明确承认可靠性有限。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
