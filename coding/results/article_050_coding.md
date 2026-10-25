# article_050 | Can LLMs Ground when they (Don’t) Know: A Study on Direct and Loaded Political Questions | 2025

研究类型概述：这是一项 LLM 行为评测/基准研究，而非人类被试实验。作者用三类问题（确认性直接问题、否定性直接问题、含虚假预设的 loaded question）考察 GPT-4-o、Mistral-7B-v03 和 Llama-3-8B 三个指令微调模型在德国政党政治事实上的知识、预设拒绝与“grounding”行为；每个 prompt 采样 3 次，loaded 回答由 7 名标注者按 accommodated/rejected/imprecise 分类，并以直接问题正确数划分 belief groups、计算 grounding score。分析主要为描述性比例、分组分布和模型/党派比较，无形式化推断统计、随机分配、功效分析或预注册。
- **研究构念（Construct）**：对话共同基础建构、面子迎合与预设虚假信息拒绝（conversational grounding, face-saving/agreement, and misinformation rejection）｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：这是一项 LLM 行为评测/基准研究，而非人类被试实验。作者用三类问题（确认性直接问题、否定性直接问题、含虚假预设的 loaded question）考察 GPT-4-o、Mistral-7B-v03 和 Llama-3-8B 三个指令微调模型在德国政党政治事实上的知识、预设拒绝与“grounding”行为；每个 prompt 采样 3 次，loaded 回答由 7 名标注者按 accommodated/rejected/imprecise 分类，并以直接问题正确数划分 belief groups、计算 grounding score。分析主要为描述性比例、分组分布和模型/党派比较，无形式化推断统计、随机分配、功效分析或预注册。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.4: 'we embedded the claims into direct questions ... and ... loaded questions ... resulted in 882 loaded, 147 disconfirmatory, and 147 confirmatory direct questions.' p.4: 'We sampled 3 responses from 3 models for each prompt.' | 问题类型（conf./disconf./loaded）被明确命名并给出水平与示例，基本要件达成；但未报告操纵检验，且所有 prompt 均发给各模型，分配/随机化程序不清，故为 0.5。 |
| A2 | 因变量 | 0.5 | p.5: 'Misinformation Accommodated ... Misinformation Rejected ... Imprecise Answer'; p.6: 'Accommodation (0), Rejection (2), Imprecise (1). These values are summed ... grounding score can range from 0 to 6'; p.5: 'Fleiss’ κ (0.82) and the average pairwise Cohen’s κ (0.72).' | 因变量指标、计分和标注信度已报告；但缺少效度证据、连续指标预处理或天花板/地板效应处理说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p.4: 'We refrain from prompt engineering'; p.5: 'We evaluated three instruction-tuned models: ... GPT-4-o ... Mistral-7B-v03 ... Llama-3-8B.' | 固定模型、固定数据源、统一极性问题形式和无 prompt engineering 可视为部分控制；但未系统列出控制变量清单，也未报告 temperature、解码等控制手段，故为 0.5。 |
| A4 | 混淆变量 | 0.5 | p.10: 'Missing knowledge due to knowledge cut-offs'; 'Political spectrum imbalance'; p.8-9 discusses political bias and face-saving as alternative explanations. | 识别并讨论了知识水平、党派偏见、知识截止和 face-saving 等潜在混淆，并作分组描述分析；但没有正式控制或敏感性分析来估计残余混淆，故为 0.5。 |
| A5 | 调节变量 | 0 | p.7: 'Does LLMs’ Knowledge Change Grounding Behaviour?' and p.8: 'Impact of Party'; 结果以分组分布/百分比呈现（Figure 2, Table 8），无交互项检验。 | 论文提出知识水平/党派是否改变 grounding 的问题，但没有乘积项交互检验、中心化/标准化或简单斜率分析；按规则提出调节问题却无交互检验记 0。 |
| A6 | 中介变量 | NA | — | 不适用：论文没有中介变量、直接/间接效应分解或中介模型。 |
| A7 | 操作性定义 | 1 | p.4 gives exact question patterns; p.5 defines annotation categories; p.6 defines belief groups and grounding-score calculation; pp.16-18 provide annotation guidelines with examples. | 关键构念（问题类型、知识、grounding）均有可复现的 prompt 构造、标注规则和计分程序，达到 1。 |
| A8 | 水平数与类型 | 0.5 | p.4 lists three question types and counts; p.5 lists three models; p.4 four parties; p.6 four belief groups. | 各因素水平和标签已报告；但未系统说明水平类型、编码间距/全距或连续化处理，故为 0.5。 |
| A9 | 单一操作化的风险 | 0.5 | p.10: 'The annotation process could be refined ... varying levels of certainty ... were not captured ... category of imprecise responses was heterogeneous.' | grounding 主要依赖单一标注方案，未报告多操作化会聚证据；作者在局限中讨论了标注操作化的限制，故为 0.5。 |
| A10 | 单一方法的风险 | NA | — | 不适用：研究对象为 LLM 输出与人工标注，不是人类自陈式多构念同源测量；共同方法偏差量表检验不适用。 |
| B1 | 被试间设计 | NA | — | 不适用：无人类被试分配到互斥条件；每个模型接受同一组 prompt，不存在人类被试间设计。 |
| B2 | 被试内设计 | NA | — | 不适用：没有人类被试内重复测量或条件顺序平衡；LLM 调用被视为独立提示，而非带顺序的反平衡被试内设计。 |
| B3 | 混合设计 | NA | — | 不适用：没有组间/组内人类因素混合设计及对应误差项。 |
| B4 | 因子设计 | 0 | p.7 Table 2/Table 3 and p.20 Tables 7-8 present model、question type、party 的描述性分解，但无完整设计矩阵、每格样本量及交互统计。 | 存在多因素描述性比较结构，但未报告交互项检验或因子模型；按因子设计要求记 0。 |
| B5 | 主效应 | 0 | p.7 Table 2/3 报告模型间百分比差异，但无主效应 F/df/p/效应量。 | 只报告描述性百分比，没有形式化主效应统计检验；记 0。 |
| B6 | 交互作用 | 0 | p.7-8 比较 belief groups、party 和 question type，但无交互项 F/df/p、简单主效应或多重比较校正。 | 未做交互作用统计检验，也未报告简单效应；记 0。 |
| B7 | 区组设计 | NA | — | 不适用：没有区组变量、分层随机或区内分配程序。 |
| B8 | 拉丁方 | NA | — | 不适用：没有拉丁方顺序设计或需要平衡的被试内条件顺序。 |
| B9 | 准实验设计 | NA | — | 不适用：不是人类准实验设计；固定 LLM 和 prompt 的基准评测不涉及非随机分组因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 不适用：没有人类被试内处理，因而无需论证处理可逆性或迁移对称性。 |
| C1 | 随机化 | NA | — | 不适用：没有把研究单位随机分配到互斥条件；所有模型面对同一 prompt 集，无分配隐藏或随机化程序。 |
| C2 | 平衡 | NA | — | 不适用：无被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p.5: fixed models GPT-4-o, Mistral-7B-v03, Llama-3-8B; p.10: 'the study was limited to the German language and political context.' | 模型版本、语言和政治语境可视为部分恒定变量，并在局限中讨论德语语境限制；但没有系统列出温度、解码、接口等恒定水平，故为 0.5。 |
| C4 | 匹配 | NA | — | 不适用：没有匹配变量、配对分配或倾向得分匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.6: 'Based on the number of correct model responses to the direct questions ... we categorize each loaded question into ... belief groups'; p.7 analyzes grounding by belief group. | 知识水平通过 direct questions 测量并作为 belief group 纳入描述分析，基本可视为纳入重要混淆变量；但未做协变量调整、斜率齐性检验或效应量报告，故为 0.5。 |
| C6 | 盲法 | 0 | p.5: 'We asked seven annotators, including the authors, to evaluate the models’ responses'; no blinding procedure reported. | 存在人工标注者，但未报告对模型身份/条件的盲法安排或盲法成功检验；可盲却未报告，记 0。 |
| C7 | 平衡的层级 | NA | — | 不适用：无被试内条件顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 不适用：LLM 每个 prompt 独立调用，无练习块或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 不适用：无人类 session 时长、休息或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不适用：独立 prompt/API 调用，无跨条件残留或清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 不适用：没有跨条件迁移或不对称迁移设计。 |
| D5 | 范围效应 | NA | — | 不适用：因变量为类别标注和正确率，不是主观量表绝对判断。 |
| E1 | 位置 / 顺序偏差 | NA | — | 不适用：无多选项位置、刺激序列或需要反平衡的被试内处理顺序；prompt 独立呈现。 |
| E2 | 默认赞同 | NA | — | 不适用：未使用 Likert/态度自评量表，无反向计分题问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不适用：无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 不适用：LLM 无人类被试需求特征；标注任务也不涉及人类被试对研究假设的推断。 |
| E5 | 实验者效应 | 0 | p.5: 'seven annotators, including the authors'; annotation guidelines in pp.16-18, but no blind arrangement reported. | 报告了标注者人数和标注指南，但未说明评分者是否知晓模型/条件，也无盲法层级和成功检验；记 0。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.6: grounding score range 0-6; p.7 Figure 2 and Table 8 show many extreme scores 0 or 6; no pilot difficulty calibration reported. | 报告了分数范围、分组分布和端点频率，可排查地板/天花板；但未报告 SD/偏度或 pilot 难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 不适用：不是人类多构念自陈量表，不存在同源自评共同方法偏差。 |
| F1 | 统计结论效度 | NA | — | 不适用：结果主要是描述性百分比和分布，没有推断统计、p 值、效应量或 CI；按规则记 NA。 |
| F2 | 内部效度 | NA | — | 不适用：固定模型和 prompt 的观察性基准评测，无随机分配、基线等价检验或被试流向，也不作严格因果推断。 |
| F3 | 构念效度 | 0.5 | p.5 reports Fleiss’ κ=0.82 and average pairwise Cohen’s κ=0.72; p.4-p.6 provide operational definitions, but no validity evidence or manipulation check. | 报告了标注信度与操作化，但缺少效度证据和操纵检验，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.5 lists three models; p.10 discusses German-language and political-spectrum limitations and need for future cross-language studies. | 报告了模型样本和若干推广边界，但无跨样本/跨情境复现，也未系统论证代表性，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p.4: 'We sampled 3 responses from 3 models for each prompt, yielding 2646 data points'; p.6 computes scores per question answer set. | 报告了 prompt/model 和 response 的层级，并说明每个 prompt 有 3 个回答；但分析以 response 百分比为主，未用多层模型处理 response 嵌套于 prompt 的聚集结构，故为 0.5。 |
| G2 | 随机效应 | NA | — | 不适用：没有拟合混合模型或随机效应模型；三个模型是固定的比较目标，不涉及从模型总体抽样的随机效应结构。 |
| G3 | 材料作为随机效应 | 0 | p.4: data consist of '38 political claims' and four parties; analyses aggregate by model/party, without item random effect or F′. | 材料/项目被当作固定刺激集，未将 claims 或 factive verbs 作为随机项目因子；结论却泛化到政治问题与 LLM grounding，记 0。 |
| G4 | 统计功效 | 0 | p.4 reports counts of prompts and 3 responses, but no a priori power analysis, effect-size target, or sample-size justification. | 没有事前功效分析或样本量论证，也未报告效应量/CI；虽为探索性基准，但按 G4 基本要件未达，记 0。 |
| G5 | 研究者自由度 | 0.5 | p.5: BLOOMZ excluded 'due to poor response quality'; p.10: 'responses to true presuppositions were collected, but they were not analyzed.' | 披露了模型排除和未分析的数据类型，部分满足透明度；但没有完整剔除/停止规则，也未明确区分验证性与探索性分析，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–21 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 没有预注册平台、编号或时间戳；未登记假设、样本规则、排除规则和分析计划；记 0。 |
| J1 | 位置偏差 | NA | — | 不适用：不涉及 LLM-as-judge、候选项排序或多选位置反平衡。 |
| J2 | 冗长偏差 | NA | — | 不适用：不使用 LLM 裁判评价生成质量，也不以长度作为评分依据；标注为人工类别判断。 |
| J3 | 谄媚 | 0.5 | p.4 contrasts confirmatory and disconfirmatory direct questions and loaded false-presupposition questions; p.7-8 reports confirmatory vs disconfirmatory accuracy and accommodation/rejection. | 通过虚假预设和问题极性操纵了用户先验立场并报告接受/拒绝率，触及 face-saving/sycophancy 风险；但未以 sycophancy 框架报告同一问题的翻转率，未区分 feedback/answer sycophancy，也未报告 RLHF/SFT 阶段，故为 0.5。 |
| J4 | 自我偏好 | NA | — | 不适用：没有 LLM-as-judge 或同源模型自评。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 不适用：没有 few-shot in-context examples；prompt 为 zero-shot 直接问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.4 gives prompt patterns for direct/loaded questions; pp.14-15 give examples; no prompt versioning, sensitivity ablation, or dev/test split reported. | 提供了 prompt 模板模式和示例，但无版本号、语义等价改写消融或 dev/test 划分说明，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不适用：问题很短，无长上下文、RAG 或关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0 | p.4: 'We sampled 3 responses'; p.5 lists model names, but no temperature, top-p, seed, or API snapshot date. | 报告了重复次数，但未报告任何采样超参（至少 temperature）或 seed；无 CI/方差估计，记 0。 |
| J9 | 重复与文本退化 | 0 | p.5: 'The models’ responses were often lengthy and complex'; no decoding strategy, repetition penalty, or degeneration rate reported. | 任务涉及开放生成，但未报告 greedy/beam/sampling、repetition penalty 或重复/退化率，记 0。 |
| J10 | 分词效应 | NA | — | 不适用：单语言德语、单脚本研究，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.10: 'The models used were released between April ... and May 2024 ... whereas the statements ... are based on party positions for the European Parliament election on June 9, 2024.' | 对照了模型发布/知识截止与数据时间，并讨论潜在时间错配；但未做污染检测、重叠率或 held-out 验证，故为 0.5。 |
| J12 | 基准饱和 | NA | — | 不适用：使用新构建的 FLEX political benchmark，并非接近饱和的公开基准；论文也未作 SOTA 饱和比较。 |
| J13 | 指令遵循 | NA | — | 不适用：因变量是知识正确性与 grounding 标注，不是指令遵循准确率。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不适用：不要求结构化/JSON 输出，也无格式合法率问题。 |
| J15 | 越狱稳健性 | NA | — | 不适用：研究不涉及越狱或安全对齐攻击评估；虽涉及政治虚假信息，但不是 jailbreak ASR 设计。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2 discusses human common ground and conversational grounding; p.8-9: 'partial alignment with human face-saving behavior'; p.5 lists model names but no human comparison data. | 明确把 LLM 行为放在人类 grounding/face-saving 理论下讨论，并比较模型间差异；但没有人类同范式对照实验，也未系统论证 LLM 构念与人类构念的异同，故为 0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不适用：不涉及随模型规模/训练进展的能力曲线或涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 不适用：无训练、RL、best-of-N 或对代理指标的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.4: 3 responses per prompt; p.5 lists model names; no precise API snapshot, confidence intervals, paired tests, or raw logs reported. | 报告了重复次数 N 和模型名称，基本满足可复现起点；但无 CI、配对检验和精确 snapshot/API 日期，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 不适用：研究使用单轮 prompt，无对话历史累积或多轮一致性衰减评估。 |

## 编码小结
研究问题清晰，操作性定义和标注流程较透明，报告了标注者间信度，且对政治偏见、知识截止和党派不对称等局限有所讨论。但该研究本质上是固定 prompt 集上的 LLM 行为观察与人工标注评测：缺少正式实验随机化、操纵检验、推断统计与效应量/CI，采样参数和解码设置未报告，材料与 prompt 的项目层面随机效应未建模，且部分数据（true presupposition 回答）收集后未分析。总体适合作为 LLM grounding 的探索性基准，但不能按严格心理实验的内部/统计效度标准解读。
