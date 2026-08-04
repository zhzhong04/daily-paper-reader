---
title: "ConServe: Fine-Grained GPU Harvesting for LLM Online and Offline Co-Serving"
title_zh: ConServe：面向LLM在线与离线共服务的细粒度GPU资源收割
authors: "Yifan Qiao, Shan Yu, Shu Anzai, Haoran Ma, Shuo Yang, Yang Wang, Miryung Kim, Yongji Wu, Yang Zhou, Jiarong Xing, Joseph E. Gonzalez, Ion Stoica, Harry Xu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/b5f8321111d4dd01e405cd6d653f58cd0ba546b3.pdf"
tags: ["query:awc"]
score: 4.0
evidence: 面向LLM服务的KV缓存管理与token级调度，可迁移至智能体工作流缓存
tldr: LLM服务面临高峰负载波动导致的GPU利用率低下问题。ConServe提出一种协同服务系统，通过延迟感知的token级调度、子迭代层间抢占和增量KV缓存管理，让离线任务填充毫秒级GPU空闲时间，同时保障在线请求延迟。该系统不直接面向智能体工作流，但其细粒度缓存与调度机制可为智能体缓存调度提供方法借鉴。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: LLM服务负载波动导致GPU利用率不足，现有系统资源管理粒度粗、干扰大。
method: 提出ConServe协同服务系统，采用延迟感知的token级调度、子迭代层间抢占和增量KV缓存管理。
result: 实验表明ConServe能利用毫秒级空闲时间执行离线任务，同时保持在线延迟目标。
conclusion: 细粒度资源调度与KV缓存管理相结合，可显著提升LLM服务效率，对智能体工作流缓存有借鉴意义。
---

## Abstract
Large language model (LLM) serving demands low latency and high throughput, but high load variability leads to significant GPU under-utilization. In this paper, we identify a synergistic but overlooked opportunity to co-serve latency-critical online requests alongside *latency-tolerant offline* tasks, which existing systems fail to exploit because their coarse-grained resource management introduces interference.
We present ConServe, a co-serving system that enables fine-grained resource sharing through latency-aware token-level scheduling, sub-iteration layer-wise preemption, and incremental KV-cache management. These mechanisms allow offline execution to fill *millisecond-scale* GPU idle time while preserving strict online latency guarantees. Across real-world workloads with Llama-3.1 and Qwen-2.5 models, ConServe improves throughput by 2.2$\times$ on average and reduces online tail latency by 2.9$\times$ over state-of-the-art systems.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- 大语言模型（LLM）在线服务要求低延迟和高吞吐，但实际负载波动剧烈，导致 GPU 利用率普遍偏低。
- 现有系统采用粗粒度的资源管理方式，难以在不干扰在线请求的前提下利用空闲 GPU 资源。
- 论文发现一个被忽视的机会：将延迟敏感的在线请求与延迟容忍的离线任务进行协同服务（co-serving），从而填补 GPU 的闲置时间。
- 整体含义：通过细粒度资源调度与缓存管理，可显著提升 LLM 服务基础设施的效率，为混合负载场景提供了新的设计思路。

## 2. 方法论

- 核心思想：让离线任务的执行“嵌入”在线服务产生的毫秒级 GPU 空闲间隙，同时严格保证在线请求的延迟目标。
- 关键技术：
  - **延迟感知的 token 级调度（latency-aware token-level scheduling）**：以 token 为最小调度单位，实时感知在线请求的延迟预算，动态决定何时插入离线计算。
  - **子迭代层间抢占（sub-iteration layer-wise preemption）**：在解码迭代内部按层粒度进行抢占，使离线任务可被快速暂停，避免阻塞在线请求。
  - **增量 KV 缓存管理（incremental KV-cache management）**：复用和维护 KV 缓存增量，降低切换成本，使在线与离线任务之间的上下文切换更加高效。
- 这些机制协同工作，使离线任务能够利用原本浪费的毫秒级时间片，同时维持在线延迟的服务质量。

## 3. 实验设计

- 使用真实世界负载（real-world workloads），模型为 Llama-3.1 和 Qwen-2.5。
- 对比对象为现有最先进的系统（state-of-the-art systems），具体名称未在摘要中给出。
- 评测指标包括吞吐量（throughput）和在线尾延迟（tail latency）。
- 需要说明：论文摘要未提供具体数据集名称、请求分布、任务类型等详细 benchmark 信息。

## 4. 资源与算力

- 论文摘要中未明确说明使用的 GPU 型号、数量、训练/推理时长或集群规模。
- 仅能确定实验基于 Llama-3.1 和 Qwen-2.5 模型，但无法获知具体硬件配置。
- 若需完整信息，需查阅论文全文的实验设置部分。

## 5. 实验数量与充分性

- 从摘要看，实验覆盖了两个主流模型（Llama-3.1、Qwen-2.5）和真实负载场景，对比了现有最优系统，验证了吞吐与延迟两个关键指标。
- 摘要未提及消融实验、不同负载强度、不同延迟目标等变化性实验，也未报告标准差或多次运行结果。
- 就现有信息而言，实验结论具有初步有效性，但充分性有限——缺少对各个机制独立贡献的验证，公平性也难以完全评估。

## 6. 主要结论与发现

- 相比最先进系统，ConServe 将吞吐量平均提升 **2.2×**。
- 在线尾延迟平均降低 **2.9×**。
- 证明了细粒度资源共享能够在保证在线服务质量的同时，有效利用 GPU 空闲时间执行离线任务。

## 7. 优点

- 问题切入点务实：针对实际系统中普遍存在的 GPU 利用率低下的痛点。
- 机制设计精细：token 级调度、子迭代抢占和增量缓存管理在技术层面具有创新性，相比粗粒度方案能更精确地控制资源。
- 结果显著：在吞吐和延迟两个核心指标上都有大幅提升，且使用了主流真实世界模型，具有现实参考价值。

## 8. 不足与局限

- 信息不全：当前仅提供摘要，缺乏实验环境、工作负载细节、对比系统具体配置等关键信息，难以判断实验的完整性与公平性。
- 未报告消融实验：无法确认每个技术组件的独立贡献，方法有效性的因果论证不够充分。
- 未讨论扩展性：没有提及在更大规模集群、多租户、异构 GPU 等场景下的表现。
- 未覆盖更多模型与任务类型：仅使用两个模型的真实负载，泛化性仍需验证。
- 实际部署复杂性：子迭代抢占与 token 级调度可能引入额外的系统开销和工程复杂度，论文摘要未涉及更详细的成本分析。

（完）
