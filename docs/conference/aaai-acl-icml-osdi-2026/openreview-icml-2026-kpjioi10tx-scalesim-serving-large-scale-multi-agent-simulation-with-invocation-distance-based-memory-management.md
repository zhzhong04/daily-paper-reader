---
title: "ScaleSim: Serving Large-Scale Multi-Agent Simulation with Invocation Distance-Based Memory Management"
title_zh: ScaleSim：基于调用距离内存管理的大规模多智能体模拟服务
authors: "Zaifeng Pan, Yipeng Shen, Zhengding Hu, Zhuang Wang, Aninda Manocha, Zheng Wang, Zhongkai Yu, Yue Guan, Yufei Ding"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d9dfdf4ac70f47d90baf3e88c3a4b4cc6038d60c.pdf"
tags: ["query:agent-cache"]
score: 9.0
evidence: 使用基于可估计智能体调用顺序的调用距离来管理前缀缓存等内存
tldr: 大规模多智能体模拟中，每个智能体独立保有私有前缀缓存等GPU状态，导致内存压力巨大。本文观察到智能体稀疏激活且调用顺序可估计，提出调用距离（invocation distance）这一抽象来统一估计未来LLM请求的相对顺序。基于此设计ScaleSim内存管理机制，按预测的调用顺序调度缓存分配与回收，优先保留即将被再次调用的智能体缓存。实验表明该方法可显著降低GPU内存占用并支持更大规模模拟。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 多智能体模拟中每个智能体维护私有前缀缓存，GPU内存随智能体数量线性膨胀。
method: 提出调用距离抽象，估计智能体未来LLM请求的相对顺序，并据此管理缓存分配与回收。
result: 实验显示ScaleSim能显著降低GPU内存压力，支持更大规模的多智能体模拟。
conclusion: 利用可估计的调用顺序进行内存管理，可高效扩展多智能体模拟系统。
---

## Abstract
LLM-based multi-agent simulations are increasingly adopted across application domains, but remain difficult to scale due to GPU memory pressure. Each agent maintains private GPU-resident states, including models, prefix caches, and adapters, which quickly exhaust device memory as the agent count grows. We identify two key properties of these workloads: sparse agent activation and an estimable agent invocation order. Based on an analysis of representative workload classes, we introduce invocation distance, a unified abstraction that estimates the relative order in which agents will issue future LLM requests. Leveraging this abstraction, we present ScaleSim, a memory-efficient LLM serving system for large-scale multi-agent simulations. ScaleSim enables proactive prefetching and priority-based eviction, supports diverse agent-specific memory through a modular interface, and achieves up to 1.74$\times$ speedup over SGLang on simulation benchmarks. ScaleSim's source code is available at https://github.com/PanZaifeng/KVFlow.

---

## 论文详细总结（自动生成）

# ScaleSim 论文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究背景**：基于 LLM 的多智能体模拟（multi-agent simulation）在多个应用领域被广泛采用，但面临严重的**GPU 内存扩展瓶颈**。
- **核心问题**：在多智能体模拟中，每个智能体都需维护私有的 GPU 驻留状态（包括模型参数、前缀缓存 prefix cache、适配器 adapters 等）。随着智能体数量增长，这些状态会迅速耗尽设备内存，导致系统难以扩展到大规模场景。
- **整体含义**：该论文旨在通过更智能的内存管理策略，使 LLM 多智能体模拟系统能够高效地支持更大规模的智能体数量，从而提升系统的可扩展性和运行效率。

## 2. 论文提出的方法论（核心思想、关键技术细节）

- **工作负载特性分析**：作者识别出多智能体模拟负载的两个关键特性：
  - **稀疏激活（sparse agent activation）**：在任意时刻，只有少数智能体处于活跃状态，大多数智能体闲置。
  - **可估计的智能体调用顺序（estimable agent invocation order）**：智能体之间在未来触发 LLM 请求的顺序可以被合理预估。
- **核心抽象——调用距离（invocation distance）**：
  - 作者提出“调用距离”这一统一抽象，用于估计智能体未来发出 LLM 请求的**相对顺序**（即距离未来调用越近的智能体，其缓存越应被保留）。
