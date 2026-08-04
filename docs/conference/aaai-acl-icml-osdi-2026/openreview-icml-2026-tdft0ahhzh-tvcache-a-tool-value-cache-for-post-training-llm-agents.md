---
title: "Tvcache: A Tool-Value Cache for Post-Training LLM Agents"
title_zh: TVCACHE：用于LLM智能体后训练的工具值缓存
authors: "Abhishek Vijaya Kumar, Bhaskar Kataria, Byungsoo Oh, Emaad Manzoor, Rachee Singh"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d1e3621dac7f3b26ccbadf9ce34b8beb98118d85.pdf"
tags: ["query:agent-cache"]
score: 5.0
evidence: 为Agent后训练设计状态化工具值缓存，最长前缀匹配复用；属Agent缓存但针对工具输出而非KV
tldr: LLM智能体RL后训练中，外部工具调用耗时长导致GPU空闲，且工具输出依赖环境状态，朴素缓存复用会出错。TVCACHE维护观察到的工具调用序列树，通过最长前缀匹配查找缓存，仅当完整工具历史一致时命中，确保环境状态相同。在终端任务等三种负载上显著降低后训练时间和成本。该工作体现了Agent工作流中的缓存调度价值，但缓存对象是工具值而非KV缓存。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 工具调用耗时数分钟使GPU空闲，重复调用浪费后训练成本，环境状态依赖导致朴素缓存不正确。
method: 用工具调用序列树记录完整历史，采用最长前缀匹配确保环境状态一致时命中缓存。
result: 在多个负载上减少重复工具调用，降低后训练时间与成本。
conclusion: 为状态敏感的Agent工作流缓存提供有效启发，但缓存的是工具输出而非KV张量。
---

## Abstract
In RL post-training of LLM agents, calls to external tools take several seconds or even minutes, leaving allocated GPUs idle and inflating post-training time and cost. While many tool invocations repeat across parallel rollouts and could in principle be cached, naively caching their outputs for reuse is incorrect since tool outputs depend on the environment state induced by prior agent interactions. We present TVCACHE, a stateful tool-value cache for LLM agent post-training. TVCACHE maintains a tree of observed tool-call sequences and performs longest-prefix matching for cache lookups: a hit occurs only when the agent’s full tool history matches a previously executed sequence, guaranteeing identical environment state. On three diverse workloads—terminal-based tasks, SQL generation, and video understanding—TVCACHE achieves cache hit rates of up to 70% and reduces median tool call execution time by up to 6.9×, with no degradation in post-training reward accumulation.

---

## 论文详细总结（自动生成）

# 论文总结：TVCACHE：用于LLM智能体后训练的工具值缓存

## 1. 核心问题与整体含义（研究动机和背景）

- 在LLM智能体的强化学习（RL）后训练过程中，智能体需要调用外部工具（如终端、SQL数据库、视频理解API等）。
- 这些外部工具调用通常需要数秒甚至数分钟才能完成，导致已分配的GPU在等待期间处于空闲状态，显著增加后训练的时间和成本。
- 虽然许多工具调用在并行的rollout中会重复出现，直觉上可以缓存其输出来复用，但**朴素缓存是不正确的**：工具输出依赖于由先前智能体交互所导致的环境状态（environment state），简单复用会得到错误结果。
- 因此，核心问题是如何在保证环境状态一致的前提下，安全地复用工具调用结果，从而降低后训练开销。

## 2. 方法论

- **核心思想**：提出一种“状态化工具值缓存”（Stateful Tool-Value Cache），记为TVCACHE。
- **数据结构**：维护一棵“已观测工具调用序列树”（tree of observed tool-call sequences），记录所有曾经执行过且产生过工具输出的工具调用历史。
- **缓存查找策略**：执行**最长前缀匹配**（longest-prefix matching）。当智能体的完整工具历史与之前某条已执行序列完全一致时，才判定为缓存命中。
- **关键保证**：只有完整工具历史完全一致，才能确保当前环境状态与缓存命中时的环境状态相同，从而保证复用工具输出是正确、安全的。
- 该方法无需修改模型或训练算法，只作为缓存层插入到后训练流程中，对原训练过程透明。

## 3. 实验设计

- **实验场景（benchmark）**：三个多样化的负载：
  1. 基于终端的任务（terminal-based tasks）
  2. SQL生成（SQL generation）
  3. 视频理解（video understanding）
- **对比方法**：摘要中未明确说明对比了哪些基线，但隐含对比对象包括“无缓存”和“朴素缓存”（naive caching）。具体基线设置需查阅全文。
- **主要指标**：缓存命中率（cache hit rate）、工具调用执行时间（tool call execution time）、后训练奖励累积（post-training reward accumulation）。

## 4. 资源与算力

- 论文摘要和元数据中**未明确说明**使用的GPU型号、数量、训练时长等具体算力资源。
- 也没有提供关于集群规模、训练成本的具体数值。
- 只能从摘要推断：外部工具调用耗时是主要瓶颈，TVCACHE缓解了GPU空闲问题，但具体硬件配置缺失。

## 5. 实验数量与充分性

- **实验数量**：共三个不同领域的负载，覆盖面较广，可以看到方法在不同任务类型上的普遍性。
- **消融实验**：摘要中未提及消融实验，例如不同匹配策略、缓存容量限制、状态一致性验证等。
- **充分性与客观性**：
  - 实验结果报告了命中率、时间加速倍数和奖励无下降，基本能说明有效性。
  - 但缺乏与更多基线的对比细节、误差范围、多次运行统计分析等，因此完整性一般。
  - 三个场景虽然是多样化的，但未覆盖所有工具调用型Agent场景，且每个场景的规模未知。

## 6. 主要结论与发现

- TVCACHE在三个负载上实现了**最高70%的缓存命中率**。
- 将工具调用的**中位执行时间最多减少了6.9倍**。
- 同时**没有降低后训练中的奖励累积**，即复用缓存不会损害最终训练效果。
- 结论：通过状态感知的缓存机制，可以有效减少重复工具调用，大幅降低LLM智能体后训练的时间和成本。

## 7. 优点

- **状态感知设计**：明确考虑了工具输出对环境状态的依赖，避免朴素缓存带来的错误。
- **简洁高效的匹配算法**：使用树结构+最长前缀匹配，在保证正确性的前提下提供快速查找。
- **即插即用**：作为缓存层插入，不改变模型和训练算法，易于集成。
- **实用价值高**：直接面向后训练成本痛点，实验显示显著加速，且不会影响性能。
- **场景多样**：覆盖交互式终端、结构化查询、多模态理解三类不同工具，展示通用性。

## 8. 不足与局限

- **信息不完整**：摘要和元数据未提供实验细节，如具体数据集、任务规模、基线实现、评估标准、超参数等，无法完全复现和验证。
- **未报告算力开销**：没有说明缓存维护本身消耗的计算和内存资源，以及缓存容量限制。
- **未讨论缓存失效策略**：当环境状态无限多样或工具历史过长时，缓存命中率可能下降；没有分析缓存大小与命中率的关系。
- **未涉及安全性与隐私**：工具输出可能包含敏感数据，缓存其值可能带来数据泄露风险。
- **未提及与现有agent缓存工作（如KV缓存）的关系**：只缓存工具值而非KV张量，在更广义的缓存框架中定位尚不清晰。
- **实验公平性存疑**：没有说明是否与无缓存/朴素缓存进行同条件对比，也没有报告方差或多次运行结果。

---

（完）
