# 109篇评测候选文献与组件需求对应

这份材料帮助回答：**一篇论文有哪些具体方法需求，这些需求涉及哪些现有组件？** 已完成109篇中已纳入研究单元及直接支撑方法的对应，供后续评测任务设计查阅。

共295条原文事实、279条具体需求、705条需求—组件关系，涉及69项现有组件中的39项；按文章×组件去重为662对。时间依据支持104篇，另5篇待补。当前尚未形成最终测试集，也没有新增组件或评测task、答案、评分规则。

## 先看结果

- [下载可筛选工作簿](tables/109篇文献组件需求配对.xlsx)：文章目录、需求对应、组件反查三个视图；请随完整仓库目录使用其中的相对文件链接。
- 网页查阅：[文章表](tables/articles.csv) · [需求对应表](tables/demand_component_matches.csv) · [组件表](tables/components.csv)。CSV链接列保留相对路径，点击查阅可使用下方逐篇目录。
- [按组件反查文献](组件反查.md)：从某项组件找相关论文和具体用法。

**对应关系表示方法功能相关，不表示手册已经足以完整复现论文，也不是论文设计质量评分。** 空白或0篇表示本轮范围未建立对应，不能扩大成全文完全不涉及。

## 中间这一层是什么？

论文实际做法 → 具体方法需求 → 现有组件。

以[NL-003729](papers/NL-003729.md)为例，作者把同一误导文档分别放在助手和用户消息中：

| 实际做法 | 方法需求 | 对应组件 |
|---|---|---|
| 比较两种消息角色 | 明确操纵因素和两个条件 | A1 自变量、A8 水平数与类型 |
| 使用相同系统提示和末尾询问 | 固定其他提示条件 | A3 控制变量、C3 恒定 |
| 在模型原本答对的题中统计被指定错误答案诱导的比例 | 定义结果指标及统计分母 | A2 因变量、A7 操作性定义、G1 分析单位 |

这一篇的3条方法需求形成7条组件关系。因此表格的705行不能当成705种需求。具体条件、分母和解释限制保留在逐篇页面与原文摘录中。

## 与旧243篇成果怎样衔接

[旧243篇成果](../literature_component_coverage/README.md)用于理解组件支持与知识缺口。本包用于理解新增评测候选文献与组件的关系，两者处理粒度和评价口径不同。当前成果沿用同一版[组件手册](../literature_component_coverage/baselines/实验组件_v1.4.md)，没有为新文献改写组件。

[整理方法与统计口径](METHODS.md)说明作用分类、日期精度、研究范围及复核边界。[109篇正文目录](../../literature/test_candidates/README.md)提供实际所读主版本PDF与公开来源；研究家族及既往使用信息保留在[文献索引](data/articles.json)。

<a id="articles"></a>

## 逐篇阅读

领域采用一层四类，可跨类：C认知、语言与情绪；D判断、决策与博弈；S社会、人格与文化；M测量与评估。

