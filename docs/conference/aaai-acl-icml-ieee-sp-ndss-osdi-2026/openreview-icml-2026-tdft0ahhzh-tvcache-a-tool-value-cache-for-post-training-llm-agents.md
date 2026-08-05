---
title: "Tvcache: A Tool-Value Cache for Post-Training LLM Agents"
title_zh: TVCache：面向LLM智能体后训练的工具值缓存
authors: "Abhishek Vijaya Kumar, Bhaskar Kataria, Byungsoo Oh, Emaad Manzoor, Rachee Singh"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d1e3621dac7f3b26ccbadf9ce34b8beb98118d85.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 提出TVCACHE有状态工具值缓存，通过完整工具调用历史匹配来复用智能体后训练中的输出。
tldr: 本文针对LLM智能体后训练中工具调用耗时且GPU空闲的问题，提出TVCACHE状态化工具值缓存。它维护已观测工具调用序列的树结构，通过最长前缀匹配保证命中时环境状态完全一致，从而安全复用工具输出。在终端任务等多个工作负载上，TVCACHE大幅减少了重复工具调用时间，显著加速了智能体后训练并降低成本，是一种面向智能体训练流程的高效缓存机制。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: LLM智能体后训练中工具调用耗时数秒甚至分钟，GPU空闲，重复调用间可缓存但需保证环境状态一致。
method: 构建工具调用序列树，利用最长前缀匹配实现状态一致的工具输出缓存复用。
result: 在多种工作负载上显著减短训练时间，降低了工具调用成本。
conclusion: 状态敏感的有值工具缓存能有效加速LLM智能体的后训练过程。
---

## Abstract
In RL post-training of LLM agents, calls to external tools take several seconds or even minutes, leaving allocated GPUs idle and inflating post-training time and cost. While many tool invocations repeat across parallel rollouts and could in principle be cached, naively caching their outputs for reuse is incorrect since tool outputs depend on the environment state induced by prior agent interactions. We present TVCACHE, a stateful tool-value cache for LLM agent post-training. TVCACHE maintains a tree of observed tool-call sequences and performs longest-prefix matching for cache lookups: a hit occurs only when the agent’s full tool history matches a previously executed sequence, guaranteeing identical environment state. On three diverse workloads—terminal-based tasks, SQL generation, and video understanding—TVCACHE achieves cache hit rates of up to 70% and reduces median tool call execution time by up to 6.9×, with no degradation in post-training reward accumulation.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机和背景）

- 论文聚焦于 **LLM 智能体的强化学习（RL）后训练阶段**。在该阶段，智能体需要反复调用外部工具（如终端命令、数据库查询、视频理解模型），每次工具调用耗时数秒甚至数分钟。
- 这种高延迟工具调用导致**昂贵的 GPU 资源大量空闲**，显著拉长了后训练时间和成本。
- 作者观察到，在并行 rollout 中**大量工具调用是重复的**，因此原则上可以缓存复用，减少重复执行。
- 但**朴素缓存不可行**：工具输出依赖于“环境状态”，而环境状态由之前智能体与环境的交互历史决定。如果忽略了状态差异，直接复用缓存结果会导致训练信号错误。

## 2. 方法论：TVCACHE 的核心思想、技术细节与算法流程

- **核心思想**：构建一种**有状态的工具值缓存**（stateful tool-value cache），只在环境状态完全一致时复用工具输出，从而在保证正确性的前提下消除重复工具调用。
- **状态表示**：将智能体的完整工具调用历史作为环境状态的代理。只有在两个序列的完整工具调用历史完全一致时，才认为它们处于相同的环境状态。
- **数据结构**：维护一个**树**，记录所有已观测到的工具调用序列。树中的每条路径对应一个已经执行过的工具调用历史。
- **缓存查找机制**：采用**最长前缀匹配**（longest-prefix matching）：
  - 当一个新的 rollout 产生部分工具调用历史时，在树中查找与当前历史匹配的最长前缀；
  - 只有当“完整工具调用历史”与某个已执行序列完全匹配时，才判定为缓存命中（hit）；
  - 这样能保证命中时环境状态完全一致，从而安全复用该状态下的工具输出。
