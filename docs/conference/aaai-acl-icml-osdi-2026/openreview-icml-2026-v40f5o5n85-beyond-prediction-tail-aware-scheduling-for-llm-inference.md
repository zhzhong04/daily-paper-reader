---
title: "Beyond Prediction: Tail-Aware Scheduling for LLM Inference"
title_zh: 超越预测：面向LLM推理的尾延迟感知调度
authors: "Yueying Li, Yuanfan Chen, Jiayang Chen, Esha Choukse, Haoran Qiu, G. Edward Suh, Rodrigo Fonseca, Ziv Scully, Udit Gupta"
date: 2026-04-30
pdf: "https://openreview.net/pdf/14985be222c6392883fbb3d19d980cc9c4e34a84.pdf"
tags: ["query:awc"]
score: 6.0
evidence: 面向LLM推理的缓存感知调度，可迁移至智能体工作流
tldr: LLM服务的解码长度高度可变，依赖预测长度的调度器在分布偏移和突发流量下会失效，且难以控制P90-P99尾延迟。本文提出一种分布感知、免预测的调度框架，用轻量统计信号和γ参数化的软优先级提升替代显式长度预测，并联合优化缓存感知的抢占决策。系统在无长度先验时也能稳定改善请求级尾延迟，同时保持高吞吐。该方法让LLM推理调度在实际负载下更为鲁棒，对智能体调用LLM的场景具有直接应用价值。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 预测驱动的调度策略对分布偏移和内存压力脆弱，尾部延迟难以控制。
method: 提出免预测、基于γ参数优先级提升的调度框架，并与缓存感知抢占联合优化。
result: 在无长度预测情况下改善P90-P99尾部延迟，同时保持高吞吐。
conclusion: 提供更鲁棒的LLM调度方案，适用于智能体调用LLM的场景。
---

## Abstract
LLM serving exhibits extreme length variability, making size-based scheduling difficult in practice. Recent LLM schedulers approximate SJF/SRPT using predicted decode lengths or rank and primarily report mean-centric metrics (e.g., TTFT/TBT). We show these prediction-driven policies can be fragile under distribution shifts, bursty arrivals, and GPU memory pressure, and still offer limited control over tail latency (P90–P99) that dominates user experience—even with perfect decode-length knowledge. We introduce a distribution-aware, prediction-free scheduling framework that replaces explicit length prediction with soft, $\gamma$-parameterized priority boosting driven by lightweight statistical signals. Our design co-optimizes scheduling with cache-aware preemption to account for memory-coupled decode dynamics that vary across workload mixes. Evaluated on Azure production traces, our method achieves a P99 TTLT up to 35--50\% lower than SRPT with perfect length prediction and a TTFT 34--47\% lower across various workloads, including reasoning-heavy and chat-heavy tasks, demonstrating a robust alternative for tail-latency optimization in online LLM serving.

---

## 论文详细总结（自动生成）

# 论文总结：Beyond Prediction: Tail-Aware Scheduling for LLM Inference

## 1. 核心问题与整体含义

- **研究背景**：LLM 在线推理服务中，每个请求的解码长度差异极大，这使得基于“请求大小”的经典调度策略（如 SJF/SRPT）在实际系统中很难直接应用。
- **已有方法的不足**：现有 LLM 调度器通常用预测的解码长度或优先级排序来近似 SJF/SRPT，同时主要关注平均类指标（如 TTFT/TBT）。这些方法在以下情况下会变得脆弱：
  - 工作负载分布发生偏移（distribution shifts）；
  - 请求到达具有突发性（bursty arrivals）；
  - GPU 内存压力较大时行为不稳定。
- **核心痛点**：即使拥有**完美的解码长度预测**，现有策略对用户感知影响最大的尾部延迟（P90–P99）仍然缺乏有效控制。
- **总体意义**：论文主张放弃“预测长度”这一不稳定前提，转而使用分布感知、免预测的调度框架，以求在真实生产负载下更鲁棒地优化尾延迟，同时保持高吞吐。

## 2. 论文提出的方法论

- **核心思想**：设计一个**分布感知（distribution-aware）**、**免预测（prediction-free）**的调度框架，取代显式的解码长度预测。
- **关键技术手段**：
  - 使用**轻量统计信号**（lightweight statistical signals）来刻画当前负载和请求状态；
  - 引入 **γ 参数化的软优先级提升（soft, γ-parameterized priority boosting）**，让调度器在不依赖精确长度预测的前提下，动态调整请求优先级；
  - 将调度与**缓存感知的抢占（cache-aware preemption）**联合优化，以处理不同工作负载混合下“内存-解码”相互耦合的动态特性。
