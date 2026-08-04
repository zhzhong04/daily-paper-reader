---
title: "Zipage: Maintain High Request Concurrency for LLM Reasoning through Compressed PagedAttention"
title_zh: Zipage：通过压缩Paged注意力机制维持LLM推理的高请求并发
authors: "Mengqi Liao, Lu Wang, Chaoyun Zhang, Bo Qiao, Si Qin, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Huaiyu Wan"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.381.pdf"
tags: ["query:awc"]
score: 6.0
evidence: 面向LLM推理的高并发KV缓存驱逐与调度，可应用于智能体推理
tldr: 针对大语言模型推理中KV缓存导致内存瓶颈、现有驱逐方法难以工业化的问题，本文提出压缩PagedAttention机制，将词元级KV缓存驱逐与PagedAttention结合，并设计综合调度策略，支持前缀缓存与异步压缩。基于此实现高并发推理引擎Zipage，在大规模数学推理任务上显著提升请求并发，为智能体工作流等推理服务提供了高效可用的缓存调度与驱逐方案。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1398, \"height\": 562, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 697, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 727, \"height\": 527, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 746, \"height\": 320, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1194, \"height\": 330, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1197, \"height\": 326, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1229, \"height\": 845, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 782, \"height\": 590, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1492, \"height\": 1160, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 738, \"height\": 364, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 655, \"height\": 790, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1179, \"height\": 758, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 727, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 726, \"height\": 393, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 628, \"height\": 399, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 666, \"height\": 323, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 775, \"height\": 360, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 766, \"height\": 362, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 592, \"height\": 1231, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 583, \"height\": 1231, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 594, \"height\": 1232, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 584, \"height\": 819, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 593, \"height\": 820, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 586, \"height\": 1243, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 599, \"height\": 1237, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 660, \"height\": 662, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 598, \"height\": 1631, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 597, \"height\": 1632, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 597, \"height\": 1632, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl381/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 597, \"height\": 1633, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 761, \"height\": 303, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 806, \"height\": 150, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 809, \"height\": 199, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 808, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl381/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 799, \"height\": 181, \"label\": \"Table\"}]"
motivation: KV缓存导致LLM推理服务内存瓶颈，现有驱逐方法难以满足工业级高并发需求。
method: 提出压缩PagedAttention，融合词元级KV缓存驱逐与PagedAttention，并设计调度策略及前缀缓存和异步压缩。
result: 在大规模数学推理任务上，Zipage显著提升请求并发，验证了高效性。
conclusion: 为工业级LLM推理场景提供高并发KV缓存管理方案，可支撑智能体推理服务。
---

## Abstract
With reasoning becoming the generative paradigm for large language models, the memory bottleneck caused by KV cache during the inference phase has become a critical factor limiting high-concurrency service capabilities. Although existing KV cache eviction methods address the memory issue, most of them are impractical for industrial-grade applications. This paper introduces Compressed PagedAttention, a method that combines token-wise KV cache eviction with PagedAttention. We propose a comprehensive scheduling strategy and support prefix caching and asynchronous compression for Compressed PagedAttention. Based on this, we have developed a high-concurrency inference engine, Zipage. On large-scale mathematical reasoning tasks, Zipage achieves around 95% of the performance of Full KV inference engines while delivering over 2.1 speedup.

---

## 论文详细总结（自动生成）

## 1. 核心问题与研究动机

- **背景**：随着推理型大语言模型（Reasoning LLMs）成为主流的生成范式，模型在复杂数学、代码等任务中会产生长序列输出，KV Cache 的显存占用随序列长度快速增长。KV Cache 内存瓶颈已取代计算的限制，成为制约 LLM 推理服务高并发能力的核心因素。
- **现有方法不足**：
  - 已有 KV Cache 驱逐（eviction）方法（如 MorphKV、R-KV、G-KV）能在算法层面将内存控制在恒定水平，但未与推理引擎集成，缺乏持续批处理（continuous batching）和前缀缓存（prefix caching）等现代工业级关键特性，实际吞吐量反而低于使用完整 KV Cache 的引擎。
  - 已集成到引擎中的方法（如 RaaS、PagedEviction）采用粗粒度的按页（page-wise）驱逐，容易丢失关键信息、损害模型性能。
  - KV-Compress 虽然支持 token 级驱逐，但仅压缩输入，且破坏前缀缓存，增加了预填充（prefilling）开销。
