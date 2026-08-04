---
title: "ThunderAgent: A Fast, Simple, and Program-Aware Agentic Inference System"
title_zh: ThunderAgent：一种快速、简单且程序感知的智能体推理系统
authors: "Hao Kang, Ziyang li, Weili Xu, Xinyu Yang, Yinfang Chen, Junxiong Wang, Beidi Chen, Tushar Krishna, Chenfeng Xu, Simran Arora"
date: 2026-04-30
pdf: "https://openreview.net/pdf/bc17cb3f24279d089e18d6aaa40d44db26cc29ba.pdf"
tags: ["query:awc"]
score: 9.0
evidence: ThunderAgent利用端到端工作流感知统一调度KV缓存与工具资源
tldr: 针对现有智能体推理系统缺乏工作流级端到端感知、导致KV缓存与工具环境管理次优的问题，ThunderAgent将智能体工作流抽象为LLM程序，实现异构资源的统一视图和程序感知调度。实验证明该方法能有效提升多轮智能体工作流的执行效率并降低缓存开销。其意义在于为智能体工作流的缓存调度提供了系统级设计范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有智能体推理系统按单请求调度资源，缺乏对工作流的端到端感知，导致KV缓存和工具执行环境管理次优。
method: 将智能体工作流抽象为LLM程序，统一管理异构资源，并实现程序感知的KV缓存与工具执行环境调度。
result: 实验表明ThunderAgent能显著提升智能体工作流吞吐并降低KV缓存开销。
conclusion: 程序感知的端到端调度是优化智能体工作流缓存与执行效率的关键方向。
---

## Abstract
Large language models (LLMs) are now used to power complex multi-turn agentic workflows. Existing systems run agentic inference by loosely assembling isolated components: an LLM inference engine (e.g., vLLM) and a tool orchestrator (e.g., Kubernetes). Although agentic workflows involve multiple LLM and tool requests, these systems schedule and allocate resources separately on a per-request basis, without end-to-end knowledge of the workflow. This leads to sub-optimal management of KV cache and tool execution environments. To address the challenges, we propose **ThunderAgent**, a fast, simple, and program-aware agentic inference system. We first abstract agentic workflows as ***LLM Programs***, enabling a unified view of heterogeneous resources, including KV caches, system states, and external tool assets such as disk memory and network ports. Built upon this abstraction, ThunderAgent introduces a program-aware scheduler and a tool resource manager designed to maximize KV cache hit rates, mitigate memory imbalances, and enable asynchronous environment preparation. Evaluations across coding, routing, and scientific discovery agents demonstrate that ThunderAgent achieves **1.5-3.6×** throughput improvements in serving, **1.8-3.9×** in RL rollout, and up to **4.2×** disk memory savings compared to state-of-the-art inference systems. To facilitate reproducibility and support future development, we open-source the system implementations of ThunderAgent at: https://github.com/ThunderAgent-org/ThunderAgent

---

## 论文详细总结（自动生成）

# 论文总结：ThunderAgent

## 1. 核心问题与整体含义
- **研究动机**：大语言模型（LLM）现已广泛用于构建复杂的多轮智能体工作流（agentic workflows）。然而，现有系统通常将推理引擎（如 vLLM）与工具编排系统（如 Kubernetes）松散组合，按单个请求独立调度资源，缺乏对工作流整体的端到端感知。
- **核心问题**：这种按请求级别的资源调度方式导致 KV 缓存和工具执行环境的管理次优，例如缓存命中率低、内存使用不均衡、工具环境准备无法与任务推进协同。
- **整体含义**：需要一种面向工作流级别的程序感知调度范式，才能本质性提升智能体推理系统的吞吐与资源效率。

## 2. 方法论
- **核心思想**：将智能体工作流抽象为 **LLM Programs**，从而建立一个对异构资源的统一抽象视图——这些资源包括 KV 缓存、系统状态，以及外部工具资产（如磁盘内存、网络端口等）。
- **关键技术**：
  - 设计**程序感知调度器（program-aware scheduler）**，以最大化 KV 缓存命中率、缓解不同工作流间的内存失衡。
  - 设计**工具资源管理器（tool resource manager）**，支持异步环境准备，使工具执行环境能提前就绪，避免阻塞 LLM 调用。
- **公式/算法流程**：摘要中未给出具体公式或算法步骤，核心流程可概括为：将工作流规约为程序 → 统一管理异构资源 → 基于程序语义进行缓存调度与环境预取。

## 3. 实验设计
- **评估场景**：覆盖三类智能体——编码（coding）、路由（routing）、科学发现（scientific discovery）。
- **对比方法**：与当前最先进的（state-of-the-art）推理系统进行对比，但摘要中未列出具体的系统名称或基准（benchmark）名称。
- **评估指标**：
  - 服务（serving）吞吐
  - 强化学习 rollout（RL rollout）吞吐
  - 磁盘内存（disk memory）占用/节省

## 4. 资源与算力
- 论文摘要中**未明确说明**使用的 GPU 型号、数量、训练或推理时长等具体算力信息。
- 因此无法从现有文本评估其资源效率的绝对值或复现成本。

## 5. 实验数量与充分性
- 摘要提及三个不同场景（编码、路由、科学发现），但**未给出详细的实验配置、具体数据集、消融实验或敏感性分析**。
- 从可获得的信息看，实验结果方向一致（性能提升），但**不足以全面判断实验的充分性与公平性**。缺失基线细节和消融对照，可能影响结论的普适性。

## 6. 主要结论与发现
- ThunderAgent 在服务吞吐上实现 **1.5–3.6×** 的提升，在 RL rollout 吞吐上实现 **1.8–3.9×** 的提升，并节省最高 **4.2×** 的磁盘内存。
- 结论：**程序感知的端到端调度是优化智能体工作流缓存命中与执行效率的关键方向**，为智能体工作流的资源管理提供了新的系统级设计范式。

## 7. 优点
- **抽象创新**：将智能体工作流抽象为 LLM 程序，统一了 KV 缓存、系统状态和外部工具资源视图，思路系统性强。
- **调度设计**：程序感知调度器直接针对工作流全生命周期优化，显著提升命中率并缓解内存失衡。
- **异步预取**：工具资源的异步准备能有效隐藏环境初始化延迟。
- **开源**：提供系统实现源码，利于复现和后续研究。

## 8. 不足与局限
- **实验细节缺失**：未提供具体数据集、基准、基线系统实现细节，难以独立复现和验证公平性。
- **算力信息缺失**：未说明训练/推理所消耗的 GPU 资源，难以评估其实际部署成本与可扩展性。
- **消融不足**：未提及对调度器、工具管理器、抽象表示等组件的消融实验，无法归因具体贡献。
- **可能存在选择性报告**：摘要只报告了提升倍率，未报告失败案例或不利场景。
- **通用性存疑**：仅在编码、路由和科学发现三类智能体上验证，对更广泛的多轮交互/多工具协同工作流的适用性有待验证。

（完）