- **公式 / 算法流程**：摘要中未给出具体公式，但从文字描述可以推断其流程大致为：
  1. 对到达请求提取轻量统计特征；
  2. 利用 γ 参数计算软优先级提升量；
  3. 在调度决策中综合考虑当前 GPU 缓存状态；
  4. 在必要时触发缓存感知的抢占，而不是简单按预测长度排队。

## 3. 实验设计

- **数据来源**：使用 **Azure 生产环境 trace** 进行评估。
- **工作负载场景**：覆盖多种混合负载，包括：
  - reasoning-heavy（推理/思维链型）任务；
  - chat-heavy（多轮对话型）任务。
- **对比方法**：
  - 主要是与 **SRPT（Shortest Remaining Processing Time）配合“完美长度预测”** 进行对比；
  - 这是一个很强的理想化基线——即假设系统知道每个请求的真实解码长度。
- **评估指标**：
  - **P99 TTLT**（Time To Last Token，整体生成完成时间）：论文报告比完美预测 SRPT 低 35–50%；
  - **TTFT**（Time To First Token，首 token 延迟）：在不同工作负载下比完美预测 SRPT 低 34–47%。

## 4. 资源与算力

- 论文摘要与元数据中**未明确说明**使用的 GPU 型号、数量、训练/评估时长、集群规模等算力信息。
- 因此无法从目前提供的材料中评估其硬件资源开销和实验成本。若要判断方法在真实系统中的部署成本，还需要查看论文正文的实验设置部分。

## 5. 实验数量与充分性

- 从摘要可见的实验维度包括：
  - 多个生产 trace 场景；
  - 多种负载类型（reasoning-heavy 与 chat-heavy）；
  - 多项关键指标（P99 TTLT、TTFT）。
- **充分性评估**：
  - 优点是使用真实生产数据作为 benchmark，且覆盖两种典型 LLM 负载，使结果具有一定代表性；
  - 但就摘要而言，**没有展示消融实验**（例如去掉缓存感知抢占、改变 γ 参数的影响）；
  - 也没有与更多现有 LLM 调度系统（如 FastServe、vLLM 相关调度、其他预测式调度器）逐一对比；
  - 没有说明重复实验次数、置信区间或统计显著性；
  - 因此仅从摘要看，**实验丰富度有限，难以完全验证方法的通用性和稳定性**。

## 6. 主要结论与发现

- 预测驱动型调度策略在长度分布偏移、突发流量和内存压力下表现脆弱，并且难以控制 P90–P99 尾延迟。
- 所提出的免预测、分布感知调度框架，在**没有长度先验信息**的情况下，仍能显著改善请求级尾延迟：
  - P99 TTLT 比“完美预测 SRPT”低 35–50%；
  - TTFT 比“完美预测 SRPT”低 34–47%。
- 说明了“软优先级提升 + 缓存感知抢占”比“精确长度预测 + 短作业优先”在实际生产负载中更鲁棒。

## 7. 优点

- **免预测设计**：不依赖预测模型的准确性，避免了分布偏移带来的系统性失效，更具实用价值。
- **关注尾延迟**：强调 P90–P99 对用户体验的主导作用，而非仅看均值，研究视角更贴近真实服务需求。
- **联合优化调度与缓存**：将内存/缓存状态纳入抢占决策，符合 LLM KV cache 解码过程中的实际瓶颈。
- **强基线对比**：与“完美预测 SRPT”对比，能清晰说明即使拥有理想信息，传统调度思路也不如所提方案，结论具有较强说服力。
- **生产环境验证**：使用 Azure 生产 trace 并覆盖 reasoning-heavy 与 chat-heavy 负载，结果具有一定真实性。

## 8. 不足与局限

- **信息不完整**：本文可获取的只有摘要和元数据，无法确认完整的算法细节、实验设置和资源消耗。
- **实验覆盖面有限**：摘要中仅提及 SRPT 对比，缺少与多种现代 LLM 调度器的横向比较。
- **缺少消融分析**：没有说明 γ 参数、统计信号、缓存感知抢占各自贡献多少，方法设计的必要性仍需更细致实验支撑。
- **未讨论开销**：统计信号采集、在线 γ 调整、缓存感知抢占决策本身的 CPU/GPU 开销未被披露。
- **未讨论公平性与 SLO**：对于多用户场景下的公平性、请求饥饿问题，以及更细粒度 SLO（如 TTFT 与 TBT 联合约束）未在摘要中涉及。
- **应用限制**：结论主要来自 Azure 生产 trace，可能无法直接推广到其他云环境、自建集群或不同模型架构。
- **元数据评分**：该论文在 OpenReview 上的得分为 6.0，属于中规中矩的录用分数，暗示审稿人可能对贡献度或实验验证存在一定保留。

（完）
