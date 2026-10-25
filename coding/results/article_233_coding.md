# article_233 | Why Larger Language Models Do In-context Learning Differently? | 2024

研究类型概述：理论分析（线性回归的低秩线性自注意力与稀疏 parity 的多头两层 Transformer）加 LLM 行为基准实验（Llama 3B/7B/13B/70B，GLUE/Subj，flipped labels 与无关句消融）。实证分析单位为 evaluation prompt/model condition，不是人类被试；主要因变量为 accuracy。
- **研究构念（Construct）**：情境学习中的噪声敏感性、先验覆盖与注意分配差异｜CA 构念锚定：认知控制（cognitive control, `trm_4aae62e4ad209`）；注意（attention, `trm_4a3fd79d09902`）；干扰控制（interference control, `trm_551f11bb8f6a8`）
- **实验任务与范式（Task / Paradigm）**：给3B至70B的现成Llama模型16个带不同翻转比例的分类示例，在五个NLP任务上测试，并比较相关/无关文本上的注意与准确率。（操纵模型规模、标签翻转比例、是否插入无关句子、任务和chat/base版本。）｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.8: 'we conduct experiments on five prevalent NLP tasks... Llama model families... 3B, 7B, 13B, 70B'; 'introduce noise by inverting an escalating percentage of in-context example labels'; Figure 1 x-axis 0, 25, 50, 75, 100. | 明确报告了噪声翻转比例与模型规模等条件及至少两个水平，但未系统说明条件分配方式与操纵检验，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.8: 'Accuracy is calculated over 1000 evaluation prompts per dataset and over 5 runs with different random seeds for each evaluation, using M = 16 in-context exemplars.' | 因变量为 accuracy，计分方式明确；但未报告信度/效度证据、分布预处理或天花板/地板说明。 |
| A3 | 控制变量 | 0.5 | p.8: 'we use M = 16 in-context exemplars'; 'We use the same templates as (Min et al., 2021)'; experiments utilize five tasks and Llama models. | 报告了部分恒定控制（模板、M=16、数据集与模型族），但未系统列出完整控制变量清单及逐一控制手段。 |
| A4 | 混淆变量 | 0.5 | p.9: 'instruction tuning will impair LLM's in-context learning capability'; p.9: 'The robustness gap only happens when both pretraining noise and inference noise exist simultaneously.' | 识别了 instruction tuning、预训练噪声、输入/标签噪声等潜在混淆，但未系统说明控制方式或残余混淆的定量威胁。 |
| A5 | 调节变量 | 0 | Figure 1 and Figure 2 p.8 show accuracy curves by model size and flipped-label percentage; no interaction F/df/p/effect size or simple slopes are reported. | 论文核心是模型规模与噪声的交互模式，但仅给出描述性曲线，没有正式交互检验、中心化或简单斜率分析，按编码规则记 0。 |
| A6 | 中介变量 | NA | — | 论文以注意力分配/特征覆盖作理论解释，但没有中介变量假设和直接/间接效应分解，中介分析不适用。 |
| A7 | 操作性定义 | 0.5 | p.8: label inversion percentage; M=16 in-context exemplars; same templates; p.8 Figure 1 caption: 1000 evaluation prompts and 5 runs; p.8 shows a partial SST-2 template example. | 关键操纵与因变量有可重复的描述，但 prompt 采样、模板全文、评分与运行细节不完整，不能完全复现。 |
| A8 | 水平数与类型 | 0.5 | p.8: model sizes '3B, 7B, 13B, 70B'; Figure 1 x-axis flipped labels 0, 25, 50, 75, 100. | 报告了水平数与取值，但未说明水平类型、水平间距/全距、连续变量中心化等。 |
| A9 | 单一操作化的风险 | 0.5 | p.8-9: label-flip experiments (Figures 1-2) plus irrelevant-sentence attention ablation (Figure 3) and theoretical two settings (linear regression, parity). | 对噪声敏感性采用了多种操作化并给出一致方向，但未量化各操作之间的会聚证据，单一 accuracy 指标仍占主导。 |
| A10 | 单一方法的风险 | NA | — | 实证因变量为客观 accuracy，自变量为提示标签翻转/模型条件；不涉及自评量表同源问题，共同方法偏差不适用。 |
| B1 | 被试间设计 | NA | — | 没有人类被试或被试组分配；不同模型规模是既有模型的观察性比较，不存在被试间随机分配。 |
| B2 | 被试内设计 | NA | — | 模型按不同 flipped-label 条件分别独立评估，每次调用无跨条件状态；未形成需要顺序平衡的被试内会话结构。 |
| B3 | 混合设计 | NA | — | 论文未把模型规模与翻转比例作为正式混合设计逐因素标注，也未使用混合模型；无人类组间/组内混合结构可编码。 |
| B4 | 因子设计 | 0 | Figures 1-2 p.8 plot five datasets, multiple model sizes, and flipped-label levels in a crossed manner; no design matrix, cell n, or ANOVA table is given. | 存在多因素组合展示，但没有完整设计矩阵、每格样本量及正式交互统计，故为部分满足；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | Figures 1-2 p.8 only show descriptive accuracy curves; no main-effect F/df/p/effect size reported. | 未报告任何因素主效应的统计检验与效应量。 |
| B6 | 交互作用 | 0 | Figures 1-2 p.8 show differing slopes by model size and flipped labels, but no interaction test, simple effects, or error bars/CI. | 有描述性交互模式，但没有交互统计检验、简单主效应或带误差的图示。 |
| B7 | 区组设计 | NA | — | 无区组/分层分配设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | 0 | p.8: experiments compare existing Llama model sizes; p.9 interprets larger models as more easily distracted; limitations p.15 only mention theoretical/style gap. | 模型规模不可随机分配，属于观察性模型比较，论文未说明准实验类型、选择偏差或对因果推断作限定，却直接作规模效应解释，故记 0。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理可逆性/迁移问题。 |
| C1 | 随机化 | NA | — | 没有条件到分析单位的随机分配；5 个 random seeds 用于评估重复，不是处理分配随机化。 |
| C2 | 平衡 | NA | — | 无需要平衡的被试内条件顺序；各条件为独立评估。 |
| C3 | 恒定 | 0.5 | p.8: 'five prevalent NLP tasks', M=16, same templates, Llama 3B/7B/13B/70B; p.15 limitations note gap to real LLM usage. | 列出了部分恒定变量及水平，但未系统说明温度、提示格式、采样设置等，外部效度限制讨论也有限。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | Figure 1 (chat/instruct-tuned) vs Figure 2 (base) p.8 separately present results by model tuning type; no formal covariate/stratification model or slope-homogeneity test. | instruction tuning 作为已知混淆被分层展示，但未纳入正式模型，也未报告调整后效应或斜率齐性检验。 |
| C6 | 盲法 | NA | — | LLM 自动评估，无人类被试、主试或评分者盲法。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级需要报告。 |
| D1 | 练习效应 | NA | — | 各评估调用为独立无状态推理，不存在跨 session 的练习效应。 |
| D2 | 疲劳效应 | NA | — | 自动短时评估，无人类疲劳或 session 时长问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 不同 flipped-label 条件独立评估，无跨条件迁移/残留。 |
| D4 | 不对称迁移 | NA | — | 无被试内跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 无主观量表或绝对判断的范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0 | p.8: M=16 in-context exemplars and partial SST-2 template are shown; no randomization/counterbalancing of exemplar order or label positions is reported. | few-shot 示例顺序可能影响 ICL，但论文未报告随机化或反平衡。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也无跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | LLM 无人类被试需求特征，任务为客观分类。 |
| E5 | 实验者效应 | NA | — | 完全自动化数据采集，无人类主试/评分者。 |
| E6 | 天花板 / 地板效应 | 0 | Figures 1-2 p.8 show mean accuracy curves, but no SD, skew, endpoint frequencies, or pilot difficulty calibration are reported. | accuracy 有上下界且图中部分条件接近端点，但未报告分布/端点频数或难度校准。 |
| E7 | 共同方法偏差 | NA | — | IV/DV 非自评同源，客观 accuracy 不涉及共同方法偏差。 |
| F1 | 统计结论效度 | 0 | p.8 Figure captions report only mean accuracy over 1000 prompts and 5 runs; no effect sizes, confidence intervals, sample-size justification, or multiple-comparison correction. | 缺少效应量/CI、样本量依据和多重性校正；只作描述性比较。 |
| F2 | 内部效度 | 0 | p.8-9 describe model/dataset comparisons; p.15 limitations mention theoretical gap but no randomization, baseline equivalence, allocation concealment, or attrition/flow handling. | 没有随机分配、基线等价性或内部效度威胁的系统评估。 |
| F3 | 构念效度 | NA | — | 核心实测为 objective accuracy，属于可直接测量的正确率指标，无需传统量表信效度论证；论文也未将其作为心理测量量表。 |
| F4 | 外部效度 | 0.5 | p.8: five GLUE/Subj tasks and Llama model families; p.15 limitations: 'simple binary classification real-world datasets... still has a gap for the practical user using the LLM scenario.' | 报告了模型/数据集来源并讨论部分推广边界，但没有抽样框、代表性或跨情境复现设计。 |
| G1 | 分析单位 | 0.5 | p.8: accuracy calculated over 1000 evaluation prompts per dataset and 5 runs; prompts are aggregated, but no analysis-unit/multilevel matching is described. | 说明了评估 prompt 与 run 的聚合层级，但未说明处理分配层级及嵌套结构处理。 |
| G2 | 随机效应 | 0 | p.8 figures average over prompts/runs; no mixed model or random-effects structure for prompt, dataset, or model is reported. | 未报告随机效应；对 prompt 抽样总体作推广时缺乏随机截距/斜率建模。 |
| G3 | 材料作为随机效应 | 0 | p.8 uses five fixed datasets and fixed templates; no item/material random effect or F′/mixed model is reported. | 数据集与 prompt 材料被当作固定材料，仅作被试/模型层面平均，未处理材料抽样。 |
| G4 | 统计功效 | 0 | p.8: 1000 evaluation prompts and 5 runs, but no a priori power analysis, expected effect size, or CI justification. | 无设计阶段功效分析或样本量推导，结果也无效应量/CI。 |
| G5 | 研究者自由度 | 0.5 | Figures 1-3 p.8-9 report all five datasets and multiple conditions; no trial/prompt exclusion rules, stopping rules, or clear confirmatory/exploratory labeling are given. | 条件与因变量展示较全，但排除规则、样本量决定和探索/验证区分缺失。 |
| G6 | 预先设定 / 预注册 | 0 | No preregistration, registered report, or analysis-plan link is mentioned in the paper. | 无可验证的预注册，故按缺失记 0。 |
| J1 | 位置偏差 | NA | — | 任务为二分类/开放式短答案生成，不涉及多候选项位置交换或 LLM-as-judge 成对比较。 |
| J2 | 冗长偏差 | NA | — | 评估指标为 accuracy，不涉及开放生成的长度—质量裁判。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场或反馈/纠错对话操纵，不涉及谄媚。 |
| J4 | 自我偏好 | NA | — | 未使用 LLM-as-judge。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.8: M=16 exemplars; flipped-label percentage is controlled; Figure captions mention 5 random seeds; partial template with two examples is shown. No full example set, arrangement counterbalancing, or multi-seed set variation is reported. | 报告了示例数量与标签翻转比例，但缺少示例排列反平衡、多示例集均值和完整提示模板。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p.8 gives only a partial SST-2 sample template; no prompt version, full template, sensitivity ablation, or dev/test separation is reported. | 未提供完整 prompt 模板，也未做措辞敏感性消融或说明是否在测试集上调 prompt。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 上下文仅为 M=16 个示例，远非长上下文/RAG 设置。 |
| J8 | 温度与采样随机性 | 0 | p.8 Figure captions: '5 runs with different random seeds'; no temperature, top-p, top-k, max tokens, exact seeds, or API snapshot are reported. | 只有 5 次重复，但缺少解码采样超参、种子取值和快照标识，未达到基本要件。 |
| J9 | 重复与文本退化 | NA | — | 任务为二分类短答案，不涉及开放生成重复/退化。 |
| J10 | 分词效应 | NA | — | 英文单语言任务，无跨语言/跨脚本比较。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.8 uses public GLUE and Subj datasets with Llama models, but no training cutoff comparison, contamination check, or private/held-out set is reported. | 未做测试集污染或数据泄漏检查。 |
| J12 | 基准饱和 | 0 | Figures 1-2 p.8 report accuracy on GLUE/Subj, but no benchmark score range, SOTA waterline, ceiling analysis, or CI-based comparison is reported. | 未评估基准饱和；部分条件可能接近高分端但未讨论。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 不要求结构化输出或格式约束。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全性/越狱评估。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 论文是 LLM 能力/机制研究，不主张把 LLM 作为人类心理学被试或测量人类同名构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 未宣称能力涌现/突变，也未报告随规模变化的能力曲线；规模只是分组比较变量。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无对 benchmark、奖励模型或 LLM-judge 的优化过程。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.8 Figure captions report 5 runs with different random seeds; model names/sizes such as Llama-2-13b and open_llama-2-3b are given, but no CI, paired test, exact snapshot/date, or raw logs are reported. | 有重复次数与部分模型标识，但缺置信区间、配对检验和精确快照。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 in-context 分类，无多轮对话历史累积。 |

## 编码小结
论文的理论刻画较完整，但实证部分属于初步验证：主要报告多模型、多数据集的 accuracy 曲线，缺少正式的推断统计、随机化/平衡细节、信效度、功效分析、污染与饱和分析、采样超参和可复现快照。大量人类被试设计组件不适用；适用的 LLM 条件比较组件多为部分报告或缺失。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 B4（0.5→0）。
