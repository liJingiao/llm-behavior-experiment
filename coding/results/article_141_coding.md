# article_141 | Do LLMs dream of elephants (when told not to)? Latent concept association and associative memory in transformers | 2024

研究类型概述：混合型研究：一方面在GPT-2、Gemma、LLaMA-2等开源LLM上用COUNTERFACT数据集做上下文劫持/事实检索扰动实验，报告Efficacy Score；另一方面提出合成latent concept association任务，对单层transformer进行理论分析与训练/冻结权重、维度、上下文长度等条件比较。分析单位为LLM样本/合成训练运行，不是人类被试。
- **研究构念（Construct）**：联想记忆中的线索依赖提取、上下文劫持与事实回忆干扰｜CA 构念锚定：回忆（recall, `trm_4a3fd79d0b95b`）；记忆提取（memory retrieval, `trm_4a3fd79d0ba01`）；长时记忆（long-term memory, `trm_4a3fd79d0a833`）
- **实验任务与范式（Task / Paradigm）**：在COUNTERFACT事实提示前加入通用或关系特异的虚假目标线索，重复增加提示次数，测试GPT-2、Gemma和LLaMA-2输出真实或错误事实的概率。（改变劫持线索类型、重复次数、关系、模型家族和规模。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4（p.4）：'Here, we prepend the hijacking sentence k times for k = 0, . . . , 5'；p.28（p.28）：'default setup has ω = 0.5, β = 1 and N (i) = V \ {i} and L = 256'，并比较fixed/trained value matrix等条件。 | 明确命名并操纵了prepend次数、hijacking scheme、模型以及合成实验中的W_V/embedding训练条件、维度、上下文长度等，且给出至少两个水平。但未报告操纵检验，LLM条件分配的单元逻辑也不完整，故为0.5。 |
| A2 | 因变量 | 0.5 | p.4（p.4）：'we report the Efficacy Score (ES)... the proportion of samples for which the token probabilities satisfy Pr[o_] > Pr[o*]'；p.6（p.6）：'accuracy is 1 − R_DL(f)'。 | 因变量指标和计分方式明确，但未报告信度/效度证据，也未说明连续指标预处理或天花板/地板控制，故为0.5。 |
| A3 | 控制变量 | 0.5 | p.4（p.4）：所有模型均在COUNTERFACT数据集上比较；p.27-28（p.27、p.28）：默认ω=0.5、β=1、L=256、hidden dimension=256、AdamW、learning rate from {0.01,0.001}。 | 报告了若干保持恒定的数据集与默认超参数，但未系统列出全部控制变量和控制手段，故为0.5。 |
| A4 | 混淆变量 | 0.5 | p.3-4（p.3、p.4）：'Due to the different capacities and capabilties of each model, the examples in Figure 1 use different hijacking techniques'；p.17（p.17）limitations仅讨论开源模型与单层transformer。 | 意识到模型能力/攻击方式差异可能影响结果，但未系统控制该潜在混淆，也未报告残余混淆或敏感性分析，故为0.5。 |
| A5 | 调节变量 | NA | — | 理论模型与实验均未提出或检验调节变量，不适用。 |
| A6 | 中介变量 | NA | — | 未提出中介假设，也未做直接/间接效应分解，不适用。 |
| A7 | 操作性定义 | 1 | p.4（p.4）给出prepend文本与ES计分；p.5（p.5）形式化latent concept association的生成过程；p.6（p.6）给出训练目标与error rate定义。 | 关键构念和主要操作化程序有明确、可复现的定义与计分方式，达到1。 |
| A8 | 水平数与类型 | 0.5 | p.4（p.4）：k=0,...,5；p.25（p.25）：Table 1/2列出P190、P103、P641、P131等关系；p.28（p.28）：m、d、L等实验水平。 | 报告了多个条件及其取值/标签，但未系统说明水平类型、间距/全距或连续变量的中心化处理，故为0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.4（p.4）generic hijacking与relation-ID hijacking；p.25-26（p.25、p.26）reverse hijacking与语义接近词；p.26（p.26）：'context hijacking does not require exact target word'。 | 对上下文劫持采用了多种操作化并显示相似趋势，但未报告正式的会聚证据或量化一致性，故为0.5。 |
| A10 | 单一方法的风险 | NA | — | 研究不涉及人类自陈量表或同源自评，共同方法偏差问题不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试组，也不存在把独立被试分配到条件的问题；LLM样本/数据集不是被试间分配单元。 |
| B2 | 被试内设计 | NA | — | LLM不同prepend条件是对同一数据集/模型的重复评估，不是需按被试顺序平衡的被试内实验；合成实验也非被试内重复测量设计。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合因素设计，不适用。 |
| B4 | 因子设计 | NA | — | 虽比较模型、prepend次数、维度等条件，但未建立需报告设计矩阵与交互项的正式因子实验/ANOVA设计。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应ANOVA检验，不适用。 |
| B6 | 交互作用 | NA | — | 没有正式交互项检验与简单主效应分析，不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 并非人类准实验中的非随机分组设计；模型比较不是以选择偏差推断处理效应的准实验。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥条件的程序；LLM评估与合成训练条件不是随机分配单元。 |
| C2 | 平衡 | NA | — | 无人类被试条件顺序，也没有需平衡的呈现顺序。 |
| C3 | 恒定 | 0.5 | p.27-28（p.27、p.28）：默认ω=0.5、β=1、N(i)=V\{i}、L=256、hidden dimension=256、AdamW、learning rate from {0.01,0.001}；p.17（p.17）讨论open-source与single-layer局限。 | 列出了一些恒定设置，但未系统列出全部恒定变量及水平，也未充分讨论这些恒定设置对外部效度的限制，故为0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配/配对程序。 |
| C5 | 纳入为变量 | NA | — | 没有把已知混淆变量作为区组或协变量纳入统计模型；该研究不是协变量调整设计。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或评分者，盲法不适用。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应需按完全平衡/拉丁方/ABBA层级处理。 |
| D1 | 练习效应 | NA | — | LLM每个prompt独立评估，合成实验也不是同一被试跨session练习设计；练习效应不适用。 |
| D2 | 疲劳效应 | NA | — | 无人类session疲劳问题；LLM评估与短训练运行不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件间无跨条件残留或清洗期问题；每个prompt/训练配置独立。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移设计。 |
| D5 | 范围效应 | NA | — | 因变量为token概率/准确率等客观指标，不涉及量表范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 研究不以多选项或序列刺激的顺序为设计变量；prepend位置是处理的一部分，不是需反平衡的选项顺序。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表，默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，需求特征不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集自动化，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.28（p.28）：'standard errors calculated over 10 runs'；p.29-40（p.29-p.40）多图报告accuracy/ES随条件变化的均值与标准误；未报告偏度或端点频率。 | 报告了均值/标准误，但未报告分布形态、端点频率或pilot难度校准，无法充分排查天花板/地板效应，故为0.5。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.4（p.4）定义ES并报告比例；p.28（p.28）报告10 runs标准误；p.43（p.43）checklist称'Standard errors are provided'。未见功效分析、95%CI或多重性校正。 | 报告了样本/运行规模与不确定性的标准误，但缺少样本量确定依据、正式效应量/置信区间、全部主要分析与多重性校正，故为0.5。 |
| F2 | 内部效度 | 0.5 | p.4（p.4）在同一COUNTERFACT样本上修改context并比较k=0,...,5；p.17（p.17）limitations只讨论开源模型和单层transformer。 | 采用同一样本内prompt扰动，基线可比性较好，但未正式报告分配/隐藏、基线检验、流向或内部效度威胁评估，故为0.5。 |
| F3 | 构念效度 | 0.5 | p.4（p.4）多种hijacking scheme；p.9（p.9）通过fixed/trained W_V、embedding structure、attention pattern等机制实验检验理论；未报告信度/效度指标或manipulation check。 | 主要测量是客观的token概率/准确率，并有多种操作化与机制检验支持构念，但缺少正式信效度证据和操纵检验，故为0.5。 |
| F4 | 外部效度 | 0.5 | p.3（p.3）使用GPT-2、Gemma base/instruct、LLaMA-2-7B；p.4（p.4）COUNTERFACT 21,919样本；p.17（p.17）承认仅开源模型、单层transformer。 | 报告了模型与数据来源并讨论部分推广边界，但未系统说明样本代表性或跨情境复现，故为0.5。 |
| G1 | 分析单位 | 0.5 | p.4（p.4）以COUNTERFACT样本聚合计算ES；p.28（p.28）合成评估集有1024个(x,y)对并以多次run标准误汇总。 | 分析层级基本落在样本/运行层面，但未明确说明处理分配层级、样本嵌套于relation/model/run的结构，也未用多层模型处理聚集，故为0.5。 |
| G2 | 随机效应 | 0 | p.28（p.28）'standard errors are over 5 runs'等，仅对多次运行聚合；未见随机效应模型或随机截距/斜率报告。 | 未说明哪些因子是随机效应；对训练运行、模型等潜在随机来源只做聚合，没有混合模型，故为0。 |
| G3 | 材料作为随机效应 | 0.5 | p.4（p.4）COUNTERFACT含多种subjects、relations；p.25（p.25）Table 1/2展示多个relation ID；但未报告item random effect或准F/混合模型。 | 材料/关系项目有多样性并显示跨relation pattern，但分析仍按项目聚合，未正式把材料作为随机因子，故为0.5。 |
| G4 | 统计功效 | 0 | 全文未见事前功效分析或样本量推导；p.28（p.28）仅给默认评估集1024对与5/10 runs；结果以图为主。 | 没有设计阶段功效分析或明确样本量论证，也没有效应量置信区间，故为0。 |
| G5 | 研究者自由度 | 0 | p.28（p.28）说明默认setup与评估集，但未报告试次/样本排除规则、全部测量因变量清单、中途停止规则或探索性/验证性分析区分。 | 研究者自由度相关报告不完整，缺少排除规则和验证性/探索性区分，故为0。 |
| G6 | 预先设定 / 预注册 | 0 | 全文无预注册平台、编号、预注册分析计划或与预注册偏离说明。 | 未见任何预注册；按编码口径无预注册记0。 |
| J1 | 位置偏差 | NA | — | 不涉及LLM-as-judge、候选A/B位置交换或多候选项排序；prepend位置是处理本身。 |
| J2 | 冗长偏差 | NA | — | 不使用LLM裁判评估开放式生成质量，冗长偏差不适用。 |
| J3 | 谄媚 | NA | — | 未操纵用户先验立场或反馈纠错，测的是事实检索被上下文劫持，不是谄媚。 |
| J4 | 自我偏好 | NA | — | 不使用LLM-as-judge，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 上下文劫持实验不是few-shot in-context learning；合成实验是训练而非few-shot。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4（p.4）给出'Do not think of {target_false}'与relation-ID prepend；p.25（p.25）Table 2给出不同relation的hijack sentence格式；未给prompt版本号、敏感性消融或dev/test划分。 | prompt模板有部分明确并可复现，也测试了多种措辞/方案，但缺少版本化、系统敏感性消融与dev/test控制，故为0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是长上下文/RAG实验；合成上下文长度L最多256且未做信息位置/U形曲线操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.27-28（p.27、p.28）AdamW、learning rate、5/10 runs标准误；未报告随机种子、精确snapshot或采样温度（LLM用token概率）。 | 有多次运行和标准误，但缺少种子/精确模型快照，且未报告采样参数，故为0.5。 |
| J9 | 重复与文本退化 | NA | — | 任务基于下一token概率/准确率，不涉及开放式长文本生成与重复退化QC。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本实验，无跨语言/跨脚本token数比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4（p.4）直接使用公开COUNTERFACT数据集；全文未报告模型训练截止日期、测试集版本对照或n-gram/DCQ污染检测。 | 使用公开事实数据集但未评估训练数据重叠或污染，故为0。 |
| J12 | 基准饱和 | NA | — | 不是接近饱和的公开基准排行榜评估，无SOTA水位/饱和问题。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；'Do not think of X'被用作上下文劫持操作，而非按否定/格式/数量等约束拆分IF准确率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求JSON/结构化格式输出，无格式合法率问题。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全对齐、有害请求或越狱攻击评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1（p.1）以人类回答对比开场：'humans do not find the two sentences factually confusing and would answer Paris'；p.5（p.5）将事实检索建模为latent semantic concept关联。 | 论文明确把LLM行为类比为联想记忆并对比人类直觉，但未系统论证LLM构念与人类同名构念的异同，也未做人类对照实验，故为0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不报告随模型规模/训练进展的涌现能力曲线，不涉及涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以benchmark/reward model/LLM-judge为优化目标并监控overoptimization。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.3（p.3）列出GPT-2、Gemma base/instruct、LLaMA-2-7B；p.28（p.28）合成实验报告5/10 runs标准误；未给精确snapshot/commit、95%CI或配对检验。 | 报告了重复运行次数和部分模型标识，但snapshot不精确、无CI/配对检验，故为0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮prompt评估，无多轮对话历史累积。 |

## 编码小结
论文清晰定义了上下文劫持、Efficacy Score、latent concept association与误差率，并用多模型、多劫持方案及合成实验提供机制证据。但统计报告以描述性曲线和运行标准误为主，缺少正式随机化、功效分析、预注册、精确快照/种子、污染检查与项目随机效应建模；人类实验设计组件大多不适用。
