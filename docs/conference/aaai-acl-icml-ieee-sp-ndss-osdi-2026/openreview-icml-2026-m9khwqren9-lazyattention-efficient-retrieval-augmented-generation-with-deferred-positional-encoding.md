---
title: "LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding"
title_zh: LazyAttention：延迟位置编码的高效检索增强生成
authors: "Haocheng Xia, Mihir Pamnani, Hanxi Fang, Supawit Chockchowwat, Yongjoo Park"
date: 2026-04-30
pdf: "https://openreview.net/pdf/c4d825d653070733092c564642dc66ac6db18eb5.pdf"
tags: ["query:cache-reuse"]
score: 8.0
evidence: 与位置无关的KV重用支持跨上下文共享缓存，可用于多智能体缓存复用
tldr: 传统KV缓存将位置信息直接嵌入缓存，导致缓存难以跨上下文重用。LazyAttention通过内核化的延迟位置编码，在注意力计算时动态调整位置，实现零拷贝、与位置无关的KV重用，避免了重量化内存开销。实验表明其在长上下文RAG和上下文学习场景中显著提升缓存复用效率，为多智能体间KV缓存共享提供了基础方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 传统KV缓存固化了位置信息，限制缓存跨上下文复用，现有方法只能前缀复用或需昂贵重编码。
method: 提出延迟位置编码的注意力机制，在内核中动态调整位置编码，实现位置无关的KV缓存复用。
result: 在RAG和上下文学习等任务中，LazyAttention以较低开销支持更灵活的缓存重用，提升推理效率。
conclusion: 位置无关的KV重用可支持多智能体/多场景间共享缓存，减少重复计算。
---

## Abstract
Key-value (KV) caching accelerates inference of large language models (LLMs) by reusing past computations for generated tokens. Its importance becomes even greater in long-context applications such as retrieval-augmented generation (RAG) and in-context learning (ICL). However, conventional KV caching embeds positional information directly into the cache, limiting its reusability. Existing solutions either restrict reuse to prefixes or require expensive memory materialization for positional re-encoding. We introduce LazyAttention, a novel attention mechanism that kernelizes deferred positional encoding to enable zero-copy, position-agnostic KV reuse. By adjusting positional encoding within attention kernels on-the-fly, LazyAttention resolves the materialization bottleneck, allowing a single physical KV copy to serve multiple logical requests at arbitrary positions. Leveraging attention kernels tailored for prefilling and decoding, our system achieves significant efficiency improvements: under skewed document distributions, it reduces time-to-first-token (TTFT) by 1.37× and increases inference throughput by 1.40× compared to the state-of-the-art Block-Attention, while maintaining comparable output quality.

---

## 论文详细总结（自动生成）

: 根据提供的论文文本，内容很简短，只有摘要和元数据。需要基于这些信息生成详细中文总结。注意论文实际文本只有标题、作者、摘要、元数据。没有实验细节、资源算力等信息。所以需要明确指出未提及的部分。按照要求的结构，尽可能从摘要和元数据推断。注意原文说“下面提供的论文内容”，但内容只有摘要和元数据，没有正文。所以要基于摘要和元数据中的信息，并诚实指出缺失的内容。生成Markdown格式，最后一行（完）。# LazyAttention：延迟位置编码的高效检索增强生成 — 论文总结

## 1. 核心问题与整体含义

- **研究背景**：KV（键值）缓存通过复用已生成 token 的中间计算，显著加速大语言模型（LLM）推理；在长上下文场景如检索增强生成（RAG）和上下文学习（ICL）中，KV 缓存的作用尤为关键。
- **核心问题**：传统 KV 缓存将**位置信息直接嵌入缓存内部**，导致缓存与特定上下文位置强绑定，难以跨不同上下文复用。
- **现有方案的局限**：
  - 已有方法要么只支持**前缀复用**（即缓存只能从开头位置开始使用），灵活性受限；
  - 要么需要**昂贵的内存物化（materialization）** 来重新编码位置信息，带来大量额外开销。
- **整体含义**：该论文旨在突破 KV 缓存的“位置绑定”限制，实现**位置无关的 KV 重用**，从而支持多个逻辑请求共享同一份物理缓存，提升推理效率并减少重复计算。

## 2. 方法论

