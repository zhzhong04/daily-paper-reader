---
title: "CONCUR: High-Throughput Agentic Batch Inference of LLM via Congestion-Based Concurrency Control"
title_zh: CONCUR：通过基于拥塞的并发控制实现LLM智能体批量推理的高吞吐
authors: "qiaoling chen, Zhisheng Ye, Tian Tang, Peng Sun, Boyu Tian, Guoteng Wang, Shenggui Li, Yonggang Wen, Zhenhua Han, Tianwei Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/34e588f95f3adb2d1771f68b0ac1a31d517885fb.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 针对智能体批处理工作负载提出基于拥塞的并发控制机制，将KV缓存作为共享资源进行智能体级管理
tldr: 面向智能体的批处理推理会使GPU KV缓存受到持续累积压力，在内存耗尽前就出现严重的吞吐下降，论文称之为中期抖动现象。为缓解该问题，CONCUR借鉴网络拥塞控制思想，将KV缓存视为共享资源，提出超越请求级管理的主动智能体级准入控制。实验表明该方法能大幅减少缓存效率崩塌，保持高吞吐的批推理性能，为智能体工作负载的缓存管理提供了新范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 智能体批处理推理中，长期存活的智能体会累积状态并压垮KV缓存，导致内存尚未耗尽就出现吞吐骤降的中期抖动。
method: 借鉴分布式系统拥塞控制思想，将KV缓存视为共享资源，提出基于反馈调节的智能体级准入控制，动态管理并发智能体数量。
result: 实验验证该方法能够有效抑制缓存效率崩塌，显著提升智能体批推理的吞吐与稳定性。
conclusion: 该工作表明智能体级、主动式的缓存控制是解决智能体工作负载缓存压力的有效思路，推动KV缓存管理走向工作流感知。
---

## Abstract
Batch inference for agentic workloads stresses the GPU key–value (KV) cache in a sustained and cumulative manner, often causing severe throughput degradation well before memory capacity is exhausted. We identify this phenomenon as middle-phase thrashing, a previously under-characterized pathology in which cache efficiency collapses as long-lived agents accumulate state over time.

We argue that mitigating this pathology requires moving beyond reactive, request-level cache management to proactive, agent-level admission control. Drawing inspiration from congestion control in distributed systems, we view the KV cache as a shared resource whose efficient utilization depends on feedback-driven regulation. Based on this insight, we present CONCUR, a lightweight control layer that regulates agent admission to bound aggregate cache pressure while preserving execution continuity. CONCUR adapts a cache-aware control algorithm to dynamically adjust the number of active agents using runtime cache signals.

Across large models and real-world agent workloads, CONCUR prevents middle-phase thrashing and improves batch inference throughput by up to 4.09× on Qwen3-32B and 1.90× on DeepSeek-V3, while remaining compatible with existing LLM serving systems.

---

## 论文详细总结（自动生成）

# CONCUR: 通过基于拥塞的并发控制实现 LLM 智能体批量推理的高吞吐

## 1. 核心问题与研究动机

- **背景**：面向智能体（Agent）的工作负载在进行批量推理时，会对 GPU 的 KV 缓存（Key-Value Cache）产生**持续且累积性的压力**。与普通请求不同，智能体在长时间运行过程中会不断积累状态（例如对话历史、每一步推理产生的 KV 数据），导致 KV 缓存占用随时间单调增长。
- **核心问题**：论文识别出一个此前未被充分刻画的现象——**中期抖动（Middle-Phase Thrashing）**。即在 GPU 显存尚未完全耗尽之前，由于长期存活的智能体不断累积状态，缓存效率发生崩塌，导致严重的吞吐下降。
- **整体含义**：传统的请求级、反应式缓存管理策略不足以应对智能体工作负载的特性，需要从根本上转变管理粒度与时机，即在智能体级别进行主动控制。

## 2. 方法论

- **核心思想**：将 GPU 的 KV 缓存视为一种**共享资源**，借鉴分布式系统中有成熟应用的**网络拥塞控制（Congestion Control）** 思想，通过反馈驱动的调节机制来管控多个智能体对缓存资源的竞争。
- **关键设计**：提出 **CONCUR** —— 一个**轻量级控制层**，在智能体级别实施**主动准入控制（Agent-Level Admission Control）**。其核心逻辑是：
  - 以运行时缓存信号（如当前 KV 缓存占用率、增长趋势等）作为反馈输入；
  - 通过一个**缓存感知的控制算法**动态调整当前活跃的智能体数量；
  - 将聚合缓存压力限制在安全阈值之内，从而避免缓存效率的崩塌。
