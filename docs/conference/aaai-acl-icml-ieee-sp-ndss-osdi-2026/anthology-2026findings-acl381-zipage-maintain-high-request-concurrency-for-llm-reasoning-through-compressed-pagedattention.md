---
title: "Zipage: Maintain High Request Concurrency for LLM Reasoning through Compressed PagedAttention"
title_zh: Zipage：通过压缩分页注意力维持LLM推理的高请求并发
authors: "Mengqi Liao, Lu Wang, Chaoyun Zhang, Bo Qiao, Si Qin, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Huaiyu Wan"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.381.pdf"
tags: ["query:awc"]
score: 7.0
evidence: KV缓存驱逐与PagedAttention结合，提供调度策略和前缀缓存
tldr: LLM推理过程中KV缓存的内存瓶颈限制了服务并发能力，现有驱逐方法难以落地。Zipage提出压缩分页注意力，将令牌级KV缓存驱逐与PagedAttention结合，并设计全面调度策略，支持前缀缓存和异步压缩。在大型数学推理任务上，Zipage在保持较高精度的同时大幅提升了请求并发度，为工业级推理引擎提供了可用的缓存驱逐方案。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1398, \"height\": 562}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 697, \"height\": 386}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 727, \"height\": 527}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 746, \"height\": 320}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1194, \"height\": 330}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1197, \"height\": 326}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1229, \"height\": 845}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 782, \"height\": 590}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1492, \"height\": 1160}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 738, \"height\": 364}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 655, \"height\": 790}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1179, \"height\": 758}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 727, \"height\": 398}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 726, \"height\": 393}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 628, \"height\": 399}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 666, \"height\": 323}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 775, \"height\": 360}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 766, \"height\": 362}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 592, \"height\": 1231}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 583, \"height\": 1231}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 594, \"height\": 1232}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 584, \"height\": 819}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 593, \"height\": 820}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 586, \"height\": 1243}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 599, \"height\": 1237}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 660, \"height\": 662}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 598, \"height\": 1631}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 597, \"height\": 1632}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 597, \"height\": 1632}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 597, \"height\": 1633}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 761, \"height\": 303}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 806, \"height\": 150}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 809, \"height\": 199}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 808, \"height\": 198}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 799, \"height\": 181}]"
motivation: KV缓存内存瓶颈限制LLM推理的高并发服务能力，现有驱逐方法难以用于工业场景。
method: 提出压缩分页注意力，融合令牌级KV驱逐与PagedAttention，并采用调度策略、前缀缓存和异步压缩。
result: 在大规模数学推理任务上，Zipage在降低内存占用的同时维持高请求并发和精度。
conclusion: Zipage为LLM推理引擎提供可落地的缓存调度与驱逐方法，有助于智能体工作流的高并发执行。
---

## Abstract
With reasoning becoming the generative paradigm for large language models, the memory bottleneck caused by KV cache during the inference phase has become a critical factor limiting high-concurrency service capabilities. Although existing KV cache eviction methods address the memory issue, most of them are impractical for industrial-grade applications. This paper introduces Compressed PagedAttention, a method that combines token-wise KV cache eviction with PagedAttention. We propose a comprehensive scheduling strategy and support prefix caching and asynchronous compression for Compressed PagedAttention. Based on this, we have developed a high-concurrency inference engine, Zipage. On large-scale mathematical reasoning tasks, Zipage achieves around 95% of the performance of Full KV inference engines while delivering over 2.1 speedup.

---

## 论文详细总结（自动生成）

# Zipage: 通过压缩分页注意力维持LLM推理的高请求并发

## 1. 论文的核心问题与整体含义（研究动机和背景）

