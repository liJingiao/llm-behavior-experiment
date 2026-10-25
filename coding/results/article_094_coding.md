# article_094 | Investigating Cultural Alignment of Large Language Models | 2024

研究类型概述：这是一项 LLM 基准/评估式研究，而非人类被试实验：以 WVS 调查问题与受访者人口学 persona 构造提示，比较四个 LLM 在英语/阿拉伯语等条件下的回答与真实调查回答之间的 cultural alignment（Hard/Soft metric），并分析模型、语言、persona 人口学维度和问题主题的差异；分析单位为 model × persona × question × prompt condition 的模型输出。
- **研究构念（Construct）**：文化对齐、社会价值表征、跨语言文化知识迁移与人口代表性｜CA 构念锚定：刻板印象（stereotypes, `trm_4a3fd79d0b285`）；态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：这是一项 LLM 基准/评估式研究，而非人类被试实验：以 WVS 调查问题与受访者人口学 persona 构造提示，比较四个 LLM 在英语/阿拉伯语等条件下的回答与真实调查回答之间的 cultural alignment（Hard/Soft metric），并分析模型、语言、persona 人口学维度和问题主题的差异；分析单位为 model × persona × question × prompt condition 的模型输出。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.5 Table 2 contrasts English vs Arabic prompting across four models; p.4 lists model pretraining mixtures and p.5 describes four independently prompted question variants. | 自变量/比较条件被明确命名并给出至少两个水平，但未报告操纵检验，语言顺序与模型条件分配程序也不充分。 |
| A2 | 因变量 | 0.5 | PDF p.5: Hard metric Hf,c=mean 1(yhat=y) and soft metric with ordinal error formula; p.12 Table 7 reports paraphrase consistency. | 因变量指标与计分方式明确，但缺少正式信效度证据及连续指标预处理/天花板地板说明。 |
| A3 | 控制变量 | 0.5 | PDF p.4: participants filtered to equal demographic distribution and each Egypt persona matched to a US persona 'with exactly the same demographics'; p.5 fixes temperature 0.7 and five samples. | 报告了 persona 匹配、固定问题集和固定温度等控制，但未系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF p.9 Limitations: 'lack of knowledge regarding the actual data sources used for pretraining... black box nature'; p.6 discusses pretraining-language effects. | 识别了预训练数据不可知、语言/文化混淆等潜在混淆，但未做敏感性分析或系统控制残余混淆。 |
| A5 | 调节变量 | 0 | PDF p.2 hypothesizes 'misalignment will increase for personas from digitally underrepresented backgrounds' and for uncommon topics; p.6 Fig.3 and p.7 Fig.4 show subgroup means. | 提出了 persona/主题的调节假设并作描述性分层展示，但没有报告交互项统计检验、中心化或简单斜率。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或中介效应分析，研究模型不包含中介路径。 |
| A7 | 操作性定义 | 1 | PDF p.3 Fig.2 gives the persona/answer-format prompt template; p.4 Table 1 defines six demographic dimensions; p.5 gives Hard/Soft alignment formulas; p.14 Fig.6 gives English/Arabic example prompts. | 关键构念均有可复现的操作化说明：语言条件、persona 提示、回答格式和文化对齐计分。 |
| A8 | 水平数与类型 | 0.5 | PDF p.4 Table 1 lists demographic dimensions and possible values; p.5 Table 2 gives English/Arabic levels and four model labels; p.12 Table 6 lists model sizes/pretraining mixtures; p.13 Table 8 gives age ranges. | 报告了水平数与各水平标签，但缺少完整的水平类型、连续变量间距/全距及中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | PDF p.5 uses both Hard and Soft metrics; p.12 Table 7 reports consistency across four question paraphrases; p.9 Limitations notes 'we only consider one survey source'. | 使用了两种对齐指标和四种问题改写，并讨论了单一调查来源局限，但未正式报告多操作化会聚证据。 |
| A10 | 单一方法的风险 | NA | — | 自变量由外部提示/模型条件设定，因变量为模型输出与独立人类调查回答的比较；不存在人类自评量表中 IV/DV 同源共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组接受单一条件；同一模型/persona 被用于多个语言和问题条件，属于重复评估而非被试间分配。 |
| B2 | 被试内设计 | NA | — | 虽然同一模型在多个条件下被重复提示，但每次为独立 API 调用，没有形成需要顺序平衡的被试内会话；顺序效应组件不适用。 |
| B3 | 混合设计 | NA | — | 不存在人类被试的组间/组内混合设计，也没有对应混合 ANOVA 模型。 |
| B4 | 因子设计 | 0 | PDF p.5 Table 2 fully crosses four models with two prompting languages and two survey countries and reports cell means, but gives no ANOVA/interaction statistics or full design matrix with per-cell N. | 存在多因素比较结构，但未报告交互项或完整因子统计量，不能记为完整因子设计报告。 |
| B5 | 主效应 | 0 | PDF p.5-6 Tables 2-3 report means and state 'significantly more culturally aligned' but provide no F/df/p or effect sizes. | 只有描述性均值/差值，没有正式主效应统计检验。 |
| B6 | 交互作用 | 0 | PDF p.5 Table 2 reports an 'Ar-En' difference column per model but no interaction F/df/p, simple-effects tests, or CIs. | 未报告交互项统计检验；语言差异列不能替代正式交互分析。 |
| B7 | 区组设计 | NA | — | 研究未采用区组/分层随机分配设计；persona 人口学匹配归入匹配组件而非区组设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或被试内顺序平衡安排。 |
| B9 | 准实验设计 | 0.5 | PDF p.2 compares naturally existing models including LLaMA-2-Chat vs AceGPT-Chat; p.9 Limitations discusses black-box pretraining and model-selection limits. | 模型/预训练条件不是随机分配的准实验比较，文中讨论了部分局限性，但未明确准实验类型、选择偏差与因果推断限定。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有跨条件顺序的被试内处理，不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 所有模型/persona 均接受多个语言/问题条件，没有把分析单位随机分配到互斥条件的程序；无随机化分配问题。 |
| C2 | 平衡 | NA | — | 条件顺序不是被试内序列设计的一部分；独立提示调用不需要顺序平衡。 |
| C3 | 恒定 | 0.5 | PDF p.5 fixes temperature to 0.7 and samples five responses per variant; p.3 Fig.2 fixes the prompt template; p.12 Table 6 lists models. | 报告了若干恒定变量和水平，但未系统讨论这些固定选择对外部效度的限制。 |
| C4 | 匹配 | 0.5 | PDF p.4: 303 unique personas, each Egyptian respondent matched to a US respondent with the same demographics except location; p.13 Table 8 gives distributions. | 报告了匹配变量和匹配后分布，但未说明正式匹配算法、均衡性检验或回归假象风险。 |
| C5 | 纳入为变量 | 0.5 | PDF p.6 Fig.3 stratifies alignment by Sex, Education, Social Class and Age; p.13 Table 8 reports demographic distributions. | 人口学变量被测量并用于匹配/分层描述，但没有作为协变量纳入统一模型、检验斜率齐性或报告调整后效应量。 |
| C6 | 盲法 | NA | — | 没有人类被试或人类评分者需要盲法；对齐分数由自动公式计算。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序，因此完全平衡/拉丁方/ABBA 层级不适用。 |
| D1 | 练习效应 | NA | — | 每次提示独立调用 LLM，无上下文内练习或跨试次学习；练习效应不适用。 |
| D2 | 疲劳效应 | NA | — | 没有人类会话疲劳问题；LLM API 调用也不存在人类疲劳控制需求。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同语言/问题条件为独立提示，无跨条件残留或迁移污染。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件顺序设计，迁移对称性不适用。 |
| D5 | 范围效应 | NA | — | 任务为固定选项的调查问答，不是绝对量值估计或李克特量表校准；Soft metric 处理序数选项距离而非范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | PDF p.14 Fig.6 shows fixed numbered survey options; no option-order randomization or counterbalancing is reported. | LLM 在固定编号选项中选择，未做选项位置随机化/反平衡，也未讨论位置效应。 |
| E2 | 默认赞同 | NA | — | 研究使用 WVS 单选题/序数题，不是含正反向题的李克特自评量表；默认赞同偏差组件不适用。 |
| E3 | 极端 / 中间反应倾向 | 0 | PDF p.5-7 Tables 2-3 and Figs.3-4 report only group means; no skew, endpoint/midpoint usage, or response-style correction is reported. | 跨国家/跨 persona 比较可能受反应风格影响，但未报告分布形态或校正。 |
| E4 | 需求特征 | NA | — | 没有人类被试，故不存在人类需求特征或事后推断研究假设比例问题。 |
| E5 | 实验者效应 | NA | — | 数据采集为自动化 API 调用，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0 | PDF p.5 Tables 2-3 report only means; no SD, skew, or endpoint frequencies are given. | 因变量有 0-1 边界，但未报告分布形态或端点频率以排查天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 不存在自评多构念同源测量；IV 为外部模型/语言条件，DV 为模型输出与人类调查的匹配。 |
| F1 | 统计结论效度 | 0 | PDF p.5-7 Tables 2-4 report means/differences and use the word 'significantly' on p.6, but no CIs, effect sizes, p-values, or multiple-comparison correction are reported. | 缺少统计推断与效应量/置信区间，样本量也无功效依据。 |
| F2 | 内部效度 | 0.5 | PDF p.4 describes filtering and matching of survey respondents; p.9 acknowledges black-box pretraining limitations; no random allocation, allocation concealment, or baseline-equivalence tests are reported. | 报告了样本筛选/匹配和部分内部效度局限，但不是随机实验，缺少正式内部效度威胁评估与被试流向。 |
| F3 | 构念效度 | 0.5 | PDF p.5 gives hard/soft alignment formulas; p.12 Table 7 reports paraphrase consistency; p.9 discusses construct and data limitations; no formal validity/manipulation check is reported. | 有操作化与 paraphrase 一致性证据，但缺少正式信度、效度和操纵检验。 |
| F4 | 外部效度 | 0.5 | PDF p.9 Limitations: only two languages/countries and one survey source; p.13 Table 8 reports persona distributions. | 报告了样本来源与推广局限，但未报告跨样本/跨情境复现。 |
| G1 | 分析单位 | 0.5 | PDF p.5 defines Sf,c = mean over q,p; responses are aggregated over persona-question cells by model/culture without explicit multilevel nesting. | 说明了聚合层级，但未明确处理 persona/question 嵌套结构或分配层级匹配。 |
| G2 | 随机效应 | 0 | PDF p.5: alignment is a mean over queries and personas; no mixed model or random effects structure is reported. | 未说明哪些因子为随机效应；若要推广到 persona/question 总体，需要随机效应建模。 |
| G3 | 材料作为随机效应 | 0 | PDF p.4: 'we select 30 questions'; p.5 averages over questions/personas; no item random effect or mixed model is reported. | 问题材料被当作固定项目处理，未考虑题目随机效应，存在项目推广不足。 |
| G4 | 统计功效 | 0 | PDF p.4 reports 303 personas and 30 questions; no power analysis, effect sizes, or CIs are reported in p.5-7 results. | 缺少事前功效分析、样本量推导和结果效应量/置信区间。 |
| G5 | 研究者自由度 | 0.5 | PDF p.4 reports selecting 30 questions and 303 personas; p.5 reports excluding identical cross-country persona answers and using five samples/majority vote; no explicit stopping rule or confirmatory/exploratory labeling. | 报告了排除规则和主要测量，但样本量决定方式与验证性/探索性分析区分不完整。 |
| G6 | 预先设定 / 预注册 | 0 | PDF p.1-9 contains no preregistration or registered-report statement. | 未报告数据收集前的公开预注册；按规则缺失记 0。 |
| J1 | 位置偏差 | 0 | PDF p.14 Fig.6 shows fixed numbered options; no candidate-position counterbalancing, A/B swap, or flip-rate analysis is reported. | 研究涉及 LLM 多选项选择，但完全未报告选项位置偏差控制。 |
| J2 | 冗长偏差 | NA | — | 评估为封闭式多项选择与人类调查答案匹配，不涉及开放式生成质量/长短比较。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场或反馈/纠错对话，谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge；评分由 Hard/Soft 公式对真实调查答案计算。 |
| J5 | 少样本示例选择与排列偏差 | NA | PDF p.4: instruction-tuned models can be assessed 'in a zero-shot manner'. | 主实验为零样本提示，未使用 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.3 Fig.2, p.14 Fig.6, and p.18 Fig.12 provide full prompt templates; no prompt-version sensitivity ablation or dev/test split is reported. | 提示模板完整可复现，但缺少语义等价措辞的敏感性消融与版本化说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 调查提示很短，无长文档/RAG 或长上下文信息位置实验。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.5: questions prompted four times and 'sample five responses... using a temperature of 0.7'; p.2 gives GPT-3.5 snapshot. | 报告了 temperature、重复次数和部分模型 snapshot，但缺少 top-p、seed、置信区间及全部模型精确版本。 |
| J9 | 重复与文本退化 | NA | — | 主要输出为短选项/编号，不涉及开放生成重复退化；解码退化组件不适用。 |
| J10 | 分词效应 | 0 | PDF p.2 and p.5 compare English vs Arabic prompting; no tokenizer revision or token-count control is reported. | 跨语言比较未控制 token 数或报告 tokenizer，语言效应可能与分词效率混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF p.4 uses public WVS-7 (2017-2021) questions; no training-cutoff comparison or contamination detection is reported. | 调查题项公开且可能进入预训练语料，但未做污染检查。 |
| J12 | 基准饱和 | NA | PDF p.5 Table 2 shows soft scores roughly 45-66 and hard scores roughly 23-40, far from ceiling. | 分数远未饱和，基准饱和风险在本研究的主要指标上不成立。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；回答格式只用于解析最终选项。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF p.3 Fig.2 instructs 'only the index of the answer' and 'Do not include any extra commentary'; no format-validity rate or retry rule is reported. | 报告了格式约束设置，但未报告格式合法率、格式失败与内容错误拆分。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估，无有害请求或攻击成功率设置。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.1-3 defines cultural alignment and working assumptions; p.5 compares model answers to WVS human responses; p.9 discusses limitations; model versions are partly reported. | 将 LLM 输出与人类调查答案对照，并讨论构念/局限，但未系统论证 LLM 构念与人类同名构念的异同。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的涌现曲线分析。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有针对 benchmark/reward/LLM-judge 进行训练或优化，不存在代理指标过优化问题。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.5 reports five sampled responses with majority vote; p.2 gives GPT-3.5 snapshot; p.12 Table 6 lists models; no CIs, paired tests, or full snapshot identifiers are reported. | 有重复采样和部分 snapshot，但缺少置信区间、配对检验及全部模型的精确检查点。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮调查问答，无多轮对话历史累积，也未外推多轮部署。 |

## 编码小结
论文清楚报告了文化对齐的操作化、提示模板和主要描述性结果，但统计推断、位置/顺序控制、跨语言 tokenization、污染检查、随机效应与预注册等均不完整或缺失。人类被试特有的分配、顺序、疲劳、需求特征等组件多不适用；LLM 评估特有的采样、提示敏感性、可复现性和跨语言偏差风险部分适用且报告不充分。
