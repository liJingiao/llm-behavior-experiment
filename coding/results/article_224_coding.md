# article_224 | BooookScore: A systematic exploration of book-length summarization in the era of LLMs | 2024

研究类型概述：LLM 书长摘要系统评测与方法学研究：比较层级合并与增量更新两种提示流程、多个基础模型与不同 chunk size，提出并验证基于 GPT-4 的 BooookScore 自动连贯性指标，同时用人类标注与偏好判断进行验证。分析单位为摘要/句子及系统级配置，不是人类被试实验。
- **研究构念（Construct）**：长篇话语连贯性、跨段信息整合、错误类型与细节权衡｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：让现成GPT-4、GPT-3.5、Claude、Mixtral和LLaMA检查点按层级合并或增量更新流程总结100本新书，并以人工错误分类和BooookScore比较。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p7: 'we now investigate the impact of several critical implementation decisions... prompting strategy, base LLM, and chunk size'; p7 Table 2 lists model and chunk size levels. | 明确命名了提示策略、基础模型、chunk size 等自变量并给出至少两个水平；但未见正式分配说明与操纵检验，只报告配置流程，故为 0.5。 |
| A2 | 因变量 | 0.5 | p6: 'BooookScore(S)=1/n sum [LLM(E,S,si)==No confusion]'; p5: precision of human annotations 79.7%, BooookScore 78.2%. | 因变量指标与计分方式明确，且有验证性精度与 bootstrap 稳定性证据；但缺少正式信度/效度体系、连续指标预处理和天花板/地板说明，故为 0.5。 |
| A3 | 控制变量 | 0.5 | p7: 'we set the chunk size to 2048, maximum summary length Gn to 900, decoding temperature to 0.5, and p=1... use identical prompts for all models except LLaMA2'. | 报告了若干保持恒定的参数和提示控制；但不是系统化控制变量清单，也未逐项说明控制手段与外部效度影响，故为 0.5。 |
| A4 | 混淆变量 | 1 | p4: 'To reduce the confounding impact of summary memorization, we manually collect 100 books published within the past year'; p4 also acknowledges residual contamination possibility. | 明确识别数据污染/记忆混淆，采用新出版书籍控制，并讨论残余风险；符合 1。 |
| A5 | 调节变量 | NA | — | 没有正式调节变量假设与交互检验；文中 chunk size 与策略的条件差异只是描述性比较，不构成调节分析，故 NA。 |
| A6 | 中介变量 | NA | — | 没有中介变量、直接/间接效应分解或因果链假设，故 NA。 |
| A7 | 操作性定义 | 1 | p3 and p13 Appendix A specify hierarchical merging and incremental updating procedures; p5 Table 1 defines eight coherence error types; p6 gives BooookScore scoring. | 关键构念和流程具有可复现操作化：提示流程、错误类型定义、句子级标注与计分公式均明确。 |
| A8 | 水平数与类型 | 0.5 | p7 Table 2 and setup report five models and chunk sizes 2048 and 88000; p3 distinguishes two prompting strategies. | 水平数与各水平标签基本明确；但未系统说明水平类型、间距/全距和连续变量中心化，故为 0.5。 |
| A9 | 单一操作化的风险 | 1 | p6 compares BooookScore with human annotations; p7 reports human-only BooookScore 82.1/89.4 vs LLM 82.4/90.8; p5 reports precision 78.2% vs 79.7%. | 连贯性使用人类标注、自动指标和人类偏好等多种操作化，并报告会聚证据，符合 1。 |
| A10 | 单一方法的风险 | 0.5 | p5-p6 BooookScore is implemented with GPT-4 and validated against human annotations; p8 reports human preference study. | 存在多方法验证（自动裁判与人类标注/偏好），但主评测仍主要依赖 GPT-4 单一裁判，未系统做共同方法偏差统计控制，故为 0.5。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或独立被试组接受单一条件的被试间实验设计；LLM 配置比较是系统级确定性运行，不是被试间分配，故 NA。 |
| B2 | 被试内设计 | NA | — | 没有明确的被试内重复测量条件顺序设计；不同摘要配置为独立生成，且无顺序平衡需求，故 NA。 |
| B3 | 混合设计 | NA | — | 无组间/组内因素混合设计，也无相应统计模型，故 NA。 |
| B4 | 因子设计 | NA | — | 研究比较多个模型、策略和 chunk size，但不是完全交叉的因子实验，未报告设计矩阵与交互项，故 NA。 |
| B5 | 主效应 | NA | — | 没有正式因子设计意义上的主效应检验，故 NA。 |
| B6 | 交互作用 | NA | — | 没有正式交互作用检验或简单效应分析，故 NA。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机设计，故 NA。 |
| B8 | 拉丁方 | NA | — | 没有被试内拉丁方顺序设计，故 NA。 |
| B9 | 准实验设计 | NA | — | 不是准实验因果设计；没有非随机分组与选择偏差讨论，故 NA。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有被试内处理可逆性/迁移对称性设计，故 NA。 |
| C1 | 随机化 | NA | — | 没有随机分配与分配隐藏机制；所有系统配置按设定确定性运行，故 NA。 |
| C2 | 平衡 | 0.5 | p8 footnote 16: 'To prevent bias, we shuffle the ordering of incremental and hierarchical summaries for each summary pair, and conceal the summarization method'. | 人类偏好子研究对呈现顺序做了随机化/反平衡；但未报告各顺序数量或平衡层级，故为 0.5。 |
| C3 | 恒定 | 0.5 | p7: 'chunk size to 2048... temperature to 0.5... p=1... identical prompts'; p15 gives model checkpoints. | 列出若干恒定参数与模型版本，但未系统讨论这些恒定选择对外部效度的限制，故为 0.5。 |
| C4 | 匹配 | NA | — | 未使用匹配设计或匹配后均衡性检验，故 NA。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为协变量/区组纳入统计模型；长度仅作相关探索，不是 ANCOVA 型设计，故 NA。 |
| C6 | 盲法 | 0.5 | p8 footnote 16: prefer化 summary ordering 并 conceal summarization method; p19: human and GPT-4 annotations are mixed, concealing origin. | 报告了对评分者/标注者施盲的安排；但未报告盲法成功检验或完整实施方式，故为 0.5。 |
| C7 | 平衡的层级 | 0.5 | p8 footnote 16 says shuffle ordering for each summary pair; no further balance-level construction is reported. | 报告了偏好判断的顺序随机化，但未明确完全平衡/拉丁方/ABBA 层级及理由，故为 0.5。 |
| D1 | 练习效应 | NA | — | 主要 LLM 摘要生成无人类或模型跨试次上下文内学习；上下文重置，练习效应不适用，故 NA。 |
| D2 | 疲劳效应 | NA | — | 虽然人类标注耗时，但研究不是重复测量被试实验；无 session 疲劳与条件时间分散设计，故 NA。 |
| D3 | 延滞 / 迁移效应 | NA | — | 每个摘要配置独立生成，无跨条件残留或清洗期设计，故 NA。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性检验需求，故 NA。 |
| D5 | 范围效应 | NA | — | 因变量为自动/标注比例与偏好选择，不是主观量表量值估计；无范围效应设计，故 NA。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p8 footnote 16: 'we shuffle the ordering of incremental and hierarchical summaries for each summary pair'. | 人类偏好判断对两摘要呈现顺序做了随机化；但未报告位置分布、翻转率或各顺序分配，故为 0.5。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，故 NA。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较，故 NA。 |
| E4 | 需求特征 | 0.5 | p8 footnote 16: conceal summarization method; p19: mix human and GPT-4 annotations and conceal their origin. | 使用盲法/来源隐藏降低需求特征；但未做事后访谈或推断比例检查，故为 0.5。 |
| E5 | 实验者效应 | 0.5 | p4: four annotators with English proofreading experience; p8 and p19 describe concealment of method/origin. | 报告了评分者来源与部分盲法安排；但未报告系统培训、脚本化程度或盲法层级细节，故为 0.5。 |
| E6 | 天花板 / 地板效应 | 0.5 | p7 Table 2 reports mean BooookScore; p17 Appendix G reports bootstrap standard deviation 0.015. | 报告了均值与一个稳定性指标，但未报告偏度、端点频率或 pilot 难度校准，故为 0.5。 |
| E7 | 共同方法偏差 | NA | — | 不涉及同源自陈式多构念测量；不适用，故 NA。 |
| F1 | 统计结论效度 | 0.5 | p7 Table 2 reports BooookScore means; p17 reports bootstrap SD 0.015; no CIs or power analysis are reported. | 有描述性效应指标和 bootstrap 稳定性，但缺少样本量确定依据、置信区间、多重性校正等，故为 0.5。 |
| F2 | 内部效度 | 0.5 | p4 controls contamination via newly published books; p7 reports config setup and identical prompts; no random allocation/flow diagram. | 对内部效度威胁有部分评估（污染、提示一致性），但不是随机实验，也无分配隐藏/基线/流向报告，故为 0.5。 |
| F3 | 构念效度 | 1 | p5: human annotation precision 79.7%, BooookScore precision 78.2%; p6-p7 human vs LLM BooookScore nearly identical; p17 bootstrap SD 0.015. | 关键测量 BooookScore 有人类验证、精度、会聚效度与稳定性证据，构念效度论证较充分。 |
| F4 | 外部效度 | 0.5 | p4: 100 newly published books, genres roughly balanced; p14 Table 3 lists titles/authors/genres; p9 limitations discuss taxonomy/model limits. | 报告了样本来源和特征并讨论部分边界，但未报告跨样本复现或系统推广边界，故为 0.5。 |
| G1 | 分析单位 | 0.5 | p6 computes sentence-level BooookScore then system-level mean across summaries; p7 Table 2 reports system-level scores. | 描述了分配/分析层级（句子→摘要→系统），但未用多层模型处理句子/书籍嵌套，故为 0.5。 |
| G2 | 随机效应 | NA | — | 无混合模型与随机效应结构；模型配置为固定系统比较而非从总体抽样的被试随机效应，故 NA。 |
| G3 | 材料作为随机效应 | 0.5 | p4 samples 100 recent books as materials; p7 aggregates BooookScore across summaries; no item random effect / mixed model. | 书籍作为材料从较大总体抽取并在系统均值中体现，但分析未显式建模书籍随机效应，故为 0.5。 |
| G4 | 统计功效 | 0 | p4 states 100 books were collected; no power analysis or sample-size rationale is reported. | 没有事前功效分析或其他样本量论证，且无效应量置信区间，故为 0。 |
| G5 | 研究者自由度 | 0.5 | p15 reports LLaMA truncation/post-processing decisions; p7 lists configurations; no full exclusion/optional-stopping disclosure. | 报告了部分数据截断与后处理规则，但未完整报告全部因变量/条件、排除数量与探索/验证区分，故为 0.5。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration statement or registry link appears in the main text, pp.1-9. | 无预注册，故为 0。 |
| J1 | 位置偏差 | NA | — | BooookScore 不是成对候选选择/排序的 LLM-as-judge 位置实验；无候选位置需要反平衡，故 NA。 |
| J2 | 冗长偏差 | 0.5 | p17 Appendix F: 'no discernible correlation between length and BooookScore'; p7 Table 2 reports average summary length. | 检查了摘要长度与得分关系，但裁判 rubric 未明确要求避免长度偏好，也未报告长度偏好的完整控制，故为 0.5。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错式对话操纵，故 NA。 |
| J4 | 自我偏好 | 0.5 | p6: 'we implement BooookScore with GPT-4'; p8 limitations: GPT-4 judge 'may have some systematic biases'; p5-p6 human validation. | 使用了 GPT-4 作为唯一裁判并评估包括 GPT-4 在内的模型；承认可能有系统偏差并有 human validation，但未量化自我偏好或采用异源陪审团，故为 0.5。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p6: 'We include two full summaries with 42 sentence-level annotations in the prompt as demonstrations'; p32-p35 prompt excerpt. | 报告了 few-shot 示例数量和部分构成，但未报告示例来源、标签比例、排列反平衡或多 seed 重采样，故为 0.5。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p28-p35 provide summary prompts and a BooookScore prompt excerpt; p5 says preliminary experiments without definitions/few-shot had reduced precision; p6 footnote says full prompt is in codebase. | 提供了若干 prompt 模板并报告初步消融观察，但 BooookScore prompt 在文中省略，未系统做敏感性消融或 dev/test 分离，故为 0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | 0.5 | p4: average book length 190K tokens; p3-p4 describes chunking; p8: Claude 2 'omits key information present in the beginning or middle'. | 明确涉及超长上下文与 chunk 设置，并定性讨论中间信息丢失；但未系统操纵关键信息位置或报告位置×正确率曲线，故为 0.5。 |
| J8 | 温度与采样随机性 | 0.5 | p7: decoding temperature 0.5; p=1 ancestral sampling; p15 model checkpoints; p17 bootstrap over summaries. | 报告了部分采样参数与模型版本，但未报告随机种子、每条件重复采样 N 或均值置信区间，故为 0.5。 |
| J9 | 重复与文本退化 | 0.5 | p7 reports temperature/p=1; p7 Table 2 reports '% rep. 3-grams'; p8 discusses LLaMA 2 repetition. | 报告了解码相关参数与重复 n-gram 指标，但未报告 repetition penalty 或所有条件解码恒定细节，故为 0.5。 |
| J10 | 分词效应 | NA | — | 研究为英语单语言、单脚本，无跨语言/跨脚本 tokenization 比较，故 NA。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p4: avoids BookSum because famous books are in pretraining data; collects 100 books published in past year; acknowledges some could still be in pretraining. | 明确识别并大幅降低污染，但未做 n-gram/DCQ 污染检测或报告污染率，故为 0.5。 |
| J12 | 基准饱和 | 0.5 | p7 Table 2 reports BooookScore from 64.5 to 91.1; p17 reports bootstrap SD 0.015; no saturation analysis. | 报告了分数量程和当前水位，但高分段可能接近上限，未讨论饱和或改用更难子集/连续指标比较，故为 0.5。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；LLaMA 2 不遵循压缩指令只是定性观察，故 NA。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求 JSON/文法约束式结构化输出实验；BooookScore 的自由文本输出仅作简单解析，未作为格式合法性指标，故 NA。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全性、越狱或有害请求评估，故 NA。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究测量文本摘要连贯性，不将 LLM 作为心理学/认知科学被试，故 NA。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 没有跨规模/训练进展的能力曲线或涌现宣称，故 NA。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有针对代理指标的优化/训练/RL/best-of-N 流程；BooookScore 用作评估而非优化目标，故 NA。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p15 reports GPT-4 2023-03-15, GPT-3.5-turbo-0301, Mixtral checkpoint, Claude 2 API in Sept 2023; p17 reports bootstrap SD; no repeated generation N or CIs. | 报告了较精确的模型 snapshot/日期和一次 bootstrap 稳定性分析，但缺少每条件重复运行 N、置信区间与配对检验，故为 0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 不是多轮对话评估；书长摘要是迭代式 chunk 处理，但不是对话历史累积，故 NA。 |

## 编码小结
论文对书长摘要的提示流程、人类标注协议和 LLM 自动指标作了较透明的描述，BooookScore 与人类标注一致性验证较扎实。但整体是系统级描述性评测：缺少正式推断统计、功效分析、随机效应建模、预注册和完整敏感性分析；对 LLM 裁判同源偏差、提示敏感性和长上下文位置效应只作了部分识别或定性讨论。
