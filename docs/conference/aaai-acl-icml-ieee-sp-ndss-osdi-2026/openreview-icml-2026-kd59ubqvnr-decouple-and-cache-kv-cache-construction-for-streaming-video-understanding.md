---
title: "Decouple and Cache: KV Cache Construction for Streaming Video Understanding"
title_zh: 解耦与缓存：面向流式视频理解的KV缓存构建
authors: "Zhanzhong Pang, Dibyadip Chatterjee, Fadime Sener, Angela Yao"
date: 2026-04-30
pdf: "https://openreview.net/pdf/045d2dd9b2c8ce0ded77e2daf04346a65aa4ad89.pdf"
tags: ["query:awc"]
score: 4.0
evidence: 面向无界流的KV缓存构建与驱逐，可类比驱逐策略
tldr: 流式视频理解需要处理无界视频流，内存和计算受限，需要不断构建和驱逐KV缓存。现有模型难以从短序列泛化到长流，且忽略了缓存构建的影响。DSCache提出一种无需训练的流式缓存构建机制，将预训练离线模型适配到流式场景，通过累积维护缓存并配合驱逐策略来扩展感知范围。实验表明DSCache支持无界流处理并提升缓存重用效果，对缓存驱逐策略设计有借鉴意义。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 无界视频流下KV缓存构建与驱逐困难，模型从短序列泛化到长流受限。
method: 提出DSCache，一种免训练的流式缓存构建机制，累积维护并驱逐KV缓存以适应无界流。
result: 实验验证DSCache能扩展到无界视频流并改善缓存重用性能。
conclusion: DSCache为缓存构建与驱逐提供了新思路，可迁移到智能体工作流的缓存管理。
---

## Abstract
Streaming video understanding requires processing unbounded video streams with limited memory and computation, posing two key challenges. First, continuously constructing new and evicting old key-value(KV) caches is required for unbounded streams. Secondly, due to the high cost of collecting and training on unbounded streams, models must learn from short sequences while generalizing to long streams. Existing streaming VideoVLLMs fail to scale to unbounded video streams or focus on cache reuse strategies, leaving the impact of cache construction underexplored. In this paper, we propose Decoupled Streaming Cache(DSCache), a training-free cache construction mechanism that adapts pretrained offline models to streaming settings. DSCache maintains a cumulative past KV cache while constructing a separate instant cache on-demand, decoupled from past caches to preserve the informativeness of recent inputs. To enable position extrapolation beyond the training length, DSCache further incorporates a position-agnostic encoding strategy, ensuring KV caches to support unseen positions and preventing position overflow. Experiments on Streaming Video QA benchmarks demonstrate DSCache's state-of-the-art performance, with an average 2.5% accuracy gains over prior methods.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：流式视频理解需要处理**无界视频流**，而内存和计算资源是有限的，因此面临两大核心挑战：
  1. 需要**持续构建新KV缓存**并**驱逐旧KV缓存**，以适配无界输入；
  2. 由于无界流的数据采集和训练成本极高，模型必须在**短序列上训练**，却要能**泛化到长视频流**。
- **已有方法的不足**：现有流式视频大语言模型（Streaming VideoVLLMs）要么**无法真正扩展到无界流**，要么只专注于**缓存重用策略**，而**忽略了缓存构建过程本身**对性能的影响。
- **整体意义**：本文指出缓存构建是关乎流式视频理解整体性能的关键环节，填补了现有研究中对缓存构建机制探索的空白。

## 2. 论文提出的方法论

- **方法名称**：Decoupled Streaming Cache（DSCache，解耦流式缓存）。
- **核心思想**：提出一种**免训练（training-free）**的缓存构建机制，将预训练好的离线视频模型适配到流式场景中，无需在长视频流上重新训练。
- **关键技术细节**：
  1. **累积过去缓存**：DSCache 维护一个累积的过去KV缓存，用于保留历史信息；
  2. **按需构建即时缓存**：同时按需构建一个独立的即时缓存（instant cache），并将其与过去的缓存**解耦**，目的是保留近期输入的信息量（informativeness），避免被历史信息淹没；
  3. **位置外推策略**：为了超越训练时的序列长度限制，DSCache 引入了一种**位置无关的编码策略**（position-agnostic encoding），确保KV缓存能够支撑未见过的位置（unseen positions），并**防止位置溢出**（position overflow）。
