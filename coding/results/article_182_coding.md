# article_182 | Can Large Language Model Agents Simulate Human Trust Behavior? | 2024

研究类型概述：LLM-as-participant 行为模拟研究。作者让多个 LLM（GPT-4、GPT-3.5 系列、text-davinci-003、Llama2、Vicuna）以 53 个人设分别参与 Trust Game 及其变体，操纵游戏类型、风险概率、受托人性别/种族、受托人是 LLM 还是人类、显式信任指令和 CoT 等提示条件；因变量主要是发送金额、Trust Rate、Lottery Rate、VRR 以及重复博弈轮次轨迹。人类数据来自既有文献，不是本文新收集的人类被试实验。
- **研究构念（Construct）**：人际信任、互惠预期、风险承担以及信任中的人口统计偏差｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：让多个现成LLM在六类信任博弈中作为信任者或受托者作出金额分配和重复互动决策，并与既有人类实验的投入、回报和动态模式比较。（改变信任博弈类型、交互轮次、对手身份、人口统计persona、外部提示和推理策略，并与人类行为基线比较。）｜CA 任务锚定：信任博弈（Trust game (TG), `tsk_uzol7erTzr9Ix`）；爱荷华赌博任务（Iowa Gambling Task, `tsk_4a57abb949ae5`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p3-4: 'We set the temperature as 1...'; p9: 'we added instructions you need to trust... and you must not trust...'; p20: '10 groups of experiments with p from 0.1 to 1.0'. | 明确报告了多个提示操纵及其水平/取值，并给出提示模板，但未报告各条件的分配方式、随机化/平衡方案，也基本没有正式 manipulation check，因此仅部分满足。 |
| A2 | 因变量 | 0.5 | p4: 'trust is widely measured by the initial amount sent'; p4 defines VRR as percentage of personas with amount within $10; p6 defines Trust Rate; p8 reports Repeated Trust Game measures. | 因变量指标与计分方式明确，金额单位为美元、比例为百分比；但未报告信度/效度统计，也未说明连续指标的剔除/预处理和天花板地板控制。 |
| A3 | 控制变量 | 0.5 | p4: 'We set the temperature as 1'; p4: 'we set up our experiments using the CAMEL framework'; p3 lists models and personas generation. | 报告了温度与框架等若干保持恒定的条件，但没有系统列出控制变量清单并逐项说明控制手段。 |
| A4 | 混淆变量 | 0 | p20 Appendix C: 'Trust Games... simplifies real-world scenarios' 仅作为泛化局限；正文未识别并控制如提示模板、人设生成、模型训练数据等潜在混淆，也未报告敏感性分析。 | 属于提示条件比较，存在内部效度意义上的混淆风险；全文未系统识别潜在混淆及其控制/残余威胁。 |
| A5 | 调节变量 | NA | — | 研究没有提出正式调节假设，也没有报告调节变量测量/操纵和交互检验；模型大小与条件差异仅是分组描述。 |
| A6 | 中介变量 | NA | — | 研究不包含中介变量或中介效应分解。 |
| A7 | 操作性定义 | 0.5 | p27-30 给出 Trust Game、Dictator Game、MAP/Risky、Lottery、Repeated 以及 intrinsic-property 操纵的完整提示；p4 与 p6 给出金额和比例指标。 | 关键构念有可执行的操作化描述和提示模板，但未充分说明从自由文本输出中抽取金额、处理无效回答及 BDI 的评分/编码规则。 |
| A8 | 水平数与类型 | 0.5 | p20: '10 groups ... p from 0.1 to 1.0'; p9 报告 gender 和 LLM vs human 条件；p3-4 描述六类游戏。 | 报告了多数条件的水平与标签，但未系统给出每个因素的水平类型、间距/全距及连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 0 | p4: 'trust is widely measured by the initial amount sent'；BDI 仅作少数示例的质性解释，未提供多操作化会聚证据；p20 局限部分未讨论单一金额指标的可推广性限制。 | agent trust 主要依赖单一发送金额指标，未讨论单一操作化对推广边界的限制。 |
| A10 | 单一方法的风险 | NA | — | 研究不是同源自陈式多构念测量；自变量是提示操纵，因变量是 LLM 生成的游戏行为选择，传统共同方法偏差检验不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或 LLM 条件间的被试间随机分配；同一模型/人设被用于多提示条件比较，不构成被试间设计。 |
| B2 | 被试内设计 | 0.5 | p8: 'We conducted 16 groups of the Repeated Trust Game...'; p43: 'dynamics of amounts sent over 7 rounds for 16 randomly sampled persona pairs'; p9: 'compared with their original trust behaviors'. | 存在明确的多轮重复测量和同一人设跨条件比较，但没有报告条件顺序平衡方案，也没有用被试/人设随机效应建模。 |
| B3 | 混合设计 | NA | — | 论文没有正式标注混合设计，也未使用混合模型或分别报告组间/组内误差项；各比较是分开的描述性实验。 |
| B4 | 因子设计 | NA | — | 虽有多个模型、游戏和提示条件，但没有作为一个正式因子设计报告设计矩阵、每格样本量和交互分析；按规则记 NA。 |
| B5 | 主效应 | NA | — | 没有正式因子设计中的主效应检验；仅有分条件均值比较和个别 t 检验，不按因子设计主效应编码。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；研究没有以非随机分组作因果识别。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM 提示条件基本为独立调用；重复博弈的轮次递进是研究对象本身，不是需要论证可逆性的处理条件。 |
| C1 | 随机化 | NA | — | 没有对被试/人设进行条件随机分配；所有模型/人设接受固定提示程序，不涉及分配隐藏。 |
| C2 | 平衡 | NA | — | 各提示条件基本作为独立 API 调用执行，条件顺序的平衡不构成必要设计；重复博弈固定轮次用于研究动态。 |
| C3 | 恒定 | 0.5 | p4: 'We set the temperature as 1'; p3-4 固定 CAMEL 框架、模型列表与提示模板。 | 报告了温度等恒定设置，但未系统列出所有恒定变量及其水平，也未讨论固定设置对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未将已知混淆变量作为区组或协变量纳入模型。 |
| C6 | 盲法 | NA | — | 全自动 LLM 数据采集，无人类被试/主试/评分者盲法安排可编。 |
| C7 | 平衡的层级 | NA | — | 未使用完全平衡、拉丁方或 ABBA 等顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 一次性游戏无练习阶段；重复博弈的轮次变化是行为动态本身，不是需要练习块控制的技能任务。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳效应；任务为短提示调用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同提示条件为独立调用；Repeated Trust Game 的跨轮信息延续是研究设计的一部分，不是处理迁移污染。 |
| D4 | 不对称迁移 | NA | — | 无跨条件残留或迁移对称性问题；重复博弈不涉及处理顺序平衡。 |
| D5 | 范围效应 | NA | — | 因变量为金额和选择比例，不是李克特/绝对量值主观评定量表。 |
| E1 | 位置 / 顺序偏差 | 0 | p27-28 的 MAP/Lottery 提示中呈现固定选项顺序，例如 'Would you choose not to trust or trust the other player?'；全文未报告选项位置随机化或反平衡。 | LLM 二元选择存在选项顺序偏差风险，但未做顺序随机化、交换或报告位置效应。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，不存在正反向计分题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 研究对象为 LLM agents，不是可事后访谈的人类被试；无人类需求特征检查适用。 |
| E5 | 实验者效应 | NA | — | 数据采集全自动，无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5 Figure 2 用圆点大小报告 amount sent 分布和中位数；p6/p8 报告 Trust Rate、Lottery Rate 等。 | 报告了部分分布信息，但没有系统给出偏度、端点频率，也没有预实验难度校准说明。 |
| E7 | 共同方法偏差 | NA | — | 因变量为行为选择而非同源自陈多构念量表；共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p6 和 p21 Table 1 只报告个别 one-tailed t-test p 值；未报告效应量、95%CI、样本量功效依据，也没有多重比较校正。 | 统计结论效度信息严重不足，仅报部分 p 值。 |
| F2 | 内部效度 | 0 | p9: 'we added instructions... and explored their impact'，但没有随机分配、分配隐藏、基线等价性、被试流向或损耗处理；p4 的 VRR 只是有效回答率。 | 存在条件比较和影响推断，但内部效度控制未报告。 |
| F3 | 构念效度 | 0.5 | p4 引用既有文献说明 Trust Game 中 amount sent 是信任的常用测量；BDI 示例用于质性解释。未报告内部一致性/重测信度或正式 manipulation check。 | 有基于既有范式的构念效度支持，但缺少自身测量的信度和正式效度/操纵检验。 |
| F4 | 外部效度 | 0.5 | p3-4 列出多种闭源/开源 LLM，p4 说明用 GPT-4 生成 53 类 personas；p20 承认 Trust Games 简化现实情境。 | 报告了模型和人设来源，并部分讨论推广边界，但没有人类样本代表性或跨情境复现结果。 |
| G1 | 分析单位 | 0 | p4: '53 types of personas'; p8: '16 groups of the Repeated Trust Game'; 分析多按模型/条件均值或比例汇总，未说明观测嵌套于 persona/model 的分析单位。 | 未清晰说明处理分配层级与统计分析层级，也未处理 persona/trial 的嵌套结构。 |
| G2 | 随机效应 | 0 | p4 报告 53 personas，p8 报告 16 groups，但全文未使用混合模型，也未说明 persona 或 group 为随机效应。 | persona 是从生成集合中抽出的分析单位，若要对 persona 总体推广应建模随机效应；本文未做。 |
| G3 | 材料作为随机效应 | NA | — | 研究不使用词项/语言材料作为需推广到材料总体的随机项目；游戏场景是固定实验范式。 |
| G4 | 统计功效 | 0 | p4/p8 仅说明 53 personas、16 groups；无事前功效分析，结果也基本不报告效应量和 CI。 | 缺少设计阶段功效分析和效应量/CI 报告。 |
| G5 | 研究者自由度 | 0.5 | p4 报告 personas 数量和模型列表；p5 定义 VRR；p8 报告 16 groups 和 7 rounds；但未说明无效回答的剔除/处理规则、样本量决定方式，也未区分验证性与探索性分析。 | 报告了较多条件和因变量，但研究者自由度信息不完整。 |
| G6 | 预先设定 / 预注册 | 0 | 全文无预注册平台、注册编号或分析计划；p51-56 的 NeurIPS checklist 也不构成预注册。 | 没有时间戳早于数据收集的预注册。 |
| J1 | 位置偏差 | 0 | p27-28 的 MAP/Lottery 提示使用固定表述顺序（如 'not to trust or trust'），未报告 A/B 交换、位置随机化或位置 × 选择曲线。 | LLM 二元选择存在位置偏差风险，但完全未提及或控制。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 或开放性生成长度评分；因变量是金额/比例。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场/反馈式对话；'you need to trust' 是实验操纵而非谄媚测量。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 裁判或成对比较评分。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，没有 few-shot in-context examples。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p27-30 给出完整提示模板；p4 报告 temperature=1。未报告 prompt 版本号、迭代日期、语义等价措辞敏感性消融或 dev/test 划分。 | 提示可复现到模板层面，但缺少版本化与敏感性分析。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短，无长文档/RAG 或长上下文位置效应实验。 |
| J8 | 温度与采样随机性 | 0.5 | p4: 'We set the temperature as 1'；未报告 top-p/top-k、随机种子、每条件重复采样次数或 bootstrap CI。 | 报告了主要采样参数之一，但随机性控制与重复运行信息不完整。 |
| J9 | 重复与文本退化 | NA | — | 主要输出是短金额/二元选择；BDI 示例仅作质性展示，未作为开放式生成质量指标。 |
| J10 | 分词效应 | NA | — | 单语言英文提示，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 不是公开基准评测，无固定测试集版本与训练截止日期对照；Trust Game 范式可能见于训练语料，但本文未按基准污染框架评估。 |
| J12 | 基准饱和 | NA | — | 不涉及基准饱和问题；不是标准 benchmark 分数比较。 |
| J13 | 指令遵循 | NA | — | 显式信任指令是操纵变量，不是以机器可判定约束测量指令遵循能力。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求 JSON/结构化输出，也不报告格式合法率。 |
| J15 | 越狱稳健性 | NA | — | 不涉及越狱或安全对齐评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1-2: 论文明确以 'agent trust' 对应 'human trust'，并提出 'behavioral alignment' 与 BDI 解释；p4 列出模型名称但 GPT-4 无精确 checkpoint，人类数据来自既有研究而非同批人类实验。 | 对 LLM 构念与人类同名构念有理论讨论和既有人类范式比较，但缺少精确权重 snapshot 与直接人类对照实验，仍有外推风险。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有报告跨规模能力曲线，也没有宣称 '涌现/突变'。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标进行训练/RL/best-of-N 优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p3-4 列出部分模型版本（如 GPT-3.5-turbo-0613）并报告 53 personas/16 groups；但未报告每条件重复运行次数、95%CI、配对检验或精确 API 日期，GPT-4 仅有 'GPT-4'。 | 具备部分可复现信息，但缺少 CI、重复运行与精确 snapshot。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p8: Repeated Trust Game 7 rounds；p43: 'dynamics of amounts sent over 7 rounds for 16 randomly sampled persona pairs'；附录 G.2/G.3 给出逐轮图。 | 确实做了多轮评估并报告逐轮轨迹，但未系统比较单轮与多轮成绩、未说明上下文截断控制，也未报告 seed/CI。 |

## 编码小结
该文是描述性/探索性的 LLM 行为模拟研究，核心贡献在于提出 agent trust 与 behavioral alignment 的比较框架，并系统比较多模型与多提示条件。优点是人设、游戏提示和 BDI 样例报告较充分；主要不足是缺少正式实验设计标注、条件顺序/位置平衡、随机化、操纵检验、信效度统计、效应量与置信区间、采样种子与重复运行、精确模型 snapshot 及预注册。很多组件对纯 LLM 行为模拟不适用，因此按实际分析单位作 NA；存在但未报告的结构按 0 或 0.5 编码。
