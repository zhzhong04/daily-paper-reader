---
title: "HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization"
title_zh: HeraSys：通过细粒度端到端优化协作服务多LLM工作流
authors: "Size Li, Zhiqing Tang, Hongrui Liang, Jianxiong Guo, Jiong Lou, Tian Wang, Weijia Jia"
date: 2026-04-30
pdf: "https://openreview.net/pdf/2ef6fab2710d7c2ab7cb014d0518496d3444e525.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 多工作流协作服务，跨工作流重用与联合调度
tldr: 现有LLM服务系统主要优化单个工作流的执行，忽略了多个并发智能体工作流之间的计算冗余问题。HeraSys通过细粒度编排，利用结构节点合并与重用来消除跨工作流冗余，并提出负载感知的联合调度策略动态管理执行顺序，从而优化端到端性能。实验表明HeraSys能显著降低延迟并提升并发工作流的吞吐量，为智能体工作流的高效协同服务提供了新思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有系统忽略多租户智能体工作流之间的计算冗余，仅优化单个工作流，导致整体效率低。
method: HeraSys通过细粒度编排实现结构节点合并与复用，并引入负载感知的联合调度策略。
result: 实验显示HeraSys在并发工作流场景下能有效消除冗余，提升端到端性能与吞吐量。
conclusion: HeraSys证明了跨工作流优化对LLM智能体工作流协同服务的重要性，可作为缓存调度的基础设施。
---

## Abstract
The proliferation of Large Language Models (LLMs) has shifted serving systems from processing isolated requests to orchestrating high-concurrency, multi-tenant agentic workflows. However, existing solutions typically prioritize intra-workflow optimization, largely neglecting the significant potential for inter-workflow optimization. In this paper, we propose HeraSys, an LLM serving system designed to optimize the end-to-end performance of concurrent workflows. Through fine-grained orchestration, HeraSys eliminates cross-workflow computational redundancy via structural node merging and reuse. Furthermore, HeraSys introduces a load-aware joint scheduling policy that dynamically manages execution order by evaluating both inter- and intra-query priorities. By integrating a resource skewing mechanism with adaptive batching and pipeline decomposition, HeraSys effectively mitigates tail latency while maintaining low average latency, thereby substantially improving system throughput. Extensive experiments demonstrate that HeraSys reduces P99 latency by up to 2.17$\times$ and increases serving throughput by up to 1.85$\times$ under strict latency guarantees.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义

- **研究背景**：随着大语言模型（LLM）的普及，服务系统正从处理孤立请求转向编排高并发、多租户的智能体工作流（agentic workflows）。
- **核心问题**：现有LLM服务系统主要关注**单个工作流内部**的优化（如工作流内的缓存、调度、推理加速），却严重忽略了**多个并发工作流之间**存在的计算冗余和资源共享潜力，导致端到端性能不佳。
- **整体含义**：HeraSys旨在解决多工作流并发场景下的效率瓶颈，将优化视角从“单工作流局部最优”扩展到“跨工作流全局协同”，为LLM智能体服务提供了新的系统级思路。

## 2. 方法论

- **核心思想**：通过**细粒度编排**（fine-grained orchestration）实现跨工作流优化，消除计算冗余，并引入**负载感知的联合调度**策略，动态管理工作流的执行顺序。
- **关键技术**：
  - **结构节点合并与重用**：将并发工作流中的相同或相似的结构节点进行合并和复用，从而避免重复计算。
  - **联合调度策略**：同时评估“查询间优先级”和“查询内优先级”，实现端到端感知的执行顺序管理。
  - **资源偏斜机制**（resource skewing）：结合自适应批处理（adaptive batching）和流水线分解（pipeline decomposition），用于缓解尾部延迟。
- **目标**：在保持低平均延迟的同时，显著降低尾延迟，提升系统吞吐量。

## 3. 实验设计

- 论文摘要中**未明确提及**具体使用的数据集、场景名称或基准（benchmark）。
- 从元数据可知，实验聚焦于“并发工作流”场景，并对比了同类LLM服务系统。
- 公开结果仅给出相对性能提升：P99 延迟最高降低 **2.17 倍**，在严格延迟保障下吞吐量最高提升 **1.85 倍**。
- 由于正文细节缺失，无法确认具体对比方法（如 vLLM、Inferflow 等）及实验配置。

## 4. 资源与算力

- 论文中**未明确说明**使用的 GPU 型号、数量、训练/实验时长等算力信息。
- 仅能从系统设计推断其面向真实多租户 LLM 服务场景，但具体硬件部署细节在当前提供的文本中缺失。

## 5. 实验数量与充分性

- 从现有文本看，实验仅给出了延迟和吞吐两个核心指标的汇总结果，**没有展示多组独立实验、消融实验或不同负载配置的细节**。
- 因此，**无法判断实验的充分性和公平性**。摘要中提及“Extensive experiments”，但未提供误差棒、显著性检验、基线配置等客观证据。
- 若仅凭当前信息，实验证据尚不充分，需要阅读全文确认。

## 6. 主要结论与发现

- HeraSys 通过跨工作流节点合并与重用，有效消除了并发工作流之间的冗余计算。
- 负载感知联合调度策略能够动态平衡不同工作流的需求，减少排队和阻塞。
- 资源偏斜机制与自适应批处理、流水线分解相结合，能显著缓解尾延迟。
- 总体而言，HeraSys 在并发多工作流场景下可大幅降低 P99 延迟并提高吞吐量，证明了“跨工作流优化”是提升 LLM 服务系统效率的关键方向。

## 7. 优点

- **问题新颖**：突破了传统只优化单工作流的局限，聚焦多租户智能体工作流的协作优化。
- **系统设计完整**：从计算冗余消除、调度策略到资源偏斜机制，形成较完整的端到端优化方案。
- **指标针对性强**：同时关注平均延迟、尾延迟和吞吐量，贴近真实服务场景的延迟敏感性需求。
- **实用定位明确**：可作为缓存/调度基础设施，支持多智能体工作流的协同服务。

## 8. 不足与局限

- **实验细节缺失**：当前摘要未给出数据集、baseline、硬件配置等关键信息，难以评估方法的普适性和竞争力。
- **公平性存疑**：未提及对比系统的优化配置、是否同等调优，存在潜在的比较偏差风险。
- **适用边界未说明**：未讨论跨工作流重用对动态性极强或异构性极高的工作流是否仍然有效。
- **工程复杂度**：细粒度编排和资源偏斜机制可能引入额外调度开销，文中未给出开销分析。
- **应用限制**：对于无共享结构的工作流组合，收益可能有限，但文中没有分析此类退化场景。

（完）
