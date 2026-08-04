---
title: Learning to Evict from Key-Value Cache
title_zh: 从键值缓存中学习驱逐策略
authors: "Luca Moschella, Laura Manduchi, Ozan Sener"
date: 2026-04-30
pdf: "https://openreview.net/pdf/875c835732794c107c4793b6fb93559f5ecd4c2c.pdf"
tags: ["query:awc"]
score: 9.0
evidence: 基于强化学习的缓存驱逐策略，使用每头智能体，直接匹配智能体系统中的缓存驱逐策略
tldr: 现有KV缓存驱逐方法依赖近期性或历史注意力分数等启发式规则，与token未来效用仅有间接关联且带来额外开销。论文将KV缓存驱逐重构为强化学习排序问题，提出KV Policy（KVP）框架：基于预计算生成轨迹，用每头轻量级RL智能体学习专用驱逐策略，并由整体奖励指导排序。该方法为缓存驱逐策略提供了基于智能体的学习范式，直接契合智能体系统中缓存驱逐算法的需求。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有KV缓存驱逐依赖启发式规则，不能直接反映token未来效用。
method: 将驱逐建模为强化学习排序问题，用每头轻量级RL智能体学习专用驱逐策略，并以整体奖励指导。
result: 在生成轨迹上训练的驱逐智能体能学习到更优的驱逐策略，降低推理成本。
conclusion: 为KV缓存驱逐提供了一种新颖的强化学习多智能体方法，可直接用于智能体系统缓存管理。
---

## Abstract
The growing size of Large Language Models (LLMs) makes efficient inference challenging, primarily due to the memory demands of the autoregressive Key-Value (KV) cache. Existing eviction or compression methods reduce cost but rely on heuristics, such as recency or past attention scores, which serve only as indirect proxies for a token’s future utility and introduce computational overhead. We reframe KV cache eviction as a reinforcement learning (RL) problem: learning to rank tokens by their predicted usefulness for future decoding. To this end, we introduce KV Policy (KVP), a framework of lightweight per-head RL agents trained on pre-computed generation traces using only key and value vectors. Each agent learns a specialized eviction policy guided by a holistic reward, derived from future utility, that evaluates the quality of the ranking across all cache budgets, requiring no modifications to the underlying LLM or additional inference. Evaluated across two model families on the long-context benchmark RULER (up to 128K tokens) and the multi-turn dialogue benchmark OASST2-4k, KVP significantly outperforms strong baselines. Zero-shot tests on standard downstream tasks (BoolQ, LongBench passage retrieval, GovReport) further show that KVP generalizes beyond its training distribution and to considerably longer sequence lengths. These results demonstrate that learning to predict future token utility is a powerful and scalable paradigm for adaptive KV cache management.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究背景**：大语言模型（LLM）规模不断增大，自回归解码过程中的键值（Key-Value, KV）缓存会消耗大量显存，成为高效推理的主要瓶颈。
- **现有方法的不足**：已有的 KV 缓存驱逐（eviction）或压缩方法虽能降低内存开销，但大多依赖启发式规则（如 token 的近期性、历史注意力分数等）。这些启发式指标只是 token 未来有用性的间接代理，并非直接衡量其后续解码的价值，而且还会引入额外的计算开销。
- **核心问题**：如何直接从数据中学习一种“能预测 token 未来效用”的驱逐策略，从而在有限缓存预算下保留最有用的信息，提升长上下文推理的效率与质量。
- **整体含义**：论文将 KV 缓存驱逐重新建模为**强化学习排序问题**，使驱逐策略可以针对每个注意力头进行专门学习，为自适应 KV 缓存管理提供了一种基于智能体的可扩展新范式。

## 2. 论文提出的方法论

- **核心思想**：将 KV 缓存驱逐视为一个**排序问题**——根据 token 对后续解码的预测有用性对所有 token 进行排序，然后按缓存预算保留排序靠前的部分。
- **方法名称**：**KV Policy（KVP）**框架。
- **关键设计**：
  - 为模型的**每个注意力头**配备一个轻量级强化学习智能体（per-head RL agent）。
  - 智能体在**预先生成的生成轨迹（pre-computed generation traces）**上训练，仅使用 KV 向量作为输入，不修改底层 LLM，也不引入额外推理开销。
  - 训练时使用一个**整体奖励（holistic reward）**，该奖励基于 token 的未来效用计算，用于评估所有缓存预算下排序质量的好坏。
