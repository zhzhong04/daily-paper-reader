---
title: "CONCUR: High-Throughput Agentic Batch Inference of LLM via Congestion-Based Concurrency Control"
title_zh: CONCUR：基于拥塞控制的LLM智能体批量高吞吐推断
authors: "qiaoling chen, Zhisheng Ye, Tian Tang, Peng Sun, Boyu Tian, Guoteng Wang, Shenggui Li, Yonggang Wen, Zhenhua Han, Tianwei Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/34e588f95f3adb2d1771f68b0ac1a31d517885fb.pdf"
tags: ["query:agent-cache"]
score: 8.0
evidence: 面向智能体批量推理的基于拥塞控制的主动式KV缓存调度，直接处理智能体工作流中的缓存管理
tldr: 论文发现智能体批量推理中KV缓存在中阶段发生抖动，缓存效率随长期智能体积累状态而崩坏。受分布式系统拥塞控制启发，将KV缓存视为共享资源，提出主动式、代理级的准入控制来调节负载。实验显示该机制可缓解吞吐下降，强调应从响应式请求级缓存管理转向主动式智能体级调度，为智能体工作流缓存管理提供新视角。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 智能体批量推理会持续累积KV缓存，导致中阶段缓存效率崩塌，吞吐严重下降。
method: 借鉴拥塞控制思想，将KV缓存视为共享资源，提出主动式agent级准入控制，进行反馈驱动的调节。
result: 有效缓解中阶段抖动，提升批量推断吞吐，避免了缓存耗尽前的性能坍塌。
conclusion: 智能体工作流需要主动、agent层面的缓存管理，而不是仅停留在请求级反应式处理。
---

## Abstract
Batch inference for agentic workloads stresses the GPU key–value (KV) cache in a sustained and cumulative manner, often causing severe throughput degradation well before memory capacity is exhausted. We identify this phenomenon as middle-phase thrashing, a previously under-characterized pathology in which cache efficiency collapses as long-lived agents accumulate state over time.

We argue that mitigating this pathology requires moving beyond reactive, request-level cache management to proactive, agent-level admission control. Drawing inspiration from congestion control in distributed systems, we view the KV cache as a shared resource whose efficient utilization depends on feedback-driven regulation. Based on this insight, we present CONCUR, a lightweight control layer that regulates agent admission to bound aggregate cache pressure while preserving execution continuity. CONCUR adapts a cache-aware control algorithm to dynamically adjust the number of active agents using runtime cache signals.

Across large models and real-world agent workloads, CONCUR prevents middle-phase thrashing and improves batch inference throughput by up to 4.09× on Qwen3-32B and 1.90× on DeepSeek-V3, while remaining compatible with existing LLM serving systems.

---

## 论文详细总结（自动生成）

# CONCUR 论文总结

> 说明：所提供的“论文 PDF 提取文本”实际为 OpenReview 的浏览器验证页面，未包含论文全文。以下总结严格基于可获得的论文元数据与摘要信息，部分细节（如公式、完整实验设置）无法展开，已在相应位置明确标注。

## 1. 核心问题与整体含义

- **研究对象**：面向智能体（agentic）工作负载的 LLM 批量推理（batch inference）。
- **核心问题**：智能体工作负载会持续、累积地占用 GPU 的 KV 缓存（key–value cache），即使远未达到显存容量上限，也会导致严重的吞吐下降。
- **关键现象**：作者将这一现象命名为 **middle-phase thrashing（中阶段抖动/颠簸）**——随着长期存活（long-lived）的智能体不断积累状态，缓存效率在中段突然崩溃。
- **整体含义**：现有的请求级（request-level）、反应式（reactive）缓存管理不足以应对智能体工作负载；缓存管理需要上升到 **智能体级（agent-level）的主动调度与控制**。

## 2. 方法论：核心思想与技术细节

- **核心思想**：将 KV 缓存视为一种**共享资源**，借鉴分布式系统中的**拥塞控制（congestion control）**思想，通过反馈驱动机制来调节负载，避免缓存过载和效率崩塌。
- **提出的方法**：**CONCUR**——一个轻量级控制层（lightweight control layer）。
  - 对智能体的进入进行**准入控制（admission control）**，限制同时活跃的智能体数量。
  - 目的是**限制聚合缓存压力（bound aggregate cache pressure）**，同时尽量保持智能体执行过程的连续性。
  - 使用**缓存感知的控制算法（cache-aware control algorithm）**，根据运行时缓存信号（runtime cache signals）动态调整活跃智能体数量。
