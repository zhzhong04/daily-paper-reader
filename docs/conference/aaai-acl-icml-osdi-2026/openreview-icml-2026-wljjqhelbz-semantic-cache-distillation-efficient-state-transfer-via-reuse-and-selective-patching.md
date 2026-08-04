---
title: "Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching"
title_zh: 语义缓存蒸馏：通过复用与选择性补丁的高效状态迁移
authors: "Qianli Ma, Zhiqing Tang, Hanshuai Cui, Zhi Yao, Weijia Jia"
date: 2026-04-30
pdf: "https://openreview.net/pdf/e80c6a92b3732eaab80f5f22c33fab08f4cd3792.pdf"
tags: ["query:cache-reuse"]
score: 8.0
evidence: 通过语义码复用KV缓存并最小化传输成本，与跨上下文KV缓存复用直接相关
tldr: 解聚式服务虽缓解了LLM推理的内存瓶颈，却带来KV缓存传输开销大且跨模型复用语义错位的问题。本文提出语义缓存蒸馏（SCD），用紧凑语义码替代原始KV传输，通过低秩子空间复用和选择性补丁机制降低传输代价并缓解语义失配。实验显示该方法能显著减少KV传输成本并保持生成质量，为多智能体间KV缓存复用提供了可行思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: KV缓存传输成为解聚式LLM服务的通信瓶颈，且跨模型复用存在语义错位。
method: 提出语义缓存蒸馏框架，用低秩子空间复用重建多数层，并用归一化输入预测进行选择性补丁。
result: 显著降低KV传输成本，同时缓解语义失配造成的生成质量下降。
conclusion: SCD为高效状态迁移和跨模型KV复用提供了通用方法，可推广至智能体上下文缓存共享。
---

## Abstract
Disaggregated serving alleviates memory bottlenecks in Large Language Model (LLM) inference but creates a severe communication bottleneck: transmitting high-dimensional Key-Value (KV) caches often dominates time-to-first-token (TTFT). Moreover, reusing caches across heterogeneous models (e.g., base and fine-tuned variants) causes semantic misalignment that accumulates over layers, degrading generation quality. We propose Semantic Cache Distillation (SCD), a loss-constrained framework that replaces raw KV transmission with compact semantic codes. SCD addresses these challenges via two mechanisms: (1) Reuse, which reconstructs most layers from low-rank subspaces to minimize transfer cost, and (2) Patch, which predicts normalized inputs at sparse transition layers to truncate error propagation. Empirically, SCD delivers up to 2.65 $\times$ TTFT speedup over the oracle consumer prefill and dominates quantization and selective recomputation baselines on the quality--latency Pareto frontier in bandwidth-constrained regimes, while keeping generation quality within 5\% F1 of the oracle.

---

## 论文详细总结（自动生成）

# 中文总结

## 1. 核心问题与整体含义（研究动机与背景）
- **背景**：大型语言模型（LLM）推理中，解聚式（disaggregated）服务架构能缓解内存瓶颈，但引入了严重的通信瓶颈——传输高维 KV 缓存往往主导了首 token 延迟（TTFT）。
- **核心问题**：
  1. **通信开销大**：原始 KV 缓存维度高、传输成本高，制约了解聚式推理的效率。
  2. **跨模型语义错位**：在不同模型（如基座模型与微调变体）之间复用缓存时，会产生语义错位，且这种错位随层数累积，导致生成质量下降。
- **整体含义**：需要一种更高效的状态迁移方式，在降低 KV 传输成本的同时，保持跨模型复用的语义一致性，从而提升解聚式 LLM 服务的整体性能。

