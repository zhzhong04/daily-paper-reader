---
title: "Tvcache: A Tool-Value Cache for Post-Training LLM Agents"
title_zh: Tvcache：面向LLM智能体后训练的工具值缓存
authors: "Abhishek Vijaya Kumar, Bhaskar Kataria, Byungsoo Oh, Emaad Manzoor, Rachee Singh"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d1e3621dac7f3b26ccbadf9ce34b8beb98118d85.pdf"
tags: ["query:awc"]
score: 9.0
evidence: 面向LLM智能体后训练的状态化工具值缓存，采用最长前缀匹配，直接处理智能体工作流缓存调度
tldr: LLM智能体RL后训练中外部工具调用耗时数秒至数分钟，导致GPU空闲且成本高昂，而简单复用工具输出会因环境状态改变而失效。TVCACHE提出状态化工具值缓存，以工具调用序列构建树，通过最长前缀匹配确保命中时环境状态一致。在终端任务等三类工作负载上显著降低后训练时间与成本，是智能体工作流缓存调度的直接范例。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: RL后训练中工具调用耗时且重复，朴素缓存因环境状态依赖而不可用。
method: 构建工具调用序列树并采用最长前缀匹配，仅在全历史匹配时缓存命中，保证环境状态一致。
result: 在多种工作负载上显著降低GPU空闲时间和后训练开销。
conclusion: 状态化缓存为智能体工作流中的可复用计算调度提供了可靠实现方法。
---

## Abstract
In RL post-training of LLM agents, calls to external tools take several seconds or even minutes, leaving allocated GPUs idle and inflating post-training time and cost. While many tool invocations repeat across parallel rollouts and could in principle be cached, naively caching their outputs for reuse is incorrect since tool outputs depend on the environment state induced by prior agent interactions. We present TVCACHE, a stateful tool-value cache for LLM agent post-training. TVCACHE maintains a tree of observed tool-call sequences and performs longest-prefix matching for cache lookups: a hit occurs only when the agent’s full tool history matches a previously executed sequence, guaranteeing identical environment state. On three diverse workloads—terminal-based tasks, SQL generation, and video understanding—TVCACHE achieves cache hit rates of up to 70% and reduces median tool call execution time by up to 6.9×, with no degradation in post-training reward accumulation.

---

## 论文详细总结（自动生成）

# 论文总结：Tvcache: A Tool-Value Cache for Post-Training LLM Agents

## 1. 核心问题与整体含义

- **研究动机**：在 LLM 智能体的强化学习（RL）后训练阶段，智能体需要频繁调用外部工具（如终端命令、SQL 引擎、视频理解 API），单次工具调用可能耗时数秒甚至数分钟。在此期间，已分配的 GPU 只能空闲等待，导致后训练时间被显著拉长、计算成本大幅上升。
- **核心挑战**：虽然许多工具调用在并行 rollout 中重复出现，理论上可以缓存复用，但**朴素缓存不可行**——因为工具输出依赖于智能体先前交互所导致的**环境状态**，相同的调用在不同状态下可能产生不同结果。
- **论文含义**：提出一种**有状态（stateful）的工具值缓存**机制，使工具调用结果可以安全复用，同时保证环境状态一致性，从而降低后训练时间和成本。

## 2. 方法论

- **核心思想**：将工具调用的历史序列视为环境状态的“指纹”，只有当前完整工具调用历史与某个已执行过的序列完全匹配时，才允许缓存命中。
- **实现技术**：
  - **维护工具调用序列树**：所有观察过的工具调用序列被组织为前缀树（trie），每个节点对应一次工具调用及其输出。
  - **最长前缀匹配（Longest-Prefix Matching）**：当智能体产生新的工具调用时，将其完整历史序列在树中查找；只有命中一个完整路径（即整个历史都匹配），才复用缓存输出。
  - **状态一致性保证**：由于环境状态完全由先前的工具序列决定，因此“全历史匹配”即可确保当前环境状态与缓存时相同，从而避免朴素缓存的状态错乱问题。
- **算法流程（文字描述）**：
  1. 初始化一棵空树，根节点代表初始状态。
  2. 每次智能体执行工具调用时，沿树中对应子节点查询。
  3. 若从根到当前节点的路径完整存在，则缓存命中，直接返回缓存结果；否则执行真实工具调用，并将新序列加入树中。
  4. 后训练过程中不断扩展树，提高后续命中率。

## 3. 实验设计

- **数据集 / 场景**：覆盖三个多样化的任务负载：
  - **终端任务**（terminal-based tasks）
  - **SQL 生成**（SQL generation）
  - **视频理解**（video understanding）
- **Benchmark**：使用这些任务上的 RL 后训练流程，监控缓存命中率、工具调用执行时间、后训练奖励累积。
- **对比方法**：文摘中明确提到“朴素缓存”（naïvely caching outputs）作为错误基线；未提及更多对比方法。实际中可能对比“无缓存”情况。

## 4. 资源与算力

- **摘要与元数据中均未明确说明**所使用的 GPU 型号、数量、训练时长、集群规模等具体算力信息。
- 仅能推断该研究涉及大规模 RL 后训练实验，且优化目标直接指向 GPU 空闲时间和总后训练成本，但具体资源细节需查阅论文全文。

## 5. 实验数量与充分性

- **实验数量**：摘要中报告了三个不同负载上的实验结果，并给出了主要指标（最高 70% 缓存命中率、最多 6.9× 中位工具调用时间下降、奖励累积无退化）。未提及消融实验或更多变体。
- **充分性评估**：
  - 覆盖了三种差异较大的任务类型（交互式终端、结构化查询、多媒体理解），具有一定代表性。
  - 但缺少关于缓存规模、命中率分布、长尾场景、超参数影响等细节；也未报告统计显著性检验。
  - 由于基于摘要信息，无法判断实验是否包含消融（如不同匹配策略、树结构变体）或公平性对比。总体而言，初步结果积极，但充分性需要全文验证。

## 6. 主要结论与发现

- TVCACHE 在三个不同负载上实现**最高 70% 的缓存命中率**。
- 将**中位工具调用执行时间降低高达 6.9×**，显著减少 GPU 空闲等待。
- **不损害后训练奖励累积**，即优化效率的同时保证了训练质量。
- 验证了“状态化缓存”对智能体工作流中可复用计算调度的有效性。

## 7. 优点

- **问题定位精准**：直接针对 RL 后训练中工具调用导致的 GPU 闲置和成本痛点。
- **方法简洁且有原则**：通过“完整历史匹配”这一强约束，优雅地规避了环境状态依赖问题，逻辑清晰。
- **通用性强**：不依赖具体工具类型，适用于终端、SQL、视频等多种接口。
- **潜力明显**：可显著降低 LLM 智能体训练成本，便于规模化应用。

## 8. 不足与局限

- **信息不完整**：由于基于摘要和元数据总结，缺乏方法细节、定理证明、伪代码、完整实验表格等，部分结论需以全文为准。
- **缓存效率上限**：最长前缀匹配要求全历史一致，在工具历史长度较大或行动多变时命中率可能下降；未讨论树的内存占用与搜索开销。
- **实验有限**：仅报告三个任务的汇总指标，无消融、无失败案例分析、无与更先进缓存策略的对比。
- **偏差风险**：工具调用时间下降可能与任务本身重复率高度相关，三个任务中终端/视频任务的重复模式可能偏高，普适性需更多场景验证。
- **未报告算力**：缺少资源占用和能耗对比，削弱了“节省成本”主张的可量化说服力。

（完）