- **公式/算法流程**：摘要中未给出具体公式。从文字描述看，其闭环流程为：
  1. 监测运行时 KV 缓存状态；
  2. 根据缓存拥塞程度计算允许的活跃智能体数量；
  3. 对新进入或待继续执行的智能体进行准入/拒绝决策；
  4. 通过反馈循环持续调节，使缓存压力维持在安全范围内。
- **兼容性**：CONCUR 设计为与现有 LLM serving 系统兼容，可作为一个附加控制层部署。

## 3. 实验设计

- **模型规模**：
  - Qwen3-32B
  - DeepSeek-V3
- **工作负载**：真实世界的智能体工作负载（real-world agent workloads），但摘要未具体说明是哪些任务或数据集。
- **对比方法**：摘要中未明确列出基线方法；从动机推断，对比对象可能包括“无控制/不限制并发”或“请求级反应式缓存管理”等做法，但无法确认。
- **评价指标**：批量推理吞吐（batch inference throughput），以及是否发生 middle-phase thrashing。

## 4. 资源与算力

- 论文摘要中**未明确说明**使用的 GPU 型号、数量、训练时长或推理基础设施细节。
- 仅能确定实验涉及百亿/千亿级模型（32B 和 DeepSeek-V3），需要较强的多卡/多节点推理环境，但具体算力配置无法从现有信息中获知。

## 5. 实验数量与充分性

- 摘要中提及的实验规模有限：两个模型、一类（真实智能体）工作负载、一个核心指标（吞吐）。
- **充分性评估**：
  - 优点：覆盖了不同规模/架构的模型（Qwen3 与 DeepSeek-V3），说明方法有一定通用性。
  - 不足：缺少数据集明细、工作负载类型、对比基线数量、消融实验（如控制算法不同参数、不同缓存阈值）等关键信息。
  - 偏差风险：若实验仅在某类智能体轨迹上验证，可能无法代表所有 agentic 工作负载；需要更多多样化的场景来证明普适性。
- 总体而言，现有摘要信息不足以充分判断实验的全面性与公平性，需要查看全文中的详细实验设置。

## 6. 主要结论与发现

- **发现一**：智能体批量推理中的性能退化主要是“中阶段抖动”造成的，而不仅仅是缓存容量不足。
- **发现二**：将 KV 缓存视为共享资源，用拥塞控制思路进行主动的智能体级准入控制，可以有效防止这种退化。
- **定量结论**：
  - 在 Qwen3-32B 上，批量推理吞吐最高提升 **4.09×**；
  - 在 DeepSeek-V3 上，批量推理吞吐最高提升 **1.90×**。
- **总体结论**：智能体工作流需要**主动、智能体层面**的缓存管理，而不是停留在请求级、反应式处理。

## 7. 优点

- **问题识别有新意**：提出“middle-phase thrashing”这一此前未被充分刻画的现象，为智能体推理性能优化提供了新视角。
- **思想迁移自然**：将分布式系统的拥塞控制引入 LLM KV 缓存管理，类比合理且有理论支撑。
- **方法轻量且兼容**：CONCUR 被设计为轻量控制层，能兼容现有 serving 系统，部署成本较低。
- **目标明确**：不是简单扩容显存或优化单请求缓存，而是从系统负载控制角度解决问题，具有较高的实际价值。

## 8. 不足与局限

- **信息可见性有限**：由于只能看到摘要，无法评估具体算法实现、控制器的稳定性/收敛性等细节。
- **实验覆盖可能有限**：仅透露两个模型和真实 agent 负载，缺少对不同智能体任务类型、不同并发规模、不同缓存容量压力条件的系统测试。
- **缺少消融与对比细节**：没有说明与哪些基线对比、是否做了消融实验、吞吐提升的绝对数值如何（可能基数较低时倍数意义有限）。
- **应用限制**：主动准入控制可能引入额外延迟或影响交互式智能体任务的实时性；对“执行连续性”的保证机制也未被说明。
- **未提及算力开销**：控制层自身的计算/内存开销没有在摘要中给出，可能影响实际部署判断。

（完）
