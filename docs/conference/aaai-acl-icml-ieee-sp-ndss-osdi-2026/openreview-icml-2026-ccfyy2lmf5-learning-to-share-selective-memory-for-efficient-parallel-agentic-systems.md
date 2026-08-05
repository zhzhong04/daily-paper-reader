---
title: "Learning to Share: Selective Memory for Efficient Parallel Agentic Systems"
title_zh: 学习共享：高效并行智能体系统的选择性记忆
authors: "Joseph Fioresi, Parth Parag Kulkarni, Ashmal Vayani, Song Wang, Mubarak Shah"
date: 2026-04-30
pdf: "https://openreview.net/pdf/36afa45a025ea9f91750ce099712175131a4547b.pdf"
tags: ["query:cache-reuse"]
score: 8.0
evidence: 并行智能体间选择性信息复用以避免重叠计算
tldr: 并行智能体系统在解决复杂任务时，不同团队常对相似子问题重复计算，带来高昂开销。本文提出学习共享（LTS），一种可学习的共享记忆机制，让并行智能体框架能够选择性地跨团队复用信息，并控制上下文增长。实验证明LTS能在保持解答质量的同时显著降低计算成本，为高效多智能体协作提供了新思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 并行智能体重复计算相似子问题，造成大量计算浪费。
method: 提出可学习的共享记忆机制LTS，选择性跨团队复用信息并控制上下文增长。
result: 实验显示显著降低重叠计算成本，保持任务性能。
conclusion: LTS能有效提升并行智能体系统的计算效率。
---

## Abstract
Agentic systems solve complex tasks by coordinating multiple agents that iteratively reason, invoke tools, and exchange intermediate results. To improve robustness and solution quality, recent approaches deploy multiple agent teams running in parallel to explore diverse reasoning trajectories. However, parallel execution comes at a significant computational cost: when different teams independently reason about similar sub-problems or execute analogous steps, they repeatedly perform substantial overlapping computation. To address these limitations, in this paper, we propose Learning to Share (LTS), a learned shared-memory mechanism for parallel agentic frameworks that enables selective cross-team information reuse while controlling context growth. LTS introduces a global memory bank accessible to all teams and a lightweight controller that decides whether intermediate agent steps should be added to memory or not. The controller is trained using stepwise reinforcement learning with usage-aware credit assignment, allowing it to identify information that is globally useful across parallel executions. Experiments on the AssistantBench and GAIA benchmarks show that LTS significantly reduces overall runtime while matching or improving task performance compared to memory-free parallel baselines, demonstrating that learned memory admission is an effective strategy for improving the efficiency of parallel agentic systems.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：智能体（Agentic）系统通过协调多个智能体迭代推理、调用工具、交换中间结果来解决复杂任务。为提高鲁棒性和解答质量，近期方法常部署**多个并行智能体团队**，探索多样化的推理路径。
- **核心问题**：并行执行带来了显著的计算开销——不同团队在独立推理时，常对**相似子问题**或**类比步骤**进行大量**重复计算**，造成计算资源的浪费。
- **整体含义**：论文旨在解决并行智能体系统中的“重复劳动”问题，通过让团队间**选择性共享信息**来消除冗余计算，从而在不牺牲任务性能的前提下显著降低计算成本。

## 2. 方法论

- **核心思想**：提出 **Learning to Share（LTS）**，一种**可学习的共享记忆机制**，使并行智能体框架能够跨团队选择性复用信息，同时控制上下文（context）增长。
- **技术细节**：
  - 设置一个**全局记忆库（global memory bank）**，对所有团队开放访问。
  - 引入一个**轻量级控制器（lightweight controller）**，决策每个中间智能体步骤是否应写入记忆库，实现**选择性记忆写入**。
  - 控制器通过**逐步强化学习（stepwise reinforcement learning）** 训练，采用**usage-aware credit assignment（基于使用情况的信用分配）**，使控制器学会识别哪些信息在并行执行中具有**全局有用性**。
- **算法流程（文字说明）**：各团队并行执行任务 → 每一步产生中间结果 → 控制器评估该结果是否值得共享 → 若值得，则写入全局记忆库 → 其他团队可在后续推理中读取该记忆，避免重复计算 → 通过RL训练持续优化控制器的决策策略。

## 3. 实验设计

- **数据集/Benchmark**：
  - **AssistantBench**：面向复杂信息检索与推理的智能体基准。
  - **GAIA**：通用AI助手基准，包含需要多步推理和工具调用的真实世界任务。
- **对比方法**：
  - 主要对比**无记忆的并行基线（memory-free parallel baselines）**，即传统并行智能体框架，团队间不进行信息共享。
- **评估指标**：
  - **整体运行时间（runtime）**：衡量计算效率。
  - **任务性能（task performance）**：衡量解答质量。

## 4. 资源与算力

- 论文在提供的摘要和元数据中**未明确说明**使用的GPU型号、数量、训练时长等算力信息。
- 仅能推断训练过程涉及**强化学习**训练轻量级控制器，但具体计算资源消耗未披露。

## 5. 实验数量与充分性

- **实验组数**：在**两个基准**（AssistantBench 和 GAIA）上进行了实验，并与无记忆并行基线对比。
- **充分性评估**：
  - **覆盖度有限**：仅对比了一种基线类型（无记忆并行），未提及与其他共享机制或优化方法的比较。
  - **缺少消融细节**：摘要中未具体说明是否包含对控制器设计、RL训练策略、记忆库容量等组件的消融实验。
  - **公平性**：论文声称LTS在降低运行时间的同时匹配或提升任务性能，但缺乏更细粒度的统计分析或多次运行方差报告。
  - 总体而言，**初步验证了有效性**，但实验的全面性和深度仍有提升空间。

## 6. 主要结论与发现

- LTS在AssistantBench和GAIA基准上**显著降低了整体运行时间**，同时**匹配或提升了任务性能**，与无记忆的并行基线相比。
- 结论表明：**学习式的记忆准入策略（learned memory admission）** 是提升并行智能体系统计算效率的有效手段。

## 7. 优点

- **问题定位精准**：直击并行智能体系统中普遍存在的重复计算痛点，具有实际意义。
- **方法论创新**：将记忆共享问题转化为**可学习的决策问题**，用强化学习训练控制器，而非手工设计共享规则。
- **可控上下文增长**：不仅提升效率，还考虑了对上下文长度的管理，避免记忆库无限膨胀。
- **结果明确**：实验显示效率与性能可以兼得，具有较强的实践价值。

## 8. 不足与局限

- **实验覆盖不足**：仅两个基准，且只对比无记忆基线，缺少更多样化的场景和更强的基线方法。
- **消融分析缺失**：控制器训练细节、记忆策略的关键组件缺乏系统性消融验证。
- **算力信息未披露**：无法评估训练LTS控制器本身的成本是否合理，可能影响实用性判断。
- **潜在偏差风险**：RL训练的目标函数与评估指标之间的对齐程度、记忆库跨任务的泛化能力尚不明确。
- **应用限制**：LTS仅针对**并行智能体框架**，对串行或混合架构的适用性未作讨论；记忆共享可能引入信息泄漏或错误传播风险，论文未深入分析。

（完）
