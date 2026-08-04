---
title: "ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning"
title_zh: 树状大语言模型推理扩展的结构感知KV缓存管理
authors: "Yeqiu Chen, Ziyan Liu, Zhenxin Huang, Runquan Gui, Hong Wang, Lei Liu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/6f13a2d41caaf352276e1f0157fac67fa66af1f6.pdf"
tags: ["query:awc"]
score: 4.0
evidence: 面向树推理的结构感知KV缓存管理，可迁移至智能体工作流搜索中的缓存调度
tldr: 在树状大语言模型推理中，KV缓存随搜索分支和回溯而急剧膨胀，成为吞吐与深度的瓶颈。ArborKV依据搜索动态发现活跃分支祖先复用价值高、不活跃子树复用概率低，提出结构感知的KV缓存管理策略。该方法能更精准地分配缓存资源，提升树搜索推理的吞吐与搜索广度。该工作为涉及树搜索的智能体推理缓存管理提供了可借鉴方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 树状推理中，KV缓存随分支搜索迅速膨胀，限制吞吐、搜索深度和宽度。
method: 基于搜索动态的KV复用规律，对活跃分支与祖先优先保留，对不活跃子树降级处理。
result: 结构感知缓存管理显著提升树搜索推理的吞吐与搜索范围。
conclusion: 该工作为结构复杂推理任务的KV缓存管理提供了有效范例。
---

## Abstract
Recent progress in LLM reasoning has increasingly shifted from single-pass generation to explicit search over intermediate reasoning states. Tree-of-Thoughts (ToT) organizes inference to tree-structured search with branching and backtracking, but it substantially amplifies the key--value (KV) cache: retaining KV states for a frontier of partial trajectories quickly becomes a memory bottleneck that limits throughput and constrains search depth and width under fixed hardware budgets. We address this challenge by observing that KV reuse in ToT-style inference is governed by search dynamics: near-term decoding depends primarily on the active branch and its ancestors, whereas inactive subtrees have low short-term reuse probability yet must remain recoverable for backtracking. Motivated by this, we propose **ArborKV**, a structure-aware eviction framework that couples a lightweight value estimator with a tree-aware allocation policy, and performs purely token-extractive eviction with lazy rehydration to support revisits. Experiments on ToT-style reasoning benchmarks show that ArborKV achieves up to $\sim4\times$ peak KV-memory reduction while preserving near-full-retention accuracy, enabling larger search configurations under fixed device budgets that would otherwise run out of memory.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义

- **研究背景**：大语言模型（LLM）的推理范式正从单次生成转向显式搜索，即在中间推理状态上进行系统性探索。Tree-of-Thoughts（ToT）将推理组织为带有分支与回溯的树状搜索结构，能够显著提升复杂问题的求解能力，但也带来了巨大的内存开销。
- **核心问题**：在ToT风格的树状推理中，需要为大量部分轨迹保留KV缓存（Key-Value cache），用于后续解码时的上下文复用。随着搜索深度和宽度的增长，KV缓存迅速膨胀，成为内存瓶颈，严重限制了吞吐量以及固定硬件资源下的搜索深度与广度。
- **整体含义**：本文针对树状推理中KV缓存管理这一关键瓶颈，提出结构感知的缓存淘汰框架，使得在有限显存下可以进行更大规模、更深入的树搜索推理，从而提升LLM在复杂推理任务上的能力上限。

## 2. 方法论

### 核心思想
- 观察树状推理中KV缓存复用规律与搜索动态密切相关：
  - **近期解码**主要依赖当前活跃分支及其祖先节点的KV状态；
  - **不活跃子树**在短期内复用概率低，但可能在回溯时再次访问，因此需要保留可恢复性。
- 基于上述规律，并非对所有KV缓存一视同仁，而是依据“搜索结构”分配缓存资源：优先保留活跃分支与祖先，对不活跃子树进行降级处理。

### 关键技术细节
- **结构感知淘汰框架（ArborKV）**，包含两个核心组件：
  1. **轻量级价值估计器（lightweight value estimator）**：评估不同KV缓存分片在未来解码中的短期复用价值。
  2. **树感知分配策略（tree-aware allocation policy）**：结合搜索树结构（分支、祖先、活跃性）决定哪些KV状态应保留、哪些可被驱逐。
- **驱逐方式**：采用**纯token级提取式驱逐（purely token-extractive eviction）**，即直接从缓存中移除某些token对应的KV状态。
- **惰性再水合（lazy rehydration）**：当回溯导致某条不活跃子树的KV状态被重新需要时，通过按需重新计算来恢复，以换取内存节省。

