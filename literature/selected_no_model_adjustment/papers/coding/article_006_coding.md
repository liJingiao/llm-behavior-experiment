# article_006 | Meaning Beyond Truth Conditions: Evaluating Discourse Level Understanding via Anaphora Accessibility (Zhu, Zhou, Charlow, Frank) | 2025 (arXiv 2502.14119v1)

研究类型概述：LLM（6 个模型，基于 token 概率/surprisal、SLOR 的最小对比评测）加一项人类基线实验（Prolific，104 人，二选一强迫选择可接受度判断）。自变量为语境句结构（existential/every/if/whenever、negation/double negation、either-or/or/conjunction 等最小对比条件）及模型/人类；因变量为"符合理论预测方向的不等式比例（% Expected）"，由 surprisal 差或 SLOR 比较得到。

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 1 | §3.1 p3-5：例(2)-(5)给出各条件，如 "EXISTENTIAL: A farmer worked in the field. / EVERY: #Every farmer worked in the field." | 自变量（语境句类型）及各水平以句例明确列出；LLM 评测无需操纵检验，人类端以 filler 做注意检查 |
| A2 | 因变量 | 0.5 | §3.2 Metrics p5: "we take the surprisal (i.e., the negative log probability) assigned by the model to individual tokens"; §4 "difference-of-difference metric ... We binarize the comparison of each trial" | 指标、计分方式明确；缺：对指标有效性的信效度证据；二值化导致信息损失、天花板（多处 ceiling）未处理；Eq.(1) 写法与 surprisal 定义（缺负号）也不一致 |
| A3 | 控制变量 | 0.5 | §3.2 Corpus p5: "manually constructed 32 semantically plausible simple sentence frames ... inspected by linguistics experts"; 附录 A 同一批 filler | 控制了句框语义合理性、continuation 相同（§5 "every pair of sentences we compare shares the continuation"）；缺句长/词频等控制的系统清单，Exp.3 各句不共享语境与续句（§6） |
| A4 | 混淆变量 | 0.5 | §5 p7-8: "adding in fact also flips the direction of the Exi>Neg comparison"; §4 p6-7 telescoping、subject bias 讨论 | 识别并检验了词汇项（in fact, either）、复杂度、telescoping 等混淆并作消融；但未做系统的残余混淆/敏感性分析 |
| A5 | 调节变量 | NA | — | 无调节假设；模型/人类差异为描述性比较 |
| A6 | 中介变量 | NA | — | 无中介 |
| A7 | 操作性定义 | 1 | §3.1 构念（anaphora accessibility）以例句+理论条件定义；Eq.(2)-(12) 给出判定不等式；§3.2 | 可复现程序（模板、指标公式、对比方向）明确 |
| A8 | 水平数与类型 | 1 | §3.1.1-3.1.3 与 附录 A: "11 comparison types (3 in Experiment 1, 4 each in Experiments 2 and 3)" | 各水平标签和取值明确，名义水平 |
| A9 | 单一操作化的风险 | 0.5 | §4 p6: 以 he-/it- 两种 continuation 重复；§5 加 "in fact" 变体；§7 Limitations 只测限定模型/构式 | 对关键构念采用多种构式（3 类算子）与变体，指标在不同实验中不同（surprisal、SLOR）；但对推广限制的讨论集中于模型和构式范围，未专门针对操作化 |
| A10 | 单一方法的风险 | NA | — | 人类判断与模型概率为独立来源，非自变量-因变量同源问卷 |
| B1 | 被试间设计 | NA | — | 人类实验各被试均接触多个条件，非被试间设计 |
| B2 | 被试内设计 | 0.5 | 附录 A p11: "Each participant received 22 test items and 44 filler items, which sums to a total of 66 trials." | 属被试内/重复测量（每人多条件最小对比）；缺顺序平衡方案和各顺序分配的报告 |
| B3 | 混合设计 | NA | — | 未按组间/组内因素建模；模型 vs 人类仅为描述性对比 |
| B4 | 因子设计 | NA | — | 无完全交叉的因子分析 |
| B5 | 主效应 | NA | — | 无因子主效应检验 |
| B6 | 交互作用 | NA | — | 无交互检验 |
| B7 | 区组设计 | NA | — | 无区组 |
| B8 | 拉丁方 | NR | 附录 A 仅说 "The experiment was also set up such that each test item was rated by at least 5 participants" | 人类端 22 个测试项如何从 352 对中分配给被试、是否用拉丁方，文中未说明；视为被试内设计下的 NR |
| B9 | 准实验设计 | NA | — | 模型/人类为被比较的群体而非需随机分配的处理 |
| B10 | 被试内设计的适用条件 | NR | — | 人类被试在各条件间是否存在启动/迁移（同一句框重复出现）未论证，文中信息不足 |
| C1 | 随机化 | NR | 附录 A p11 未提及项目呈现顺序/选项位置的随机化 | 人类试次顺序和 Sentence 1/2 位置是否随机，文中未说明 |
| C2 | 平衡 | NR | 同上 | 无条件顺序平衡的报告 |
| C3 | 恒定 | 1 | §5 p7: "every pair of sentences we compare shares the continuation but not the context sentences"; §3.2 同一 A100/API 推理 | 列出恒定要素（续句、模板、句框）；对外部效度限制在 Limitations 中有所涉及 |
| C4 | 匹配 | NA | — | 无匹配 |
| C5 | 纳入为变量 | NA | — | 无协变量分析 |
| C6 | 盲法 | NA | — | 评测为自动指标，人类任务 2AFC 无评分者 |
| C7 | 平衡的层级 | NR | — | 同 C2 |
| D1 | 练习效应 | NR | 附录 A 仅有 44 filler | 未说明是否有练习试次或试次位置控制 |
| D2 | 疲劳效应 | NA | — | 66 试次（约 12 分钟：$3 对应 $14.41/小时）较短，文中未讨论；对 LLM 部分不适用 |
| D3 | 延滞/迁移效应 | NR | — | 同 B10 |
| D4 | 不对称迁移 | NR | — | 同 B10 |
| D5 | 范围效应 | NA | — | 二选一强迫选择而非绝对量表评分 |
| E1 | 位置/顺序偏差 | NR | 附录 A p11 | 未报告 Sentence 1/Sentence 2 位置与呈现顺序是否随机或平衡 |
| E2 | 默认赞同 | NA | — | 二选一，无量表题 |
| E3 | 极端/中间反应倾向 | NA | — | 无量表 |
| E4 | 需求特征 | NR | — | 未说明被试对研究目的的知晓或事后检查 |
| E5 | 实验者效应 | NA | — | 在线自动化 Gorilla 实验，无主试交互 |
| E6 | 天花板/地板效应 | 0.5 | §4 p6: "LLMs continue to score at ceiling"; "humans scored even higher at ceiling" | 观察并讨论了多处天花板，但未做难度校准，亦未将其作为需处理的问题 |
| E7 | 共同方法偏差 | NA | — | 非同源问卷测量 |
| F1 | 统计结论效度 | 0.5 | Fig.6-9 带误差棒；§4-6 以 % Expected 与 50% 对比 | 呈现误差棒，但无显著性检验、效应量/CI 数值、多重性校正、样本量依据 |
| F2 | 内部效度 | 0.5 | 附录 A p11: "Participants who scored below 90% accuracy on the filler items were excluded"; "85 of them (81.73%) passed the filler check" | 报告了排除标准和通过率；缺随机分配程序与基线等价（无分组）|
| F3 | 构念效度 | 0.5 | §3.1 理论依据（动态语义）；§5 讨论词汇项对结果的影响 | 有理论效度和变体检验以区分"词汇线索 vs 结构知识"；缺指标信度、人类判断一致性等 |
| F4 | 外部效度 | 0.5 | 附录 A: "104 native speakers of English ... reside in the United States"; Limitations p9 | 报告样本来源与特征，并在 Limitations 说明未测 GPT-4o 等 SOTA 模型；缺其他语言/人群的推广讨论 |
| G1 | 分析单位 | 0.5 | §4 "We binarize the comparison of each trial" | 分析单位为试次/句对，已明确；被试内和句框嵌套结构未建模处理 |
| G2 | 随机效应 | 0 | Fig.6-9 仅 % Expected 与误差棒 | 未使用混合模型，未声明被试/项目作随机效应 |
| G3 | 材料作为随机效应 | 0 | §3.2: "we manually constructed 32 semantically plausible simple sentence frames" | 句框（材料）为抽样的 32 个，但分析中未作随机因素，仅汇总比例 |
| G4 | 统计功效 | 0 | 附录 A: "each test item was rated by at least 5 participants" | 无功效分析；仅有每项最少评分数的设计说明，无样本量依据 |
| G5 | 研究者自由度 | 0.5 | 附录 A: 排除标准 <90% filler；§3.2 "9816 experimental sentences"; §5 "in fact" 变体 | 数据排除规则报告；未说明 32 框是否全部保留、全部指标是否都已报告；未区分验证与探索分析 |
| G6 | 预先设定/预注册 | 0 | — | 全文无预注册信息 |
| J1 | 位置偏差 | NA | — | 以概率比较，无选项位置；该偏差对 token 概率评测不适用 |
| J2 | 冗长偏差 | NA | — | 无 LLM 裁判；但 SLOR 已用长度归一（|s|），属指标层面 |
| J3 | 谄媚 | NA | — | 无对话/用户立场 |
| J4 | 自我偏好 | NA | — | 无 LLM-as-judge |
| J5 | 少样本示例选择与排列偏差 | NA | — | 零样本概率评估，无 few-shot |
| J6 | 提示敏感性/脆弱性 | 0.5 | §5 "Influence of Specific Lexical Items" 加 "in fact" 变体，he/it 变体（Fig.7） | 对语境/续句措辞做了变体消融，并据此得出"依赖词汇项"的结论；无提示模板版本化（非提示式评测），也无 dev/test 分离 |
| J7 | 长上下文信息位置效应 | NA | — | 句子/短篇语境，非长上下文 |
| J8 | 温度与采样随机性 | NA | — | 评估为确定性概率打分，无采样解码 |
| J9 | 重复与文本退化 | NA | — | 无文本生成 |
| J10 | 分词效应 | 0.5 | §6 p8: "unigram probabilities ... obtained from the tokenizers of the Llama3 family and the GPT3 family, respectively." | 提到不同模型族用各自 tokenizer 计算 unigram 概率及 SLOR 对长度归一；未记录 tokenizer 版本，也未控制 token 数差异对 surprisal 之和的影响 |
| J11 | 测试集污染/数据泄漏 | 0 | — | 自建刺激由 GPT-4o 辅助生成，未评估与训练数据的重叠，未对照训练截止；Limitations 亦未提及 |
| J12 | 基准饱和 | 0.5 | §4 "LLMs continue to score at ceiling"; §6 "models achieved ceiling performance" | 识别出多项对比已天花板，但未换用连续指标或更难子集 |
| J13 | 指令遵循 | NA | — | 非指令遵循测量 |
| J14 | 输出格式约束/结构化输出 | NA | — | 无结构化输出 |
| J15 | 越狱稳健性 | NA | — | 非安全评估 |
| J16 | LLM 作为被试的范式定位 | 1 | §3.2 Metrics: "We adopt the evaluation paradigm in Futrell et al. (2019) that considers LLMs as psycholinguistic subjects."; Limitations "Behavioral versus Mechanistic Level Evaluations" | 明确界定 LLM 行为构念（surprisal 偏好 vs 人类可接受度判断），并与人类基线并行对照，讨论两者异同（telescoping、subject bias、词汇依赖 vs 结构抽象），且承认仅在行为层面 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无规模/训练曲线上的涌现宣称（模型规模作比较而非曲线） |
| J18 | 指标博弈与奖励过优化 | NA | — | 无优化目标 |
| J19 | 评估可复现性与种子/检查点依赖 | 0.5 | §3.2 Model p5: "Llama3-2-1B, Llama3-2-3B, Llama3-1-8B and Llama3-1-8B-Instruct ... babbage-002 and davinci-002"; 脚注 "See the GitHub link for the unigram probability results" | 给出模型标识和硬件；打分确定性故无需种子/重复，但缺 CI、配对检验；GitHub 链接在文中提及但正文未给出 URL |
| J20 | 多轮对话中的一致性衰减 | NA | — | 非多轮对话 |

## 编码小结
本篇是"LLM 作心理语言学被试"的最小对比评测，加一个 Prolific 人类 2AFC 基线；J16 记 1，J 节中凡涉及生成/裁判/采样/多轮的组件基本 NA。人类实验部分对顺序、随机化、平衡、练习等细节几乎不报告，故 B8/B10/C1/C2/C7/D1/D3/D4/E1/E4 记 NR（文本信息不足而非确认未做）。统计方面仅有柱状图与误差棒，无检验、功效、随机效应和预注册，G2/G3/G4/G6 记 0，G2/G3 的判定依据是"读到分析仅为比例汇总"。不确定处：A2 将指标二值化及公式小错归入 0.5；J10 的分词器信息是否足以达到基本要件；B2 因每人只看部分条件是否算典型被试内设计。