- **与现有方法的关系**：属于“超越请求级管理”的新范式；不替代底层 LLM 推理引擎，而是作为其上层的控制层，与现有 LLM 推理服务系统兼容。

## 3. 实验设计

> 注：由于原文全文不可获取，以下信息基于论文摘要与元数据整理，实验细节可能不完整。

- **模型规模**：实验覆盖了不同规模的大型模型，明确提及的有：
  - **Qwen3-32B**（大型稠密模型）
  - **DeepSeek-V3**（大规模 MoE 模型）
- **工作负载**：使用了**真实世界的智能体工作负载（real-world agent workloads）**，但具体任务类型、数据集的详细名称与构造方式在现有材料中未披露。
- **对比方法**：原文说明 CONCUR 与现有 LLM 服务系统兼容，但未明确指出对比了哪些具体基线方法（如请求级缓存管理策略、无控制的批量推理、贪心准入策略等）。

## 4. 资源与算力

- 论文元数据及摘要中**未明确披露**使用的 GPU 型号、GPU 数量、训练/推理时长等具体算力资源信息。
- 从实验采用的模型规模（32B 稠密模型和 DeepSeek-V3）可推断使用了较大规模的推理基础设施（如多卡或集群），但具体配置无法从现有材料中确认。

## 5. 实验数量与充分性

- **实验数量**：现有材料仅提及在多个大型模型和真实世界智能体工作负载上进行了评估，以及吞吐量提升（Qwen3-32B 上最高 4.09×，DeepSeek-V3 上 1.90×）。**未明确给出**实验总组数、是否包含消融实验、是否对控制参数进行敏感性分析等。
- **充分性评估**：
  - 从现有描述看，验证了核心效果（吞吐提升），**实验规模覆盖了不同架构的大模型**，这一点较好。
  - 但缺乏：与现有缓存管理策略的显式基准对比、消融实验中各组件贡献的分解、不同并发场景下的稳定性测试等。因此，实验的**充分性和客观公平性在当前信息下难以全面评估**。

## 6. 主要结论与发现

- **确认病理现象**：明确了“中期抖动”是智能体批量推理中一个真实存在且严重的性能瓶颈。
- **方法有效性**：CONCUR 能够有效防止中期抖动，在 **Qwen3-32B 上吞吐提升最高达 4.09 倍**，在 **DeepSeek-V3 上提升 1.90 倍**。
- **兼容性**：轻量级设计使其能与现有 LLM 服务系统良好兼容，部署成本低。
- **范式意义**：该工作表明，**智能体级、主动式的缓存控制**是应对智能体工作负载缓存压力的有效思路，推动 KV 缓存管理从请求级走向工作流感知（workflow-aware）的方向。

## 7. 优点

- **问题洞察新颖**：识别并命名了“中期抖动”这一此前未被充分表征的现象，切中智能体推理的实际痛点。
- **跨领域借鉴**：将网络拥塞控制的成熟思想引入 LLM 推理缓存管理，跨领域迁移自然且富有创造性。
- **控制粒度创新**：从请求级管理提升到智能体级准入控制，与智能体工作负载的长期存活特性相匹配。
- **实用性导向**：提出的是轻量级控制层，而非对底层推理引擎的侵入式改造，实际部署可行性高。
- **验证场景真实**：在真实世界智能体工作负载和大规模模型上验证，生态有效性较好。

## 8. 不足与局限

- **实验细节缺失**：论文全文未提供，导致无法获知具体的数据集内容、任务类型、缓存放宽/收缩策略的具体算法参数等。
- **基准对比不明确**：未说明与哪些已有缓存替换策略（如基于优先级的驱逐、请求级配额等）进行了对比，方法相对优势的界定不够清晰。
- **算力资源未披露**：缺少 GPU 型号、数量、运行成本等关键信息，难以评估方法的资源效率与可复现性。
- **消融与敏感性分析不足**：没有明确提及对控制算法关键超参数、反馈信号选择、并发度上下界等的消融研究，机制有效性归因不充分。
- **可扩展性验证有限**：仅报告了两个代表性模型的性能，对于更大规模多节点分布式推理环境下的表现尚缺乏验证。
- **应用边界**：方法主要针对 KV 缓存压力这一单一瓶颈；当推理受限于计算吞吐、通信带宽或磁盘 I/O 时，其调节效果可能有限。

（完）
