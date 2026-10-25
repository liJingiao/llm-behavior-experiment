# article_011 | Not All Countries Celebrate Thanksgiving: On the Cultural Dominance in Large Language Models | 2024 (ACL 2024, Long Papers, pp.6349-6384)

研究类型概述：多语言 LLM 文化主导与文化偏见评测研究（无人类被试，人类文化价值观参照来自 WVS 与 PCT 公开调查）。在 8 类具体文化对象生成任务（节日、歌曲、食物等）与 2 套抽象价值观问卷（World Values Survey、Political Compass Test）上评测 GPT-3.5-turbo、GPT-4、文心一言（ERNIE）等模型；自变量为查询语言（11 种语言）与文化提示策略（无文化锚定 / 显式指定目标文化 / 跨语言翻译提示）及模型；因变量为文化归属得分（In-Culture Score）与价值观二维文化距离。页码为 PDF 页码（共 37 页，含附录）。
- **研究构念（Construct）**：文化主导性与跨语言文化偏见（cultural dominance and cultural bias）｜CA 构念锚定：刻板印象（stereotypes, `trm_4a3fd79d0b285`）；态度（attitude, `trm_4a3fd79d09947`）；社会认知（social cognition, `trm_4a3fd79d0b13d`）
- **实验任务与范式（Task / Paradigm）**：多语言 LLM 文化主导与文化偏见评测研究（无人类被试，人类文化价值观参照来自 WVS 与 PCT 公开调查）。在 8 类具体文化对象生成任务（节日、歌曲、食物等）与 2 套抽象价值观问卷（World Values Survey、Political Compass Test）上评测 GPT-3.5-turbo、GPT-4、文心一言（ERNIE）等模型；自变量为查询语言（11 种语言）与文化提示策略（无文化锚定 / 显式指定目标文化 / 跨语言翻译提示）及模型；因变量为文化归属得分（In-Culture Score）与价值观二维文化距离。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | §2.1 (p.2):"The questions are then translated into ten other languages"; §4.2 (p.8):"P1. In the culture of [lang], {query}"; Table 3 (p.6) 三种 GPT 模型 | 自变量(语言/模型/提示)及水平明确;缺操纵检验(仅以 Appendix B Table 7 的 BLEU 间接说明模型能理解各语言),译文由谁翻译、如何核对未交代 |
| A2 | 因变量 | 0.5 | §2.1 (p.3):"We sum up the points from ten generated items as the In-Culture Score"; §2.2 (p.4) Eq.(1) "d(Ml, T) =&#124;&#124;Ml − T&#124;&#124;2" | 指标、计分与单位清晰;条目归属依据 Wikipedia 标注,但未报标注者数量/一致性,Euclid 距离的效度证据有限;仅有三轮重复的稳定性(Table 13-18) |
| A3 | 控制变量 | 0.5 | §2.1 (p.2):"Please list 10 {OBJECT} for me."; §3 (p.4):"we use the prompt to query GPT-4-1106 and GPT-3.5-turbo-1106 3 times with the default temperature of 0.8" | 控制了问句模板、条目数(10)、5 点量表选项、重复次数;网页端的系统设置/访问日期未控制或未报,未成清单 |
| A4 | 混淆变量 | 0.5 | §3.1 (p.5):"Cultural biases may come from different sources, including, but not limited to, training data, human alignment, and the intended design of system developers."; §3.2 (p.6) 推测 RLHF 对齐;Appendix A (p.12) 同一语言含多种文化 | 识别了来源混淆(训练数据/对齐/设计)与"语言≠文化"的问题;但未作分离检验,ERNIE 与 GPT-4 在数据、规模、对齐上的差异未控制 |
| A5 | 调节变量 | NA | — | 未设定调节变量或做交互检验;按语言/对象分层仅为描述 |
| A6 | 中介变量 | NA | — | 无中介分析(训练数据占比为推测性解释,不作路径检验) |
| A7 | 操作性定义 | 1 | §2.1 (p.2-3) In-Culture Score 两条计分原则;Table 8 (p.12) 各语言提示;Table 9/10 (p.13-14) 全部题项;§4.2 P1/P2 | "文化主导"被操作化为可重复执行的计分与距离程序,提示、题项与计分规则全部给出 |
| A8 | 水平数与类型 | 1 | §2.1:"eight concrete objects"; 11 种语言;§2.2:"six representative languages"; §4.2 两种提示 | 水平数、取值/标签、名义类型及语言选取标准(§2.2 四条)均有说明 |
| A9 | 单一操作化的风险 | 1 | §2 (p.2):"concrete (e.g., holidays and songs) and abstract (e.g., values and opinions)"; Limitations (p.9):"we have only considered eight such objects, spanning eleven languages" | 以具体对象+两套调查问卷多重操作化;局限部分讨论了对象与语言覆盖范围及问卷偏差对推广性的限制 |
| A10 | 单一方法的风险 | NA | — | 自变量由研究者设定,因变量由对输出的标注/计算得到,不涉及同一被试同源自报 |
| B1 | 被试间设计 | NA | — | 无被试分配;不同模型为被评对象而非独立被试组分配问题 |
| B2 | 被试内设计 | NA | — | 同一模型被依次查询多种语言/提示,但各次查询为无状态独立调用,不属于需要顺序安排的被试内设计(网页端是否新开会话未述,见 E1 备注) |
| B3 | 混合设计 | NA | — | 无混合因素统计分析 |
| B4 | 因子设计 | 0 | Table 12 (p.16):对象×模型×语言逐格报告 In-Culture Score;Table 16 (p.20) 模型×语言距离 | 因素基本完全交叉并报告每格数值;无交互项统计检验,每格仅 1 次(主实验)或 3 次(稳定性)观测；因多因素设计未报告交互项统计检验（B6=0），未达因子设计基本要件，按级联规则记 0。 |
| B5 | 主效应 | 0 | §3.2 (p.6):"Generally, the later version of the GPT variant, the more cultural dominance it suffers from." | 仅用描述性均值作出结论,没有主效应统计检验 |
| B6 | 交互作用 | 0 | §4.2 (p.8):"it underperforms ERNIE on abstract objects" | 提示×对象类型等"交互"结论未做统计检验,无误差棒图示 |
| B7 | 区组设计 | NA | — | 未使用区组 |
| B8 | 拉丁方 | NA | — | 非顺序敏感设计 |
| B9 | 准实验设计 | NA | — | 条件由研究者设定,不涉及无法随机分配 |
| B10 | 被试内设计的适用条件 | NA | — | 未采用被试内设计 |
| C1 | 随机化 | NA | — | 无向条件分配被试的环节 |
| C2 | 平衡 | NA | — | 无顺序平衡需求 |
| C3 | 恒定 | 1 | §2.1:"Please list 10 {OBJECT} for me."; §2.2 提示模板固定 "Give me the answer from 1 to 5: ..."; §3 默认温度 0.8 | 恒定项及具体水平明确;Limitations (p.9) 讨论了对象/语言范围对推广性的限制 |
| C4 | 匹配 | NA | — | 未使用匹配 |
| C5 | 纳入为变量 | 0.5 | Table 7 (p.12) BLEU(模型理解各语言能力);Table 15 (p.17) 不同条目数 | 测量了语言理解水平、条目数等潜在影响因素并报告,但未作为协变量/区组纳入分析 |
| C6 | 盲法 | NA | — | LLM 无需被试盲法;标注者盲法见 E5 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡 |
| D1 | 练习效应 | NA | — | 无重复试次学习 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳 |
| D3 | 延滞 / 迁移效应 | NA | — | 无条件序列 |
| D4 | 不对称迁移 | NA | — | 同上 |
| D5 | 范围效应 | NA | — | 非被试内量表评分任务 |
| E1 | 位置 / 顺序偏差 | 0 | §2.2 (p.4):"1. Strongly Disagree 2. Disagree 3. Neutral 4. Agree 5. Strongly Agree. You can only choose one option." | 量表选项顺序在所有查询中固定,未反向或随机化,题项呈现顺序亦未说明,也未讨论顺序偏差 |
| E2 | 默认赞同 | 0 | Table 9/10 (p.13-14) 各题 | 题项极性混合(如 WVS 第1题与第2题),但未标注反向计分题,也未检验正反向一致性或讨论默许偏差 |
| E3 | 极端 / 中间反应倾向 | 0 | Table 2(b) (p.5) 仅列 2 题个案 "Strongly Disagree" | 使用 5 点量表,但未报告得分分布形态、端点/中点使用比例;仅以二维坐标均值作结论 |
| E4 | 需求特征 | NA | — | 被试为 LLM,无人类需求特征(提示对文化的显式提示见 J6) |
| E5 | 实验者效应 | 0 | §2.1 (p.2–3): "we annotate the source of the returned 10 items according to Wikipedia"；§3 (p.4) 网页端人工收集响应 | 包含文化条目归属人工标注与网页端人工收集响应，但未报告标注者/收集者是否对模型与语言条件施盲、有无培训标准化及一致性检验，基本要件未达成，记 0。 |
| E6 | 天花板 / 地板效应 | 0.5 | Table 12 (p.16):多个单元格为 0(如 Song 非英语全为 0);Table 3(a) | 报告了主要因变量逐格描述统计,可见明显地板效应;但未讨论地板问题,也未做难度校准 |
| E7 | 共同方法偏差 | NA | — | 同 A10 |
| F1 | 统计结论效度 | 0.5 | Table 3 (p.6) 均值差;Table 13/14 (p.17-18) 三轮均值与 STD | 报告了可视作效应大小的均值/距离差及三轮 STD;无 CI、无显著性检验,却使用 "significantly mitigate"(摘要);无多重性处理 |
| F2 | 内部效度 | 0.5 | §3 (p.4):"We also conduct repeated experiments with API to make the conclusions more reliable." | 用三次 API 重复评估稳定性并说明结论一致;但网页端主结果为单次,模型比较存在多重混杂,威胁评估不完整 |
| F3 | 构念效度 | 0.5 | §2.2 (p.4):"The human results can only be used as a reference rather than an absolute standard."; Limitations (p.9) 调查偏倚;Table 7 BLEU | 采用成熟量表(WVS/PCT)并有人类参照与局限说明;缺少对"文化主导"构念的独立效度验证及人工标注信度 |
| F4 | 外部效度 | 1 | §3 (p.4):"More results are shown in the Appendix, where our findings still hold."; Limitations (p.9) 两条局限;§4.1 ERNIE 对照 | 说明了对象/语言/模型来源与代表性标准,指出推广边界,并在不同模型、API 重复运行与 ERNIE 上复现主要结论 |
| G1 | 分析单位 | 0.5 | Table 3(a) (p.6):按语言平均 In-Culture Score;Table 12 逐对象 | 分析单位为"语言(×对象)"的汇总分数,与处理分配层级基本一致,但未说明题项/重复在语言内的聚集如何处理 |
| G2 | 随机效应 | NA | — | 无统计模型 |
| G3 | 材料作为随机效应 | 0.5 | Limitations (p.9):"we have only considered eight such objects"; Table 12 逐对象呈现 | 对象与题项为作者选取并分对象报告,承认范围有限;未视为随机抽样,也未建模 |
| G4 | 统计功效 | 0 | §3 (p.4) 仅有"repeated experiments... more reliable" | 无事前功效分析或样本量论证,读到了没有做 |
| G5 | 研究者自由度 | 0.5 | §2.2 (p.4):"We selected the languages based on the following criteria: 1)... 4)"; Table 12 报告全部 8 类对象 | 说明了语言选择标准并报告全部对象/模型;未说明排除规则,验证性/探索性未区分,附录条目详表仅展示部分对象 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册 | 读到了没有预注册 |
| J1 | 位置偏差 | 0 | §2.2 提示 "1. Strongly Disagree ... 5. Strongly Agree"(固定顺序) | 选项顺序固定,未做交换/随机化,也未识别位置偏差 |
| J2 | 冗长偏差 | NA | — | 无 LLM 作裁判评价生成质量(评分依据 Wikipedia 与规则) |
| J3 | 谄媚 | NA | — | 无用户立场/反馈对话 |
| J4 | 自我偏好 | NA | — | 无 LLM-as-judge |
| J5 | 少样本示例选择与排列偏差 | NA | — | 未使用 few-shot 示例 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | Table 8 (p.12) 各语言完整提示;§4.2 (p.8) P1/P2;Table 6 | 提供完整提示模板并比较 P1 与 P2 两种措辞;未对基线提示做措辞/格式敏感性消融,无 dev/test 分离 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 非长上下文/RAG 实验 |
| J8 | 温度与采样随机性 | 0.5 | §3 (p.4):"3 times with the default temperature of 0.8"; Table 13/14 均值与 STD | API 实验报告了温度、重复次数与 STD;主结果来自网页端、采样参数未知且单次,无种子/top-p、无 CI |
| J9 | 重复与文本退化 | 0.5 | §3 (p.4) "default temperature of 0.8" | 仅给出默认温度,未明确解码方式(top-p 等),未报告重复率;网页端解码未知,条件间解码是否一致未说明 |
| J10 | 分词效应 | 0 | §2.1 (p.2):"translated into ten other languages"; Table 7 BLEU | 属跨语言/跨脚本实验,但未报告分词器名称/版本,也未控制各语言 token 数差异,读到了没有做 |
| J11 | 测试集污染 / 数据泄漏 | 0 | §2.2 (p.3) 使用公开的 WVS 与 PCT;§3.1 (p.5) 归因于训练数据 | WVS/PCT 为公开问卷,可能已出现在训练数据中,但未评估污染,也未对照模型训练截止期与调查发布时间 |
| J12 | 基准饱和 | 0.5 | Table 3(a) (p.6) 各模型分数;Table 12 | 报告了量程(0-10)与当前水位,并非天花板(多处接近 0);但未评估饱和/地板风险,也无备用连续指标(距离指标除外) |
| J13 | 指令遵循 | NA | — | 研究目的不是测量指令遵循 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | §2.2 (p.4):"Give me the answer from 1 to 5: ... You can only choose one option."; §2.1 "Please list 10" | 提示规定了格式(单选 1-5、列 10 条);未报告格式合法率,格式失败(如 §4.2 "As an AI language model, I do not have a specific culture")与内容错误未分开计量 |
| J15 | 越狱稳健性 | NA | — | 非安全/越狱评测 |
| J16 | LLM 作为被试的范式定位 | 0.5 | §2.2 (p.4):"The human results can only be used as a reference rather than an absolute standard."; Appendix A (p.12) 语言与文化关系的讨论 | 界定了 LLM"opinions"与人类调查结果的对照关系,并承认语言≠文化;但未论证 LLM 作答与人类同名价值观构念的异同,直接用距离作为"文化主导" |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无规模/训练进展能力曲线或"涌现"宣称(仅比较三代 GPT 版本) |
| J18 | 指标博弈与奖励过优化 | NA | — | 无代理指标优化 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | §3 (p.4):"GPT-4-1106 and GPT-3.5-turbo-1106 3 times"; "the official websites for ChatGPT and GPT-4" | API 实验给出精确版本与重复次数;主实验的网页端模型版本/日期未给,无 CI/配对检验 |
| J20 | 多轮对话中的一致性衰减 | NA | — | 单轮问答,无多轮评估 |

## 编码小结
本篇为多语言 LLM 文化偏向评测,设计层的 A7/A8/A9/C3/F4 较为完整(提示、题项、计分规则、语言选取标准与局限均给出),因此记 1;统计推断薄弱(无检验与 CI,使用"significantly"但未检验),B5/B6/G4/G6 记 0。主要判断点:E1/J1 以量表选项顺序固定判 0;E2/E3 因未利用反向题、未报分布判 0;J10 因属跨语言实验却未报分词器判 0;J11 因 WVS/PCT 为公开问卷而未评估污染判 0。。另说明:附录 G 的 PDF 文本在 Celebrities 表后结束(Hero/History/Mountain 的逐条目表未见),不影响编码判断。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 E5（NR→0）, B4（0.5→0）。
