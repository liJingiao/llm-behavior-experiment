# 缺口处理结果与训练证据

每行对应一项具体知识需求。定稿方法正文为原手册及附录缺少的操作“补入具体做法”，为原库只支持部分步骤的操作“补全已有指导”。另列原附录已支持的规则和仅属真人参照的操作。点缺口编号可查该项的原问题和各篇论文的依据，点小节可查定稿说明。

[从原建议承接组件查方法小节](#by-component) · [按缺口查论文需求、事实与原文证据](#paper-evidence)

## K01 统计分析：从研究问题到可解释的结果

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_boot_distribution"></a>经验重抽样分布与区间构造 [KG_BOOT_DISTRIBUTION](#evidence-kg_boot_distribution) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 按独立单位有放回取样、每次重算统计量再读经验分布。013、186等的区间类型或误差条定义未报，保留未知。 |
| <a id="gap-kg_boot_paired"></a>配对重抽样比较 [KG_BOOT_PAIRED](#evidence-kg_boot_paired) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 同题两列共用抽中的索引，再计算配对差值。120/D025未给具体复样单位，235/D027未给尾概率规则。 |
| <a id="gap-kg_boot_dependence"></a>依赖结构与重抽样单位 [KG_BOOT_DEPENDENCE](#evidence-kg_boot_dependence) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 补明情境整簇抽、按对象重建距离及估计权重。064/D011按情境，237/D019另有逐距离项的做法，二者的有效性不能互借。 |
| <a id="gap-kg_boot_basic"></a>basic区间构造 [KG_BOOT_BASIC](#evidence-kg_boot_basic) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 用原估计的两倍减去经验分布反序的上、下分位点得到basic区间。055/D015确认basic类型，配对实现与种子未报告。 |
| <a id="gap-kg_boot_percentile"></a>百分位区间构造 [KG_BOOT_PERCENTILE](#evidence-kg_boot_percentile) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 给出有限B下经验逆分布直接取位和线性插值。237/D014的零起算24、974适用于该代码；D019及D025按各自重抽对象解释。 |
| <a id="gap-kg_boot_sd"></a>重抽样分布SD的解释与计算 [KG_BOOT_SD](#evidence-kg_boot_sd) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 重算统计量的SD估计其标准误；224/D023对100条摘要均值重抽，087/D012的SD误差条没有95%区间的含义。 |
| <a id="gap-kg_boot_pipeline"></a>派生统计量的重抽样计算链 [KG_BOOT_PIPELINE](#evidence-kg_boot_pipeline) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 按目标在每次抽中样本后重算基线、归一或拟合。024/D012计算PN/PS，173/D007的分母相关，229/D010的BT重拟合细节未确认。 |
| <a id="gap-kg_boot_test"></a>重抽样检验与P值构造 [KG_BOOT_TEST](#evidence-kg_boot_test) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 补入均值差零假设下的中心化重抽、比较统计量与双侧尾计数实例。121/D032、235/D027的复样次数均不足以识别其具体尾算法。 |
| <a id="gap-kg_boot_transform"></a>区间变换与重叠判据 [KG_BOOT_TRANSFORM](#evidence-kg_boot_transform) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 复用跨零区间取绝对值时包含零的规则；补明两个83%区间分离近似检验的独立、等SE、正态条件，237/D014的经验判据不作通则。 |
| <a id="gap-kg_boot_conditional"></a>固定变换下重抽样的条件范围 [KG_BOOT_CONDITIONAL](#evidence-kg_boot_conditional) | 补全已有指导 | [K01-12](K01_statistics.md#k01-12) | 补明固定投影与每次重估投影的目标区别。237/D025在既有PCA投影下重算几何量，所得区间只覆盖条件变异。 |
| <a id="gap-kg_unit_estimand"></a>个体层与合并层估计对象的区别 [KG_UNIT_ESTIMAND](#evidence-kg_unit_estimand) | 仅属真人参照 | [K01-01](K01_statistics.md#k01-01) | 003/D320的特殊操作是把真人参照的试次合并拟合，未产生每位参与者的参数和离散度。保留出处；正文另说明机器实验中按模型或试次汇总的含义。 |
| <a id="gap-kg_pearson"></a>Pearson积差相关计算及适用解释 [KG_PEARSON](#evidence-kg_pearson) | 补全已有指导 | [K01-02](K01_statistics.md#k01-02) | 保留标准化协方差、常数列及独立性限制；补充逐题、题内与聚合相关的对象差异。145/D015每10答聚合后的高r不能代表逐答一致。 |
| <a id="gap-kg_point_biserial"></a>二值—连续点二列相关 [KG_POINT_BISERIAL](#evidence-kg_point_biserial) | 补全已有指导 | [K01-02](K01_statistics.md#k01-02) | 用0/1编码后求Pearson，按编码1的比例和总体SD解释组均值差，翻转编码改变符号。127/D025的二元项是专家多数票。 |
| <a id="gap-kg_pearson_interpret"></a>相关验证与绝对评分一致的区别 [KG_PEARSON_INTERPRET](#evidence-kg_pearson_interpret) | 补全已有指导 | [K01-02](K01_statistics.md#k01-02) | 指标整体平移缩放也能给出r=1，需另查尺度和逐项误差。068/D218的人类评分用于对模型指标作参照。 |
| <a id="gap-kg_pearson_lag"></a>时滞相关的对齐与依赖边界 [KG_PEARSON_LAG](#evidence-kg_pearson_lag) | 补全已有指导 | [K01-02](K01_statistics.md#k01-02) | 按时滞裁掉无匹配端点，区分预定零时滞与搜索最大值；168/D022的时序自相关影响通常独立性检验。 |
| <a id="gap-kg_pearson_matrix"></a>相似矩阵相关的输入与依赖 [KG_PEARSON_MATRIX](#evidence-kg_pearson_matrix) | 补全已有指导 | [K01-02](K01_statistics.md#k01-02) | 共享对象的矩阵取非对角三角元素一次，按对象处理依赖；补出原始与测量信度校正的尺度差异，121/D012未报告的展平方式仍未知。 |
| <a id="gap-kg_spearman"></a>Spearman秩变换、并列与单调解释 [KG_SPEARMAN](#evidence-kg_spearman) | 补全已有指导 | [K01-03](K01_statistics.md#k01-03) | 两列共同筛缺失、分别转秩并取秩的Pearson。086/D009有大量并列，不能照无并列简式；矩阵情形还要保留对象依赖。 |
| <a id="gap-kg_kendall"></a>Kendall序对计分、归一与并列变体 [KG_KENDALL](#evidence-kg_kendall) | 补全已有指导 | [K01-03](K01_statistics.md#k01-03) | 按一致、逆序及单列并列的对数构造τ；167/D016印出的τ-a公式不支持补认实际调用τ-b。 |
| <a id="gap-kg_fisher_contrast"></a>Fisher变换及相关差异检验 [KG_FISHER_CONTRAST](#evidence-kg_fisher_contrast) | 补全已有指导 | [K01-04](K01_statistics.md#k01-04) | 独立样本用Fisher z标准误，补清共享对象联合重抽并计算相关差的做法。026/D032和222/D023的依赖处理与秩相关条件分别保留。 |
| <a id="gap-kg_effect_cohen_q"></a>Fisher变换相关差的Cohen q需补知识 [KG_EFFECT_COHEN_Q](#evidence-kg_effect_cohen_q) | 补全已有指导 | [K01-04](K01_statistics.md#k01-04) | 在一致的参照方向上取两个Fisher变换相关之差。045/D018的q与同文均值d、优势比OR分开，比较共享对象时另需处理依赖。 |
| <a id="gap-kg_t_mean_execution"></a>均值差t检验的标准误、方差版本、自由度与尾方向 [KG_T_MEAN_EXECUTION](#evidence-kg_t_mean_execution) | 补全已有指导 | [K01-05](K01_statistics.md#k01-05) | 补出单样本均值检验、独立组统计量及预定单双尾；配对t用差值、Welch用分组方差。107/D019报告Welch，不能因材料对应改记配对t。 |
| <a id="gap-kg_variance_f_pretest"></a>方差比F检验及用其选择t版本的限制 [KG_VARIANCE_F_PRETEST](#evidence-kg_variance_f_pretest) | 补全已有指导 | [K01-05](K01_statistics.md#k01-05) | 174/D007按方差比预检选择Student或Welch，按组自由度查F尾。预检与随后检验合成的错误率需整体考虑。 |
| <a id="gap-kg_z_mean_execution"></a>z检验的标准误来源、正态近似与双尾推断 [KG_Z_MEAN_EXECUTION](#evidence-kg_z_mean_execution) | 补全已有指导 | [K01-05](K01_statistics.md#k01-05) | 估计差减假设差后除以有依据的SE，按预定方向取正态尾。115/D011与177/D021的单位和双侧选择分别解释。 |
| <a id="gap-worker_3_kg_f_variance_pretest"></a>F方差比预检及条件t检验路由操作知识 [worker_3_KG_F_VARIANCE_PRETEST](#evidence-worker_3_kg_f_variance_pretest) | 补全已有指导 | [K01-05](K01_statistics.md#k01-05) | 174/D006的论文正文报告方差比F预检及全研究的0.01显著性水平。作者公开代码将较大方差放在分子，把相应F分布的上尾概率乘二。 |
| <a id="gap-kg_signed"></a>Wilcoxon差值符号秩推断需补知识 [KG_SIGNED](#evidence-kg_signed) | 补全已有指导 | [K01-06](K01_statistics.md#k01-06) | 补明以W⁺的大小选择单侧方向和翻转符号参照的前提，保留零差、并列及差值对称性。199/D219是d′相对1的大于侧。 |
| <a id="gap-kg_test_mann_whitney"></a>Mann–Whitney U秩和比较 [KG_TEST_MANN_WHITNEY](#evidence-kg_test_mann_whitney) | 补全已有指导 | [K01-06](K01_statistics.md#k01-06) | 两独立组混合排序得U，用预定方向及适当并列处理。104/D012按类型比较，校正前后的结果不能互换。 |
| <a id="gap-kg_test_kruskal_wallis"></a>Kruskal–Wallis多组秩比较 [KG_TEST_KRUSKAL_WALLIS](#evidence-kg_test_kruskal_wallis) | 补全已有指导 | [K01-06](K01_statistics.md#k01-06) | 对独立组秩和构造H并用并列因子修正；031/D013整体拒绝后另作成对比较，H本身不给差异组别。 |
| <a id="gap-worker_4_gap_friedman"></a>Friedman块内重复秩检验操作支持 [worker_4_gap_friedman](#evidence-worker_4_gap_friedman) | 补全已有指导 | [K01-06](K01_statistics.md#k01-06) | 明确R_j为条件在各区组的秩和，逐块处理并列再计算Q。220/D007的块构造与自由度仍以该篇披露为限。 |
| <a id="gap-kg_tukey"></a>Tukey成对比较规则 [KG_TUKEY](#evidence-kg_tukey) | 补全已有指导 | [K01-07](K01_statistics.md#k01-07) | 以共同MSE、组量、组数和误差自由度计算学生化极差。049/D020实际使用的误差结构未知，具体显著对不能由方法名恢复。 |
| <a id="gap-kg_anova_execution"></a>ANOVA平方和、误差项、自由度与F推断 [KG_ANOVA_EXECUTION](#evidence-kg_anova_execution) | 补全已有指导 | [K01-07](K01_statistics.md#k01-07) | 组间/组内均方比处理独立单因素设计；因子交互及重复测量须配合实际设计和误差项。163/D006–D007同时有模型、选项及交互。 |
| <a id="gap-kg_table_chisquare"></a>类别频数的χ²检验操作与解释需补 [KG_TABLE_CHISQUARE](#evidence-kg_table_chisquare) | 补全已有指导 | [K01-08](K01_statistics.md#k01-08) | 以边际总数构造期望格与自由度，按观测计数检验，检查稀疏格和重复单位。237/D027对双零格加数会改变样本计数。 |
| <a id="gap-kg_table_fisher"></a>固定边际Fisher精确检验操作与解释需补 [KG_TABLE_FISHER](#evidence-kg_table_fisher) | 补全已有指导 | [K01-08](K01_statistics.md#k01-08) | 给定边际枚举可行表，2×2按超几何概率和预定尾计算。144/D009未报告具体表维和尾侧，不把重复测量视作自动独立。 |
| <a id="gap-kg_test_mcnemar"></a>McNemar配对二元边际比较 [KG_TEST_MCNEMAR](#evidence-kg_test_mcnemar) | 补全已有指导 | [K01-08](K01_statistics.md#k01-08) | 只用同题在两条件不一致的两个计数，在二项精确或卡方近似中注明连续性修正。114/D013未说明1至6分怎样映为两类。 |
| <a id="gap-worker_3_kg_cramer_v"></a>列联表Cramér V关联强度操作知识 [worker_3_KG_CRAMER_V](#evidence-worker_3_kg_cramer_v) | 补入具体做法 | [K01-08](K01_statistics.md#k01-08) | 用χ²按N和最小表维缩放开方得无方向强度；179/D013的品牌间加权方式未说明，不能代填等权。 |
| <a id="gap-kg_test_binomial"></a>二项事件计数的尾概率检验 [KG_TEST_BINOMIAL](#evidence-kg_test_binomial) | 补全已有指导 | [K01-09](K01_statistics.md#k01-09) | 在独立同概率的零模型下，按成功数累加指定方向的二项尾。243/D011从原支持集筛剩两项后，条件化事件和尾侧都须重新界定。 |
| <a id="gap-worker_1_kg_exact_multinomial"></a>PMF排序双侧精确多项检验需补知识 [worker_1_KG_EXACT_MULTINOMIAL](#evidence-worker_1_kg_exact_multinomial) | 补入具体做法 | [K01-09](K01_statistics.md#k01-09) | 243/D012固定类别、计数总和和均匀零概率，枚举并累加PMF不超过观测值的向量；此处的双侧按概率排序。 |
| <a id="gap-kg_prec_sem"></a>均值标准误及有效重复单位的估计与解释知识 [KG_PREC_SEM](#evidence-kg_prec_sem) | 补全已有指导 | [K01-10](K01_statistics.md#k01-10) | 独立单位均值用s/√n，带权或相关时按权重和协方差求SE。205/D014代码以层×运行为n，实际独立性未证实。 |
| <a id="gap-kg_prec_coef"></a>回归系数标准误的估计与解释知识 [KG_PREC_COEF](#evidence-kg_prec_coef) | 补全已有指导 | [K01-10](K01_statistics.md#k01-10) | 系数SE由协方差矩阵对角开方；按误差结构选常规、异方差稳健或成簇估计。008/D015系数的SE不可拿参数本身的SD替换。 |
| <a id="gap-kg_prec_cluster"></a>按聚类单位估计标准误的估计与解释知识 [KG_PREC_CLUSTER](#evidence-kg_prec_cluster) | 补全已有指导 | [K01-10](K01_statistics.md#k01-10) | 同簇残差得分先求和再进入夹心协方差，交代簇数及修正。021/D012按选项对聚类，具体小样本修正未报告。 |
| <a id="gap-kg_prec_tci"></a>t统计量均值置信区间的估计与解释知识 [KG_PREC_TCI](#evidence-kg_prec_tci) | 补全已有指导 | [K01-10](K01_statistics.md#k01-10) | 补明精确的小样本均值t区间要求独立、同一正态总体，使用样本SD估SE和n−1自由度；非正态小样本的覆盖率未获保证。若比较配对均值差应以独立差值为单位。033/D017报告五运行t区间，具体配对和实现未详。 |
| <a id="gap-kg_prec_normal"></a>正态临界值乘标准误区间的估计与解释知识 [KG_PREC_NORMAL](#evidence-kg_prec_normal) | 补全已有指导 | [K01-10](K01_statistics.md#k01-10) | 按正态近似临界值乘有效SE构造区间；040/D015给出均值±1.96SEM，有限样本适配性由独立单位和分布决定。 |
| <a id="gap-kg_prec_binom"></a>二项比例plug-in标准误的估计与解释知识 [KG_PREC_BINOM](#evidence-kg_prec_binom) | 补全已有指导 | [K01-11](K01_statistics.md#k01-11) | 独立Bernoulli单位以p̂(1−p̂)/n估方差，边界处plug-in退化。186/D005为一个SE；同题两比例差需处理协方差。 |
| <a id="gap-kg_prec_cp"></a>Clopper–Pearson二项置信区间的估计与解释知识 [KG_PREC_CP](#evidence-kg_prec_cp) | 补全已有指导 | [K01-11](K01_statistics.md#k01-11) | 补齐0次或全成功时等尾二项反演的另一侧端点。195/D003有限样本证书依赖其iid检测事件口径。 |
| <a id="gap-kg_prec_dci"></a>Cohen d近似标准误与区间的估计与解释知识 [KG_PREC_DCI](#evidence-kg_prec_dci) | 补全已有指导 | [K01-11](K01_statistics.md#k01-11) | 按所采用的标准化均差和两组n选方差近似，再配正态临界值；205/D022共享材料不直接满足独立组d的公式条件。 |
| <a id="gap-kg_prec_wilson"></a>Wilson score二项置信区间的估计与解释知识 [KG_PREC_WILSON](#evidence-kg_prec_wilson) | 补全已有指导 | [K01-11](K01_statistics.md#k01-11) | 给出Wilson区间的中心和半宽，在极端比例仍保留不确定性；212/D014的重复观测依赖不会由score公式消失。 |
| <a id="gap-kg_mc_dynamic_baseline"></a>随状态更新的随机任务机会模拟 [KG_MC_DYNAMIC_BASELINE](#evidence-kg_mc_dynamic_baseline) | 补入具体做法 | [K01-13](K01_statistics.md#k01-13) | 119/D024从初始库存开始选合法随机组合，每步更新状态后再算可行成绩；固定首步机会率无法描述后续轨迹。 |
| <a id="gap-kg_mc_null_quantile"></a>随机任务轨迹零分布与分位阈值 [KG_MC_NULL_QUANTILE](#evidence-kg_mc_null_quantile) | 补全已有指导 | [K01-13](K01_statistics.md#k01-13) | 145/D025以随机策略反复运行适用任务，每条轨迹重新计分，再用预定分位数作阈值，保留作者排除的任务。 |
| <a id="gap-kg_permutation_reference"></a>重排机会分布构造与尾概率 [KG_PERMUTATION_REFERENCE](#evidence-kg_permutation_reference) | 补入具体做法 | [K01-13](K01_statistics.md#k01-13) | 声明交换单元、保持配对或簇、按每次重排重算原统计量。020/D026用打乱生成机会分布后另作t比较，168/D012按更小Hamming的左尾计数。 |
| <a id="gap-kg_test_permanova"></a>距离矩阵PERMANOVA [KG_TEST_PERMANOVA](#evidence-kg_test_permanova) | 补入具体做法 | [K01-13](K01_statistics.md#k01-13) | 由共同对象的距离矩阵求总、组内及组间平方和，构造pseudo-F并按允许的对象置换取右尾；048/D019同题跨语言的依赖需核对。 |
| <a id="gap-kg_bonferroni"></a>Bonferroni操作规则 [KG_BONFERRONI](#evidence-kg_bonferroni) | 补全已有指导 | [K01-14](K01_statistics.md#k01-14) | 先定一族m个检验，再按α/m或截断的mp判定。243/D015的不同阶段各有比较族，154/D020所用族仍未知。 |
| <a id="gap-kg_holm"></a>Holm逐步校正规则 [KG_HOLM](#evidence-kg_holm) | 补全已有指导 | [K01-14](K01_statistics.md#k01-14) | 排序后依序降低校正倍数，从首个未过阈值处停止。120/D019针对成对秩比较；020/D030未交代的族不由方法名推定。 |
| <a id="gap-kg_bh"></a>BH校正规则与解释 [KG_BH](#evidence-kg_bh) | 补全已有指导 | [K01-14](K01_statistics.md#k01-14) | 排序取满足iα/m的最大i，拒绝此前项并给反向累计最小的调整p。160/D016每种偏差为一族，依赖条件仍应说明。 |
| <a id="gap-kg_fdr_interpretation"></a>FDR控制目标的解释 [KG_FDR_INTERPRETATION](#evidence-kg_fdr_interpretation) | 补全已有指导 | [K01-14](K01_statistics.md#k01-14) | FDR关注拒绝集合中错误比例的期望，FWER关注至少一个错误。104/D013和121/D025仅报FDR，算法继续留空。 |
| <a id="gap-worker_3_kg_fisher_p_combination"></a>Fisher对数p值合并操作知识 [worker_3_KG_FISHER_P_COMBINATION](#evidence-worker_3_kg_fisher_p_combination) | 补入具体做法 | [K01-14](K01_statistics.md#k01-14) | 独立且连续均匀零p值时，−2Σlog(p)参照2m自由度卡方；179/D012的品牌内共享资料可能使p值相关。 |
| <a id="gap-kg_effect_inverse_variance"></a>按逆方差精度加权合并估计需补知识 [KG_EFFECT_INVERSE_VARIANCE](#evidence-kg_effect_inverse_variance) | 补入具体做法 | [K01-15](K01_statistics.md#k01-15) | 逆采样方差加权汇总同目标效应并按依赖结构求SE。003/D319用五个模型，方差的具体估计未完整报告。 |
| <a id="gap-kg_effect_standardized_difference"></a>按适当变异尺度标准化均值差需补知识 [KG_EFFECT_STANDARDIZED_DIFFERENCE](#evidence-kg_effect_standardized_difference) | 补全已有指导 | [K01-15](K01_statistics.md#k01-15) | 同一观测单位前后差按配对差SD标准化，两独立组用pooled SD。014/D215的逐对分布图不能读作均值差区间。 |
| <a id="gap-kg_effect_odds_ratio"></a>以优势比表示二元结果差异需补知识 [KG_EFFECT_ODDS_RATIO](#evidence-kg_effect_odds_ratio) | 补全已有指导 | [K01-15](K01_statistics.md#k01-15) | 由事件概率转优势后作组间比，反转参照则取倒数。045/D018涉及OR向d的转换时须满足潜在logistic尺度假设。 |
| <a id="gap-worker_4_gap_reml_meta"></a>REML随机效应元分析操作支持 [worker_4_gap_reml_meta](#evidence-worker_4_gap_reml_meta) | 补全已有指导 | [K01-15](K01_statistics.md#k01-15) | 补出无调节变量的REML异质方差目标、log OR权重及反变换，175/D023排除重叠Pooled，多个相关效应不得强作独立。 |
| <a id="gap-worker_5_epsilon_squared_gap"></a>Kruskal–Wallis秩统计效应量：操作知识 [worker_5_EPSILON_SQUARED_gap](#evidence-worker_5_epsilon_squared_gap) | 补入具体做法 | [K01-15](K01_statistics.md#k01-15) | 按199/D217的(H−k+1)/(N−k)由秩检验量换算效应，原代码等组量设定和负值处置需说明。 |
| <a id="gap-worker_5_rank_biserial_gap"></a>独立与配对秩二列效应计分：操作知识 [worker_5_RANK_BISERIAL_gap](#evidence-worker_5_rank_biserial_gap) | 补入具体做法 | [K01-15](K01_statistics.md#k01-15) | 独立样本按有方向的U归一，配对数据以正负秩和之差除总和。199/D218的零差与方向按论文代码保留。 |
| <a id="gap-kg_reg_linear_fit"></a>线性响应模型的系数拟合的操作与解释知识 [KG_REG_LINEAR_FIT](#evidence-kg_reg_linear_fit) | 补全已有指导 | [K01-16](K01_statistics.md#k01-16) | 从设计行与响应建立线性预测，最小化平方残差并识别共线。085/D023的二次基函数仍线性于系数；未注明准则的实例不补认OLS。 |
| <a id="gap-kg_reg_contrast_matrix"></a>回归对比编码及系数含义的操作与解释知识 [KG_REG_CONTRAST_MATRIX](#evidence-kg_reg_contrast_matrix) | 补全已有指导 | [K01-16](K01_statistics.md#k01-16) | 用组内−.5/+.5、组外0的实例落实对比列和截距、交互的条件解释，衔接073/D010的两组内对比。 |
| <a id="gap-kg_reg_wls_fit"></a>加权最小二乘关联拟合的操作与解释知识 [KG_REG_WLS_FIT](#evidence-kg_reg_wls_fit) | 补全已有指导 | [K01-16](K01_statistics.md#k01-16) | 最小化加权残差平方和并按权重含义选SE。123/D016的职业人口权重界定代表性，与逆误差方差权重分开。 |
| <a id="gap-kg_reg_r2_score"></a>固定回归解释方差R²的计算与解释的操作与解释知识 [KG_REG_R2_SCORE](#evidence-kg_reg_r2_score) | 补全已有指导 | [K01-16](K01_statistics.md#k01-16) | 按既定基准总变差和残差和计算R²，注明拟合内外与截距。049/D007的固定回归与混合模型条件R²使用不同定义。 |
| <a id="gap-kg_reg_logistic_fit"></a>二元或二项logistic系数与条件优势解释的操作与解释知识 [KG_REG_LOGISTIC_FIT](#evidence-kg_reg_logistic_fit) | 补全已有指导 | [K01-17](K01_statistics.md#k01-17) | 按二元或成组成功数建立logit似然，明确参照和交互；系数指数是条件优势比。032/D011用每对话成功数和总数，未报告的链接设置不代填。 |
| <a id="gap-kg_reg_probit_fit"></a>probit选择模型估计的操作与解释知识 [KG_REG_PROBIT_FIT](#evidence-kg_reg_probit_fit) | 补全已有指导 | [K01-17](K01_statistics.md#k01-17) | 以标准正态CDF将线性预测转成选择概率，再按观察选择拟合似然。035/D009的策略特征预测选择并不识别模型内部机制。 |
| <a id="gap-kg_reg_elastic_refit"></a>弹性网筛选后无惩罚logistic重拟合的操作与解释知识 [KG_REG_ELASTIC_REFIT](#evidence-kg_reg_elastic_refit) | 补入具体做法 | [K01-17](K01_statistics.md#k01-17) | 写出混合L1/L2加权损失。032/D012先选非零变量再无惩罚拟合，同数据筛选使后续p值的通常解释受限。 |
| <a id="gap-kg_reg_l2_logistic_fit"></a>带类别权重的L2正则logistic分析的操作与解释知识 [KG_REG_L2_LOGISTIC_FIT](#evidence-kg_reg_l2_logistic_fit) | 补全已有指导 | [K01-17](K01_statistics.md#k01-17) | 在共同目标式中区分类别权重、λ和特征缩放；243/D028是训练分析器预测状态，不代表对被测LLM重新训练。 |
| <a id="gap-kg_reg_mixed_fit"></a>线性或广义混合模型的参数与方差估计的操作与解释知识 [KG_REG_MIXED_FIT](#evidence-kg_reg_mixed_fit) | 补全已有指导 | [K01-18](K01_statistics.md#k01-18) | 线性模型区分固定和随机部分并用ML/REML，广义混合模型条件于随机效应建似然再积分。099/D008的机器概率与D015真人二元反应分开。 |
| <a id="gap-kg_mixed_r2_nakagawa"></a>混合模型Nakagawa边际与条件R²的操作知识 [KG_MIXED_R2_NAKAGAWA](#evidence-kg_mixed_r2_nakagawa) | 补入具体做法 | [K01-18](K01_statistics.md#k01-18) | 固定预测与随机方差分别进入边际/条件R²分子；049/D005的随机斜率需结合设计点和响应尺度汇总。 |
| <a id="gap-kg_reg_coef_wald_test"></a>回归系数Wald z或t推断的操作与解释知识 [KG_REG_COEF_WALD_TEST](#evidence-kg_reg_coef_wald_test) | 补全已有指导 | [K01-19](K01_statistics.md#k01-19) | 估计系数减假设值后除以相应SE，对比使用cᵀCov(β)c。073/D013明确z/p，按所报参照解释而不将任意±当SE。 |
| <a id="gap-kg_reg_model_f_test"></a>线性回归模型F检验的操作与解释知识 [KG_REG_MODEL_F_TEST](#evidence-kg_reg_model_f_test) | 补全已有指导 | [K01-19](K01_statistics.md#k01-19) | 用受限与完整模型RSS差按新增自由度归一，再除残差均方。165/D025三个设置的分母自由度仅1，保留小样本限制。 |
| <a id="gap-kg_model_emm"></a>拟合模型的估计边际均值与对比的操作知识 [KG_MODEL_EMM](#evidence-kg_model_emm) | 补全已有指导 | [K01-19](K01_statistics.md#k01-19) | 给出参考格设计行的加权线性组合、条件间对比和SE，区分先逆链接还是先平均。099/D011的未报校正方法保留未知。 |
| <a id="gap-kg_model_lrt"></a>嵌套模型似然与deviance比较的操作知识 [KG_MODEL_LRT](#evidence-kg_model_lrt) | 补入具体做法 | [K01-19](K01_statistics.md#k01-19) | 取两倍完整与受限模型对数似然差，按嵌套约束、边界及选择后条件判断参照。032/D013顺序加项与099/D010逐项删项不同。 |
| <a id="gap-kg_fit_tjur"></a>二元回归Tjur区分系数的操作知识 [KG_FIT_TJUR](#evidence-kg_fit_tjur) | 补入具体做法 | [K01-19](K01_statistics.md#k01-19) | 补明两类均有观测、差值方向及界限。073/D014的指标是阳/阴性观测的平均拟合概率之差，和OLS方差解释度分开。 |
| <a id="gap-kg_reg_bayes_hier_fit"></a>贝叶斯层级线性回归估计的操作与解释知识 [KG_REG_BAYES_HIER_FIT](#evidence-kg_reg_bayes_hier_fit) | 补全已有指导 | [K01-20](K01_statistics.md#k01-20) | 按响应建似然并以群体参数与先验将组系数部分汇合，联立后验拟合。133/D016对斜率抽样形成区间，不能还原成平均r。 |
| <a id="gap-kg_reg_bayes_multinom_fit"></a>贝叶斯多项logistic层级估计的操作与解释知识 [KG_REG_BAYES_MULTINOM_FIT](#evidence-kg_reg_bayes_multinom_fit) | 补全已有指导 | [K01-20](K01_statistics.md#k01-20) | 给出基准类η=0、非基准类别的相对log优势、softmax与后验逐类对比。133/D010的条件分布中各类概率相互依赖。 |
| <a id="gap-kg_reg_bayes_logodds_weight"></a>广义Bayes先验与似然权重回归的操作与解释知识 [KG_REG_BAYES_LOGODDS_WEIGHT](#evidence-kg_reg_bayes_logodds_weight) | 补入具体做法 | [K01-20](K01_statistics.md#k01-20) | 主观概率先作logit，再对先验logit和log似然比拟合含截距模型，以斜率表示相对权重。003/D309概率端点需声明处理。 |
| <a id="gap-kg_post_nuts_summary"></a>NUTS后验抽样及参数/预测可信区间需补知识 [KG_POST_NUTS_SUMMARY](#evidence-kg_post_nuts_summary) | 补全已有指导 | [K01-20](K01_statistics.md#k01-20) | 以多链R-hat、ESS、发散等检视抽样，参数分位点与通过似然另抽响应的预测区间对应不同目标。133/D012分开两类摘要。 |
| <a id="gap-kg_post_gaussian_additive"></a>Gaussian加性模型的Bayesian估计需补知识 [KG_POST_GAUSSIAN_ADDITIVE](#evidence-kg_post_gaussian_additive) | 补全已有指导 | [K01-20](K01_statistics.md#k01-20) | 高斯似然配合分类加性效应、先验及可识别约束形成联合后验。197/D016没有凭软件名补认具体抽样器。 |
| <a id="gap-kg_post_contrast_interval"></a>后验参数差值及可信区间比较需补知识 [KG_POST_CONTRAST_INTERVAL](#evidence-kg_post_contrast_interval) | 补全已有指导 | [K01-20](K01_statistics.md#k01-20) | 逐次联合后验抽样中先取参数差，再汇总可信区间。197/D017报告95%及是否跨零，具体是否为HDI未报。 |
| <a id="gap-kg_post_grid_marginal"></a>有限参数网格后验及边缘化需补知识 [KG_POST_GRID_MARGINAL](#evidence-kg_post_grid_marginal) | 补入具体做法 | [K01-21](K01_statistics.md#k01-21) | 按各网格点的似然、先验及格宽归一，沿非目标参数求和，再算后验均值。200/D021的离散步长敏感性与均值目标分开。 |
| <a id="gap-kg_post_ordered_bayes_factor"></a>有序替代假设的边缘似然比较需补知识 [KG_POST_ORDERED_BAYES_FACTOR](#evidence-kg_post_ordered_bayes_factor) | 补入具体做法 | [K01-21](K01_statistics.md#k01-21) | 分别归一共享参数模型与有序约束模型的先验并积分取边缘似然比，保留网格精度。200/D022将参数区间扩大后改用更粗网格。 |
| <a id="gap-worker_2_likelihood_chance_gap"></a>与均匀机会参照比较最大对数似然操作与解释 [worker_2_likelihood_chance_gap](#evidence-worker_2_likelihood_chance_gap) | 补入具体做法 | [K01-21](K01_statistics.md#k01-21) | 同一套观测与首手/全局动作单位下计算机会模型和拟合模型的对数似然。178/D012原公式符号与数值例的张力不自行消除。 |
| <a id="gap-kg_explain_rf_impurity"></a>随机森林不纯度重要性需补知识 [KG_EXPLAIN_RF_IMPURITY](#evidence-kg_explain_rf_impurity) | 补入具体做法 | [K01-22](K01_statistics.md#k01-22) | 在树上按样本权重累计节点分裂后的不纯度降低，再跨树汇总。014/D220用它选前15个可视化特征，重要性不表示因果大小。 |
| <a id="gap-kg_explain_linear_shap"></a>线性模型SHAP与背景参照需补知识 [KG_EXPLAIN_LINEAR_SHAP](#evidence-kg_explain_linear_shap) | 补入具体做法 | [K01-22](K01_statistics.md#k01-22) | 线性模型在独立背景下用β_j(x_j−E_bg X_j)分解；保留相关背景设置和预测尺度。243/D031在留出集汇总绝对归因。 |
| <a id="gap-kg_pred_grouped_cv"></a>按同来源组划折的调参交叉验证需补知识 [KG_PRED_GROUPED_CV](#evidence-kg_pred_grouped_cv) | 补全已有指导 | [K01-22](K01_statistics.md#k01-22) | 按来源划分训练和验证，必要时兼顾类型比例，并将调参置于训练折内。014/D208同一doc_id的人机记录须同折。 |
| <a id="gap-kg_pred_oob_estimate"></a>袋外预测与拟合内/外部测试的区分需补知识 [KG_PRED_OOB_ESTIMATE](#evidence-kg_pred_oob_estimate) | 补全已有指导 | [K01-22](K01_statistics.md#k01-22) | 每个观测仅汇总没抽到它的树的预测，记录袋外覆盖；014/D218将RF的OOB列标作Training，与lasso拟合内评分区分。 |
| <a id="gap-kg_pred_cv_grid_holdout"></a>内层网格调参与外层留出的预测评价需补知识 [KG_PRED_CV_GRID_HOLDOUT](#evidence-kg_pred_cv_grid_holdout) | 补全已有指导 | [K01-22](K01_statistics.md#k01-22) | 分层切分后在内层训练折拟合预处理、网格选择，再独立估计整套过程的预测性能。243/D029实际先在整个外层训练集标准化，照实记录。 |
| <a id="gap-kg_prec_prop"></a>方差传播及变换后区间精度的估计与解释知识 [KG_PREC_PROP](#evidence-kg_prec_prop) | 补全已有指导 | [K01-23](K01_statistics.md#k01-23) | 补出正态绝对值的折叠分布及其均值、方差，再按职业权重汇总。118/D012中最终截界和临界值未报告，不能重建确切95%区间。 |
| <a id="gap-kg_var_binomial_propagation"></a>二项比例与独立均值的方差传播 [KG_VAR_BINOMIAL_PROPAGATION](#evidence-kg_var_binomial_propagation) | 补全已有指导 | [K01-23](K01_statistics.md#k01-23) | 独立二项比例按p̂(1−p̂)/n求方差，118/D010用d=2p−1故增四倍；独立职业平均再按权重平方求和。 |
| <a id="gap-kg_var_linear_residual"></a>线性等式check的标准化残差 [KG_VAR_LINEAR_RESIDUAL](#evidence-kg_var_linear_residual) | 补入具体做法 | [K01-23](K01_statistics.md#k01-23) | 按实际线性系数与协方差传播，并区分150/D021的Bernoulli形式诊断尺度、β稳定项及D023的违界分支，不能当普适z检验。 |
| <a id="gap-kg_var_delta_residual"></a>乘积与全概率约束的一阶误差传播 [KG_VAR_DELTA_RESIDUAL](#evidence-kg_var_delta_residual) | 补入具体做法 | [K01-23](K01_statistics.md#k01-23) | 用乘积或全概率残差对各参数的梯度传播一阶误差；150/D022的条件方向及符号张力不靠此公式替原作者修正。 |
| <a id="gap-kg_cv_compare"></a>不同测量跨数据集的CV比较需补知识 [KG_CV_COMPARE](#evidence-kg_cv_compare) | 补全已有指导 | [K01-24](K01_statistics.md#k01-24) | 以SD除均值比较相对离散，先辨量尺零点及均值是否接近零。041/D018的跨数据集指标差异还取决于任务和构成。 |
| <a id="gap-kg_distance_skew"></a>成对距离的非对称性偏度 [KG_DISTANCE_SKEW](#evidence-kg_distance_skew) | 补入具体做法 | [K01-24](K01_statistics.md#k01-24) | 以参照γ和成对距离比衡量对称性，分母为零时未定义。058/D006并未给有方向的三阶矩偏度，保留报告中的数值不一致。 |
| <a id="gap-kg_density_kde"></a>核密度估计与分布展示 [KG_DENSITY_KDE](#evidence-kg_density_kde) | 补入具体做法 | [K01-24](K01_statistics.md#k01-24) | 说明核、带宽和密度归一，按有界指标调整边界。177/D018给每个边界点加Gaussian核，平滑与后续Wasserstein距离分开。 |
| <a id="gap-kg_density_violin"></a>小提琴密度形状的分组展示 [KG_DENSITY_VIOLIN](#evidence-kg_density_violin) | 补入具体做法 | [K01-24](K01_statistics.md#k01-24) | 把平滑密度映成对称宽度，须明确带宽和各组面积/样本量的缩放约定。026/D011无法只凭均值重建所画分布。 |
| <a id="gap-kg_smooth_lowess"></a>LOWESS局部加权回归平滑 [KG_SMOOTH_LOWESS](#evidence-kg_smooth_lowess) | 仅属真人参照 | [K01-24](K01_statistics.md#k01-24) | 078/D005仅平滑历史国会议员用词者的意识形态趋势。原文将它列为历史语料案例，该操作没有测量或控制模型行为。 |
| <a id="gap-kg_test_shapiro"></a>Shapiro–Wilk正态性诊断 [KG_TEST_SHAPIRO](#evidence-kg_test_shapiro) | 补全已有指导 | [K01-25](K01_statistics.md#k01-25) | 用排序样本与正态次序统计量权重构成W，由适配算法求p。107/D011对原分数及模型内成对句差的未拒绝均不构成正态证明。 |
| <a id="gap-kg_fit_normal_distribution"></a>观测分布的正态模型拟合 [KG_FIT_NORMAL_DISTRIBUTION](#evidence-kg_fit_normal_distribution) | 补全已有指导 | [K01-25](K01_statistics.md#k01-25) | 补出正态MLE的均值、方差分母与由密度得到区间概率的关系。123/D017没有给出采用MLE的证据，拟合图亦不能验证大数定律。 |
| <a id="gap-kg_token_label_z"></a>词项标签零基线z关联诊断 [KG_TOKEN_LABEL_Z](#evidence-kg_token_label_z) | 补全已有指导 | [K01-25](K01_statistics.md#k01-25) | 明确含词的独立单位、标签计数、零基线及零模型SE，说明同文内重复、多个词项比较的边界。122/D017使用的阈值本身不能证明捷径可泛化。 |
| <a id="gap-kg_test_levene"></a>Levene方差齐性检验 [KG_TEST_LEVENE](#evidence-kg_test_levene) | 补全已有指导 | [K01-25](K01_statistics.md#k01-25) | 各组与指定中心的绝对离差进入组间F比较。089/D009非显著不足以证明相同方差；159/D021的中心和配对处置未详。 |
| <a id="gap-kg_test_ks"></a>Kolmogorov–Smirnov分布检验 [KG_TEST_KS](#evidence-kg_test_ks) | 补全已有指导 | [K01-25](K01_statistics.md#k01-25) | 按经验CDF最大距离和一/两样本问题选参照；075/D014未交代如何处理同样本估参，197/D011同一条链跨代依赖不能忽略。 |
| <a id="gap-kg_test_runs"></a>Wald–Wolfowitz游程随机性检验 [KG_TEST_RUNS](#evidence-kg_test_runs) | 补入具体做法 | [K01-25](K01_statistics.md#k01-25) | 保留原顺序数二元游程，给定两类总数求零分布，必要时使用精确参照。021/D028未拒绝游程检验不能推得序列必然随机。 |
| <a id="gap-kg_power_correlation"></a>针对相关的功效与样本量规划 [KG_POWER_CORRELATION](#evidence-kg_power_correlation) | 补全已有指导 | [K01-26](K01_statistics.md#k01-26) | 根据相关量级、尾侧、功效及独立配对单位规划样本，Pearson Fisher近似有分布前提。088/D009在人类标定机器实验材料时用相关筛题招募，不认作模型调用数或已复验其功效。 |
| <a id="gap-kg_sampling_gaussian_plugin"></a>二项比例高斯误差及plug-in模型 [KG_SAMPLING_GAUSSIAN_PLUGIN](#evidence-kg_sampling_gaussian_plugin) | 补全已有指导 | [K01-26](K01_statistics.md#k01-26) | 补明150/D020以F代未知T形成高斯零模型方差，σ²控制严格度，只有在对应假设下可类比独立二项均值，未做bootstrap。 |
| <a id="gap-kg_gaussian_rejection_quantile"></a>标准正态双侧阈值的检验解释 [KG_GAUSSIAN_REJECTION_QUANTILE](#evidence-kg_gaussian_rejection_quantile) | 补全已有指导 | [K01-26](K01_statistics.md#k01-26) | 按双侧1−α/2或单侧1−α取正态临界值；150/D024的γσ=.129是该理论参照下的判据，不等于数据证实99%覆盖。 |
| <a id="gap-kg_test_tost"></a>预定界限内两单侧等效检验 [KG_TEST_TOST](#evidence-kg_test_tost) | 补入具体做法 | [K01-26](K01_statistics.md#k01-26) | 预定实质量尺上下界，分别拒绝两个单侧零假设才可支持等效。023/D015将标准化界转换到Brier尺度，常规非显著没有同样含义。 |
| <a id="gap-kg_univariate_f_select"></a>单变量F关联特征评分 [KG_UNIVARIATE_F_SELECT](#evidence-kg_univariate_f_select) | 补入具体做法 | [K01-27](K01_statistics.md#k01-27) | 补出每个单变量相对截距基准的RSS差和残差自由度计算F，再排序。135/D031据F选前五，不能解释为控制其他特征后的贡献。 |
| <a id="gap-kg_select_aic"></a>AIC前向模型项选择 [KG_SELECT_AIC](#evidence-kg_select_aic) | 补入具体做法 | [K01-27](K01_statistics.md#k01-27) | 最大对数似然与参数数目共同决定AIC；073/D012用前向路径选择结构，最终无随机项不证明初始结构比较不重要。 |
| <a id="gap-kg_select_bic"></a>BIC候选模型比较 [KG_SELECT_BIC](#evidence-kg_select_bic) | 补入具体做法 | [K01-27](K01_statistics.md#k01-27) | 相同观测和相同似然尺度下，用k log n惩罚比较BIC。243/D014原文称最低BIC，代码按似然差排序，二者一致性取决于维数和样本。 |
| <a id="gap-worker_2_constrained_lrt_gap"></a>约束等概率备择与迭代似然比删项操作与解释 [worker_2_constrained_lrt_gap](#evidence-worker_2_constrained_lrt_gap) | 补入具体做法 | [K01-27](K01_statistics.md#k01-27) | 243/D013逐一比较候选低频项，按当前支持集校正并删除选中项。低频项在论文图2与作者代码中的计算不同，第27节并列两种写法及其对选项去留的影响。 |
| <a id="gap-worker_2_bartlett_gap"></a>Bartlett相关矩阵球形检验操作与解释 [worker_2_bartlett_gap](#evidence-worker_2_bartlett_gap) | 补入具体做法 | [K01-28](K01_statistics.md#k01-28) | 在相关矩阵非退化且模型适用时，以样本量修正的负log行列式和p(p−1)/2自由度检验单位矩阵。229/D027显著结果不能决定因子数。 |
| <a id="gap-worker_3_kg_minres_varimax_efa"></a>MINRES提取并Varimax旋转的探索性因素分析操作知识 [worker_3_KG_MINRES_VARIMAX_EFA](#evidence-worker_3_kg_minres_varimax_efa) | 补全已有指导 | [K01-28](K01_statistics.md#k01-28) | 按非对角残差拟合共同因子，选维后以Varimax正交旋转解释载荷。229/D028的特征值门槛和三因子为个案配置。 |

## K02 标注、裁决与信度

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_cohen"></a>Cohen机会校正一致性需补知识 [KG_COHEN](#evidence-kg_cohen) | 补全已有指导 | [K02-02](K02_annotation_reliability.md#k02-02) | 从共同标注集计算观察与边际机会一致，再作校正。049的模型预测对人标注可用；097未说明哪些专家重叠，不能重建配对。 |
| <a id="gap-kg_cohen_mean"></a>两两Cohen及其聚合需补知识 [KG_COHEN_MEAN](#evidence-kg_cohen_mean) | 补全已有指导 | [K02-02](K02_annotation_reliability.md#k02-02) | 每对按其共同对象算κ，保留权重与样本重叠。050的多对均值和080的跨域汇总均不能作一次多人κ。 |
| <a id="gap-kg_weighted"></a>有序加权Cohen一致性需补知识 [KG_WEIGHTED](#evidence-kg_weighted) | 补全已有指导 | [K02-02](K02_annotation_reliability.md#k02-02) | 有序类别先指定损失矩阵，再校正边际机会损失。019未报告权重，线性和平方权重只能作为可选约定。 |
| <a id="gap-kg_fleiss"></a>Fleiss多评分者一致性需补知识 [KG_FLEISS](#evidence-kg_fleiss) | 补全已有指导 | [K02-03](K02_annotation_reliability.md#k02-03) | 在原计数公式上补入同一输出逐维建表及份额缺原计数时的限制；059的多维解释评分、069的类别份额不能自动合并。 |
| <a id="gap-kg_rel_fleiss"></a>多评分者类别机会一致的Fleiss κ操作与解释需补 [KG_REL_FLEISS](#evidence-kg_rel_fleiss) | 补全已有指导 | [K02-03](K02_annotation_reliability.md#k02-03) | 按题内成对一致与总体边际做机会校正。180的裁判对错和214资深审阅者修改标签对应不同测量阶段，不能当作一张原始评分表。 |
| <a id="gap-kg_gwet"></a>原文Gwet gamma的信度目标需补知识 [KG_GWET](#evidence-kg_gwet) | 补全已有指导 | [K02-03](K02_annotation_reliability.md#k02-03) | 增补明确选择无权重AC1时的机会项与适用条件，区分原始同意率、机会模型及带权尺度。054的gamma变体、多选聚合未报，不能据此重算或推广200句子集。 |
| <a id="gap-kg_kappa_family"></a>具体κ变体未明的机会校正信度目标需补知识 [KG_KAPPA_FAMILY](#evidence-kg_kappa_family) | 补全已有指导 | [K02-03](K02_annotation_reliability.md#k02-03) | 可登记机会校正目标与评分者设计；067和075的变体未明，不能从人数推定Fleiss或Cohen。 |
| <a id="gap-kg_alpha"></a>Krippendorff一致性alpha需补知识 [KG_ALPHA](#evidence-kg_alpha) | 补全已有指导 | [K02-04](K02_annotation_reliability.md#k02-04) | 以有效的重合计数、距离和缺失模式构造Do/De。053仅比较人类作答，作为该例范围限制；人工评价实验材料或模型输出的操作仍可使用。 |
| <a id="gap-kg_rel_krippendorff"></a>观测与期望分歧的Krippendorff α操作与解释需补 [KG_REL_KRIPPENDORFF](#evidence-kg_rel_krippendorff) | 补全已有指导 | [K02-04](K02_annotation_reliability.md#k02-04) | 按尺度选距离，报告有效对象及机会分歧；112分层平均不等于池化，219的条件子集另算。高原始一致率不替代α。 |
| <a id="gap-kg_rel_icc"></a>方差成分ICC一致性估计操作与解释需补 [KG_REL_ICC](#evidence-kg_rel_icc) | 补全已有指导 | [K02-05](K02_annotation_reliability.md#k02-05) | 先选评者效应、绝对一致或一致性、单次或平均评分，再选方差分析或相应区间。220虽给ICC2及区间，未明的聚合及区间法保留未知。 |
| <a id="gap-kg_rel_cronbach"></a>条目方差与总分方差的Cronbach α操作与解释需补 [KG_REL_CRONBACH](#evidence-kg_rel_cronbach) | 补全已有指导 | [K02-06](K02_annotation_reliability.md#k02-06) | 由对象×条目矩阵计算条目与总分方差，处理方向、缺失及重复层级。029的聚合分不够反推矩阵，088的跨模型计算也不支持单维性结论。 |
| <a id="gap-kg_rel_spearman_brown"></a>分半相关的Spearman–Brown长度校正 [KG_REL_SPEARMAN_BROWN](#evidence-kg_rel_spearman_brown) | 补全已有指导 | [K02-06](K02_annotation_reliability.md#k02-06) | 逐cue随机分半后各建强度，求半间相关再按平行半测假设校正。103所用系数名称不决定第一步相关种类。 |
| <a id="gap-kg_rel_split_correlation"></a>随机分半后重构表征并比较相关 [KG_REL_SPLIT_CORRELATION](#evidence-kg_rel_split_correlation) | 补全已有指导 | [K02-06](K02_annotation_reliability.md#k02-06) | 分原始反应或句子，在各半重建频数、语气矩阵再比。047的两处数值和分割表述分别保存，不能自动加长度校正。 |
| <a id="gap-kg_rel_matched_fisher_mean"></a>跨初始化维度匹配和Fisher变换平均 [KG_REL_MATCHED_FISHER_MEAN](#evidence-kg_rel_matched_fisher_mean) | 补全已有指导 | [K02-07](K02_annotation_reliability.md#k02-07) | 先在同一对象上作维度匹配，再Fisher变换平均并逆变换。121每个原维取最大值，不强加独一配对，记录同数据选优的偏差。 |
| <a id="gap-kg_rel_attenuation"></a>用分半可靠性校正相关衰减 [KG_REL_ATTENUATION](#evidence-kg_rel_attenuation) | 补全已有指导 | [K02-07](K02_annotation_reliability.md#k02-07) | 用两系统信度几何均值校正观察相关，同时保留原相关；121外部RSM与另抽样的直接一致率不是同一量。 |
| <a id="gap-kg_rel_noise_ceiling"></a>重复试次信噪比噪声上限与R²归一 [KG_REL_NOISE_CEILING](#evidence-kg_rel_noise_ceiling) | 补全已有指导 | [K02-08](K02_annotation_reliability.md#k02-08) | 明确模型表征预测人脑测量时，信号噪声和重复次数来自目标器官的观测，R²和上限先统一尺度；121的三次重复不能计作模型采样。 |

## K03 文本与语义评价

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_cosine"></a>余弦度量的方向归一与适用范围 [KG_COSINE](#evidence-kg_cosine) | 补入具体做法 | [K03-01](K03_text_semantics.md#k03-01) | 保留非零向量点积除范数及相似方向；新增121的模型特征三选一与人体脑区参照、159的BIOS评分工具验证边界。045的方向比较不测幅度，042的点积检索不改为余弦。 |
| <a id="gap-kg_cosine_semantic"></a>以嵌入余弦构成语义比较协议 [KG_COSINE_SEMANTIC](#evidence-kg_cosine_semantic) | 补入具体做法 | [K03-01](K03_text_semantics.md#k03-01) | 区分对应参考集最近邻、全配对与质心，补入长文分块和027的句向量分数与逐token匹配的名称冲突；159的BIOS得分仅验证工具。 |
| <a id="gap-kg_frozen_representation"></a>读取与构造现成冻结表征 [KG_FROZEN_REPRESENTATION](#evidence-kg_frozen_representation) | 补入具体做法 | [K03-01](K03_text_semantics.md#k03-01) | 保留词、句、图文、池化、掩码及归一要求；增加054的词外项删样与196的多词/子词回退，比较前核对有效分母。编码器冻结并不说明下游分类头也冻结。 |
| <a id="gap-kg_dependency"></a>依存关系表示与匹配需补知识 [KG_DEPENDENCY](#evidence-kg_dependency) | 补入具体做法 | [K03-02](K03_text_semantics.md#k03-02) | 从句法解析中取有方向的依存边或仅取关系标签，明确比较单位。070的标签F1只支持标签重叠，不能推出两树相同。 |
| <a id="gap-kg_lemma"></a>词形还原与形态归一需补知识 [KG_LEMMA](#evidence-kg_lemma) | 补入具体做法 | [K03-02](K03_text_semantics.md#k03-02) | 逐词按词性及上下文归到词元；新增先保留短语跨度再决定逐词归一或整词匹配，防止归一时遗失多词边界。078的具体清洗次序保留为实例。 |
| <a id="gap-kg_contig"></a>最长共同连续片段匹配需补知识 [KG_CONTIG](#evidence-kg_contig) | 补入具体做法 | [K03-03](K03_text_semantics.md#k03-03) | 相等时对角加一、不等时归零，表中最大值给最长共同连续片段长。027、042用该长度，不可用平均n-gram精确率替代。 |
| <a id="gap-kg_lcs"></a>最长公共子序列匹配需补知识 [KG_LCS](#evidence-kg_lcs) | 补入具体做法 | [K03-03](K03_text_semantics.md#k03-03) | 不等时可跳过任侧元素，允许非连续；按目标选择原文长度或分别按两侧长度归一。127用于原文覆盖、155用于文本打分、165用于检索。 |
| <a id="gap-kg_span"></a>带类型跨度匹配需补知识 [KG_SPAN](#evidence-kg_span) | 补入具体做法 | [K03-04](K03_text_semantics.md#k03-04) | 统一文档与偏移量后按起点、终点、类型严格一一匹配，再算TP/FP/FN。065的实体跨度评估与逐词多数类准确率分别计算。 |
| <a id="gap-kg_bleu"></a>BLEU匹配、长度惩罚与聚合 [KG_BLEU](#evidence-kg_bleu) | 补入具体做法 | [K03-05](K03_text_semantics.md#k03-05) | 按参考最大次数裁剪各阶计数，合成几何均值后乘长度惩罚；记录语料级汇总及零计数平滑。134用低重合指较少重复，011的翻译分数不能证明文化等值。 |
| <a id="gap-kg_rouge_l"></a>非连续LCS及ROUGE-L序列归约 [KG_ROUGE_L](#evidence-kg_rouge_l) | 补入具体做法 | [K03-05](K03_text_semantics.md#k03-05) | LCS分别除以候选和参考序列长度形成P、R，再按权重求F；摘要级union-LCS另定句界。242用词干化F与阈值，224的短篇辅助评价不推广到整库。 |
| <a id="gap-kg_chrf_pp"></a>ChrF++字符词阶数与F聚合 [KG_CHRF_PP](#evidence-kg_chrf_pp) | 补入具体做法 | [K03-05](K03_text_semantics.md#k03-05) | 补明SacreBLEU的字符及词一/二元阶匹配计数、有效阶汇总、Fβ分母与语料计数聚合，并区别另一平滑路径。165仅首行译文进入比较。 |
| <a id="gap-worker_1_kg_meteor"></a>METEOR词对齐与片段惩罚需补知识 [worker_1_KG_METEOR](#evidence-worker_1_kg_meteor) | 补入具体做法 | [K03-05](K03_text_semantics.md#k03-05) | 先按情景与行动选人类参考，再将生成词与参考一一对齐，汇总P/R并按连续片段数惩罚。110的低分不能独立证明后果推断质量。 |
| <a id="gap-worker_5_bertscore_gap"></a>上下文词元向量最相似匹配与BERTScore归约：操作知识 [worker_5_BERTSCORE_gap](#evidence-worker_5_bertscore_gap) | 补入具体做法 | [K03-06](K03_text_semantics.md#k03-06) | 上下文词向量相似矩阵沿行和列分别取最大，再分别平均成P/R并合成F；不要求一一匹配。223使用precision，196的负分截零属于展示。 |
| <a id="gap-kg_simcse_score"></a>SimCSE参考语义评分的使用边界 [KG_SIMCSE_SCORE](#evidence-kg_simcse_score) | 补入具体做法 | [K03-06](K03_text_semantics.md#k03-06) | 每步输出与明确的参照配对后读取评分并应用阈值。012对照起初的故事，0.74是其阈值，底层具体度量未报告。 |
| <a id="gap-kg_bleurt"></a>BLEURT参考质量评分协议 [KG_BLEURT](#evidence-kg_bleurt) | 补入具体做法 | [K03-06](K03_text_semantics.md#k03-06) | 给定候选和参照取已有BLEURT的连续分；058把分位映到MQM另立校准步骤，076作翻译比较，分值均不直接等于实际人评。 |
| <a id="gap-kg_unieval"></a>UniEval分维度质量评价 [KG_UNIEVAL](#evidence-kg_unieval) | 补入具体做法 | [K03-06](K03_text_semantics.md#k03-06) | 按任务准备源文、候选或参照，分别读取指定维度后汇总。058只用流畅与可懂维度，得分变化不确认译文忠实。 |
| <a id="gap-worker_1_kg_blanc"></a>摘要条件下源文遮蔽预测增益需补知识 [worker_1_KG_BLANC](#evidence-worker_1_kg_blanc) | 补入具体做法 | [K03-07](K03_text_semantics.md#k03-07) | 在同一组掩码上配对无摘要/有摘要的命中，补明relative净改善的分子和分母，区分BLANC-help和BLANC-tune。224未报掩码细节留在个案。 |
| <a id="gap-worker_5_supert_gap"></a>源文伪参考选择与SUPERT语义评价：操作知识 [worker_5_SUPERT_gap](#evidence-worker_5_supert_gap) | 补入具体做法 | [K03-07](K03_text_semantics.md#k03-07) | 从源文构造伪参考，编码后按两个方向的最大token相似度归约，再按方案合并多个伪参考。224没有交代选句配置，不把作者软件的一种方案认作其实用设置。 |
| <a id="gap-kg_nli_relation_interpretation"></a>有方向的NLI关系及核验含义 [KG_NLI_RELATION_INTERPRETATION](#evidence-kg_nli_relation_interpretation) | 补入具体做法 | [K03-08](K03_text_semantics.md#k03-08) | 明确P→H方向与支持、矛盾、未定三类含义，再按用途过滤或计分。027的错误文档同样可能支持自己的错误前提。 |
| <a id="gap-kg_nli_zero_shot_bridge"></a>类别标签到NLI假设与分类输出的映射 [KG_NLI_ZERO_SHOT_BRIDGE](#evidence-kg_nli_zero_shot_bridge) | 补入具体做法 | [K03-08](K03_text_semantics.md#k03-08) | 把待分类文本作前提、类别含义作候选假设，选择多标签或互斥分数归约；048的讨论/拒答标签及拒答词过滤另有语义，模型命名和模板未知保留。 |
| <a id="gap-kg_factive_diagnostic"></a>事实性预设、嵌入命题与问句极性的区分 [KG_FACTIVE_DIAGNOSTIC](#evidence-kg_factive_diagnostic) | 补入具体做法 | [K03-08](K03_text_semantics.md#k03-08) | 分开标注触发词、嵌入命题与主句问答极性，再解释模型回应。050对主句答否不自动否认预设，德语触发词的边界承接到实例。 |
| <a id="gap-kg_tfidf_weighting"></a>TF-IDF的文档参照与词项权重解释 [KG_TFIDF_WEIGHTING](#evidence-kg_tfidf_weighting) | 补入具体做法 | [K03-09](K03_text_semantics.md#k03-09) | 先定文档单位与参照库，由文档内词频和跨库文档频率加权。033是先筛候选再人工处理；047词云颜色的平滑与归一未给定。 |
| <a id="gap-worker_4_gap_bm25"></a>BM25词项检索与重排操作支持 [worker_4_gap_bm25](#evidence-worker_4_gap_bm25) | 补入具体做法 | [K03-09](K03_text_semantics.md#k03-09) | 按查询词的逆文档频率、文内饱和词频及长度归一合并得分并截取top-k。235重排搜索结果，127在检索子集没有命中不足以宣布整库无匹配。 |
| <a id="gap-worker_3_kg_vector_neighbor_retrieval"></a>向量近邻索引与记忆片段检索操作知识 [worker_3_KG_VECTOR_NEIGHBOR_RETRIEVAL](#evidence-worker_3_kg_vector_neighbor_retrieval) | 补入具体做法 | [K03-09](K03_text_semantics.md#k03-09) | 补写排序后保留片段及文档ID、去重、拼接与上下文预算。103的词级近邻、177的分块检索、242的context外片段返回单位不同；202使用Faiss仍不能确定具体度量。 |
| <a id="gap-worker_2_corpus_query_gap"></a>语料索引存在性与文档共现查询操作与解释 [worker_2_corpus_query_gap](#evidence-worker_2_corpus_query_gap) | 补入具体做法 | [K03-10](K03_text_semantics.md#k03-10) | 补写按文档ID取交集与连续词序存在查询的区别。072的文档命中可含歧义，223的近似计数保留遗漏，127精确查询后才转语义匹配。 |
| <a id="gap-worker_2_ngram_backoff_gap"></a>最长已见前缀的n-gram回退概率操作与解释 [worker_2_ngram_backoff_gap](#evidence-worker_2_ngram_backoff_gap) | 补入具体做法 | [K03-10](K03_text_semantics.md#k03-10) | 按目标token查最长已见上下文，逐级缩短到有计数的前缀再求条件频率；223对单个零值与整串全零的特殊处理仅作其个案。 |
| <a id="gap-worker_2_suffix_index_gap"></a>后缀数组成员与重复频次搜索操作与解释 [worker_2_suffix_index_gap](#evidence-worker_2_suffix_index_gap) | 补入具体做法 | [K03-10](K03_text_semantics.md#k03-10) | 排序后的后缀起点按完整前缀二分取左右界，连续相邻后缀的公共前缀长决定重复桶；239的桶端点及实现记号不明继续保留。 |
| <a id="gap-worker_4_gap_substring_twopointer"></a>DJ SEARCH单调双指针匹配查询操作支持 [worker_4_gap_substring_twopointer](#evidence-worker_4_gap_substring_twopointer) | 补入具体做法 | [K03-11](K03_text_semantics.md#k03-11) | 在精确成员查询的子串闭包下，成功扩右界、失败移左界并恢复最短跨度，指针单调故至多线性数量的查询。127末端不一致保留。 |
| <a id="gap-worker_4_gap_span_prefix_search"></a>基于余弦缓存与前缀和的连续跨度检索操作支持 [worker_4_gap_span_prefix_search](#evidence-worker_4_gap_span_prefix_search) | 补入具体做法 | [K03-11](K03_text_semantics.md#k03-11) | 缓存词对余弦和文档侧最大值的前缀和；反向须按每个跨度更新最大值，两向较差者通过阈值才命中。127这一路无精确子串闭包保证。 |
| <a id="gap-kg_dirichlet_word_logodds"></a>Dirichlet收缩词频log-odds差异 [KG_DIRICHLET_WORD_LOGODDS](#evidence-kg_dirichlet_word_logodds) | 补入具体做法 | [K03-12](K03_text_semantics.md#k03-12) | 以背景语料给出先验强度，两组各算平滑log-odds再相减，以近似方差平方根标准化。039未报的先验强度单列。 |
| <a id="gap-worker_3_kg_lexicon_sentiment"></a>词典及组合规则情绪计分操作知识 [worker_3_KG_LEXICON_SENTIMENT](#evidence-worker_3_kg_lexicon_sentiment) | 补入具体做法 | [K03-12](K03_text_semantics.md#k03-12) | 保留否定、强度、标点等组合规则；补写工具字段、阈值与输出类别的对应。175用VADER compound，064用TextBlob polarity，两个量尺不能互换默认阈值。 |
| <a id="gap-worker_2_flesch_gap"></a>Flesch系句词音节可读性量尺操作与解释 [worker_2_flesch_gap](#evidence-worker_2_flesch_gap) | 补入具体做法 | [K03-13](K03_text_semantics.md#k03-13) | 根据句、词、音节数分别计算Reading Ease与Kincaid Grade，记录易度和年级的相反方向。067列出两种分，243明确调用年级版，042版本不明。 |
| <a id="gap-worker_2_ari_gap"></a>Automated Readability Index操作与解释 [worker_2_ari_gap](#evidence-worker_2_ari_gap) | 补入具体做法 | [K03-13](K03_text_semantics.md#k03-13) | ARI由每词字符数和每句词数按给定系数组合，空分母单列。064以≤0筛句，筛选阈值不代替计分。 |
| <a id="gap-worker_2_fog_gap"></a>Gunning–Fog复杂词可读性操作与解释 [worker_2_fog_gap](#evidence-worker_2_fog_gap) | 补入具体做法 | [K03-13](K03_text_semantics.md#k03-13) | 按平均句长和复杂词百分比组合Fog；明确复杂词的音节、专名等排除规则。197使用textstat，不把教育年数量尺解作实际读者理解。 |
| <a id="gap-worker_5_readability_consensus_gap"></a>多可读性量尺的学校年级共识：操作知识 [worker_5_READABILITY_CONSENSUS_gap](#evidence-worker_5_readability_consensus_gap) | 补入具体做法 | [K03-13](K03_text_semantics.md#k03-13) | 补入textstat 0.7.10的七项三票、Reading Ease转换成年级票及众数/同票规则。035测的是已有模型文本，所用软件版本仍未报告。 |
| <a id="gap-worker_5_lexical_types_gap"></a>类型语法的补语与mass-count解释：操作知识 [worker_5_LEXICAL_TYPES_gap](#evidence-worker_5_lexical_types_gap) | 补全已有指导 | [K03-14](K03_text_semantics.md#k03-14) | 从每次解析的词汇条目追到继承类型、补语与可数性，再对同表面词分别计数。104的law不同条目是实例；解析失败不说明模型没有这种语言能力。 |

## K04 概率取得、条件化与分布比较

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_prob_token_read"></a>候选token的条件概率与logprob读出所需操作知识 [KG_PROB_TOKEN_READ](#evidence-kg_prob_token_read) | 补入具体做法 | [K04-01](K04_probability.md#k04-01) | 补明044同一论文里的top10候选求和与指定完成词取分两条路径，以及强制后分布语义未知的处理。037取补数、168缺项、238置−100均不能冒充实测概率。 |
| <a id="gap-kg_prob_arch_head"></a>不同模型架构的预测位置与概率头接口所需操作知识 [KG_PROB_ARCH_HEAD](#evidence-kg_prob_arch_head) | 补入具体做法 | [K04-01](K04_probability.md#k04-01) | decoder的下一词、encoder的掩码和encoder-decoder的目标位置各自绑定前缀与token。020/072的sentinel约定须随架构辨认。 |
| <a id="gap-kg_top"></a>top-K预测熵检测信号的知识边界 [KG_TOP](#evidence-kg_top) | 补入具体做法 | [K04-02](K04_probability.md#k04-02) | 区分截断熵贡献、top-K内归一条件熵和再除log K；低熵不能当作事实可靠性的证明。 |
| <a id="gap-kg_prob_tail_bound"></a>截断候选分布中缺失token质量上界所需操作知识 [KG_PROB_TAIL_BOUND](#evidence-kg_prob_tail_bound) | 补入具体做法 | [K04-02](K04_probability.md#k04-02) | 仅在返回真实top-K且保留原概率时，可用尾部总质量与最后返回项概率的较小者界定单个漏项。002所用上界及再归一需注明。 |
| <a id="gap-kg_prob_biased_tail"></a>logit调整与截断尾部近似的候选测量所需操作知识 [KG_PROB_BIASED_TAIL](#evidence-kg_prob_biased_tail) | 补入具体做法 | [K04-02](K04_probability.md#k04-02) | 标明偏置干预和尾部均匀假设。020的可见候选受logit bias改变，不能回推干预前尾部排序。 |
| <a id="gap-kg_prob_perplexity"></a>条件文本困惑度及目标范围计分所需操作知识 [KG_PROB_PERPLEXITY](#evidence-kg_prob_perplexity) | 补入具体做法 | [K04-03](K04_probability.md#k04-03) | 只对指定目标token平均负条件log再取指数。020单向模型与masked模型须分别报告，004印刷符号冲突保留。 |
| <a id="gap-kg_prob_causal_chain"></a>自回归目标序列条件概率与surprisal取得所需操作知识 [KG_PROB_CAUSAL_CHAIN](#evidence-kg_prob_causal_chain) | 补入具体做法 | [K04-03](K04_probability.md#k04-03) | 在真实前缀上按选定目标计算log和，排除只作为条件的提示。077打分整段而006打分续尾；055教师强制的损失不等同自由生成频率。 |
| <a id="gap-kg_prob_slor"></a>unigram基准的长度归一SLOR所需操作知识 [KG_PROB_SLOR](#evidence-kg_prob_slor) | 补入具体做法 | [K04-03](K04_probability.md#k04-03) | 扣除同一分词规则下的unigram对数基线，按目标长度归一。006的参照语料与符号须保留，这个数没有校准概率含义。 |
| <a id="gap-kg_prob_masked_pll"></a>双向逐token遮蔽伪对数似然所需操作知识 [KG_PROB_MASKED_PLL](#evidence-kg_prob_masked_pll) | 补入具体做法 | [K04-04](K04_probability.md#k04-04) | 固定其他token逐位置遮蔽；092的整词子词同遮与031逐词元遮蔽是不同协议，分数不等同自回归联合似然。 |
| <a id="gap-kg_prob_random_mask_chain"></a>随机mask填回链与句概率近似的解释 [KG_PROB_RANDOM_MASK_CHAIN](#evidence-kg_prob_random_mask_chain) | 补入具体做法 | [K04-04](K04_probability.md#k04-04) | 全mask后按指定顺序填回真词，各步条件随路径改变。166的100个随机顺序为个案配置，多个log链的均值不能确立唯一联合分布。 |
| <a id="gap-worker_4_gap_unmasked_token_score"></a>完整可见输入的AUL/AULA评分操作支持 [worker_4_gap_unmasked_token_score](#evidence-worker_4_gap_unmasked_token_score) | 补入具体做法 | [K04-04](K04_probability.md#k04-04) | AUL在可见整句上计分，AULA再按attention归约。107的目标仍可见，须同遮蔽PLL分开。 |
| <a id="gap-kg_prob_reference_rank"></a>参照引导的token到词排名协议 [KG_PROB_REFERENCE_RANK](#evidence-kg_prob_reference_rank) | 补入具体做法 | [K04-05](K04_probability.md#k04-05) | 由054的目标词前缀限制候选，补成整词后映回token序位。未匹配和并列须明示，参照引导结果不等自由生成命中率。 |
| <a id="gap-kg_hdiff"></a>两分布熵差的集中度比较的知识边界 [KG_HDIFF](#evidence-kg_hdiff) | 补入具体做法 | [K04-06](K04_probability.md#k04-06) | 明确用各自分布的熵相减、顺序和单位。021称RE的数与通常KL不同；熵相等并不说明分布相同。 |
| <a id="gap-kg_entmeasure"></a>解释分布熵的测量解释的知识边界 [KG_ENTMEASURE](#evidence-kg_entmeasure) | 补入具体做法 | [K04-06](K04_probability.md#k04-06) | 明确得分转换、赞数加权、支持集和温度再读熵。100的人类评论与模型输出来源不同，弥散程度不能直接认作认知歧义。 |
| <a id="gap-kg_perplex"></a>熵与有效类别数的转换的知识边界 [KG_PERPLEX](#evidence-kg_perplex) | 补入具体做法 | [K04-06](K04_probability.md#k04-06) | 以配套的对数底/指数转换为有效类别数，并注明类别数归一。129的确定性分数依赖候选集。 |
| <a id="gap-worker_5_gini_simpson_gap"></a>类型概率二次集中度的异类概率解释：操作知识 [worker_5_GINI_SIMPSON_gap](#evidence-worker_5_gini_simpson_gap) | 补入具体做法 | [K04-06](K04_probability.md#k04-06) | 在有放回异类概率上补入无放回的计数公式及N≥2条件。104以token分布计数，不混作类型总数或Shannon熵。 |
| <a id="gap-kg_ig"></a>预期熵减与信息增益的知识边界 [KG_IG](#evidence-kg_ig) | 补入具体做法 | [K04-07](K04_probability.md#k04-07) | 从先验熵扣除按答案概率加权的后验熵，零质量分支贡献为零。140正文公式符号不一，不能据教程消除原文冲突。 |
| <a id="gap-kg_decomp"></a>混合前后熵的分解解释的知识边界 [KG_DECOMP](#evidence-kg_decomp) | 补全已有指导 | [K04-07](K04_probability.md#k04-07) | 对各提示形式先混合后算熵，并与逐形式熵加权比较；相反的确定回答可有零条件熵、高混合熵。 |
| <a id="gap-kg_jsdiag"></a>多形式JSD与不确定性来源诊断的知识边界 [KG_JSDIAG](#evidence-kg_jsdiag) | 补全已有指导 | [K04-07](K04_probability.md#k04-07) | 各形式到混合分布的加权KL等于形式间JSD。191的1−JSD另有方向及单位；不能直接称一致概率。 |
| <a id="gap-kg_kl"></a>有方向KL分布比较的知识边界 [KG_KL](#evidence-kg_kl) | 补入具体做法 | [K04-08](K04_probability.md#k04-08) | 统一支持，明示谁是参考及平滑。096参照来自联合和边缘关系；106的人类潜在分布是代理，偏离量没有因果含义。 |
| <a id="gap-kg_js"></a>Jensen–Shannon散度与距离的知识边界 [KG_JS](#evidence-kg_js) | 补入具体做法 | [K04-08](K04_probability.md#k04-08) | 先混合再求相对熵，对称散度开根才是距离。100用距离，147的均值方向符号属于后加显示变换。 |
| <a id="gap-kg_jsshift"></a>JSD逐词贡献分解的知识边界 [KG_JSSHIFT](#evidence-kg_jsshift) | 补入具体做法 | [K04-08](K04_probability.md#k04-08) | 对共同词表逐词求两侧的加权KL贡献再排序。039的参照是两文本混合，和外部背景下的词显著性有别。 |
| <a id="gap-kg_pmi"></a>PMI联合相对独立基准的关联的知识边界 [KG_PMI](#evidence-kg_pmi) | 补入具体做法 | [K04-08](K04_probability.md#k04-08) | 联合频率相对边缘乘积取log，报告事件、底数和稀有项。060的上下文边际明确，平均PMI检验不能证明所有变量独立。 |
| <a id="gap-kg_cross"></a>对称负交叉熵比较的知识边界 [KG_CROSS](#evidence-kg_cross) | 补入具体做法 | [K04-08](K04_probability.md#k04-08) | 哪个分布给权重、哪个供log项必须明确。095使用末位置全词表的两方向负交叉熵平均，较高分的方向由负号决定。 |
| <a id="gap-kg_wasserstein"></a>Wasserstein的支持集、运输代价与尺度 [KG_WASSERSTEIN](#evidence-kg_wasserstein) | 补入具体做法 | [K04-09](K04_probability.md#k04-09) | 增补离散选项位置与计数/权重的实际输入，防止把概率数组当支持值。021使用多维实现，196的名义标签代价未知，147后加方向符号。 |
| <a id="gap-kg_calib_background_median"></a>属性背景中位数校准 [KG_CALIB_BACKGROUND_MEDIAN](#evidence-kg_calib_background_median) | 补入具体做法 | [K04-10](K04_probability.md#k04-10) | 从对应属性位置的校准集估log中位数，再减偏置并取最大。143另处写平均的矛盾留在实例，不据此改写通用步骤。 |
| <a id="gap-kg_calib_contentfree"></a>无内容输入的先验概率校准 [KG_CALIB_CONTENTFREE](#evidence-kg_calib_contentfree) | 补入具体做法 | [K04-10](K04_probability.md#k04-10) | 在同模板中性输入上估标签偏好，明确映射及近零分母。020比率中代数抵消和158实际无内容校准是两种情况。 |
| <a id="gap-kg_calib_pride"></a>PriDe排列先验重校准 [KG_CALIB_PRIDE](#evidence-kg_calib_pride) | 补入具体做法 | [K04-10](K04_probability.md#k04-10) | 在均衡排列中求ID先验，再按内容概率除先验归一；158的静态修正依赖排列下内容效应可迁移。 |
| <a id="gap-kg_pairrank_mle"></a>TopK成对条件似然估计候选分布 [KG_PAIRRANK_MLE](#evidence-kg_pairrank_mle) | 补入具体做法 | [K04-11](K04_probability.md#k04-11) | 明确038题内候选的无惩罚有限唯一解须由正权重胜边双向可达。跨组无比较时尺度未定，只有单向胜边时相对强度趋向边界，求解超参数仍未知。 |
| <a id="gap-kg_prob_ccp"></a>主张条件概率评分与词到主张聚合所需操作知识 [KG_PROB_CCP](#evidence-kg_prob_ccp) | 补入具体做法 | [K04-12](K04_probability.md#k04-12) | 先用NLI区分替换词的蕴涵、矛盾和无关，再按词条件概率归约到主张。015的跨主张平均与阈值另记。 |
| <a id="gap-worker_5_semantic_entropy_gap"></a>双向蕴涵聚类后的语义概率熵：操作知识 [worker_5_SEMANTIC_ENTROPY_gap](#evidence-worker_5_semantic_entropy_gap) | 补入具体做法 | [K04-12](K04_probability.md#k04-12) | 问句内按双向蕴涵归类并累加质量，再算语义熵、跨问句归约。015低熵可能源自稳定错误。 |
| <a id="gap-kg_joint"></a>逐步信心到联合正确概率的解释需补知识 [KG_JOINT](#evidence-kg_joint) | 补入具体做法 | [K04-13](K04_probability.md#k04-13) | 先定义此前各步都正确的条件，再连乘；038分步口头信心的边际乘积须有额外假设，模型直接报总分与重算分开。 |
| <a id="gap-worker_2_first_event_gap"></a>首次事件生存概率及奖励操作与解释 [worker_2_first_event_gap](#evidence-worker_2_first_event_gap) | 补入具体做法 | [K04-13](K04_probability.md#k04-13) | 补入117正文式（2）：从首次答对概率累积C_t，以真人进度h_t形成K_t=h_t C_t及剩余项，奖励R与误差1−R分开。原文h_t叙述与求和的含义有张力，正式末轮处理及附录示例冲突保留。 |
| <a id="gap-worker_5_first_success_gap"></a>有限无放回首成功的期望次数：操作知识 [worker_5_FIRST_SUCCESS_gap](#evidence-worker_5_first_success_gap) | 补入具体做法 | [K04-13](K04_probability.md#k04-13) | 引用有限N中s个成功元素无放回首个成功的位置分布与期望。016是理论难度，s为零须另定义耗尽停止。 |
| <a id="gap-kg_folded_normal_moments"></a>绝对正态变量的折叠分布矩 [KG_FOLDED_NORMAL_MOMENTS](#evidence-kg_folded_normal_moments) | 补入具体做法 | [K04-14](K04_probability.md#k04-14) | 正态差值取绝对值后用折叠正态一、二阶矩，跨组按权重及协方差传播。118不能把原差值的SD当绝对差SD。 |
| <a id="gap-worker_2_beta_cdf_gap"></a>已定Beta后验中的点估计累计概率位置操作与解释 [worker_2_beta_cdf_gap](#evidence-worker_2_beta_cdf_gap) | 补入具体做法 | [K04-14](K04_probability.md#k04-14) | 在点估计处求正则化不完全Beta积分；085用它衡量后验累计位置，与后验均值误差或错误概率不同。 |
| <a id="gap-worker_4_gap_bayes_prompt_factor"></a>提示式Bayesian因子分解与近似父节点删除操作支持 [worker_4_gap_bayes_prompt_factor](#evidence-worker_4_gap_bayes_prompt_factor) | 补入具体做法 | [K04-15](K04_probability.md#k04-15) | 联合链式分解可直接成立，删父节点则需明示近似独立假设与重组条件；235的提示图不构成因果识别。 |

## K05 校准、区分能力与排序评价

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_bin_sq"></a>箱内平方差加权校准需补知识 [KG_BIN_SQ](#evidence-kg_bin_sq) | 补全已有指导 | [K05-01](K05_evaluation.md#k05-01) | 给出同一箱平方偏差与绝对偏差的数值差异，保留Nk/N权重。023、116都明确按方差型箱内偏差记分，不等于逐例Brier。 |
| <a id="gap-kg_bin_abs"></a>箱内绝对差加权校准需补知识 [KG_BIN_ABS](#evidence-kg_bin_abs) | 补全已有指导 | [K05-01](K05_evaluation.md#k05-01) | 补明端点归箱和空箱权重。117以clue加权、130以exact match比较、147箱数未知，不从一个实验代填另一个。 |
| <a id="gap-kg_bin_unknown"></a>已命名但未细报形式的ECE需补知识 [KG_BIN_UNKNOWN](#evidence-kg_bin_unknown) | 补入具体做法 | [K05-01](K05_evaluation.md#k05-01) | 只对齐概率条件目标及分箱程序；038/146未报损失或边界时保留未知，无法从ECE名称确定实际实现。 |
| <a id="gap-kg_bin_target"></a>条件校准目标与图形评价需补知识 [KG_BIN_TARGET](#evidence-kg_bin_target) | 补全已有指导 | [K05-01](K05_evaluation.md#k05-01) | 用同一声称信心组的实际正确频率检查条件匹配，再用箱近似该目标。172的图示刻度不能用作实际箱边。 |
| <a id="gap-kg_bin_class"></a>最高类别及按类的条件校准需补知识 [KG_BIN_CLASS](#evidence-kg_bin_class) | 补全已有指导 | [K05-02](K05_evaluation.md#k05-02) | 对最高类命中和各类one-vs-rest分别分箱；106的按类等权、等距log箱及概率轴等宽方案各有不同权重。 |
| <a id="gap-kg_curve_roc"></a>ROC阈值曲线与排序AUC操作与解释需补 [KG_CURVE_ROC](#evidence-kg_curve_roc) | 补入具体做法 | [K05-03](K05_evaluation.md#k05-03) | 按正负例总数归一得到TPR/FPR，跨阈值并对并列给半权。147印刷分母冲突、073只给ROC图时照实区分，AUC不证明概率已校准。 |
| <a id="gap-kg_curve_pr"></a>目标类Precision–Recall曲线面积操作与解释需补 [KG_CURVE_PR](#evidence-kg_curve_pr) | 补入具体做法 | [K05-03](K05_evaluation.md#k05-03) | 补上以检错为目标时如何同时定正类与分数方向，038、147的方向冲突仍属原文限制；149的两种参照各自有不同正例基率。 |
| <a id="gap-kg_curve_map"></a>平均精度AP与多标签mAP操作与解释需补 [KG_CURVE_MAP](#evidence-kg_curve_map) | 补入具体做法 | [K05-03](K05_evaluation.md#k05-03) | 明列AP的排名累积、截断和平均口径。020按人类前一至五位形成五个相关集；136多标签的类平均细节未报。 |
| <a id="gap-kg_score_mcc"></a>二元混淆矩阵Matthews相关系数 [KG_SCORE_MCC](#evidence-kg_score_mcc) | 补入具体做法 | [K05-04](K05_evaluation.md#k05-04) | 从四格计数和边际总数得MCC；常数预测导致零分母，030后续把负值截零属于另一个变换。 |
| <a id="gap-kg_pair_btl_spectral"></a>BTL成对比较谱排序 [KG_PAIR_BTL_SPECTRAL](#evidence-kg_pair_btl_spectral) | 补入具体做法 | [K05-05](K05_evaluation.md#k05-05) | 从胜负图构造转移矩阵、求平稳强度且检查连通性。087只报告谱排名，不用示例矩阵替原文补超参。 |
| <a id="gap-kg_bt_pair_fit"></a>Bradley–Terry成对强度拟合 [KG_BT_PAIR_FIT](#evidence-kg_bt_pair_fit) | 补入具体做法 | [K05-05](K05_evaluation.md#k05-05) | 补入无惩罚、已定标的有限唯一解要求按正胜权重建成的有向图强连通，分开无跨组比较和单向跨组胜出。225的软胜权重、229的换位计分各留原义。 |
| <a id="gap-kg_pair_swiss_schedule"></a>累计分驱动的Swiss锦标赛排序 [KG_PAIR_SWISS_SCHEDULE](#evidence-kg_pair_swiss_schedule) | 补入具体做法 | [K05-06](K05_evaluation.md#k05-06) | 各轮按当前累计分匹配，再处理判胜、轮空、同分和终止；154跑五轮属具体赛程，和BT总体能力估计分开。 |
| <a id="gap-kg_elo_online"></a>逐场Elo技能更新 [KG_ELO_ONLINE](#evidence-kg_elo_online) | 补入具体做法 | [K05-06](K05_evaluation.md#k05-06) | 用赛前分同时求双方预期胜率再按K逐场更新；017的初值、K和赛程作为实例，不能将它当静态胜率转换。 |
| <a id="gap-kg_elo_rating"></a>Elo量尺的竞技评级与胜率换算 [KG_ELO_RATING](#evidence-kg_elo_rating) | 补入具体做法 | [K05-06](K05_evaluation.md#k05-06) | 给出约400分量尺及BT强度的换算；179未明逐场或批量估计，不能据Elo名称或BayesElo换算重建比赛程序。 |
| <a id="gap-worker_1_kg_ari"></a>机会校正的分区Rand一致需补知识 [worker_1_KG_ARI](#evidence-worker_1_kg_ari) | 补入具体做法 | [K05-07](K05_evaluation.md#k05-07) | 基于相同对象两分区的列联表计共同成对数和固定边际的机会期望。032的Leiden与196的已知分区是不同参照，ARI不是个体标签正确率。 |

## K06 认知模型、因果推断与符号方法

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_beta_conjugate"></a>Beta与二项观测的共轭更新 [KG_BETA_CONJUGATE](#evidence-kg_beta_conjugate) | 补入具体做法 | [K06-01](K06_cognitive_causal.md#k06-01) | 补明Beta先验密度与二项似然相乘时的两项幂次更新。085的文字与公式对θ类型不一致；θ的后验和下一次观测成功概率须分开。 |
| <a id="gap-kg_discounted_pseudocounts"></a>折扣伪计数与动态信念参照 [KG_DISCOUNTED_PSEUDOCOUNTS](#evidence-kg_discounted_pseudocounts) | 补入具体做法 | [K06-01](K06_cognitive_causal.md#k06-01) | 每步先按遗忘系数衰减两侧计数，随后将新事件加到对应一侧；按明确的更新时点归一化。085的拟合损失未给，曲线相近仅说明该参照能描述行为。 |
| <a id="gap-kg_bayes_linear_predict"></a>线性概率模型的先验到后验预测 [KG_BAYES_LINEAR_PREDICT](#evidence-kg_bayes_linear_predict) | 补入具体做法 | [K06-02](K06_cognitive_causal.md#k06-02) | 指定设计矩阵、系数先验与观测噪声，算出后验均值和协方差，再预测新点。135的oracle预先掌握生成机制，其结果须按额外信息解释。 |
| <a id="gap-kg_kalman_belief"></a>高斯Kalman信念递推 [KG_KALMAN_BELIEF](#evidence-kg_kalman_belief) | 补入具体做法 | [K06-02](K06_cognitive_causal.md#k06-02) | 给定所选臂的先验均值方差及噪声更新信念。035用均值差和标准差差构造解释量；135仅更新被选臂，初值与跨任务重置保留未知。 |
| <a id="gap-kg_finite_bayes_update"></a>有限假设或世界的似然加权更新 [KG_FINITE_BAYES_UPDATE](#evidence-kg_finite_bayes_update) | 补入具体做法 | [K06-03](K06_cognitive_causal.md#k06-03) | 有限假设上逐项乘先验与观测似然并归一，分母为0单列。162使用错配噪声；200用真值相容的0/1过滤，二者分开。 |
| <a id="gap-kg_posterior_transmission"></a>后验驱动的通信与代际数据传递 [KG_POSTERIOR_TRANSMISSION](#evidence-kg_posterior_transmission) | 补入具体做法 | [K06-03](K06_cognitive_causal.md#k06-03) | 补明162的代内复制、成功通信入缓冲、更新后生成跨代样本和先验重置。该后验复制发生在贝叶斯代理仿真，LLM实验传递的是生成示例。 |
| <a id="gap-kg_conditional_gibbs"></a>交替条件抽样与联合分布解释 [KG_CONDITIONAL_GIBBS](#evidence-kg_conditional_gibbs) | 补入具体做法 | [K06-03](K06_cognitive_causal.md#k06-03) | 以最新一句/语气交替生成后传给对侧。补明047人和GPT分开起链，禁止真人重返同链仅是招募安排。联合分布解释需条件相容与混合，90条链不证明收敛。 |
| <a id="gap-kg_cog_utility_softmax"></a>效用到随机选择的Luce/softmax行为模型需补知识 [KG_COG_UTILITY_SOFTMAX](#evidence-kg_cog_utility_softmax) | 补入具体做法 | [K06-04](K06_cognitive_causal.md#k06-04) | 固定选择集与效用尺度，以指数归一取得行动概率。026为说话者预期联合收益，187为物品可加效用，200的说者和听者可有不同敏感度。 |
| <a id="gap-kg_inverse_utility"></a>选择似然到效用后验及偏好预测 [KG_INVERSE_UTILITY](#evidence-kg_inverse_utility) | 补入具体做法 | [K06-04](K06_cognitive_causal.md#k06-04) | 将前向选择似然与效用先验相乘后归一。187既可读某物品的后验期望，也可读其为最佳的后验概率，未给的积分实现留空。 |
| <a id="gap-kg_pragmatic_posterior"></a>规范语用的动机及奖励后验 [KG_PRAGMATIC_POSTERIOR](#evidence-kg_pragmatic_posterior) | 补入具体做法 | [K06-04](K06_cognitive_causal.md#k06-04) | 先合并说听双方收益，得到说话者的话语似然，再乘奖励、动机先验并边缘化得到听者后验。026式子给比例，归一化常数与积分细节未报。 |
| <a id="gap-kg_cog_rw_fit"></a>RW预测误差更新与softmax选择似然拟合需补知识 [KG_COG_RW_FIT](#evidence-kg_cog_rw_fit) | 补入具体做法 | [K06-05](K06_cognitive_causal.md#k06-05) | 在每个试次以更新前的Q计算选择概率，再按奖励预测误差更新已选项；按观察选择的负对数似然拟合一组或两组学习率。003的正负学习差属于行为模型参数。 |
| <a id="gap-kg_cog_switch_identification"></a>切换选择不等式识别效用参数区间需补知识 [KG_COG_SWITCH_IDENTIFICATION](#evidence-kg_cog_switch_identification) | 补入具体做法 | [K06-05](K06_cognitive_causal.md#k06-05) | 补写跨系列先用切换不等式约束前一组参数，再在可行范围内求后续参数的条件范围。008取区间中点，空交集与多解要保留，不解释为抽样误差。 |
| <a id="gap-kg_cog_decision_model_comparison"></a>效用/概率权重及行为决策模型的拟合比较需补知识 [KG_COG_DECISION_MODEL_COMPARISON](#evidence-kg_cog_decision_model_comparison) | 补入具体做法 | [K06-05](K06_cognitive_causal.md#k06-05) | 同一组观察选择，按各理论的前向收益、概率权重、未选项或混合规则产生预测，在相同比较条件下算损失；008的参数化不移植到187。 |
| <a id="gap-kg_cog_bound_optimization"></a>L-BFGS-B行为参数拟合需补知识 [KG_COG_BOUND_OPTIMIZATION](#evidence-kg_cog_bound_optimization) | 补入具体做法 | [K06-06](K06_cognitive_causal.md#k06-06) | 定义损失、可行边界、初值、梯度和停止条件后运行L-BFGS-B，区分到达迭代上限和收敛。085实际优化初值与损失缺报。 |
| <a id="gap-kg_cog_level_mixture"></a>Poisson认知层级信念及logit混合预测需补知识 [KG_COG_LEVEL_MIXTURE](#evidence-kg_cog_level_mixture) | 补入具体做法 | [K06-06](K06_cognitive_causal.md#k06-06) | 对每个层级只归一较低层的对手权重，按该层精度求自身策略，再用总体Poisson权重混合。178的γ乘层数进入logit，保留截断尾质量。 |
| <a id="gap-kg_cog_count_mle"></a>认知选择模型的计数对数似然参数估计需补知识 [KG_COG_COUNT_MLE](#evidence-kg_cog_count_mle) | 补入具体做法 | [K06-06](K06_cognitive_causal.md#k06-06) | 以各条件实际行动次数作权，将理论行动概率取对数后求和最大化，联合估计层级混合参数。178的参数不直接等于模型可观察的思考层数。 |
| <a id="gap-kg_causal_identify"></a>图查询组合的因果可识别性判定 [KG_CAUSAL_IDENTIFY](#evidence-kg_causal_identify) | 补入具体做法 | [K06-07](K06_cognitive_causal.md#k06-07) | 先列图、查询与可用观测/干预分布，再查可识别性、定义域与平凡解。009借此筛除不合适的金标题，未把它当作模型在线工具。 |
| <a id="gap-kg_causal_do_engine"></a>干预查询的因果调整与do规则求解 [KG_CAUSAL_DO_ENGINE](#evidence-kg_causal_do_engine) | 补入具体做法 | [K06-07](K06_cognitive_causal.md#k06-07) | 按图检查后门阻断与正值性，合法时按调整集求和；无合适后门集再查其他识别途径。009的数据生成求解器与作答端分开。 |
| <a id="gap-worker_5_scm_generation_gap"></a>结构模型的事实与do干预参照生成：操作知识 [worker_5_SCM_GENERATION_gap](#evidence-worker_5_scm_generation_gap) | 补入具体做法 | [K06-08](K06_cognitive_causal.md#k06-08) | 指定外生联合分布与方程，按拓扑序生成事实；干预时只替换相应方程再往下生成。024使用已知逻辑模型作参照。 |
| <a id="gap-worker_5_counterfactual_aap_gap"></a>溯因—结构干预—反事实预测：操作知识 [worker_5_COUNTERFACTUAL_AAP_gap](#evidence-worker_5_counterfactual_aap_gap) | 补入具体做法 | [K06-08](K06_cognitive_causal.md#k06-08) | 对个体已见证据求外生状态后验，替换处理方程，再用同一后验生成结果。009反事实金标区别于重新从总体外生分布采样的干预边际。 |
| <a id="gap-kg_causal_pnps_estimate"></a>由观测及干预数据识别PN/PS [KG_CAUSAL_PNPS_ESTIMATE](#evidence-kg_causal_pnps_estimate) | 补入具体做法 | [K06-09](K06_cognitive_causal.md#k06-09) | 在单调性等识别条件和数据源可比时，用观测联合事件与干预结果频率构造PN或PS；分母须为正。024负估计可暴露误差或假设问题。 |
| <a id="gap-kg_causal_observable_proxy"></a>可观测替代跨世界反事实的效应近似操作与解释需补 [KG_CAUSAL_OBSERVABLE_PROXY](#evidence-kg_causal_observable_proxy) | 补全已有指导 | [K06-09](K06_cognitive_causal.md#k06-09) | 明确代理替代的是哪一个跨世界量，先算相对原答的改变，再解释分量之差。148的ADCE依赖代理可比性，合成例的趋势不能决定实际文本上的偏差方向。 |
| <a id="gap-kg_graph_er"></a>Erdos–Renyi概率图生成 [KG_GRAPH_ER](#evidence-kg_graph_er) | 补入具体做法 | [K06-10](K06_cognitive_causal.md#k06-10) | 按是否允许自环、方向与节点数确定候选边，每条边独立按p抽取。037每图再抽p，样本混合后图密度不同。 |
| <a id="gap-kg_graph_edge_product"></a>独立边概率的完整图似然 [KG_GRAPH_EDGE_PRODUCT](#evidence-kg_graph_edge_product) | 补入具体做法 | [K06-10](K06_cognitive_causal.md#k06-10) | 固定候选边全集，在条件独立假设下乘存在边p与所有缺失边1−p，log尺度可求和。037的概率图不据此变成具有边依赖的ERGM。 |
| <a id="gap-kg_graph_ergm"></a>ERGM指数族图概率与MAP拟合 [KG_GRAPH_ERGM](#evidence-kg_graph_ergm) | 补入具体做法 | [K06-10](K06_cognitive_causal.md#k06-10) | 图统计与参数点乘后取指数，用合法图空间的配分函数归一，加入参数先验求MAP。037未给从软概率图到拟合的完整转换。 |
| <a id="gap-kg_sdt_sensitivity_criterion"></a>等方差SDT辨别力和决策准则 [KG_SDT_SENSITIVITY_CRITERION](#evidence-kg_sdt_sensitivity_criterion) | 补全已有指导 | [K06-11](K06_cognitive_causal.md#k06-11) | 保留d′与c₀的正态轴及β换算；补入199逐block裁剪并取绝对值的实例，区分041的有符号阈值及其未报告的极端率处理。 |
| <a id="gap-kg_meta_sdt_probabilities"></a>MetaSDT条件置信概率矩阵 [KG_META_SDT_PROBABILITIES](#evidence-kg_meta_sdt_probabilities) | 补入具体做法 | [K06-11](K06_cognitive_causal.md#k06-11) | 分别在回答A/B的半轴内按置信阈值截区间，正态CDF差除以等真类下该回答的概率；逐行核对4×k概率和。 |
| <a id="gap-kg_meta_sdt_fit"></a>固定准则及单调正确率约束的MetaSDT拟合 [KG_META_SDT_FIT](#evidence-kg_meta_sdt_fit) | 补入具体做法 | [K06-11](K06_cognitive_causal.md#k06-11) | 固定响应准则、初始化辨别力并有序拟合阈值，强制模型的条件正确率随置信递增。041叙述的逼近目标与印刷argmax冲突，不能声称作者已经按改写求解。 |
| <a id="gap-worker_1_kg_shapley"></a>Shapley联盟边际贡献分配需补知识 [worker_1_KG_SHAPLEY](#evidence-worker_1_kg_shapley) | 补入具体做法 | [K06-12](K06_cognitive_causal.md#k06-12) | 先给每个联盟及空联盟的价值和缺席者规则，再按排列加权各成员的边际贡献。153使用近似价值时需另查效率误差。 |
| <a id="gap-worker_2_probability_logic_gap"></a>否定等价蕴含概率约束操作与解释 [worker_2_probability_logic_gap](#evidence-worker_2_probability_logic_gap) | 补入具体做法 | [K06-13](K06_cognitive_causal.md#k06-13) | 核对事件属于同一背景，再把否定映到互补、等价映到相等、蕴含映到单调不等式。150的相容性分数不检验事件最终是否发生。 |
| <a id="gap-worker_2_probability_joint_gap"></a>交并差事件概率界操作与解释 [worker_2_probability_joint_gap](#evidence-worker_2_probability_joint_gap) | 补入具体做法 | [K06-13](K06_cognitive_causal.md#k06-13) | 将交并概率送入包含排除式和Fréchet两端界；把并拆为互斥两部分时方可直接求和。150的不同检查可分别定位哪种关系失配。 |
| <a id="gap-worker_2_probability_conditional_gap"></a>条件链与全概率约束操作与解释 [worker_2_probability_conditional_gap](#evidence-worker_2_probability_conditional_gap) | 补入具体做法 | [K06-13](K06_cognitive_causal.md#k06-13) | 补齐三事件连乘第三项应条件于前两个事件的表达式；与二事件连乘和全概率互斥划分并用。150原文条件方向冲突不据此更改。 |
| <a id="gap-worker_3_kg_log_score_arbitrage"></a>一致结局下对数评分套利与概率修正操作知识 [worker_3_KG_LOG_SCORE_ARBITRAGE](#evidence-worker_3_kg_log_score_arbitrage) | 补入具体做法 | [K06-14](K06_cognitive_causal.md#k06-14) | 补充同义两事件等权log-odds平均的闭式、否定补概率和多个检查下权重更新；条件事件None按一致世界支付项处理。值与最优修正概率分开。 |
| <a id="gap-worker_4_gap_matrix_ode"></a>一致性check的矩阵逆微分方程数值求解操作支持 [worker_4_gap_matrix_ode](#evidence-worker_4_gap_matrix_ode) | 补入具体做法 | [K06-14](K06_cognitive_causal.md#k06-14) | 以可行世界和问题索引组成评分导数矩阵，从旧概率沿线性系统给出的导数积分，到奇异边界按事件停止。150未定义非方阵求逆和数值容差，须保留这些个案限制。 |
| <a id="gap-kg_logodds_convergence"></a>递归算子与对数几率收敛条件 [KG_LOGODDS_CONVERGENCE](#evidence-kg_logodds_convergence) | 补入具体做法 | [K06-14](K06_cognitive_causal.md#k06-14) | 在仿射递推固定点与斜率条件外，补明确定改写、点态有限log-odds和相邻平均收敛的前提。197实测有限轮表现，不能由其自动推出随机算子都收敛。 |
| <a id="gap-kg_spatial_relation_solving"></a>方向关系约束的编码、组合与解码 [KG_SPATIAL_RELATION_SOLVING](#evidence-kg_spatial_relation_solving) | 补入具体做法 | [K06-15](K06_cognitive_causal.md#k06-15) | 统一方向与坐标之后把明确的网格关系译成位移，经路径组合再解目标对象的相对方位；断开或多路径冲突另报。217坐标命名冲突不由工具代填。 |
| <a id="gap-worker_3_kg_relation_closure"></a>关系图对称逆向与传递闭包扩充操作知识 [worker_3_KG_RELATION_CLOSURE](#evidence-worker_3_kg_relation_closure) | 补入具体做法 | [K06-15](K06_cognitive_causal.md#k06-15) | 分别追踪真假三元组，以逆关系与非对称约束导出真边和负边，仅对指定关系作传递。093的人工图用于建立给模型答题评分的参照，未标注边保留未知。 |
| <a id="gap-worker_3_kg_weighted_maxsat"></a>WCNF硬软约束加权MaxSAT推断操作知识 [worker_3_KG_WEIGHTED_MAXSAT](#evidence-worker_3_kg_weighted_maxsat) | 补入具体做法 | [K06-15](K06_cognitive_causal.md#k06-15) | 按每张图把关系三元组变成布尔变量，关系规则作硬约束，置信作软权，求全局赋值；区分满足权重与RC2报告的未满足代价。 |
| <a id="gap-worker_2_concept_lattice_gap"></a>闭包形式概念格构造操作与解释 [worker_2_concept_lattice_gap](#evidence-worker_2_concept_lattice_gap) | 补入具体做法 | [K06-16](K06_cognitive_causal.md#k06-16) | 从对象-属性二值关系双向取共同属性与所有者，枚举并去重闭包对，再按extent包含连成偏序。136的阈值改变二值语境，可能随之改变概念格。 |
| <a id="gap-worker_3_kg_priority_qscfg"></a>带优先级准同步CFG解析执行操作知识 [worker_3_KG_PRIORITY_QSCFG](#evidence-worker_3_kg_priority_qscfg) | 补入具体做法 | [K06-16](K06_cognitive_causal.md#k06-16) | 把输入、输出两端的同索引非终结符绑定到同一子解析，按输出序列重组，冲突时取规则优先级。138的MiniSCAN解释器与ACRE集合判定分别处理。 |
| <a id="gap-worker_2_symbolic_material_gap"></a>符号关系驱动题目与唯一gold生成操作与解释 [worker_2_symbolic_material_gap](#evidence-worker_2_symbolic_material_gap) | 补入具体做法 | [K06-17](K06_cognitive_causal.md#k06-17) | 把实体、单位和关系建成有类型的单未知方程，按合法依赖顺序求值，检查查询唯一再填语言模板。160采用线性证明链，缺参或无定义运算要排除。 |
| <a id="gap-worker_3_kg_constraint_enumeration"></a>约束配置的穷举与解计数操作知识 [worker_3_KG_CONSTRAINT_ENUMERATION](#evidence-worker_3_kg_constraint_enumeration) | 补入具体做法 | [K06-17](K06_cognitive_causal.md#k06-17) | 枚举完整有限空间，再按任务约束筛选并用规范表示去重。241含旋转等价的情形，概率分母取决于原抽样空间与各等价类重数。 |
| <a id="gap-worker_3_kg_memoized_capacity_dp"></a>容量约束多重集分配的记忆化深度优先DP操作知识 [worker_3_KG_MEMOIZED_CAPACITY_DP](#evidence-worker_3_kg_memoized_capacity_dp) | 补入具体做法 | [K06-17](K06_cognitive_causal.md#k06-17) | 用元素类型索引和剩余容量作DP状态，枚举合法分配并递归计数，按终态约束给0/1。241排序可合并子问题，是否重计还取决于入路径重数。这是辅助计算足迹。 |
| <a id="gap-worker_2_roots_gap"></a>网格候选数值求根与切点补查操作与解释 [worker_2_roots_gap](#evidence-worker_2_roots_gap) | 补入具体做法 | [K06-18](K06_cognitive_causal.md#k06-18) | 对两曲线差先用网格查异号括区间，再查导数变号的切点候选，核残差与区间并按精度去重。241实际round两位，有限网格可能漏根。 |
| <a id="gap-worker_3_kg_propositional_soundness"></a>外显命题推理的逐步有效性审核操作知识 [worker_3_KG_PROPOSITIONAL_SOUNDNESS](#evidence-worker_3_kg_propositional_soundness) | 补全已有指导 | [K06-18](K06_cognitive_causal.md#k06-18) | 把推理化成前提、结论的布尔式，查是否存在使前提真而结论假的赋值；局部步和总体结论分别判读。051自然句与图注冲突时不能凭单一图签认定有效。 |
| <a id="gap-worker_5_csp_sufficiency_gap"></a>CSP可推导性与最小充分变量集合：操作知识 [worker_5_CSP_SUFFICIENCY_gap](#evidence-worker_5_csp_sufficiency_gap) | 补入具体做法 | [K06-19](K06_cognitive_causal.md#k06-19) | 在所有合法完整赋值上检查同一补充答案是否确定目标，再按最少变量数或包含极小给出充分集。016允许多个同样正确的单变量询问。 |
| <a id="gap-worker_5_csp_backward_gap"></a>正反目标反向搜索构造缺信息任务：操作知识 [worker_5_CSP_BACKWARD_gap](#evidence-worker_5_csp_backward_gap) | 补入具体做法 | [K06-19](K06_cognitive_causal.md#k06-19) | 从目标真与假分别反搜合法赋值，挑只差一个变量的兼容对，隐去该变量后再次求解，验证信息确实不足且补回充分。 |
| <a id="gap-worker_5_csp_depth_gap"></a>由蕴涵关系排除浅层充分变量：操作知识 [worker_5_CSP_DEPTH_gap](#evidence-worker_5_csp_depth_gap) | 补全已有指导 | [K06-19](K06_cognitive_causal.md#k06-19) | 识别能产生较浅解的其他变量并列为禁问，重新检查仍有达到目标深度的合法解。016用符号反搜深度定义题目条件。 |
| <a id="gap-worker_5_csp_parse_solve_gap"></a>解析并求解CSP验证候选答案：操作知识 [worker_5_CSP_PARSE_SOLVE_gap](#evidence-worker_5_csp_parse_solve_gap) | 补入具体做法 | [K06-19](K06_cognitive_causal.md#k06-19) | 先按指定变量域解析方程，再分别核查有解、目标答案正确与语义对应。016保留同题多个正确表达，无法解析与解析后答错分记。 |
| <a id="gap-worker_2_bfs_gap"></a>符号状态/依赖图的广度与反向搜索操作与解释 [worker_2_bfs_gap](#evidence-worker_2_bfs_gap) | 补入具体做法 | [K06-20](K06_cognitive_causal.md#k06-20) | 保留逐层展开、动作前提/效果、去重与最短步数；补写对部分初态的合法完整化分别求计划，以及016如何辨别是否仍须提问。204的图路径同样用单位边成本。 |
| <a id="gap-worker_2_tot_gap"></a>thought/action两级候选广度搜索操作与解释 [worker_2_tot_gap](#evidence-worker_2_tot_gap) | 补入具体做法 | [K06-20](K06_cognitive_causal.md#k06-20) | 先生成思考候选和投票，再生成行动、投票并执行合法转移，把候选状态接到下一层。017这套树展开与整题多次独立采样投票不同。 |
| <a id="gap-worker_4_gap_tot_transition"></a>ToT链状态展开与合法转移操作支持 [worker_4_gap_tot_transition](#evidence-worker_4_gap_tot_transition) | 补入具体做法 | [K06-20](K06_cognitive_causal.md#k06-20) | 在chain、target、unused状态转移上，补明217每步两次扩展须各自验证与当前对象真实可连接；无候选即失败，达到目标才解码链。 |
| <a id="gap-worker_4_gap_tot_beam_bfs"></a>ToT评分束宽约束的广度搜索操作支持 [worker_4_gap_tot_beam_bfs](#evidence-worker_4_gap_tot_beam_bfs) | 补入具体做法 | [K06-20](K06_cognitive_causal.md#k06-20) | 每一层先生成和评分再保留固定宽度前沿，达到目标或深度上限停。217的束宽3深度10和140的束宽10深度3是不同预算，剪枝后不保证全局最优。 |
| <a id="gap-worker_2_mcts_gap"></a>Monte Carlo Tree Search对手策略操作与解释 [worker_2_mcts_gap](#evidence-worker_2_mcts_gap) | 补入具体做法 | [K06-21](K06_cognitive_causal.md#k06-21) | 沿树策略选择、扩展、模拟，再将回报按一致的行动者视角回传更新次数与价值，预算耗尽后定根行动。017的模拟次数已报，探索常数与平局规则未知。 |
| <a id="gap-worker_4_gap_alternating_tree"></a>交替问题/答案的模拟树操作支持 [worker_4_gap_alternating_tree](#evidence-worker_4_gap_alternating_tree) | 补入具体做法 | [K06-22](K06_cognitive_causal.md#k06-22) | 节点带已有问答历史和可能集合；问题扩成多个候选，YES/NO分别更新互斥且完备的子集，再交替递归到固定深度。均匀先验才可用子集数目比估概率。 |
| <a id="gap-worker_4_gap_tree_reward"></a>模拟树累积奖励与向根价值传播操作支持 [worker_4_gap_tree_reward](#evidence-worker_4_gap_tree_reward) | 补入具体做法 | [K06-22](K06_cognitive_causal.md#k06-22) | 140中的累计奖励由根向下传，叶值初始化后在回答节点按概率、在问题节点按候选均值或特定变体的最大值回传。乘积路径准则保留其独立含义。 |
| <a id="gap-worker_4_gap_beam_decode"></a>确定性及多项式beam解码操作支持 [worker_4_gap_beam_decode](#evidence-worker_4_gap_beam_decode) | 补入具体做法 | [K06-23](K06_cognitive_causal.md#k06-23) | 同一前沿的多个前缀逐token扩展、累计分数并按长度及终止规则选择幸存者；区分确定性与随机束选取。191只对支持接口的模型比较。 |
| <a id="gap-worker_4_gap_residual_decode"></a>注意力奖励驱动的Residual Decoding操作支持 [worker_4_gap_residual_decode](#evidence-worker_4_gap_residual_decode) | 补入具体做法 | [K06-23](K06_cognitive_causal.md#k06-23) | 对每个top-n候选单独读取对问题和上下文的注意力，按logit加注意力比值项重排，再追加最佳token。061的第15层和权重是实例条件，零分母需说明。 |
| <a id="gap-worker_4_gap_graph_structure"></a>随机树比较图构造 [worker_4_gap_graph_structure](#evidence-worker_4_gap_graph_structure) | 补入具体做法 | [K06-24](K06_cognitive_causal.md#k06-24) | 构造随机树需满足n−1边、连通且无环；给定生成分布后赋方向关系，按可达性推导。204未说明使用均匀Prüfer生成，不能根据树约束倒推。 |
| <a id="gap-worker_4_gap_syllogism_dfs"></a>DFS有效三段论链与Hamiltonian前提路径操作支持 [worker_4_gap_syllogism_dfs](#evidence-worker_4_gap_syllogism_dfs) | 补入具体做法 | [K06-24](K06_cognitive_causal.md#k06-24) | 只以仍有有效结论的前提组合延长DFS，再在共享项连接图里求满足结论端点且每前提恰用一次的排列。204的有效性与语句顺序是两个条件。 |
| <a id="gap-worker_4_gap_cycle_reach"></a>以环和不可达性构造不一致/未知图题操作支持 [worker_4_gap_cycle_reach](#evidence-worker_4_gap_cycle_reach) | 补入具体做法 | [K06-24](K06_cognitive_causal.md#k06-24) | 插入能闭合有向环的边以构造矛盾。若查询两方向均无传递可达路径才判未知；未直接给边不足以判未知。 |
| <a id="gap-worker_4_gap_graph_iso"></a>节点重命名同构去重操作支持 [worker_4_gap_graph_iso](#evidence-worker_4_gap_graph_iso) | 补入具体做法 | [K06-25](K06_cognitive_causal.md#k06-25) | 用保持所有有向邻接的节点双射判同构，给等价类保存代表及重命名映射。232的图库去重不能仅比较度数序列。 |
| <a id="gap-worker_4_gap_dsep"></a>d-separation与MEC归并操作支持 [worker_4_gap_dsep](#evidence-worker_4_gap_dsep) | 补入具体做法 | [K06-25](K06_cognitive_causal.md#k06-25) | 沿无向路径检查非碰撞点的条件化和碰撞点或其后代的条件化，再核全路径是否阻断。232以图蕴含条件独立集合归类，不能用有限观测中的零相关直接替代。 |
| <a id="gap-worker_4_gap_mec_gold"></a>跨MEC图关系必然蕴含金标操作支持 [worker_4_gap_mec_gold](#evidence-worker_4_gap_mec_gold) | 补入具体做法 | [K06-25](K06_cognitive_causal.md#k06-25) | 在每个等价图分别检查直接边、排除直接边的祖先/后代及共同原因/结果，再跨全类量化。232的非必然蕴含包括部分图为真的情形，图例命名冲突留存。 |
| <a id="gap-kg_conditional_complexity"></a>条件渐近计算成本 [KG_CONDITIONAL_COMPLEXITY](#evidence-kg_conditional_complexity) | 补入具体做法 | [K06-26](K06_cognitive_causal.md#k06-26) | 分别计状态数、分支、深度和单步成本，分块还要计块内工作与边界，再注明简化的参数条件。016是树深成本，177的条件线性也不是硬件耗时。 |
| <a id="gap-kg_truncated_attention_bound"></a>截断注意力的质量保留与近似条件 [KG_TRUNCATED_ATTENTION_BOUND](#evidence-kg_truncated_attention_bound) | 补入具体做法 | [K06-26](K06_cognitive_causal.md#k06-26) | 计算保留注意力质量及重归一；有界value向量且丢弃质量ε<1时可用2Mε界定输出差。177用近邻选择不能保证任一输入都捕获足够质量。 |
| <a id="gap-kg_stochastic_recurrence_analysis"></a>随机递推的误差累积与极限核查 [KG_STOCHASTIC_RECURRENCE_ANALYSIS](#evidence-kg_stochastic_recurrence_analysis) | 补入具体做法 | [K06-27](K06_cognitive_causal.md#k06-27) | 独立系数与零均值噪声下推导二阶矩递推，比较起始误差与稳态。216原文提出的U形和唯一停止点不由常系数解自动推出。 |
| <a id="gap-kg_linear_attention_formal"></a>注意力矩阵计算与指定输出读取 [KG_LINEAR_ATTENTION_FORMAL](#evidence-kg_linear_attention_formal) | 补入具体做法 | [K06-28](K06_cognitive_causal.md#k06-28) | 把已标记示例和标签为零的查询列组成输入，核矩阵维度、缩放及残差，读取右下元素。233的定义仅用于指定形式模型。 |
| <a id="gap-kg_rank_weighted_optimum"></a>秩约束加权谱逼近 [KG_RANK_WEIGHTED_OPTIMUM](#evidence-kg_rank_weighted_optimum) | 补入具体做法 | [K06-28](K06_cognitive_causal.md#k06-28) | 在指定高斯任务与秩约束下将总体风险配方为加权Frobenius目标，求前r个经权重缩放的谱方向。233给解析解，未给实际训练必达此解的证明。 |
| <a id="gap-kg_gaussian_risk_decomposition"></a>高斯矩的期望风险分解 [KG_GAUSSIAN_RISK_DECOMPOSITION](#evidence-kg_gaussian_risk_decomposition) | 补入具体做法 | [K06-28](K06_cognitive_causal.md#k06-28) | 用高斯四阶矩及独立零均值标签噪声分解有限样本、遗漏信号、收缩风险；只有小秩已含全部有用信号时，增秩才仅引入额外噪声。233的M与N可不同。 |
| <a id="gap-kg_nonlinear_population_objective"></a>多头非线性前向与正则总体目标 [KG_NONLINEAR_POPULATION_OBJECTIVE](#evidence-kg_nonlinear_population_objective) | 补入具体做法 | [K06-29](K06_cognitive_causal.md#k06-29) | 明确各头的ReLU响应、带符号组合、hinge总体损失及矩阵范数正则，以大N和小正则的条件解释解。233形式目标与经验任务准确率分别读。 |
| <a id="gap-kg_combinatorial_representation"></a>模式覆盖的表征构造与下界 [KG_COMBINATORIAL_REPRESENTATION](#evidence-kg_combinatorial_representation) | 补入具体做法 | [K06-29](K06_cognitive_causal.md#k06-29) | 用二进制位构造对角矩阵及相反配对，正负模式覆盖给出限定任务分布下的头数下界。233小模型与大模型即使覆盖嵌套，尺度参数仍会变化。 |
| <a id="gap-kg_concentration_projection"></a>集中界与投影噪声能量 [KG_CONCENTRATION_PROJECTION](#evidence-kg_concentration_projection) | 补入具体做法 | [K06-29](K06_cognitive_causal.md#k06-29) | 由样本集中界得带失败概率δ的余项，将噪声投影到给定子空间，以协方差的迹计算期望能量。233的能量比不同于准确率比，δ也不是实测p值。 |
| <a id="gap-worker_2_nback_generation_gap"></a>受目标比例约束的n-back序列生成操作与解释 [worker_2_nback_generation_gap](#evidence-worker_2_nback_generation_gap) | 引用已有附录 | [K06-30](K06_cognitive_causal.md#k06-30) | 原构念任务附录H.3.6.2（n-back行）已明确当前刺激与n步前是否相同并要求报告目标比例。K06-30为查阅入口。199用的warm-up、非目标生成与随机设置按论文记录，不能由定义反推。 |

## K07 动态状态、记忆与外部执行

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_program_execution_bridge"></a>生成程序或规则的执行输入与结果回收 [KG_PROGRAM_EXECUTION_BRIDGE](#evidence-kg_program_execution_bridge) | 补入具体做法 | [K07-01](K07_state_execution.md#k07-01) | 将生成片段与输入、运行器、实际输出/异常及测试关联；030仅允许辅助运行不能推全样本执行。057数值核对、151全测试通过、164属性组合返回值的后续判据不同。 |
| <a id="gap-kg_environment_action_bridge"></a>行动到环境步进及观测反馈 [KG_ENVIRONMENT_ACTION_BRIDGE](#evidence-kg_environment_action_bridge) | 补入具体做法 | [K07-02](K07_state_execution.md#k07-02) | 对194的文本动作先解析、查合法性再由环境步进，区分非法、截断和终局；环境回报与子目标评分的权重单独记录。 |
| <a id="gap-kg_flow_environment"></a>行为驱动状态、奖励与观测更新 [KG_FLOW_ENVIRONMENT](#evidence-kg_flow_environment) | 补入具体做法 | [K07-02](K07_state_execution.md#k07-02) | 补明同时行动须使用共同轮初状态，收齐才更新；128的私密提交和公开讨论、119的新增库存、003的实际奖励依各自协议进入下一步。 |
| <a id="gap-kg_flow_private_channels"></a>分角色分阶段私密/公开消息路由 [KG_FLOW_PRIVATE_CHANNELS](#evidence-kg_flow_private_channels) | 补全已有指导 | [K07-03](K07_state_execution.md#k07-03) | 按角色与阶段记录可读私密字段、公开转发内容和历史。005的笔记可见范围与012的逐跳转述分别处理，终止语不代表成交。 |
| <a id="gap-kg_flow_group_aggregation"></a>成员讨论到群组行动和共同反馈 [KG_FLOW_GROUP_AGGREGATION](#evidence-kg_flow_group_aggregation) | 补全已有指导 | [K07-03](K07_state_execution.md#k07-03) | 记录成员的发言、共同投票及反馈文本的形成顺序。010的群体评论会改动后续环境，统计单位不能按独立意见处理。 |
| <a id="gap-kg_search_evidence_bridge"></a>查询到检索证据及模型输入的衔接 [KG_SEARCH_EVIDENCE_BRIDGE](#evidence-kg_search_evidence_bridge) | 补入具体做法 | [K07-04](K07_state_execution.md#k07-04) | 从查询、返回、筛选一直记录到模型实际看见的材料；042正文清洗、154查询结果列表和235摘要/商业系统回答的可核查性不同。 |
| <a id="gap-kg_memory_function_io"></a>外部记忆函数的查询更新与回填 [KG_MEMORY_FUNCTION_IO](#evidence-kg_memory_function_io) | 补入具体做法 | [K07-05](K07_state_execution.md#k07-05) | 把读写调用与具体存储、回传结果和当轮上下文连接；242的主动检索、默认可见核心记忆与被动检索须分别记录。 |
| <a id="gap-kg_flow_memory_summary"></a>轨迹摘要作为后续记忆的更新 [KG_FLOW_MEMORY_SUMMARY](#evidence-kg_flow_memory_summary) | 补全已有指导 | [K07-05](K07_state_execution.md#k07-05) | 将摘要写入时点、源轨迹、后续读入及更新保存；010经营摘要的选择与来源保留，未说明的检索器设置不可代填。 |
| <a id="gap-kg_flow_negotiated_settlement"></a>贡献估计驱动协商与事后结算 [KG_FLOW_NEGOTIATED_SETTLEMENT](#evidence-kg_flow_negotiated_settlement) | 补全已有指导 | [K07-06](K07_state_execution.md#k07-06) | 补明按最后共同接受的提案结算，区分发言、接受、实际到账及无协议分支。153的Shapley贡献是议价输入，不保证等于最终分配。 |
| <a id="gap-kg_flow_adaptive_match"></a>重估强度后的最近未赛对手调度 [KG_FLOW_ADAPTIVE_MATCH](#evidence-kg_flow_adaptive_match) | 补入具体做法 | [K07-07](K07_state_execution.md#k07-07) | 各轮先用当时的结果拟合BT，保留已赛集合，再选最近未赛对手。225的随机首场和后续更新不能用最终静态分数替代。 |
| <a id="gap-worker_2_kv_partition_gap"></a>KV分区与检索token位置编码、softmax注意力衔接的执行步骤 [worker_2_kv_partition_gap](#evidence-worker_2_kv_partition_gap) | 补入具体做法 | [K07-08](K07_state_execution.md#k07-08) | 177的sink、局部窗口和移出事件分别记录原位置与逐层KV，检索后按规定位置编码接回attention。 |
| <a id="gap-worker_2_layer_event_queue_gap"></a>逐层检索邻近事件队列的去重/移出、token预算填充与注意力接口 [worker_2_layer_event_queue_gap](#evidence-worker_2_layer_event_queue_gap) | 补入具体做法 | [K07-08](K07_state_execution.md#k07-08) | 逐层维护事件及邻居队列、去重移出，并以token预算划分配额。177的±1是具体配置，不能把一层结果当全层共用。 |
| <a id="gap-worker_2_kv_offload_gap"></a>LRU槽位复用、GPU/CPU/磁盘迁移与跨设备层执行的协调 [worker_2_kv_offload_gap](#evidence-worker_2_kv_offload_gap) | 补入具体做法 | [K07-09](K07_state_execution.md#k07-09) | 缓存槽与设备、事件和层相绑定，LRU迁移后等数据可用再复用；177的GPU/CPU/磁盘搬运与改变窗口长度属于不同操作。 |
| <a id="gap-worker_2_event_scheduler_gap"></a>兼容约束的yield/wait/callback调度操作与解释 [worker_2_event_scheduler_gap](#evidence-worker_2_event_scheduler_gap) | 补入具体做法 | [K07-10](K07_state_execution.md#k07-10) | 记录等待条件、恢复优先、回调注册/清理及填充token。242的隔离条件仍可能靠filler触发回调，不能推定无干扰。 |
| <a id="gap-worker_2_virtual_clock_gap"></a>本地虚拟时钟与真实等待桥接操作与解释 [worker_2_virtual_clock_gap](#evidence-worker_2_virtual_clock_gap) | 补入具体做法 | [K07-10](K07_state_execution.md#k07-10) | 区分进程可见的虚拟时间与外部真实等待；242仅对兼容的同机时钟推进，记录时戳和到期事件。 |

## K08 模型内部测量与临时干预

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_input_gradient"></a>输入乘梯度归因的目标与读出 [KG_INPUT_GRADIENT](#evidence-kg_input_gradient) | 补入具体做法 | [K08-02](K08_internal_methods.md#k08-02) | 固定标量目标，对可微嵌入求梯度，逐坐标与输入相乘，按声明方式归约。第157篇对前提按词元数平均；其确切目标和符号处理未报告，不能从注意权重反推。 |
| <a id="gap-kg_integrated_gradients"></a>参考路径上的积分梯度归因 [KG_INTEGRATED_GRADIENTS](#evidence-kg_integrated_gradients) | 补入具体做法 | [K08-02](K08_internal_methods.md#k08-02) | 把参考、积分路径、目标和聚合绑定到实际张量。第061篇对内部量作20步近似，推理和作答阶段目标不同。第236篇以KL作电路归因；新稿区分两种用法，并保留后者参照与步数未知。 |
| <a id="gap-kg_conditional_gradient"></a>条件输出概率的输入梯度方向 [KG_CONDITIONAL_GRADIENT](#evidence-kg_conditional_gradient) | 补入具体做法 | [K08-02](K08_internal_methods.md#k08-02) | 对同一给定输出的条件对数概率，求其关于输入嵌入的梯度，跨通用提示平均。第192篇以此构造方向；原文对取哪个位置的描述不一致，不能登记为已经做了方向注入。 |
| <a id="gap-kg_checkpoint_influence"></a>训练与测试loss梯度的跨快照影响近似 [KG_CHECKPOINT_INFLUENCE](#evidence-kg_checkpoint_influence) | 补入具体做法 | [K08-03](K08_internal_methods.md#k08-03) | 在各既有检查点用同一目标词序列，计算文档前缀与测试上下文参数梯度的内积，再跨检查点和配对汇总。第223篇只抽取部分文档，影响近似不能替代删除文档后的重训比较。 |
| <a id="gap-kg_gradient_discrete_input"></a>梯度引导离散输入候选搜索 [KG_GRADIENT_DISCRETE_INPUT](#evidence-kg_gradient_discrete_input) | 补入具体做法 | [K08-04](K08_internal_methods.md#k08-04) | 第161篇用各模型嵌入梯度提出单词元改动，再解码为共同字符串、用各模型自己的分词器重算联合目标并选优。记录初始化与停止条件，跨模型不强制词元数相同。 |
| <a id="gap-kg_deletion_representation_sensitivity"></a>输入删除的内部敏感性测量 [KG_DELETION_REPRESENTATION_SENSITIVITY](#evidence-kg_deletion_representation_sensitivity) | 补入具体做法 | [K08-04](K08_internal_methods.md#k08-04) | 第161篇逐一删除词元，分别取原序列和删后序列的末层末位置表征，以L2距离表示敏感程度。保留长度与末位置可能改变的限制；两种相对归一描述分别列明。 |
| <a id="gap-kg_internal_vocab_readout"></a>内部向量到词表的读出接口及解释 [KG_INTERNAL_VOCAB_READOUT](#evidence-kg_internal_vocab_readout) | 补入具体做法 | [K08-05](K08_internal_methods.md#k08-05) | 对六篇读出实例区分残差、FFN增量、head输出与神经元value，并分开输出词表解码和输入词身份匹配。补上095的首词元对数概率、234的第一名复制检验、169的整词检索各应保存什么。 |
| <a id="gap-kg_rep_tensor_access"></a>内部张量的测量位置与对齐 [KG_REP_TENSOR_ACCESS](#evidence-kg_rep_tensor_access) | 补入具体做法 | [K08-01](K08_internal_methods.md#k08-01) | 明确层、张量、位置、运行阶段与轴，补入从回答词query行取输入key列的办法，以及052的FFN正值频率与157正值计数的分母差异。同一读接口可接不同指标，不能默认沿相同方向汇总。 |
| <a id="gap-kg_rep_contrast_direction"></a>对比残差方向的构造与含义 [KG_REP_CONTRAST_DIRECTION](#evidence-kg_rep_contrast_direction) | 补入具体做法 | [K08-06](K08_internal_methods.md#k08-06) | 按层与词元角色配对取残差差，再按研究指定的样本集合平均。第139篇用归一后的自身减他人方向，第143篇估计实体或属性的位置差；两篇的尺度和后续干预另记。 |
| <a id="gap-kg_local_brain_rsa"></a>局部/ROI脑表征的相似结构对照 [KG_LOCAL_BRAIN_RSA](#evidence-kg_local_brain_rsa) | 补入具体做法 | [K08-07](K08_internal_methods.md#k08-07) | 补入现成脑数据作为模型对照量时，成对重排刺激索引、比哪两项相似度的操作。第121篇局部球与区域低维表示是不同来源；限于对齐和读取，采用现成参照即可使用。 |
| <a id="gap-kg_key_adjacency_graph"></a>内部key到token关系图 [KG_KEY_ADJACENCY_GRAPH](#evidence-kg_key_adjacency_graph) | 补入具体做法 | [K08-07](K08_internal_methods.md#k08-07) | 第177篇以同一局部窗口内指定head的key点积构成token带权图，把事件作为社区考察。保留点积尺度，负权、自环与社区优化须另行说明，不能由原attention矩阵替代。 |
| <a id="gap-kg_embedding_soft_input"></a>嵌入层访问与soft输入接口 [KG_EMBEDDING_SOFT_INPUT](#evidence-kg_embedding_soft_input) | 补入具体做法 | [K08-06](K08_internal_methods.md#k08-06) | 第195篇用开放的嵌入输入接口，把预先指定的扰动作用到前缀嵌入后继续前向；保留位置与掩码衔接。原文两种噪声支持范围的表述不一致，不从接口推定其实际分布。 |
| <a id="gap-kg_fixed_representation_projection"></a>固定方向的跨位置/跨层投影解释 [KG_FIXED_REPRESENTATION_PROJECTION](#evidence-kg_fixed_representation_projection) | 补入具体做法 | [K08-06](K08_internal_methods.md#k08-06) | 补入205按句内词元平均后投既有轴及固定目标层轴观察跨层读数、234用最终分量矩阵读早期检查点的区分。139从对比方向移除表面偏好投影属于固定坐标处理；三例均不要求本步骤更新权重。 |
| <a id="gap-kg_write_read_composition"></a>矩阵写读空间的composition含义 [KG_WRITE_READ_COMPOSITION](#evidence-kg_write_read_composition) | 补入具体做法 | [K08-08](K08_internal_methods.md#k08-08) | 第234篇按数据流把前head的OV矩阵与后head的Q、K或V读矩阵配对，用乘积Frobenius范数除以两个范数的乘积。可另对指定秩一分量重算；静态通信分数不等于实测因果贡献。 |
| <a id="gap-kg_existing_sae_encoding"></a>现成SAE的表示转换接口 [KG_EXISTING_SAE_ENCODING](#evidence-kg_existing_sae_encoding) | 补入具体做法 | [K08-08](K08_internal_methods.md#k08-08) | 第235篇将既有模型的dense表示交给现成SAE，取稀疏特征后另拟合预测回归。先核对模型、层和预处理的兼容性；原文没有给足的池化和层细节记作未知，不能写成重新训练了SAE。 |
| <a id="gap-kg_act_runtime_tensor_edit"></a>定位运行时张量并替换、扰动或移除指定信号 [KG_ACT_RUNTIME_TENSOR_EDIT](#evidence-kg_act_runtime_tensor_edit) | 补入具体做法 | [K08-09](K08_internal_methods.md#k08-09) | 对21个需求共用的运行时干预补入三次前向、三项指标和跨提示的token角色对齐。第060篇逐点恢复；143有下游钳制；169使用跨提示写回。掩码后重归一、已归一权重替换和残差/特征置零仍分别记录。 |
| <a id="gap-kg_act_directional_derivative"></a>沿内部召回梯度施加瞬时扰动并求输出方向导数 [KG_ACT_DIRECTIONAL_DERIVATIVE](#evidence-kg_act_directional_derivative) | 补入具体做法 | [K08-10](K08_internal_methods.md#k08-10) | 定义两个标量目标，在起点固定第一个的梯度方向，对第二个目标求沿该方向在零点的导数。第095篇D008支持该干预，D013仅支持共同答对子集上更换读出指标，不能充当第二个干预实例。 |
| <a id="gap-kg_act_pseudoinverse_suppression"></a>由输出矩阵伪逆回映射并抑制语义相关输出 [KG_ACT_PSEUDOINVERSE_SUPPRESSION](#evidence-kg_act_pseudoinverse_suppression) | 补入具体做法 | [K08-10](K08_internal_methods.md#k08-10) | 第134篇在词表与隐空间之间用伪逆取最小二乘表示并回投，保留线性映射和概率的区别。正文给出在logits中修正再归一的可用选择；原研究的采样桥接与下标含义仍未知。 |
| <a id="gap-kg_act_rope_position"></a>修改逐层RoPE旋转以干预表观位置 [KG_ACT_ROPE_POSITION](#evidence-kg_act_rope_position) | 补入具体做法 | [K08-11](K08_internal_methods.md#k08-11) | 第143篇保持真实词元序列，逐位置改变指定旋转以扫描实体或属性的表观位置，再相对未移动对照读数。清楚记录作用在Q/K的哪一步以及缓存一致性，不能用重排文本代替此操作。 |
| <a id="gap-kg_rep_manual_circuit_trace"></a>从输出向输入人工选择归因路径以重建内部电路 [KG_REP_MANUAL_CIRCUIT_TRACE](#evidence-kg_rep_manual_circuit_trace) | 补入具体做法 | [K08-12](K08_internal_methods.md#k08-12) | 第236篇从目标输出反推，逐步人工选择Q/K/V归因分支。记录入选和未展开分支、所用归因与干预，再标示图上显示的主干；路径图不能推断所有未入选连接都不参与。 |
| <a id="gap-worker_3_kg_tied_softmax_attention"></a>绑定嵌入的单层softmax注意力前向操作知识 [worker_3_KG_TIED_SOFTMAX_ATTENTION](#evidence-worker_3_kg_tied_softmax_attention) | 补入具体做法 | [K08-13](K08_internal_methods.md#k08-13) | 按第141篇第4.2节核对列softmax、键维缩放、值变换、嵌入转置绑定读出和末位logits。纠正暗示原文默认使用因果mask的问题；需要概率时再沿类别轴归一。 |
| <a id="gap-worker_5_wanda_importance_gap"></a>权重幅值与激活范数联合重要性：操作知识 [worker_5_WANDA_IMPORTANCE_gap](#evidence-worker_5_wanda_importance_gap) | 补入具体做法 | [K08-14](K08_internal_methods.md#k08-14) | 从删去单条连接的输出变化推出连接权重绝对值乘输入特征激活范数，区分逐输入列广播与全部特征共享一值。第075篇的公式和文字维度表述不清；记录为重要性测量，不据目标函数推断作者实际剪枝。 |

## K09 材料构造、图结构与表征几何

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-kg_normal_mixture_generation"></a>正态与混合正态材料的生成规则 [KG_NORMAL_MIXTURE_GENERATION](#evidence-kg_normal_mixture_generation) | 补入具体做法 | [K09-01](K09_structure_geometry.md#k09-01) | 先按权重抽分量再按该分量的均值、标准差取样，混合方差还受峰间差异影响。029/D002用生成材料测模型对新概念的取样；双峰权重、截断和逐次重采样均未报告。 |
| <a id="gap-worker_5_gaussian_task_gap"></a>协方差Gaussian随机线性任务与标签噪声生成：操作知识 [worker_5_GAUSSIAN_TASK_gap](#evidence-worker_5_gaussian_task_gap) | 补入具体做法 | [K09-01](K09_structure_geometry.md#k09-01) | 补明233/D002在理论预训练分布中为每任务独立抽一次标准正态权重，并在整个prompt共享；特征按给定协方差抽取。评价另给定权重结构，仅为context标签加入独立噪声，query真值不加。 |
| <a id="gap-worker_5_parity_task_gap"></a>dictionary下重要任务混合与相关sparse parity生成：操作知识 [worker_5_PARITY_TASK_gap](#evidence-worker_5_parity_task_gap) | 补入具体做法 | [K09-01](K09_structure_geometry.md#k09-01) | 将233/D008的任务生成拆成按1−p_T或p_T选集合和集合内均匀选异坐标两步。保留任务维γ偏置的联合分布、正交字典映射和乘积标签；论文并未报告用这个理论生成器训练经验部分的LLM。 |
| <a id="gap-worker_5_population_risk_gap"></a>平方损失经验风险与总体风险定义：操作知识 [worker_5_POPULATION_RISK_gap](#evidence-worker_5_population_risk_gap) | 补入具体做法 | [K09-01](K09_structure_geometry.md#k09-01) | 233/D004在回归预训练定义中将B个独立prompt的平方误差和除以2B，再对任务、上下文和查询取期望。补明评价另加的context标签噪声只进相应评价期望，不能混入原预训练风险。 |
| <a id="gap-kg_kmeans_grouping"></a>K-means表征分组与中心解释 [KG_KMEANS_GROUPING](#evidence-kg_kmeans_grouping) | 补入具体做法 | [K09-02](K09_structure_geometry.md#k09-02) | 保留分配最近均值中心与更新中心的交替操作，补清161从中心选最近原例、110中心选帖的具体映射未报、210六维偏好聚类只需返回语言的分组。048按话题组织问题材料，四种输出用途分别保留。 |
| <a id="gap-kg_cluster_order_diagnostics"></a>聚类数的目标曲线诊断与选择 [KG_CLUSTER_ORDER_DIAGNOSTICS](#evidence-kg_cluster_order_diagnostics) | 补入具体做法 | [K09-02](K09_structure_geometry.md#k09-02) | 逐k比较inertia。第210篇按新增簇带来的收益递减选4；补清048从3到20扫描、按自定先降后升规则取转折，若未转折取20。局部求解可使观察值偏离全局最优曲线，未据此替作者解释。 |
| <a id="gap-kg_kmedoids_selection"></a>以真实候选为中心的K-Medoids选择 [KG_KMEDOIDS_SELECTION](#evidence-kg_kmedoids_selection) | 补入具体做法 | [K09-02](K09_structure_geometry.md#k09-02) | 076/D012把候选答案按语义距离分组，每组的medoid是真实候选；用使组内距离和较小的候选取代均值中心。本例k=3，少于3个候选时的处理及语义度量不详。 |
| <a id="gap-worker_1_kg_silhouette"></a>簇内与最近异簇距离轮廓评价需补知识 [worker_1_KG_SILHOUETTE](#evidence-worker_1_kg_silhouette) | 补入具体做法 | [K09-03](K09_structure_geometry.md#k09-03) | 逐点比较同簇平均距离和最近他簇平均距离并归一，补准确的标签数界2≤k≤n−1。129/D019只报告名称及数值，分组过程不详；较低轮廓值不足以确证材料多样性。 |
| <a id="gap-kg_topic_discovery"></a>语料主题发现与主题表征 [KG_TOPIC_DISCOVERY](#evidence-kg_topic_discovery) | 补入具体做法 | [K09-04](K09_structure_geometry.md#k09-04) | 179/D039以BERTopic在简介、用户名与推文中发现主题，再让GPT给主题命名、按主题看胜率。正文提供表征、分组、提取主题词到命名的关系，常见模块不认作该篇给定配置。 |
| <a id="gap-kg_topic_lda"></a>LDA文档主题概率表示 [KG_TOPIC_LDA](#evidence-kg_topic_lda) | 补入具体做法 | [K09-04](K09_structure_geometry.md#k09-04) | 由文档和主题层的Dirichlet分布生成词，再对语料推断文档主题向量。067设7主题；110对一万帖拟合200主题，再把推断向量交给聚类。二者语料预处理和具体拟合细节均不补猜。 |
| <a id="gap-kg_integer_selection"></a>整数变量、联合约束与全局材料子集选择 [KG_INTEGER_SELECTION](#evidence-kg_integer_selection) | 补入具体做法 | [K09-05](K09_structure_geometry.md#k09-05) | 166/D010一次按两个模型的中位概率限制和相反排名选自然句，另一次从100个三元组选10个最大化总争议。正文说明双模型分别满足的十分位配额怎样耦合到同一组选中变量。 |
| <a id="gap-worker_5_capacity_cluster_gap"></a>容量约束的最小费用流聚类分配：操作知识 [worker_5_CAPACITY_CLUSTER_gap](#evidence-worker_5_capacity_cluster_gap) | 补入具体做法 | [K09-05](K09_structure_geometry.md#k09-05) | 建词到簇的有费用容量边，每词送1单位流，16词分到4簇且每簇接收4单位；据此解固定中心的最小费用分配。196/D006未报具体距离/中心实现，普通四簇输出不保证容量。 |
| <a id="gap-kg_discrete_hillclimb"></a>离散可行邻域、局部下降与停机规则 [KG_DISCRETE_HILLCLIMB](#evidence-kg_discrete_hillclimb) | 补入具体做法 | [K09-06](K09_structure_geometry.md#k09-06) | 166/D012访问合法位置并更新满足约束、降低目标的词，均衡访问8个位置、连续8次未改善才停。终止相对于所选起点和邻域，无需推断全局最优或训练模型权重。 |
| <a id="gap-worker_4_gap_greedy_maxcover"></a>贪心最大覆盖文档选择操作支持 [worker_4_gap_greedy_maxcover](#evidence-worker_4_gap_greedy_maxcover) | 补入具体做法 | [K09-06](K09_structure_geometry.md#k09-06) | 127/D016每次优先选能增加最多尚未覆盖n-gram的文档，更新并集后再选下一个。重叠匹配只贡献一次增量；该篇并列选择规则未报。 |
| <a id="gap-kg_dsl_ast_template"></a>DSL解析对象图并生成程序签名模板需补知识 [KG_DSL_AST_TEMPLATE](#evidence-kg_dsl_ast_template) | 补入具体做法 | [K09-07](K09_structure_geometry.md#k09-07) | 164/D004将允许的类型和字段解析成对象/语法树，再构造类、参数和中性文档字符串供模型补全。这里生成的是题材代码，不表示被测模型遵守输出文法或所生成程序经过测试。 |
| <a id="gap-kg_template_predicate_binding"></a>受控句式模板的对象绑定与关系谓词转换需补知识 [KG_TEMPLATE_PREDICATE_BINDING](#evidence-kg_template_predicate_binding) | 补入具体做法 | [K09-07](K09_structure_geometry.md#k09-07) | 为有方向的实体对绑定两个槽位和关系，将问题也转为谓词。补清217/D005模板匹配属于纯规则Map+ASP参照，另一条路线由语言模型抽取再接同一ASP；模型解析错误不能归给基线。 |
| <a id="gap-worker_1_kg_symbolic_composition"></a>受约束随机符号函数嵌套需补知识 [worker_1_KG_SYMBOLIC_COMPOSITION](#evidence-worker_1_kg_symbolic_composition) | 补入具体做法 | [K09-07](K09_structure_geometry.md#k09-07) | 241/D009让表达式与可调用函数按同序嵌套，检查定义域和候选函数区别，有限次重试找含交点的题。后续数值求根另见K06第18节；发布代码与论文每题的版本对应未知。 |
| <a id="gap-kg_dr_mds"></a>MDS相似/距离到低维布局 [KG_DR_MDS](#evidence-kg_dr_mds) | 补入具体做法 | [K09-08](K09_structure_geometry.md#k09-08) | 明确经典MDS中不相似度逐元素平方、双中心化和按正特征值平方根取坐标，保留metric与nonmetric拟合的区别。001的17例、047的人机80点、222的19价值各有自己的矩阵；121只用MDS初始化t-SNE，未统一指定距离桥。 |
| <a id="gap-kg_dr_tsne"></a>t-SNE邻域概率嵌入 [KG_DR_TSNE](#evidence-kg_dr_tsne) | 补入具体做法 | [K09-09](K09_structure_geometry.md#k09-09) | 根据高维邻域概率与低维Student-t相似度拟合，图距不代替原空间计分。补196以降维预处理聚类与绘图两种用途、220等级着色未检验分类。025、075、121、129、136、237的图层、子集或初始化各有边界，不能借图推总体准确率。 |
| <a id="gap-kg_dr_umap"></a>UMAP邻域结构嵌入 [KG_DR_UMAP](#evidence-kg_dr_umap) | 补入具体做法 | [K09-09](K09_structure_geometry.md#k09-09) | 从指定距离和邻居数构造局部关系再拟合低维坐标。003的人机定量距离出自原空间，047的句子/语气共同投影辅助解释，171报告17主题的UMAP图、未报告据此发现主题的具体模型。 |
| <a id="gap-kg_dr_pca"></a>PCA主轴投影与方差保留 [KG_DR_PCA](#evidence-kg_dr_pca) | 补入具体做法 | [K09-10](K09_structure_geometry.md#k09-10) | 按拟合材料中心化、取协方差主轴、投影并计算累计解释方差，新样本复用同一变换。237/D023在外部文本拟合10维后转换生成嵌入（计算det另见第13节）；220用第一主成分定义方向但符号/池化不明。003阈值叙述与比例冲突，104/129/137/196/234的分析或绘图区别于预测器训练。 |
| <a id="gap-kg_dr_svd"></a>SVD谱分解与截断重建 [KG_DR_SVD](#evidence-kg_dr_svd) | 补入具体做法 | [K09-10](K09_structure_geometry.md#k09-10) | 用奇异值加权的左右向量外积重建矩阵与截断分量；补上取保留能量时对奇异值平方累计的分母及中心化条件。015从协方差谱取log均值，141保留rank-m，228选择材料表示，234拆QK/OV权重；不同输入不能沿用同一方差解释。 |
| <a id="gap-kg_dr_constrained"></a>约束正交子空间分解 [KG_DR_CONSTRAINED](#evidence-kg_dr_constrained) | 补入具体做法 | [K09-11](K09_structure_geometry.md#k09-11) | 137/D004先取共享向量与低秩残差，再由伪逆归一得到满足正交条件的共享分量并作第二次分解。检查奇异值吸收和重构，保留原式1/d与列数L的差异，不假定已复现未报的秩。 |
| <a id="gap-worker_4_gap_euclidean_geometry"></a>欧氏表征距离及尺度解释操作支持 [worker_4_gap_euclidean_geometry](#evidence-worker_4_gap_euclidean_geometry) | 补全已有指导 | [K09-12](K09_structure_geometry.md#k09-12) | 补入逐维差平方和开根号、共同缩放和逐维缩放的区别。045按五个量尺坐标，047用同一MDS平面，048用多语嵌入，127与运输距离比较；129句对共享句子、135负距离取均值，这些数值只在各自坐标和抽样单位下解释。 |
| <a id="gap-worker_4_gap_dot_embedding"></a>嵌入点积相关性测量操作支持 [worker_4_gap_dot_embedding](#evidence-worker_4_gap_dot_embedding) | 补入具体做法 | [K09-12](K09_structure_geometry.md#k09-12) | 042/D018给题目和512-token窗口的TASB向量作点积；展开为两模长乘余弦，未归一时阈值95依赖所用表征与窗口，不能套用到别的编码器。 |
| <a id="gap-worker_4_gap_rbf_similarity"></a>RBF核的数据点任务相似度操作支持 [worker_4_gap_rbf_similarity](#evidence-worker_4_gap_rbf_similarity) | 补入具体做法 | [K09-12](K09_structure_geometry.md#k09-12) | 135/D024以径向核把特征距离变成相似度，再对当前点与以往任务的点取均值；带宽与坐标尺度决定衰减，逐点平均使大样本任务权重更高。未报告的带宽留在该篇记录。 |
| <a id="gap-worker_4_gap_inner_hamming"></a>潜变量Hamming与嵌入内积的几何关系操作支持 [worker_4_gap_inner_hamming](#evidence-worker_4_gap_inner_hamming) | 补入具体做法 | [K09-12](K09_structure_geometry.md#k09-12) | 141/D014先在相同潜变量编码下计不相等的位数，再分组看嵌入内积；区分自内积b₀与异token的近似线性关系，矩阵条件和尺度限制保留。 |
| <a id="gap-kg_cov_det"></a>协方差行列式与表示覆盖解释 [KG_COV_DET](#evidence-kg_cov_det) | 补入具体做法 | [K09-13](K09_structure_geometry.md#k09-13) | 237/D023用固定10维PCA坐标的经验协方差取行列式，表示各特征值的乘积。对照代码补上极大似然的1/n分母及矩阵缩放的d次方影响；不同维度与秩亏值不能直接作语义覆盖比较。 |
| <a id="gap-worker_2_projection_variance_gap"></a>特征方向标量投影的方差操作与解释 [worker_2_projection_variance_gap](#evidence-worker_2_projection_variance_gap) | 补入具体做法 | [K09-13](K09_structure_geometry.md#k09-13) | 047/D024先沿已单位化的特征方向投影，再计算坐标的一维方差uᵀSu；它依赖原MDS尺度。保留正文mean r与附录方差定义的差别，不能补成相关平方。 |
| <a id="gap-worker_2_cov_trace_gap"></a>经验协方差迹的总方差操作与解释 [worker_2_cov_trace_gap](#evidence-worker_2_cov_trace_gap) | 补入具体做法 | [K09-13](K09_structure_geometry.md#k09-13) | 237/D017对原嵌入的经验协方差求对角和，得到各坐标方差之和；补出代码采用1/n中心化协方差，与n−1样本协方差的比例不同。该数值与平均句间距离和十维det分别计算。 |
| <a id="gap-worker_4_gap_principal_angle"></a>低秩子空间最小主夹角操作支持 [worker_4_gap_principal_angle](#evidence-worker_4_gap_principal_angle) | 补入具体做法 | [K09-13](K09_structure_geometry.md#k09-13) | 141/D013对已训练与构造或随机矩阵的低秩列空间取最小主角。补明近零表示最接近的一对方向近似对齐，精确为零才有共同非零方向；其余方向可相去甚远，数值零还须结合容差解释。 |
| <a id="gap-worker_5_procrustes_gap"></a>Procrustes坐标拟合对齐：操作知识 [worker_5_PROCRUSTES_gap](#evidence-worker_5_procrustes_gap) | 补入具体做法 | [K09-13](K09_structure_geometry.md#k09-13) | 222/D015以同次序19个价值点对齐模型与既有人类二维MDS，通过中心化、正交矩阵和对齐残差消除坐标任意性。人类分布是衡量模型结构的外部参照；是否允许反射和尺度调整未给。 |
| <a id="gap-worker_1_kg_adjacent_boundary_search"></a>单趟相邻社区边界搜索需补知识 [worker_1_KG_ADJACENT_BOUNDARY_SEARCH](#evidence-worker_1_kg_adjacent_boundary_search) | 补入具体做法 | [K09-14](K09_structure_geometry.md#k09-14) | 177/D008单趟更新相邻社区。补明成员向右侧社区移动时边界索引β̂≤β，并交代最后一个右邻、conductance低值与伪码argmax的未说明处。单趟同目标改善不能证明全局最优或语义效度。 |
| <a id="gap-worker_2_modularity_gap"></a>随机边参照的社区模块度操作与解释 [worker_2_modularity_gap](#evidence-worker_2_modularity_gap) | 补入具体做法 | [K09-14](K09_structure_geometry.md#k09-14) | 177/D006将实际边权减去度数零模型的期望，按同社区指示加总。通用模块度与该篇的1/(4m)外系数分别列出；在同目标上优化后的分数不提供独立检验。 |
| <a id="gap-worker_2_conductance_gap"></a>图割导通与内部体积归一操作与解释 [worker_2_conductance_gap](#evidence-worker_2_conductance_gap) | 补入具体做法 | [K09-14](K09_structure_geometry.md#k09-14) | 177/D007按割边权除以较小一侧内部volume，并取较小割值，保留其与常用度数体积的区别。补明若把低conductance目标接到统一argmax，需显式反向，论文没有写出这一转换。 |
| <a id="gap-worker_2_leiden_gap"></a>Leiden模块度社区分区操作与解释 [worker_2_leiden_gap](#evidence-worker_2_leiden_gap) | 补入具体做法 | [K09-14](K09_structure_geometry.md#k09-14) | 032/D020用Leiden模块度分区作机器任务评分所需的算法参照，需经过节点移动、细化与图聚合；下游ARI仅比较已有标签。未将该分区当成人工唯一金标。 |
| <a id="gap-kg_graph_motif"></a>图motif及交替子结构统计 [KG_GRAPH_MOTIF](#evidence-kg_graph_motif) | 补入具体做法 | [K09-15](K09_structure_geometry.md#k09-15) | 037/D013的ERGM充分统计量包括边、三角、星、交替三角及二路径；正文用共享邻居和递减权重解释重叠结构。若输入是软边，必须交代二值化或概率假设；原文未报的计算配置不填入。 |
| <a id="gap-worker_1_kg_ego_subgraph"></a>ego邻域中心移除子图取样需补知识 [worker_1_KG_EGO_SUBGRAPH](#evidence-worker_1_kg_ego_subgraph) | 补全已有指导 | [K09-15](K09_structure_geometry.md#k09-15) | 037/D002在真实网络均匀采中心，提取邻域诱导的子图、移除中心并按5–30节点选材料。移除中心可能断连，调查该性质不能替论文新增连通性筛选；与随机生成ER图分别记录。 |
| <a id="gap-worker_4_gap_network_statistics"></a>图密度/局部聚类与加权度操作支持 [worker_4_gap_network_statistics](#evidence-worker_4_gap_network_statistics) | 补入具体做法 | [K09-15](K09_structure_geometry.md#k09-15) | 103/D020分开计算边数相对于可能边数的密度、邻居间三角形聚类及节点加权度；pruned与原图的节点集会改变分母。WAE只是边权均值；图文关于密度方向的冲突保留。 |
| <a id="gap-worker_2_clique_dedup_gap"></a>相似图极大团去重操作与解释 [worker_2_clique_dedup_gap](#evidence-worker_2_clique_dedup_gap) | 补入具体做法 | [K09-16](K09_structure_geometry.md#k09-16) | 补入在无向相似图遍历find_cliques并保留全部极大团成员的可操作入口。100/D009按阈值连边、团内选最不相似解释、重叠成员按团平均相似度唯一指派；既非找最大团也非选medoid。 |
| <a id="gap-worker_3_kg_graph_label_diffusion"></a>对称归一邻接图的种子标签传播操作知识 [worker_3_KG_GRAPH_LABEL_DIFFUSION](#evidence-worker_3_kg_graph_label_diffusion) | 补入具体做法 | [K09-17](K09_structure_geometry.md#k09-17) | 103/D011对称度归一权重，按带重启迭代分发五维种子得分，解固定点并核残差。原文实际闭式省了1−α；相同α仅整体缩放，跨α和固定阈值的数值比较会受影响。 |
| <a id="gap-worker_4_gap_graph_edit"></a>图编辑距离操作支持 [worker_4_gap_graph_edit](#evidence-worker_4_gap_graph_edit) | 补入具体做法 | [K09-18](K09_structure_geometry.md#k09-18) | 009/D021按给定节点/边属性的插入、删除、替换成本，联合搜索对应和最低代价编辑序列；保留近似上界与最优值区别。该篇报告均值但成本未报，集合F1不能补这个参数。 |
| <a id="gap-worker_1_kg_embedding_dtw"></a>嵌入距离动态时间规整路径需补知识 [worker_1_KG_EMBEDDING_DTW](#evidence-worker_1_kg_embedding_dtw) | 补入具体做法 | [K09-19](K09_structure_geometry.md#k09-19) | 168/D020把生成文本和原转录的GPT-2词元嵌入作欧氏FastDTW，再沿所得路径映回时轴。补清有增删时按序号对齐会错、先估计路径再使用已有时间戳；近似路径不保证真实同时发音。 |
| <a id="gap-worker_3_kg_forced_alignment"></a>既有转录与语音录音的强制词时序对齐操作知识 [worker_3_KG_FORCED_ALIGNMENT](#evidence-worker_3_kg_forced_alignment) | 补入具体做法 | [K09-19](K09_structure_geometry.md#k09-19) | 168/D003由录音、转录和对齐器得到各词毫秒起止时间，再把词内时段均分给子token，供模型分段定位。这是模型结果进入外部时间基准的桥；均分不是直接测得的子词时刻。 |
| <a id="gap-worker_4_gap_gaussian_smooth"></a>Gaussian核平滑与显示插值操作支持 [worker_4_gap_gaussian_smooth](#evidence-worker_4_gap_gaussian_smooth) | 补入具体做法 | [K09-20](K09_structure_geometry.md#k09-20) | 在声明的一维轴或二维网格按核权重卷积，区分σ、边界和插值。205逐层平滑均值与SEM，225平滑35×35热图后才插值；插出的像素不是独立重复。 |
| <a id="gap-worker_5_gaussian_peak_gap"></a>Gaussian时间平滑与阈值局部峰检测：操作知识 [worker_5_GAUSSIAN_PEAK_gap](#evidence-worker_5_gaussian_peak_gap) | 补入具体做法 | [K09-20](K09_structure_geometry.md#k09-20) | 补清168/D008的峰检测作用于已有人类按键共识，产出的边界直接评分模型分段。不同故事配置分别取2秒宽/95百分位或σ=.2秒/90百分位，后两者的相邻峰及重复边界须去重；模型没有用按键曲线生成自己的边界。 |
| <a id="gap-worker_4_gap_wordnet_basic_sense"></a>WordNet基本义/语境义驱动inapt替换操作支持 [worker_4_gap_wordnet_basic_sense](#evidence-worker_4_gap_wordnet_basic_sense) | 补全已有指导 | [K09-21](K09_structure_geometry.md#k09-21) | 054/D006以基本义与语境义的对照选WordNet synset，优先用同义词、缺候选时看上位词，检查语法与来源域以构造inapt材料。词义不唯一时保留人工裁决和选择理由。 |
| <a id="gap-worker_4_gap_syntax_np_prune"></a>句法树NP剪枝生成子问题操作支持 [worker_4_gap_syntax_np_prune](#evidence-worker_4_gap_syntax_np_prune) | 补全已有指导 | [K09-21](K09_structure_geometry.md#k09-21) | 091/D007在句法树中定位含命名实体的NP，保留根问题，取最深NP转yes/no。补明原文用带文档模型回答No才确认该候选；比较题的JJR/RB过滤另行，来源对解析器表述有差异。 |
| <a id="gap-worker_4_gap_syntax_coref_template"></a>主语共指约束的谓词模板挖掘操作支持 [worker_4_gap_syntax_coref_template](#evidence-worker_4_gap_syntax_coref_template) | 补全已有指导 | [K09-21](K09_structure_geometry.md#k09-21) | 123/D004要求候选Y与主语共指或修饰主语，抽取跨关键词谓词，统一时态、合并报告动词结构并用X替换主语。本文放宽双关键词同现，工具及全部模板未知。 |
| <a id="gap-kg_cortical_register"></a>功能影像配准与皮层表面投影 [KG_CORTICAL_REGISTER](#evidence-kg_cortical_register) | 补入具体做法 | [K09-22](K09_structure_geometry.md#k09-22) | 121/D026把模型表征与人脑响应的关联或预测表现投到各被试对应的皮层网格，补清结果图比较的是共同刺激下的外部参照。R²筛选和噪声归一只影响显示；不能把皮层图读成模型内部神经元分布。 |
| <a id="gap-worker_4_gap_polygon_cv"></a>阈值连通域与轮廓简化的多边形计数操作支持 [worker_4_gap_polygon_cv](#evidence-worker_4_gap_polygon_cv) | 补入具体做法 | [K09-23](K09_structure_geometry.md#k09-23) | 241/D012、D013按固定阈值、4连通与面积过滤、外轮廓和弧长比例简化计顶点。补明实际partition驱动按选定边数统计最小区域，没有调用全嵌套枚举；发布代码与论文生成图之间仍缺运行对应。 |

## K10 可解密的公开材料发布

| 具体需求与论文证据 | 定稿处理 | 正文位置 | 具体结果和适用范围 |
|---|---|---|---|
| <a id="gap-worker_4_gap_encrypted_release"></a>公开评测集加密发布及解密脚本操作支持 [worker_4_gap_encrypted_release](#evidence-worker_4_gap_encrypted_release) | 补全已有指导 | [K10-01](K10_release.md#k10-01) | 055/D018以公开密文和可用解密途径兼顾访问与降低普通抓取取得明文的机会。沿用发布版本、取回核对和暴露面说明；本条提供材料发布指导，不能据此判定某模型从未见过数据。 |

<a id="by-component"></a>
## 从原建议承接组件查方法小节

原缺口表把每项缺口交给一个建议承接组件。下列链接沿用这个分工，以便从组件找到相关方法。同一小节只列一次，范围外实例另列于对应组件下。

<a id="methods-a2"></a>
### [A2](COMPONENTS.md#a2)

- K01 统计分析：从研究问题到可解释的结果　[24](K01_statistics.md#k01-24)
- K03 文本与语义评价　[01](K03_text_semantics.md#k03-01)、[03](K03_text_semantics.md#k03-03)、[04](K03_text_semantics.md#k03-04)、[05](K03_text_semantics.md#k03-05)、[06](K03_text_semantics.md#k03-06)、[07](K03_text_semantics.md#k03-07)、[08](K03_text_semantics.md#k03-08)、[09](K03_text_semantics.md#k03-09)、[12](K03_text_semantics.md#k03-12)、[13](K03_text_semantics.md#k03-13)
- K04 概率取得、条件化与分布比较　[01](K04_probability.md#k04-01)、[02](K04_probability.md#k04-02)、[03](K04_probability.md#k04-03)、[04](K04_probability.md#k04-04)、[05](K04_probability.md#k04-05)、[06](K04_probability.md#k04-06)、[07](K04_probability.md#k04-07)、[08](K04_probability.md#k04-08)、[09](K04_probability.md#k04-09)、[10](K04_probability.md#k04-10)、[12](K04_probability.md#k04-12)、[13](K04_probability.md#k04-13)
- K05 校准、区分能力与排序评价　[01](K05_evaluation.md#k05-01)、[02](K05_evaluation.md#k05-02)、[03](K05_evaluation.md#k05-03)、[04](K05_evaluation.md#k05-04)、[05](K05_evaluation.md#k05-05)、[06](K05_evaluation.md#k05-06)、[07](K05_evaluation.md#k05-07)
- K06 认知模型、因果推断与符号方法　[02](K06_cognitive_causal.md#k06-02)、[10](K06_cognitive_causal.md#k06-10)、[11](K06_cognitive_causal.md#k06-11)、[12](K06_cognitive_causal.md#k06-12)、[13](K06_cognitive_causal.md#k06-13)、[14](K06_cognitive_causal.md#k06-14)、[18](K06_cognitive_causal.md#k06-18)
- K08 模型内部测量与临时干预　[14](K08_internal_methods.md#k08-14)
- K09 材料构造、图结构与表征几何　[01](K09_structure_geometry.md#k09-01)、[03](K09_structure_geometry.md#k09-03)、[12](K09_structure_geometry.md#k09-12)、[13](K09_structure_geometry.md#k09-13)、[15](K09_structure_geometry.md#k09-15)、[17](K09_structure_geometry.md#k09-17)、[18](K09_structure_geometry.md#k09-18)、[19](K09_structure_geometry.md#k09-19)、[20](K09_structure_geometry.md#k09-20)

<a id="methods-a6"></a>
### [A6](COMPONENTS.md#a6)

- K06 认知模型、因果推断与符号方法　[07](K06_cognitive_causal.md#k06-07)、[09](K06_cognitive_causal.md#k06-09)

<a id="methods-a7"></a>
### [A7](COMPONENTS.md#a7)

- K03 文本与语义评价　[02](K03_text_semantics.md#k03-02)、[08](K03_text_semantics.md#k03-08)、[09](K03_text_semantics.md#k03-09)、[10](K03_text_semantics.md#k03-10)、[11](K03_text_semantics.md#k03-11)、[14](K03_text_semantics.md#k03-14)
- K04 概率取得、条件化与分布比较　[13](K04_probability.md#k04-13)、[15](K04_probability.md#k04-15)
- K06 认知模型、因果推断与符号方法　[08](K06_cognitive_causal.md#k06-08)、[10](K06_cognitive_causal.md#k06-10)、[14](K06_cognitive_causal.md#k06-14)、[15](K06_cognitive_causal.md#k06-15)、[16](K06_cognitive_causal.md#k06-16)、[17](K06_cognitive_causal.md#k06-17)、[18](K06_cognitive_causal.md#k06-18)、[19](K06_cognitive_causal.md#k06-19)、[20](K06_cognitive_causal.md#k06-20)、[21](K06_cognitive_causal.md#k06-21)、[22](K06_cognitive_causal.md#k06-22)、[23](K06_cognitive_causal.md#k06-23)、[24](K06_cognitive_causal.md#k06-24)、[25](K06_cognitive_causal.md#k06-25)、[26](K06_cognitive_causal.md#k06-26)、[28](K06_cognitive_causal.md#k06-28)、[29](K06_cognitive_causal.md#k06-29)、[30](K06_cognitive_causal.md#k06-30)
- K07 动态状态、记忆与外部执行　[01](K07_state_execution.md#k07-01)、[02](K07_state_execution.md#k07-02)、[03](K07_state_execution.md#k07-03)、[04](K07_state_execution.md#k07-04)、[05](K07_state_execution.md#k07-05)、[06](K07_state_execution.md#k07-06)、[07](K07_state_execution.md#k07-07)、[08](K07_state_execution.md#k07-08)、[09](K07_state_execution.md#k07-09)、[10](K07_state_execution.md#k07-10)
- K08 模型内部测量与临时干预　[01](K08_internal_methods.md#k08-01)、[02](K08_internal_methods.md#k08-02)、[03](K08_internal_methods.md#k08-03)、[04](K08_internal_methods.md#k08-04)、[05](K08_internal_methods.md#k08-05)、[06](K08_internal_methods.md#k08-06)、[07](K08_internal_methods.md#k08-07)、[08](K08_internal_methods.md#k08-08)、[09](K08_internal_methods.md#k08-09)、[10](K08_internal_methods.md#k08-10)、[11](K08_internal_methods.md#k08-11)、[12](K08_internal_methods.md#k08-12)、[13](K08_internal_methods.md#k08-13)
- K09 材料构造、图结构与表征几何　[01](K09_structure_geometry.md#k09-01)、[02](K09_structure_geometry.md#k09-02)、[04](K09_structure_geometry.md#k09-04)、[05](K09_structure_geometry.md#k09-05)、[06](K09_structure_geometry.md#k09-06)、[07](K09_structure_geometry.md#k09-07)、[13](K09_structure_geometry.md#k09-13)、[14](K09_structure_geometry.md#k09-14)、[15](K09_structure_geometry.md#k09-15)、[16](K09_structure_geometry.md#k09-16)、[21](K09_structure_geometry.md#k09-21)、[22](K09_structure_geometry.md#k09-22)、[23](K09_structure_geometry.md#k09-23)

<a id="methods-f1"></a>
### [F1](COMPONENTS.md#f1)

- K01 统计分析：从研究问题到可解释的结果　[02](K01_statistics.md#k01-02)、[03](K01_statistics.md#k01-03)、[04](K01_statistics.md#k01-04)、[05](K01_statistics.md#k01-05)、[06](K01_statistics.md#k01-06)、[07](K01_statistics.md#k01-07)、[08](K01_statistics.md#k01-08)、[09](K01_statistics.md#k01-09)、[10](K01_statistics.md#k01-10)、[11](K01_statistics.md#k01-11)、[12](K01_statistics.md#k01-12)、[13](K01_statistics.md#k01-13)、[14](K01_statistics.md#k01-14)、[15](K01_statistics.md#k01-15)、[16](K01_statistics.md#k01-16)、[17](K01_statistics.md#k01-17)、[18](K01_statistics.md#k01-18)、[19](K01_statistics.md#k01-19)、[20](K01_statistics.md#k01-20)、[21](K01_statistics.md#k01-21)、[22](K01_statistics.md#k01-22)、[23](K01_statistics.md#k01-23)、[24](K01_statistics.md#k01-24)、[25](K01_statistics.md#k01-25)、[26](K01_statistics.md#k01-26)、[27](K01_statistics.md#k01-27)、[28](K01_statistics.md#k01-28)
- K03 文本与语义评价　[12](K03_text_semantics.md#k03-12)
- K04 概率取得、条件化与分布比较　[11](K04_probability.md#k04-11)、[14](K04_probability.md#k04-14)
- K05 校准、区分能力与排序评价　[05](K05_evaluation.md#k05-05)、[06](K05_evaluation.md#k05-06)
- K06 认知模型、因果推断与符号方法　[01](K06_cognitive_causal.md#k06-01)、[02](K06_cognitive_causal.md#k06-02)、[03](K06_cognitive_causal.md#k06-03)、[04](K06_cognitive_causal.md#k06-04)、[05](K06_cognitive_causal.md#k06-05)、[06](K06_cognitive_causal.md#k06-06)、[10](K06_cognitive_causal.md#k06-10)、[11](K06_cognitive_causal.md#k06-11)、[14](K06_cognitive_causal.md#k06-14)、[27](K06_cognitive_causal.md#k06-27)、[28](K06_cognitive_causal.md#k06-28)、[29](K06_cognitive_causal.md#k06-29)
- K09 材料构造、图结构与表征几何　[08](K09_structure_geometry.md#k09-08)、[09](K09_structure_geometry.md#k09-09)、[10](K09_structure_geometry.md#k09-10)、[11](K09_structure_geometry.md#k09-11)、[13](K09_structure_geometry.md#k09-13)、[14](K09_structure_geometry.md#k09-14)、[20](K09_structure_geometry.md#k09-20)
- 范围外实例 [LOWESS局部加权回归平滑](#gap-kg_smooth_lowess)。

<a id="methods-f3"></a>
### [F3](COMPONENTS.md#f3)

- K01 统计分析：从研究问题到可解释的结果　[28](K01_statistics.md#k01-28)
- K02 标注、裁决与信度　[02](K02_annotation_reliability.md#k02-02)、[03](K02_annotation_reliability.md#k02-03)、[04](K02_annotation_reliability.md#k02-04)、[05](K02_annotation_reliability.md#k02-05)、[06](K02_annotation_reliability.md#k02-06)、[07](K02_annotation_reliability.md#k02-07)、[08](K02_annotation_reliability.md#k02-08)

<a id="methods-g1"></a>
### [G1](COMPONENTS.md#g1)

- 范围外实例 [个体层与合并层估计对象的区别](#gap-kg_unit_estimand)。

<a id="methods-g4"></a>
### [G4](COMPONENTS.md#g4)

- K01 统计分析：从研究问题到可解释的结果　[26](K01_statistics.md#k01-26)

<a id="methods-j11"></a>
### [J11](COMPONENTS.md#j11)

- K10 可解密的公开材料发布　[01](K10_release.md#k10-01)

<a id="methods-j20"></a>
### [J20](COMPONENTS.md#j20)

- K07 动态状态、记忆与外部执行　[03](K07_state_execution.md#k07-03)、[05](K07_state_execution.md#k07-05)

<a id="paper-evidence"></a>
## 按缺口查论文需求、事实与原文证据

每条需求链接指向论文的组件判断记录。事实与原文记录中可按 F 编号查提取事实，按 E 编号查引文及其在论文中的位置。

<a id="evidence-kg_boot_distribution"></a>
### KG_BOOT_DISTRIBUTION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_distribution)

从观测选择有放回重抽样单位、重算目标统计量并形成经验分布/区间的操作；区分数据复样与再次调用模型

- [article_013/D012 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_013.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_013.json)　事实 F010、F016。原文证据 E008、E014、E019。
- [article_049/D014 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_049.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_049.json)　事实 F012、F017。原文证据 E044、E043、E051。
- [article_067/D026 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_067.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_067.json)　事实 F022。原文证据 E016。
- [article_121/D014 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F012。原文证据 E021、E022、E023。
- [article_186/D013 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_186.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_186.json)　事实 F010、F041。原文证据 E032、E127、E128、E129、E130、E131、E132、E133。
- [article_188/D015 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_188.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_188.json)　事实 F012、F022。原文证据 E004、E041、E042、E064、E065、E066、E067。
- [article_193/D012 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_193.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_193.json)　事实 F013。原文证据 E039、E040。

<a id="evidence-kg_boot_paired"></a>
### KG_BOOT_PAIRED

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_paired)

成对保留同一题/观测的比较值、重算差异统计量并形成比较分布；与独立抽两组的区别

- [article_120/D025 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_120.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_120.json)　事实 F028。原文证据 E045。
- [article_235/D027 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F011。原文证据 E020、E021、E022。

<a id="evidence-kg_boot_dependence"></a>
### KG_BOOT_DEPENDENCE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_dependence)

簇重抽样和相关距离项/原始反应重抽样的单位选择及估计目标；区分已实施方案与其适用性

- [article_064/D011 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_064.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_064.json)　事实 F020。原文证据 E021。
- [article_237/D019 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F020。原文证据 E060、E061。

<a id="evidence-kg_boot_basic"></a>
### KG_BOOT_BASIC

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_basic)

basic区间的分布分位数、以原估计反射端点的规则及其适用解释

- [article_055/D015 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_055.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_055.json)　事实 F016、F017、F019。原文证据 E042、E043、E044、E045、E046、E051、E052、E053。

<a id="evidence-kg_boot_percentile"></a>
### KG_BOOT_PERCENTILE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_percentile)

从重抽样统计量排序取分位点、尾概率及有限复样的端点约定

- [article_237/D014 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F016。原文证据 E048、E049、E050。
- [article_237/D019 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F020。原文证据 E060、E061。
- [article_237/D025 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F026。原文证据 E075、E076。

<a id="evidence-kg_boot_sd"></a>
### KG_BOOT_SD

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_sd)

统计量复样分布SD、原始观测SD和置信区间的区别；SD误差条的范围解释

- [article_047/D026 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F013、F014、F019、F021、F029。原文证据 E035、E036、E037、E038、E044、E045、E052、E055、E065、E066、E051、E067、E068。
- [article_087/D012 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_087.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_087.json)　事实 F015。原文证据 E011、E016、E032。
- [article_133/D017 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_133.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_133.json)　事实 F025。原文证据 E055、E056。
- [article_224/D023 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_224.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_224.json)　事实 F022。原文证据 E063。

<a id="evidence-kg_boot_pipeline"></a>
### KG_BOOT_PIPELINE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_pipeline)

重抽后重算构成最终统计量的估计步骤，保持相关基线、归一化或拟合分数的依赖；不能只重抽最终标量

- [article_024/D012 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_024.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_024.json)　事实 F014。原文证据 E009、E011、E031。
- [article_047/D026 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F013、F014、F019、F021、F029。原文证据 E035、E036、E037、E038、E044、E045、E052、E055、E065、E066、E051、E067、E068。
- [article_173/D007 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_173.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_173.json)　事实 F007、F022。原文证据 E017、E018、E055、E056。
- [article_229/D010 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_229.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_229.json)　事实 F005。原文证据 E009、E010、E011、E012。

<a id="evidence-kg_boot_test"></a>
### KG_BOOT_TEST

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_test)

说明零假设参照、比较统计量和尾概率的构造；有放回复样次数本身不足以确定P值

- [article_121/D032 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F024。原文证据 E039、E040。
- [article_235/D027 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F011。原文证据 E020、E021、E022。

<a id="evidence-kg_boot_transform"></a>
### KG_BOOT_TRANSFORM

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_transform)

非单调绝对值变换遇跨零区间的处理，以及以两个区间重叠推断差异的条件

- [article_237/D014 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F016。原文证据 E048、E049、E050。

<a id="evidence-kg_boot_conditional"></a>
### KG_BOOT_CONDITIONAL

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_boot_conditional)

固定已估计投影再重抽反应，与每次重新估计投影所涵盖不确定性的区别

- [article_237/D025 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F026。原文证据 E075、E076。

<a id="evidence-kg_unit_estimand"></a>
### KG_UNIT_ESTIMAND

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_unit_estimand)

个体分数或参数的平均与合并所有试次后拟合所得参数并不等价；权重、非线性及个体异质性如何改变估计对象

- [article_003/D320 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_003.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_003.json)　事实 F006、F037、F013。原文证据 E009、E015、E045、E066、E067。

<a id="evidence-kg_pearson"></a>
### KG_PEARSON

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_pearson)

标准化协方差计算、零方差/离群/聚合尺度的影响、线性关联与绝对一致/因果的区别；需要推断时明确独立性与检验条件

- [article_007/D016 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_007.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_007.json)　事实 F005、F014。原文证据 E004、E006、E028。
- [article_020/D031 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F027。原文证据 E029、E030、E032。
- [article_026/D024 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_026.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_026.json)　事实 F017、F019、F024。原文证据 E005、E008、E010、E027、E011、E038。
- [article_029/D025 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_029.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_029.json)　事实 F022。原文证据 E024、E019、E026、E041、E042。
- [article_030/D027 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_030.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_030.json)　事实 F020。原文证据 E026。
- [article_044/D020 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_044.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_044.json)　事实 F018。原文证据 E018、E017、E024。
- [article_051/D014 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_051.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_051.json)　事实 F016。原文证据 E046、E047。
- [article_064/D018 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_064.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_064.json)　事实 F021、F022。原文证据 E032、E033、E034、E035。
- [article_074/D016 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_074.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_074.json)　事实 F016。原文证据 E009、E016。
- [article_098/D021 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_098.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_098.json)　事实 F018。原文证据 E016、E017。
- [article_100/D019 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F015。原文证据 E012。
- [article_105/D027 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_105.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_105.json)　事实 F023。原文证据 E066、E067。
- [article_108/D017 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_108.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_108.json)　事实 F017、F018。原文证据 E008、E022。
- [article_111/D011 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_111.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_111.json)　事实 F011。原文证据 E020、E010。
- [article_121/D012 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F011、F019、F022、F023、F030。原文证据 E018、E019、E020、E033、E034、E037、E038、E039、E049。
- [article_127/D023 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F026。原文证据 E042。
- [article_145/D015 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_145.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_145.json)　事实 F015。原文证据 E042、E043、E038、E099、E040。
- [article_158/D008 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_158.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_158.json)　事实 F009、F010。原文证据 E015、E016。
- [article_165/D026 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_165.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_165.json)　事实 F024、F025。原文证据 E051、E052、E053。
- [article_168/D022 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_168.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_168.json)　事实 F021、F022。原文证据 E038、E039、E040、E041。
- [article_176/D017 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_176.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_176.json)　事实 F018、F022、F023。原文证据 E039、E043、E044、E045、E046。
- [article_179/D038 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F026。原文证据 E077、E078。
- [article_187/D010 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_187.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_187.json)　事实 F008。原文证据 E025、E026。
- [article_191/D019 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_191.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_191.json)　事实 F020、F021。原文证据 E010、E063、E064、E065。
- [article_194/D017 · 需求记录 r12](../../../analysis/literature_component_coverage/records/assessments/article_194.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_194.json)　事实 F023。原文证据 E062、E063、E064。
- [article_206/D010 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_206.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_206.json)　事实 F011。原文证据 E027、E028。
- [article_207/D008 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_207.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_207.json)　事实 F007、F026。原文证据 E012、E013、E047。
- [article_210/D015 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_210.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_210.json)　事实 F019、F020、F022。原文证据 E040、E041、E042、E043、E046、E047、E048、E049。
- [article_228/D023 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_228.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_228.json)　事实 F022、F023。原文证据 E061、E062、E063、E064、E065、E066。
- [article_229/D003 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_229.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_229.json)　事实 F003、F007、F008、F024。原文证据 E006、E015、E016、E017、E056、E057、E058、E059。
- [article_230/D019 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_230.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_230.json)　事实 F020、F021、F025、F026、F027、F028。原文证据 E045、E046、E047、E048、E049、E050、E057、E058、E059、E060、E061、E062、E063、E064、E065。

<a id="evidence-kg_point_biserial"></a>
### KG_POINT_BISERIAL

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_point_biserial)

二值编码方向、组比例/均值/离散程度到系数的关系及推断条件

- [article_070/D019 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_070.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_070.json)　事实 F018、F020。原文证据 E016、E017。
- [article_088/D023 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_088.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_088.json)　事实 F025。原文证据 E027。
- [article_127/D025 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F027。原文证据 E043、E044。

<a id="evidence-kg_pearson_interpret"></a>
### KG_PEARSON_INTERPRET

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_pearson_interpret)

线性相关不保证逐条相等、无系统偏移或完整效度；明确相关验证能支持什么

- [article_068/D218 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_068.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_068.json)　事实 F026。原文证据 E053、E054。

<a id="evidence-kg_pearson_lag"></a>
### KG_PEARSON_LAG

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_pearson_lag)

lag改变配对与有效数据段；零lag与搜索最大lag用途不同，自相关对推断的影响

- [article_168/D022 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_168.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_168.json)　事实 F021、F022。原文证据 E038、E039、E040、E041。

<a id="evidence-kg_pearson_matrix"></a>
### KG_PEARSON_MATRIX

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_pearson_matrix)

明确矩阵取值/向量化的配对规则及共享对象引起的元素依赖，区分原始相关与信度校正

- [article_121/D012 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F011、F019、F022、F023、F030。原文证据 E018、E019、E020、E033、E034、E037、E038、E039、E049。

<a id="evidence-kg_spearman"></a>
### KG_SPEARMAN

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_spearman)

从对应观测转秩、处理并列/缺失秩、计算秩相关；区分无并列简式与一般方法及推断条件

- [article_007/D018 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_007.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_007.json)　事实 F016、F017。原文证据 E009、E010。
- [article_016/D017 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F016、F021、F023、F024。原文证据 E022、E024、E027、E029、E030。
- [article_020/D032 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F012。原文证据 E031。
- [article_021/D015 · 需求记录 r30](../../../analysis/literature_component_coverage/records/assessments/article_021.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_021.json)　事实 F016。原文证据 E022、E023、E035。
- [article_021/D022 · 需求记录 r30](../../../analysis/literature_component_coverage/records/assessments/article_021.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_021.json)　事实 F022。原文证据 E015、E017、E037。
- [article_040/D018 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_040.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_040.json)　事实 F018。原文证据 E018、E019。
- [article_065/D016 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_065.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_065.json)　事实 F013、F017、F018。原文证据 E019、E023、E024。
- [article_070/D017 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_070.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_070.json)　事实 F016、F020。原文证据 E012、E013、E017。
- [article_086/D009 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_086.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_086.json)　事实 F010、F011。原文证据 E007、E011。
- [article_088/D007 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_088.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_088.json)　事实 F008、F009、F010、F025。原文证据 E009、E010、E016、E017、E027。
- [article_096/D015 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_096.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_096.json)　事实 F016、F018。原文证据 E009、E017、E021、E022、E023。
- [article_100/D017 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F014。原文证据 E011、E022、E023。
- [article_103/D013 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_103.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_103.json)　事实 F011、F012。原文证据 E029、E030、E031、E032。
- [article_118/D009 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_118.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_118.json)　事实 F012、F018、F019。原文证据 E012、E013、E015、E018、E011、E023、E027。
- [article_159/D012 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_159.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_159.json)　事实 F011。原文证据 E025、E026。
- [article_179/D037 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F024。原文证据 E070、E071、E072。
- [article_183/D010 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_183.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_183.json)　事实 F012、F014。原文证据 E023、E024、E025、E067、E027、E028。
- [article_187/D011 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_187.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_187.json)　事实 F008、F018、F022。原文证据 E025、E026、E046、E047、E048、E010、E054、E055。
- [article_194/D016 · 需求记录 r12](../../../analysis/literature_component_coverage/records/assessments/article_194.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_194.json)　事实 F021、F022。原文证据 E019、E058、E020、E059、E060、E061。
- [article_207/D007 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_207.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_207.json)　事实 F007、F009、F013、F015、F016、F018、F022、F023。原文证据 E012、E013、E016、E017、E022、E023、E026、E027、E028、E029、E030、E033、E034、E035、E036、E040、E041。
- [article_210/D017 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_210.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_210.json)　事实 F022。原文证据 E046、E047、E048、E049。
- [article_214/D023 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_214.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_214.json)　事实 F023。原文证据 E052、E053、E027、E065、E022。
- [article_219/D038 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_219.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_219.json)　事实 F032。原文证据 E089、E090、E091。
- [article_222/D010 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_222.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_222.json)　事实 F008、F009、F013、F017。原文证据 E018、E019、E020、E021、E029、E035、E036。
- [article_223/D011 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F009、F013、F015。原文证据 E018、E019、E025、E029、E030、E031、E032。
- [article_225/D041 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_225.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_225.json)　事实 F031、F032。原文证据 E087、E088、E089、E090、E091。
- [article_228/D024 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_228.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_228.json)　事实 F022、F023。原文证据 E061、E062、E063、E064、E065、E066。
- [article_229/D005 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_229.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_229.json)　事实 F008。原文证据 E017。
- [article_235/D022 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F005、F008、F029、F033。原文证据 E010、E011、E014、E015、E065、E066、E067、E068、E078、E079。
- [article_243/D033 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F026、F027、F060。原文证据 E053、E054、E055、E056、E124、E125。

<a id="evidence-kg_kendall"></a>
### KG_KENDALL

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_kendall)

一致/逆序对、归一化及并列处理；区分τ-a式、τ-b等变体而不替原文指定软件默认

- [article_007/D017 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_007.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_007.json)　事实 F016、F017。原文证据 E009、E010。
- [article_021/D016 · 需求记录 r30](../../../analysis/literature_component_coverage/records/assessments/article_021.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_021.json)　事实 F016。原文证据 E022、E023、E035。
- [article_091/D008 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_091.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_091.json)　事实 F007。原文证据 E008、E009。
- [article_120/D016 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_120.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_120.json)　事实 F018、F021。原文证据 E029、E035、E034。
- [article_167/D016 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_167.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_167.json)　事实 F015、F018、F019、F021、F022。原文证据 E010、E037、E038、E042、E043、E044、E045、E046、E047、E048。
- [article_179/D047 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F031。原文证据 E091、E092、E093、E094。
- [article_189/D016 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_189.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_189.json)　事实 F015。原文证据 E040、E041、E042。
- [article_225/D042 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_225.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_225.json)　事实 F031、F032。原文证据 E087、E088、E089、E090、E091。
- [article_228/D025 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_228.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_228.json)　事实 F022、F023。原文证据 E061、E062、E063、E064、E065、E066。
- [article_235/D023 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F012。原文证据 E023、E024。

<a id="evidence-kg_fisher_contrast"></a>
### KG_FISHER_CONTRAST

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_fisher_contrast)

相关到z的变换、两相关独立/共享样本时的方差结构、秩相关适用边界及差异解释

- [article_026/D032 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_026.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_026.json)　事实 F024、F025。原文证据 E010、E011、E038。
- [article_045/D015 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_045.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_045.json)　事实 F018。原文证据 E016、E040、E042。
- [article_222/D023 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_222.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_222.json)　事实 F017、F018。原文证据 E035、E036、E037。

<a id="evidence-kg_effect_cohen_q"></a>
### KG_EFFECT_COHEN_Q

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_effect_cohen_q)

相关系数Fisher变换的差及方向、独立/依赖相关的解释边界

- [article_045/D018 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_045.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_045.json)　事实 F028、F011、F016、F017、F018、F019。原文证据 E042、E035、E040、E011、E015、E016、E017。

<a id="evidence-kg_t_mean_execution"></a>
### KG_T_MEAN_EXECUTION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_t_mean_execution)

从独立或配对观测构造差值标准误与t统计；区分合并方差Student与Welch及其自由度，并按预定单/双尾计算p和区间

- [article_020/D027 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F015、F026。原文证据 E015、E036、E037、E038、E040。
- [article_020/D028 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F026、F021、F028。原文证据 E014、E021、E036、E038、E039、E040。
- [article_023/D013 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F012、F013。原文证据 E012、E015、E016。
- [article_023/D014 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F013。原文证据 E015、E016。
- [article_023/D029 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F027。原文证据 E025、E026。
- [article_045/D013 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_045.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_045.json)　事实 F007、F010、F011、F014、F016、F017。原文证据 E007、E010、E011、E013、E015、E016。
- [article_057/D010 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_057.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_057.json)　事实 F010。原文证据 E025、E026。
- [article_060/D011 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_060.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_060.json)　事实 F012。原文证据 E035、E036、E037。
- [article_076/D005 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_076.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_076.json)　事实 F005。原文证据 E001、E002。
- [article_080/D019 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_080.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_080.json)　事实 F022。原文证据 E018、E019、E020。
- [article_100/D018 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F014。原文证据 E011、E022、E023。
- [article_103/D019 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_103.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_103.json)　事实 F017。原文证据 E046、E047、E048。
- [article_105/D028 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_105.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_105.json)　事实 F024。原文证据 E068、E069、E070。
- [article_107/D019 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_107.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_107.json)　事实 F019。原文证据 E025、E026。
- [article_111/D017 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_111.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_111.json)　事实 F012。原文证据 E021、E022。
- [article_119/D023 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_119.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_119.json)　事实 F007、F020。原文证据 E003、E024、E025、E004、E020。
- [article_124/D025 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_124.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_124.json)　事实 F027、F028。原文证据 E011、E051、E034。
- [article_128/D017 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_128.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_128.json)　事实 F017、F019。原文证据 E034、E035、E036、E037、E038、E043、E044、E045。
- [article_140/D019 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_140.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_140.json)　事实 F028。原文证据 E057、E058。
- [article_154/D016 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_154.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_154.json)　事实 F019、F020、F023。原文证据 E053、E054、E055、E056、E057、E061、E062。
- [article_154/D019 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_154.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_154.json)　事实 F021、F023。原文证据 E058、E059、E061、E062。
- [article_157/D013 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_157.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_157.json)　事实 F016、F018、F019、F020。原文证据 E007、E034、E040、E061、E062、E063、E067、E068、E069、E070、E071、E072。
- [article_160/D015 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_160.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_160.json)　事实 F012、F016。原文证据 E030、E036、E037、E038、E039。
- [article_164/D018 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_164.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_164.json)　事实 F016。原文证据 E027、E004、E028。
- [article_168/D016 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_168.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_168.json)　事实 F017、F018。原文证据 E009、E030、E031、E032、E033。
- [article_169/D016 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_169.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_169.json)　事实 F017。原文证据 E042、E043。
- [article_174/D007 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_174.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_174.json)　事实 F005。原文证据 E008。
- [article_182/D009 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_182.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_182.json)　事实 F008、F009。原文证据 E015、E016、E017、E057。
- [article_228/D007 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_228.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_228.json)　事实 F006。原文证据 E017、E018、E019。
- [article_237/D011 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F014、F027。原文证据 E041、E042、E043、E077、E078、E079。

<a id="evidence-kg_variance_f_pretest"></a>
### KG_VARIANCE_F_PRETEST

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_variance_f_pretest)

方差比、各组自由度与F参考分布及分布假设；明确预检后选Student/Welch的决策及对最终推断的影响

- [article_174/D007 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_174.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_174.json)　事实 F005。原文证据 E008。

<a id="evidence-kg_z_mean_execution"></a>
### KG_Z_MEAN_EXECUTION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_z_mean_execution)

明确估计差与零假设、标准误来源和依赖/样本条件，以标准化统计量和正态尾计算p；不把所有均值比较默认z

- [article_115/D011 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_115.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_115.json)　事实 F012、F016。原文证据 E020、E022。
- [article_177/D021 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F022。原文证据 E044。

<a id="evidence-worker_3_kg_f_variance_pretest"></a>
### worker_3_KG_F_VARIANCE_PRETEST

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_3_kg_f_variance_pretest)

方差比统计量与自由度、正态独立条件、双侧尾概率及据预检选t检验的误差影响

- [article_174/D006 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_174.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_174.json)　事实 F005。原文证据 E008。

<a id="evidence-kg_signed"></a>
### KG_SIGNED

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_signed)

差值中心化、绝对差排序与符号秩和、零差/并列及对称性条件，单/双侧推断

- [article_014/D206 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_014.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_014.json)　事实 F006。原文证据 E010、E038、E047。
- [article_075/D015 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_075.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_075.json)　事实 F017。原文证据 E012。
- [article_120/D018 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_120.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_120.json)　事实 F020。原文证据 E024、E034、E035。
- [article_142/D018 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_142.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_142.json)　事实 F017、F019。原文证据 E033、E034、E036。
- [article_159/D020 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_159.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_159.json)　事实 F017。原文证据 E039、E040。
- [article_166/D027 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_166.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_166.json)　事实 F024、F031。原文证据 E042、E043、E044、E061、E062、E063。
- [article_199/D219 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F013、F014、F022。原文证据 E008、E015、E013。

<a id="evidence-kg_test_mann_whitney"></a>
### KG_TEST_MANN_WHITNEY

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_test_mann_whitney)

秩和/U构造、ties、独立性及分布/位置解释条件

- [article_029/D008 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_029.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_029.json)　事实 F006、F009。原文证据 E003、E007、E009、E010、E008、E048。
- [article_104/D012 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_104.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_104.json)　事实 F008。原文证据 E020、E021、E022、E023、E024、E025。
- [article_120/D023 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_120.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_120.json)　事实 F023、F026。原文证据 E039、E043。
- [article_127/D013 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F013、F014、F019、F025。原文证据 E025、E026、E027、E033、E041。
- [article_199/D215 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F014。原文证据 E014。

<a id="evidence-kg_test_kruskal_wallis"></a>
### KG_TEST_KRUSKAL_WALLIS

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_test_kruskal_wallis)

多组秩和H、ties与独立样本假设及后续比较

- [article_031/D013 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_031.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_031.json)　事实 F009。原文证据 E011、E013。
- [article_199/D214 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F014。原文证据 E014。

<a id="evidence-worker_4_gap_friedman"></a>
### worker_4_gap_friedman

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_4_gap_friedman)

重复测量块内排序、秩和统计量与χ²近似及ties修正

- [article_220/D007 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_220.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_220.json)　事实 F007。原文证据 E012、E013。

<a id="evidence-kg_tukey"></a>
### KG_TUKEY

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_tukey)

学生化极差、共同误差和样本结构的适用边界

- [article_023/D017 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F015。原文证据 E018、E019。
- [article_049/D020 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_049.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_049.json)　事实 F017。原文证据 E051。

<a id="evidence-kg_anova_execution"></a>
### KG_ANOVA_EXECUTION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_anova_execution)

按一因素或因子设计建立方差分解、匹配误差项和自由度，以均方比及F分布推断；区分主效应与交互、独立与重复测量适用

- [article_023/D016 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F015。原文证据 E018、E019。
- [article_049/D019 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_049.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_049.json)　事实 F017。原文证据 E051、E052。
- [article_089/D008 · 需求记录 r14](../../../analysis/literature_component_coverage/records/assessments/article_089.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_089.json)　事实 F012。原文证据 E009。
- [article_101/D014 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_101.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_101.json)　事实 F013、F014。原文证据 E034、E035、E036、E037、E038。
- [article_163/D006 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_163.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_163.json)　事实 F005、F006。原文证据 E009、E010、E011。
- [article_163/D007 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_163.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_163.json)　事实 F005、F006、F011、F012。原文证据 E009、E010、E011、E018、E019、E020。
- [article_228/D026 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_228.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_228.json)　事实 F024。原文证据 E067、E068、E069。

<a id="evidence-kg_table_chisquare"></a>
### KG_TABLE_CHISQUARE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_table_chisquare)

观测/期望频数、统计量自由度及稀疏/重复观测适用条件

- [article_020/D029 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F026、F004、F017、F018。原文证据 E025、E026、E017、E018、E041、E043。
- [article_035/D027 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_035.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_035.json)　事实 F016。原文证据 E015。
- [article_114/D012 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_114.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_114.json)　事实 F013、F019。原文证据 E008、E009、E022。
- [article_179/D011 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F008。原文证据 E017。
- [article_237/D027 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F028。原文证据 E080、E081。

<a id="evidence-kg_table_fisher"></a>
### KG_TABLE_FISHER

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_table_fisher)

固定边际下精确概率、表维数与单双侧选择及比较单位

- [article_144/D009 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_144.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_144.json)　事实 F010、F021、F022、F025。原文证据 E025、E024、E026、E050、E051、E052、E053、E059、E060、E061、E062、E010、E072。

<a id="evidence-kg_test_mcnemar"></a>
### KG_TEST_MCNEMAR

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_test_mcnemar)

不一致格构造、精确/近似/连续性修正及配对有效性

- [article_048/D016 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_048.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_048.json)　事实 F013。原文证据 E030。
- [article_092/D010 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_092.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_092.json)　事实 F013。原文证据 E010。
- [article_107/D017 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_107.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_107.json)　事实 F015、F016。原文证据 E020、E021、E022。
- [article_114/D013 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_114.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_114.json)　事实 F016。原文证据 E014。

<a id="evidence-worker_3_kg_cramer_v"></a>
### worker_3_KG_CRAMER_V

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_cramer_v)

χ²按样本数与表维度缩放、无方向强度解释及跨品牌权重

- [article_179/D013 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F008。原文证据 E017。

<a id="evidence-kg_test_binomial"></a>
### KG_TEST_BINOMIAL

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_test_binomial)

独立试验单位、零概率、尾侧及精确二项尾判定

- [article_029/D018 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_029.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_029.json)　事实 F013、F014、F016、F020。原文证据 E004、E016、E014、E011、E012、E013、E020、E046、E047、E018、E051。
- [article_040/D023 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_040.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_040.json)　事实 F019。原文证据 E020、E021。
- [article_243/D011 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F012、F015、F041、F044。原文证据 E020、E021、E022、E028、E029、E085、E088。

<a id="evidence-worker_1_kg_exact_multinomial"></a>
### worker_1_KG_EXACT_MULTINOMIAL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_exact_multinomial)

固定总计数下多项事件枚举、零假设PMF及概率排序双侧尾部求和

- [article_243/D012 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F013、F042。原文证据 E023、E024、E086。

<a id="evidence-kg_prec_sem"></a>
### KG_PREC_SEM

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_sem)

均值精度与样本离散的区别；从重复离散到均值SE的计算、有效独立n和相关/不等权的影响

- [article_005/D022 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_005.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_005.json)　事实 F019、F022。原文证据 E010、E017、E012、E023、E024。
- [article_020/D033 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F029、F015。原文证据 E021、E022、E042。
- [article_024/D011 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_024.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_024.json)　事实 F013、F012。原文证据 E009、E010、E030、E032、E033、E036。
- [article_032/D016 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_032.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_032.json)　事实 F014。原文证据 E012、E015、E016。
- [article_039/D018 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_039.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_039.json)　事实 F014。原文证据 E009、E010、E011、E023。
- [article_044/D023 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_044.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_044.json)　事实 F020、F016。原文证据 E014、E022、E028。
- [article_046/D007 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_046.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_046.json)　事实 F007、F008。原文证据 E005、E006、E007。
- [article_065/D014 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_065.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_065.json)　事实 F012、F009。原文证据 E011、E014、E015、E018。
- [article_082/D015 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_082.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_082.json)　事实 F012、F018。原文证据 E007、E013。
- [article_125/D018 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_125.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_125.json)　事实 F017、F018、F024、F030、F031。原文证据 E037、E038、E039、E040、E049、E050、E051、E058、E059、E014、E060、E029、E036、E022、E061。
- [article_141/D018 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_141.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_141.json)　事实 F017、F018、F020、F022、F025、F026。原文证据 E028、E029、E030、E031、E032、E033、E035、E036、E040、E041、E042、E043、E053、E054、E055、E056。
- [article_162/D019 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_162.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_162.json)　事实 F014。原文证据 E031、E032。
- [article_163/D015 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_163.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_163.json)　事实 F011、F016。原文证据 E018、E019、E024。
- [article_167/D020 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_167.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_167.json)　事实 F017、F018、F025。原文证据 E041、E042、E043、E053、E054。
- [article_179/D046 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F030。原文证据 E089、E090。
- [article_197/D018 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_197.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_197.json)　事实 F017。原文证据 E026、E047、E016。
- [article_199/D213 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F002、F004、F012、F019、F020。原文证据 E008、E024、E016、E012。
- [article_205/D014 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_205.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_205.json)　事实 F013。原文证据 E041、E042。
- [article_206/D014 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_206.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_206.json)　事实 F015。原文证据 E037、E038。
- [article_209/D018 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_209.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_209.json)　事实 F016、F025。原文证据 E028、E029、E046、E047、E048、E049。

<a id="evidence-kg_prec_coef"></a>
### KG_PREC_COEF

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_coef)

回归系数抽样方差/标准误、设计与残差假设、稳健或聚类方案的适用区别

- [article_008/D015 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_008.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_008.json)　事实 F011、F018、F019。原文证据 E004、E005、E018、E019、E010、E016、E015、E030、E017。
- [article_073/D013 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_073.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_073.json)　事实 F016。原文证据 E022、E023、E024、E025、E026、E027。

<a id="evidence-kg_prec_cluster"></a>
### KG_PREC_CLUSTER

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_cluster)

聚类方差估计以簇而非簇内观测作独立单位、簇数及小样本修正对精度的影响

- [article_021/D012 · 需求记录 r30](../../../analysis/literature_component_coverage/records/assessments/article_021.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_021.json)　事实 F011。原文证据 E007、E008。

<a id="evidence-kg_prec_tci"></a>
### KG_PREC_TCI

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_tci)

均值SE、t临界值/自由度、独立重复与小样本分布假设如何构成区间

- [article_033/D017 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_033.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_033.json)　事实 F014。原文证据 E009、E027、E031。

<a id="evidence-kg_prec_normal"></a>
### KG_PREC_NORMAL

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_normal)

正态近似区间由点估计加减临界值乘SE构成及适用性、边界和依赖条件

- [article_040/D015 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_040.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_040.json)　事实 F014。原文证据 E033、E009、E010。

<a id="evidence-kg_prec_binom"></a>
### KG_PREC_BINOM

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_binom)

二项比例方差p(1−p)/n、plug-in标准误、边界与独立Bernoulli条件

- [article_018/D023 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_018.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_018.json)　事实 F024。原文证据 E012、E026。
- [article_173/D006 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_173.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_173.json)　事实 F007。原文证据 E017、E018。
- [article_186/D005 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_186.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_186.json)　事实 F005。原文证据 E015、E016、E017、E018。

<a id="evidence-kg_prec_cp"></a>
### KG_PREC_CP

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_cp)

通过二项尾概率反演构造Clopper–Pearson区间、边界情形及保守覆盖与iid前提

- [article_195/D003 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_195.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_195.json)　事实 F004。原文证据 E013、E014、E015。

<a id="evidence-kg_prec_dci"></a>
### KG_PREC_DCI

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_dci)

标准化均差d的特定近似抽样方差、两组样本大小、正态区间和配对依赖边界

- [article_205/D022 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_205.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_205.json)　事实 F021。原文证据 E064、E065、E066。

<a id="evidence-kg_prec_wilson"></a>
### KG_PREC_WILSON

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_wilson)

二项score检验反演成Wilson区间、小样本和0/1边界行为及独立样本前提

- [article_212/D014 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_212.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_212.json)　事实 F015。原文证据 E032。

<a id="evidence-kg_mc_dynamic_baseline"></a>
### KG_MC_DYNAMIC_BASELINE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_mc_dynamic_baseline)

状态转移/库存更新、随机合法行为及随路径重算机会性能

- [article_119/D024 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_119.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_119.json)　事实 F021。原文证据 E021。

<a id="evidence-kg_mc_null_quantile"></a>
### KG_MC_NULL_QUANTILE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_mc_null_quantile)

由随机策略轨迹重算任务分数、构造零分布并取分位数

- [article_145/D025 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_145.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_145.json)　事实 F027。原文证据 E077、E076、E075、E011、E098、E047、E017。

<a id="evidence-kg_permutation_reference"></a>
### KG_PERMUTATION_REFERENCE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_permutation_reference)

交换性与重排单元、保留配对/聚集结构、重算统计量和尾概率

- [article_020/D026 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F026。原文证据 E014、E045。
- [article_055/D017 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_055.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_055.json)　事实 F021。原文证据 E058、E059。
- [article_096/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_096.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_096.json)　事实 F009、F011、F012、F013、F014。原文证据 E004、E005、E007、E008、E015。
- [article_104/D011 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_104.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_104.json)　事实 F007。原文证据 E018、E019。
- [article_121/D015 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F012、F013。原文证据 E021、E022、E023、E024。
- [article_168/D012 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_168.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_168.json)　事实 F013、F015、F016。原文证据 E002、E003、E026、E028、E029。

<a id="evidence-kg_test_permanova"></a>
### KG_TEST_PERMANOVA

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_test_permanova)

距离平方和、组内指标、置换交换性与右尾统计

- [article_048/D019 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_048.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_048.json)　事实 F016。原文证据 E037、E053。

<a id="evidence-kg_bonferroni"></a>
### KG_BONFERRONI

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_bonferroni)

检验族大小与调整p/阈值的计算关系、局部校正的解释范围

- [article_014/D214 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_014.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_014.json)　事实 F006。原文证据 E010、E048。
- [article_154/D020 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_154.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_154.json)　事实 F019、F020、F021。原文证据 E053、E054、E055、E056、E057、E058、E059。
- [article_175/D011 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_175.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_175.json)　事实 F009、F039。原文证据 E014、E015、E101、E102、E103、E104、E105、E106。
- [article_199/D216 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F014。原文证据 E014。
- [article_243/D015 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F014、F015、F026、F043、F044、F060。原文证据 E025、E026、E027、E028、E029、E053、E054、E087、E088、E124、E125。

<a id="evidence-kg_holm"></a>
### KG_HOLM

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_holm)

排序、逐步拒绝或调整p的操作规则及适用条件

- [article_020/D030 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F026、F027、F012。原文证据 E014、E015、E016、E017、E018、E029、E030、E031、E036、E038、E040、E043。
- [article_120/D019 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_120.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_120.json)　事实 F020。原文证据 E024、E034、E035。

<a id="evidence-kg_bh"></a>
### KG_BH

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_bh)

排序、阈值/调整p、拒绝集合及错误发现率的适用解释

- [article_023/D018 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F016、F026。原文证据 E020、E025。
- [article_096/D011 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_096.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_096.json)　事实 F014。原文证据 E004、E007、E008、E015。
- [article_160/D016 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_160.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_160.json)　事实 F012。原文证据 E030。
- [article_166/D028 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_166.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_166.json)　事实 F024、F031。原文证据 E042、E043、E044、E061、E062、E063。

<a id="evidence-kg_fdr_interpretation"></a>
### KG_FDR_INTERPRETATION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_fdr_interpretation)

错误发现率目标及其与家族错误率的区别；不指定未报告算法

- [article_104/D013 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_104.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_104.json)　事实 F008。原文证据 E021、E022、E023、E024、E025。
- [article_121/D025 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F024。原文证据 E039、E040。

<a id="evidence-worker_3_kg_fisher_p_combination"></a>
### worker_3_KG_FISHER_P_COMBINATION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_fisher_p_combination)

−2Σlog(p)的卡方参照、检验数自由度及依赖p值下的适用性

- [article_179/D012 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F008。原文证据 E017。

<a id="evidence-kg_effect_inverse_variance"></a>
### KG_EFFECT_INVERSE_VARIANCE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_effect_inverse_variance)

各效应采样方差、逆方差归一权重、依赖性和合并目标

- [article_003/D319 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_003.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_003.json)　事实 F036、F029。原文证据 E061、E068、E069。

<a id="evidence-kg_effect_standardized_difference"></a>
### KG_EFFECT_STANDARDIZED_DIFFERENCE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_effect_standardized_difference)

配对差SD与独立组pooled SD的选择、方向和解释边界

- [article_014/D215 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_014.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_014.json)　事实 F022、F007。原文证据 E011、E038、E044、E046。
- [article_045/D018 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_045.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_045.json)　事实 F028、F011、F016、F017、F018、F019。原文证据 E042、E035、E040、E011、E015、E016、E017。
- [article_205/D021 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_205.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_205.json)　事实 F020。原文证据 E061、E062、E063。

<a id="evidence-kg_effect_odds_ratio"></a>
### KG_EFFECT_ODDS_RATIO

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_effect_odds_ratio)

优势与概率的区别、参照组方向、零单元及向其他效应尺度转换的假设

- [article_045/D018 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_045.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_045.json)　事实 F028、F011、F016、F017、F018、F019。原文证据 E042、E035、E040、E011、E015、E016、E017。

<a id="evidence-worker_4_gap_reml_meta"></a>
### worker_4_gap_reml_meta

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_4_gap_reml_meta)

用各分类器OR及采样不确定性估计异质方差τ²并作随机效应加权汇总

- [article_175/D023 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_175.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_175.json)　事实 F033。原文证据 E085、E086、E087。

<a id="evidence-worker_5_epsilon_squared_gap"></a>
### worker_5_EPSILON_SQUARED_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_epsilon_squared_gap)

由H、组数k、总N计算(H-k+1)/(N-k)及秩效应的解释边界。

- [article_199/D217 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F014。原文证据 E014。

<a id="evidence-worker_5_rank_biserial_gap"></a>
### worker_5_RANK_BISERIAL_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_rank_biserial_gap)

独立U的1-2U/(n1n2)与配对正负秩和差比两分支、方向及零差并列处理。

- [article_199/D218 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F014。原文证据 E014、E015。

<a id="evidence-kg_reg_linear_fit"></a>
### KG_REG_LINEAR_FIT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_linear_fit)

设计矩阵、截距、线性预测与残差目标的对应，最小二乘求解和秩/拟合适用边界；实例未注明估计准则时不擅填OLS

- [article_008/D013 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_008.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_008.json)　事实 F017、F018、F022。原文证据 E011、E012、E029、E018、E019、E010、E005、E013、E026、E030。
- [article_020/D017 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F014、F015。原文证据 E009、E015、E016、E021、E032、E033。
- [article_047/D023 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F020。原文证据 E053。
- [article_049/D022 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_049.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_049.json)　事实 F020。原文证据 E056、E057、E058。
- [article_085/D023 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_085.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_085.json)　事实 F020。原文证据 E021、E018。
- [article_097/D014 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_097.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_097.json)　事实 F017、F018。原文证据 E010、E011、E020、E021。
- [article_128/D026 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_128.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_128.json)　事实 F026、F027。原文证据 E060、E061、E062、E063、E064、E065、E066。
- [article_135/D012 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_135.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_135.json)　事实 F007、F015、F023、F035。原文证据 E007、E022、E031、E032、E037、E038、E044、E045、E046、E047、E048、E051、E052、E055、E056、E058、E059、E064。
- [article_148/D012 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_148.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_148.json)　事实 F013、F014。原文证据 E029、E030、E031、E032、E033、E034。
- [article_156/D015 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_156.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_156.json)　事实 F016、F022。原文证据 E049、E050、E051、E052、E067、E068、E069、E070。
- [article_165/D024 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_165.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_165.json)　事实 F024、F025。原文证据 E051、E052、E053。
- [article_178/D018 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_178.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_178.json)　事实 F019、F020、F025。原文证据 E049、E050、E051、E052、E053、E063、E064。
- [article_179/D014 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F009。原文证据 E018、E019。
- [article_197/D013 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_197.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_197.json)　事实 F013、F026。原文证据 E040、E041、E055、E056、E057。

<a id="evidence-kg_reg_contrast_matrix"></a>
### KG_REG_CONTRAST_MATRIX

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_contrast_matrix)

sum-to-zero与组内嵌套对比列的构造、参照/权重及截距和系数所对应的比较

- [article_073/D010 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_073.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_073.json)　事实 F015。原文证据 E014、E016。

<a id="evidence-kg_reg_wls_fit"></a>
### KG_REG_WLS_FIT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_wls_fit)

按声明权重最小化加权残差平方和、权重所定义的目标总体和误差解释；人口权重不得自动当逆方差权重

- [article_123/D016 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_123.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_123.json)　事实 F021、F022。原文证据 E009、E039、E040、E041。

<a id="evidence-kg_reg_r2_score"></a>
### KG_REG_R2_SCORE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_r2_score)

残差与基准总变差的R²定义、拟合评价范围及截距/基准影响，区分固定回归R²、混合边际/条件R²和逐项预测准确率

- [article_049/D007 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_049.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_049.json)　事实 F011、F020。原文证据 E041、E042、E056、E057、E058。
- [article_179/D015 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F009。原文证据 E018、E019。

<a id="evidence-kg_reg_logistic_fit"></a>
### KG_REG_LOGISTIC_FIT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_logistic_fit)

二元/分组二项似然、logit链接、系数估计与基线编码、由系数到条件OR及概率的区别

- [article_013/D021 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_013.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_013.json)　事实 F020。原文证据 E026、E029。
- [article_032/D011 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_032.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_032.json)　事实 F012、F024。原文证据 E006、E014、E026、E027。
- [article_073/D009 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_073.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_073.json)　事实 F013、F018、F019。原文证据 E008、E012、E014、E015。
- [article_119/D019 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_119.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_119.json)　事实 F017。原文证据 E014、E016。
- [article_139/D009 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F008。原文证据 E029。
- [article_175/D007 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_175.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_175.json)　事实 F008、F010、F015、F020、F027、F029、F040、F041。原文证据 E013、E016、E024、E025、E026、E035、E036、E070、E071、E072、E075、E076、E077、E107、E108、E109、E110、E111、E112、E113、E114。

<a id="evidence-kg_reg_probit_fit"></a>
### KG_REG_PROBIT_FIT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_probit_fit)

标准正态CDF链接、选择似然与参数拟合、预测量尺度及系数解释

- [article_035/D009 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_035.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_035.json)　事实 F006、F007。原文证据 E004、E011。
- [article_135/D020 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_135.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_135.json)　事实 F019、F020、F032。原文证据 E034、E035、E036、E054、E055、E056、E057、E064、E065。

<a id="evidence-kg_reg_elastic_refit"></a>
### KG_REG_ELASTIC_REFIT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_reg_elastic_refit)

混合L1/L2惩罚与非零预测量选择，再无惩罚重拟合；调参和选择后推断的适用边界

- [article_032/D012 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_032.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_032.json)　事实 F012、F024。原文证据 E006、E014、E026、E027。

<a id="evidence-kg_reg_l2_logistic_fit"></a>
### KG_REG_L2_LOGISTIC_FIT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_l2_logistic_fit)

L2惩罚、类别权重与正则强度的目标函数影响、标准化与调参/留出评价的依赖边界

- [article_243/D028 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F023、F038、F058。原文证据 E046、E047、E079、E080、E081、E122。

<a id="evidence-kg_reg_mixed_fit"></a>
### KG_REG_MIXED_FIT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_mixed_fit)

固定和随机部分联合估计、响应分布与链接、随机效应积分或线性混合ML/REML及比较边界；具体线性/二项变体按实例保留

- [article_007/D015 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_007.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_007.json)　事实 F015。原文证据 E023、E026。
- [article_049/D004 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_049.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_049.json)　事实 F004、F011。原文证据 E014、E015、E041、E042、E030。
- [article_070/D009 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_070.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_070.json)　事实 F010、F011。原文证据 E007、E009、E010。
- [article_092/D011 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_092.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_092.json)　事实 F014。原文证据 E011。
- [article_099/D008 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_099.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_099.json)　事实 F009、F011、F016、F018。原文证据 E005、E007、E008、E010、E016、E018、E019。
- [article_099/D015 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_099.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_099.json)　事实 F015。原文证据 E009、E010。
- [article_106/D011 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_106.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_106.json)　事实 F009、F010。原文证据 E007、E021、E022、E008。
- [article_154/D022 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_154.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_154.json)　事实 F022、F024。原文证据 E060、E063。
- [article_175/D009 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_175.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_175.json)　事实 F010、F013、F015、F016、F020、F038、F039、F040、F041、F042。原文证据 E016、E021、E024、E025、E026、E027、E035、E036、E059、E060、E061、E062、E097、E098、E099、E100、E101、E102、E103、E104、E105、E106、E107、E108、E109、E110、E111、E112、E113、E114、E115、E116、E117、E118。

<a id="evidence-kg_mixed_r2_nakagawa"></a>
### KG_MIXED_R2_NAKAGAWA

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_mixed_r2_nakagawa)

固定部分、随机部分及残差方差的分解和分母，区分边际/条件与OLS解释率；随机斜率和响应尺度影响按适用模型说明

- [article_049/D005 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_049.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_049.json)　事实 F005。原文证据 E016、E017、E018、E019。

<a id="evidence-kg_reg_coef_wald_test"></a>
### KG_REG_COEF_WALD_TEST

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_coef_wald_test)

系数相对假设值与SE之比、z或有限自由度t参照、尾方向和系数对比解释；SE估计知识另归MF21

- [article_073/D013 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_073.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_073.json)　事实 F016。原文证据 E022、E023、E024、E025、E026、E027。

<a id="evidence-kg_reg_model_f_test"></a>
### KG_REG_MODEL_F_TEST

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_model_f_test)

受限/非受限残差平方和与自由度构造F，明确比较目标、误差假设及模型级推断

- [article_165/D025 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_165.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_165.json)　事实 F024、F025。原文证据 E051、E052、E053。

<a id="evidence-kg_model_emm"></a>
### KG_MODEL_EMM

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_model_emm)

参考格、协变量设定与平均权重、响应/链接尺度及系数线性组合形成的边际预测和对比

- [article_099/D011 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_099.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_099.json)　事实 F010、F016。原文证据 E007、E008、E016、E018。

<a id="evidence-kg_model_lrt"></a>
### KG_MODEL_LRT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_model_lrt)

完整/受限模型的似然差、参数自由度与卡方近似条件，顺序加项或删项区别；混合模型ML/REML和边界/选择后推断限制

- [article_032/D013 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_032.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_032.json)　事实 F013、F024、F026。原文证据 E014、E012、E026、E027、E028、E021。
- [article_099/D010 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_099.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_099.json)　事实 F010、F015。原文证据 E007、E008、E009、E010。

<a id="evidence-kg_fit_tjur"></a>
### KG_FIT_TJUR

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_fit_tjur)

Tjur区分系数的观测类别与拟合概率输入、计算定义、有效范围及与OLS/其他伪R²的区别

- [article_073/D014 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_073.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_073.json)　事实 F016。原文证据 E022、E023、E024、E025。

<a id="evidence-kg_reg_bayes_hier_fit"></a>
### KG_REG_BAYES_HIER_FIT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_bayes_hier_fit)

响应似然、分层先验/超先验与部分汇合、后验拟合和后验对比；已注明NUTS时保留其算法身份

- [article_013/D011 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_013.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_013.json)　事实 F010。原文证据 E017、E019。
- [article_133/D016 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_133.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_133.json)　事实 F005、F019、F020、F021、F029。原文证据 E017、E018、E044、E045、E046、E047、E048、E062、E063、E064、E086。

<a id="evidence-kg_reg_bayes_multinom_fit"></a>
### KG_REG_BAYES_MULTINOM_FIT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_reg_bayes_multinom_fit)

pivot识别、非基准类别log-odds、softmax类别概率及分层参数先验与后验估计

- [article_133/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_133.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_133.json)　事实 F016。原文证据 E040、E041、E042。

<a id="evidence-kg_reg_bayes_logodds_weight"></a>
### KG_REG_BAYES_LOGODDS_WEIGHT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_reg_bayes_logodds_weight)

主观后验logit、先验logit及log似然比的测量连接，再以含截距线性拟合识别权重和概率端点边界

- [article_003/D309 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_003.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_003.json)　事实 F007、F008、F009。原文证据 E011、E046、E047、E068。

<a id="evidence-kg_post_nuts_summary"></a>
### KG_POST_NUTS_SUMMARY

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_post_nuts_summary)

NUTS后验抽样与收敛诊断、后验预测生成及参数/预测区间目标区别

- [article_133/D012 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_133.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_133.json)　事实 F017、F018、F019、F020。原文证据 E013、E043、E044、E045、E046、E047、E086。

<a id="evidence-kg_post_gaussian_additive"></a>
### KG_POST_GAUSSIAN_ADDITIVE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_post_gaussian_additive)

明确似然/先验到联合后验的估计及参数约束

- [article_197/D016 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_197.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_197.json)　事实 F015、F016、F026。原文证据 E043、E044、E045、E046、E055、E056、E057。

<a id="evidence-kg_post_contrast_interval"></a>
### KG_POST_CONTRAST_INTERVAL

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_post_contrast_interval)

保留联合后验依赖地取参数差并形成可信区间，解释零点和概率含义

- [article_197/D017 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_197.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_197.json)　事实 F016、F026。原文证据 E044、E045、E046、E055、E056、E057。

<a id="evidence-kg_post_grid_marginal"></a>
### KG_POST_GRID_MARGINAL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_post_grid_marginal)

网格似然与先验归一、干扰参数边缘化及后验均值与网格敏感性

- [article_200/D021 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_200.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_200.json)　事实 F016。原文证据 E047、E048。

<a id="evidence-kg_post_ordered_bayes_factor"></a>
### KG_POST_ORDERED_BAYES_FACTOR

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_post_ordered_bayes_factor)

相等/有序受限参数空间的先验归一、边缘似然及Bayes factor解释

- [article_200/D022 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_200.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_200.json)　事实 F017。原文证据 E049、E050。

<a id="evidence-worker_2_likelihood_chance_gap"></a>
### worker_2_likelihood_chance_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_likelihood_chance_gap)

似然相同观测单位、机会分布参照与拟合优劣解释

- [article_178/D012 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_178.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_178.json)　事实 F013。原文证据 E034、E035。

<a id="evidence-kg_explain_rf_impurity"></a>
### KG_EXPLAIN_RF_IMPURITY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_explain_rf_impurity)

节点不纯度降低的特征归因、树间汇总与尺度/相关特征偏差

- [article_014/D220 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_014.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_014.json)　事实 F024、F006。原文证据 E039、E045、E050。

<a id="evidence-kg_explain_linear_shap"></a>
### KG_EXPLAIN_LINEAR_SHAP

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_explain_linear_shap)

背景分布、线性预测分解及特征依赖假设、局部归因和全局绝对均值的区别

- [article_243/D031 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F025、F059。原文证据 E050、E051、E052、E123。

<a id="evidence-kg_pred_grouped_cv"></a>
### KG_PRED_GROUPED_CV

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_pred_grouped_cv)

组/分层fold构造、训练验证轮换与参数选择、评价数据隔离

- [article_014/D208 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_014.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_014.json)　事实 F013、F023。原文证据 E039、E049、E051、E052。

<a id="evidence-kg_pred_oob_estimate"></a>
### KG_PRED_OOB_ESTIMATE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_pred_oob_estimate)

OOB逐观测未入袋树预测聚合及其与拟合内、CV和外部测试的目标差别

- [article_014/D218 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_014.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_014.json)　事实 F009、F025。原文证据 E042、E043、E052、E053。

<a id="evidence-kg_pred_cv_grid_holdout"></a>
### KG_PRED_CV_GRID_HOLDOUT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_pred_cv_grid_holdout)

分层折、参数网格、预处理归属和选择/评价数据重用的界限

- [article_243/D029 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F023、F024、F058、F059。原文证据 E046、E047、E048、E049、E122、E123。

<a id="evidence-kg_prec_prop"></a>
### KG_PREC_PROP

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_prec_prop)

线性汇总方差/协方差传播、独立近似的含义及非线性/绝对值转换后的精度

- [article_118/D012 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_118.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_118.json)　事实 F013、F014。原文证据 E010、E011、E013、E014。

<a id="evidence-kg_var_binomial_propagation"></a>
### KG_VAR_BINOMIAL_PROPAGATION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_var_binomial_propagation)

plug-in p(1−p)/n、线性变换平方系数及独立职业均值方差

- [article_118/D010 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_118.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_118.json)　事实 F013。原文证据 E010、E011、E013。

<a id="evidence-kg_var_linear_residual"></a>
### KG_VAR_LINEAR_RESIDUAL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_var_linear_residual)

不同概率估计误差合成、plug-in和β稳定化后的残差标准化

- [article_150/D021 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F023、F025。原文证据 E056、E057、E058、E061、E062。
- [article_150/D023 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F026、F038。原文证据 E063、E064、E091、E089、E092、E093。

<a id="evidence-kg_var_delta_residual"></a>
### KG_VAR_DELTA_RESIDUAL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_var_delta_residual)

乘积/总概率展开、梯度系数及截去高阶σ项后的方差

- [article_150/D022 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F024、F027、F038。原文证据 E059、E060、E065、E091、E089、E092、E093。

<a id="evidence-kg_cv_compare"></a>
### KG_CV_COMPARE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_cv_compare)

比率尺度和有意义零点、零/负均值及跨异质数据集/指标比较的限制

- [article_041/D018 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_041.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_041.json)　事实 F016。原文证据 E019、E020、E021、E022、E023。

<a id="evidence-kg_distance_skew"></a>
### KG_DISTANCE_SKEW

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_distance_skew)

相对参照点的成对距离比及对称/退化解释

- [article_058/D006 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_058.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_058.json)　事实 F005、F018、F024。原文证据 E012、E013、E046、E047、E058。

<a id="evidence-kg_density_kde"></a>
### KG_DENSITY_KDE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_density_kde)

核/带宽、边界和归一化后的密度

- [article_023/D020 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F018。原文证据 E032、E033。
- [article_105/D019 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_105.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_105.json)　事实 F014、F015。原文证据 E037、E040、E042。
- [article_177/D018 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F019。原文证据 E037、E038。

<a id="evidence-kg_density_violin"></a>
### KG_DENSITY_VIOLIN

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_density_violin)

密度到对称宽度映射、组间面积缩放及平滑规则

- [article_026/D011 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_026.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_026.json)　事实 F008。原文证据 E004、E015、E016。

<a id="evidence-kg_smooth_lowess"></a>
### KG_SMOOTH_LOWESS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_smooth_lowess)

邻域跨度、距离权重及局部回归/稳健选项

- [article_078/D005 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_078.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_078.json)　事实 F006。原文证据 E006、E007。

<a id="evidence-kg_test_shapiro"></a>
### KG_TEST_SHAPIRO

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_test_shapiro)

有序样本权重和W统计、P值及未拒绝的含义

- [article_107/D011 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_107.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_107.json)　事实 F010。原文证据 E012。

<a id="evidence-kg_fit_normal_distribution"></a>
### KG_FIT_NORMAL_DISTRIBUTION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_fit_normal_distribution)

正态参数估计、密度拟合及拟合优度与适用性检查

- [article_123/D017 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_123.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_123.json)　事实 F023。原文证据 E010、E042。

<a id="evidence-kg_token_label_z"></a>
### KG_TOKEN_LABEL_Z

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_token_label_z)

词频条件概率的零基线、z标准化及多词适用条件

- [article_122/D017 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_122.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_122.json)　事实 F018、F020、F021。原文证据 E036、E037、E039、E040。

<a id="evidence-kg_test_levene"></a>
### KG_TEST_LEVENE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_test_levene)

相对中心的绝对离差变换、组间F检验及依赖/方向解释

- [article_089/D009 · 需求记录 r14](../../../analysis/literature_component_coverage/records/assessments/article_089.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_089.json)　事实 F012。原文证据 E009。
- [article_159/D021 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_159.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_159.json)　事实 F018。原文证据 E041、E042。

<a id="evidence-kg_test_ks"></a>
### KG_TEST_KS

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_test_ks)

经验CDF最大差、一/两样本零分布及参数估计/重复依赖条件

- [article_075/D014 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_075.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_075.json)　事实 F017。原文证据 E012。
- [article_197/D011 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_197.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_197.json)　事实 F011、F025。原文证据 E006、E036、E037、E038、E054。

<a id="evidence-kg_test_runs"></a>
### KG_TEST_RUNS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_test_runs)

二值序列游程数、条件零分布和有限样本/独立性适用

- [article_021/D028 · 需求记录 r30](../../../analysis/literature_component_coverage/records/assessments/article_021.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_021.json)　事实 F027、F028。原文证据 E027、E028。

<a id="evidence-kg_power_correlation"></a>
### KG_POWER_CORRELATION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_power_correlation)

针对目标相关及检验形式的样本量计算与依赖条件

- [article_088/D009 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_088.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_088.json)　事实 F008。原文证据 E009。

<a id="evidence-kg_sampling_gaussian_plugin"></a>
### KG_SAMPLING_GAUSSIAN_PLUGIN

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_sampling_gaussian_plugin)

独立比例方差、正态近似、未知真值代入及误差阶次

- [article_150/D020 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F022。原文证据 E054、E055。

<a id="evidence-kg_gaussian_rejection_quantile"></a>
### KG_GAUSSIAN_REJECTION_QUANTILE

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_gaussian_rejection_quantile)

双侧临界分位数与单侧区分及近似零模型下有效性

- [article_150/D024 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F028、F019。原文证据 E045、E046、E066、E067。

<a id="evidence-kg_test_tost"></a>
### KG_TEST_TOST

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_test_tost)

实质等效界及两单侧零假设的联合拒绝

- [article_023/D015 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F014。原文证据 E017、E029。

<a id="evidence-kg_univariate_f_select"></a>
### KG_UNIVARIATE_F_SELECT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_univariate_f_select)

单变量回归的F统计构造及其单变量选择解释

- [article_135/D031 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_135.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_135.json)　事实 F021。原文证据 E006、E009、E049、E050、E059、E061、E062、E063、E064、E065。

<a id="evidence-kg_select_aic"></a>
### KG_SELECT_AIC

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_select_aic)

似然/参数惩罚及候选路径比较

- [article_073/D012 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_073.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_073.json)　事实 F014。原文证据 E014。

<a id="evidence-kg_select_bic"></a>
### KG_SELECT_BIC

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_select_bic)

样本量惩罚、有效参数个数及同数据候选可比性

- [article_243/D014 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F014、F015、F043。原文证据 E025、E026、E027、E028、E029、E087。

<a id="evidence-worker_2_constrained_lrt_gap"></a>
### worker_2_constrained_lrt_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_constrained_lrt_gap)

等概率高/低项约束备择的合法拟合、候选迭代删除与停止及选择后解释；一般似然比统计量和参照分布共用既有MODEL_LRT。

- [article_243/D013 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F014、F043。原文证据 E025、E026、E027、E087。

<a id="evidence-worker_2_bartlett_gap"></a>
### worker_2_bartlett_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_bartlett_gap)

相关矩阵行列式球形假设、样本量修正统计量与自由度及适切性解释

- [article_229/D027 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_229.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_229.json)　事实 F027。原文证据 E063。

<a id="evidence-worker_3_kg_minres_varimax_efa"></a>
### worker_3_KG_MINRES_VARIMAX_EFA

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_3_kg_minres_varimax_efa)

MINRES共同方差提取、保留维度和Varimax旋转载荷的操作及解释；球形性预检由独立Bartlett知识条目承接。

- [article_229/D028 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_229.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_229.json)　事实 F027、F028。原文证据 E063、E064、E065。

<a id="evidence-kg_cohen"></a>
### KG_COHEN

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_cohen)

观察一致Po与类别边际机会一致Pe、κ校正和基率解释

- [article_049/D011 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_049.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_049.json)　事实 F011、F022。原文证据 E041、E043、E063、E064、E065。
- [article_051/D011 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_051.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_051.json)　事实 F013。原文证据 E036、E037、E038。
- [article_097/D005 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_097.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_097.json)　事实 F004。原文证据 E003、E013、E015。
- [article_100/D011 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F008、F011。原文证据 E008、E009。
- [article_138/D022 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_138.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_138.json)　事实 F022。原文证据 E026、E027、E028、E029。
- [article_149/D013 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_149.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_149.json)　事实 F011。原文证据 E025、E026。
- [article_171/D013 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_171.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_171.json)　事实 F010。原文证据 E031、E032。
- [article_213/D016 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_213.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_213.json)　事实 F017、F018。原文证据 E038、E039、E033。

<a id="evidence-kg_cohen_mean"></a>
### KG_COHEN_MEAN

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_cohen_mean)

各评分者对的机会一致模型及两两κ聚合的重叠样本/权重含义

- [article_050/D010 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_050.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_050.json)　事实 F010。原文证据 E034、E035、E036。
- [article_080/D006 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_080.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_080.json)　事实 F006。原文证据 E016。

<a id="evidence-kg_weighted"></a>
### KG_WEIGHTED

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_weighted)

等级差权重进入观察/机会一致的规则及两两系数聚合解释

- [article_019/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_019.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_019.json)　事实 F011、F012。原文证据 E007、E014。

<a id="evidence-kg_fleiss"></a>
### KG_FLEISS

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_fleiss)

题内类别计数和总体边际下的机会一致、多人聚合及共同标注结构

- [article_050/D009 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_050.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_050.json)　事实 F010。原文证据 E034、E035、E036。
- [article_059/D016 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_059.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_059.json)　事实 F019。原文证据 E052。
- [article_069/D006 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_069.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_069.json)　事实 F009。原文证据 E009。

<a id="evidence-kg_rel_fleiss"></a>
### KG_REL_FLEISS

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_fleiss)

题内成对一致、总体类别边际机会一致及κ校正

- [article_081/D005 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_081.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_081.json)　事实 F004。原文证据 E013。
- [article_180/D013 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_180.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_180.json)　事实 F014。原文证据 E036。
- [article_185/D007 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_185.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_185.json)　事实 F007、F020、F022。原文证据 E019、E020、E050、E051、E054、E080。
- [article_214/D008 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_214.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_214.json)　事实 F010。原文证据 E018、E019。

<a id="evidence-kg_gwet"></a>
### KG_GWET

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_gwet)

所命名机会校正系数的机会模型、适用尺度及与原始一致率的区别；实际算法变体待原文明确

- [article_054/D009 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_054.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_054.json)　事实 F011。原文证据 E030、E031。

<a id="evidence-kg_kappa_family"></a>
### KG_KAPPA_FAMILY

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_kappa_family)

机会一致校正和评分者/类别结构对解释的影响；具体κ变体不从人数推定

- [article_067/D011 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_067.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_067.json)　事实 F010。原文证据 E009。
- [article_075/D021 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_075.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_075.json)　事实 F021。原文证据 E012、E013。

<a id="evidence-kg_alpha"></a>
### KG_ALPHA

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_alpha)

观察/期望分歧、测量尺度距离及不完整重叠标注的处理规则

- [article_048/D009 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_048.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_048.json)　事实 F008。原文证据 E007、E021。
- [article_053/D014 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_053.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_053.json)　事实 F015。原文证据 E050、E051。
- [article_062/D006 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_062.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_062.json)　事实 F008。原文证据 E020、E021、E022。

<a id="evidence-kg_rel_krippendorff"></a>
### KG_REL_KRIPPENDORFF

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_krippendorff)

观察/期望分歧构造、距离尺度、缺失评定及1−Do/De

- [article_112/D004 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_112.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_112.json)　事实 F005。原文证据 E005、E014、E027、E028。
- [article_176/D016 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_176.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_176.json)　事实 F019。原文证据 E040。
- [article_219/D025 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_219.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_219.json)　事实 F021、F022。原文证据 E057、E058、E059、E060、E061、E062、E063、E064。

<a id="evidence-kg_rel_icc"></a>
### KG_REL_ICC

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_icc)

随机/固定评者、绝对一致/一致性、单次/平均形式及方差比和区间

- [article_220/D006 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_220.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_220.json)　事实 F006。原文证据 E011。

<a id="evidence-kg_rel_cronbach"></a>
### KG_REL_CRONBACH

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_cronbach)

条目/观测矩阵、方差协方差与总分公式、误差/同质性解释边界

- [article_029/D023 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_029.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_029.json)　事实 F019。原文证据 E018、E054。
- [article_088/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_088.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_088.json)　事实 F010。原文证据 E018。
- [article_220/D005 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_220.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_220.json)　事实 F006。原文证据 E011。

<a id="evidence-kg_rel_spearman_brown"></a>
### KG_REL_SPEARMAN_BROWN

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_spearman_brown)

随机分半、两半强度相关及2r/(1+r)校正与假设

- [article_103/D005 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_103.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_103.json)　事实 F004。原文证据 E009、E010。

<a id="evidence-kg_rel_split_correlation"></a>
### KG_REL_SPLIT_CORRELATION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_split_correlation)

分割单位、每半重建频数/相关矩阵及相应向量相关信度

- [article_047/D015 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F013、F014、F016。原文证据 E035、E036、E037、E038、E043、E044、E045。

<a id="evidence-kg_rel_matched_fisher_mean"></a>
### KG_REL_MATCHED_FISHER_MEAN

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_matched_fisher_mean)

最大相关维度匹配、r-to-z平均反变换及匹配选择影响

- [article_121/D010 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F010。原文证据 E017。

<a id="evidence-kg_rel_attenuation"></a>
### KG_REL_ATTENUATION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_attenuation)

两系统分半信度的几何均值除法及低信度适用边界

- [article_121/D013 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F011。原文证据 E018、E019、E020。

<a id="evidence-kg_rel_noise_ceiling"></a>
### KG_REL_NOISE_CEILING

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_rel_noise_ceiling)

ncsnr²/(ncsnr²+1/n)及百分比尺度下预测R²归一

- [article_121/D024 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F023、F024。原文证据 E038、E039、E040。

<a id="evidence-kg_cosine"></a>
### KG_COSINE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cosine)

点积/范数归一、零向量边界、相似与距离的方向及其对模长不敏感的含义；保持向量坐标可比

- [article_025/D007 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_025.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_025.json)　事实 F009。原文证据 E007。
- [article_027/D011 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_027.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_027.json)　事实 F010、F024。原文证据 E009、E027、E031、E032、E030。
- [article_033/D004 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_033.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_033.json)　事实 F005。原文证据 E026。
- [article_035/D021 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_035.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_035.json)　事实 F013。原文证据 E008、E015。
- [article_045/D025 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_045.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_045.json)　事实 F025。原文证据 E028、E029、E030。
- [article_047/D025 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F021、F023。原文证据 E055、E056、E057。
- [article_054/D012 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_054.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_054.json)　事实 F013。原文证据 E035、E036、E037。
- [article_080/D017 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_080.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_080.json)　事实 F017、F018。原文证据 E013、E014。
- [article_091/D004 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_091.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_091.json)　事实 F004。原文证据 E003、E004、E005、E006。
- [article_098/D010 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_098.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_098.json)　事实 F009。原文证据 E003。
- [article_100/D008 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F007、F016。原文证据 E007、E013、E025。
- [article_104/D006 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_104.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_104.json)　事实 F005、F011。原文证据 E010、E011、E012、E013、E014、E032、E033、E034。
- [article_118/D014 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_118.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_118.json)　事实 F016。原文证据 E015、E016。
- [article_121/D007 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F007、F022、F027、F029、F030。原文证据 E014、E037、E003、E046、E047、E048、E049。
- [article_127/D006 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F006。原文证据 E010。
- [article_139/D016 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F015。原文证据 E013、E028、E041。
- [article_139/D024 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F021、F022。原文证据 E018、E031、E032、E019。
- [article_145/D013 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_145.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_145.json)　事实 F013。原文证据 E038、E039、E040、E099、E043。
- [article_151/D010 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_151.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_151.json)　事实 F012、F024。原文证据 E034、E035、E036、E019、E053、E054。
- [article_154/D010 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_154.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_154.json)　事实 F008、F029、F032。原文证据 E030、E031、E032、E033、E071、E072、E076、E077。
- [article_159/D017 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_159.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_159.json)　事实 F014。原文证据 E033。
- [article_169/D017 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_169.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_169.json)　事实 F018。原文证据 E044、E045。
- [article_171/D009 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_171.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_171.json)　事实 F008。原文证据 E027、E028、E029。
- [article_179/D007 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F005、F006、F029。原文证据 E009、E010、E011、E012、E013、E086、E087、E088。
- [article_190/D011 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_190.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_190.json)　事实 F007。原文证据 E005、E051。
- [article_191/D006 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_191.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_191.json)　事实 F006、F008。原文证据 E031、E034、E035。
- [article_192/D007 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_192.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_192.json)　事实 F007、F021。原文证据 E025、E023、E024、E061、E062。
- [article_210/D020 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_210.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_210.json)　事实 F023。原文证据 E050、E051。
- [article_213/D005 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_213.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_213.json)　事实 F006、F007。原文证据 E017、E018、E019、E020、E021。
- [article_219/D005 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_219.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_219.json)　事实 F004、F005、F006、F007。原文证据 E011、E012、E013、E014、E015、E016。
- [article_223/D004 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F004、F005。原文证据 E009、E010、E011、E012。
- [article_237/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F013。原文证据 E037、E038、E039、E040。
- [article_243/D020 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F020、F055。原文证据 E042、E118。

<a id="evidence-kg_cosine_semantic"></a>
### KG_COSINE_SEMANTIC

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cosine_semantic)

句/词/图文表示的输入与参照对应、池化/配对或最近邻归约、阈值语义与表示依赖；不要求本研究重训编码器

- [article_025/D007 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_025.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_025.json)　事实 F009。原文证据 E007。
- [article_027/D011 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_027.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_027.json)　事实 F010、F024。原文证据 E009、E027、E031、E032、E030。
- [article_035/D021 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_035.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_035.json)　事实 F013。原文证据 E008、E015。
- [article_054/D012 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_054.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_054.json)　事实 F013。原文证据 E035、E036、E037。
- [article_080/D017 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_080.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_080.json)　事实 F017、F018。原文证据 E013、E014。
- [article_091/D004 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_091.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_091.json)　事实 F004。原文证据 E003、E004、E005、E006。
- [article_098/D010 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_098.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_098.json)　事实 F009。原文证据 E003。
- [article_100/D008 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F007、F016。原文证据 E007、E013、E025。
- [article_118/D014 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_118.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_118.json)　事实 F016。原文证据 E015、E016。
- [article_120/D011 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_120.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_120.json)　事实 F014。原文证据 E031、E032、E033。
- [article_127/D006 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F006。原文证据 E010。
- [article_145/D013 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_145.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_145.json)　事实 F013。原文证据 E038、E039、E040、E099、E043。
- [article_151/D010 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_151.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_151.json)　事实 F012、F024。原文证据 E034、E035、E036、E019、E053、E054。
- [article_154/D010 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_154.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_154.json)　事实 F008、F029、F032。原文证据 E030、E031、E032、E033、E071、E072、E076、E077。
- [article_159/D017 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_159.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_159.json)　事实 F014。原文证据 E033。
- [article_171/D009 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_171.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_171.json)　事实 F008。原文证据 E027、E028、E029。
- [article_179/D007 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F005、F006、F029。原文证据 E009、E010、E011、E012、E013、E086、E087、E088。
- [article_190/D011 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_190.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_190.json)　事实 F007。原文证据 E005、E051。
- [article_210/D020 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_210.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_210.json)　事实 F023。原文证据 E050、E051。
- [article_213/D005 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_213.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_213.json)　事实 F006、F007。原文证据 E017、E018、E019、E020、E021。
- [article_219/D005 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_219.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_219.json)　事实 F004、F005、F006、F007。原文证据 E011、E012、E013、E014、E015、E016。
- [article_223/D004 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F004、F005。原文证据 E009、E010、E011、E012。
- [article_237/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F013。原文证据 E037、E038、E039、E040。
- [article_243/D020 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F020、F055。原文证据 E042、E118。

<a id="evidence-kg_frozen_representation"></a>
### KG_FROZEN_REPRESENTATION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_frozen_representation)

区分token/词/句表征，实际编码读出、池化/归一和OOV处理

- [article_042/D006 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F007。原文证据 E004。
- [article_042/D018 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F014。原文证据 E015、E004。
- [article_047/D027 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F027。原文证据 E005、E063、E064。
- [article_048/D003 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_048.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_048.json)　事实 F004、F015。原文证据 E013、E035、E036、E003。
- [article_054/D011 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_054.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_054.json)　事实 F013。原文证据 E035、E036、E037。
- [article_170/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_170.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_170.json)　事实 F009。原文证据 E032、E033。
- [article_177/D015 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F015、F016。原文证据 E030、E031、E032。
- [article_196/D004 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_196.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_196.json)　事实 F010、F011、F012。原文证据 E034、E035、E036、E037、E038、E012、E032。
- [article_202/D006 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_202.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_202.json)　事实 F012。原文证据 E020、E021。
- [article_237/D009 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F012。原文证据 E033、E034、E035、E036。
- [article_238/D008 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_238.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_238.json)　事实 F009。原文证据 E030、E031、E032、E033。

<a id="evidence-kg_dependency"></a>
### KG_DEPENDENCY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dependency)

依存解析的关系标签表示、匹配单位及句法重叠的解释

- [article_070/D016 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_070.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_070.json)　事实 F018、F019。原文证据 E016、E017、E020。

<a id="evidence-kg_lemma"></a>
### KG_LEMMA

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_lemma)

屈折到词元的形态归一、上下文歧义和多词边界

- [article_078/D012 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_078.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_078.json)　事实 F014。原文证据 E011。

<a id="evidence-kg_contig"></a>
### KG_CONTIG

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_contig)

最长共享连续片段的匹配规则、单位及与平均n-gram重合的区别

- [article_027/D029 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_027.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_027.json)　事实 F023。原文证据 E028、E029、E033。
- [article_042/D017 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F014、F022。原文证据 E015、E004、E024、E027。

<a id="evidence-kg_lcs"></a>
### KG_LCS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_lcs)

保持顺序而允许非连续的公共子序列、匹配长度与连续片段的区别及相应归一

- [article_127/D008 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F008。原文证据 E013、E014、E015。
- [article_155/D013 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_155.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_155.json)　事实 F006、F008、F012、F014、F017、F018、F022、F025、F027。原文证据 E026、E027、E032、E040、E041、E047、E054、E055、E056、E057、E064、E065、E071、E072、E076、E077。
- [article_165/D005 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_165.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_165.json)　事实 F010。原文证据 E014、E022、E023。

<a id="evidence-kg_span"></a>
### KG_SPAN

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_span)

标注span边界与类型同时匹配、单位和重复/重叠候选如何形成TP/FP/FN

- [article_065/D011 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_065.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_065.json)　事实 F010。原文证据 E016、E017。

<a id="evidence-kg_bleu"></a>
### KG_BLEU

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_bleu)

参考约束的n-gram计数裁剪、各阶精确率组合、长度惩罚，以及句级/语料级聚合与零匹配处理的区别

- [article_011/D016 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_011.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_011.json)　事实 F015。原文证据 E024。
- [article_110/D022 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_110.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_110.json)　事实 F015。原文证据 E005、E025、E026。
- [article_134/D015 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_134.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_134.json)　事实 F013、F016、F017。原文证据 E004、E005、E007、E017、E027、E028、E030、E049。
- [article_165/D022 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_165.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_165.json)　事实 F027。原文证据 E056、E057。
- [article_179/D023 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F015。原文证据 E042、E043、E044。
- [article_223/D015 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F011。原文证据 E021。

<a id="evidence-kg_rouge_l"></a>
### KG_ROUGE_L

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_rouge_l)

最长公共子序列匹配与连续片段区别、序列长度归一及P/R/F归约；明确句级/摘要级变体

- [article_068/D220 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_068.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_068.json)　事实 F026。原文证据 E053、E054。
- [article_179/D024 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F015。原文证据 E042、E043、E044。
- [article_224/D025 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_224.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_224.json)　事实 F023。原文证据 E064、E065。
- [article_242/D014 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_242.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_242.json)　事实 F026、F055。原文证据 E054、E055、E128、E129、E130、E131。

<a id="evidence-kg_chrf_pp"></a>
### KG_CHRF_PP

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_chrf_pp)

字符及词n-gram计数、各阶P/R聚合与F权重、字符/词边界及句级/语料级配置

- [article_165/D021 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_165.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_165.json)　事实 F012、F014、F015、F016、F021、F022。原文证据 E027、E028、E029、E014、E033、E034、E035、E036、E037、E018、E038、E044、E045、E046。

<a id="evidence-worker_1_kg_meteor"></a>
### worker_1_KG_METEOR

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_meteor)

词匹配与对齐、对齐精确召回组合及片段惩罚机制

- [article_110/D023 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_110.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_110.json)　事实 F015。原文证据 E005、E025、E026。

<a id="evidence-worker_5_bertscore_gap"></a>
### worker_5_BERTSCORE_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_bertscore_gap)

上下文词元相似矩阵、方向最大匹配及precision/recall/F1归约和尺度解释。

- [article_068/D221 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_068.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_068.json)　事实 F026。原文证据 E053、E054。
- [article_110/D021 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_110.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_110.json)　事实 F015。原文证据 E005、E025、E026。
- [article_149/D021 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_149.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_149.json)　事实 F018。原文证据 E036、E037、E038。
- [article_179/D025 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F015。原文证据 E042、E043、E044。
- [article_196/D021 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_196.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_196.json)　事实 F005、F006、F020。原文证据 E005、E028、E029、E053、E048。
- [article_223/D018 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F012。原文证据 E022、E023、E024。

<a id="evidence-kg_simcse_score"></a>
### KG_SIMCSE_SCORE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_simcse_score)

现成编码器评分的参考单位、相似度输出/阈值意义及语义相近与事实保真的区别；底层具体度量以实际报告为准

- [article_012/D018 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_012.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_012.json)　事实 F020。原文证据 E030、E033。

<a id="evidence-kg_bleurt"></a>
### KG_BLEURT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_bleurt)

参考/候选译文的配对、连续学习式分数的解释及与真实人评量尺的区别；额外标定另列

- [article_058/D010 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_058.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_058.json)　事实 F010。原文证据 E025、E026、E027。
- [article_076/D003 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_076.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_076.json)　事实 F002、F031。原文证据 E008、E015、E021、E022、E030。

<a id="evidence-kg_unieval"></a>
### KG_UNIEVAL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_unieval)

现成评分器各维度的输入、输出归约与适用解释，区分流畅/可懂与忠实性/总体质量

- [article_058/D018 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_058.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_058.json)　事实 F021。原文证据 E053、E054。

<a id="evidence-worker_1_kg_blanc"></a>
### worker_1_KG_BLANC

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_blanc)

无摘要与有摘要的匹配mask预测比较、帮助增益归约及任务解释边界

- [article_224/D026 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_224.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_224.json)　事实 F024。原文证据 E066、E067、E068。

<a id="evidence-worker_5_supert_gap"></a>
### worker_5_SUPERT_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_supert_gap)

从长源文构造伪参考及摘要语义匹配归约，区别BERTScore直接给定人工参照。

- [article_224/D027 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_224.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_224.json)　事实 F024。原文证据 E066、E067、E068。

<a id="evidence-kg_nli_relation_interpretation"></a>
### KG_NLI_RELATION_INTERPRETATION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_nli_relation_interpretation)

明确前提/假设方向及entailment、neutral、contradiction的区别，并把标签连接到当前文本对或候选过滤；区分文本内部支持与外部事实真值。

- [article_015/D022 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_015.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_015.json)　事实 F021。原文证据 E028。
- [article_027/D010 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_027.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_027.json)　事实 F009。原文证据 E008。
- [article_146/D003 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_146.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_146.json)　事实 F004、F006。原文证据 E008、E009、E014。
- [article_161/D007 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_161.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_161.json)　事实 F005。原文证据 E012、E013。

<a id="evidence-kg_nli_zero_shot_bridge"></a>
### KG_NLI_ZERO_SHOT_BRIDGE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_nli_zero_shot_bridge)

把待分类文本与类别含义转换为NLI前提/假设并从关系输出形成类别评分，明确多语标签语义与实际拒答的区别。

- [article_048/D014 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_048.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_048.json)　事实 F012。原文证据 E029。

<a id="evidence-kg_factive_diagnostic"></a>
### KG_FACTIVE_DIAGNOSTIC

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_factive_diagnostic)

区分事实性动词触发的嵌入命题承诺与表层是非问句的回答极性，并据此解释拒绝错误预设和仅否认主句的不同；不同触发词的投射边界不能由模板名称推定相同。

- [article_050/D004 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_050.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_050.json)　事实 F005。原文证据 E016、E017、E018。

<a id="evidence-kg_tfidf_weighting"></a>
### KG_TFIDF_WEIGHTING

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_tfidf_weighting)

文档频率与局部词频的区别、参照文档集合、逆文档频率加权及其与语料差异的解释边界。

- [article_033/D004 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_033.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_033.json)　事实 F005。原文证据 E026。
- [article_047/D028 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F027。原文证据 E064、E063。

<a id="evidence-worker_4_gap_bm25"></a>
### worker_4_gap_bm25

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_bm25)

基于词频饱和、IDF与文档长度归一形成BM25排序并截取候选集

- [article_091/D006 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_091.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_091.json)　事实 F005。原文证据 E003、E006。
- [article_127/D005 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F005。原文证据 E009。
- [article_235/D044 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F032。原文证据 E075、E076、E077。

<a id="evidence-worker_3_kg_vector_neighbor_retrieval"></a>
### worker_3_KG_VECTOR_NEIGHBOR_RETRIEVAL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_vector_neighbor_retrieval)

查询/存储表征对应、近邻排序与索引近似、返回片段及context装配边界

- [article_103/D007 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_103.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_103.json)　事实 F005。原文证据 E011。
- [article_177/D010 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F010。原文证据 E021、E022。
- [article_177/D015 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F015、F016。原文证据 E030、E031、E032。
- [article_202/D006 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_202.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_202.json)　事实 F012。原文证据 E020、E021。
- [article_242/D018 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_242.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_242.json)　事实 F031、F032。原文证据 E063、E064。

<a id="evidence-worker_2_corpus_query_gap"></a>
### worker_2_corpus_query_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_corpus_query_gap)

索引查询的token/文档单位、精确与近似返回边界及存在性/共现计数取得接口

- [article_072/D013 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_072.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_072.json)　事实 F015、F016。原文证据 E006、E008、E014、E015。
- [article_127/D004 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F005。原文证据 E009。
- [article_223/D006 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F007。原文证据 E014、E015。

<a id="evidence-worker_2_ngram_backoff_gap"></a>
### worker_2_ngram_backoff_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_ngram_backoff_gap)

查询最长存在前缀、零计数逐级回退及条件频率链的构造

- [article_223/D019 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F013。原文证据 E025。

<a id="evidence-worker_2_suffix_index_gap"></a>
### worker_2_suffix_index_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_suffix_index_gap)

后缀数组的相邻有序位置比较、重复桶范围与完整序列成员查询

- [article_239/D004 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_239.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_239.json)　事实 F005。原文证据 E012、E013。
- [article_239/D011 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_239.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_239.json)　事实 F011。原文证据 E028、E029、E030。

<a id="evidence-worker_4_gap_substring_twopointer"></a>
### worker_4_gap_substring_twopointer

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_substring_twopointer)

匹配时推进j、不匹配推进i并j=max(i+L,j)、利用子串闭包复用查询结果

- [article_127/D003 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F004。原文证据 E007、E008。

<a id="evidence-worker_4_gap_span_prefix_search"></a>
### worker_4_gap_span_prefix_search

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_span_prefix_search)

缓存已得词向量匹配分数及其连续和，遍历长度至少L的连续跨度，并按两向阈值判定返回结果及分析查询成本。

- [article_127/D007 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F007。原文证据 E011、E012。

<a id="evidence-kg_dirichlet_word_logodds"></a>
### KG_DIRICHLET_WORD_LOGODDS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dirichlet_word_logodds)

informative先验计数、后验log-odds差及方差z标准化

- [article_039/D006 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_039.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_039.json)　事实 F007。原文证据 E004。

<a id="evidence-worker_3_kg_lexicon_sentiment"></a>
### worker_3_KG_LEXICON_SENTIMENT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_lexicon_sentiment)

词项极性/强度、否定和组合规则、工具输出尺度与阈值的对应

- [article_039/D014 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_039.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_039.json)　事实 F012、F019。原文证据 E012、E021、E022。
- [article_064/D008 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_064.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_064.json)　事实 F009。原文证据 E017。
- [article_175/D015 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_175.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_175.json)　事实 F015、F017、F030。原文证据 E024、E025、E026、E028、E029、E030、E031、E078、E079、E080。
- [article_197/D008 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_197.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_197.json)　事实 F009。原文证据 E031、E032。

<a id="evidence-worker_2_flesch_gap"></a>
### worker_2_flesch_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_flesch_gap)

Reading Ease与Kincaid Grade的不同系数/方向、句词音节输入及年级/易度解释

- [article_042/D013 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F014。原文证据 E015、E004。
- [article_067/D006 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_067.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_067.json)　事实 F005。原文证据 E032、E033。
- [article_243/D019 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F019、F054。原文证据 E041、E117。

<a id="evidence-worker_2_ari_gap"></a>
### worker_2_ari_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_ari_gap)

字符/词/句比例的ARI计分及量尺解释

- [article_064/D006 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_064.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_064.json)　事实 F008。原文证据 E016。

<a id="evidence-worker_2_fog_gap"></a>
### worker_2_fog_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_fog_gap)

句长与复杂词比例的组合及音节/例外词规则

- [article_197/D009 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_197.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_197.json)　事实 F009。原文证据 E031、E032。

<a id="evidence-worker_5_readability_consensus_gap"></a>
### worker_5_READABILITY_CONSENSUS_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_readability_consensus_gap)

将多个已得可读性量尺组合为学校年级共识，明确参与成员、量尺转换与聚合；各基础量尺公式共用既有条目，原文未报默认成员不能补猜。

- [article_035/D030 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_035.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_035.json)　事实 F027。原文证据 E034。

<a id="evidence-worker_5_lexical_types_gap"></a>
### worker_5_LEXICAL_TYPES_gap

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_5_lexical_types_gap)

HPSG/ERG词汇类型层级、补语选择及同表面词mass-count行为的对应。

- [article_104/D019 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_104.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_104.json)　事实 F016。原文证据 E047、E048、E049。

<a id="evidence-kg_prob_token_read"></a>
### KG_PROB_TOKEN_READ

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_token_read)

把候选文字与token身份、预测位置和条件前缀绑定；区分logprob、概率和logit，区分真实返回候选与缺失/截断值，说明读数对应的响应事件。

- [article_002/D008 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_002.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_002.json)　事实 F008。原文证据 E011、E015。
- [article_007/D013 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_007.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_007.json)　事实 F011。原文证据 E007。
- [article_021/D006 · 需求记录 r30](../../../analysis/literature_component_coverage/records/assessments/article_021.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_021.json)　事实 F007。原文证据 E003。
- [article_022/D007 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_022.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_022.json)　事实 F010、F021。原文证据 E009、E003、E019。
- [article_035/D004 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_035.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_035.json)　事实 F004。原文证据 E003、E004。
- [article_037/D009 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_037.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_037.json)　事实 F008、F031。原文证据 E008、E047。
- [article_038/D023 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_038.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_038.json)　事实 F023。原文证据 E021、E023。
- [article_042/D009 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F011。原文证据 E012、E014、E016、E017、E018。
- [article_042/D022 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F017。原文证据 E008、E019。
- [article_044/D008 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_044.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_044.json)　事实 F009。原文证据 E001、E006、E020。
- [article_044/D009 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_044.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_044.json)　事实 F009。原文证据 E007。
- [article_060/D004 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_060.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_060.json)　事实 F005、F006。原文证据 E017、E018、E019、E020、E021。
- [article_063/D009 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_063.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_063.json)　事实 F009。原文证据 E011。
- [article_083/D006 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_083.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_083.json)　事实 F007。原文证据 E008、E009。
- [article_085/D004 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_085.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_085.json)　事实 F005。原文证据 E006。
- [article_086/D004 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_086.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_086.json)　事实 F005。原文证据 E003、E004。
- [article_093/D008 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_093.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_093.json)　事实 F008。原文证据 E007、E021。
- [article_095/D013 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_095.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_095.json)　事实 F019。原文证据 E021、E022。
- [article_099/D004 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_099.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_099.json)　事实 F007、F011。原文证据 E004、E008、E010。
- [article_116/D008 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_116.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_116.json)　事实 F007。原文证据 E001、E002。
- [article_117/D009 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_117.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_117.json)　事实 F008、F009。原文证据 E005、E022、E024。
- [article_139/D003 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F004、F006。原文证据 E003、E004、E005、E006、E015。
- [article_143/D004 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F005。原文证据 E010、E011。
- [article_157/D015 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_157.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_157.json)　事实 F019、F020。原文证据 E007、E034、E069、E070、E071、E072。
- [article_158/D004 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_158.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_158.json)　事实 F005。原文证据 E009。
- [article_167/D012 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_167.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_167.json)　事实 F013、F020。原文证据 E009、E011。
- [article_168/D018 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_168.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_168.json)　事实 F019。原文证据 E034、E035、E036。
- [article_173/D027 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_173.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_173.json)　事实 F005、F038。原文证据 E014、E015、E101、E102、E103。
- [article_188/D020 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_188.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_188.json)　事实 F016。原文证据 E051、E052、E053。
- [article_189/D006 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_189.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_189.json)　事实 F005、F007。原文证据 E021、E022、E025、E026。
- [article_193/D008 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_193.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_193.json)　事实 F007、F009。原文证据 E004、E026、E030、E031、E032、E033。
- [article_205/D011 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_205.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_205.json)　事实 F011。原文证据 E034、E035、E036、E037。
- [article_207/D004 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_207.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_207.json)　事实 F005、F009。原文证据 E009、E016、E017。
- [article_208/D006 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_208.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_208.json)　事实 F007、F008、F009。原文证据 E015、E016、E017、E018。
- [article_225/D004 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_225.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_225.json)　事实 F005。原文证据 E014、E015、E016。
- [article_226/D006 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_226.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_226.json)　事实 F008、F009。原文证据 E015、E016、E017。
- [article_231/D006 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_231.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_231.json)　事实 F003、F004、F005、F026。原文证据 E005、E006、E007、E046、E047。
- [article_238/D013 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_238.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_238.json)　事实 F013。原文证据 E043、E044、E045。
- [article_243/D022 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_243.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_243.json)　事实 F021、F045、F046。原文证据 E043、E089、E090、E091、E092。

<a id="evidence-kg_prob_arch_head"></a>
### KG_PROB_ARCH_HEAD

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_arch_head)

按decoder下一位置、encoder mask位置、encoder-decoder sentinel及decoder目标定位读出；保持对应条件上下文和token身份。

- [article_020/D005 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F005。原文证据 E024。
- [article_072/D006 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_072.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_072.json)　事实 F006、F007。原文证据 E003、E004、E020。
- [article_136/D004 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_136.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_136.json)　事实 F008、F009。原文证据 E021、E022、E023。
- [article_159/D006 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_159.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_159.json)　事实 F006。原文证据 E013、E014。
- [article_188/D009 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_188.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_188.json)　事实 F009、F010。原文证据 E032、E033、E034、E035、E036、E037、E038、E039。

<a id="evidence-kg_top"></a>
### KG_TOP

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_top)

截断支持与概率再归一/熵归一的区别，以及预测分散与事实可靠性之间的测量边界

- [article_015/D018 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_015.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_015.json)　事实 F020。原文证据 E027。

<a id="evidence-kg_prob_tail_bound"></a>
### KG_PROB_TAIL_BOUND

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_tail_bound)

利用剩余总质量与最小已返概率共同约束未返token，并区分上界赋值、真实概率和随后条件归一。

- [article_002/D010 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_002.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_002.json)　事实 F010。原文证据 E015。

<a id="evidence-kg_prob_biased_tail"></a>
### KG_PROB_BIASED_TAIL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_biased_tail)

区分运行时logit bias后的候选分布、topK可见范围与尾部均匀假设；定义何种排名/比较仍可解释。

- [article_020/D006 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F006。原文证据 E024、E006、E009。

<a id="evidence-kg_prob_perplexity"></a>
### KG_PROB_PERPLEXITY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_perplexity)

条件token负loglikelihood的长度平均和指数、仅目标范围的损失mask；区分真实序列困惑度与masked伪困惑度及tokenization依赖。

- [article_004/D015 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_004.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_004.json)　事实 F015。原文证据 E016。
- [article_009/D012 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_009.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_009.json)　事实 F010、F020。原文证据 E008、E033、E035、E036。
- [article_020/D019 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F019、F025。原文证据 E012、E022、E039、E040。
- [article_027/D028 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_027.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_027.json)　事实 F023。原文证据 E028、E029、E033。
- [article_042/D016 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F014。原文证据 E015、E004。
- [article_070/D021 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_070.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_070.json)　事实 F022。原文证据 E021、E022。
- [article_099/D006 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_099.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_099.json)　事实 F008。原文证据 E005。
- [article_139/D008 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F009。原文证据 E011、E026。
- [article_149/D019 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_149.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_149.json)　事实 F014。原文证据 E029、E030。

<a id="evidence-kg_prob_causal_chain"></a>
### KG_PROB_CAUSAL_CHAIN

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_causal_chain)

使用真实已知前缀逐位置取得目标token条件概率；联合链、log和与负log surprisal符号对应，区分提示自身与待测续句。

- [article_006/D003 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_006.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_006.json)　事实 F003、F004、F011。原文证据 E008、E009、E019、E016。
- [article_018/D017 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_018.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_018.json)　事实 F019、F020。原文证据 E013、E024、E026。
- [article_031/D007 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_031.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_031.json)　事实 F007、F008。原文证据 E006、E013、E007。
- [article_038/D021 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_038.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_038.json)　事实 F023。原文证据 E021、E023。
- [article_055/D004 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_055.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_055.json)　事实 F005、F006、F007、F015。原文证据 E012、E013、E014、E015、E016、E017、E018、E041。
- [article_057/D011 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_057.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_057.json)　事实 F011。原文证据 E027、E028。
- [article_065/D005 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_065.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_065.json)　事实 F005。原文证据 E008、E009。
- [article_070/D005 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_070.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_070.json)　事实 F004、F005、F012。原文证据 E002、E005、E006、E021、E022、E026。
- [article_077/D005 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_077.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_077.json)　事实 F008。原文证据 E006。
- [article_085/D002 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_085.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_085.json)　事实 F003。原文证据 E002、E003、E033、E024。
- [article_092/D004 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_092.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_092.json)　事实 F007。原文证据 E007、E008。
- [article_097/D012 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_097.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_097.json)　事实 F016。原文证据 E010、E017、E018。
- [article_106/D004 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_106.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_106.json)　事实 F004。原文证据 E003、E006、E013。
- [article_161/D002 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_161.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_161.json)　事实 F003。原文证据 E007、E008、E009、E010。
- [article_162/D011 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_162.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_162.json)　事实 F010。原文证据 E022。
- [article_166/D005 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_166.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_166.json)　事实 F006。原文证据 E011、E012。
- [article_177/D003 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F005。原文证据 E014、E015。
- [article_202/D011 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_202.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_202.json)　事实 F018、F019。原文证据 E030、E031、E032、E033、E034。
- [article_206/D003 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_206.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_206.json)　事实 F006。原文证据 E013、E014。
- [article_223/D008 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F009、F017。原文证据 E018、E019、E035。
- [article_230/D011 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_230.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_230.json)　事实 F011。原文证据 E020、E021、E022。

<a id="evidence-kg_prob_slor"></a>
### KG_PROB_SLOR

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_slor)

以同tokenization的unigram参照从句log概率扣除词频基线再按token数归一，并界定分数方向和非校准概率解释。

- [article_006/D007 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_006.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_006.json)　事实 F015。原文证据 E018、E019、E020。

<a id="evidence-kg_prob_masked_pll"></a>
### KG_PROB_MASKED_PLL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_masked_pll)

逐位置遮蔽后以左右上下文取得概率并累加log值，区分单token/整词遮蔽与真实自回归联合概率。

- [article_031/D008 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_031.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_031.json)　事实 F007、F008。原文证据 E006、E013、E007。
- [article_092/D005 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_092.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_092.json)　事实 F008。原文证据 E008。
- [article_107/D008 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_107.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_107.json)　事实 F007。原文证据 E007、E006、E009、E003。
- [article_166/D033 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_166.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_166.json)　事实 F030、F032。原文证据 E058、E059、E060、E064、E065。

<a id="evidence-kg_prob_random_mask_chain"></a>
### KG_PROB_RANDOM_MASK_CHAIN

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_random_mask_chain)

从全mask按顺序逐真实词填回的条件概率链；不同顺序条件空间变化，以及平均log链不保证一致真实联合分布的解释。

- [article_166/D006 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_166.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_166.json)　事实 F007。原文证据 E013。

<a id="evidence-worker_4_gap_unmasked_token_score"></a>
### worker_4_gap_unmasked_token_score

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_unmasked_token_score)

原句所有目标token可见时逐tokenlog概率的自条件评分及attention归约

- [article_107/D008 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_107.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_107.json)　事实 F007。原文证据 E007、E006、E009、E003。

<a id="evidence-kg_prob_reference_rank"></a>
### KG_PROB_REFERENCE_RANK

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_reference_rank)

取得模型token排名，按参考词前缀续写后把完整匹配映回token秩，并限定这种参照引导的候选空间。

- [article_054/D016 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_054.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_054.json)　事实 F018。原文证据 E054、E055、E056、E058。

<a id="evidence-kg_hdiff"></a>
### KG_HDIFF

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_hdiff)

熵差的方向、量纲和相等熵不等于相同分布；不能与通常称relative entropy的KL混同

- [article_021/D009 · 需求记录 r30](../../../analysis/literature_component_coverage/records/assessments/article_021.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_021.json)　事实 F008。原文证据 E004、E033。

<a id="evidence-kg_entmeasure"></a>
### KG_ENTMEASURE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_entmeasure)

从加权解释得分到概率分布的选择及其熵含义；支持集大小、softmax变换与构念解释的关系

- [article_100/D015 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F012、F014、F015、F018、F019、F024。原文证据 E010、E011、E023、E022、E012、E014、E024、E015。

<a id="evidence-kg_perplex"></a>
### KG_PERPLEX

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_perplex)

对数底与指数底配套、熵转有效类别数及支持集归一后的含义，区别概率与确定性分数

- [article_129/D002 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_129.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_129.json)　事实 F002、F006。原文证据 E004、E005、E006、E016、E017、E018。

<a id="evidence-worker_5_gini_simpson_gap"></a>
### worker_5_GINI_SIMPSON_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_gini_simpson_gap)

类型频率的二次集中度1-Σp²如何定义及为何表示两次独立抽取为异类的概率；区分该指标与类型数及Shannon熵。

- [article_104/D010 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_104.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_104.json)　事实 F007、F017。原文证据 E018、E019、E050、E051。

<a id="evidence-kg_ig"></a>
### KG_IG

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_ig)

先验熵与答案条件熵期望之差、答案概率权重及零质量分支的解释

- [article_140/D007 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_140.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_140.json)　事实 F011。原文证据 E028、E029、E030。

<a id="evidence-kg_decomp"></a>
### KG_DECOMP

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_decomp)

平均条件熵和混合分布熵的区别，区分形式内部不确定与形式间冲突

- [article_191/D017 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_191.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_191.json)　事实 F015、F016、F018、F027。原文证据 E051、E052、E008、E057、E058、E059、E077、E078、E079。

<a id="evidence-kg_jsdiag"></a>
### KG_JSDIAG

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_jsdiag)

各形式到平均分布的generalizedJSD与条件/边际熵关系，区分形式敏感和形式内不确定

- [article_191/D017 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_191.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_191.json)　事实 F015、F016、F018、F027。原文证据 E051、E052、E008、E057、E058、E059、E077、E078、E079。

<a id="evidence-kg_kl"></a>
### KG_KL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_kl)

方向性、参考分布、共同支持与零概率边界及对数尺度，不把分布偏离自动解释为因果效应

- [article_022/D012 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_022.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_022.json)　事实 F015。原文证据 E012、E013。
- [article_096/D002 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_096.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_096.json)　事实 F002。原文证据 E001、E012、E013。
- [article_106/D008 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_106.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_106.json)　事实 F008。原文证据 E004。
- [article_133/D013 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_133.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_133.json)　事实 F003、F018、F022、F030、F031。原文证据 E012、E013、E044、E049、E050、E065、E066、E067、E068、E069、E070、E085。

<a id="evidence-kg_js"></a>
### KG_JS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_js)

以混合分布为参照的散度、权重、底数/归一与distance平方根区别

- [article_100/D022 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F018。原文证据 E014。
- [article_124/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_124.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_124.json)　事实 F012、F029。原文证据 E028、E029、E030、E031、E052、E053。
- [article_147/D027 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_147.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_147.json)　事实 F018。原文证据 E033、E034。
- [article_225/D012 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_225.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_225.json)　事实 F009。原文证据 E025、E026、E027、E028。

<a id="evidence-kg_jsshift"></a>
### KG_JSSHIFT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_jsshift)

将JSD分解为各词贡献、文本自身参考与外部先验的区别，贡献排序不是原始词频排序

- [article_039/D013 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_039.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_039.json)　事实 F011。原文证据 E006、E021。

<a id="evidence-kg_pmi"></a>
### KG_PMI

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_pmi)

联合相对边缘乘积的独立性基准、正负/尺度与点式关联解释，不以平均PMI的检验直接证明所有依赖结构

- [article_060/D010 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_060.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_060.json)　事实 F012。原文证据 E035、E036、E037。

<a id="evidence-kg_cross"></a>
### KG_CROSS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cross)

交叉熵的参考/加权方向、对称化和与JSD/KL的区别；高分含义依赖作者定义的负号

- [article_095/D007 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_095.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_095.json)　事实 F010。原文证据 E007。

<a id="evidence-kg_wasserstein"></a>
### KG_WASSERSTEIN

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_wasserstein)

概率质量、支持位置与ground cost、耦合最小运输及阶数/尺度解释；区分原非负距离和额外显示方向符号

- [article_002/D012 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_002.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_002.json)　事实 F012。原文证据 E012、E016。
- [article_021/D008 · 需求记录 r30](../../../analysis/literature_component_coverage/records/assessments/article_021.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_021.json)　事实 F008、F009、F012、F015、F018、F022。原文证据 E004、E036、E012、E022、E019、E020、E015、E017、E037。
- [article_147/D026 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_147.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_147.json)　事实 F018。原文证据 E033、E034。
- [article_177/D019 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F019、F025。原文证据 E037、E038、E049、E050、E051。
- [article_196/D018 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_196.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_196.json)　事实 F004。原文证据 E025、E026、E027。
- [article_237/D012 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F015。原文证据 E044、E045、E046、E047。

<a id="evidence-kg_calib_background_median"></a>
### KG_CALIB_BACKGROUND_MEDIAN

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_calib_background_median)

对属性位置估计背景偏好、校准集与测试信息边界及适用性

- [article_143/D006 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F006。原文证据 E012、E068。

<a id="evidence-kg_calib_contentfree"></a>
### KG_CALIB_CONTENTFREE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_calib_contentfree)

无内容参照构造、先验偏好估计及预测分布校准映射

- [article_020/D011 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F010、F017、F018。原文证据 E028、E011、E041。
- [article_158/D011 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_158.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_158.json)　事实 F012。原文证据 E017、E018、E019。

<a id="evidence-kg_calib_pride"></a>
### KG_CALIB_PRIDE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_calib_pride)

跨排列先验估计与矩阵校准及输入不变假设

- [article_158/D012 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_158.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_158.json)　事实 F012。原文证据 E017、E018、E019。

<a id="evidence-kg_pairrank_mle"></a>
### KG_PAIRRANK_MLE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_pairrank_mle)

条件排序似然、唯一答案集合、单纯形参数化及题内优化

- [article_038/D014 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_038.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_038.json)　事实 F014、F015。原文证据 E009、E019、E020。

<a id="evidence-kg_prob_ccp"></a>
### KG_PROB_CCP

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_prob_ccp)

在NLI已筛候选上形成条件概率比例，再按CCP词/主张定义聚合；区分语义候选筛选与最终不确定性。

- [article_015/D022 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_015.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_015.json)　事实 F021。原文证据 E028。

<a id="evidence-worker_5_semantic_entropy_gap"></a>
### worker_5_SEMANTIC_ENTROPY_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_semantic_entropy_gap)

主张问句采样、双向蕴涵形成语义等价类、类概率求和及熵到主张归约。

- [article_015/D024 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_015.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_015.json)　事实 F022。原文证据 E030、E032。

<a id="evidence-kg_joint"></a>
### KG_JOINT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_joint)

条件正确概率与边际信心的区别、联合事件链及依赖结构下乘积解释

- [article_038/D007 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_038.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_038.json)　事实 F009。原文证据 E005、E041。

<a id="evidence-worker_2_first_event_gap"></a>
### worker_2_first_event_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_first_event_gap)

置信到首次buzz概率的条件链、此前未发生的生存乘积、总质量及与人类累计正确曲线奖励的关系

- [article_117/D018 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_117.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_117.json)　事实 F015、F021。原文证据 E009、E031、E034、E035、E036。

<a id="evidence-worker_5_first_success_gap"></a>
### worker_5_FIRST_SUCCESS_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_first_success_gap)

N变量含s充分变量的无放回首成功分布及期望(N+1)/(s+1)。

- [article_016/D029 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F015。原文证据 E004、E005。

<a id="evidence-kg_folded_normal_moments"></a>
### KG_FOLDED_NORMAL_MOMENTS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_folded_normal_moments)

正态绝对值的CDF/指数项均值、方差及跨组传播

- [article_118/D011 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_118.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_118.json)　事实 F014。原文证据 E010、E011、E014。

<a id="evidence-worker_2_beta_cdf_gap"></a>
### worker_2_beta_cdf_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_beta_cdf_gap)

Beta后验CDF求值及尾端位置解释，区别后验均值误差和置信区间

- [article_085/D015 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_085.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_085.json)　事实 F018。原文证据 E018、E019、E020。

<a id="evidence-worker_4_gap_bayes_prompt_factor"></a>
### worker_4_gap_bayes_prompt_factor

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_bayes_prompt_factor)

在变量顺序下把联合概率分解为条件项，依据分布影响/统计可得性近似删父节点后重组

- [article_235/D003 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F002、F003、F019、F020。原文证据 E004、E005、E006、E007、E039、E040、E041、E042、E043、E044。

<a id="evidence-kg_bin_sq"></a>
### KG_BIN_SQ

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_bin_sq)

以置信条件化的校准目标和分箱分辨率/箱内抵消，平方损失与绝对损失区别

- [article_023/D019 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_023.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_023.json)　事实 F017。原文证据 E020、E021、E022、E031。
- [article_116/D014 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_116.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_116.json)　事实 F009、F014。原文证据 E003、E011、E012。

<a id="evidence-kg_bin_abs"></a>
### KG_BIN_ABS

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_bin_abs)

以置信条件化的校准目标、分箱粗化/箱内抵消及边界解释

- [article_117/D019 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_117.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_117.json)　事实 F016。原文证据 E026、E028。
- [article_130/D011 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_130.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_130.json)　事实 F011。原文证据 E028、E029。
- [article_147/D012 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_147.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_147.json)　事实 F010、F015。原文证据 E016、E026、E027、E028、E029。

<a id="evidence-kg_bin_unknown"></a>
### KG_BIN_UNKNOWN

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_bin_unknown)

ECE的条件校准目标、置信分箱与经验正确率比较；具体损失按原文未报保留

- [article_038/D017 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_038.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_038.json)　事实 F016。原文证据 E011、E035。
- [article_146/D019 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_146.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_146.json)　事实 F018。原文证据 E040、E041、E039。

<a id="evidence-kg_bin_target"></a>
### KG_BIN_TARGET

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_bin_target)

条件正确频率匹配声称置信的含义及ECE对该目标的分箱近似

- [article_172/D025 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_172.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_172.json)　事实 F009、F025、F026。原文证据 E010、E024、E027、E028、E060、E061、E062、E063。

<a id="evidence-kg_bin_class"></a>
### KG_BIN_CLASS

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_bin_class)

top-label与classwise目标、跨类权重及对数/等宽分箱的不同近似

- [article_106/D007 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_106.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_106.json)　事实 F007。原文证据 E004、E007、E021。

<a id="evidence-kg_curve_roc"></a>
### KG_CURVE_ROC

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_curve_roc)

目标类/分数方向、按正负类数计算TPR/FPR、阈值曲线面积与并列分数解释

- [article_015/D036 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_015.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_015.json)　事实 F023。原文证据 E031。
- [article_038/D018 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_038.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_038.json)　事实 F016。原文证据 E011、E035。
- [article_041/D016 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_041.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_041.json)　事实 F016。原文证据 E019、E020、E021、E022、E023。
- [article_073/D015 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_073.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_073.json)　事实 F016。原文证据 E026、E027。
- [article_107/D013 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_107.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_107.json)　事实 F011、F012。原文证据 E013、E014。
- [article_116/D012 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_116.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_116.json)　事实 F009、F013、F015。原文证据 E003、E007、E008、E009、E010、E013。
- [article_127/D018 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F023。原文证据 E038、E039。
- [article_146/D027 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_146.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_146.json)　事实 F018。原文证据 E040、E041、E039。
- [article_147/D013 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_147.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_147.json)　事实 F011。原文证据 E017。
- [article_159/D015 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_159.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_159.json)　事实 F013。原文证据 E030、E031、E032。
- [article_186/D012 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_186.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_186.json)　事实 F010。原文证据 E032。
- [article_188/D012 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_188.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_188.json)　事实 F011。原文证据 E040、E004。
- [article_208/D004 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_208.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_208.json)　事实 F005、F012、F023、F024、F025、F026。原文证据 E009、E010、E011、E012、E022、E023、E045、E046、E047、E048、E049、E050、E051、E052、E053、E054、E055、E056。

<a id="evidence-kg_curve_pr"></a>
### KG_CURVE_PR

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_curve_pr)

目标类、分数方向、precision/recall及积分规则和基率影响

- [article_038/D019 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_038.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_038.json)　事实 F016。原文证据 E011、E035。
- [article_147/D015 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_147.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_147.json)　事实 F012。原文证据 E018、E019、E020。
- [article_149/D024 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_149.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_149.json)　事实 F019、F018。原文证据 E036、E037、E038、E039。

<a id="evidence-kg_curve_map"></a>
### KG_CURVE_MAP

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_curve_map)

按得分排序的precision/recall累积、AP规则与类/例平均口径

- [article_020/D014 · 需求记录 r28](../../../analysis/literature_component_coverage/records/assessments/article_020.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_020.json)　事实 F011。原文证据 E006。
- [article_136/D013 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_136.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_136.json)　事实 F014、F020。原文证据 E031、E039、E040、E052。

<a id="evidence-kg_score_mcc"></a>
### KG_SCORE_MCC

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_score_mcc)

四格混淆矩阵乘积差及边缘归一、退化分母与负相关解释

- [article_030/D019 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_030.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_030.json)　事实 F015。原文证据 E007、E008、E006。

<a id="evidence-kg_pair_btl_spectral"></a>
### KG_PAIR_BTL_SPECTRAL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_pair_btl_spectral)

成对胜负矩阵、潜在优势模型和谱求解/可识别条件

- [article_087/D008 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_087.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_087.json)　事实 F010。原文证据 E008、E029、E030。

<a id="evidence-kg_bt_pair_fit"></a>
### KG_BT_PAIR_FIT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_bt_pair_fit)

成对logistic似然、强度锚定与软/硬胜场权重

- [article_225/D017 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_225.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_225.json)　事实 F012、F033。原文证据 E034、E035、E092、E093、E094。
- [article_229/D009 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_229.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_229.json)　事实 F005。原文证据 E009、E010、E011、E012。

<a id="evidence-kg_pair_swiss_schedule"></a>
### KG_PAIR_SWISS_SCHEDULE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_pair_swiss_schedule)

按累计分配对、多轮对手安排和并列/排名程序

- [article_154/D013 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_154.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_154.json)　事实 F011、F012。原文证据 E036、E037、E038。

<a id="evidence-kg_elo_online"></a>
### KG_ELO_ONLINE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_elo_online)

预期胜率、K步长及顺序更新的评级机制

- [article_017/D015 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_017.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_017.json)　事实 F016。原文证据 E009、E031。

<a id="evidence-kg_elo_rating"></a>
### KG_ELO_RATING

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_elo_rating)

成对对赛到Elo强度及差值胜率映射，明确实际估计方式

- [article_179/D028 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F017、F031。原文证据 E047、E048、E049、E091、E092、E093、E094。

<a id="evidence-worker_1_kg_ari"></a>
### worker_1_KG_ARI

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_ari)

成对共簇列联、随机分区期望及ARI机会校正和负值解释

- [article_032/D021 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_032.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_032.json)　事实 F020、F026。原文证据 E021、E023、E027、E028。
- [article_196/D016 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_196.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_196.json)　事实 F004。原文证据 E025、E026、E027。

<a id="evidence-kg_beta_conjugate"></a>
### KG_BETA_CONJUGATE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_beta_conjugate)

区分未知成功概率、观测计数、先验参数及Beta后验参数，建立似然×先验到后验的共轭关系。

- [article_085/D011 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_085.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_085.json)　事实 F013。原文证据 E013。

<a id="evidence-kg_discounted_pseudocounts"></a>
### KG_DISCOUNTED_PSEUDOCOUNTS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_discounted_pseudocounts)

在每次观测前衰减两类伪计数并加入当前事件，以归一后的计数形成预测；区分等权共轭累积与有遗忘的动态参照。

- [article_085/D012 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_085.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_085.json)　事实 F014、F016。原文证据 E012、E014、E015、E016。

<a id="evidence-kg_bayes_linear_predict"></a>
### KG_BAYES_LINEAR_PREDICT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_bayes_linear_predict)

在明确线性模型假设下结合观测与参数先验取得后验预测，并区分默认先验与知道生成分布的oracle信息。

- [article_135/D009 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_135.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_135.json)　事实 F006、F022。原文证据 E007、E020、E021、E031、E037、E044、E052、E055、E056、E059。

<a id="evidence-kg_kalman_belief"></a>
### KG_KALMAN_BELIEF

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_kalman_belief)

高斯先验和观测噪声、Kalman增益及所选状态均值方差递推

- [article_035/D008 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_035.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_035.json)　事实 F006。原文证据 E004。
- [article_135/D018 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_135.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_135.json)　事实 F018、F031。原文证据 E012、E054、E055、E056、E064、E065。

<a id="evidence-kg_finite_bayes_update"></a>
### KG_FINITE_BAYES_UPDATE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_finite_bayes_update)

定义假设/世界、先验、观测或话语似然，更新并归一化后验；区分硬相容过滤与带噪观测似然。

- [article_162/D004 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_162.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_162.json)　事实 F006。原文证据 E014。
- [article_200/D019 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_200.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_200.json)　事实 F014。原文证据 E042、E043。

<a id="evidence-kg_posterior_transmission"></a>
### KG_POSTERIOR_TRANSMISSION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_posterior_transmission)

把当前后验接入发送/重建过程，只保存成功通信数据再更新，并生成下一代输入；区分个体更新和通信筛选压力。

- [article_162/D004 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_162.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_162.json)　事实 F006。原文证据 E014。

<a id="evidence-kg_conditional_gibbs"></a>
### KG_CONDITIONAL_GIBBS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_conditional_gibbs)

从两个条件生成/判断任务交替传递最新状态，明确Markov结构、条件分布相容性及初值/混合/收敛对联合样本解释的影响。

- [article_047/D005 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F006、F007。原文证据 E016、E017、E018、E019、E020、E022。

<a id="evidence-kg_cog_utility_softmax"></a>
### KG_COG_UTILITY_SOFTMAX

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cog_utility_softmax)

候选效用、指数归一选择概率和逆温度含义；前向选择与逆向偏好推断区别

- [article_026/D021 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_026.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_026.json)　事实 F016。原文证据 E005。
- [article_187/D017 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_187.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_187.json)　事实 F016。原文证据 E043。
- [article_200/D018 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_200.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_200.json)　事实 F013、F014。原文证据 E040、E041、E042、E043。

<a id="evidence-kg_inverse_utility"></a>
### KG_INVERSE_UTILITY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_inverse_utility)

从效用到选择的forward likelihood反推效用分布，区分后验效用期望与某物品效用最大的后验事件概率。

- [article_187/D018 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_187.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_187.json)　事实 F016、F017。原文证据 E043、E044、E045。

<a id="evidence-kg_pragmatic_posterior"></a>
### KG_PRAGMATIC_POSTERIOR

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_pragmatic_posterior)

把speaker话语似然与奖励/动机先验结合并对潜变量边缘化

- [article_026/D022 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_026.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_026.json)　事实 F016。原文证据 E005。

<a id="evidence-kg_cog_rw_fit"></a>
### KG_COG_RW_FIT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cog_rw_fit)

逐试次价值更新、选择似然、正负学习率参数化及似然优化

- [article_003/D312 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_003.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_003.json)　事实 F016。原文证据 E019。

<a id="evidence-kg_cog_switch_identification"></a>
### KG_COG_SWITCH_IDENTIFICATION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cog_switch_identification)

从前后选择建立效用不等式、联合缩窄可行域和条件识别；中点摘要与识别假设

- [article_008/D006 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_008.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_008.json)　事实 F006、F007、F011。原文证据 E021、E004、E022、E005。
- [article_008/D015 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_008.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_008.json)　事实 F011、F018、F019。原文证据 E004、E005、E018、E019、E010、E016、E015、E030、E017。

<a id="evidence-kg_cog_decision_model_comparison"></a>
### KG_COG_DECISION_MODEL_COMPARISON

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cog_decision_model_comparison)

收益效用、概率权重、启发式/后悔和理论混合的模型结构及不同预测含义

- [article_008/D002 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_008.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_008.json)　事实 F002。原文证据 E001。
- [article_187/D022 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_187.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_187.json)　事实 F019、F020。原文证据 E007、E049、E050、E008、E051。

<a id="evidence-kg_cog_bound_optimization"></a>
### KG_COG_BOUND_OPTIMIZATION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cog_bound_optimization)

目标函数与参数边界接口、L-BFGS-B迭代与收敛条件

- [article_085/D013 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_085.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_085.json)　事实 F015、F016。原文证据 E014、E015、E016。

<a id="evidence-kg_cog_level_mixture"></a>
### KG_COG_LEVEL_MIXTURE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cog_level_mixture)

低层对手策略递归与截断归一、层级精度logit响应及总体Poisson混合

- [article_178/D007 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_178.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_178.json)　事实 F009。原文证据 E026、E027。
- [article_178/D009 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_178.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_178.json)　事实 F011。原文证据 E030、E031、E032。

<a id="evidence-kg_cog_count_mle"></a>
### KG_COG_COUNT_MLE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cog_count_mle)

由模型动作概率形成计数似然、联合参数识别和数值最大化

- [article_178/D010 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_178.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_178.json)　事实 F012。原文证据 E033。

<a id="evidence-kg_causal_identify"></a>
### KG_CAUSAL_IDENTIFY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_causal_identify)

结构图与效应查询的识别条件、无定义和平凡解边界

- [article_009/D003 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_009.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_009.json)　事实 F002、F005。原文证据 E002、E003、E004、E021。

<a id="evidence-kg_causal_do_engine"></a>
### KG_CAUSAL_DO_ENGINE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_causal_do_engine)

阻断非因果路径、合法调整集与干预分布变换

- [article_009/D004 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_009.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_009.json)　事实 F002、F004、F026。原文证据 E002、E003、E004、E020、E023、E027、E028、E017。

<a id="evidence-worker_5_scm_generation_gap"></a>
### worker_5_SCM_GENERATION_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_scm_generation_gap)

外生变量联合分布、结构方程及do替换子模型的事实/干预采样。

- [article_024/D003 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_024.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_024.json)　事实 F003、F006、F007、F008、F009、F017。原文证据 E003、E014、E007、E018、E038、E008、E019、E021、E017、E020、E026、E005。

<a id="evidence-worker_5_counterfactual_aap_gap"></a>
### worker_5_COUNTERFACTUAL_AAP_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_counterfactual_aap_gap)

按证据更新外生分布P(u|e)，替换X结构方程并用同后验预测Y。

- [article_009/D005 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_009.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_009.json)　事实 F004、F026。原文证据 E020、E023、E027、E003、E028、E017。

<a id="evidence-kg_causal_pnps_estimate"></a>
### KG_CAUSAL_PNPS_ESTIMATE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_causal_pnps_estimate)

单调性等假设下两数据源的事件频率连接与必要/充分性估计

- [article_024/D006 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_024.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_024.json)　事实 F001、F003、F004、F015、F017、F018。原文证据 E001、E015、E003、E014、E016、E009、E031、E005、E007、E011、E017。

<a id="evidence-kg_causal_observable_proxy"></a>
### KG_CAUSAL_OBSERVABLE_PROXY

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_causal_observable_proxy)

替代反事实的可比性/识别假设和近似偏差，以及输出变化指标对应的目标效应

- [article_148/D004 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_148.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_148.json)　事实 F003、F028、F029。原文证据 E006、E007、E061、E062、E039、E053、E063、E064。

<a id="evidence-kg_graph_er"></a>
### KG_GRAPH_ER

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_graph_er)

节点候选与概率边的随机图定义及生成

- [article_037/D003 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_037.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_037.json)　事实 F003。原文证据 E011。

<a id="evidence-kg_graph_edge_product"></a>
### KG_GRAPH_EDGE_PRODUCT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_graph_edge_product)

完整候选边空间、独立假设下存在/缺失边联合概率

- [article_037/D012 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_037.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_037.json)　事实 F010。原文证据 E004。

<a id="evidence-kg_graph_ergm"></a>
### KG_GRAPH_ERGM

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_graph_ergm)

充分图统计、配分函数、有界先验及MAP估计

- [article_037/D014 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_037.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_037.json)　事实 F010。原文证据 E004。

<a id="evidence-kg_sdt_sensitivity_criterion"></a>
### KG_SDT_SENSITIVITY_CRITERION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_sdt_sensitivity_criterion)

c0决策轴参数化、与β的区别及极端率处理

- [article_041/D010 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_041.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_041.json)　事实 F009、F010。原文证据 E008、E009、E010、E011。
- [article_199/D211 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F012、F022。原文证据 E008、E013。

<a id="evidence-kg_meta_sdt_probabilities"></a>
### KG_META_SDT_PROBABILITIES

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_meta_sdt_probabilities)

答A/B阈值与应答条件下的正态CDF区间概率矩阵

- [article_041/D011 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_041.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_041.json)　事实 F011、F012。原文证据 E009、E012、E013、E014。

<a id="evidence-kg_meta_sdt_fit"></a>
### KG_META_SDT_FIT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_meta_sdt_fit)

固定c0/初始化与条件正确率单调约束下的参数优化

- [article_041/D013 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_041.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_041.json)　事实 F013、F014。原文证据 E015、E016、E017、E018、E014。

<a id="evidence-worker_1_kg_shapley"></a>
### worker_1_KG_SHAPLEY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_shapley)

联盟价值、加入前后反事实边际贡献、排列权重及效率性质和近似边界

- [article_153/D006 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_153.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_153.json)　事实 F006、F012、F030。原文证据 E018、E025、E050。

<a id="evidence-worker_2_probability_logic_gap"></a>
### worker_2_probability_logic_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_probability_logic_gap)

逻辑否定、等价和蕴含对应概率互补、相等和单调关系

- [article_150/D013 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F016。原文证据 E042。

<a id="evidence-worker_2_probability_joint_gap"></a>
### worker_2_probability_joint_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_probability_joint_gap)

包含排除、Fréchet交并界及互斥分解的成立条件

- [article_150/D014 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F017。原文证据 E043。

<a id="evidence-worker_2_probability_conditional_gap"></a>
### worker_2_probability_conditional_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_probability_conditional_gap)

条件事件方向、连乘链和全概率分解及其相容解释

- [article_150/D015 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F018、F038。原文证据 E044、E091、E089、E092、E093。

<a id="evidence-worker_3_kg_log_score_arbitrage"></a>
### worker_3_KG_LOG_SCORE_ARBITRAGE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_log_score_arbitrage)

一致世界约束下max–min收益求解、零一边界与None处理及加权顺序修正

- [article_150/D016 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F019。原文证据 E045、E046。
- [article_150/D017 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F020。原文证据 E047、E048、E049、E050、E051。
- [article_150/D018 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F020。原文证据 E047、E048、E049、E050、E051。
- [article_150/D030 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F032。原文证据 E073。

<a id="evidence-worker_4_gap_matrix_ode"></a>
### worker_4_gap_matrix_ode

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_matrix_ode)

由s′和N/A构成A(p)、解p′=A^-1·1至detA=0的约束数值积分

- [article_150/D019 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_150.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_150.json)　事实 F021。原文证据 E052、E053。

<a id="evidence-kg_logodds_convergence"></a>
### KG_LOGODDS_CONVERGENCE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_logodds_convergence)

区分确定更新、点态对数几率序列及极限域，说明相关违例指标或移动平均的收敛条件。

- [article_197/D015 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_197.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_197.json)　事实 F014、F026。原文证据 E042、E055、E056、E057。

<a id="evidence-kg_spatial_relation_solving"></a>
### KG_SPATIAL_RELATION_SOLVING

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_spatial_relation_solving)

把对象间方向事实编码为同一坐标约定下的位移关系，通过逻辑规则组合/求解并解码目标对象关系；区分模板抽取、运行接口与关系推导。

- [article_217/D006 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_217.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_217.json)　事实 F008、F010、F022。原文证据 E018、E020、E022、E053、E054、E055、E056。

<a id="evidence-worker_3_kg_relation_closure"></a>
### worker_3_KG_RELATION_CLOSURE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_relation_closure)

按关系类型实例化四类约束并生成真/假关系闭包，区分缺省未知与假

- [article_093/D005 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_093.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_093.json)　事实 F006、F010。原文证据 E005、E006、E008、E009、E010。

<a id="evidence-worker_3_kg_weighted_maxsat"></a>
### worker_3_KG_WEIGHTED_MAXSAT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_weighted_maxsat)

三元组变量、LM置信软权重、硬约束与最优可满足赋值

- [article_093/D011 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_093.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_093.json)　事实 F010、F011。原文证据 E008、E009、E010、E021。

<a id="evidence-worker_2_concept_lattice_gap"></a>
### worker_2_concept_lattice_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_concept_lattice_gap)

对象属性Galois闭包、extent/intent对枚举及包含偏序构格

- [article_136/D007 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_136.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_136.json)　事实 F002、F012。原文证据 E013、E027、E028、E032、E055、E056。

<a id="evidence-worker_3_kg_priority_qscfg"></a>
### worker_3_KG_PRIORITY_QSCFG

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_priority_qscfg)

非终结符绑定、输入输出同步展开及冲突规则优先级解析

- [article_138/D007 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_138.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_138.json)　事实 F006。原文证据 E005、E031、E032。

<a id="evidence-worker_2_symbolic_material_gap"></a>
### worker_2_symbolic_material_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_symbolic_material_gap)

关系谓词、单未知算术约束、线性证明链结构及唯一最终结果生成

- [article_160/D002 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_160.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_160.json)　事实 F003。原文证据 E005、E006、E007、E008。

<a id="evidence-worker_3_kg_constraint_enumeration"></a>
### worker_3_KG_CONSTRAINT_ENUMERATION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_constraint_enumeration)

构造完整候选空间、检查问题专属约束、等价配置去重及计数分母

- [article_241/D011 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_241.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_241.json)　事实 F006、F012。原文证据 E016、E032、E033、E034、E035。

<a id="evidence-worker_3_kg_memoized_capacity_dp"></a>
### worker_3_KG_MEMOIZED_CAPACITY_DP

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_memoized_capacity_dp)

状态i/剩余容量、递归分配、排序状态合并与不可区分箱子的计数语义

- [article_241/D032 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_241.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_241.json)　事实 F036。原文证据 E096、E097、E098。

<a id="evidence-worker_2_roots_gap"></a>
### worker_2_roots_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_roots_gap)

网格变号与数值根、导数极值切点候选、残差/范围验收和数值精度去重

- [article_241/D010 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_241.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_241.json)　事实 F005、F043。原文证据 E015、E121。

<a id="evidence-worker_3_kg_propositional_soundness"></a>
### worker_3_KG_PROPOSITIONAL_SOUNDNESS

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_3_kg_propositional_soundness)

蕴含/双条件/异或语义、反例及局部推理与全结论分别检验

- [article_051/D009 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_051.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_051.json)　事实 F012、F018、F019、F020。原文证据 E031、E034、E035、E052、E053、E054、E055、E056、E057、E058、E059、E060、E061、E062、E063。

<a id="evidence-worker_5_csp_sufficiency_gap"></a>
### worker_5_CSP_SUFFICIENCY_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_csp_sufficiency_gap)

变量域/约束赋值的蕴涵判断、最小充分集合搜索与多个正确充分变量的定义。

- [article_016/D002 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F002。原文证据 E003。

<a id="evidence-worker_5_csp_backward_gap"></a>
### worker_5_CSP_BACKWARD_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_csp_backward_gap)

从目标真/假反向枚举赋值、仅一变量不同的配对及删后无法蕴涵目标的验证。

- [article_016/D003 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F004、F005。原文证据 E006、E007、E036。

<a id="evidence-worker_5_csp_depth_gap"></a>
### worker_5_CSP_DEPTH_gap

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_5_csp_depth_gap)

识别较浅解的充分变量集合并构造禁止询问的invalid set。

- [article_016/D004 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F005。原文证据 E007。

<a id="evidence-worker_5_csp_parse_solve_gap"></a>
### worker_5_CSP_PARSE_SOLVE_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_csp_parse_solve_gap)

变量自然数域与方程解析、求解对答案验证及不可解析处置。

- [article_016/D008 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F008。原文证据 E013。

<a id="evidence-worker_2_bfs_gap"></a>
### worker_2_bfs_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_bfs_gap)

状态合法转移、前提效果、逐层展开/剪枝、最短计划与部分状态充分性检查

- [article_016/D005 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F006、F007。原文证据 E008、E009。
- [article_016/D006 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F007。原文证据 E008、E010、E011、E012。
- [article_016/D015 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F015。原文证据 E004、E005。
- [article_016/D018 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F017。原文证据 E021、E019、E037、E038。
- [article_204/D005 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_204.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_204.json)　事实 F006。原文证据 E010、E011。

<a id="evidence-worker_2_tot_gap"></a>
### worker_2_tot_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_tot_gap)

候选thought和action分阶段展开、投票选择及树搜索状态衔接

- [article_017/D008 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_017.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_017.json)　事实 F011。原文证据 E006、E022。

<a id="evidence-worker_4_gap_tot_transition"></a>
### worker_4_gap_tot_transition

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_tot_transition)

chain/target/unused状态更新、真实关系连接校验及两候选扩展

- [article_217/D013 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_217.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_217.json)　事实 F016。原文证据 E036、E037、E038、E039、E040、E041、E043。

<a id="evidence-worker_4_gap_tot_beam_bfs"></a>
### worker_4_gap_tot_beam_bfs

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_tot_beam_bfs)

按层维护候选前沿、按实际状态评分保留指定束宽、检查目标并按深度停止；b3/深度10与b10/深度3是同机制参数

- [article_140/D013 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_140.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_140.json)　事实 F018。原文证据 E043、E044。
- [article_217/D015 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_217.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_217.json)　事实 F016、F017。原文证据 E036、E037、E038、E039、E040、E041、E042、E043。

<a id="evidence-worker_2_mcts_gap"></a>
### worker_2_mcts_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_mcts_gap)

树节点选择/扩展、模拟回报回传与预算到行动选择的过程

- [article_017/D009 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_017.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_017.json)　事实 F012、F022。原文证据 E004、E025、E026。

<a id="evidence-worker_4_gap_alternating_tree"></a>
### worker_4_gap_alternating_tree

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_alternating_tree)

问题m分支与答案YES/NO二分交替递归、沿真实加模拟历史更新候选集合

- [article_140/D006 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_140.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_140.json)　事实 F008、F009。原文证据 E022、E023、E024、E025、E026。

<a id="evidence-worker_4_gap_tree_reward"></a>
### worker_4_gap_tree_reward

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_tree_reward)

Ra向下累加、叶Re初始化、答案概率加权与问题均值/最大值向上回传及CRPS路径乘积

- [article_140/D009 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_140.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_140.json)　事实 F013、F025。原文证据 E034、E053、E054。

<a id="evidence-worker_4_gap_beam_decode"></a>
### worker_4_gap_beam_decode

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_beam_decode)

宽度10的序列候选维护、累计分排序和确定性/随机beam分支

- [article_191/D026 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_191.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_191.json)　事实 F026。原文证据 E074、E075、E076。

<a id="evidence-worker_4_gap_residual_decode"></a>
### worker_4_gap_residual_decode

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_residual_decode)

top-n候选logits与第15层问题/上下文attention比值融合及逐步argmax解码

- [article_061/D013 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_061.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_061.json)　事实 F015、F016。原文证据 E036、E037、E038。

<a id="evidence-worker_4_gap_graph_structure"></a>
### worker_4_gap_graph_structure

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_graph_structure)

生成满足树连通/无环约束的随机邻接结构及赋予可传递方向关系；与Erdos–Renyi独立边采样不同

- [article_204/D004 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_204.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_204.json)　事实 F005。原文证据 E007、E008、E009。

<a id="evidence-worker_4_gap_syllogism_dfs"></a>
### worker_4_gap_syllogism_dfs

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_syllogism_dfs)

维持有效结论的递归延展及端点受限Hamiltonian排序

- [article_204/D006 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_204.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_204.json)　事实 F007、F027。原文证据 E012、E054、E055。

<a id="evidence-worker_4_gap_cycle_reach"></a>
### worker_4_gap_cycle_reach

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_cycle_reach)

成环边插入、方向可达性及未知查询筛选

- [article_204/D017 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_204.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_204.json)　事实 F022、F023。原文证据 E042、E043、E044、E045。

<a id="evidence-worker_4_gap_graph_iso"></a>
### worker_4_gap_graph_iso

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_graph_iso)

保持邻接结构的同构判定与等价类去重

- [article_232/D003 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_232.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_232.json)　事实 F002。原文证据 E004、E005。

<a id="evidence-worker_4_gap_dsep"></a>
### worker_4_gap_dsep

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_dsep)

chain/fork/collider阻断、后代条件与等价独立集

- [article_232/D004 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_232.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_232.json)　事实 F003。原文证据 E006、E007、E008。

<a id="evidence-worker_4_gap_mec_gold"></a>
### worker_4_gap_mec_gold

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_mec_gold)

祖先/后代排除直接边、共因共果的图计算及全MEC量化

- [article_232/D005 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_232.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_232.json)　事实 F004、F021。原文证据 E009、E010、E049、E050、E051。

<a id="evidence-kg_conditional_complexity"></a>
### KG_CONDITIONAL_COMPLEXITY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_conditional_complexity)

按状态空间、分支、搜索深度或分块构造逐步成本，并明确简化到某一渐近阶所需条件。

- [article_016/D018 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_016.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_016.json)　事实 F017。原文证据 E021、E019、E037、E038。
- [article_177/D027 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F030。原文证据 E058、E059。

<a id="evidence-kg_truncated_attention_bound"></a>
### KG_TRUNCATED_ATTENTION_BOUND

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_truncated_attention_bound)

区分全softmax权重、子集重归一及丢弃质量，说明用集中/代表性假设连接近似输出的条件。

- [article_177/D028 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F031。原文证据 E060、E061。

<a id="evidence-kg_stochastic_recurrence_analysis"></a>
### KG_STOCHASTIC_RECURRENCE_ANALYSIS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_stochastic_recurrence_analysis)

由递推式及独立性推导偏差/噪声的期望误差，核查维度、符号和极限，并检验有限最优停止点的成立条件。

- [article_216/D010 · 需求记录 r14](../../../analysis/literature_component_coverage/records/assessments/article_216.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_216.json)　事实 F015、F016。原文证据 E023、E024、E025、E026、E027、E028、E029、E030、E031、E032、E033、E057、E058、E059、E060、E061、E062、E063、E064、E065。

<a id="evidence-kg_linear_attention_formal"></a>
### KG_LINEAR_ATTENTION_FORMAL

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_linear_attention_formal)

说明输入矩阵、注意力乘积与残差结构的维度对应，以及指定query输出如何由矩阵读取。

- [article_233/D003 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F003。原文证据 E008、E009、E010。

<a id="evidence-kg_rank_weighted_optimum"></a>
### KG_RANK_WEIGHTED_OPTIMUM

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_rank_weighted_optimum)

把总体目标化为加权Frobenius逼近，结合协方差特征方向和秩约束求缩放谱解并解释最优条件。

- [article_233/D005 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F004、F005。原文证据 E011、E012、E013、E014、E015、E016、E017、E018。

<a id="evidence-kg_gaussian_risk_decomposition"></a>
### KG_GAUSSIAN_RISK_DECOMPOSITION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_gaussian_risk_decomposition)

运用高斯四阶矩、迹运算及独立性展开预测均方误差，分开有限样本、标签噪声、遗漏信号和收缩项。

- [article_233/D007 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F006、F007、F017。原文证据 E019、E020、E021、E022、E023、E024、E025、E026、E053、E054、E055、E056、E057。

<a id="evidence-kg_nonlinear_population_objective"></a>
### KG_NONLINEAR_POPULATION_OBJECTIVE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_nonlinear_population_objective)

区分多头输出、ReLU组合、margin hinge目标和矩阵范数正则，并交代总体极限与最优解讨论的对象。

- [article_233/D009 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F009。原文证据 E030、E031。

<a id="evidence-kg_combinatorial_representation"></a>
### KG_COMBINATORIAL_REPRESENTATION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_combinatorial_representation)

将目标连接到加权未覆盖模式，构造正负模式的表征覆盖并给所需单元数量下界及适用条件。

- [article_233/D010 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F010、F016、F019。原文证据 E032、E033、E034、E035、E051、E052、E063、E064。

<a id="evidence-kg_concentration_projection"></a>
### KG_CONCENTRATION_PROJECTION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_concentration_projection)

连接有限样本集中界、投影子空间及正交/对称假设，推导概率余项和期望噪声能量。

- [article_233/D011 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F010、F017。原文证据 E032、E033、E034、E035、E053、E054、E055、E056、E057。

<a id="evidence-worker_2_nback_generation_gap"></a>
### worker_2_nback_generation_gap

训练前手册及附录的支持程度为已支持。[返回处理结果](#gap-worker_2_nback_generation_gap)

核心单独缺少n步历史匹配的任务规则；含附录后此规则已提供，不再作为该基线缺口。

- [article_199/D202 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_199.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_199.json)　事实 F003、F006、F009、F019、F021。原文证据 E003、E006、E017、E021。

<a id="evidence-kg_program_execution_bridge"></a>
### KG_PROGRAM_EXECUTION_BRIDGE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_program_execution_bridge)

区分生成的代码/规则文本与真实运行；将程序、输入及必要测试绑定到解释器或求解器，回收数值/返回值/测试状态，再与后续计分衔接。

- [article_030/D012 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_030.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_030.json)　事实 F009。原文证据 E038、E039、E040、E041。
- [article_057/D004 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_057.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_057.json)　事实 F004。原文证据 E010。
- [article_062/D014 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_062.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_062.json)　事实 F020。原文证据 E055、E056。
- [article_138/D008 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_138.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_138.json)　事实 F007。原文证据 E005、E030、E033。
- [article_151/D031 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_151.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_151.json)　事实 F005、F009、F010。原文证据 E014、E015、E026、E027、E028、E029、E030。
- [article_152/D007 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_152.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_152.json)　事实 F010。原文证据 E029、E030。
- [article_162/D017 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_162.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_162.json)　事实 F013。原文证据 E027、E028、E029、E030。
- [article_164/D007 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_164.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_164.json)　事实 F007。原文证据 E013、E014。
- [article_212/D009 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_212.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_212.json)　事实 F011。原文证据 E023、E024。
- [article_217/D006 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_217.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_217.json)　事实 F008、F010、F022。原文证据 E018、E020、E022、E053、E054、E055、E056。
- [article_230/D004 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_230.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_230.json)　事实 F005。原文证据 E009、E010。
- [article_235/D011 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F003、F009。原文证据 E006、E007、E016。

<a id="evidence-kg_environment_action_bridge"></a>
### KG_ENVIRONMENT_ACTION_BRIDGE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_environment_action_bridge)

将文本行动映射到环境可接受动作，调用状态转移并回收观测、合法性、终局/反馈；区分模型自述状态与环境实际状态。

- [article_194/D008 · 需求记录 r12](../../../analysis/literature_component_coverage/records/assessments/article_194.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_194.json)　事实 F009、F010、F011、F017、F018。原文证据 E036、E037、E006、E038、E039、E040、E041、E011、E012、E049、E050、E051、E052。

<a id="evidence-kg_flow_environment"></a>
### KG_FLOW_ENVIRONMENT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_flow_environment)

状态/合法动作/奖励/观测的转移及同步执行

- [article_003/D303 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_003.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_003.json)　事实 F010、F013、F015、F017、F021、F035。原文证据 E015、E048、E049、E050、E051、E056、E057、E065。
- [article_010/D005 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_010.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_010.json)　事实 F006、F007、F013、F024。原文证据 E002、E025、E026、E033。
- [article_017/D003 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_017.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_017.json)　事实 F003。原文证据 E003。
- [article_082/D002 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_082.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_082.json)　事实 F006、F007。原文证据 E005、E006、E007、E016。
- [article_119/D002 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_119.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_119.json)　事实 F002、F005。原文证据 E001、E021、E002、E004。
- [article_128/D002 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_128.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_128.json)　事实 F002、F003、F006。原文证据 E003、E004、E005、E006、E011。

<a id="evidence-kg_flow_private_channels"></a>
### KG_FLOW_PRIVATE_CHANNELS

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_flow_private_channels)

各代理读写权限、公开转发字段、阶段切换和私密状态保留

- [article_005/D005 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_005.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_005.json)　事实 F006、F008。原文证据 E002、E028、E009、E013。
- [article_005/D006 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_005.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_005.json)　事实 F016。原文证据 E018、E019、E020。
- [article_012/D007 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_012.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_012.json)　事实 F008、F026。原文证据 E005、E037、E038、E040、E041。
- [article_017/D005 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_017.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_017.json)　事实 F006、F009。原文证据 E016、E017、E019。
- [article_040/D004 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_040.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_040.json)　事实 F008、F009。原文证据 E029、E030、E007、E031、E037。
- [article_082/D005 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_082.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_082.json)　事实 F005、F007。原文证据 E004、E005、E006。
- [article_122/D004 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_122.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_122.json)　事实 F005、F004。原文证据 E016、E013、E014、E015。

<a id="evidence-kg_flow_group_aggregation"></a>
### KG_FLOW_GROUP_AGGREGATION

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_flow_group_aggregation)

成员发言/可见信息调度及多成员意见汇成共同反馈的协议

- [article_010/D009 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_010.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_010.json)　事实 F004、F010。原文证据 E004、E005。

<a id="evidence-kg_search_evidence_bridge"></a>
### KG_SEARCH_EVIDENCE_BRIDGE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_search_evidence_bridge)

按查询实际调用检索服务，区分snippet/全文/商用回答等返回物，组织为后续估计输入并区分未检得证据与已检得无答案。

- [article_042/D004 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F004、F005。原文证据 E003、E009。
- [article_154/D009 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_154.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_154.json)　事实 F006、F007。原文证据 E027、E028、E029。
- [article_235/D043 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F032。原文证据 E075、E076、E077。

<a id="evidence-kg_memory_function_io"></a>
### KG_MEMORY_FUNCTION_IO

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_memory_function_io)

明确函数操作对象及读写边界，将查询结果与更新后的外部状态衔接到当前上下文，区分可见核心记忆与需访问的外部记忆。

- [article_242/D019 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_242.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_242.json)　事实 F032。原文证据 E064。

<a id="evidence-kg_flow_memory_summary"></a>
### KG_FLOW_MEMORY_SUMMARY

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_flow_memory_summary)

总结选择、写入/读取更新及原轨迹与摘要的来源边界

- [article_010/D006 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_010.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_010.json)　事实 F006、F013。原文证据 E002、E025、E028。

<a id="evidence-kg_flow_negotiated_settlement"></a>
### KG_FLOW_NEGOTIATED_SETTLEMENT

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-kg_flow_negotiated_settlement)

估计贡献转为提案/反提案/接受和最终结算的联动

- [article_153/D008 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_153.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_153.json)　事实 F003、F008、F025。原文证据 E014、E015、E021、E044、E045。

<a id="evidence-kg_flow_adaptive_match"></a>
### KG_FLOW_ADAPTIVE_MATCH

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_flow_adaptive_match)

每轮拟合BT后更新强度、未赛集合及最近对手选择

- [article_225/D021 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_225.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_225.json)　事实 F014。原文证据 E040、E041。

<a id="evidence-worker_2_kv_partition_gap"></a>
### worker_2_kv_partition_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_kv_partition_gap)

KV分区与检索token位置编码、softmax注意力衔接的执行步骤

- [article_177/D002 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F004。原文证据 E012、E013。

<a id="evidence-worker_2_layer_event_queue_gap"></a>
### worker_2_layer_event_queue_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_layer_event_queue_gap)

逐层检索邻近事件队列的去重/移出、token预算填充与注意力接口

- [article_177/D011 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F011、F014。原文证据 E023、E028、E029。

<a id="evidence-worker_2_kv_offload_gap"></a>
### worker_2_kv_offload_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_kv_offload_gap)

LRU槽位复用、GPU/CPU/磁盘迁移与跨设备层执行的协调

- [article_177/D025 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F028。原文证据 E056。

<a id="evidence-worker_2_event_scheduler_gap"></a>
### worker_2_event_scheduler_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_event_scheduler_gap)

兼容任务选择、等待条件恢复优先级、时间/token阻塞解除及持续回调生命周期

- [article_242/D006 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_242.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_242.json)　事实 F006、F018、F048、F050。原文证据 E016、E017、E018、E040、E041、E105、E106、E107、E111、E112、E113。

<a id="evidence-worker_2_virtual_clock_gap"></a>
### worker_2_virtual_clock_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_virtual_clock_gap)

进程可见时间跳跃、同机agent时间同步及不兼容时真实等待回退

- [article_242/D007 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_242.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_242.json)　事实 F007、F011。原文证据 E019、E025、E026。

<a id="evidence-kg_input_gradient"></a>
### KG_INPUT_GRADIENT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_input_gradient)

固定模型上选择目标量和可微输入表示，获取目标梯度并与输入组合成重要度；符号与维度归约须与实际实现对应。

- [article_157/D016 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_157.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_157.json)　事实 F021。原文证据 E008、E073、E074。

<a id="evidence-kg_integrated_gradients"></a>
### KG_INTEGRATED_GRADIENTS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_integrated_gradients)

区分目标量、参考端点和积分路径，沿路径读取梯度并作积分或离散近似，保留之后的head/token聚合边界。

- [article_061/D006 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_061.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_061.json)　事实 F008、F014。原文证据 E022、E023、E032、E033、E034、E035。
- [article_236/D010 · 需求记录 r12](../../../analysis/literature_component_coverage/records/assessments/article_236.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_236.json)　事实 F011、F012、F026。原文证据 E028、E029、E030、E031、E032、E033、E034、E066、E067、E068、E069、E070。

<a id="evidence-kg_conditional_gradient"></a>
### KG_CONDITIONAL_GRADIENT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_conditional_gradient)

固定输出目标及条件上下文，对输入嵌入求条件log概率梯度，以局部方向编码操作差异；区分方向估计与实际激活向量干预。

- [article_192/D005 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_192.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_192.json)　事实 F006、F007、F008。原文证据 E021、E022、E023、E024、E025、E026。

<a id="evidence-kg_checkpoint_influence"></a>
### KG_CHECKPOINT_INFLUENCE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_checkpoint_influence)

在既有快照定义文档与测试目标loss，分别求参数梯度、点积并跨快照/配对归约；明确这是影响近似。

- [article_223/D025 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_223.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_223.json)　事实 F017、F019。原文证据 E035、E037。

<a id="evidence-kg_gradient_discrete_input"></a>
### KG_GRADIENT_DISCRETE_INPUT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_gradient_discrete_input)

对固定模型目标求输入梯度，构造单token候选，经不同分词器解码到共同字符串，以跨模型任务目标比较并迭代选择。

- [article_161/D003 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_161.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_161.json)　事实 F003、F004。原文证据 E007、E008、E009、E010、E011。

<a id="evidence-kg_deletion_representation_sensitivity"></a>
### KG_DELETION_REPRESENTATION_SENSITIVITY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_deletion_representation_sensitivity)

明确逐一删除对象，分别执行原输入和删后输入，定位可比较的层/位置表征，以变化量形成重要度；解释序列缩短和上下文变化的边界。

- [article_161/D025 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_161.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_161.json)　事实 F020、F021。原文证据 E040、E041。

<a id="evidence-kg_internal_vocab_readout"></a>
### KG_INTERNAL_VOCAB_READOUT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_internal_vocab_readout)

明确读取残差/更新/head输出/value向量何者，选择输出解码矩阵或输入embedding参照，保留实际归一、偏置、取词与logit/概率/匹配目标；解释读出与实际生成及因果作用的区别。

- [article_060/D013 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_060.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_060.json)　事实 F015、F017。原文证据 E045、E046、E047、E049、E050、E051。
- [article_095/D004 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_095.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_095.json)　事实 F007。原文证据 E004。
- [article_161/D028 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_161.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_161.json)　事实 F022。原文证据 E042、E043、E006。
- [article_169/D007 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_169.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_169.json)　事实 F007、F009、F012。原文证据 E021、E022、E025、E026、E027、E028、E029、E032。
- [article_231/D011 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_231.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_231.json)　事实 F010、F019、F028。原文证据 E014、E015、E030、E031、E032、E051、E052、E053。
- [article_234/D025 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_234.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_234.json)　事实 F021。原文证据 E048。

<a id="evidence-kg_rep_tensor_access"></a>
### KG_REP_TENSOR_ACCESS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_rep_tensor_access)

把层、head、token、FFN非线性值、残差/更新或attention区域对应到实际输入，获取明确张量并保留轴与位置语义。

- [article_015/D019 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_015.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_015.json)　事实 F020。原文证据 E027。
- [article_015/D020 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_015.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_015.json)　事实 F020。原文证据 E027。
- [article_052/D008 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_052.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_052.json)　事实 F008。原文证据 E020、E021。
- [article_061/D009 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_061.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_061.json)　事实 F011。原文证据 E027。
- [article_075/D022 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_075.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_075.json)　事实 F023、F024。原文证据 E014。
- [article_075/D026 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_075.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_075.json)　事实 F027、F028。原文证据 E021、E029。
- [article_107/D007 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_107.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_107.json)　事实 F006。原文证据 E008、E009、E006。
- [article_139/D024 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F021、F022。原文证据 E018、E031、E032、E019。
- [article_141/D015 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_141.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_141.json)　事实 F023。原文证据 E044、E045、E046、E047。
- [article_157/D017 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_157.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_157.json)　事实 F021、F022。原文证据 E008、E073、E074、E075、E076、E077。
- [article_157/D027 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_157.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_157.json)　事实 F033。原文证据 E009、E101、E102、E103。
- [article_169/D003 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_169.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_169.json)　事实 F003、F007、F012、F016、F020。原文证据 E003、E015、E021、E022、E032、E040、E041、E048、E049、E050。
- [article_169/D014 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_169.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_169.json)　事实 F016。原文证据 E040、E041。
- [article_170/D029 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_170.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_170.json)　事实 F025。原文证据 E009、E064。
- [article_208/D011 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_208.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_208.json)　事实 F010、F011、F026。原文证据 E019、E020、E021、E052、E053、E054、E055、E056。
- [article_220/D015 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_220.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_220.json)　事实 F021、F028。原文证据 E037、E038、E050、E051、E052、E053。
- [article_231/D010 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_231.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_231.json)　事实 F010、F022、F023、F028。原文证据 E014、E015、E037、E038、E039、E040、E041、E051、E052、E053。
- [article_233/D019 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F014。原文证据 E046、E047、E048。
- [article_234/D006 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_234.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_234.json)　事实 F007、F016、F017、F018、F022、F023。原文证据 E015、E031、E032、E033、E034、E035、E036、E037、E038、E039、E040、E049、E050、E051、E052、E053、E054。
- [article_236/D011 · 需求记录 r12](../../../analysis/literature_component_coverage/records/assessments/article_236.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_236.json)　事实 F013。原文证据 E035。

<a id="evidence-kg_rep_contrast_direction"></a>
### KG_REP_CONTRAST_DIRECTION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_rep_contrast_direction)

按条件和目标token位置对应残差，形成差向量并按实际规程归一，说明方向所表征的对比以及与后续激活干预的区别。

- [article_139/D012 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F012。原文证据 E005、E013。
- [article_143/D010 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F011。原文证据 E020、E021。

<a id="evidence-kg_local_brain_rsa"></a>
### KG_LOCAL_BRAIN_RSA

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_local_brain_rsa)

按被试空间的球/ROI取得信号并构造相同刺激索引的相似结构，连接脑与模型RSM作区域对照；区别局部空间与低维ROI表示来源。

- [article_121/D023 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F020、F022、F026。原文证据 E035、E037、E043。

<a id="evidence-kg_key_adjacency_graph"></a>
### KG_KEY_ADJACENCY_GRAPH

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_key_adjacency_graph)

把局部每head的key对关系映成带权token邻接矩阵，说明点积的坐标/尺度和事件community含义。

- [article_177/D005 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F006。原文证据 E016。

<a id="evidence-kg_embedding_soft_input"></a>
### KG_EMBEDDING_SOFT_INPUT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_embedding_soft_input)

将文本前缀取得嵌入矩阵，在该空间施加已定义扰动并经embedding输入接口运行固定模型，保留开放访问和位置衔接要求。

- [article_195/D005 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_195.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_195.json)　事实 F008、F010。原文证据 E022、E023、E024、E025、E027。

<a id="evidence-kg_fixed_representation_projection"></a>
### KG_FIXED_REPRESENTATION_PROJECTION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_fixed_representation_projection)

在明确残差坐标中使用同一既有方向或矩阵读出，保持轴、层、token span及不同checkpoint表示的对应关系。

- [article_139/D013 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F013。原文证据 E006。
- [article_205/D007 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_205.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_205.json)　事实 F006。原文证据 E016、E017。
- [article_205/D025 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_205.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_205.json)　事实 F025。原文证据 E072。
- [article_234/D023 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_234.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_234.json)　事实 F016、F018、F019。原文证据 E031、E032、E036、E037、E038、E039、E040、E041、E042。

<a id="evidence-kg_write_read_composition"></a>
### KG_WRITE_READ_COMPOSITION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_write_read_composition)

解释OV/QK等矩阵的写入/读取空间、乘积及Frobenius量纲，区分整矩阵和已分解分量的通信度量。

- [article_234/D003 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_234.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_234.json)　事实 F003、F004、F020。原文证据 E007、E008、E009、E010、E043、E044、E045、E046、E047。

<a id="evidence-kg_existing_sae_encoding"></a>
### KG_EXISTING_SAE_ENCODING

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_existing_sae_encoding)

从现成模型dense表示衔接到已给SAE编码器的稀疏特征，区分其输入层/表示来源、编码输出与下游监督拟合。

- [article_235/D020 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_235.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_235.json)　事实 F026。原文证据 E057、E058、E059、E060。

<a id="evidence-kg_act_runtime_tensor_edit"></a>
### KG_ACT_RUNTIME_TENSOR_EDIT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_act_runtime_tensor_edit)

指定层、token、head/神经元/残差坐标，记录来源运行或方向，执行替换、加噪、加减/投影/置零；区分输入与输出时段及下游重新计算或钳制。注意分数遮罩、归一后权重置换与残差改值分别明确，不能互换。

- [article_052/D011 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_052.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_052.json)　事实 F010、F011、F020。原文证据 E023、E024、E025、E026、E027、E028、E060、E061。
- [article_060/D015 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_060.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_060.json)　事实 F018、F020。原文证据 E052、E053、E054、E056、E057、E058。
- [article_060/D017 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_060.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_060.json)　事实 F021。原文证据 E059。
- [article_061/D010 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_061.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_061.json)　事实 F012。原文证据 E028、E029。
- [article_119/D020 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_119.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_119.json)　事实 F018。原文证据 E017、E018。
- [article_137/D005 · 需求记录 r14](../../../analysis/literature_component_coverage/records/assessments/article_137.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_137.json)　事实 F006、F007、F008。原文证据 E019、E020、E021、E022、E023、E024、E025、E026、E092、E093、E094。
- [article_139/D017 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F016。原文证据 E015、E016。
- [article_139/D020 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F018。原文证据 E020、E022。
- [article_139/D021 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F019。原文证据 E021、E022。
- [article_139/D022 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_139.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_139.json)　事实 F020。原文证据 E022、E023。
- [article_143/D002 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F003、F004。原文证据 E006、E007、E002、E003、E008、E009。
- [article_143/D011 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F012、F014、F018。原文证据 E022、E023、E025、E026、E035、E036。
- [article_143/D013 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F015、F016。原文证据 E027、E028、E029、E030、E031、E032。
- [article_143/D015 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F019、F020。原文证据 E037、E038、E035、E039。
- [article_143/D017 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F023。原文证据 E047、E048。
- [article_169/D008 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_169.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_169.json)　事实 F010、F011、F019。原文证据 E030、E031、E046、E047。
- [article_169/D011 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_169.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_169.json)　事实 F014、F015。原文证据 E035、E036、E037、E038、E039。
- [article_231/D005 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_231.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_231.json)　事实 F003、F005、F008、F009、F012、F013、F016、F022、F023、F026。原文证据 E005、E007、E011、E012、E013、E019、E020、E021、E025、E037、E038、E039、E040、E041、E046、E047。
- [article_234/D009 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_234.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_234.json)　事实 F009、F010、F012、F023。原文证据 E017、E018、E019、E020、E021、E023、E024、E052、E053、E054。
- [article_236/D012 · 需求记录 r12](../../../analysis/literature_component_coverage/records/assessments/article_236.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_236.json)　事实 F014、F016、F017。原文证据 E036、E037、E040、E041、E042。
- [article_236/D013 · 需求记录 r12](../../../analysis/literature_component_coverage/records/assessments/article_236.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_236.json)　事实 F014。原文证据 E036、E037。

<a id="evidence-kg_act_directional_derivative"></a>
### KG_ACT_DIRECTIONAL_DERIVATIVE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_act_directional_derivative)

分别定义召回与输出目标，计算召回对中间状态梯度，令xhat=x+α∇R并求输出对α在0的导数，不能把有限步梯度优化或单个输出log概率读出当同一方法。

- [article_095/D008 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_095.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_095.json)　事实 F011。原文证据 E008。
- [article_095/D013 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_095.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_095.json)　事实 F019。原文证据 E021、E022。

<a id="evidence-kg_act_pseudoinverse_suppression"></a>
### KG_ACT_PSEUDOINVERSE_SUPPRESSION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_act_pseudoinverse_suppression)

在词表与隐藏维度间定义E和Moore–Penrose伪逆，回映射已答分布、再投回并从生成量中减去缩放分量；区分logit、线性映射值与合法概率分布。

- [article_134/D006 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_134.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_134.json)　事实 F007、F008。原文证据 E018、E019、E020、E044、E045。

<a id="evidence-kg_act_rope_position"></a>
### KG_ACT_ROPE_POSITION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_act_rope_position)

区分真实序列位置与逐层旋转位置，将对应位置旋转替换为目标位置旋转并保持激活内容与其他变量边界。

- [article_143/D008 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_143.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_143.json)　事实 F009。原文证据 E016、E017。

<a id="evidence-kg_rep_manual_circuit_trace"></a>
### KG_REP_MANUAL_CIRCUIT_TRACE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_rep_manual_circuit_trace)

逐步在Q/K/V路径选择与节点间建立归因连接，记录分支保留与电路边界；梯度估计另由既有IG知识承接，不能把选择后的示意主干当完整自动发现。

- [article_236/D010 · 需求记录 r12](../../../analysis/literature_component_coverage/records/assessments/article_236.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_236.json)　事实 F011、F012、F026。原文证据 E028、E029、E030、E031、E032、E033、E034、E066、E067、E068、E069、E070。

<a id="evidence-worker_3_kg_tied_softmax_attention"></a>
### worker_3_KG_TIED_SOFTMAX_ATTENTION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_tied_softmax_attention)

one-hot嵌入、Q/K列归一softmax、缩放、V变换及绑定转置末位logit读取

- [article_141/D007 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_141.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_141.json)　事实 F014。原文证据 E024。

<a id="evidence-worker_5_wanda_importance_gap"></a>
### worker_5_WANDA_IMPORTANCE_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_wanda_importance_gap)

稀疏近似目标到逐连接权重×激活范数的推导、维度/广播及聚合意义。

- [article_075/D024 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_075.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_075.json)　事实 F025、F030。原文证据 E023、E025。

<a id="evidence-kg_normal_mixture_generation"></a>
### KG_NORMAL_MIXTURE_GENERATION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_normal_mixture_generation)

均值、标准差与生成分布的对应；混合分量及其权重如何共同确定材料分布

- [article_029/D002 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_029.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_029.json)　事实 F004。原文证据 E002、E007、E036、E037、E038。

<a id="evidence-worker_5_gaussian_task_gap"></a>
### worker_5_GAUSSIAN_TASK_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_gaussian_task_gap)

多元协方差Gaussian特征、独立任务权重、内积标签及context独立噪声的联合生成关系。

- [article_233/D002 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F003、F006。原文证据 E008、E009、E010、E019、E020、E021、E022。

<a id="evidence-worker_5_parity_task_gap"></a>
### worker_5_PARITY_TASK_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_parity_task_gap)

正交dictionary映射、重要/非重要索引对混合及γ偏置联合二元特征与乘积标签。

- [article_233/D008 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F008。原文证据 E027、E028、E029。

<a id="evidence-worker_5_population_risk_gap"></a>
### worker_5_POPULATION_RISK_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_population_risk_gap)

随机任务/提示分布下平方损失期望、经验1/(2B)归一及B趋无穷的总体目标。

- [article_233/D004 · 需求记录 r11](../../../analysis/literature_component_coverage/records/assessments/article_233.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_233.json)　事实 F004。原文证据 E011、E012、E013、E014。

<a id="evidence-kg_kmeans_grouping"></a>
### KG_KMEANS_GROUPING

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_kmeans_grouping)

从给定表征的距离和簇内目标形成中心/成员分配，区分簇中心向量与真实样本；用于选样时明确如何取得代表，用于结果分析时保留其分组解释。

- [article_048/D004 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_048.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_048.json)　事实 F004。原文证据 E013、E014。
- [article_110/D006 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_110.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_110.json)　事实 F004。原文证据 E008、E009。
- [article_161/D009 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_161.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_161.json)　事实 F006。原文证据 E014、E015。
- [article_210/D014 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_210.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_210.json)　事实 F018。原文证据 E037、E038、E039。

<a id="evidence-kg_cluster_order_diagnostics"></a>
### KG_CLUSTER_ORDER_DIAGNOSTICS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cluster_order_diagnostics)

区分簇内紧致性目标、k扫描和选择判据；解释Elbow折中与论文自行定义的非标准转折规则，不能混用。

- [article_048/D004 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_048.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_048.json)　事实 F004。原文证据 E013、E014。
- [article_210/D014 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_210.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_210.json)　事实 F018。原文证据 E037、E038、E039。

<a id="evidence-kg_kmedoids_selection"></a>
### KG_KMEDOIDS_SELECTION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_kmedoids_selection)

以候选间距离组织簇并选真实候选代表，区分medoid与平均向量centroid，保留相似度来源及候选不足等实现边界。

- [article_076/D012 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_076.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_076.json)　事实 F012。原文证据 E006、E022。

<a id="evidence-worker_1_kg_silhouette"></a>
### worker_1_KG_SILHOUETTE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_silhouette)

逐点簇内平均距离、最近其他簇平均距离及轮廓归一化和边界解释

- [article_129/D019 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_129.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_129.json)　事实 F014、F015。原文证据 E040、E041、E042、E043。

<a id="evidence-kg_topic_discovery"></a>
### KG_TOPIC_DISCOVERY

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_topic_discovery)

说明从文档表示到主题分组/表示的发现流程，区分数据驱动主题与已有标签计数、以及后续人工或模型命名。

- [article_179/D039 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_179.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_179.json)　事实 F027。原文证据 E079、E080、E081、E082、E083。

<a id="evidence-kg_topic_lda"></a>
### KG_TOPIC_LDA

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_topic_lda)

文档/主题/词概率生成模型及推断得到主题分布

- [article_067/D007 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_067.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_067.json)　事实 F005。原文证据 E032。
- [article_110/D005 · 需求记录 r21](../../../analysis/literature_component_coverage/records/assessments/article_110.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_110.json)　事实 F004。原文证据 E008、E009。

<a id="evidence-kg_integer_selection"></a>
### KG_INTEGER_SELECTION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_integer_selection)

将候选是否选中编码为整数变量，联合目标/容量/分层约束，可行性及求解和最优性状态解释

- [article_166/D010 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_166.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_166.json)　事实 F010、F016。原文证据 E016、E017、E024。

<a id="evidence-worker_5_capacity_cluster_gap"></a>
### worker_5_CAPACITY_CLUSTER_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_capacity_cluster_gap)

距离代价、流网络容量和每簇固定四词的可行最小费用分配。

- [article_196/D006 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_196.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_196.json)　事实 F007、F018。原文证据 E030、E049、E050。

<a id="evidence-kg_discrete_hillclimb"></a>
### KG_DISCRETE_HILLCLIMB

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_discrete_hillclimb)

定义可替换邻域/约束，按目标下降接受替换、更新当前材料与连续无改进终止；识别局部最优与起点依赖

- [article_166/D012 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_166.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_166.json)　事实 F012。原文证据 E020。

<a id="evidence-worker_4_gap_greedy_maxcover"></a>
### worker_4_gap_greedy_maxcover

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_greedy_maxcover)

每步按新增未覆盖匹配n-gram数选择文档并更新覆盖集合

- [article_127/D016 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F018、F019。原文证据 E032、E033。

<a id="evidence-kg_dsl_ast_template"></a>
### KG_DSL_AST_TEMPLATE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dsl_ast_template)

DSL语法、类型/属性到对象AST的解析及代码模板生成接口

- [article_164/D004 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_164.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_164.json)　事实 F006。原文证据 E010、E011、E012。

<a id="evidence-kg_template_predicate_binding"></a>
### KG_TEMPLATE_PREDICATE_BINDING

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_template_predicate_binding)

句式模板匹配、实体槽位绑定与方向关系谓词转换

- [article_217/D005 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_217.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_217.json)　事实 F007、F022。原文证据 E017、E013、E053、E054。

<a id="evidence-worker_1_kg_symbolic_composition"></a>
### worker_1_KG_SYMBOLIC_COMPOSITION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_symbolic_composition)

函数生成器的表达式/可调用对象一致嵌套、类型约束、复合深度和不同函数筛选

- [article_241/D009 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_241.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_241.json)　事实 F042。原文证据 E116、E117、E118、E119、E120。

<a id="evidence-kg_dr_mds"></a>
### KG_DR_MDS

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dr_mds)

相似输入到距离的桥、metric/nonmetric目标与低维拟合、应力/失真和布局自由度

- [article_001/D014 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_001.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_001.json)　事实 F016。原文证据 E018。
- [article_047/D020 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F018。原文证据 E004、E049、E050、E051。
- [article_121/D017 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F014。原文证据 E025。
- [article_222/D013 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_222.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_222.json)　事实 F010。原文证据 E022。

<a id="evidence-kg_dr_tsne"></a>
### KG_DR_TSNE

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dr_tsne)

邻域概率、perplexity/初始化与低维优化，以及局部/全局距离解释边界

- [article_025/D021 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_025.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_025.json)　事实 F022。原文证据 E024、E007。
- [article_075/D023 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_075.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_075.json)　事实 F024。原文证据 E014。
- [article_121/D017 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F014。原文证据 E025。
- [article_129/D022 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_129.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_129.json)　事实 F015。原文证据 E042、E043。
- [article_136/D017 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_136.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_136.json)　事实 F021。原文证据 E005、E027、E032、E036、E041、E042、E055、E056。
- [article_196/D010 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_196.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_196.json)　事实 F009、F029。原文证据 E016、E069、E018、E070、E071、E072。
- [article_220/D018 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_220.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_220.json)　事实 F025、F028。原文证据 E045、E050、E051、E052、E053。
- [article_237/D029 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F029。原文证据 E082、E083、E084、E085。

<a id="evidence-kg_dr_umap"></a>
### KG_DR_UMAP

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dr_umap)

邻域结构到低维坐标拟合、尺度参数及失真解释

- [article_003/D317 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_003.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_003.json)　事实 F024、F025。原文证据 E030、E060、E063、E070。
- [article_047/D033 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F027。原文证据 E005、E063、E064。
- [article_171/D006 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_171.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_171.json)　事实 F005。原文证据 E002、E019、E020。

<a id="evidence-kg_dr_pca"></a>
### KG_DR_PCA

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dr_pca)

拟合样本与预处理、主轴/载荷和投影、累计解释方差及维度选择

- [article_003/D321 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_003.json) · [事实与原文记录 r3](../../../analysis/literature_component_coverage/records/extractions/article_003.json)　事实 F032。原文证据 E038。
- [article_104/D007 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_104.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_104.json)　事实 F005。原文证据 E012、E013、E014。
- [article_129/D021 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_129.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_129.json)　事实 F015。原文证据 E042、E043。
- [article_137/D014 · 需求记录 r14](../../../analysis/literature_component_coverage/records/assessments/article_137.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_137.json)　事实 F015。原文证据 E004、E018、E043、E045、E046、E047、E048、E049、E050、E095、E096。
- [article_196/D009 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_196.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_196.json)　事实 F009。原文证据 E016。
- [article_220/D016 · 需求记录 r17](../../../analysis/literature_component_coverage/records/assessments/article_220.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_220.json)　事实 F022、F028。原文证据 E039、E050、E051、E052、E053。
- [article_234/D022 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_234.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_234.json)　事实 F026。原文证据 E060。
- [article_237/D023 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F024。原文证据 E070、E071、E072。

<a id="evidence-kg_dr_svd"></a>
### KG_DR_SVD

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dr_svd)

左右奇异向量、奇异值、rank1分量和截断重建/投影及谱保留

- [article_015/D020 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_015.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_015.json)　事实 F020。原文证据 E027。
- [article_141/D012 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_141.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_141.json)　事实 F020、F024。原文证据 E035、E036、E048、E049、E050、E051、E052。
- [article_228/D003 · 需求记录 r18](../../../analysis/literature_component_coverage/records/assessments/article_228.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_228.json)　事实 F003、F022。原文证据 E008、E009、E010、E061、E062、E063、E064。
- [article_234/D002 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_234.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_234.json)　事实 F002、F004。原文证据 E004、E005、E006、E009、E010。

<a id="evidence-kg_dr_constrained"></a>
### KG_DR_CONSTRAINED

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_dr_constrained)

两阶段低秩近似、伪逆归一和正交约束求解

- [article_137/D004 · 需求记录 r14](../../../analysis/literature_component_coverage/records/assessments/article_137.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_137.json)　事实 F004、F005。原文证据 E017、E018、E019、E020、E043、E092、E095、E096。

<a id="evidence-worker_4_gap_euclidean_geometry"></a>
### worker_4_gap_euclidean_geometry

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_4_gap_euclidean_geometry)

在可比坐标和明确量尺的表征空间解释欧氏距离或负L2相似度，区分方向、模长与坐标尺度变化对距离的作用，以及从距离或距离离散度推到心理/任务差异的边界。

- [article_045/D024 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_045.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_045.json)　事实 F025。原文证据 E028、E029、E030。
- [article_047/D021 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F019、F022。原文证据 E052、E050。
- [article_048/D018 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_048.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_048.json)　事实 F015。原文证据 E035、E036、E013。
- [article_127/D022 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_127.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_127.json)　事实 F026。原文证据 E042。
- [article_129/D018 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_129.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_129.json)　事实 F014、F015。原文证据 E040、E041、E042、E043。
- [article_135/D025 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_135.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_135.json)　事实 F029、F039。原文证据 E009、E049、E050、E053、E059、E061、E062、E063、E064、E065。

<a id="evidence-worker_4_gap_dot_embedding"></a>
### worker_4_gap_dot_embedding

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_dot_embedding)

TASB题目与512token窗口向量点积的未归一模长与方向贡献、阈值95的表征依赖

- [article_042/D018 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_042.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_042.json)　事实 F014。原文证据 E015、E004。

<a id="evidence-worker_4_gap_rbf_similarity"></a>
### worker_4_gap_rbf_similarity

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_rbf_similarity)

径向核带宽与特征尺度、当前点对以往任务点的核值平均

- [article_135/D024 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_135.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_135.json)　事实 F023。原文证据 E009、E038、E049、E050、E059、E061、E062、E063、E064、E065。

<a id="evidence-worker_4_gap_inner_hamming"></a>
### worker_4_gap_inner_hamming

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_inner_hamming)

按潜变量token的Hamming分组分析内积及b0/−aDH+b分段关系的尺度含义

- [article_141/D014 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_141.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_141.json)　事实 F022。原文证据 E040、E041、E042、E043。

<a id="evidence-kg_cov_det"></a>
### KG_COV_DET

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cov_det)

经验协方差矩阵及行列式的广义方差解释，尺度/维度/秩依赖

- [article_237/D023 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F024。原文证据 E070、E071、E072。

<a id="evidence-worker_2_projection_variance_gap"></a>
### worker_2_projection_variance_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_projection_variance_gap)

从MDS点到指定特征方向的标量投影、方向规范化和投影方差及尺度解释

- [article_047/D024 · 需求记录 r26](../../../analysis/literature_component_coverage/records/assessments/article_047.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_047.json)　事实 F021。原文证据 E054、E056。

<a id="evidence-worker_2_cov_trace_gap"></a>
### worker_2_cov_trace_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_cov_trace_gap)

经验协方差构造、trace总方差及表示维度/尺度依赖

- [article_237/D017 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_237.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_237.json)　事实 F018。原文证据 E055、E056、E057。

<a id="evidence-worker_4_gap_principal_angle"></a>
### worker_4_gap_principal_angle

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_principal_angle)

SVD所得列子空间的正交基、主角计算及最小角的共享方向含义

- [article_141/D013 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_141.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_141.json)　事实 F020。原文证据 E035、E036。

<a id="evidence-worker_5_procrustes_gap"></a>
### worker_5_PROCRUSTES_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_procrustes_gap)

估计旋转/平移等变换、尺度/反射约束和残差对应。

- [article_222/D015 · 需求记录 r13](../../../analysis/literature_component_coverage/records/assessments/article_222.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_222.json)　事实 F010、F020。原文证据 E022、E041、E042、E043、E044。

<a id="evidence-worker_1_kg_adjacent_boundary_search"></a>
### worker_1_KG_ADJACENT_BOUNDARY_SEARCH

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_adjacent_boundary_search)

候选边界区间、社区状态更新及单趟邻移目标优化的程序与局限

- [article_177/D008 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F009、F021。原文证据 E019、E020、E041、E042、E043。

<a id="evidence-worker_2_modularity_gap"></a>
### worker_2_modularity_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_modularity_gap)

加权图随机边期望、同社区指示及模块度归一/方向解释

- [article_177/D006 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F007、F020、F021。原文证据 E017、E039、E040、E041、E042、E043。

<a id="evidence-worker_2_conductance_gap"></a>
### worker_2_conductance_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_conductance_gap)

跨边权、两侧内部volume及最小比的定义和图割解释

- [article_177/D007 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_177.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_177.json)　事实 F008、F021。原文证据 E018、E041、E042、E043。

<a id="evidence-worker_2_leiden_gap"></a>
### worker_2_leiden_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_leiden_gap)

按模块度目标进行Leiden节点移动、社区细化与聚合求参考分区

- [article_032/D020 · 需求记录 r23](../../../analysis/literature_component_coverage/records/assessments/article_032.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_032.json)　事实 F020。原文证据 E021、E023。

<a id="evidence-kg_graph_motif"></a>
### KG_GRAPH_MOTIF

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_graph_motif)

三角/星/交替三角与二路径的图结构定义和计算，软图输入处理

- [article_037/D013 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_037.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_037.json)　事实 F010、F011、F024。原文证据 E004、E010、E012、E029、E019、E020。

<a id="evidence-worker_1_kg_ego_subgraph"></a>
### worker_1_KG_EGO_SUBGRAPH

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_1_kg_ego_subgraph)

ego邻域提取、移除中心与规模筛选的联合规则和所保留图结构边界

- [article_037/D002 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_037.json) · [事实与原文记录 r2](../../../analysis/literature_component_coverage/records/extractions/article_037.json)　事实 F003。原文证据 E011。

<a id="evidence-worker_4_gap_network_statistics"></a>
### worker_4_gap_network_statistics

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_network_statistics)

边密度分母、局部三角形/邻居计数及权重度的图定义和pruned节点集合

- [article_103/D020 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_103.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_103.json)　事实 F018。原文证据 E049、E050。

<a id="evidence-worker_2_clique_dedup_gap"></a>
### worker_2_clique_dedup_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_2_clique_dedup_gap)

极大团枚举、最不相似代表选择及跨团节点按平均相似度唯一指派

- [article_100/D009 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_100.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_100.json)　事实 F007。原文证据 E007。

<a id="evidence-worker_3_kg_graph_label_diffusion"></a>
### worker_3_KG_GRAPH_LABEL_DIFFUSION

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_graph_label_diffusion)

D^−1/2WD^−1/2归一、重启传播及逆矩阵固定点的尺度和孤立点条件

- [article_103/D011 · 需求记录 r19](../../../analysis/literature_component_coverage/records/assessments/article_103.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_103.json)　事实 F009。原文证据 E023、E024、E025。

<a id="evidence-worker_4_gap_graph_edit"></a>
### worker_4_gap_graph_edit

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_graph_edit)

节点/边插入删除替换成本与节点匹配下的最小编辑序列

- [article_009/D021 · 需求记录 r27](../../../analysis/literature_component_coverage/records/assessments/article_009.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_009.json)　事实 F017、F019。原文证据 E014、E032。

<a id="evidence-worker_1_kg_embedding_dtw"></a>
### worker_1_KG_EMBEDDING_DTW

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_1_kg_embedding_dtw)

局部距离到单调规整路径的累计代价、路径约束及近似对齐边界

- [article_168/D020 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_168.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_168.json)　事实 F020。原文证据 E037。

<a id="evidence-worker_3_kg_forced_alignment"></a>
### worker_3_KG_FORCED_ALIGNMENT

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_3_kg_forced_alignment)

转录词到声学时间段的对齐、token与词位置桥接及边界误差处理

- [article_168/D003 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_168.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_168.json)　事实 F003。原文证据 E015。

<a id="evidence-worker_4_gap_gaussian_smooth"></a>
### worker_4_gap_gaussian_smooth

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_gaussian_smooth)

沿明确的一维曲线轴或二维网格执行Gaussian核卷积，处理核宽、权重与边界；区分平滑后的统计量、原始观测与随后二次显示插值的网格语义。

- [article_205/D015 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_205.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_205.json)　事实 F013。原文证据 E041、E042。
- [article_225/D031 · 需求记录 r22](../../../analysis/literature_component_coverage/records/assessments/article_225.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_225.json)　事实 F022。原文证据 E061、E062。

<a id="evidence-worker_5_gaussian_peak_gap"></a>
### worker_5_GAUSSIAN_PEAK_gap

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_5_gaussian_peak_gap)

在已有平滑时间信号上按百分位设阈值，执行局部最大与相邻峰分离、选峰和去重，并解释检测边界的时间分辨率。

- [article_168/D008 · 需求记录 r15](../../../analysis/literature_component_coverage/records/assessments/article_168.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_168.json)　事实 F010。原文证据 E021。

<a id="evidence-worker_4_gap_wordnet_basic_sense"></a>
### worker_4_gap_wordnet_basic_sense

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_4_gap_wordnet_basic_sense)

按MIPVU区分基本义与语境义、定位WordNet synset并在无synonym时取hypernym的词义关系

- [article_054/D006 · 需求记录 r24](../../../analysis/literature_component_coverage/records/assessments/article_054.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_054.json)　事实 F009、F010。原文证据 E025、E026、E027、E028、E029。

<a id="evidence-worker_4_gap_syntax_np_prune"></a>
### worker_4_gap_syntax_np_prune

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_4_gap_syntax_np_prune)

NP及命名实体子节点识别、根保留和最深NP改写yes/no、比较类JJR/RB过滤

- [article_091/D007 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_091.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_091.json)　事实 F006、F007。原文证据 E007、E008、E009。

<a id="evidence-worker_4_gap_syntax_coref_template"></a>
### worker_4_gap_syntax_coref_template

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_4_gap_syntax_coref_template)

Y词与主语共指/修饰关系判断、跨关键词谓词抽取及过去时/that合并

- [article_123/D004 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_123.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_123.json)　事实 F004、F005、F006。原文证据 E019、E020、E021、E022、E023、E024。

<a id="evidence-kg_cortical_register"></a>
### KG_CORTICAL_REGISTER

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-kg_cortical_register)

个体解剖网格、功能到解剖配准与表面投影

- [article_121/D026 · 需求记录 r25](../../../analysis/literature_component_coverage/records/assessments/article_121.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_121.json)　事实 F025。原文证据 E041、E042。

<a id="evidence-worker_4_gap_polygon_cv"></a>
### worker_4_gap_polygon_cv

训练前手册及附录的支持程度为无支持。[返回处理结果](#gap-worker_4_gap_polygon_cv)

灰度127阈值、4连通面积>10筛选后跳过前两标签、外轮廓及.005弧长approxPolyDP顶点计数

- [article_241/D012 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_241.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_241.json)　事实 F045。原文证据 E123、E124、E125、E126。
- [article_241/D013 · 需求记录 r16](../../../analysis/literature_component_coverage/records/assessments/article_241.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_241.json)　事实 F006、F046。原文证据 E016、E127、E128。

<a id="evidence-worker_4_gap_encrypted_release"></a>
### worker_4_gap_encrypted_release

训练前手册及附录的支持程度为部分支持。[返回处理结果](#gap-worker_4_gap_encrypted_release)

公开密文与人可解密脚本的发布路径、抓取暴露面和可读性权衡

- [article_055/D018 · 需求记录 r20](../../../analysis/literature_component_coverage/records/assessments/article_055.json) · [事实与原文记录 r1](../../../analysis/literature_component_coverage/records/extractions/article_055.json)　事实 F022。原文证据 E060、E061。
