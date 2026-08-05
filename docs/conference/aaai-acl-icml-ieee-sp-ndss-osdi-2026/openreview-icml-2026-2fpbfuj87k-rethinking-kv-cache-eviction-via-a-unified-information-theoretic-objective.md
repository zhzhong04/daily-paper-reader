---
title: Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective
title_zh: 通过统一信息论目标重新思考KV缓存驱逐
authors: "Jiaming Yang, Chenwei Tang, Liangli Zhen, Jiancheng Lv"
date: 2026-04-30
pdf: "https://openreview.net/pdf/0e5ae4ce50e149a18ac7db8356aa5b486bfcf616.pdf"
tags: ["query:awc"]
score: 6.0
evidence: 提出统一的KV缓存驱逐信息论目标，可迁移至智能体系统
tldr: KV缓存是LLM推理的关键，但内存开销是长上下文生成的瓶颈。现有驱逐策略多依赖经验启发，缺乏严格理论基础。本文从信息瓶颈原理重新思考KV缓存驱逐，在注意力的线性-高斯代理下推导出封闭形式的互信息目标，刻画保留KV子集的有效信息容量。该公式表明多种现有驱逐策略可视为同一容量最大化原则的不同近似，并据此提出CapKV策略，为长上下文推理提供更可靠的缓存驱逐基础。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有KV缓存驱逐策略缺乏理论根基，多依赖经验启发性规则。
method: 基于信息瓶颈原理推导线性-高斯注意力代理下的封闭式互信息目标，并据此提出CapKV驱逐策略。
result: 揭示了多种现有策略实为同一容量最大化原则的近似，CapKV提供了更严格的理论基础。
conclusion: 信息论视角统一了KV缓存驱逐策略，为长上下文场景的缓存管理奠定了理论基础。
---

## Abstract
Key–value (KV) caching is essential for large language model inference, yet its memory overhead poses a critical bottleneck for long-context generation. Existing eviction policies predominantly rely on empirical heuristics, lacking a rigorous theoretical foundation. This work rethinks KV cache eviction through the lens of the Information Bottleneck principle. Under a linear–Gaussian surrogate of attention, we derive a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset. This formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle. Guided by this insight, we introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores. This approach replaces heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal. Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 论文的核心问题与整体含义
- **研究动机**：KV（键值）缓存是大型语言模型（LLM）推理中不可或缺的机制，但其内存开销随上下文长度急剧增长，成为长上下文生成的主要瓶颈。为缓解该问题，现有工作提出多种 KV 缓存驱逐（eviction）策略，即主动丢弃部分缓存条目以节省内存。
- **核心问题**：现有驱逐策略大多基于经验性启发式规则（如按注意力分数、位置频率等），缺乏统一且严格的理论基础，导致其在不同场景下的有效性难以保证，也阻碍了进一步的理论优化。
- **整体含义**：本文尝试从根本上回答“应该保留哪些 KV 缓存子集”这一问题，借助信息瓶颈（Information Bottleneck, IB）原理构建统一的理论框架，将缓存驱逐重新定义为信息容量最大化问题，从而为长上下文推理中的缓存管理提供可解释、可推广的指导原则。

## 2. 论文提出的方法论
- **核心思想**：从信息论角度重新审视 KV 缓存驱逐问题。给定已产生的上下文及其对应的 KV 状态，目标是寻找一个保留子集，使其在预测未来 token 时保留最大的“有效信息”。这一思想与信息瓶颈原理高度契合——在压缩/丢弃信息的同时，最大化与目标任务相关的信息。
- **关键技术细节**：
  - 采用注意力机制的**线性-高斯代理模型**（linear–Gaussian surrogate），将注意力计算近似为高斯过程，从而使得互信息（mutual information）具有可解析的封闭形式表达式。
  - 在该代理下，推导出保留缓存子集与预测信号之间的互信息封闭解，该解刻画了子集的“有效信息容量”，即保留哪些 KV 条目能最有效地支持后续生成。
  - 通过分析该互信息目标，论文揭示：多种现有驱逐策略（例如按注意力分数、随机采样、位置启发式等）本质上都可被解释为同一“容量最大化”原则的不同近似或不同约束条件下的特例。
