# article_121 | Human-like object concept representations emerge naturally in multimodal large language models | 2025

研究类型概述：观察性/比较性计算认知科学研究：让 LLM/MLLM 完成 odd-one-out 相似性判断并学习 SPoSE 低维嵌入，再与人类行为相似性和 NSD fMRI 表征做 RSA 比较；不是随机分组实验。分析单位主要是模型行为/对象/试次以及 fMRI 被试/ROI/体素。
- **研究构念（Construct）**：自然物体概念表征、类别组织与人机概念空间相似性｜CA 构念锚定：语义记忆（semantic memory, `trm_4a3fd79d0b083`）；语义加工（semantic processing, `trm_4a3fd79d0b87a`）
- **实验任务与范式（Task / Paradigm）**：向现成ChatGPT-3.5 Turbo提供自然物体的名称与简短文本描述，让模型在约470万组三元组中选择异类，并把选择结构与人类异类判断得到的概念空间比较。（系统改变物体三元组与语义类别，比较文本LLM、人类和多模态模型的异类判断及其低维表征。）｜CA 任务锚定：语义判断任务（semantic decision task, `trm_4f240cb09f8e5`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | p13: 'The prompt structure used was standardized...'；p12: 研究比较 ChatGPT-3.5 与 Gemini Pro Vision 等模型，而非操纵实验条件。 | 没有主动操纵的自变量；模型/提示比较是观察性比较，补充中的引导提示只是示例，不是正式水平。 |
| A2 | 因变量 | 1 | p2: '4.7 million triplet similarity judgments ... 1,854 unique objects'；p5: 'accuracies were 56.7% ... chance = 33.3% ... noise ceilings'；p14: SPoSE objective；p15: split-half reliability normalization。 | 因变量指标（判断选择概率、SPoSE 维度、RSA r、分类准确率）与计分方式明确；报告重复性、split-half、held-out 预测和噪声天花板等信效度/边界信息。 |
| A3 | 控制变量 | 0.5 | p13: 'temperature ... set to 0.01'；p13: MLLM images '512 x 512 pixels'；p13: 使用统一 prompt。 | 报告了若干实际恒定控制（温度、图像尺寸、prompt），但未系统列出控制变量清单及逐项控制手段。 |
| A4 | 混淆变量 | 0.5 | p12: 'focus on ChatGPT-3.5 and Gemini Pro Vision (v1.0)' 与 'impact of varying language prompts'；p12: object-level vs image-level annotations。 | 识别了模型覆盖、提示差异、注释粒度等潜在混淆，但未系统控制或做残余混淆的敏感性分析。 |
| A5 | 调节变量 | NA | — | 理论模型与结果分析不包含调节变量或交互检验。 |
| A6 | 中介变量 | NA | — | 不包含中介变量或间接效应分解。 |
| A7 | 操作性定义 | 1 | p13: 给出 LLM/MLLM odd-one-out prompt 与解析规则；p14: 给出 SPoSE 嵌入、目标函数、优化与剪枝流程；p15: 给出 RSA、searchlight 与 voxel-wise encoding 程序。 | 关键构念均有可重复的操作化：odd-one-out 选择概率、SPoSE 嵌入、RSA 相关、fMRI 编码。 |
| A8 | 水平数与类型 | NA | — | 没有需要报告水平数与间距的操纵自变量；模型比较是观察性分组。 |
| A9 | 单一操作化的风险 | 1 | p5: 比较 SPoSE 嵌入与原始特征的 odd-one-out 预测；p5 Fig.2j: behavioral RSM 与 cosine RSM 相关；p11: 模型嵌入与脑活动对齐。 | 关键构念采用多种操作化并报告会聚证据，且用 held-out 行为与脑数据验证。 |
| A10 | 单一方法的风险 | 1 | p5: 'behavioral judgment method aligned better with human-derived RSM than the cosine distance method'；p11: 'link LLMs’ embeddings with brain responses'。 | 研究使用行为判断、模型原始特征、fMRI/RSA 等多方法来源，明确说明来源差异，不需要同源自评式 CMB 检验。 |
| B1 | 被试间设计 | NA | — | 无人类被试或 LLM 试次被随机分配到互斥实验条件的被试间设计。 |
| B2 | 被试内设计 | NA | — | 无被试内条件顺序设计；同一模型面对不同对象/三元组不是实验条件重复测量。 |
| B3 | 混合设计 | NA | — | 无组间/组内因素混合设计。 |
| B4 | 因子设计 | NA | — | 不是多因素完全交叉的因子实验；模型、类别、对象不是本研究的因子设计结构。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应检验。 |
| B6 | 交互作用 | NA | — | 无交互项检验或简单主效应分析。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层随机设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序平衡。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理研究；人类数据为既有数据集，LLM 数据为 API 行为采集，无因果处理分配。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | p13: 'we gathered all human-used similarity judgments' 与标准化模型调用；无随机分配描述。 | 研究单位没有被分配到互斥条件；无随机化分配机制。 |
| C2 | 平衡 | NA | — | 无实验条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | p13: 'temperature ... set to 0.01'；'images displayed at 512 x 512 pixels'；p13: 标准 prompt。 | 列出若干恒定设置，但未系统列出所有恒定变量及其水平；对相应外部效度限制只部分讨论。 |
| C4 | 匹配 | NA | — | 没有匹配设计；GPT-4 子样本随机抽取 1,000/2,171 属重采样比较，不是匹配。 |
| C5 | 纳入为变量 | NA | — | 未把已知混淆变量作为区组或协变量纳入 ANOVA/ANCOVA 类模型。 |
| C6 | 盲法 | NA | — | 无实验分组或需要盲法的被试/评分条件；维度命名不是条件评分实验。 |
| C7 | 平衡的层级 | NA | — | 无完全平衡/拉丁方/ABBA 顺序设计。 |
| D1 | 练习效应 | NA | p13: 每个三元组以独立 prompt 收集判断，LLM 无上下文内学习。 | LLM 试次独立、无练习块；人类数据为既有数据，不涉及新实验练习效应。 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳；人类数据为既有大规模在线数据，未设计 session 疲劳控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同试次/模型调用相互独立，无跨条件清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉处理，无不对称迁移问题。 |
| D5 | 范围效应 | NA | — | 主要因变量为离散 odd-one-out 选择、相似性/RSA 与准确率，不是 Likert/绝对量值量表。 |
| E1 | 位置 / 顺序偏差 | 0 | p13: prompt 固定为 'Given a triplet of objects {[Object_A], [Object_B], [Object_C]}...'，未报告三元组内对象位置随机化或反平衡。 | 存在候选对象 A/B/C 位置偏差风险，但全文未报告任何顺序/位置随机化或平衡方案。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无新的人类实验被试和掩饰情节；LLM 任务的引导性/提示偏差在 J6 处理。 |
| E5 | 实验者效应 | NA | — | 数据采集为自动化 API 与既有人类数据；无实验主试期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5: 'accuracies were 56.7% ... noise ceilings ... 65.1%'；p11: fMRI 结果用 85% noise ceiling 评估；p16: 报告 bootstrap 与 FDR。 | 报告均值/CI 与噪声天花板，但未报告偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式 IV/DV 同源测量；行为、模型特征和 fMRI 来源不同。 |
| F1 | 统计结论效度 | 0.5 | p5: 报告 accuracy 的 95% CI 与 noise ceiling；p11: 'FDR-corrected'；p16: '2,000 times' bootstrap；p14: 20 reruns。 | 报告效应量与置信区间、多重校正；但无事前功效分析或明确样本量确定依据。 |
| F2 | 内部效度 | NA | p13: 人类数据来自既有 MTurk 数据集；LLM 行为通过标准 prompt 采集。 | 纯观察/比较研究，无随机分配与因果处理，不适用实验内部效度评估。 |
| F3 | 构念效度 | 1 | p2-p5: SPoSE 嵌入的稳定性、预测性与 held-out 行为预测；p14: 20 次随机初始化重复性；p15: split-half reliability；p11: 脑表征验证。 | 报告了关键测量的信度、预测效度和多操作化会聚证据；无实验操纵故无 manipulation check。 |
| F4 | 外部效度 | 0.5 | p12: 人类样本 12,340 名被试及人口学特征；p12: 讨论仅两个模型和 prompt 局限；p13: NSD 使用 S1/S2/S5/S7 四名被试。 | 报告了样本来源与部分边界条件，但未系统给出抽样框/代表性，也未报告跨样本复现。 |
| G1 | 分析单位 | 0.5 | p14: SPoSE 在 1,854 个对象上学习，三元组为输入；p15-p16: RSA/searchlight/voxel-wise 以对象与体素为单位并做 bootstrap。 | 说明了对象/试次与 fMRI 体素层级，但未用多层模型显式处理三元组嵌套于对象、试次嵌套于模型等聚集结构。 |
| G2 | 随机效应 | 0 | p10: fMRI 结果为 'n=4 subjects'；p15-p16: RSA/encoding 按被试或 ROI 汇总并报告均值，未说明随机效应结构。 | 研究跨被试和对象做推广，但统计模型未报告随机效应；未将应随机的被试/模型因子显式建模。 |
| G3 | 材料作为随机效应 | 0.5 | p14: category prediction 使用 leave-one-object-out；p13: 48 typical objects 完整采样；p14: 1,854 THINGS 对象池。 | 对象/材料被视为从更大对象总体抽样并有 held-out 验证，但未用 item random effect 或准 F/混合模型同时建模对象与被试。 |
| G4 | 统计功效 | 0.5 | p5: accuracy 与 noise ceiling 的 CIs；p11: RSA/encoding 的 CIs 与 FDR；p16: bootstrap。 | 报告效应量与置信区间，但无设计阶段功效分析或明确样本量推导。 |
| G5 | 研究者自由度 | 0.5 | p12: 人类数据排除 818,240 trials 及标准；p13: Gemini 拒绝回答时采用 image replacement；但未报告 LLM 排除数量/停止规则。 | 报告了部分排除规则与因变量，但未完整报告所有试次排除、样本量决定方式及验证/探索分析区分。 |
| G6 | 预先设定 / 预注册 | 0 | p16: 仅见 Data availability 与 Code availability，无预注册平台/编号。 | 无预注册，且未区分验证性与事后探索性分析。 |
| J1 | 位置偏差 | 0 | p13: 固定 prompt 按 [Object_A]/[Object_B]/[Object_C] 呈现三元组，未报告位置交换、反平衡或翻转率。 | LLM odd-one-out 存在候选位置偏差风险，但未做任何位置反平衡或报告位置×选择结果。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 或开放式生成质量评分；长度偏差不构成绩效评估风险。 |
| J3 | 谄媚 | NA | — | 无用户立场、反馈、纠错或多轮谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不涉及 LLM 裁判/成对比较评分，无自我偏好风险。 |
| J5 | 少样本示例选择与排列偏差 | NA | p13: 标准 prompt 中未加入 few-shot 示例，属 zero-shot。 | 无 in-context few-shot 示例选择与排列问题。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p13: 给出完整 LLM/MLLM prompt；p12: 'impact of varying language prompts'；p33-p34: 补充材料展示引导提示示例。 | prompt 模板明确，但未做系统敏感性消融、版本化或 dev/test 分离；引导提示只作定性示例。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | p13: prompt 仅含三元组对象描述或三张图像，上下文远低于长上下文/RAG 场景。 | 无长上下文或 RAG 信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p13: 'temperature ... set to 0.01'；p13: 噪声天花板抽样 1,000 triplets、每类 14-25 次；p14: SPoSE 20 reruns。 | 报告了温度和部分重复运行，但未完整报告 seed、top-p/top-k、所有条件重复采样与 CI，闭源 API 快照也不精确。 |
| J9 | 重复与文本退化 | 0.5 | p13: temperature 0.01；p13: 从第一句用 string matching 解析选择。 | 报告了部分解码设置，但未报告 greedy/beam、repetition penalty、重复率/退化率；解释文本的退化未作为 QC。 |
| J10 | 分词效应 | NA | — | 单语言英语 prompt，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p13: 模型包括 gpt-3.5-turbo、Gemini Pro Vision v1.0、gpt-4-0314 等；p12: 使用公开 THINGS 数据库与公开描述；未报告训练截止日期与污染检测。 | 测试对象与描述为公开材料，但未做训练截止日期对照或 n-gram/DCQ 污染检查。 |
| J12 | 基准饱和 | 1 | p5: 报告 chance=33.3%、模型 accuracy、noise ceiling 与 bootstrap CI；p11: 使用连续 RSA 与 noise-normalized R²；p10: 报告噪声天花板。 | 报告分数量程/水位并采用连续相似性指标与噪声天花板，未在饱和基准上宣称显著提升。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循；虽然 prompt 要求先回答再解释，但未按约束类型测量 IF 准确率。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p13: LLM 要求 'Please give the answer first and then explain'，从第一句 string matching；MLLM 提取 'left, middle, or right'。 | 有输出格式要求与解析规则，但未报告格式合法率、重试策略，也未把格式失败与内容错误分开统计。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p2: 'human-like conceptual representations'、'mental representations in LLM and MLLM'；p14: 用 odd-one-out/SPoSE 推断 LLM 低维嵌入；p13: 给出模型版本并与人类同范式对照。 | 明确了 LLM 上所测对象概念表征并与人类同名构念对照，但未系统讨论二者的理论异同，跨模型比较也非正式随机化自变量。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及跨模型规模/训练进展的能力曲线，也未以规模阶梯宣称涌现；标题中的 emerge 不是 scaling 曲线分析。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无 RL、best-of-N 或按代理指标优化模型的环节。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p13: 报告 gpt-3.5-turbo、Gemini Pro Vision v1.0、gpt-4-0314、Llama3.1-8B-Instruct、Qwen2_VL-7B；p5: 1,000 bootstraps；p14: 20 reruns；p16: 公开代码与数据。 | 报告了重复次数、bootstrap CI 和部分版本标识，但未对每个 API 给出精确 snapshot/调用日期与随机种子，模型比较也未做配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | p13: 每个三元组由单轮 prompt 查询；无对话历史累积。 | 严格单轮任务，不涉及多轮一致性衰减。 |

## 编码小结
核心方法报告较充分：odd-one-out 任务、SPoSE、RSA、交叉验证、噪声天花板和重复初始化均有描述。主要局限是设计上无随机分配/顺序平衡，LLM 位置偏差、提示敏感性、采样种子与快照、污染检查、预注册/功效等报告不足；大量人类实验设计组件对本研究不适用。
