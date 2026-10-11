# LLM心理学与行为科学入选文章

本目录保存118篇通过统一筛选标准的文章。它不是单纯的“无微调论文库”：所有文章同时满足来源与日期、T0、T1和E1—E4。

完整标准只有一份：[`provenance/selection_criteria.md`](provenance/selection_criteria.md)。

## 统一标准

- **T0：文本可执行。**正式实验的模型输入、输出和计分可以用文本或确定性的离散结构稳定执行。
- **T1：不要求训练或参数更新。**正式复现不要求自行预训练、微调、LoRA、RL、知识编辑，或训练必需的分类器、probe、回归头、reward model等学习组件。
- **E1—E4：心理学与行为科学资格。**LLM是相关行为实验主体；研究的是明确的心理学／行为科学问题；构念与实验可重建；结果可以解释行为规律。

Prompt、system prompt、few-shot／in-context examples、解码、采样、RAG、工具调用、不更新权重的推理期干预，以及普通统计分析或认知模型拟合，不视为训练或微调。

## 当前集合

- 入选：118篇；
- 来源内容候选：170篇；
- 其中52篇因正式实验需要训练、微调、参数更新或必要学习组件而未进入本集合；
- PDF和全文文本均为独立普通文件，不是符号链接或替身文件；
- 本集合编号为`article_001`—`article_118`。

## 文件

- `papers/`：118篇PDF；
- `texts/`：118份全文文本；
- `SELECTED_ARTICLES.md`：人类可读目录；
- `selected_articles.csv`、`selected_articles.jsonl`：结构化清单；
- `NUMBER_MAPPING.csv`：本集合编号与来源集合编号的对应关系；
- `SHA256SUMS`：PDF和文本的SHA-256；
- `provenance/selection_criteria.md`：唯一筛选标准；
- `provenance/fulltext_repair_record.md`：两份全文文件的修复记录；
- `summary.json`、`validation.json`：集合摘要与校验结果。

## 编号与边界

本目录按入选顺序重新连续编号。来源集合编号保存在`source_selected_number`和`NUMBER_MAPPING.csv`中，稳定内部ID未改变。

目录名`selected_no_model_adjustment`为发布时沿用的技术路径；判断文章是否合格时，以v1.6统一标准全文为准，而不是仅看目录名。