| 编号与依据 | 文章 | 领域 | 当前时间状态 |
|---|---|---|---|
| [NL-001342](papers/NL-001342.md) | ARCHE: A Novel Task to Evaluate LLMs on Latent Reasoning Chain Extraction | C | 窗内依据已核 |
| [NL-001343](papers/NL-001343.md) | Mind the Gap: The Divergence Between Human and LLM-Generated Tasks | C、S | 窗内依据已核 |
| [NL-001347](papers/NL-001347.md) | Detecting Emotional Dynamic Trajectories: An Evaluation Framework for Emotional Support in Language Models | C | 窗内依据已核 |
| [NL-003464](papers/NL-003464.md) | Amplifying Trans and Nonbinary Voices: A Community-Centred Harm Taxonomy for LLMs | S | 窗内依据已核 |
| [NL-003567](papers/NL-003567.md) | “What do you call a dog that is incontrovertibly true? Dogma”: Testing LLM Generalization through Humor | C | 窗内依据已核 |
| [NL-003582](papers/NL-003582.md) | Tracing and Dissecting How LLMs Recall Factual Knowledge for Real World Questions | C | 窗内依据已核 |
| [NL-003591](papers/NL-003591.md) | Beyond the Answer: Advancing Multi-Hop QA with Fine-Grained Graph Reasoning and Evaluation | C | 窗内依据已核 |
| [NL-003704](papers/NL-003704.md) | Do LLMs Understand Dialogues? A Case Study on Dialogue Acts | C | 窗内依据已核 |
| [NL-003729](papers/NL-003729.md) | Exploring the Impact of Instruction-Tuning on LLM’s Susceptibility to Misinformation | S | 窗内依据已核 |
| [NL-003757](papers/NL-003757.md) | Internal Value Alignment in Large Language Models through Controlled Value Vector Activation | S | 窗内依据已核 |
| [NL-003806](papers/NL-003806.md) | PIPER: Benchmarking and Prompting Event Reasoning Boundary of LLMs via Debiasing-Distillation Enhanced Tuning | C | 窗内依据已核 |
| [NL-003814](papers/NL-003814.md) | LLMs Trust Humans More, That’s a Problem! Unveiling and Mitigating the Authority Bias in Retrieval-Augmented Generation | S | 窗内依据已核 |
| [NL-004803](papers/NL-004803.md) | Efficient Prior-Guided Reasoning for Robust Retrieval-Augmented Generation under Conflicts | C | 窗内依据已核 |
| [NL-004814](papers/NL-004814.md) | LitVISTA: A Benchmark for Narrative Orchestration in Literary Text | C | 窗内依据已核 |
| [NL-004819](papers/NL-004819.md) | Debiasing Reward Models via Causally Motivated Inference-Time Intervention | M | 窗内依据已核 |
| [NL-004821](papers/NL-004821.md) | Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math | C | 窗内依据已核 |
| [NL-004823](papers/NL-004823.md) | Red Teaming Large Reasoning Models | C | 时间待补 |
| [NL-004824](papers/NL-004824.md) | InsLogicBench: An Argumentation Logic Grounded Benchmark for Complex Insurance Claims Adjudication | C | 窗内依据已核 |
| [NL-004829](papers/NL-004829.md) | Think in Sentences: Explicit Sentence Boundaries Enhance Language Model’s Capabilities | C | 窗内依据已核 |
| [NL-004831](papers/NL-004831.md) | Phun-Bench: Evaluating LLMs on Phonological Understanding in Chinese | C | 窗内依据已核 |
| [NL-004839](papers/NL-004839.md) | MORPHOGEN: A Multilingual Benchmark for Evaluating Gender-Aware Morphological Generation | C | 窗内依据已核 |
| [NL-004840](papers/NL-004840.md) | Large Language Models Are Bad Dice Players: LLMs Struggle to Generate Random Numbers from Statistical Distributions | C | 窗内依据已核 |
| [NL-004849](papers/NL-004849.md) | Automated Creativity Evaluation of Language Models Across Open-Ended Tasks | C、M | 窗内依据已核 |
| [NL-004852](papers/NL-004852.md) | How Training Data Shapes the Use of Parametric and In-Context Knowledge in Language Models | C | 窗内依据已核 |
| [NL-004863](papers/NL-004863.md) | Are they lovers or friends? Evaluating LLMs’ Social Reasoning in English and Korean Dialogues | S | 窗内依据已核 |
| [NL-004880](papers/NL-004880.md) | InsideOut: Measuring and Mitigating Insider–Outsider Bias in Interview Script Generation | S | 窗内依据已核 |
| [NL-004884](papers/NL-004884.md) | ADVICE: Answer-Dependent Verbalized Confidence Estimation | C | 窗内依据已核 |
| [NL-004892](papers/NL-004892.md) | Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment | S | 窗内依据已核 |
| [NL-004899](papers/NL-004899.md) | Truth or Sophistry? LoFa: A Benchmark for LLM Robustness Against Logical Fallacies | C | 窗内依据已核 |
| [NL-004913](papers/NL-004913.md) | Good Arguments Against the People Pleasers: How Reasoning Mitigates (Yet Masks) LLM Sycophancy | S | 窗内依据已核 |
| [NL-004914](papers/NL-004914.md) | Can Persona-Prompted LLMs Emulate Subgroup Values? An Empirical Analysis of Generalisability and Fairness in Cultural Alignment | S | 窗内依据已核 |
| [NL-004923](papers/NL-004923.md) | Into the Gray Zone: Domain Contexts Can Blur LLM Safety Boundaries | D | 窗内依据已核 |
| [NL-004933](papers/NL-004933.md) | Know Your Place: Diagnosing Implicit Social Adaptation Failures in Chinese Large Language Models | S | 窗内依据已核 |
| [NL-004936](papers/NL-004936.md) | Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents | C | 时间待补 |
| [NL-004971](papers/NL-004971.md) | Stable-RAG: Mitigating Retrieval-Permutation-Induced Hallucinations in Retrieval-Augmented Generation | C | 窗内依据已核 |
| [NL-004974](papers/NL-004974.md) | CogEvolve: A Multimodal Benchmark for Evaluating Relational Reasoning in Semantic Extension | C | 窗内依据已核 |
| [NL-004981](papers/NL-004981.md) | Attention Basin: Why Contextual Position Matters in Large Language Models | C | 窗内依据已核 |
| [NL-005001](papers/NL-005001.md) | Inflated Excellence or True Performance? Rethinking Medical Diagnostic Benchmarks with Dynamic Evaluation | C | 窗内依据已核 |
| [NL-005004](papers/NL-005004.md) | ConfSpec: Efficient Step-Level Speculative Reasoning via Confidence-Gated Verification | C | 窗内依据已核 |
| [NL-005017](papers/NL-005017.md) | False Friends in the Shell: Unveiling the Emoticon Semantic Confusion in Large Language Models | C | 窗内依据已核 |
| [NL-005021](papers/NL-005021.md) | LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals | C | 窗内依据已核 |
| [NL-005024](papers/NL-005024.md) | AwarenessBench: Assessing Cognitive Capabilities of Language Models | C | 窗内依据已核 |
| [NL-005026](papers/NL-005026.md) | Can LLMs Estimate Cognitive Complexity of Reading Comprehension Items? | C | 窗内依据已核 |
| [NL-005031](papers/NL-005031.md) | LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations | S | 窗内依据已核 |
| [NL-005045](papers/NL-005045.md) | When Personalization Legitimizes Risks: Uncovering Safety Vulnerabilities in Personalized Dialogue Agents | S | 窗内依据已核 |
| [NL-005051](papers/NL-005051.md) | Neo-Classic: A Benchmark for Evaluating Linguistic-Aesthetic Reasoning in Classical Chinese Poetry | C | 窗内依据已核 |
| [NL-005071](papers/NL-005071.md) | Probing Semantic Alignment, Lexical Invariance, and Syntactic Influence in LLM Metaphor Processing | C | 窗内依据已核 |
| [NL-005079](papers/NL-005079.md) | REST: Stress Testing Large Reasoning Models by Asking Multiple Problems at Once | C | 窗内依据已核 |
| [NL-005083](papers/NL-005083.md) | ALIGN: Word Association Learning for Cultural Alignment in Large Language Models | S | 窗内依据已核 |
| [NL-005085](papers/NL-005085.md) | ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models | C | 窗内依据已核 |
| [NL-005097](papers/NL-005097.md) | Bloom-Eval: A Hierarchical Evaluation Benchmark for Automatic Survey Generation Based on Bloom’s Taxonomy | M | 窗内依据已核 |
| [NL-005098](papers/NL-005098.md) | Fair-CCD: Mitigating Bias in Large Language Models for Tabular Classification Through Context-Contrastive Decoding | S | 窗内依据已核 |
| [NL-005106](papers/NL-005106.md) | EIFFEL: a novel benchmark to measure bias of English heavy training on French idiomatic expressions | C | 窗内依据已核 |
| [NL-005120](papers/NL-005120.md) | Why Are We Moral? An LLM-based Agent Simulation Approach to the Study of Moral Evolution | S、D | 窗内依据已核 |
| [NL-005124](papers/NL-005124.md) | Location Not Found: Exposing Implicit Local and Global Biases in Multilingual LLMs | S | 窗内依据已核 |
| [NL-005125](papers/NL-005125.md) | LLMs in Sarcasm Detection? It’s elementary! (Or is it?) | C | 窗内依据已核 |
| [NL-005126](papers/NL-005126.md) | Beyond Itinerary Planning—A Real-World Benchmark for Multi-Turn and Tool-Using Travel Tasks | C | 窗内依据已核 |
| [NL-005130](papers/NL-005130.md) | Persona-E²: A Human-Grounded Dataset for Personality-Shaped Emotional Responses to Textual Events | C、S | 窗内依据已核 |
| [NL-005134](papers/NL-005134.md) | SILO-BENCH: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems | C、D | 窗内依据已核 |
| [NL-005137](papers/NL-005137.md) | Whose Facts Win? LLM Source Preferences under Knowledge Conflicts | S | 窗内依据已核 |
| [NL-005145](papers/NL-005145.md) | LLMs (Almost) Never Abstain Under Medical Uncertainty | D、C | 窗内依据已核 |
| [NL-005147](papers/NL-005147.md) | Culture-Aware Machine Translation in Large Language Models: Benchmarking and Investigation | C | 窗内依据已核 |
| [NL-006709](papers/NL-006709.md) | From myth to model: Representation of “the Jew” in generative AI. | S | 窗内依据已核 |
| [NL-006926](papers/NL-006926.md) | How well do large language models mirror human cognition of word concepts?: A comparison of psychological ratings for early-acquired English words | C | 窗内依据已核 |
| [NL-008491](papers/NL-008491.md) | CoEmpaTeam: Enhancing Cognitive Empathy using LLM-based Avatars and Dynamic Role Play in Virtual Reality | S | 窗内依据已核 |
| [NL-008591](papers/NL-008591.md) | From Expectation to Evaluation: Expectation Cues Systematically Bias LLM and Human Judgment | D、S | 窗内依据已核 |
| [NL-008616](papers/NL-008616.md) | TALES: A Taxonomy and Analysis of Cultural Representations in LLM-generated Stories | S | 窗内依据已核 |
| [NL-008630](papers/NL-008630.md) | Identifying, Explaining, and Correcting Ableist Language with AI | S | 窗内依据已核 |
| [NL-010489](papers/NL-010489.md) | Reading between the lines: LLMs match or exceed human empathic accuracy using text alone | S | 窗内依据已核 |
| [NL-012915](papers/NL-012915.md) | VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks | C | 窗内依据已核 |
| [NL-012934](papers/NL-012934.md) | Death of the Novel(ty): Beyond n-Gram Novelty as a Metric for Textual Creativity | C、M | 窗内依据已核 |
| [NL-012949](papers/NL-012949.md) | DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs | C、M | 窗内依据已核 |
| [NL-012950](papers/NL-012950.md) | Flipping the Dialogue: Training and Evaluating User Language Models | C、S | 窗内依据已核 |
| [NL-012954](papers/NL-012954.md) | All Code, No Thought: Current Language Models Struggle to Reason in Ciphered Language | C | 窗内依据已核 |
| [NL-012973](papers/NL-012973.md) | When Agents “Misremember” Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems | S | 窗内依据已核 |
| [NL-013008](papers/NL-013008.md) | OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety | M | 窗内依据已核 |
| [NL-013031](papers/NL-013031.md) | A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments | D | 窗内依据已核 |
| [NL-013039](papers/NL-013039.md) | Demystifying Deep Search: A Holistic Evaluation with Hint-free Multi-Hop Questions and Factorised Metrics | C | 窗内依据已核 |
| [NL-013040](papers/NL-013040.md) | PersonaX: Multimodal Datasets with LLM-Inferred Behavior Traits | M | 窗内依据已核 |
| [NL-013044](papers/NL-013044.md) | Attend to the Active: Structure-Aware Dynamic Attention in LLMs for Compositional Instruction Following | C | 窗内依据已核 |
| [NL-017408](papers/NL-017408.md) | CauSciBench: Can LLMs Automate Causal Inference in Real-World Scientific Research? | C | 时间待补 |
| [NL-017426](papers/NL-017426.md) | Beyond Majority Voting: LLM Aggregation by Leveraging Higher-Order Information | C | 窗内依据已核 |
| [NL-017442](papers/NL-017442.md) | Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth | C | 窗内依据已核 |
| [NL-017450](papers/NL-017450.md) | ORLoopBench: Solver-in-the-Loop Benchmarks for Self-Correction and Behavioral Rationality in Operations Research | D | 窗内依据已核 |
| [NL-017453](papers/NL-017453.md) | Biases in the Blind Spot: Detecting What LLMs Fail to Mention | S、C | 窗内依据已核 |
| [NL-017456](papers/NL-017456.md) | A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents | C | 窗内依据已核 |
| [NL-017458](papers/NL-017458.md) | How does information access affect LLM monitors’ ability to detect sabotage? | M | 窗内依据已核 |
| [NL-017461](papers/NL-017461.md) | Language Model Circuits Are Sparse in the Neuron Basis | C | 窗内依据已核 |
| [NL-017485](papers/NL-017485.md) | Sycophancy Towards Researchers Drives Performative Misalignment | C | 窗内依据已核 |
| [NL-017512](papers/NL-017512.md) | DRIFT-BENCH: Diagnosing CoopeRative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction | S | 窗内依据已核 |
| [NL-017520](papers/NL-017520.md) | INDUCTION: Finite-Structure Concept Synthesis in First-Order Logic | C | 窗内依据已核 |
| [NL-017531](papers/NL-017531.md) | Reasoning Structure of Large Language Models | C | 时间待补 |
| [NL-017534](papers/NL-017534.md) | Skill Neologisms: Towards Skill-based Continual Learning | C | 窗内依据已核 |
| [NL-017549](papers/NL-017549.md) | Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering | C | 窗内依据已核 |
| [NL-017564](papers/NL-017564.md) | Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought | C | 窗内依据已核 |
| [NL-024752](papers/NL-024752.md) | Competing Biases underlie Overconfidence and Underconfidence in LLMs | C、D | 窗内依据已核 |
| [NL-025056](papers/NL-025056.md) | Deep Value Benchmark: Measuring Whether Models Generalize Deep values or Shallow Preferences | S、D | 窗内依据已核 |
| [NL-027371](papers/NL-027371.md) | Improving Audit Realism with Inference-Time Compute and Deployment Scaffolds | C | 窗内依据已核 |
| [NL-027389](papers/NL-027389.md) | Inter-Agent Influence: Evaluating Persuasion, Deception and Coercion in Multi-Agent Systems | D、S | 窗内依据已核 |
| [NL-027410](papers/NL-027410.md) | Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking | M | 窗内依据已核 |
| [NL-027469](papers/NL-027469.md) | Long-Lived AI Agents Age Too: They Quietly Decay After Deployment | C | 窗内依据已核 |
| [NL-027484](papers/NL-027484.md) | LLMs Show No Signs Of Individuated Metacognition | C | 窗内依据已核 |
| [NL-027499](papers/NL-027499.md) | A Unifying Perspective on Language Model Interpretability | C | 窗内依据已核 |
| [NL-027500](papers/NL-027500.md) | Cross-User Poisoning: User-Task Boundary Failures in Multi-User Collaborative Language Agents | S | 窗内依据已核 |
| [NL-027522](papers/NL-027522.md) | Evaluation Awareness in Language Models Has Limited Effect on Behaviour | C | 窗内依据已核 |
| [NL-027537](papers/NL-027537.md) | Model Incrimination: Investigating Whether Concerning Behavior Reﬂects Misalignment | D | 窗内依据已核 |
| [NL-031129](papers/NL-031129.md) | What Does the AI Doctor Value? Auditing Pluralism in the Clinical Ethics of Language Models | S | 窗内依据已核 |
| [NL-031155](papers/NL-031155.md) | The Future of Facts: Tracing the Factual Generation-Verification Gap | C | 窗内依据已核 |
| [NL-031841](papers/NL-031841.md) | Statutory construction and interpretation for AI | S | 时间待补 |
