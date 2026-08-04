---
title: "CONCUR: High-Throughput Agentic Batch Inference of LLM via Congestion-Based Concurrency Control"
title_zh: CONCUR：基于拥塞控制的LLM智能体批量推理高吞吐并发管理
authors: "qiaoling chen, Zhisheng Ye, Tian Tang, Peng Sun, Boyu Tian, Guoteng Wang, Shenggui Li, Yonggang Wen, Zhenhua Han, Tianwei Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/34e588f95f3adb2d1771f68b0ac1a31d517885fb.pdf"
tags: ["query:awc"]
score: 9.0
evidence: 面向智能体批量推理的智能体级KV缓存准入控制，直接对应智能体工作流的缓存调度
tldr: 智能体批量推理会持续累积GPU KV缓存，导致在内存未满前吞吐量就大幅下降，作者将其定义为中阶段抖动。CONCUR将该问题视为共享资源的拥塞控制问题，提出主动的智能体级准入控制，利用反馈驱动机制调节缓存使用。实验证明该机制能有效缓解缓存崩溃，显著提升智能体工作负载的批处理吞吐量。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 智能体工作负载在批量推理中长时间累积KV缓存，造成内存未满时吞吐率急剧下降的中阶段抖动问题。
method: 借鉴拥塞控制思想，将KV缓存视为共享资源，设计智能体级准入控制与反馈调节策略。
result: 实验显示CONCUR能有效避免中阶段缓存崩溃，显著提高吞吐量。
conclusion: 从请求级被动管理转向智能体级主动控制是保障智能体批量推理效率的关键。
---

## Abstract
Batch inference for agentic workloads stresses the GPU key–value (KV) cache in a sustained and cumulative manner, often causing severe throughput degradation well before memory capacity is exhausted. We identify this phenomenon as middle-phase thrashing, a previously under-characterized pathology in which cache efficiency collapses as long-lived agents accumulate state over time.

We argue that mitigating this pathology requires moving beyond reactive, request-level cache management to proactive, agent-level admission control. Drawing inspiration from congestion control in distributed systems, we view the KV cache as a shared resource whose efficient utilization depends on feedback-driven regulation. Based on this insight, we present CONCUR, a lightweight control layer that regulates agent admission to bound aggregate cache pressure while preserving execution continuity. CONCUR adapts a cache-aware control algorithm to dynamically adjust the number of active agents using runtime cache signals.

Across large models and real-world agent workloads, CONCUR prevents middle-phase thrashing and improves batch inference throughput by up to 4.09× on Qwen3-32B and 1.90× on DeepSeek-V3, while remaining compatible with existing LLM serving systems.

---

## 论文详细总结（自动生成）

# CONCUR：基于拥塞控制的 LLM 智能体批量推理高吞吐并发管理

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **背景**：随着大语言模型（LLM）从单轮问答走向复杂智能体（agent）工作流，批量推理系统需要同时服务多个长时间运行的智能体任务。每个智能体会持续产生和累积 GPU 上的键值（KV）缓存，导致缓存占用随时间不断增长。
- **核心问题**：作者观察到，在这种“持续积累型”负载下，GPU 的 KV 缓存往往在容量尚未耗尽之前就出现严重的吞吐量下降。他们将该现象定义为 **中阶段抖动（middle-phase thrashing）**——一种此前未被充分刻画的病态行为：随着长生命周期智能体不断积累状态，缓存效率突然崩溃，系统吞吐量大幅下滑。
- **重要性**：这一问题不能靠简单的请求级缓存淘汰或显存扩容解决，因为智能体状态的长期性和累积性决定了缓存必须被保留。因此，需要从调度和并发的更高层面进行干预，才能保障批处理推理的整体效率。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将 KV 缓存视为一种 **共享资源**，借鉴分布式系统中的 **拥塞控制（congestion control）** 思想，通过反馈驱动的调节机制来避免缓存过载导致的性能崩塌。作者主张从“被动的请求级缓存管理”转向“主动的智能体级准入控制（admission control）”。
- **关键技术设计**：
  - **智能体级准入控制**：不再单独管理单个请求的缓存，而是控制当前活跃的智能体（agent）数量，从而限制聚合缓存压力。
  - **缓存感知的控制算法**：CONCUR 实现了一个轻量级控制层，利用运行时缓存信号（如缓存占用率、增长速率等）动态调整允许并发运行的智能体数量。
  - **保持执行连续性**：在调节准入时，尽量不中断已经运行的智能体，避免任务失效，保证工作流的完整性。
  - **兼容性**：CONCUR 被设计为独立于具体 LLM 推理引擎的轻量模块，可以嵌入现有 serving 系统而无需大规模改动。