- 随着大语言模型（LLM）向推理范式的演进（如数学、代码等复杂任务），模型在解码阶段生成的序列长度大幅增加，导致 KV cache 占用的显存急剧膨胀。
- LLM 服务系统的核心瓶颈已从“计算能力”转向“显存容量”：在长序列、高并发场景下，有限的 KV cache 内存限制了可同时服务的请求数量，制约了请求并发度。
- 现有 KV cache 驱逐（eviction）方法虽然能在算法层面降低内存占用，但在系统层面存在根本性不匹配：
  - 部分方法（如 MorphKV、R-KV、G-KV）虽能在解码过程中保持常量显存，但未与现代推理引擎（如 vLLM、SGLang）集成，缺乏连续批处理、前缀缓存等关键能力，实际吞吐量反而低于使用完整 KV cache 的引擎。
  - 另一些方法将驱逐集成到引擎中，但采用粗粒度的按页驱逐，容易丢失关键信息，损害模型性能。
  - KV-Compress 虽支持 token 级驱逐，但仅压缩输入，且破坏前缀缓存，增加预填充成本。
- 论文提出 **Compressed PagedAttention**，将 token 级别的 KV cache 驱逐与 PagedAttention 相结合，并实现工业级推理引擎 **Zipage**，在保持接近完整 KV 性能的同时显著提升请求并发度和吞吐量。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法流程

### 2.1 核心思想：Compressed PagedAttention

- 基于 PagedAttention，为每个请求设定最大 block 数量 $N_{max}$：
  - 解码阶段每个请求占用的 block 数被限制为不超过 $N_{max}$（预填充阶段可暂时超过）。
  - 当请求占用 $N \geq N_{max}$ 个 block 且最后一个 block 写满时，触发压缩操作：
    1. 根据注意力得分评估 KV cache 条目的重要性；
    2. 保留 top-k 个重要条目（$k = (N_{max}-1) \times b$）；
    3. 将保留条目重新紧凑排列到前 $N_{max}-1$ 个 block 中；
    4. 第 $N_{max}$ 个 block 保留给后续解码，其余 block 释放。
- 由此保证每个请求在解码过程中内存使用固定有上限，从而支撑高并发。

### 2.2 压缩过程的流水线

- **观测窗口（Observation Window）**：取请求最后一个 block 中最近 $w$ 个 token 的 query 状态作为重要性的评判依据，预分配 query cache $Q \in \mathbb{R}^{L \times M \times w \times h_q \times d}$。
- **最大并发约束**：通过线性规划确定最大并发 $M$，满足：
  - $m_{kv} \times N_{total} + M \times m_q \leq m_{available}$
  - $M \leq \frac{N_{total}}{N_{max}}$
- **评分函数**：基本形式为观测窗口 query 与各 key 的注意力得分；可集成 R-KV 的冗余得分、G-KV 的全局得分；观测窗口内条目标记得分 $+\infty$ 以保证保留。
- **压缩重组**：通过双指针遍历，将保留的 KV cache 条目写入紧凑的连续页位置，更新 block table。
- **Lightning Redundancy Score**：针对原始冗余得分 $O(N^2 b^2)$ 复杂度过高的问题，提出为 $O(N b^2)$ 的轻量版本，基于“相似表示具有序列局部性”的观察，仅计算同一 block 内 key 的相似度，显著降低压缩时间且性能更优。

### 2.3 混合调度（Hybrid Scheduling）

- 为 Compressed PagedAttention 设计了专门的调度策略，取代简单的“受限调度”（concurrency 不超过 $M$）。
- 规则要点：
  - 仅有运行队列中前 $M$ 个请求有资格分配 query slot；
  - 占用 block 数较少（小于 $N_{max}$）或最后一个 block 仍有足够空间、且未分配 query slot 的请求仍可继续解码；
  - 运行中无 query slot 的请求一旦不再满足条件则被阻塞；
  - query slot 释放后优先分配给运行队列中最靠前的未分配请求；
  - 若无空闲 block，触发抢占：优先移除无 query slot 的末尾请求；若全部移除完仍不足，则退化为受限调度。
- 该策略避免了受限调度导致的 block 利用率低的问题，尤其适用于短输入/短输出请求较多的混合负载。

### 2.4 共享前缀缓存（Shared Prefix Cache）

