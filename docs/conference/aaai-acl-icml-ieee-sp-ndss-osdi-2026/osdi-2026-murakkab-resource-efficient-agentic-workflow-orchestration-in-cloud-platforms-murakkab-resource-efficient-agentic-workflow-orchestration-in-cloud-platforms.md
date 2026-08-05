---
title: "Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms"
title_zh: Murakkab：云平台上资源高效的代理工作流编排
authors: "Gohar Irfan Chaudhry, Esha Choukse, Haoran Qiu, Íñigo Goiri, Rodrigo Fonseca, Adam Belay, Ricardo Bianchini"
date: 2026-01-01
pdf: "https://arxiv.org/pdf/2508.18298v2"
tags: ["query:awc"]
score: 6.0
evidence: 代理工作流的资源高效编排，支持工作流感知的资源管理，类比缓存调度与驱逐
tldr: 代理工作流由多个模型和工具协作组成，现有框架将其视为不透明的调用序列，导致资源浪费。Murakkab 提出声明式抽象，将工作流组件解耦，从而在精度、延迟、能耗和成本之间进行系统级权衡，实现资源高效的编排与调度。这种工作流感知的资源管理方式与缓存调度和驱逐密切相关，为代理工作流的可扩展部署提供基础设施支撑。
source: OSDI-2026-USENIX
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 909, \"height\": 421, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 916, \"height\": 222, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 912, \"height\": 253, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 898, \"height\": 927, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 437, \"height\": 289, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 450, \"height\": 276, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 907, \"height\": 607, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 441, \"height\": 291, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 446, \"height\": 277, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1843, \"height\": 344, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1776, \"height\": 341, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 886, \"height\": 342, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 881, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 881, \"height\": 389, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 894, \"height\": 360, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 877, \"height\": 1007, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 896, \"height\": 365, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 594, \"height\": 483, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 878, \"height\": 269, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 589, \"height\": 481, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 590, \"height\": 479, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 914, \"height\": 439, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1834, \"height\": 555, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 875, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 895, \"height\": 360, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 897, \"height\": 325, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 901, \"height\": 345, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 765, \"height\": 176, \"label\": \"Table\"}, {\"url\": \"assets/tables/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 766, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 580, \"height\": 201, \"label\": \"Table\"}, {\"url\": \"assets/tables/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 830, \"height\": 540, \"label\": \"Table\"}, {\"url\": \"assets/tables/osdi-2026-usenix/osdi-2026-murakkab-resource-efficient-agentic-workflow-orchestration-in-cloud-platforms/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 914, \"height\": 539, \"label\": \"Table\"}]"
motivation: 代理工作流服务中组件分散且耦合，导致资源浪费和服务质量下降，缺乏系统级的资源权衡。
method: Murakkab 引入声明式抽象，将工作流组件解耦，支持跨精度、延迟、能耗和成本的联合优化与资源调度。
result: 该系统提升了代理工作流服务的资源效率，有助于满足服务水平目标，但摘要未给出具体实验数据。
conclusion: Murakkab 可作为代理工作流缓存调度与驱逐的基础设施，实现工作流感知的资源管理。
---

## Abstract
Agentic workflows commonly coordinate multiple models and tools with complex control logic. They are quickly becoming the dominant paradigm for AI applications. However, serving them remains inefficient with today's frameworks. The key problem is that they expose workflows as opaque sequences of model and tool calls that tightly couple agent logic with model and hardware choices. Often, these workflow components are fragmented across different entities, preventing systems from reasoning about trade-offs across accuracy, latency, energy, and cost. This leads to resource waste and degraded service-level objectives (SLOs). We present Murakkab, a resource-efficient serving system for agentic workflows. Murakkab introduces a declarative abstraction that decouples workflow specification from execution configuration. A profile-guided optimizer and adaptive runtime jointly manage the full stack: orchestrating workflow components, mapping them to models and hardware, and dynamically reconfiguring execution to satisfy user-defined SLOs. By exposing the internal structure of agentic workflows, Murakkab enables cross-layer optimization that existing frameworks and cloud schedulers cannot achieve. Our evaluation on diverse workflows shows that Murakkab reduces GPU usage by up to 2.8$\times$, energy consumption by 3.7$\times$, and cost by 4.3$\times$ while maintaining SLOs.

---

## 论文详细总结（自动生成）

# Murakkab：云平台上资源高效的代理工作流编排

## 1. 核心问题与研究动机

