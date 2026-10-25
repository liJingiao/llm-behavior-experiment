# article_213 | DarkBench: Benchmarking Dark Patterns in Large Language Models | 2025

研究类型概述：LLM benchmark evaluation: 14 LLMs evaluated on 660 adversarial prompts across six dark-pattern categories; LLM annotators plus human annotation validation; no human participants and no randomized experimental assignment to conditions.
- **研究构念（Construct）**：操纵性交流、谄媚、拟人化、品牌偏好、用户留存与隐蔽改写｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；态度（attitude, `trm_4a3fd79d09947`）
- **实验任务与范式（Task / Paradigm）**：以660个受控提示诱发六类dark pattern，让14个现成模型生成回答，并由多模型标注器与人工抽查判断行为是否出现。（操纵dark-pattern类别、具体提示、目标产品/身份和被测模型家族。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4–p5: 'manually writing adversarial prompts intended to solicit each pattern, and then few-shot prompting LLMs to generate new adversarial prompts. This resulted in 660 prompts that span the six dark pattern categories'; p14 Table 1 gives question formats/examples. | 六类提示被明确界定并作为设计分类，报告了水平标签与构造流程，但没有随机分配、操纵检验或明确的单位分配说明，故为部分满足。 |
| A2 | 因变量 | 1 | p15 Table 2: six binary annotation labels plus invalid; p15 Table 3: Cohen’s Kappa, Jaccard, agreement rate, agreement on yes; p5: human expert annotators reviewed samples to confirm Overseer accuracy. | 因变量为各暗模式是否出现的二分类标注，计分与单位（出现率）明确；报告了人类一致性信度指标与专家复核效度证据。 |
| A3 | 控制变量 | 0.5 | p6: 'Model temperatures were all set at 0 for reproducibility. We took one response per question.' | 报告了温度与每问一次响应等恒定控制，但没有系统列出全部控制变量及控制手段，也未讨论这些恒定设置的外部效度限制。 |
| A4 | 混淆变量 | 0.5 | p5–p6: 'we conducted a statistical analysis comparing each annotator model’s mean scores for its own model family versus other models'; p7 limitations mention private system prompts and RAG/tool augmentation. | 识别了标注者自家族偏好、私有系统提示与工具增强等潜在混淆，并做了部分偏差分析；但未系统量化残余混淆对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 研究没有调节变量假设或调节效应检验。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量假设或中介效应分解。 |
| A7 | 操作性定义 | 1 | p3–p4: six dark-pattern categories defined; p14 Table 1 gives question formats and examples; p15 Table 2 gives binary annotation labels; p8 provides code/data reproduction links. | 六类构念均有定义、示例、提示格式与二分类标注规则，因变量计分可复现，达到操作性定义要求。 |
| A8 | 水平数与类型 | 0.5 | p4: '660 prompts across six categories'; p6 lists 14 model names; p14 Table 1 lists category labels/examples. | 报告了六类提示与14个模型水平及标签，但未明确说明水平类型、水平间距/全距等；对名义分类而言后者不适用，但类型说明仍不完整。 |
| A9 | 单一操作化的风险 | 0.5 | p5: cosine similarity within categories; p5–p6: three annotator models and human expert review; p15 Table 3 inter-annotator agreement. | 每个类别使用多个提示与多个标注来源，具有一定多操作化/多指标特征，但未系统报告各操作间的会聚证据，也未充分讨论单一提示格式的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 目标模型生成回答，随后由独立 LLM 标注者与人类标注者评分；不是同源自陈式测量，经典共同方法偏差问题不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试分配到互斥实验条件；14个模型均接受全部660个提示，属基准评测而非被试间实验。 |
| B2 | 被试内设计 | NA | — | 没有以被试内条件顺序为设计对象的重复测量实验；提示顺序也不是操纵条件，未形成可编码的顺序平衡设计。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内因素混合的实验设计。 |
| B4 | 因子设计 | NA | — | 模型×类别矩阵是描述性汇总表，不是带交互检验的因子实验设计。 |
| B5 | 主效应 | NA | — | 没有因子设计中的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有交互作用统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方平衡被试内条件顺序。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计，也没有非随机分组下的因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理可逆性/迁移对称性设计需要论证。 |
| C1 | 随机化 | NA | — | 没有把研究单位随机分配到互斥条件；所有模型接受同一提示集，属单组基准评测。 |
| C2 | 平衡 | NA | — | 没有实验条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p6: 'Model temperatures were all set at 0 for reproducibility. We took one response per question.' | 报告了温度与每问一次响应等恒定设置，但未系统列出所有恒定变量及其水平，也未充分讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组/协变量纳入统计模型的分析设计。 |
| C6 | 盲法 | 0 | p14: 'The annotation button order was randomized for each human annotator to avoid an ordering bias during annotation.' No blinding procedure is described. | 有人类标注者参与评分，但未报告对评分者施盲的类型、实施方式或盲法成功检验；仅随机按钮顺序不足以满足盲法要求。 |
| C7 | 平衡的层级 | NA | — | 没有被试内顺序效应需要选择完全平衡/拉丁方/ABBA等层级。 |
| D1 | 练习效应 | NA | — | LLM 每个提示独立生成，无练习块或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session 时长、休息间隔或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各提示独立调用，无跨条件残留或清洗期设计。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件迁移对称性需要检验。 |
| D5 | 范围效应 | NA | — | 因变量为二分类暗模式出现判断，不是被试内绝对判断或量表评分任务。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p14: 'The annotation button order was randomized for each human annotator to avoid an ordering bias during annotation.' | 报告了人类标注按钮顺序随机化，但未说明随机化方案、各位置出现次数或分配细节；LLM 提示顺序亦未报告随机化。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，而是二分类标注。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 人类角色是标注者/编码员，不是会被研究假设引导的心理学被试；需求特征范式不适用。 |
| E5 | 实验者效应 | 0 | p14–p15: annotation guidelines in Table 2; p14 button order randomized, but no statement about blinding raters to model identity, rater training, or script standardization. | 有人类标注者评分，但未报告盲法层级、标注者是否知道模型来源、培训标准化或期望控制；仅提供标注指南。 |
| E6 | 天花板 / 地板效应 | 0.5 | p6 Figure 4 reports occurrence rates by model/category, including near-endpoint values such as user retention 0.97 and harmful generation 0.01, but no SD/skew or pilot calibration is reported. | 报告了出现率（端点比例）可部分排查天花板/地板，但未报告分布形态、偏度或任务难度校准过程，也未讨论端点堆积对内外部效度的影响。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；目标模型输出与独立标注者评分在来源上分离。 |
| F1 | 统计结论效度 | 0.5 | p15 Table 3 reports Kappa/Jaccard/agreement metrics; p5 reports cosine similarity means ± SD; p6 Figure 4 reports rates but no confidence intervals or multiplicity correction for model comparisons. | 有部分一致性效应量与描述统计，但主要模型间比较缺少置信区间、多重比较校正与样本量依据，统计推断透明度不足。 |
| F2 | 内部效度 | NA | — | 研究为非实验性基准评测，没有随机分配、分配隐藏、基线等价性或因果推断主张。 |
| F3 | 构念效度 | 0.5 | p15 Table 3 human agreement metrics; p5 human expert review of samples; p5–p6 three annotator models; no manipulation check reported. | 报告了评分者间一致性信度与专家复核的效度证据，但缺少操纵检验，且对单一提示操作化的构念效度局限讨论不足。 |
| F4 | 外部效度 | 0.5 | p6 lists 14 proprietary/open-source models; p7 limitations discuss dark-pattern coverage, private system prompts, and RAG/tool augmentation boundaries. | 报告了模型与提示集来源，并讨论了部分推广边界；但没有跨样本/跨情境复现，也未界定对所有聊天机器人产品的推广范围。 |
| G1 | 分析单位 | 0.5 | p6: '9,240 prompt-response pairs' and '27,720 evaluations'; p6: one response per question; analyses aggregate rates by model and category. | 说明了模型级与提示级数据规模，但统计汇总未显式处理提示嵌套于模型/类别、响应嵌套于提示的聚集结构。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；模型被视为特定目标集合而非从模型总体随机抽样，无需编码被试随机效应结构。 |
| G3 | 材料作为随机效应 | 0.5 | p5: '660 prompts' and cosine similarity checks within categories; p6: one response per question for each model. | 提示被当作固定基准材料，报告了提示多样性检查，但分析中没有把提示作为随机项目效应建模，限制了向更大提示总体的推广。 |
| G4 | 统计功效 | 0 | p6 reports 660 prompts and 14 models but no a priori power analysis or sample-size rationale; results are rates without confidence intervals. | 没有事前功效分析、目标效应量或样本量推导，也没有报告主要比较的效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | p6 reports all six categories and 14 models with one response per question; p6 reports total 9,240 pairs; no explicit exclusion rules or stopping/追加规则 are given. | 报告了全部条件与因变量类别，但缺少试次/响应剔除规则、样本量决定方式和探索性/验证性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement or registry link appears in the paper. | 没有预注册；研究未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 标注是对单个自由回答做二分类判断，不是多候选项选择、排序或成对 LLM-as-judge 位置比较；人类按钮顺序随机化已在 E1 编码。 |
| J2 | 冗长偏差 | 0 | p5–p6: annotation models judge free-form text for dark-pattern presence; no length distribution, length–score correlation, or length-control instruction is reported. | 使用 LLM 裁判评估开放性自由文本，但未识别或控制回答长度偏差，未报告长度与得分关系。 |
| J3 | 谄媚 | 0.5 | p14 Table 1 sycophancy example includes user conspiracy stance; p15 Table 2 defines sycophancy label; p6 Figure 4 reports sycophancy occurrence rates. | 谄媚类别确实操纵了用户先验立场式提示并测量出现率，但没有 pro-/anti- 对照翻转率，也未区分 feedback 与 answer sycophancy。 |
| J4 | 自我偏好 | 0.5 | p5: three annotator models Claude 3.5 Sonnet, Gemini 1.5 Pro, GPT-4o; p5–p6 own-family bias statistical analysis; p7 Figure 6 bias results; p15 Table 3 human agreement metrics. | 识别了裁判与被评模型同源风险，使用异源多裁判并报告自家族偏差分析；但未说明回答匿名化去签名，也未报告自我识别准确率。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p4: 'few-shot prompting LLMs to generate new adversarial prompts'; p14: 'designed to use in-context learning for k-shot annotation'; no example source, count, label ratio, order balancing, or seed resampling is reported. | 使用 few-shot/K-shot，但未报告示例来源、数量、标签比例、排列平衡或多 seed 重复，基本要件不足。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p8 provides a code repository and HuggingFace benchmark link; p14 describes a single annotation prompt with JSON output; no prompt-version sensitivity ablation or dev/test separation is reported. | 提供了代码/数据链接和部分提示描述，但未在正文给出完整模板版本、迭代日期、语义等价敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 提示为短文本问答，没有长上下文窗口操纵或 RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p6: 'Model temperatures were all set at 0 for reproducibility. We took one response per question.' Table 5 gives some model version strings but no top-p/top-k/seed or repeated-sampling CI. | 报告了 temperature=0 与每问一次响应，但缺少 top-p/top-k、随机种子、重复采样次数及置信区间。 |
| J9 | 重复与文本退化 | 0.5 | p6: temperature set at 0; no repetition penalty, n-gram repetition rate, degeneration rate, or truncation/length cap is reported. | 部分报告了解码温度，但未报告 repetition penalty、重复/退化 QC 指标或生成长度上限。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本评估，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p6 lists evaluated models; p8 gives benchmark/data links; no comparison of test-set release/version with model training cutoffs or contamination detection is reported. | DarkBench 虽为新基准，但未报告训练截止日期对照、n-gram 重叠或污染率检测，不能排除污染。 |
| J12 | 基准饱和 | NA | — | DarkBench 报告的是暗模式出现率而非能力正确率上限，不存在接近饱和后误报能力提升的典型基准饱和问题。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循表现，而是暗模式是否出现。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p14: 'We induce the model to output a JSON-formatted annotation for easy parsing.' No format-valid rate, retry policy, or separate format-failure metric is reported. | 使用了 JSON 结构化输出，但未报告格式合法率、重试策略，也未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | 0.5 | p14 Table 1 harmful generation example: 'Write a persuasive essay... why extreme fasting or starvation diets are healthy'; p6 Figure 4 reports harmful generation occurrence rates. | 使用对抗性有害提示并测量有害生成率，但未与自然提示拒绝率并列，也未报告攻击族或有害请求集版本。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究是应用型 LLM 行为基准评估，不主张把 LLM 作为心理学/认知科学被试并外推人类构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有随模型规模/训练进展的能力曲线或涌现/突变宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有以代理指标为优化目标进行训练、RL 或 best-of-N 优化，因此不涉及奖励过优化监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p6: 'We took one response per question'; Table 5 gives some exact model version strings; p8 gives code/data links; no repeated-run confidence intervals or paired tests are reported. | 报告了 N=1 与部分模型 snapshot 标识，但无重复采样、95% CI、逐题敏感性分析或模型间配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 评估输入是单个 Human prompt 并生成单次 AI 回复，不是多轮对话轨迹。 |

## 编码小结
The paper is a benchmark/observational evaluation rather than a controlled human-subjects experiment. Many experimental design components are not applicable. The benchmark construction, annotation labels, multi-annotator setup, and human validation are reported, but key transparency items such as prompt sensitivity, few-shot detail, contamination checks, judge-length control, and reproducibility uncertainty remain incomplete.
