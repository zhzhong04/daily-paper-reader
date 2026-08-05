---
title: "Beyond Prediction: Tail-Aware Scheduling for LLM Inference"
title_zh: 超越预测：面向LLM推断的尾延迟感知调度
authors: "Yueying Li, Yuanfan Chen, Jiayang Chen, Esha Choukse, Haoran Qiu, G. Edward Suh, Rodrigo Fonseca, Ziv Scully, Udit Gupta"
date: 2026-04-30
pdf: "https://openreview.net/pdf/14985be222c6392883fbb3d19d980cc9c4e34a84.pdf"
tags: ["query:awc"]
score: 5.0
evidence: 面向LLM推断的缓存感知抢占调度，用于控制尾部延迟
tldr: 该文针对LLM服务中解码长度多样导致调度困难、预测驱动策略在分布偏移和突发流量下脆弱的问题，提出无需预测的分布感知调度框架，利用轻量统计信号进行参数化的优先提升，并与缓存感知抢占协同优化。实验显示在压力场景下能有效控制P90-P99尾延迟。虽然不针对代理工作流，但其缓存感知调度方法可迁移至代理应用的缓存调度场景。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 解决LLM服务中基于预测的长度调度在分布偏移下脆弱且难以控制尾延迟的问题。
method: 提出无预测的分布感知调度框架，使用软优先提升和缓存感知抢占共同优化。
result: 在突发流量和内存压力下显著改善尾延迟表现。
conclusion: 为LLM推断提供了一种稳健的调度与缓存协同设计。
---

## Abstract
LLM serving exhibits extreme length variability, making size-based scheduling difficult in practice. Recent LLM schedulers approximate SJF/SRPT using predicted decode lengths or rank and primarily report mean-centric metrics (e.g., TTFT/TBT). We show these prediction-driven policies can be fragile under distribution shifts, bursty arrivals, and GPU memory pressure, and still offer limited control over tail latency (P90–P99) that dominates user experience—even with perfect decode-length knowledge. We introduce a distribution-aware, prediction-free scheduling framework that replaces explicit length prediction with soft, $\gamma$-parameterized priority boosting driven by lightweight statistical signals. Our design co-optimizes scheduling with cache-aware preemption to account for memory-coupled decode dynamics that vary across workload mixes. Evaluated on Azure production traces, our method achieves a P99 TTLT up to 35--50\% lower than SRPT with perfect length prediction and a TTFT 34--47\% lower across various workloads, including reasoning-heavy and chat-heavy tasks, demonstrating a robust alternative for tail-latency optimization in online LLM serving.

---

## 论文详细总结（自动生成）

# 超越预测：面向LLM推断的尾延迟感知调度——论文总结

## 一、论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：LLM（大语言模型）在线服务中的解码长度存在极大差异（即“长度可变性”），这导致基于请求大小（size-based）的调度在实际系统中难以实现。现有的LLM调度器通常使用**预测的解码长度**来近似SJF/SRPT（短作业优先/最短剩余处理时间优先）策略，并使用SJF/SRPT策略对请求进行排序和调度。
- **现存方法的不足**：作者指出，这类**预测驱动的调度策略**存在三个主要脆弱点：
  1. **分布偏移**：预测模型在训练数据分布与实际工作负载分布不一致时，性能会急剧下降；
  2. **突发流量**：在突发性请求到达场景下，预测的准确性和调度的稳定性难以保证；
  3. **GPU内存压力**：当GPU内存受限时，调度策略与缓存/内存管理之间的耦合关系变得更加复杂，单纯的预测驱动策略难以应对。
- **被忽视的核心指标**：现有调度器主要报告**均值导向的指标**（如TTFT首次生成时间、TBT块间时间），但对**尾延迟（P90–P99）** 的控制能力有限——而尾延迟恰恰是主导用户体验的关键指标。作者强调，**即使拥有完美的解码长度预测（perfect decode-length knowledge）**，现有方法仍然无法对尾延迟提供有效控制。
- **研究意义**：该论文试图从根本上解决LLM服务中“基于预测的长度调度”在真实生产环境中鲁棒性不足的问题，提出一种不依赖显式预测、能够在负载变化和内存压力下稳健优化尾延迟的调度新范式。

## 二、论文提出的方法论

### 核心思想
- 提出一种**分布感知（distribution-aware）且无预测（prediction-free）** 的调度框架。
- 核心思路是：**用轻量级统计信号驱动的软优先级提升（soft priority boosting）来代替显式的解码长度预测**，从而避免预测误差和分布偏移带来的风险。

### 关键技术细节
1. **γ参数化的软优先提升**：
   - 引入一个可调参数 γ（gamma），对请求的优先级进行软性（而非硬性）的提升。
   - 这种参数化设计使得调度策略能够在不同负载特征（如推理密集型 vs. 聊天密集型）之间自适应地调节优先级权重。
   - 与传统的硬优先级（明确将短请求放在前面）不同，软优先级提升允许更平滑、更鲁棒的调度决策。
2. **缓存感知抢占（Cache-Aware Preemption）**：
   - 调度器将与**缓存（KV cache）相关的内存耦合解码动态**纳入考量。
   - 由于不同工作负载混合场景下的内存行为差异很大，调度策略需要与缓存管理协同优化（co-optimize），即在抢占请求时考虑其缓存占用情况和内存压力。
   - 这使调度器在GPU内存受限时能够有效管理请求的缓存资源，从而避免因内存瓶颈导致的尾延迟恶化。
