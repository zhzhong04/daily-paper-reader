---
title: "Learning to Share: Selective Memory for Efficient Parallel Agentic Systems"
title_zh: 学习共享：面向高效并行智能体系统的选择性记忆
authors: "Joseph Fioresi, Parth Parag Kulkarni, Ashmal Vayani, Song Wang, Mubarak Shah"
date: 2026-04-30
pdf: "https://openreview.net/pdf/36afa45a025ea9f91750ce099712175131a4547b.pdf"
tags: ["query:agent-cache"]
score: 8.0
evidence: 通过可学习的选择性记忆共享，在并行智能体团队间复用中间结果
tldr: 针对并行多智能体系统在类似子问题上重复计算的问题，Learning to Share提出了一种可学习的共享记忆机制，能够在不同团队间选择性地复用信息并控制上下文增长。该方法在保持任务解决质量的同时显著降低计算开销，为智能体系统中的跨上下文信息复用提供了直接思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 并行智能体团队在推理相似子问题时存在大量重复计算，导致计算开销严重。
method: 设计可学习的共享记忆机制，智能选择跨团队信息进行复用，同时控制上下文长度增长。
result: 在并行智能体任务上显著减少重复计算，同时保持较高的任务解决质量。
conclusion: 证明了智能体系统通过选择性信息共享可以大幅提升效率，可启发KV缓存等推理资源的复用方案。
---

## Abstract
Agentic systems solve complex tasks by coordinating multiple agents that iteratively reason, invoke tools, and exchange intermediate results. To improve robustness and solution quality, recent approaches deploy multiple agent teams running in parallel to explore diverse reasoning trajectories. However, parallel execution comes at a significant computational cost: when different teams independently reason about similar sub-problems or execute analogous steps, they repeatedly perform substantial overlapping computation. To address these limitations, in this paper, we propose Learning to Share (LTS), a learned shared-memory mechanism for parallel agentic frameworks that enables selective cross-team information reuse while controlling context growth. LTS introduces a global memory bank accessible to all teams and a lightweight controller that decides whether intermediate agent steps should be added to memory or not. The controller is trained using stepwise reinforcement learning with usage-aware credit assignment, allowing it to identify information that is globally useful across parallel executions. Experiments on the AssistantBench and GAIA benchmarks show that LTS significantly reduces overall runtime while matching or improving task performance compared to memory-free parallel baselines, demonstrating that learned memory admission is an effective strategy for improving the efficiency of parallel agentic systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与研究动机

- **研究背景**：智能体系统（Agentic Systems）通过协调多个智能体完成复杂任务，智能体之间需要迭代推理、调用工具并交换中间结果。为了提升任务的鲁棒性和解的质量，近期方法倾向于并行运行多个智能体团队，以探索多样的推理轨迹。
- **核心问题**：并行执行带来了巨大的计算开销——当不同团队独立推理**相似子问题**或执行**类似步骤**时，它们会反复执行大量重叠计算，造成严重的计算资源浪费。
- **整体含义**：该论文旨在解决并行智能体系统中的"重复计算"痛点，探索如何在多个团队之间安全、高效地复用中间推理结果，从而在维持任务解决质量的前提下显著降低计算成本。

## 2. 方法论：Learning to Share (LTS)

- **核心思想**：提出一种**可学习的共享记忆机制**，通过全局记忆银行（global memory bank）在并行团队之间实现选择性的跨团队信息复用，同时严格控制上下文长度的增长。
- **关键技术组件**：
  - **全局共享记忆银行**：所有并行团队均可访问的统一记忆存储，保存具有全局复用价值的中间智能体步骤。
  - **轻量级控制器（Lightweight Controller）**：决定某个中间步骤是否应被写入共享记忆。
  - **强化学习训练**：使用**逐步强化学习（stepwise reinforcement learning）** 配合**感知用量的信用分配（usage-aware credit assignment）** 训练控制器，使其学会识别哪些信息在并行执行中对多个团队具有全局效用。

## 3. 实验设计

- **评测基准（Benchmark）**：
  - **AssistantBench**：面向智能体助手能力的综合评测集。
  - **GAIA**：通用智能体辅助任务基准，包含需要多步推理与工具调用的现实场景。
- **对比方法**：主要对比**无共享记忆的并行基线（memory-free parallel baselines）**，即在同等并行架构下不进行跨团队信息复用的方法。
- **评价指标**：整体运行时间（runtime）、任务解决质量（task performance）。

## 4. 资源与算力

- **原文未明确说明**：该论文的摘要中未提及GPU型号、数量、训练时长或推理阶段的硬件配置等具体算力信息。
- 仅能从模型设计推测：控制器为"轻量级"，额外开销较小，但具体硬件环境无从得知。

## 5. 实验数量与充分性

- **实验数量**：
  - 两个主流基准数据集（AssistantBench、GAIA）上的主实验。
  - 根据摘要描述，未明确提及额外的消融实验或变体分析。
- **充分性评估**：
  - **优点**：所选的 AssistantBench 和 GAIA 均为智能体领域公认的基准，具有一定代表性。
  - **不足**：从摘要来看，缺乏针对不同并行规模（如团队数量）、不同记忆容量上限、控制器不同训练策略的系统性消融分析；也未报告方差或多次运行的统计显著性。整体实验丰富度一般，结论的说服力依赖于论文正文中的完整实验设计。

## 6. 主要结论与发现

- LTS 在 **显著降低整体运行时间** 的同时，能够 **匹配或提升** 任务性能（相比无记忆的并行基线）。
- 证明了"学习式记忆准入（learned memory admission）"是提升并行智能体系统效率的有效策略。
- 从更广的视角来看，该工作表明智能体系统中的选择性信息共享可以大幅提升效率，可为 KV 缓存等推理资源的跨上下文复用提供启发。

## 7. 优点

- **问题切入精准**：直击并行智能体系统中高频出现的"相似子问题重复计算"痛点，实际意义强。
- **方法设计巧妙**：将"是否写入共享记忆"建模为可学习的决策问题，用强化学习训练控制器，避免了人工设计规则的不灵活性。
- **针对性技术细节**：采用 stepwise RL 与 usage-aware credit assignment，能够细粒度地识别"对多个团队都有用"的中间信息，具有较强的技术深度。
- **效率与质量兼顾**：同时优化了计算开销和任务性能两个目标，实用价值高。
- **泛化启示**：提出的思路不仅限于智能体系统本身，还可迁移至 KV 缓存管理、多任务推理复用等相关场景。

## 8. 不足与局限

- **算力信息缺失**：未报告训练和推理的具体硬件配置，难以评估部署门槛与实际资源需求。
- **实验覆盖有限**：仅两个 benchmark，且未明确报告消融实验；缺少对记忆容量、团队数量、任务类型多样性等关键因素的敏感性分析。
- **抽象信息不足**：目前仅能基于摘要分析，缺乏对控制器训练细节、奖励设计、记忆读取/写入机制的算法级描述。
- **潜在偏差风险**：GAIA 和 AssistantBench 中的任务类型可能存在偏向，在更广泛的实际部署场景中的泛化能力尚待验证。
- **应用限制**：共享记忆可能引入跨团队的噪声信息，当任务间相关性较弱时，选择性共享的收益可能下降甚至带来负面干扰，这一风险在摘要中未被讨论。
- **可行性未充分验证**："显著降低运行时间"的量化幅度、"匹配或提升"的具体指标数值均未在摘要中给出，需要阅读全文验证统计显著性。

---

（完）
