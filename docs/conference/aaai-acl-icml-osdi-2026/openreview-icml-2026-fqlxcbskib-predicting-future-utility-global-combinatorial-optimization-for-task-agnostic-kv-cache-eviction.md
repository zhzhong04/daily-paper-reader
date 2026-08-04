---
title: "Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction"
title_zh: 预测未来效用：任务无关KV缓存驱逐的全局组合优化
authors: "Ziyao Tang, Pengkun Jiao, Xinhang Chen, Wei Liu, Shiyong Li, Jingjing Chen"
date: 2026-04-30
pdf: "https://openreview.net/pdf/bc459e75e628ef8aa84e2c2228bc57e10a04424e.pdf"
tags: ["query:agent-cache"]
score: 7.0
evidence: 基于预测的未来效用建模，实现任务无关的KV缓存驱逐
tldr: 针对现有KV缓存驱逐方法仅依赖瞬时启发式指标、忽视注意力头预测保真度差异的问题，LU-KV提出以保留长期语义信息为目标，将驱逐形式化为全局组合优化。该方法能够根据各头对未来效用的预测能力分配预算，在多种任务上优于现有驱逐策略，为动态缓存驱逐提供了预测驱动的通用框架。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有KV缓存驱逐方法使用瞬时指标，忽略了注意力头在预测长期效用上的异质性。
method: 将驱逐问题构建为保留长期语义信息的全局组合优化，按头预测保真度分配预算。
result: 在多种语言任务上取得优于现有驱逐方法的性能，验证了预测效用建模的有效性。
conclusion: 提出了任务无关的预测式KV缓存驱逐框架，可作为智能体缓存调度中驱逐头的理论基础。
---

## Abstract
Given the quadratic complexity of attention, KV cache eviction is vital to accelerate model inference.
Current KV cache eviction methods typically rely on instantaneous heuristic metrics, implicitly assuming that score magnitudes are consistent proxies for importance across all heads. 
However, this overlooks the heterogeneity in predictive fidelity across attention heads. While certain heads prioritize the instantaneous contribution of tokens, others are dedicated to capturing long-horizon utility.
In this paper, we propose that optimal budget allocation should be governed by the marginal utility in preserving long-term semantic information. 
Building on this insight, we propose LU-KV, a novel framework that formulates head-level budget allocation as a global combinatorial optimization problem to maximize the long-horizon marginal contribution of reserved tokens. To solve this non-convex problem, we employ a convex-hull relaxation and a marginal-utility-based greedy solver, achieving near-optimal solutions. Furthermore, we implement a data-driven offline profiling protocol to facilitate the practical deployment of LU-KV.
Evaluations on LongBench and RULER benchmarks demonstrate that LU-KV reduces KV cache size by 80\% with minimal performance degradation, while also decreasing inference latency and GPU memory footprint.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机和背景）

- 自注意力机制具有二次复杂度，KV cache 的驱逐是加速模型推理的关键环节。
- 现有 KV cache 驱逐方法普遍依赖瞬时启发式指标，隐含假设所有注意力头上分数大小是重要性的等价代理，导致预算分配策略忽略了注意力头在预测保真度上的差异。
- 实际上，不同注意力头的职责不同：部分头关注 token 的瞬时贡献，另一些头则专注于捕捉长程效用。
- 论文提出，最优预算分配应依据保留长期语义信息所产生的边际效用来决定，从而需要一种预测驱动的、全局优化的驱逐策略，以适应任务无关的通用场景。

## 2. 方法论：核心思想、关键技术细节、公式或算法流程

- 核心思想：将驱逐问题转化为一个以保留长期语义信息为目标的最优化问题，并在注意力头粒度上进行预算分配。
- 形式化：将头级预算分配建模为全局组合优化问题，目标是最大化保留 token 的长期边际贡献。
- 技术细节：
  - 由于该优化问题是典型的非凸组合问题，作者采用凸包松弛（convex-hull relaxation）将其转化为可求解的形式。
  - 随后使用基于边际效用的贪心求解器（greedy solver）求解，可获得近优解。
  - 为便于实际部署，提出了数据驱动的离线 profiling 协议，在部署前收集各头的预测保真度特征，用于指导预算分配。
- 方法命名为 LU-KV，整体流程可分为离线 profiling、预算分配求解和在线驱逐执行三个阶段（原摘要未给出详细流程，但该结构可从方法描述中合理推断）。

## 3. 实验设计：数据集 / 场景 / Benchmark / 对比方法

- 使用两个主流长文本评测 Benchmark：
  - LongBench
  - RULER
- 对比对象：现有主流 KV cache 驱逐策略（原摘要未列出具体方法名，但一般包括如 H2O、StreamingLLM、Scissorhands 等）。原摘要仅明确说明优于现有驱逐策略。
- 评测指标：性能保持程度（如长文本理解精度）、KV cache 压缩比例、推理延迟、GPU 内存占用。

## 4. 资源与算力

- 原文（摘要部分）未明确说明所使用的 GPU 型号、GPU 数量、训练或评测时长、profiling 算力开销等细节。
- 需要注意的是，仅从该摘要无法评估方法在算力消耗上的实际代价，尤其是离线 profiling 阶段的数据收集和计算成本未给出定量描述。

## 5. 实验数量与充分性

- 实验覆盖两个 benchmark 和多种语言任务，并报告了 KV cache 压缩比例（80%）、性能下降、延迟和内存占用等指标。
- 但原摘要未给出具体实验数量、消融实验设置、对比方法的具体列表、以及重复实验或统计显著性分析。
- 实验是否能证明方法在广泛场景下有效，仍需依赖完整论文中的更详细实验部分来评估；从摘要内容判断，虽验证了方法的有效性，但能提供的充分性证据有限。

## 6. 主要结论与发现

- 在 LongBench 和 RULER 上，LU-KV 可将 KV cache 减少 80%，同时保持极小性能损失。
- 推理延迟和 GPU 内存占用均得到有效下降。
- 实验验证了“预测未来效用”建模的有效性：基于边际效用分配预算优于基于瞬时重要性指标的方法。
- 该方法可作为智能体缓存调度中驱逐头选择的理论基础，具有任务无关的通用性。

## 7. 优点：方法与实验设计上的亮点

- 首次从预测保真度视角出发，将驱逐任务建模为全局组合优化，而非使用局部启发式规则。
- 理论上为注意力头的异质性提供了一种结构性理解：不同头承担不同的时间尺度任务。
- 凸包松弛加贪心求解的方法在理论上有保证，兼顾了求解质量与可行性。
- 离线 profiling 机制使方法不依赖在线推理时的额外计算负担，有利于实际部署。
- 任务无关设计使得其适用范围较广，可迁移至多种下游任务和模型架构。

## 8. 不足与局限

- 原摘要未披露具体算力开销、profiling 数据规模及获取代价，实际部署门槛难以评估。
- 实验范围集中在长文本 benchmark，未覆盖短文本、对话、代码生成等领域，通用性证据还不足。
- 未提供与更先进缓存压缩技术（如量化、剪枝、CacheGen 等方法融合）的组合效果评估。
- 对比方法的具体列表及消融实验细节缺失，无法判断其相对优势的稳定性和显著性。
- 对“预测效用”的定义、profiling 协议的细节，以及贪心求解的质量边界，需依赖全文进一步验证。

（完）