## 2. 方法论：核心思想、关键技术细节与流程
- **方法名称**：语义缓存蒸馏（Semantic Cache Distillation, SCD）。
- **核心思想**：不直接传输原始 KV 缓存，而是用紧凑的“语义码”（semantic codes）替代原始 KV 传输，并通过“复用 + 选择性补丁”机制平衡传输成本与生成质量。
- **关键技术细节**：
  - **Reuse（复用）机制**：通过低秩子空间（low-rank subspaces）重建大多数层的 KV 缓存，从而最小化传输成本。
  - **Patch（补丁）机制**：在稀疏的“过渡层”上预测归一化输入（normalized inputs），以截断跨层误差传播，缓解语义错位带来的质量损失。
  - **损失约束框架**：SCD 是一个 loss-constrained 框架，即优化目标中显式约束重建/传输带来的信息损失，使 KV 压缩与跨模型复用在质量约束下进行。
- **算法流程（文字描述）**：
  1. 将原始 KV 缓存编码为紧凑的语义码，代替高维 KV 张量进行传输。
  2. 在接收端，利用低秩子空间从语义码中重建大部分层的 KV。
  3. 对少量关键过渡层，根据归一化输入预测结果执行选择性补丁，修正重建误差。
  4. 通过损失约束控制整体重建误差，保证下游生成质量。

## 3. 实验设计
- **数据集/场景**：论文摘要未明确列出具体数据集名称，只提到“oracle consumer prefill”作为参考基准，以及带宽受限（bandwidth-constrained）场景。
- **Benchmark**：使用“oracle consumer prefill”作为理想上界，对比质量-延迟帕累托前沿（quality–latency Pareto frontier）。
- **对比方法**：
  - 量化（quantization）基线；
  - 选择性重计算（selective recomputation）基线；
  - oracle（直接使用完整 consumer prefill）作为上界。
- **评价指标**：TTFT 加速比、F1（生成质量）。

## 4. 资源与算力
- **论文摘要中未明确说明**使用的 GPU 型号、数量、训练/推理时长、显存占用等资源信息。
- 仅能推断实验涉及 KV 缓存传输与 LLM 推理，但具体硬件配置无细节可总结。

## 5. 实验数量与充分性
- **实验数量**：从摘要看，至少包含三类对比（量化、选择性重计算、oracle），并报告了 TTFT 加速与 F1 质量结果；未明确提及消融实验或多种数据集上的重复实验。
- **充分性判断**：
  - **客观性**：使用 oracle 作为上界、帕累托前沿对比，比较公平。
  - **充分性有限**：由于摘要篇幅限制，未给出多数据集、多模型规模、多带宽条件的详细结果，也未展示消融实验（如 Reuse 和 Patch 各自贡献）。因此实验完整性存疑，需阅读全文确认。

## 6. 主要结论与发现
- 相比 oracle consumer prefill，SCD 最高可实现 **2.65 倍 TTFT 加速**。
- 在带宽受限场景下，SCD 在质量-延迟帕累托前沿上**优于量化与选择性重计算基线**。
- 同时，生成质量保持在 oracle 的 **5% F1 以内**，即显著降低传输成本的同时几乎不损失生成质量。

## 7. 优点
- **方法设计有针对性**：同时解决 KV 传输带宽和跨模型语义错位两个关键问题。
- **可解释性强**：Reuse 负责降成本，Patch 负责控误差，分工清晰。
- **理论约束完备**：采用 loss-constrained 框架，使压缩过程有明确的质量边界。
- **实用性强**：在带宽受限场景下获得显著 TTFT 收益，且质量损失可控，适合实际部署。

## 8. 不足与局限
- **实验细节缺失**：摘要未提供数据集列表、模型规模、KV 层数、带宽参数等，结果泛化性难以评估。
- **未报告算力/资源消耗**：无法判断方法本身的额外计算开销（如语义码编码、归一化输入预测）是否值得。
- **跨模型泛化范围不明**：仅提到 base 与 fine-tuned 变体，未覆盖不同架构、不同 tokenizer 等更常见的异构场景。
- **无消融分析**：Reuse 与 Patch 各自贡献未见单独量化，机制有效性难以分离。
- **论文状态**：来自 ICML-2026-Accepted，但来源是论文元数据，具体审稿意见和最终版本有待核实。

（完）
