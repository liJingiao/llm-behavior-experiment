# article_164 | Bias Unveiled: Investigating Social Bias in LLM-Generated Code | 2025

研究类型概述：基准/评测研究，并包含提示策略与温度消融以及偏见缓解实验。分析单位是四个 LLM 在 SocialBias-Bench 的 343 个任务上生成的代码片段（每模型 1715 条）；无人类被试。核心比较包括：模型（4 个）、七类人口维度、CBS/BLS/Pass@attribute，以及默认、CoT、正角色+CoT、三轮迭代提示和温度变化。
- **研究构念（Construct）**：代码决策中的人口群体歧视与偏见缓解｜CA 构念锚定：刻板印象（stereotypes, `trm_4a3fd79d0b285`）；态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：让四种现成代码LLM为包含人口属性的人本任务生成可执行决策代码，以Solar生成测试输入并直接比较不同群体的程序输出。（改变年龄、性别、族裔等七类人口属性、代码任务、模型以及CoT、正向角色和迭代对话提示。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: four subject LLMs are named; p.4: three mitigation strategies; p.6 Fig.4: temperature values 0.2–1.0. | 自变量（模型、缓解策略、温度）有明确水平/标签和部分操纵程序，但未报告单位分配方式与操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.4: CBS=Nb/Ne×100; BLS=Ni_bias/Nbias; Pass@attribute=(TP+TN)/(TP+TN+FP+FN). | 因变量指标与计分方式明确，但无信度/效度证据、连续指标预处理或天花板/地板效应说明。 |
| A3 | 控制变量 | 0.5 | p.3: 'keeping the Docstring in a neutral tone and using (self) as method parameters'; p.5: 5 snippets per task. | 报告了若干控制做法（中性 docstring、self 参数、固定每任务 5 个片段），但未系统列出控制变量清单并逐一说明控制手段。 |
| A4 | 混淆变量 | 0.5 | p.2: 'The ablation of temperature and prompt variation shows the sensitivity varies on models and bias types'; p.3: neutral code prompts to avoid misleading prompts. | 识别并部分控制了提示措辞/温度等潜在混淆，但未系统讨论残余混淆或敏感性分析对内部效度的威胁。 |
| A5 | 调节变量 | NA | — | 研究没有调节变量理论模型，也未做乘积项交互检验；温度消融是描述性比较而非正式调节分析，故不适用。 |
| A6 | 中介变量 | NA | — | 无中介变量假设，也无直接/间接效应分解，故不适用。 |
| A7 | 操作性定义 | 0.5 | p.3-4: DSL/textX generates code prompts and executable tests; p.4: metric formulas; p.4-5: exact CoT and P-CoT prompts; p.5: three iterative cycles. | 关键构念有可重复的操作化描述（任务、测试用例、指标公式、部分提示），但迭代提示具体指令与完整测试生成细节不完整，故部分满足。 |
| A8 | 水平数与类型 | 0.5 | p.5: four model names; p.4: default, iterative-1/2/3, CoT, P-CoT; p.6 Fig.4: t=0.2,0.4,0.6,0.8,1.0. | 报告了模型与缓解策略的水平/标签，温度也有取值，但未说明水平类型、间距/全距或连续变量中心化等。 |
| A9 | 单一操作化的风险 | 0.5 | p.4: CBS, BLS, BLS@Range, Pass@attribute; p.6-7 Tables 3-5. | 使用了多种指标测量偏见与功能正确性，但未报告各操作化/指标之间的会聚证据，也未讨论单一操作化对推广的限制。 |
| A10 | 单一方法的风险 | NA | — | 研究不是自陈式测量；自变量为模型/提示，因变量为可执行测试与代码行为，不存在人类自评同源共同方法偏差问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试，也没有被试间条件分配；分析单位是 LLM 生成的代码片段，故被试间设计不适用。 |
| B2 | 被试内设计 | NA | — | 无人类被试内重复测量设计；虽然同一任务在多个模型/条件下评估，但不属于被试内设计。 |
| B3 | 混合设计 | NA | — | 没有组间/组内因素的混合设计及相应误差项，故不适用。 |
| B4 | 因子设计 | NA | — | 未构成完全交叉的因子实验设计；模型、人口维度、缓解策略未以 ANOVA 因子结构及交互项完整报告。 |
| B5 | 主效应 | NA | — | 没有因子设计意义上的主效应检验（F、df、p、效应量），故不适用。 |
| B6 | 交互作用 | NA | — | 没有正式交互作用检验与简单主效应分析；仅描述不同模型/条件下的分数差异。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计，也无区组变量与区内随机分配。 |
| B8 | 拉丁方 | NA | — | 无被试内条件顺序设计，不需要拉丁方平衡。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验；模型/提示条件由研究者固定设置，不涉及非随机分组的选择偏差与因果推断限定。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内设计，因此处理可逆性与迁移对称性不适用。 |
| C1 | 随机化 | NA | — | 无人类被试分配到互斥条件；LLM 条件按模型/提示设定，非随机分配问题。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，因此没有顺序平衡方案。 |
| C3 | 恒定 | 0.5 | p.5: model versions and SocialBias-Bench; p.4: 'initial prompt design, including default style and temperature'. | 报告了部分恒定因素（模型版本、数据集、默认提示风格），但未系统列出所有恒定变量及水平，也未讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计，无匹配变量或匹配后均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作为区组因素或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 评估由可执行测试自动完成，无人类被试/主试/评分者盲法问题。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级，故不适用。 |
| D1 | 练习效应 | NA | — | LLM 代码生成通常按独立调用处理；迭代提示是处理条件本身，不是人类练习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 无人类疲劳效应，且实验不是长时间人类 session。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无药物/学习消退意义上的清洗期；迭代反馈是设计中的干预，不是跨条件迁移污染。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件残留，故不对称迁移不适用。 |
| D5 | 范围效应 | NA | — | 因变量为客观代码测试指标，不是绝对判断或量表评分，无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | NA | — | 没有选项/刺激呈现顺序的被试内操纵；测试用例按属性组合生成，不属于选项位置平衡问题。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，故需求特征不适用。 |
| E5 | 实验者效应 | NA | — | 数据采集与评分完全自动化，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 3 reports CBS percentages; p.7 Table 5 reports several 0.00 values; no SD/skew or pilot calibration. | 报告了主要指标的聚合数值并出现端点值，但未报告分布形态、标准差/偏度、端点频率或任务难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式多构念测量，故共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0 | p.6: 'mean and p-value'; p.7 Table 5 uses '*' for t-test significance; no effect sizes or CIs. | 仅报告 CBS 均值与 p 值/显著性星号，未报告效应量、置信区间、样本量确定依据或多重性校正。 |
| F2 | 内部效度 | 0.5 | p.5: experiment setup and mitigation strategies; p.7: t-test significance in Table 5. | 报告了条件设置与部分比较，但无随机分配、分配隐藏、基线等价性、损耗/流向或系统的内部效度威胁评估。 |
| F3 | 构念效度 | 0.5 | p.2: Eq.1 defines bias via f(np,pi)≠f(np,p'i); p.3-4: DSL-generated executable tests; p.3: second author cross-checks task definitions. | 提供了构念定义与操作化、任务人工核对，但未报告测量信度/效度证据或操纵检验，也未系统论证构念对应关系。 |
| F4 | 外部效度 | 0.5 | p.5: four LLMs and 343 SocialBias-Bench tasks; p.7: conclusion generalizes to current LLMs. | 报告了模型与任务来源/特征，但未明确抽样代表性、推广边界条件或跨样本/跨情境复现结果。 |
| G1 | 分析单位 | 0.5 | p.5: 'For each coding task, we used an LLM to generate 5 code snippets ... 1715 generated code snippets'; p.7: t-test. | 说明了生成/分析单位为代码片段并给出每模型数量，但未处理片段嵌套于任务、任务嵌套于类别的结构，统计层级不明确。 |
| G2 | 随机效应 | 0 | p.5-6: results are aggregated by model/demographic; no random-effects/mixed model is reported. | 未说明随机效应/固定效应结构；任务/片段被视为固定或独立观测，未分离任务随机方差，推断可推广性受限。 |
| G3 | 材料作为随机效应 | 0 | p.5: 343 tasks; p.6 Tables 3-4 aggregate across tasks; no item/task random effect. | 未将任务/材料作为随机效应纳入分析，无法把结论正式推广到任务总体。 |
| G4 | 统计功效 | 0 | p.6-7: no power analysis, effect sizes, or CIs; only p-values/asterisks. | 没有事前功效分析或其他样本量论证，也未报告效应量与置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.5: 5 snippets per task; p.7: 'Only 1% of the generated code ... is not executable'; Table 5 only GPT-3.5 due to space. | 报告了每任务片段数与部分非可执行代码比例，但未完整报告排除规则/数量、全部模型全部条件结果及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–10 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册平台、编号、分析计划或验证性/探索性区分，按规则记 0。 |
| J1 | 位置偏差 | NA | — | 不涉及多候选项选择、排序或 LLM-as-judge 成对比较；评估由可执行测试完成。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM 裁判评估开放文本长度/质量，故冗长偏差不适用。 |
| J3 | 谄媚 | NA | — | 没有操纵用户先验立场或测量迎合/谄媚；迭代反馈来自 Solar 测试结果，不是用户立场框架。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge，评估基于可执行测试，无自我偏好裁判问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，未使用 few-shot in-context examples（相关工作中提到他人使用 few-shot，但本研究未用）。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4: exact CoT prompt and positive role-play+CoT prompt; p.5: iterative prompt refinement; no full template/version or semantic-equivalence ablation. | 给出了部分提示文本并做了提示策略/温度消融，但未提供完整模板版本、迭代日期、dev/test 划分或系统措辞敏感性分析。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短代码提示，不涉及长文档/RAG 或长上下文位置效应。 |
| J8 | 温度与采样随机性 | 0.5 | p.5: temperature settings; p.5: 5 code snippets per task; p.6 Fig.4: CBS across t=0.2–1.0. | 报告了 temperature 与每任务重复 5 次，但缺 top-p/top-k、随机种子、95% CI 及闭源 API 调用日期/snapshot 的完整统计设计。 |
| J9 | 重复与文本退化 | 0.5 | p.5: 'default style and temperature'; p.6: temperature variation; no repetition penalty/degeneration QC. | 报告了温度设置与代码生成，但未说明 greedy/beam/sampling、repetition penalty、重复率/退化率或截断比例。 |
| J10 | 分词效应 | NA | — | 单语言（英语）、单脚本，且无跨格式输入比较，分词效应不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3: SocialBias-Bench is newly constructed; p.5: four model names/versions; no contamination detection or training-cutoff comparison. | 未报告测试集与模型训练数据截止日期的对照，也未做 n-gram/DCQ 等污染检查，不能排除记忆复现。 |
| J12 | 基准饱和 | 0.5 | p.6 Table 3: CBS values 28.34–60.58; p.7: Pass@attribute 66.60–79.60; no saturation/CI discussion. | 报告了分数与量程，未接近明显天花板，但未讨论饱和问题或做 bootstrap CI 比较；部分满足。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；任务是代码生成并测量偏见与 Pass@attribute，故不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.7: 'Only 1% of the generated code in our experiment is not executable'; p.3: tests are syntax-error-free. | 报告了代码可执行率/格式相关结果，但未报告结构化输出约束设置、格式合法率与内容错误的分开指标、重试策略或输出归一化规则。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估，故不适用。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究是软件公平性/代码生成评测，不主张测量 LLM 的心理学/认知构念，故不适用。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随模型规模或训练进展的能力曲线与涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | 0 | p.5: iterative prompting uses feedback from Solar's bias testing results; p.7 Table 5 evaluates on the same test suite. | 迭代提示直接用 Solar 测试结果作为反馈并再用同一测试集评估，未用独立 held-out 人类评估监控代理指标优化；存在代理指标过优化风险且未分离。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5: model names/versions and 5 snippets per task; p.7: code/data artifact links; no repeats/CI or exact commit. | 报告了模型版本/日期与重复生成数量，并公开代码数据，但缺重复次数置信区间、精确 snapshot/commit、配对检验与原始推理日志。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.5: 'three cycles of interaction and prompt refinement'; p.7 Table 5: IterPrompt-1/2/3. | 迭代提示构成三轮多轮反馈并报告每轮 CBS，但未说明上下文是否截断、历史累积方式及多轮一致性衰减分析。 |

## 编码小结
论文提出 Solar 框架与 SocialBias-Bench，系统评测并尝试缓解 LLM 代码生成中的社会偏见；指标公式、任务构造与部分提示策略报告较清楚。但统计报告不完整：缺效应量与置信区间、随机效应/任务嵌套建模、污染检查、预注册与多种敏感性控制；部分人类实验设计组件不适用。
