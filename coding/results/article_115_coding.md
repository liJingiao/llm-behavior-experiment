# article_115 | Assessing Reliability and Political Bias In LLMs’ Judgements of Formal and Material Inferences With Partisan Conclusions | 2025

研究类型概述：这是一项 LLM 基准评测/计算实验，分析单位是各 LLM 配置下对构造出的推理样本的单次判断输出；研究者系统操纵推理类型（形式/实质）、有效性（有效/无效）、政治倾向（左/右）、论证变式（default/conlast/perm/rand）、few-shot 设置（0/8/32）与指令措辞，并比较 16 个开放/闭源 LLM 配置及英/德两种语言。核心因变量为标签正确率与加权政治偏差分数。
- **研究构念（Construct）**：形式/实质推理可靠性与党派政治偏差｜CA 构念锚定：态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：这是一项 LLM 基准评测/计算实验，分析单位是各 LLM 配置下对构造出的推理样本的单次判断输出；研究者系统操纵推理类型（形式/实质）、有效性（有效/无效）、政治倾向（左/右）、论证变式（default/conlast/perm/rand）、few-shot 设置（0/8/32）与指令措辞，并比较 16 个开放/闭源 LLM 配置及英/德两种语言。核心因变量为标签正确率与加权政治偏差分数。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.5: 'We use a total variation of 9 instruction patterns... combinations of three different descriptions of the task with three different few-shot (FS) settings (0 FS, 8 FS, 32 FS).' p.5 Table 3: default/conlast/perm/rand. | 明确命名并给出多个受控因素及水平；但未报告操纵检验，单位分配/运行顺序也只部分说明，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.6: 'An LLMs’ judging a valid inference as valid and an invalid as invalid was mapped onto 1, everything else onto 0.' p.6: 'randomly selecting 500 outputs and checking for accuracy... precision over 98%'; 'We run the entire experiment three times and average'. | 因变量指标（正确率、偏差分数）、计分和抽取规则明确，且报告了抽取精度与三次运行；但无传统信度/效度证据或连续指标预处理说明。 |
| A3 | 控制变量 | 0.5 | p.13: 'Hardware For the open LLMs, we used a GPU cluster consisting of V100 GPUs...'; p.14 Table 6 lists models/precision/HF sources; p.5: 'we balance our samples as much as possible'. | 报告了硬件、模型版本/精度和 few-shot 结构的一部分控制；但未系统列出所有恒定变量，也未报告温度等生成参数。 |
| A4 | 混淆变量 | 0.5 | p.4: 'we include variations of the arguments that are immaterial to the validity... such as premise order and the insertion of a random premise.' p.8 discusses effects of conclusion position and random premise. | 识别并操纵了若干潜在混淆（前提顺序、结论位置、随机前提）作为变式；但未系统说明残余混淆或敏感性分析。 |
| A5 | 调节变量 | 0 | p.3: 'we hypothesize that it might be more liable to political bias'（实质推理相对形式推理）；p.15 Table 9 分别给出 material/formal 偏差分数，但无交互检验。 | 提出了推理类型与偏差关系的主张，但只分列偏差分数，没有正式交互检验或简单斜率，属提出调节性假设却未做交互分析。 |
| A6 | 中介变量 | NA | — | 全文没有中介变量或中介效应分析，理论模型不含中介路径，故不适用。 |
| A7 | 操作性定义 | 1 | p.5 Table 2/3 与 p.5 dataset 说明给出论证模式、变式与指令；p.6 给出正则抽取与偏差指标；p.13 Appendix C 给出加权偏差公式。 | 关键构念（形式/实质、有效/无效、左右倾向、偏差）均有可观测操作化与计分程序，足以复现实验材料与指标。 |
| A8 | 水平数与类型 | 0.5 | p.5 Table 3: four variations default/conlast/perm/rand; p.5: '0 FS, 8 FS, 32 FS'; p.5: '384 argument patterns'. | 报告了主要因素的水平数与标签；但未说明水平类型（名义/等级/连续）、间距与全距、连续变量中心化等。 |
| A9 | 单一操作化的风险 | 0.5 | p.5: 'We devise 4 variations for each... yielding 192 basic patterns' and total 384 argument patterns; p.9 ablation with chess/poker dataset gives 'a picture similar to Figure 1'. | 采用多个论证模板、变式和非政治消融，具备多操作化；但会聚证据主要是描述性相似，未报告正式会聚/信度指标。 |
| A10 | 单一方法的风险 | NA | — | 这不是自陈式多构念测量；自变量是外部构造的 prompt/样本条件，因变量是模型标签输出，共同方法偏差检验在此不是有意义的设计组件。 |
| B1 | 被试间设计 | NA | — | 无人类被试或独立被试组分配到处理条件；这是 LLM 基准评测，模型配置为固定评估对象，不适用被试间设计。 |
| B2 | 被试内设计 | NA | — | 每个样本为独立单轮 prompt，未形成需要被试内顺序平衡的人类重复测量设计；不按人类被试内设计编码。 |
| B3 | 混合设计 | NA | — | 无组间/组内混合的被试设计，也没有相应混合 ANOVA 误差项结构，故不适用。 |
| B4 | 因子设计 | 0.5 | p.5 报告多因素水平（形式/实质、有效/无效、左右、4 种变式、0/8/32 FS），p.5 给出 384 patterns/3216 English samples；但无完整逐格设计矩阵或 ANOVA 主效应/交互表。 | 存在多因素交叉的基准数据结构；但未报告完整设计矩阵、每格样本量和正式 ANOVA/交互统计量，仅部分满足。 |
| B5 | 主效应 | 0.5 | p.7 Figure 1 and p.7 text report accuracy varying by few-shot, validity and formal/material; p.8 discusses average differences. | 报告了描述性主效应趋势（few-shot、形式/实质、有效/无效），但无 F/df/p/效应量等完整统计量，也未在交互显著时限定主效应解释。 |
| B6 | 交互作用 | 0.5 | p.7 Figure 1 shows accuracy by validity/formal-material/variation; p.8 discusses 'the effect of the “rand” variation'; no interaction F/df/p or error bars reported. | 报告了若干亚组比较与变式效应模式，但没有正式交互检验、简单效应和多重比较校正，图示也未给误差棒/CI。 |
| B7 | 区组设计 | NA | — | 没有区组/分层随机分配设计；模型与样本分层是评估结构，不是实验区组设计。 |
| B8 | 拉丁方 | NA | — | 不存在需要拉丁方平衡的被试内条件顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验；无人类非随机分组与因果效应估计问题。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理，因此不涉及处理可逆性或迁移对称性论证。 |
| C1 | 随机化 | NA | — | 基准评测把所有样本交给所有模型配置，没有需要随机分配的人类/被试单位；不适用随机化分配组件。 |
| C2 | 平衡 | NA | — | 未使用需要条件顺序平衡的被试内设计；few-shot 组合平衡属于示例选择问题，不按条件顺序平衡编码。 |
| C3 | 恒定 | 0.5 | p.13 reports hardware; p.14 Table 6 lists model names, precision and HF sources; p.5 says samples are balanced. | 报告了部分恒定条件（硬件、模型版本、精度、平衡 few-shot），但未系统列出所有环境/生成参数，也未充分讨论恒定条件对外部效度的限制。 |
| C4 | 匹配 | NA | — | 没有匹配/配对分配程序，不适用匹配设计。 |
| C5 | 纳入为变量 | NA | — | 没有将混淆变量作为协变量纳入模型或做 ANCOVA；模型/精度等作为分组评估因素而非协变量，故不按此组件编码。 |
| C6 | 盲法 | NA | — | 不涉及人类被试、主试或评分者盲法；自动抽取与人工检查不是条件盲法设计。 |
| C7 | 平衡的层级 | NA | — | 无被试内条件顺序平衡层级，故不适用。 |
| D1 | 练习效应 | NA | — | 每个 prompt 基本独立，LLM 无人类式练习效应；无练习块或试次位置控制问题。 |
| D2 | 疲劳效应 | NA | — | LLM 评估无人类疲劳效应；无 session 时长/休息安排的需要。 |
| D3 | 延滞 / 迁移效应 | NA | — | 样本独立单轮判断，未设置跨条件交叉或清洗期；不涉及延滞/迁移效应。 |
| D4 | 不对称迁移 | NA | — | 无跨条件残留或不对称迁移问题；每样本独立编码。 |
| D5 | 范围效应 | NA | — | 因变量为标签正确率和偏差分数，不是绝对判断/量表评分；无范围效应问题。 |
| E1 | 位置 / 顺序偏差 | 0.5 | p.5 Table 3 includes conlast (conclusion to the end), perm (reorder premises), rand; p.7 Figure 1 reports effects of these variations. p.27 says 8 FS left-leaning examples followed by right-leaning, 32 FS random order. | 明确操纵了前提顺序/结论位置并报告其影响，也部分说明 few-shot 顺序；但测试样本本身未报告随机化/完整反平衡方案，故为部分满足。 |
| E2 | 默认赞同 | NA | — | 不使用 Likert/态度自评量表，无反向计分与默许偏差问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 不使用等级量表，也不做跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试，不存在需求特征或事后访谈检查。 |
| E5 | 实验者效应 | NA | — | 数据采集完全自动化，无人类主试/评分者的实验者效应。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.7 Table 4 reports mean accuracy by LLM, language and validity; e.g., gpt-4o English valid = 0.99. No SD/skew/endpoint frequencies or pilot difficulty calibration reported. | 报告了均值可看出部分接近天花板的格；但未报告分布形态/端点频率，也未说明难度校准，故部分满足。 |
| E7 | 共同方法偏差 | NA | — | 不是同源自陈式多构念测量；自变量为外部 prompt 条件，因变量为模型标签，CMB 不是适用组件。 |
| F1 | 统计结论效度 | 0.5 | p.16 Table 10 reports mean bias, N, SD, Z-stat; p.8 reports bias percentages. No power analysis, CIs, or multiple-comparison correction reported. | 报告了效应量性质的偏差分数、N、SD 与显著性检验；但缺样本量依据、CI 与多重性校正说明。 |
| F2 | 内部效度 | 0.5 | p.5 describes controlled synthetic sample construction; p.6 reports three runs and discards; no random assignment/concealment or baseline equivalence. | 通过构造数据和变式控制了一部分内部效度威胁，但无随机分配、分配隐藏或基线等价性/被试流向，故部分满足。 |
| F3 | 构念效度 | 0.5 | p.6: manual check of 500 outputs 'precision over 98%'; p.5 reports many argument patterns; p.9 discusses bias amplitude; no formal construct validity or manipulation check. | 报告了抽取精度的质量检查与多模板操作，但缺少正式信度/效度证据和操纵检验，故部分满足。 |
| F4 | 外部效度 | 0.5 | p.1 abstract: samples 'synthetically generated... covering both English and German'; p.10 limitations: 'rather schematic test dataset'; p.9 cross-language and non-political ablation. | 报告了样本来源、语言和部分推广边界；但无代表性抽样或跨样本复现，故部分满足。 |
| G1 | 分析单位 | 0.5 | p.6 describes model/sample evaluation; p.16 Table 10 reports N≈9,600 outputs per model and Z-tests; no mixed model for item/model nesting. | 说明了模型和样本层面的评估结构，但统计分析把输出当作独立观测，未显式处理样本/模板/模型嵌套，故部分满足。 |
| G2 | 随机效应 | 0 | p.14 Table 6 lists fixed model configurations; p.16 hypothesis tests are per model; no random-effects structure reported. | 模型/配置被当作固定对象，未报告随机效应与随机截距/斜率；对“LLM 总体”的推广缺少随机效应建模。 |
| G3 | 材料作为随机效应 | 0 | p.5: '384 argument patterns' derived from finite templates; p.15 Table 9 reports bias by inference kind; no item random effect or F′/mixed model. | 材料/论证模板被视为固定刺激，未把项目作为随机效应，存在将结论推广到任意材料的风险。 |
| G4 | 统计功效 | 0.5 | p.16 Table 10 reports N, SD, Z-stat and bias means; p.8 reports bias scores. No a priori power analysis or CI. | 报告了效应量性质的偏差分数，但无事前功效分析或样本量论证，也缺 CI，故部分满足。 |
| G5 | 研究者自由度 | 0.5 | p.6 reports discarded samples and a first-run discard of 252 German samples; p.14 Tables 7-8 report discarded counts; p.6 describes regex extraction. | 披露了排除规则、数量与部分异常；但未完整区分验证性/探索性分析，也未说明全部停止规则。 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及公开预注册、注册编号或数据收集前分析计划。 | 无预注册；属事后报告的分析流程，故为 0。 |
| J1 | 位置偏差 | NA | — | 不涉及 LLM-as-judge 的候选位置 A/B 交换或排序判断；结论位置/前提顺序已在 E1 处理。 |
| J2 | 冗长偏差 | NA | — | 不涉及用 LLM 裁判评估开放生成质量或长度偏好；因变量为标签正确率/偏差。 |
| J3 | 谄媚 | NA | — | 没有用户先验立场、反馈或纠错对话操纵；任务是闭卷式推理判定。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 评估模型输出；无裁判自我偏好问题。 |
| J5 | 少样本示例选择与排列偏差 | 0.5 | p.27: 8 FS composition balanced by valid/invalid, gender, leaning; 32 FS balanced and 'present the examples in a random order'; 8 FS 'left leaning examples followed by right leaning examples'. | 报告了示例来源、数量与标签/属性比例，并说明 32 FS 随机顺序、8 FS 固定左右顺序；但只用一套 held-out 示例，未做多 seed/多示例集重采样，模板也仅部分给出。 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | p.5: 'total variation of 9 instruction patterns' for each inference kind; p.26 Tables 21-24 give instruction templates in English/German. | 提供了完整指令模板并做语义措辞变化，但未报告版本/日期、dev/test 划分或系统 prompt 搜索过程，属部分满足。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 没有长上下文或 RAG 设置；每个 prompt 仅含短论证和 few-shot 示例。 |
| J8 | 温度与采样随机性 | 0.5 | p.6: 'We run the entire experiment three times and average over the results'; p.14 Table 6 gives model snapshots/precision. No temperature/top-p/seed reported. | 有三次重复运行和模型版本，但缺采样超参、seed、逐次方差/CI，故部分满足。 |
| J9 | 重复与文本退化 | 0 | p.6: 'we set no limits to output length' and used regex extraction; no decoding strategy or repetition/degeneration rate reported. | 任务含自由推理输出，适用；但未报告 greedy/sampling、repetition penalty、重复率或截断规则，故为 0。 |
| J10 | 分词效应 | 0 | p.7 Table 4 compares English vs German accuracy; no tokenizer name/version or token/word ratio reported. | 存在跨语言比较，分词/脚本差异是实际风险；但未记录分词器或控制 token 数，故为 0。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.5 describes a newly constructed dataset; p.14 lists model names/versions; no training cutoff vs dataset overlap or contamination check reported. | 未报告测试集与训练截止日期对照，也未做污染检测；不能把分数直接视为无污染泛化。 |
| J12 | 基准饱和 | 0.5 | p.7 Table 4 reports accuracy values, including gpt-4o English valid 0.99; p.8 calls gpt-4o an exception but does not analyze ceiling/saturation. | 报告了分数量程和接近上限的格，但未在接近天花板时改用连续指标或 CI 比较，故部分满足。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；指令只是任务提示，格式抽取另在 J14 处理。 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | p.26 instructions require ending with **valid** or **invalid**; p.6 describes regex extraction; p.14 Tables 7-8 report discarded samples. | 报告了格式约束与解析失败数量，但没有正式格式合法率、重试策略，且未区分格式失败与内容错误，故部分满足。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱或有害请求评估。 |
| J16 | LLM 作为被试的范式定位 | 0.5 | p.2 defines 'shallow heuristic' and 'bias' with references to human cognition; p.9 discusses safety implications; p.14 reports model versions. | 把 LLM 判断作为政治偏差/浅层启发式来研究，并与人类概念作了部分理论连接；但无系统构念效度论证或人类对照，故部分满足。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 不涉及随规模/训练进展宣称涌现能力的能力曲线。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 没有对代理指标进行训练/RL/best-of-N 优化；纯基准评估。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | p.6: three runs averaged; p.14 Table 6 gives gpt-4o-2024-08-06, gpt-4o-mini-2024-07-18 and open-model HF sources/precision. No seeds, CIs or paired tests. | 报告了重复次数与较精确的模型 snapshot；但缺 bootstrap CI、配对检验、开源模型 commit/seed，故部分满足。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验严格单轮，无多轮对话历史累积，也不主张多轮部署一致性。 |

## 编码小结
该研究的优点是数据集构造清晰、包含形式/实质推理与左右倾向的逻辑等价配对、报告了指令/few-shot/论证变式消融、给出偏差指标及三语言/模型比较；但作为 LLM 基准评测，许多实验心理学设计组件不适用。适用组件中，多数只能给 0.5：关键操纵和评分可复现，但缺少操纵检验、正式信效度、采样参数、随机/项目层次建模、功效分析、预注册、污染/饱和分析等。人类被试分配与顺序平衡类组件因无人类被试而记 NA；LLM 特有的 few-shot、prompt、跨语言、评估可复现性等按实际风险编码。
