---
title: "LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents"
title_zh: LRAgent：面向多LoRA LLM智能体的高效KV缓存共享
authors: "Hyesung Jeon, Hyeongju Ha, Jae-Joon Kim"
date: 2026-04-30
pdf: "https://openreview.net/pdf/aad6d5a22a6ab8a9ad7c83d6bff25e05e9d49a41.pdf"
tags: ["query:agent-cache"]
score: 9.0
evidence: 面向多LoRA LLM智能体的KV缓存共享框架，直接解决跨智能体缓存复用
tldr: 多LoRA智能体系统虽然共享预训练骨干，但每个智能体仍为相同的工具增强轨迹独立存储KV缓存，造成大量内存与计算浪费。LRAgent观察到跨智能体的缓存差异主要由适配器输出主导，而骨干激活高度相似，因此将缓存分解为共享的基础组件与适配器专属组件。通过复用共享部分，显著降低多智能体场景下的KV缓存开销。这对于智能体流水线中的缓存共享具有直接意义。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 多LoRA智能体共享同一个骨干但各自存储完整KV缓存，造成显著内存与计算浪费。
method: 将KV缓存分解为共享的预训练骨干基础和离散的适配器部分，实现复用。
result: 实验显示在保持任务质量的同时大幅降低缓存内存和计算开销。
conclusion: 基于骨干与适配器分解的缓存共享可高效支持多LoRA智能体系统。
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

# LRAgent：面向多LoRA LLM智能体的高效KV缓存共享——论文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：多LLM智能体系统通常通过**多LoRA（Multi-LoRA）** 实现角色分工——多个智能体共享同一个预训练骨干模型（Backbone），仅通过轻量级适配器（Adapter）实现差异化。这一架构在保持模型能力的同时，大幅降低了多智能体的部署成本。
- **问题**：尽管这些智能体共享预训练权重，但**每个智能体仍然独立构建并存储自己的KV缓存**（KV Cache），用于相同的、较长的、经过工具增强的轨迹（Tool-Augmented Trajectories）。这种冗余造成了巨大的显存（Memory）和计算（Compute）开销。
- **核心观察**：跨智能体比较时，KV缓存的差异主要由**适配器（Adapter/LoRA）输出**主导，而共享的预训练骨干产生的激活（Activations）高度相似。
- **整体含义**：现有KV缓存共享方法普遍忽视了多LoRA这一特殊场景。LRAgent填补了这一空白，通过将缓存分解为“可共享的基础部分”和“适配器专属部分”，实现了多LoRA智能体场景下的高效缓存复用，兼顾了内存效率、计算效率与任务质量。

## 2. 方法论（核心思想、关键技术、公式或算法流程）

### 2.1 核心思想
- **缓存分解**：将KV缓存分解为两个部分：
  - **共享基础组件（Shared Base Component）**：来自预训练骨干权重的激活，跨智能体高度相似，可以被多个智能体安全共享。
  - **适配器依赖组件（Adapter-Dependent Component）**：来自LoRA权重的贡献，是智能体间差异的主要来源，需要按智能体单独存储。
- **低秩存储**：适配器组件天然具有低秩特性（LoRA本身即为低秩分解），因此LRAgent将其以固有的低秩形式存储，而非展开成完整的隐藏维度（Hidden Dimension），从而进一步压缩显存占用。

### 2.2 关键技术
- **共享低秩缓存与冗余计算消除**：结合**共享-$A$多LoRA架构**（Shared-$A$ Multi-LoRA Architectures，即多个LoRA共享相同的投影矩阵$A$，仅$B$矩阵不同），LRAgent不仅共享基础组件，还共享低秩缓存本身，从而**避免不同智能体对已处理上下文的重复计算**。
- **Flash-LoRA-Attention 内核**：为高效重建适配器贡献，论文提出了专用内核。该内核**重新排列注意力计算的执行顺序**（Reorders Attention Computation），避免将低秩缓存物化为完整的隐藏维度（Full Dimension），从而在不引入额外开销的前提下完成注意力计算。

### 2.3 算法流程（文字说明）
1. 前向传播过程中，将每个Transformer层的KV激活拆分为骨干贡献和LoRA贡献。
2. 骨干贡献被存入共享缓存池，供所有智能体复用。
3. LoRA贡献以低秩形式直接存储（利用Shared-$A$架构进一步共享$A$投影结果）。
4. 在注意力计算阶段，Flash-LoRA-Attention按重排后的顺序合并共享缓存与低秩适配器贡献，在不显式物化完整KV矩阵的条件下完成注意力计算。