- **意义**：迫切需要一种将在工业级推理引擎中可用的 token 级 KV Cache 驱逐方法与 PagedAttention 相结合，在保持模型性能的同时显著提升请求并发与吞吐量。

---

## 2. 方法论

### 2.1 整体思路

- 提出 **Compressed PagedAttention**：将 **token 级 KV 缓存驱逐**与 **PagedAttention** 结合，在不同层和注意力头间灵活驱逐不重要的 KV 条目，并将保留条目紧凑重排，实现每请求内存有界，支持高并发。

### 2.2 核心机制

- **每请求块数上限**：每个请求在解码阶段占用的块数不超过 \(N_{\text{max}}\)（预填充阶段可暂时超出）。
- **压缩触发条件**：当请求占用的块数 \(N \ge N_{\text{max}}\) 且最后一个块已写满时，触发压缩操作；将不重要的 KV Cache 条目驱逐，保留的条目重排至前 \(N_{\text{max}} - 1\) 个块中，第 \(N_{\text{max}}\) 个块留给后续解码，其余块被释放。
- **观察窗口**：采用最后 \(w\) 个 token 的查询状态作为观测窗口，计算各 KV Cache 条目的注意力得分，并为窗口内条目分配 \(+\infty\) 得分保证其一定保留。
- **得分函数**：基础形式为注意力得分；可融合 R-KV 的冗余得分（redundancy score）和 G-KV 的全局得分（global score），用于更全面评估条目的重要性。
- **Ligntning Redundancy Score**：针对原始冗余得分 \(O(N^2 b^2)\) 计算复杂度过高的问题，利用相邻 token 表征局部相似性，将复杂度降为 \(O(N b^2)\)，同时性能优于原始版本。
- **Top-k 保留**：按分数保留最高 \((N_{\text{max}} - 1) \times b\) 个 KV 缓存条目，并通过内核重排使得 KV Cache 在页内连续紧凑。

### 2.3 混合调度（Hybrid Scheduling）

- 并发被分为「未压缩运行」与「已压缩运行」两类状态。
- 仅前 \(M\) 个运行请求有资格分配查询槽位（query slots）；请求若占块数少于 \(N_{\text{max}}\) 或最后一块剩余 token 数足够，则无需查询槽也可解码。
- 无空闲块时触发抢占，优先卸载未分配查询槽的请求，之后回退到约束调度（constrained scheduling）。

### 2.4 共享前缀缓存支持

- 以块级别共享前缀；压缩时目标块根据共享块数量 \(N_{\text{prefix}}\) 动态确定，保留共享前缀结构不被破坏。
- 启用前缀共享时可能出现死锁，因此需要抢占未压缩请求。

### 2.5 异步压缩与解码

- 解码占推理总时间约 90%，压缩约占 8-9%；每步需要压缩的请求不足 1%。
- 若压缩与解码串行执行，会拖慢大量无需压缩的请求；因此采用**异步执行机制**：可解码的请求直接继续解码，待压缩的请求完成后加入后续解码步骤，显著提升 GPU 利用率和吞吐量。

---

## 3. 实验设计

### 3.1 模型与数据集

- **模型**：Qwen3 系列（0.6B、8B、14B、32B）及 DeepSeek-R1 Distill Llama 8B（DS Llama 8B）。
- **数据集/基准**：
  - **AMC 23**（数学，短输入长输出）
  - **AIME 24**（数学）
  - **GSM8K**（数学，短输入短输出）
  - **AMC 23 + GSM8K 混合负载**
  - **LiveCodeBench v1**（代码）
  - **LongBench 的 MultiFieldQA 子集**（长输入短输出）
- **评估指标**：TPOT（每输出 token 时间）、TPS（tokens/s）、pass@1、加速比（Speedup）。

### 3.2 对比方法

- HF-Gen（HuggingFace 生成，Full KV 基线）
- MorphKV、R-KV、G-KV（解码期驱逐方法，不具备持续批处理能力）
- vLLM v0.13.0（成熟的工业级推理引擎）
- Nano-vLLM（轻量级 PagedAttention 实现）
- 消融实验：禁用异步压缩、禁用共享前缀、禁用混合调度

---

## 4. 资源与算力

- **GPU**：Qwen3 32B 使用 **2 张 NVIDIA A100 GPU** 张量并行；其余模型均在 **单张 A100 GPU** 上运行。
- 论文**未明确说明**训练/调优时长、GPU 总时数及能耗数据。
- 采样温度为 0.6；KV Cache 预算默认设为 2048；块大小 \(b=256\)，窗口大小 \(w=16\)。
- 模型均为现有开源预训练模型，本工作不涉及训练，只做推理评估。

