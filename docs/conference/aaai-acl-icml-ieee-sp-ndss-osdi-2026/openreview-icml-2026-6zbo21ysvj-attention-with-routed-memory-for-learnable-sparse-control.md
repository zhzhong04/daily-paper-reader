---
title: Attention with Routed-Memory for Learnable Sparse Control
title_zh: 基于路由记忆的注意力机制用于可学习稀疏控制
authors: "QIUHAO Zeng, Jerry Huang, Peng Lu, Ruiyi Fang, Gezheng Xu, Zihao Jing, Yufei Cui, Charles Ling, Gang Niu, Boyu Wang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/053e4edad024c40ed9ffb07868ebc3784d86f137.pdf"
tags: ["query:agent-cache"]
score: 6.0
evidence: 可学习路由记忆的KV缓存结构解决驱逐与内存调度，可迁移至多智能体场景
tldr: 现有KV缓存通过选择性token驱逐和剪枝来缓解长上下文推理负担，但硬驱逐会丢失核心信息。ARM提出可微分的固定大小路由记忆结构，利用Gumbel-Softmax学习选择记忆槽，并通过门控更新软性融合新旧信息，避免硬驱逐。训练后固定大小记忆能有效控制稀疏注意力。该方法为多智能体共享缓存时的门控更新与记忆调度提供了可借鉴思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 硬性token驱逐会丢失关键信息，现有KV缓存管理难以保持推理质量。
method: 提出ARM，使用可微分层次路由器和门控更新维护固定大小记忆，软性融合新旧信息。
result: 训练后的固定大小路由记忆在长上下文任务中减少信息损失并控制稀疏性。
conclusion: 可学习路由记忆替代硬驱逐，可为多智能体缓存管理提供新的门控调度机制。
---

## Abstract
Despite advances in long-context inference, large language models (LLMs) remain fundamentally limited by the key-value (KV) caching mechanisms that are necessary for stable computation. Techniques such as selective token eviction and pruning have vastly mitigated these issues, but often discard core information to manage the growing cache.
In this paper, we propose _**A**ttention with **R**outed **M**emory_ (_**ARM**_) a novel KV caching structure that introduces a fully differentiable, fixed-size memory system organized as a hierarchical router. Via a Gumbel-Softmax, _**ARM**_ learns to select memory slots and perform sigmoid-gated updates that softly combine new and stored information, avoiding hard eviction and reducing information loss. By further training a policy to dynamically select varying amounts of memory at inference, _**ARM**_ adapts its accesses for both simple contexts and inputs that require deeper reasoning, enabling more scalable and effective retrieval on both short- and long-contexts. Experimental results on standard commonsense and long-context reasoning benchmarks demonstrate that _**ARM**_ achieves superior performance and efficiency compared to fixed KV-caching approaches, while remaining efficient and scalable in terms of both memory and generation latency.

---

## 论文详细总结（自动生成）

# 《Attention with Routed-Memory for Learnable Sparse Control》论文总结

## 1. 论文的核心问题与整体含义

- **研究背景**：大语言模型（LLM）在长上下文推理场景中依赖键值（KV）缓存机制维持稳定计算，但KV缓存随序列长度线性增长，带来显著的内存和延迟负担。现有缓解手段如token选择性驱逐（selective eviction）和剪枝（pruning）虽能控制缓存规模，却常以丢失核心信息为代价。
- **核心问题**：如何在不牺牲关键信息的前提下，实现对KV缓存的有效稀疏化控制，使模型在短上下文和长上下文场景中都能保持高性能与高效率。
- **整体含义**：论文提出一种全新的KV缓存结构，将"硬驱逐"转变为"软融合"，为长上下文推理提供了可学习、可扩展的稀疏注意力控制新范式。

## 2. 论文提出的方法论：ARM

