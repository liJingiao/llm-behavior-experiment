# article_203 | Position: Theory of Mind Benchmarks are Broken for Large Language Models | 2025

研究类型概述：这是一篇 ICML 2025 position paper，核心是理论批判与指标提出：区分 literal theory of mind 与 functional theory of mind，并以多个开源 LLM 在 RPS、IBS、IPD 重复矩阵游戏中与固定/ tit-for-tat 伙伴交互作为案例实验。分析单位为模型 × prompting 策略 × 游戏 × 伙伴策略 × episode/step；无人类被试，属于 LLM 行为评测与多智能体模拟研究。
- **研究构念（Construct）**：字面心智理论与功能性心智理论、伙伴适应和行动一致性｜CA 构念锚定：心理理论（theory of mind, `trm_4a3fd79d0b392`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：让多个现成开放模型在文本化重复博弈中预测简单伙伴策略，并据此与伙伴互动，分别测量伙伴预测和自身行动的理性适应。（改变伙伴策略、博弈类型、互动长度、模型及提示方法，并与表格型理性基线比较。）｜CA 任务锚定：心理理论任务（theory of mind task, `trm_4c8a8467304e2`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4: 'Our prompting strategy for the LLM policy pi_i follows what was established ... by Akata et al. (2023)'; p6: 'We consider three high-level classes of prompting strategies'; p7 Table 2; p19–24 Figures 1–18. | 明确命名并比较了多种 prompting 策略、游戏与伙伴策略，且给出 prompt 模板；但没有传统操纵检验，也没有说明条件分配的随机化/平衡方式，故为 0.5。 |
| A2 | 因变量 | 0.5 | p4: 'We report the accuracy ... as ToM %'; 'regret per step ... ΔFunctional/T'; p5 Table 1; p17: 'confidence intervals are based on the actual sample size'. | 因变量指标与计分方式明确（ToM% 与 regret per step），并报告置信区间；但没有信度/效度证据，也未说明连续指标的预处理或天花板/地板控制，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p17: 'playing a sequence of 100 step episodes ... over 24 hours or a maximum of 100 episodes. Every model was evaluated for at least 30 episodes'; p18: LLAMA-2 70B Chat quantized. | 报告了 API、episode 长度、运行时长/上限、最少 episode 数、模型量化等部分恒定条件，但没有系统列出控制变量清单及逐一控制手段，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p28: 'action representation is great way for us to control the extent that this knowledge is evoked'; p7: long-context ablation; p28: 'inductive bias can be helpful ... while also hurting convergence'. | 识别并部分操纵了动作表示先验知识、长上下文推理等潜在混淆，也讨论了残余影响；但未系统报告所有残余混淆及敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 论文没有明确的调节变量理论假设，也没有报告乘积项交互检验或简单斜率分析，因此该组件不适用。 |
| A6 | 中介变量 | NA | — | 论文没有中介变量或直接/间接效应分解，因此该组件不适用。 |
| A7 | 操作性定义 | 1 | p3 Definitions 2.1–2.2; p4 metrics; p19–24 Figures 1–18 prompt templates; p17 payoff tables. | 对 literal ToM 与 functional ToM 给出了形式定义和可计算指标，对 prompting 与游戏规则给出了可复现模板和 payoff 结构，操作化较完整。 |
| A8 | 水平数与类型 | 0.5 | p6 lists LM/QA/CoT/Plans+Insights/Reflexion/Social; p7 Table 2; p18 action representations; p27 Table 10. | 报告了多种 prompting、游戏、伙伴策略和动作表示的水平与标签，但未系统给出每个因素的水平类型、间距/全距或连续变量中心化说明，故为 0.5。 |
| A9 | 单一操作化的风险 | 1 | p7 Table 2 across RPS/IBS/IPD; p27 Table 10 tit-for-tat; p28–40 Figures 20–43 action types. | 关键构念在多种游戏、伙伴策略和动作表示下重复操作化，并报告了跨操作的会聚/分离模式，符合多操作化要求。 |
| A10 | 单一方法的风险 | 0 | p1–4: LLM prompts and LLM-generated actions are the IV/DV source; no common-method bias test reported. | 自变量（prompt/条件）与因变量（LLM 动作预测/regret）来自同一 LLM 生成渠道，但全文没有报告共同方法偏差的程序控制或统计检验。 |
| B1 | 被试间设计 | NA | — | 没有人类被试，也没有把独立分析单位随机分配到互斥条件的人类被试间设计，故不适用。 |
| B2 | 被试内设计 | 0.5 | p6–7: same models evaluated across prompting strategies (Table 2); p17: episode protocol; no condition-order balancing reported. | 同一模型跨多个 prompting/游戏条件评估，具有重复测量性质，但没有报告条件顺序平衡方案或各顺序分配，故为 0.5。 |
| B3 | 混合设计 | 0 | p5–7 Tables 1–3; p27 Table 10; no per-factor between/within labeling or mixed error terms. | 研究比较模型间差异与模型内 prompting/游戏条件，但没有逐因素标注组间/组内属性，也没有使用混合模型或分别报告两类误差项。 |
| B4 | 因子设计 | 0 | p5 Table 1; p7 Table 2; p27 Table 10 report cell means but no full design matrix, cell n, or interaction statistics. | 存在多因素交叉比较，但未给出完整设计矩阵、每格样本量，也未报告交互项统计量，故未满足因子设计报告要求。 |
| B5 | 主效应 | 0 | p5–8 Tables 1–3 only descriptive means ± intervals; no main-effect F/df/p/effect size. | 论文只报告描述性均值与区间，没有对因素主效应做正式统计检验。 |
| B6 | 交互作用 | 0 | p5–8 Tables 1–3; no interaction test or simple-effects analysis. | 没有报告交互项统计检验，也没有在交互显著时做简单主效应或事后比较。 |
| B7 | 区组设计 | NA | — | 研究没有使用区组/分层变量进行区组设计，故不适用。 |
| B8 | 拉丁方 | NA | — | 研究没有使用拉丁方设计，故不适用。 |
| B9 | 准实验设计 | NA | — | 该研究不是准实验设计；模型/条件比较不涉及人类非随机分组与因果推断的准实验框架。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM 各条件为独立会话/重置上下文，不涉及人类被试内处理可逆性与迁移对称性问题。 |
| C1 | 随机化 | NA | — | 没有人类被试分配；LLM 模型与条件不是通过随机分配程序分配到互斥组，故不适用。 |
| C2 | 平衡 | NA | — | LLM 每个条件独立会话、无跨条件残留，条件顺序不构成需要平衡的迁移问题，故不适用。 |
| C3 | 恒定 | 1 | p17: Watsonx API, 100-step episodes, 24h/100 episode cap, ≥30 episodes; p18 quantization; p9 conclusion 'simple matrix games with very simple partners' as boundary. | 明确列出了 API、episode 长度、运行上限、最少 episode 数、量化设置等恒定条件，并在结论中说明简单矩阵游戏/简单伙伴的外部效度边界。 |
| C4 | 匹配 | NA | — | 研究没有使用匹配程序，故不适用。 |
| C5 | 纳入为变量 | NA | — | 研究没有把混淆变量作为协变量或区组因素纳入统计模型，也没有 ANCOVA 分析，故不适用。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类被试或人类评分者需要盲法，故不适用。 |
| C7 | 平衡的层级 | NA | — | 没有需要选择完全平衡/拉丁方/ABBA 层级的条件顺序设计，故不适用。 |
| D1 | 练习效应 | 0.5 | p4: 'interaction horizon ... 10x longer ... to make sure behavior converges'; p28: convergence curves; no practice block/trial trimming/covariate. | 通过 100 步 horizon 和收敛曲线考虑了上下文内学习/初期不稳定，但没有练习块、前段试次截除标准或将试次位置作为协变量，故为 0.5。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳效应，且任务由 API 自动运行，不适用疲劳控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个条件为独立会话并重置上下文，不存在跨条件延滞/迁移残留，故不适用。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移结构，故不涉及不对称迁移检验。 |
| D5 | 范围效应 | NA | — | 因变量为客观动作准确率/regret，不是主观量值估计或李克特量表，不涉及范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | p17 lists action0/action1/action2 in fixed order; p19 Figure 1 compares token probabilities for listed actions; no position randomization/counterbalancing reported. | LLM 从固定顺序列出的动作选项中选择，但未报告对动作/选项顺序做随机化或反平衡，也未讨论位置偏差。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，不涉及默认赞同偏差。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 研究不使用等级量表，也没有跨群体反应风格比较，故不适用。 |
| E4 | 需求特征 | NA | — | LLM 无人类被试需求特征，且研究不涉及人类掩饰情节或事后访谈，故不适用。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试/评分者，故不适用实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5 Table 1: ToM % values e.g. 97.4 ± 0.4, 96.8 ± 0.2; only mean ± interval, no skew/endpoint frequencies or difficulty calibration. | 报告了均值与区间，部分 ToM% 接近天花板，但未报告偏度、端点频率或 pilot 难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 该研究不是同源自陈式多构念量表测量，不适用共同方法偏差的程序控制/统计检验框架。 |
| F1 | 统计结论效度 | 0.5 | p17: 'at least 30 episodes and confidence intervals ...'; p5 Table 1 reports ± intervals; no power analysis or multiplicity correction. | 报告了均值与置信区间，但缺样本量确定依据（功效分析）、多重性校正和正式统计假设检验说明，故为 0.5。 |
| F2 | 内部效度 | 0.5 | p17 episode protocol; p28 discusses inductive-bias confound; no random assignment/allocation concealment/flow. | 评估了动作表示等内部效度威胁，并报告了部分运行协议；但没有随机分配、分配隐藏、基线等价检验或被试流向/损耗处理，故为 0.5。 |
| F3 | 构念效度 | 0.5 | p3 Definitions; p7 Table 2 shows literal vs functional dissociation across games; no reliability coefficients or manipulation check. | 通过形式定义、跨游戏/伙伴的区分模式提供了构念效度论证，但没有报告信度系数、操纵检验或多操作化会聚统计，故为 0.5。 |
| F4 | 外部效度 | 1 | p17 model list/API episodes; p9 conclusion limits to 'simple matrix games with very simple partners'; p25–27 cross-model/game replication. | 报告了模型来源/版本、游戏与伙伴设置，在结论中明确推广边界为简单矩阵游戏/简单伙伴，并在多个模型与游戏上报告结果，外部效度报告较完整。 |
| G1 | 分析单位 | 0.5 | p17: episodes and 'confidence intervals are based on the actual sample size'; p5–8 means aggregated over episodes; no multilevel model separating step/episode variance. | 说明了 episode 层面的样本量，但统计上主要用 episode 均值与区间，未显式处理 step 嵌套于 episode、episode 嵌套于模型/条件的聚集结构，故为 0.5。 |
| G2 | 随机效应 | 0 | p5–8 Tables; models treated as fixed comparison groups; no random-effects structure reported. | 模型与条件被当作固定比较组，未报告随机效应结构，也未说明结论可推广到哪些模型总体。 |
| G3 | 材料作为随机效应 | 0 | p5–8 fixed RPS/IBS/IPD games and fixed partner policies; no item/material random effect. | 游戏与伙伴策略被视为固定的有限材料，没有作为从更大材料总体抽样的随机因子纳入分析。 |
| G4 | 统计功效 | 0 | p17: ≥30 episodes/24h cap but no a priori power analysis; p5 Table 1 reports intervals but no formal power. | 没有事前功效分析或样本量论证，仅报告了区间，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p18: 'we always report the best value' for Reflexion memory; p17 episode stopping; no exclusion rules or full analysis registry. | 报告了部分运行/停止规则，但存在按最佳 memory size 选择报告的研究者自由度，且未完整报告排除规则、全部条件与验证性/探索性分析区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration/platform/link reported in the paper. | 全文没有公开预注册、注册编号或分析计划，故为 0。 |
| J1 | 位置偏差 | 0 | p17 fixed action0/action1/action2 listing; p19 Figure 1; no A/B swap or position-randomization/flip-rate report. | 涉及多动作选择，但动作选项按固定顺序列出，未做位置反平衡/交换重判，也未报告位置×正确率或翻转率。 |
| J2 | 冗长偏差 | NA | — | 研究不涉及 LLM 作为裁判评估开放性生成长短，故不适用冗长偏差。 |
| J3 | 谄媚 | NA | — | 任务没有用户先验立场/framing 操纵，不涉及谄媚偏差。 |
| J4 | 自我偏好 | NA | — | 研究不使用 LLM-as-judge 或成对比较评分，故不适用自我偏好偏差。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p7: 'three in-context examples of ideal thought processes' (CoT 3-Shot); p23 Figure 13 template; no multi-seed/order counterbalancing reported. | 使用了 3 个 few-shot 示例并提供了模板，但没有报告示例来源、标签比例、多 seed 重采样或排列反平衡，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p19–24 Figures 1–18 provide complete prompt templates; no prompt version dates, sensitivity ablation, or dev/test split reported. | 公布了较完整的 prompt 模板，但没有版本号/迭代日期、语义等价措辞的敏感性消融或 dev/test 划分说明，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0 | p7: ablate history/payoffs and add S2A; no actual token counts or position × accuracy manipulation reported. | 研究了长上下文困难并做了 history/payoff 消融，但没有报告实际 token 数，也没有操纵关键信息首/中/尾位置并报告位置×正确率曲线。 |
| J8 | 温度与采样随机性 | 0.5 | p20: 'generates an answer with stochastic decoding'; p17: ≥30 episodes and CIs; no temperature/top-p/seed values reported. | 报告了 stochastic decoding、重复 episode 数与置信区间，但没有报告 temperature、top-p、seed 等采样超参，故为 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p20: stochastic decoding with retry until template match; 'Failures were relatively uncommon'; no repetition penalty/rate reported. | 报告了解码策略与格式重试，但没有报告 repetition penalty、n-gram 重复率/退化率或生成长度上限，故为 0.5。 |
| J10 | 分词效应 | NA | — | 研究为单语言（英语）单脚本实验，无跨语言/跨脚本比较，故不适用分词效应。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p27: 'neutral action representations J, F, B to avoid contamination following prior work'; no training cutoff/contamination-rate check reported. | 识别了动作名称可能带来先验知识/污染风险，并采用中性动作表示缓解；但没有报告模型训练截止日期或污染检测率，故为 0.5。 |
| J12 | 基准饱和 | 0.5 | p5 Table 1 ToM% near ceiling (97.4, 96.8); no saturation discussion or switch to continuous metric for literal ToM. | 报告了分数量程与部分接近天花板的 ToM%，但没有讨论基准饱和或改用连续指标/更难子集来避免噪声范围内差异，故为 0.5。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，故不适用指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p20: responses accepted only if matching template and action list, otherwise re-query; 'Failures were relatively uncommon'; no format legality rate reported separately. | 报告了格式约束与重试策略，但没有报告格式合法率，也未把格式失败与内容错误作为独立指标，故为 0.5。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/越狱评估，故不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1–2 distinguishes literal vs functional ToM and discusses human ToM benchmarks; p5 critiques passive QA benchmarks; no human same-paradigm comparison. | 明确界定了 LLM 上所测构念与人类同名构念的关系，并批评了人类启发式基准；但没有报告与人类数据的同范式对照实验，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 论文没有宣称跨规模“涌现/突变”能力曲线；虽有 LLAMA-2 不同规模描述性比较，但不构成涌现分析，故不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及对代理指标/奖励模型的优化训练，故不适用指标博弈与奖励过优化。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p17: ≥30 episodes and CIs; model names only (e.g., LLAMA-3 70B Instruct) without snapshot/date; no paired bootstrap/McNemar. | 报告了重复 episode 数与置信区间，但模型标识不精确（无 snapshot/日期），也没有配对检验或原始日志，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p4: T=100 interaction steps; p28–40 per-step regret curves; no per-round vs cumulative separation or context-truncation report. | 进行了 100 步多轮交互并报告 per-step 曲线，但没有系统区分单轮与多轮成绩，也未说明每轮是否截断历史，故为 0.5。 |

## 编码小结
论文清楚提出了 literal/functional ToM 的概念区分，并给出了较完整的操作化定义、prompt 模板和多种案例比较；但作为实证部分，它主要是描述性基准比较，缺少正式推断统计、随机化/顺序平衡、信效度证据、功效分析与预注册，且对长上下文位置效应、解码随机性、评估可复现性等 LLM 特有问题报告不完整。因此多数适用组件只能给 0.5，若干设计组件因无人类被试分配而记 NA。
