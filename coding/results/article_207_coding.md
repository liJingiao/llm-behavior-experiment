# article_207 | Large Language Models are Geographically Biased | 2024

研究类型概述：这是一项面向 LLM 的地理—社会经济刻板偏差的零样本基准/观察性评估：在采样地理坐标上构造统一 prompt，让多个 LLM 对客观主题、敏感主观主题和地理独立主题给出 0.0–9.9 评分，并与地理真值或社会经济锚定分布比较，提出并比较 bias score。没有人类被试、没有随机分配到实验条件，核心分析单位是模型 × 主题 × 地点评分。
- **研究构念（Construct）**：地理—社会经济刻板偏差与地域评价不平等｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：用零样本地理提示让多种现成LLM对全球地点在客观和敏感主观主题上评分，并与真实社会经济指标比较。（改变地点、客观或主观主题、模型和提示组成。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6：'We use GPT-4 Turbo ... GPT-3.5 Turbo ... Gemini Pro, Mixtral 8x7B, and Llama 2 70B'；同页列出 objective、sensitive subjective、geographically independent topics；p.4给出 prompt 前缀。 | 模型与主题作为比较条件，水平/标签较明确；但没有真正随机分配或操纵检验，故只给 0.5。 |
| A2 | 因变量 | 0.5 | p.5 eqs.1–3：Spearman ρ、MAD、bias score By=ρ·MAD·a^2；p.6定义 answer rate；p.4评分刻度为 0.0–9.9。 | 因变量指标与计分方式明确，但无心理测量式信度/效度证据或端点校准说明，给 0.5。 |
| A3 | 控制变量 | 0.5 | p.3：'To avoid the confounding factor of fine-tuning ... add a prefix ... zero-shot ratings'；p.4：'greedy sampling (temperature of 0.0)'；p.6列出模型版本。 | 报告了 zero-shot、temperature、prompt 形式和模型版本等控制，但未系统列出控制变量清单，给 0.5。 |
| A4 | 混淆变量 | 0.5 | p.3明确把 fine-tuning 视为偏差评估的 confounding factor 并用 zero-shot 规避；p.14 Table 4/5 做 prompt 元素消融。 | 识别并处理了至少一个潜在混淆（fine-tuning），但未系统讨论残余混淆与全部内部效度威胁，给 0.5。 |
| A5 | 调节变量 | NA | — | 没有调节变量假设，也没有乘积项交互检验；模型/主题差异只是分组比较，不按调节效应编码。 |
| A6 | 中介变量 | NA | — | 没有中介变量或直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | p.4 Figure 2 展示完整 prompt（坐标、地址、nearby places、评分格式）；p.5说明 2000 个 prompt 的 importance/farthest-point sampling；p.5 eqs.1–3 给出指标公式；p.6列出主题与模型。 | 关键构念的操作化程序、评分格式、采样方式和指标公式较完整，可复现性较高。 |
| A8 | 水平数与类型 | 0.5 | p.6列出 6 个 objective topics、5 个 sensitive subjective topics、5 个 geographically independent topics 以及 5 个模型；p.4评分刻度 0.0–9.9。 | 水平数与取值/标签明确，但未系统说明水平类型、间距/全距或连续变量中心化，给 0.5。 |
| A9 | 单一操作化的风险 | 1 | p.7-8]] Table 1/2 报告评分与真值/社会经济锚定分布的相关；p.8 Table 3 报告 bias score；p.13 Appendix A.2 用真实推荐型 prompt 发现一致方向；p.14用 prompt 消融检验稳健性。 | 关键构念有多种操作化/补充证据，并报告了与主评分结果的一致性，给 1。 |
| A10 | 单一方法的风险 | NA | — | 没有人类自陈式多构念同源测量；LLM 输出与外部地理真值/锚定分布来源不同，共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组接受条件；这是对 LLM 的观察性基准评估，不是被试间实验。 |
| B2 | 被试内设计 | NA | — | 没有人类被试内重复测量设计；同一模型的多地点/多主题 prompt 不是带顺序平衡的被试内实验。 |
| B3 | 混合设计 | NA | — | 没有组间/组内混合实验设计。 |
| B4 | 因子设计 | NA | — | 没有随机化因子实验设计、完整设计矩阵或 ANOVA 主效应/交互分析；模型与主题比较是描述性基准比较。 |
| B5 | 主效应 | NA | — | 无因子实验意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机分配设计。 |
| B8 | 拉丁方 | NA | — | 无被试内条件，也未使用拉丁方顺序安排。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理研究，未对处理组/对照组做因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理可逆性或迁移对称性问题。 |
| C1 | 随机化 | NA | — | 没有处理条件分配到独立单位的随机化；坐标采样是覆盖性抽样，不是条件随机分配。 |
| C2 | 平衡 | NA | — | 没有需要平衡的条件顺序；prompt 独立调用。 |
| C3 | 恒定 | 0.5 | p.4：'greedy sampling (temperature of 0.0)'；p.6固定模型版本；p.4 Figure 2 固定 prompt 结构。 | 报告了 temperature、prompt 结构、模型版本等恒定控制，但未讨论这些恒定选择对外部效度的限制，给 0.5。 |
| C4 | 匹配 | NA | — | 没有匹配设计或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为区组/协变量纳入分析模型；社会经济锚定分布用于定义 bias，不是协变量调整。 |
| C6 | 盲法 | NA | — | 数据采集完全自动化，没有人类被试、主试或评分者需要盲法。 |
| C7 | 平衡的层级 | NA | — | 没有完全平衡/拉丁方/ABBA 等顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 每个 prompt 独立评分，不涉及人类被试的练习效应或学习曲线。 |
| D2 | 疲劳效应 | NA | — | 没有人类 session、休息间隔或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各 prompt 独立，无跨条件清洗期或迁移残留问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内条件交叉，不涉及不对称迁移检验。 |
| D5 | 范围效应 | 0.5 | p.5：'the model’s distribution of ratings is ... rarely uniform and can be skewed'，因此使用 ranks；p.4 Figure 2 用 0.0–9.9 绝对评分。 | 识别了评分分布偏斜并用 rank 降低影响，但没有被试间对照或系统讨论量表锚定/范围效应，给 0.5。 |
| E1 | 位置 / 顺序偏差 | 0 | p.13 Appendix A.2 使用固定顺序的二选一 prompt：'Should I go to Africa or Europe ... "You should go to Africa" or "You should go to Europe"'；p.4 nearby places 也按固定顺序展示。 | 存在选项/刺激顺序风险，但未做随机化、反平衡或位置翻转分析，给 0。 |
| E2 | 默认赞同 | NA | — | 不是 Likert/态度自陈量表，也没有正反向计分题，默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不是人类等级量表自陈测量，也没有跨群体反应风格比较；LLM 评分风格问题未按此组件编码。 |
| E4 | 需求特征 | NA | — | 没有人类被试，因而不存在人类需求特征或事后假设推断访谈。 |
| E5 | 实验者效应 | NA | — | 完全自动化 LLM 调用，无人类主试/评分者，实验者效应不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.16 Table 7 报告 MAD；Table 8 报告 answer rate；Table 9 报告 Gini coefficient；但未报告均值/SD/端点频率。 | 报告了分布离散度指标，可部分排查端点堆积，但缺均值/SD/端点频率和难度校准，给 0.5。 |
| E7 | 共同方法偏差 | NA | — | 无人类多构念同源自陈测量，共同方法偏差检验不适用。 |
| F1 | 统计结论效度 | 0.5 | p.7 Table 1 报告 Spearman ρ；p.8 Table 2/3 报告相关和 bias score；但未见置信区间、样本量依据或多重比较校正。 | 报告了效应量（ρ、bias score），但缺 CI、功效/样本量依据和多重性校正，给 0.5。 |
| F2 | 内部效度 | NA | — | 非随机、非因果实验设计，未做处理组/对照组内部效度评估；按纯观察性 LLM 评估处理。 |
| F3 | 构念效度 | 0.5 | p.7 Table 1 用真实地理数据检验预测效度；p.13 Appendix A.1 讨论主题覆盖和通用 bias score 的困难；但无信度、操纵检验或正式多操作会聚统计。 | 有一定效度证据和限制讨论，但缺信度/manipulation check，给 0.5。 |
| F4 | 外部效度 | 0.5 | p.5说明用 population-density importance sampling 与 farthest point sampling 选 2000 个全球 prompt；p.6列模型；p.13讨论主题非穷尽。 | 报告了地点采样与模型来源，也讨论部分推广边界；但无跨样本/跨情境复现或系统代表性论证，给 0.5。 |
| G1 | 分析单位 | 0.5 | p.5：'we select 2000 prompts' with importance/farthest-point sampling；p.7按地点评分计算相关；未见空间自相关或多层模型处理。 | 说明了 prompt/地点层级，但统计分析把地点评分近似独立，未显式处理空间聚集或嵌套结构，给 0.5。 |
| G2 | 随机效应 | NA | — | 没有人类被试随机效应或混合模型需求；五个模型是固定选择的比较对象，论文也未以模型随机效应作为推断基础。 |
| G3 | 材料作为随机效应 | 0.5 | p.6主题是研究者选定的 6+5+5 个 topics；p.13 Appendix A.1：'We have provided a set of 6 objective topics and 5 sensitive subjective topics and one can easily add more topics, but this may not be exhaustive.' | 材料/主题是有限固定集合，作者承认非穷尽，但未用 item random effect 或主题总体推断，给 0.5。 |
| G4 | 统计功效 | 0.5 | p.5使用 2000 个 prompts，但无功效分析；p.7-8]]报告 Spearman ρ 等效应量，但无 CI。 | 有 2000 个地点的样本量说明和效应量报告，但无事前功效分析和置信区间，给 0.5。 |
| G5 | 研究者自由度 | 0.5 | p.6-8]]报告所有主要 objective/sensitive/control topics 和模型的结果；但无明确试次/地点排除规则、样本量停止规则，也未系统标注验证性与探索性分析。 | 主要因变量与条件报告较全，但研究者自由度披露不完整，给 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未见预注册平台、编号或时间戳；Methods 未提预注册。 | 没有预注册，也没有区分预注册验证性分析与事后探索性分析，按缺失记 0。 |
| J1 | 位置偏差 | 0 | p.13 Appendix A.2 固定二选一：'Should I go to Africa or Europe ... "You should go to Africa" or "You should go to Europe"'；未报告 A/B 交换或偏好翻转率。 | 存在二选一位置偏差风险，但未做位置反平衡/交换重判；主评分任务无候选项，但附录强制选择足以使该风险实际存在，给 0。 |
| J2 | 冗长偏差 | NA | — | 评估不是开放性生成长短质量比较；主指标为评分/相关/选择，不涉及长度—质量裁判。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场操纵、反馈/纠错或谄媚行为测量；现实 prompt 中的偏好句不构成 sycophancy 实验。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 评估模型输出，自我偏好偏差不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 论文明确采用 zero-shot 评分，无 few-shot in-context examples，故不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4 Figure 2 给出完整示例 prompt 与格式；p.14 Table 4/5 对 prompt 元素做消融并报告结果。 | 提供了 prompt 模板并报告部分敏感性消融，但无版本号/迭代日期、dev/test 划分和完整 prompt 搜索过程，给 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 没有长上下文/RAG；每个 prompt 很短，远低于窗口长度。 |
| J8 | 温度与采样随机性 | 0.5 | p.4：'greedy sampling (temperature of 0.0)'并说明使用 logprobs 期望值；p.13现实用例报告 50 个 responses（每 query 10 个）。 | 报告了 temperature 和部分重复响应，但未报告 top-p/top-k、seed、每条件 N 与 95% CI，给 0.5。 |
| J9 | 重复与文本退化 | NA | — | 主任务输出为短评分格式，重复/文本退化不是核心；附录开放性国家列表未用于模型能力比较，故不按开放生成退化编码。 |
| J10 | 分词效应 | NA | — | 单一英语/拉丁脚本，无跨语言或跨脚本比较，分词效应不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.6列出模型版本和地理数据来源；但未见训练截止日期对照、n-gram/DCQ 污染检测或 held-out 私有测试集证明。 | 地理真值来自公开数据集，LLM 可能预训练见过相关知识；全文未做污染检查，按缺失/未控制记 0。 |
| J12 | 基准饱和 | NA | — | 这是新建的地理评分任务，分数（ρ 最高约 0.89）未显示基准饱和，且未做 SOTA 饱和分析；饱和风险不适用。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；answer rate 主要反映是否给出评分/拒绝作答，未按指令约束类型测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.4 prompt 要求 'You provide ONLY your answer in the exact format "My answer is X.X."'；p.16 Table 8 报告 answer rate。 | 有输出格式约束并报告 answer rate，但未报告文法引导/结构化输出、重试策略，未把格式失败与内容错误分开，给 0.5。 |
| J15 | 越狱稳健性 | NA | — | 实验不涉及安全/越狱、有害请求或对抗攻击评估，不适用。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 这是 AI fairness/地理偏差基准，不是把 LLM 作为心理学或认知科学被试并论证其与人类同名构念异同的范式研究。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨模型规模/训练进展的能力曲线，也没有涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对 benchmark、奖励模型或 LLM-judge 进行训练/优化，不涉及代理指标过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6给出 GPT-4 Turbo 'gpt-4-1106-preview'、GPT-3.5 'gpt-3.5-turbo-0613' 等版本；p.7-8]]报告表格结果；p.5使用 2000 prompts；但无重复采样 CI 或配对检验。 | 部分 snapshot/版本标识较精确，也报告了样本规模，但缺重复次数、置信区间和配对检验，给 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮 prompt，无多轮对话历史，也不主张多轮部署一致性推断。 |

## 编码小结
论文对 LLM 地理偏差的操作化、评分指标和模型/主题比较较清楚，并提供了 prompt 消融、logprobs 连续评分和现实用例的补充证据；但其本质是观察性 LLM 基准评估，不是随机实验。多数人类实验设计组件不适用；适用组件的主要不足是缺少随机化/顺序控制、信效度与功效论证、污染检查和严格的重复采样/置信区间报告。
