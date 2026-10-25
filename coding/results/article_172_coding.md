# article_172 | Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study | 2025

研究类型概述：该文是 LLM 基准评测与提示操纵研究，并附带基于 GPT-4 生成校准数据的开源模型微调。核心操纵为角色引导（教师/同学、法官/律师、无角色）、强提醒、线索真伪（truth/random）和 1-3 步自我反思；因变量为多项选择正确率、口头置信度、completion degree 与 ECE 校准。分析单位主要是题目/提示设置层面的聚合比较，模型组为固定模型而非随机样本。
- **研究构念（Construct）**：元认知式自我知识、错误线索依赖、权威敏感性与口头置信度校准｜CA 构念锚定：元认知（metacognition, `trm_4a3fd79d0a920`）；错误监测（error detection, `trm_4a3fd79d0a20c`）；行为监控（performance monitoring, `trm_4a3fd79d0ac30`）
- **实验任务与范式（Task / Paradigm）**：让GPT-3.5和GPT-4在知识问答中经历无角色、教师/同学或法官/律师角色，配合正确或随机答案提醒并连续自我反思三步，报告答案和置信度。（操纵角色身份、是否强提醒、线索正确或随机、反思步骤、知识领域和模型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4: 'introduce different roles such as teacher, classmate or no-role ... correct or random answer'; p6: 'prompt settings of step-1 and step-2'; p15-16 Table 7 lists step-3 prompts. | 明确命名并给出角色/提醒/线索水平，但未报告操纵检验，分配方式仅可推知为同一批题接受多设置。 |
| A2 | 因变量 | 0.5 | p7 Tables 2-3 use accuracy and confidence; p9 'we define a new metric ... com ... 2×A×C/(A+C)'; p20 ECE; p16 non-numerical confidence excluded. | 因变量指标与计分基本明确，但缺信效度证据和系统预处理/天花板说明。 |
| A3 | 控制变量 | 0.5 | p6: 'default temperature'; 'same seed as 42'; 'maximum length to 2048'; LoRA rank/alpha and hardware. | 报告了若干恒定的模型与训练参数，但不是系统控制变量清单，也未逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p8: 'shortcut on roles, or bias that LLM has learned during training'; p23: 'training data ... difficult to eliminate hidden biases' and 'shortcut features'. | 识别了训练数据/捷径偏差，但未说明具体控制方式或残余混淆的敏感性分析。 |
| A5 | 调节变量 | 0 | p8: 'under role guidance, LLM is less affected by random answers'; Tables 2-3 compare Δ under roles. | 研究实质上提出角色对错误线索效应的调节，但未做正式交互检验、中心化或简单斜率。 |
| A6 | 中介变量 | NA | — | 理论模型不含中介变量，也无直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p4 RQ1 defines self-knowledge as insisting/correcting under misleading guidance; p5 double-calibrated; p9 com scoring; p20 ECE; p15-16 prompts. | 关键构念均给出可执行的操作化：提示模板、选择正确率、数值置信度、com 与 ECE。 |
| A8 | 水平数与类型 | 0.5 | p7 Tables 2-3 list Role (T/C/w/o), Rem (7/3), Cue (t/r); p15-16 Table 7 lists role-cue prompts; steps 1-3 fixed. | 给出各水平标签，但未报告水平类型、间距/全距，且表中的 3/7 编码含义不够清楚。 |
| A9 | 单一操作化的风险 | 0.5 | p7-8 jointly use acc and conf; p20 adds ECE/calibration; p23 discusses overconfidence limits. | 采用多个指标/数据集但未系统报告会聚证据；对单一置信度操作的局限只作部分讨论。 |
| A10 | 单一方法的风险 | NA | — | 不是多构念自陈式同源测量；自变量是外部提示操纵，因变量为客观正确率/数值置信度，CMB 框架不适用。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立 LLM 单位被随机分到互斥条件；模型比较是固定模型组，不是被试间分配。 |
| B2 | 被试内设计 | 0.5 | p6: 'about 1,645 samples under 9 prompt settings'; p15 similarly 3,180 JEC-QA samples under 9 settings. | 同一批题在同一模型内接受多提示设置，属重复测量结构；但未报告条件顺序平衡，也未把题目/模型作为随机效应。 |
| B3 | 混合设计 | NA | — | 没有明确的人类被试混合设计，也未按组间/组内因素建立混合 ANOVA 模型。 |
| B4 | 因子设计 | 0 | p7 Tables 2-3 and p8-9 Tables 4-6 fully cross Role, Rem, Cue and step; no ANOVA table. | 因子水平有完整交叉呈现，但未给设计矩阵/每格样本量，也无 F、df、p、效应量；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | p7-9 tables report factor-level acc/conf and Δ; no F/p/effect size. | 仅有各因素水平均值/差值的描述性比较，未报告主效应的正式统计检验结果与效应量，基本要件未达成，记 0。 |
| B6 | 交互作用 | 0 | p8 describes role guidance reduces random-cue drop; Tables 2-3 allow descriptive role×cue comparison. | 有角色×线索的描述性交互模式，但无交互检验、简单主效应、多重比较或误差棒；因未报告交互项的正式统计检验结果，按级联规则基本要件未达成记 0。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方或顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不存在非随机分组准实验；模型比较不是准实验处理分配。 |
| B10 | 被试内设计的适用条件 | NA | — | 三步自我反思是固定序列的内在流程，不是需要平衡的重复处理；未以被试内适用条件设计。 |
| C1 | 随机化 | NA | p15: '1,645 samples under 9 prompt settings'. | 同一题接受全部提示设置，没有互斥条件分配，因此无随机分配/分配隐藏可评。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序平衡问题；提示设置独立调用。 |
| C3 | 恒定 | 0.5 | p6: 'default temperature'; 'same seed as 42'; 'maximum length to 2048'; p15 model snapshots GPT-3.5 turbo-1106/GPT-4 turbo-0409. | 列出并固定了部分模型/训练参数，但未系统报告所有恒定变量及外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配。 |
| C5 | 纳入为变量 | NA | — | 未把已知混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | 0 | p18: 'employ GPT-4 and human annotation to evaluate the internal consistency'; Table 12 reports human annotation; no blinding described. | 存在人工评分/标注环节，但全文未报告盲法安排或施盲对象，可能受条件知晓影响。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 顺序设计。 |
| D1 | 练习效应 | NA | — | 无人类练习阶段；提示设置独立调用，步骤内反思不是练习效应控制问题。 |
| D2 | 疲劳效应 | NA | — | 无人类疲劳/session 设计；LLM 调用无疲劳风险。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各提示设置独立；三步反思的上下文传递是设计本身，不是跨条件迁移残留。 |
| D4 | 不对称迁移 | NA | — | 无跨条件不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 无人类 Likert/绝对量值判断的范围效应；置信度是模型直接数值输出。 |
| E1 | 位置 / 顺序偏差 | 0 | p2 example options A/B/C; p19: 'choices are usually identified by a letter (e.g., A, B, C, D)'; no option-order randomization reported. | 多选选项顺序固定，未做随机化/反平衡，也未分析位置效应。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征/事后访谈。 |
| E5 | 实验者效应 | NA | — | 主要数据自动采集；无人类主试或评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p7-9 tables report mean acc/conf; p23 notes 'few instances ... below 80%' confidence and overconfidence. | 报告了均值并讨论高置信/过自信，但缺 SD、偏度、端点频率和 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 同 A10：非多构念自陈式测量，无共同方法偏差检验需求。 |
| F1 | 统计结论效度 | 0 | p7-9 Tables 2-6 report only acc/conf/Δ; no CI, effect size, power, or multiplicity correction. | 仅描述性比较，未报告效应量/置信区间/样本量依据/多重性校正。 |
| F2 | 内部效度 | 0.5 | p6 same seed and model versions; p8/p23 discuss shortcut/bias; no allocation concealment or baseline equivalence test. | 有同一批题跨设置比较和部分混淆讨论，但无随机分配、基线检验或被试流向。 |
| F3 | 构念效度 | 0.5 | p18 Table 12 compares GPT-4 and human consistency; p23 limitations; no formal reliability/validity or manipulation check. | 有操作化与部分一致性证据，但缺工具信度/效度、正式操纵检验和单一操作局限系统讨论。 |
| F4 | 外部效度 | 0.5 | p5-6 describe EG-QA, JEC-QA, openBookQA and model families; p23 limitations. | 报告了数据集/模型来源与部分边界，但无代表性抽样、系统推广边界或跨情境复现分析。 |
| G1 | 分析单位 | 0.5 | p6/p15: prompt settings applied to 1,645 or 3,180 samples; p7-9 aggregate accuracy by setting. | 处理分配在提示设置层，分析在样本汇总层；未显式处理题目嵌套或单位匹配。 |
| G2 | 随机效应 | 0 | p7-9 tables; no mixed model or random effects reported. | 模型/题目均按固定效应处理，未报告随机效应结构。 |
| G3 | 材料作为随机效应 | 0 | p5-6 use fixed benchmark item sets; p7-9 aggregate over items; no item random effect. | 材料/题目被视为固定集合，未把题目作为随机抽样总体建模。 |
| G4 | 统计功效 | 0 | p6 no a priori power analysis; p7-9 no CI/effect size. | 未报告事前功效分析或样本量论证，也未报告效应量/CI。 |
| G5 | 研究者自由度 | 0.5 | p16: '10-20%' non-numerical confidence excluded; p5-6 data splits; no confirmatory/exploratory distinction. | 报告了部分排除规则和数据划分，但未完整说明所有因变量/条件选择及样本量决定方式。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration or registered report mentioned; p6 only code link. | 无预注册，也未区分验证性与探索性分析。 |
| J1 | 位置偏差 | 0 | p2 example lists fixed A/B/C options; p19 letters A-D; no candidate-position counterbalancing or flip-rate analysis. | 选择题位置固定，未做位置反平衡/随机化或位置×正确率分析。 |
| J2 | 冗长偏差 | NA | — | 评估以多选正确率/置信度为主，不涉及开放生成长短比较或 LLM 质量裁判。 |
| J3 | 谄媚 | 0.5 | p4: 'incorporate cue information alongside strong reminders, such as the correct or random answer'; p7-8 accuracy drop under random cues and role effects. | 操纵了外部错误线索/角色立场并测量准确率变化，但未报告逐题答案翻转率，也未区分 feedback/answer sycophancy。 |
| J4 | 自我偏好 | 0.5 | p18: 'employ GPT-4 and human annotation to evaluate the internal consistency'; Table 12 reports ConGPT and Conhuman for GPT-4. | 以 GPT-4 评判自身推理一致性，存在同源裁判风险；有人类对照但未量化自我偏好或匿名化。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，无 few-shot 示例选择/排列。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p6 gives step-1/step-2 prompt text; p15-16 Table 7 gives step-3 templates; p2 gives response format. | 公布了主要模板和多提示设置，但无版本化、语义等价敏感性消融或 dev/test 分离说明。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | p16 Table 8: avg input tokens 219.33-226.46. | 上下文很短，无长文档/RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p6: 'default temperature'; 'same seed as 42'; p15: GPT-3.5 turbo-1106 and GPT-4 turbo-0409. | 报告了温度/种子/快照，但未报告 top-p/top-k、重复采样次数或置信区间。 |
| J9 | 重复与文本退化 | NA | — | 任务为多选短输出，不涉及开放生成退化/重复率比较。 |
| J10 | 分词效应 | NA | p5 EG-QA is bilingual; p6 JEC-QA Chinese; no cross-language tokenization comparison. | 虽有中英数据，但不做跨语言/跨脚本能力比较，也未分析分词效应。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p5-6 use public JEC-QA/openBookQA and web-sourced EG-QA; p15 GPT-4 turbo-0409; no contamination check. | 未对照训练截止日期，也未做 n-gram/DCQ 污染检测。 |
| J12 | 基准饱和 | 0.5 | p7-9 report accuracy near 0.91-0.99 in some settings; no SOTA/ceiling or CI comparison. | 报告了分数水位，但未系统评估饱和或改用连续指标/更难子集。 |
| J13 | 指令遵循 | NA | p16 mentions GPT-3.5 instruction-following weakness but not as designed DV. | 研究不以指令遵循为因变量，无机器可判定的约束类型拆分。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p2 response format 'step: {step}, analysis: {analysis}, answer: {answer}, confidence: {confidence}'; p16 non-numerical confidence 10-20% excluded; p9 completion degree. | 有格式约束和部分格式失败统计，但未报告整体格式合法率、重试策略或把格式失败与内容错误完全分开。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1 abstract: 'treat LLM as a student'; p3-4 'know what LLM knows'; p6 model versions. | 明确以人类学生/自我知识作类比，但未系统论证 LLM 构念与人类同名构念异同，也无人类同范式对照。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨规模/训练进展能力曲线。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | p5 uses double-calibrated GPT-4 data for fine-tuning; p8-10 evaluate on ID/OOD/openBookQA; no independent human held-out overoptimization monitoring. | 优化对象为 LLM 生成/校准数据，评估对象为基准集，二者有分离；但未报告代理-真实双曲线或人类金标准。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p6 seed 42 and model links; p15 GPT snapshots; no repeated N/CI/paired tests. | 有精确快照/种子，但无重复采样置信区间或配对检验，原始日志未发布。 |
| J20 | 多轮对话中的一致性衰减 | NA | p2 prompt shows Step 1-3 in a single prompt/response; no multi-turn dialogue history. | 严格为单轮提示内多步反思，不构成多轮对话评估。 |

## 编码小结
论文在提示模板、数据集、模型版本和部分训练参数上报告较充分，且核心构念有操作性定义；但统计推断薄弱，几乎没有效应量/置信区间、正式交互检验、随机化/顺序控制、题目随机效应或污染检查。角色与错误线索效应主要以描述性表格和 Δ 值呈现，不能支持强因果或心理测量式构念结论。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B6（0.5→0）, B4（0.5→0）, B5（0.5→0）。
