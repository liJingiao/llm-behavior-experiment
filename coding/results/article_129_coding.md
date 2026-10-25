# article_129 | Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs | 2025

研究类型概述：论文提出不确定性感知公平性指标 UCerF 和 SynthBias 数据集，并在多个开源 LLM 上做性别—职业代词指代公平性基准评测。分析单位是模型×样本/任务条件的评测结果，不是人类被试实验，也没有对模型或人类被试进行条件随机分配。
- **研究构念（Construct）**：性别—职业联结偏差中的置信度不对称｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：让十个现成开源LLM完成性别代词—职业共指最小对任务。（在语义相同的句子中替换性别代词、职业和句式复杂度，比较顺/逆刻板条件。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | — | 本研究是基准评测，模型、数据集和任务类型是比较对象而非研究者主动操纵并随机分配的自变量；无操纵程序或操纵检验，故不适用。 |
| A2 | 因变量 | 0.5 | p.4 p.4: Eqs. (1)-(5) define normalized certainty, desirability, and UCerF; p.6 p.6: 'we calculate the accuracy, equalized odds (EO), and perplexity (Jelinek et al., 1977) along with UCerF.' | 因变量指标和计分公式明确，但未报告这些指标的信度/效度证据，也未说明连续指标的预处理或防端点效应方案。 |
| A3 | 控制变量 | 0.5 | p.6 p.6: 'We use the official checkpoints for evaluation. Each experiment is evaluated on five random seeds.' | 报告了固定官方 checkpoint 与五次随机种子等部分控制，但没有系统列出所有控制变量及控制手段，也未报告温度、解码参数等关键恒定设置。 |
| A4 | 混淆变量 | NA | — | 无操纵自变量和因果推断，属于观察性基准比较；不存在传统内部效度意义上的自变量混淆控制问题。 |
| A5 | 调节变量 | NA | — | 论文没有调节变量假设，也没有乘积项交互检验或简单斜率分析。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量假设，也没有直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.4 p.4: UCerF equations; p.6 p.6: intrinsic prompt 'The pronoun <pronoun> refers to the' and MCQ prompt; p.16-p.17 p.16-p.17: full GPT-4o generation prompts. | 关键测量与指标给出可复现公式；预测提取、perplexity 计算、任务 prompt 和数据生成 prompt 均有明确操作化，足以复现主要流程。 |
| A8 | 水平数与类型 | NA | — | 没有把某个多水平变量作为实验自变量并报告其水平类型、间距和全距；模型/数据集/任务只是评测分组。 |
| A9 | 单一操作化的风险 | 0.5 | p.23-p.24 p.23-p.24: Table 9 compares UCerF under perplexity, Rényi divergence, and Fisher-Rao distance; 'Some consistency can be observed ... Falcon-40B is ranked second most fair under all three uncertainty estimators.' | 关键的不确定性构念用了多种估计器并给出一定会聚证据，但主要是排名一致性的定性报告，缺少正式的会聚效度统计；对单一数据集/单一主要指标的局限讨论也有限。 |
| A10 | 单一方法的风险 | NA | — | 研究不使用人类自陈量表，也不是自评式多构念测量；所有指标均由模型预测概率和客观数据集计算，共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试间分配；模型评测不是把独立被试分配到互斥条件。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量与条件顺序平衡设计；每个模型在样本上评测但无被试顺序分配。 |
| B3 | 混合设计 | NA | — | 没有需逐因素标注组间/组内的混合实验设计。 |
| B4 | 因子设计 | NA | — | 没有实验因子设计、完整设计矩阵或每格样本量；多模型/多数据集结果只是评测组织，不是因子实验。 |
| B5 | 主效应 | NA | — | 不是因子实验，无主效应检验与交互受限解释。 |
| B6 | 交互作用 | NA | — | 没有交互项统计检验与简单效应分析。 |
| B7 | 区组设计 | NA | — | 没有区组变量、区组划分和区内随机分配。 |
| B8 | 拉丁方 | NA | — | 没有被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计，也没有非随机分组下的因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内设计的可逆性/迁移对称性适用条件问题。 |
| C1 | 随机化 | NA | — | 没有实验条件分配与随机化；MCQ 选项随机顺序属于刺激位置控制，不是被试/单位分配。 |
| C2 | 平衡 | NA | — | 没有条件顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p.6 p.6: 'We use the official checkpoints for evaluation. Each experiment is evaluated on five random seeds.' | 固定了模型 checkpoint 和随机种子等部分环境变量，但未系统报告温度、解码设置、运行环境等恒定水平，也未讨论固定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有采用匹配设计或匹配变量。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组或协变量纳入协方差分析；FP 指标是性能与公平性的组合，不是协变量控制。 |
| C6 | 盲法 | NA | — | 模型评测为自动评分，没有需要对条件施盲的人类被试/评分者；人类标注只用于数据集验证，不涉及实验分组盲法。 |
| C7 | 平衡的层级 | NA | — | 没有需要选择完全平衡、拉丁方或 ABBA 的顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 每个样本基本独立评测，无跨试次学习或练习效应；不涉及练习块与试次位置协变量。 |
| D2 | 疲劳效应 | NA | — | 自动模型评测无人类 session 疲劳风险；也没有长时间 session 设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个 prompt 独立，无跨条件清洗期或残留效应问题。 |
| D4 | 不对称迁移 | NA | — | 没有跨条件顺序残留与不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 不使用人类被试内绝对判断或李克特量表，无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.6 p.6: MCQ options 'including the two occupations and “None of the above” in a random order.' | 报告了选项随机顺序，但未说明随机化算法、各选项在每个位置的出现次数或位置—正确率分析。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 不是人类被试实验，没有掩饰情节或事后假设推断检查；众包标注者只做数据标注。 |
| E5 | 实验者效应 | NA | — | 模型评测完全自动化，无人类主试或人类评分者在实验条件下传递期望。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.8 p.8: Fig. 8 visualizes histograms of D(x_i) and U(x_i); p.14 p.14: Table 2 reports accuracy, EO, perplexity, UCerF means. | 报告了均值与部分分布图，但没有系统性报告偏度、端点频率或 pilot 难度校准；对天花板/地板效应的讨论不完整。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念测量，不存在共同方法偏差的同源自评问题。 |
| F1 | 统计结论效度 | 0 | p.6 p.6: 'Each experiment is evaluated on five random seeds'; p.8 p.8: Fig. 6 and p.14 p.14: Table 2 report metric values and ranks. | 仅报告点估计和排名，没有效应量、置信区间、正式模型比较检验或多重性校正，也没有样本量/功效依据。 |
| F2 | 内部效度 | NA | — | 观察性基准评测，无随机分配与因果效应主张；不适用传统内部效度评估。 |
| F3 | 构念效度 | 0.5 | p.5 p.5: human annotation with '75% consensus ... among at least four annotators'; p.6 p.6: human validation yields 31,756 samples and WinoBias comparison. | 数据集构念效度有人工验证与与 WinoBias 的比较，但未报告指标信度、评分者信度统计或 UCerF 的正式效度证据。 |
| F4 | 外部效度 | 0.5 | p.6 p.6: models 'selected based on their popularity and availability'; p.9 p.9: limitations note US-centric occupations and binary pronouns. | 报告了模型来源与部分推广边界，但不是代表性抽样，也未系统报告跨样本/跨情境复现；外部效度讨论有限。 |
| G1 | 分析单位 | 0.5 | p.6 p.6: metrics are computed and 'Each experiment is evaluated on five random seeds'; p.8 p.8: model rankings aggregate over samples. | 评测以样本级指标汇总到模型级比较，但没有明确处理样本/职业/模板的嵌套或聚类结构；因无正式推断检验，未构成严重单位错误。 |
| G2 | 随机效应 | NA | — | 模型是固定的具体 checkpoint 集合，目标是描述这些模型而非从随机模型总体推断；无混合模型随机效应需求。 |
| G3 | 材料作为随机效应 | 0 | p.4-p.6 p.4-p.6: 31,756 samples and 40 occupations; p.15 p.15: fixed WinoBias occupation list; metrics averaged across items. | 材料和职业被视为固定刺激集合，分析中没有将项目/材料作为随机效应或使用混合模型/准 F 比，结论对任意材料的推广受限。 |
| G4 | 统计功效 | 0 | p.6 p.6: ten LLMs evaluated on five seeds; no power analysis or CI reported in Fig. 6/Table 2. | 没有事前功效分析或样本量推导，也没有对模型比较报告效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.5 p.5: 'We begin the data-cleaning process with a set of automatic rule-based filters'; p.6 p.6: dataset filtering criteria and 31,756 final samples; Appendix H includes additional conditions. | 数据清洗和排除规则较详细，附录也报告了额外结果，但没有明确样本量停止规则，也未系统区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–25 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未提及预注册平台、注册编号或数据收集前分析计划；不应记 NR，因为适用但未做。 |
| J1 | 位置偏差 | 0.5 | p.6 p.6: MCQ options are presented 'in a random order'. | 涉及多选题选项位置并做了随机顺序，但未报告位置反平衡细节、交换前后翻转率或位置×正确率曲线；模型版本/采样参数报告也不完整。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判或开放式生成长短比较；评分基于下一 token 概率和 perplexity，长度偏差风险不适用。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错对话，无谄媚风险操纵。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 或模型生成互评，无自我偏好裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.5 p.5: 'Each prompt contains ... 3 positive and 3 negative samples'; p.16-p.17 p.16-p.17: full few-shot prompts. | SynthBias 生成使用了 few-shot 示例并报告了数量/比例和完整模板，但未报告示例排列反平衡、多 seed 重采样或示例选择敏感性。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5 p.5 and p.16-p.17 p.16-p.17 provide full generation prompts; p.6 p.6 gives intrinsic and MCQ evaluation prompts; p.21 p.21 explores similar sentence sensitivity. | 提供了较完整 prompt 模板，但没有版本号、正式语义等价措辞敏感性消融和 dev/test 划分说明；附录 G 主要是输入句相似性而非 prompt 模板敏感性。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为单句或短句，不涉及长文档/RAG 的信息位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | p.6 p.6: 'Each experiment is evaluated on five random seeds.' | 报告了五次重复/随机种子，但没有报告 temperature、top-p、top-k 等采样超参，也没有报告多次采样的均值±CI；评估主要用 token 概率，采样随机性披露不完整。 |
| J9 | 重复与文本退化 | NA | — | 任务不涉及开放生成文本的重复与退化评估；主要是下一词/选项概率评分。 |
| J10 | 分词效应 | NA | — | 单语言英文、单脚本研究，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.2 p.2: WinoBias is a public benchmark; p.5 p.5: SynthBias is generated by GPT-4o-2024-08-06; no training-cutoff or overlap check reported. | 使用公开 WinoBias 和自建合成数据，但没有对照模型训练截止日期、做 n-gram/DCQ 污染检测或明确证明 SynthBias 未见于训练语料。 |
| J12 | 基准饱和 | 0.5 | p.8 p.8: Fig. 6 reports model scores/ranks; p.22 p.22: MCQ type1 UCerF approaches 0.999. | 报告了基准分数量程和当前模型水位，但未系统讨论饱和、连续指标替代或 bootstrap CI；MCQ 部分已明显接近上限。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；MCQ 的作答要求不是按约束类型测量指令遵循。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | MCQ 通过 A/B/C 下一 token 概率评分，不是自由生成结构化输出，也没有格式合法率/重试策略的测量对象。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全性、越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 这是应用型 LLM 公平性基准评测，不主张把 LLM 作为人类心理学/认知科学被试，也未围绕人类同名构念做理论论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较不同规模模型，但没有跨规模/训练进展的能力曲线，也不宣称涌现或突变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究提出并评估 UCerF 指标，但没有把代理指标作为训练/奖励优化目标，不存在 overoptimization 设计。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6 p.6: five random seeds and 'official checkpoints'; no exact snapshot hashes, CIs, or paired tests reported. | 报告了重复次数和模型名称/官方 checkpoint，但没有每分数 CI、精确 snapshot 标识、配对检验或原始推理日志，可复现性报告不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 prompt 评测，没有多轮对话历史或跨轮一致性设计。 |

## 编码小结
这是一项 LLM 基准评测与指标/数据集构建研究，而非传统实验心理学研究。其优势是任务、指标与数据生成—清洗流程的操作化较清楚，报告了多种不确定性指标与多个数据集上的结果；不足是缺少传统实验设计组件、统计不确定性与功效论证、预注册、污染检查与精确快照/采样参数，模型比较主要依赖点估计与排名。因此大量人类被试设计组件应记 NA；与 LLM 评测直接相关的 J1、J5、J6、J8、J11、J12、J19 按实际情况部分满足或缺失。