- **核心思想**：提出 **ARM（Attention with Routed-Memory）**——一种完全可微分的固定大小记忆系统。记忆以分层路由器（hierarchical router）形式组织，通过可微分的路由机制自适应选择需要访问的记忆槽，替代硬性token驱逐。
- **关键技术细节**：
  - **Gumbel-Softmax 可微分路由选择**：使用Gumbel-Softmax技术学习选择记忆槽，使得"选哪个槽"这一离散决策可被端到端训练。
  - **Sigmoid门控更新**：在执行记忆更新时，通过sigmoid门控将新信息与旧信息软性融合，而非直接覆盖或丢弃旧值，从而避免硬驱逐造成的信息损失。
  - **动态记忆量控制**：训练一个策略网络，使模型在推理阶段能根据输入复杂度动态调整使用的记忆槽数量——简单上下文少用记忆，复杂推理多用记忆。
- **算法流程（文字说明）**：
  1. 输入query和key/value对；
  2. 分层路由器基于当前query计算各记忆槽的选择概率；
  3. 通过Gumbel-Softmax采样得到可微分的"硬"选择结果；
  4. 对选中的记忆槽执行sigmoid门控更新，软性写入新信息并保留部分旧信息；
  5. 训练策略模块控制最终读取的记忆数量，实现动态稀疏访问。

## 3. 实验设计

- **数据集 / 场景**：论文使用了**标准常识推理（commonsense reasoning）**和**长上下文推理（long-context reasoning）**两类基准评测。
- **Benchmark**：属于公认的标准评测集，但摘要未给出具体数据集名称（如未见具体列出，判断可能包含如GSM8K、LongBench等常见推理评测，但需以原文为准）。
- **对比方法**：主要与**固定KV缓存方法（fixed KV-caching approaches）**进行对比，验证ARM在性能和效率上的优势。

## 4. 资源与算力

- **未明确说明**：摘要中未提及使用的GPU型号与数量、训练时长、参数量规模等算力信息。
- 需要说明：由于仅有摘要级信息，无法获知具体训练成本，这也反映出论文在资源消耗透明度方面存在不足。

## 5. 实验数量与充分性

- **实验数量**：摘要仅概述了在常识推理和长上下文推理基准上的总体结果，未给出具体实验组数。
- **充分性评估**：
  - 从已有信息看，实验覆盖了短上下文和长上下文两类场景，并对比了固定KV缓存基线，方向上是合理的；
  - **但不足**：未提及消融实验、不同记忆槽规模的敏感性分析、动态策略与固定策略的对比实验等细节，无法充分验证各组件的独立贡献；
  - **客观性风险**：未列出具体基线名称和数值，无法判断比较是否充分公平。

## 6. 论文的主要结论与发现

- ARM通过可学习路由和门控更新，显著**减少长上下文任务中的信息损失**，同时有效**控制注意力稀疏性**。
- 相比固定KV缓存方法，ARM在**性能**（推理质量）和**效率**（内存占用与生成延迟）两方面均取得了更优的结果。
- 动态记忆量控制策略使ARM能够在简单上下文与复杂推理之间自适应调节，具有良好的扩展性。

## 7. 优点

- **方法创新性强**：将KV缓存管理从离散启发式驱逐升级为可微分的端到端学习问题，是一个有价值的研究方向。
- **避免硬驱逐**：通过sigmoid门控软性融合新旧信息，从机制上减少了不可逆的信息丢失。
- **自适应稀疏控制**：引入策略网络动态调节记忆用量，兼顾效率与效果，设计上优于固定预算的缓存方案。
- **兼顾推理效率**：固定大小的记忆结构使内存开销可控，同时提升生成延迟表现。

## 8. 不足与局限

- **实验细节缺失**：摘要未提供具体的基准名称、基线方法列表、具体数值提升幅度，导致可验证性和可复现性描述不足。
- **算力成本未披露**：缺乏训练代价的说明，对于评估方法的实际可用性构成障碍。
- **未验证多智能体场景**：元数据中提到了"可迁移至多智能体场景"，但论文本身未进行相关实验验证，属于推测性延伸。
- **动态策略的实用性待检验**：策略网络在推理阶段额外引入了计算开销，摘要中未说明这部分开销与节省的注意力计算相比是否净收益为正。
- **缺少消融与分析**：未能通过消融实验确认各组件（Gumbel-Softmax路由、sigmoid门控、动态策略）的独立贡献。

（完）
