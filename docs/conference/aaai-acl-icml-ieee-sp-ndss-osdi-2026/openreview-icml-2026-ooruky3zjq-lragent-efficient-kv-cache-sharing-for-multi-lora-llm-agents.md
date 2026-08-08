---
title: "LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents"
title_zh: LRAgent：面向多LoRA LLM智能体的高效KV缓存共享
authors: "Hyesung Jeon, Hyeongju Ha, Jae-Joon Kim"
date: 2026-04-30
pdf: "https://openreview.net/pdf/aad6d5a22a6ab8a9ad7c83d6bff25e05e9d49a41.pdf"
tags: ["query:cache-reuse"]
score: 9.0
evidence: 直接针对多LoRA智能体间共享KV缓存以减少重复计算
tldr: 针对多LoRA智能体系统中每个智能体为相同工具增强轨迹独立存储KV缓存导致的内存与计算开销问题，提出LRAgent框架。该框架将KV缓存分解为共享的预训练基座组件与各适配器组件，利用不同智能体间基座激活高度相似的特点实现缓存共享。实验表明该方法能显著降低存储与计算开销，同时保持角色特化能力，为大规模多智能体LLM应用提供高效的缓存复用方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 多LoRA智能体共享基座权重但各自维护独立KV缓存，造成大量重复计算和内存浪费。
method: 提出LRAgent，将KV缓存分解为共享基座组件与适配器组件，基于基座激活相似性进行跨智能体缓存共享。
result: 实验表明该框架显著降低KV缓存存储与计算开销，同时保持各智能体的角色特化性能。
conclusion: 通过解耦基座与适配器缓存，实现多智能体间KV缓存的高效复用，提升大规模多智能体系统推理效率。
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

# LRAgent：面向多 LoRA LLM 智能体的高效 KV 缓存共享

## 1. 核心问题与整体含义

- **研究背景**：多 LLM 智能体系统常通过 multi-LoRA 实现角色专业化（role specialization），即多个智能体共享同一个预训练骨干网络（pretrained backbone），各自只使用轻量 LoRA 适配器来区分角色。
- **核心问题**：虽然智能体共享基础模型权重，但在处理相同的长工具增强轨迹（tool-augmented trajectories）时，**每个智能体仍然独立构建并存储自己的 KV cache**，造成大量内存和计算冗余。
- **研究空白**：现有 KV cache 共享方法大多没有专门针对 multi-LoRA 智能体场景进行设计。
- **整体含义**：LRAgent 旨在利用“共享骨干激活高度相似”这一观察，在 multi-LoRA 智能体系统中实现跨智能体的 KV cache 共享，从而降低长上下文场景下的内存与计算开销，同时保持角色专业化能力。

## 2. 方法论

### 2.1 核心思想

- 作者观察到：跨智能体时，KV cache 的差异主要来自 **LoRA 适配器输出**，而共享预训练骨干产生的激活值高度相似。
- 因此，不再为每个智能体保存完整 KV cache，而是把 cache 分解为：
  - **共享基础组件**：来自预训练权重（backbone）的部分；
  - **适配器依赖组件**：来自 LoRA 权重的部分。

### 2.2 关键设计

- **共享基础缓存**：所有智能体复用同一份 backbone 产生的 KV 缓存，避免重复存储。
- **低秩存储适配器组件**：适配器部分天然是低秩（low-rank）的，因此以低秩形式保存，而不是扩展为完整维度。
- **依赖 shared-A multi-LoRA 架构**：在 shared-A 的多 LoRA 设置下（各智能体共享 LoRA 的 A 矩阵），低秩缓存也可以跨智能体共享，从而进一步避免重复计算。
- **Flash-LoRA-Attention 内核**：为了运行时高效重建适配器贡献，该内核重新排列注意力计算顺序，避免将低秩缓存先物化（materialize）成完整 K/V 矩阵，从而减少内存访问和计算量。

### 2.3 算法流程（文字描述）

1. 多个 LoRA 智能体共享同一个 pre-trained 模型，并使用 shared-A 的 LoRA 结构。
2. 对同一个长上下文，先计算并保存 backbone 部分的基础 K/V cache，作为全局共享组件。
3. 对每个智能体的 LoRA 适配器，计算低秩形式的 adapter 组件并保存。
4. 在 attention 计算时，通过 Flash-LoRA-Attention 内核，将 query 与基础 cache 以及低秩 adapter 贡献合并计算，而不是把低秩 cache 展开为完整维度。
5. 某个智能体已经处理过的上下文，可被其他智能体复用，从而减少重复的预填充（prefill）计算。

