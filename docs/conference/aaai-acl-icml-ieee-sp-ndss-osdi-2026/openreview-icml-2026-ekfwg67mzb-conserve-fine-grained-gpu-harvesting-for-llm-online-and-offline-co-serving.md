---
title: "ConServe: Fine-Grained GPU Harvesting for LLM Online and Offline Co-Serving"
title_zh: ConServe：面向LLM在线与离线协同服务的细粒度GPU回收
authors: "Yifan Qiao, Shan Yu, Shu Anzai, Haoran Ma, Shuo Yang, Yang Wang, Miryung Kim, Yongji Wu, Yang Zhou, Jiarong Xing, Joseph E. Gonzalez, Ion Stoica, Harry Xu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/b5f8321111d4dd01e405cd6d653f58cd0ba546b3.pdf"
tags: ["query:awc"]
score: 6.0
evidence: LLM服务中的细粒度调度与增量KV缓存管理，与代理工作流的缓存调度相关
tldr: LLM服务中在线请求对延迟敏感，离线任务可容忍延迟，但现有系统粗粒度资源管理导致GPU利用率低。ConServe 利用令牌级调度、子迭代层间抢占和增量KV缓存管理，实现细粒度资源共享，在不破坏在线延迟保证的前提下填充毫秒级GPU空闲。其KV缓存管理方法可为代理工作流中的缓存调度提供参考，通过更精细的调度和缓存利用提升推理吞吐。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: LLM服务负载波动大，GPU利用率低，粗粒度资源管理难以同时满足在线延迟和离线吞吐需求。
method: ConServe 采用令牌级调度、子迭代层间抢占和增量KV缓存管理，让离线任务填充在线请求的空闲GPU时间。
result: 该方法能有效利用GPU空闲时间，同时保持严格的在线延迟服务质量，提升整体吞吐。
conclusion: ConServe 展示了LLM服务中的细粒度缓存调度和资源管理技术，可支持代理工作流的缓存调度优化。
---

## Abstract
Large language model (LLM) serving demands low latency and high throughput, but high load variability leads to significant GPU under-utilization. In this paper, we identify a synergistic but overlooked opportunity to co-serve latency-critical online requests alongside *latency-tolerant offline* tasks, which existing systems fail to exploit because their coarse-grained resource management introduces interference.
We present ConServe, a co-serving system that enables fine-grained resource sharing through latency-aware token-level scheduling, sub-iteration layer-wise preemption, and incremental KV-cache management. These mechanisms allow offline execution to fill *millisecond-scale* GPU idle time while preserving strict online latency guarantees. Across real-world workloads with Llama-3.1 and Qwen-2.5 models, ConServe improves throughput by 2.2$\times$ on average and reduces online tail latency by 2.9$\times$ over state-of-the-art systems.

---

## 论文详细总结（自动生成）

## 论文总结：ConServe — 面向LLM在线与离线协同服务的细粒度GPU回收

### 1. 核心问题与整体含义
- **研究背景**：大语言模型（LLM）服务要求低延迟与高吞吐，但实际负载波动剧烈，导致GPU利用率显著不足。
- **核心问题**：在线请求对延迟极度敏感，而离线任务（如批量分析）可以容忍延迟。现有系统由于采用粗粒度的资源管理方式，在混合调度在线与离线任务时会产生严重干扰，因此未能利用两者互补的调度机会。
- **整体含义**：需要一种能同时满足在线延迟服务质量（SLO）与离线吞吐需求的细粒度资源共享机制，以提升GPU整体利用率。

### 2. 方法论
- **核心思想**：通过细粒度的调度与抢占，让离线任务“填充”在线请求产生的毫秒级GPU空闲时间，同时严格保证在线请求的延迟。
- **关键技术**：
  - **延迟感知的令牌级（token-level）调度**：将调度单位从请求或批处理层细化到令牌粒度，以更灵活地穿插执行在线与离线任务。
  - **子迭代层间抢占（sub-iteration layer-wise preemption）**：允许在模型迭代的中间层进行抢占，相比整层或整请求抢占更精细，能快速响应在线请求，并最小化离线任务的资源浪费。
  - **增量KV缓存管理（incremental KV-cache management）**：通过管理KV缓存的增量状态，减少抢占与恢复时的开销，保证离线任务可以安全暂停和恢复。
- **整体流程**：系统实时监控在线请求到达，在毫秒级空闲窗口内启动离线计算；一旦在线请求到达，立即通过子迭代抢占暂停离线任务，并在KV缓存支持下快速恢复在线推理，从而同时获得高吞吐与低延迟。

### 3. 实验设计
- **测试模型**：Llama-3.1 和 Qwen-2.5 系列模型。
- **负载类型**：真实世界（real-world）在线与离线混合负载。
- **对比基准**：与当前最先进（state-of-the-art）的相关系统进行对比（具体名称未在摘要中列出）。
- **评估指标**：吞吐量（throughput）和在线尾延迟（tail latency）。
- **说明**：摘要中未提供具体数据集名称、请求混合比例、延迟分布等详细设置。

### 4. 资源与算力
- **未明确说明**：摘要中未提及GPU型号、数量、集群规模或训练/推理时长等具体算力信息。
- 只能推断使用了支持Llama-3.1和Qwen-2.5等模型的实际GPU环境，但无法确认具体硬件配置。

### 5. 实验数量与充分性
- **摘要层面信息有限**：仅给出了平均吞吐提升2.2倍、尾延迟降低2.9倍的总体结果，未提供实验组数、消融实验、不同负载下的详细对比。
- **充分性评估**：由于获取到的内容仅为摘要，无法判断实验的全面性与公平性。需要查看论文全文中的详细实验章节，才能评估是否涵盖不同QPS、不同模型规模、不同混合比例等场景。
- **潜在偏差**：摘要中未报告误差棒、多次重复实验或统计显著性检验，因此结果的稳健性未知。

### 6. 主要结论与发现
- ConServe 通过细粒度资源共享，在保持严格在线延迟服务质量的前提下，有效利用了GPU空闲时间。
- 与最先进系统相比，平均吞吐量提升约 2.2 倍，在线尾延迟降低约 2.9 倍。
- 证明令牌级调度 + 层间抢占 + 增量KV缓存管理的组合是协同在线/离线任务的有效方案。

### 7. 优点
- **细粒度调度**：令牌级粒度比传统请求/批级别调度更灵活，能捕捉毫秒级空闲窗口。
- **子迭代抢占**：降低抢占开销，使在线请求能被快速插入执行，同时减少离线任务的失效损失。
- **KV缓存管理**：针对LLM推理特有的缓存状态进行增量管理，提升切换效率，具有工程实用价值。
- **问题切中要害**：针对GPU利用率低这一真实痛点，提出的在线/离线协同思路具有较高应用价值。

### 8. 不足与局限
- **信息不完整**：由于获取内容仅包括摘要，无法对完整方法、实验设定、系统实现细节进行深入评价。
- **实验细节缺失**：缺少数据集、负载特性、硬件配置、基线系统的具体实现和调参方式，难以判断结果的可复现性。
- **基准覆盖**：仅提及两个模型家族，未展示不同规模（如7B/70B/405B）、不同架构（如MoE）下的表现，泛化性存疑。
- **潜在工程限制**：细粒度调度与抢占会引入额外系统开销；对KV缓存的管理也可能增加内存压力；该方案是否适用于多租户、多卡并行等复杂场景未在摘要中说明。
- **未讨论安全性**：离线任务抢占频繁可能影响其自身吞吐稳定性，摘要未分析对离线作业效能的负面影响。

（完）