3. **无需预测的调度流程**：
   - 系统不再显式估计每个请求的解码长度，而是利用请求到达时的轻量统计信号（如到达模式、当前队列长度、缓存状态等）进行实时调度决策。
   - 通过γ参数的调节，调度策略可以在“偏向短请求”和“兼顾公平/长请求”之间取得平衡。

## 三、实验设计

- **数据集/工作负载**：使用 **Azure生产环境轨迹（Azure production traces）** 进行评估，涵盖多种工作负载类型，包括：
  - **推理密集型（reasoning-heavy）** 任务；
  - **聊天密集型（chat-heavy）** 任务。
- **评估场景**：实验中考虑了多种压力条件，包括突发流量和GPU内存压力场景，以考察调度策略在非理想条件下的鲁棒性。
- **对比方法**：主要对比**SRPT（Shortest Remaining Processing Time）** 策略，并且特别强调了对比的是**具有完美解码长度预测的SRPT**（即理论上的最优基线），这是非常强的对比基线。
- **主要评估指标**：TTLT（Time To Last Token，最终生成时间）、TTFT（Time To First Token，首次生成时间）、尾延迟（P90–P99）。

## 四、资源与算力

- 论文的摘要和提取文本中**未明确说明**所使用的具体算力资源，包括GPU型号、GPU数量、训练时长、推理部署规模等。
- 从论文性质（调度系统研究）推断，其验证过程可能依赖模拟或小规模原型实现，而非大规模训练或部署，但文中未给出明确的资源清单。
- **需要指出**：由于文本提取内容有限，关于算力和实验环境的信息并不完整，读者若需准确了解软硬件配置，需查阅论文完整版本。

## 五、实验数量与充分性

- **实验组数量**：从摘要透露的信息来看，实验设计了**不同工作负载类型**（推理密集型、聊天密集型）下的评估，同时考察了**突发流量**和**GPU内存压力**等压力场景，并结合了多种指标（P99 TTLT、TTFT等）。
- **充分性评估**：
  - **积极方面**：选择“完美预测的SRPT”作为对比基线，使得实验结论具有很强的说服力——即使面对理论上最优的预测驱动方法，本文方法仍能取得显著优势。
  - **局限性**：由于可见文本只包含摘要，未提供完整的实验细节（如具体实验次数、各工作负载下更细粒度的消融实验、不同γ取值的敏感性分析等），因此无法全面评估实验的完备性和统计显著性。整体来看，实验设计思路是合理且具有针对性的，但实验覆盖面的完整程度需要进一步阅读全文确认。

## 六、论文的主要结论与发现

1. **预测驱动调度策略确实脆弱**：即使使用完美的解码长度预测，SRPT类策略在分布偏移、突发流量和GPU内存压力下仍然难以有效控制尾延迟（P90–P99）。
2. **无预测方法优于有预测方法**：本文提出的分布感知、无预测调度框架，在Azure生产轨迹上取得了显著优于“完美预测SRPT”的效果：
   - **P99 TTLT降低35%–50%**；
   - **TTFT降低34%–47%**。
3. **调度与缓存协同优化是可行的**：通过将调度决策与缓存感知抢占相结合，可以在内存受限的情况下稳健地提升尾延迟表现。
4. **稳健性增强**：该方法在不同类型工作负载（推理密集型、聊天密集型）下均表现良好，说明其具有跨场景的通用性和稳健性。

## 七、优点

- **问题选取具有现实意义**：面向LLM服务中真实存在的尾延迟问题，直接针对用户可感知的体验指标（P90–P99），而非仅关注均值指标。
- **方法论具有创新性**：抛弃显式预测，改用轻量统计信号+参数化优先级提升，从根本上规避了预测误差和分布偏移风险。
- **理论基线设定严格**：与“完美的解码长度预测的SRPT”对比，使得结果的优越性具有极强的说服力。
- **调度与缓存协同优化的视角稀缺**：将调度问题与KV cache内存管理耦合起来考虑，切中LLM服务中的实际瓶颈（内存压力下的解码动态），具有较高的工程实践价值。
- **结果显著且跨场景稳健**：在多个工作负载类型和压力条件下均取得了一致的延迟改善，说明方法具有较好的泛化性。

## 八、不足与局限

- **实验细节不完整**：摘要中未展示延时分布曲线、不同压力程度下的细粒度结果、γ参数的敏感性分析、不同负载强度下的扩展实验等，实验的深度有待全文验证。
- **没有说明算力/部署开销**：新增的统计信号感知和缓存感知抢占机制所需的额外计算开销、内存开销以及部署复杂度在摘要中未提及。
- **实际部署可行性待验证**：虽然实验结果在Azure生产轨迹上表现良好，但该轨迹可能只代表特定类型的数据中心负载，其他类型的生产环境（如边缘部署、多租户场景）是否同样适用仍不确定。
- **未讨论与现有系统的集成方式**：论文未说明如何将这种调度框架嵌入到现有的LLM serving系统（如vLLM、TGI等）中，实际落地的工程成本未知。
- **γ参数的调优依赖**：虽然γ参数化了优先级提升的强度，但如何在不同场景下自动调节γ值（还是依赖人工选择），以及其对最终性能的敏感度，需要更多说明。

（完）
