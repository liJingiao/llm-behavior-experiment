# article_063 | Measuring Inductive Biases of In-Context Learning with Underspecified Demonstrations | 2023

研究类型概述：计算/行为基准评测：在二分类少样本 ICL 中构造两个特征同等预测标签的 underspecified demonstrations，以 disambiguating test set 上的 h-accuracy 衡量 GPT-3 系列模型的特征偏置，并比较语义 verbalizer、指令、解释、消歧示例等干预能否把偏置导向 h1 或 h2。分析单位为模型×干预×特征/数据集×随机提示集，非人类被试实验。
- **研究构念（Construct）**：上下文学习中的特征归纳偏置与表面线索依赖（feature-based inductive bias in in-context learning）｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：计算/行为基准评测：在二分类少样本 ICL 中构造两个特征同等预测标签的 underspecified demonstrations，以 disambiguating test set 上的 h-accuracy 衡量 GPT-3 系列模型的特征偏置，并比较语义 verbalizer、指令、解释、消歧示例等干预能否把偏置导向 h1 或 h2。分析单位为模型×干预×特征/数据集×随机提示集，非人类被试实验。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_6：列出 Baseline、Semantic verbalizer、Instruction、Explanation、Disambiguation 五种干预及构造方式；PDF_PAGE_4：模型为 TEXT-DAVINCI-002 与 DAVINCI。 | 干预类型与模型条件被明确命名，水平数和取值基本可辨；但未报告操纵检验，模型 checkpoint 也不是随机分配的自变量，故为部分满足。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_3：定义 h-accuracy = (1/&#124;Dtest&#124;) Σ 1[f(x)=h(x)]；PDF_PAGE_4：报告 1,200 个平衡测试样例、每个实验随机三个提示集并汇报平均表现。 | 因变量指标与计分方式清楚；但缺少正式信度/效度证据，只有随机提示集上的标准差，未系统说明连续指标预处理或信效度。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_3：'ordering the demonstration examples randomly and performing label calibration'；PDF_PAGE_4：所有实验使用 temperature 0，示范集 16 个且 8/8 平衡。 | 报告了若干控制变量及手段，如随机顺序、标签校准、固定温度；但未系统列出完整控制变量清单和控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_3：承认 ICL 对 demonstration 顺序、多数标签/近因偏差等敏感并称已控制；PDF_PAGE_5：模型差异 'may be due to some aspect of instruction tuning'；PDF_PAGE_9：限制部分讨论模型/任务覆盖。 | 识别并控制了顺序与标签偏差等潜在混淆，也提到指令微调解释不确定；但未系统报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | NA | — | 没有提出正式调节假设或调节分析；按特征/模型分层的差异属于描述性比较，不构成 A5 所需的交互检验与简单斜率设计。 |
| A6 | 中介变量 | NA | — | 没有中介变量、中介假设或直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_3：给出 ICL prompt 模板 t(x)=“Input: $x Label: ”、v(0)=“0”、v(1)=“1”；PDF_PAGE_6：说明 verbalizer、instruction、explanation、disambiguation 的构造；PDF_PAGE_16-20：完整列出 verbalizers、instructions、template explanations。 | 关键构念（特征函数、h-accuracy、干预）均有可复现的操作化程序，且代码/数据公开。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_4 Table 1：列出各数据集及默认/替代特征；PDF_PAGE_6：列出五种干预的水平；PDF_PAGE_4：两个 GPT-3 checkpoint。 | 水平数与各水平标签基本明确；但未逐变量明确名义/等级类型及连续变量的间距/全距/中心化说明，故部分满足。 |
| A9 | 单一操作化的风险 | 0.5 | PDF_PAGE_4：在 IMDb、Yelp、CivilComments、MultiNLI、BoolQ 上使用多组特征对；PDF_PAGE_9：Limitations 明确讨论 task coverage 和 feature coverage 仅限四类二分类任务与手工特征。 | 对特征偏置采用多数据集、多特征操作化；但未报告各操作间的会聚统计，仅以描述性结果呈现，且单一 h-accuracy 指标的局限讨论有限。 |
| A10 | 单一方法的风险 | NA | — | 研究为客观 LLM 输出评测，不涉及人类自陈式同源测量；共同方法偏差检验不作为适用要求。 |
| B1 | 被试间设计 | NA | — | 没有人类被试组或独立被试分配；所有条件在同一模型/提示集上评估，B1 的被试间逻辑不适用。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内设计或跨条件顺序安排；同一模型重复评估不等同于被试内条件顺序设计。 |
| B3 | 混合设计 | NA | — | 没有组间/组内人类被试因素的混合设计。 |
| B4 | 因子设计 | 0 | PDF_PAGE_6 Table 2：按模型和 steer 方向汇总各干预相对 baseline 的变化；PDF_PAGE_8 Table 3：按特征报告 h2-accuracy 与干预差值。 | 存在模型×干预×特征/数据集的多因素比较结构，并描述条件差异；但无完整设计矩阵、逐格样本量及 ANOVA 的 F/df/p/效应量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | PDF_PAGE_6 Table 2：报告 baseline 与各干预的平均 h1/h2-accuracy 变化；PDF_PAGE_7 Figure 3：按 steer 方向展示各干预。 | 可读取干预的主效应趋势与均值差，但未报告正式主效应统计量、效应量，也未在条件差异存在时明确限制主效应解释。 |
| B6 | 交互作用 | 0 | PDF_PAGE_7：指出干预效果取决于 'prior feature bias and the intended feature are aligned'；PDF_PAGE_8 Table 3：比较不同特征上的干预效果。 | 有描述性交互/条件效应模式，但未做正式交互检验、简单效应或多重比较校正，也无带误差棒的正式交互图；因未报告交互项的正式统计检验结果，按级联规则基本要件未达成记 0。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计；无需要控的前测或自然属性区组变量。 |
| B8 | 拉丁方 | NA | — | 没有被试内条件顺序设计，未使用拉丁方。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理分配研究；没有非随机分组与因果处理效应估计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 干预条件不在独立被试/单元间随机分配；示范随机抽样不等于处理分配随机化。 |
| C2 | 平衡 | NA | — | 各干预分开施加，条件顺序不构成需要平衡的顺序效应；示范顺序控制归入 E1/J5。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_4：'we use a temperature value of 0'、16 个 demonstrations、1,200 test examples，OpenAI API 于 2023 年 1 月调用；PDF_PAGE_9：讨论模型与任务覆盖限制。 | 报告了部分恒定变量及水平，并在局限中讨论外部效度；但未系统列出所有恒定变量及其水平。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组或协变量纳入统计模型；label calibration 是提示质量控制，不是 ANCOVA 协变量。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或评分者，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序，故无完全平衡/拉丁方/ABBA 层级选择。 |
| D1 | 练习效应 | NA | — | 每个 prompt 独立评估，无练习块、试次位置或跨时间练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session、疲劳或休息安排；模型调用不存在疲劳效应。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件以独立 prompt 评估，无跨条件清洗期或迁移残留问题。 |
| D4 | 不对称迁移 | NA | — | 无条件间迁移对称性检验需求；无跨处理残留。 |
| D5 | 范围效应 | NA | — | 不使用主观量表或绝对量值判断；h-accuracy 的范围限制归入 E6/天花板地板讨论。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_3：'ordering the demonstration examples randomly'；PDF_PAGE_4：每个实验随机抽取三个提示集。 | 对示范顺序做了随机化并重复 3 个提示集；但未报告每类示例在各位置出现次数、位置平衡细节或位置×表现曲线。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或事后访谈检查；LLM 提示实验不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_7 Figure 3 caption：'omit results for steering towards h1 on sentiment analysis since the baseline already has a near-perfect preference for h1 with little room for improvement'；PDF_PAGE_5 Figure 2：部分 h-accuracy 接近上限。 | 识别并规避了明显天花板情形，报告了均值和种子标准差；但未系统报告偏度/端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念测量，无同源自评共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_4：每个实验随机三个提示集、1,200 测试样例；PDF_PAGE_5 Figure 2：误差棒为三个随机种子的标准差；PDF_PAGE_6 Table 2：报告准确率变化。 | 报告了均值差和种子间 SD，可视为不确定性信息；但缺少样本量功效依据、95%CI、正式效应量和多重性校正。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_4：balanced 16 个示范、随机三个提示集、1,200 平衡测试样例；PDF_PAGE_3：随机顺序与 label calibration。 | 对提示抽样、标签平衡和顺序进行了控制，但无人类分配隐藏/基线等价/流失问题；内部效度讨论不完整。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_3：以 h1/h2 accuracy 差行为化 feature bias；PDF_PAGE_9：承认仅使用二分类手工特征，h-accuracy 比较学习函数与特征函数预测。 | 构念操作化与指标对应关系较清楚；但无正式信度/效度检验、无 manipulation check，讨论单一操作化局限。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_4：使用 IMDb、Yelp、CivilComments、MultiNLI、BoolQ；PDF_PAGE_9：Limitations 明确 model/task/feature coverage 边界。 | 报告了数据来源和部分推广边界；但未报告跨模型/跨任务系统复现矩阵或对真实用户分布的抽样代表性。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_4：每个实验随机采样 three sets of prompts，并在 1,200 个测试例上平均；PDF_PAGE_5：误差棒对应三个随机提示集。 | 说明了提示集抽样与聚合分析层级，但未用多层/混合模型显式处理测试例或提示集嵌套，只做均值与 SD。 |
| G2 | 随机效应 | 0.5 | PDF_PAGE_4：'randomly sample three sets of prompts'；PDF_PAGE_5：误差棒为三个随机种子的标准差。 | 体现了提示抽样随机变异，但未报告正式随机效应结构或固定/随机因子清单。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_4 Table 1：材料为多数据集、多手工特征对；PDF_PAGE_9：feature coverage 明确为手工特征集合的局限。 | 使用了多材料/多特征并讨论覆盖限制，但未将材料/项目作为随机效应纳入混合模型或准 F 检验。 |
| G4 | 统计功效 | 0 | PDF_PAGE_4 与 PDF_PAGE_6：描述样本/提示数量和结果，但全文未见事前功效分析、目标功效或预期效应量来源；结果主要报告均值与 SD，未报告 CI。 | 没有设计阶段功效分析或样本量论证，也没有正式效应量/CI；不满足 G4 基本要件。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_4：说明 16 个示范、三个提示集、1,200 测试样例；PDF_PAGE_7：明确因天花板省略 sentiment 的 steer-towards-h1 结果；附录 PDF_PAGE_13-20 给出完整干预模板。 | 报告了较多条件与省略理由，但未系统给出试次/样本排除规则、停止规则，也未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | PDF_PAGE_4、PDF_PAGE_9 及全文未出现预注册平台、注册编号或分析计划； PDF_PAGE_21-22 的 ACL checklist 也未提及预注册。 | 无公开预注册，未区分预注册验证性与事后探索性分析。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项位置选择、排序或 LLM-as-judge 成对比较；模型是按标签 verbalizer 概率预测 0/1。 |
| J2 | 冗长偏差 | NA | — | 不是开放生成长短质量评估，长度偏差不构成本研究的主要评估风险。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或多轮纠错框架，不测量谄媚。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 作为裁判评估模型输出。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | PDF_PAGE_4：每个实验随机采样 balanced set of 16 demonstrations，8 个 y=0、8 个 y=1，'randomly shuffled'，并随机三个提示集报告平均；PDF_PAGE_3：进行 label calibration；PDF_PAGE_16-20：提供 verbalizer/instruction/explanation 模板。 | 示例来源、数量、类别比例、随机顺序与三个提示集均值/SD 均有报告；但未明确报告系统性顺序反平衡、每位置出现次数或逐位置分析，故部分满足。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_6：说明 instruction/explanation/verbalizer 格式；PDF_PAGE_16-20：列出所有模板；PDF_PAGE_4：temperature 0、OpenAI API 2023 年 1 月。 | 提供了较完整 prompt 模板和代码链接，但未做 prompt 措辞/格式敏感性消融，也未明确 dev/test 分离与版本迭代记录。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文仅为 16 个示范，远低于长上下文/RAG 场景，无中间迷失或信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_4：'we use a temperature value of 0'，OpenAI API 调用在 2023 年 1 月；每个实验三个随机提示集。 | 报告了 temperature、API 时间和重复提示集；但未报告 top-p/top-k、最大生成长度、精确 snapshot、重复采样 CI 或 seed 值。 |
| J9 | 重复与文本退化 | NA | — | 任务为短标签分类/概率评分，不涉及开放生成退化；解码策略对重复文本影响不适用。 |
| J10 | 分词效应 | NA | — | 实验为英文单语、单脚本数据集，无跨语言/跨脚本 tokenization 比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_4：使用 IMDb、Yelp、CivilComments、MultiNLI、BoolQ 等公开数据集，并说明 OpenAI API 于 2023 年 1 月调用；全文未报告训练截止日期对照或污染检测。 | 使用公开基准/数据而未评估预训练数据重叠，不能排除记忆污染；不满足 J11 基本要件。 |
| J12 | 基准饱和 | 0.5 | PDF_PAGE_7 Figure 3 caption：因 baseline 对 sentiment h1 已近完美而省略 steer-towards-h1；PDF_PAGE_5 Figure 2：部分条件接近 100%。 | 识别到部分条件下存在天花板并省略结果，但未系统改用连续指标或 bootstrap CI 比较，也未报告 SOTA 量程位置。 |
| J13 | 指令遵循 | NA | — | 因变量为特征偏置/h-accuracy，不是指令遵循测量；指令仅作为干预。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 通过标签词概率 argmax 评分，不涉及需解析的结构化自由生成或格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或拒绝率评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究定位为 LLM/ICL 的计算行为分析与 NLP 任务评估，不主张把模型作为人类心理学被试或外推人类心理学结论。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 仅比较两个 GPT-3 checkpoint，未报告随规模/训练进展的能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对代理指标进行训练、RL、best-of-N 等优化；是静态评测而非优化过程监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_4：模型为 TEXT-DAVINCI-002/DAVINCI，temperature 0，API 于 2023 年 1 月调用；PDF_PAGE_5：误差棒为三个随机提示集的标准差；PDF_PAGE_1：代码和数据公开链接。 | 报告了重复提示集、模型名称、API 时间和数据/代码；但缺少精确 API snapshot/commit hash、95%CI、配对检验和逐题日志，snapshot 标识不够精确。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮 ICL prompt 评估，无多轮对话历史累积。 |

## 编码小结
论文对 ICL 特征偏置的操作化、提示构造和干预定义较清楚，提供数据、代码链接及大量附录模板；但统计分析以均值、差值、3 个随机提示集上的 SD 为主，缺少正式交互/主效应检验、CI、功效分析、预注册、污染检测、精确 API snapshot 和系统提示敏感性分析。大量人类被试分配、顺序平衡、盲法、自陈量表等组件对本研究不适用，应记 NA 而非 0。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B6（0.5→0）, B4（0.5→0）。
