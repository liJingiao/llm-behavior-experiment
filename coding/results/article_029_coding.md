# article_029 | A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive | 2025

研究类型概述：理论与实证结合的 LLM 行为研究：以 LLM 为分析对象，通过提示词系统操纵描述性成分（输入分布均值 Cμ）与规范性成分（Cv/理想值），在虚构概念、500 个既有概念、原型评分及医学案例中检验采样偏倚；包含多模型比较，另附录报告人类实验/人类研究对照。
- **研究构念（Construct）**：描述性与规范性反应采样启发式（descriptive versus prescriptive sampling heuristics）｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：理论与实证结合的 LLM 行为研究：以 LLM 为分析对象，通过提示词系统操纵描述性成分（输入分布均值 Cμ）与规范性成分（Cv/理想值），在虚构概念、500 个既有概念、原型评分及医学案例中检验采样偏倚；包含多模型比较，另附录报告人类实验/人类研究对照。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p3: 'We run the experiment with the following setting for Cv: a higher value being ideal, a lower value being ideal, and a control experiment having no explicit ideal direction'; p5: 'positive, negative, and neutral (control experiment)'; p6: 'vary Cmu in the range of 45 to 845 in intervals of hundreds' and 'eight different grading scheme'. | 自变量 Cv 与 Cμ 被明确命名并给出至少两个水平及取值，也说明用独立提示上下文重复 100 次；但未报告正式操纵检验，水平分配/随机化细节也不完整，故 0.5。 |
| A2 | 因变量 | 0.5 | p4: 'α = (A(C) − S(C)) × sign(A(C) − I(C))'; p8: 'Cronbach’s alpha of 0.96' for prototype composite; p6 Table 1 reports means of A(C) and S(C). | 因变量指标与计分方式清楚（S(C)、A(C)、I(C)、α/α̂、7 点原型评分），但主要采样指标没有信度/效度证据，也没有连续指标预处理或天花板/地板说明；仅原型评分报告 α，故 0.5。 |
| A3 | 控制变量 | 0.5 | p3: 'keeping the rest of the prompt same'; p5: 'we use the same prompt in all cases, varying only Cv'; p4: prompts are in 'independent contexts'. | 报告了若干控制手段（保持提示词相同、独立上下文、虚构概念、无评分/随机评分控制），但未系统列出全部控制变量及逐一控制方式，故 0.5。 |
| A4 | 混淆变量 | 0.5 | p3: 'we introduce a novel concept C to eliminate potential confounding effects associated with using pre-existing concepts'; p5: 'To exclude this alternative explanation, we compute the significance in the shift ... from the average reported by the LLM'; p9: 'the origin of these norms ... remains under-explored'. | 识别并控制了先验知识、分布近似误差、提示词等潜在混淆，并讨论规范性来源未解；但未系统报告残余混淆的敏感性分析，故 0.5。 |
| A5 | 调节变量 | NA | — | 论文未提出或检验调节假设；模型规模/RLHF 仅作描述性比较，未作为正式调节变量建模。 |
| A6 | 中介变量 | NA | — | 论文未提出或检验中介假设，也没有直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p3–p5 详细描述 Cμ、Cv、A(C)、I(C)、S(C) 的创设与提问方式；p20、p24–p26、p29–p30 给出完整提示词与原型材料；p4 给出 α 公式。 | 关键构念均有可复现的操作化：提示词、评分等级、采样问题、α 计分和原型材料均给出。 |
| A8 | 水平数与类型 | 0.5 | p5: Cv 为 positive/negative/neutral 三水平；p6: Cμ 从 45 到 845、每 100 一档并配合 8 种评分峰值；p8: 原型评分为 7-point scale。 | 报告了主要水平数与取值，但未完整说明水平类型、间距/全距及连续变量入模中心化等细节，故 0.5。 |
| A9 | 单一操作化的风险 | 1 | p4: 与人类研究对照；p5–p6: 多种 Cμ、多种提示词和不同虚构词；p6–p7: 500 个概念、10 个领域、15 个模型；p8: 原型评分另设实验；p17–p19 报告提示词稳健性。 | 关键构念采用多种操作化/材料/模型，并报告跨设置会聚结果；对局限也有讨论。 |
| A10 | 单一方法的风险 | 0.5 | p4: 各测量在 'independent contexts (i.e., prompts)' 中完成；p5–p6: 强调同一提示词仅改变 Cv；但无共同方法偏差统计检验。 | IV 与 DV 均通过 LLM 提示词实现，存在同方法风险；论文用独立上下文和提示词变体作程序性缓解，但未报告 CMB 统计检验，故 0.5。 |
| B1 | 被试间设计 | NA | — | 无人类被试组间分配；LLM 条件由独立 API 提示调用承担，不是经典被试间设计。 |
| B2 | 被试内设计 | NA | — | 没有同一 LLM ‘被试’在固定上下文中接受全部水平的重复测量设计；每次提示为独立上下文，故不按人类被试内设计编码。 |
| B3 | 混合设计 | NA | — | 无人类组间/组内混合设计，也无相应的混合误差项。 |
| B4 | 因子设计 | 0 | p3–p6: 系统变化 Cv 与 Cμ；p6 Table 1、p16 Table 6 和 Figure 7 展示联合变化，但全文未报告交互项统计量或完整设计矩阵。 | 存在多因素系统操纵，但未报告交互检验；按编码表‘多因素但完全未报告交互项’记 0。 |
| B5 | 主效应 | 0.5 | p5–p6: 报告 Cv 正/负条件下 S(C) 与 A(C) 的 Mann-Whitney p 值；p16 Table 6 报告不同 Cμ 下样本均值变化。 | 报告了主要因素效应的统计检验/均值模式，但缺少 F/df、效应量与交互受限说明，故 0.5。 |
| B6 | 交互作用 | 0 | p16 Figure 7 仅以图形展示 Cμ 与 Cv 的联合变化；未见交互项 F、df、p、效应量或简单效应检验。 | 未对交互项作统计检验，不能仅凭图形交叉断言交互。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；LLM 条件由提示词系统设定，没有自然分组/不可随机分配情形。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及人类被试内处理的不可逆性/迁移对称性问题；LLM 各条件为独立上下文。 |
| C1 | 随机化 | 0 | p3: 'in independent contexts (i.e., prompts), we repeat the procedure M times'; p6: 每个组合运行 100 次，但未报告随机分配、随机数工具或分配隐藏。 | 条件由固定提示词系统分配，未报告随机化机制；不是概率分配。 |
| C2 | 平衡 | NA | — | 各条件为独立提示上下文，无需要平衡的条件顺序。 |
| C3 | 恒定 | 0.5 | p6: GPT-4 主实验使用 temperature 0.8；p28 Table 15 报告 GPT-4 temp 0；p4 列出模型族与版本名；p3 'keeping the rest of the prompt same'。 | 报告了部分恒定变量（模型、温度、提示词）及其水平，但未系统讨论其对外部效度的限制，故 0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配程序。 |
| C5 | 纳入为变量 | 0.5 | p7 Table 2 按模型规模/RLHF 状态比较显著性；p7 讨论 'larger model sizes' 与 'RLHF exacerbates it'。 | 模型规模/训练阶段等已知混淆被观察并纳入比较，但未作为正式协变量/区组并检验斜率齐性，故 0.5。 |
| C6 | 盲法 | NA | — | 数据采集完全自动化，无人类被试/主试/评分者盲法安排。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级可报告。 |
| D1 | 练习效应 | NA | — | LLM 每次条件为独立提示上下文，无上下文内练习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳问题；LLM 调用为短提示任务。 |
| D3 | 延滞 / 迁移效应 | NA | — | 独立上下文且无跨条件残留/洗脱期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性设计。 |
| D5 | 范围效应 | 0.5 | p8: 原型评分使用 '7-point scale ranging from not at all average/ideal/... to completely average/ideal/...'; p31 Table 18 给出各原型评分。 | 报告了量表锚点，但未讨论范围效应或采用被试间对照，故 0.5。 |
| E1 | 位置 / 顺序偏差 | 0 | p20 示例提示词中 100 个 glubbing 小时及等级以固定列表呈现；未报告对选项/刺激顺序的随机化或反平衡。 | 存在多项刺激/选项序列，但未报告任何位置/顺序控制，记 0。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表；原型评分为 7 点示例评分而非正反向题量表。 |
| E3 | 极端 / 中间反应倾向 | 0.5 | p8 和 p31 Table 18 报告原型评分均值及逐项评分；但未报告偏度、端点/中点使用比例或反应风格校正。 | 有评分数据且可观察分布，但未系统报告分布形态或跨模型反应风格威胁，故 0.5。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征；LLM 提示任务不涉及掩饰情节或事后访谈。 |
| E5 | 实验者效应 | NA | — | 完全自动化 API 采集，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p6 Table 1 报告 S(C)/A(C) 均值；p31 Table 18 给出 0–7 评分原始值；但未报告端点频率或 pilot 难度校准。 | 报告了均值/SD 与部分原始分布信息，但未系统排查天花板/地板效应或说明任务难度校准，故 0.5。 |
| E7 | 共同方法偏差 | NA | — | 不是人类同源自陈式多构念测量；共同方法问题已在 A10 按 LLM 提示方法处理。 |
| F1 | 统计结论效度 | 0.5 | p6 报告 p=0.003、p<0.001 等；p7 Table 2 报告显著性/比例；p4 定义 α；但无 95%CI、功效分析或多重比较校正说明。 | 报告了效应量式指标（α、比例）与 p 值，但缺少 CI、样本量依据和多重性校正，故 0.5。 |
| F2 | 内部效度 | 0.5 | p3–p6: 用独立上下文、同一提示词、A(C) 对照、无评分/随机评分控制排除提示词和统计近似误差；但无随机分配/分配隐藏和被试流向。 | 对内部效度威胁有评估和控制，但非随机分配且无分配隐藏/流向报告，故 0.5。 |
| F3 | 构念效度 | 0.5 | p8: 原型评分 'Cronbach’s alpha of 0.96'；p4: 用 A(C)≈Cμ 作统计近似检查；p6–p8 与人类研究比较。 | 报告了部分信度与操纵/近似检查，但主要采样指标缺少效度证据和系统多操作化论证，故 0.5。 |
| F4 | 外部效度 | 0.5 | p6–p7: 500 个概念、10 个领域、15 个模型；p8: 8 个概念×6 个 exemplar；p9: 讨论医疗与公平等应用边界。 | 报告了样本/材料来源和跨模型/跨领域复现，但未给出抽样框、代表性或明确推广边界，故 0.5。 |
| G1 | 分析单位 | 0.5 | p6: 'For each concept, we run the three prompts ten times...'; p7: 跨概念用 binomial test；p8: 跨 exemplar 聚合。 | 说明了提示/运行/概念的分析层级，但未用多层模型显式处理概念、exemplar 与模型嵌套，故 0.5。 |
| G2 | 随机效应 | 0 | p6–p8: 结果以逐概念 binomial 检验、均值比较和跨模型表格呈现；全文未见随机效应或混合模型说明。 | 概念/模型本可视为从更大总体抽样，但分析未包含随机效应结构，推断可推广性受限。 |
| G3 | 材料作为随机效应 | 0.5 | p8: 8 个概念、每个 6 个 exemplar；p31 Table 18 逐 exemplar 报告评分；但未报告 item random effect 或准 F/混合模型。 | 材料被当作多项目抽样并汇总，但未在模型中将材料/项目作为随机效应，故 0.5。 |
| G4 | 统计功效 | 0.5 | p6: 每个条件运行 100 次；p7 Table 2 报告显著性/比例；p4 定义 α；无事前功效分析或 CI。 | 报告了效应量式指标与重复次数，但缺少设计阶段功效分析和置信区间，故 0.5。 |
| G5 | 研究者自由度 | 0.5 | p6: 'Prompts failed for 10 concepts and the value of A(C) and I(C) were the same for 46 concepts'; p8: 原型实验报告 39/46；p17–p19 报告提示词变体。 | 报告了部分排除规则与大量条件，但未完整说明所有因变量/条件的验证性-探索性区分及样本量停止规则，故 0.5。 |
| G6 | 预先设定 / 预注册 | 0.5 | p12 Appendix D: 'A total of 1,200 participants were assigned across six conditions in a 2 × 3 pre-registered design.' 但无注册平台/编号、分析计划或偏离说明。 | 附录提及人类实验为预注册设计，但主 LLM 实验未见预注册细节，且无注册链接/分析计划，故 0.5。 |
| J1 | 位置偏差 | 0 | p20 提示词以固定顺序列出 100 个样本选项；p17–p19 只改变提示措辞，未报告选项位置反平衡或交换前后翻转率。 | LLM 从列表中采样，存在选项位置风险，但未报告位置随机化/反平衡。 |
| J2 | 冗长偏差 | NA | — | 不涉及 LLM-as-judge 对开放式生成长短的质量评分。 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈/纠错对话式评估。 |
| J4 | 自我偏好 | 0 | p17 Appendix H.2: 'We use a critique model which could encourage deliberation...'; 仅报告 critique score 与样本值相关，未报告裁判模型身份、是否与被评模型同源或匿名化。 | 使用了 LLM 批判/评分模型，但未识别或控制自我偏好/同源裁判偏差。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验不是 few-shot in-context learning 示例选择；提示中的 100 个带等级样本是输入分布材料，不是 few-shot 示例集。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p17: 'To show that the observations ... are not caused by specific choice of prompt we perform the experiments with different variations'; p17–p19 报告多种提示词变体/debiasing prompt；p20 给出完整提示词。 | 提供完整提示词并做敏感性消融，但未报告提示词版本/日期、dev/test 划分或完整 prompt 搜索过程，故 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短提示词/100 个数值样本，不涉及长文档或 RAG 位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | p6: GPT-4 主实验 'temperature of 0.8'；p28 Table 15: 'GPT-4 (Temp 0)'；p6 每个设置运行 100 次并报告均值/显著性；未报告 top-p、seed 或 CI。 | 报告了温度与重复次数，但缺少 top-p/top-k、seed、精确 snapshot 和置信区间，故 0.5。 |
| J9 | 重复与文本退化 | NA | — | 输出为数值/评分，不涉及开放式长文本退化或重复率控制。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言单脚本，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 不是标准基准评测；使用虚构概念与既有常识概念，未以公开测试集分数作泛化结论，故不按基准污染编码。 |
| J12 | 基准饱和 | NA | — | 不涉及标准基准饱和。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p20: 'Print only the number and not the complete sentence. The value should be an integer value between 0 and 100.' 但未报告格式合法率、解析失败率或重试策略。 | 报告了输出格式约束，但未报告格式失败率/重试策略，故 0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p2–p4: 明确以人类认知/采样理论为框架，定义 descriptive 与 prescriptive component；p8–p9: 与人类研究比较并声明 'we do not intend to contribute to humanizing' AI；p7 Table 2 将模型作为比较层面。 | 对 LLM 构念与人类同名构念的关系有界定和比较，但未报告精确权重快照，跨模型比较也未作为正式随机/规模自变量建模，故 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p7: 'The influence of prescriptive norms seems to get larger as the model size increases'，Table 2 列出不同规模模型；但未展示连续指标曲线或多 seed 的涌现检验。 | 报告了规模趋势并讨论 inverse scaling，但缺少连续指标/多种子曲线以排除指标诱导假象，故 0.5。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标的训练/优化或奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p6: 每个概念/条件运行 10 或 100 次并报告均值/SD；p7 Table 2 报告跨模型显著性；但模型仅写 GPT-4/GPT-3.5/Claude 等，无精确 API snapshot/日期或配对检验。 | 报告了重复次数和部分变异性，但缺少精确 snapshot、CI 与配对检验，故 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示，无多轮对话历史累积。 |

## 编码小结
论文提出了较清晰的理论框架并报告了大量提示词、概念、模型和重复运行结果，核心现象在多个设置下复现。但方法报告在随机化、分配隐藏、精确模型快照、主要因变量信效度、效应量/置信区间、多层/随机效应建模及部分提示/顺序控制方面不完整；部分人类实验设计组件对 LLM 分析单位不适用。
