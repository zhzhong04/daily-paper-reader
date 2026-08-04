---
title: "LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents"
title_zh: LRAgent：面向多LoRA LLM智能体的高效KV缓存共享
authors: "Hyesung Jeon, Hyeongju Ha, Jae-Joon Kim"
date: 2026-04-30
pdf: "https://openreview.net/pdf/aad6d5a22a6ab8a9ad7c83d6bff25e05e9d49a41.pdf"
tags: ["query:cache-reuse"]
score: 9.0
evidence: LRAgent将缓存分解为共享基座与适配器组件，在多LoRA智能体间共享KV缓存
tldr: 多LoRA智能体系统虽共享预训练基座，却为相同轨迹各自维护独立KV缓存，造成显著冗余；LRAgent观察到跨智能体缓存差异主要由适配器输出引起，因此将缓存分解为共享基座组件与适配器组件并分别处理。实验显示该方法大幅降低KV缓存内存与计算开销，为多智能体语境下的KV缓存复用提供了直接有效的机制。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 多LoRA智能体共享基座但各自保存相同的长轨迹KV缓存，造成大量内存和计算冗余。
method: 将缓存分解为共享的预训练基座组件与适配器组件，分别管理以实现KV缓存共享。
result: 实验表明LRAgent显著降低多智能体场景下的KV缓存内存占用与计算开销。
conclusion: 利用共享基座激活的相似性进行缓存分解是跨智能体缓存复用的有效方向。
---

## Abstract
Role specialization in multi-LLM agent systems is often realized via multi-LoRA, where agents share a pretrained backbone and differ only through lightweight adapters.
Despite sharing base model weights, each agent independently builds and stores its own KV cache for the same long, tool-augmented trajectories, incurring substantial memory and compute overhead.
Existing KV cache sharing methods largely overlook this multi-LoRA setting.
We observe that, across agents, cache differences are dominated by adapter outputs, while activations from the shared pretrained backbone remain highly similar.
Based on this observation, we propose LRAgent, a KV cache sharing framework for multi-LoRA agents that decomposes the cache into a shared base component from the pretrained weights and an adapter-dependent component from LoRA weights.
LRAgent reduces memory overhead by sharing the base component and storing the adapter component in its inherent low-rank form, and further reduces compute overhead, enabled by shared-$A$ multi-LoRA architectures, by also sharing the low-rank cache and avoiding redundant computations for contexts already processed by other agents.
To efficiently reconstruct adapter contributions at runtime, we introduce Flash-LoRA-Attention, a kernel that reorders attention computation to avoid materializing the low-rank cache to full dimension.
LRAgent achieves throughput and time-to-first-token latency close to fully shared caching, while preserving accuracy near the non-shared caching baseline across agentic question-answering benchmarks.

---

## 论文详细总结（自动生成）

# LRAgent：面向多LoRA LLM智能体的高效KV缓存共享

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：多LLM智能体系统通常采用 multi-LoRA 架构实现角色专门化（role specialization），即所有智能体共享同一个预训练基座模型（pretrained backbone），仅通过轻量级 LoRA 适配器区分各自的功能与角色。
- **问题**：尽管各智能体共享基座权重，但在处理相同的、长序列、工具增强（tool-augmented）的轨迹（trajectories）时，每个智能体仍然独立构建并存储各自的 KV 缓存（KV cache），导致显著的内存（memory）和计算（compute）开销冗余。
- **研究缺口**：现有的 KV 缓存共享方法大多面向单模型多请求或跨请求的复用场景，并未针对多 LoRA 智能体这一设定进行专门设计与优化。
- **关键观察**：论文发现，跨智能体的缓存差异主要由 LoRA 适配器输出主导，而来自共享预训练基座的激活（activations）在不同智能体之间保持高度相似。这为缓存分解与共享提供了基础。

## 2. 提出的方法论

- **核心思想**：将 KV 缓存分解为两个组成部分：
  - **共享基座组件（shared base component）**：由预训练权重产生，可在多个智能体之间共享；
  - **适配器依赖组件（adapter-dependent component）**：由 LoRA 权重产生，因智能体而异。
- **内存开销削减机制**：
  - 共享基座组件，使其只存储一份；
  - 适配器组件利用其内在的低秩（low-rank）结构进行存储，避免全维度显式物化。
