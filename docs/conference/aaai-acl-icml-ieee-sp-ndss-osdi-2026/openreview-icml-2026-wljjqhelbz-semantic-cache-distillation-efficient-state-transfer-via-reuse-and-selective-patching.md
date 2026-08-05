---
title: "Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching"
title_zh: 语义缓存蒸馏：通过复用与选择性修补实现高效状态迁移
authors: "Qianli Ma, Zhiqing Tang, Hanshuai Cui, Zhi Yao, Weijia Jia"
date: 2026-04-30
pdf: "https://openreview.net/pdf/e80c6a92b3732eaab80f5f22c33fab08f4cd3792.pdf"
tags: ["query:cache-reuse"]
score: 7.0
evidence: 通过复用与选择性修补实现跨上下文的KV缓存高效状态迁移
tldr: 语义缓存蒸馏方法针对LLM推理中KV缓存传输开销大以及异构模型间缓存复用产生语义偏差的问题，提出用紧凑的语义编码替代原始KV传输，并通过复用与选择性修补两个机制分别压缩传输成本与修正语义错位。实验表明该方法能在降低通信开销的同时保持生成质量。该工作为跨上下文的高效KV缓存复用与迁移提供了通用技术路径。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 解决LLM推理中KV缓存传输成为瓶颈以及异构模型间缓存复用导致语义错位的问题。
method: 提出SCD框架，用紧凑语义编码替代原始KV传输，采用Reuse重建低秩层、Patch预测归一化输入。
result: 实验表明SCD在显著降低缓存传输开销的同时保持了生成质量。
conclusion: SCD为跨模型与跨上下文的KV缓存复用迁移提供了一种通用高效的方案。
---

## Abstract
Disaggregated serving alleviates memory bottlenecks in Large Language Model (LLM) inference but creates a severe communication bottleneck: transmitting high-dimensional Key-Value (KV) caches often dominates time-to-first-token (TTFT). Moreover, reusing caches across heterogeneous models (e.g., base and fine-tuned variants) causes semantic misalignment that accumulates over layers, degrading generation quality. We propose Semantic Cache Distillation (SCD), a loss-constrained framework that replaces raw KV transmission with compact semantic codes. SCD addresses these challenges via two mechanisms: (1) Reuse, which reconstructs most layers from low-rank subspaces to minimize transfer cost, and (2) Patch, which predicts normalized inputs at sparse transition layers to truncate error propagation. Empirically, SCD delivers up to 2.65 $\times$ TTFT speedup over the oracle consumer prefill and dominates quantization and selective recomputation baselines on the quality--latency Pareto frontier in bandwidth-constrained regimes, while keeping generation quality within 5\% F1 of the oracle.

---

## 论文详细总结（自动生成）

# 中文总结

## 1. 核心问题与整体含义

- **研究背景**：大语言模型（LLM）推理中，**分离式服务（disaggregated serving）** 虽缓解了内存瓶颈，却引入了新的通信瓶颈——传输高维 **KV 缓存** 会显著拉长 **首 token 延迟（TTFT）**。
- **另一个问题**：在不同模型（如基座模型与微调变体）之间**复用缓存**时，会产生**语义错位（semantic misalignment）**，且这种偏差随层数累积，导致生成质量下降。
- **整体含义**：论文致力于解决 LLM 推理中 KV 缓存**传输成本高**与**跨模型复用质量差**这两大核心矛盾，属于高效推理与缓存复用领域的通用技术路线。

## 2. 方法论：语义缓存蒸馏（Semantic Cache Distillation, SCD）

- **核心思想**：不直接传输原始高维 KV 缓存，而是用一个**紧凑的语义编码（compact semantic codes）** 替代，从而在保持生成质量的前提下大幅降低通信开销。
- **损失约束框架**：整个方法是一个**有损失约束（loss-constrained）** 的框架，保证编码/解码过程的语义保真度。
- **两大机制**：
  - **Reuse（复用）**：
    - 针对大多数层，从**低秩子空间（low-rank subspaces）** 重建 KV 缓存。
    - 目的：最小化传输成本，因为低秩表示比原始 KV 张量要紧凑得多。
  - **Patch（选择性修补）**：
    - 在**稀疏的过渡层（sparse transition layers）** 上预测**归一化输入（normalized inputs）**。
    - 目的：截断跨层误差传播，修正由低秩重建带来的语义错位，保证生成质量。
- **算法流程（文字说明）**：
  1. 在源模型侧，将 KV 缓存投影到低秩语义子空间，提取紧凑语义编码；
  2. 将编码传输到目标模型侧，通过 Reuse 机制重建大多数层的 KV 缓存；
  3. 在少数关键过渡层，利用已重建的上下文预测归一化输入，并通过 Patch 机制对重建结果进行修正；
  4. 最终在目标模型上完成 prefill 或增量推理，得到生成结果。

