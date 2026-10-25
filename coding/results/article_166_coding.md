# article_166 | Testing the limits of natural language models for predicting human language judgements | 2023

研究类型概述：人类行为实验与九个语言模型的计算模型比较研究：100名英语母语者在成对八词句子中判断哪句更可能，并给出三点信心；研究比较n-gram、RNN/LSTM与多种Transformer模型对句子概率的判断与人类选择的一致性。分析单位为被试组/刺激集层面的重复复制，并比较模型作为候选认知模型，而非把LLM当作被试或裁判。
- **研究构念（Construct）**：人类语言概率判断与语言模型—人类感知一致性｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让九种现成语言模型对受控的成对句子赋予相对概率，并让人类独立判断哪一句更可能出现；比较模型预测与人类选择。（比较随机句对、语料库筛选的争议句对和通过固定输入优化生成的争议句对，并按目标模型组合分层。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.9: 'the four main experimental conditions: selected controversial sentence pairs; natural versus synthetic pair...' and 'The order of trials... were randomized'. p.8 describes selection/synthesis of controversial pairs. | 句子对条件/模型对作为刺激操纵变量被明确命名并给出水平，但未报告操纵检验；条件创设程序和分配方式只部分描述。 |
| A2 | 因变量 | 0.5 | p.2: participants judged 'which of two sentences they would be more likely to encounter' and 'confidence... on a three-point scale'; p.10 describes binarized correctness, averaging across sentence pairs and ten participants, and noise-ceiling bounds. | 因变量指标与计分方式明确，但缺乏正式信度/效度证据及连续指标预处理的完整说明；有控制试次排除规则。 |
| A3 | 控制变量 | 0.5 | p.8: sentences filtered to eight distinct words, no punctuation except final, shared 29,157-word vocabulary, inappropriate words excluded; p.9: trial order and left-right position randomized. | 报告了多项恒定/随机化控制，但不是系统列出控制变量清单并逐一说明控制手段，完整性一般。 |
| A4 | 混淆变量 | 0.5 | p.7: 'we did not systematically control the training corpora... observed differences are due to differences in the training sets rather than the model architecture'; p.8 reports token-count control analysis. | 识别了训练语料/架构等潜在混淆并讨论残余威胁，也做了token数控制分析，但未系统控制所有混淆或做完整敏感性分析。 |
| A5 | 调节变量 | NA | — | 理论模型和设计中没有明确的调节变量与交互假设，故不适用。 |
| A6 | 中介变量 | NA | — | 理论模型和设计中没有中介变量或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | p.7–10详细说明模型概率计算、自然句采样、争议句合成、人类选择/信心计分；p.10提供代码和数据链接。 | 关键构念（模型句子概率、人类选择、置信度、模型—人类一致性）都有可观测、可复现的操作化程序，并有代码/数据。 |
| A8 | 水平数与类型 | 1 | p.7: 'nine models from three distinct classes: n-gram models, RNNs and transformers' and lists names; p.9: 36 model pairs × 4 main conditions = 144 trials. | 报告了九个模型及模型对/条件水平及标签；水平为分类变量，无连续间距/中心化问题。全距即所有候选模型/条件组合。 |
| A9 | 单一操作化的风险 | 1 | p.3 Fig.4使用含信心的有序相关；p.10同时报告二值正确率与连续log-ratio相关；p.7讨论八词英语句子的推广限制。 | 关键构念采用二值选择与有序置信/连续概率比等多种指标并报告会聚结果，也讨论了刺激范围限制。 |
| A10 | 单一方法的风险 | NA | — | 模型预测和人类判断来自不同来源（计算模型 vs 人类行为），不存在自变量/因变量同源自评问题。 |
| B1 | 被试间设计 | NA | p.9: each ten-subject group saw a unique stimulus set; every stimulus set contained one pair from every model-pair × condition combination. | 所有被试均接受全部条件类型/模型对结构，差异在于刺激集，不是被试间条件分配；纯被试间设计不适用。 |
| B2 | 被试内设计 | 0.5 | p.9: 'The order of trials... as well as the left–right screen position... were randomized for all participants'; p.10: ten groups provided ten independent replications. | 确为被试内重复测量并有随机顺序处理，但未报告各顺序人数/平衡方案细节，且统计模型未显式将被试作为随机效应。 |
| B3 | 混合设计 | NA | — | 没有逐因素标明的组间×组内混合实验设计；不同刺激集组不是实验处理因素。 |
| B4 | 因子设计 | 0 | p.9: 36 model pairs × four main conditions accounted for 144 trials, plus random/control trials. | 存在模型对×条件的因子式交叉结构，但未报告完整设计矩阵/每格样本量，也未用ANOVA表报告主效应与交互；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | p.2–3 reports model comparisons and Wilcoxon tests with FDR; e.g. 'GPT-2 and RoBERTa showing the best human consistency and 2-gram the worst'. | 报告了模型间主比较及显著性，但缺少效应量与完整自由度/方差分析，且未在显著交互时讨论主效应解释受限。 |
| B6 | 交互作用 | 0 | p.2–3 compare model accuracies across random, controversial natural and synthetic conditions separately, but no formal condition × model interaction test is reported. | 虽然不同条件下模型排名看似不同，但全文未报告交互项统计检验，也未给简单效应/校正。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配被试的设计；十个刺激集组是独立复制，不是用于控制个体差异的区组变量。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方设计；试次顺序为随机化而非拉丁方顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；研究为实验室式在线行为实验与计算模型比较，不涉及非随机处理分配。 |
| B10 | 被试内设计的适用条件 | 0.5 | p.2: binary forced-choice 'minimizes the role of between-trial context effects by setting an explicit local context within each trial'; p.9 randomized trial order. | 对顺序/局部上下文效应有所论证并随机化，但未正式论证处理可逆性或检验迁移对称性。 |
| C1 | 随机化 | NA | — | 没有把被试分配到互斥处理条件的随机化；试次顺序/左右位置随机化在E1中编码。 |
| C2 | 平衡 | 0.5 | p.9: trial order within stimulus set and left–right screen position randomized for all participants. | 报告了顺序随机化，但未说明平衡层级、各顺序人数，也未论证迁移对称性。 |
| C3 | 恒定 | 0.5 | p.8: eight-word sentences, shared vocabulary, punctuation/inappropriate-word filters; p.7 limitation: 'all eight-word English sentences'. | 列出多项恒定刺激特征并讨论外部效度限制，但未系统列出所有实验环境/模型版本等恒定变量水平。 |
| C4 | 匹配 | NA | — | 未对被试做匹配；刺激的十等分概率分层选择不是被试匹配程序。 |
| C5 | 纳入为变量 | 0.5 | p.8: token counts of preferred vs non-preferred synthetic sentences were statistically compared; Supplementary Table 1; p.9 stratified selection by natural sentence probability decile. | 测量并分析了token数这一潜在混淆，但未将其作为协变量纳入主模型或报告ANCOVA斜率齐性/调整后效应。 |
| C6 | 盲法 | NA | — | 在线自动化人类被试实验，无组间处理分配或人类评分者盲法安排；条件也不是可隐藏的处理。 |
| C7 | 平衡的层级 | 0.5 | p.9: order of trials and left–right position randomized for all participants. | 报告了随机顺序，但未明确平衡层级、构造方法、各顺序人数及顺序效应形状假设。 |
| D1 | 练习效应 | 0 | p.9–10 describe 144 model-pair/condition trials plus random/control trials and a 90-min limit, but no practice block, trial-position covariate, or early-trial exclusion rule. | 存在大量重复试次且可能有练习/学习效应，但未报告练习块或试次位置控制。 |
| D2 | 疲劳效应 | 0 | p.9: 'a 90-min time limit was enforced for the whole experiment' and progress bar; no rest interval schedule reported. | 长时程任务有疲劳风险，但未报告休息间隔、时长或时间分散方案。 |
| D3 | 延滞 / 迁移效应 | 0.5 | p.2: binary forced-choice 'minimizes... between-trial context effects'; p.9 randomized trial order. | 识别了试次间上下文/迁移风险并用局部强制选择与随机顺序减轻，但无清洗期或条件对建模。 |
| D4 | 不对称迁移 | 0 | p.9 describes randomized trial order, but no test of order × condition or discussion of asymmetric transfer. | 未检验迁移对称性，也未讨论平衡是否失效；对于重复句子判断任务该风险至少应说明。 |
| D5 | 范围效应 | 1 | p.2: absolute probability ratings are complicated by between-trial context effects; binary forced-choice with local context was chosen; confidence rated on three-point scale. | 明确识别绝对量值判断的范围/上下文效应，并用局部强制选择避免范围效应；主因变量不是绝对量表。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.9: 'The order of trials within each stimulus set as well as the left–right screen position of sentences in each sentence pair were randomized for all participants.' | 明确报告了试次顺序和左右位置随机化，但未给随机化方案类型、各位置出现次数或顺序组分配细节。 |
| E2 | 默认赞同 | NA | — | 研究不使用Likert/态度自评量表；主因变量是二选一，另有三点信心评分，不是多题项默许偏差量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有多题项等级量表，也没有跨群体/跨文化反应风格比较。 |
| E4 | 需求特征 | 0 | p.9 describes task instructions asking which sentence is more probable and confidence, but no cover story or post-experimental inquiry of hypothesis awareness. | 未报告掩饰情节、盲法或事后需求特征检查；被试可能推断任务与句子自然性/概率有关。 |
| E5 | 实验者效应 | NA | — | 完全在线自动化采集，无人类主试/评分者参与，实验者期望传递不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.10 reports agreement rates (e.g. 52.2%, 36.6%, 67.6%, 60.0%) and Figs.1/3/4 show accuracy distributions; no skew/endpoint frequencies or pilot difficulty calibration are reported. | 有均值/分布图与一致性比例，但缺少正式端点频率、偏度和预实验难度校准说明。 |
| E7 | 共同方法偏差 | NA | — | 模型预测与人类行为来源天然分离，不适用共同方法偏差的同源自评问题。 |
| F1 | 统计结论效度 | 0.5 | p.10: Wilcoxon signed-rank tests with Benjamini–Hochberg FDR; ten independent replications; figures show accuracy distributions, but no effect-size/CI table. | 多重比较校正和检验报告较好，但缺正式效应量与95%置信区间，样本量依据也不完整。 |
| F2 | 内部效度 | 0.5 | p.9: trial order and left-right position randomized; p.10: 21 participants rejected for failing control trials and replaced; p.7 discusses residual training-corpus confound. | 报告了试次随机化与数据排除/替换，但无分配隐藏、基线等价或完整被试流向；内部效度威胁有部分讨论。 |
| F3 | 构念效度 | 0.5 | p.10 reports inter-subject agreement/noise ceiling and control-trial exclusion; p.8 compares probability estimators and token-count controls. | 有构念一致性和控制试次的部分证据，但缺正式信度/效度统计与操纵检验报告。 |
| F4 | 外部效度 | 0.5 | p.9: 100 native English-speaking US-based Prolific participants, age 34.08±12.32, 55 male; p.7 limitation to eight-word English sentences. | 报告了样本来源/特征并明确八词英语句子的推广边界，但无跨样本/跨语言复现。 |
| G1 | 分析单位 | 0.5 | p.9: ten groups each received a unique stimulus set; p.10: 'these groups provided ten independent replications'. | 处理在试次/刺激集内重复，分析聚合到被试组层面并用十组做检验；未用多层模型显式处理被试/试次嵌套。 |
| G2 | 随机效应 | 0.5 | p.10 uses ten independent group-level accuracy outcomes in Wilcoxon tests; no mixed-model random-effect structure is reported. | 以十组独立复制部分处理了刺激/被试抽样变异，但未明确报告随机截距/随机效应及可推广总体。 |
| G3 | 材料作为随机效应 | 0.5 | p.8–9 describe sampling natural sentences and stratified selection; p.10 aggregates across sentence pairs and uses ten unique stimulus sets; no (1&#124;item) or F′ reported. | 材料被当作从更大句子总体抽样，并有十组刺激集复制，但分析未显式加入项目随机效应或准F比。 |
| G4 | 统计功效 | 0.5 | p.2 argues binary forced-choice 'provides substantially more statistical power' than acceptability ratings; p.9 reports 100 participants; no formal power analysis or effect-size CIs reported. | 有设计敏感度/统计功效的口头论证，但无目标功效、预期效应量与样本量推导，结果也缺CI。 |
| G5 | 研究者自由度 | 0.5 | p.10 reports rejecting 21 participants and replacing them; all main conditions/models are described; code/data posted. No explicit confirmatory vs exploratory distinction. | 排除规则和主要条件/模型报告较完整，但未区分验证性与探索性分析，也未完整说明样本量停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered-report statement appears in the main text; p.10 only reports data/code availability. | 未发现公开预注册；按口径记0，而不是NR。 |
| J1 | 位置偏差 | NA | — | 不涉及LLM-as-judge、候选项排序或LLM成对偏好选择；人类左右位置随机化已在E1编码。 |
| J2 | 冗长偏差 | NA | — | 不涉及LLM裁判或开放式生成长度比较；无长度—质量偏差评估场景。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈式对话或谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不使用LLM-as-judge，无裁判模型自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 没有few-shot in-context示例；模型只被用于计算句子概率。 |
| J6 | 提示敏感性 / 脆弱性 | NA | — | 没有自定义提示模板或提示敏感性实验；模型概率计算不是prompt-based生成。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 刺激为八词短句，无长上下文或RAG设置。 |
| J8 | 温度与采样随机性 | NA | — | 不涉及LLM生成式解码采样；双向模型概率估计使用100个随机排列，但不是temperature/top-p解码实验，因此J8不适用。 |
| J9 | 重复与文本退化 | NA | — | 不涉及开放生成、beam/sampling解码或重复退化评估。 |
| J10 | 分词效应 | 0.5 | p.8: 'tokenization schemes varied across models' and the authors test token-count differences; Supplementary Table 1. No tokenizer revision/version is given in the main text. | 识别并经验控制了不同模型分词/token数差异，但未报告分词器版本/revision。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.8: natural sentences sampled 'while ensuring that there was no overlap between training and testing sentences' for n-gram/RNN corpus; p.7 notes training corpora were not systematically controlled for transformers. | 对部分自训练模型做了训练/测试重叠控制，但未对预训练Transformer做污染检测或训练截止日期对照。 |
| J12 | 基准饱和 | NA | — | 使用新构建的高争议句子对，模型准确率远未接近天花板；不是饱和基准评测，故饱和风险不适用。 |
| J13 | 指令遵循 | NA | — | 因变量是人类句子概率判断/模型概率一致性，不是指令遵循。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 没有结构化输出或格式约束要求。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 本研究没有把LLM当作心理学被试进行行为实验；人类是被试，语言模型是候选计算模型。故J16的LLM-as-participant范式定位不适用。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的涌现曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及以代理指标为优化目标或对指标进行奖励优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.10 reports ten independent replications and posts code/data (github/Zenodo); model families are named, but exact checkpoint/snapshot identifiers and paired CIs for every model score are not systematically given in the main text. | 有重复与可复现代码/数据，但模型snapshot标识和逐分数CI/配对检验报告不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单次句子对判断，无多轮对话历史累积。 |

## 编码小结
论文对人类句子概率判断与语言模型—人类一致性做了较系统的实验与建模比较，刺激选择/合成、模型概率估计、人类选择与置信评分、噪声上限及多重比较校正均有报告；但若干实验心理学质控项（正式功效分析、盲法/需求特征检查、随机化细节、正式信效度、随机效应/项目随机效应建模）只部分报告或缺失。LLM相关风险多数不适用，因为本研究不做LLM-as-judge、few-shot提示、生成式解码或安全评估。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
