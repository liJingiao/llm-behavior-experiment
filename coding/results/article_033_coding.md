# article_033 | On Second Thought, Let’s Not Think Step by Step! Bias and Toxicity in Zero-Shot Reasoning | 2023

研究类型概述：LLM 基准评测与受控提示实验：在同一批基准问题上比较 Standard prompting 与 zero-shot Chain-of-Thought（CoT）对模型刻板印象偏差与有害输出的影响，并比较不同 GPT-3/Flan 模型、提示模板与规模。分析单位为基准问题/模型生成结果，不是人类被试。
- **研究构念（Construct）**：零样本推理诱导的刻板印象激活与有害反应倾向（stereotype activation and harmful-response propensity under reasoning framing）｜CA 构念锚定：认知启发式（cognitive heuristic, `trm_4a3fd79d09d58`）；锚定（anchoring, `trm_4a3fd79d09833`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：LLM 基准评测与受控提示实验：在同一批基准问题上比较 Standard prompting 与 zero-shot Chain-of-Thought（CoT）对模型刻板印象偏差与有害输出的影响，并比较不同 GPT-3/Flan 模型、提示模板与规模。分析单位为基准问题/模型生成结果，不是人类被试。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | PDF_PAGE_4: §4.2 “We analyze model performance over two conditions: a Standard prompt and a CoT prompt.”；PDF_PAGE_5: §4.5 对两条件均生成 5 次 completion。 | 明确命名并报告了至少两个提示条件及操纵程序；但没有报告操纵检验，条件分配也仅隐含为同题/多模型比较。 |
| A2 | 因变量 | 0.5 | PDF_PAGE_5: §4.4 “we use accuracy... Acc = Nunk /N”；HarmfulQ “manually label model outputs as encouraging or discouraging”。 | 因变量指标与计分方式明确；但未报告评分者信度、效度证据或连续指标预处理/端点效应说明。 |
| A3 | 控制变量 | 0.5 | PDF_PAGE_4: “To reduce the effect of positional bias, we randomly shuffle the type of answer...”；PDF_PAGE_5: “two prompt formats”及“temperature = 0.7, max_tokens = 256”。 | 报告了若干控制手段（提示格式、选项位置随机化、统一 API 参数），但未系统列出控制变量清单及逐一控制方式。 |
| A4 | 混淆变量 | 0.5 | PDF_PAGE_7: §6 “Differences in instruction following and RLHF across these models may confound the isolated impact of CoT...”；PDF_PAGE_9 讨论模型推广限制。 | 识别了指令微调/RLHF 与模型规模等潜在混淆，并用多模型和 Flan 作为补充；但未系统报告残余混淆或敏感性分析。 |
| A5 | 调节变量 | 0 | PDF_PAGE_6-7: §5.3 报告 “harms induced by CoT appear to get worse as model scale increase”，但未给出模型规模×CoT 的正式交互检验。 | 论文提出/讨论了随规模与指令微调变化的趋势，但没有正式交互项检验或简单斜率统计，故按调节分析核心要求判 0。 |
| A6 | 中介变量 | NA | — | 研究模型不包含中介变量，也未提出中介假设或做直接/间接效应分解。 |
| A7 | 操作性定义 | 1 | PDF_PAGE_4-5: §4.2-4.4 描述 Standard/CoT 操作与评分公式；PDF_PAGE_13: Appendix A 给出完整提示模板。 | 自变量操纵步骤、因变量记录与计分方式均可复现，达到逐构念操作化要求。 |
| A8 | 水平数与类型 | 0.5 | PDF_PAGE_4: §4.2 两种提示条件；§4.3 两种提示格式；PDF_PAGE_5: 多个 davinci 模型。 | 报告了水平数与各水平标签；但未明确水平类型、间距/全距及连续模型规模的中心化等说明。 |
| A9 | 单一操作化的风险 | 1 | PDF_PAGE_2: “reformulate three benchmarks measuring representational bias”；PDF_PAGE_9: “general agreement across our analyses mitigates the flaws of each individual benchmark”。 | 关键构念采用多个基准与多种模型/提示格式操作化，并报告了跨分析总体一致的会聚性证据。 |
| A10 | 单一方法的风险 | NA | — | 该研究不是人类自陈式同源测量；自变量为提示操纵，因变量为模型行为输出，不涉及共同方法偏差意义上的同源自评。 |
| B1 | 被试间设计 | NA | — | 无人类被试组间分配；同一基准问题在 Standard 与 CoT 条件下被独立调用，不存在独立被试组。 |
| B2 | 被试内设计 | NA | — | 虽然同一批问题在多条件下比较，但各条件为独立 API 调用，无时间顺序或被试内顺序平衡设计。 |
| B3 | 混合设计 | NA | — | 不存在被试组间/组内混合设计。 |
| B4 | 因子设计 | 0 | PDF_PAGE_5: Table 2 交叉呈现 CoT/No CoT、两种提示格式和多个模型；但 HarmfulQ 未完全按提示格式交叉，且无完整设计矩阵/ANOVA。 | 有多因素比较结构，但不是完整报告的设计矩阵与交互统计；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | PDF_PAGE_5-6: Table 2 与 §5 报告 CoT 相对 Standard 的平均百分点差异及 95% CI。 | 报告了 CoT 主效应式差异与区间，但未报告 F/df/效应量，也未在交互显著时声明解释受限。 |
| B6 | 交互作用 | 0 | PDF_PAGE_6-7: 规模与指令微调趋势以描述性比较呈现；未报告 CoT×模型/规模交互统计检验。 | 论文讨论了不同模型/规模下的趋势，但没有正式交互检验、简单主效应或校正后比较。 |
| B7 | 区组设计 | NA | — | 未使用区组或分层随机设计。 |
| B8 | 拉丁方 | NA | — | 未使用拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；提示条件由研究者设定，不是非随机分组的人类干预研究。 |
| B10 | 被试内设计的适用条件 | NA | — | 没有人类被试内处理顺序设计，不涉及处理可逆性/迁移对称性论证。 |
| C1 | 随机化 | NA | — | 无人类被试或独立实验单位被随机分配到互斥条件；选项位置随机化属于 E1/J1，不是条件分配随机化。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需要平衡。 |
| C3 | 恒定 | 0.5 | PDF_PAGE_5: 使用 “standard parameters... temperature = 0.7, max_tokens = 256”，并统一评估参数；PDF_PAGE_9 讨论模型推广限制。 | 报告了主要恒定 API 参数与部分外部效度限制，但未系统列出所有恒定变量及其水平。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 未把混淆变量作为协变量或区组纳入统计模型；模型/提示格式是比较条件而非协变量调整。 |
| C6 | 盲法 | 0 | PDF_PAGE_5: §4.4 “we manually label model outputs as encouraging or discouraging”；全文未报告评分者盲法。 | 有害输出的人工标注可能受条件可见性影响，且未报告对评分者施盲或盲法成功检验。 |
| C7 | 平衡的层级 | NA | — | 无被试内顺序平衡层级。 |
| D1 | 练习效应 | NA | — | 每个提示条件为独立调用，无练习块或上下文内学习顺序。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳风险；API 批量评测不涉及休息安排。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各条件独立调用且不共享对话上下文，无跨条件残留/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或顺序设计。 |
| D5 | 范围效应 | NA | — | 因变量为 accuracy/有害输出率等客观判定指标，不是主观量表绝对判断。 |
| E1 | 位置 / 顺序偏差 | 0.5 | PDF_PAGE_4: “To reduce the effect of positional bias, we randomly shuffle the type of answer associated with each of the options (A), (B), (C)”。 | 明确报告了选项位置随机化以控制位置偏差；但未报告随机化方案细节、各位置出现次数或位置×正确率。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无反向计分题问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试可推断研究假设；任务是模型提示评测，不存在人类需求特征。 |
| E5 | 实验者效应 | NA | — | 数据采集由 API 自动完成；仅对 HarmfulQ 输出做人工毒性标签，不涉及主试-被试实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | PDF_PAGE_5-7: Table 2/Table 3 报告均值及 95% CI；如 TD3 CrowS Pairs 为 “100 ± 0%”。 | 报告了均值与区间，可看出部分条件接近上限；但未报告偏度/端点频率，也未讨论天花板效应或任务难度校准。 |
| E7 | 共同方法偏差 | NA | — | 非自陈式多构念测量，无同源测量比例或共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | PDF_PAGE_5: “generate 5 completions... compute 95% confidence intervals”；Table 2 报告百分点差异。 | 报告了效应量式差异和 95% CI，并报告多个分析；但无样本量/功效依据，也未说明多重比较校正。 |
| F2 | 内部效度 | 0.5 | PDF_PAGE_4-5: 随机打乱选项位置、使用两套提示格式与统一参数；PDF_PAGE_7 讨论指令微调混淆。 | 对部分内部效度威胁有控制与讨论；但无分配隐藏、基线等价性、被试流向/损耗等报告（LLM 评测中部分不适用）。 |
| F3 | 构念效度 | 0.5 | PDF_PAGE_2-3: 使用 CrowS-Pairs、StereoSet、BBQ 与自建 HarmfulQ；PDF_PAGE_9 讨论基准局限；但无评分者信度或操纵检验。 | 有既有基准效度和多操作化证据，但缺少信度统计、操纵检验与人工标注一致性报告。 |
| F4 | 外部效度 | 0.5 | PDF_PAGE_3: 报告各基准样本量；PDF_PAGE_9: 讨论 “Generalizing beyond GPT-3” 等边界。 | 报告了数据来源与部分推广边界；但模型/基准代表性有限，未报告跨情境复现实验。 |
| G1 | 分析单位 | 0.5 | PDF_PAGE_5: §4.4 按问题计算 accuracy，§4.5 对每条件生成 5 次并汇总 CI。 | 分析层级隐含为基准问题/生成结果，但未明确说明分配层级与统计层级的匹配，也未处理问题嵌套于数据集的结构。 |
| G2 | 随机效应 | NA | — | 无人类被试随机效应需求；模型变体作为固定比较条件处理，未做混合模型。 |
| G3 | 材料作为随机效应 | 0 | PDF_PAGE_3: 抽样 1508 句及 1100 个 BBQ 问题；PDF_PAGE_5 仅按条件汇总 accuracy，未报告 item random effect 或准 F 比。 | 材料/问题来自有限基准样本，但分析未把项目作为随机效应，限制了对材料总体的推广。 |
| G4 | 统计功效 | 0.5 | PDF_PAGE_5: 每条件 5 次生成并报告 95% CI；全文无事前功效分析。 | 报告了效应量式差异与 CI，但缺少目标功效、预期效应量和样本量推导。 |
| G5 | 研究者自由度 | 0.5 | PDF_PAGE_5: HarmfulQ 通过 TF-IDF 相似度与人工复核去除重复问题；各基准与条件多数报告；无预注册/终点调整说明。 | 报告了部分排除规则与多个因变量/条件，但未完整区分验证性与探索性分析、样本量停止规则或所有分析决策。 |
| G6 | 预先设定 / 预注册 | 0 | PDF_PAGE_16: ACL 责任清单未见预注册信息；全文无注册平台/编号。 | 无公开预注册，也未区分预注册验证性分析与事后探索性分析。 |
| J1 | 位置偏差 | 0.5 | PDF_PAGE_4: 选项位置随机 shuffle；PDF_PAGE_5: 报告模型版本、temperature=0.7、max_tokens=256 与 5 次生成。 | 有位置反平衡/随机化且报告了裁判/生成参数；但未报告位置翻转率或位置×正确率曲线。 |
| J2 | 冗长偏差 | NA | — | 不使用 LLM-as-judge 评估开放生成质量；因变量为偏见选择正确率或人工有害性标签，不涉及长度被误当质量。 |
| J3 | 谄媚 | NA | — | 无用户先验立场或反馈式对话操纵，不评估谄媚。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 作为裁判；评估基于答案匹配或人工毒性标签。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 研究明确为零样本（zero-shot）设置，不使用 few-shot in-context 示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | PDF_PAGE_13: Appendix A 提供两套完整提示模板；PDF_PAGE_4: §4.3 使用 BigBench CoT 与 Inv. Scaling 两格式。 | 公布了完整模板并比较两种格式；但无版本号、敏感性消融、dev/test 划分或 prompt 搜索过程报告。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长文档、RAG 或长上下文信息位置实验。 |
| J8 | 温度与采样随机性 | 0.5 | PDF_PAGE_5: “temperature = 0.7, max_tokens = 256”，生成 5 completions，报告 95% CI 与 API 评估日期。 | 报告了主要采样参数、重复次数与区间；但未报告 top-p/top-k、随机种子或精确 API snapshot。 |
| J9 | 重复与文本退化 | 0.5 | PDF_PAGE_5: 报告 temperature 与 max_tokens；PDF_PAGE_7 提到 CoT 输出更详细，但无 repetition penalty/退化率。 | 有部分解码设置，但未系统报告解码策略、重复率/退化率或截断比例。 |
| J10 | 分词效应 | NA | — | 所有数据集为英文，无跨语言/跨脚本比较，不涉及分词效率混淆。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | PDF_PAGE_3: 使用公开的 CrowS-Pairs、StereoSet、BBQ；全文未报告训练截止日期与测试集重叠检查。 | 未做基准污染/数据泄漏检测，也未对照模型训练数据截止日期。 |
| J12 | 基准饱和 | 0.5 | PDF_PAGE_5-7: Table 2/3 中部分分数很高，如 TD3 CrowS Pairs “100 ± 0%”、StereoSet “96 ± 0%”。 | 报告了基准分数和高水位，但未讨论饱和问题，也未改用连续指标或更难子集；部分条件接近天花板。 |
| J13 | 指令遵循 | NA | — | 因变量不是指令遵循准确率；研究比较 CoT 对偏见/毒性的影响，而非指令约束遵循。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | PDF_PAGE_4-5: 使用 “So the answer is” 做 Answer Extraction 并抽取选项；未报告格式合法率或重试策略。 | 描述了答案抽取式格式约束，但未报告格式失败率、重试/后处理规则，也未将格式失败与内容错误分开。 |
| J15 | 越狱稳健性 | 0 | PDF_PAGE_5: HarmfulQ 由自然有害问题组成，评估 encouraging/discouraging 输出；未测试对抗越狱攻击。 | 属于安全/有害输出评估，但只报告自然提示下的拒绝/非毒性率，没有对抗攻击成功率或攻击族信息。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文是 NLP 公平性/安全基准评测，不主张将 LLM 作为心理学被试测量人类同名构念，也未做人类构念对照。 |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | PDF_PAGE_6-8: 报告 GPT-3 与 Flan 不同规模下的 accuracy 曲线及 95% CI，并讨论 CoT 随规模变化的趋势。 | 报告了规模曲线及区间，但主要使用离散 accuracy 指标，未展示连续指标或多 seed 曲线来排除指标诱导的“涌现”假象。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究没有训练、RL、best-of-N 或针对代理指标的优化过程，只是评测现有模型。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | PDF_PAGE_5: 5 次生成、95% CI、模型名称与 API 评估日期；未报告随机种子、逐题日志或配对检验。 | 有重复次数、区间与模型版本/日期，但缺少精确 snapshot、配对比较和原始推理日志，复现性报告不完整。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示评测，无多轮对话历史积累，也不主张多轮部署一致性。 |

## 编码小结
论文清楚描述了 CoT 与 Standard 两种提示条件、两套提示模板、多个偏见/有害性基准及主要评分方式，并用 5 次生成和 95% CI 汇总结果；但统计推断以描述性百分比差异为主，缺少正式交互检验、功效分析、预注册、项目随机效应及若干 LLM 评估风险控制（污染、饱和、位置翻转率、格式合法率等）的系统报告。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
