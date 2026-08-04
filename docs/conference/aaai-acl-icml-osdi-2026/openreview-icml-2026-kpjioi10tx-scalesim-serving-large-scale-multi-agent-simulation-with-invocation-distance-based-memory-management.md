---
title: "ScaleSim: Serving Large-Scale Multi-Agent Simulation with Invocation Distance-Based Memory Management"
title_zh: ScaleSim：基于调用距离的内存管理实现大规模多智能体模拟服务
authors: "Zaifeng Pan, Yipeng Shen, Zhengding Hu, Zhuang Wang, Aninda Manocha, Zheng Wang, Zhongkai Yu, Yue Guan, Yufei Ding"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d9dfdf4ac70f47d90baf3e88c3a4b4cc6038d60c.pdf"
tags: ["query:awc"]
score: 8.0
evidence: ScaleSim利用调用距离管理多智能体模拟中各智能体的前缀缓存与GPU内存
tldr: 大规模LLM多智能体模拟因智能体私有GPU状态（模型、前缀缓存、适配器）导致显存迅速耗尽，扩展困难。ScaleSim发现此类负载具有稀疏激活和可估计调用顺序的特点，提出调用距离抽象来预测未来请求顺序，并据此管理前缀缓存等内存资源。实验显示该方法显著提升可支持的智能体规模并降低内存压力，为多智能体系统中的缓存驱逐策略提供了实用基础。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 大规模LLM多智能体模拟中每个智能体私有GPU状态迅速耗尽显存，难以扩展。
method: 提出调用距离统一抽象估计智能体未来请求顺序，据此进行前缀缓存等内存的管理与回收。
result: 实验表明ScaleSim能支持更大规模的多智能体模拟并显著降低显存压力。
conclusion: 利用智能体调用顺序的可估计性可实现高效的多智能体缓存与内存管理。
---

## Abstract
LLM-based multi-agent simulations are increasingly adopted across application domains, but remain difficult to scale due to GPU memory pressure. Each agent maintains private GPU-resident states, including models, prefix caches, and adapters, which quickly exhaust device memory as the agent count grows. We identify two key properties of these workloads: sparse agent activation and an estimable agent invocation order. Based on an analysis of representative workload classes, we introduce invocation distance, a unified abstraction that estimates the relative order in which agents will issue future LLM requests. Leveraging this abstraction, we present ScaleSim, a memory-efficient LLM serving system for large-scale multi-agent simulations. ScaleSim enables proactive prefetching and priority-based eviction, supports diverse agent-specific memory through a modular interface, and achieves up to 1.74$\times$ speedup over SGLang on simulation benchmarks. ScaleSim's source code is available at https://github.com/PanZaifeng/KVFlow.

---

## 论文详细总结（自动生成）

# 中文总结

## 1. 核心问题与整体含义

- **研究背景**：基于 LLM 的多智能体模拟（multi-agent simulation）正在被广泛应用于多个领域，但随着智能体数量增长，GPU 内存成为主要瓶颈。每个智能体都维护私有的 GPU 驻留状态，包括模型、前缀缓存（prefix cache）和适配器（adapter），导致设备内存迅速耗尽，系统难以扩展。
- **核心问题**：如何在有限 GPU 内存下高效服务大规模多智能体模拟，使更多智能体能够同时运行。
- **整体含义**：该工作揭示了多智能体负载的两个关键特性——**智能体稀疏激活**（同一时刻只有少量智能体活跃）和**可估计的调用顺序**，并据此构建了面向大规模多智能体模拟的内存管理机制，为提升系统扩展性提供了新思路。

## 2. 方法论

- **核心思想**：利用多智能体负载的可预测性，提前管理内存资源，避免盲目缓存导致的内存浪费。
- **关键抽象——调用距离（invocation distance）**：
  - 提出一种统一抽象，用于估计智能体未来发起 LLM 请求的相对顺序。
  - 通过分析代表性工作负载类别，可以预测哪些智能体将在近期被调用，以及调用的先后次序。