- **算法流程（文字描述）**：
  1. 监控每个时间窗口内的 KV 缓存使用情况和变化趋势。
  2. 根据缓存拥塞程度计算一个“安全”的活跃智能体数量上限。
  3. 对新到达的智能体任务进行准入判断：若当前活跃数低于上限则允许进入，否则排队等待。
  4. 周期性更新控制参数，以响应缓存状态的变化（类似于 TCP 拥塞窗口的反馈调节，但针对智能体数量而非数据包速率）。

## 3. 实验设计

- **使用的模型**：Qwen3-32B 和 DeepSeek-V3，覆盖中等规模与超大规模 LLM。
- **工作负载**：使用了真实世界的智能体工作负载（real-world agent workloads），具体任务类型（如多步工具调用、对话编排等）在提供的材料中未详细说明。
- **Benchmark 与对比方法**：提供的材料中并未明确列出对比基线。通常此类研究会与传统的请求级缓存管理、固定并发限制、无准入控制等方案对比，但本次给定文本中未提及具体基线名称。
- **评价指标**：主要指标为批处理吞吐量（batch inference throughput）以及是否避免中阶段抖动。

## 4. 资源与算力

- 提供的文本中 **没有明确说明** 使用的 GPU 型号、数量、训练/推理时长等具体算力资源信息。
- 仅从模型规模（Qwen3-32B、DeepSeek-V3）推测需要较大显存的多卡推理环境，但无法获知确切硬件配置。这一信息缺失可能影响对结果可复现性的完整评估。

## 5. 实验数量与充分性

- 从摘要看，实验至少覆盖了 **两个不同规模的大模型** 和 **多种真实智能体工作负载**，并且报告了相对于现有系统的吞吐量提升倍数（最高 4.09× 和 1.90×）。
- 但提供的材料中 **没有给出具体的实验组数**，例如：
  - 是否做了不同负载强度下的压力测试？
  - 是否有针对不同并发上限、不同缓存容量配置的敏感性分析？
  - 是否有消融实验（如去掉反馈控制、或使用固定准入阈值）？
- 因此，仅凭现有信息无法判断实验的全面性和统计显著性。摘要中的“up to”表明是最好情况下的提升，未给出平均表现、方差、或其他负载下的结果，客观性证据不足。

## 6. 论文的主要结论与发现

- 中阶段抖动是智能体批量推理中真实存在且严重的性能瓶颈，其根因是长生命周期智能体对 KV 缓存的持续累积占用。
- 将 KV 缓存视为共享资源、采用拥塞控制式的智能体级准入控制，可以有效防止缓存崩溃。
- CONCUR 方法在 Qwen3-32B 上最高带来 **4.09×** 的批处理吞吐量提升，在 DeepSeek-V3 上最高带来 **1.90×** 提升，且与现有 LLM serving 系统兼容。

## 7. 优点

- **问题定义新颖**：首次明确提出“中阶段抖动”这一现象，为智能体推理性能优化提供了新视角。
- **思想迁移巧妙**：将成熟的网络拥塞控制理论迁移到 LLM 缓存管理领域，类比自然且具有理论支撑。
- **干预粒度恰当**：从请求级被动管理提升到智能体级主动控制，更贴合智能体工作负载的语义。
- **轻量且兼容**：控制层实现简单，无需改动底层推理引擎，便于实际部署。
- **效果显著**：在 32B 和超大模型上均取得数倍的吞吐量提升，实际价值明显。

## 8. 不足与局限

- **细节缺失**：提供的文本只有摘要和元数据，缺乏方法公式、算法伪代码、超参数设置、系统实现细节等关键内容，难以完全复现验证。
- **实验覆盖不明**：未明确对比基线，未报告不同负载组合、不同缓存容量、不同智能体数量下的详细结果，也没有给出吞吐量提升的置信区间或多次运行的标准差。
- **资源信息缺乏**：未披露 GPU 型号、数量、显存大小等算力配置，影响对结果公平性的判断。
- **应用范围限制**：目前只验证了 LLM 推理场景中的 KV 缓存控制，对于其他共享资源（如带宽、CPU）是否同样适用未做讨论；且对智能体任务本身的语义（如任务优先级、时间约束）未涉及，可能只适用于非实时批量场景。
- **潜在偏差风险**：摘要中的“up to”可能是特定负载下最优结果，若负载特性变化，收益可能大幅下降，存在选择性报告风险。

---

（完）
