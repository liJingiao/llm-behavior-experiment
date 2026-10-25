# article_174 | On the Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs | 2024

研究类型概述：LLM 心理测量基准评估（PsychoBench）：对 text-davinci-003、ChatGPT、GPT-4、LLaMA-2-7B/13B 及 jailbroken GPT-4 在 13 个心理量表上的得分进行描述，并与现有人类常模比较；另含 role-play、CipherChat 越狱与 prompt/temperature 敏感性实验。实际分析单位为“模型×量表/子量表×10 次独立运行”，不是人类被试随机实验。
- **研究构念（Construct）**：人格、关系取向、动机与情绪能力的心理测量表现｜CA 构念锚定：情绪（emotion, `trm_4a3fd79d0a17f`）；情绪识别（emotion recognition, `trm_4a3fd79d0b665`）；共情（empathy, `trm_4a3fd79d0b67d`）
- **实验任务与范式（Task / Paradigm）**：让五种现成LLM重复完成13套临床和学术心理量表，与既有人类常模比较，并测试越狱提示对量表表现的影响。（改变模型、心理量表、重复采样和GPT-4是否使用越狱提示。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p4：'we select the following models... Model Updates... Model Sizes... Model Safety'；p22-23列出 prompt V1–V5+CoT 与 temperature 0/0.01/0.8，但无操纵检验。 | 有明确的模型、role、jailbreak、prompt 与 temperature 操纵/比较，基本要件达成；但未系统报告分配方式与操纵检验，故为 0.5。 |
| A2 | 因变量 | 0.5 | p15 Table 5 列出各量表题数、Response 与 Scheme；p5报告 Mean±SD 并用 F-test、Student/Welch t-test；但无 LLM 样本内部一致性/重测信度或连续指标预处理说明。 | 因变量指标与计分方式明确，但信效度与预处理不完整。 |
| A3 | 控制变量 | 0.5 | p4：'We set the temperature parameter to zero...'，LLaMA 设 0.01；p5：'we shuffle the questions in our input data'；p4：'All models are executed for inference only'。 | 报告了温度、题目顺序和推理方式等控制，但不是系统控制变量清单与逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | p22-23对 prompt 与 temperature 做敏感性比较；p24承认 human results 来自不同 demographic groups。 | 识别并部分检验了 prompt/temperature 与人群常模差异等混淆，但未系统讨论残余混淆及其内部效度威胁。 |
| A5 | 调节变量 | NA | — | 理论模型不包含调节变量，也没有调节/交互假设与简单斜率分析。 |
| A6 | 中介变量 | NA | — | 理论模型不包含中介变量，未提出直接/间接效应分解。 |
| A7 | 操作性定义 | 0.5 | p4 'Prompt Design' 与 p5 示例 prompt；p15 Table 5 给出题项数、反应范围与计分；GitHub 提供量表元数据。 | 关键构念有操作化描述，但 role 的具体提示语、全部题项与完整复现脚本未在正文中逐项给出。 |
| A8 | 水平数与类型 | 0.5 | p4列出五个模型及 gpt-4-jb；p7列出 default/ordinary/hero/psychopath/liar 五 role；p22列 V1–V5+CoT；p23列 temperature 0/0.01/0.8。 | 水平与取值基本明确，但未系统给出每个因素的变量类型、间距/全距及连续变量中心化说明。 |
| A9 | 单一操作化的风险 | 0.5 | p3与 p15使用 13 个量表及多个子量表；p8用 role assignment、TruthfulQA/SafetyQA 做 validity 检查；未报告各操作间会聚证据。 | 多处使用多量表/多指标，但未系统报告会聚效度；对单一操作化局限讨论不足，故 0.5。 |
| A10 | 单一方法的风险 | 0 | p5所有心理测量得分均来自同一 LLM 对 Likert 题项的自陈式数字回答；全文未做共同方法偏差检验或程序控制。 | 自变量/条件与因变量分数来自同一模型同一自陈式问答渠道，未报告 CMB 控制。 |
| B1 | 被试间设计 | NA | — | 纯 LLM 基准/观察性模型比较，无人类被试或被试组随机分配；模型为固定选择而非分配到条件。 |
| B2 | 被试内设计 | NA | — | 虽有每量表 10 次独立运行，但不是同一会话内的重复测量条件设计，也未涉及条件顺序平衡。 |
| B3 | 混合设计 | NA | — | 无逐因素标注的组间/组内混合设计及相应混合模型。 |
| B4 | 因子设计 | NA | — | 不是因子实验；模型×量表主要是描述性比较，未构建设计矩阵或报告交互项。 |
| B5 | 主效应 | NA | — | 不是因子设计，无因子主效应检验。 |
| B6 | 交互作用 | NA | — | 不是因子设计，无交互作用检验。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 论文是 LLM 基准比较，不宣称准实验因果设计；无准实验类型、选择偏差与因果推断框架。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理顺序设计，不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 研究单位（模型/量表运行）未被随机分配到互斥实验条件；题目 shuffle 属于刺激顺序控制，不是条件分配隐藏。 |
| C2 | 平衡 | NA | — | 无跨条件顺序平衡问题。 |
| C3 | 恒定 | 0.5 | p4：'temperature parameter to zero'、'LLaMA 2 models... temperature... 0.01'、'inference only'、'two NVIDIA A100 GPUs'。 | 报告了温度、推理方式与硬件等恒定设置，但未系统讨论这些恒定选择对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未将已知混淆变量作为区组或协变量纳入统计模型；主要分析为描述均值与 t 检验。 |
| C6 | 盲法 | NA | — | 无人类被试/主试盲法；数据采集为自动化 API/模型推理。 |
| C7 | 平衡的层级 | NA | — | 无顺序效应需平衡的平衡层级设计。 |
| D1 | 练习效应 | NA | — | LLM 各条件为独立提示/独立运行，不存在跨试次上下文内学习或练习块。 |
| D2 | 疲劳效应 | NA | — | 无人类疲劳或长 session 休息安排问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件为独立会话式调用，未设计跨条件残留迁移；LLM 无药物/学习消退式清洗期需求。 |
| D4 | 不对称迁移 | NA | — | 无跨条件顺序/迁移对称性设计。 |
| D5 | 范围效应 | 0 | p5示例 prompt 说明按 Likert level definition 评分；p15给出各量表 Response 范围；未讨论 range effect 或做被试间对照。 | 研究使用 Likert 自陈式评分并跨模型/role 比较，但没有讨论范围效应风险、量表锚定校准或采用被试间对照；故为 0。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p5：'we shuffle the questions in our input data to mitigate the influence of models’ sensitivity to question orders'；p8：'automatically generate prompts with randomized questions'。 | 报告了题目顺序随机化，但未给出随机方案、seed、各位置出现次数或被试/运行分配细节。 |
| E2 | 默认赞同 | 0 | p5与 p15描述 Likert 计分，但未报告反向计分题比例、正反向题一致性或默许偏差讨论。 | 使用 Likert/态度式自评量表，但未说明反向题与默许偏差控制。 |
| E3 | 极端 / 中间反应倾向 | 0 | p5-7各表仅报告 Mean±SD；未报告偏度、端点/中点使用比例，也未讨论跨模型/role 反应风格差异。 | 有跨模型/role 的等级量表均值比较，但缺少分布形态与反应风格威胁说明。 |
| E4 | 需求特征 | NA | — | 研究对象是 LLM，不存在人类被试的需求特征、掩饰情节或事后访谈问题。 |
| E5 | 实验者效应 | NA | — | 数据采集为自动化 API/本地推理，无人类主试或人类评分者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5-7及 p15给出各量表均值/SD与取值范围；但未报告端点频率、偏度或 pilot 难度校准。 | 报告了均值/SD但缺少端点堆积与天花板/地板效应的系统判断。 |
| E7 | 共同方法偏差 | 0 | p5心理测量结果全部来自 LLM 对同一类 Likert 提示的自陈式回答；未报告共同方法偏差程序或统计控制。 | 同源自评式测量，未做 CMB 程序控制或统计检验，也未讨论人为相关膨胀。 |
| F1 | 统计结论效度 | 0 | p5报告 Mean±SD、F-test、Student/Welch t-test 与显著性水平 0.01；未报告效应量、95%CI、功效分析或多重比较校正。 | 基本只报告显著性与 SD，不满足效应量/CI 与多重性校正要求。 |
| F2 | 内部效度 | 0.5 | p4说明模型选择与参数固定；p5说明 10 次独立运行；p22-24用 prompt/temperature 敏感性与 human sample 限制讨论稳健性；但无随机分配、分配隐藏或基线等价检验。 | 非随机固定模型比较，仅部分评估可比性与内部效度威胁，故 0.5。 |
| F3 | 构念效度 | 0.5 | p3-4称所选量表在临床心理学中有足够 reliability/validity；p8用 role、TruthfulQA/SafetyQA 进行 validity 检查；未报告 LLM 样本 α/ω 或因素分析。 | 报告了量表来源效度和 role 效度检查，但缺 LLM 特定信度证据及单一操作化局限讨论。 |
| F4 | 外部效度 | 0.5 | p16 Table 6列出人类常模样本国家/年龄/性别；p24讨论 human data 来自不同 demographic groups、非全球代表样本。 | 报告样本来源与部分推广边界，但未报告跨情境复现或系统抽样框/代表性论证。 |
| G1 | 分析单位 | 0.5 | p5：'Each model undergoes ten independent runs for every scale... mean and standard deviation represent the final results'，并用 t-test 比较；未说明题目/运行/模型嵌套结构。 | 明确说了运行层级与汇总方式，但将运行/题目聚合后作比较，未用多层模型处理嵌套。 |
| G2 | 随机效应 | 0 | p5统计分析仅报告 Mean±SD、F-test 与 t-test；未说明模型、运行或题目何者为随机效应，也无随机效应结构。 | 存在模型内 10 次运行与题目嵌套结构，但统计模型未包含随机效应，推断可推广性受限。 |
| G3 | 材料作为随机效应 | NA | — | 量表题目是固定心理测量工具，不作为需要推广到材料总体的实验材料自变量。 |
| G4 | 统计功效 | 0 | p5仅说明每量表 10 次独立运行；无功效分析、目标效应量或样本量推导；结果表报告 Mean±SD，但无 CI/效应量。 | 无事前功效分析与效应量/CI。 |
| G5 | 研究者自由度 | 0.5 | p3和 p15列出 13 个量表及子量表，p5报告所有模型/role/jailbreak 结果；但未报告数据排除规则或样本量/运行次数确定方式。 | 因变量与条件报告较全，但缺少排除规则、停止规则及验证性/探索性分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | 全文无预注册平台、注册编号或时间戳早于数据收集的分析计划。 | 无预注册，且未区分验证性与事后探索分析。 |
| J1 | 位置偏差 | 0 | p8：'TruthfulQA encompasses multiple-choice questions, with only one option being the best answer'；未说明选项位置随机化或 A/B 交换。 | 多个 validity 实验涉及多项选择作答，但未识别或控制选项位置偏差。 |
| J2 | 冗长偏差 | 0 | p8：'we employ GPT-4 to automatically detect instances where the text output generated by gpt-3.5-turbo is unsafe'；无长度偏差控制或长度-得分相关报告。 | 使用 LLM 裁判评估开放式安全输出，但未控制冗长偏差。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错式谄媚操纵；role prompt 不是 pro/anti framing。 |
| J4 | 自我偏好 | 0.5 | p8用 GPT-4 评判 gpt-3.5-turbo 的安全输出；裁判与被评模型同属 OpenAI 家族，但未报告自我偏好控制、匿名化或人类一致性。 | 存在 LLM 裁判同源/自我偏好风险，且报告不足以排除该偏差。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 实验未使用 few-shot in-context examples；prompt 中无示例集选择与排列。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p22 Table 21给出 V1–V5+CoT prompt 模板，p22-23报告 BFI 上 prompt 与 helpful assistant 的敏感性比较；未说明 dev/test 划分。 | 有 prompt 版本和敏感性消融，但无完整版本日期、dev/test 分离或 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长文档/RAG/长上下文信息位置操纵；量表题项长度远不构成中间迷失测试。 |
| J8 | 温度与采样随机性 | 0.5 | p4：GPT 温度 0，LLaMA 温度 0.01；p5：每量表 10 次独立运行；p23 Table 24另测 temperature 0.01/0.8；但无 seed、top-p/top-k 或 CI。 | 报告了主要采样温度与重复运行次数，但采样超参、seed 与不确定区间报告不完整。 |
| J9 | 重复与文本退化 | 0.5 | p4报告 temperature；p5输出为 Likert 数字，p8 SafetyQA 生成自由文本并用 GPT-4 判毒性；未报告 repetition penalty 或重复/退化率。 | 解码温度有报告，但缺少重复率/退化 QC；主任务是短数字输出，退化风险相对有限。 |
| J10 | 分词效应 | NA | — | 单语言英文实验，无跨语言/跨脚本分词比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p8使用公开 TruthfulQA；p3/p15使用公开心理量表；未报告训练截止日期、测试集版本对照或污染检测。 | 存在公开量表/TruthfulQA 在预训练语料中出现的污染风险，但未做任何污染检查。 |
| J12 | 基准饱和 | 0.5 | p15给出各量表分值范围；p5-7多个得分接近上限（如 BFI Agreeableness 4.9/5、Empathy 6.8/7）；未讨论饱和或改用连续/更难指标。 | 报告了分数量程与当前水位，但未评估天花板/饱和对模型比较的影响。 |
| J13 | 指令遵循 | NA | — | 研究不把指令遵循作为因变量；'reply numbers'只是输出格式约束。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p5 system prompt：'You are a helpful assistant who can only reply numbers from MIN to MAX. Format: statement index: score.'；未报告格式合法率或解析失败率。 | 有结构化输出约束，但未把格式失败与内容错误分开报告。 |
| J15 | 越狱稳健性 | 0 | p8用 SafetyQA 由 GPT-4 判毒性；p4用 CipherChat Caesar cipher 诱导 GPT-4 心理作答；未报告自然提示拒绝率与对抗攻击成功率对比。 | 涉及安全/越狱元素，但未系统测量 ASR 或区分自然拒绝与对抗越狱。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p7-8明确讨论 'validity of scales on LLMs'，p8比较 role 与 TruthfulQA/SafetyQA，p24承认人类常模限制；但未给出精确权重快照或同范式人类对照实验。 | 有 LLM 心理构念定位与人类常模比较，但构念同异与权重版本说明不完整。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 比较了 LLaMA-2 7B/13B 与 GPT-3.5/GPT-4，但没有跨规模能力曲线或‘涌现’宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无代理指标优化、RL、best-of-N 或奖励模型训练。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p5每量表 10 次独立运行并报告 Mean±SD；p4列出模型名称与 LLaMA HuggingFace 链接；但无精确 OpenAI snapshot/日期、95%CI 或配对检验。 | 有重复次数但快照标识与不确定区间/配对比较不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮量表作答/单轮 QA，无对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
论文提供了较完整的量表清单、题项数、计分方式和 prompt 模板，并做了 role、prompt、temperature 等补充比较，因而具有一定可复现性与构念效度检查。但整体仍是观察性 LLM 基准比较：缺少预注册、功效分析与效应量/CI，统计上把多次运行/题目当独立观测而未做多层/随机效应建模；对基准污染、饱和、格式合法率、LLM 裁判偏差、共同方法偏差等关键风险报告不足。