- **背景**：大语言模型（LLM）与多模态模型逐渐成为 AI 应用的核心，而“代理工作流”（Agentic Workflow）正在成为主流范式。这类工作流由多个模型和工具协作完成复杂任务，例如视频问答、代码生成、数学解题等。
- **核心问题**：
  - 现有框架（如 LangGraph、LangChain、LlamaIndex）把工作流实现为“不透明”的模型/工具调用序列，代理逻辑与模型选择、硬件配置**紧密耦合**，导致工作流难以被系统优化。
  - 工作流开发、代理提供商、云平台三者**分散且缺乏协调**，各自追求不同目标（质量、延迟、成本、资源利用率），造成全局资源浪费和服务等级目标（SLO）下降。
  - 工作流、代理节点、硬件三层存在大量可配置旋钮，配置空间呈组合爆炸，人工选择不可行。
- **核心洞察**：
  1. 云平台缺少对工作流内部结构和资源需求的可见性；
  2. 不同层面的配置旋钮引入精度、延迟、能耗、成本之间的复杂权衡；
  3. 配置空间复杂度随代理数量和参数数量组合增长，人工优化不可行。

## 2. 方法论：Murakkab 的设计

Murakkab 是一个面向多租户代理工作流的资源高效服务系统，核心思想是**声明式工作流规范 + 自适应、SLO 感知的运行时系统**，将“应该做什么”与“具体如何执行”分离。

### 核心思想
- **声明式抽象**：开发者用自然语言描述子任务及其数据流，不需要指定模型、硬件、资源参数。执行细节由系统自动选择和配置。
- **端到端可见性**：系统暴露工作流内部结构，使得编排（orchestration）与资源管理（resource management）统一优化，实现跨层调度、共置和复用。

### 系统生命周期与关键组件
1. **开发阶段（Development）**
   - 提供“执行器库”（Executor Library），包含 LLM、结构化组合（如 self-reflection、LLM Debate）、工具（如 OpenCV、MCP 工具）等。
   - 每个执行器有文本描述、接口规范、可配置参数列表。
   - “工作流编排器”（Workflow Orchestrator）用具备工具调用能力的 LLM 将声明式任务解析为“逻辑工作流”（Logical Workflow），即 DAG，并做类型检查。

2. **优化与部署阶段（Optimization & Deployment）**
   - 引入**Profile-Guided Optimization（PGO）**思想，建立两层 profile：
     - **工作流 profile**：记录不同工作流/执行器配置下的精度、token 负载等；
     - **模型 profile**：记录模型在不同 GPU、并行度、负载下的 TTFT、TPOT、能耗、成本等。
   - **工作流优化器（Workflow Optimizer）**：每轮优化周期（默认 60 分钟）运行一次，将逻辑工作流转换为可执行工作流，决定：
     - 工作流参数，
     - 每个执行器使用的模型/工具，
     - 硬件类型与并行度，
     - 各模型实例数量与负载分配。
   - 优化问题被建模为**混合整数线性规划（MILP）**，可最小化能耗、最小化成本，或在成本预算下最大化精度。

3. **执行阶段（Execution）**
   - 运行时接收请求及其 SLO（质量、延迟、成本，分为 best/good/fair/basic 四个等级）。
   - **自动扩缩容（Auto-Scaler）**：基于短时间窗口监控，快速扩容以避免 SLO 违反。
   - 支持动态请求：用户可不指定工作流，系统根据自然语言查询动态组合已有工作流。

## 3. 实验设计

### 工作流与场景
- 主要评估三个代表性工作流：
  - **Video Q/A**：多模态，场景检测、帧提取、语音转文字、目标检测 + LMM 问答；
  - **Code Generation**：文本型，多 LLM Debate 编写、测试、执行代码；
  - **Math Q/A**：self-reflect 结构的数学解题（放在附录）。
- 实验场景包括：
  - 单工作流优化；
  - 多工作流联合优化与复用；
  - 动态资源可用性适应；
  - DAG 感知调度（并行子任务放置）；
  - 优化周期频率敏感性分析。

### 数据与基准
- 没有公开的代理工作流生产 trace，因此使用 **Azure LLM 推理服务 24 小时生产 trace**（2024 年 5 月）中 chat 和 coding 请求近似模拟工作负载。
- 质量评估使用公开 benchmark：VideoMME、HumanEval、MATH 等。

### 对比方法
- **Static**：手工配置的静态基线（类似 LangGraph），使用 Gemma-3-27B + A100，不感知负载和 SLO 变化。
- **Mrkb Opt**：Murakkab 针对每个 workflow–SLO 组合单独优化（最小化能耗或成本）。
- **Mrkb Opt+Mult**：Murakkab 跨所有 workflow–SLO 组合联合优化，最大化模型实例的共置和复用。

## 4. 资源与算力

- 实验在 **Microsoft Azure A100 和 H100 VM** 上进行：
  - A100 VM：8 × NVIDIA A100 80GB；
  - H100 VM：8 × NVIDIA H100 80GB。
