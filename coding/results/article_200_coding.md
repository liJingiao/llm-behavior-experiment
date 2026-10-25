# article_200 | How do Large Language Models Navigate Conflicts between Honesty and Helpfulness? | 2024

研究类型概述：该研究不是人类被试实验，而是把多个 LLM 作为行为主体，在 signaling bandits 范式中测量其在诚实与有用性之间的取舍；操纵或比较的因素包括 vanilla vs. chain-of-thought 提示、neutral/honest/helpful 目标提示、模型系列及 RLHF 前后版本，以及蘑菇/住房/餐饮等情境。分析单位主要是每个 LLM 在每个条件/试次下的生成响应，并用 RSA 类心理模型拟合 λ、βS 等参数。
- **研究构念（Construct）**：对话中的诚实—有用性权衡与语用价值敏感性｜CA 构念锚定：态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）；语言理解（language comprehension, `trm_4a3fd79d0a775`）
- **实验任务与范式（Task / Paradigm）**：让多种现成LLM在数值近似、信息省略和日常对话情境中选择或生成回答，并与心理学模型和人类模式比较。（改变事实精确度、听者目标、对话框架、现成模型检查点及CoT或价值提示。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: “We also prompt with and without chain-of-thought”; p.7: “adding a prompt that encourages either honesty or helpfulness”; p.13-16 Appendix A lists full prompts and prior snippets. | 明确命名并报告了提示类型（vanilla/CoT）与目标提示（honest/helpful/neutral）的水平及操纵程序，但未报告独立的操纵检验；因此为部分满足。 |
| A2 | 因变量 | 0.5 | p.5: “prompt the LLM to generate 30 responses for each trial”; p.6: “fraction of their utterances that are truthful and the fraction that are helpful”; p.17 Table 2 reports % parsed, % truthful, % helpful, λ. | 因变量指标与计分方式有明确界定（truthful/helpful 比例、endorsement、拟合 λ），但未报告心理测量信度/效度证据，也未系统说明连续指标的预处理与端点效应处理；故不足以记 1。 |
| A3 | 控制变量 | 0.5 | p.5: “We use temperature = 0.1, top p = 0.9 for the LLaMa models… temperature = 0.7, top p = 1 for the Mixtral models… temperature = 1, top p = 1 for the GPT models”; “Vanilla prompts were limited to 20 response tokens and CoT responses were limited to 500”; p.5 also randomizes stimuli. | 报告了若干控制变量及其控制手段（解码参数、生成长度上限、刺激随机化、解析规则），但未系统列出完整控制变量清单并逐一说明，故为部分满足。 |
| A4 | 混淆变量 | 0.5 | p.5: “outputs may be sensitive to the ordering of stimuli… Thus, we randomize stimuli”; p.13: weaker models required additional prompt engineering; p.7: Llama often “always endorse or always stay silent… We therefore omit it”. | 识别了刺激顺序、弱模型输出无效、模型输出退化为常数等潜在混淆，并报告了相应控制/排除；但未系统评估残余混淆或做敏感性分析，故为 0.5。 |
| A5 | 调节变量 | NA | — | 全文没有把某个调节变量作为理论模型中的调节项，也未报告乘积项交互检验或简单斜率分析；模型/提示比较属于分组比较而非正式调节设计，因此不适用。 |
| A6 | 中介变量 | NA | — | 研究理论模型不包含中介变量，也没有直接/间接效应分解或 a/b 路径报告。 |
| A7 | 操作性定义 | 1 | p.3-4 Eq.1-9 formalize honesty/helpfulness and combined utility; p.5: “We prompt LLMs to act as a tour guide… exactly 4 words long”; p.13-16 full prompts; p.5 parsing rules. | 关键构念和任务都给出了可复现的操作化：精确公式、提示全文、响应格式、解析规则和模型拟合程序；满足操作性定义要求。 |
| A8 | 水平数与类型 | 1 | p.5: “with and without chain-of-thought”; p.7: neutral, honesty, helpfulness prompt conditions; p.13-16 prompts list exact feature/value labels; Tables 3-4 label objective and CoT conditions. | 报告了各操纵条件的水平数与具体标签；这些是分类变量，水平间距/全距不适用，未涉及连续自变量入回归的中心化问题。 |
| A9 | 单一操作化的风险 | 1 | p.4-7 three experiments and multiple behavioral metrics (truthful/helpful fractions, endorsement, fitted λ); p.8 compares GPT-4 Turbo with human data; p.9: “controlled domains… cannot guarantee generalization to real-world contexts”. | 关键构念通过多个实验、多个指标及人类数据对照进行三角验证，并在讨论中明确承认受控情境的推广限制。 |
| A10 | 单一方法的风险 | NA | — | 研究不使用自陈量表，自变量为提示，因变量为解析后的模型行为/拟合参数，不是同源自评测量；共同方法偏差问题不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试被分配到独立条件；模型之间的比较也不是随机分配的被试间实验。因此经典被试间设计不适用。 |
| B2 | 被试内设计 | 0.5 | p.5: “For each experiment, we investigate…”; p.7: “fit the model to data from each LLM and compare parameter values”; p.5 reports stimulus randomization but not prompt-condition order. | 同一 LLM 在 vanilla/CoT、neutral/honest/helpful 等条件下被重复评估，属于 LLM 分析单位的重复测量/条件内比较；但未报告条件顺序平衡方案或各顺序分配。 |
| B3 | 混合设计 | NA | — | 论文没有建立正式的组间×组内混合设计，也未使用混合模型或分别报告组间/组内误差项；各模型被分别拟合，故不按混合设计编码。 |
| B4 | 因子设计 | 0 | p.17-19 Tables 2-4 cross models, objective prompts, CoT, and settings; p.6 Table 1 reports CoT-vs-default model comparisons. | 多因素条件在表格中大体完整呈现，但未给正式 ANOVA 设计矩阵、每格样本量、交互项 F/df/p/效应量；只能算部分满足；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0.5 | p.6 Table 1 reports Bayes factors for λ_CoT > λ_default; p.17 Table 2 reports λ and βS by model/prompt; p.7-8 describe prompt/RLHF differences. | 报告了若干主效应方向及 Bayes factor/参数差异，但未报告 F 值、自由度、p 值与效应量；故为部分满足。 |
| B6 | 交互作用 | 0 | p.6 Table 1 only compares CoT vs default within models; p.7-8 describe varying effects across models but report no formal interaction test or simple-effects follow-up. | 没有对交互项做正式统计检验，也没有报告简单主效应或交互图示误差；若按多因素设计编码，核心交互检验缺失。 |
| B7 | 区组设计 | NA | — | 没有区组/分层变量、区组划分或区内随机分配程序。 |
| B8 | 拉丁方 | NA | — | 没有使用拉丁方顺序安排。 |
| B9 | 准实验设计 | 0 | p.5: “two pairs of models before and after RLHF, allowing us to investigate how RLHF influences model behavior”; p.6 claims “RLHF strictly improves both honesty and helpfulness”. | RLHF 前后模型是现成模型的非随机比较，但论文未说明这是准实验、未讨论选择偏差/模型差异等内部效度威胁，却直接作因果性表述；按准实验编码为 0。 |
| B10 | 被试内设计的适用条件 | NA | — | LLM 各条件通过独立 API 调用/独立提示实现，不存在人类被试内设计中需要论证的处理可逆性和迁移对称性问题。 |
| C1 | 随机化 | 0.5 | p.5: “we shuffle the magnitudes associated with each type of feature, and shuffle the values assigned to features… we randomize between ascending and descending”. | 报告了对刺激/特征/数值顺序的概率化随机化，但未报告随机数生成工具、种子或分配隐藏机制；也无条件分配随机化。 |
| C2 | 平衡 | 0.5 | p.5 randomizes feature order and ascending/descending value order, but gives no per-order counts or balance hierarchy. | 存在顺序随机化/部分平衡，但未说明平衡层级、每种顺序的分配数量或迁移对称性前提。 |
| C3 | 恒定 | 0.5 | p.5 reports model-specific temperature/top-p and 20/500 token limits; p13 reports prompt suffixes for weaker models. | 列出了若干被恒定的技术变量及其水平，但未系统讨论这些恒定化对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有使用匹配或配对分配。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为区组因素或协变量纳入统计模型。 |
| C6 | 盲法 | NA | — | 数据采集和响应解析为自动化/规则化流程，没有人类主试或评分者需要盲法。 |
| C7 | 平衡的层级 | 0 | p.5 randomizes feature order and ascending/descending value order, but gives no per-order counts or balance hierarchy. | 研究存在被试内/序列顺序平衡需求（同 C2），但未明确选用完全平衡、拉丁方或 ABBA 层级，亦未报告构造方法与顺序效应形状假设，记 0。 |
| D1 | 练习效应 | NA | — | LLM 各试次为独立提示调用，没有跨试次上下文内学习或练习效应控制问题。 |
| D2 | 疲劳效应 | NA | — | 任务为短时 API 生成，不涉及人类 session 时长或疲劳控制。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同条件通过独立调用实现，不存在跨条件残留/清洗期问题。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移或不对称迁移设计。 |
| D5 | 范围效应 | NA | — | 因变量为客观选择/解析结果，不是被试内绝对判断或 Likert 量表，范围效应不适用。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.5: “we shuffle the magnitudes associated with each type of feature, and shuffle the values assigned to features… we randomize between ascending and descending”. | 报告了对刺激顺序和数值顺序的随机化，但未说明具体随机化方案、各位置出现次数或试次分配细节。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，默认赞同偏差不适用。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 没有等级量表或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 研究对象为 LLM，不存在人类被试的需求特征操纵与事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集与规则解析，无人类实验者/评分者期望效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.17 Table 2 shows GPT-4 100% truthful and GPT-4 Turbo 1.00 truthful; p.7 says Llama often always endorsed or stayed silent and analyses were omitted as meaningless; p.6 Fig.2 reports fractions. | 报告了均值/比例并识别了端点堆积与均匀输出，但未系统报告偏度、端点频率或 pilot 难度校准过程。 |
| E7 | 共同方法偏差 | NA | — | 没有多构念自陈式测量，IV 与 DV 也非自评同源结构。 |
| F1 | 统计结论效度 | 0.5 | p.6 Table 1 reports Bayes factors; p.17-19 Tables 2-4 report posterior mean λ and parse/truth/helpful rates; no confidence intervals or power analysis reported. | 报告了参数估计和 Bayes factor，但缺少样本量确定依据、95% CI、多重性校正及完整统计假设检验报告，故为部分满足。 |
| F2 | 内部效度 | 0.5 | p.5 reports stimulus randomization and model-specific decoding settings; p.7 omits Llama conditions with uniform outputs; p.13 reports prompt engineering for weak models. | 有刺激随机化和部分排除/偏离说明，但没有随机条件分配、分配隐藏、基线等价性或被试流向；仅部分评估内部效度威胁。 |
| F3 | 构念效度 | 0.5 | p.3-4 formalizes honesty/helpfulness via RSA utility equations; p.5 reports parsing and 30 responses per trial; p.8 compares with human data; p.9 discusses construct caveats. | 构念有形式化定义、与人类数据的对照及效度讨论，但未报告心理测量信度、评分者信度或正式操纵检验，故为 0.5。 |
| F4 | 外部效度 | 0.5 | p.5 lists model suite and hyperparameters; p.7-8 Experiment 3 adds housing/dining settings; p.9: “controlled domains… cannot guarantee generalization to real-world contexts”. | 报告了模型来源/特征和部分推广限制，并增加现实情境，但无代表性抽样、跨样本复现或系统边界条件检验。 |
| G1 | 分析单位 | 0.5 | p.5: “generate 30 responses for each trial”; p.6: “fit the psychological model… to data from each LLM”; no multilevel model or trial-level variance separation is reported. | 说明了响应生成和分析是在 LLM/试次层级进行，但未说明 30 个响应的嵌套结构如何进入模型，也未用多层模型分离试次/响应方差。 |
| G2 | 随机效应 | NA | — | 统计模型为每个 LLM 单独拟合固定参数模型，没有随机效应结构；研究也不把模型或试次作为从更大总体抽样的随机因子，因此随机效应组件不适用。 |
| G3 | 材料作为随机效应 | NA | — | Experiment 1 明确枚举 6 个特征×5 个数值的 30 种可能话语；Experiment 2/3 使用固定构造的情境，并未把材料视为从更大材料总体抽样，因此不要求材料随机效应。 |
| G4 | 统计功效 | 0 | p.5 reports “30 responses for each trial” but no power analysis, target effect size, or sample-size justification; Tables 2-4 report no confidence intervals. | 没有事前功效分析或样本量论证，也没有报告效应量置信区间；按统计功效组件核心要求未达成。 |
| G5 | 研究者自由度 | 0.5 | p.5 reports discarding responses that fail parsing; p.7 reports omitting Llama conditions with uniform outputs; p.17-19 provide full result tables. | 报告了部分排除规则和全部主要表格，但未说明样本量/30 次重复的决定方式、是否中途停止或完整区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.5-9 methods/results do not mention preregistration, registration number, or a confirmatory/exploratory distinction. | 全文未见公开预注册或分析计划；按既定口径，未预注册记 0。 |
| J1 | 位置偏差 | NA | — | 研究不是 LLM-as-judge 成对比较，也没有多候选项 A/B 位置操纵；Experiment 1 的刺激顺序随机化已归入 E1，而非裁判位置偏差。 |
| J2 | 冗长偏差 | NA | — | 评估不涉及 LLM 裁判对开放生成长短的质量评分；输出被限制为短格式/二元答案，长度偏差不适用。 |
| J3 | 谄媚 | NA | — | 研究操纵的是 honesty/helpfulness 目标提示，不是用户先验立场、反馈或纠错；谄媚风险不适用。 |
| J4 | 自我偏好 | NA | — | 没有使用 LLM-as-judge 评估模型输出，因此不存在裁判自我偏好/同源偏差组件。 |
| J5 | 少样本示例选择与排列偏差 | NA | p.5 and Appendix A: prompts are zero-shot task instructions; no few-shot in-context examples are reported. | 实验为零样本提示，不使用 few-shot 示例，故示例选择/排列偏差不适用。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5: “We performed prompt engineering in weaker and non-chat models to encourage valid responses”; p.13-16 provide full prompt templates; p13 notes prompts were highly similar across models. | 公布了完整提示模板并说明了对弱模型的提示工程，但没有 prompt 版本号、迭代日期、语义等价措辞的敏感性消融或 dev/test 划分。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 实验上下文很短，不涉及长文档、RAG 或关键信息位置操纵。 |
| J8 | 温度与采样随机性 | 0.5 | p.5 reports temperature/top-p by model family and “30 responses for each trial”; also reports 20/500 token limits; no random seed, confidence intervals, or API snapshot dates are reported. | 报告了主要采样超参与重复次数，但缺少种子、95% CI、精确 snapshot 日期及 top-k/repetition penalty 等完整信息。 |
| J9 | 重复与文本退化 | 0.5 | p.5 reports temperature/top-p and response-length limits (20 vs. 500 tokens); no repetition penalty, n-gram repetition rate, or degeneration/truncation rate is reported. | 有解码策略和长度上限信息，但未报告重复/退化 QC 指标；CoT 条件包含自由推理文本，因此仍需部分扣分。 |
| J10 | 分词效应 | NA | — | 研究为单语言、单脚本英文提示与输出，没有跨语言/跨脚本或跨格式输入比较。 |
| J11 | 测试集污染 / 数据泄漏 | NA | — | 研究使用自定义行为范式与自建提示，不是公开基准评测；未把标准测试集分数作为泛化能力结论，因此污染组件不适用。 |
| J12 | 基准饱和 | NA | — | 没有使用标准基准分数量表或 SOTA 饱和比较；GPT-4 的端点表现已在 E6 中处理。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量，也没有按否定/数量/格式/风格约束拆分指令遵循准确率；格式约束只作为任务实现细节。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.5: responses parsed by regular expressions/rules; “those without exactly one feature and one value were discarded”; p.17-19 report parse accuracy; p.13 gives exact 4-word output format. | 报告了结构化输出要求和格式合法率（解析准确率），并将格式失败与内容指标分开；但没有使用 grammar-constrained decoding、重试策略或输出归一化细节。 |
| J15 | 越狱稳健性 | NA | — | 研究不涉及安全/对齐评估、有害请求或越狱攻击。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.1-2 explicitly use “psychological models and experiments designed to characterize human behavior to analyze LLMs”; p.8 compares GPT-4 Turbo to human participants; p.9 acknowledges “people necessarily bring vastly different social and physical groundings”. | 论文明确把 LLM 行为与人类同名构念作理论联系并给出人类对照，也讨论了构念迁移风险；但模型仅以名称标识，缺少精确权重/API snapshot 及更系统的构念效度论证。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 研究没有报告随模型规模/训练进展的能力曲线，也不宣称涌现或相变。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究不涉及以 benchmark、奖励模型或 LLM-judge 为优化目标的训练/RL/best-of-N 优化，因此代理指标过优化不适用。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.5 reports 30 responses per trial and model names; p.17-19 report posterior means and parse accuracy; no exact API snapshot/date, confidence intervals, or paired tests are reported. | 报告了重复生成次数和模型名称，但 snapshot 标识不精确，且缺少 CI、逐题敏感性分析或配对检验。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮提示-响应，没有多轮对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
论文清晰报告了实验范式、提示模板、模型版本类别、解码参数、响应解析与主要行为指标，并提供了多模型、多实验和与人类数据对照的结果；但其统计报告以参数后验均值、Bayes factor 和描述性表格为主，缺少许多实验心理学的随机分配、信效度、功效分析、预注册及正式交互/多层模型细节。大量人类被试特有的分配、顺序、需求特征和自陈量表组件不适用。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）, C7（NA→0）。
