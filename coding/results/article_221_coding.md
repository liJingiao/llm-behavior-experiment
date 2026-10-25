# article_221 | Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation | 2024

研究类型概述：LLM 多智能体谈判基准与模拟实验；分析单位为多轮谈判会话、其中各 agent/deal 的得分与成功率，并以多次随机 agent 顺序运行进行平均；无人类被试。
- **研究构念（Construct）**：多方谈判中的合作、竞争、恶意、联盟与策略适应｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：让现成LLM扮演多方利益相关者，在多议题谈判游戏中轮流提案、接受或拒绝，并比较合作、竞争、贪婪和恶意角色。（操纵玩家目标、阈值、角色类型、模型组合、玩家/议题数量、规划提示和博弈难度。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.6 Table 1 报告 'Prompt structure ablation study'，列出 prev. deals/others’ prefer./candidates/selection/planning 的有无；p.4 §3.2 报告 compromising/greedy/adversarial 激励；p.5 §4.1 报告 20 次运行。 | 自变量被明确命名并给出多个水平及提示操纵程序，但未报告操纵检验，分配方式也仅部分说明，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.5–6 定义 final success、any success、own score、collective score、wrong deals、score leakage ratio，并给出 S_pi 与成功判定公式。 | 因变量指标与计分方式清楚，但未系统报告信度、效度、连续指标预处理或天花板/地板说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.5 §4.1：24/28 rounds、history window 6/7、temperature 0、每次 20 runs with random order；p.8 调难度时 'keeping everything else fixed'。 | 报告了多个人为保持恒定的设置，但未形成系统控制变量清单并逐一说明外部效度限制，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.5–8 通过 temperature、rounds、history window 与 prompt ablation 控制部分因素；p.10 Limitations 主要讨论 scaling 与 threshold，而非残余混淆。 | 识别并控制了部分潜在混淆，但未充分讨论残余混淆或敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 理论模型未提出调节假设，未做正式调节/交互检验；混合种群比较只是分组描述，不是调节模型。 |
| A6 | 中介变量 | NA | — | 理论模型未包含中介变量，未做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p.2–4 描述 parties/issues/scoring/thresholds；p.4 §3.2 给出 compromising/greedy/adversarial 操作；p.5–6 给出 metrics；Appendix K/L 与 p.18 Algorithm 1 给出完整 prompt 与流程。 | 关键游戏、激励变体与因变量均有可重复的操作化程序，达到 1。 |
| A8 | 水平数与类型 | 0.5 | p.6 Table 1 给出五个 CoT 阶段的 presence/absence；p.9 Table 6 给出 variants；p.8 Table 4 给出 difficulty 的可行解数；p.5 给出模型列表。 | 报告了多组水平与取值，但未统一说明各水平类型、间距/全距或完整设计矩阵，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.8–9 使用 base/rewrite/new games、compromising/greedy/adversarial variants 与多个 metrics；p.10 Limitations 未讨论单一操作化局限。 | 关键构念有多个游戏/变体/指标上的操作化，但未正式报告会聚证据，也未讨论单一操作化推广限制，故为 0.5。 |
| A10 | 单一方法的风险 | NA | — | 因变量由游戏规则自动计分，不是自陈式同源测量；共同方法偏差框架不适用于该基准设计。 |
| B1 | 被试间设计 | 0.5 | p.5 §4.1：each experiment run 20 times with random order of agents；各条件在独立模拟会话中执行。 | 条件由独立会话承担，具有被试间/会话间逻辑，但未明确说明被试间分配程序与每格样本量，故为 0.5。 |
| B2 | 被试内设计 | NA | — | 不存在同一分析单位接受所有实验条件的人类被试内设计；多轮是同一次谈判过程，不是重复条件分配。 |
| B3 | 混合设计 | NA | — | 未使用正式混合设计 ANOVA 或混合模型，也未逐因素标注组间/组内并分别报告误差项。 |
| B4 | 因子设计 | NA | — | 提示结构消融不是完整因子设计；未报告完整设计矩阵、每格样本量与交互项统计，故按无正式因子设计记为 NA。 |
| B5 | 主效应 | NA | — | 无正式因子设计主效应统计检验；Table 1 为描述性消融比较。 |
| B6 | 交互作用 | NA | — | 无因子交互项统计检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；条件由模拟配置分配，而非自然分组。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内条件设计，故不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | 0.5 | p.18 Algorithm 1：order ← [shuffle(P), ..., shuffle(P)]；p.5 §4.1 报告 4 consecutive random ordering 与 20 runs。 | 报告了 agent 发言顺序的随机化，但未报告随机数工具、种子、分配隐藏或基线均衡性检验，故为 0.5。 |
| C2 | 平衡 | 0.5 | p.5 报告 random ordering of agents；p.18 Algorithm 1 每轮 shuffle(P)。 | 有随机顺序安排，但未报告平衡层级、每种顺序计数或迁移对称性前提，故为 0.5。 |
| C3 | 恒定 | 0.5 | p.5：temperature 0、24/28 rounds、history window 6/7；p.8 调难度时 keeping everything else fixed。 | 列出了若干恒定设置，但未系统列出全部恒定变量及其外部效度限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对分配。 |
| C5 | 纳入为变量 | NA | — | 未将已知混淆变量作为协变量/区组纳入 ANCOVA 或类似模型；模型与难度被作为操纵/分层因素处理。 |
| C6 | 盲法 | NA | — | 自动化 LLM 模拟，无人类被试/主试盲法；LLM judge 的偏差另在 J4 讨论。 |
| C7 | 平衡的层级 | 0 | p.5 报告 random ordering of agents；p.18 Algorithm 1 每轮 shuffle(P)。 | 研究存在被试内/序列顺序平衡需求（同 C2），但未明确选用完全平衡、拉丁方或 ABBA 层级，亦未报告构造方法与顺序效应形状假设，记 0。 |
| D1 | 练习效应 | NA | — | 多轮谈判中的适应不是跨条件练习块；各条件会话独立重置，无人类练习效应控制需求。 |
| D2 | 疲劳效应 | NA | — | LLM 模拟不存在人类疲劳效应，且单次会话并非需要休息安排的人类长时实验。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件使用独立会话/上下文，未跨条件共享历史，故无清洗期/迁移污染问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移，故不涉及不对称迁移检验。 |
| D5 | 范围效应 | NA | — | 不使用主观量表或绝对量值估计，因变量为规则计算的得分与成功率。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.5 §4.1 报告 random ordering of the 6/7 agents；p.18 Algorithm 1 使用 shuffle(P) 安排每轮 agent 顺序。 | 对多 agent 发言顺序做了随机化，但未报告位置出现次数或平衡方案细节，故为 0.5。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，且无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，故不存在人类需求特征或事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 无人类主试/评分者实验者效应；自动化数据采集与规则计分。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7–8 Table 3/4 报告 any success 可接近 100、wrong deals 可接近 0；p.8 通过难度变化避免饱和；p.6 Fig. 3 报告轮次曲线。 | 报告了接近端点的比例并调节难度，但未系统报告偏度/端点频率与 pilot 校准过程，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念测量；因变量为客观规则计分，无共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | p.14 Checklist 称 'All graphs are reported with confidence intervals'；p.5 每次 20 runs；p.6–9 表格主要报告均值/百分比，未报功效分析或统一效应量。 | 部分图有置信区间且重复运行，但缺事前功效、系统效应量与多重性校正，故为 0.5。 |
| F2 | 内部效度 | 0.5 | p.5 使用 20 次随机 agent 顺序运行；p.18 Algorithm 1 随机打乱顺序；但未报告基线等价、分配隐藏、被试流向或 API 失败/损耗。 | 报告了部分分配随机化与内部效度控制，但缺基线等价和损耗处理，故为 0.5。 |
| F3 | 构念效度 | 0.5 | p.6–7 报告 ToM 偏好推断准确率 61% vs 42%，p.9 Fig. 5 检查激励一致性；但未系统报告指标信度/效度。 | 有一些构念相关检查与多指标证据，但缺正式信效度和操纵检验，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.5 列出模型；p.8 Table 4 使用 rewritten/new games 与不同难度；p.10 Limitations 讨论 scaling/threshold。 | 报告了模型与游戏边界并做多种游戏比较，但未系统说明模型/游戏抽样代表性及跨情境复现，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p.5–6 metrics 在 session/agent/deal 层计算；p.5 每次实验 20 runs 后平均；p.6 Table 1 按配置汇总，但未用多层模型处理轮次嵌套于会话。 | 说明了分析层级并多次运行，但未显式处理会话内轮次/agent 的嵌套结构，故为 0.5。 |
| G2 | 随机效应 | 0.5 | p.5 报告每个实验 20 次 random order 运行；p.18 随机打乱 agent order；全文未报告混合模型随机效应结构。 | 通过随机顺序与重复运行处理方差，但未报告随机/固定效应结构，故为 0.5。 |
| G3 | 材料作为随机效应 | 0.5 | p.8 使用 base、rewritten、new games 与 extended game；p.8–9 比较多个游戏，但未将 game/item 作为随机效应建模。 | 使用了多个游戏实例以检验稳健性，但分析中未把游戏材料作为随机抽样因子，故为 0.5。 |
| G4 | 统计功效 | 0 | p.14 Checklist 未报告事前功效分析；p.6–9 主要报告百分比结果，未报告系统效应量与置信区间。 | 缺少设计阶段功效分析或样本量论证，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p.7 报告排除 Mistral 7b/Llama-2 7b（未遵循格式）；p.5 报告 20 runs；p.8 extended game 80 runs；所有主要 metrics 均报告，但未区分验证/探索分析。 | 报告了排除规则、主要指标和部分运行次数，但未完整说明停止规则及验证/探索区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.14 Checklist 与全文未见预注册平台/编号；仅提供代码与提示词。 | 无公开预注册，故为 0。 |
| J1 | 位置偏差 | NA | — | 研究不是 LLM-as-judge 的候选位置/成对排序实验；deal 选项为固定语义标签，未做候选位置操纵。 |
| J2 | 冗长偏差 | NA | — | GPT-4 裁判用于检测分数泄漏，不是评价开放式生成质量或长度偏好。 |
| J3 | 谄媚 | NA | — | 无用户先验立场/反馈/纠错式对话，故不涉及谄媚操纵。 |
| J4 | 自我偏好 | 0 | p.6：'We use GPT-4 as a judge to verify whether public answers contain any mention or values of scores or thresholds'；p.5 同时评估 GPT-4 agents。 | 使用被评模型家族 GPT-4 作裁判，未识别或控制自我偏好/同源偏差，故为 0。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，不是 few-shot in-context learning；未使用示例集选择/排列。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | Appendix K/L 给出完整 prompt 模板；p.6 Table 1 做 prompt 结构消融；但未报告 prompt 版本日期、语义等价敏感性消融或 dev/test 分离。 | 模板公开且有结构性消融，但缺完整敏感性/版本控制，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文仅为最近 6/7 条交互，不是长文档/RAG 长上下文实验。 |
| J8 | 温度与采样随机性 | 0.5 | p.5 报告 sampling temperature 0 并每次实验 20 runs；Appendix B 报告 temp 1；未报告 top-p/top-k/seed/API snapshot 日期。 | 报告了温度与重复次数，但采样细节与随机种子不完整，故为 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.5 报告 temperature 0；p.6–7 与 Fig. 3 讨论重复/饱和 deals；未报告 repetition penalty、n-gram 重复率或截断比例。 | 有基本解码设置并讨论重复现象，但缺系统重复/退化 QC，故为 0.5。 |
| J10 | 分词效应 | NA | — | 单语言英文、单脚本实验，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.8 仅提及 training data contamination 与 older benchmarks 饱和，但未报告测试集版本/训练截止日期对照或污染检测；base game 又改编自公开谈判练习。 | 基准评测存在污染风险但未做污染检查或报告污染率，故为 0。 |
| J12 | 基准饱和 | 0.5 | p.8 明确讨论 older benchmarks saturation 并通过 new games 与 Table 4 难度变化避免饱和；未报告饱和分析的 CI/连续指标。 | 识别了饱和问题并增加难度/新游戏，但缺连续指标或正式 CI 比较，故为 0.5。 |
| J13 | 指令遵循 | 0 | p.6 以 GPT-4 judge 检测是否泄漏 scores/thresholds；p.8 报告 leaked scores ratio，但无机器可判定的正则/函数标准。 | 指令遵循（不泄漏分数）仅用 LLM 裁判测量，未按约束类型机器判定，故为 0。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.5 要求用 tags 标记 deals/scratchpads/answers/plans 以自动解析；p.7 排除未遵循基本格式的模型；但未报告格式合法率/重试策略。 | 报告了结构化输出设置，但缺格式合法率与格式失败独立指标，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及越狱/有害请求安全评估；adversarial variant 是游戏内破坏谈判角色，不是 jailbreak。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.29 Appendix J：'do not make claims about whether these properties are truly satisfied in agents, and we do not intend to anthropomorphize LLMs'；p.7 报告 ToM 偏好推断 61% vs 42%。 | 对 LLM 构念解释有警示且做 ToM 检查，但未系统与人类同名构念对照，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告随模型规模/训练进展的涌现能力曲线，也未宣称突变式涌现。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对基准/奖励模型/LLM-judge 的优化训练或 best-of-N 代理优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 报告每次实验 20 runs；p.14 提供代码/prompt 链接且称图有 CI；但模型仅给名称，无精确 snapshot/API 日期，表内无配对检验。 | 有重复次数与可复现材料，但 snapshot 和配对统计不完整，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.3–5 报告 24/28 rounds、history window 6/7；p.6 Fig. 3 给出 p1 各轮 deal 进展；p.9–10 讨论动态 coalition/echo；未系统报告每轮独立/累积评分。 | 确做多轮评估并报告部分逐轮轨迹，但未完整按轮次拆分一致性/衰减分析，故为 0.5。 |

## 编码小结
该文提出并用 LLM 多智能体模拟评估多方谈判基准，主要操纵提示结构、游戏变体/激励、模型与难度等，因变量为规则可计算的谈判成功与得分指标。整体方法透明、提示与算法公开较充分，但在操纵检验、信效度、随机化/种子细节、预注册、LLM 裁判偏差与统计不确定性报告方面有限。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 C7（NA→0）。