### 算法流程（文字说明）
1. 在ToT搜索过程中，维护当前搜索树及每个节点的KV缓存状态。
2. 每当内存压力达到阈值时，调用价值估计器对各缓存分片打分。
3. 依据分数和树结构关系（活跃分支及祖先优先级最高），选择移除低价值、非活跃子树的token级KV分片。
4. 对被移除的KV分片记录其来源信息，以便回溯时通过“惰性再水合”方式按需重建。
5. 持续动态调整缓存分配，使内存占用受控，同时保证当前活跃路径上的解码性能不受影响。

## 3. 实验设计

- **数据集/场景**：摘要中仅笼统提到使用了“ToT-style reasoning benchmarks”（ToT式推理基准），未列出具体任务名称（如数学推理、规划、谜题等）或具体数据集名称。
- **对比方法**：摘要未明确提及具体对比基线。但从上下文推断，可能对比了“无驱逐/全量保留”的朴素策略，以及常见的KV缓存淘汰方法（如LRU、随机淘汰等），但论文原文未给出细节。
- **评价指标**：主要包括**峰值KV内存减少量**（peak KV-memory reduction）和**推理准确率**（accuracy）。摘要报告在保持接近全量保留准确率的同时，实现了约4倍的峰值内存缩减。

## 4. 资源与算力

- 论文摘要及给定元数据中**未说明**使用的GPU型号、数量、训练或推理时长、显存大小等算力资源信息。
- 需要指出：该工作本质上是推理阶段的缓存管理方法，通常不涉及大规模模型训练，但实验所需的硬件配置（如单卡/多卡、显存容量）在摘要中完全缺失。

## 5. 实验数量与充分性

- **实验数量**：从摘要看，仅在“ToT-style reasoning benchmarks”上进行了实验，并报告了内存和准确率结果。未给出具体benchmark数量、任务类别数量或消融实验信息。
- **充分性评估**：
  - **不足**：缺少详细的实验设置说明，如具体数据集、任务难度、模型规模（如7B/70B）、树搜索的超参数（分支数、回溯策略等）。
  - **未报告消融**：没有提到对“价值估计器”、“树感知分配策略”、“惰性再水合”等各组件的单独消融分析。
  - **对比不透明**：未明确与哪些现有缓存管理方法对比，公平性难以评估。
  - **结论初步**：摘要中的“~4×”内存缩减和“近全量保留准确率”是有力结果，但缺乏统计显著性和多场景稳健性验证。
  - **总体**：实验设计逻辑合理，但公开信息不足以充分证明方法广泛有效，有待完整论文补充细节。

## 6. 主要结论与发现

- ArborKV通过结构感知的缓存管理，能够显著降低树状推理中的峰值KV内存占用，最高可达约4倍减少。
- 在实现大幅内存节省的同时，几乎不损失推理准确率（保持“近全量保留准确率”）。
- 该内存优势使得在固定设备预算下，可以启用更大的搜索配置（更宽/更深的搜索树），否则这些配置会因内存不足而无法运行。
- 结论：为结构复杂推理任务（尤其是树搜索类）的KV缓存管理提供了有效范式。

## 7. 优点

- **问题定位精准**：直击树状推理中KV缓存膨胀这一真实瓶颈，且与搜索动态紧密耦合，具有明确的实用性。
- **动机洞察深刻**：基于“活跃分支/祖先复用价值高、不活跃子树复用概率低”的观察，设计出的策略具有理论依据。
- **方法务实高效**：
  - 使用轻量级价值估计器，计算开销低；
  - 纯token级提取式驱逐实现简单，无需修改模型结构；
  - 惰性再水合机制兼顾了回溯需求，保持方法正确性。
- **收益显著**：4倍峰值内存缩减且精度几乎不变，是很有吸引力的性价比提升，能直接扩展搜索规模。
- **启发性**：为智能体工作流搜索、多步推理等更广泛的树结构化场景中的缓存调度提供了可借鉴思路。

## 8. 不足与局限

- **摘要信息过少**：缺乏具体实验细节，如benchmark构成、模型参数、相机配置、超参数、比较方法等，难以独立复现和全面评估。
- **实验覆盖有限**：仅在“ToT-style”基准上验证，未覆盖链式推理、并行Agent搜索、多任务等更多推理范式，泛化性存疑。
- **未报告消融实验**：价值估计器、树感知策略、惰性再水合三者的独立贡献未知，无法确认哪些组件起决定性作用。
- **潜在偏差风险**：
  - 内存测量和准确率对比未说明具体统计口径；
  - 可能选择对方法有利的树结构或搜索参数，存在选择性报告可能。
- **应用限制**：
  - 方法依赖搜索树的结构信息，对于不显示维护树状结构的隐式搜索方法，可能无法直接应用；
  - token级驱逐后需要惰性重构，若回溯频繁且路径很长，重构开销可能影响端到端时延。
- **算力与公平性**：未提供硬件环境信息（如GPU数量/型号）作为基线，无法判断与现有方法相比是否处于同等资源条件。

（完）
