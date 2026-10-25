# article_154 | Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers | 2025

研究类型概述：大规模专家盲评研究：比较人类专家、LLM 代理、LLM 代理+人类重排三种研究想法来源；人类评审者对想法进行 1-10 分多指标评审，并辅以 LLM 代理生成、LLM 排序/评审、想法多样性分析。主要分析单位为评审、想法与评审者，统计上使用评审独立、想法平均、评审者配对及线性混合模型。
- **研究构念（Construct）**：创造力、创新性、可行性、生成多样性与自我评价偏差｜CA 构念锚定：创造性思维（creative thinking, `trm_4a3fd79d09f42`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：让提示驱动的LLM研究构思Agent与NLP研究者在相同主题和写作格式下独立生成研究想法，再由专家盲评；另比较LLM排序与人工重排，并分析扩展生成数量时的多样性和LLM自评失效。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p1: 'we design a carefully controlled comparison of human and LLM ideas'；p2 Figure 1 列出 Human、AI、AI+Human Rerank 三条件；p3: 'same set of natural language instructions including the same topic description, idea template, and demonstration example'；p6: reviewers randomly assigned within selected topics and conditions balanced。 | 自变量为想法来源/条件，明确有 3 个水平并报告了生成与评审分配程序；但缺少针对各条件的正式操纵检验，p3 的 50% 区分准确率更接近风格匿名化检查，故记 0.5。 |
| A2 | 因变量 | 0.5 | p4: novelty, excitement, feasibility, expected effectiveness 与 overall，均 1-10 分并附自由文本理由；p8 Table 5 报告均值、SD、min/max；p9 报告 inter-reviewer agreement 56.1%；p23-26 给出完整评审量表定义。 | 因变量指标与计分方式明确，并报告评审者一致性及量表锚点；但缺少正式内部一致性/效度证据，也未系统说明连续指标预处理或天花板/地板效应。 |
| A3 | 控制变量 | 1 | p3: 'standardize the styles of human and LLM ideas and match their topic distribution'；p3 报告相同 instruction/template/demo；p6: 'all ideas are anonymized' 且避免同机构作者评审。 | 系统列出并实施了主题匹配、写作风格标准化、统一说明与模板、匿名评审、避免同机构污染等控制手段，符合 1。 |
| A4 | 混淆变量 | 1 | p3 明确讨论 topic、writeup format、writing style、evaluation process 等潜在混淆及控制；p7-8 用三种统计检验处理评审/想法/评审者层面混淆；p9 讨论评审主观性；p15 讨论 human baseline 与 scope 局限。 | 识别了主要混淆并提出多重控制与敏感性/替代统计检验，同时讨论残余局限，符合 1。 |
| A5 | 调节变量 | NA | — | 论文没有提出调节变量假设，也没有以交互项为核心的调节分析；topic 仅作随机效应/描述性分解，不构成理论调节模型。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解，不适用。 |
| A7 | 操作性定义 | 1 | p3-4 说明想法写作模板、评审指标与评分锚点；p19 给出完整 project proposal template；p23-26 给出完整 review form；p4-5、p27 详细描述 ideation agent、RAG、去重、排序流程。 | 关键构念均有可复现的操作化程序：条件生成、写作模板、评审量表、评分锚点和代理流程均较明确，符合 1。 |
| A8 | 水平数与类型 | 0.5 | p2 Figure 1 列出三种条件：Human Ideas、AI Ideas、AI Ideas + Human Rerank；p6 说明评审者在条件间平衡分配。 | 水平数与各水平标签清楚，但未明确说明水平类型（名义/等级）、水平间距/全距；对分类条件这些项虽不关键，按严格完整性记 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p4 使用 novelty、excitement、feasibility、effectiveness、overall 五个指标；p9-10 另用多个 LLM evaluator 与人工评分比较；p15 讨论仅评估 idea 本身、未来需执行项目验证。 | 关键构念有多指标/多评审来源，并讨论单一想法评审的局限；但未系统报告各操作化之间的会聚证据，记 0.5。 |
| A10 | 单一方法的风险 | NA | — | 自变量来源为人类/LLM 生成，因变量来自独立的人类专家盲评，二者方法来源天然分离，无同源共同方法偏差问题。 |
| B1 | 被试间设计 | NA | p6: 'Each reviewer gets at least one human idea and one AI idea'；p37 Table 13 平均每位评审者评审 2.5 个条件。 | 评审者并非只接受一个条件，设计不是被试间设计；条件比较发生在想法层面并由同一评审者跨条件评价。 |
| B2 | 被试内设计 | 0.5 | p6: 评审者被分配 2 到 7 个想法，平均 3.8 个评审、2.5 个条件；p38 使用 reviewer 与 idea 随机效应。 | 存在评审者内的重复评审结构，但未报告评审条件呈现顺序的平衡方案或各顺序分配，故为部分满足。 |
| B3 | 混合设计 | 0.5 | p6 评审者跨 2-3 个条件评审；p38 LMM 将 condition 作固定效应，reviewer 与 idea 作方差成分/随机效应，并含 topic 随机斜率。 | 数据具混合结构并使用了混合模型，但方法部分未逐因素明确标注组间/组内属性，也未分别报告两类误差项，记 0.5。 |
| B4 | 因子设计 | NA | — | 核心设计为单因素三水平条件比较；topic 不是与条件完全交叉的实验因素，未构成因子设计。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应/交互结构，只有三条件比较；不适用。 |
| B6 | 交互作用 | NA | — | 未设定并检验条件间交互作用；topic 分解仅为描述性/随机效应。 |
| B7 | 区组设计 | NA | — | 未使用区组设计；topic 与 reviewer 以随机效应/分配平衡方式处理，不是传统区组变量。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方设计。 |
| B9 | 准实验设计 | 0.5 | p3 明确讨论并控制 topic、format、writing style 等潜在混淆；p6 随机分配评审并避免同机构；p15 讨论 human baseline 与仅评估 ideas 的局限。 | 想法来源无法像被试处理一样随机分配，研究采用匹配与标准化控制；但未明确报告准实验类型、选择偏差来源及因果推断限定，故记 0.5。 |
| B10 | 被试内设计的适用条件 | 0 | p6 显示同一评审者会评审多个条件；全文未讨论评审条件的可逆性/迁移对称性。 | 存在评审者内跨条件重复评价，但未论证处理可逆性或迁移对称性，也未说明缓解措施。 |
| C1 | 随机化 | 0.5 | p6: 'We then randomly assign them to ideas within their selected topics'，并平衡每个评审者的条件数量。 | 报告了随机分配与条件平衡，但未报告随机数生成工具、分配隐藏机制或随机化后基线均衡性检验。 |
| C2 | 平衡 | 0 | p6 说明按主题随机分配并在每个评审者内平衡条件；未报告条件呈现顺序的平衡方案。 | 有跨条件重复评价，但未报告顺序平衡方案及各顺序分配，无法排除顺序效应。 |
| C3 | 恒定 | 1 | p3 所有参与者使用相同 instruction/template/demo；p4 代理使用 claude-3-5-sonnet-20240620；p4 统一 review form；p15 讨论仅限 prompting-based NLP 的外部效度局限。 | 明确列出统一模板、统一量表、固定代理模型版本等恒定条件，并讨论范围局限，符合 1。 |
| C4 | 匹配 | 0.5 | p3: 'for each selected topic, we generate a corresponding LLM idea. This exactly matches the idea topic distribution'；p3 使用 LLM style normalization。 | 报告了主题匹配与风格标准化，但未正式报告匹配后均衡性检验或回归假象讨论；按部分满足记 0.5。 |
| C5 | 纳入为变量 | 0.5 | p38 LMM：Score ~ Condition，Topic 随机截距与 Condition 随机斜率，ReviewerID 与 IdeaID 方差成分；p39 Table 16 报告系数、SE、p 与方差成分。 | 已知混淆（topic/reviewer/idea）被纳入混合模型并报告调整后系数；但未检验协变量斜率齐性等假设，也未报告效应量置信区间，记 0.5。 |
| C6 | 盲法 | 1 | p3: 所有想法经 style normalization，且小规模人类研究中专家区分 AI/人类想法的准确率仅 50%；p6: 'all ideas are anonymized'。 | 评审者盲于想法来源，匿名化与风格标准化实施明确，并有区分准确率检查，符合 1。 |
| C7 | 平衡的层级 | 0 | p6 仅报告随机分配与条件数量平衡，未报告完全平衡/拉丁方/ABBA 等顺序平衡层级。 | 存在评审顺序效应风险，但未明确所选平衡层级、构造方法或顺序效应形状假设。 |
| D1 | 练习效应 | 0 | p6 评审者被分配 2 到 7 个想法；全文无练习块、截除初段试次或试次位置协变量报告。 | 跨多个想法的评审可能有练习/熟悉化效应，但未报告任何练习控制。 |
| D2 | 疲劳效应 | 0.5 | p6: 评审者有一周时间完成评审，平均 3.8 个 reviews；p7 Table 4 报告每次评审平均 31.7 分钟、长度等。 | 报告了部分工作量与单次时长，但未报告休息间隔、单 session 总时长及条件时间分散方案，记 0.5。 |
| D3 | 延滞 / 迁移效应 | 0 | p6 同一评审者评审多个条件；p38 模型未包含条件对/顺序项，全文未讨论清洗期或跨条件残留。 | 跨条件连续评审可能存在对比/迁移，但未识别迁移效应、未设置清洗期、未将条件对建模。 |
| D4 | 不对称迁移 | 0 | 全文未报告迁移对称性检验或顺序×条件交互分析。 | 存在跨条件重复评价但假设迁移对称且未检验，亦未讨论平衡失效风险。 |
| D5 | 范围效应 | 0.5 | p4 与 p23-26 使用 1-10 分量表，并为每个分数点提供明确文字锚点；但未讨论范围效应或做被试间对照。 | 采用了较明确的绝对锚定量表，降低部分范围效应；但未识别范围效应风险、未做被试间对照，记 0.5。 |
| E1 | 位置 / 顺序偏差 | 0 | p6 评审者被随机分配到所选主题下的想法；未报告想法呈现顺序的随机化或反平衡。 | 有多个刺激/想法连续呈现，但未做或未报告呈现顺序控制，存在位置/顺序偏差风险。 |
| E2 | 默认赞同 | NA | — | 研究使用单条目 1-10 分评审量表而非 Likert/态度多题量表，无反向计分题适用性。 |
| E3 | 极端 / 中间反应倾向 | 0.5 | p8 Table 5 与 p37 Table 14 报告各条件均值、SD、min/max；未报告偏度、端点/中点使用比例或反应风格校正。 | 提供了部分分布信息（均值/SD/极值），但未系统检查极端/中间反应倾向，也未讨论其对条件比较的威胁。 |
| E4 | 需求特征 | 0.5 | p3 使用 style normalization，小规模检查中专家区分 AI/人类想法仅 50%；p6 所有想法匿名化。 | 采用盲法/匿名化降低需求特征，并报告了区分准确率检查；但无正式事后访谈中推断研究假设比例及 debriefing 流程。 |
| E5 | 实验者效应 | 0.5 | p3 与 p6 表明评审者对想法来源盲；p4、p23-26 提供标准化评审表与评分定义。 | 报告了评审者盲法与标准化量表，但未说明主试/评分者人数、培训标准化或脚本化程度。 |
| E6 | 天花板 / 地板效应 | 0.5 | p8 Table 5 报告各条件均值、SD、min/max；p37 Table 14 同样报告；未报告偏度/端点频率或 pilot 难度校准。 | 均值与极值显示评分未明显贴近端点，但缺少正式天花板/地板效应分析与任务难度校准，记 0.5。 |
| E7 | 共同方法偏差 | NA | — | 自变量为想法来源，因变量为独立人类评审者的评分，来源分离，不构成同源自评共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | p8 Table 5、p37 Table 15、p39 Table 16 报告均值、SD、p 值、Bonferroni 校正及 LMM 系数/SE；未报告事前功效、效应量置信区间或样本量依据。 | 报告了主要分析、多重校正与部分效应信息，但缺少功效分析与正式 CI/效应量，记 0.5。 |
| F2 | 内部效度 | 0.5 | p6 描述随机分配评审、平衡条件、避免同机构；p32 报告原始 50 个人类想法中剔除 1 个；但无分配隐藏、基线等价性检验或被试流向图。 | 内部效度控制有随机分配和剔除记录，但关键分配隐藏/基线/损耗流程信息不完整。 |
| F3 | 构念效度 | 0.5 | p4 与 p23-26 提供评审指标定义及锚点；p9 报告 inter-reviewer agreement 56.1%，并与 NeurIPS/ICLR 比较；但无正式内部一致性、效度检验或操纵检验。 | 有内容定义、评审者间一致性与评审质量统计，但信效度证据不完整，单一指标局限讨论也有限。 |
| F4 | 外部效度 | 0.5 | p6 报告招募渠道、49 位作者来自 26 个机构、79 位评审者来自 32 个机构及资历统计；p15 明确研究限于 NLP prompting-based research。 | 样本来源与特征报告充分，并讨论范围边界；但无跨样本/跨情境复现，推广边界仍有限，记 0.5。 |
| G1 | 分析单位 | 1 | p7-8 明确区分 Test 1 以 review 为独立点、Test 2 以 idea 为独立点、Test 3 以 reviewer 为独立点；p38 使用 LMM 处理 topic/reviewer/idea 层级结构。 | 论文明确讨论处理/分析单位及非独立性，并用混合模型分离 reviewer 与 idea 方差，符合 1。 |
| G2 | 随机效应 | 1 | p38: model = smf.mixedlm('Score ~ Condition', groups=Topic, re_formula='~Condition', vc_formula={'ReviewerID':..., 'IdeaID':...})；p39 Table 16 报告方差成分。 | 明确 condition 为固定效应，topic 随机截距/随机斜率，reviewer 与 idea 为随机方差成分，结构报告完整。 |
| G3 | 材料作为随机效应 | 1 | p38 LMM 将 IdeaID 作为 variance component；p39 Table 16 报告 Idea Var。 | 想法被视为从更大想法总体抽样并纳入随机效应，使结论不局限于 49 个具体想法，符合 1。 |
| G4 | 统计功效 | 0 | p6 招募 N=49 idea writers、N=79 reviewers；全文无事前功效分析、样本量推导或效应量置信区间报告。 | 未报告设计阶段功效分析或其他样本量论证，亦缺少正式效应量/CI；虽有统计分析，不满足本组件。 |
| G5 | 研究者自由度 | 0.5 | p32 报告收集 50 个人类想法并剔除 1 个；p8 报告五个评审指标及三条件结果；主结果与 in-depth analysis/附录分析有一定区分，但未说明样本量决定/停止规则，也未明确标注验证性与探索性。 | 报告了排除规则与全部主要因变量/条件，但样本量决定方式和验证/探索分析区分不完整。 |
| G6 | 预先设定 / 预注册 | 0 | p15 仅说明未来 EMNLP 2024 比较研究 'We pre-registered our analysis plan'；当前主研究无预注册信息。 | 主研究未预注册，且未区分主研究的验证性与探索性分析，故记 0。 |
| J1 | 位置偏差 | 0 | p5 使用 pairwise comparisons 与 Swiss system tournament 进行 LLM 排序；未报告 A/B 交换、位置反平衡或交换前后偏好翻转率。 | 使用 LLM 成对判断但完全未涉及候选项位置控制，存在位置偏差风险。 |
| J2 | 冗长偏差 | 0 | p6 Table 3 显示 AI ideas 平均 1186.3 词、Human ideas 901.7 词；p5 LLM ranker 用于筛选；正文未报告长度—得分相关或长度控制 rubric。 | 使用 LLM 进行想法排序/评估且被评文本长度差异明显，但未对冗长偏差作控制或量化说明。 |
| J3 | 谄媚 | NA | — | 研究不涉及用户立场、反馈或多轮纠错对话，无谄媚偏差操纵场景。 |
| J4 | 自我偏好 | 0.5 | p4 代理 backbone 为 claude-3-5-sonnet-20240620；p5 使用 Claude-3.5-Sonnet 作 pairwise ranker；p10 Table 6 比较 GPT-4o、Claude-3.5 pairwise、AI Scientist reviewer 等，并报告各自准确率。 | 存在被评 AI 想法与裁判模型同源风险；论文使用多个异源 evaluator 并报告各自结果，但未明确量化自我偏好或报告同源裁判控制。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p4: 'We craft k = 6 demonstration examples' 并放入 idea generation prompt；p19-21 与 p28 给出模板/示例；p4 说明从 top-ranked papers 随机选 k=10 拼接。 | 报告了 few-shot 示例数量与来源，但未报告标签比例、排列反平衡、多示例集 seed 重复或完整生成 prompt。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p22 给出完整 style standardization prompt；p84-85 对检索论文数 N、k、base model、RAG/prev 等 prompt setup 做消融；但未报告 prompt 版本号、语义等价措辞敏感性或 dev/test 划分。 | 部分提示模板与多组 setup 消融公开，但缺少系统提示版本化、敏感性消融和测试集调参说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0 | p4 使用 RAG，保留 top k=20，最大 N=120 篇，选 k=10 篇标题/摘要加入 prompt；未报告实际 token 数、关键信息位置操纵或位置×正确率曲线。 | 存在 RAG 但未检查长上下文信息位置效应，也未报告上下文 token 量。 |
| J8 | 温度与采样随机性 | 0.5 | p4: 'prompt the LLM to generate 4000 seed ideas on each research topic'；p4 使用 claude-3-5-sonnet-20240620；p84: 'We use a temperature of 1.0 for all the generations'。 | 报告了 temperature、模型 snapshot 与大量重复生成；但未完整报告 top-p/top-k、seed、每条件重复采样置信区间。 |
| J9 | 重复与文本退化 | 0 | p4-5 报告基于 embedding 的去重，约 5% 非重复想法；未报告 greedy/beam/sampling 解码策略或 repetition penalty。 | 虽测量了重复/多样性，但未报告解码策略与退化控制，无法把重复率与解码设置区分。 |
| J10 | 分词效应 | NA | — | 实验为单语言英文研究想法生成与评审，不涉及跨语言/跨脚本 token 化比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p5 使用 1200 篇 ICLR 2024 LLM 相关投稿及 review scores/decisions 验证 ranker；未报告模型训练截止日期与 ICLR 2024 数据的重叠/污染检测。 | LLM ranker 验证使用公开 ICLR 2024 数据，存在训练记忆/污染风险，但未做任何污染检查；主人类评审虽为新生成想法，仍记 0。 |
| J12 | 基准饱和 | NA | — | 研究不是标准能力基准评测，不存在基准接近饱和后仍宣称微小提升的问题。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循准确率，未设置可机器判定的指令约束集。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p3 与 p19 使用固定 project proposal 模板；p22 使用 LLM style standardization；p3 表示作者人工核验内容保留，但未报告格式合法率/重试策略。 | 有结构化写作模板和格式标准化，但未把格式失败与内容错误分开报告，也未给格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 研究未评估模型安全性/越狱稳健性；Safety 只是研究想法主题之一，不是越狱测试。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究定位为 LLM 科研想法生成能力与人类专家比较的工程/应用评估，不主张把 LLM 作为心理学被试测量人类同名心理构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随模型规模/训练进展的能力曲线，也未宣称涌现。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | p5 使用 LLM ranker 作为代理筛选 top ideas；p8 用人类专家评审作为最终评价；p10 与 p32 Table 8 比较 AI ranker 与 human rerank 的重叠/得分差异。 | 有代理指标与独立人类评估的分离比较，但未报告随优化轮数变化的代理分数与真实人类分数双曲线，也未系统监控 overoptimization。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p4 报告 claude-3-5-sonnet-20240620；p1 声明释放 agent implementation 与所有人类 review scores；p10 Table 6 的 LLM evaluator 准确率为单点结果，未报告重复 N/CI/配对检验。 | 模型 snapshot 与数据发布较好，但 LLM 评估比较缺少重复次数、置信区间和配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究为单轮想法生成与评审，不涉及多轮对话一致性衰减。 |

## 编码小结
论文核心发现是 AI 想法在专家盲评中新颖性高于人类专家想法，其他指标大致相当；设计上对主题匹配、写作风格标准化、匿名评审和评审分配做了较系统的控制，并报告多种统计检验与混合模型。但若干人类评审顺序/疲劳/迁移控制、正式操纵检验、功效分析、预注册与 LLM 评估偏差控制报告不足；LLM 评审的自我偏好与长度偏差也未充分量化。
