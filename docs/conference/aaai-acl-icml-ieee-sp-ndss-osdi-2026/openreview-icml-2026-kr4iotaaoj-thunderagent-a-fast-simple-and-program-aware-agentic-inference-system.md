---
title: "ThunderAgent: A Fast, Simple, and Program-Aware Agentic Inference System"
title_zh: ThunderAgent：一种快速、简单且程序感知的智能体推理系统
authors: "Hao Kang, Ziyang li, Weili Xu, Xinyu Yang, Yinfang Chen, Junxiong Wang, Beidi Chen, Tushar Krishna, Chenfeng Xu, Simran Arora"
date: 2026-04-30
pdf: "https://openreview.net/pdf/bc17cb3f24279d089e18d6aaa40d44db26cc29ba.pdf"
tags: ["query:awc"]
score: 9.0
evidence: 面向智能体工作流中KV缓存调度的程序感知推理系统
tldr: 现有系统将智能体推理拆分为独立的LLM推理引擎和工具编排器，按请求调度资源，导致KV缓存和工具环境管理欠佳。ThunderAgent将智能体工作流抽象为LLM程序，统一视图下联合调度KV缓存与工具执行环境，从而避免按请求调度带来的次优问题，提升端到端性能。该系统展示了工作流感知缓存调度在智能体推理中的关键作用。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有智能体推理系统按请求独立调度KV缓存和工具资源，缺少工作流端到端信息，导致缓存管理次优。
method: 将智能体工作流抽象为LLM程序，以统一方式调度KV缓存和工具执行环境，实现工作流感知的资源管理。
result: 实验表明该方法能显著提升智能体推理的端到端效率与资源利用率。
conclusion: 工作流感知的KV缓存调度能够改善智能体推理系统的资源管理与性能。
---

## Abstract
Large language models (LLMs) are now used to power complex multi-turn agentic workflows. Existing systems run agentic inference by loosely assembling isolated components: an LLM inference engine (e.g., vLLM) and a tool orchestrator (e.g., Kubernetes). Although agentic workflows involve multiple LLM and tool requests, these systems schedule and allocate resources separately on a per-request basis, without end-to-end knowledge of the workflow. This leads to sub-optimal management of KV cache and tool execution environments. To address the challenges, we propose **ThunderAgent**, a fast, simple, and program-aware agentic inference system. We first abstract agentic workflows as ***LLM Programs***, enabling a unified view of heterogeneous resources, including KV caches, system states, and external tool assets such as disk memory and network ports. Built upon this abstraction, ThunderAgent introduces a program-aware scheduler and a tool resource manager designed to maximize KV cache hit rates, mitigate memory imbalances, and enable asynchronous environment preparation. Evaluations across coding, routing, and scientific discovery agents demonstrate that ThunderAgent achieves **1.5-3.6×** throughput improvements in serving, **1.8-3.9×** in RL rollout, and up to **4.2×** disk memory savings compared to state-of-the-art inference systems. To facilitate reproducibility and support future development, we open-source the system implementations of ThunderAgent at: https://github.com/ThunderAgent-org/ThunderAgent

---

## 论文详细总结（自动生成）

## 论文总结：ThunderAgent：一种快速、简单且程序感知的智能体推理系统

### 1. 核心问题与整体含义（研究动机与背景）

- **背景**：大语言模型（LLMs）正越来越多地被用于驱动复杂的多轮智能体工作流（agentic workflows），这类工作流涉及多个 LLM 请求与外部工具调用。
- **核心问题**：现有智能体推理系统（如 vLLM + Kubernetes）将 LLM 推理引擎和工具编排器松散组装，按单个请求（per-request）独立调度和分配资源，缺乏对工作流端到端的全局视野，导致 **KV 缓存** 与 **工具执行环境** 管理次优——包括缓存命中率低、内存失衡、工具环境准备无法异步进行等问题。
- **整体含义**：本文指出，现有系统“按请求调度”的范式忽略了工作流层面的信息，是智能体推理性能瓶颈的关键。需要从工作流端到端的视角重新设计资源调度，以提升推理系统的整体效率与资源利用率。

### 2. 方法论：核心思想、关键技术细节

- **核心思想——LLM 程序抽象**：将智能体工作流抽象为 **LLM 程序（LLM Programs）**，它为异构资源（KV 缓存、系统状态、外部工具资产如磁盘内存和网络端口）提供统一视图，从而打破按请求调度的次优性。
- **程序感知调度器（Program-aware Scheduler）**：
  - 基于 LLM 程序抽象，在统一视图下联合调度 KV 缓存与工具执行环境，而不是分开、按请求调度。
  - 以 **最大化 KV 缓存命中率** 为目标进行调度决策。
