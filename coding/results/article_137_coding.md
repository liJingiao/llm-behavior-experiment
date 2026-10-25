# article_137 | When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners | 2025

研究类型概述：这是一项面向LLM内部表征的机制干预与多语言基准评估研究：在推理时从隐藏状态中投影去除语言特定子空间，并在10个开放权重LLM、11种语言、3个多语言推理基准上比较干预前后准确率，另含层级/消融强度分析与SFT/RL对照。分析单位为模型—基准—语言下的题目聚合准确率，不是人类被试实验。
- **研究构念（Construct）**：语言加工与推理过程的功能分离及跨语言迁移｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：从11种语言样本的隐藏状态经SVD提取语言特异子空间，在10个现成开放权重模型推理时投影移除该子空间，跨MGSM等三项任务和层位置测量推理准确率与输出语言保持。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.3: “ĥ = h − λM_s^T M_s h”；p.27: “we perform a grid search to find the best results, applying a λ in the range of 0 to 0.4 at the middle layers and -0.4 to 0 at the higher layers.” | 自变量可识别为是否进行L-R disentanglement及λ/层位；有干预方程与部分水平范围，并用PCA和language fidelity做机制验证。但未逐模型报告最终选定的λ、完整分配与操纵检验统计，故为0.5。 |
| A2 | 因变量 | 0.5 | p.5: “We use Accuracy as the evaluation metric for all benchmarks”；同页表注：“The values in parentheses indicate language fidelity.” | 因变量指标与计分方式（accuracy、language fidelity）明确，但未报告测量信效度、题目/评分者信度、连续指标预处理及天花板/地板说明，故为0.5。 |
| A3 | 控制变量 | 0.5 | p.5: “For each model, we disentangle the language-specific components from mid-layer hidden states and then re-inject them at higher layers”；p.28 Table 4列出各模型middle/higher layer ranges。 | 报告了固定层段、模型与基准等部分控制做法，但未系统列出采样参数、prompt、随机种子等控制变量及控制手段，故为0.5。 |
| A4 | 混淆变量 | 0.5 | p.24: “we also observe a degradation in language fidelity, especially when intervention is applied in higher layers”；p.10: “the exact causes remain opaque due to the lack of transparency in model training data.” | 识别了层位/语言保真度权衡及预训练数据不透明等潜在混淆，并做层级分析；但未系统报告残余混淆控制或敏感性分析，故为0.5。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量理论模型，也没有乘积项交互检验、中心化/标准化或简单斜率分析；跨语言/跨模型差异仅作描述性比较，故NA。 |
| A6 | 中介变量 | NA | — | 论文不包含中介变量或直接/间接效应分解，故NA。 |
| A7 | 操作性定义 | 0.5 | p.3: 投影消融公式（Eq.3）；p.25: Algorithm 1给出language subspace probing流程；p.5: 说明accuracy与language fidelity。 | 核心构念有可执行的操作化描述（子空间提取、投影消融、准确率/保真度），但prompt模板、最终λ/层位选择等复现关键细节未在正文完整给出，故为0.5。 |
| A8 | 水平数与类型 | 0.5 | p.3: “λ is a coefficient to control the ablation strength”；p.27: λ范围0–0.4与−0.4–0；p.28 Table 4列出层级区间。 | 报告了部分水平/取值与类型线索（baseline vs ablation、连续λ、层位），但缺完整水平间距、全距及连续变量中心化说明，故为0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.5: 三个benchmarks（MGSM、XWinograd、M-MMLU）；p.4: PCA与language fidelity验证；p.24: 讨论层位与语言保真度权衡。 | 用多个任务/模型/指标提供会聚证据，但核心干预仍主要是单一操作化，且未系统讨论单一操作化对构念推广的限制，故为0.5。 |
| A10 | 单一方法的风险 | NA | — | 研究不依赖同源自陈量表；IV为激活干预，DV为基准准确率/语言识别指标，不存在人类问卷式共同方法偏差问题，故NA。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配；同一模型与题目在baseline与干预条件下比较，不构成被试间设计，故NA。 |
| B2 | 被试内设计 | NA | — | 条件比较为同一模型/题目的独立推理评估；无跨条件时序或延续学习，也没有需要平衡的被试内条件顺序，故NA。 |
| B3 | 混合设计 | NA | — | 不是组间/组内因素混合的人类实验设计，未按混合设计建模，故NA。 |
| B4 | 因子设计 | NA | — | 研究虽跨模型/语言/基准报告结果，但未以ANOVA/因子设计矩阵和交互项组织分析，故不按因子设计编码，NA。 |
| B5 | 主效应 | NA | — | 未报告因子设计意义下的主效应统计检验（F、df、p、效应量），故NA。 |
| B6 | 交互作用 | NA | — | 未报告正式交互检验与简单主效应；跨语言/模型差异为描述性比较，故NA。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计，故NA。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计，故NA。 |
| B9 | 准实验设计 | NA | — | 不是准实验研究；无自然分组/非随机分配的人类或现场实验结构，故NA。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及人类被试内处理的不可逆性/迁移对称性问题，故NA。 |
| C1 | 随机化 | NA | — | 基准题目并未被随机分配到互斥条件；同一模型/题目在baseline与干预下评估，不存在人类式随机分配，故NA。 |
| C2 | 平衡 | NA | — | 无条件顺序平衡问题；各条件为独立推理运行，故NA。 |
| C3 | 恒定 | 0.5 | p.5: “disentangle ... from mid-layer hidden states and then re-inject them at higher layers”；p.28 Table 4: exact layer ranges。 | 报告了固定层段/模型/基准等部分恒定设置，但未系统列出解码、prompt、硬件/版本等恒定变量及其外部效度限制，故为0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配设计，故NA。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组或协变量纳入统计模型，故NA。 |
| C6 | 盲法 | NA | — | 评估为自动化基准评分，无人类被试/评分者盲法安排，故NA。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级需要报告，故NA。 |
| D1 | 练习效应 | NA | — | 基准题目独立推理，无练习块或上下文内学习设计；不存在人类式练习效应控制问题，故NA。 |
| D2 | 疲劳效应 | NA | — | 无人类session、休息间隔或疲劳控制问题，故NA。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立推理调用，无跨条件残留/清洗期问题，故NA。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性需要检验，故NA。 |
| D5 | 范围效应 | NA | — | 因变量为客观准确率/语言识别指标，不是绝对判断或量表评分，故NA。 |
| E1 | 位置 / 顺序偏差 | 0 | p.26: XWinograd “formulated as a fill-in-a-blank task with binary options”；M-MMLU为“multiple-choice questions”。全文未报告选项顺序随机化或反平衡。 | 存在多选/二选一刺激，选项位置偏差风险实际存在；论文未报告任何选项顺序随机化/反平衡方案，核心做法缺失，故为0。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表，故NA。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较，故NA。 |
| E4 | 需求特征 | NA | — | 无人类被试，无法合理产生人类式需求特征；未使用掩饰情节，故NA。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集与评分，无人类主试/评分者期望效应，故NA。 |
| E6 | 天花板 / 地板效应 | 0 | p.5 Table 1显示高分语言接近上限，如Qwen-3-8B-Thinking English 96.4、QwQ-32B English 95.6并提升至97.6；正文未报告偏度、端点频率或任务难度校准。 | 因变量存在明显高分/接近天花板风险，但未报告分布形态、端点频率、SD或任务难度校准，未讨论天花板/地板对内部效度的影响，故为0。 |
| E7 | 共同方法偏差 | NA | — | IV为激活干预，DV为客观基准准确率/语言识别；不存在同源自评式共同方法偏差，故NA。 |
| F1 | 统计结论效度 | 0 | p.27: “We conduct significance tests ... showing ... statistically significant gains (p < 0.05) on most benchmarks.” 正文/表格未报告效应量或95% CI，也未报告样本量与功效依据。 | 仅报告部分p<0.05结论，基本要件“效应量或置信区间”未达成；无功效分析、无多重性校正说明，故为0。 |
| F2 | 内部效度 | 0.5 | p.5 Table 1在同一模型上给出baseline与+L-R Disentangle结果；p.27仅说明λ网格搜索。 | 同模型同基准的baseline对照提供一定基线等价性，但未报告随机分配/分配隐藏（LLM评估中不适用）之外的内部效度威胁评估、流程与敏感性分析，故为0.5。 |
| F3 | 构念效度 | 0.5 | p.4: PCA与language fidelity用于验证removed components的“linguistic nature”；p.5: 多基准accuracy。未报告工具信度/效度统计。 | 有机制操纵检验与多基准证据，但缺关键测量的信度/效度报告及单一操作化局限的系统讨论，故为0.5。 |
| F4 | 外部效度 | 0.5 | p.5: 10 open-weight LLMs、11 languages、3 benchmarks；p.34: 追加PolyMath。 | 报告了模型、语言、基准来源与跨模型/跨任务复现，但未论证对闭源模型/其他任务/真实部署情境的代表性与明确推广边界，故为0.5。 |
| G1 | 分析单位 | 0 | p.5 Table 1按模型、语言报告聚合accuracy；正文未说明题目/语言/模型嵌套结构或分析层级。 | 处理施加于模型内部、评估在题目层面但分析使用聚合均值；未说明分配层级与统计层级匹配，也未用多层模型处理题目/语言嵌套，故为0。 |
| G2 | 随机效应 | 0 | p.5 Table 1将10个模型作为独立行报告；未描述混合模型或随机效应结构。 | 未说明哪些因子为随机/固定效应，模型被当作固定复制而非抽样总体；推断可推广范围不清，故为0。 |
| G3 | 材料作为随机效应 | 0 | p.26列出固定benchmarks（MGSM、XWinograd、M-MMLU），p.5报告聚合accuracy；未将题目/语言/材料作为随机效应建模。 | 使用有限基准题项与固定语言集，却仅按聚合准确率比较，未采用item/language随机效应或准F检验，存在材料固定效应问题，故为0。 |
| G4 | 统计功效 | 0 | p.27只报告“p < 0.05 on most benchmarks”；未报告事前功效分析、预期效应量、样本量/重复次数推导或效应量CI。 | 无设计阶段功效分析，也无结果部分效应量与CI，故为0。 |
| G5 | 研究者自由度 | 0.5 | p.27: “we perform a grid search to find the best results, applying a λ in the range of 0 to 0.4 ...”；主表报告选定后的最佳结果。 | 披露了λ网格搜索，但未完整报告所有搜索配置、最终选定规则、全部排除/停止规则，也未明确区分验证性与探索性分析，故为0.5。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未出现预注册平台、注册编号、样本停止规则或分析计划。 | 无预注册，且存在按基准网格搜索选最佳超参的做法；未区分验证性与探索性分析，故为0。 |
| J1 | 位置偏差 | 0 | p.26: XWinograd为“binary options”，M-MMLU为“multiple-choice questions”；全文未报告A/B交换、选项位置随机化或位置×正确率分析。 | LLM在多选/二选一基准中作答，候选位置偏差风险实际存在；未做任何位置反平衡或随机化报告，故为0。 |
| J2 | 冗长偏差 | NA | — | 评估为基准accuracy，不使用LLM裁判做开放生成质量/长短比较，故NA。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场、反馈或多轮纠错输入，不涉及谄媚操纵，故NA。 |
| J4 | 自我偏好 | NA | — | 不使用LLM-as-judge或成对偏好评估，故NA。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 正文未报告使用few-shot in-context示例；按标准基准评估处理，故NA。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p.5仅说明“implemented based on the vLLM framework”并使用benchmarks与accuracy；未提供prompt模板、版本号、敏感性消融或dev/test划分。 | 自定义推理prompt的完整模板和敏感性控制缺失，存在提示工程隐性自由度，故为0。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 任务上下文为短数学/常识/知识题，不涉及长文档/RAG或长上下文位置控制，故NA。 |
| J8 | 温度与采样随机性 | 0 | p.27只给出λ范围与网格搜索；未报告temperature、top-p、top-k、seed、每条件重复次数或置信区间。 | LLM非确定性作为统计随机源未纳入设计，无法复现采样条件，故为0。 |
| J9 | 重复与文本退化 | 0 | p.5/p.27未报告解码策略（greedy/beam/sampling）、repetition penalty、重复率或生成长度截断。 | 模型生成推理文本，但解码与文本退化控制未报告，故为0。 |
| J10 | 分词效应 | 0 | p.5: 选择11种语言跨语系评估；全文未报告tokenizer名称/revision或各语言token/词数比。 | 跨语言比较未控制分词长度，语言效应可能与token化效率混淆，故为0。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.5与p.26使用公开MGSM/XWinograd/M-MMLU/MATH/PolyMath；未报告测试集版本日期与模型训练截止日期对照或污染检测。 | 未做任何基准污染/数据泄漏检查，却把公开基准分数解释为多语言泛化能力，故为0。 |
| J12 | 基准饱和 | 0 | p.5 Table 1显示多个模型英语准确率约95–97，且干预后进一步提升；正文未讨论基准饱和或改用连续指标。 | 基准存在接近天花板风险，但未报告SOTA水位、CI比较或饱和应对，仍以小数点差异宣称提升，故为0。 |
| J13 | 指令遵循 | NA | — | 因变量为推理/知识准确率，不是指令遵循测量，故NA。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 实验不要求JSON/结构化格式输出，也未把格式失败作为独立指标，故NA。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全性、越狱或有害请求评估，故NA。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究为LLM机制干预与能力基准评估，人类认知神经科学仅作为动机，不主张测量与人类同名的心理学构念或把LLM作为心理学被试，故NA。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文比较多个模型规模但未报告跨规模/训练进展的能力曲线，也未宣称“涌现/突变”，故NA。 |
| J18 | 指标博弈与奖励过优化 | 0 | p.27: “we perform a grid search to find the best results, applying a λ in the range ...”；随后在相同基准上报告该最佳结果，未使用独立held-out评估监控调参过拟合。 | 优化对象（λ/层位网格搜索）与最终评估基准未分离，存在对代理准确率过优化风险且未画代理-真实双曲线，故为0。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.27仅称“statistically significant gains (p < 0.05)”；未报告每分数重复次数N、95% CI、精确snapshot、配对检验或原始推理日志。 | 评估可复现性所需重复、区间和精确模型标识不足，只有模型家族名称，故为0。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮基准推理，无多轮对话历史累积，也不主张多轮部署一致性，故NA。 |

## 编码小结
论文在跨模型、跨语言、跨基准上提供了较丰富的干预效应证据和一定的机制验证（PCA、language fidelity、层级/强度分析），但统计与可复现报告偏弱：未报告解码采样、重复次数、置信区间、精确模型snapshot、prompt模板与敏感性分析；超参与层选择使用同一基准网格搜索，存在测试集调优和研究者自由度风险；选项位置、分词长度、基准污染与饱和等LLM评估偏差基本未控制。