- **计算开销削减机制**：在 shared-A 多 LoRA 架构下，进一步共享低秩缓存，避免对其他智能体已经处理过的上下文进行冗余计算。
- **运行时重建优化（Flash-LoRA-Attention）**：
  - 提出了一种新的注意力内核（kernel），通过重新排列注意力计算顺序，避免在运行时将低秩缓存物化到完整维度。
  - 该内核能够在运行时高效重建适配器贡献（adapter contributions），从而在不牺牲性能的前提下实现共享。

## 3. 实验设计

- **场景/基准（Benchmark）**：使用的是 agentic question-answering（智能体问答）类基准任务。摘要中未列出具体数据集名称（如 HotpotQA、AgentBench 等），仅笼统提及 agentic question-answering benchmarks。
- **对比方法**：
  - **非共享缓存基线（non-shared caching baseline）**：即各智能体独立缓存的标准做法；
  - **完全共享缓存（fully shared caching）**：一种理想化的共享上限或近似方案；
  - 论文将 LRAgent 的结果同时与上述两者对比，考察其在精度、吞吐量和延迟上的折中表现。
- **评估指标**：吞吐量（throughput）、首 token 时间（time-to-first-token, TTFT）、以及任务精度（accuracy）。

## 4. 资源与算力

- **未明确说明**：所提供的论文摘要与元数据中，没有提及所使用的 GPU 型号、GPU 数量、训练或推理的具体时长，也未提及能耗等资源信息。若需更多算力细节，需查阅论文全文的实验章节。

## 5. 实验数量与充分性

- **从摘要可见的实验维度**：
  - 对比了 LRAgent 与非共享缓存基线、完全共享缓存的吞吐量与 TTFT 延迟；
  - 报告了在 agentic QA 基准上的精度表现。
- **充分性评估**：
  - 摘要层面的信息不足以全面评估实验充分性。未列出具体数据集数量、消融实验（如对 Flash-LoRA-Attention 的单独消融、对不同 LoRA 数量/秩的扩展性实验）、不同模型规模（7B/13B/70B）的覆盖，也未报告多智能体数量变化带来的扩展性分析。
  - 总体而言，核心结论（性能接近全共享、精度接近非共享）已被报告，但实验的完整性和公平性仍需全文验证。

## 6. 主要结论与发现

- 在智能体问答基准上，LRAgent 的**吞吐量和 TTFT 延迟接近完全共享缓存**的水平，同时**精度接近非共享缓存基线**。
- 这验证了“共享预训练基座激活的相似性”这一观察的有效性——即缓存分解为基座组件与适配器组件，是实现跨智能体缓存复用的可行且高效的方向。
- 表明多 LoRA 智能体场景中的 KV 缓存冗余可以通过结构化的分解与共享机制被大幅削减，而不显著损失模型质量。

## 7. 优点

- **观察驱动的方法设计**：论文基于对跨智能体缓存差异来源的实证观察（适配器主导差异、基座激活高度相似）来设计方法，具有较强的动机支撑。
- **内存与计算的双重优化**：不仅减少内存占用（共享基座组件 + 低秩存储适配器组件），还减少计算量（复用低秩缓存、避免冗余计算）。
- **系统级贡献（Flash-LoRA-Attention）**：提出专用的内核级优化，解决运行时重建低秩缓存的高效性问题，使方法在实际部署中具备可行性。
- **定位清晰**：填补了 KV 缓存共享研究在多 LoRA 智能体场景下的空白，具有明确的应用价值。

## 8. 不足与局限

- **实验细节不透明**：从摘要和元数据来看，未提供具体数据集、模型规模、基线实现细节和消融实验，难以全面评估方法的普适性与公平性。
- **可扩展性未知**：未报告在更大规模智能体数量、更长轨迹、更复杂工具调用场景下的表现，低秩缓存共享的收益是否会随智能体数量增加而收敛或衰减尚不清楚。
- **依赖 shared-A 架构**：方法的部分计算优化（低秩缓存共享与复用）依赖于 shared-A 多 LoRA 架构假设，对于非 shared-A 架构（如每智能体独立 A 矩阵）的适用性需要额外适配。
- **应用限制**：该方法主要面向同轨迹（同一上下文）被多智能体重复处理的 agentic 场景；对于各智能体完全独立、无共享上下文的场景，收益有限。
- **信息可用性限制**：受限于提供的输入内容（仅摘要级文本），无法对论文的完整实验设置、复现难度和更深入的技术细节（如公式、伪代码）进行验证。

（完）
