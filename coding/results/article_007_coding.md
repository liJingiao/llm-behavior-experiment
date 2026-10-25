# article_007 | When the LM misunderstood the human chuckled: Analyzing garden path effects in humans and language models (Amouyal, Meltzer-Asscher, Berant) | 2025 (arXiv 2502.09307v1)

研究类型概述：人类（Prolific 单试次在线理解实验）加大规模 LLM 评测（GPT/Llama-3/Qwen-2.5/Gemma-2/OLMo 共约 50 个模型/检查点，few-shot 提示取答案 token 概率）。自变量为句法结构（GP vs non-GP）、宾语合理性（plausible/implausible）、动词类型（optionally transitive vs reflexive/unaccusative）及动词及物倾向；因变量为理解问题的正确率（LLM 为正确答案概率），并以 Kendall tau/Spearman 比较人与模型，另做复述与文生图验证。
- **研究构念（Construct）**：花园路径句加工与句法重分析（garden-path processing and syntactic reanalysis）｜CA 构念锚定：句法加工（syntactic processing, `trm_4a3fd79d0b34b`）；句法分析（syntactic parsing, `trm_4a3fd79d0b340`）；句子理解（sentence comprehension, `trm_4a3fd79d0b892`）
- **实验任务与范式（Task / Paradigm）**：人类（Prolific 单试次在线理解实验）加大规模 LLM 评测（GPT/Llama-3/Qwen-2.5/Gemma-2/OLMo 共约 50 个模型/检查点，few-shot 提示取答案 token 概率）。自变量为句法结构（GP vs non-GP）、宾语合理性（plausible/implausible）、动词类型（optionally transitive vs reflexive/unaccusative）及动词及物倾向；因变量为理解问题的正确率（LLM 为正确答案概率），并以 Kendall tau/Spearman 比较人与模型，另做复述与文生图验证。｜CA 任务锚定：阅读广度任务（reading span task, `trm_4c40d168898db`）；句图匹配任务（sentence-picture matching task, `trm_4f241e8a01052`）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | §3.1 Materials p4: "we manipulated the structure of the sentence (GP or non-GP) and plausibility of the noun as the verb's object (plausible or implausible)"; Table 1 | 自变量（句法结构、宾语合理性、动词类型）与各水平明确，合理性经 GPT-4 预评筛选；但人类被试分配到各水平的具体随机化机制未完整报告，按统一级联口径记 0.5。 |
| A2 | 因变量 | 0.5 | §3.1: "Each of the 456 sentence-question pair"; "GP question targets the potential misinterpretation"; §4.1 "We extract the probabilities of the correct and incorrect answers tokens" | 指标、计分、正确答案规则（"yes" 为错）明确；缺信效度证据（如题目有效性）、LLM 的概率与人类二分正确率尺度不同未讨论 |
| A3 | 控制变量 | 0.5 | §3.1 Procedure p4: "Sentences were displayed word-by-word, with each word shown for 400ms and a 100ms blank screen between words"; "The single-trial design prevents fatigue ... and learning effects"; 材料为最小对（Appendix B） | 列出呈现速度、问句时限、单试次；缺对词频、句长等的系统控制说明 |
| A4 | 混淆变量 | 0.5 | §3.1 "The simple question probes basic understanding"; §3.2 verb-bias 与 accuracy 相关 "weak (≤0.19)" | 以简单问题作理解基线，并分析动词及物倾向这一潜在混淆；未系统讨论材料来源（24 条原材料+21 条自编）造成的差异，也无敏感性分析 |
| A5 | 调节变量 | 0 | §3.2: "the effect of structure (GP vs. non-GP was stronger for the former verbs)"; Appendix C Table 3 | 报告了结构×动词类型的差异并分别做 GLMM，但未做正式交互项检验与简单斜率；因提出条件/调节性比较却未报告乘积项交互统计检验，按级联规则基本要件未达成记 0。 |
| A6 | 中介变量 | NA | — | 无中介假设（复述/生图任务为验证，非中介） |
| A7 | 操作性定义 | 1 | §3.1 Materials；§6.1 三项自动指标 "a format metric ... a found-verb metric ... a correct-paraphrase metric"；§6.2 四类人工图像标签 | GP、合理性、动词类型、理解错误均有可复现操作化；Appendix B 给出全部句子 |
| A8 | 水平数与类型 | 1 | §3.1: "45 sentences sets with optionally transitive verbs ... 24 additional sets with reflexive/unaccusative verbs"; Appendix A 列出动词及物倾向 0.102–0.775 | 水平数、取值和类型（名义+连续的 transitivity bias）明确 |
| A9 | 单一操作化的风险 | 1 | Abstract: "we test LLM comprehension ... with paraphrasing and text-to-image generation tasks"; Limitations p9: "our focus was limited to measuring reading comprehension on Subject/Object GP sentences" | 理解问答、复述、文生图三种操作化，并在局限中说明范围限制 |
| A10 | 单一方法的风险 | NA | — | 人类与模型数据来源独立，不涉及同源问卷自变量-因变量 |
| B1 | 被试间设计 | 0.5 | §3.1: "Participants completed two practice items, followed by one experimental sentence and one question."; "shown to 10 participants" | 每名被试仅看一个实验句，实质为被试间；但未明说如何分配到各条件（是否随机） |
| B2 | 被试内设计 | NA | — | 人类为单试次；LLM 各"被试"遍历所有条件但属重复评测，文中不作被试内设计表述 |
| B3 | 混合设计 | NA | — | 未按组间/组内因素建模 |
| B4 | 因子设计 | 0 | §3.1 Materials: 结构（2）×合理性（2）完全交叉，另一组动词类型仅在 plausible 中（不完全交叉）；Fig. 1 | 主要 2×2 交叉且报告条件均值；但整体并非完全因子（reflexive 仅 GP×nonGP），也无每格 n 和因子交互完整统计；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | §3.2: "the difference between GP and non-GP sentences was significant for implausible (p = .019) and reflexive (p = 2.52e-13) sets"; Table 3 Estimate/P-value | 报告了估计值与 p，缺 SE/CI/效应量；GLMM 分条件而非联合模型 |
| B6 | 交互作用 | 0 | §3.2: "the effect of structure ... was stronger for the former verbs" | 仅描述性提及，无正式交互项检验和事后比较；因未报告交互项的正式统计检验结果，按级联规则基本要件未达成记 0。 |
| B7 | 区组设计 | NA | — | 无区组 |
| B8 | 拉丁方 | NA | — | 单试次，无需拉丁方 |
| B9 | 准实验设计 | NA | — | 人类实验为分配式在线实验，非准实验 |
| B10 | 被试内设计的适用条件 | NA | — | 未采用被试内；作者以单试次规避（见 A3） |
| C1 | 随机化 | 0 | §3.1 (p.4): "Each of the 456 sentence-question pair was shown to 10 participants" | 人类单试次被试间设计将每名被试分配至 456 个句子-问题对之一，但未报告随机分配方法、随机数生成工具及分配隐藏机制，基本要件未达成，记 0。 |
| C2 | 平衡 | NA | §3.1 (p.4): "Participants completed two practice items, followed by one experimental sentence and one question. The single-trial design..." | 人类实验为单试次被试间设计（每人仅完成 1 道正式实验题），LLM 端为无状态独立调用，均无被试内条件顺序平衡需求，故记 NA。 |
| C3 | 恒定 | 1 | §3.1 Procedure: 呈现时长、问题时限 5 秒、练习 2 题；§4.1 同一提示格式 | 恒定变量与具体水平明确 |
| C4 | 匹配 | 0.5 | §3.1: "We select pairs where the plausible sentence had a rating of at least 3 points higher than its implausible counterpart" | 材料层面按 GPT-4 合理性评分匹配最小对；未报告匹配后均衡性（如词频、长度）检验 |
| C5 | 纳入为变量 | 0.5 | §3.2: 动词 transitivity bias 与 accuracy 的 Pearson 相关 | 测量并分析了该变量，但未作为协变量纳入模型（仅相关） |
| C6 | 盲法 | NA | — | 人类在线自动化任务；图像人工标注的盲法见 E5 |
| C7 | 平衡的层级 | NA | §3.1 (p.4) 单试次被试间设计说明 | 同 C2，人类单试次被试间设计与 LLM 独立调用均无被试内条件顺序平衡层级需求，故记 NA。 |
| D1 | 练习效应 | 0.5 | §3.1: "Participants completed two practice items ... The single-trial design prevents fatigue (Christianson et al., 2022) and learning effects (Fine et al., 2013)." | 人类实验设置了 2 道练习题并以单试次设计规避练习效应（达成基本要件），但未报告练习结束标准或试次位置协变量分析，按统一级联口径记 0.5。 |
| D2 | 疲劳效应 | NA | §3.1 (p.4): "The single-trial design prevents fatigue ... average completion time was 1:50 minutes" | 人类实验为单试次被试间设计（B2=NA）且总时长仅约 1 分 50 秒（远短于 10 分钟），LLM 端为独立调用，按编码规则属无疲劳风险的极短被试间任务，记 NA。 |
| D3 | 延滞 / 迁移效应 | NA | §3.1 (p.4) 单试次被试间设计与 LLM 独立会话调用 | 人类实验为单试次被试间设计（每人仅接触单一实验条件，B2=NA），LLM 端为每题独立调用重置上下文，不存在跨条件延滞/迁移，按编码规则记 NA。 |
| D4 | 不对称迁移 | NA | — | 无多条件迁移（单试次） |
| D5 | 范围效应 | NA | — | 二选一问答而非量表评分 |
| E1 | 位置 / 顺序偏差 | 0.5 | §4.1 (p.5): "Each sentence is presented to the model 8 times, using two system prompts and four example orderings" | LLM 端对少样本示例顺序采用了 4 种排列组合进行反平衡，达成顺序控制基本要件；但未报告完整排列细节及人类端 Yes/No 选项位置随机化，故记 0.5。 |
| E2 | 默认赞同 | 0 | §3.1 问题均以 "Did ...?" 询问，正确答案多为 No；§2 "we consider 'yes' to be a wrong answer" | 读到题目设计：GP 问题的正确答案固定为 No，未设反向题，也未讨论 yes 偏向可能混入理解错误；对"misinterpretation"的度量构念存在 yes-bias 混淆 |
| E3 | 极端 / 中间反应倾向 | NA | — | 二选一，无量表 |
| E4 | 需求特征 | NA | §3.1 (p.4) 逐词 400ms 呈现加 5 秒限时理解问答的单试次实验设计 | 人类实验采用限时逐词阅读与单试次理解判断范式，每名被试仅接触单个句子，无法合理推断跨条件的句法与宾语合理性假设，故记 NA。 |
| E5 | 实验者效应 | 0.5 | §6.2: "manually categorized the resulting images into four groups" | 人工分类图像，未说明标注者人数、是否盲、一致性，也未培训；人类实验端为自动化无实验者 |
| E6 | 天花板 / 地板效应 | 0.5 | §3.2: "The accuracy on simple questions was high (average 95.4%, minimum 92.4%, maximum 98.7%) ... average accuracy of 37.0% on GP questions"; §6.2 "almost all LLMs, the accuracy on the non-GP sentences is above 90%" | 报告了简单题近天花板（作为基线），GP 题 37%；多个 LLM 条件接近天花板/地板（如 Gemma-2B ≈0.001）仅陈列于 Table 4，未专门讨论其处理 |
| E7 | 共同方法偏差 | NA | — | 同 A10 |
| F1 | 统计结论效度 | 0.5 | Appendix C Table 3: "SentenceType: Estimate -0.46, P-Value: 0.069"; Fig.1 误差棒 | 报告估计和 p 值与 GLMM；缺 CI、效应量、多重性校正、样本量依据；LLM 比较未做检验 |
| F2 | 内部效度 | 0.5 | §3.1 单试次、10 人/项；§3.2 无排除标准描述 | 有设计层面控制；缺分配程序、被试流向与损耗（招募人数、排除）报告 |
| F3 | 构念效度 | 0.5 | §6 "the results mirror the sentence comprehension question results"; §6.1 AUC "minimal AUC being 0.595, the maximal 0.774 and the average 0.696" | 通过复述/文生图三任务做收敛验证；缺核心 DV 本身的信度；GP 正确答案 "No"（实为 not necessarily）的计分有效性未验证 |
| F4 | 外部效度 | 0.5 | §3.1 "Native English speakers were recruited via the Prolific platform"; Limitations p9 | 样本来源描述有限（人数、年龄等缺）；局限中说明仅 subject/object GP 且最新模型未纳入 |
| G1 | 分析单位 | 0.5 | Appendix C: 公式 "SentenceType + (1 + SentenceType \&#124;SetId)" | 以句组（SetId）为随机项，说明分析层级；被试嵌套（单试次，一人一观测）和模型家族嵌套未单独说明 |
| G2 | 随机效应 | 0.5 | Table 3 公式含 "(1 + ... \&#124;SetId)" | 说明了句组为随机效应及随机斜率结构；被试因单试次无需随机项但未说明；Reflexive 公式 "(1 + SetId)" 写法与其他不一致 |
| G3 | 材料作为随机效应 | 0.5 | Appendix C Table 3: "(1 + SentenceType \&#124;SetId)", "(1 + ManipulationType \&#124;SetId)" | 人类数据 GLMM 将材料集（SetId）作为随机截距/斜率纳入（达成基本要件），但主评测的 LLM 端分析仅按条件聚合而未将材料作为随机效应建模，故记 0.5。 |
| G4 | 统计功效 | 0 | §3.1 "shown to 10 participants" | 无功效分析或样本量依据，仅给每项人数 |
| G5 | 研究者自由度 | 0.5 | §6.1 "Models that scored below 90% accuracy in the format and found-verb metrics (Qwen2.5-1.5B, Qwen2.5-3B) were filtered out"; §4.1 脚注2 "We also experimented with chain-of-thought-prompting, which did not lead to a signifnicant change"; §6.2 脚注5 "We tried 3 other text-to-image models ... not good enough" | 报告了模型排除规则及若干未报告结果的探索；人类被试排除规则缺失；未区分验证性/探索性 |
| G6 | 预先设定 / 预注册 | 0 | p.1–18 全文（含方法、致谢、脚注与数据代码声明）均未提及公开预注册平台、注册编号或事前分析计划 | 全文无预注册（三个假设为文献推导，但未预注册） |
| J1 | 位置偏差 | NA | — | 单一 Yes/No 回答，无候选项位置（Yes/No 标签位置不涉及选项排列） |
| J2 | 冗长偏差 | NA | — | 无 LLM-as-judge |
| J3 | 谄媚 | NA | — | 无用户立场操纵 |
| J4 | 自我偏好 | NA | — | 无 LLM-as-judge（复述评估为规则化自动指标） |
| J5 | 少样本示例选择与排列偏差 | 0.5 | §4.1: "few-shot prompting ... The examples did not contain GP structures. Each model was prompted 8 times, using two system prompts and four example orderings."; Appendix D | 报告示例来源（非 GP）、4 例、4 种排列与 2 个 system prompt 并平均；缺标签比例（示例 Yes/No=2:2）的显式说明与示例选择敏感性分析 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | §4.1 "Each model was prompted 8 times, using two system prompts and four example orderings"; Appendix D、F 给出完整 prompt | 提供完整 prompt 并通过多版本平均缓解；未作逐版本敏感性分析、版本化与 dev/test 分离 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 短句任务 |
| J8 | 温度与采样随机性 | NA | — | 以答案 token 概率评估，无采样（论文未报告温度，因取概率）；复述/生图的采样超参未报告但并非核心 |
| J9 | 重复与文本退化 | NA | — | 核心任务非生成；复述任务以规则指标，解码未报告但不属核心 |
| J10 | 分词效应 | NA | — | 单语英语，各模型概率为答案 token 而非跨语言比较 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | §3.1: "24 coming from Christianson et al. (2001), 21 crafted for this study" | 材料部分取自公开文献（可能出现在训练数据），部分自编；论文未评估污染或与训练截止对照，亦未讨论，但有新编材料缓冲 |
| J12 | 基准饱和 | 0.5 | §6.1 "accuracy on the non-GP sentences is above 90%"; §4.2 "o1-preview ... 78%" | 报告水位并指出最强模型仍未饱和；未专门评估饱和或改用连续指标（实际用概率为连续指标） |
| J13 | 指令遵循 | 0.5 | §6.1 "format metric (verifying that the paraphrase consists of two sentences), a found-verb metric" | 复述任务有机器可判的格式/动词指标并据此过滤模型；非按约束类型拆分 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | §6.1 同上 "Models that scored below 90% accuracy in the format and found-verb metrics ... were filtered out" | 格式合法性与内容（correct-paraphrase）分开记录；未报告各模型格式合法率数值 |
| J15 | 越狱稳健性 | NA | — | 非安全评估 |
| J16 | LLM 作为被试的范式定位 | 1 | Intro p2: "whether the same aspects of GP structures cause processing difficulties in humans and LLMs"; Appendix D prompt "You are a linguistic experiment subject."; §5 对比同任务；§4.2 "there is no reason to suspect that they should suffer from the same processing difficulties that humans do" | 明确界定构念（GP 误解）、用同一任务对照人类，并讨论 LLM 与人类机制可能不同及其局限（仅行为层面、无阅读时间） |
| J17 | 涌现能力争议与指标诱导假象 | 0.5 | §5 Pretraining tokens: "In OLMo-7B, we see an increase in Kendall Tau correlation with the increase in number of pretraining tokens."; Table 4 | 展示随规模/训练 token 的曲线，用连续指标（概率与相关）；未宣称涌现，也无多 seed |
| J18 | 指标博弈与奖励过优化 | NA | — | 无优化 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | §4.1 Models 列出各家族与 OLMo 15 个检查点；§4.1 "prompted 8 times"; Table 4 | 模型与检查点标识较完整（OLMo 以 token 数标识）；GPT 系列无 snapshot 日期，无 CI/配对检验 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 单轮任务 |

## 编码小结
本篇属"人类单试次实验 + 大规模 LLM 同任务评测"的混合设计：人类端用单试次回避练习、疲劳与迁移（D1–D3 记 1），LLM 端以 few-shot 与多版本提示平均并给出 Appendix D/F 全部提示。材料作为随机效应（G3）与 LLM 范式定位（J16）较好，A9 以三种任务验证记 1。薄弱处：人类端被试分配、随机化、排除标准与功效均缺（C1/C2/C7/E1/E4 NR，G4/G6 0），LLM 端缺 CI/检验。E2 判 0 的理由是正确答案固定为 No 且未讨论 yes 偏向，此处有解释空间（也可视为 NA）；B1 因未说明分配机制记 0.5；J11 对公开材料污染的处理偏宽。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 C1（NR→0）, C2（NR→NA）, C7（NR→NA）, E1（NR→0.5）, E4（NR→NA）, A1（1→0.5）, D1（1→0.5）, D2（1→NA）, D3（1→NA）, G3（1→0.5）, B6（0.5→0）, B4（0.5→0）, A5（0.5→0）。