## 3. 实验设计

- **由于提供的仅为摘要，具体数据集、benchmark 与对比方法未完全展开，但可从摘要中归纳**：
  - **场景**：带宽受限（bandwidth-constrained）的分离式推理环境，涉及基座模型与微调变体间的跨模型缓存复用。
  - **Benchmark**：未具体列出数据集名称，但以 **TTFT 加速比**、**生成质量（F1）** 为核心指标，并绘制了 **质量—延迟 Pareto 前沿**。
  - **对比方法**：
    - **Oracle consumer prefill**（无缓存复用的标准重计算基线，作为性能上限）；
    - **量化方法（quantization）**；
    - **选择性重计算（selective recomputation）** 基线。
  - **性能结果**：
    - 与 oracle consumer prefill 相比，SCD 最高可实现 **2.65× TTFT 加速**；
    - 在带宽受限场景下，SCD 在质量—延迟 Pareto 前沿上**优于**量化和选择性重计算基线；
    - 生成质量保持在 oracle 的 **5% F1 以内**。

## 4. 资源与算力

- **摘要中未提及任何具体算力信息**，包括 GPU 型号、数量、训练/推理时长、显存占用等。
- 论文可能将算力细节放在正文或附录中，但当前提取文本未包含；因此不能对训练成本做出准确评估。

## 5. 实验数量与充分性

- **从摘要可确认的实验类型**：
  - 性能对比实验（TTFT 加速比与生成质量）；
  - Pareto 前沿分析实验（涵盖 SCD、量化、选择性重计算三种方法）；
  - 跨模型缓存复用实验（基座 vs 微调变体）。
- **未提及**：
  - 消融实验（Reuse 与 Patch 各自贡献的单独验证）；
  - 不同模型规模（如 7B/13B/70B）的扩展实验；
  - 不同数据集多样性；
  - 带宽变化范围对性能影响的敏感性分析。
- **充分性判断**：虽然核心结论有一定支撑，但由于仅有摘要信息，实验的**全面性、客观性与公平性**无法完全验证。摘要仅给出了与两个基线的 Pareto 对比，未展示误差累积的具体曲线、不同层数下 Patch 稀疏度的影响等细节。

## 6. 主要结论与发现

- SCD 能够在**显著降低 KV 缓存传输开销**（TTFT 最高提升 2.65×）的同时，**保持生成质量**（F1 偏差 ≤ 5%）。
- 通过“低秩重建 + 稀疏层修补”的组合，SCD 在**带宽受限场景**中同时获得了速度和质量的有利权衡，优于量化和选择性重计算基线。
- 该结果表明，**紧凑语义编码替代原始 KV 传输**是一种缓解分离式推理通信瓶颈的有效范式，并能为跨模型缓存复用提供通用解决方案。

## 7. 优点

- **问题定位精准**：同时针对分离式推理的通信瓶颈和跨模型缓存复用的语义错位，切中实际部署痛点。
- **方法设计紧凑**：Reuse 与 Patch 分工明确——Reuse 负责压缩传输成本，Patch 负责修正语义偏差，形成低秩重建与稀疏修正的互补机制。
- **引入损失约束**：使压缩过程具有可量化的保真度控制，而非无约束的启发式压缩。
- **结果具有实用性**：在保持 oracle 5% F1 以内的前提下获得 2.65× TTFT 加速，说明方法具备实际部署价值。
- **评价视角合理**：采用质量—延迟 Pareto 前沿对比，不是单一指标比拼，更能反映真实场景下的工程权衡。

## 8. 不足与局限

- **实验细节缺失**：摘要未给出具体数据集、模型规模、参数量、通信带宽设定等关键实验条件，难以判断结论的适用范围。
- **算力与开销信息不透明**：未提及 SCD 本身在源模型端编码和目标模型端解码的计算开销，如果额外计算代价过高，可能抵消通信节省。
- **跨模型偏差能力有限验证**：只提到微调变体的复用，对于更激进的异构模型（如不同架构、不同 tokenizer）之间的适配效果未展示。
- **Patch 机制的设计细节不充分**：如何选择“稀疏过渡层”、patch 预测的模型结构与额外延迟成本未披露，可能导致复现困难。
- **潜在偏差风险**：Pareto 前沿对比中，量化和选择性重计算的超参选择是否最优未知；若基线调参不充分，结论可能偏乐观。
- **应用限制**：方法依赖低秩假设和稀疏修正，对于长上下文、超大模型或注意力分布高度非低秩的场景，其有效性和压缩比可能下降。

（完）
