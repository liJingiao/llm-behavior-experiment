# article_103 | Comparing Moral Values in Western English-speaking societies and LLMs with Word Associations | 2025

研究类型概述：计算/观察性比较研究：使用既有英语人类词关联数据WA-H与Llama-3.1-8B-Instruct生成的WA-L，构建关联图，并用MFD/eMFD传播和评估道德价值；分析单位为cue词/概念、关联图和五维道德分数，无人类被试随机分配或实验条件操纵。
- **研究构念（Construct）**：道德价值表征、道德基础与心理词典中的概念关联｜CA 构念锚定：社会规范加工（social norm processing, `trm_58c80b824c51b`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：计算/观察性比较研究：使用既有英语人类词关联数据WA-H与Llama-3.1-8B-Instruct生成的WA-L，构建关联图，并用MFD/eMFD传播和评估道德价值；分析单位为cue词/概念、关联图和五维道德分数，无人类被试随机分配或实验条件操纵。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | NA | — | 研究为计算/观察性比较：使用既有WA-H数据并生成WA-L，不存在研究者随机分配水平到被试/试次的实验自变量；'human vs LLM'是观察分组而非操纵变量。 |
| A2 | 因变量 | 0.5 | p4: 'We prompted Llama... up to three responses per cue'; p4: split-half reliability; p6 Table 1: Spearman correlations with eMFD; p8 Table 4: emotion/concreteness scores; p13 Appendix A prompt. | 因变量指标与计分基本明确（关联强度、moral scores、precision@K、与eMFD相关、情绪/具体性比例/强度），并有WA-L split-half reliability和eMFD效标相关；但未系统报告所有指标信度、分布/端点及天花板地板控制，故0.5。 |
| A3 | 控制变量 | 0.5 | p4: 'employ the exact same instructions as used in the WA-H data collections'; 'repeating this process 100 times for each cue'; p5: 'optimal temperature of 2.1.' | 报告了cue集合、prompt、重复次数和温度等关键控制，但未系统列出全部控制变量清单及控制手段，故0.5。 |
| A4 | 混淆变量 | NA | — | 无实验操纵的自变量，故不存在内部效度意义上的处理混淆；模型/文化等外部/构念限制在p10 limitations讨论，不按A4编码。 |
| A5 | 调节变量 | NA | — | 未提出或检验调节假设；五维MFT比较为描述性/分组比较，无乘积项交互与简单斜率。 |
| A6 | 中介变量 | NA | — | 未提出或检验中介模型，无直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | p4-p5: 12k cues, 100 repetitions, graph construction; p5: propagation equation F_{t+1}=...; p13 Appendix A full system/user prompt; p1 footnote code/data link. | 关键构念均有可复现操作化：关联生成prompt、重复次数、图构建、MFD种子、随机游走传播公式、eMFD评估与词典计分。 |
| A8 | 水平数与类型 | NA | — | 无操纵的多水平实验自变量；human/LLM来源与五维MFT是观察分组/维度，不是实验因素水平。 |
| A9 | 单一操作化的风险 | 0.5 | p2: acknowledges MFT definitions under active research; p10: concept-level alignment limitation; p6-p8: one main moral-score pipeline plus emotion/concreteness indicators. | 道德构念主要依赖单一MFD/eMFD+关联图管线；虽有情绪、具体性和图属性等补充指标，但未系统报告多操作化会聚证据，局限讨论也较概括，故0.5。 |
| A10 | 单一方法的风险 | NA | — | 非自评问卷式同源测量；核心比较基于计算生成的关联图与外部词典评分，不适用常见CMB检验框架。 |
| B1 | 被试间设计 | NA | — | 无被试间实验分配：人类数据为既有WA-H，LLM为同一模型生成；不存在独立被试组承担条件。 |
| B2 | 被试内设计 | NA | — | 无被试内条件重复设计；100次LLM生成是重复采样并聚合为关联强度，不是同一分析单位接受多条件。 |
| B3 | 混合设计 | NA | — | 无组间×组内混合实验设计。 |
| B4 | 因子设计 | NA | — | 不是因子实验；human vs LLM与五维MFT不是完全交叉并随机分配的处理结构，未做ANOVA交互。 |
| B5 | 主效应 | NA | — | 无因子设计及主效应ANOVA；表1/4为相关或描述性/t检验比较。 |
| B6 | 交互作用 | NA | — | 无交互项检验或简单主效应。 |
| B7 | 区组设计 | NA | — | 无区组/分层随机设计；按POS选择279 cues是评估抽样分层，不是实验区组。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 非随机比较但不是准实验干预设计，不主张处理因果效应，故不按准实验编码。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内设计，不涉及可逆性/迁移对称性。 |
| C1 | 随机化 | NA | — | 无处理条件分配；随机子集/随机split仅用于温度调参/可靠性，不是随机化分配与隐藏。 |
| C2 | 平衡 | NA | — | 无条件顺序需平衡。 |
| C3 | 恒定 | 1 | p4: 'Llama-3.1-8B-Instruct'; 'exact same instructions'; '100 times for each cue'; p5: 'optimal temperature of 2.1'; p10: model/culture limitations. | 关键恒定项（模型版本、prompt、温度、重复次数）明确，并在Limitations讨论模型选择与文化外部效度限制；虽未报API日期，核心恒定控制清楚。 |
| C4 | 匹配 | NA | — | 未使用匹配/配对设计。 |
| C5 | 纳入为变量 | NA | — | 无实验处理条件下的已知混淆变量协变量/区组分析。 |
| C6 | 盲法 | NA | — | 数据采集与评分完全自动化，无人类被试/评分者盲法需求。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | LLM每个cue独立生成，未设练习块或上下文内学习；人类数据为档案数据。 |
| D2 | 疲劳效应 | NA | — | 无人类长session；LLM短prompt调用无疲劳/休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 无跨条件清洗期/迁移风险；各cue独立生成。 |
| D4 | 不对称迁移 | NA | — | 无跨条件顺序或迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 主要指标为关联图/词典分数与相关，不是被试内绝对判断或李克特量表。 |
| E1 | 位置 / 顺序偏差 | NA | — | 无被试内刺激/选项顺序设计；每个cue独立prompt，三词输出顺序未作为分析变量。 |
| E2 | 默认赞同 | NA | — | 不使用Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表；无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试参与与事后访谈；LLM prompt虽有人类角色框架，但不属人类需求特征检查。 |
| E5 | 实验者效应 | NA | — | 完全自动化采集/评分，无人类主试或评分者。 |
| E6 | 天花板 / 地板效应 | 0.5 | p5 Figure 4: precision@K near perfect at k=1 and declines; p6 Table 1 correlations; p13 Figure 5 reliability; no distribution/endpoint discussion. | 报告了precision@K曲线和相关系数，可看出k=1接近天花板；但未报告正式均值/SD/偏度/端点频率，也未说明任务难度校准或讨论天花板影响，故0.5。 |
| E7 | 共同方法偏差 | NA | — | 无多构念自评问卷及同源测量比例；不适用CMB统计检验。 |
| F1 | 统计结论效度 | 0.5 | p6 Table 1: Spearman correlations and n, 'All correlations are statistically significant (p ≤ 0.01)'; p8 Table 4: t-test p<0.05. | 报告了相关/效应量与部分p值、样本量，但无95%CI、无样本量确定依据、无多重比较校正，故0.5。 |
| F2 | 内部效度 | NA | — | 纯观察/计算比较，无随机分配或因果处理效应主张；不按实验内部效度编码。 |
| F3 | 构念效度 | 0.5 | p4 split-half reliability; p5 Figure 4 precision@K; p6 Table 1 correlation with eMFD as validity; p10 limitations. | 报告了关联生成信度/效标相关和部分图指标，但无操纵检验（无操纵），多操作化会聚有限，故0.5。 |
| F4 | 外部效度 | 0.5 | p4: WA-H ~90k native English speakers, primarily US/UK/Canada/Australia; p10: 'only covers Western, English-speaking cultures'; 'different models might exhibit different behaviors'. | 报告了样本来源与代表性边界，并明确模型/文化推广限制；但只测一个模型、无跨样本/跨情境复现，故0.5。 |
| G1 | 分析单位 | 0.5 | p4: 'repeating this process 100 times for each cue word'; 'Monte-Carlo approximation'; p5: construct WA graphs then propagate to GMN; graph-level analysis. | 说明了100次生成并聚合到cue/图级别，但没有用多层模型显式处理重复生成嵌套于cue的结构，故0.5。 |
| G2 | 随机效应 | NA | — | 未使用混合模型或随机效应推断；分析为图/概念层面的固定计算，不涉及需要随机截距/斜率的抽样总体。 |
| G3 | 材料作为随机效应 | 0.5 | p4: 12k cues; p6: evaluation on eMFD intersection (n=2,186) and held-out seed subtraction; p13 Table 5: 12,216 nodes. | 材料/概念覆盖面很大且在eMFD held-out词上评估，体现跨项目推广；但未用item random effect或混合模型，故0.5。 |
| G4 | 统计功效 | 0 | — (全文无功效分析/样本量依据；仅p6 Table 1 n和p8 t检验) | 无事前功效分析或样本量论证；虽报告相关/部分效应量，但无CI，按G4判0。 |
| G5 | 研究者自由度 | 0.5 | p5: random subset 400 cues for temperature; p6: 277 tuning words vs 1,909 evaluation; p5: 279 cues selected from MFD; p1 code/data link. | 报告了部分抽样/排除与数据划分，但未完整列出所有因变量/条件、样本量决定方式或明确区分验证性与探索性分析，故0.5。 |
| G6 | 预先设定 / 预注册 | 0 | — (全文无预注册平台/编号或时间戳) | 未预注册主要假设、分析计划、排除规则；按校准口径，无预注册记0。 |
| J1 | 位置偏差 | NA | — | 不涉及LLM-as-judge、排序或多项选择位置反平衡。 |
| J2 | 冗长偏差 | NA | — | 不涉及LLM裁判评分开放生成质量的长短比较。 |
| J3 | 谄媚 | NA | — | 无用户先验立场/反馈/纠错对话操纵。 |
| J4 | 自我偏好 | NA | — | 不使用LLM作为裁判评估模型输出。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | Appendix A prompt为零样本，无few-shot示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p13 Appendix A full system/user prompt; p4: 'LLM responses are known to be unstable with respect to changes in prompts...'. | 公布了完整prompt模板并讨论prompt敏感性，但未做措辞版本敏感性消融、未说明dev/test划分或prompt搜索过程，故0.5。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文仅为短prompt+cue word，无长文档/RAG。 |
| J8 | 温度与采样随机性 | 0.5 | p4-p5: 100 repetitions per cue, random subset 400 cues, temperature tuned to 2.1; p5 Figure 4 shaded SD over 50 runs. | 报告了temperature和重复次数/部分SD，但未报top-p/top-k/seed或主分析bootstrap CI，闭源/模型snapshot细节不足，故0.5。 |
| J9 | 重复与文本退化 | 0.5 | p4: 'we tune Llama's temperature'; 'repeating this process 100 times'; p5 Figure 4 diversity/robustness. | 报告了temperature和重复生成，但未明确解码策略（sampling/greedy）、repetition penalty，也未报n-gram重复率/退化率，故0.5。 |
| J10 | 分词效应 | NA | — | 单语言英语、单脚本，无跨语言/跨格式比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p1: 'leakage of moral questionnaires into the LLMs’ training data ... raises questions'; p4: MFD/eMFD used; no training cutoff or overlap test. | 虽承认问卷泄漏风险，但未报告模型训练截止日期、eMFD/MFD污染重叠检测或held-out私有集，故0。 |
| J12 | 基准饱和 | NA | — | 主要评估为连续相关和precision@K，不是接近饱和的标准基准；未在饱和基准上宣称显著提升。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量；无约束指令遵循测量。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p13 Appendix A: 'Output your response in the following format: response1, response2, response3'; no format-validity rate reported. | 提出了逗号分隔结构化输出要求，但未报告格式合法率、重试/后处理规则，也未把格式失败与内容错误分开，故0.5。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p1-p2: measures 'mental lexicon' of LLMs via word associations; p10: model/culture limitations; no systematic LLM-human construct comparison beyond same paradigm. | 明确把LLM词关联作为心理词典/道德价值代理并与人类同范式数据比较，但未系统论证LLM构念与人类同名构念异同，且仅一个模型，故0.5。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无跨规模/训练进展能力曲线，不涉及涌现宣称。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无对代理指标的训练/RL/best-of-N优化；alpha调参在held-out eMFD上评估，不属overoptimization研究。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p4: model Llama-3.1-8B-Instruct; 100 reps; p5 Figure 4 SD over 50 runs; p1 code/data link; no API date/commit hash or CI for main correlations. | 有重复次数、部分SD和代码数据，但模型snapshot不精确、主相关无95%CI/配对检验，故0.5。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮prompt，每个cue独立生成，无对话历史累积。 |

## 编码小结
该文在操作化、流程透明度和代码数据公开方面较强，但属于benchmark-like的观察性计算比较而非受控实验。大量人类实验设计组件不适用；主要薄弱点是单模型、无预注册/功效分析、prompt与采样敏感性未充分消融、训练污染未量化、构念效度和跨模型推广有限。
