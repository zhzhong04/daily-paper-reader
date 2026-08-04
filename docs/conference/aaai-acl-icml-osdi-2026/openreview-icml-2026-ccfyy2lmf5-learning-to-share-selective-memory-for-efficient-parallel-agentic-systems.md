---
title: "Learning to Share: Selective Memory for Efficient Parallel Agentic Systems"
title_zh: 学会共享：面向高效并行智能体系统的选择性记忆
authors: "Joseph Fioresi, Parth Parag Kulkarni, Ashmal Vayani, Song Wang, Mubarak Shah"
date: 2026-04-30
pdf: "https://openreview.net/pdf/36afa45a025ea9f91750ce099712175131a4547b.pdf"
tags: ["query:cache-reuse"]
score: 7.0
evidence: 并行智能体系统中的选择性跨团队信息复用，契合跨上下文缓存复用
tldr: 并行运行的多个智能体团队常对相似子问题或步骤重复计算，造成大量资源浪费。Learning to Share（LTS）提出一种学习式共享记忆机制，使团队间能够选择性地复用信息，同时控制上下文增长。这本质上消除跨团队重复计算，与多智能体间共享上下文缓存以避免重算的目标一致，可为缓存复用提供策略参考。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 并行智能体团队独立推理时存在大量重叠计算，增加成本。
method: 提出学习式共享记忆机制（LTS），选择性复用跨团队信息并控制上下文增长。
result: 在并行智能体框架上减少重复计算，提升资源效率。
conclusion: 通过共享记忆实现跨团队信息复用，与缓存复用目标一致，可启发智能体缓存共享设计。
---

## Abstract
Agentic systems solve complex tasks by coordinating multiple agents that iteratively reason, invoke tools, and exchange intermediate results. To improve robustness and solution quality, recent approaches deploy multiple agent teams running in parallel to explore diverse reasoning trajectories. However, parallel execution comes at a significant computational cost: when different teams independently reason about similar sub-problems or execute analogous steps, they repeatedly perform substantial overlapping computation. To address these limitations, in this paper, we propose Learning to Share (LTS), a learned shared-memory mechanism for parallel agentic frameworks that enables selective cross-team information reuse while controlling context growth. LTS introduces a global memory bank accessible to all teams and a lightweight controller that decides whether intermediate agent steps should be added to memory or not. The controller is trained using stepwise reinforcement learning with usage-aware credit assignment, allowing it to identify information that is globally useful across parallel executions. Experiments on the AssistantBench and GAIA benchmarks show that LTS significantly reduces overall runtime while matching or improving task performance compared to memory-free parallel baselines, demonstrating that learned memory admission is an effective strategy for improving the efficiency of parallel agentic systems.

---

## 论文详细总结（自动生成）

# 论文总结：Learning to Share: Selective Memory for Efficient Parallel Agentic Systems

## 1. 核心问题与整体含义（研究动机和背景）

- **背景**：智能体系统（Agentic systems）通过协调多个智能体进行迭代推理、工具调用和中间结果交换来解决复杂任务。为提升鲁棒性和答案质量，近期方法并行部署多个智能体团队，探索多样化的推理轨迹。
- **核心问题**：并行执行带来显著的计算开销——不同团队在独立推理相似子问题或执行类似步骤时，会重复进行大量重叠计算，造成资源浪费。
- **整体含义**：本文旨在通过“选择性共享记忆”机制来消除跨团队的重复计算，从而在保持任务性能的同时提升并行智能体系统的效率。这与跨上下文缓存复用（cache reuse）的目标高度一致，可为多智能体间的缓存共享设计提供策略参考。

## 2. 论文提出的方法论