- **流程概要**：
  1. 智能体在 rollout 中调用工具；
  2. TVCACHE 在树中查找当前工具历史的最长匹配前缀；
  3. 若完整历史匹配成功，直接返回缓存中的工具输出，跳过实际工具执行；
  4. 若未命中，则真实执行工具，并将新的调用序列与输出更新到树中（作为后续缓存）。

## 3. 实验设计

- **工作负载 / 场景**：论文在**三个多样化的工作负载**上进行评估：
  - 终端任务（terminal-based tasks）
  - SQL 生成（SQL generation）
  - 视频理解（video understanding）
- **Benchmark**：摘要未明确说明具体数据集名称，但三个场景覆盖了文本指令型（终端）、结构化查询（SQL）和多模态理解（视频），体现了跨任务域的泛化能力。
- **对比方法**：摘要未提及与其他缓存方法的具体对比，仅隐含与“朴素缓存”（naive caching）进行对比，表明朴素缓存因状态不一致而不可用。TVCACHE 的基线可能是“无缓存”设置。

## 4. 资源与算力

- 摘要中**未明确说明**所使用的 GPU 型号、数量、训练时长、集群规模等算力细节。
- 仅提到“降低后训练时间和成本”，但缺乏具体资源消耗数据（如 GPU 小时数节省量）。
- 因此无法从论文摘要部分获得量化算力信息。

## 5. 实验数量与充分性

- **实验数量**：摘要仅列出三个工作负载，未提供更细粒度的实验（如不同智能体规模、不同 RL 算法、不同模型、不同缓存容量的消融实验等）。
- **充分性评估**：
  - 三项任务覆盖了**指令型、结构查询型、多模态型**三种典型工具调用场景，具有一定的多样性；
  - 但缺乏消融实验（如最长前缀匹配 vs. 状态无关匹配、树结构效率、缓存失效策略等）的公开描述；
  - 没有与已有缓存方案（如基于语义相似度或嵌入的缓存）进行系统性比较；
  - 缓存命中率和加速比是衡量有效性的关键指标，但只有中位数加速比和最高命中率，未报告分布或统计显著性。
  - 因此，实验**初步验证了有效性，但充分性、客观性和公平性**不足以在摘要层面定论。

## 6. 主要结论与发现

- TVCACHE 在三个工作负载上达到**最高 70% 的缓存命中率**。
- **中位工具调用执行时间减少最多 6.9 倍**。
- 在不影响后训练奖励累积（reward accumulation）的前提下实现加速，表明缓存复用未引入偏差或状态错误。
- 结论表明：**状态敏感的有值工具缓存**能够有效加速 LLM 智能体的后训练过程，并降低计算成本。

## 7. 优点

- **方法论严谨**：通过“完整工具历史匹配”保证环境状态一致，从根源上解决了朴素缓存的状态失效问题。
- **实现简洁可扩展**：用树结构与最长前缀匹配，既高效又易于增量更新。
- **跨任务验证**：在终端、SQL、视频三个差异较大的场景中均有效，说明方法具有通用性。
- **不牺牲训练质量**：奖励累积无退化，确保加速不是以牺牲学习效果为代价。

## 8. 不足与局限

- **资源细节缺失**：未报告 GPU 类型/数量、总训练步骤、时间节省的绝对值，导致无法评估实际部署成本效益。
- **实验完备性不足**：未展示消融研究、敏感性分析、缓存规模扩展性、失败案例（如误命中导致的错误状态）等。
- **对比基线有限**：未与基于嵌入/语义相似度的缓存、或其他工具调用优化技术（如并行执行、预测性预取）进行量化比较。
- **状态代理的假设**：将“完整工具历史”等同于“环境状态”可能并非在所有任务中都成立；对存在随机环境、或外部状态无法由工具历史完全确定的任务，该方法的正确性保障有限。
- **缓存命中率上限**：依赖 rollout 中工具历史的重复性；在探索性强的任务中命中率可能显著下降。

（完）
