# Selected papers without model adjustment

本目录是项目当前筛选结果中的独立文章库，只包含模型调整专项审计结果为 `NO_HOLD` 的文章。

## 内容

- 文章：118篇
- PDF：`papers/article_001.pdf`—`papers/article_118.pdf`
- 全文文本：`texts/article_001.txt`—`texts/article_118.txt`
- 人类可读目录：`SELECTED_ARTICLES.md`
- 新旧编号映射：`NUMBER_MAPPING.csv`
- 结构化元数据：`selected_articles.csv`、`selected_articles.jsonl`
- 文件哈希：`SHA256SUMS`
- 筛选口径：`provenance/selection_policy.md`
- 全文修复记录：`provenance/fulltext_repair_record.md`
- 发布验证：`validation.json`

## “无模型调整”的含义

纳入文章的正式实验可以使用现成模型/API，以及 prompt、system prompt、in-context examples、解码、采样、RAG、工具调用或不更新权重的推理期干预；但不要求作者进行预训练、继续预训练、SFT、LoRA、adapter、soft prompt、RLHF/DPO/PPO/GRPO、知识编辑，或训练正式实验必需的分类器、probe、回归头、reward model与RL代理。

普通统计分析、回归及认知模型拟合不被视为调整被测神经模型。

## 编号和追溯

本目录使用独立连续编号001—118。`source_selected_number`及`NUMBER_MAPPING.csv`保留它们在170篇来源selected集合中的原编号；稳定内部ID没有改变。

## 状态边界

这是内容筛选和模型调整审计后的文章集合。个别条目的截止日前正式版本资格仍可能保留在元数据的 `formal_date_status` 中，不能把内容纳入自动解释为所有形式资格均已最终确认。

## 文件性质

这里的PDF和文本均为普通独立文件，不是符号链接。`SHA256SUMS`和`validation.json`用于验证文件完整性。
