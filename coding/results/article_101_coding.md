# article_101 | Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View | 2024

研究类型概述：多智能体LLM基准/模拟实验：操纵角色特质、思维模式序列、智能体数量、协作轮次与骨干模型，在MMLU、MATH、Chess Move Validity上评估准确率、token成本、共识与从众等指标；分析单位为题目/社会条件/试验，不是人类被试。
- **研究构念（Construct）**：从众、共识形成、群体协作与人格特质对社会互动的影响｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；态度（attitude, `trm_4a3fd79d09947`）
- **实验任务与范式（Task / Paradigm）**：多智能体LLM基准/模拟实验：操纵角色特质、思维模式序列、智能体数量、协作轮次与骨干模型，在MMLU、MATH、Chess Move Validity上评估准确率、token成本、共识与从众等指标；分析单位为题目/社会条件/试验，不是人类被试。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: 'S1 = ... S4 = ...' and 'eight possible 3-round collaborative strategies'; p.19 Table 5 prompts; p.62 Appendix I prompt sanity check. | 明确报告特质、思维模式与策略水平；但未说明单位分配/随机化，操纵检验仅为提示 sanity check，故0.5。 |
| A2 | 因变量 | 0.5 | p.4: 'average accuracy (Acc) and their respective standard deviations across five trials'; p.20: 'majority vote' and answers 'matched against the ground truth' with matching rules. | 因变量指标和计分方式明确；无信效度证据、连续指标预处理或天花板/地板说明，故0.5。 |
| A3 | 控制变量 | 0.5 | p.18 Table 4 decoding parameters; p.19 Table 5 prompts; p.4 50 sampled questions. | 报告了模型版本、温度、top-k/top-p、提示和部分数据设置，但未系统列出控制变量清单及控制手段，0.5。 |
| A4 | 混淆变量 | 0 | p.9 Limitations discusses expense, adaptive decisions, broader traits and manual validation, but not identified confounds or sensitivity analysis. | 未明确识别潜在混淆及其控制，也未报告残余混淆或敏感性分析；适用却缺失，记0。 |
| A5 | 调节变量 | NA | — | 无调节变量假设或交互检验；按规则记NA。 |
| A6 | 中介变量 | NA | — | 无中介变量假设或直接/间接效应分解；按规则记NA。 |
| A7 | 操作性定义 | 1 | p.19 Table 5 gives full role/thinking/question prompts; p.20 gives majority-vote and answer-matching rules; p.30 defines conformity and consensus formulas. | 逐构念给出可复现的提示、输出格式、计分规则和从众/共识操作化，达到1。 |
| A8 | 水平数与类型 | 0.5 | p.4 lists two traits, four societies and eight 3-round strategies; p.6 reports agent numbers 2–10 and rounds 3–10. | 水平数和取值明确；未系统标注水平类型、间距/全距或连续变量中心化，0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.19 uses single role-playing prompt per trait; p.62 Appendix I sanity check; p.9 mentions broader traits as limitation. | 关键特质主要是单一提示操作化；有 sanity check 和部分局限讨论，但无多操作会聚证据，0.5。 |
| A10 | 单一方法的风险 | NA | — | 非人类自评/多构念量表研究；IV与DV均来自LLM输出，共同方法偏差检验不适用于此类设计。 |
| B1 | 被试间设计 | NA | — | 无人类被试间分配；LLM条件为全交叉评估，不构成人类被试间设计。 |
| B2 | 被试内设计 | NA | — | 无人类被试内顺序设计；策略/轮次为独立条件运行，无顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 未构成混合设计；对 society 和 strategy 分别做单因素 ANOVA，而非混合模型。 |
| B4 | 因子设计 | 0 | p.5 Table 2 crosses 4 societies × 8 strategies; p.20 Table 6/7 report separate one-way ANOVAs. | 有多因素交叉表，但未报告交互项、完整设计矩阵、每格样本量和 F/df/效应量，基本要件未达，0。 |
| B5 | 主效应 | 0.5 | p.20 Table 6/7 report p-values for society and strategy main effects. | 报告了主效应统计检验，但仅p值，无F/df/效应量；交互未检验，故0.5。 |
| B6 | 交互作用 | 0 | p.20 Table 6/7 only one-way ANOVAs; no interaction term reported. | 完全未报告交互检验及简单效应，0。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计；按规则记NA。 |
| B8 | 拉丁方 | NA | — | 无拉丁方设计；按规则记NA。 |
| B9 | 准实验设计 | NA | — | 非人类准实验；无随机分配问题与准实验类型，记NA。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内设计，不涉及可逆性/迁移对称性，记NA。 |
| C1 | 随机化 | NA | — | 条件全交叉，无独立单位随机分配；题目随机抽样不是处理分配。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，无需平衡方案。 |
| C3 | 恒定 | 0.5 | p.18 Table 4 lists model, temperature, top-k, top-p; p.19 Table 5 lists prompts. | 列出多个恒定参数，但未系统列恒定变量清单及外效限制；0.5。 |
| C4 | 匹配 | NA | — | 无匹配设计；按规则记NA。 |
| C5 | 纳入为变量 | NA | — | 未将混淆变量作区组/协变量纳入模型；无此设计，记NA。 |
| C6 | 盲法 | NA | — | 无人类被试/评分者盲法；不适用。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级；不适用。 |
| D1 | 练习效应 | NA | — | LLM每条件独立调用，无人类练习效应或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 无人类疲劳/长session设计；不适用。 |
| D3 | 延滞 / 迁移效应 | NA | — | 条件间无跨条件残留或清洗期问题；不适用。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题；不适用。 |
| D5 | 范围效应 | NA | — | 无主观量表或绝对判断范围效应；不适用。 |
| E1 | 位置 / 顺序偏差 | 0 | p.19 MMLU prompt fixes options as 'A) <A>, B) <B>, C) <C>, D) <D>'; p.4 only randomly samples questions, not option order. | 多选题选项顺序固定，未做位置随机化/反平衡，也未讨论选项位置偏差，0。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表；不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，无跨群体反应风格比较；不适用。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征/事后访谈；不适用。 |
| E5 | 实验者效应 | NA | — | 无人类主试/评分者参与；不适用。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5 Table 2 reports mean±SD accuracy for all conditions; p.4 describes MATH levels 3–5. | 报告均值/SD，但无偏度、端点频率或 pilot 难度校准；不能充分排查天花板/地板，0.5。 |
| E7 | 共同方法偏差 | NA | — | 非人类自评多构念测量，无共同方法偏差问题；不适用。 |
| F1 | 统计结论效度 | 0 | p.20 reports p-values; p.5 reports mean±SD but no effect sizes or confidence intervals. | 仅报告p值与均值/SD，无效应量、CI、样本量依据或多重性校正，0。 |
| F2 | 内部效度 | 0.5 | p.4–5 uses same sampled questions and fixed models; p.18 fixes decoding; p.9 limitations. | 同一题集与固定流程提供一定基线可比，但无随机分配/分配隐藏/流失说明，内部效度威胁评估不完整，0.5。 |
| F3 | 构念效度 | 0.5 | p.62 Appendix I performs prompt sanity check; p.19 prompts; p.20 answer matching and manual validation. | 有提示 sanity check 和规则/人工校验，但无信度/效度指标，0.5。 |
| F4 | 外部效度 | 0.5 | p.4 describes 50-question samples; p.6 evaluates other LLMs; p.9 limitations discuss broader traits and tasks. | 报告数据集与模型来源，并讨论部分边界；但样本代表性和跨情境复现不系统，0.5。 |
| G1 | 分析单位 | 0.5 | p.4 averages accuracy/SD 'across five trials'; p.20 uses one-way ANOVA on condition-level results. | 以均值聚合题目/试验后做ANOVA，未显式处理题目/试验嵌套；部分说明分析层级但不足，0.5。 |
| G2 | 随机效应 | 0 | p.20 one-way ANOVAs; no mixed models or random effects reported. | 模型/社会/策略均按固定效应分析，未设题目或试验随机截距，未报告可推广总体，0。 |
| G3 | 材料作为随机效应 | 0 | p.4 randomly selects 50 questions per dataset; p.20 analyzes aggregate accuracy, not item-level mixed models. | 题目为有限抽样但未作 item 随机效应或准F，结论不能推广到材料总体，0。 |
| G4 | 统计功效 | 0 | p.4 uses 50 questions and five trials, citing expense; p.20 reports p-values but no power analysis. | 无事前功效分析或样本量功效依据，无效应量/CI，0。 |
| G5 | 研究者自由度 | 0.5 | p.20 reports non-compliance/matching exclusions; p.4 describes sampling; no clear confirmatory/exploratory separation. | 报告部分排除规则与全部主要条件，但样本量决策和验证/探索分析区分不完整，0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.9 Reproducibility Statement points to GitHub; no preregistration or registered report. | 无预注册，记0。 |
| J1 | 位置偏差 | 0 | p.19 MMLU options are fixed in order; no A/B swap or position randomization reported. | LLM多选题存在候选项位置，但未反平衡/随机化，未报告位置偏差，0。 |
| J2 | 冗长偏差 | NA | — | 不用LLM裁判评估开放生成质量；准确率由规则匹配，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 无用户先验立场/反馈操纵；同侪从众另有测量，不属用户谄媚。 |
| J4 | 自我偏好 | NA | — | 无LLM-as-judge或成对比较；不适用。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验为零样本提示，无few-shot示例；不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.19 Table 5 provides full prompt templates; p.62 Appendix I performs prompt sanity check; p.18 lists decoding parameters. | 公布完整模板并做提示检查，但无版本号、语义敏感性消融或dev/test划分，0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p.18: LLaMA2 context limit 4096 and 'prune content from the earlier rounds'. | 报告上下文限制和截断策略，但无实际token数与关键信息位置×正确率分析，0.5。 |
| J8 | 温度与采样随机性 | 0.5 | p.18 Table 4 reports temperature/top-k/top-p; p.4 reports five trials with mean/SD. | 报告采样超参和5次重复，但无随机种子、95%CI或所有模型精确snapshot，0.5。 |
| J9 | 重复与文本退化 | 0.5 | p.18 Table 4 reports decoding parameters, but no repetition penalty or degeneration QC metrics. | 报告解码策略，但未报告重复率/退化率/截断比例，0.5。 |
| J10 | 分词效应 | NA | — | 单语言英文任务，无跨语言/跨脚本比较；不适用。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.4 uses public MMLU, MATH and BIG-Bench Chess Move Validity; no training cutoff comparison or contamination test. | 未报告测试集版本与模型训练截止日期对照，也无污染检测，0。 |
| J12 | 基准饱和 | 0.5 | p.5 Table 2 reports accuracy scores; p.4 describes datasets but no SOTA/ceiling analysis. | 报告分数量级但未给SOTA位置、CI或饱和分析；MMLU约60–70未近天花板，仍缺正式评估，0.5。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；格式不合规仅用于排除，非按约束类型测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.19 specifies output formats (\boxed{(X)}, regex); p.20 says non-compliant multiple answers are disregarded. | 格式约束设置明确，但未报告格式合法率/重试策略，格式失败与内容错误未分开，0.5。 |
| J15 | 越狱稳健性 | NA | — | 无安全/越狱评估；不适用。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1 abstract claims human-like social behaviors; p.3 introduces social psychology concepts; p.9 limitations. | 以社会心理学构念解释LLM行为，但无人类同范式对照或系统构念等价论证，0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨规模/训练进展的涌现曲线；模型比较为固定时点评估，不适用。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无代理指标优化、RL或best-of-N环节，不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4 reports five trials; p.5 uses gpt-3.5-turbo-1106; p.18 reports decoding parameters. | 有N=5、SD和部分snapshot，但无CI/配对检验/原始日志，开源模型snapshot不精确，0.5。 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | p.6 evaluates 3–10 collaboration rounds; p.7 Figure 4 reports round-wise accuracy; p.18 describes context pruning for LLaMA. | 做了多轮评估并按轮次展示，但存在历史截断，未系统比较单轮/多轮差值及截断影响，0.5。 |

## 编码小结
论文提供了较完整的LLM多智能体协作实验框架、提示与解码参数，但统计上以单因素ANOVA和p值为主，缺少交互检验、效应量/CI、功效分析、随机效应/项目推广与污染控制；多数人类被试特有组件不适用。
