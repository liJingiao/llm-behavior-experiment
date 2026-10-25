# article_158 | Fool Your (Vision and) Language Model with Embarrassingly Simple Permutations | 2024

研究类型概述：纯 LLM/VLLM 基准与对抗评测研究：以多项选择问答（MCQA）题目为分析单位，操纵/比较选项排列攻击、位置轮换、选项剪枝、不同提示/攻击方式、防御与微调策略，评估模型准确率变化；不属于人类被试实验。
- **研究构念（Construct）**：多项选择中的选择不变性、顺序敏感性、位置偏差与虚假符号关联｜CA 构念锚定：推理（reasoning, `trm_4a3fd79d0aec1`）；决策（decision making, `trm_4a3fd79d0a038`）
- **实验任务与范式（Task / Paradigm）**：只依据纯文本LLM实验：多种现成LLM在MMLU、ARC-Challenge、BoolQ、SocialIQA和MedMCQA上回答语义不变但选项顺序不同的问题，并进一步减少干扰项、固定正确答案位置、改变选项符号和比较推理期缓解方法。视觉模型与LoRA微调单元不作为纳入依据。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | p.2: “simply iterate through the possible permutations of MCQ options… cease permutation once the model produces an incorrect prediction”; p.3: Table 3 compares original vs adversarial attack. | 主自变量为原始选项顺序 vs 对抗排列，并报告了搜索程序与多个变体；但未报告正式操纵检验或完整分配程序，故为部分满足。 |
| A2 | 因变量 | 0.5 | p.3: “We use accuracy as our primary metric… extract the probability assigned to each choice in the first position. The option with the highest probability is then selected”; greedy decoding for reproducibility. | 因变量指标与计分方式明确，但缺少信效度证据及连续指标预处理/端点效应说明。 |
| A3 | 控制变量 | 0.5 | p.3: “we use greedy decoding to ensure reproducibility”; p.3: experiments on A100-80GB GPUs; p.2-3 lists models and public datasets. | 报告了部分控制手段（贪心解码、固定设备、公开数据/模型），但未系统列出控制变量清单及逐项控制方式。 |
| A4 | 混淆变量 | 1 | p.4: “To analyse whether position bias can explain our results, we compare our adversarial permutation results to the performance… under position bias analysis”; p.5: symbol-content spurious correlation analysis. | 明确识别并检验了位置偏差与符号—内容虚假相关等替代解释，并讨论了排列攻击效应不能由位置偏差完全解释。 |
| A5 | 调节变量 | NA | — | 全文无调节变量理论假设、测量/操纵方式或交互检验；研究为基准评测，不适用调节模型。 |
| A6 | 中介变量 | NA | — | 全文无中介变量定义、路径分解或中介效应检验；研究不包含中介模型。 |
| A7 | 操作性定义 | 0.5 | p.2 Eq.(1): maximize loss over permutations; p.3: prompt option symbols and select highest-probability choice. | 关键构念有可重复算法与计分，但正文未给出完整 prompt 模板，部分复现细节依赖代码链接，操作化不完整。 |
| A8 | 水平数与类型 | 0.5 | p.2: iterate possible permutations; p.3: model sizes 7B/13B/20B/70B; p.5: “reducing the number of total choices from four to either three or two”. | 报告了主要条件及水平取值，但未系统说明水平类型、间距/全距及连续变量中心化等。 |
| A9 | 单一操作化的风险 | 1 | p.4: position bias analysis; p.4-5: CircularEval and symbol attack; p.5: answer-set pruning; p.4-5: multiple datasets/models. | 关键构念使用多种操作化（位置轮换、循环评估、符号攻击、剪枝、不同数据集）并有比较结果，报告了会聚性证据。 |
| A10 | 单一方法的风险 | NA | — | 研究使用客观 MCQA 准确率，非自陈式多构念测量；无共同方法偏差意义上的同源自评问题。 |
| B1 | 被试间设计 | NA | — | 无人类被试或被试组分配；模型/数据集的比较不是随机分配的独立被试组。 |
| B2 | 被试内设计 | NA | — | 不是标准的被试内重复测量设计；主攻击按每题搜索到首次错误即停止，未报告完整条件顺序平衡或顺序组分配。 |
| B3 | 混合设计 | NA | — | 不存在组间/组内混合设计，也未使用混合设计统计模型。 |
| B4 | 因子设计 | NA | — | 模型×数据集×条件主要作为描述性基准网格呈现，未做因子设计方差分析或报告交互项。 |
| B5 | 主效应 | NA | — | 无因子设计意义上的主效应统计检验。 |
| B6 | 交互作用 | NA | — | 无交互项统计检验或简单效应分析。 |
| B7 | 区组设计 | NA | — | 无区组/分层设计。 |
| B8 | 拉丁方 | NA | — | 无拉丁方顺序设计。 |
| B9 | 准实验设计 | NA | — | 不是准实验设计，也不做人类因果效应推断。 |
| B10 | 被试内设计的适用条件 | NA | — | 无人类被试内处理可逆性/迁移对称性问题。 |
| C1 | 随机化 | NA | — | 无随机分配；基准条件由确定性评估和对抗搜索产生，研究单位未被分配到互斥实验条件。 |
| C2 | 平衡 | NA | — | 无人类被试条件顺序平衡；选项位置控制主要在 E1/J1 中体现。 |
| C3 | 恒定 | 0.5 | p.3: “we use greedy decoding to ensure reproducibility”; p.3: experiments on A100-80GB GPUs; p.2-3: public checkpoints and datasets. | 提到部分恒定控制（解码、设备、公开权重/数据），但未系统列出所有恒定变量及其水平，也未讨论外部效度限制。 |
| C4 | 匹配 | NA | — | 未使用匹配设计。 |
| C5 | 纳入为变量 | 0.5 | p.4: compares adversarial permutation with position-bias analysis; Table 6 reports slot-specific accuracy. | 测量并比较了位置偏差这一潜在混淆，但未将其作为协变量/区组纳入同一模型，也未检验斜率齐性或调整后效应。 |
| C6 | 盲法 | NA | — | 无人类被试、主试或评分者盲法安排。 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡层级选择问题；非被试内顺序设计。 |
| D1 | 练习效应 | NA | — | LLM 评估为独立提示/单轮问答，无跨试次练习效应；ICL 示例是提示上下文而非练习块。 |
| D2 | 疲劳效应 | NA | — | 无人类 session 时长或疲劳控制问题。 |
| D3 | 延滞 / 迁移效应 | NA | — | 各提示/条件独立评估，无药物或学习式跨条件残留；不涉及清洗期。 |
| D4 | 不对称迁移 | NA | — | 无跨条件迁移对称性问题。 |
| D5 | 范围效应 | NA | — | 因变量为客观准确率，不涉及主观量表范围效应。 |
| E1 | 位置 / 顺序偏差 | 1 | p.2: iterate through possible permutations; p.4: “always rotating the correct answer to a specific slot (A/B/C/D)”; p.5 Table 6 and p.15 Figure 4 report position/permutation patterns. | 系统进行了选项排列与正确项位置轮换，并报告各位置/排列下的准确率；顺序/位置偏差控制充分。 |
| E2 | 默认赞同 | NA | — | 研究不使用 Likert/态度自评量表，无默认赞同问题。 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无等级量表得分分布或跨群体反应风格比较。 |
| E4 | 需求特征 | NA | — | 无人类被试需求特征；LLM 评估无掩饰情节/事后访谈设计。 |
| E5 | 实验者效应 | NA | — | 完全自动化模型评估，无人类主试/评分者期望传递问题。 |
| E6 | 天花板 / 地板效应 | 0.5 | p.3: accuracy metric; p.4 Table 3 includes “Random Chance”; p.5 notes many conditions below chance after attack. | 报告了均值准确率与随机水平，并指出低于机会水平；但未报告标准差、偏度、端点频率或 pilot 难度校准。 |
| E7 | 共同方法偏差 | NA | — | 无自陈式同源多构念测量，不涉及共同方法偏差程序/统计控制。 |
| F1 | 统计结论效度 | 0.5 | p.2 Tables 1-2 report #QA pairs; p.4 Table 3 reports accuracy and relative drops; no confidence intervals or multiplicity correction. | 报告了样本规模和准确率/相对下降等效应信息，但缺少置信区间、正式功效分析、多重性校正和统计假设检验。 |
| F2 | 内部效度 | NA | — | 无随机分配、分配隐藏、被试流向或损耗；不是人类因果实验设计。 |
| F3 | 构念效度 | 0.5 | p.4-5 compares position bias, CircularEval, symbol attack and adversarial permutation; p.2-3 uses many models/datasets. | 通过多种攻击/数据集提供构念相关证据，但未报告正式信度/效度指标或操纵检验统计量。 |
| F4 | 外部效度 | 0.5 | p.3: “a diverse array of language and vision-language MCQA datasets… ensuring our findings are generalizable”; p.4-5 reports cross-dataset/model replications. | 报告了多模型、多数据集来源与跨数据集结果，但未系统说明抽样代表性、纳入排除标准和推广边界。 |
| G1 | 分析单位 | 0.5 | p.3: accuracy computed over QA pairs; p.15 Figure 4 analyzes per-question permutation proportions; no hierarchical/mixed model. | 分析单位可辨认为 QA 题目/回答，但同一题目的多次排列被聚合，未显式处理题目嵌套于数据集/排列的聚集结构。 |
| G2 | 随机效应 | NA | — | 未使用混合效应模型；各模型是固定评估目标而非从模型总体随机抽样的随机效应单位，无随机效应推断需求。 |
| G3 | 材料作为随机效应 | NA | — | 测试题目是基准观测项而非实验操纵的材料因素；论文未做项目层随机效应推广，也无混合模型分析。 |
| G4 | 统计功效 | 0 | p.2 Tables 1-2 give QA-pair counts, but no power analysis; p.4 results are mean accuracies without CIs. | 无事前功效分析或样本量论证，结果未报告置信区间。 |
| G5 | 研究者自由度 | 0.5 | p.3 lists models/datasets; p.12 Appendix A.2 enumerates additional prompting/attack analyses; p.6-7 reports defenses and fine-tuning. | 报告了大量条件与因变量，但未报告试次/题目排除规则、样本量停止规则，也未明确区分验证性与探索性分析。 |
| G6 | 预先设定 / 预注册 | 0 | p.1-p.8 contains no preregistration statement, registry identifier, or prespecified analysis plan. | 无公开预注册或时间戳早于数据收集的分析计划；按缺失记 0。 |
| J1 | 位置偏差 | 1 | p.2: permutation over option order; p.4: position-bias condition rotating correct answer to A/B/C/D; p.5 Table 6 and p.22 qualitative examples. | 明确分析并控制候选项位置/顺序，报告各位置准确率与排列攻击结果；未使用 LLM-as-judge，故裁判相关子项不适用。 |
| J2 | 冗长偏差 | NA | — | 评估为严格 MCQA 选项准确率，不涉及开放生成长短比较或 LLM 裁判长度偏差。 |
| J3 | 谄媚 | NA | — | 任务无用户先验立场/纠错反馈输入，不涉及谄媚操纵。 |
| J4 | 自我偏好 | NA | — | 不使用 LLM-as-judge 或成对模型输出裁判，无自我偏好风险。 |
| J5 | 少样本示例选择与排列偏差 | 0 | p.12: “Table 20 compares the performance before and after adversarial attack with in-context learning”; p.18-20 ICL tables report results but no shot count/source/order. | 确实使用 ICL/few-shot 变体，但未报告示例来源、每类数量、标签比例、排列平衡或多 seed 重采样。 |
| J6 | 提示敏感性 / 脆弱性 | 0 | p.3 describes option-symbol prompting and probability extraction; p.1 only gives code link; full prompt template/version not provided. | 正文未给出完整 prompt 模板、版本、敏感性消融或 dev/test 划分；代码链接不足以满足完整模板要求。 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 无长上下文或 RAG 设置；输入为短 MCQA 提示。 |
| J8 | 温度与采样随机性 | 0.5 | p.3: “we use greedy decoding to ensure reproducibility”; p.21 Table 26 compares temperature=0.5/1.5, top-k, nucleus sampling. | 报告了主要解码策略并做了温度/采样比较，但未报告随机种子、每条件重复次数及置信区间。 |
| J9 | 重复与文本退化 | NA | — | 任务为短选项输出/概率抽取，不涉及开放生成退化或重复率问题。 |
| J10 | 分词效应 | NA | — | 单语言英文基准，无跨语言/跨脚本比较，无分词长度混淆风险。 |
| J11 | 测试集污染 / 数据泄漏 | 0 | p.3 lists public datasets and model names; no test-set release date vs training cutoff comparison or contamination detection. | 使用公开基准但未做污染检查、n-gram 重叠或训练截止日期对照，不能排除记忆/污染。 |
| J12 | 基准饱和 | 0.5 | p.4 Table 3 reports baseline accuracies and random chance; some datasets/models are near ceiling (e.g., BoolQ/GPT), but no SOTA/saturation analysis. | 报告了基准分数与随机水平，但未系统说明当前 SOTA、天花板风险或饱和时的连续指标替代。 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为因变量；任务是 MCQA 准确率评估，无约束指令遵循指标。 |
| J14 | 输出格式约束 / 结构化输出 | NA | — | 未要求 JSON/文法约束等结构化输出；仅做选项符号概率抽取，无格式合法率实验。 |
| J15 | 越狱稳健性 | NA | — | 不涉及安全/越狱评估，无有害请求或对抗越狱设置。 |
| J16 | LLM 作为被试的范式定位 | NA | — | 研究为工程/应用型基准与对抗鲁棒性评估，不主张测量人类心理学/认知构念。 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 虽比较不同模型规模，但未报告“涌现能力”曲线或相关主张；不属于涌现争议研究。 |
| J18 | 指标博弈与奖励过优化 | NA | — | 研究未以 benchmark/奖励模型/LLM-judge 作为代理指标进行优化，无 overoptimization 设计。 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0 | p.3 lists model names and greedy decoding; no exact snapshot/commit/API date, no repeated runs, no confidence intervals or paired tests. | 评估可复现性报告不足：缺少精确模型快照、重复次数、CI 和配对比较。 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 实验为单轮 MCQA，无多轮对话历史累积或一致性衰减问题。 |

## 编码小结
论文系统展示了 LLM/VLLM 对 MCQA 选项排列的脆弱性，覆盖多模型、多数据集，并对位置偏差、符号—内容虚假相关、剪枝、ICL、采样策略和多种防御做了丰富比较。主要不足是描述性基准评测为主，缺少置信区间、重复采样、精确模型快照/日期、污染检查、完整 prompt 模板与正式功效分析；大量人类实验设计组件对本研究不适用。
