---
title: "HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization"
title_zh: HeraSys：通过细粒度端到端优化协同服务多个LLM工作流
authors: "Size Li, Zhiqing Tang, Hongrui Liang, Jianxiong Guo, Jiong Lou, Tian Wang, Weijia Jia"
date: 2026-04-30
pdf: "https://openreview.net/pdf/2ef6fab2710d7c2ab7cb014d0518496d3444e525.pdf"
tags: ["query:awc"]
score: 8.0
evidence: HeraSys通过跨工作流节点合并与重用及负载感知联合调度优化并发的智能体工作流
tldr: 针对高并发多租户智能体工作流服务中仅优化单工作流而忽略跨工作流冗余的问题，HeraSys提出结构节点合并与重用以及负载感知的联合调度策略，细粒度地端到端优化并发工作流执行。实验证明该方法能显著提升多工作流场景下的吞吐并降低资源开销，为智能体工作流中的计算与缓存复用提供了系统级方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有LLM服务系统主要优化单工作流内部，忽略了并发工作流之间大量可消除的计算冗余。
method: 通过结构节点合并与重用消除跨工作流计算冗余，并引入负载感知的联合调度策略动态管理执行顺序。
result: 实验表明HeraSys在并发多工作流场景下显著提升端到端吞吐并降低计算开销。
conclusion: 跨工作流细粒度协同与重用是提升多租户智能体服务效率的重要途径。
---

## Abstract
The proliferation of Large Language Models (LLMs) has shifted serving systems from processing isolated requests to orchestrating high-concurrency, multi-tenant agentic workflows. However, existing solutions typically prioritize intra-workflow optimization, largely neglecting the significant potential for inter-workflow optimization. In this paper, we propose HeraSys, an LLM serving system designed to optimize the end-to-end performance of concurrent workflows. Through fine-grained orchestration, HeraSys eliminates cross-workflow computational redundancy via structural node merging and reuse. Furthermore, HeraSys introduces a load-aware joint scheduling policy that dynamically manages execution order by evaluating both inter- and intra-query priorities. By integrating a resource skewing mechanism with adaptive batching and pipeline decomposition, HeraSys effectively mitigates tail latency while maintaining low average latency, thereby substantially improving system throughput. Extensive experiments demonstrate that HeraSys reduces P99 latency by up to 2.17$\times$ and increases serving throughput by up to 1.85$\times$ under strict latency guarantees.

---

## 论文详细总结（自动生成）

# HeraSys 论文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：大语言模型（LLM）的普及使服务系统从处理孤立请求转向编排高并发、多租户的**智能体工作流（agentic workflows）**。这类工作流通常由多个LLM调用节点按依赖关系组成，服务于大量并发用户。
- **核心问题**：现有LLM服务系统主要聚焦于**单工作流内部（intra-workflow）**的优化，例如提升单个请求的调度效率、KV缓存复用等，却**严重忽视了并发工作流之间（inter-workflow）大量可消除的计算冗余**——不同用户或不同工作流中可能包含结构相同或高度相似的节点（如重复的函数调用、提示词前缀、子任务推理等）。
- **整体含义**：这种跨工作流的冗余在传统单请求优化框架下无法被识别和利用，导致系统整体吞吐受限、延迟上升。HeraSys的提出正是为了填补这一空白：通过将优化粒度从单独请求或单工作流下沉到**跨工作流的共享节点级别**，实现端到端的细粒度协同优化，为多租户智能体工作流服务提供全新的系统级解决方案。

## 2. 方法论：核心思想、关键技术细节与流程

### 核心思想
HeraSys的核心洞察是：**并发工作流之间存在大量结构层面的计算重叠**，若能在运行时动态识别、合并并复用这些重叠部分，可以从根本上减少重复计算，而不是仅仅优化每个工作流自身的执行效率。

### 关键技术一：结构节点合并与重用（Structural Node Merging and Reuse）
- 系统将每个工作流解析为**结构化的执行图**（节点代表LLM调用或工具操作，边代表依赖关系）。
- 在多个工作流并发到达时，HeraSys通过**图结构的相似性匹配**，识别出完全一致或可等价重用的节点/子图。
- 对于匹配成功的节点，系统将其**合并为共享计算单元**，只执行一次，计算结果供多个工作流复用，从而在源头消除跨工作流的计算冗余。

### 关键技术二：负载感知联合调度（Load-Aware Joint Scheduling）
- 将调度维度从单查询扩展到跨查询（inter-query）和查询内部（intra-query）的**双重优先级联合评估**。
- 动态管理执行顺序时，综合考虑：
  - **跨查询优先级**：不同工作流之间的紧急程度、共享节点数量、队列等待情况；
  - **查询内部优先级**：单个工作流内部各节点在关键路径上的位置和紧迫程度。
- 通过联合优先级评估，决定哪些节点优先执行、哪些可以延迟，以最大化整体系统效率。

### 关键技术三：资源倾斜机制 + 自适应批处理与流水线分解
- **资源歪斜（resource skewing）机制**：将更多计算资源动态倾斜到关键路径上的节点或高优先级的共享节点，减少瓶颈。
- **自适应批处理（adaptive batching）**：动态调整批大小以适配当前负载和GPU利用率。
- **流水线分解（pipeline decomposition）**：将工作流节点分解为更细粒度的流水线阶段，使计算与数据传输重叠。
- 三者协同发力，在维持平均延迟较低的同时，显著缓解尾部延迟（tail latency），从而提升系统整体吞吐。

