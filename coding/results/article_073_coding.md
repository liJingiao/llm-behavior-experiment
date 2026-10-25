# article_073 | Representations of Fact, Fiction and Forecast in Large Language Models: Epistemics and Attitudes | 2025

研究类型概述：行为基准式 LLM 评估：用受控故事操纵模态语义、证据类型和问答格式，测试八个开放权重指令微调模型的选择准确率；分析单位为模型对独立提示的回答，模型规模/家族比较属观察性分组，无人类被试、无随机分配。
- **研究构念（Construct）**：认识情态与证据敏感的信念/态度表达（epistemic modality and evidence-sensitive belief/attitude expression）｜CA 构念锚定：态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：行为基准式 LLM 评估：用受控故事操纵模态语义、证据类型和问答格式，测试八个开放权重指令微调模型的选择准确率；分析单位为模型对独立提示的回答，模型规模/家族比较属观察性分组，无人类被试、无随机分配。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4 §4.1: 'In the condition with a necessity modal... In the condition with a possibility modal...'；p.5: three QA formats (direct slot, indirect slot, indirect sentence). | 明确命名并定义模态条件、故事类型与 QA 格式的水平和构造方式；但未见操纵检验，也未说明单位如何随机分配（全部提示系统性交叉）。 |
| A2 | 因变量 | 0.5 | p.5 §4.1: 'We measure the performance with accuracy and paired accuracy'；p.7 §5.1: accuracy, paired accuracy, joint accuracy. | 因变量指标与计分规则明确，但未报告信度/效度证据或连续指标预处理/端点控制（离散准确率）。 |
| A3 | 控制变量 | 0.5 | p.3 §3.2: 'We use greedy decoding for the result'；p.4 §4.1: controlled stories/templates；p.4: A100 GPUs. | 报告了若干保持恒定的做法（固定模型版本、贪心解码、受控故事模板），但未系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p.2 §1: 'risk of data contamination... To address such concerns, we design controlled stories'；p.9 Limitations: English only, no human participants. | 识别了污染/世界知识等潜在混淆并以自制受控故事降低风险，但未系统说明残余混淆或敏感性分析。 |
| A5 | 调节变量 | 0.5 | p.6: 'The interaction between number of parameters and modal condition is also significant...'；p.14 Tables 3-4: sum-to-zero contrast coding；p.5 Fig.3 error bars. | 模型规模作为调节变量并检验交互，报告对比编码和图示；但没有正式简单斜率/多重比较校正。 |
| A6 | 中介变量 | NA | — | 无中介假设与中介分析。 |
| A7 | 操作性定义 | 1 | p.4-5 §4.1 and p.7 §5.1 design; p.16-19 Appendix E full prompt templates; p.2 code link. | 关键构念通过具体的受控故事模板、提示格式和答案计分操作化，示例与模板足以复现。 |
| A8 | 水平数与类型 | 1 | p.4-5: factor levels (story type base/1-shot/counterfactual; modal necessity/possibility; QA direct/indirect slot/indirect sentence); p.14 Tables 3-4. | 各因子水平数与标签明确，均为分类变量，并用 sum-to-zero 对比编码；连续间距/全距不适用。 |
| A9 | 单一操作化的风险 | 0.5 | p.4: five templates; p.4-5: three QA formats; p.6 and p.8 show effects vary across formats/templates. | 关键构念采用多种故事模板与问答格式，但未报告各操作化之间的会聚证据；结果反而显示格式敏感性。 |
| A10 | 单一方法的风险 | NA | — | 不是多构念自陈量表；IV 为提示/story 操纵，DV 为模型离散回答正确率，人类共同方法偏差框架不适用。 |
| B1 | 被试间设计 | NA | p.4: eight fixed open-weight models; p.6 regression by LLM class. | 无人类被试或独立被试组分配；模型为固定评估对象。 |
| B2 | 被试内设计 | NA | p.4: 'We use greedy decoding'；p.5 independent prompts. | 每个提示独立生成，不存在被试内条件顺序或重复测量顺序设计。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合的人或被试设计。 |
| B4 | 因子设计 | 0.5 | p.4-5 factors fully crossed; p.6 and p.20-22 logistic interaction tables; p.14 contrast coding. | 存在多因素交叉并报告交互，但未给完整设计矩阵/每格样本量；统计为 logistic 系数而非 ANOVA F/df/效应量。 |
| B5 | 主效应 | 0.5 | p.6: 'number of parameters has a significant impact...'；p.20-21 Tables 7-10 main effects. | 主效应以 b/SE/z/p 报告，但无标准化效应量/CI，且交互显著时未明确声明主效应解释受限。 |
| B6 | 交互作用 | 0.5 | p.6: interaction coefficients and p values; p.5 Fig.3, p.8 Fig.5 and p.15 Figs.6-9 with 95% CI error bars. | 报告交互显著性和图示误差棒，但未做正式简单主效应检验或多重比较校正。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | 0 | p.6: 'number of parameters has a significant impact on response accuracy'；p.8: medium parameters 'lead to a significant increase'. | 比较不同规模模型属非随机分组，却未以准实验框架报告分配限制、选择偏差或因果推断局限。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理顺序，不涉及可逆性/迁移对称性。 |
| C1 | 随机化 | NA | p.4-5 fixed prompts fully crossed; no random allocation mentioned. | 所有模型接受同一固定提示集，无随机分配机制；不是随机化实验。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序，无需平衡。 |
| C3 | 恒定 | 0.5 | p.4: eight specified open-weight models, Huggingface, greedy decoding, A100 GPUs; p.9 Limitations: English only. | 报告了部分恒定控制（模型版本、解码、硬件）并提到语言限制，但未系统列出所有恒定变量及外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配。 |
| C5 | 纳入为变量 | NA | — | 未把已知混淆变量作为协变量或区组纳入模型；随机效应尝试不等同于协变量控制。 |
| C6 | 盲法 | NA | — | 数据采集全自动，无人类被试/评分者盲法。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | p.4 greedy decoding; p.5 independent prompts. | 每个提示独立，无练习块或跨试次学习。 |
| D2 | 疲劳效应 | NA | — | LLM 评估无人类疲劳/休息问题；任务为短提示。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每条件独立提示，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无迁移对称性/交叉设计。 |
| D5 | 范围效应 | NA | — | 因变量为离散正确率，不是主观量表/绝对量值估计。 |
| E1 | 位置 / 顺序偏差 | 0 | p.5 prompts: '...may or has to?'；p.7: 'know, believe or doubt' and '1 know, 2 believe, 3 doubt'；p.16-19 Appendix E fixed option order. | 候选项顺序在所有提示中固定（may 始终在前/编号固定），未随机化或反平衡，未报告位置效应。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 评估无人类被试需求特征/掩饰情节。 |
| E5 | 实验者效应 | NA | — | 全自动数据采集，无人类主试/评分者。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6 Table 1: Qwen2.5-72B Acc 95.3; p.8 Table 2: many Joint Acc 0; p.5/8 figures 95% CI. | 报告了均值、CI，并出现明显高/低端点；但未报告偏度、端点频率或 pilot 难度校准，也未讨论天花板/地板效应。 |
| E7 | 共同方法偏差 | NA | — | 非多构念同源自陈测量；无共同方法偏差检验需求。 |
| F1 | 统计结论效度 | 0.5 | p.20-22 Tables 7-14: b, SE, z, p, R2 Tjur, AIC, Observations; p.5/8 figures 95% CI. | 报告了效应量（R2 Tjur）和部分 CI 图示，但无样本量功效依据、无模型系数 CI、无多重比较校正。 |
| F2 | 内部效度 | 0 | p.6: 'number of parameters has a significant impact on response accuracy'；p.8: medium parameters 'lead to a significant increase'. | 无随机分配、基线等价或流失/内部效度威胁报告，却使用因果性较强的 'impact/lead to' 表述。 |
| F3 | 构念效度 | 0.5 | p.1-2 theoretical framework of epistemic modality; p.3-4 controlled stories; p.9 Limitations: no human participants. | 构念有理论来源并用多模板/多格式操作化，但无正式信度/效度统计或操纵检验；与人类构念的对应主要靠文献对照。 |
| F4 | 外部效度 | 0.5 | p.4: eight open-weight instruction-tuned models listed; p.9 Limitations: English-only, no human participants, multimodal future work. | 报告模型样本与部分边界，但未论证代表性、抽样框或跨情境复现。 |
| G1 | 分析单位 | 0.5 | p.14 Appendix C.1: assessed random intercepts/slopes by LLM, template, item nested within template; AIC dropped all random effects; final simple logistic regression. | 说明了分配/分析层级并检验嵌套结构，但最终仍用简单 logistic 回归，未在模型中分离聚集方差。 |
| G2 | 随机效应 | 1 | p.14 Appendix C.1: 'We assessed random intercepts and random slopes...'；'eventually we fitted simple logistic regression models, without any random effects'. | 明确报告了候选随机效应（LLM、template、item）和最终固定效应模型，随机结构透明度足够。 |
| G3 | 材料作为随机效应 | 0.5 | p.14: by-item random intercepts and slopes considered; none improved AIC; final no random item effect. | 材料/项目被视为可检验的随机因子并做了模型选择，但最终未纳入 item 随机效应，也未用准 F/混合模型合并被试与项目变异。 |
| G4 | 统计功效 | 0 | p.20-22 observations 1800/1440; no power analysis or sample-size justification; p.20-22 R2 Tjur. | 无事前功效分析或样本量论证，未报告系数置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.4 eight models; p.6 and p.8 all DVs/conditions reported; no exclusion or stopping rules stated. | 报告了全部模型和主要因变量/条件，但未说明试次剔除、样本量决定或验证/探索分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement/link in manuscript. | 未见预注册；分析计划未在数据收集前登记。 |
| J1 | 位置偏差 | 0 | p.5 direct/indirect prompts fix 'may or has to' order; p.7 fixes 'know, believe or doubt' order; p.16-19 Appendix E. | 未对候选位置做反平衡/随机化，也未报告交换顺序后的翻转率或位置×正确率。 |
| J2 | 冗长偏差 | NA | — | 任务为单词/编号选择，不涉及开放生成长度与质量比较。 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈/纠错对话操纵。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge 或成对模型评判。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.5: 1-shot stories introduce additional similar narratives with lexical variations; p.16-17 Appendix E full one-shot prompts. | 使用固定 one-shot 示例并给出模板，但未报告示例来源抽样、标签比例、排列反平衡或多 seed 重采样。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5 and p.16-19 Appendix E provide full prompt templates and three QA formats; no prompt version/date or sensitivity ablation beyond formats. | 模板完整、格式敏感性有一定检验，但无版本号、dev/test 划分或语义等价措辞消融。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文为短故事，无长上下文/RAG 设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.4: 'We use greedy decoding for the result'；models accessed via Huggingface; no temperature/seed/repeat N. | 报告了解码策略，但未报 temperature/top-p/seed/模型精确 snapshot，也未做重复采样与 CI 估计。 |
| J9 | 重复与文本退化 | NA | — | 输出为单词/编号选择，不涉及开放生成重复/退化。 |
| J10 | 分词效应 | NA | p.9 Limitations: English-only. | 单语言、单脚本研究，无跨语言分词比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.2 mentions contamination risk in large real-world datasets; p.4 uses 30 ToMi stories; no training cutoff or contamination detection reported. | 使用公开 ToMi 子集和自制模板，但未报告模型训练截止日期、污染检测或污染率。 |
| J12 | 基准饱和 | 0.5 | p.6 Table 1: Qwen2.5-72B 95.3% Acc; p.5/8 figures with 95% CI; no SOTA/saturation discussion. | 报告了分数量程和较高水位，但未讨论基准饱和、连续指标或更难子集。 |
| J13 | 指令遵循 | NA | — | 研究因变量是语义选择正确率，不是指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.5 prompts: 'Please ONLY respond with may or has to as your answer'；p.16-19 same fixed-format instructions; no format-validity rate reported. | 有明确输出格式约束，但未报告格式合法率/解析失败率，也未把格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.3 §3: 'knowledge cannot be directly measured, but can be inferred from observable behavior'；p.8-9 compares LLM behavior to child/adult literature; p.9 Limitations: no human participants tested. | 明确将 LLM 行为作为构念指标并与人类文献对照，但未做同范式人类对照实验；跨模型比较基本按模型类别处理。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | p.6: only small vs medium model categories; no scale curve/emergence claim. | 仅两档模型规模比较，不涉及跨规模涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无代理指标优化/训练/RL/best-of-N 环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4 model names and greedy decoding; p.20-22 observations; p.5/8 figures 95% CI; p.2 code link; no commit hash/seed/paired tests. | 有模型版本、观测数和部分 CI/代码，但 snapshot 不精确、未报告种子/重复次数与配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮提示，无对话历史累积。 |

## 编码小结
研究设计清晰，刺激模板与代码公开，并系统比较了多个模型、故事类型和问答格式；主要不足是选项/位置顺序未平衡，缺少预注册、功效分析、污染检查和精确可复现性信息，且对模型规模差异使用较强因果表述而未充分限定。许多人类被试特有的分配、顺序、疲劳和盲法组件不适用。
