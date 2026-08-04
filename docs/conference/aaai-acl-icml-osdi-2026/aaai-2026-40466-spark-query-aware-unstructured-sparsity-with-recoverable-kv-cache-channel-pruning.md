---
title: "SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning"
title_zh: SparK：查询感知的非结构化稀疏与可恢复KV缓存通道剪枝
authors: "Huanxuan Liao, Yixing Xu, Shizhu He, Guanchen Li, Xuanwu Yin, Dong Li, Emad Barsoum, Jun Zhao, Kang Liu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40466/44427"
tags: ["query:agent-cache"]
score: 4.0
evidence: 查询感知的KV缓存通道剪枝，可迁移至缓存驱逐但非面向智能体
tldr: 长上下文推理中，现有KV缓存压缩多沿时间轴进行token驱逐或合并，忽略了通道维度的重要性差异。SparK观察到通道显著性随查询和位置变化，提出查询感知的非结构化稀疏剪枝方法，并支持可恢复的通道剪枝。该方法能在保持精度的同时降低内存与计算开销，但并未面向智能体工作流或跨智能体缓存共享场景。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40466/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 885, \"height\": 269, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40466/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 566, \"height\": 447, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40466/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 878, \"height\": 487, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40466/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1831, \"height\": 496, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40466/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1840, \"height\": 1196, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40466/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1566, \"height\": 617, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40466/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 721, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40466/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 890, \"height\": 296, \"label\": \"Table\"}]"
motivation: 现有KV缓存压缩忽略通道维度的重要性变化，难以平衡效率与精度。
method: 通过查询感知的非结构化稀疏性识别重要通道，并设计可恢复的通道剪枝机制。
result: 在保持模型精度的前提下降低KV缓存内存与注意力计算开销。
conclusion: 利用查询与位置相关的通道显著性可实现更优的KV缓存压缩。
---

