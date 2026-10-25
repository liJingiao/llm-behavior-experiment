# article_078 | From Dogwhistles to Bullhorns: Unveiling Coded Rhetoric with Language Models | 2023

研究类型概述：计算语言学/NLP 研究：构建狗哨词分类与词表，对历史国会演讲做观察性案例研究，并用 GPT-3/ GPT-4 进行提示词操纵下的狗哨识别与生成评估，另用 Perspective API 做毒性检测评估。无人类被试；分析单位主要是狗哨词条、提示变体、模型生成文本、HateCheck 模板句和 API 分数。
- **研究构念（Construct）**：隐语/狗哨修辞理解与群体条件化社会意义推断（coded rhetoric/dogwhistle interpretation and group-conditioned social meaning）｜CA 构念锚定：语言理解（language comprehension, `trm_4a3fd79d0a775`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：计算语言学/NLP 研究：构建狗哨词分类与词表，对历史国会演讲做观察性案例研究，并用 GPT-3/ GPT-4 进行提示词操纵下的狗哨识别与生成评估，另用 Perspective API 做毒性检测评估。无人类被试；分析单位主要是狗哨词条、提示变体、模型生成文本、HateCheck 模板句和 API 分数。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_5: 'For each input term, we construct 12 prompts (6 definitions including none, and each with or without a secret cue).' PDF_PAGE_8: 'fill ... with a standard group label, a slur, or a dogwhistle'. | 提示定义、secret cue 和替换词类别被明确操纵，水平数与取值基本清楚；但操纵检验、单位分配细节和随机化未报告。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_6: 'The first author manually evaluated whether or not each of the 5,760 GPT-3 generations contains the covert meaning'; PDF_PAGE_8: 'Perspective API scores a text between 0 and 1 for a range of attributes'. | 因变量指标与计分方式有界定；但缺少测量信度、效度证据及连续指标预处理/防地板天花板说明。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_5 footnote 3: 'text-davinci-002 ... max_tokens=256, temperature=0.0 ... num_outputs=1'; PDF_PAGE_14: 'temperature=0.7, and num_outputs=5'. | 报告了模型版本及部分解码超参数等恒定条件；但没有系统列出控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_9: 'GPT-3’s performance ... may be ... because ... fewer data from transphobic communities ... formatting'; PDF_PAGE_10: 'operationalize dogwhistles as a static binary'. | 识别了训练数据频率、格式、词表非穷尽等潜在混淆或替代解释；但未系统控制或做敏感性分析，也未充分量化残余威胁。 |
| A5 | 调节变量 | NA | — | 论文没有正式提出调节变量假设或进行调节/交互模型检验；按分类词表分组的描述性差异不构成受控调节分析。 |
| A6 | 中介变量 | NA | — | 研究没有中介变量或中介效应分析。 |
| A7 | 操作性定义 | 0.5 | PDF_PAGE_5: 'For each input term, we construct 12 prompts ...'; PDF_PAGE_6: 'manually evaluated whether ... contains the covert meaning'; PDF_PAGE_10: 'operationalize dogwhistles as a static binary'. | 关键构念有操作化描述，提示和评估指标较具体；但人工判断隐蔽含义的编码细则不足，狗哨构念本身也被简化为静态二元。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_5: '6 definitions including none, and each with or without a secret cue'; PDF_PAGE_8: 'standard group label, a slur, or a dogwhistle'; Table A.2 lists five definitions. | 水平数与各水平标签基本明确；但未明确说明水平类型、间距/全距或连续变量中心化等。 |
| A9 | 单一操作化的风险 | 0.5 | PDF_PAGE_5-PDF_PAGE_6: two GPT-3 tasks (covert meaning identification, surfacing); PDF_PAGE_10: 'static binary' limitation. | 对狗哨识别采用多种任务/指标，但未报告各操作间会聚证据；同时在局限部分讨论了单一静态二元操作化的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 研究不是人类自陈量表设计，IV/DV 不涉及同源自评式共同方法偏差；评估使用模型生成、人工判断和外部 API 分数。 |
| B1 | 被试间设计 | NA | — | 无人类被试或无独立被试组分配；提示条件被系统交叉/同一词条评估，不是被试间设计。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量设计及其顺序平衡结构；同一词条被多个独立提示评估，按生成/词条层级分析。 |
| B3 | 混合设计 | NA | — | 无人类组间/组内混合设计。 |
| B4 | 因子设计 | 0 | PDF_PAGE_5: '12 prompts (6 definitions including none, and each with or without a secret cue)'; PDF_PAGE_6 Table 2 reports collapsed prompt conditions. | 存在 6×2 提示词因子结构并给出部分单元结果；但未给完整设计矩阵、每格样本量及 ANOVA F/df/效应量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | PDF_PAGE_6 Table 2: '.085 [±.025] ... .543 [±.010]'; PDF_PAGE_15 Table A.6 reports definition means and 95% CIs. | 报告了定义与 secret cue 的主效应式比例及置信区间；但无正式主效应检验统计量与效应量。 |
| B6 | 交互作用 | 0 | PDF_PAGE_15: 'variation ... based on prompt features, dogwhistle register, and the interaction between the two'; Figure A.2 descriptive only. | 仅作描述性/图示化交互断言，未报告交互项统计检验、简单主效应或多重比较；按规则记 0。 |
| B7 | 区组设计 | NA | — | 无区组设计或分层随机分配程序。 |
| B8 | 拉丁方 | NA | — | 无人类被试内顺序设计，无需拉丁方平衡。 |
| B9 | 准实验设计 | NA | — | 研究不是准实验因果设计；历史演讲分析为观察性描述，LLM 评估为基准式比较。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，不涉及可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无人类被试或独立单位的随机分配；提示条件为系统构造并交叉评估。 |
| C2 | 平衡 | NA | — | 无需要平衡的条件顺序；提示生成按独立 API 调用进行，无被试内顺序平衡结构。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_5 footnote 3: model and decoding parameters; PDF_PAGE_14: 'temperature=0.7, and num_outputs=5'; PDF_PAGE_8: Perspective API description. | 报告了固定模型与部分解码/API 条件；但未系统列出所有恒定变量及其水平，也未充分讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未使用协变量或区组因素进入统计模型；词表类型/人群只用于描述性分组。 |
| C6 | 盲法 | 0 | PDF_PAGE_6: 'The first author manually evaluated whether or not each of the 5,760 GPT-3 generations contains the covert meaning'. | 存在人工评分/判断环节，但未报告盲法、施盲对象或盲法成功检验；存在评分者知道条件与假设的风险。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 无人类学习/练习效应问题；LLM 提示为独立生成。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留/清洗期结构；API 生成按独立提示进行。 |
| D4 | 不对称迁移 | NA | — | 无人类被试内交叉设计，不涉及不对称迁移。 |
| D5 | 范围效应 | NA | — | 不涉及人类主观量表判断的范围效应。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选项、序列刺激或人类被试内处理顺序；提示词为独立构造与调用。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征与事后访谈问题。 |
| E5 | 实验者效应 | NA | — | 无人类主试与参与者互动；人工评估偏差已在 C6 记录。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_6 Table 2 reports proportions with CIs; PDF_PAGE_7: 'full 100% recall of Islamophobic dogwhistles'. | 报告了比例、均值式结果和部分置信区间，可观察二元端点；但未报告分布/偏度/端点频率，也无 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念同源测量，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_6 Table 2: '±.025' etc.; PDF_PAGE_15 Table A.3: '95% CI'; PDF_PAGE_5 footnote 3 for generations. | 报告了部分比例及置信区间；但无样本量确定依据/功效分析，且多组比较未说明多重性校正。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_5 describes 12 prompts per term and 5,760 generations; PDF_PAGE_9-PDF_PAGE_10 discusses training-data confounds and limitations. | 设计构造与部分内部效度威胁有描述，但无随机分配、分配隐藏、基线等价或被试流向/损耗处理。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_10: 'operationalize dogwhistles as a static binary'; PDF_PAGE_5-PDF_PAGE_6 manual evaluation procedure. | 对构念局限和词表来源有讨论，但没有评分者信度、正式效度证据或操纵检验；单一操作化局限被承认。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_10: 'they are all in English with the vast majority coming from the U.S. political and cultural contexts'; PDF_PAGE_4 glossary size. | 报告了材料来源与语言/文化边界，并讨论推广限制；但无跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_5: '480 variants with 12 prompts ... 5,760 generations'; PDF_PAGE_6: precision/recall computed over glossary terms and generations. | 说明了提示/生成/词条等层级，但统计上把生成聚合为比例并用置信区间，未显式建模生成嵌套于词条/提示的聚集结构。 |
| G2 | 随机效应 | NA | — | 无人类被试随机效应或混合模型；模型/条件作为固定处理，材料推广问题见 G3。 |
| G3 | 材料作为随机效应 | 0.5 | PDF_PAGE_5: 'We generate responses for each dogwhistle in the glossary'; PDF_PAGE_10: 'our glossary is not exhaustive'. | 承认词表非穷尽、材料有抽样局限；但分析中未把词条/材料作为随机效应，也未用混合模型推广到材料总体。 |
| G4 | 统计功效 | 0 | PDF_PAGE_5-PDF_PAGE_8: no power analysis or sample-size justification; PDF_PAGE_6 only reports proportion CIs. | 无事前功效分析或其他样本量论证，也未系统报告效应量与 CI 作为功效依据。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_5: 'We generate responses for each dogwhistle in the glossary'; PDF_PAGE_10: 'initial push' and limitation discussion; exact prompts in project repository. | 报告了主要词表/生成数量及部分探索性定位，但未完整列出全部提示条件、排除规则和验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | PDF_PAGE_5-PDF_PAGE_10: no preregistration or registered analysis plan mentioned. | 无公开预注册；分析路径和探索性结果未与预注册计划对照。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较中的位置偏差。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判对开放生成质量评分，故无长度被误当质量的裁判偏差。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或对话式纠错操纵。 |
| J4 | 自我偏好 | NA | — | 无 LLM-as-judge 评估模型输出，故自我偏好/同源裁判偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验未使用 few-shot in-context learning 示例集；GPT-4 部分为指令式、零样本/单条文本识别。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_5: 'we construct 12 prompts (6 definitions including none...)'; PDF_PAGE_14: 'Exact prompt text can be found in our project repository.' | 报告了多定义提示敏感性并指向完整模板，但未给出版本/迭代日期、dev/test 划分或系统语义等价消融。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文或 RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_5 footnote 3: 'temperature=0.0 ... num_outputs=1'; PDF_PAGE_14: 'temperature=0.7, and num_outputs=5'. | 报告了主要采样超参和输出次数，但未报告随机种子、top-p/top-k、API snapshot/日期或按条件重复采样的完整方差估计。 |
| J9 | 重复与文本退化 | 0.5 | PDF_PAGE_14: 'post-process by: splitting by newline characters, removing enumeration ...'; PDF_PAGE_5 footnote 3 decoding details. | 报告了解码设置和后处理；但未报告重复率/退化率等生成质量指标，也未系统比较解码策略对结果的影响。 |
| J10 | 分词效应 | NA | — | 材料主要为英语单词/短语，无跨语言或跨脚本比较；PDF_PAGE_10 明确限制为 English/U.S. 语境。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_9: 'the model is simply memorizing articles or social media posts that explicitly call out certain expressions as dogwhistles'; no cutoff or overlap check reported. | 仅定性提醒训练数据/记忆风险，未报告测试集与训练截止日期对照、污染检测、污染率或 held-out 验证。 |
| J12 | 基准饱和 | NA | — | 研究使用自建词表/任务而非有明确 SOTA 与饱和风险的基准；未宣称在饱和基准上显著提升。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，也没有按约束类型测量可机器判定的指令遵循。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求严格结构化输出；仅有枚举列表后处理，未做格式合法率分析。 |
| J15 | 越狱稳健性 | NA | — | 不是安全/越狱评估；虽研究毒性检测规避，但未测自然拒绝率与对抗攻击成功率。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究将 GPT-3 作为 NLP 工具评估狗哨识别能力，不主张测量与人类同名的心理学构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨模型规模或训练进展的能力曲线，不涉及涌现/指标诱导假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无训练、RL、best-of-N 或对代理指标的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_5 footnote 3: 'text-davinci-002'; PDF_PAGE_14: hyperparameters; PDF_PAGE_6 Table 2 CIs; project repository mentioned. | 报告了模型名、部分超参、生成数量和部分 CI，并发布输出；但无精确 API snapshot/日期、无配对检验，重复采样设计不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示/生成，无多轮对话一致性衰减问题。 |

## 编码小结
论文将资源构建、观察性历史分析与多项 LLM/毒性检测基准评估结合。与人类实验设计相关的分配、平衡、盲法等组件大多不适用；提示词因子操纵、模型评估可复现性、统计报告和材料随机效应等组件部分报告但不完整。主要缺陷包括无预注册/功效分析、无系统污染检查、无评分者间信度、提示条件与词条/生成本身的嵌套未建模。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
