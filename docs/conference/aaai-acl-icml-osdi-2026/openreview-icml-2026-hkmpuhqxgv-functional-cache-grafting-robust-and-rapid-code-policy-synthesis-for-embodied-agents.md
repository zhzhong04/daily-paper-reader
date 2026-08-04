---
title: "Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents"
title_zh: 功能缓存嫁接：面向具身智能体的稳健快速代码策略合成
authors: "Saehun Chun, Wonje Choi, Sera Choi, Sanghyun Ahn, Honguk Woo"
date: 2026-04-30
pdf: "https://openreview.net/pdf/e6cbcea9f9e647f6863524749cc0e7f8e7a6545b.pdf"
tags: ["query:awc"]
score: 9.0
evidence: 缓存函数级代码骨架及对应的Transformer KV缓存，直接面向具身智能体工作流的缓存
tldr: 具身智能体策略生成受长提示重复预fill和完全生成式解码鲁棒性差的限制。FCGraft提出功能缓存嫁接框架，维护函数级验证代码骨架及其提示级Transformer KV缓存库，并通过嫁接复用避免重复预fill。实验表明该方法能够加速策略合成并提升API匹配、安全防护等鲁棒性，为智能体工作流中的缓存调度提供了直接范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 具身智能体代码策略生成受长提示重复预fill和解码鲁棒性限制。
method: 构建函数级代码骨架及关联的Transformer KV缓存库，通过缓存嫁接复用加快生成并提高鲁棒性。
result: 在多种具身环境任务上提升了生成速度与代码策略鲁棒性。
conclusion: 功能缓存为智能体工作流缓存调度提供了具体技术路径。
---

## Abstract
Code-writing large language models (CodeLLMs) generate executable code policies for embodied agents by translating natural language goals and environmental constraints into structured control programs. However, policy generation in open-domain embodied environments suffers from two fundamental limitations:
(i) delayed decoding caused by repetitive prefill computation over long prompts, and
(ii) limited robustness due to fully generative decoding, which often produces API mismatches, missing safety guards, and unstable control logic. To address these limitations, we present FCGraft, a Functional Cache Grafting framework.
FCGraft maintains a library of function-level validated code skeletons and their associated prompt-level Transformer key–value (KV) caches, and synthesizes new policies by retrieving relevant functions and grafting their KV caches when a new task is provided. Given retrieved function caches, FCGraft performs cache grafting via stitching, which composes cached function segments into a composite policy, and patching, which locally adapts only the necessary code regions to satisfy task-specific parameters and constraints with minimal additional decoding. By eliminating redundant prefill computation, this approach reduces generation latency, while reusing validated control structures improves robustness over prompt-level caching methods RAGCache, achieving $18.31\$% higher task success rate and $2.3\times$ faster policy synthesis.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- 本文针对**具身智能体（embodied agents）** 的代码策略生成问题：利用代码大语言模型（CodeLLMs）将自然语言目标和环境约束转化为可执行的控制程序。
- 现有方法在**开放域具身环境**中存在两个根本性缺陷：
  1. **解码延迟高**：长提示（long prompts）需要反复进行 prefill 计算，导致冗余计算和响应缓慢。
  2. **鲁棒性差**：完全生成式解码（fully generative decoding）容易产生 API 不匹配、缺少安全防护、控制逻辑不稳定等问题。
- 核心意义：如何在不牺牲鲁棒性的前提下，大幅提升代码策略合成的速度，是具身智能体实际部署的关键挑战。

## 2. 方法论：核心思想、关键技术细节与算法流程

- **总体框架**：提出 **FCGraft（Functional Cache Grafting，功能缓存嫁接）** 框架。
- **核心思想**：构建一个**函数级验证代码骨架库**，并为每个骨架保存**提示级 Transformer 键值（KV）缓存**。当新任务到来时，检索相关函数并直接“嫁接”其 KV 缓存，从而避免重复的 prefill 计算。
- **关键技术细节**：
  - **库构建**：维护函数级、已验证的代码骨架及其对应的 prompt 级 KV 缓存。
  - **检索机制**：给定新任务，检索相关函数缓存。
  - **嫁接操作**：
    - **拼接（stitching）**：将缓存的函数段组合成一个复合策略。
    - **修补（patching）**：仅对必要的代码区域进行局部调整，以满足任务特定参数和约束，所需额外解码量最小化。