- 支持前缀共享，但压缩过程会破坏共享前缀结构（不同请求可能保留不同子集）。
- 解决方案：
  - 按 block 级别跟踪引用计数，引用数 >1 的 block 视为共享；
  - 压缩时不再原地重组，而是将目标指向新分配的 block：
    - 若共享 block 数 $N_{prefix} \geq N_{max}-1$，分配 $N_{max}-1$ 个新 block 作为压缩目标；
    - 若 $N_{prefix} < N_{max}-1$，分配 $N_{prefix}$ 个新 block，并复用请求原有的 $N_{max}-1-N_{prefix}$ 个 block；
  - 压缩完成后共享 block 引用计数减 1。
- 启用前缀共享后，新 block 需在压缩前分配，可能导致无空闲 block 的死锁，因此需要引入抢占机制（抢占最后无压缩状态的请求）。

### 2.5 异步解码与压缩

- 统计表明，压缩操作仅涉及极少数请求（约 $1/b$ 比例），且压缩时间约占解码时间的 40%–70%。
- 若串行执行压缩与解码，会不必要地延迟大量无需压缩的请求，且压缩 batch 过小导致 GPU 利用率低。
- Zipage 将压缩与解码异步执行：无需压缩的请求立即继续解码，需要压缩的请求完成压缩后加入后续解码步骤，从而提升 GPU 利用率和整体吞吐。

## 3. 实验设计

### 3.1 数据集 / 场景

- **AMC 23**：数学竞赛题，短输入、长输出，作为主要推理任务。
- **AIME 24**：更难的数学竞赛题，长输出。
- **GSM8K**：简单数学题，短输入、短输出。
- **混合负载（Mixture）**：AMC 23 + GSM8K，模拟长短输出混合场景。
- **LiveCodeBench v1**：代码生成任务。
- **LongBench 的 MultiFieldQA**：长输入、短输出场景。
- 所有评测使用温度 0.6 采样，评估指标为 pass@1、TPS、TPOT、Speedup。

### 3.2 对比方法

- **Full KV 基线**：Nano-vLLM（轻量 PagedAttention 实现）、vLLM、HF-Gen（HuggingFace generation）。
- **KV cache 驱逐方法**：MorphKV、R-KV、G-KV（解码期驱逐、常量显存，但不支持连续批处理等工业特性）。
- **消融配置**：关闭异步压缩、关闭混合调度、关闭共享前缀缓存。

### 3.3 模型规模

- Qwen3 系列：0.6B、8B、14B、32B。
- DeepSeek-R1 Distill Llama 8B（简称 DS Llama 8B）。
- 8B 及以下模型在单卡 A100 上运行，Qwen3 32B 使用 2 卡 A100 张量并行。

## 4. 资源与算力

- 所有实验使用 **A100 GPU**：
  - 除 Qwen3 32B 使用 **2 张 A100 张量并行**外，其余模型均在 **单张 A100** 上完成。
- 论文未明确说明训练/评测的总时长、具体 GPU 型号（如 40GB/80GB）以及能耗等细节。
- 也未报告每个 benchmark 的完整运行时间表，仅通过实时吞吐量图（横轴为秒）间接展示部分场景耗时（如 AMC 23 上 Zipage 约 10000 秒量级）。

## 5. 实验数量与充分性

### 5.1 实验数量

- 三大类任务（数学、代码、长文本）共 5 个数据集/负载。
- 多种模型规模（0.6B–32B，两个系列）。
- 大量消融实验：
  - 异步压缩、混合调度、共享前缀缓存的独立消融（TPS/TPOT 对比）；
  - KV cache budget 扫描（512/1024/2048/4096）；
  - 全局评分、冗余评分的消融；
  - 温度参数 $\tau$、权重 $\lambda$、衰减率 $\alpha$ 的超参数搜索；
  - pooling 策略消融；
  - Flash Redundancy Score 与 Lightning Redundancy Score 对比；
  - 不同层步长（layer stride）的效率实验。
- 与 6 种以上基线方法的对比。

### 5.2 充分性与客观性

