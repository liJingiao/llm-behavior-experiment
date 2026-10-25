# article_010 | CompeteAI: Understanding the Competition Dynamics of Large Language Model-based Agents | 2024 (ICML 2024, PMLR 235)

研究类型概述：LLM 多智能体竞争博弈模拟研究（无人类被试）。构建双餐厅竞争模拟环境（CompeteAI，由 GPT-4 驱动 2 家餐厅智能体与顾客智能体在 15 天内迭代互动），自变量为顾客类型（个体顾客 10 人 vs. 团体顾客 15 组，分别独立运行 9 次与 6 次）及模拟天数（Day 1–15）；因变量为两家餐厅的日客流占比、净收入、菜品评分、需求满足度及策略行为（差异化与模仿比例）。页码为 PDF 页码（共 17 页，含附录）。
- **研究构念（Construct）**：竞争动力学与策略性社会行为（competition and strategic social behavior）｜CA 构念锚定：社会认知（social cognition, `trm_4a3fd79d0b13d`）；决策（decision making, `trm_4a3fd79d0a038`）；信任（trust, `trm_N7MLgAsJBIbiQ`）
- **实验任务与范式（Task / Paradigm）**：LLM 多智能体竞争博弈模拟研究（无人类被试）。构建双餐厅竞争模拟环境（CompeteAI，由 GPT-4 驱动 2 家餐厅智能体与顾客智能体在 15 天内迭代互动），自变量为顾客类型（个体顾客 10 人 vs. 团体顾客 15 组，分别独立运行 9 次与 6 次）及模拟天数（Day 1–15）；因变量为两家餐厅的日客流占比、净收入、菜品评分、需求满足度及策略行为（差异化与模仿比例）。｜CA 任务锚定：CA 无直接任务条目（属社会调查/多轮交互/LLM 特定行为评测范式，依 v1.6 H.4/H.5 标注具体实验任务）

