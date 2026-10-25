# article_143 | How do Language Models Bind Entities in Context? | 2024

研究类型概述：这是一项 LLM 机制可解释性研究，用因果中介/激活替换干预分析 LLaMA 与 Pythia 家族模型在上下文实体—属性绑定任务中的内部表征。分析单位为模型、任务、上下文实例与查询，核心操纵包括实体/属性激活替换、位置干预、均值干预、跨任务向量迁移与不同模型规模/任务比较。
- **研究构念（Construct）**：工作语境中实体与属性的临时绑定及其可迁移表征｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；问题解决（problem solving, `trm_4a3fd79d0adb7`）
- **实验任务与范式（Task / Paradigm）**：构造CAPITALS、SHAPES、FRUITS等多实体文本语境，查询指定实体的属性，测量正确token概率；随后交换、抹除或跨任务迁移实体和属性位置的绑定向量。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: 'we fix k in {0,1} and intervene on either just the entity, just the attribute, neither, or both'; p.5: 'We use LLaMA 30-b here'; p.7: 'we fix n = 2 and use 500 samples to estimate'. | 实体/属性替换、control/attribute/entity/both 等条件水平明确，程序详尽；但主要是同一批上下文上的干预比较，无正式单位随机分配或独立操纵检验，按完整性记 0.5。 |
| A2 | 因变量 | 0.5 | p.2: 'The mean log prob metric... Top-1 accuracy... median-calibrated accuracy'; p.12 App A 给出三种指标的公式与 N=100 上下文。 | 因变量指标与计分方式明确，且说明了校准；但未报告测量信度/效度证据，连续指标的抽样不确定性也未系统处理，记 0.5。 |
| A3 | 控制变量 | 0.5 | p.5: 'We use LLaMA 30-b here and elsewhere unless otherwise stated'; p.4: n=2 CAPITALS；p.7: random vectors 作为对照；p.2: N=100 contexts。 | 报告了固定模型、固定任务模板、样本量与随机向量对照等部分控制手段，但没有系统列出所有额外变量及逐项控制方式，记 0.5。 |
| A4 | 混淆变量 | 0.5 | p.6: 'We interpret this gradual trend as an artifact of position-dependent bias'; p.14: PARALLEL 'breaks the confounder... entity always appear in the same sentence as attributes'；p.15: 讨论 direct binding 替代机制。 | 识别并讨论了位置依赖偏差、CAPITALS 句式混淆及替代机制等内部效度威胁，并给出部分控制/校准；但未系统量化残余混淆或敏感性分析，记 0.5。 |
| A5 | 调节变量 | NA | — | 论文没有以调节变量为设计核心的正式调节假设与交互分析；模型规模效应仅作为泛化性描述，不作为调节模型编码。 |
| A6 | 中介变量 | 0 | p.3: 'causal mediation analysis... intervening on the value of the node and measuring the model output'；p.4: 以 Z_entity/Z_attribute 替换检验因子性。 | 论文使用因果干预分析中间激活，但没有按经典中介分析报告直接/间接效应大小、a/b 路径、bootstrap CI 或效应分解；若将中间激活视为中介变量，核心报告要求未达成，记 0。 |
| A7 | 操作性定义 | 1 | p.3-4 给出 Z_context、激活替换与因果中介步骤；p.14-16 Appendix D 给出 CAPITALS/PARALLEL/FRUITS/SHAPES/BIOS 的完整 prompt 模板与计分任务。 | 关键操纵与测量均有可复现的操作化说明，包括激活替换、位置干预、prompt 与指标公式。 |
| A8 | 水平数与类型 | 0.5 | p.4: n=2 与 k in {0,1}；p.7: n=2/3、500 samples；p.8 Fig.6 列出 Pythia/LLaMA 规模及多任务；p.8 Table2 列出任务名。 | 报告了主要条件水平、任务与模型族，但未集中给出所有自变量的水平类型、间距/全距及连续变量处理，记 0.5。 |
| A9 | 单一操作化的风险 | 1 | p.4-7 同时用 factorizability、position independence、mean interventions；p.8 跨 CAPITALS/PARALLEL/SHAPES/FRUITS/BIOS 与跨模型检验；p.15 讨论 direct binding 的边界。 | 关键构念 binding ID 采用多种任务、多种干预与跨任务迁移的会聚证据，并讨论了非普适边界，符合多操作化要求。 |
| A10 | 单一方法的风险 | NA | — | 本研究不是问卷/自陈式同源测量，而是对内部激活做因果干预并读取模型 logits；共同方法偏差的程序/统计检验不适用于该机制分析。 |
| B1 | 被试间设计 | NA | — | 无人类或独立被试组分配；所有条件在同一模型/上下文上通过独立前向干预计算，不构成被试间设计。 |
| B2 | 被试内设计 | NA | — | 条件并非作为有顺序的重复处理施加给同一被试；激活替换为独立前向计算，无学习/顺序效应，故不按人类被试内设计编码。 |
| B3 | 混合设计 | NA | — | 不存在人类组间/组内因素混合设计。 |
| B4 | 因子设计 | NA | — | 论文虽比较 control/entity/attribute/both 等条件，但没有正式因子设计、设计矩阵与主效应/交互 ANOVA 分析，按规则不编码为因子设计。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 没有正式交互项统计检验；both 条件仅作为机制一致性描述。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计；研究为模型内部激活的受控干预分析。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理顺序与迁移/可逆性设计；激活替换不涉及被试学习或处理后效。 |
| C1 | 随机化 | NA | — | 没有把互斥实验条件随机分配给独立实验单位；上下文采样与干预计算不构成随机化分配。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序平衡问题；各干预为独立前向计算。 |
| C3 | 恒定 | 0.5 | p.5: 'We use LLaMA 30-b here and elsewhere unless otherwise stated'；p.2: N=100 contexts；p.7: 500 samples；p.8: 固定任务集合与模型集合。 | 报告了部分恒定变量（模型、模板、样本量）与范围；但没有系统列出所有环境/实现常量，也未专门讨论这些恒定设置对外部效度的限制，记 0.5。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有把混淆变量作为协变量/区组纳入统计模型的分析。 |
| C6 | 盲法 | NA | — | 无人类被试或人类评分者，无法施盲；数据采集为自动化模型评估。 |
| C7 | 平衡的层级 | NA | — | 无条件顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | LLM 条件为独立前向计算，无上下文内练习/学习效应。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长或疲劳效应。 |
| D3 | 延滞 / 迁移效应 | NA | — | 跨任务向量迁移是有意操纵的分析，不是同一单位先后接受处理导致的残留/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件顺序残留与不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 因变量为 log prob/准确率，不是需要量表锚定的绝对判断或李克特评分。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.6: 对实体/属性位置做 {X_E0 -> x, X_E1 -> X_E1-(x-X_E0)} 干预并考查 swapped condition；p.13: 用 median-calibrated accuracy 控制 position-dependent bias。 | 论文识别并系统干预了位置效应，且用校准减轻位置偏差；但没有对采样上下文中的实体/属性呈现顺序做随机化/反平衡报告，故记 0.5。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征与事后访谈问题。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Table1 报告 control 条件准确率 0.99/1.00、干预条件 0.00/0.03；p.8 Table2 报告 mean accuracy 与 chance=0.33；但未报告偏度/端点频率或 pilot 难度校准。 | 报告了条件均值和 chance baseline，可见接近天花板/地板的现象；但缺少完整分布、端点频率与预实验难度校准说明，记 0.5。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念量表，共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.2: N=100 contexts；p.7: 500 samples；p.7 Table1 与 p.8 Table2 报告均值/准确率，但无 CI、功效分析或多重比较校正。 | 报告了样本量与描述性效应量，但未报告置信区间、样本量确定依据或多重性校正，记 0.5。 |
| F2 | 内部效度 | 0.5 | p.4-6 使用源/目标上下文的激活替换与位置干预；p.6 讨论 position-dependent bias；p.15 报告 direct binding 替代机制；但无随机分配/基线等价检验。 | 对内部效度威胁有较好评估并设 control 条件；但无分配隐藏、基线等价性检验或被试流向类报告，记 0.5。 |
| F3 | 构念效度 | 0.5 | p.4-7 通过 factorizability、position independence、mean interventions 验证构念；p.8 多任务与跨任务迁移；p.15 讨论 direct binding 边界；但无形式化信度/效度统计。 | binding ID 构念有多操作化与干预会聚证据，也讨论非普适机制；但未报告传统信度/效度指标与正式操纵检验统计，记 0.5。 |
| F4 | 外部效度 | 0.5 | p.8 Fig.6 比较 Pythia 与 LLaMA 规模；p.8 Table2 跨 CAPITALS/PARALLEL/SHAPES/FRUITS/BIOS；p.1 声明代码与数据公开；p.9 讨论向其他模型的泛化猜想。 | 报告了模型族、规模与任务来源，并讨论一定推广边界（direct binding 例外）；但没有精确 checkpoint/训练语料代表性或跨样本复现细节，记 0.5。 |
| G1 | 分析单位 | 0.5 | p.2: 'we sample N=100 contexts. For each context c, we query the LM with every entity'；p.12 App A: 对 N 个上下文与查询实体计算并平均。 | 说明了分析在上下文/查询层面并进行平均，但未说明分配层级与统计模型匹配，也未对 context/query 嵌套结构建模，记 0.5。 |
| G2 | 随机效应 | 0 | p.12 App A 仅对 N 个上下文按查询取平均；全文无混合模型或随机效应结构报告。 | 上下文是从任务分布中采样的分析单位，但分析未将上下文等作为随机效应，也未说明随机截距/斜率；对于向上下文总体推广的推断不足。 |
| G3 | 材料作为随机效应 | 0 | p.8 Table2 使用多个 source task 的差向量；p.16 App F 用 500 samples 估 Δ，但未报告 item/material random effects。 | 研究使用有限的实体/属性材料与任务，但未把材料/项目作为随机因子纳入分析，也未使用准 F 或混合模型来推广到材料总体。 |
| G4 | 统计功效 | 0 | p.2 仅报告 N=100 contexts；p.7 使用 500 samples；全文无功效分析、预期效应量来源或 CI。 | 没有事前功效分析或样本量论证，结果以描述性均值为主且无置信区间，记 0。 |
| G5 | 研究者自由度 | 0.5 | p.4: 明确 control/attribute/entity/both 条件；p.2: N=100；p.7: 500 samples；p.8: 多个任务与模型；但无试次剔除规则、停止规则与验证性/探索性区分。 | 条件与主要因变量报告较完整，也没有明显隐藏条件；但缺失数据排除规则、样本量决定方式和探索性与验证性分析标注，记 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.2 提供代码与数据链接，但全文无预注册平台、注册编号、预注册分析计划或偏离说明。 | 没有公开预注册，故记 0。 |
| J1 | 位置偏差 | NA | — | 研究不涉及 LLM-as-judge 或多项候选项排序；虽有位置偏差分析，但不是选择/排序裁判中的 A/B 位置反平衡设计。 |
| J2 | 冗长偏差 | NA | — | 不涉及 LLM 对开放式生成质量的长短比较。 |
| J3 | 谄媚 | NA | — | 无用户立场、反馈或对话式纠错输入，不涉及谄媚偏差。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 评估模型输出。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 主任务为零样本上下文/指令提示，不使用 few-shot in-context examples 作为操纵。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.14-16 Appendix D 给出完整 prompt 模板；但全文未做语义等价 prompt 敏感性消融，也未说明 dev/test prompt 调参与版本化。 | 完整模板可复现，但缺提示版本、敏感性消融和 dev/test 划分，记 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文很短（少量实体/属性句），不涉及长上下文/RAG 的中间迷失问题。 |
| J8 | 温度与采样随机性 | NA | — | 研究直接评估模型对候选 token 的 log probability/校准准确率，不依赖采样生成文本；未涉及采样温度与随机种子作为主要实验随机源。 |
| J9 | 重复与文本退化 | NA | — | 任务为短属性 token 的 log-prob 评估，不涉及开放生成重复/退化。 |
| J10 | 分词效应 | NA | — | 单语言、单脚本实验，无跨语言/跨格式分词长度比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 主要实验为自建合成上下文并分析内部机制，不是以公开 benchmark 分数宣称泛化能力；虽然附录使用 BIOS/SST-2，但不构成本文主要能力结论。 |
| J12 | 基准饱和 | NA | — | 不是基准饱和评估；任务准确率虽接近上限，但研究目的为机制干预而非排行榜提升。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，无约束型指令准确率评估。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化/文法约束输出。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1: 'How humans solve binding... is a fundamental problem in psychology. Here, we study binding in LMs'；p.3 footnote: 'We do not claim or assume that LMs actually have beliefs in the sense that humans do.' | 论文把 binding 作为认知/计算构念并明确不直接假定类人信念，但未系统比较 LLM 与人类同名构念或做人类对照实验，记 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | p.8 Fig.6 展示 Pythia/LLaMA 规模—准确率曲线，并称 'their effectiveness increases with model scale'；p.9 称 'only the larger models exhibited binding IDs'。 | 报告了规模曲线并作规模相关宣称，但主要使用校准准确率离散曲线，未报告多 seed、置信区间或连续指标曲线来排除指标诱导假象，记 0.5。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不涉及对代理指标进行训练/优化或奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.2: N=100 contexts 与公开代码链接；p.7: 500 samples 估计 Δ；p.5/p.8 仅给出 LLaMA-30b、Pythia/LLaMA 家族与规模；无精确 checkpoint、CI 或配对检验。 | 报告了样本重复数与模型族/规模，并公开代码，但缺精确 snapshot、置信区间与配对比较，记 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮上下文问答/激活干预，不涉及多轮对话一致性衰减。 |

## 编码小结
论文提出了 binding ID 机制，并通过多种激活干预与跨任务迁移给出较强的机制证据；但研究不是人类被试实验，许多人类实验设计/质控组件不适用。统计报告以均值/校准准确率为主，缺少置信区间、随机效应模型、精确 snapshot 与预注册等信息。
