---
title: "Beyond Prediction: Tail-Aware Scheduling for LLM Inference"
title_zh: 超越预测：面向LLM推理的尾延迟感知调度
authors: "Yueying Li, Yuanfan Chen, Jiayang Chen, Esha Choukse, Haoran Qiu, G. Edward Suh, Rodrigo Fonseca, Ziv Scully, Udit Gupta"
date: 2026-04-30
pdf: "https://openreview.net/pdf/14985be222c6392883fbb3d19d980cc9c4e34a84.pdf"
tags: ["query:agent-cache"]
score: 5.0
evidence: LLM调度中的缓存感知抢占，与缓存管理相关但非智能体特定
tldr: LLM服务中长度变化大，现有基于预测的调度器对分布漂移和突发流量脆弱，且难以控制尾延迟。本文提出无预测的调度框架，用轻量统计信号进行γ参数化的软优先级提升，并与缓存感知的抢占协同优化。该设计在GPU内存压力下仍能改善P99延迟，对缓存感知调度有参考价值，但未面向智能体工作流。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有预测驱动的调度器在分布偏移和突发流量下表现脆弱，无法有效控制尾延迟。
method: 使用轻量统计信号进行软优先级提升，并与缓存感知的抢占策略联合优化。
result: 在多种负载下改善P90-P99尾延迟，且无需长度预测。
conclusion: 无预测的分布感知调度可增强LLM服务的鲁棒性和尾延迟控制。
---

## Abstract
LLM serving exhibits extreme length variability, making size-based scheduling difficult in practice. Recent LLM schedulers approximate SJF/SRPT using predicted decode lengths or rank and primarily report mean-centric metrics (e.g., TTFT/TBT). We show these prediction-driven policies can be fragile under distribution shifts, bursty arrivals, and GPU memory pressure, and still offer limited control over tail latency (P90–P99) that dominates user experience—even with perfect decode-length knowledge. We introduce a distribution-aware, prediction-free scheduling framework that replaces explicit length prediction with soft, $\gamma$-parameterized priority boosting driven by lightweight statistical signals. Our design co-optimizes scheduling with cache-aware preemption to account for memory-coupled decode dynamics that vary across workload mixes. Evaluated on Azure production traces, our method achieves a P99 TTLT up to 35--50\% lower than SRPT with perfect length prediction and a TTFT 34--47\% lower across various workloads, including reasoning-heavy and chat-heavy tasks, demonstrating a robust alternative for tail-latency optimization in online LLM serving.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义

- **研究背景**：LLM 在线推理服务存在极端的长短请求差异（如普通聊天与深度推理任务的解码长度相差巨大），传统基于任务大小的调度策略（如 SJF/SRPT）在实际系统中难以直接应用。
- **现有方法的局限**：近期 LLM 调度器普遍采用“预测解码长度”的方式近似 SJF/SRPT，或仅使用排序机制，且评测指标以均值（TTFT/TBT）为主。然而论文指出，这类预测驱动策略在**分布漂移**、**突发流量**和**GPU 内存压力**下非常脆弱，即使在拥有完美长度预测的理想情况下，对 P90–P99 尾延迟的控制能力依然有限——而尾延迟恰恰是决定用户体验的关键指标。
- **核心问题**：能否设计一种**不依赖显式长度预测**的调度框架，从根本上提升 LLM 推理服务在真实生产负载下的尾延迟鲁棒性？

## 2. 论文提出的方法论

- **核心思想**：提出**分布感知、无预测**（distribution-aware, prediction-free）的调度框架，放弃显式预测解码长度，转而使用**轻量统计信号**驱动调度决策。
- **关键技术细节**：
  - **γ 参数化的软优先级提升（Soft Priority Boosting）**：不再对请求做硬性的大小分类或排序，而是根据统计信号以“软”方式为请求提升优先级，γ 参数控制提升强度，从而避免预测误差带来的极端调度错误。
  - **缓存感知的抢占协同优化（Cache-Aware Preemption）**：调度与 LLM 推理中的 KV cache 管理深度耦合，论文将调度策略与缓存感知的抢占机制联合设计，以适配不同负载混合下内存与计算的动态变化。