| 组件ID | 组件名 | 编码值 | 证据位置/引文 | 备注 |
|---|---|---|---|---|
| A1 | 自变量 | 0.5 | §3 (p.4):"We run experiments 9 and 6 times for individual and group customers, respectively"; §3.4.3 (p.6) | 明确操纵顾客类型(个体/团体)两个水平并给出各水平运行次数;缺操纵检验,团体与个体在成员构成上同时变化(个体 10 人、团体 15 组),分配程序未述 |
| A2 | 因变量 | 0.5 | §3.4.3 (p.6):"one restaurant has more than 80% of the customers until the competition ends (Day 15)"; §2.5 (p.4):"s = 0.5 × c/p + 0.5 × f/5000" | 赢者通吃阈值、菜品得分公式、菜单相似度等均有界定;但得分公式是作者"empirical mechanism",缺信效度证据;行为类别(差异化/模仿)的编码方式未交代 |
| A3 | 控制变量 | 0.5 | §3.4.1 (p.6):"If two restaurants share the same settings (cuisine type, initial funding)"; Fig.6 (p.13) Constraints 1)-4) | 列出了若干保持恒定/约束的变量(餐厅数、顾客数、天数、每日一餐、起始资金、模型版本),但无系统清单且部分取值(起始资金)未报 |
| A4 | 混淆变量 | 0.5 | §4 (p.7):"we doubt that the model could have already memorized these popular theories and examples, leading to these 'common' behaviors triggered by our prompts" | 识别了"训练数据记忆"这一混淆;但"竞争提升质量"未设无竞争对照,个体/团体差异与顾客构成混淆未讨论,残余混淆未检验 |
| A5 | 调节变量 | NA | — | 研究未设定调节变量或交互假设;个体/团体被作为主自变量 |
| A6 | 中介变量 | NA | — | 未做中介分析;"反馈环路"仅为叙述性机制解释 |
| A7 | 操作性定义 | 0.5 | Fig.7/Fig.8 (p.13-14) 提示模板含 "< Designed JSON format> ..."; Table 3 动作 API; Table 4/5 顾客特征; 摘要:"Code is available at https://github.com/microsoft/competeai" | 环境、API、顾客属性、赢者通吃定义可复现;但提示模板在文中被省略,差异化/模仿/马太效应等构念如何判定为发生(判定程序)缺失 |
| A8 | 水平数与类型 | 1 | §3 (p.4) 个体 vs 团体;§2.4 (p.3):"10 individual customers, 4 families, 4 colleagues, 3 couples, and 4 friends" | 水平数(2)、标签、名义类型明确;无连续水平 |
| A9 | 单一操作化的风险 | 0.5 | §6 (p.8):"(1) Sample Size and Diversity... (3) Version-Specific Findings. Our results are based on GPT-4-0613" | 竞争仅在单一餐厅情境、2 家餐厅、单一模型中操作化;局限部分讨论了样本多样性与版本,但未讨论"竞争"构念的单一操作化对推广性的限制 |
| A10 | 单一方法的风险 | NA | — | 自变量(顾客配置)由研究者设定,因变量来自模拟日志,不存在同一被试同源自报问题 |
| B1 | 被试间设计 | 0.5 | §3 (p.4):"9 and 6 times for individual and group customers" | 个体/团体条件由相互独立的模拟运行承担,实质为组间;但文中未明确用"被试间"表述,也未说明运行如何分配到条件及是否独立初始化 |
| B2 | 被试内设计 | NA | — | 同一模拟内的 15 天为动态过程而非条件重复测量;无被试内条件操纵 |
| B3 | 混合设计 | NA | — | 无混合因素统计分析 |
| B4 | 因子设计 | NA | — | 仅单因素(顾客类型),无交叉因素 |
| B5 | 主效应 | NA | — | 非因子设计 |
| B6 | 交互作用 | NA | — | 非因子设计 |
| B7 | 区组设计 | NA | — | 未使用区组 |
| B8 | 拉丁方 | NA | — | 非被试内顺序设计 |
| B9 | 准实验设计 | NA | — | 模拟环境内条件由研究者直接设定,不涉及无法随机分配的准实验情形 |
| B10 | 被试内设计的适用条件 | NA | — | 未使用被试内设计 |
| C1 | 随机化 | NA | — | 条件为研究者预设配置,无向条件分配被试的随机化环节;随机种子/采样随机性见 J8 |
| C2 | 平衡 | NA | — | 无条件顺序 |
| C3 | 恒定 | 0.5 | §2.2 (p.3):"2 restaurants and 50 customers... We set the simulation runs for 15 days"; "GPT-4 (0613)"; §6 局限(1)(2) | 列出恒定项并在局限中讨论外推;起始资金等具体水平未报 |
| C4 | 匹配 | NA | — | 未使用匹配 |
| C5 | 纳入为变量 | 0 | §3.3 (p.5) 仅分顾客类型比较决策理由 | 个体/团体的成员收入、口味、健康等特征差异未作为协变量/区组纳入分析,读到了没有做 |
| C6 | 盲法 | NA | — | 实验对象为 LLM 智能体,被试盲法不适用;分析者盲法见 E5 |
| C7 | 平衡的层级 | NA | — | 无顺序平衡 |
| D1 | 练习效应 | NA | — | 智能体跨日记忆与学习是被研究的现象本身,不是需控制的练习效应 |
| D2 | 疲劳效应 | NA | — | LLM 无疲劳 |
| D3 | 延滞 / 迁移效应 | NA | — | 无条件序列迁移 |
| D4 | 不对称迁移 | NA | — | 同上 |
| D5 | 范围效应 | NA | — | 非被试内量表评分任务 |
| E1 | 位置 / 顺序偏差 | 0 | Fig.8 (p.14):提示固定呈现 "RESTAURANT 1" 然后 "RESTAURANT 2"; §3.4.2 (p.6):"on Day 1, the majority of customers choose R1" | 读到餐厅呈现顺序固定、未随机或互换,也未讨论位置偏差;而"R1 初始优势"恰是核心发现,位置偏差未被排除 |
| E2 | 默认赞同 | NA | — | 无量表评分与反向计分题 |
| E3 | 极端 / 中间反应倾向 | NA | — | 无量表反应风格问题 |
| E4 | 需求特征 | NA | — | 被试为 LLM 智能体,不存在人类意义的需求特征 |
| E5 | 实验者效应 | 0 | §3.3 (p.5): "we summarized the reasons for different customers and categorized them into several primary topics" | 对顾客决策理由与餐厅策略行为（差异化/模仿）做了人工归纳分类，但未报告编码者盲法安排、培训标准化或评分者间信度，基本要件未达成，记 0。 |
| E6 | 天花板 / 地板效应 | 0.5 | Fig.5(b) (p.7):R2 客流降至 0,R1 稳定在 50;Fig.5(c) 菜品均分曲线 | 呈现了主要因变量的分布/端点(客流已触顶/触底);对饱和与难度校准无讨论 |
| E7 | 共同方法偏差 | NA | — | 同 A10 |
| F1 | 统计结论效度 | 0 | §3.4.3 (p.6):"winner-take-all happens more frequently in single customers (66.7%) and rarely for group customers (only happened once, which is 16.7%)"; Table 2 | 仅有百分比与均值,无显著性检验、置信区间、效应量;n=9 与 6 的小样本下直接作出因果性结论;样本量依据仅为成本 |
| F2 | 内部效度 | 0.5 | §3.4.4 (p.7):"We find that competition is the key factor in this improvement"; §4 (p.7) 记忆化讨论 | 分配程序未述;对威胁作了部分评估(记忆化),但缺无竞争对照,因果表述强于设计 |
| F3 | 构念效度 | 0.5 | §2.2 (p.3):"It is imperative to rigorously assess how well agents' behaviors... correspond to empirical human actions"; Table 2 与理论对照 | 以与经典理论的对应(Table 2)提供间接效度证据;承认需验证但未报告任何对人类数据的校验,菜品得分公式无效度证据 |
| F4 | 外部效度 | 0.5 | §6 (p.8):"our experiments did not involve a significant number of restaurants and customers"; "Version-Specific Findings" | 说明了样本(GPT-4-0613、2 餐厅、50 顾客)与局限;无跨情境/跨模型复现 |
| G1 | 分析单位 | 0.5 | §3 (p.4):"We run experiments 9 and 6 times"; Fig.3 按顾客/群体汇总所有实验 | 分析混用运行级(赢者通吃)与顾客/天级(决策理由、菜品分),未说明嵌套聚集(顾客嵌套于运行,天嵌套于运行)如何处理 |
| G2 | 随机效应 | NA | — | 无统计模型 |
| G3 | 材料作为随机效应 | 0 | §2.4 (p.3) 顾客由作者手工设定(Table 4/5) | 顾客与情境为作者设计的固定集合,未视为从总体抽样,结论却推广至一般竞争动力学 |
| G4 | 统计功效 | 0.5 | 脚注1 (p.4):"due to the high cost of the simulation... the average API fee for running single once is $50, while the cost is $90 for group customers" | 仅以成本说明运行次数,无事前功效分析 |
| G5 | 研究者自由度 | 0.5 | 脚注2 (p.4):"all analyses are based on data from all experiments"; §2.2:"if one of the restaurants decides to quit the race, the simulation will end" | 说明使用全部运行数据与终止规则;各分析多为案例选取,未列全部因变量,验证性/探索性未区分,"赢者通吃"阈值是否事后设定未说明 |
| G6 | 预先设定 / 预注册 | 0 | 全文未提及预注册 | 读到了没有预注册 |
| J1 | 位置偏差 | 0 | Fig.8 (p.14) 固定顺序 Restaurant 1 -> Restaurant 2 | 同 E1:作为选择的 LLM 顾客面对两家餐厅,未交换位置或随机化 |
| J2 | 冗长偏差 | 0 | §2.4 (p.3-4):顾客依据餐厅"customer score, advertisement, menu, and comments"选择 | 顾客 LLM 实质为裁判,所见广告与评论文本长度/详尽度可能影响选择,文中未识别或控制 |
| J3 | 谄媚 | NA | — | 无用户立场/纠错对话;(顾客提示"don't just praise"属评论指令,不构成谄媚评估) |
| J4 | 自我偏好 | 0.5 | §2.2 (p.3):"both restaurants and customers are powered by LLM-based agents, which are GPT-4 (0613)" | 报告了裁判(顾客)与被评(餐厅)同为 GPT-4-0613;未识别或控制自我偏好风险 |
| J5 | 少样本示例选择与排列偏差 | NA | — | 未使用 few-shot 示例 |
| J6 | 提示敏感性 / 脆弱性 | 0.5 | Fig.7/Fig.8 (p.13-14) 提示片段;摘要给出代码链接 | 展示了部分提示模板(含省略)与开源代码;无提示变体敏感性分析、无版本化与 dev/test 分离 |
| J7 | 长上下文信息位置效应 / 中间迷失 | NA | — | 非长上下文/RAG 实验(尽管输入含日账、最近十条评论) |
| J8 | 温度与采样随机性 | 0.5 | §3 (p.4):"We run experiments 9 and 6 times"; §2.2 GPT-4 (0613) | 报告了重复运行次数;未报告 temperature/top-p/种子,无置信区间 |
| J9 | 重复与文本退化 | 0 | §2–§3 (p.3–6) 多智能体开放生成菜单、广告、评论与决策理由，全文未报告解码参数 | 实验涉及多轮开放式文本生成，但全文未报告解码策略（temperature、top-p、repetition penalty）及重复/退化率控制，基本要件未达成，记 0。 |
| J10 | 分词效应 | NA | — | 非跨语言/跨格式实验 |
| J11 | 测试集污染 / 数据泄漏 | 0.5 | §4 (p.7):"we doubt that the model could have already memorized these popular theories and examples" | 识别了训练记忆(理论/例子)可能导致"与理论吻合";给出版本 GPT-4-0613,但无训练截止期对照或污染检测 |
| J12 | 基准饱和 | NA | — | 非基准评测 |
| J13 | 指令遵循 | NA | — | 研究不以指令遵循为构念 |
| J14 | 输出格式约束 / 结构化输出 | 0.5 | Fig.7 (p.13):"your response must follow the following format: < Designed JSON format>"; Fig.8 JSON 输出格式 | 动作与评分均要求 JSON 格式;未报告格式合法率或格式失败处理,格式失败与内容错误未区分 |
| J15 | 越狱稳健性 | NA | — | 非安全评测 |
| J16 | LLM 作为被试的范式定位 | 0.5 | §4 (p.7):"But why agents possess these behaviors are unexplored due to the black-box nature..."; 结论 (p.9):"LLM-based agents can be used to simulate a competitive environment" | 将智能体行为类比人类市场行为并以理论吻合作为依据,同时承认可能源于训练数据记忆;但未明确界定 LLM 所测构念与人类"竞争/马太效应"的异同,也未做人类对照 |
| J17 | 涌现能力争议与指标诱导假象 | NA | — | 无规模曲线或涌现宣称 |
| J18 | 指标博弈与奖励过优化 | NA | — | 无代理指标优化目标 |
| J19 | 评估可复现性与种子 / 检查点依赖 | 0.5 | §6 (p.8):"Our results are based on GPT-4-0613. We acknowledge that future API updates may affect the results"; §3 重复次数 | 给出精确 snapshot 与重复次数、开源代码;无 CI、种子或配对检验 |
| J20 | 多轮对话中的一致性衰减 | 0.5 | Fig.4/5 (p.6-7) 按天(Day 1-15)客流与菜品均分曲线 | 做了多日多轮追踪并分日报告;但对象不是一致性/指令遵循衰减,未控制或分析上下文截断(仅用摘要记忆与最近 10 条评论)对行为的影响 |

## 编码小结
本篇为 LLM 多智能体社会模拟,仅有"顾客类型(个体/团体)"一个明确操纵;被试内、因子、平衡、人类反应偏差类组件大多 NA。核心弱点在统计与因果推断:无任何推断统计(F1 记 0)、小样本 9/6 次、无无竞争对照,同时 R1/R2 固定呈现顺序(E1/J1 记 0)与初始优势发现可能混杂。判断分歧点:A1/B1 因条件配置明确但分配与独立性未述,记 0.5;J2 将顾客视作"LLM 裁判"属解读性判断(若视为环境机制则应 NA);G3 将手工设计的顾客集视为未作随机抽样记 0;J20 因对象并非一致性衰减而仅给 0.5。。

**统一口径复核修订注记**：按《实验组件_v1.4》级联判定规则与跨组件一致性要求，本次复核修订了 E5（NR→0）, J9（NR→0）。
