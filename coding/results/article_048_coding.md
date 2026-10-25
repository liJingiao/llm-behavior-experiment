# article_048 | Delving into Multilingual Ethical Bias: The MSQAD with Statistical Hypothesis Tests for Large Language Models | 2025

研究类型概述：多语言 LLM 伦理/社会偏差基准研究：构建 MSQAD 数据集，以语言为受控输入条件（英语、韩语、中文、西班牙语、德语、印地语），对同一敏感问题生成回答，并用 McNemar 检验拒绝率差异、用 PERMANOVA 检验回答嵌入分布差异；另比较 6 个额外 LLM。无人类被试分配，分析单位为问题/回答/语言对，模型为固定比较对象。
- **研究构念（Construct）**：跨语言伦理偏见与文化条件化反应行为（cross-linguistic social/ethical bias and culturally conditioned response behavior）｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：多语言 LLM 伦理/社会偏差基准研究：构建 MSQAD 数据集，以语言为受控输入条件（英语、韩语、中文、西班牙语、德语、印地语），对同一敏感问题生成回答，并用 McNemar 检验拒绝率差异、用 PERMANOVA 检验回答嵌入分布差异；另比较 6 个额外 LLM。无人类被试分配，分析单位为问题/回答/语言对，模型为固定比较对象。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 1 | PDF p.4: “translated the generated questions into six languages: English, Korean, Chinese, Spanish, German, and Hindi.” PDF p.5: “all factors were held constant except for the language used.” PDF p.15 Table 5: GEMBA translation-quality scores for the language versions. | 语言被明确命名为唯一操纵自变量，有 6 个具体水平；每个问题扩展到所有语言并以等价提示生成回答；附录用 GEMBA 检查翻译等值性，可视为操纵/等值检查。 |
| A2 | 因变量 | 0.5 | PDF p.5-7: McNemar rejection rates and PERMANOVA on response embeddings; PDF p.16: zero-shot multilingual BERT classifier with 0.8 probability threshold and rejection-expression filtering. | 因变量指标和计分方式明确：拒绝率与嵌入距离分布。但主分类器缺少金标准信效度证据，嵌入测量也没有报告重测/一致性；连续嵌入指标未见预处理或天花板/地板说明，故为部分满足。 |
| A3 | 控制变量 | 1 | PDF p.9: “we set the use of prompt configuration and a translation service as control variables.” PDF p.15-16: “prompt configurations ... translation service ... and the pre-trained language model (PLM) used for each statistical test were all held constant.” | 系统列出并说明将提示配置、翻译服务、统计检验用 PLM 保持恒定；模型版本也具体列出，控制变量报告较完整。 |
| A4 | 混淆变量 | 0.5 | PDF p.9 Limitations: “potential bias in using LLMs” and “refined dataset may still contain noise”; PDF p.19: translation service could produce unintended translations, mitigated by prompt design. | 识别了 LLM 数据生成偏差、翻译误差与提示配置等潜在混淆并说明控制思路，但没有对残余混淆做敏感性分析或量化内部效度威胁，故为 0.5。 |
| A5 | 调节变量 | NA | — | 论文没有正式界定调节变量，也没有对语言×主题或语言×模型交互项做统计检验；主题和模型比较是分层描述，不构成调节模型，故不适用。 |
| A6 | 中介变量 | NA | — | 论文没有提出或检验中介机制，也没有直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | PDF p.4: “translated the generated questions into six languages”; PDF p.15-16: classifier、threshold、PERMANOVA公式与拒绝表达过滤；PDF p.18-21: 全文提示模板。 | 关键构念有可复现操作化：语言通过翻译 API 与语言特定提示操作化，拒绝通过分类器和阈值判定，回答分布通过嵌入和 PERMANOVA 计分，提示模板公开。 |
| A8 | 水平数与类型 | 1 | PDF p.4: six languages “English, Korean, Chinese, Spanish, German, and Hindi”; PDF p.5: language as only independent variable. | 语言变量有 6 个明确水平且为名义类别；对分类变量不涉及数值间距与全距。主题与模型作为分层/比较维度另行描述。 |
| A9 | 单一操作化的风险 | 1 | PDF p.5-7: 同时使用 McNemar 拒绝率与 PERMANOVA 嵌入分布；PDF p.17: human annotation of acceptable responses aligns with English being most informative. | 对伦理偏差采用拒绝行为和嵌入分布两种操作化，并辅以人类评分；人类判断与嵌入分析方向一致，提供了会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是自陈式多构念测量，IV 是输入语言，DV 是模型生成回答的客观文本分类/嵌入；不存在人类问卷式的共同方法偏差结构，故不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试，也不存在把独立被试组分到不同语言条件的被试间设计；语言条件是在同一问题/模型上重复生成的不同提示输入。 |
| B2 | 被试内设计 | NA | — | 虽然每个问题在多种语言下生成回答，但每次是独立单轮 LLM 调用，无人类重复测量顺序或跨条件学习；没有需要平衡的被试内顺序设计。 |
| B3 | 混合设计 | NA | — | 没有组间与组内被试因素的混合设计；模型比较与主题分析是固定对象/分层描述。 |
| B4 | 因子设计 | NA | — | 没有报告完整因子设计矩阵、每格样本量和主效应/交互 ANOVA；语言、主题、模型并未作为完全交叉因子统一建模。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验；结果按语言对、主题和模型分别呈现。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验或简单效应分析；不构成因子设计的交互检验。 |
| B7 | 区组设计 | NA | — | 没有区组变量、划分依据或区内随机分配程序；主题分层只是分别展示结果。 |
| B8 | 拉丁方 | NA | — | 没有拉丁方顺序设计或相应被试分配。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验；语言是研究者直接设置的提示条件，不是自然分组或不可随机分配的人群体。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理顺序，也无处理可逆性/迁移对称性问题；每次语言提示为独立调用。 |
| C1 | 随机化 | NA | — | 没有把分析单位随机分配到互斥实验条件；每个问题在六种语言下均生成回答，缺少需要随机分配的组间条件。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，因此无顺序平衡层级或各顺序被试数可报告。 |
| C3 | 恒定 | 0.5 | PDF p.9: prompt configuration and translation service designated as control variables; PDF p.15-16: PLM and prompt configurations held constant; PDF p.18-21: full prompts. | 列出并恒定提示配置、翻译服务、统计 PLM 与主要模型版本，并讨论控制变量设置的外部效度限制；但未报告温度、采样参数等关键 LLM 恒定设置，故为部分满足。 |
| C4 | 匹配 | NA | — | 没有使用匹配设计、匹配变量或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组或协变量纳入统计模型；研究主要通过恒定控制处理混淆。 |
| C6 | 盲法 | NA | — | 无人类被试分组，条件语言本身不可隐藏；没有实验条件盲法结构。人类评分者主要用于辅助标注，不是主实验盲法对象。 |
| C7 | 平衡的层级 | NA | — | 没有顺序效应，也没有完全平衡/拉丁方/ABBA 层级需要选择。 |
| D1 | 练习效应 | NA | — | LLM 每次语言提示为独立单轮调用，无跨试次学习或练习效应；不是人类练习块设计。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长、休息间隔或疲劳效应问题；LLM 生成也没有相应疲劳机制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留或清洗期问题；各语言提示独立生成，不共享对话上下文。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉处理，故无迁移对称性检验问题。 |
| D5 | 范围效应 | NA | — | 主因变量为拒绝率与嵌入距离，不是被试内绝对判断或量表评级；人类 1–5 评分仅用于辅助验证，不涉及主范围效应设计。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有多选、排序或序列刺激呈现；语言条件不是按固定/随机顺序呈现给同一被试的刺激序列。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert 自评量表测量主构念；无默许偏差所需的正面/反向题结构。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 主分析不是跨群体等级量表比较；人类评分只用于辅助效度检查，未将反应风格作为主要威胁。 |
| E4 | 需求特征 | NA | — | 无人类被试参与主任务，不存在需求特征或事后猜测实验假设的问题。 |
| E5 | 实验者效应 | NA | — | 数据主要由自动化 LLM 生成；虽有人类评分者，但不存在主试期望传递或主试-被试交互结构。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF p.5-6 Figure 5: rejection rates across languages and topics; PDF p.13 Table 2: human question-validity scores with mean(SD); PDF p.17 Table 6: human informativeness score proportions. | 报告了拒绝率与部分人类评分的均值/比例，可粗略检查端点；但核心嵌入指标没有分布形态、偏度或正式天花板/地板分析，任务难度校准也未系统报告。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；无共同方法偏差的问卷式程序控制或统计检验需求。 |
| F1 | 统计结论效度 | 0 | PDF p.5-7: reports McNemar χ² and PERMANOVA F/permutation p-value; PDF p.5: 5% critical value 3.838; no effect sizes or confidence intervals reported. | 报告了检验统计量和显著性门槛，但没有效应量或置信区间，也没有明确的多重比较校正；不满足基本要件。 |
| F2 | 内部效度 | 0.5 | PDF p.4: same questions translated into six languages with GEMBA quality check (Table 5, p.15); PDF p.9: prompt configuration and translation service controlled. | 无随机分配与分配隐藏（LLM 条件非人类随机分配），但通过翻译等值检查和恒定控制提升内部效度；未系统评估选择、模型版本变化等内部效度威胁。 |
| F3 | 构念效度 | 0.5 | PDF p.13: Krippendorff’s α = 0.72/0.61/0.68 for human question validity; PDF p.15 Table 5: GEMBA translation quality; PDF p.16: classifier lacks gold labels. | 人类题项效度和翻译质量有信度/效度证据，但主 DV 的拒绝分类器无金标准信效度，嵌入测量构念对应关系论证不足。 |
| F4 | 外部效度 | 0.5 | PDF p.1/4: HRW news across 17 topics and six languages; PDF p.8-9: six additional LLMs; PDF p.9 Limitations: only six languages, future expansion. | 报告了数据来源、主题、语言和模型范围，并讨论扩展到更多语言的限制；但未系统论证新闻/问题代表性，也未做跨样本复现。 |
| G1 | 分析单位 | 0.5 | PDF p.5: McNemar test pairs responses to the same question across languages; PDF p.6-7: PERMANOVA distance matrix within each topic; PDF p.16: analysis based on rejection rate and response distribution. | 处理层级是问题内语言提示，分析在问题/回答层级，McNemar 做了配对；但 PERMANOVA 没有显式建模问题嵌套，分配层级与分析层级的对应说明不完整。 |
| G2 | 随机效应 | NA | — | 不存在人类被试随机效应；模型是固定的被比较系统而非从总体抽样的被试样本。材料/题项推广问题在 G3 评价。 |
| G3 | 材料作为随机效应 | 0.5 | PDF p.13 Table 3/4: thousands of generated questions per topic; PDF p.5-7: analyses aggregate across questions without item random effects or mixed models. | 题项来自主题下的较大问题池，McNemar 以问题为配对单位，某种程度上利用了题项抽样；但没有把题项作为随机效应纳入 PERMANOVA 或统一混合模型，结论向任意问题的推广仍不完整。 |
| G4 | 统计功效 | 0 | PDF p.13-14: reports numbers of questions and clustering selection; no a priori power analysis or expected effect size; PDF p.5-8: no confidence intervals/effect sizes. | 没有事前功效分析或样本量推导，也没有用效应量/CI 支撑检验；不满足要求。 |
| G5 | 研究者自由度 | 0.5 | PDF p.14 Table 4: clustering threshold n=97 and bottom 1% removal; PDF p.16: 0.8 classifier threshold and rejection-expression filtering; appendices report all topics. | 报告了主要数据选择/剔除规则并展示全部主题结果；但未见样本量停止规则、全部分析的事前/探索性区分，研究者自由度披露不完整。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未见预注册平台、注册编号或分析计划；PDF p.9 仅报告事后 Limitations。 | 没有预注册或时间戳早于数据收集的公开分析计划，故为 0。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM-as-judge 的候选位置比较、A/B 交换或多项选择正确答案位置随机化。 |
| J2 | 冗长偏差 | NA | — | 没有使用 LLM 裁判对开放式回答长度/质量进行成对比较；人类评分用于辅助验证，不构成长度偏差的 LLM 裁判设计。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈纠错或多轮谄媚操纵；任务是中立敏感问题生成。 |
| J4 | 自我偏好 | NA | — | 主偏差评测不使用 LLM-as-judge 评估被评模型回答；GEMBA 仅用于翻译质量辅助检查，且使用独立 gpt-4o，非主裁判结构。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 没有 few-shot in-context examples；拒绝分类是零样本分类器，GEMBA 也是零样本翻译评估。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.18-21: full prompt templates for question generation, acceptable and non-acceptable response generation in six languages; PDF p.15: model versions. | 公布了完整提示模板与模型版本，但没有提示措辞敏感性消融、dev/test 划分或提示搜索过程说明；仅部分满足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 没有长上下文/RAG 或关键信息位置操纵；输入为短新闻/问题提示。 |
| J8 | 温度与采样随机性 | 0 | PDF p.18: gpt-3.5-turbo-0125 用于 response generation；PDF p.8/18: vLLM 与模型版本；未见 temperature、top-p、seed 或重复次数。 | 只报告模型版本/接口，未报告采样超参、随机种子和每条件重复采样，无法评估 LLM 非确定性；不满足基本要件。 |
| J9 | 重复与文本退化 | 0 | PDF p.4/18-21: open-ended response generation with full prompts; no decoding strategy, repetition penalty, repetition/degeneration rate, or truncation ratio reported. | 任务涉及开放式生成，且案例中可见退化/无关输出，但论文未报告解码策略和重复率/退化率 QC 指标。 |
| J10 | 分词效应 | 0 | PDF p.4: six languages and scripts; no tokenizer name/revision, token/word ratio, or token-length control reported. | 跨语言比较明确存在，但未报告分词器版本或控制各语言 token 数差异，语言效应可能与分词/长度混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.4: self-constructed MSQAD from HRW news and LLM generation; PDF p.8/18: model versions listed; no training cutoff or contamination check. | 虽为自建数据集，但没有报告训练数据截止日期对照、n-gram 重叠或 held-out 证明；未处理新闻/生成数据可能已在预训练语料中的污染风险。 |
| J12 | 基准饱和 | NA | — | 研究不是以准确率/SOTA 性能提升为核心的基准饱和评估；没有接近天花板的基准分数比较，故不适用。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循；没有约束指令准确率或 IFEval 式可验证指令集。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 实验不要求结构化输出或 JSON/grammar-constrained 解码；无格式合法率与内容错误分离问题。 |
| J15 | 越狱稳健性 | 0.5 | PDF p.15 A.4: “to generate non-acceptable responses, we employed a jailbreak by adding sentences designed to prevent the LLM from evading sensitive requests”; PDF p.5-6: rejection rates by language. | 确有敏感请求和 jailbreak 生成非可接受回答，测量了不同语言下的拒绝率；但没有并列自然提示拒绝率与对抗攻击成功率，也未区分攻击族/ASR，故只部分满足。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 这是 NLP 中的跨语言社会/伦理偏差基准，不主张把 LLM 当作人类心理学/认知科学被试来测量同名心理构念；故不适用。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模或训练进展的连续能力曲线，也没有宣称“涌现/突变”。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有以代理指标为训练/优化目标，也没有 RL、best-of-N 或奖励模型优化环节；纯评测研究。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.18: exact model identifiers (e.g., gpt-3.5-turbo-0125; gemma-7b; Llama-2-7b-chat-hf); PDF p.5-7: McNemar/permutation tests; no repeated sampling N or 95% CI. | 提供了较精确的模型/接口版本，并做了配对/置换检验；但没有报告每分数重复次数与置信区间，开源模型也未报告 seed/checkpoint 敏感性，故部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮提示生成，无对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
该研究是数据集构建加统计假设检验的 LLM 跨语言偏差评测，不是人类被试实验。语言操纵、翻译等值检查、提示和模型版本有较多报告，但核心因变量分类器信效度、重复采样/置信区间、随机种子与解码参数、提示敏感性、污染检查、多重校正和材料随机效应等报告不足。许多人类被试实验特有组件不适用，记为 NA；对确有 LLM 条件的部分按 LLM 分析单位评价。
