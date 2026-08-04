---
title: "ThunderAgent: A Fast, Simple, and Program-Aware Agentic Inference System"
title_zh: ThunderAgent：快速、简单且程序感知的智能体推理系统
authors: "Hao Kang, Ziyang li, Weili Xu, Xinyu Yang, Yinfang Chen, Junxiong Wang, Beidi Chen, Tushar Krishna, Chenfeng Xu, Simran Arora"
date: 2026-04-30
pdf: "https://openreview.net/pdf/bc17cb3f24279d089e18d6aaa40d44db26cc29ba.pdf"
tags: ["query:agent-cache"]
score: 9.0
evidence: 程序感知的智能体推理系统，利用端到端工作流知识调度KV缓存与工具资源
tldr: 现有智能体推理系统将LLM推理引擎与工具编排器松散组合，按请求独立调度资源，缺乏端到端工作流知识，导致KV缓存和工具环境管理次优。ThunderAgent将智能体工作流抽象为LLM程序，建立异构资源统一视图，实现程序感知的KV缓存与工具执行调度。该方法针对工作流整体优化，减少了延迟并提升资源利用率，为智能体工作流中的缓存调度与驱逐提供了系统级支持。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有关键组件松耦合、按请求调度，缺乏端到端工作流知识，导致KV缓存管理次优。
method: 用LLM程序抽象智能体工作流，统一建模KV缓存与工具环境，实现工作流级程序感知调度。
result: 实验显示减少工作流执行延迟并提升资源利用率，优于现有系统。
conclusion: 证明了工作流感知调度对智能体系统KV缓存管理的关键作用。
---

## Abstract
Large language models (LLMs) are now used to power complex multi-turn agentic workflows. Existing systems run agentic inference by loosely assembling isolated components: an LLM inference engine (e.g., vLLM) and a tool orchestrator (e.g., Kubernetes). Although agentic workflows involve multiple LLM and tool requests, these systems schedule and allocate resources separately on a per-request basis, without end-to-end knowledge of the workflow. This leads to sub-optimal management of KV cache and tool execution environments. To address the challenges, we propose **ThunderAgent**, a fast, simple, and program-aware agentic inference system. We first abstract agentic workflows as ***LLM Programs***, enabling a unified view of heterogeneous resources, including KV caches, system states, and external tool assets such as disk memory and network ports. Built upon this abstraction, ThunderAgent introduces a program-aware scheduler and a tool resource manager designed to maximize KV cache hit rates, mitigate memory imbalances, and enable asynchronous environment preparation. Evaluations across coding, routing, and scientific discovery agents demonstrate that ThunderAgent achieves **1.5-3.6×** throughput improvements in serving, **1.8-3.9×** in RL rollout, and up to **4.2×** disk memory savings compared to state-of-the-art inference systems. To facilitate reproducibility and support future development, we open-source the system implementations of ThunderAgent at: https://github.com/ThunderAgent-org/ThunderAgent

---

## 论文详细总结（自动生成）

# ThunderAgent 论文总结

## 1. 核心问题与研究动机

- **背景**：大语言模型（LLM）已被广泛用于构建复杂的多轮智能体（Agent）工作流，例如编程辅助、路由决策和科学发现等场景。
- **核心问题**：现有智能体推理系统将 LLM 推理引擎（如 vLLM）与工具编排器（如 Kubernetes）**松散组合**，在调度时仅按单个请求独立分配资源，缺乏对端到端工作流的整体认知。
- **导致的后果**：
  - KV 缓存管理次优，命中率低；
  - 工具执行环境的资源分配存在内存失衡；
  - 工作流执行延迟高，资源利用率不足。
- **核心洞察**：智能体工作流本质上是一系列有依赖关系的 LLM 调用与工具调用构成的程序结构，系统应感知这一结构以实现全局优化。

## 2. 方法论

### 核心思想
- 将智能体工作流抽象为 **LLM 程序（LLM Programs）**，以此建立对异构资源的统一视图。
- 基于该抽象，实现**程序感知（Program-Aware）**的调度与资源管理，使调度决策面向工作流整体而非孤立请求。

### 关键技术细节
- **统一资源视图**：将 KV 缓存、系统状态、外部工具资源（如磁盘内存、网络端口）纳入同一抽象框架进行建模。
- **程序感知调度器（Program-Aware Scheduler）**：
  - 利用工作流级知识预测后续 LLM 调用和工具调用的资源需求；
  - 以最大化 KV 缓存命中率为目标进行缓存调度与驱逐决策。
