# article_175 | Large language models act as if they are part of a group | 2025

研究类型概述：计算/观察型 LLM 心理行为研究：研究 1 对 77 个 LLM 用 'We are'/'They are' 提示生成句子并以 RoBERTa 情感分类估计内群体偏爱与外群体敌意；研究 2 用美国党派 Twitter 数据微调 GPT-2/BLOOM 等模型并操纵删除比例；研究 3 分析 WildChat、LMSYS 的真实人机对话。分析单位为生成句子，嵌套于模型/数据集，用逻辑回归和混合效应模型估计优势比。
- **研究构念（Construct）**：最小群体条件下的内群体偏爱、外群体敌意与社会身份偏差｜CA 构念锚定：情绪（emotion, `trm_4a3fd79d0a17f`）；情绪识别（emotion recognition, `trm_4a3fd79d0b665`）；共情（empathy, `trm_4a3fd79d0b67d`）
- **实验任务与范式（Task / Paradigm）**：让77个现成基础或指令模型分别完成1,000个“We are”和1,000个“They are”句子，比较生成文本的正负情感，并在自然人机对话中复核群体语言偏差。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF p.2: 'We prompted each model to generate 2,000 sentences starting with “We are” or “They are”'; PDF p.6: default prompt and instruction prompt templates. | 自变量（句子群体、提示类型、微调数据条件）有命名与水平，但缺少操纵检验，且条件并非随机分配，故为 0.5。 |
| A2 | 因变量 | 0.5 | PDF p.2: sentences classified as positive, neutral or negative using a RoBERTa-based classifier; PDF p.7: logistic regression equations controlling TTR and total tokens. | 因变量测量指标和计分方式清楚，并有十种替代分类器稳健性；但无正式信度统计、分类器准确率或端点预处理说明，故 0.5。 |
| A3 | 控制变量 | 0.5 | PDF p.2: 'controlling for type-to-token ratio and sentence length as proxies for data generation quality'; PDF p.7: regression equations; PDF p.7: C4 context randomly sampled. | 报告了主要协变量与过滤规则，但未系统列出全部控制变量及其控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF p.7: 'We considered controlling for sentence topic... results quite similar without this control, we decided to omit it'; PDF p.6: English-centric and single-turn limitations. | 识别了主题、长度、语境、语料代表性等潜在混淆并做部分稳健性检验，但未系统报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | 0.5 | PDF p.4: mixed-effects logistic regression with sentence type, fine-tuned indicator and 'their interaction'; asymmetric effect reported; PDF p.4: model size analysis. | 有调节/交互检验（微调、模型类型、模型规模），但缺中心化/标准化说明和正式简单斜率分析。 |
| A6 | 中介变量 | NA | — | 全文无中介假设或中介效应分析。 |
| A7 | 操作性定义 | 1 | PDF p.6–7: prompts ('We are'/'They are' vs context+instruction template), word-count and 5-gram filtering, RoBERTa classification, and logistic regression equations. | 关键构念的操作化（群体提示、句子生成、情感计分、优势比）可复现。 |
| A8 | 水平数与类型 | 0.5 | PDF p.2 and p.6: two sentence groups and two prompt settings; PDF p.4: fine-tuning with 0%/50% removal and multiple model sizes. | 主要水平与标签报告了；连续规模/比例变量的水平类型、间距、全距和中心化说明不完整。 |
| A9 | 单一操作化的风险 | 1 | PDF p.2: robustness checks with ten alternate sentiment classification strategies; PDF p.7: prompt variations; PDF p.6: 'simplified view... not meant as a sentence-level classifier'. | 多种分类器和提示变式提供会聚证据，并明确讨论单一探针的可推广性限制。 |
| A10 | 单一方法的风险 | 0.5 | PDF p.2: generated sentences are classified by 'a separate pretrained classification model'; PDF p.7: alternate classifiers robustness. | 条件与结果均来自同一生成文本，未做正式共同方法偏差检验；仅有方法稳健性，故 0.5。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立模型组分配；每个模型在同一研究中生成 ingroup 与 outgroup 句子，不能按人类被试间设计编码。 |
| B2 | 被试内设计 | 0.5 | PDF p.2: each model generated 2,000 sentences (1,000 per group) with 'We are' and 'They are'; PDF p.7: regressions use 1,000 per group. | 模型内比较两个句子群体，属重复生成；但未报告条件生成顺序、随机化或平衡方案。 |
| B3 | 混合设计 | 0.5 | PDF p.4: mixed-effects logistic regressions including 'model and partisanship as random effects'; sentence type and fine-tuning as fixed effects. | 存在模型内（句子类型）与模型间（微调/模型类型）因素，但未逐因素明确标注组间/组内并分别报告误差项。 |
| B4 | 因子设计 | 0.5 | PDF p.4: 'binary indicators of sentence type, whether the model was fine-tuned or not, and their interaction'; Fig. 3. | 有 2×2 式因素与交互，但未给完整设计矩阵、每格样本量和 ANOVA 式完整统计表。 |
| B5 | 主效应 | 0.5 | PDF p.4: main effects of sentence type and fine-tuning reported as odds ratios with CIs; Fig. 2/3. | 主效应以 OR/CI 报告，但无 F、df、ηp²；交互存在时未系统声明主效应解释受限。 |
| B6 | 交互作用 | 0.5 | PDF p.4: interaction between sentence type and fine-tuning; 'outgroup sentences are especially likely to be negative after fine-tuning'; Fig. 2/3 error bars. | 报告了交互并在图中有 CI，但缺简单主效应检验与多重比较校正。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计；模型族仅作随机效应，不是区组设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方或顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；微调比较不是人类非随机分组设计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内顺序处理/可逆性设计；LLM 句子独立生成，微调使用独立模型副本。 |
| C1 | 随机化 | NA | — | 每个模型固定接受两种提示，无随机分配模型到条件；C4 上下文仅随机采样，不是处理分配随机化。 |
| C2 | 平衡 | NA | — | 无有序条件呈现，故无顺序平衡要求。 |
| C3 | 恒定 | 0.5 | PDF p.6: 'nucleus sampling with a set P value of 0.95 and a temperature value of 1.0'; '8-bit precision'; 'A100-SXM-80GB'; maximum generation length 50. | 列出主要恒定生成参数，但未列全 API 模型快照/日期等；外部效度限制有讨论但不完整。 |
| C4 | 匹配 | NA | — | 无被试匹配；对人类语料随机降采样至相同规模，不是匹配变量控制。 |
| C5 | 纳入为变量 | 0.5 | PDF p.2 and p.7: TTR and total tokens included as covariates in logistic regressions; model/party as random effects. | 已知混淆纳入模型，但未检验斜率齐性/ANCOVA 假设，也未报告调整后效应量。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类被试/评分者盲法可行。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 句子生成无练习块或学习曲线；条件独立。 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳；生成任务短且自动。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个提示/模型生成相互独立；微调使用独立副本；无跨条件清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移设计。 |
| D5 | 范围效应 | NA | — | 因变量为自动情感分类/优势比，不是主观量表绝对判断。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选项或序列刺激；提示中 C4 上下文随机采样但不属选项/处理顺序平衡。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征或事后访谈。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试/评分者。 |
| E6 | 天花板 / 地板效应 | 0 | PDF p.3 Fig. 1 reports odds ratios with 95% CIs; PDF p.7 only gives filtering rules; no positivity/negativity rate distribution or endpoint frequencies. | 未报告主要因变量分布/端点频率，无法排查天花板/地板；按适用但未做记 0。 |
| E7 | 共同方法偏差 | 0.5 | PDF p.2: sentence group and sentiment derived from same generated sentence; PDF p.7: alternate classifiers used for robustness. | 同源文本测量，仅有替代分类器稳健性，无正式 CMB 程序控制/统计检验。 |
| F1 | 统计结论效度 | 0.5 | PDF p.2: significance threshold P<0.0004 (0.05/112); PDF p.3 Fig. 1 odds ratios with 95% CI; PDF p.7 N=2,000 sentences/model. | 报告效应量/CI 和多重校正，但无事前功效分析/样本量依据。 |
| F2 | 内部效度 | 0.5 | PDF p.6–7: fine-tuning procedure and model list; PDF p.4: base vs fine-tuned comparisons; limitations p.6. | 报告了主要处理和基线比较，但无随机分配/分配隐藏、基线等价检验或正式内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | PDF p.2: RoBERTa classifier; robustness with ten classifiers; PDF p.6: 'simplified view... not meant as a sentence-level classifier'. | 有构念论证和替代分类器效度证据，但无正式信度统计和操纵检验。 |
| F4 | 外部效度 | 1 | PDF p.6: 77 LLMs list and sources; PDF p.5 Study 3 uses WildChat/LMSYS; PDF p.6 discusses English-centric and single-turn boundaries. | 样本来源、多模型/多语料复现和推广边界均有明确报告。 |
| G1 | 分析单位 | 0.5 | PDF p.2 and p.4: mixed-effects models with model name as random effect; PDF p.8 Study 3 uses dataset as random effect. | 分析层级（句子嵌套于模型/数据集）有随机效应处理，但未明确说明分配层级与分析层级匹配的原则。 |
| G2 | 随机效应 | 0.5 | PDF p.4: 'model and partisanship as random effects'; PDF p.8: 'dataset variable as a random effect'. | 报告了主要随机效应因子，但未完整说明随机截距/斜率结构及可推广总体。 |
| G3 | 材料作为随机效应 | NA | — | 没有把有限项目/材料作为自变量载体；句子是生成输出，非固定材料随机抽样设计。 |
| G4 | 统计功效 | 0.5 | PDF p.2: 2,000 sentences per model; PDF p.7: minimum 1,000 distinct per group; Fig. 1 CIs. | 报告了样本规模和效应量/CI，但无事前功效分析或预期效应量依据。 |
| G5 | 研究者自由度 | 0.5 | PDF p.7: exclusion if fewer than ten characters/five words or 5-gram overlap; 'between 40 and 70% of raw sentences were filtered out'; all 77 models listed. | 排除规则和模型清单较透明，但未区分验证/探索分析、未说明停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | PDF p.6–8 Methods and PDF p.10 OSF data/code statement; no preregistration mentioned. | 无公开预注册或分析计划登记；按未预注册记 0。 |
| J1 | 位置偏差 | NA | — | 无多候选选择、排序或 LLM-as-judge 成对比较。 |
| J2 | 冗长偏差 | NA | — | 使用自动情感分类而非 LLM 裁判；虽有长度协变量，但不存在生成质量长度偏差评价。 |
| J3 | 谄媚 | NA | — | 无用户先验立场操纵或谄媚测量。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge，故无自我偏好偏差。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 为零样本提示，无 few-shot 示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF p.6: full default and instruction prompt templates; PDF p.8: alternative group-identity prompts 'showing similar results'. | 提供模板并做了部分提示变式稳健性，但无版本/日期、dev/test 划分或系统敏感性消融。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文仅为一句 C4 文本，远低于长上下文/RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | PDF p.6: nucleus sampling P=0.95, temperature=1.0, max generation length 50; 1,000 sentences per group. | 报告主要采样参数和大量重复，但未报告随机种子、top-k、API 快照日期。 |
| J9 | 重复与文本退化 | 0.5 | PDF p.7: 5-gram overlap filtering and min word/character thresholds; PDF p.6: nucleus sampling. | 报告解码并过滤重复，但未报告 n-gram 重复率/退化率等 QC 指标。 |
| J10 | 分词效应 | NA | — | 单语言英文研究，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 不是公开基准测试；生成句子为研究探针，不涉及测试集污染评估。 |
| J12 | 基准饱和 | NA | — | 无基准饱和问题。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/格式约束输出。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | PDF p.1: LLMs as 'compelling proxies for studying human behavior'; PDF p.4: human-corpus baseline; PDF p.6: limitations 'simplified view... English-centric'. | 明确讨论 LLM 构念与人类构念并可做同类句子对照，但闭源模型快照不精确，理论异同讨论仍不完整。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未宣称跨规模涌现/突变；仅报告规模与偏差的回归。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标的优化或奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF p.2: 2,000 sentences/model; Fig. 1/2/3 odds ratios with 95% CIs; PDF p.6 model list, but no exact API snapshot dates. | 报告 N 和 CI，但 snapshot/seed 不精确，模型比较未系统做配对检验。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | PDF p.5: Study 3 uses WildChat/LMSYS 'natural dialogs'; PDF p.6: limitation 'our measure of bias is single-turn... multi-turn'. | 分析了真实对话数据但未按轮次独立评分或控制上下文截断，不能识别跨轮衰减。 |

## 编码小结
论文核心发现清楚，提示、生成、过滤、情感分类和回归流程相对可复现；但研究不是人类被试实验，许多分配、顺序、盲法等组件不适用。主要不足是：模型快照/采样种子等复现信息不完整，操纵检验与正式信效度统计不足，且未预注册。
