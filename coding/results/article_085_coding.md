# article_085 | Enough Coin Flips Can Make LLMs Act Bayesian | 2025

研究类型概述：计算/LLM行为实验与基准式比较：在开源LLM上操纵显式偏差提示、ICL样例长度、模型家族/规模、切换点K与注意力分析，提取token概率并与贝叶斯后验比较；无人类被试。
- **研究构念（Construct）**：Bayesian belief updating、prior/evidence整合与概率判断｜CA 构念锚定：认知控制（cognitive control, `trm_4aae62e4ad209`）；注意（attention, `trm_4a3fd79d09902`）；干扰控制（interference control, `trm_551f11bb8f6a8`）
- **实验任务与范式（Task / Paradigm）**：计算/LLM行为实验与基准式比较：在开源LLM上操纵显式偏差提示、ICL样例长度、模型家族/规模、切换点K与注意力分析，提取token概率并与贝叶斯后验比较；无人类被试。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p5: 'When I flip coins, they land on heads X% of the time'; p5: 'providing the LLM with a sequence of samples from that distribution'; p5: ICL Length 1/3/5/10/20/100; p14 C.4: 50 result prompts and 5 instruct prompts. | 明确命名并给出多个操纵水平（偏差θ、ICL长度、模型/规模），但未报告操纵检验，分配方式也主要是固定条件而非随机分配，故为0.5。 |
| A2 | 因变量 | 0.5 | p4 Eq.12: TVD δ(p∗,p̂M)=1/2 Σ&#124;p∗(o)−p̂M(o)&#124;; p5 Fig.5 mean TVD vs bias for ICL lengths; p4 'renormalize the distribution over the support Ω'. | 因变量指标与计分方式（TVD、归一化token概率）明确，且报告均值与标准差；但无正式信效度证据，连续指标预处理/端点效应说明不充分。 |
| A3 | 控制变量 | 0.5 | p14 C.4: 'we normalize across a large set of 50 potential result prompts ... and 5 instruct prompts'; p3-p4: fixed support Ω and linear renormalization. | 报告了提示变体与归一化等控制手段，但未系统列出所有控制变量及逐一控制方式，故为0.5。 |
| A4 | 混淆变量 | 0.5 | p14 C.4: 'The specific prompt itself may have an impact ... To help alleviate this variance ... normalize across ... 50 potential result prompts'; p4: tokenization of [_tails] handled in Appendix C; p9 limitations discuss restricted posterior. | 识别并部分控制了提示措辞与tokenization等潜在混淆，但未系统给出残余混淆/敏感性分析对内部效度的威胁，故为0.5。 |
| A5 | 调节变量 | NA | p5 'Effect of model scale'; p6 'Does attention impact updates?' | 论文对模型规模/注意力作描述性比较或相关分析，未建立调节模型、乘积项交互检验或简单斜率分析；按规则记NA而非0。 |
| A6 | 中介变量 | NA | — | 全文无中介变量、直接/间接效应或中介模型。 |
| A7 | 操作性定义 | 1 | p3-p4: 定义 Bernoulli/Beta 后验、token序列概率式(10)-(12)与TVD；p13-p14 C.1-C.4: 给出outcome support、线性重归一化、chat template和50/5种提示；p14 Fig.C.1/C.2列出提示全文。 | 关键构念（偏差提示、ICL序列、模型token概率、贝叶斯后验与TVD）均给出可复现的操作化程序，达到1。 |
| A8 | 水平数与类型 | 0.5 | p5: ICL Length 1,3,5,10,20,100; p5: Pythia sizes 70M–12B; p6: K∈[10,90]; p14 C.4: 50 result prompts and 5 instruct prompts; p19 Fig.E.7: θ=0.00,0.10,...,1.00. | 报告了主要水平数与取值/范围，但未系统标注水平类型、间距/全距或连续变量中心化说明，故为0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p4 Fig.2 prior extraction; p6 Table 1 best-fit γ; p7 Fig.7 posterior trajectories; p18 Appendix G dice-rolling results 'correlate well' with coin results; p9 limitations discuss discrete/categorical predictions. | 使用多模型、多任务、多指标（TVD、γ、后验轨迹）但未正式报告各操作间会聚证据与系统单一操作局限，故为0.5。 |
| A10 | 单一方法的风险 | NA | p13 C.1: 'we extract this distribution directly from the language model'; p4 Eq.11-12. | 自变量是提示操纵，因变量是token-logit测量，非人类自陈同源，共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或被试组分配；模型不是在互斥条件间随机分配的被试。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量与条件顺序平衡设计；LLM提示条件按独立logit提取，不涉及被试顺序分配。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合设计及对应误差项。 |
| B4 | 因子设计 | NA | — | 论文按模型、偏差与ICL长度作图，但未建立正式完整因子设计、设计矩阵或ANOVA主效应/交互分析；按规则记NA。 |
| B5 | 主效应 | NA | — | 无正式因子设计的主效应检验（F、df、p、效应量）。 |
| B6 | 交互作用 | NA | — | 无正式交互项统计检验、简单主效应与多重比较校正。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 无准实验处理分配或选择偏差/因果推断设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内设计，故不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 固定模型与固定提示集，无随机分配/分配隐藏机制；不涉及单位到条件的随机化。 |
| C2 | 平衡 | NA | — | 无人类被试条件顺序，无平衡方案。 |
| C3 | 恒定 | 0.5 | p14 C.4: 50 result prompts and 5 instruct prompts; p13-p16 Appendix D lists exact open-source model identifiers and architectures; p9 limitations discuss closed-source exclusion. | 报告了模型、提示集和归一化流程等恒定控制，但未系统列出恒定变量及其具体水平与外部效度限制，故为0.5。 |
| C4 | 匹配 | NA | — | 无匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 无已知混淆变量作为区组/协变量纳入模型。 |
| C6 | 盲法 | NA | — | 全自动logit提取，无人类被试/主试/评分者盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级设计。 |
| D1 | 练习效应 | NA | — | 每个提示条件独立计算token概率，无人类练习块或跨条件学习；ICL长度是操纵变量而非练习阶段。 |
| D2 | 疲劳效应 | NA | — | 无人类session时长/疲劳问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留或清洗期；动态切换实验中的γ衰减建模属于序列内证据衰减，不是条件间迁移。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件顺序，故无迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | p14 C.4: 'normalize across a large set of 50 potential result prompts, and 5 instruct prompts'; p2 cites ICL 'ordering sensitivity' but no permutation/randomization of ICL example order is reported. | 虽然使用50种提示措辞变体，但未对ICL示例顺序/候选项位置做随机化或反平衡，也未报告位置×结果；故为0。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM自动实验，无人类需求特征/掩饰情节/事后访谈。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试或评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5 Fig.3/Fig.5 show mean TVD and shaded one SD; p5 discusses extremes 'instruct models showed improved performance at the extremes of bias values'; p9 limitations discuss restricted posterior slice. | 报告了均值/SD与部分极端条件表现，但未报告偏度、端点频率或pilot难度校准，故为0.5。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念测量，共同方法偏差的统计检验不适用。 |
| F1 | 统计结论效度 | 0.5 | p7: attention correlations 'θ1: (R=0.02,p=0.48), θ2: (R=−0.03,p=0.36)'; p5 Fig.3 shaded one SD; p5 Fig.5 mean TVD; no power analysis/CI reported. | 报告了部分效应量（R）与均值/SD，但缺样本量确定依据、95%CI、多重性校正及完整统计假设说明，故为0.5。 |
| F2 | 内部效度 | 0.5 | p14 C.4 prompt normalization across 50 variants; p9 limitations discuss restricted posterior and closed-source models; no random allocation/baseline equivalence/flow. | 有一定内部效度控制（提示变体平均）与局限讨论，但无随机分配、分配隐藏、基线等价或正式威胁评估，故为0.5。 |
| F3 | 构念效度 | 0.5 | p4 Eq.10-12 define model distribution and TVD; p4 Fig.2 prior extraction; p14 C.2-C.4 normalization and prompts; p9 limitations discuss discrete/categorical scope. | 构念操作化清晰且使用多提示/多模型，但无正式信效度统计、操纵检验或系统多操作化会聚分析，故为0.5。 |
| F4 | 外部效度 | 0.5 | p4 lists Gemma-2, Phi-2/Phi-3.5, Llama-3.1, Mistral-7B, OLMoE; p5 Pythia scaling suite; p9 limitations discuss closed-source and complex probabilistic environments. | 报告了模型来源与规模特征，并讨论边界，但未界定对LLM总体的代表性、未系统跨样本/跨情境复现，故为0.5。 |
| G1 | 分析单位 | 0.5 | p5 Fig.3: 'aggregated across prompts (N=50)'; p14 C.4 prompt normalization; p19 Fig.E.7 model-size × θ plots. | 分析单位是模型×提示/条件，并说明按50个提示聚合；但无多层模型分离提示/模型方差，故为0.5。 |
| G2 | 随机效应 | 0 | p4 Fig.2 model list; p5 Fig.6 Pythia sizes; p19 Fig.E.7 model-size plots; no mixed-effects/random-effects model reported. | 模型/规模作为固定类别或描述性分组，未将模型或提示作为随机效应；对LLM总体推断的可推广性未建模。 |
| G3 | 材料作为随机效应 | 0 | p14 C.4: 50 potential result prompts; p4 Fig.3 N=50; no item random effect or mixed model. | 提示被视为固定刺激集合，未在分析中作材料/项目随机效应，限制向任意提示总体的推广。 |
| G4 | 统计功效 | 0 | p5 Fig.3/Fig.5 report means/SD; p7 correlations report R,p; no a priori power analysis or sample-size justification. | 无设计阶段功效分析、目标功效/预期效应量，也未系统报告CI；仅报告p值/描述统计与部分R。 |
| G5 | 研究者自由度 | 0.5 | p4-p5 list multiple models and ICL lengths; p13 Appendix A says code will be released; p18 Appendix G reports additional dice-rolling results; no explicit exclusion rules or confirmatory/exploratory labeling. | 报告了较多条件与模型并承诺代码，但未报告数据排除规则、样本量决定方式，也未区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–23 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 无预注册平台、注册号或数据收集前分析计划；属未预注册研究。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或LLM-as-judge成对比较；未操纵候选位置。 |
| J2 | 冗长偏差 | NA | — | 无LLM裁判或开放性生成长短比较。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈/纠错或多轮谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 无LLM-as-judge评估。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p5: 'provide the LLM with a sequence of samples from that distribution'; p5 Fig.5 ICL lengths 1,3,5,10,20,100; p7 Fig.5/Appendix E additional ICL length results. | 使用few-shot/ICL示例并报告长度与来源为Bernoulli样本，但未报告多seed重采样、排列反平衡或每类示例比例的完整细节，故为0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p14 C.4: 'normalize across a large set of 50 potential result prompts ... and 5 instruct prompts'; p15 Fig.C.1 and Fig.C.2 provide prompt lists; no version dates/dev-test split. | 提供了较完整提示模板并跨50种措辞平均，具有一定敏感性控制；但无版本管理、dev/test划分与正式消融，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短ICL序列（最多100例），非长文档/RAG；未操纵长上下文信息位置。 |
| J8 | 温度与采样随机性 | NA | p13 C.1: 'we found that sampling was often unreliable, and thus, we extract this distribution directly from the language model' | 直接提取token概率/logit，不使用温度采样或生成式解码，故采样超参/seed编码不适用。 |
| J9 | 重复与文本退化 | NA | — | 不涉及开放生成或重复/退化文本；输出为固定outcome的token概率。 |
| J10 | 分词效应 | NA | — | 单一英语、单脚本实验，无跨语言/跨格式分词效率比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 使用自建coin-flip/ICL提示与生成的Bernoulli结果，不是公开基准测试集；未主张固定测试集泛化分数。 |
| J12 | 基准饱和 | NA | — | 不是基准SOTA比较，无基准饱和/提升宣称；TVD虽有下界但未作饱和推断。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，无约束指令准确率测量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化JSON/文法约束输出；仅计算固定outcome的token概率。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p4: 'we are not claiming that LLMs themselves are explicitly Bayesian ... do model predictive distributions have Bayesian behavior?'; p4: 'treat models themselves as point-wise estimators'; p9 discusses LLM-as-world-model and limitations. | 明确讨论LLM上所测贝叶斯行为与人类/规范贝叶斯构念的关系，并避免直接声称模型内部即贝叶斯；但无人类同范式对照实验，模型快照也不够精确，故为0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p5 Fig.6 and p19 Fig.E.7: TVD (continuous) across Pythia sizes for θ=0.00,...,1.00 and ICL lengths; p5: 'model scale has negligible impact on order dynamics'; no multi-seed/CI emergence test. | 报告了连续TVD规模曲线且未作突变/涌现宣称，但缺多seed曲线与置信区间，故为0.5。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL、best-of-N或对代理指标的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5 Fig.3: 'aggregated across prompts (N=50)' with one SD; p13-p16 Appendix D gives model identifiers; no commit hash/API date/CI/paired test. | 报告了提示重复数N=50与开源模型名称，但缺精确snapshot、bootstrap CI、配对检验和原始推理日志，故为0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮提示/单次序列补全，无多轮对话历史累积。 |

## 编码小结
论文对核心变量、token概率提取和贝叶斯后验比较的操作化较清晰，且提供了50种提示变体与多种模型/任务结果；但随机化、盲法、预注册、功效分析、正式随机效应与部分统计报告不足。大量人类被试特有的分配/顺序组件不适用，LLM特定风险中覆盖了提示敏感性、few-shot与可复现性，但未覆盖裁判类、安全类与多轮类风险。
