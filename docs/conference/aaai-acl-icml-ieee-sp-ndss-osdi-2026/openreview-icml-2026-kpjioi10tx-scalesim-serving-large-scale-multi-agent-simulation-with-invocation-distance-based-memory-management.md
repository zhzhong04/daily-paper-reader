---
title: "ScaleSim: Serving Large-Scale Multi-Agent Simulation with Invocation Distance-Based Memory Management"
title_zh: ScaleSim：基于调用距离的显存管理实现大规模多智能体仿真服务
authors: "Zaifeng Pan, Yipeng Shen, Zhengding Hu, Zhuang Wang, Aninda Manocha, Zheng Wang, Zhongkai Yu, Yue Guan, Yufei Ding"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d9dfdf4ac70f47d90baf3e88c3a4b4cc6038d60c.pdf"
tags: ["query:agent-cache"]
score: 8.0
evidence: 提出基于调用距离的显存管理抽象，管理多智能体LLM仿真中的私有前缀缓存，应对多智能体系统的缓存调度与驱逐问题。
tldr: 大规模多智能体LLM仿真的部署常因每个智能体私有的模型、前缀缓存和适配器等GPU常驻状态而难以扩展。论文利用智能体激活稀疏且调用顺序可估计的特性，提出调用距离这一统一抽象，并基于它构建显存高效的服务系统ScaleSim，以此管理各智能体的前缀缓存、模型等资源。实验表明该方法能显著降低显存压力，支撑更大规模的多智能体仿真，为智能体协作场景中的缓存与显存调度提供了实用方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 多智能体仿真中每个智能体私有GPU状态导致显存快速耗尽，难以扩展。
method: 使用调用距离统一估计智能体未来请求顺序，据此在服务系统中管理模型与前缀缓存。
result: 显著降低大规模多智能体仿真的GPU显存压力，支持更多智能体运行。
conclusion: 调用距离抽象能有效指导多智能体仿真中的显存与缓存资源管理。
---

## Abstract
LLM-based multi-agent simulations are increasingly adopted across application domains, but remain difficult to scale due to GPU memory pressure. Each agent maintains private GPU-resident states, including models, prefix caches, and adapters, which quickly exhaust device memory as the agent count grows. We identify two key properties of these workloads: sparse agent activation and an estimable agent invocation order. Based on an analysis of representative workload classes, we introduce invocation distance, a unified abstraction that estimates the relative order in which agents will issue future LLM requests. Leveraging this abstraction, we present ScaleSim, a memory-efficient LLM serving system for large-scale multi-agent simulations. ScaleSim enables proactive prefetching and priority-based eviction, supports diverse agent-specific memory through a modular interface, and achieves up to 1.74$\times$ speedup over SGLang on simulation benchmarks. ScaleSim's source code is available at https://github.com/PanZaifeng/KVFlow.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **背景**：基于大语言模型（LLM）的多智能体模拟在多个应用领域日益普及。
- **核心问题**：大规模多智能体模拟面临严重的 GPU 显存压力。每个智能体都维护私有的 GPU 常驻状态（包括模型参数、前缀缓存 prefix cache、适配器 adapters 等），随着智能体数量增加，显存迅速耗尽，导致系统难以扩展。
- **整体含义**：论文聚焦于如何在大规模多智能体模拟场景下提高 GPU 内存利用效率，从而在有限显存资源下支持更多智能体、提升服务规模，是该领域系统层面的重要探索。

## 2. 方法论

- **核心观察**：多智能体模拟负载具有两个关键特性——**稀疏激活**（每个时刻只有少量智能体被调用）和**可估计的调用顺序**（智能体未来发起 LLM 请求的相对顺序可以被预测）。
- **核心概念》调用距离（invocation distance）**：一种统一抽象，用于估计各智能体未来发出 LLM 请求的相对先后顺序，从而为内存调度提供依据。
- **系统实现——ScaleSim**：
  - **主动预取（proactive prefetching）**：根据调用距离提前将即将被使用的智能体状态（如前缀缓存）加载到 GPU 显存。
  - **基于优先级的驱逐（priority-based eviction）**：按调用距离远近来决定哪些状态应被优先驱逐出显存。
  - **模块化接口**：通过统一接口支持不同类型的智能体私有内存（模型、前缀缓存、适配器等）。
- **算法流程（文字描述）**：
  1. 分析代表性工作负载类别，统计智能体调用规律。
  2. 为每个智能体计算调用距离，形成未来请求顺序估计。
  3. 调度器根据调用距离决定预取时机和驱逐优先级。
  4. 在智能体实际发起请求前完成所需状态加载，并回收近期不会被访问的状态内存。

## 3. 实验设计

- **Benchmark**：使用仿真基准（simulation benchmarks），但摘要中未明确说明具体数据集/场景名称。
- **对比方法**：与 **SGLang** 进行对比（SGLang 是一个流行的 LLM 推理/服务系统）。
- **实验结果**：在仿真基准上取得最高 **1.74× 加速比**（相对于 SGLang）。
- 由于摘要信息有限，无法得知更细粒度的实验设置（如具体智能体数量、场景类型、任务分布等）。

## 4. 资源与算力

- **摘要中未说明**具体使用的 GPU 型号、数量、显存大小、训练/推理时长等资源细节。
- 论文可能以“有限 GPU 资源”为前提讨论效果，但未在摘要中列出具体硬件配置。
- 需要阅读论文全文才能确认算力信息。

## 5. 实验数量与充分性

- 摘要中仅给出**一个总体结果**（与 SGLang 对比的加速比），未列出多组实验、不同场景或消融实验的细节。
- 从摘要看，实验**充分性不足**：缺少对不同工作负载、不同智能体规模、不同内存压力条件、不同调度策略（如无预取/不同驱逐策略）等的系统性对比。
- 客观性与公平性：仅对比 SGLang 一个基线，对比范围较窄；未披露硬件与参数细节，难以判断结果是否完全公平，但作为系统类论文，通常会在正文中补充更全面的实验。

## 6. 主要结论与发现

- 通过利用调用顺序特性，可以大幅改善多智能体模拟的内存效率与可扩展性。
- ScaleSim 在内存受限条件下支持更多智能体，显著提升大规模模拟的服务规模。
- 在仿真基准上，ScaleSim 相较 SGLang 可实现最高 1.74 倍加速。

## 7. 优点

- **问题实际且重要**：多智能体模拟的显存瓶颈是真实且紧迫的系统挑战。
- **抽象简洁有效**：调用距离这一统一抽象抓住了多智能体负载“稀疏激活 + 可预测顺序”的核心特征，为调度提供可操作指标。
- **方案系统化**：同时考虑预取与驱逐，且模块化接口支持多种私有状态，具有较强的通用性。
- **结果有说服力**：相对于成熟系统 SGLang 的加速比体现出实际收益。

## 8. 不足与局限

- **实验信息过少**：摘要仅报告单一加速比，缺乏详细实验数据（如不同规模、不同场景、内存占用曲线等）。
- **基线单一**：仅与 SGLang 对比，未与其他多智能体模拟系统或专用缓存策略对比。
- **资源信息缺失**：未说明 GPU 型号/数量等算力条件，难以复现和评估泛化性。
- **假设依赖**：方法依赖“可估计的调用顺序”，若智能体调用具有高度随机性或动态变化，调用距离估计可能失效，适用范围可能受限。
- **系统复杂度**：大规模系统中的预取与驱逐协调可能引入额外开销，摘要未分析这些开销。

（完）