- **核心思想**：提出 Learning to Share（LTS），一种**学习式共享记忆机制**，允许并行团队之间选择性地复用信息，同时控制上下文增长。
- **关键技术细节**：
  - **全局记忆库（Global Memory Bank）**：所有团队共享的全局记忆存储，可保存对多个团队有用的中间步骤信息。
  - **轻量级控制器（Lightweight Controller）**：负责决定每个智能体的中间步骤是否应被添加到全局记忆库中，实现选择性信息录入。
  - **训练方式**：使用**逐步强化学习（stepwise reinforcement learning）** 并配合**使用感知的信用分配（usage-aware credit assignment）**，使控制器学会识别哪些信息在并行执行中具有全局价值。
  - **流程示意**：各团队并行运行 → 产生中间步骤 → 控制器评估该步骤是否具有跨团队复用价值 → 若有用则写入全局记忆库 → 后续团队可从记忆库中读取并复用，同时通过选择性机制避免上下文无限增长。
- **公式与算法**：摘要中未给出具体公式；算法流程如上所述，属于学习式记忆准入控制机制。

## 3. 实验设计

- **数据集 / 基准**：
  - **AssistantBench**：面向助手型智能体的多步骤推理基准。
  - **GAIA**：通用AI助手基准，涵盖多种复杂任务。
- **对比方法**：
  - 主要对比“无记忆的并行基线”（memory-free parallel baselines），即不进行跨团队信息复用的标准并行智能体框架。
  - 未提及对比其他记忆机制或缓存复用方法。
- **评估指标**：包括整体运行时间（runtime）和任务性能（task performance）。

## 4. 资源与算力

- **摘要中未明确说明**：未提及GPU型号、数量、训练时长、参数量等算力信息。
- **结论**：论文在资源与算力方面缺乏可量化的公开信息，无法据此评估训练成本或可复现性。

## 5. 实验数量与充分性

- **实验数量**：摘要中仅提及两个基准（AssistantBench 和 GAIA）上的实验结果，未明确描述具体实验组数（如不同基线的数量、超参数敏感性测试、消融实验的详细设计）。
- **充分性评估**：
  - 从摘要信息看，实验覆盖了两个主流基准，验证了LTS在减少运行时间方面的有效性，但实验规模相对有限。
  - 未提及消融实验（如控制器不同训练策略、记忆库大小、选择阈值的敏感性）、跨不同智能体架构的泛化实验，以及与其他记忆/缓存方法的对比，因此充分性和全面性有待加强。
  - 基线仅描述为“memory-free parallel baselines”，对比范围较窄，可能不足以证明LTS的优势是普遍性的。

## 6. 论文的主要结论与发现

- LTS在AssistantBench和GAIA上**显著减少了整体运行时**，同时**匹配或改善了任务性能**，相比无记忆并行基线有明显优势。
- 验证了“学习式记忆准入”是一种提升并行智能体系统效率的有效策略。
- 论文隐含结论：跨团队选择性信息复用可以在避免上下文爆炸的前提下，消除大量重复计算，为并行智能体的资源优化提供了新思路。

## 7. 优点

- **问题针对性强**：精准识别了并行智能体系统中的重复计算痛点，具有实际应用价值。
- **方法新颖**：将“记忆准入控制”建模为强化学习问题，并引入使用感知的信用分配，让控制器学习全局有用的信息，而非简单启发式规则。
- **效率与性能兼顾**：不仅降低运行时间，还能保持甚至提升任务性能，表明选择性共享不会牺牲答案质量。
- **与缓存复用高度相关**：其核心思想可直接迁移至跨上下文缓存设计，具有启示意义。

## 8. 不足与局限

- **信息不完整**：提供的材料仅包含摘要，缺乏方法细节、公式、实验设置、消融分析和算力信息，难以进行深入验证。
- **实验覆盖有限**：仅两个基准，且对比基线类型单一，未与显式缓存复用方法或其他记忆机制对比，说服力受限。
- **泛化性未知**：未讨论在不同类型智能体（如工具调用频繁型、多轮对话型）、不同记忆容量或长上下文场景下的表现。
- **偏差风险**：强化学习训练可能依赖特定任务分布，存在过拟合基准的风险；控制器决策的“全局有用性”定义也可能存在偏差。
- **应用限制**：学习式共享记忆需要训练，部署成本较高；在任务分布变化剧烈或团队数量较小时，收益可能不明显。

（完）