- **算法流程（文字描述）**：
  1. 输入新任务自然语言描述与环境约束；
  2. 从函数缓存库中检索匹配的函数骨架；
  3. 通过拼接和修补操作融合缓存片段，生成完整策略；
  4. 仅对少量区域进行解码，输出最终代码。

## 3. 实验设计

- **数据集/场景**：论文摘要中未具体列出数据集名称，但提到“多种具身环境任务”，属于**开放域具身环境 benchmark**。
- **对比方法**：主要与 **RAGCache**（一种提示级缓存方法）进行对比。
- **评价指标**：
  - 任务成功率（Task Success Rate）
  - 策略合成速度（Policy Synthesis Speed）
- **实验规模**：摘要未给出具体实验数量或场景个数，仅报告了整体平均结果。消融实验等细节未在提供文本中说明。

## 4. 资源与算力

- 论文提供的文本中**未明确提及 GPU 型号、数量、训练时长、推理环境等资源信息**。
- 仅能从“Transformer KV 缓存”推断使用了基于 Transformer 结构的 CodeLLM，但具体模型规模（如参数数量、是否微调）未说明。
- 因此，算力相关细节目前无法从给定内容中获取。

## 5. 实验数量与充分性

- 由于只提供了摘要，**无法判断具体实验组数**（例如涉及多少任务、多少环境、多少随机种子）。
- 从摘要信息看，仅提供了与 RAGCache 的一个对比结果（成功率 +18.31%，速度提升 2.3 倍），**缺少与更多基线（如完全生成式 baseline、其他缓存方法）的对比**。
- 未提及消融实验（例如缝合 vs 修补各自贡献、检索准确性影响等），所以**实验充分性尚不明确**；不过作为 ICML 2026 接收论文，可能存在完整实验，但当前文本不足以评估其公平性和客观性。

## 6. 主要结论与发现

- **FCGraft 能有效消除冗余 prefill 计算**，从而显著降低策略生成延迟。
- **复用已验证的控制结构**相比提示级缓存方法（RAGCache）能大幅提升鲁棒性：
  - 任务成功率提高 **18.31%**；
  - 策略合成速度提升 **2.3 倍**。
- 验证了“函数级缓存嫁接”在具身智能体代码策略合成中的有效性和可行性。

## 7. 优点

- **创新性强**：从函数级粒度结合 KV 缓存，突破传统 prompt 级缓存的粗粒度局限。
- **直击痛点**：同时解决预填充延迟和完全生成式解码的鲁棒性问题，兼顾速度与质量。
- **实用主义设计**：拼接与修补结合，只解码必要代码区域，降低计算开销。
- **成果显著**：在速度和成功率上均实现大幅提升，证明方法具有实际应用前景。

## 8. 不足与局限

- **信息不完整**：仅基于摘要，缺乏方法细节、公式、算法伪代码、模型架构等关键信息。
- **基线对比有限**：仅与 RAGCache 对比，未与更多 SOTA 方法（如长提示缓存、模块化生成、少样本提示等）比较。
- **实验覆盖不详**：未说明具体任务类型、难度、机器人形态、感知复杂度等，开放域泛化能力未知。
- **潜在偏差风险**：KV 缓存嫁接的召回率和函数库覆盖度严重依赖检索器质量；如果函数库不足或检索偏差，可能影响公平性。
- **应用限制**：需要预构建验证代码骨架库，这要求前期人工或自动标注成本；同时只能适用于具有明确函数边界的控制程序，对其他代码生成任务可能不通用。
- **硬件与可复现性**：未提供资源消耗和配置，无法评估其在不同算力环境下的可推广性。

（完）
