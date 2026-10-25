# article_223 | Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data | 2025

研究类型概述：LLM 能力溯源的观察性/基准分析，辅以小规模 prompt 优化实验；分析单位为 n-gram pair/test example、模型规模与任务，不是人类被试实验。
- **研究构念（Construct）**：分布式记忆、泛化与任务类型下的知识使用规律｜CA 构念锚定：归纳推理（inductive reasoning, `trm_4a3fd79d0a590`）；推理（reasoning, `trm_4a3fd79d0aec1`）
- **实验任务与范式（Task / Paradigm）**：在翻译、事实问答、世界知识和数学推理任务上，比较现成模型输出概率与预训练语料task-gram分布，并沿模型规模和训练检查点追踪。（比较任务类型、模型规模、预训练检查点、n-gram配对和鼓励记忆/泛化的提示。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.9–10（p.9、p.10）Section 7 用 GPT4o 重写 prompt，以 WIMBD n-gram count 反馈分别最大化/最小化；p.17 Table 2 给出两套 prompt 与 avg 3-gram count；p.9 Table 1 比较 memorization/generalization prompt 下准确率。 | 主动操纵的 prompt 条件有明确两水平和操纵程序，并给出 n-gram count 作为操纵检查；但未明确随机/分配逻辑，且主分析多为观察性，故 0.5。 |
| A2 | 因变量 | 0.5 | p.5–6（p.5、p.6）WMT 用 BLEU，TriviaQA 用 exact match accuracy，MMLU 用最高预测概率选项 accuracy，GSM8K 因 <5% 改用 BERTScore；p.4 定义 Spearman ρ 为 Mem。 | 因变量指标与计分明确，但无信效度、连续指标预处理或天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | p.4（p.4）固定 Pythia 家族与 Pile/Dolma、固定任务；p.3（p.3）使用 minimal instruction template；p.5（p.5）WMT 用 greedily generated translation。 | 提到固定模型、语料、模板和解码，但未系统列控制变量清单与控制手段。 |
| A4 | 混淆变量 | 0.5 | p.5（p.5）用 n=8/14 n-gram overlap 去污染；p.6（p.6）承认性能曲线也可由泛化解释；p.16（p.16）不同余弦阈值敏感性；p.14（p.14）过滤方法敏感性限制。 | 识别污染、过滤阈值等威胁并做部分控制/敏感性，但未系统讨论残余混淆。 |
| A5 | 调节变量 | 0 | p.7–8（p.7、p.8）将 MMLU 分为 knowledge-intensive vs reasoning-intensive 并分别报告 Mem 曲线，但未报告正式交互检验或简单斜率统计。 | 有任务类型差异的实质假设/分组比较，但无交互项检验；按规则记 0。 |
| A6 | 中介变量 | NA | — | 理论模型不包含中介变量与中介效应分解。 |
| A7 | 操作性定义 | 1 | p.3（p.3）Def.1–2 给出 task-gram table 与 task-gram LM 公式；p.4（p.4）Def.3 给出 Mem 的 Spearman ρ 操作化；p.8–9（p.8、p.9）influence 公式；p.5–6 各任务指标定义。 | 关键构念均给出可复现的公式化操作化与计分。 |
| A8 | 水平数与类型 | 0.5 | p.4（p.4）模型规模 13M–12B，任务 WMT/TriviaQA/MMLU/GSM8K；p.5（p.5）与 p.16（p.16）n=2,3,5 及阈值；但未列全部具体模型规格或连续变量中心化说明。 | 有水平取值与任务/n 水平，但水平类型、间距/全距与连续模型规模处理不完整。 |
| A9 | 单一操作化的风险 | 1 | p.5–8（p.5–p.8）同时用 task-gram LM、∞-gram LM、novel n-gram count；p.8–9（p.8、p.9）用 gradient influence；p.9–10 prompt 操纵；结果相互印证。 | 关键构念多操作化并报告会聚证据。 |
| A10 | 单一方法的风险 | NA | — | IV（预训练语料频率/模型规模/任务）与 DV（LLM 概率/准确率）来源不同，无同源自评共同方法问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试或按被试分配条件；模型/任务比较不是被试间随机分配。 |
| B2 | 被试内设计 | NA | — | 非人类被试内重复测量设计；离线基准评测无被试条件顺序平衡。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合实验设计。 |
| B4 | 因子设计 | NA | — | 非实验因子设计；未用 ANOVA 设计矩阵/每格样本量。 |
| B5 | 主效应 | NA | — | 无因子设计主效应检验。 |
| B6 | 交互作用 | NA | — | 无实验交互项检验。 |
| B7 | 区组设计 | NA | — | 无区组/分层分配。 |
| B8 | 拉丁方 | NA | — | 无被试内拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验处理分配；主要是观察性/相关性分析与影响估计。 |
| B10 | 被试内设计的适用条件 | NA | — | 无被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 无随机分配的处理条件；LLM 离线评测无分配隐藏。 |
| C2 | 平衡 | NA | — | 无被试内条件顺序需平衡。 |
| C3 | 恒定 | 0.5 | p.4（p.4）Pythia 全家族、Pile；OLMo 1B/7B、Dolma；p.3（p.3）minimal instruction template；p.5（p.5）WMT greedy；p.14（p.14）讨论模型/语料局限。 | 列出部分固定因素及局限，但未系统报告所有恒定水平与外部效度限制。 |
| C4 | 匹配 | NA | — | 无匹配设计。 |
| C5 | 纳入为变量 | NA | — | 无可作为协变量/区组纳入的已知实验混淆；模型规模等作为分析维度而非 ANCOVA 协变量。 |
| C6 | 盲法 | NA | — | 全自动 LLM 评测，无人类被试/评分者可盲。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级问题。 |
| D1 | 练习效应 | NA | — | Zero-shot/离线评测，每条件无上下文内练习学习。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 疲劳风险；LLM 评测无疲劳设计。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各评测独立，无跨条件残留/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观指标（准确率/BLEU/BERTScore/相关系数），无主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 0 | p.6（p.6）'MMLU performance is evaluated by the accuracy of the option with the highest LM predicted probability.' 全文未报告选项位置随机化/反平衡。 | MMLU 多项选择存在选项位置偏差风险，但未做任何顺序/位置控制或讨论。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表分布与跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，无掩饰情节/需求特征。 |
| E5 | 实验者效应 | NA | — | 全自动数据采集，无人类主试/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.5–6（p.5、p.6）报告 MMLU 随机 25%，GSM8K Pythia <5% 故改用 BERTScore；Figure 3 展示性能曲线，但无完整均值/SD/偏度/端点频率或 pilot 校准。 | 有部分端点/难度信息，但未系统排查天花板/地板。 |
| E7 | 共同方法偏差 | NA | — | IV 与 DV 非同一自评来源，无共同方法偏差问题。 |
| F1 | 统计结论效度 | 0.5 | p.7（p.7）Figure 4 用实心/灰色星标 p<0.05；p.4（p.4）给出测试集 2.5K/10K；但无 CI、功效分析或明确多重比较校正。 | 报告了效应量（Spearman ρ）和显著性，但缺 CI、样本量依据与多重性校正。 |
| F2 | 内部效度 | 0.5 | p.5（p.5）n=8/14 overlap 去污染；p.8–9（p.8、p.9）gradient influence 作为 complementary causal evidence；但无随机分配/基线等价。 | 对内部效度威胁有部分处理（污染检查、影响函数），但因果识别与残余混淆报告不完整。 |
| F3 | 构念效度 | 0.5 | p.3–4（p.3、p.4）明确定义 Mem 与任务指标；p.5–8（p.5–p.8）task-gram LM 与 ∞-gram LM 对比、多任务/多模型；p.8–9 influence 收敛。 | 有构念定义与多操作化会聚证据，但无正式信度/效度统计或操纵检验。 |
| F4 | 外部效度 | 0.5 | p.4（p.4）报告模型家族/语料/四个数据集；p.7（p.7）GSM8K 有 Pythia 与 OLMo 复现；p.14（p.14）讨论 Pythia/Pile 过时与 WIMBD 限制。 | 报告样本来源并讨论边界，但非代表性抽样，跨情境复现有限。 |
| G1 | 分析单位 | 0.5 | p.4（p.4）Def.3 在所有 n-gram pair Φ 上计算 ρ；p.9（p.9）influence 对测试集和 R=50 文档平均；未说明 n-gram/样本/任务嵌套结构。 | 说明了分析落在 n-gram pair/test example 层级，但未处理其嵌套与分配层级匹配。 |
| G2 | 随机效应 | NA | — | 无混合模型/随机效应结构；模型规模作为固定分析维度，无被试随机效应需求。 |
| G3 | 材料作为随机效应 | 0.5 | p.4（p.4）四个任务/数据集；p.7（p.7）MMLU 57 子任务分组；p.16（p.16）列出任务子类；但无 (1&#124;item)/(1&#124;task) 随机效应模型。 | 有跨任务/材料复现，但未把材料/任务作为随机效应建模，故 0.5。 |
| G4 | 统计功效 | 0 | 全文无功效分析；p.4（p.4）仅报告测试集规模 2.5K/10K，未给目标功效/预期效应量；结果以 p<0.05 和 ρ 为主。 | 无事前功效分析或样本量论证。 |
| G5 | 研究者自由度 | 0.5 | p.4–6（p.4–p.6）列出四个任务及指标；p.7 Figure 4 报告多个 n/模型；但无剔除规则、停止规则或验证性/探索性区分。 | 报告多数条件与因变量，但研究者自由度披露不完整。 |
| G6 | 预先设定 / 预注册 | 0 | 全文无预注册平台/编号或分析计划；Section 7 prompt 优化为探索性。 | 无预注册。 |
| J1 | 位置偏差 | 0 | p.6（p.6）MMLU 用最高预测概率选项；全文未报告选项位置随机化/交换重判或位置×正确率。 | LLM 多项选择存在位置偏差风险，但未控制。 |
| J2 | 冗长偏差 | NA | — | 无 LLM-as-judge 评估开放生成质量；Table 1 用准确率，prompt 优化非质量裁判。 |
| J3 | 谄媚 | NA | — | 无用户立场/反馈对话式评估。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM 裁判打分，无自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 任务为零样本评测（minimal instruction），无 few-shot 示例。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.3（p.3）minimal instruction template；p.9–10 与 p.17 Table 2、p.18 meta prompt 给出完整优化 prompt 与两套任务 prompt；但无版本号/语义等价敏感性消融/dev-test 划分。 | 提供了完整 prompt 模板但未做敏感性分析/版本化。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 不是长上下文/RAG 实验；WIMBD/∞-gram 是语料检索，不是上下文窗口利用。 |
| J8 | 温度与采样随机性 | 0 | p.5（p.5）仅说 WMT 用 greedily generated translation；未报告 temperature/top-p/seed/重复采样或 CI。 | 单次离线评测，未报告采样超参与随机性。 |
| J9 | 重复与文本退化 | 0.5 | p.5（p.5）WMT greedy generation；p.6（p.6）GSM8K 生成 CoT 并用 BERTScore；但未报告 repetition penalty、重复率/退化率或条件间解码一致性。 | 有部分解码说明，缺重复/degeneration QC。 |
| J10 | 分词效应 | 0 | p.4（p.4）WMT 含 Hungarian/Czech/German/Italian/Spanish/French 等跨语言；全文未报告 tokenizer 名称/版本或 token/词数比。 | 跨语言比较未控制分词效应。 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | p.5（p.5）'ensuring there are no large n-grams (n = 8 and n = 14) overlaps between the Pile and the testing data'，采用 GPT3 报告去污染方法；未报告污染率/训练截止日期细节。 | 有污染检查但未量化污染率与截止日期对照。 |
| J12 | 基准饱和 | 0.5 | p.6（p.6）报告 MMLU 随机 25%、Pythia 部分任务 <10%，GSM8K Pythia <5% 故改用 BERTScore；未系统报告 SOTA/饱和位置或 CI 比较。 | 报告了部分基准水位与随机基线，但未系统评估饱和或 SOTA，故 0.5。 |
| J13 | 指令遵循 | NA | — | 不以指令遵循为因变量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化输出解析。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究 LLM 能力溯源，不主张测量人类心理学构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较模型规模，但未宣称涌现/突变，未做涌现曲线检验；风险不存在。 |
| J18 | 指标博弈与奖励过优化 | 0.5 | p.9–10（p.9、p.10）用 GPT4o 按 WIMBD n-gram count 奖励优化 prompt，最大化/最小化 n-gram count；Table 1 用独立零样本准确率评估；附录 E 给 prompt。但无代理-真实双曲线/过优化拐点。 | 代理优化与评估对象分离，但未监控 overoptimization。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.4（p.4）仅列 Pythia 规模与 OLMo 1B/7B；无重复次数、CI、精确 snapshot/commit、配对检验或日志发布。 | 评估可复现性报告不足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 严格单轮零样本评测，无多轮对话历史。 |

## 编码小结
论文提出 task-gram LM 与 distributional memorization，用 Pythia/OLMo 在 WMT、TriviaQA、MMLU、GSM8K 上做相关性、影响函数与 prompt 操纵分析。优点是构念操作化清晰、多操作化会聚、污染检查；主要限制是无预注册/功效分析/随机种子与 CI、多项选择位置未平衡、无混合模型处理材料与样本嵌套、prompt 实验报告不完整。
