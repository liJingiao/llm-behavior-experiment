# article_130 | STEER: Assessing the Economic Rationality of Large Language Models | 2024

研究类型概述：LLM 基准评测/观察性模型比较研究：构建 64 个经济理性元素的 MCQA 基准（134,750 题），评估 14 个 LLM，并比较 self-explanation、few-shot、模型规模、年级/领域等条件下的表现；不是人类被试实验，也不是 LLM-as-judge 研究。分析单位为题目/模型/元素层面的聚合得分。
- **研究构念（Construct）**：经济理性、偏好一致性、认知偏差与战略决策｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让14个现成LLM完成64类经济理性元素的选择题，覆盖效用公理、风险/歧义、认知偏差、博弈、社会选择和机制设计，并比较提示策略。（改变理性元素、题目年级难度、决策环境、模型规模和zero/few-shot、自我解释、CoT提示。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: ‘For each question, we select n ∈ {0, 1, 2, 4, 5} examples’; p.5: two self-explanation approaches ‘dubbed separate and together’; p.6 Table 1 lists 14 LLMs. | 提示改编与模型规模等条件被命名并给出水平，但未报告随机分配、平衡或操纵检验；仅部分满足设计层要求。 |
| A2 | 因变量 | 0.5 | p.4: ‘Exact-match accuracy ... fraction of questions answered correctly’; p.4 defines normalized accuracy and ECE; p.3: validation spot-check ‘98.54% ... deemed valid by 2 validators’. | 因变量指标与计分公式明确，但缺少正式的测量信度/效度统计与连续指标的不确定性/预处理说明。 |
| A3 | 控制变量 | 0.5 | p.5: ‘We decoded from all LLMs by sampling with temperature 0’; p.3: static system prompt is appended during generation; p.5: few-shot examples selected ‘within the corresponding domain and grade level’. | 报告了温度固定、提示生成方式与领域/年级约束等部分控制，但未系统列出控制变量清单与逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | p.8: ‘We conjecture that this could be due to model alignment (RLHF) having treated medical domains as sensitive.’ | 在医疗领域表现波动处提出了可能的对齐/RHLF 混淆解释，但未系统控制或做残余混淆敏感性分析。 |
| A5 | 调节变量 | NA | p.7 Figure 6 and p.8 report grade/domain subgroup patterns, but no formal interaction/moderation tests are reported. | 论文没有调节变量理论假设或交互检验；按规则不适用。 |
| A6 | 中介变量 | NA | 全文无中介变量、间接效应或效应分解。 | 没有中介假设或中介分析。 |
| A7 | 操作性定义 | 1 | p.2–3 describe templates, generation, domains, grade levels and validation; p.4 gives exact-match/normalized accuracy/ECE formulas; p.12–22 define each element with illustrations. | 关键构念被操作化为可生成、可评分、可复核的 MCQA 元素，并给出评分程序，复现性较好。 |
| A8 | 水平数与类型 | 0.5 | p.5: few-shot n ∈ {0,1,2,4,5}; p.5: self-explanation separate/together; p.3: grade levels 1–13; p.6 Table 1 lists model parameter sizes. | 报告了主要条件的水平与取值，但未系统说明变量类型、间距/全距或连续变量的中心化/标准化处理。 |
| A9 | 单一操作化的风险 | 0.5 | p.2: taxonomy of 64 elements; p.3: ‘5 templates ... totaling between 10–40 templates per element’; p.4 lists multiple scoring metrics. | 使用了多元素、多模板、多指标来测量经济理性，但未报告各操作之间的正式会聚效度证据。 |
| A10 | 单一方法的风险 | NA | p.2–4 use MCQA with a correct answer and exact-match scoring; no self-report multi-construct measurement. | 该研究不是人类自陈式多构念测量；IV 为提示条件，DV 为客观 MCQA 得分，不按共同方法偏差框架编码。 |
| B1 | 被试间设计 | NA | p.5: models are treated as black boxes; p.6 Table 1 lists models; no human or LLM subject allocation to independent groups. | 没有独立被试组分配；模型为固定评估对象，不是被试间实验。 |
| B2 | 被试内设计 | NA | p.5 describes independent prompt conditions and evaluation; no session-level repeated-measures order or counterbalancing is reported. | 同一基准可在多个条件下评估，但每个 prompt 为独立调用，不存在会话内条件顺序问题。 |
| B3 | 混合设计 | NA | 全文无组间/组内因素标注或混合设计统计模型。 | 不是混合实验设计。 |
| B4 | 因子设计 | NA | p.5–8 compare models and prompt variants descriptively; no factorial design matrix or ANOVA interaction table. | 没有正式因子设计及主效应/交互分析。 |
| B5 | 主效应 | NA | 没有因子设计主效应的 F、df、p、效应量报告。 | 不适用。 |
| B6 | 交互作用 | NA | 没有交互项统计检验或简单效应分析。 | 不适用。 |
| B7 | 区组设计 | NA | 全文无区组变量、分层或区内随机分配。 | 不适用。 |
| B8 | 拉丁方 | NA | 全文无拉丁方或顺序平衡设计。 | 不适用。 |
| B9 | 准实验设计 | NA | p.5–8 are benchmark evaluation and model comparisons, not a quasi-experimental causal design. | 没有准实验分组、选择偏差或因果推断框架可编码。 |
| B10 | 被试内设计的适用条件 | NA | 没有人类被试内处理的顺序/迁移问题。 | 不适用。 |
| C1 | 随机化 | NA | p.5–6 evaluate fixed models on a benchmark; no random allocation of analysis units to mutually exclusive conditions. | 没有需随机分配的互斥实验条件；LLM 评估为全基准或条件网格评估。 |
| C2 | 平衡 | NA | 没有条件顺序平衡方案。 | 不适用。 |
| C3 | 恒定 | 0.5 | p.5: ‘temperature 0’; p.3: static system prompt; p.6 Table 1 lists model versions; p.8 notes results are lower bounds under tested prompts. | 报告了温度固定和模型版本等恒定条件，也提到外部效度局限，但未系统列出所有恒定变量及水平。 |
| C4 | 匹配 | NA | 全文无匹配变量或匹配后分配程序。 | 不适用。 |
| C5 | 纳入为变量 | NA | 没有协变量/区组纳入分析以调整已知混淆。 | 该基准分析未采用 ANCOVA/协变量设计；相关风险在 A4 中记录。 |
| C6 | 盲法 | NA | 主实验为自动评分；人工验证仅用于题项效度检查，未作为条件盲法评分设计。 | 没有需要条件盲法的人类被试或实验评分者。 |
| C7 | 平衡的层级 | NA | 没有平衡层级或顺序效应假设。 | 不适用。 |
| D1 | 练习效应 | NA | p.5: independent LLM calls with temperature 0; no human practice/trial sequence. | LLM 每题独立调用，无练习效应或试次学习结构。 |
| D2 | 疲劳效应 | NA | 没有人类 session 时长、休息或疲劳控制。 | 不适用。 |
| D3 | 延滞 / 迁移效应 | NA | 每个 prompt 独立生成，无跨条件清洗期或残留迁移设计。 | 不适用。 |
| D4 | 不对称迁移 | NA | 没有迁移对称性检验或跨条件残留。 | 不适用。 |
| D5 | 范围效应 | NA | 因变量为 MCQA 正确率/校准，不是主观量表评分。 | 无范围效应/量表锚定问题。 |
| E1 | 位置 / 顺序偏差 | 0 | p.2: each question has ‘a set of candidate choices, exactly one of which is correct’; no randomization or counterbalancing of correct-option position is reported. | MCQA 存在选项位置偏差风险，但论文未报告选项顺序随机化或反平衡；适用且缺失。 |
| E2 | 默认赞同 | NA | 研究使用 MCQA，不使用 Likert/态度自评量表。 | 不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | 没有等级量表得分的端点/中点使用或跨群体反应风格比较。 | 不适用。 |
| E4 | 需求特征 | NA | p.5: LLMs are treated as black boxes; no human participants or cover story/debriefing. | 不涉及人类被试需求特征。 |
| E5 | 实验者效应 | NA | 数据采集为 API/本地 GPU 自动运行，无人类主试或评分者期望传递。 | 不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Table 2 reports mean exact-match and normalized accuracy; p.7 Figure 6 reports grade-level curves; p.3 discusses grade-level difficulty. | 报告了均值与难度分级，但未报告 SD/偏度/端点频率或 pilot 校准的完整细节。 |
| E7 | 共同方法偏差 | NA | 没有自陈式多构念同源测量。 | 不适用。 |
| F1 | 统计结论效度 | 0.5 | p.7 Table 2 reports point-estimate accuracy; p.7 reports head-to-head comparisons; no confidence intervals, power analysis or multiple-comparison correction are reported. | 有主要性能指标点估计，但缺少 CI、样本量依据和多重性校正。 |
| F2 | 内部效度 | NA | p.5–6 evaluate fixed black-box models on a benchmark; no random assignment, baseline equivalence, attrition or human flow diagram. | 非人类随机试验，内部效度不按被试分配/损耗框架评估。 |
| F3 | 构念效度 | 0.5 | p.3: ‘98.54% ... deemed valid by 2 validators, with the lowest validation rate being 97%’; p.6 aligns elements with vNM axioms; no formal inter-rater reliability or manipulation check. | 有题项验证和理论构念对齐，但缺正式信度/效度统计与操纵检验。 |
| F4 | 外部效度 | 0.5 | p.6 Table 1 lists 14 models, versions and parameter sizes; p.8 notes results are lower bounds under tested prompts and calls for more models/strategies. | 报告了模型样本与部分边界，但没有代表性抽样论证或跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.4 scores questions and aggregates by element; p.7 Table 2 averages over benchmark; no multilevel model for questions nested in templates/elements/domains. | 明确了题目/模型/元素层级的聚合，但未显式处理题目嵌套结构或分析单位匹配。 |
| G2 | 随机效应 | NA | p.7 uses descriptive averages; no mixed-effects model or random-effect specification. | 该文没有随机效应统计模型；作为固定模型集的描述性基准，不按混合模型随机效应编码。 |
| G3 | 材料作为随机效应 | NA | 题目是基准测量工具而非作为随机抽取的刺激总体进入混合模型；p.3 generates templates/questions, p.7 aggregates. | 没有材料/项目随机效应分析需求或相应模型。 |
| G4 | 统计功效 | 0 | p.2: ‘It would be impractical to hand-construct enough questions ...’; p.5 reports 134,750 test questions; no prospective power analysis or CI. | 未做事前功效分析或样本量推导；仅报告大规模题量，不足以满足 G4。 |
| G5 | 研究者自由度 | 0.5 | p.3: programmatically removed malformed questions and randomly spot-checked 100 samples (10%) per triple; p.2 says all model outputs are released; p.6 says results focus mainly on normalized accuracy for space. | 报告了部分排除/验证规则与公开输出，但未完整列出全部条件、所有分析及验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未出现预注册平台、注册编号或分析计划预注册。 | 无预注册；按口径记 0。 |
| J1 | 位置偏差 | 0 | p.2: MCQA questions have ‘candidate choices, exactly one of which is correct’; no answer-position randomization, swap rejudging, or position bias analysis is reported. | 多选项选择场景存在位置偏差风险，但未做任何反平衡或位置分析。 |
| J2 | 冗长偏差 | NA | p.4 scoring is exact-match/normalized accuracy/ECE; no LLM-as-judge or open-ended length-quality comparison. | 不涉及裁判长度偏差。 |
| J3 | 谄媚 | NA | p.2–5 use objective MCQA prompts; no user stance, feedback or correction manipulation. | 无用户立场输入，不适用谄媚风险。 |
| J4 | 自我偏好 | NA | p.4 uses exact-match/ECE, not LLM-as-judge. | 不涉及裁判自我偏好。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.5: few-shot n ∈ {0,1,2,4,5}, examples selected within corresponding domain and grade level; no example source, label ratio, order counterbalancing or multi-seed resampling is reported. | few-shot 条件存在，但示例选择与排列控制信息严重不足。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4 Figure 2 shows an example user/system prompt; p.6 says web interface exposes ‘precise inputs and prompts’; no prompt versioning, sensitivity ablation or dev/test separation is reported. | 提供了部分模板/可访问提示，但未报告版本、敏感性消融与测试集调参控制。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | p.5 few-shot examples up to n=5; no long-context or RAG manipulation. | 上下文很短，不适用长上下文位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | p.5: ‘decoded from all LLMs by sampling with temperature 0’; p.6 Table 1 gives model versions; no top-p/top-k/seed/repeated runs/CI are reported. | 报告了温度与部分模型版本，但采样超参、随机种子、重复次数和不确定性估计不完整。 |
| J9 | 重复与文本退化 | 0.5 | p.5 reports temperature 0; no repetition penalty, n-gram repetition/degeneration rate, or length-truncation QC is reported. | 解码策略仅部分报告；未检查重复/退化，尽管主任务为短选项 MCQA。 |
| J10 | 分词效应 | NA | 研究为英文单语言 MCQA，无跨语言/跨脚本比较。 | 不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.2: benchmark questions are generated with GPT-4 Turbo; p.6 lists model versions; no training-cutoff comparison or contamination detection (DCQ/n-gram overlap) is reported. | 新生成基准降低了部分风险，但未明确证明未见于训练语料，也未做污染检查。 |
| J12 | 基准饱和 | NA | p.7 Table 2: GPT-4 Turbo normalized accuracy 0.3302; p.7 reports high-grade performance near random; benchmark is far from ceiling. | 新难题基准且远未饱和，不适用饱和风险。 |
| J13 | 指令遵循 | NA | 主因变量为 MCQA 正确率，不是指令遵循测量。 | 不适用。 |
| J14 | 输出格式约束 / 结构化输出 | NA | p.2–4 do not impose/parse JSON or grammar-constrained structured outputs as an experimental factor. | 不适用结构化输出格式风险。 |
| J15 | 越狱稳健性 | NA | 研究不涉及有害请求、越狱或安全对齐评估。 | 不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1–2 frame the work as assessing economic rationality and cognitive biases; p.8 says future work should determine how humans score as a baseline. | 论文将 LLM 构念与人类经济理性/认知偏差关联，讨论了部分理论关系，但没有人类对照实验，也未系统论证构念等价性。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | p.7 reports model size correlated with performance across 14 models; no emergent-ability claim or scaling-curve analysis with continuous metrics/seeds. | 不是跨训练规模/训练进展的涌现曲线研究；仅作模型间规模相关描述。 |
| J18 | 指标博弈与奖励过优化 | NA | 研究为推理评估，无 RL、best-of-N 或奖励模型优化。 | 不涉及代理指标优化与 overoptimization。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6 Table 1 gives versions such as ‘GPT-4 Turbo (1106-preview)’ and ‘GPT-3.5 Turbo (0613)’; p.2 says all model outputs are released; no repeat N, CI or paired tests are reported. | 有部分 snapshot 标识与输出公开，但缺少重复次数、置信区间和配对不确定性分析。 |
| J20 | 多轮对话中的一致性衰减 | NA | p.5 prompts and few-shot examples are single-turn; no multi-round dialogue evaluation. | 不适用多轮一致性衰减。 |

## 编码小结
论文在构念分解、题目生成与人工验证、公开输出和系统化基准构建方面较扎实；但作为基准评测，缺少选项位置控制、置信区间/重复采样、预注册、功效分析与污染检查，few-shot 示例选择与提示敏感性报告也不完整。许多人类实验设计组件不适用于其实际分析单位，应记 NA；可适用的 LLM 评估风险（位置偏差、few-shot、提示敏感性、采样随机性、污染、可复现性）多数只部分满足或未满足。