- **算法流程（文字说明）**：系统在线收集请求的轻量统计特征（非长度预测），针对当前负载分布动态调整 γ 优先级提升策略，并与缓存感知的抢占决策协同，在 GPU 内存受限的情况下决定哪些请求应优先执行/抢占/恢复。整个过程无需提前获知请求的解码长度。

## 3. 实验设计

- **数据集与场景**：使用 **Azure 生产环境轨迹（Azure production traces）**，覆盖多种真实负载，包括 **推理密集型（reasoning-heavy）** 和 **聊天密集型（chat-heavy）** 任务。
- **Benchmark/基线**：
  - 主要对比基线为 **SRPT（最短剩余处理时间）**，并假设其拥有**完美的解码长度预测**（即理想化上界）。
  - 同时对比现有预测驱动调度器。
- **评测指标**：P99 TTLT（time-to-last-token，尾延迟）、TTFT（time-to-first-token）等。

## 4. 资源与算力

- 论文摘要与元数据中**未明确说明**使用了何种 GPU 型号、数量、集群规模或训练/推理时长。
- 作为一项系统/调度层面的研究，其实验可能在较小规模或仿真环境中完成，但具体硬件配置在本次提供的材料中缺失，无法进一步确认。

## 5. 实验数量与充分性

- 从现有材料看，实验主要包括：
  - 在 Azure 生产轨迹上的端到端评估（多种负载混合）；
  - 覆盖推理密集型和聊天密集型任务；
  - 与完美预测 SRPT 的对照实验，验证无预测方法的优越性。
- **充分性评估**：
  - **优势**：选择“完美预测 SRPT”作为基线具有很强的说服力——即使预测完美，现有方法仍受限于尾延迟，而无预测方法能做得更好，凸显了方法本身的优势。
  - **不足**：提供的信息有限，未展示消融实验（如 γ 参数敏感性、不同统计信号选择、抢占策略单独效果等），也未明确测试极端突发流量的边界条件。由于材料仅为摘要层面，实验数据的完整性无法充分判断。

## 6. 论文的主要结论与发现

- 相比拥有完美长度预测的 SRPT，本方法在 **P99 TTLT 上降低 35–50%**，在 **TTFT 上降低 34–47%**。
- 结果在多种负载（推理密集、聊天密集）下均保持一致，说明**无预测、分布感知的调度**是更鲁棒的尾延迟优化方案。
- 结论：在在线 LLM 服务中，放弃显式长度预测、转而结合轻量统计信号和缓存感知抢占，可以同时提升系统的鲁棒性和尾延迟控制能力。

## 7. 优点

- **方法创新性**：跳出预测驱动调度的主流范式，用轻量统计信号替代长度预测，规避了预测误差和分布漂移的脆弱性。
- **协同设计**：将调度与 KV cache 感知的抢占联合优化，贴近实际 LLM 推理引擎的内存耦合特性，工程落地性强。
- **评测严格**：以“完美预测的 SRPT”为对比基线，是一种强基线设置，结论更有说服力。
- **生产环境验证**：基于 Azure 生产轨迹，覆盖多种负载类型，外部效度较高。
- **指标聚焦**：明确以 P99 尾延迟为核心优化目标，契合真实用户体验。

## 8. 不足与局限

- **算力细节缺失**：未报告 GPU 型号、数量、部署规模等资源信息，难以评估方法的实际开销和可扩展性。
- **实验信息有限**：当前材料仅提供摘要级信息，缺乏消融研究、参数敏感性分析、不同负载压力下的细粒度实验结果。
- **偏向系统层面**：论文更多关注调度策略，未深入探讨与模型层（如投机解码、分块预填充）的协同可能性。
- **非智能体特定**：该调度器面向通用在线 LLM 服务，并未针对智能体工作流（如多轮工具调用、长链推理）做专门优化，因此对智能体场景的适用性需进一步验证。
- **γ 参数调优**：软优先级提升中的 γ 参数如何在动态负载中自适应调节，文中未充分说明，可能存在部署调参成本。

（完）
