# LLM心理学与行为科学入选文章

本目录保存243篇通过统一筛选标准的文章。标准见[selection_criteria.md](provenance/selection_criteria.md)：同一正式实验单元必须满足来源与日期、T0、T1和E1—E4。

正式实验须能够以文本稳定执行、研究明确的心理学或行为科学问题，并且不要求自行训练、微调、更新参数或训练必要学习组件。具体适用的实验单元以逐篇终审记录为准；文章中其他独立实验不自动获得纳入资格。

## 当前集合

- `article_001`—`article_118`：既有118篇，本次编号、PDF和文本均未改变。
- `article_119`—`article_243`：新增125篇，来自3,811篇原缺摘要组完成摘要优先筛选后的全文终审。
- 新组摘要阶段3,635篇有摘要文章已全部审查；176篇仍无摘要，保留待补证。
- 141篇直接全文候选与21篇来源/日期通过记录形成162篇终审目标，最终125篇纳入、37篇排除；另5篇在前置日期核验排除。
- 旧摘要组45篇未决记录继续延后，不计入本库。

## 文件

- [SELECTED_ARTICLES.md](SELECTED_ARTICLES.md)：文章目录，点击题名打开PDF。
- `papers/`和`texts/`：243篇PDF与243份文本，均为独立普通文件。
- `selected_articles.jsonl`、`selected_articles.csv`：结构化清单。
- `NUMBER_MAPPING.csv`：正式编号、来源编号和稳定ID映射。
- `SHA256SUMS`：486份正文文件的SHA-256。
- [provenance/selection_criteria.md](provenance/selection_criteria.md)：v1.6统一标准，本次未改动。
- [provenance/stage_b_included_reviews.jsonl](provenance/stage_b_included_reviews.jsonl)：新增125篇的来源与日期、纳入实验单元、门槛、结果与证据页码；保留既有视觉检查记录，不附本地渲染缓存。
- [provenance/release_243.json](provenance/release_243.json)：增量发布范围及溯源哈希。
- `summary.json`、`validation.json`：集合摘要和本次文件发布验证；验证不代替科学全文终审。
- [provenance/fulltext_repair_record.md](provenance/fulltext_repair_record.md)：既有两篇全文修复记录。
- [NOTICE.md](NOTICE.md)：原文权利说明。

沿用`selected_no_model_adjustment`路径，以保持已有引用可用。目录名不表示筛选标准只有“无需微调”。本次只更新共享仓库的文献区。
