---
title: Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective
title_zh: 基于统一信息论目标的KV缓存驱逐再思考
authors: "Jiaming Yang, Chenwei Tang, Liangli Zhen, Jiancheng Lv"
date: 2026-04-30
pdf: "https://openreview.net/pdf/0e5ae4ce50e149a18ac7db8356aa5b486bfcf616.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 面向缓存驱逐的统一信息论方法，可应用于智能体系统的缓存管理
tldr: 现有KV缓存驱逐策略多依赖经验启发式，缺乏理论指导。本文基于信息瓶颈原理，在线性-高斯注意力近似下推导出闭式互信息目标，刻画保留缓存子集的有效信息容量，并将多种已有策略统一为该目标的不同近似。基于此提出CapKV方法，在长上下文生成中显著提升推理效率与缓存利用率，为智能体等系统的缓存管理提供了通用可迁移的驱逐策略。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: KV缓存内存开销是长文本生成的关键瓶颈，现有驱逐策略缺乏理论基础。
method: 基于信息瓶颈原理推导互信息闭式目标，并据此提出统一的缓存驱逐方法。
result: 该方法能统一多种启发式策略，并提升长上下文生成中的缓存利用率。
conclusion: 从信息论角度重新定义KV缓存驱逐问题，为高效缓存管理提供了通用理论框架。
---

## Abstract
Key–value (KV) caching is essential for large language model inference, yet its memory overhead poses a critical bottleneck for long-context generation. Existing eviction policies predominantly rely on empirical heuristics, lacking a rigorous theoretical foundation. This work rethinks KV cache eviction through the lens of the Information Bottleneck principle. Under a linear–Gaussian surrogate of attention, we derive a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset. This formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle. Guided by this insight, we introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores. This approach replaces heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal. Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity.

---

## 论文详细总结（自动生成）

# 基于统一信息论目标的KV缓存驱逐再思考——论文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **研究背景**：键值（Key-Value, KV）缓存是大语言模型（LLM）推理的关键组件，但其内存开销随着上下文长度增长而急剧膨胀，成为长上下文生成的主要瓶颈。
- **核心问题**：现有KV缓存驱逐（eviction）策略大多依赖经验性启发式规则（如基于注意力分数、频率等），缺乏严格的理论基础，导致缓存利用率与生成质量之间的权衡难以得到系统性的分析与优化。
- **整体意义**：本文首次从信息论视角重新审视KV缓存驱逐问题，将“保留哪些KV对”这一工程问题抽象为“最大化保留缓存子集的有效信息容量”的理论问题，为高效缓存管理提供了统一的理论框架，而非就事论事的修补方案。

## 2. 方法论：核心思想、关键技术细节与算法流程

- **核心思想——信息瓶颈（Information Bottleneck, IB）原理**：将KV缓存驱逐视为一个有损压缩问题，目标是找到一个保留子集，使其在压缩原始缓存的同时，最大化与后续生成预测相关的互信息（Mutual Information）。
- **线性-高斯近似下的闭式目标**：在线性-高斯注意力替代模型（linear–Gaussian surrogate of attention）的假设下，作者推导出了互信息目标的闭式解。该闭式表达式刻画了保留KV缓存子集所能承载的“有效信息容量”，从而给出了一个可计算、可优化的驱逐准则。
- **统一解释已有策略**：该公式化框架揭示了一个重要事实——现有多种启发式驱逐策略（如基于注意力分数、基于范数、基于频率等的策略）实际上都可以被解释为同一个“容量最大化”原则的不同近似形式。这使得看似零散的经验方法被统一到一个理论伞下。
- **CapKV方法**：
  - 直接以信息保留为目标，使用**对数行列式近似（log-determinant approximation）** 来计算信息容量；
  - 结合**统计杠杆分数（statistical leverage scores）** 来高效近似该目标，使得方法在计算上可行；
  - 用理论驱动的选择机制替代启发式选择，在驱逐KV对时保留最大化的预测信号。
- **算法流程（文字说明）**：(1) 根据当前上下文和注意力结构构造线性-高斯近似模型；(2) 计算各KV候选的统计杠杆分数，近似其对互信息目标的边际贡献；(3) 在预算约束下迭代保留贡献最大的子集；(4) 生成过程中动态维护该子集。

