---
title: Learning to Evict from Key-Value Cache
title_zh: 学习从键值缓存中驱逐
authors: "Luca Moschella, Laura Manduchi, Ozan Sener"
date: 2026-04-30
pdf: "https://openreview.net/pdf/875c835732794c107c4793b6fb93559f5ecd4c2c.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 通过强化学习智能体学习KV缓存驱逐策略，可迁移到基于智能体的系统中
tldr: 现有KV缓存驱逐依赖启发式（如最近性、注意力分数），仅间接反映未来效用且带来开销。本文提出KVP框架，将驱逐形式化为强化学习问题，每头使用轻量级RL智能体对Token的未来效用排序，并基于整体奖励学习专门策略。实验显示其优于启发式驱逐方法，为LLM缓存管理提供了可迁移的学习式驱逐策略。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有KV缓存驱逐方法依赖启发式指标，无法直接反映Token未来效用且计算开销高。
method: 提出KVP框架，将驱逐建模为强化学习，用轻量级逐头RL智能体基于键值向量学习Token排序策略。
result: 在训练的生成轨迹上，KVP优于基于启发式的缓存驱逐基线，降低了推理成本。
conclusion: 学习式驱逐策略能更有效地管理KV缓存，并适用于LLM驱动的代理系统。
---

## Abstract
The growing size of Large Language Models (LLMs) makes efficient inference challenging, primarily due to the memory demands of the autoregressive Key-Value (KV) cache. Existing eviction or compression methods reduce cost but rely on heuristics, such as recency or past attention scores, which serve only as indirect proxies for a token’s future utility and introduce computational overhead. We reframe KV cache eviction as a reinforcement learning (RL) problem: learning to rank tokens by their predicted usefulness for future decoding. To this end, we introduce KV Policy (KVP), a framework of lightweight per-head RL agents trained on pre-computed generation traces using only key and value vectors. Each agent learns a specialized eviction policy guided by a holistic reward, derived from future utility, that evaluates the quality of the ranking across all cache budgets, requiring no modifications to the underlying LLM or additional inference. Evaluated across two model families on the long-context benchmark RULER (up to 128K tokens) and the multi-turn dialogue benchmark OASST2-4k, KVP significantly outperforms strong baselines. Zero-shot tests on standard downstream tasks (BoolQ, LongBench passage retrieval, GovReport) further show that KVP generalizes beyond its training distribution and to considerably longer sequence lengths. These results demonstrate that learning to predict future token utility is a powerful and scalable paradigm for adaptive KV cache management.

---

## 论文详细总结（自动生成）

## 论文总结

### 1. 核心问题与整体含义（研究动机和背景）
- 大规模语言模型（LLM）推理面临的主要瓶颈是自回归解码过程中键值（Key-Value, KV）缓存的内存占用越来越大。
- 现有 KV 缓存驱逐或压缩方法通常依赖启发式规则（如最近性、历史注意力分数），但这些指标只是 token 未来效用的间接代理，且会引入额外计算开销。
- 论文主张将 KV 缓存驱逐问题重新定义为强化学习（RL）问题：通过学习对 token 在解码中的未来有用性进行排序，从而使驱逐策略更直接、更高效。
- 整体含义：提出**KVP（KV Policy）**框架，用轻量级 RL 智能体实现自适应的缓存管理，为 LLM 推理降本增效提供新范式。

### 2. 方法论：核心思想、关键技术细节、流程
- **核心思想**：学习预测 token 的未来效用，并按此排序决定哪些 token 应被驱逐。
- **关键技术细节**：
  - 采用**逐头（per-head）轻量级 RL 智能体**，每个注意力头学习独立的驱逐策略。
  - 智能体训练仅使用**键（key）和值（value）向量**，无需修改底层 LLM 或进行额外推理。
  - 训练数据来源于**预计算的生成轨迹**（pre-computed generation traces）。
  - 奖励设计为**整体奖励（holistic reward）**，基于未来效用，并跨越所有缓存预算评估排序质量。
- **流程（文字说明）**：
  1. 收集预生成的 LLM 对话/续写轨迹，提取 KV 向量。
  2. 为每个注意力头初始化轻量级 RL 智能体。
  3. 以键值向量为输入，智能体输出 token 的效用排序。
  4. 根据排序执行驱逐，并计算综合奖励（覆盖不同缓存预算下的未来解码表现）。
  5. 通过强化学习更新智能体，学习最优驱逐策略。

### 3. 实验设计
- **数据集 / 场景**：
  - **RULER**：长上下文评测基准，序列长度最高达 **128K tokens**。
  - **OASST2-4k**：多轮对话评测基准。
  - **零样本下游任务**：BoolQ、LongBench passage retrieval（段落检索）、GovReport。
- **模型家族**：在**两个不同模型家族**上进行了评估。
- **对比方法**：与**强基线（strong baselines）**对比，但摘要中未明确列出具体基线名称。

### 4. 资源与算力
- 论文提供的文本信息中**未明确提及**训练所用的 GPU 型号、数量、训练时长或能耗等资源细节。
- 只能推测其方法为轻量级逐头 RL 智能体，且仅使用键值向量，因此计算开销可能较低，但具体数值无从得知。

### 5. 实验数量与充分性
- 实验覆盖了长上下文、多轮对话、零样本通用任务等多个场景，且跨两个模型家族，整体设计较为全面。
- 但摘要中**没有给出具体的性能数值、基线比较细节、消融实验或超参数敏感性分析**，因此无法完全客观地评估实验的公平性与充分性。
- 论文声明显著优于强基线，但缺少可验证的具体结果支撑。

### 6. 主要结论与发现
- KVP 在 RULER 和 OASST2-4k 上显著优于基于启发式的缓存驱逐基线。
- 零样本测试表明 KVP 能泛化到训练分布之外的场景，并扩展到比训练时更长的序列长度。
- 结论：学习预测 token 未来效用是一种**强大且可扩展**的自适应 KV 缓存管理范式，可有效降低推理成本，并适用于 LLM 驱动的代理系统。

### 7. 优点
- **问题重新定义**：将缓存驱逐从启发式转向 RL 学习，更直接地优化未来效用。
- **轻量级设计**：逐头小代理，仅使用键值向量，避免了修改 LLM 或增加推理负担。
- **整体奖励**：单一奖励函数统一评估所有缓存预算下的排序质量，策略具有全局观。
- **强泛化能力**：零样本跨任务、跨长度表现良好，说明学到的是通用驱逐规律。
- **不侵入底层模型**：训练和推理解耦，易于集成到现有系统中。

### 8. 不足与局限
- **信息不完整**：文中未提供基线的具体名称、性能数值、消融实验等关键细节，限制了可复现性评判。
- **算力信息缺失**：未报告训练资源和时间，难以评估实际部署成本。
- **可能依赖轨迹质量**：训练依赖预计算生成轨迹，轨迹分布与真实在线分布可能存在偏差。
- **逐头智能体**：虽然轻量，但可能未建模跨头交互，对复杂上下文中的驱逐决策可能不够全面。
- **未来效用奖励的度量**：如何精确、无偏地估计“未来效用”仍是挑战，摘要未展开说明其定义或计算方式。

（完）