---

## 5. 实验数量与充分性

### 5.1 实验数量

- **效率分析**：Qwen3 8B 在 3 种负载（AMC 23、混合负载、LongBench）下进行主实验与 3 项消融实验，以及和 Nano-vLLM 的多维度对比。
- **与其他框架对比**：Qwen3 8B 和 DS Llama 8B 在 AMC 23 上与 6 种基线对比 TPS 和 pass@1。
- **KV Cache 预算影响**：在 3 个数据集 × 3 个模型规模 × 4 种预算（512/1024/2048/4096）下评估 pass@1、平均输出长度、TPS 和加速比。
- **不同模型规模**：Qwen3 0.6B/8B/14B/32B 和 DS Llama 8B 在 AMC 23 上的 TPS/pass@1 与实时吞吐曲线。
- **内核设计细节实验**：层步长（layer stride）、衰减率 \(\alpha\)、\(\lambda\) 与温度 \(\tau\) 的联合搜索、池化策略等（附录 C）。

### 5.2 充分性与客观性

- **优点**：实验覆盖多个模型规模、多种推理负载类型（数学、代码、长文档）、多个 KV 预算档位；提供了丰富的消融实验和实现细节参数搜索。
- **不足**：所有的效率实验均基于离线推理模式，未实现在线服务引擎，未报告 TTFT（首个 token 时间）；无法直接验证在线动态请求到达场景中的表现。与同样集成 KV 压缩到引擎的 RaaS、PagedEviction 未做对比（无公开代码）。

---

## 6. 主要结论与发现

- Zipage 在数学推理任务上（AMC 23，KV budget=2048）达到 Full KV 引擎约 **95% 的模型性能**，同时带来 **超过 2.1× 的吞吐加速**。
- 在 KV budget=4096 时，AMC 23 与 AIME 24 上的性能均接近 Full KV（约 95% 以上），吞吐提升 2 倍以上；代码任务约 95% 性能、约 1.6 倍加速。
- Zipage 在相同并发区间下较 Nano-vLLM 的逐步解码时间更短，且能在高并发区间（100-200）长时间稳定运行，而 Nano-vLLM 的并发呈现低并发周期性波动。
- 异步压缩、共享前缀缓存和混合调度各自在不同负载下都能带来显著吞吐收益。
- 随着 KV 预算减小，不仅性能下降，平均输出长度还会增加，可能有损用户体验。

---

## 7. 优点（论文亮点）

- **系统级可行性**：将 token 级 KV 驱逐直接融入 PagedAttention 调度框架，补齐了此前算法级驱逐方法和工业级引擎之间的鸿沟。
- **工业级特性齐备**：支持持续批处理、共享前缀缓存、异步压缩/解码，与现代推理引擎（vLLM、SGLang）生态兼容。
- **精细粒度驱逐**：per-token、per-layer、per-head 的内存控制，避免页面级驱逐导致的关键信息丢失。
- **高效内核优化**：跨层并行压缩、闪电冗余得分（O(N²b²) → O(Nb²)）等实现大幅压缩了压缩过程耗时。
- **丰富的消融与超参数分析**：对 layer stride、\(\alpha\)、\(\lambda\)、\(\tau\)、池化策略等给出了系统性的实验和推荐配置。

---

## 8. 不足与局限

- **仅离线评估**：尚未实现在线服务引擎，未报告 TTFT；在线场景存在排队时延，结论不能直接推广到动态服务环境。
- **未对比集成式方法**：因 RaaS 和 PagedEviction 没有公开代码，未能与同样做系统级 KV 压降低对比。
- **固定预算限制**：不同难度请求共享固定 KV 预算，未实现按请求实际长度动态调整 \(N_{\text{max}}\)。
- **安全边界**：假设可信单租户部署环境，未考虑多租户隔离和对抗性共驻防护。
- **泛化性局限**：超参数推荐（如 \(\lambda=0.2\)、\(\tau=0.4\)、\(\alpha=0.8\)）主要基于 AMC 23 单一数据集评估，缺乏跨数据集的广泛验证。
- **模型覆盖有限**：主要基于 Qwen 和 DS Llama 系列，未覆盖更多架构（如 Mixtral、Command R 等）。

---

（完）