## 3. 实验设计

- **场景**：智能体式问答（agentic question-answering）任务，涉及多智能体角色专业化以及长工具增强轨迹。
- **Benchmark**：论文摘要只提到使用了“agentic question-answering benchmarks”（复数），但**没有在给定内容中列出具体数据集名称**。
- **对比方法**：
  - 非共享缓存基线（non-shared caching baseline）：每个智能体独立构建完整 KV cache；
  - 完全共享缓存（fully shared caching）：所有智能体完全共享 KV cache；
  - 本方法 LRAgent。
- **评价指标**：吞吐量（throughput）、首 token 延迟（time-to-first-token, TTFT）、任务准确率（accuracy）。

## 4. 资源与算力

- 在给定摘要和元数据中，**没有明确说明使用的 GPU 型号、GPU 数量、训练/推理时长、LoRA rank 规模、模型尺寸等算力信息**。
- 因此无法评估其资源消耗或可扩展性，只能确认其目标是降低 KV cache 内存和计算开销。

## 5. 实验数量与充分性

- 给定内容中只报告了“在多个 agentic QA benchmark 上”的总体结果，**没有列出具体实验组数**。
- 从指标覆盖来看，实验同时考虑了性能（accuracy）和效率（throughput、TTFT），是比较合理的评价维度。
- 但**缺少可验证的实验细节**：例如数据集名称、智能体数量、LoRA rank、上下文长度、内存节省量、消融实验等。
- 因此，基于当前信息只能判断实验设计方向合理，但**无法确认实验是否充分、客观、公平**。元数据中显示该论文得到 9.0 的评分，并被标注为 ICML-2026 接收，但这一信息不足以替代完整实验证据。

## 6. 主要结论与发现

- 跨智能体的 KV cache 差异主要由 LoRA 适配器贡献主导，而 backbone 激活高度相似。
- LRAgent 通过“共享基础组件 + 低秩适配器组件 + 专用注意力内核”的方式，可以在 multi-LoRA 智能体系统中高效共享 KV cache。
- 实验结果表明：
  - **吞吐量和 TTFT 接近“完全共享缓存”的上界**；
  - **准确率接近“非共享缓存”的基线**，即没有明显牺牲角色专业化能力。
- 总体结论：利用共享骨干的相似性进行 KV cache 共享，是提升多 LoRA 智能体系统效率的有效途径。

## 7. 优点

- **问题切入精准**：关注了 multi-LoRA 智能体系统这一被现有 KV cache 共享方法忽略的重要场景。
- **观察驱动设计**：基于“骨干激活相似、适配器输出主导差异”的实证观察构建方法，动机清晰。
- **兼顾内存与计算**：既减少 KV cache 存储，又通过 shared-A 架构和低秩形式避免重复计算。
- **工程可实现性强**：Flash-LoRA-Attention 内核设计避免了低秩缓存物化成完整矩阵，使得方法在实际推理中高效落地。
- **效率-精度权衡良好**：能接近完全共享缓存的速度，同时保持接近非共享缓存的准确率。

## 8. 不足与局限

- **信息不完整**：当前只能基于摘要和元数据总结，缺少模型架构、实验数据集、实现细节等关键内容。
- **依赖特定架构**：计算共享部分依赖 shared-A 的 multi-LoRA 设计；如果各智能体的 LoRA A 矩阵也彼此不同，低秩缓存共享可能无法直接适用。
- **前提可能受限**：方法建立在“跨智能体 backbone 激活高度相似”的观察之上；如果角色差异极大、适配器对隐藏状态影响显著，基础缓存共享的收益或准确性可能下降。
- **准确率影响尚不明确**：摘要只说“接近非共享缓存基线”，但没有给出具体误差范围或在哪些任务上可能出现退化。
- **实验覆盖不足**：未给出实际内存节省比例、可支持的上下文长度、智能体规模、LoRA rank 规模等关键数据，难以全面评估方法的上限和适用范围。
- **客观性风险**：只有单一论文摘要，没有提供对应实现代码、完整结果表和消融实验，因此难以独立验证实验公平性。

（完）