- **ScaleSim 系统设计**：
  - 基于调用距离预测，实现**主动预取（proactive prefetching）**：在智能体即将被调用前，提前加载其需要的缓存或状态。
  - 实现**基于优先级的驱逐（priority-based eviction）**：当内存不足时，优先驱逐距离未来调用较远的智能体缓存，保留即将被调用的缓存。
  - 通过**模块化接口**支持管理多种智能体特定内存（如前缀缓存、适配器等），使系统具备通用性。

## 3. 实验设计（数据集 / 场景 / Benchmark / 对比方法）

- **Benchmark**：论文使用“模拟基准测试（simulation benchmarks）”进行评估，但具体数据集或模拟场景类型（如社交模拟、游戏环境、机器人协作等）在摘要中**未明确说明**。
- **对比方法**：主要与 **SGLang**（一个常见的 LLM 推理与服务系统）进行对比。
- **评估指标**：以端到端性能（如速度提升倍数）作为主要指标，报告了最高 **1.74×** 的加速比。

## 4. 资源与算力

- 摘要中**未提供**任何有关算力资源的具体信息，例如：
  - GPU 型号（如 A100、H100 等）
  - GPU 数量
  - 训练或推理时长
  - 内存容量配置
- 因此，无法从现有信息中总结资源需求情况，需要阅读全文才能确认。

## 5. 实验数量与充分性

- 摘要中仅给出了一个整体性能对比结果（与 SGLang 相比的最高加速比），**未提及**实验的具体数量、不同场景的测试、消融实验（如对调用距离预测质量、预取/驱逐策略的单独分析）等。
- 因此，从摘要来看，**实验证据的充分性不够透明**，无法判断实验是否全面覆盖了不同工作负载、内存压力水平或智能体规模变化的情况。
- 不过，论文已被 ICML-2026 接收，可能正文包含更详细实验；仅凭摘要无法充分评估其客观性和公平性。

## 6. 论文的主要结论与发现

- **核心发现**：多智能体模拟中的智能体调用具有可预测的顺序性，可以利用这一特性来优化缓存管理。
- **ScaleSim 的效果**：通过调用距离驱动的内存管理，ScaleSim 能显著降低 GPU 内存压力，从而支持更大规模的多智能体模拟。
- **性能收益**：在模拟基准测试中，ScaleSim 相对 SGLang 最高可获得 **1.74× 的加速**。
- **总体结论**：利用可估计的调用顺序进行内存管理，是高效扩展多智能体模拟系统的一种有效途径。

## 7. 优点（方法或实验设计亮点）

- **问题选择精准**：直击多智能体模拟中的 GPU 内存瓶颈，具有实际意义。
- **工作负载洞察**：识别出“稀疏激活”和“可估计调用顺序”两个关键性质，为系统设计提供了扎实依据。
- **统一抽象**：提出“调用距离”这一简洁抽象，将复杂的调度问题转化为基于相对顺序的优先级问题，便于系统实现。
- **设计完整**：同时包含主动预取、优先级驱逐和模块化接口，覆盖了内存管理的多个方面，具有一定通用性。
- **开源**：提供源代码（https://github.com/PanZaifeng/KVFlow），有助于复现和后续研究。

## 8. 不足与局限

- **实验细节缺失**：摘要中未报告具体的实验场景、数据集规模、智能体数量范围、内存压力水平等信息，难以判断其在何种条件下取得 1.74× 加速比。
- **对比范围有限**：仅与 SGLang 对比，未提及与其他内存管理方案或缓存策略的比较。
- **未报告消融实验**：缺少对调用距离预测误差、预取与驱逐策略各自贡献的消融分析，使得方法有效性的来源不够清晰。
- **资源信息不明**：没有给出 GPU 型号和数量，无法评估方法在不同硬件配置下的可迁移性。
- **可能存在的偏差风险**：若 benchmark 场景偏向可预测性较强的模拟类型，则结论可能对随机性更强、调用顺序更难预测的真实应用泛化能力有限。

（完）