## 3. 实验设计

> 注：由于当前仅获取到论文摘要，以下基于摘要中披露的信息进行总结，具体数据集与对比方法的细节在摘要中有限。

- **数据集/场景**：
  - 使用了**智能体问答基准（Agentic Question-Answering Benchmarks）**，具体数据集名称在摘要中未列出。
- **对比方法**：
  - **完全共享缓存（Fully Shared Caching）**：上界参照，忽略智能体差异。
  - **非共享缓存基线（Non-Shared Caching Baseline）**：标准的多LoRA智能体各自独立缓存方案。
  - 现有其他KV缓存共享方法（在摘要中未逐一列出，但论文指出已有方法未覆盖多LoRA场景）。
- **评估指标**：
  - **吞吐量（Throughput）**
  - **首Token延迟（Time-to-First-Token, TTFT）**
  - **任务准确性（Accuracy）**

## 4. 资源与算力

- **未明确说明**：原文摘要中**未提及**使用的GPU型号、GPU数量、训练/推理时长、显存占用等具体算力信息。
- 仅在结论中提及“显著降低内存开销”和“计算开销”，但未给出具体数字或硬件配置。如需评估实际资源消耗，需要阅读论文全文的实验部分。

## 5. 实验数量与充分性

- **实验覆盖面**：从摘要来看，实验涵盖**吞吐量、TTFT和准确性**三类关键指标，但仅在“智能体问答”一类任务上验证。
- **充分性评估**：
  - **优点**：核心对比维度（性能 vs. 质量）设置合理，两个极端基线（完全共享 vs. 非共享）提供了清晰的下界与上界参照。
  - **不足**：
    - 摘要中**未提及消融实验**（如不同LoRA秩、不同智能体数量、不同轨迹长度的影响）。
    - 仅在QA基准上评估，**未覆盖更广泛的多智能体场景**（如多轮对话、代码生成、复杂工具调用等）。
    - 具体数据集数量和规模未知，实验广度在摘要层面难以全面评估。

## 6. 主要结论与发现

- LRAgent实现的**吞吐量和TTFT延迟接近“完全共享缓存”的理想上界**，同时保持了**接近“非共享缓存基线”的任务准确性**。
- 核心结论是：通过将KV缓存分解为共享骨干基础与适配器低秩组件，**能够以极小的精度损失换取接近理想情况的内存与计算性能**，为多LoRA智能体系统提供了高效的缓存共享方案。
- 该结果验证了“跨智能体KV缓存差异主要由适配器贡献主导”的初始观察。

## 7. 优点与亮点

- **问题敏锐性**：准确识别出多LoRA智能体场景中“共享权重但缓存不共享”的显著资源浪费，切中实际部署痛点。
- **方法论创新**：
  - 将KV缓存按“骨干/适配器”维度分解，思路简洁且契合LoRA架构本质。
  - 利用Shared-$A$架构实现低秩缓存的二次共享，进一步消除冗余计算。
  - Flash-LoRA-Attention内核通过重排计算顺序避免高维物化，工程实现层面具有实用性。
- **实验结果**：在性能和精度之间取得了很好的平衡，证明了方法的实用价值——既不像完全共享那样牺牲精度，又比非共享缓存大幅提升效率。

## 8. 不足与局限

- **实验覆盖有限**：仅在智能体问答基准上验证，未展示在更多任务类型（如多智能体协作、长链推理、多模态等）上的泛化能力。
- **架构依赖**：方法有效性的一个重要前提是**Shared-$A$多LoRA架构**；对于不共享$A$矩阵的通用LoRA设置，低秩缓存共享的收益可能受限。
- **实现复杂性**：引入专用内核（Flash-LoRA-Attention）和缓存分解机制，对现有推理框架的改造难度与工程成本未在摘要中讨论。
- **信息缺失**：摘要中未给出硬件资源、具体显存节省数字、数据集规模等定量信息，难以独立评估其实际收益程度。
- **潜在偏差风险**：缓存分解依赖“骨干激活高度相似”这一观察，在极端情况下（如LoRA秩很大或适配器训练差异极大时），该假设是否仍然成立需要进一步验证。

---

（完）
