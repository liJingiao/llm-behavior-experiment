# article_180 | The Art of Saying No: Contextual Noncompliance in Language Models | 2024

研究类型概述：数据集/基准构建与 LLM 评测论文，并比较多种训练策略。分析单位为 prompt/query 及模型条件；使用 GPT-3.5 作为 LLM 裁判计算 compliance rate，非人类被试实验。
- **研究构念（Construct）**：情境性拒绝、认识论谨慎、不确定性承认以及过度服从与过度拒绝｜CA 构念锚定：决策（decision making, `trm_4a3fd79d0a038`）；风险寻求（risk seeking, `trm_4a3fd79d0b64e`）；风险规避（risk aversion, `trm_4a3fd79d0b642`）
- **实验任务与范式（Task / Paradigm）**：让多个现成聊天模型回答1,000个不完整、不支持、不确定、安全和人格化请求及其对照请求，并操纵是否加入固定system prompt。（操纵请求类别、请求是否真正需要拒绝及有无要求适当不服从的system prompt，并比较多个现成模型。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p7: “We evaluate using two input formats: one where the model receives only the prompt ..., and another where we provide an additional system prompt”; p8: “we explore four training strategies” (SFT, continued SFT, LoRA, DPO). | 明确命名并报告了输入格式与训练策略等操纵条件及主要水平，但未报告操纵检验，分配/重复方式也不属于经典被试分配，完整性不足。 |
| A2 | 因变量 | 0.5 | p6: “We report compliance rate as our final metric, i.e., the percentage of input prompts that the model directly complies with”; p6: 300 outputs 人工验证，“93% ... accurate ... 63% Fleiss Kappa”. | 因变量指标与计分方式明确，且有裁判与人工一致性证据；但无条目级信度/效度体系、无连续指标预处理或天花板/地板效应说明，故为部分满足。 |
| A3 | 控制变量 | 0.5 | p23 Figure 6: “System Prompt used in all our evaluations”; p33 Appendix D.1 列出训练超参与 A100 设置；p43 checklist: “greedy decoding for generation which is deterministic.” | 报告了若干保持恒定的设置（统一 system prompt、训练超参、硬件、贪心解码），但未系统列出控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p4: “the categories are not exclusive”; p10 Limitations: synthetic data “may be noisy”, taxonomy 未覆盖全部范围, US-specific legality may have bias. | 识别了合成数据噪声、类别覆盖和西方中心 legality 等潜在混淆/局限，但未系统说明控制方式，也未做残余混淆敏感性分析。 |
| A5 | 调节变量 | NA | — | 理论模型与实验设计没有明确调节变量或交互假设，故不适用。 |
| A6 | 中介变量 | NA | — | 理论模型与实验设计没有中介变量或中介效应分解，故不适用。 |
| A7 | 操作性定义 | 1 | p3–p4 对 Incomplete/Indeterminate/Unsupported/Humanizing/Safety 各类给出定义与示例；p24 Table 4 列出 acceptable/unacceptable behaviors；p6 Figure 3 给出 compliance judge prompt；p5 描述 query/response 生成步骤。 | 关键构念（noncompliance 类别、可接受/不可接受行为、compliance rate）均有可观测、可重复执行的操作化说明与模板。 |
| A8 | 水平数与类型 | 0.5 | p7 两种输入格式；p8 四种训练策略；p9 用 10%、25%、50%、75%、100% 的 COCONOT 训练数据；p6 列出多模型族与规模。 | 报告了主要条件的水平数与标签，但未系统说明每个自变量的水平类型、间距/全距或连续变量中心化处理。 |
| A9 | 单一操作化的风险 | 0 | p6 主要评估指标为单一 GPT-3.5-judged compliance rate；p6 有人工验证但不是第二操作化；p10 Limitations 未讨论单一 compliance 指标对推广性的限制。 | 关键构念主要依赖单一 LLM 裁判指标，未见多操作化会聚证据，也未在局限中明确讨论单一操作化限制。 |
| A10 | 单一方法的风险 | NA | — | 非自陈多构念研究；自变量为模型/提示/训练条件，因变量为外部 LLM 裁判评分，不构成典型共同方法偏差设计。 |
| B1 | 被试间设计 | NA | — | 无人类被试间分配；所有模型在固定测试集上评估，同一模型可跨条件/类别，不是被试间设计。 |
| B2 | 被试内设计 | NA | — | 虽然同一模型会接受不同输入格式，但每个 prompt 独立推理，无条件顺序学习或顺序平衡问题，不属于需要顺序平衡的被试内重复测量设计。 |
| B3 | 混合设计 | NA | — | 无组间/组内因素混合的人类实验结构。 |
| B4 | 因子设计 | NA | — | 无经典因子实验设计矩阵，也未进行主效应/交互项的推断统计检验。 |
| B5 | 主效应 | NA | — | 无因子设计主效应推断，故不适用。 |
| B6 | 交互作用 | NA | — | 无因子设计交互项推断，故不适用。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层分配设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序平衡设计。 |
| B9 | 准实验设计 | NA | — | 不是人类准实验设计；模型/训练条件比较不属于该组件定义下的准实验。 |
| B10 | 被试内设计的适用条件 | NA | — | 不涉及被试内处理的不可逆性或迁移对称性判断。 |
| C1 | 随机化 | NA | — | 研究单位（prompt）未随机分配到互斥处理条件；模型评估使用同一固定测试集，无处理分配随机化。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p23 Figure 6: 统一 system prompt；p33 Appendix D.1: 报告 max seq. length 2048、训练超参与 A100 设置；p43: “greedy decoding for generation”. | 报告了部分恒定设置及水平，但未系统讨论这些恒定选择对外部效度的限制。 |
| C4 | 匹配 | NA | — | 未使用匹配/配对分配设计。 |
| C5 | 纳入为变量 | NA | — | 没有将已知混淆变量作为区组或协变量纳入统计模型。 |
| C6 | 盲法 | 0 | p6 Figure 3 的 judge prompt 仅含 Question/Response；p6 人工验证由作者完成；全文未报告盲法类型、施盲对象或盲法成功检验。 | 有 LLM 裁判与人工验证环节，但未报告盲法安排及实施方式。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | LLM 每个 prompt/条件独立推理，无跨试次练习效应或上下文内学习设计。 |
| D2 | 疲劳效应 | NA | — | 无人类 session、休息间隔或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件清洗期或残留迁移设计。 |
| D4 | 不对称迁移 | NA | — | 无迁移对称性检验需求。 |
| D5 | 范围效应 | NA | — | 不使用主观量表或绝对判断范围效应设计。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无多选/多刺激序列呈现；COCONOT 中每个 prompt 单次提交给模型，不涉及选项或刺激顺序随机化。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无默认赞同偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征或掩饰情节问题。 |
| E5 | 实验者效应 | NA | — | 数据采集主要为自动化 LLM 推理与 LLM 裁判，无人类主试期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p7 Table 2 报告大量 compliance rates，contrast set 达 97.4/98.4，多处为 0.0；p40 Table 16 亦有多项接近端点；但未讨论天花板/地板效应或 pilot 难度校准。 | 报告了端点频率/分布信息，但未讨论天花板/地板对内部效度或区分度的影响，也无 pilot 校准说明。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念测量，不涉及共同方法偏差的同源量表问题。 |
| F1 | 统计结论效度 | 0 | p7 Table 2 仅报告 compliance rate 点估计；p6 评估集约 1001 prompts；p43 checklist 明确 “error bars ... [N/A]”。 | 无效应量/置信区间、无多重性校正，样本量也无功效分析依据；主要报告描述性比例。 |
| F2 | 内部效度 | 0 | p8 比较多种训练策略与基线模型；p43 checklist 说明因计算限制不报告 error bars；未报告随机分配、基线等价检验或损耗/flow。 | 存在训练策略效果比较，但未报告随机分配、分配隐藏、基线等价性及多次运行/损耗处理，内部效度控制不足。 |
| F3 | 构念效度 | 0.5 | p6: 300 个输出人工验证，“93% ... 63% Fleiss Kappa”；p5 人工复核评估集；p24 Table 4 给出 judge 标准；但无正式操纵检验。 | 报告了 LLM judge 与人工验证的一致性和评估标准，但缺正式效度证据及操纵检验。 |
| F4 | 外部效度 | 0.5 | p4–p5 描述 COCONOT 数据来源（合成、SituatedQA、WildChats 等）；p6 评测多模型族；p10 Limitations 讨论合成数据、覆盖范围及文化边界。 | 报告了数据来源、模型集合和部分推广边界，但样本非概率抽样，跨情境复现主要限于模型集合，边界讨论不系统。 |
| G1 | 分析单位 | 0.5 | p6: compliance rate 按模型与类别汇总；p5 评估集 1001 条；未说明多层/聚集模型。 | 可看出分析单位为 prompt/类别且按模型聚合，但未明确说明分配层级与统计层级匹配，也未处理 prompt 嵌套于类别的聚集结构。 |
| G2 | 随机效应 | NA | — | 未使用混合模型；模型作为固定比较条件而非从总体抽样的随机效应，故该组件不适用。 |
| G3 | 材料作为随机效应 | 0.5 | p5 使用 1000 条人工验证评估 prompt；p7 Table 2 按类别聚合；p10 Limitations 承认 “dataset may not have covered all of it”。 | 承认 prompt 集覆盖有限，但分析未将 item/prompt 作为随机效应，仅报告类别汇总。 |
| G4 | 统计功效 | NA | — | 研究主要为描述性基准评测和训练策略比较，无预设效应量或推断性功效分析设计。 |
| G5 | 研究者自由度 | 0.5 | p5 报告从约 25K 初始 query、10% 作评估、自动过滤/去重、人工验证后得到 1000 条；p8 报告 10%–100% 训练数据实验；但未区分验证性与探索性分析。 | 报告了部分样本量决定与过滤流程，但剔除数量、全部选择路径及验证/探索分析区分不完整。 |
| G6 | 预先设定 / 预注册 | 0 | p.1–44 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文未报告预注册平台、注册编号或数据分析计划；适用但缺失。 |
| J1 | 位置偏差 | 0 | p6 主评估使用 GPT-3.5 对单条 response 分类；p32 AlpacaEval 使用 GPT-4 成对比较；全文未报告候选项位置交换、正确答案位置随机化或偏好翻转率。 | 主 compliance 评估没有候选项位置问题，但 AlpacaEval 成对偏好存在位置偏差风险且未报告任何反平衡/位置控制。 |
| J2 | 冗长偏差 | 0.5 | p32: “AlpacaEval V2 with length control”；但 p6 的 compliance judge prompt 未含长度控制，全文未报告长度与得分相关系数。 | 对 AlpacaEval 报告了长度控制，但核心 compliance judge 未控制长度偏差，也未报告长度—得分关系。 |
| J3 | 谄媚 | NA | — | 任务为无用户先验立场操纵的静态 query 评估，不涉及谄媚/立场附和测量。 |
| J4 | 自我偏好 | 0 | p6 使用 GPT-3.5 作为 judge；p7 被评模型包括 GPT-4、GPT-3.5 等；未报告裁判与被评模型同源、自我偏好或异源陪审团。 | LLM-as-judge 评估覆盖同家族模型，但未识别或控制自我偏好偏差。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p4: 每个子类约 10 个 seed，并用 “k demonstrations randomly sampled from the pool” 迭代生成；p25 Figure 7 给出 few-shot 生成 prompt；未报告多 seed 重采样或排列反平衡。 | 报告了 few-shot 示例来源与数量，但未报告示例排列反平衡、多个示例集 seed 的均值/方差及模板全文之外的完整控制。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p6 Figure 3、p23 Figure 6、p25 Figure 7、p30 Figure 9/10、p35 Figure 11 等给出多份完整 prompt 模板；但无版本号/迭代日期、敏感性消融或 dev/test 划分说明。 | 公布了完整模板，满足基本要件；但未做语义等价提示敏感性分析，也未说明是否在测试集上调 prompt。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 研究不是长上下文/RAG 实验，上下文长度不是核心操纵变量。 |
| J8 | 温度与采样随机性 | 0 | p43 checklist: “greedy decoding for generation which is deterministic”；p32 Codex-Eval 使用 temperature 0.8；但未报告完整 temperature/top-p/seed，也无重复采样置信区间。 | 仅单次运行且采样超参报告不完整，未估计 LLM 非确定性方差，故未达基本要件。 |
| J9 | 重复与文本退化 | 0.5 | p43 报告使用 greedy decoding；p33 报告 max seq. length 2048；但未报告 n-gram 重复率、退化率或截断比例。 | 报告了解码策略，但缺重复/退化质量控制和生成长度截断统计。 |
| J10 | 分词效应 | NA | — | 研究为英文单语言、单脚本任务，无跨语言/跨脚本分词比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p5 使用 sentence transformers 做训练/评估去重并人工验证；p4–p5 数据部分来自 SituatedQA、WildChats 和合成生成；但未报告测试集发布日期与各模型训练截止日期对照或污染率检测。 | 做了训练—评估去重，降低内部重叠；但未评估模型预训练语料与公开来源数据的污染风险。 |
| J12 | 基准饱和 | 0.5 | p7 Table 2 中 contrast set 分数达 97.4/98.4，多个子项为 0.0；p8 Table 3 也有接近端点分数；未改用连续指标或 bootstrap CI 讨论饱和。 | 报告了基准分数量程与部分端点水位，但未在接近天花板/地板时改用连续指标或 CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究测量 contextual noncompliance，不是指令遵循分数，故该组件不适用。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p6 Figure 3 要求 judge 输出 “<label>CLASS</label>”；p25 Figure 7 要求生成 “python list”；但未报告格式合法率、重试策略及格式失败与内容错误的分开统计。 | 存在结构化格式约束，但缺格式合法率与重试/归一化报告。 |
| J15 | 越狱稳健性 | 0.5 | p8 报告 HarmBench “attack success rate (ASR)”；p4 明确 “we do not include ... jailbreaking” 于评估和训练；p10 将抗越狱列为未来工作。 | 报告了 DirectRequest ASR 与自然安全拒绝指标，但明确未覆盖对抗越狱攻击族，也未并列自然拒绝率与对抗 ASR 的完整对照。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文主要是工程/基准评估与训练方法研究，不主张 LLM 作为心理学被试测量人类同名心理构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽有 Llama/Tulu 不同规模比较，但未报告随规模的能力曲线，也未宣称涌现/突变，故不适用。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | p8 使用 COCONOT 作为训练目标并比较 SFT/LoRA/DPO；p8–p9 同时报告 MMLU、AlpacaEval、HarmBench、XSTest 等 held-out 指标；p9 Figure 4 显示训练数据增加时 contrast set compliance 变化，但无独立人类评估或 overoptimization 双曲线。 | 优化目标与部分评估集分离，并报告了代理训练对多基准的影响；但未用独立 held-out 人类评估监控过优化，也未系统画出代理分数—真实泛化双曲线。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p6 报告模型版本如 “gpt-4-1106-preview”“Llama-2/3”“Tulu-2”等；p43 明确不报告 error bars，采用 greedy decoding；全文无重复次数 N、置信区间或配对检验。 | 有部分模型版本/snapshot 标识，但缺重复运行、CI、配对检验与完整可复现实验日志。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格为单轮 query-response 评估，无多轮对话历史累积，故不适用。 |

## 编码小结
该研究的核心贡献是提出 contextual noncompliance taxonomy、构建 COCONOT 评估/训练资源、评测多个 LLM，并比较 SFT/LoRA/DPO 等训练策略。整体属于 LLM 基准评估与训练方法研究，不是传统人类被试实验；因此大量人类实验设计组件不适用。适用组件中，变量与指标报告较清楚，但采样随机性、提示敏感性、裁判同源、置信区间/重复运行及预注册等 LLM 评估特有质量控制报告不充分。