- **算法流程（文字说明）**：
  1. 构建注意力线性-高斯代理，将查询、键、值映射为随机变量；
  2. 推导保留缓存子集的互信息目标函数；
  3. 基于该目标，提出 **CapKV（Capacity-aware KV eviction）** 策略；
  4. CapKV 使用**对数行列式（log-determinant）近似**，并借助**统计杠杆分数（statistical leverage scores）** 高效估计保留子集对信息容量的贡献；
  5. 在每一步驱逐时，优先保留使信息容量损失最小的键值条目，从而替代纯启发式选择。

## 3. 实验设计
- 由于原始摘要未详细列出具体数据集与 benchmark 名称，无法给出精确清单。但根据摘要所述：
  - **场景**：长上下文生成任务，涉及多个模型和多个长上下文基准（long-context benchmarks）。
  - **对比方法**：与若干现有的 KV 缓存驱逐策略进行对比，包括基于启发式的典型方法（大概率包括如 H2O、StreamingLLM、Scissorhands 等常见方法，但原文未明确点名）。
  - **评估指标**：重点考察内存效率与生成保真度（generational fidelity）之间的权衡，同时可能包含推理速度、召回率等指标。
- **数据集/模型**：摘要未给出具体模型规模与数据集名称，需结合原文补全。

## 4. 资源与算力
- 论文摘要中**未明确提及**所使用的 GPU 型号、数量、训练或推理时长等算力资源信息。
- 可能的原因包括：该研究主要聚焦于推理阶段的缓存策略，不涉及大规模训练；或者相关细节仅在论文正文或附录中描述。因此在当前可见信息范围内，无法评估其算力成本。

## 5. 实验数量与充分性
- **实验数量**：摘要仅提到“跨多个模型和多个长上下文基准”进行了“大量实验”，但未给出具体实验组数。
- 从摘要描述看，实验至少包括：
  - 多个不同规模的 LLM（模型数量应≥2）；
  - 多个长上下文 benchmark（应≥3，以覆盖不同任务类型）；
  - 与多种现有驱逐策略的对比；
  - 很可能包含针对不同内存预算（缓存保留比例）的敏感性分析。
- **充分性与公平性**：在摘要层面无法判断实验细节是否完整。若正文包含消融实验（无消融、不同近似方式对比）以及不同上下文长度下的测试，则可认为较为充分。但作者没有在摘要中明确列出消融和基线集合，因此不能断定其全面性。从“一致优于先前方法”的结论来看，至少在其测试的配置下是充分的，但可能存在未覆盖的极端长上下文或更复杂任务的风险。

## 6. 论文的主要结论与发现
- 提出了 KV 缓存驱逐的统一信息论目标，该目标基于信息瓶颈原理，具有严格的理论推导。
- 证明了多种现有 KV 缓存驱逐策略本质上都是该统一目标的不同近似，从而统一了看似分散的启发式方法。
- 基于这一理论，提出了 CapKV 方法，利用对数行列式和统计杠杆分数直接优化信息保留，避免了启发式选择的主观性。
- 实验表明，CapKV 在多个模型和长上下文基准上优于以往方法，实现了内存效率与生成质量之间更好的平衡。

## 7. 优点
- **理论贡献显著**：为原本经验驱动的 KV 缓存驱逐提供了清晰的信息论解释，建立了统一目标框架，增强了可解释性。
- **方法具有普适性**：统一目标能够覆盖多种现有策略，说明框架具有较高的抽象能力和推广潜力。
- **计算高效**：使用对数行列式和统计杠杆分数进行近似，避免了复杂的全局优化，适合在线推理场景。
- **实验验证充分**（若正文详细）：涵盖多模型、多基准，且与多种基线对比，结论具有说服力。

## 8. 不足与局限
- **信息可见性受限**：当前摘要中缺少实验细节（数据集、模型规模、基线名称、消融实验等），无法对实验的全面性和公平性做出完全判断。
- **线性-高斯代理的适用性**：该方法依赖注意力线性-高斯代理假设，真实注意力机制非线性且非高斯，代理模型可能与实际分布存在偏差；在极端长上下文或非标准注意力结构（如稀疏注意力、线性注意力）下，其有效性需额外验证。
- **信息瓶颈目标的近似误差**：log-determinant 近似和杠杆分数可能在高维或病态协方差矩阵下不够精准，影响驱逐决策。
- **未讨论算力开销**：没有提及该策略本身的运行时开销，以及相对于被节省的内存是否在整体推理效率上始终占优。
- **局限性**：主要针对推理阶段的缓存管理，未考虑训练阶段；对 KV 缓存量化、联合压缩等其他内存优化技术的结合可能性尚未讨论。

（完）
