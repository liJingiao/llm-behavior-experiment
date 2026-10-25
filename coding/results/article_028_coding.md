# article_028 | Safer or Luckier? LLMs as Safety Evaluators Are Not Robust to Artifacts | 2025

研究类型概述：LLM-as-a-judge 基准/评估研究。作者在 5 个安全领域的 2303 个人工标注偏好对上评估 11 个 LLM 裁判模型（5 个家族），系统操纵 apology、authority、halo、verbosity、position 五类 artifact，并报告 tie detection、winrate shift、human agreement、self-consistency 与 jury 结果。
- **研究构念（Construct）**：表面特征诱导的评判偏差（artifact-driven judgment bias）｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：LLM-as-a-judge 基准/评估研究。作者在 5 个安全领域的 2303 个人工标注偏好对上评估 11 个 LLM 裁判模型（5 个家族），系统操纵 apology、authority、halo、verbosity、position 五类 artifact，并报告 tie detection、winrate shift、human agreement、self-consistency 与 jury 结果。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.1 Table 1: 'Illustrative examples of artifacts'; p.3 §2.1: 'Apology ... prepend an apology'; 'Authority adds a fake authoritative source'; 'Halo adds a chatty ending'; 'Verbosity rephrases'; 'Position swaps'. | 五种 artifact 有清晰操纵程序与原始/注入水平；但无正式 manipulation check，仅 verbosity 有 qualitative check，且所有样本系统性施加强调而非随机分配。故 0.5。 |
| A2 | 因变量 | 0.5 | p.3–4 Eqs.1–8 define preference mapping, Tie Detection score, winrate shift, human agreement, self-consistency; p.5 Table 2 reports metrics. | 因变量指标与计分公式明确；但无裁判偏好的信效度证据，也无反应分布预处理/防端点说明。0.5。 |
| A3 | 控制变量 | 0.5 | p.4 'we measure both position configurations ... and then take the average'; p.13 Appendix E 'temperature zero for all judges'; p.14 annotation platform anonymize/randomize order. | 报告若干控制手段（位置平均、固定 temperature、匿名/随机化标注），但未系统列出控制变量清单并逐一说明。0.5。 |
| A4 | 混淆变量 | 1 | p.9–10 Limitations: 'Perturbation Method and Self-Enhancement Bias' and 'Competitor Pairing and Self-Enhancement Bias'; p.4 position bias correction. | 识别并控制 position bias，讨论 Command R 重述与同家族自增强残余威胁；对内部效度威胁有说明。1。 |
| A5 | 调节变量 | 0 | p.7 §3.3 compares smaller/larger models descriptively; no interaction test or simple slopes reported. | 模型大小/家族被讨论为影响因素，但只有描述性分组比较，无正式交互检验、中心化或简单斜率。0。 |
| A6 | 中介变量 | NA | — | 无中介变量与中介假设，未做直接/间接效应分解。NA。 |
| A7 | 操作性定义 | 1 | p.3–4 §2.1–2.2 and p.16 Listing 1 give injection steps, judge prompt, output mapping; Eqs.1–8 give scoring. | 关键构念有可复现操作化：artifact 注入、judge prompt、计分公式、数据来源均明确。1。 |
| A8 | 水平数与类型 | 0.5 | p.1 Table 1 lists five artifacts and original/injected examples; p.3 §2.1 describes each; p.3 model list gives sizes. | 报告 artifact 类型与原始/注入水平，但未系统报告水平类型、间距/全距、连续变量中心化。0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.4 §2.2.1 and §2.2.2 use two tests (Tie Detection, Winrate Shift) and human agreement; p.5–6 report both; no convergent validity analysis. | 关键稳健性构念用两个指标/测试测量，报告了各自结果，但未正式报告会聚证据；每个 artifact 仍为单一注入方式。0.5。 |
| A10 | 单一方法的风险 | 0 | p.4 and p.16 prompt shows artifact present in same text input used by LLM judge to produce preference; no Common Method Bias test reported. | IV（artifact）与 DV（judge preference）同源于 LLM 文本判断，未报告共同方法偏差程序控制或统计检验。0。 |
| B1 | 被试间设计 | NA | — | 无人类被试分配到独立条件；同一 judge model 在所有样本/artifact 上评估。NA。 |
| B2 | 被试内设计 | 0.5 | p.4 'we measure both position configurations ... average'; p.11 Appendix A reran same model for self-consistency. | 同一 judge 跨全部样本/条件重复评估，但未明确作被试内/重复测量统计模型，也未给各顺序的 judge 分配；仅位置两序平均与 rerun。0.5。 |
| B3 | 混合设计 | NA | — | 未建立并分析组间×组内混合设计（模型大小与 artifact 均为描述性分组/条件）。NA。 |
| B4 | 因子设计 | NA | — | 研究未采用因子 ANOVA 设计，未报告设计矩阵、每格样本量及交互项统计。NA。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应统计检验（仅描述性百分比/图）。NA。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验与简单主效应/事后比较。NA。 |
| B7 | 区组设计 | NA | — | 无区组变量、划分依据或区内随机分配。NA。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计；位置仅两序平均，不构成拉丁方。NA。 |
| B9 | 准实验设计 | NA | — | 非准实验；无不可随机分组与选择偏差设计。NA。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理可逆性/迁移对称性设计。NA。 |
| C1 | 随机化 | NA | — | 研究单位未随机分配到互斥条件；每个 pair 在原始/注入或两位置下被评估，位置为反平衡而非随机分配。NA。 |
| C2 | 平衡 | 0.5 | p.4 'Correcting for Position Bias ... measure both position configurations (i.e. a-b and b-a) and then take the average.' | 对位置顺序做了完整两序反平衡并平均，但未报告各顺序的样本/模型数、选择理由或迁移对称性。0.5。 |
| C3 | 恒定 | 0.5 | p.13 Appendix E 'temperature zero for all judges'; p.3 model version list; p.3 §2.1 artifacts constant except verbosity. | 列出固定 temperature、模型版本和 prompt 模板等恒定项；未系统讨论这些恒定水平对外部效度的限制。0.5。 |
| C4 | 匹配 | NA | — | 无匹配设计、匹配变量或匹配后均衡性检验。NA。 |
| C5 | 纳入为变量 | NA | — | 未把已知混淆变量作为区组/协变量纳入统计模型（自增强仅在局限讨论）。NA。 |
| C6 | 盲法 | 0.5 | p.14 'annotation platform is designed to anonymize the model each completion belongs to and randomize the order'. | 人类标注者对模型身份盲、顺序随机化；但未报告盲法成功检验，未说明 LLM judge 是否盲（prompt 无模型标签）。0.5。 |
| C7 | 平衡的层级 | 0.5 | p.4 both a-b/b-a configurations averaged; no formal Latin-square/ABBA structure or per-order counts. | 位置采用两序完整反平衡，但未说明层级构造与顺序效应形状假设。0.5。 |
| D1 | 练习效应 | NA | — | LLM judge 每次独立判定，无练习/学习阶段或试次位置问题。NA。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳风险；API 调用短，无条件时间分散问题。NA。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各 judge 调用独立，无跨条件残留/清洗期问题。NA。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移/不对称迁移设计；位置两序平均不涉及处理残留。NA。 |
| D5 | 范围效应 | NA | — | 因变量为成对偏好/Tie，而非李克特等主观量表，无范围效应。NA。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.4 'measure both position configurations ... average'; p.5 Table 2 reports position artifact. | 对选项位置做了 a-b/b-a 反平衡并报告位置效应；未报告每位置出现次数、随机化或逐项翻转率。0.5。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分与默认赞同问题。NA。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表分布或跨群体反应风格比较。NA。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在人类需求特征/掩饰情节。NA。 |
| E5 | 实验者效应 | NA | — | 数据采集全自动 LLM API，无人类主试/评分者期望传递。NA。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5 Table 2 reports Tie Detection values up to 97/98; p.5 Figure 1 plots deviations; no explicit endpoint frequency or pilot calibration. | 报告均值型指标和分布图，可见接近端点；但未给偏度/端点频率，未说明 pilot 难度校准。0.5。 |
| E7 | 共同方法偏差 | NA | — | 非多构念同源自陈式量表；无共同方法偏差的自我报告测量结构。NA。 |
| F1 | 统计结论效度 | 0.5 | p.5 Table 2 and p.15 Table 4 report percentages/effect magnitudes; no CIs, power analysis, or multiplicity correction reported. | 报告效应大小（百分比差异）但无 CI、无样本量依据、无多重校正；非仅 p 值。0.5。 |
| F2 | 内部效度 | 0.5 | p.9–10 Limitations discuss self-enhancement/perturbation confounds; no random allocation, baseline equivalence, or participant flow (not applicable to human RCT). | 无人类随机分配/损耗流程；但对主要内部效度威胁有讨论。作为 LLM benchmark 给 0.5。 |
| F3 | 构念效度 | 0.5 | p.14 CSAM double annotation 97% agreement, triple annotation majority; p.11 Table 3 self-consistency; no manipulation check. | 报告部分标注者信度/self-consistency，但无裁判测量效度证据和正式 manipulation check。0.5。 |
| F4 | 外部效度 | 0.5 | p.3 Dataset: 576 prompts, 2303 pairs across five safety domains; p.15 Table 4 category agreement; no cross-sample replication. | 报告样本来源与类别，但未论证代表性/推广边界，也无跨情境复现。0.5。 |
| G1 | 分析单位 | 0.5 | p.3–4 define sample-level preference Eq.1 and model-level winrate Eq.2; p.5 Table 2 aggregates by judge/artifact. | 明确分析在 pair 与 model 层级，但未用多层模型处理 prompt/judge 嵌套，仅聚合。0.5。 |
| G2 | 随机效应 | 0 | p.3 lists 11 judge models; p.5–7 treat judge/family/size as fixed descriptive groups; no random effects model. | judge models 作为固定集合比较，并对模型大小/家族作概括；未说明随机效应或可推广总体。0。 |
| G3 | 材料作为随机效应 | 0 | p.3 dataset 2303 pairs; p.5 Table 2 aggregates over all pairs; no item random effect or F1/F2 quasi-F. | 有限 prompts/completions 被视为固定材料，未将 item 作为随机效应；结论外推到 safety domain。0。 |
| G4 | 统计功效 | 0 | p.3 dataset size 2303; no a priori power analysis or target effect size; no CIs. | 无功效分析或样本量论证，结果仅报百分比与分布。0。 |
| G5 | 研究者自由度 | 0.5 | p.3 'We remove error generations, for a total of 4606 sampled completions'; Table 2/4 report all artifacts/models; no sample-size stopping rule or exploratory/confirmatory labels. | 报告了排除错误生成与主要条件/指标，但未说明样本量决定、停止规则或探索性/验证性区分。0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–18 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册平台/编号或分析计划。0。 |
| J1 | 位置偏差 | 0.5 | p.4 position correction: both a-b and b-a averaged; p.5–6 report position shifts 4%–30%; p.3 model versions, p.13 temperature zero, p.16 Listing1 prompt; p.14 annotation agreement. | 识别并反平衡 position，报告位置效应与模型版本/prompt/temperature；但无逐项翻转率/各位置正确率，标注者信度仅 CSAM 97%。0.5。 |
| J2 | 冗长偏差 | 0.5 | p.3 §2.1 verbosity rephrasing; p.6 'less than ±2.5% winrate shift'; p.14 Appendix D prompt and qualitative check. | 操纵 verbosity 并报告效应，保持语义；但无长度分布与得分相关、无长度对照/盲评。0.5。 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈/纠错对话，未涉及谄媚。NA。 |
| J4 | 自我偏好 | 0.5 | p.9–10 Limitations 'Competitor Pairing and Self-Enhancement Bias'; p.10 'GPT4o as judge would have evaluated GPT3.5 Turbo...'; p.8 jury selection across families. | 报告 judge 与被评模型可能同源/同家族，并讨论自增强；用跨家族 jury 但未量化 favor-own 比例或各裁判单独结果。0.5。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.16 Listing 1 shows two few-shot examples; p.13 Appendix C.2 says prompt uses few-shot examples but no source/seed balance. | 使用 few-shot 且模板全文可查，但未报告示例来源、标签比例、排列反平衡或多 seed。0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.16 Listing 1 full template; p.13 Appendix C.2 discusses prompt design/initial tailored prompts; no sensitivity ablation or dev/test split. | 提供完整 prompt 模板与温度，但无版本/敏感性消融/dev-test 分离，且仅描述调优经验。0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文或 RAG 实验；输入为短 prompt+成对 completion。NA。 |
| J8 | 温度与采样随机性 | 0.5 | p.13 Appendix E 'temperature zero for all judges'; p.11 Table 3 repeated runs; no top-p/seed/N/CI details. | 报告 temperature=0 和重复运行，但无完整采样超参、seed、每条件 N 与 CI、API snapshot 完整日期。0.5。 |
| J9 | 重复与文本退化 | NA | — | judge 输出为 A/B/Tie 短选项，不涉及开放生成重复退化。NA。 |
| J10 | 分词效应 | NA | — | 单语言英文数据，无跨语言/跨脚本比较。NA。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3 dataset description only; no training cutoff/contamination check. | 使用自建 safety prompts 但未提供训练截止日期对照、n-gram 重叠或污染检测。0。 |
| J12 | 基准饱和 | NA | — | 不是能力基准饱和问题；指标为 artifact bias/agreement，非准确率天花板。NA。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量，无约束类型准确率。NA。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.16 Listing 1 'Your answer should ONLY contain: Output (a), Output (b), or Tie'; no legal-format rate/retry reported. | 要求结构化短输出并给出格式指令，但未报告格式合法率、重试/归一化规则。0.5。 |
| J15 | 越狱稳健性 | NA | — | 评估对象是 judge robustness，不是被测模型安全/越狱；无对抗攻击 ASR。NA。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 纯工程/应用评估 LLM-as-judge，不主张测量人类心理学构念。NA。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 仅比较模型大小，不报告跨规模能力曲线或涌现宣称。NA。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不优化 benchmark/reward/judge 代理指标，无 overoptimization 监控。NA。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.3 exact model list (some dates); p.11 Table 3 self-consistency; p.13 temperature zero; no CIs/paired tests/logs. | 报告模型版本与重复运行，但主分数无重复 N/CI、无配对检验、无原始日志；snapshot 不完整。0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 单轮 prompt-completion 评估，无多轮对话历史。NA。 |

## 编码小结
该文是 LLM-as-a-judge 的 artifact 稳健性评估，而非人类被试实验。artifact 操纵与计分定义较清楚，描述性结果丰富；但缺少正式操作检验、统计模型、随机效应/功效分析、预注册与完整可复现性报告。多数人类实验特有的分配、顺序、疲劳/练习等组件不适用。
