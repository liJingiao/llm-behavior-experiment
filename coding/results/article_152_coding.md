# article_152 | Large Language Models Can Be Easily Distracted by Irrelevant Context | 2023

研究类型概述：这是一项 LLM 基准评测/行为评测研究：构建 GSM-IC，在 GSM8K 题目中插入无关句，比较不同提示技术、模型与无关信息类型对算术推理准确率的影响。没有人类被试；分析单位是测试题/示例（嵌套于 100 个 base problem），处理条件是提示方法与构造出的无关信息变体。
- **研究构念（Construct）**：无关信息造成的注意干扰、问题求解分心性与抗干扰策略｜CA 构念锚定：认知控制（cognitive control, `trm_4aae62e4ad209`）；注意（attention, `trm_4a3fd79d09902`）；干扰控制（interference control, `trm_551f11bb8f6a8`）
- **实验任务与范式（Task / Paradigm）**：在GSM8K问题中加入不改变正确答案的无关句子构成GSM-IC，对现成code-davinci-002和text-davinci-003比较多种提示方式、无关信息类型/位置/相关性、自一致性解码以及显式忽略指令，并扩展到DROP。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p3: 'we then generate ... adding to each base problem one sentence containing irrelevant information'; factors described; p5: 'we compare the performance of different prompting techniques'; p17-18: full prompts. | 自变量（提示技术、是否含无关上下文、是否加指令、SC 等）被命名并给出多水平及构造程序，但未报告操纵检验，条件分配也不是随机分配。 |
| A2 | 因变量 | 0.5 | p4: Accmicro 与 Accmacro 公式；p6 Table 3 报告 micro/macro/normalized accuracy。 | 因变量指标与计分方式明确（精确答案匹配的准确率），但无信度/效度证据，也无连续指标预处理或天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | p5: 'mainly use code-davinci-002 ... greedy decoding (τ = 0); ... sample 20 responses with temperature τ = 0.7'; p4: 'only use one simple exemplar ... to avoid over-fitting'. | 报告了固定模型、解码设置、示例选择与采样规模等控制，但未系统列出控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p14: 若插入句导致歧义则 'we fix the question'；p3: 从 GSM8K training set 取 dev 并 'avoid potential tuning-on-test-set issues'；p8: 讨论 4-exemplar prompt 的 overfitting。 | 识别并处理了歧义、测试集调参和提示过拟合等潜在混淆，但未系统报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | 0 | p3: 无关句按 topic、role-name overlap、number range 三因素构造；p8 Table 4: 按这些因素拆分准确率。 | 论文明确考察影响敏感性的因素，但只报告分层描述性拆分，没有正式的调节交互检验或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 本研究没有中介变量或中介假设。 |
| A7 | 操作性定义 | 1 | p3: GSM-IC 构造协议（模板、role/name、数字范围）；p4: 准确率公式；p17-18: 所有提示模板。 | 关键构念（无关上下文、提示方法、准确率）给出可观测、可复现的操作化与计分方式，且提供完整提示。 |
| A8 | 水平数与类型 | 0.5 | p3: 三个因素各含 in/off、yes/no、in/out 水平；p5: 两个模型与 greedy/SC 设置；p13 Figure 5: base problems 需 2–7 步。 | 水平数与标签基本明确，但未系统说明各变量是名义/等级/连续、水平间距/全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 0.5 | p8 Table 5: 在 GSM8K dev 与 SVAMP 上检查提示变体；p9: 扩展到 DROP；p9: 'future work ... other tasks and different language models'. | 使用了多个指标与多个任务提供一定多操作化证据，但没有报告各操作间的会聚统计；对单一算术推理任务的外推限制仅简要讨论。 |
| A10 | 单一方法的风险 | NA | — | 这是客观基准评测，不涉及自陈式多构念同源测量，共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配；所有测试题在各提示条件下被评测，不存在被试间独立组分配。 |
| B2 | 被试内设计 | NA | — | 虽然同一批题被多个提示条件评测，但 LLM 调用相互独立，无被试内顺序平衡意义上的重复测量设计。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内混合的人类被试设计。 |
| B4 | 因子设计 | 0 | p6 Table 3 与 p8 Table 4 给出按方法与无关信息因素拆分的准确率，但没有完整设计矩阵、每格样本量或交互统计检验。 | 研究比较多个条件并构造正交因素，但未报告正式因子设计分析或交互项。 |
| B5 | 主效应 | 0 | p6 Table 3: 报告各方法准确率均值；无 F、df、p、效应量。 | 主效应只有描述性准确率比较，没有正式统计检验或效应量。 |
| B6 | 交互作用 | 0 | p8 Table 4: 按 topic/role overlap/number range 拆分准确率；未报告交互项检验、简单效应或误差棒。 | 有描述性分层比较，但没有交互作用统计检验。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；没有非随机人类分组与选择偏差问题。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 基准评测没有把分析单位随机分配到互斥条件；所有题在多个条件下评测。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件呈现顺序。 |
| C3 | 恒定 | 0.5 | p5: 固定使用 code-davinci-002 / text-davinci-003，greedy τ=0，SC 用 τ=0.7；p9: 将其他模型和任务留作 future work。 | 报告了模型与解码等恒定设置，并简要讨论外推限制，但未系统列出恒定变量清单。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p7 Figure 4 按推理步数拆分准确率；p8 Table 4 按无关句因素拆分。 | 对题目的推理步数与无关信息类型做了分层分析，但没有作为协变量/区组纳入正式模型，也未检验斜率齐性。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者可施盲。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | LLM 每次调用独立，不存在人类被试式练习效应或学习迁移。 |
| D2 | 疲劳效应 | NA | — | LLM 评测不涉及人类疲劳或 session 时长。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件调用彼此独立，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 不存在被试内交叉条件的不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观准确率，不是量表评分类绝对判断。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选项、多刺激或被试内处理顺序需要随机化/反平衡。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert 或态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，故无需求特征或欺瞒检查问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p3: 'our base dataset is an “easy” subset of GSM8K'；p6 Table 3 报告各条件准确率；未报告 SD、偏度或端点频率。 | 报告了条件准确率均值并承认 base set 偏易，可能接近天花板，但没有分布、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | IV 与 DV 不是同源自陈式多构念测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p6 Table 3 只报告准确率点估计；无置信区间、效应量、功效分析或多重性校正。 | 统计结论效度报告不足。 |
| F2 | 内部效度 | NA | — | 无人类随机分配、分配隐藏或流失问题；所有方法在固定基准题上比较，内部效度问题主要转为污染问题（J11）。 |
| F3 | 构念效度 | 0.5 | p4: 'We manually verify that ... generated sentences are acceptable ... and adding them does not affect the standard solution'；p8 Table 5 在原 GSM8K/SVAMP 上检查提示变体。 | 对干扰句有内容效度/正确性核查，并在原基准上检查退化，但没有信度证据或操纵检验。 |
| F4 | 外部效度 | 1 | p3: 1,000 dev、100 base、4,000 examples；p8 Table 5: GSM8K dev/SVAMP；p9: DROP 扩展；p9: 讨论其他任务/模型为 future work。 | 报告了基准来源、样本特征、跨数据集扩展及外推边界；虽非人类样本，但外部效度报告较完整。 |
| G1 | 分析单位 | 0.5 | p4: 定义 micro accuracy 按单题平均、macro accuracy 按 base problem 类平均；p6 Table 3 同时报告两者。 | 明确区分题目层与 base-problem 类层，并用 macro 聚合处理嵌套；但未用多层模型显式分离聚集方差。 |
| G2 | 随机效应 | NA | — | 无人类被试/评分者随机效应；模型比较按固定条件处理。项目/材料随机效应问题在 G3 评估。 |
| G3 | 材料作为随机效应 | 0 | p4: 准确率在固定 4K 示例与 100 个 base problems 上聚合；没有项目随机效应、(1&#124;item) 或准 F 比。 | 所用题目/材料被当作固定集合，未建模项目抽样，结论向任意 GSM8K 题目的推广缺少统计支持。 |
| G4 | 统计功效 | 0 | p5: 'Being mindful of the experiment costs, we uniformly sample 4,000 examples'；无功效分析或 CI。 | 样本量由成本与可行性决定，未报告事前功效分析，结果也无置信区间。 |
| G5 | 研究者自由度 | 0.5 | p3: base 题从 dev 中选可被至少一种提示技术解出的 100 题；p5: 采样 4,000 题；未系统报告排除/解析失败规则，也未区分验证性与探索性分析。 | 披露了关键的 base-problem 选择与采样方式，但研究者自由度报告不完整。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册或注册编号。 | 无预注册，且未区分验证性与探索性分析。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放生成质量，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户先验立场或反馈纠错操纵。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 评估模型输出。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p4: 'we only use one simple exemplar for our main experiments'；p17-18: 给出完整 prompts；p8 Table 6: 比较 1 与 4 exemplars。 | 报告了 few-shot 示例来源、数量与内容，但未做多 seed 重采样、顺序反平衡或示例选择敏感性分析。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p17-18: 所有提示模板完整列出；p8 Table 6: 比较 1 vs 4 exemplars；p3: 避免在 test set 上调参。 | 提供了完整 prompt 模板并做了部分提示变体比较，但没有语义等价措辞的敏感性消融、版本号或系统 dev/test 提示调参说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是长上下文/RAG 信息位置实验；DROP passage 也不是对关键信息首/中/尾位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p5: 'greedy decoding (i.e., temperature τ = 0)'；SC 实验 'sample 20 responses with temperature τ = 0.7'。 | 报告了 temperature 与 SC 重复采样次数，但未报告 top-p/top-k、随机种子、API snapshot 日期或置信区间。 |
| J9 | 重复与文本退化 | 0.5 | p5: 非 SC 用 greedy，SC 用 20 次采样；未报告 repetition penalty、重复率/退化率或生成长度上限。 | 解码策略已报告，但未把重复与文本退化作为 QC 指标。 |
| J10 | 分词效应 | NA | — | 单语言英文任务，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p3: base problems 来自 'GSM8K training set'；全文未报告模型训练截止日期、测试集与训练数据重叠检查或污染率。 | GSM-IC 由公开 GSM8K training set 派生，未做污染评估；可能把记忆/暴露误当泛化能力。 |
| J12 | 基准饱和 | 0.5 | p3: 'our base dataset is an “easy” subset of GSM8K'；Table 2 base accuracies 95.0/94.0/83.0/44.0，SC 后更高；主要 GSM-IC 分数较低。 | 报告了 base set 接近天花板的情况并用 normalized accuracy 参照，但未对饱和问题做系统连续指标或 CI 分析。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；'ignore irrelevant information' 只是提示干预，结果仍是数学准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p4: PROGRAM 'execute the generated Python code using an external Python interpreter'；p17-18: program prompt 模板；未报告格式合法率或执行失败率。 | 存在结构化程序输出与执行约束，但未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1: 引用心理学中无关信息降低问题解决准确率，并将 LLM 表现称为 'distractibility'；全文没有人类同范式对照或系统构念异同论证。 | 把 LLM 的准确率下降类比为认知'分心'，但未论证该构念与人类分心的对应关系，也未报告人类对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨规模/训练进展的涌现曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以代理指标为目标的训练/RL/best-of-N 优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5: 报告 code-davinci-002、text-davinci-003 与 SC 20 samples；p6 Table 3 为单点准确率，无置信区间、配对检验或精确 snapshot 日期。 | 有模型版本名称与部分重复采样信息，但缺少精确 snapshot、CI 与配对比较，复现性报告不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮问答/推理，无多轮对话历史累积。 |

## 编码小结
论文对数据集构造、提示模板、模型与解码设置有较充分描述，但主要采用描述性准确率比较，缺少推断统计、置信区间、项目随机效应、污染检查、信效度与预注册；多数人类实验设计组件不适用。整体是扎实的基准评测，但统计与可复现性报告不完整。