- **优点**：实验覆盖了不同输入/输出长度分布、不同模型规模、多种预算设置，消融系统深入；同时报告了吞吐量、延迟、模型质量（pass@1）、并发行为、block 利用率等多维指标，具有较强的说服力。
- **潜在不足**：
  - 所有评测均为离线批处理推理，未评估在线服务的 TTFT 等指标；
  - 未与 RaaS、PagedEviction 等集成式压缩方法对比（作者指出其无公开代码）；
  - 超参数建议（如 $\lambda=0.2, \tau=0.4$）主要基于单一数据集 AMC 23 得出，泛化性有限；
  - 在 TPOT 指标上，由于抢占和重新排队影响，某些配置的 TPOT 反而更高，作者承认该指标在此场景下意义有限，更偏重 TPS，但公平性上仍需注意。

## 6. 论文的主要结论与发现

- Compressed PagedAttention 能够在工业级 PagedAttention 框架中实现 token 级 KV cache 驱逐，保持内存占用有界，且支持连续批处理、前缀缓存、异步压缩等关键能力。
- Zipage 在数学推理任务（AMC 23）上，以 2048 的 KV cache budget 实现约 95% 的 Full KV 性能，同时获得超过 **2.1 倍**的吞吐提升；在 AIME 24 上 4096 budget 时达到类似效果，代码任务（LiveCodeBench）在 4096 budget 下约 95% 性能、约 1.6 倍加速。
- 混合调度能有效提高短请求混合场景的 block 利用率；共享前缀缓存对长输入共享前缀场景加速明显；异步压缩在所有场景下均提升 TPS。
- Lightning Redundancy Score 将冗余评分计算时间降低到接近单步解码的水平，且相比 flash 版本性能更优。
- 较小的 KV cache budget 会导致模型性能下降并增加平均输出长度（生成更多冗余 token），影响用户体验；合理选择 budget 需要在性能、吞吐和用户体验之间权衡。

## 7. 优点

- **系统-算法协同设计**：首次将 token 级 KV cache 驱逐与 PagedAttention 完整集成，并解决了调度、前缀共享、异步执行等系统级关键问题，具有较高的工程可用性。
- **可落地的工业级方案**：相比 MorphKV、R-KV、G-KV 等纯算法方法，Zipage 直接面向实际推理引擎，兼容连续批处理与前缀缓存，弥补了相关方法难以落地的问题。
- **高效 GPU 内核优化**：针对分页 KV cache 实现了注意力评分、全局评分、冗余评分、压缩搬移等专用 Triton 内核，并提出闪电冗余评分，大幅降低压缩开销。
- **实验体系全面**：多模型、多数据集、多预算、多消融变量的实验设置，对吞吐、延迟、性能和质量均有报告，分析较为透彻。
- **共享前缀缓存的巧妙设计**：通过重定向压缩目标而非原地重组，保留共享前缀，避免一致性破坏。
- **异步压缩机制**：利用压缩请求占比极小的特性，将压缩与解码并行，显著提升 GPU 利用率和系统吞吐，思路简洁有效。

## 8. 不足与局限

- **仅离线评估**：未实现在线引擎，未报告 TTFT 等在线服务关键指标，排队时间主导时 TTFT 参考意义有限。
- **未与部分集成式方法对比**：如 RaaS、PagedEviction 因缺乏公开代码未纳入比较；KV-Compress 仅压缩输入，在长输出场景下与 vLLM 行为接近，也未充分对比。
- **固定 budget 策略**：所有请求使用相同的 KV cache 预算，未根据请求难度动态调整。作者承认可将 $N_{max}$ 作为每请求属性调整，但未来才计划实现。
- **安全与部署范围限制**：Zipage 仅面向可信单租户环境，不支持多租户隔离或对抗性共置保护，限制了其在云服务中的适用场景。
- **统计功效有限**：部分基准题目较少（如 AMC 23/40 题、AIME 24/30 题），采样次数有限（如 32 次），pass@1 的置信区间可能较宽。
- **超参数敏感性**：全局评分、冗余评分、温度等超参数对模型和任务敏感，论文仅基于少量数据集给出推荐，泛化性有待验证。
- **长输出场景的体验问题**：预算过小时输出长度显著增加（如 AMC 23 中 512 budget 时输出长度扩展到 157.7%），可能增加用户等待时间和成本。
- **未详细报告显存占用、能耗等系统数据**，对算力资源的具体需求描述不够透明。

（完）