- 推理引擎：vLLM（v0.9）；语音转文字用 Speaches；目标检测用 OmDet。
- 论文没有报告训练成本；Murakkab 本身不做模型训练，只做 serving 和编排。
- Profile 构建是“轻量级”的，每种配置只测一次，但文中未给出具体 profiling 开销的量化指标。
- 优化求解用 Gurobi，MILP 时间限制 300 秒。

## 5. 实验数量与充分性

### 主要实验组
1. **单工作流优化**（Video Q/A、Code Generation、Math Q/A），分别在不同精度 SLO 和延迟 SLO 下，对比 Min-Energy 和 Min-Cost 目标；
2. **多工作流联合优化**：Video Q/A + Code Gen（70% 高精度 + 30% 低延迟），以及 Math + Code Gen，对比三种策略；
3. **动态资源约束实验**：固定 2000 个 A100，改变 H100 数量（0–500），观察资源配置调整；
4. **DAG 感知调度案例**：验证“并行 Video Q/A + Code Gen”请求在 GPU/CPU 不同放置下的延迟和资源效率；
5. **优化周期敏感性**：epoch 从 20 分钟到 6 小时，分析成本、利用率、需求欠预测率。

### 充分性与客观性
- 优点：工作流种类多样（多模态/文本/推理），SLO 覆盖质量和延迟，优化目标覆盖能耗和成本，还做了系统敏感性分析。
- 不足：
  - **对比基线过于简单**：只有“静态手工配置”一种 baseline，未与其他实际优化调度系统（如 Parrot、Autellix、Loki）直接对比；
  - **生产 trace 为近似替代**：没有真实代理工作流 trace，而是用 LLM 单模型推理 trace 映射；
  - **多工作流实验中 SLO 分布固定**（70%/30%），未做不同 SLO 比例的敏感性分析；
  - 很多具体配置细节（如表 4、表 5）放在附录，主文实验数量有限。

## 6. 主要结论与发现

- Murakkab 相比现有静态框架，在保持质量与延迟 SLO 的同时：
  - GPU 使用量最高降低 **2.8 倍**；
  - 能耗最高降低 **3.7 倍**；
  - 成本最高降低 **4.3 倍**。
- 多工作流联合优化 + 复用（Opt+Mult）相比单独优化（Opt）在 Video+Code 场景中进一步减少 GPU 21.1%、能耗 20.2%、成本 17.3%。
- 对精度 SLO 的“适度放松”可带来显著资源节省：例如 Code Gen 从 best 到 good，能耗和成本分别下降约 10.5 倍和 8.7 倍。
- Murakkab 能利用 H100 等更高效 GPU 优化能耗，在资源受限环境下动态调整分配。
- DAG 感知调度可有效使用 CPU 执行轻量模型（如 Whisper），避免 GPU 浪费，同时满足延迟 SLO。
- 优化周期存在三区域权衡（buffer 主导、平衡、不确定性主导），60 分钟为较优选择。

## 7. 优点

- **声明式抽象**设计干净，能将工作流逻辑与执行配置解耦，减少开发者负担。
- **Profile-guided optimization** 将“工作流 profile”和“模型 profile”分层，可复用、可增量更新，新模型/硬件接入成本低。
- **MILP 全局优化 + 自动扩缩容**相结合，兼顾长期资源分配和短期负载波动。
- **DAG 级可见性**支持异构任务并行、CPU/GPU 协同放置、跨工作流复用，实现了现有框架无法做到的跨层优化。
- 评估覆盖多工作流、多 SLO、多目标和资源动态性，结论具有一定说服力。

## 8. 不足与局限

- **基线偏弱**：只与一种手工静态配置对比，缺乏与其他优化 serving 系统的公平对比，无法证明 Murakkab 在真实复杂系统中的相对优势。
- **trace 近似**：用普通 LLM 推理 trace 模拟代理工作流负载，可能低估真实工作流的输入输出长度、分支结构和资源波动。
- **Profile 成本未量化**：构建大量工作流和模型 profile 需要时间和资源，论文未详细说明 profiling 的开销和更新频率。
- **MILP 扩展性存疑**：配置空间组合爆炸，MILP 在更大规模集群、更多工作流和模型下的求解时间和可扩展性未充分验证。
- **依赖 LLM 作为 orchestrator**：自动任务—执行器匹配可能有错误或不确定性问题，虽然设计中有反馈循环，但未给出其准确率和端到端影响。
- **仅评估三种工作流**：对更复杂、更长序列、含循环/条件分支的 agentic workflow 覆盖不足。
- **能耗/成本模型依赖实验环境**：结果可能受特定 GPU、vLLM 版本和配置影响，泛化性有待验证。

（完）
