# 无模型调整文章库筛选口径

本集合来自170篇内容筛选通过的selected文章，并于2026-10-11应用模型调整专项审计。

## 纳入本库

正式实验使用现有checkpoint或API，或者仅进行以下操作：

- 修改prompt或system prompt；
- in-context examples / few-shot；
- temperature、解码和采样；
- RAG、外部记忆和工具调用；
- 不更新权重的推理期干预；
- 普通统计分析、回归和认知模型拟合；
- 多个现成模型投票或组成jury。

## 不纳入本库

正式实验需要作者执行以下任一操作：

- 从头训练或继续预训练；
- SFT、微调；
- LoRA、adapter、soft prompt；
- RLHF、DPO、PPO、GRPO；
- 知识编辑；
- 训练Tokenizer后重新训练模型；
- 训练正式实验必需的分类器、probe、回归头、reward model或RL代理。

## 结果

- 来源selected：170篇；
- 本库收录：118篇；
- 模型调整hold：52篇；
- 模糊项：0篇。