- **ScaleSim 系统设计**：
  - **主动预取（proactive prefetching）**：根据调用距离预测，提前将即将需要的智能体状态（如前缀缓存）加载到 GPU 内存。
  - **基于优先级的驱逐（priority-based eviction）**：在内存不足时，优先驱逐调用距离较远的智能体状态，保留近期会使用的状态。
  - **模块化接口**：支持多种智能体专用的内存类型（模型、前缀缓存、适配器等），便于统一管理和扩展。
- **算法流程（文字说明）**：
  1. 监控当前智能体执行状态与历史调用模式；
  2. 计算每个智能体的调用距离，得到未来请求顺序的估计；
  3. 根据调用距离为每个智能体的内存对象分配优先级；
  4. 执行预取（对距离近的对象）与驱逐（对距离远的对象）；
  5. 动态更新调用距离估计，适应模拟中的变化。

## 3. 实验设计

- **数据集/场景**：论文基于代表性工作负载类别进行分析，但具体数据集名称未在提供的文本中详述，推测使用了多种多智能体模拟任务（如社交模拟、协作任务等）。
- **Benchmark**：采用模拟基准（simulation benchmarks），与主流 LLM serving 系统 **SGLang** 进行对比。
- **对比方法**：主要对比 SGLang，评估 ScaleSim 在内存效率和端到端性能上的提升。

## 4. 资源与算力

- 提供的文本和元数据中**未明确说明**使用的 GPU 型号、数量、训练时长或推理部署的具体硬件配置。
- 只能从实验结果推测使用了实际 GPU 集群，但具体资源配置无法从当前信息中确认。

## 5. 实验数量与充分性

- 从现有摘要和元数据看，实验包括：
  - 与 SGLang 的对比实验，报告了最高 **1.74× 加速比**；
  - 涉及内存压力降低和多智能体规模扩展能力的评估；
  - 可能还包含对不同工作负载类别和不同智能体配置的测试。
- **充分性评估**：
  - 加速比和规模提升的数据支持了核心主张，但公开信息中未显示详尽的消融实验（如单独验证预取效果、驱逐策略效果、不同调用距离预测精度的影响）。
  - 对比基线较少（仅 SGLang），缺少与其他多智能体 serving 系统或专用缓存管理方案的比较。
  - 总体来说实验结果能初步证明有效性，但全面性和公平性尚需更详细论文内容佐证。

## 6. 主要结论与发现

- 多智能体模拟负载具有**稀疏激活**和**可估计调用顺序**的特性，这为内存管理提供了可利用的先验信息。
- 通过 **调用距离** 这一统一抽象，可以有效预测未来请求顺序，从而实现主动预取与优先级驱逐。
- ScaleSim 在模拟基准上比 SGLang 获得最高 **1.74× 的端到端加速**，并能支持更大规模的智能体数量，显著降低 GPU 显存压力。
- 结论：利用智能体调用顺序的可估计性，可实现高效的多智能体缓存与内存管理，为大规模 LLM 多智能体模拟服务提供实用基础。

## 7. 优点

- **问题定位准确**：聚焦于多智能体模拟中智能体私有状态导致的内存瓶颈，是一个实际且重要的问题。
- **观察新颖**：识别出多智能体负载“稀疏激活”和“可估计调用顺序”这两个关键特性，并据此设计系统，而非通用缓存策略。
- **抽象简洁有效**：调用距离统一了不同智能体内存对象的生命周期管理，具有较好的通用性。
- **模块化设计**：支持多种智能体专用内存（模型、前缀缓存、适配器），易于扩展到不同场景。
- **开源**：提供源代码，利于复现和后续研究。

## 8. 不足与局限

- **实验细节缺失**：提供的文本中未给出具体数据集、任务类型、智能体数量范围、硬件配置等关键信息，难以独立验证实验的充分性。
- **对比基线单一**：仅与 SGLang 对比，未与其他缓存管理方案或专用多智能体 serving 系统比较，优越性证据不够全面。
- **未提供消融分析**：缺少对调用距离预测误差、预取开销、驱逐策略敏感性等关键设计的消融实验，尚不清楚各组件贡献度。
- **应用限制**：方法依赖“可估计调用顺序”这一假设，对于调用顺序随机或动态变化很大的多智能体负载，性能可能退化。
- **算力信息缺失**：没有说明实验所用 GPU 资源和训练/推理成本，影响成本效益评估。

（完）