## Abstract
Long-context inference in large language models (LLMs) is increasingly constrained by the KV cache bottleneck: memory usage grows linearly with sequence length, while attention computation scales quadratically. Existing approaches address this issue by compressing the KV cache along the temporal axis through strategies such as token eviction or merging to reduce memory and computational overhead. However, these methods often neglect fine-grained importance variations across feature dimensions (i.e., the channel axis), thereby limiting their ability to effectively balance efficiency and model accuracy. In reality, we observe that channel saliency varies dramatically across both queries and positions: certain feature channels carry near-zero information for a given query, while others spike in relevance. To address this oversight, we propose SPARK, a training-free plug-and-play method that applies unstructured sparsity by pruning KV at the channel level, while dynamically restoring the pruned entries during attention score computation. Notably, our approach is orthogonal to existing KV compression and quantization techniques, making it compatible for integration with them to achieve further acceleration. By reducing channel-level redundancy, SPARK enables processing of longer sequences within the same memory budget. For sequences of equal length, SPARK not only preserves or improves model accuracy but also reduces KV cache storage by over 30% compared to eviction-based methods. Furthermore, even in an aggressive pruning ratio of 80%, SPARK maintains performance with less degradation than 5% compared to the based eviction method, demonstrating robustness and effectiveness. Our code will be available at \url{https://github.com/AMD-AIG-AIMA/AMD-Spark}.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与研究动机

- **背景**：长上下文推理已成为大语言模型（LLM）的重要应用场景，但 KV 缓存（Key-Value Cache）成为关键性能瓶颈——内存占用随序列长度线性增长，注意力计算随序列长度二次增长。例如，LLaMA3.1-8B 在 100K token 上下文时，KV 缓存超过 50GB，远超模型本身规模。
- **现有方法的不足**：已有 KV 压缩工作主要沿 **时间轴**（token 驱逐/合并）、**空间轴**（层/头剪枝）和**量化**方向展开，但这些方法往往忽略**通道维度**（feature channel）上的细粒度重要性差异。且现有通道剪枝方法（如 ThinK）采用**结构化均匀剪枝**，假设通道重要性在整个序列中保持一致。
- **关键观察**：通道显著性（channel saliency）随查询（query）和位置（position）剧烈变化。数据显示：
  - 不同 token 依赖不同的通道子集，呈高度非结构化稀疏模式；
  - 通道间变异系数（CV）平均超过 1.1，证明通道重要性是上下文敏感的；
  - 非结构化剪枝显著优于结构化剪枝（50% 剪枝率时性能损失 1.2% vs 4.2%；80% 时差距扩大至 27.4%）。

## 2. 方法论：SparK

### 2.1 核心思想

- 提出 **查询感知的非结构化通道剪枝**（Query-Aware Unstructured Channel Pruning），将通道剪枝重塑为**关键通道集合选择问题**，目标是最大化保留通道的总显著性贡献。
- 引入**可恢复机制**：不直接丢弃被剪通道，而是利用预填充阶段缓存的分布统计量，在注意力计算时动态重建被剪条目，缓解信息损失。

### 2.2 技术细节

- **通道显著性度量**：定义代理显著性分数 $w_{j,t}^i = \|q_{j,t}^i\|_2 \|k_{j,t}^i\|_2$，用于估计每个 token 每个通道对注意力机制的贡献。理论推导基于最小化剪枝前后注意力权重的 Frobenius 范数差异，在通道近似不相关的假设下，问题简化为逐 token 贪心选择 Top-T 通道。
- **掩码构建**：给定剪枝率 λ，保留 $T = \lfloor (1-\lambda)D \rfloor$ 个最重要通道，构造二元掩码 $S_i \in \{0,1\}^{S \times D}$。
- **计算优化**：为避免逐 token 计算查询向量的开销（对齐 SnapKV/ThinK），使用**局部观测窗口**（observation window）内查询向量的均值 $q_j^i$ 替代逐 token 查询向量计算显著性分数。
- **通道恢复函数 F**：利用预填充阶段存储的分布统计量（均值 μ、标准差 σ、被剪条目的均值 μ_pruned），从以下分布中采样近似分数值，并反推 key 条目：
  - **高斯分布**：$\tilde{w} \sim N(\mu_i, \sigma_i^2)$
  - **指数分布**：$\tilde{w} \sim \exp(1/\mu_i)$
  - **退化分布**（只保留均值）：$\tilde{w} = \mu_{i,\text{pruned}}$
  - 恢复的 key 条目计算为 $\tilde{k}_{j,t}^i = \tilde{w}_{j,t}^i / \|q_j^i\|_2$，以保持内积一致性。默认使用退化分布（消融实验显示其最稳定）。
- **扩展变体**：
  - **SparK-g**（分组剪枝）：将 D 个通道分为 g 组，按重要性施加渐进剪枝率；
  - **SparK-p**（Top-p 动态阈值）：保留累积重要性超过 99% 的通道，无需手动设定剪枝率。
  - 也可扩展至**价值（Value）缓存剪枝**（基于范数启发式）。
- **正交性**：SparK 与时间轴方法（SnapKV、PyramidKV 等）、量化方法正交，可无缝集成实现进一步加速。

## 3. 实验设计

### 3.1 数据集与基准

- **LongBench**：包含 16 个任务，覆盖单文档 QA、多文档 QA、摘要、少样本学习、合成任务、代码等 6 大类。
- **RULER**：专门评估长上下文检索与推理能力，包含 Niah、MKey、MValue、MQuery、VT、CWE、FWE、QA 等子任务。
- 使用 LLaMA-3/3.1-8B/70B-Instruct、Qwen3-8B/32B 等多种规模模型。

### 3.2 对比方法

- 全量 KV 缓存（Vanilla）；
- 时间轴压缩方法：StreamingLLM、SnapKV、PyramidKV、ExpectedAttention、TOVA；
- 通道剪枝方法：ThinK（结构化剪枝，作为主要对比对象）；
- 将 SparK/ThinK 分别与 SnapKV、PyramidKV 组合，在不同 KV 预算（128、512）和剪枝率（0.5、0.8）下进行对比。

### 3.3 主要定量结果

- **LongBench**（LLaMA-3-8B-Instruct）：
  - SparK(0.8) + SnapKV 相比 SnapKV 基线平均性能损失 < 5%；而 ThinK(0.8) + SnapKV 平均性能损失高达约 65%；
  - SparK(0.8) + PyramidKV 在多数任务上保持与 PyramidKV 基线相当的水平；
  - SparK 在不同 KV 预算（128/512）和剪枝率（0.5/0.8）下均显著优于 ThinK。
- **RULER**（20% KV 预算，16K 输入）：
  - ThinK(0.8) 平均性能低于 3%（接近崩溃）；SparK(0.8) 与基线 eviction 方法差距保持在 3% 以内；
  - SparK(0.5) 匹配或超过基线策略，优于 ThinK(0.5)。

### 3.4 分析实验

- **剪枝率影响**：SparK 在 40%–90% 剪枝率范围内始终优于 ThinK 和无恢复版本，尤其在 λ=0.8 时优势显著（性能下降 < 5%，ThinK 下降 > 35%）。
- **吞吐量**：SparK 在 8K–128K 输入长度下维持稳定推理速度，与 ThinK 吞吐相当（恢复步骤额外开销可忽略）；全量 KV 基线在 64K 以上内存溢出（OOM）。
- **内存-性能权衡**：SparK 在相同 KV 预算下性能最优；实现对 KV 缓存存储的 30%+ 缩减。
- **联合 KV 剪枝**：键+值同时剪枝（如 0.5+0.5 配置）相比单键剪枝平均性能损失仅约 0.35，极端配置（0.8+0.8）附加损失控制在 5% 以内。
- **恢复分布消融**：三种分布（高斯、指数、退化）性能接近，退化分布长序列最稳，指数分布短序列略优。
- **自适应变体消融**：SparK-p（阈值 99%）和 SparK-g（g=4/5）均匹配固定剪枝率基线性能，其中 g=4 在更低平均剪枝率（0.44）下取得更高性能。

## 4. 资源与算力

- 论文**未明确说明**所使用的 GPU 型号、数量、训练/推理时长或具体算力开销。
- 值得注意：SparK 是**训练免费**（training-free）方法，无需梯度更新或额外训练阶段；其额外开销主要在预填充阶段计算显著性分数（通过观测窗口均值向量降低开销）和推理阶段的恢复采样，论文通过吞吐量实验表明这部分开销可忽略。

## 5. 实验数量与充分性评估

- **实验数量**：较为充分。包含：
  - 2 个主流长上下文基准（LongBench 16 任务、RULER 13 类子任务）；
  - 5 个模型系列（LLaMA-3/3.1-8B/70B、Qwen3-8B/32B）；
  - 4 个基线对比方法 + 2 个集成方法（SnapKV、PyramidKV）交叉组合；
  - 3 组消融实验（恢复分布、自适应变体、KV 联合剪枝）；
  - 3 类分析实验（剪枝率、吞吐量、内存-性能权衡）。
- **公平性**：论文指出所有方法采用一致的超参数设置；ThinK 和 SparK 在相同剪枝率下对比，且与相同的 eviction 基线组合，确保对比公平。
- **中立评价**：实验覆盖范围较全，但仍有局限——主要依赖 LLaMA 和 Qwen 两个模型家族；RULER 实验仅在 8B 模型上报告完整结果；未报告方差/多次运行标准差；未与低秩方法（如 MLA、ShadowKV）和量化方法（如 KVQuant）做端到端对比。

## 6. 主要结论与发现

- 通道显著性在 token 维度上呈高度非结构化分布，结构化剪枝无法有效捕获这种动态性；
- **非结构化剪枝 + 通道恢复** 是在高剪枝率下保持模型性能的关键；
- SparK 在 80% 通道剪枝率（对应总 KV 缓存 40% 内存缩减）下，相比 eviction 基线方法性能损失 < 5%，而 ThinK 损失超过 65%；
- SparK 与时间轴压缩（SnapKV、PyramidKV）正交互补，可同时获得内存缩减与计算加速；
- 简单的退化分布（均值）恢复已足够稳健，说明核心收益来自“保留结构完整性”而非精确重建——将剪枝条目替换为低幅常数即可显著减少注意力分数失真。

## 7. 方法亮点

- **提出新范式**：首次将“非结构化通道剪枝 + 可恢复重建”引入 KV 缓存压缩，区别于 ThinK 的结构化剪枝；
- **理论严谨**：从组合优化问题出发，通过 Frobenius 范数展开和通道独立性假设，推导出简洁的贪心近似解；
- **即插即用、训练免费**：无需微调或重训练，可直接应用于任意现有 LLM；
- **正交兼容**：可与 token 驱逐、量化等技术联合使用，便于集成到现有推理系统；
- **计算开销低**：基于观测窗口均值查询向量计算显著性，恢复阶段仅需轻量采样；
- **通用性强**：在多个模型、多个基准、多个剪枝率下均表现稳定；
- **提供自适应变体**：SparK-p 和 SparK-g 免去人工调节剪枝率的麻烦。

## 8. 不足与局限

- **算力信息缺失**：论文未报告实验所用 GPU 型号、数量及总耗时，降低了复现便利性；
- **模型覆盖有限**：虽然验证了 5 个模型，但主要集中在 LLaMA-3/3.1 和 Qwen3 系列；未覆盖更广泛的架构（如 MoE、Mamba 等）；
- **RULER 实验报告不完整**：主表格仅报告 8B 模型的 20% KV 预算、16K 输入设置；
- **恢复机制的近似性**：退化分布（常数替换）本质是粗粒度近似，在极端剪枝率（>90%）或对精度极度敏感的任务上效果未知；
- **未与低秩/量化方法对比**：缺少与 MLA、ShadowKV、KVQuant 等方法在同一框架下的端到端对比；
- **缺少统计显著性检验**：未报告多次运行方差；
- **价值缓存剪枝较初步**：使用简单的范数启发式，未做与 key 剪枝同等的理论推导；
- **非面向智能体场景**：如元数据所示，本文方法主要面向通用长上下文推理加速，未涉及智能体工作流中的跨会话缓存共享或多轮工具调用等场景。

（完）