## 3. 实验设计：数据集、基准与对比方法

- **数据集/场景**：元数据仅指明使用了“多种长上下文基准”（long-context benchmarks），未给出具体数据集名称（如LongBench、RULER等是否包含在内尚不明确）。
- **模型覆盖**：实验在“多种模型”（multiple models）上进行，说明结论具有一定跨模型泛化性，但具体模型列表（如LLaMA系列、Mistral等）未在元数据中列出。
- **对比方法**：与“先前方法”（prior methods）进行比较，包括各类已有的启发式驱逐策略。由于本文的统一框架已将多种已有策略纳入同一理论体系，对比应涵盖这些代表性基线（如H2O、StreamingLLM、Scissorhands等，具体名单未在给定材料中列出）。

## 4. 资源与算力

- **未明确说明**：给定材料（包括元数据和摘要）中**没有提及**任何具体算力信息——包括GPU型号与数量、训练/推理时长、显存占用等。
- **推测性说明**：考虑到是ICML 2026录用论文且涉及长上下文推理，大概率使用了商用GPU集群（如A100/H100），但这一信息无法从现有材料中确认，属于缺失信息项。

## 5. 实验数量与充分性

- **实验数量**：元数据描述为“跨多种模型和多个长上下文基准的广泛实验”（extensive experiments），但从现有材料中**无法得知具体的实验组数**——不知道涉及多少个数据集、多少组消融实验、多少次重复运行。
- **充分性评估**：
  - 从范围上看，覆盖多模型、多基准是加分项，说明方法有一定泛化能力；
  - 但具体消融实验（如对数行列式近似的贡献、杠杆分数的效率优势、不同预算下的表现）是否有系统性验证，在现有材料中缺乏证据；
  - **客观性提示**：无法核实对比实验是否使用了相同的上下文长度、相同的解码设置、相同的评估指标等，因此公平性只能以论文被ICML录用作为间接保证。

## 6. 主要结论与发现

- **理论结论**：KV缓存驱逐可以统一为一个信息容量最大化问题；多种已有启发式策略是该统一原则的近似特例。
- **方法结论**：CapKV在保留预测信号方面优于启发式方法，实现了更好的内存效率与生成保真度（generational fidelity）之间的权衡。
- **实践意义**：为长上下文LLM推理提供了理论驱动、可迁移的缓存管理方案，不依赖于特定模型架构的直觉设定。

## 7. 优点

- **理论创新性强**：首次将信息瓶颈原理系统性地引入KV缓存驱逐问题，填补了该领域缺乏理论基础的空白。
- **统一视角具有解释力**：将看似庞杂的启发式策略统一到同一理论框架下，不仅解释了“为什么它们有效”，还为改进提供了方向。
- **方法可操作**：闭式互信息目标与杠杆分数近似使得理论目标可以在实际推理中高效计算，不是纸上谈兵。
- **应用场景广**：对智能体系统、长文档问答、多轮对话等依赖长上下文的应用场景均有缓存管理的借鉴价值。
- **评估维度全面**：同时关注内存效率与生成质量两个维度，而非单方面优化。

## 8. 不足与局限

- **信息缺失**：给定材料中缺乏具体数据集、模型列表、基线方法清单、消融实验细节，无法对实验充分性做出完整判断。
- **算力信息空白**：未提供任何资源开销数据（GPU数量、时间成本等），读者难以评估该方法在实际部署中的成本门槛。
- **理论假设的适用边界**：线性-高斯注意力近似虽然在数学上提供了可解性，但真实注意力机制是非线性的，该近似的适用范围（如对不同层、不同头、不同长度下的有效性）需要在论文正文中加以验证；从现有材料看，这一边界条件未被充分讨论。
- **长期依赖场景的潜在风险**：信息容量最大化在理论上是最优的，但在极端长上下文中，早期信息的信息量衰减问题是否会导致“核心记忆”被过早驱逐，仍需进一步验证。
- **未见多语言/多模态验证**：若仅限英文文本基准，泛化性证据仍有不足。

（完）
