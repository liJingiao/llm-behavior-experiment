# article_219 | Assessing Large Language Models on Climate Information | 2024

研究类型概述：该研究是以科学传播框架为基础的 LLM 基准评估与人类评分研究：对 300 个气候问题、多个 LLM 答案按 8 个呈现性与认识论维度进行专家评分，并辅以提示变体、AI Assistance 暴露、AIS 归因评估和 GPT-4-as-judge 的辅助实验。核心分析单位是 question–answer–dimension–rating，而非传统人类被试分组实验。
- **研究构念（Construct）**：科学传播中的表述充分性、认识论充分性与不确定性沟通｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：让现成LLM回答300个气候问题，由具相关教育背景的评审按八个科学传播维度逐项编码，并比较普通和dimension-aware提示。（比较模型、气候问题类别、普通/维度感知提示和表述/认识论维度。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: “Dimension-Aware Prompts ... Table 1 compares GPT-4 with either the ’basic’ or ’dimension-aware’ prompts”; p.7: three AI Assistance exposure settings (“Without AI Assistance”, “previous exposure”, “With AI Assistance”). | 存在明确的提示变体和 AI Assistance 暴露条件，至少两个水平及标签已给出；但缺少完整的分配程序、各组分配方式和操纵检验报告。 |
| A2 | 因变量 | 1 | p.3: “Each answer is assessed by three human raters”; p.25: “5-point scale from completely disagree to completely agree”; p.32: pairwise distance and Krippendorff’s alpha; p.40: validation study with 30 examples. | 评分工具、条目/维度、5 点评分与 issue 计分均明确；报告了评分者间信度、验证研究和理论驱动的构念界定。连续指标预处理不适用于此类 Likert 评分。 |
| A3 | 控制变量 | 0.5 | p.4: answer prompt fixed to “3-4 sentence paragraph” and “For consistency, we always use GPT-4” for auxiliary data; p.25: 32 raters all with climate-related undergraduate degree; p.27: tutorial and admission test. | 报告了若干控制做法（固定答案长度、固定 GPT-4 辅助、评分者教育背景、训练/准入），但没有系统列出控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.8: “the assistance may also influence the raters beyond enhancing discovery”; “rating dimensions inherently have a subjective component”; p.8: no gold ratings for calibration. | 识别了 AI Assistance 影响、评分主观性和缺少 gold ratings 等效度威胁，并部分讨论；但没有系统控制这些混淆或进行残余混淆的敏感性分析。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节假设、调节变量测量/操纵或乘积项交互检验；按题源/主题的分解只是描述性比较，不构成本编码表意义上的调节分析。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量、直接/间接效应分解或因果链检验。 |
| A7 | 操作性定义 | 1 | p.23 Table 8 gives full prompts for answer generation, URL retrieval, keypoint extraction, passage rating, AI Assistance, and dimension statements; p.26 Table 11 gives rating statements and issue checklists; p.3 gives 5-point scoring. | 关键构念均有可复现的操作化：答案生成提示、辅助数据流程、评分陈述、issue 选项和计分方式明确。 |
| A8 | 水平数与类型 | 0.5 | p.4 lists seven evaluated models; p.5 Table 1 gives basic vs augmented prompt; p.7 gives three AI Assistance exposure settings. | 报告了主要条件的水平数与标签，但没有系统给出水平类型、间距/全距，连续或有序变量的中心化/标准化说明也缺失。 |
| A9 | 单一操作化的风险 | 0.5 | p.26 Table 11 uses multiple dimensions and issue indicators for presentational/epistemological adequacy; p.32 reports inter-rater agreement; p.40 reports validation on 30 examples; p.8 discusses subjective component and limited gold calibration. | 关键构念采用多维度、多 issue 指标，并有验证研究；但没有报告同一构念不同操作化之间的会聚证据，单一维度仍主要依赖单一评分陈述。 |
| A10 | 单一方法的风险 | NA | — | 自变量主要是模型/提示条件，因变量为人类专家评分，来源并不相同；另有 AIS 和 LLM rater 作为辅助多方法比较，不属于同源自评的共同方法偏差问题。 |
| B1 | 被试间设计 | 0.5 | p.7: “Without AI Assistance refers to a setting where a specific pool of raters is never exposed” versus “With AI Assistance denotes the standard setting where assistance is shown”. | AI Assistance 暴露涉及不同评分者池，存在组间比较逻辑；但未报告随机分配、各组人数或独立组承担条件的完整说明。 |
| B2 | 被试内设计 | 0.5 | p.3: each answer assessed by three raters; p.26: “We query each dimension separately in the interface”; p.31 rating interface shows sequential rating of dimensions. | 同一评分者对同一答案的多个维度进行重复评分，存在被试内/重复测量结构；但未报告维度顺序平衡方案及各顺序分配。 |
| B3 | 混合设计 | 0.5 | p.7 gives between-pool AI Assistance settings; p.26 says each dimension queried separately within the same rating interface. | 结构上包含组间（助评暴露池）与组内（维度/答案重复评分）因素，但论文未逐因素标注组间/组内，也未使用混合模型分别报告误差项。 |
| B4 | 因子设计 | NA | — | 模型、维度和题源构成交叉比较，但这不是随机化因子实验；论文只做逐维度的模型比较和描述性 trade-off，未给出完整设计矩阵或 ANOVA 交互分析。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应 ANOVA；模型间比较是逐维度 pairwise t-tests，而非各因素主效应检验。 |
| B6 | 交互作用 | NA | — | 论文讨论 trade-offs，但没有对交互项作正式统计检验，也没有简单主效应/多重比较校正。 |
| B7 | 区组设计 | NA | — | 题目按来源/主题/因果类型分层抽样，但这不是实验区组设计；没有区组变量、区内随机分配或区组固定/随机效应建模。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序安排。 |
| B9 | 准实验设计 | NA | — | 这是基准评估而非准实验；没有非随机分组因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有对被试内处理可逆性/迁移对称性的实验设计论证；主要重复评分结构不是处理条件。 |
| C1 | 随机化 | 0 | p.7 describes separate AI Assistance exposure settings but reports no random assignment, random-number tool, allocation concealment, or baseline balance. | 若将助评暴露视为实验条件，则未见概率分配或分配隐藏；不能判定为真正随机化。 |
| C2 | 平衡 | 0 | p.26: “We query each dimension separately”; p.31 rating interface shows a fixed order of screening and dimensions; no counterbalancing reported. | 同一答案的维度评分按界面固定顺序进行，未报告顺序平衡或各顺序的评分者分配。 |
| C3 | 恒定 | 0.5 | p.4: fixed answer prompt (“3-4 sentence paragraph”), “For consistency, we always use GPT-4” for auxiliary data; p.8: limitations note evaluation is limited to the evaluated context. | 报告了若干恒定变量（提示、辅助模型、评分环境），但没有完整列出所有恒定变量及其水平，也缺少系统外部效度讨论。 |
| C4 | 匹配 | NA | — | 没有匹配或倾向得分匹配设计。 |
| C5 | 纳入为变量 | 0 | p.24 Table 9 reports answer length/sentence statistics but these are not included as covariates or blocking factors in the rating models. | 已知的答案长度、模型风格等潜在混淆被测量或描述，但没有作为协变量/区组纳入分析，也未检验斜率齐性。 |
| C6 | 盲法 | 0 | No blinding procedure is reported for human raters; p.31 interface shows raters see question, answer, and AI Assistance. | 评分者可看到答案与助评内容，论文未报告对模型身份、条件或评分者施盲及盲法成功检验。 |
| C7 | 平衡的层级 | 0 | p.26: “We query each dimension separately”; p.31 rating interface shows a fixed order of screening and dimensions; no counterbalancing reported. | 研究存在被试内/序列顺序平衡需求（同 C2），但未明确选用完全平衡、拉丁方或 ABBA 层级，亦未报告构造方法与顺序效应形状假设，记 0。 |
| D1 | 练习效应 | 0.5 | p.27: “In the tutorial ... 4 examples of increasing difficulty”; p.27: admission test before entering the rating pool. | 有练习/训练和无数据收集的 tutorial，部分控制练习效应；但未报告试次位置协变量或练习阶段结束标准。 |
| D2 | 疲劳效应 | 0 | p.43-44 reports average rating times per dimension and per rating, but no session length, rest breaks, or condition time-dispersion plan. | 论文分析评分耗时，但未报告疲劳控制安排（休息间隔、session 时长、条件分散）。 |
| D3 | 延滞 / 迁移效应 | 0.5 | p.7: “Without AI Assistance, but previous exposure” refers to raters who worked on previous studies that included assistance; p.7 reports they are in a “middle” position. | 识别并比较了先前助评暴露的潜在迁移/学习效应；但没有洗脱期、条件对建模或正式迁移分析。 |
| D4 | 不对称迁移 | 0.5 | p.7: previous-exposure raters detect more issues than assistance-unaware but less than with-assistance raters, suggesting learning from repeated exposure. | 报告了不对称迁移/学习效应的迹象，但没有正式检验迁移对称性或量化残留偏差方向与大小。 |
| D5 | 范围效应 | 0 | No range-effect or scale-anchoring analysis is reported for the 5-point Likert ratings; p.32 only notes alpha can be misleading under low variability. | 使用重复 Likert 评分但未讨论范围效应、绝对锚定或被试间对照。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选项、排序、序列刺激或需要随机化/反平衡的刺激呈现顺序；主要是单答案评分。 |
| E2 | 默认赞同 | 0 | p.26 Table 11 lists positively worded agreement statements such as “The answer is accurate” and “The information is presented well”; no reverse-coded items or acquiescence discussion. | Likert 量表全部为单向正向陈述，未设反向题，也未讨论默认赞同偏差。 |
| E3 | 极端 / 中间反应倾向 | 0 | Tables 3-4 report means and 95% CIs only; Tables 12-16 report agreement, not skewness or endpoint/midpoint use proportions. | 没有报告评分分布形态或跨群体反应风格校正；仅凭均值/CI比较模型。 |
| E4 | 需求特征 | 0 | p.29 gives instructions to raters but no cover story, hypothesis masking, or post-experimental inquiry about inferred study hypotheses. | 未使用掩饰情节或事后检查需求特征；评分者已知任务是对 LLM 回答做质量评估。 |
| E5 | 实验者效应 | 0 | p.27 tutorial and admission test; p.29 standardized instructions; no report of blinding of raters/analysts or experimenter expectation control. | 虽有评分教程与标准化流程，但全文未报告评分者盲法层级（评分者是否知晓模型/条件，见 C6=0），未达实验者/评分者效应控制的基本要件，记 0。 |
| E6 | 天花板 / 地板效应 | 0.5 | Tables 3-4 report means with 95% CIs; presentational means often near 4.5; p.32 notes low variability can make alpha misleading when many examples are rated 5. | 报告了均值和 CI，并注意到高分堆积的可能，但没有系统报告偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 自变量为模型/提示条件，因变量为专家评分，不属于同源自陈式多构念测量；共同方法偏差不是主要设计问题。 |
| F1 | 统计结论效度 | 0.5 | p.16 Tables 3-4 report mean ratings with 95% confidence intervals; p.17-18 Tables 5-6 report pairwise t-tests; no power analysis or multiple-comparison correction is reported. | 报告了效应量式的均值与 95% CI，但缺样本量确定依据、功效分析和多重性校正说明。 |
| F2 | 内部效度 | 0.5 | p.3-4: same 300 questions used across models, but no random assignment/allocation concealment; p.8 discusses internal validity limitations and absence of gold ratings. | 有共同题目对照并讨论了部分效度威胁，但没有随机分配、分配隐藏、基线等价性检验或被试流向/损耗处理。 |
| F3 | 构念效度 | 1 | p.32-36 report pairwise distance and Krippendorff’s alpha; p.40 reports validation on 30 known-issue examples; p.3 and p.27 report expert rater selection, tutorial, and admission test. | 关键测量的评分者信度、验证证据和构念来源均有报告；没有传统 manipulation check，但研究不是自变量操纵实验。 |
| F4 | 外部效度 | 0.5 | p.25 Table 10 and p.25 A.7 report 32 raters’ demographics and education; p.3 reports 300 questions from three sources; p.8 limits claims to evaluated context. | 报告了评分者样本来源与特征、题目来源和一定推广边界，但没有跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.3: each answer assessed by three raters; p.16 reports system-level means; p.32 reports inter-rater agreement; no multilevel model accounting for ratings nested in raters/questions. | 说明了评分单位但未在统计模型中显式分离评分者/题目/答案的嵌套方差，主要用聚合均值和 bootstrap/CI。 |
| G2 | 随机效应 | 0.5 | p.32-36 report inter-rater agreement but the main tables report aggregated means; no random-effects structure is specified. | 承认评分者间变异并报告一致性，但未报告把评分者/题目作为随机效应的模型结构，推断总体范围不明确。 |
| G3 | 材料作为随机效应 | 0.5 | p.3-4: 300 questions sampled from three sources; p.20-21 describes stratified sampling; main analyses aggregate across questions without item random effects. | 题目被视为来自更大题池的样本，并在抽样上分层；但统计模型未显式纳入题目随机效应或准 F 比。 |
| G4 | 统计功效 | 0.5 | p.16 Tables 3-4 report 95% CIs; no a priori power analysis or sample-size derivation is reported. | 报告了均值与置信区间，但缺事前功效分析、预期效应量来源和样本量推导。 |
| G5 | 研究者自由度 | 0.5 | p.20-21 reports question filtering/deduplication and sampling; p.3 reports 300 final questions; no explicit distinction between confirmatory and exploratory analyses or preregistration. | 报告了题目筛选和部分排除规则，但没有完整列出所有事后分析、样本量停止规则和验证性/探索性区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration platform, registration number, or time-stamped analysis plan is reported. | 未见预注册；分析计划与探索性分析未区分。 |
| J1 | 位置偏差 | NA | — | 研究不涉及多候选项选择、排序或成对 LLM-as-judge 位置比较；LLM rater 是单答案评分。 |
| J2 | 冗长偏差 | 0.5 | p.4 anchors answer generation to “3-4 sentence paragraph”; p.24 Table 9 reports answer length statistics; p.19 Table 7 reports “too long/too short” issues; no length–score correlation is reported. | 对生成长度有提示约束并报告长度和长度相关问题，但没有报告长度与评分的相关系数或盲评/长度对照。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场、反馈/纠错对话，无法构成谄媚操纵。 |
| J4 | 自我偏好 | 0.5 | p.41: “GPT-4 rater is more generous towards OpenAI models than humans are”; GPT-4 is also used as rater while OpenAI models are evaluated. | 识别了裁判模型与被评模型同源及自我偏好风险，但没有采用异源陪审团、匿名化或量化自我偏好比例。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主要提示是 zero-shot 指令式提示，未使用 few-shot in-context examples；Table 8 中没有 few-shot 示例集。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.23 Table 8 and p.42 Table 21 provide full prompt templates; p.5 Table 1 compares basic vs dimension-aware prompts. | 公布了完整提示模板并比较了一个提示变体，但没有系统做语义等价措辞的敏感性消融，也未说明 dev/test 划分和 prompt 调优过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p.4: for each keypoint, GPT-4 retrieves a Wikipedia article and “We pick the 3 highest scoring ones as evidence”; no token counts or key-information position manipulation are reported. | 有 RAG/证据段落排序流程，但没有报告实际上下文 token 数、关键信息位置操纵或位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0.5 | p.41: LLM rater uses “temperature 0.6” and samples 3 responses; answer generation/sampling parameters and seeds for main LLMs are not reported. | 辅助 LLM rater 部分报告了温度和重复采样，但主 LLM 答案生成的 temperature、top-p、seed、重复次数和 CI 不完整。 |
| J9 | 重复与文本退化 | 0.5 | p.19 Table 7 reports “repetitive” issue prevalence by model; decoding strategy, repetition penalty, and truncation are not reported. | 有重复率相关的质量问题统计，但没有报告解码策略或 repetition penalty，无法排除重复退化与模型能力混淆。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本评估，没有跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.3-4: questions from Google Trends, Skeptical Science, and GPT-4-generated Wikipedia questions; p.4: data collected September–October 2023; p.6: no evidence GPT-4 performs better on GPT-4-generated questions. | 报告了题集来源和收集时间，并初步检查了 GPT-4 自生成题优势，但没有训练截止日期对照、n-gram/DCQ 污染检测或污染率。 |
| J12 | 基准饱和 | 0.5 | p.5: results suggest sufficient “resolution and range”; presentational means in Table 3 are around 4.3-4.7, near the 5-point ceiling. | 报告了分数量程与部分模型差异，但未在接近上限的呈现性维度上改用连续指标或更难子集，也未系统做饱和检验。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；没有约束型指令遵循准确率测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 主要评估是开放式答案的人类维度评分，不要求结构化输出；LLM rater 的格式输出只是辅助实现细节，未构成格式合法率实验。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全性、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 这是应用型 LLM 气候信息评估，不主张把 LLM 作为心理学/认知科学被试来测量人类同名构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的能力曲线或涌现能力宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对 benchmark、奖励模型或 LLM-judge 进行训练/RL/best-of-N 优化，因此不涉及代理指标奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4: data collected September–October 2023; p.16 Tables 3-4 report 95% CIs; p.17-18 report pairwise t-tests; p.23 and p.42 provide prompts. No exact API snapshot hashes or generation seeds are reported. | 报告了模型名称、收集月份、置信区间和 pairwise 检验，并公开提示；但 snapshot 标识不够精确，主生成无重复次数/seed 与配对 bootstrap 细节。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究是单轮问答与单轮评分，没有多轮对话历史累积或多轮一致性衰减评估。 |

## 编码小结
论文完整报告了评分工具、提示模板、评分者训练与部分信度/验证证据，但随机分配、盲法、混合效应模型、功效分析、预注册等质控与推断组件多处缺失或不完整。许多人类实验设计组件因研究主要是基准评估/评分研究而记 NA；适用之处按实际报告判为 0、0.5 或 1。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 C7（NA→0）, E5（0.5→0）。