- **算法流程（文字说明）**：
  1. 先用目标 LLM 在若干任务上生成轨迹，收集 KV 缓存变化过程及后续 token 的依赖关系；
  2. 对每个注意力头，定义状态为当前 KV 缓存内容，动作为选择要驱逐的 token，奖励来自排序质量（如后续解码的困惑度或命中率折算）；
  3. 每个智能体通过强化学习学习一个专用驱逐策略，目标是在任意缓存预算下最大化整体奖励；
  4. 推理时，每个头按各自策略动态驱逐低效用 token，从而控制整体缓存大小。

## 3. 实验设计

- **训练/评估基准**：
  - **RULER**：长上下文 benchmark，评估序列长度高达 **128K tokens**。
  - **OASST2-4k**：多轮对话 benchmark。
- **零样本泛化测试**：在标准下游任务上直接测试，包括
  - **BoolQ**（问答/推理）
  - **LongBench passage retrieval**（长文档检索）
  - **GovReport**（长文摘要）
  - 测试序列长度远超训练分布，用于验证泛化能力。
- **对比方法**：论文提到“显著优于强基线（strong baselines）”，但摘要中未列出具体基线名称。通常该类工作会对比近期性驱逐、注意力分数驱逐、H2O、StreamingLLM 等启发式方法。
- **模型家族**：使用了两个不同的模型家族进行实验，但摘要未说明具体型号。

## 4. 资源与算力

- 原文摘要和元数据中**未明确说明**使用的 GPU 型号、数量、训练时长等算力信息。
- 因此无法给出具体资源清单。若需了解，应查阅论文正文中的实验设置部分。

## 5. 实验数量与充分性

- **实验组数**：摘要中提到了三个 benchmark（RULER、OASST2-4k、零样本下游任务），涵盖长上下文、多轮对话、问答、检索、摘要等多种任务类型，且跨越两个模型家族和不同的序列长度。
- **充分性评估**：
  - 从覆盖范围看，实验设计较为**全面**：既考察了训练分布内性能，也考察了分布外零样本泛化和长度外推。
  - 但摘要未展示**消融实验**（如去掉每头智能体、替换奖励函数、不同缓存预算下的表现曲线等），也未给出具体数值和误差线，因此无法完全判断其统计显著性和公平性。
  - 缺少与更多先进基于学习的驱逐方法对比的细节。整体而言，实验设计框架是合理的，但需要结合全文才能确认其充分性。

## 6. 论文的主要结论与发现

- 在长上下文基准 RULER（最高 128K）和多轮对话基准 OASST2-4k 上，KVP **显著优于强基线**。
- 在 BoolQ、LongBench passage retrieval、GovReport 等下游任务上的零样本测试表明，KVP 具备良好的**泛化能力**，可迁移到训练分布之外，且能处理**显著更长的序列**。
- 结论：**学习预测 token 未来效用**是一种强大且可扩展的自适应 KV 缓存管理范式，比固定启发式规则更有效。

## 7. 优点

- **问题建模新颖**：将缓存驱逐从启发式切换为强化学习排序问题，直接优化 token 的未来效用。
- **轻量级多智能体设计**：每个注意力头独立学习策略，避免单一全局策略带来的次优；且智能体仅用 KV 向量，无需修改原模型，不增加推理计算负担。
- **训练方式离线化**：利用预计算轨迹训练，对基础模型无侵入性，便于部署。
- **整体奖励引导**：使用跨缓存预算的整体奖励评估排序质量，使策略在动态缓存规模下都能保有一定鲁棒性。
- **实验泛化性较强**：覆盖多种任务、多个模型家族，并验证零样本与长度外推，增强了说服力。

## 8. 不足与局限

- **资源与训练成本未明确**：摘要未提及训练智能体所需的计算资源、时间开销，可能限制可复现性。
- **基线信息不完整**：未列出具体对比方法，无法准确评估相对提升幅度。
- **缺乏消融与敏感性分析**：没有说明每头智能体的必要性、奖励设计不同选择的影响、不同缓存预算下的性能曲线等。
- **潜在偏差风险**：训练轨迹来自特定模型分布，可能偏好训练时使用的任务类型；零样本泛化虽好，但下游任务数量有限，覆盖面仍有限。
- **应用限制**：只能处理 KV 缓存驱逐问题，对需要重计算或模型结构修改的压缩方法无法比较；多智能体策略在推理时可能需要额外状态存储，实际部署开销需评估。

（完）
