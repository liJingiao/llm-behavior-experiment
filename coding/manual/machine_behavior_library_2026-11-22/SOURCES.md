# 方法来源与阅读范围

核查日期：2026-11-05。正文实例主要来自已有A事实与逐项证据；下面的原始方法、作者实现和官方文档用于核对通用定义、公式与接口。按相关部分定向阅读，不声称通读所有网页，也未执行下载的来源代码。网页/代码链接可能随上游更新；引用日期与实际读取地址保存在[source_register.json](source_register.json)。

## 现有项目材料

- 已逐项阅读69项手册、构念任务附录、编码表、381项缺口与10个主题建议；原文件保持原样。
- [逐项对应](TRACEABILITY.md)提供所有951条需求实例的A/B版本与事实、证据ID。应用事实不替代通用方法依据；通用方法也不倒填原论文未知配置。
- 本轮对article_137第25页及CCP原论文第6页渲染核对公式；article_233按已有原文证据核对谱系数、模式构造和适用条件；article_178补查层级精度。
- article_055仓库仅静态查看，未解密数据；新增查看与原A的历史检查范围分开。

## 通用方法与实现依据

同一来源可以支持多个相关小节；“支持”限定在所列定义/算法/接口，不表示该来源为全节所有实例事实背书。

|编号|来源|用途/正文位置|本轮核查范围|
|---|---|---|---|
|S001|[SciPy Pearson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html)|[02 Pearson相关、点二列相关与相关的边界](K01_statistics.md#k01-02)；[04 Fisher变换、相关差异和Cohen q](K01_statistics.md#k01-04)|定向核对相关定义、公式或接口；未运行来源代码|
|S002|[Spearman](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html)|[03 Spearman与Kendall：比较顺序关系](K01_statistics.md#k01-03)|定向核对相关定义、公式或接口；未运行来源代码|
|S003|[Kendall](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kendalltau.html)|[03 Spearman与Kendall：比较顺序关系](K01_statistics.md#k01-03)|定向核对相关定义、公式或接口；未运行来源代码|
|S004|[独立t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)|[05 比较均值：配对t、Student、Welch与z](K01_statistics.md#k01-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S005|[配对t](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)|[05 比较均值：配对t、Student、Welch与z](K01_statistics.md#k01-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S006|[U](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html)|[06 秩检验：独立样本、配对样本与重复区组](K01_statistics.md#k01-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S007|[符号秩](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html)|[06 秩检验：独立样本、配对样本与重复区组](K01_statistics.md#k01-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S008|[Kruskal](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html)|[06 秩检验：独立样本、配对样本与重复区组](K01_statistics.md#k01-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S009|[Friedman](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.friedmanchisquare.html)|[06 秩检验：独立样本、配对样本与重复区组](K01_statistics.md#k01-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S010|[Tukey方法与假设](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.tukey_hsd.html)|[07 ANOVA、因子效应与Tukey比较](K01_statistics.md#k01-07)|定向核对相关定义、公式或接口；未运行来源代码|
|S011|[χ²](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)|[08 类别比较：χ²、Fisher与McNemar](K01_statistics.md#k01-08)|定向核对相关定义、公式或接口；未运行来源代码|
|S012|[Fisher](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fisher_exact.html)|[08 类别比较：χ²、Fisher与McNemar](K01_statistics.md#k01-08)|定向核对相关定义、公式或接口；未运行来源代码|
|S013|[二项检验](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html)|[09 二项尾概率与精确多项检验](K01_statistics.md#k01-09)|定向核对相关定义、公式或接口；未运行来源代码|
|S014|[比例区间类型与边界](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_confint.html)|[11 二项比例区间与标准化均差区间](K01_statistics.md#k01-11)|定向核对相关定义、公式或接口；未运行来源代码|
|S015|[SciPy bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)|[12 Bootstrap：从观测重抽到最终统计量](K01_statistics.md#k01-12)|定向核对相关定义、公式或接口；未运行来源代码|
|S016|[置换方法与尾部约定](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html)|[13 置换、随机机会模拟与PERMANOVA](K01_statistics.md#k01-13)|定向核对相关定义、公式或接口；未运行来源代码|
|S017|[statsmodels多重检验](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html)|[14 多重比较：先定义比较族，再选择错误控制目标](K01_statistics.md#k01-14)|定向核对相关定义、公式或接口；未运行来源代码|
|S018|[Cochrane第10章§10.6](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10)|[15 效应量、方向与跨结果合并](K01_statistics.md#k01-15)|定向核对相关定义、公式或接口；未运行来源代码|
|S019|[statsmodels元分析示例](https://www.statsmodels.org/stable/examples/notebooks/generated/metaanalysis1.html)|[15 效应量、方向与跨结果合并](K01_statistics.md#k01-15)|定向核对相关定义、公式或接口；未运行来源代码|
|S020|[线性模型官方说明](https://scikit-learn.org/stable/modules/linear_model.html)|[16 线性拟合、权重和对比编码](K01_statistics.md#k01-16)；[17 Logistic、probit与正则化回归](K01_statistics.md#k01-17)|定向核对相关定义、公式或接口；未运行来源代码|
|S021|[Stan二元链接](https://mc-stan.org/docs/stan-users-guide/regression.html)|[17 Logistic、probit与正则化回归](K01_statistics.md#k01-17)；[20 贝叶斯回归、层级模型与后验比较](K01_statistics.md#k01-20)|定向核对相关定义、公式或接口；未运行来源代码|
|S022|[混合模型公式与估计](https://www.statsmodels.org/stable/mixed_linear.html)|[18 混合模型、随机结构与混合模型R²](K01_statistics.md#k01-18)|定向核对相关定义、公式或接口；未运行来源代码|
|S023|[GLM](https://www.statsmodels.org/stable/glm.html)|[19 系数检验、模型比较和估计边际均值](K01_statistics.md#k01-19)|定向核对相关定义、公式或接口；未运行来源代码|
|S024|[诊断说明](https://mc-stan.org/learn-stan/diagnostics-warnings.html)|[20 贝叶斯回归、层级模型与后验比较](K01_statistics.md#k01-20)|定向核对相关定义、公式或接口；未运行来源代码|
|S025|[分组交叉验证](https://scikit-learn.org/stable/modules/cross_validation.html)|[22 调参、外部评价、OOB与特征归因](K01_statistics.md#k01-22)|定向核对相关定义、公式或接口；未运行来源代码|
|S026|[Shapiro](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html)|[25 分布诊断、方差检验与游程](K01_statistics.md#k01-25)|定向核对相关定义、公式或接口；未运行来源代码|
|S027|[KS](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html)|[25 分布诊断、方差检验与游程](K01_statistics.md#k01-25)|定向核对相关定义、公式或接口；未运行来源代码|
|S028|[Levene](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html)|[25 分布诊断、方差检验与游程](K01_statistics.md#k01-25)|定向核对相关定义、公式或接口；未运行来源代码|
|S029|[因子提取与旋转接口](https://factor-analyzer.readthedocs.io/en/latest/factor_analyzer.html)|[28 Bartlett球形性、MINRES与Varimax](K01_statistics.md#k01-28)|定向核对相关定义、公式或接口；未运行来源代码|
|S030|[Cohen实现与权重说明](https://www.statsmodels.org/stable/generated/statsmodels.stats.inter_rater.cohens_kappa.html)|[02 两名评分者：Cohen κ、加权κ与两两聚合](K02_annotation_reliability.md#k02-02)|定向核对相关定义、公式或接口；未运行来源代码|
|S031|[Fleiss与不同机会模型](https://www.statsmodels.org/stable/generated/statsmodels.stats.inter_rater.fleiss_kappa.html)|[03 多名类别评分者：Fleiss κ及未明变体](K02_annotation_reliability.md#k02-03)|定向核对相关定义、公式或接口；未运行来源代码|
|S032|[实现与缺失矩阵约定](https://github.com/pln-fing-udelar/fast-krippendorff)|[04 Krippendorff α：不一致、距离与缺失](K02_annotation_reliability.md#k02-04)|定向核对相关定义、公式或接口；未运行来源代码|
|S033|[Pingouin信度实现及ANOVA公式](https://github.com/raphaelvallat/pingouin/blob/master/src/pingouin/reliability.py)；[实际读取](https://raw.githubusercontent.com/raphaelvallat/pingouin/master/src/pingouin/reliability.py)|[05 连续评分的ICC：一致还是数值相同](K02_annotation_reliability.md#k02-05)；[06 内部一致性、分半和长度校正](K02_annotation_reliability.md#k02-06)|静态读取对应官方源文件；checked_url列给出本轮实际读取地址|
|S034|[Sentence Transformers相似度与接口区分](https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)|[01 冻结表征、余弦与语义比较协议](K03_text_semantics.md#k03-01)|定向核对相关定义、公式或接口；未运行来源代码|
|S035|[BLEU操作与语料聚合](https://www.nltk.org/api/nltk.translate.bleu_score.html)|[05 BLEU、ROUGE-L、ChrF++和METEOR](K03_text_semantics.md#k03-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S036|[ROUGE实现及两种LCS](https://github.com/google-research/google-research/tree/master/rouge)|[05 BLEU、ROUGE-L、ChrF++和METEOR](K03_text_semantics.md#k03-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S037|[SacreBLEU配置](https://github.com/mjpost/sacrebleu)|[05 BLEU、ROUGE-L、ChrF++和METEOR](K03_text_semantics.md#k03-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S038|[METEOR](https://www.nltk.org/api/nltk.translate.meteor_score.html)|[05 BLEU、ROUGE-L、ChrF++和METEOR](K03_text_semantics.md#k03-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S039|[作者实现](https://github.com/Tiiiger/bert_score)|[06 BERTScore与参考语义评分器](K03_text_semantics.md#k03-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S040|[SimCSE](https://github.com/princeton-nlp/SimCSE)|[06 BERTScore与参考语义评分器](K03_text_semantics.md#k03-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S041|[BLEURT](https://github.com/google-research/bleurt)|[06 BERTScore与参考语义评分器](K03_text_semantics.md#k03-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S042|[UniEval](https://github.com/maszhongming/UniEval)|[06 BERTScore与参考语义评分器](K03_text_semantics.md#k03-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S043|[BLANC作者实现](https://github.com/PrimerAI/blanc)|[07 无人工参考的摘要评价：BLANC与SUPERT](K03_text_semantics.md#k03-07)|定向核对相关定义、公式或接口；未运行来源代码|
|S044|[SUPERT作者实现](https://github.com/yg211/acl20-ref-free-eval)|[07 无人工参考的摘要评价：BLANC与SUPERT](K03_text_semantics.md#k03-07)|定向核对相关定义、公式或接口；未运行来源代码|
|S045|[评分源代码](https://raw.githubusercontent.com/yg211/acl20-ref-free-eval/master/ref_free_metrics/supert.py)|[07 无人工参考的摘要评价：BLANC与SUPERT](K03_text_semantics.md#k03-07)|定向核对相关定义、公式或接口；未运行来源代码|
|S046|[文本特征文档](https://scikit-learn.org/stable/modules/feature_extraction.html)|[09 TF-IDF、BM25与向量检索](K03_text_semantics.md#k03-09)|定向核对相关定义、公式或接口；未运行来源代码|
|S047|[Lucene BM25](https://lucene.apache.org/core/9_9_2/core/org/apache/lucene/search/similarities/BM25Similarity.html)|[09 TF-IDF、BM25与向量检索](K03_text_semantics.md#k03-09)|定向核对相关定义、公式或接口；未运行来源代码|
|S048|[NLTK VADER](https://www.nltk.org/api/nltk.sentiment.vader.html)|[12 词频log-odds与情绪词典](K03_text_semantics.md#k03-12)|定向核对相关定义、公式或接口；未运行来源代码|
|S049|[textstat作者文档](https://github.com/textstat/textstat)|[13 可读性量尺及年级共识](K03_text_semantics.md#k03-13)|定向核对相关定义、公式或接口；未运行来源代码|
|S050|[ERG文档入口](https://delph-in.github.io/docs/erg/ErgTop/)|[14 类型语法与同表面词的不同用法](K03_text_semantics.md#k03-14)|定向核对相关定义、公式或接口；未运行来源代码|
|S051|[生成输出与分数接口](https://huggingface.co/docs/transformers/main_classes/text_generation)|[01 候选token概率及预测位置](K04_probability.md#k04-01)|定向核对相关定义、公式或接口；未运行来源代码|
|S052|[官方困惑度定义与窗口处理](https://huggingface.co/docs/transformers/perplexity)|[03 自回归序列、surprisal和困惑度](K04_probability.md#k04-03)|定向核对相关定义、公式或接口；未运行来源代码|
|S053|[熵与相对熵](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html)|[06 熵、有效类别数、熵差与二次集中度](K04_probability.md#k04-06)；[08 KL、Jensen–Shannon、逐词贡献、交叉熵与PMI](K04_probability.md#k04-08)|定向核对相关定义、公式或接口；未运行来源代码|
|S054|[Jensen–Shannon distance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.jensenshannon.html)|[08 KL、Jensen–Shannon、逐词贡献、交叉熵与PMI](K04_probability.md#k04-08)|定向核对相关定义、公式或接口；未运行来源代码|
|S055|[一维Wasserstein](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html)|[09 Wasserstein：概率质量移动了多远](K04_probability.md#k04-09)|定向核对相关定义、公式或接口；未运行来源代码|
|S056|[原方法入口](https://proceedings.mlr.press/v139/zhao21c.html)|[10 概率偏好校准：无内容、背景中位数和PriDe](K04_probability.md#k04-10)|定向核对相关定义、公式或接口；未运行来源代码|
|S057|[PriDe原文§3.2—3.3](https://arxiv.org/html/2309.03882v2)|[10 概率偏好校准：无内容、背景中位数和PriDe](K04_probability.md#k04-10)|定向核对相关定义、公式或接口；未运行来源代码|
|S058|[原论文](https://aclanthology.org/2024.findings-acl.558/)|[12 CCP与语义熵：把不确定性接到主张](K04_probability.md#k04-12)|读取原始方法PDF第5—6页；第6页公式经渲染视觉核对，原名Claim-Conditioned Probability|
|S059|[校准目标与可靠性图](https://scikit-learn.org/stable/modules/calibration.html)|[01 条件校准、可靠性图与分箱损失](K05_evaluation.md#k05-01)|定向核对相关定义、公式或接口；未运行来源代码|
|S060|[指标的定义与平均方式](https://scikit-learn.org/stable/modules/model_evaluation.html)|[03 ROC、PR、AP与特定排名MAP](K05_evaluation.md#k05-03)|定向核对相关定义、公式或接口；未运行来源代码|
|S061|[成对比较的BTL、迭代谱排名与估计接口](https://choix.lum.li/en/latest/)|[05 Bradley–Terry拟合与谱排序](K05_evaluation.md#k05-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S062|[官方接口与停止条件](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-lbfgsb.html)|[06 有界优化、认知层级和计数似然](K06_cognitive_causal.md#k06-06)|定向核对相关定义、公式或接口；未运行来源代码|
|S063|[反事实计算说明](https://www.pywhy.org/dowhy/main/user_guide/causal_tasks/what_if/counterfactuals.html)|[08 SCM采样与溯因—干预—预测](K06_cognitive_causal.md#k06-08)|定向核对相关定义、公式或接口；未运行来源代码|
|S064|[ER生成接口](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.gnp_random_graph.html)|[10 ER随机图、独立边似然与ERGM](K06_cognitive_causal.md#k06-10)|定向核对相关定义、公式或接口；未运行来源代码|
|S065|[ODE接口及事件检测](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)|[14 一致性套利、矩阵ODE和收敛分析](K06_cognitive_causal.md#k06-14)|定向核对相关定义、公式或接口；未运行来源代码|
|S066|[PySAT RC2](https://pysathq.github.io/docs/html/api/examples/rc2.html)|[15 空间关系、关系闭包与加权MaxSAT](K06_cognitive_causal.md#k06-15)|定向核对相关定义、公式或接口；未运行来源代码|
|S067|[求根接口](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root_scalar.html)|[18 求根与外显逻辑有效性](K06_cognitive_causal.md#k06-18)|定向核对相关定义、公式或接口；未运行来源代码|
|S068|[图论接口与规则](https://networkx.org/documentation/stable/reference/algorithms/d_separation.html)|[25 同构、d-separation与MEC金标](K06_cognitive_causal.md#k06-25)|定向核对相关定义、公式或接口；未运行来源代码|
|S069|[积分梯度接口与完整性误差](https://captum.ai/docs/extension/integrated_gradients)|[02 输入梯度、条件方向与积分梯度](K08_internal_methods.md#k08-02)|定向核对相关定义、公式或接口；未运行来源代码|
|S070|[TracIn及影响接口](https://captum.ai/api/influence.html)|[03 跨checkpoint梯度影响](K08_internal_methods.md#k08-03)|定向核对相关定义、公式或接口；未运行来源代码|
|S071|[activation patching](https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.patching.html)|[09 临时张量干预及对照](K08_internal_methods.md#k08-09)|定向核对相关定义、公式或接口；未运行来源代码|
|S072|[Wanda作者实现中的逐列广播](https://raw.githubusercontent.com/locuslab/wanda/main/lib/prune.py)|[14 Wanda式权重—激活重要性](K08_internal_methods.md#k08-14)|定向核对相关定义、公式或接口；未运行来源代码|
|S073|[聚类方法](https://scikit-learn.org/stable/modules/clustering.html)|[02 K-means、k选择与K-medoids](K09_structure_geometry.md#k09-02)|定向核对相关定义、公式或接口；未运行来源代码|
|S074|[官方模块说明](https://maartengr.github.io/BERTopic/)|[04 LDA与嵌入主题发现](K09_structure_geometry.md#k09-04)|定向核对相关定义、公式或接口；未运行来源代码|
|S075|[混合整数优化](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html)|[05 整数选材与容量约束分配](K09_structure_geometry.md#k09-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S076|[最小费用流](https://developers.google.com/optimization/flow/mincostflow)|[05 整数选材与容量约束分配](K09_structure_geometry.md#k09-05)|定向核对相关定义、公式或接口；未运行来源代码|
|S077|[MDS官方说明](https://scikit-learn.org/stable/modules/manifold.html)|[08 MDS：从相似矩阵到坐标](K09_structure_geometry.md#k09-08)；[09 t-SNE与UMAP](K09_structure_geometry.md#k09-09)|定向核对相关定义、公式或接口；未运行来源代码|
|S078|[UMAP参数](https://umap-learn.readthedocs.io/en/latest/parameters.html)|[09 t-SNE与UMAP](K09_structure_geometry.md#k09-09)|定向核对相关定义、公式或接口；未运行来源代码|
|S079|[PCA、SVD与分解](https://scikit-learn.org/stable/modules/decomposition.html)|[10 PCA与SVD](K09_structure_geometry.md#k09-10)|定向核对相关定义、公式或接口；未运行来源代码|
|S080|[主角接口](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.subspace_angles.html)|[13 方差、子空间夹角与Procrustes](K09_structure_geometry.md#k09-13)|定向核对相关定义、公式或接口；未运行来源代码|
|S081|[正交Procrustes](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.orthogonal_procrustes.html)|[13 方差、子空间夹角与Procrustes](K09_structure_geometry.md#k09-13)|定向核对相关定义、公式或接口；未运行来源代码|
|S082|[模块度定义](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.quality.modularity.html)|[14 社区目标、Leiden与顺序边界优化](K09_structure_geometry.md#k09-14)|定向核对相关定义、公式或接口；未运行来源代码|
|S083|[conductance](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cuts.conductance.html)|[14 社区目标、Leiden与顺序边界优化](K09_structure_geometry.md#k09-14)|定向核对相关定义、公式或接口；未运行来源代码|
|S084|[Leiden](https://leidenalg.readthedocs.io/en/stable/intro.html)|[14 社区目标、Leiden与顺序边界优化](K09_structure_geometry.md#k09-14)|定向核对相关定义、公式或接口；未运行来源代码|
|S085|[Gaussian filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html)|[20 Gaussian平滑、峰检测与显示](K09_structure_geometry.md#k09-20)|定向核对相关定义、公式或接口；未运行来源代码|
|S086|[轮廓和多边形近似接口](https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html)；[实际读取](https://raw.githubusercontent.com/opencv/opencv/4.x/doc/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.markdown)|[23 图像区域到多边形边数](K09_structure_geometry.md#k09-23)|静态读取对应官方源文件；checked_url列给出本轮实际读取地址|
|S087|[作者仓库](https://github.com/TristanThrush/i-am-a-strange-dataset)|[01 公开密文、解密入口与可获取性](K10_release.md#k10-01)|定向核对相关定义、公式或接口；未运行来源代码|
|S088|[簇稳健协方差接口及小样本修正](https://www.statsmodels.org/stable/generated/statsmodels.stats.sandwich_covariance.cov_cluster.html)|[簇稳健协方差接口及小样本修正](K01_statistics.md#k01-10)|簇稳健协方差接口及小样本修正；静态定向阅读|
|S089|[McNemar精确/近似区分](https://www.statsmodels.org/stable/generated/statsmodels.stats.contingency_tables.mcnemar.html)|[McNemar精确/近似区分](K01_statistics.md#k01-08)|McNemar精确/近似区分；静态定向阅读|
|S090|[TOST等效边界与单侧检验](https://www.statsmodels.org/stable/generated/statsmodels.stats.weightstats.ttost_ind.html)|[TOST等效边界与单侧检验](K01_statistics.md#k01-26)|TOST等效边界与单侧检验；静态定向阅读|
|S091|[REML元分析方差参数与估计选项](https://wviechtb.github.io/metafor/reference/rma.uni.html)|[REML元分析方差参数与估计选项](K01_statistics.md#k01-15)|REML元分析方差参数与估计选项；静态定向阅读|
|S092|[混合模型R²的方差组成](https://easystats.github.io/performance/reference/r2_nakagawa.html)|[混合模型R²的方差组成](K01_statistics.md#k01-18)|混合模型R²的方差组成；静态定向阅读|
|S093|[参考格、边际均值和对比](https://rvlenth.github.io/emmeans/articles/basics.html)|[参考格、边际均值和对比](K01_statistics.md#k01-19)|参考格、边际均值和对比；静态定向阅读|
|S094|[独立/相关背景的线性SHAP](https://shap.readthedocs.io/en/latest/generated/shap.LinearExplainer.html)|[独立/相关背景的线性SHAP](K01_statistics.md#k01-22)|独立/相关背景的线性SHAP；静态定向阅读|
|S095|[袋外预测与不纯度特征重要性](https://scikit-learn.org/stable/modules/ensemble.html)|[袋外预测与不纯度特征重要性](K01_statistics.md#k01-22)|袋外预测与不纯度特征重要性；静态定向阅读|
|S096|[胜率方向与Rank Centrality转移率](https://raw.githubusercontent.com/lucasmaystre/choix/master/choix/lsr.py)|[胜率方向与Rank Centrality转移率](K05_evaluation.md#k05-05)|胜率方向与Rank Centrality转移率；静态定向阅读|
|S097|[节点移动、细化与聚合三阶段](https://leidenalg.readthedocs.io/en/stable/reference.html)|[节点移动、细化与聚合三阶段](K09_structure_geometry.md#k09-14)|节点移动、细化与聚合三阶段；静态定向阅读|
|S098|[edgewise/dyadwise共享邻居项与衰减参数](https://statnet.r-universe.dev/ergm/doc/manual.html)|[edgewise/dyadwise共享邻居项与衰减参数](K09_structure_geometry.md#k09-15)|edgewise/dyadwise共享邻居项与衰减参数；静态定向阅读|
|S099|[重合矩阵、期望重合与距离实现](https://raw.githubusercontent.com/pln-fing-udelar/fast-krippendorff/main/src/krippendorff/krippendorff.py)|[重合矩阵、期望重合与距离实现](K02_annotation_reliability.md#k02-04)|重合矩阵、期望重合与距离实现；静态定向阅读|

## 解释边界

公式的基础代数推导和教学算例由本轮写作给出，均不称论文结果。未报告的Gwet变体、某些评分配置和作者公式冲突仍按对应小节保留；本轮交付解决方法知识与使用边界，不声称已经重现这些论文的全部原始数值。

本包由同一助手编写与复核，不称独立评审。检查程序只验证结构、引用与算例，不能自动给科学验收或改变B状态。