- **算法流程（文字描述）**：在处理流式输入时，DSCache 将历史信息累积在长期缓存中，对当前输入段构建独立的短期缓存，两者互不干扰；配合位置无关编码，使缓存在超出训练长度的位置下仍可正常计算注意力，从而支持无界流的持续推理。

## 3. 实验设计

- **数据集 / 场景**：使用 **Streaming Video QA benchmarks**（流式视频问答基准）作为主要评测场景。
- **对比方法**：与现有的流式视频理解方法（包括仅做缓存重用的方法）进行对比。
- **评测结果**：DSCache 在多个流式视频问答任务上取得了**最优性能（state-of-the-art）**，相较于此前的方法平均提升 **2.5% 准确率**。

## 4. 资源与算力

- 论文中**未明确提及**具体的GPU型号、数量、训练时长等算力资源信息。
- 需要指出的是，DSCache 本身是**免训练（training-free）**方法，因此其主要开销在于**推理阶段**的缓存管理和位置编码计算，而非训练成本；但文中并未给出具体的推理计算量或内存占用数据。

## 5. 实验数量与充分性

- 从现有信息来看，实验主要在 **Streaming Video QA benchmarks** 上进行，并报告了与多个基线方法的对比结果。
- 由于摘要中未详细列出每个子数据集的具体实验数量、消融实验（例如缓存解耦、位置无关编码的各自贡献）以及更细粒度的性能分析，**实验充分性信息不足**，难以全面判断其严谨程度。
- 不过，文章在多个benchmark上的**平均准确率提升**作为统一指标，且与现有方法进行对比，具备一定的客观性和可比性；但缺少关于驱逐策略组合、缓存规模敏感性等维度的进一步验证。

## 6. 论文的主要结论与发现

- DSCache 能够**有效支持无界视频流**的流式理解，且无需额外训练即可将离线模型适配到流式场景。
- **缓存构建**与缓存重用同等重要，将二者解耦能够显著提升流式视频理解性能。
- 位置无关编码策略有效解决了**长序列位置外推**和**位置溢出**问题，保证了缓存在未见过位置上的可用性。
- 实验表明，DSCache 相较现有方法在流式视频QA任务上取得了稳定的性能提升（平均 +2.5% 准确率），验证了该方法的有效性和通用性。

## 7. 优点

- **创新性**：首次在流式视频理解中系统性地研究缓存构建机制，而非只关注缓存重用。
- **免训练适配**：无需采集和标注无界视频流数据进行训练，显著降低了部署成本。
- **解耦设计**：将过去缓存与即时缓存分开维护，兼顾历史信息与近期信息的信息量，思路清晰合理。
- **位置外推**：考虑到了KV缓存在位置泛化上的技术难点，提供了一种简单有效的编码策略。
- **可迁移性**：缓存构建与驱逐的设计思路可类比到智能体工作流等场景中的缓存管理，具有跨领域借鉴价值。

## 8. 不足与局限

- **实验信息不够详细**：摘要中未列出具体数据集名称、消融实验内容、基线方法细节，难以全面评估实验的覆盖范围和严谨程度。
- **算力与部署成本未说明**：虽为免训练方法，但推理时的显存占用、时间开销、缓存规模上限等关键指标未给出数据。
- **缺乏消融验证**：未能确认"解耦缓存"和"位置无关编码"各自对性能的量化贡献。
- **基准范围有限**：目前验证集中于流式视频QA任务，是否适用于其他流式理解任务（如在线动作识别、实时视频监控等）仍待验证。
- **位置无关编码的潜在偏差**：位置无关策略在缓解位置溢出的同时，可能会在一定程度上损失位置信息带来的语义区分度，论文未讨论这一潜在权衡。

（完）