- **工具资源管理器（Tool Resource Manager）**：
  - 缓解内存失衡问题；
  - 支持**异步环境准备**（asynchronous environment preparation），即提前为后续工具调用准备执行环境，减少等待延迟。

### 算法流程（文字说明）
1. 将智能体工作流解析为 LLM 程序，识别各步骤的依赖关系与资源需求；
2. 调度器根据程序结构预判未来请求，决定 KV 缓存的保留、复用与驱逐策略；
3. 工具资源管理器根据程序进度，异步预分配和准备工具执行环境；
4. 在执行过程中持续更新工作流状态，动态调整调度策略。

## 3. 实验设计

- **评测场景**：
  - 编码（Coding）智能体；
  - 路由（Routing）智能体；
  - 科学发现（Scientific Discovery）智能体。
- **评测任务类型**：
  - **服务（Serving）任务**：衡量多用户并发场景下的系统吞吐；
  - **强化学习（RL Rollout）任务**：衡量智能体训练/推理过程中批量 rollout 的效率；
  - **资源效率评估**：磁盘内存使用量。
- **对比方法**：现有最先进的推理系统（未具体列出名称，但明确声称与 state-of-the-art 系统进行对比，涉及 vLLM 等代表性系统）。

## 4. 资源与算力

- 论文元数据中**未明确提及** GPU 型号、数量、训练时长或推理集群规模等具体算力信息。
- 仅能从实验内容推断涉及大规模 LLM 推理与 RL rollout，通常需要多卡 GPU 集群支持，但具体配置需要查看论文全文或开源仓库获取。

## 5. 实验数量与充分性

- **实验覆盖面**：涵盖三个差异化场景（编码、路由、科学发现），覆盖了两种典型负载（在线 serving 与 RL rollout），并评估了资源效率指标。
- **充分性评价**：
  - **优点**：场景选择具有代表性，能较好体现智能体工作流的多样性；同时评估延迟/吞吐和资源效率两个维度，角度较全面。
  - **不足**：作为系统类论文，缺少更细粒度的消融实验信息（如调度器各组件单独贡献、缓存策略对比、不同工作流复杂度的扩展性等）；未报告对比方法的配置细节与公平性控制措施，无法完全确认实验的客观性。

## 6. 主要结论与发现

- ThunderAgent 在服务（serving）场景下实现 **1.5–3.6×** 的吞吐提升；
- 在 RL rollout 场景下实现 **1.8–3.9×** 的吞吐提升；
- 相比现有最优推理系统，节省了最高 **4.2×** 的磁盘内存；
- 核心结论：**工作流级别的程序感知调度对于智能体系统的 KV 缓存管理和资源分配具有关键作用**，是提升智能体推理系统整体效率的有效途径。

## 7. 优点

- **思路创新**：首次明确将智能体工作流抽象为"LLM 程序"，将系统优化视角从单请求提升到工作流整体，设计理念具有启发性和通用性。
- **系统完整性**：同时考虑了 KV 缓存与工具资源两类异构资源，覆盖面广；异步环境准备和内存均衡设计解决了实际部署中的关键痛点。
- **性能提升显著**：在吞吐和资源节省两个维度均获得数倍提升，效果可量化且有说服力。
- **开源可复现**：提供开源实现，有利于后续研究者在真实环境中验证和扩展。
- **负载覆盖全面**：同时考虑在线推理（serving）和 RL rollout 两种重要负载模式，贴近实际应用需求。

## 8. 不足与局限

- **算力信息缺失**：未披露具体 GPU 型号、数量和训练/评测成本，难以评估系统的实际部署门槛。
- **消融实验不足**：缺少对不同调度策略、缓存驱逐算法和资源管理机制独立贡献的分析，难以判断各组件效果的具体来源。
- **公平性存疑**：未详细说明对比系统的配置优化程度和评测控制变量，可能引入对比偏差。
- **应用限制**：对工作流结构的解析依赖明确的程序抽象，对于动态性强、非结构化或跨系统协作的智能体工作流，其适用性有待验证；程序分析本身可能引入额外开销。
- **实验场景有限**：未涉及多租户大规模集群、长时运行稳定性、异构模型混合部署等生产环境关键因素。
- **可扩展性未充分讨论**：程序感知调度在大规模并发工作流下是否存在调度器自身的性能瓶颈，论文没有给出深入分析。

---

（完）
