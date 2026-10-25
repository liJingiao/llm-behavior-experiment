# article_013 | Understanding Social Reasoning in Language Models with Language Models | 2023

研究类型概述：混合型研究：提出基于因果模板、由语言模型生成题项的 BigToM 社会推理/ToM 基准，并对多个 LLM 在 0-shot、0-shot-CoT、1-shot、1-shot-CoT 等条件及不同推断条件上评估，另设人类基线；同时有人类评分者比较 BigToM 与 crowd-sourced、expert-written 题项质量。主要分析单位是测试题/模板与模型条件，而非人类被试的随机分组实验。
- **研究构念（Construct）**：社会推理与心理理论（social reasoning and theory of mind）｜CA 构念锚定：心理理论（theory of mind, `trm_4a3fd79d0b392`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：混合型研究：提出基于因果模板、由语言模型生成题项的 BigToM 社会推理/ToM 基准，并对多个 LLM 在 0-shot、0-shot-CoT、1-shot、1-shot-CoT 等条件及不同推断条件上评估，另设人类基线；同时有人类评分者比较 BigToM 与 crowd-sourced、expert-written 题项质量。主要分析单位是测试题/模板与模型条件，而非人类被试的随机分组实验。｜CA 任务锚定：心理理论任务（theory of mind task, `trm_4c8a8467304e2`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: 'we focus on the following inferences: Initial Percept to Initial Belief ... Forward Belief ... Forward Action ... Backward Belief'；p.5: 'we generate 200 templates and extract 25 conditions from each template'；p.7: 'four types of prompts: 0-shot, 0-shot-chain-of-thought, 1-shot, and 1-shot-chain-of-thought'。 | 明确命名并报告了多个操纵条件/水平及生成程序；但未报告对条件操纵的 manipulation check，未清楚说明单位如何随机分配到条件，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.7: 'We compare models on their accuracy to answer the questions'；p.4: 人类评分题项为 1-5 Likert；p.6: 'overall percentage agreement between experts on the first question was 93.94%'。 | 因变量指标与计分方式基本明确（准确率、1-5 评分、专家二值判断），并有部分评分者一致性/CI；但模型准确率缺少信效度与重复采样信息，也未系统说明天花板/地板或连续指标预处理。 |
| A3 | 控制变量 | 0.5 | p.5: 'To control for context effects, we further include a control condition in which the Causal Event is replaced with a Random Event'；p.7: 'most deterministic setting with a temperature of 0'；p.5: 生成使用 gpt-4-0314 且 temperature 0.5。 | 报告了若干控制变量与控制手段（random-event 控制、温度、初始信念有无），但未系统列出完整控制变量清单及各项控制方式。 |
| A4 | 混淆变量 | 1 | p.9: 'Our evaluation methodology may appear circular ... to validate our hypothesis about circularity not being a confound, we generate an evaluation set with claude-2'；p.9: 讨论生成数据的内容偏差、刻板印象和句法相似性等残余限制。 | 识别了模型生成题项与被评模型同源、内容偏差等潜在混淆，并用 Claude-2 生成集做交叉验证；同时如实讨论残余偏差与限制，基本符合 1。 |
| A5 | 调节变量 | NA | — | 理论模型与主要分析未包含调节变量或调节假设；模型/提示类型比较属多因素评估，但未以调节模型进行交互检验与简单斜率分析。 |
| A6 | 中介变量 | NA | — | 研究未提出中介假设，也未报告直接/间接效应分解或 a/b 路径。 |
| A7 | 操作性定义 | 0.5 | p.5: 定义 context/desire/action/percept/belief/causal event 等模板变量及 TB/FB 条件；p.5: 三阶段生成与拼接流程；p.8: 说明 'success on the false belief task as TB ∧ False Belief'。 | 关键构念（ToM 推断条件）与准确率计分有较具体操作化，但完整 prompt、人类基线细节在附录中未给出，主文不足以完全复现。 |
| A8 | 水平数与类型 | 0.5 | p.5: 总共有 25 conditions；p.8 Table 2 呈现 Forward Belief/Forward Action/Backward Belief 的 TB/FB；p.7: 四种 prompt 类型。 | 报告了主要条件的水平数与标签，但未在主文完整列出 25 个条件的全部取值/类型/间距，也未说明多因素设计的完整结构。 |
| A9 | 单一操作化的风险 | 0.5 | p.5: 使用多个推断条件（Forward Belief、Forward Action、Backward Belief）和 True/False Belief 版本；p.9: 讨论模型生成题项的局限。 | 关键构念使用了多个任务操作化，但未系统报告不同操作之间的会聚证据；对单一操作化局限的讨论也主要是生成数据偏差，而非多操作会聚。 |
| A10 | 单一方法的风险 | NA | — | 核心测量为客观多项选择准确率与人类评分，不是同源自陈式 IV/DV；共同方法偏差框架不适用于模型准确率比较。 |
| B1 | 被试间设计 | NA | — | 无人类被试随机分配到独立条件；LLM 评估按测试题独立调用，条件由模板生成而非被试间分配。 |
| B2 | 被试内设计 | NA | — | 虽然同一模型会接受多个条件，但每次评估是独立 prompt，论文未将其作为有顺序/延续的重复测量设计处理；无被试内顺序平衡问题。 |
| B3 | 混合设计 | NA | — | 不存在人类被试的组间/组内混合设计；模型与条件比较是基准评估，不是混合实验设计。 |
| B4 | 因子设计 | 0 | p.8 Table 2 呈现 GPT-4 在不同 condition 与 method 下的准确率；p.5 报告 25 个条件与多种 prompt；但未见 ANOVA/交互统计表。 | 存在多因素交叉评估结构，但论文只报告描述性准确率，未报告正式交互项、设计矩阵每格样本量与效应量，故核心统计报告未达成。 |
| B5 | 主效应 | 0 | p.8 Table 2 为描述性准确率；p.8-9 讨论条件差异但未报告主效应 F/df/p/效应量。 | 多因素评估下未报告正式主效应统计检验，仅有描述性比较。 |
| B6 | 交互作用 | 0 | p.8 Table 2 与 p.9 讨论模型/条件表现差异，但无交互项检验、简单主效应或交互图误差棒。 | 未报告交互作用统计检验；不能仅凭表格和折线式描述断言交互。 |
| B7 | 区组设计 | NA | — | 未使用区组/分层设计，也无区组变量与区内随机分配。 |
| B8 | 拉丁方 | NA | — | 无人类被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计；属于基准构建与模型评估，不涉及非随机分配下的因果推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理顺序与可逆性/迁移对称性问题；LLM prompt 独立。 |
| C1 | 随机化 | NA | — | 没有把独立分析单位随机分配到互斥条件的结构；每个模板系统地生成各条件，LLM 调用为独立评估。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡，故无平衡层级问题。 |
| C3 | 恒定 | 0.5 | p.5: 生成模型为 'gpt-4-0314 with a temperature of 0.5 and default parameters'；p.7: 评估使用 'temperature of 0'；p.9: 讨论生成偏差、句法相似性等外部效度限制。 | 报告了部分恒定变量（模型版本、温度）并讨论限制；但未系统列出所有恒定设备/环境/采样配置及其水平。 |
| C4 | 匹配 | NA | — | 未使用匹配或配对分配，无匹配变量与均衡性检验。 |
| C5 | 纳入为变量 | NA | — | 未把混淆变量作为区组或协变量纳入 ANCOVA/回归；内容混淆通过 random-event 等设计控制处理，而非协变量分析。 |
| C6 | 盲法 | 0 | p.4 与 p.6 描述人类评分者对 BigToM、socialIQa、Expert 题项评分，但未报告对评分者施盲或条件隐藏的成功检验。 | 人类评分研究存在条件来源（数据集类型）可影响评分的风险；论文未报告盲法安排，故核心盲法信息缺失。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | 无练习 block 或跨试次学习设计；LLM 评估每次独立 prompt，人类评分也无练习效应控制需求。 |
| D2 | 疲劳效应 | NA | — | 无长 session 或条件时间分散设计；任务为线上评分/短问答，疲劳风险与条件混淆不构成主要设计问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | LLM 每条件/题项独立调用，无跨条件上下文残留；未涉及需要清洗期的迁移设计。 |
| D4 | 不对称迁移 | NA | — | 无被试内交叉条件，故无迁移对称性或平衡失效问题。 |
| D5 | 范围效应 | 0 | p.4: 人类评分使用 1-5 strongly disagree–strongly agree；p.6: 仅报告均值与 95% CI，未讨论范围效应或绝对锚。 | 量表评分任务存在范围/锚定效应风险；论文未报告被试间对照、绝对锚或范围效应控制。 |
| E1 | 位置 / 顺序偏差 | 0 | p.7: 任务为 'a story, followed by a question and two answer options'；Fig.1/Table 1 展示固定顺序选项；未报告选项顺序随机化或反平衡。 | 多选题存在选项位置偏差风险；论文未报告对选项/刺激顺序做随机化或反平衡。 |
| E2 | 默认赞同 | 0 | p.4: 题项均为正向措辞的同意度量表，如 'The story is easy to understand'、'The correct answer ... is clear and unambiguous'；未见反向题或默许偏差讨论。 | Likert 量表全部单向措辞，未设反向题，也未讨论默许偏差。 |
| E3 | 极端 / 中间反应倾向 | 0 | p.4 使用 1-5 评分；p.6 报告均值与 CI，但未报告偏度、端点/中点使用比例或跨数据集反应风格校正。 | 量表评分存在极端/中间反应倾向风险；论文未报告分布形态或反应风格校正。 |
| E4 | 需求特征 | 0 | p.4 与 p.6 描述人类评分任务，但未报告 cover story、单盲程序或 post-experimental inquiry。 | 评分者可推测研究比较模型生成与人类撰写题项的质量；未报告需求特征检查或掩饰情节。 |
| E5 | 实验者效应 | NA | — | 数据收集为自动化在线评分/LLM API 调用，无人类主试或评分者面对面接触；不涉及实验者期望传递。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.8 Table 2 报告 GPT-4 各条件准确率，多处接近 .99；p.6 报告人类评分均值与 95% CI；但未报告偏度、端点频率或 pilot 难度校准。 | 报告了主要准确率/评分均值与部分 CI，可初步识别高值，但未系统排查天花板/地板效应或说明任务难度校准。 |
| E7 | 共同方法偏差 | NA | — | 核心 IV 为条件/提示类型，DV 为客观准确率或题项质量评分，不是同源自陈式多构念测量；共同方法偏差不适用。 |
| F1 | 统计结论效度 | 0.5 | p.6: 专家评分报告 95% CI；p.6: 人类题项评分用 'Bayesian linear mixed effects regression'；p.8 Table 2 模型准确率无 CI；未报告功效分析或多重性校正。 | 报告了部分效应量/CI 和混合模型，但缺样本量确定依据、模型比较的 CI 与多重比较校正，统计假设检验说明不完整。 |
| F2 | 内部效度 | 0.5 | p.5: 使用 random-event 控制、with/without initial belief 等控制条件；p.9: 讨论 circularity 与生成数据偏差；但无随机分配、分配隐藏或被试流向。 | 对部分内部效度威胁有设计控制和讨论，但缺正式随机分配/分配隐藏/基线等价或损耗报告。 |
| F3 | 构念效度 | 0.5 | p.6: 专家评分者一致性 93.94%，题项质量评分与人类评分对比；p.9: 讨论模型生成题项的效度限制；未报告 manipulation check。 | 有部分信度/效度证据（评分者一致性、人类质量评分、跨模型生成验证），但缺正式操纵检验与完整构念效度论证。 |
| F4 | 外部效度 | 0.5 | p.7: 列出 text-davinci-003、gpt-3.5-turbo、gpt-4-0314、claude-v1.3、llama-65b-q5；p.9: 讨论合成数据偏差、句法相似性与未来更真实场景。 | 报告了模型来源并讨论推广边界，但未报告人类样本来源/代表性，也未系统给出跨样本复现。 |
| G1 | 分析单位 | 0.5 | p.6: 人类评分分析使用 'Bayesian linear mixed effects regression'；p.8: 模型准确率按条件汇总；未说明题项嵌套模板/模型的层级。 | 提及混合模型但未明确分配层级与统计层级匹配，也未说明模板/题项/模型的嵌套结构。 |
| G2 | 随机效应 | 0.5 | p.6: 'Bayesian linear mixed effects regression'；未报告哪些因子为随机效应、随机截距/斜率结构。 | 人类评分分析提到混合效应，但未报告完整随机效应结构；模型准确率分析未使用混合模型。 |
| G3 | 材料作为随机效应 | 0 | p.5: 'we generate 200 templates and extract 25 conditions from each template'，共 5000 题；p.8 准确率按条件汇总，未见 item/template 随机效应或准 F 比。 | 材料/模板显然来自更大生成总体，但分析未将题目/模板作为随机效应，结论可能被过度推广到任意题项。 |
| G4 | 统计功效 | 0 | p.6: 提到 'We doubled the size of our participants and items upon reviewer’s request'；未见事前功效分析、目标功效或预期效应量。 | 无设计阶段功效分析或样本量推导；模型准确率也未报告 CI 作为精度依据。 |
| G5 | 研究者自由度 | 0.5 | p.5: 共 25 条件、5000 题；p.8 主文只聚焦 6 个条件，其余称在 App. E；p.6 注明按审稿要求加倍参与者与题项。 | 报告了部分条件与样本量决定信息，但未明确数据排除规则、全部条件/DV 的完整报告，也未系统区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0.5 | p.6 footnote 5: 'Preregistration Experiment 1: https://osf.io/qxj2s'；p.7 footnote 7: 'Preregistration Experiment 2: https://osf.io/zxw6m'；p.6 说明因审稿要求将参与者与题项加倍。 | 存在公开预注册链接并说明一处偏离/加倍，但主文未报告预注册假设、分析计划、排除规则及验证/探索分析区分。 |
| J1 | 位置偏差 | 0 | p.7: 模型收到 'a story, followed by a question and two answer options'；Fig.1/Table 1 中选项顺序固定；未报告交换 A/B 或位置随机化。 | LLM 多选题选择存在位置偏差风险；论文未做选项位置反平衡、交换重判或报告位置×正确率。 |
| J2 | 冗长偏差 | NA | — | 研究不以 LLM 裁判评价开放生成质量；主要因变量为多项选择准确率/人类质量评分，不涉及长度偏差。 |
| J3 | 谄媚 | NA | — | 无用户先验立场、反馈或多轮对话式谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge 评估模型输出；人类评分与客观准确率不涉及自我偏好裁判偏差。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.7: 'The example used for the 1-shot prompt is from the Forward Belief - False Belief condition, where the inference variable is the belief of the agent'；p.5: 生成阶段使用 3 few-shot examples。 | 报告了 1-shot 示例来源与数量，但未报告示例顺序反平衡、多 seed 重采样、示例集与测试集隔离细节，完整模板主要在项目页/附录。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.7: 评估四种 prompt 类型并比较；p.5: 生成 prompt 由因果模板构造；项目页称已发布 prompts 与 scripts。 | 有 prompt 类型比较和模板发布声明，但主文未给完整模板版本、语义等价敏感性消融、dev/test 划分与 prompt 搜索过程。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 故事上下文很短，远低于长上下文窗口，也无 RAG/长文档设置。 |
| J8 | 温度与采样随机性 | 0.5 | p.5: 生成使用 gpt-4-0314 'temperature of 0.5 and default parameters'；p.7: 评估使用 'temperature of 0'；未报告 seed、top-p、重复采样 N 或 CI。 | 报告了主要温度设置，但缺完整采样超参、seed 与重复运行/CI；生成阶段还有随机性。 |
| J9 | 重复与文本退化 | NA | — | 评估任务为多项选择/短答案，不是开放生成；未涉及解码退化率与重复率分析。 |
| J10 | 分词效应 | NA | — | 单语言英文，无跨语言/跨脚本比较，不涉及分词效率混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.3: 指出先前 ToM 测试存在 'risk of dataset leakage'；p.7: 列出 gpt-4-0314 等模型版本；p.9: 用 Claude-2 生成集做交叉验证。 | 意识到污染风险并使用新生成基准与跨模型验证，但未报告模型训练截止日期、测试集发布日期对照或污染率检测。 |
| J12 | 基准饱和 | 0 | p.8 Table 2: GPT-4 在 Forward Belief 等条件准确率多处为 .98–.99；论文未讨论基准饱和或改用连续指标。 | 准确率接近天花板但未识别饱和问题，也未改用连续指标/更难子集或 bootstrap CI 比较。 |
| J13 | 指令遵循 | NA | — | 研究因变量是 ToM 问答准确率，不是指令遵循；无 IFEval 式约束遵循评估。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 未使用 JSON/grammar-constrained/结构化输出实验；任务为普通多项选择问答，格式合法率非报告重点。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱、有害请求或对抗攻击评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.3: 将 ToM 界定为归因心理状态的能力并讨论人类/机器 ToM；p.7: 与人类基线比较；p.8: 比较模型表现与人类模式；p.9: 讨论局限但不系统论证 LLM ToM 与人类 ToM 构念等价性。 | 明确把 LLM 作为 ToM 能力被试并报告模型版本、与人类同范式比较；但未系统说明 LLM 构念与人类同名构念的异同，仍有外推风险。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未报告跨模型规模/训练进展的能力曲线，不涉及涌现或规模突变宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究是基准评估，没有以代理指标为优化目标进行训练/RL/best-of-N 优化，不涉及 overoptimization 监控。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.7: 报告模型版本 'text-davinci-003, gpt-3.5-turbo, gpt-4-0314, claude-v1.3, llama-65b-q5' 且评估温度 0；项目页称发布 prompts 与 evaluation scripts；但模型准确率无重复次数/CI/配对检验。 | 报告了较精确的模型版本与部分可复现资源，但缺重复运行 N、95% CI、逐题日志与配对统计检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 研究严格单轮问答/评分，无对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
该文的核心贡献是基准构建与 LLM 行为评估，附带人类题项质量评分。条件构造和题项生成程序较清楚，多个 ToM 推断条件也得到定义；但许多统计推断、随机化/位置平衡、采样种子、置信区间、构念效度与可复现性报告不完整，尤其缺少对多选题选项位置的系统控制、对模型准确率的重复采样与 CI、以及多因素交互的正式统计检验。