- **核心思想**：提出 **LazyAttention** 注意力机制，将位置编码“延迟”到注意力计算阶段，而非在缓存写入时固化。
- **关键技术细节**：
  - **内核化延迟位置编码**：在注意力内核（attention kernel）内部**动态地调整位置编码**，而不是预先将位置信息写入 KV 缓存；
  - **零拷贝（zero-copy）与位置无关**：由于缓存中不包含特定位置信息，**同一份物理 KV 缓存**可以被多个逻辑请求以任意位置“借用”；
  - **解决物化瓶颈**：避免了传统方法中为重新编码位置而进行的内存物化和数据复制。
- **算法流程（文字说明）**：
  1. 在预填充阶段，按常规方式计算 Key 和 Value，但**不将位置编码集成到缓存值中**；
  2. 将位置信息单独保存或按需生成；
  3. 在解码/注意力计算阶段，内核中根据当前请求的实际位置，**动态地将正确的相对位置编码应用到相应的 Key 上**（或等效地在注意力分数计算中调整位置偏差）；
  4. 由于缓存本身不带位置，多个请求可以在不同位置复用同一缓存副本。
- **系统实现**：针对预填充和解码分别设计了定制的注意力内核，以最大化效率。

## 3. 实验设计

- **数据集与场景**：
  - 长上下文 **RAG（检索增强生成）** 场景；
  - **ICL（上下文学习 / in-context learning）** 场景；
  - 采用**倾斜文档分布（skewed document distributions）** 的测试环境。
- **Benchmark**：论文未明确提及具体公开数据集名称（如 LongBench、MT-Bench 等），仅描述了场景类型。
- **对比方法**：
  - 以 **Block-Attention** 作为最先进基线（state-of-the-art）；
  - 同时隐含对比了传统 KV 缓存及前缀复用方案。
- **评估指标**：首 token 时间（TTFT）、推理吞吐量、输出质量。

## 4. 资源与算力

- **论文中未明确说明**使用的 GPU 型号、数量、训练时长或推理硬件配置。
- 摘要仅提及实现了针对预填充和解码的注意力内核，但没有给出任何算力/资源细节。
- 因此无法评估其资源消耗的绝对规模。

## 5. 实验数量与充分性

- **实验数量**：从摘要和元数据看，论文至少进行了性能对比（TTFT、吞吐量）和质量对比实验，覆盖 RAG 和 ICL 两类场景，使用了倾斜分布设置。
- **充分性评估**：
  - **信息不足**：由于只提供摘要，无法确知是否包含消融实验（如不同位置跨度、不同请求数量、不同模型大小等）；
  - **客观性**：与 Block-Attention 对比是合理的强基线选择，但缺乏对更多基线（如 PagedAttention、vLLM 中的前缀缓存、StreamingLLM 等）的对比信息；
  - **公平性**：未说明对照组与实验组是否在相同硬件、批量大小、精度下测试，无法完全判断公平性。

## 6. 主要结论与发现

- **效率提升显著**：在倾斜文档分布下，相比 Block-Attention：
  - **TTFT 降低 1.37 倍**；
  - **推理吞吐量提升 1.40 倍**；
  - 同时保持**可比的输出质量**。
- **可行性验证**：证明位置无关的 KV 重用在实践中是可行的，且能以较低开销实现更灵活的缓存重用。
- **更广泛意义**：位置无关的 KV 共享可扩展到**多智能体/多场景间的缓存复用**，减少全局重复计算。

## 7. 优点

- **问题切中要害**：传统 KV 缓存的位置绑定是一个根本限制，论文的切入点清晰且重要。
- **零拷贝设计优雅**：通过内核内动态调整位置编码，避免了昂贵的内存物化，是一种轻量且高效的解决方案。
- **复用粒度突破**：从“仅前缀复用”扩展到“任意位置复用”，显著提升缓存灵活性。
- **性能增益明确**：给出与 SOTA 的量化对比，TTFT 和吞吐量的提升说明实际收益。
- **场景选择合理**：RAG 和 ICL 都是长上下文、高缓存重用的典型场景，有实际应用价值。

## 8. 不足与局限

- **实验细节缺失**：由于仅提供摘要，无法确认具体数据集、模型规模、上下文长度范围，实验覆盖的广度不明确。
- **未报告算力资源**：无法判断其相对成本，也无法复现或对比资源效率。
- **质量评估可能不足**：摘要仅说“可比输出质量”，但未说明具体评测指标（如 ROUGE、BLEU、人工评估等），也看不出是否对多样本进行了统计检验。
- **倾斜分布假设**：性能优势是在“倾斜文档分布”下取得的，对于均匀分布或极端长尾分布的效果尚不明确。
- **多智能体扩展仅为推测**：元数据提到可用于多智能体缓存复用，但摘要中没有直接实验证据，属于推广性推断。

（完）