- **工具资源管理器（Tool Resource Manager）**：
  - 负责管理外部工具所需的资源（如磁盘内存、网络端口）。
  - 实现 **异步环境准备**，解决内存失衡（memory imbalance）问题，提升工具启动效率。
- **技术要点**（基于摘要概括）：
  - 工作流感知的缓存调度：利用工作流结构信息预知未来 KV 复用模式，优化缓存分配。
  - 统一资源配置：将 KV 缓存与工具环境资源放在同一调度视图下协同管理，避免按请求调度的局部最优陷阱。

> 注：摘要中未提供具体公式或详细算法伪代码，算法流程的文字化描述如上。

### 3. 实验设计

- **评估场景**：覆盖 **编码（coding）、路由（routing）、科学发现（scientific discovery）** 三类智能体代理。
- **主要任务类别**：
  - 服务（serving）吞吐量：模拟在线服务场景下的智能体推理。
  - RL rollout：验证在强化学习训练数据生成（rollout）场景下的性能。
  - 磁盘内存占用：评估工具环境的资源效率。
- **对比基线**：与当前最先进的（state-of-the-art）推理系统进行对比（如 vLLM 类系统 + Kubernetes 类工具编排器，摘要中未指明具体基线名称）。
- **具体 benchmark**：摘要未提供具体数据集名称，仅给出场景类别。

### 4. 资源与算力

- **论文明确说明部分**：论文中 **未明确说明** 使用的 GPU 型号、GPU 数量、训练时长或推理时的具体硬件配置。
- **可推断信息**：作为系统类论文，实验应涉及 GPU 集群部署，但具体算力细节在摘要中不可得。

### 5. 实验数量与充分性

- **实验数量**：
  - 摘要报告了三大类场景（编码、路由、科学发现）下的性能结果。
  - 每类场景中报告了 serving 和 RL rollout 两组指标，以及磁盘内存节约指标。
  - 未提及消融实验数量。
- **充分性与客观性评估**：
  - **充分性中等**：覆盖了三个具有代表性的智能体应用场景，并在 serving 和 RL rollout 两种关键部署模式下验证，维度较为全面。
  - **客观性风险**：摘要中未明确列出对比基线系统的具体名称与版本，也未描述超参数设置、工具集类型（如代码执行工具、检索工具）等细节，因此难以完全客观地判断比较的公平性。
  - **缺失项**：缺少消融实验（如验证各组件贡献度）、扩展性测试（不同工作流规模）、以及对不同 KV 缓存策略的对比分析。

### 6. 主要结论与发现

- **性能提升**：
  - **1.5–3.6×**：服务（serving）吞吐量提升。
  - **1.8–3.9×**：RL rollout 吞吐量提升。
  - **最高 4.2×**：磁盘内存节省。
- **核心发现**：工作流感知的 KV 缓存调度能显著改善智能体推理系统的资源管理与端到端性能，优于按请求调度的传统方案。
- **附加贡献**：开源系统实现（https://github.com/ThunderAgent-org/ThunderAgent），以促进可复现性与后续研究。

### 7. 优点

- **问题定位精准**：指出按请求调度与按工作流调度的根本性差异，抓住了智能体推理系统区别于普通 LLM 推理的关键挑战。
- **抽象统一**：提出 LLM 程序抽象，将 KV 缓存与工具环境统一为可调度资源，观点新颖且系统设计简洁。
- **场景覆盖多样**：包括编码、路由、科学发现三类差异明显的智能体应用，并在 serving 与 RL rollout 两大部署场景验证，增强了结论的普适性。
- **量化收益显著**：吞吐量提升 1.5–3.9 倍、磁盘节省 4.2 倍，提升幅度大，具备较强的实际应用价值。
- **开源实现**：提供了代码仓库，有利于复现和后续扩展。

### 8. 不足与局限

- **实验细节披露有限**：摘要中未提供数据集名称、工具集类型、 workload 规模、对比系统的具体配置等信息，实验的可复现性证据不足。
- **缺少消融与敏感性分析**：未展示各组件（调度器 vs. 资源管理器）的独立贡献，也未分析不同工作流特性（如工具调用频率、KV 复用模式）对系统性能的影响。
- **算力信息缺失**：未说明硬件平台（GPU 型号、数量等），难以评估系统在不同硬件条件下的可迁移性。
- **应用限制**：LLM 程序抽象是否适用于所有智能体框架（如多智能体协作、动态图结构工作流）尚不明确；未来工作可能需要扩展到更复杂的工作流拓扑。
- **证据级别**：当前为 ICML-2026 接收论文，仅有摘要性信息，未提供完整实验细节供深入评估。

---

（完）
