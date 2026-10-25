# article_088 | Value Portrait: Assessing Language Models’ Values through Psychometrically and Ecologically Valid Items | 2025

研究类型概述：基准构建与心理测量验证研究：招募人类标注者对真实 query-response 对进行相似性评分，计算其与 PVQ-21/BFI-10 得分的相关以构建 Value Portrait；随后对 44 个 LLM 进行零样本 Likert 评分评估，并做 persona 人口偏差与 value steering 分析。分析单位为人类参与者×item 的相关，以及 LLM 模型×item/prompt 的评分。
- **研究构念（Construct）**：Schwartz基本价值取向、人格价值表达与人口群体价值偏差｜CA 构念锚定：态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；冲动性（impulsivity, `trm_50070dce14554`）
- **实验任务与范式（Task / Paradigm）**：基准构建与心理测量验证研究：招募人类标注者对真实 query-response 对进行相似性评分，计算其与 PVQ-21/BFI-10 得分的相关以构建 Value Portrait；随后对 44 个 LLM 进行零样本 Likert 评分评估，并做 persona 人口偏差与 value steering 分析。分析单位为人类参与者×item 的相关，以及 LLM 模型×item/prompt 的评分。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p6 §3.4.1: 'we use six prompts ... three ... reversing their order of options ... averaging'; p8 §4.2: 'diverse demographic personas'; p9 §4.3: 'steered ... toward value dimensions'. | 有 prompt/persona/steering 多水平操纵，但未报告单位分配方式与正式操纵检验，故为部分满足。 |
| A2 | 因变量 | 1 | p5 §3.2.3: 6-point Likert; p6 §3.4.1: mean score then subtract average; p6-7 §3.4.2 and Table 4: Cronbach α 0.76–0.96; p7 validity: Spearman criterion-related validity. | 因变量指标、计分、量表单位、信度与效度证据及 response-scale 归一化均有报告。 |
| A3 | 控制变量 | 0.5 | p7 §4.1.1: 'temperature parameter to 0 across all models'; p5 §3.2.3: 'PVQ-21 and BFI-10 placed at the end to reduce priming'; Appendix E: prescreen 98% approval, balanced age/gender. | 报告了若干控制手段，但未系统列出控制变量清单并逐一说明。 |
| A4 | 混淆变量 | 0.5 | p10 §6: ESS may not reflect non-Western; annotator demographics limited ethnic diversity; Appendix L: social desirability/self-report limitations. | 识别并讨论了多个混淆与局限，但未做敏感性分析，且训练数据污染等威胁未系统控制。 |
| A5 | 调节变量 | NA | — | 理论模型无明确调节变量与交互检验；模型大小/推理能力仅作描述性分组比较。 |
| A6 | 中介变量 | NA | — | 理论模型无中介变量与直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p4-5 §3.2 pipeline; p6 §3.4 evaluation; Appendix G.2 complete prompts. | 关键构念（价值/BFI、评分程序、prompt）均有可复现操作化描述。 |
| A8 | 水平数与类型 | 0.5 | p6 §3.4.1 six prompts; p8 §4.2 persona categories; p9 §4.3 ten steering values; no level type/spacing. | 报告了主要条件水平，但未系统说明水平类型、间距/全距或连续变量中心化。 |
| A9 | 单一操作化的风险 | 1 | p6-7 §3.4.2 Cronbach α and criterion validity; p25 Appendix C cross-loadings; Appendix L limitations; six prompts averaged. | 价值构念使用多条目、多 prompt 与 PVQ/BFI 多工具，并报告会聚/效度证据与局限。 |
| A10 | 单一方法的风险 | 0.5 | p5 §3.2.3 PVQ/BFI at end to reduce priming; Appendix E attention checks; Appendix L social desirability; no CMB statistical test. | 人类自评与 LLM 评分存在同源风险，有程序控制但无共同方法偏差统计检验。 |
| B1 | 被试间设计 | NA | — | 无被试间实验条件分配；44 个模型为观察性比较而非随机分组。 |
| B2 | 被试内设计 | NA | — | 无被试内处理条件顺序设计；所有模型对固定 item 集评分，不是条件顺序实验。 |
| B3 | 混合设计 | NA | — | 无组间+组内混合设计。 |
| B4 | 因子设计 | NA | — | 无因子设计及完整设计矩阵。 |
| B5 | 主效应 | NA | — | 无因子设计主效应检验。 |
| B6 | 交互作用 | NA | — | 无交互作用检验。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方平衡。 |
| B9 | 准实验设计 | NA | — | 无准实验分组。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理效应与迁移/可逆性问题。 |
| C1 | 随机化 | NA | — | 无实验条件随机分配；属单组观察/评估。 |
| C2 | 平衡 | NA | — | 无处理条件顺序需平衡。 |
| C3 | 恒定 | 0.5 | p7 §4.1.1 temperature=0; Appendix G.1 API providers and 8/16-bit quantization; no external validity discussion. | 报告了部分恒定设置（温度、模型版本、量化），但未系统讨论其外部效度限制。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 无实验组间协变量分析需求；人口学变量用于 persona 操纵而非协变量控制。 |
| C6 | 盲法 | NA | — | 数据采集自动化，无人类主试/评分者盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM 每 item 独立提示，无上下文学习；人类调查无练习块设计。 |
| D2 | 疲劳效应 | 0.5 | p5 Appendix E: expected completion 20 min; exclude <6 min; no rest breaks. | 有人类调查时长过滤，但未报告休息间隔或条件时间分散。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件残留/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无迁移对称性检验。 |
| D5 | 范围效应 | 0.5 | p6 §3.4.1: subtract average of all item responses to adjust differences in how LLMs use response scales. | 用归一化处理 response-scale 使用差异，但未做被试间对照或绝对锚校准。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p6 §3.4.1: six prompts, three reversed order of options, averaged. | 做了选项顺序反转，但未报告各位置出现次数、翻转率或分配细节。 |
| E2 | 默认赞同 | 0 | p5 §3.2.3: six-point Likert; no reverse-scored item or acquiescence discussion. | 未报告反向计分题，也未讨论默许偏差。 |
| E3 | 极端 / 中间反应倾向 | 0 | Table 5 p30 only mean normalized scores; no skew/endpoint proportions. | 未报告量表分数分布形态，也未讨论跨群体反应风格威胁。 |
| E4 | 需求特征 | 0 | p37 Appendix J: 'We inform annotators that the data will be used to evaluate the value orientations of language models'; no cover story/post-experimental inquiry. | 未使用掩饰情节或事后访谈检查需求特征。 |
| E5 | 实验者效应 | NA | — | 数据采集自动化，无人类主试/评分者。 |
| E6 | 天花板 / 地板效应 | 0 | Table 5 p30 reports means only; no endpoint frequencies or pilot difficulty calibration. | 未报告端点频率/偏度或任务难度校准。 |
| E7 | 共同方法偏差 | 0.5 | p5 §3.2.3 PVQ/BFI at end; Appendix E attention checks; Appendix L social desirability; no Harman/ULMC. | 有程序控制，但无共同方法偏差统计检验。 |
| F1 | 统计结论效度 | 0.5 | p5 §3.2.3: 46 participants per pair to detect r=0.3, power=0.8; p2: 549 significant correlations; no CI/multiple correction. | 有功效分析与效应量，但缺置信区间与多重性校正说明。 |
| F2 | 内部效度 | NA | — | 非随机实验、无因果推断主张。 |
| F3 | 构念效度 | 1 | p6-7 §3.4.2 and Table 4: Cronbach α 0.76–0.96; p7 criterion-related validity; Appendix C cross-loadings; Appendix L limitations. | 信度、效度、交叉载荷与操作化局限均有报告。 |
| F4 | 外部效度 | 0.5 | p10 §6: ESS Western limitation; annotator ethnic diversity limited; Appendix J demographics; 44 models across families. | 报告了样本来源与部分边界，但未报告跨样本/跨情境复现。 |
| G1 | 分析单位 | 0.5 | p6 §3.4.1: mean score per value dimension across items; no multilevel model for item nesting. | 存在 item 嵌套于模型/维度的结构，但分析用聚合均值，未显式多层建模。 |
| G2 | 随机效应 | NA | — | 未使用混合模型，分析为描述统计/相关。 |
| G3 | 材料作为随机效应 | 0 | p5 §3.2.3: 520 fixed query-response pairs; no (1&#124;item) random effect. | 材料/项目被视为固定集，未在分析中考虑 item 随机效应。 |
| G4 | 统计功效 | 0.5 | p5 §3.2.3 power analysis; Table 4/5 effect sizes; no CI. | 有事前功效分析与效应量，但未报告置信区间。 |
| G5 | 研究者自由度 | 0.5 | p27 Appendix E exclusion criteria and ~5% excluded; p5 sample size; no confirmatory/exploratory distinction. | 报告了排除规则和样本量决定，但未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–42 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册声明。 |
| J1 | 位置偏差 | 0.5 | p6 §3.4.1: three prompts + reversed option order, averaged; no flip-rate report. | 做了选项位置反转，但未报告翻转率/位置×评分曲线及完整平衡细节。 |
| J2 | 冗长偏差 | NA | — | 不涉及 LLM 裁判或开放生成质量长短比较。 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈/纠错对话式评估。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM-as-judge 成对比较。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 零样本评估，无 few-shot 示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p6 §3.4.1 six prompts; Appendix G.2 full templates; no sensitivity ablation/dev-test split. | 公布了完整 prompt 模板，但未报告语义敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文/RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p7 §4.1.1 temperature=0; no seed/repetition/CI. | 报告了温度，但缺 seed、重复采样次数与置信区间。 |
| J9 | 重复与文本退化 | 0.5 | p7 §4.1.1 temperature=0 only; no decoding strategy/repetition rate. | 仅报告温度，未明确解码策略、repetition penalty 或重复率。 |
| J10 | 分词效应 | NA | — | 单语言英文研究，无跨语言/脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p3 §2.2 mentions contamination concern; no test set/training cutoff overlap analysis. | 仅提及污染担忧，未对 Value Portrait 做污染检测或训练截止日期对照。 |
| J12 | 基准饱和 | NA | — | 非能力基准，无基准饱和问题。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | Appendix G.2 p28: 'Your response must contain ONLY ONE of these exact phrases'; no format-valid rate. | 有严格输出格式约束，但未报告格式合法率或重试策略。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 1 | Appendix L p38-39: discusses ground truth/self-report and LLM value inference; p8 §4.2 human ESS comparison; Appendix G.1 model snapshots. | 明确讨论 LLM 价值构念与人类同名构念的关系、人类数据对照及模型快照，符合 LLM-as-participant 的构念定位要求。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | Table 8 p32 variance across dimensions; §G.4 size scaling; no multi-seed/CI. | 报告了跨规模连续指标（价值分数方差），但未多 seed/CI 排除指标假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无对代理指标的优化/RL/best-of-N 环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | Appendix G.1 p27-28 specific model versions (e.g., gpt-4o-2024-05-13); no repetition N/CI. | 提供了较精确的模型 snapshot，但未报告重复次数、置信区间或配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮评分，无多轮对话历史累积。 |

## 编码小结
论文在基准构念化、条目筛选、信效度验证和 LLM 评估可复现信息方面较扎实；但多数实验设计/顺序平衡/盲法等人类实验组件不适用于该基准评估设计，部分偏差控制（如位置翻转率、格式合法率、污染检测、预注册、CI/重复采样）报告不足。