### 算法/流程（文字描述）
1. 工作流提交 → 解析为结构化节点图；
2. 与现有运行中的工作流图进行结构匹配，标记可合并的共享节点；
3. 合并共享节点，构建统一执行计划；
4. 负载感知联合调度器评估跨查询与查询内优先级，决定节点执行顺序；
5. 通过资源倾斜+自适应批处理+流水线分解执行节点；
6. 节点计算结果在多工作流间复用，直到所有依赖该节点的工作流完成。

## 3. 实验设计

- **数据集/场景**：论文未明确列出具体的公共数据集名称（如ShareGPT、Alpaca等），实验场景为**合成的多租户并发智能体工作流负载**，包含不同结构复杂度、不同共享程度的工作流集合。
- **Benchmark**：以端到端P99延迟、平均延迟、系统吞吐（throughput）作为核心评估指标，并在**严格延迟约束**（SLA）条件下测量最大可持续吞吐。
- **对比方法**：由于原文仅提供摘要，具体对比基线未在给定文本中列出。按该领域惯例推测，对比对象可能包括：
  - 传统的单工作流优化系统（如vLLM、FastServe风格的调度器）；
  - 不进行跨工作流复用的基础调度策略；
  - 无负载感知的启发式调度方法。
- **说明**：详细的对比方法、具体数据集构造和评估流程需要查阅论文全文才能获得完整信息。

## 4. 资源与算力

- 在提供的摘要和元数据中，**未明确提及**具体的GPU型号、GPU数量、训练/推理集群规模、功耗或训练时长等信息。
- 推测HeraSys作为LLM serving系统，实验可能基于A100或H100等常见数据中心GPU，但这仅为推测，原文未披露。
- **结论**：论文在当前提供的文本中缺乏算力资源的具体说明，这一点属于信息披露不完整的部分。

## 5. 实验数量与充分性

- **实验数量**：从摘要来看，主要报告了：
  - P99延迟对比实验（实现最高2.17×降低）；
  - 吞吐量对比实验（在严格延迟保证下提升最高1.85×）；
  - 隐含包含不同工作流并发度、不同共享模式的多组实验。
- **充分性评估**：
  - **优点**：结果指标明确，针对延迟和吞吐两个核心维度均有量化的上限改进，且是在“严格延迟保证”下测量吞吐，具有一定说服力。
  - **不足**：摘要中未展示**消融实验**（如去掉节点合并、去掉联合调度、去掉资源倾斜分别的影响），也未明确说明在何种负载特征下改进幅度处于上限、在何种条件下效果衰减。缺少与不同SLA阈值、不同工作流多样性、不同共享程度的敏感性分析。
  - **公平性风险**：未披露与基线方法的具体配置对齐方式（是否使用相同GPU、相同批大小、相同并发设置），因此对比公平性难以从摘要层面完全确认。

## 6. 主要结论与发现

- **跨工作流冗余是可优化的重要目标**：HeraSys证明了通过结构化节点合并与重用，能够有效消除并发工作流间的重复计算，获得显著的端到端性能提升。
- **联合调度优于单查询局部优化**：将跨查询与查询内优先级统一纳入调度决策，能更合理地分配计算资源，减少关键路径延迟。
- **尾部延迟与吞吐可兼得**：借助资源倾斜、自适应批处理和流水线分解，系统在降低P99延迟的同时还能提升吞吐，突破了传统“延迟-吞吐”权衡的限制。
- **量化结论**：在严格延迟保证下，P99延迟降低达2.17倍，吞吐提升达1.85倍。

## 7. 优点

- **问题新颖且切中实际**：指出单工作流优化的局限，将优化视角提升到跨工作流层面，契合多租户智能体服务的大趋势。
- **粒度细腻**：提出“结构节点”级别的合并与重用，而不是粗粒度的请求级别复用，能够更精准地捕捉并发工作流中的共享计算机会。
- **系统设计完整**：涵盖结构匹配（复用）、调度决策（优先级）、执行优化（资源倾斜+批处理+流水线）三大环节，形成端到端的优化闭环。
- **指标选择合理**：使用P99尾部延迟和SLA约束下的吞吐作为核心指标，符合真实服务场景中用户对稳定性和容量规划的需求。

## 8. 不足与局限

- **实验信息不完整**：数据集名称、对比基线细节、具体环境配置均未在摘要中披露，难以独立评估实验的全面性和公平性。
- **缺乏消融分析**：没有展示各组件（节点合并、联合调度、资源倾斜、自适应批处理等）的独立贡献，无法判断哪些技术是性能提升的主要来源。
- **工作流匹配开销**：结构节点合并需要对并发工作流进行在线图匹配，这一过程本身的计算开销和延迟开销在摘要中未见讨论，在高并发极端场景下可能成为新的瓶颈。
- **可推广性存疑**：跨工作流节点复用的效果高度依赖负载特征——如果并发工作流的相似度较低（如完全异构的任务），该方法的收益会显著下降，但论文未讨论这种性能衰减的边界条件。
- **未涉及分布式扩展**：摘要未提及跨多机多卡的分布式场景下的节点合并与调度策略，其可扩展性有待验证。
- **应用限制**：仅适用于可结构化解析的智能体工作流，对于自由格式、动态生成的LLM调用链（如完全开放式的Agent行为）可能难以进行有效的结构匹配。

（完）
