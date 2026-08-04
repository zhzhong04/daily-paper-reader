---
title: "Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling"
title_zh: 简单即更好：乘法或许就是LLM请求调度所需的一切
authors: "Dingyan Zhang, Jinbo Han, Kaixi Zhang, Xingda Wei, Sijie Shen, Chenguang Fang, Wenyuan Yu, Jingren Zhou, Rong Chen"
date: 2026-01-01
pdf: "https://arxiv.org/pdf/2603.15202v3"
tags: ["query:agent-cache"]
score: 6.0
evidence: 面向KV缓存感知的请求调度指标，可迁移到智能体工作流中的调度与缓存管理
tldr: LLM请求调度需要在路由实例具备KVCache与负载均衡之间权衡，现有组合方法复杂且需调参。本文提出将两个精心选择的指标——一个KVCache感知、一个负载感知——直接相乘，得到简单而有效的调度分数。该方法无需复杂模拟器，便可同时保证缓存命中与负载均衡。对于智能体工作流中的缓存感知调度具有直接借鉴价值。
source: OSDI-2026-USENIX
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 750, \"height\": 284, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 781, \"height\": 385, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 718, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 826, \"height\": 466, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1741, \"height\": 489, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 738, \"height\": 466, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 860, \"height\": 225, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 844, \"height\": 264, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 850, \"height\": 290, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 855, \"height\": 257, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1698, \"height\": 785, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 755, \"height\": 378, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 830, \"height\": 186, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1817, \"height\": 772, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 735, \"height\": 248, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1561, \"height\": 703, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 777, \"height\": 195, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 774, \"height\": 289, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 759, \"height\": 681, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 839, \"height\": 442, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 811, \"height\": 352, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 808, \"height\": 249, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 878, \"height\": 1113, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 806, \"height\": 287, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 795, \"height\": 214, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1694, \"height\": 984, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1736, \"height\": 324, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 849, \"height\": 242, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 819, \"height\": 392, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1736, \"height\": 292, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-031.webp\", \"caption\": \"\", \"page\": 0, \"index\": 31, \"width\": 739, \"height\": 391, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-032.webp\", \"caption\": \"\", \"page\": 0, \"index\": 32, \"width\": 846, \"height\": 388, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-033.webp\", \"caption\": \"\", \"page\": 0, \"index\": 33, \"width\": 829, \"height\": 519, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-034.webp\", \"caption\": \"\", \"page\": 0, \"index\": 34, \"width\": 750, \"height\": 389, \"label\": \"Figure\"}, {\"url\": \"assets/figures/osdi-2026-usenix/osdi-2026-simple-is-better-multiplication-may-be-all-you-need-for-llm-request-scheduling/fig-035.webp\", \"caption\": \"\", \"page\": 0, \"index\": 35, \"width\": 853, \"height\": 599, \"label\": \"Figure\"}]"
motivation: 现有调度方法为兼顾缓存与负载均衡而设计复杂组合，难以调优且可能次优。
method: 使用两个指标（KV缓存感知与负载均衡）的乘法作为调度分数，简单无需调参。
result: 实验证明乘法组合在多种工作负载下优于复杂调度策略。
conclusion: 简单的乘法指标即可高效平衡缓存可用性与负载均衡，可用于请求调度。
---

## Abstract
High-quality LLM request scheduling requires meeting two key objectives: ensuring the routed instance has KVCache to accelerate request execution, and ensuring that the workload is balanced across instances. Achieving both objectives is challenging because pursuing one may compromise the other. Current approaches use various combinators (e.g., linear combinations) to compute a scheduling score that combines indicators for the two objectives. These approaches are complex: they either require significant workload-specific hyperparameter tuning or model-hardware-aware simulator development, yet could still lead to suboptimal performance. In this paper, we show that using a simple multiplication of two carefully chosen indicators: one KVCache-aware (new prefill tokens if routed to an instance) and one load-balancing-aware (current batch size of the instance), as the scheduling score (LMETRIC) can achieve both objectives simultaneously without any hyperparameter tuning. The key idea is that the simply multiplied score considers both objectives in a manner similar to a linear combination, but the original hyperparameters cancel out during comparison, so no tuning is needed to find the best parameters. The two indicators are chosen based on our analysis of LLM characteristics. Our extensive experiments show that this simple approach can reduce TTFT by 92% and 39%, and TPOT by 24% and 51%, compared to vLLM-v1 and an in-production scheduler on real-world workloads covering chatbots and coding agents. We also derive the mathematical conditions under which multiplication may fail, and find that such conditions are extremely rare in practice and can be detected (and mitigated) beforehand. LMETRIC has been deployed in production and canary release confirms its effectiveness

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 核心问题与整体含义（研究动机与背景）

- **问题背景**：在 LLM 集群化部署中，全局调度器需要将请求路由到多个服务实例（instance）上。LLM 请求服务分为 prefill 和 decode 两阶段，分别影响 TTFT 和 TPOT。高质量的调度需要同时满足两个目标：
  - **KV$ 感知（KV$-awareness）**：将请求路由到拥有匹配 KV$ 缓存的实例，从而跳过重复计算，显著降低 prefill/decode 延迟；
  - **负载均衡（load balancing）**：避免部分实例过载、部分空闲，保证整体资源高效利用。
- **现存矛盾**：两个目标相互冲突——过度追求 KV$ 命中会导致请求集中到少数热门实例，破坏负载均衡；而单纯负载均衡则忽略了 KV$ 带来的巨大加速收益。
- **现有组合策略的不足**：
  - **线性组合**：需要工作负载相关的超参数调优，且静态权重应对动态负载时次优；
  - **过滤式组合**：同样需要调阈值，且偏向负载均衡，不能充分利用 KV$；
  - **模拟式组合**：依赖高精度模拟器，开发复杂，需按模型、硬件、部署场景定制，且预测误差仍会导致性能次优。
- **论文主张**：用**两个精心选择的指标直接相乘**作为调度分数，即可同时实现 KV$ 感知和负载均衡，且无需超参数调优，无需模拟器。该方法名为 **LMETRIC**。

## 2. 方法论：核心思想、关键技术细节与算法流程

### 2.1 核心思想
- **将线性组合中的“加法”替换为“乘法”**。线性组合分数为 `Score_i = λ·KV_i + (1-λ)·LOAD_i`，其比较实例 i、j 时依赖于 λ。而乘法形式变为 `Score_i = KV_i × LOAD_i`，在比较两个实例时，常数因子（如 λ 和 1-λ）会被约去，因而无需调参。
- 关键在于选择两个能分别代表 KV$ 感知和负载均衡的指标，且指标间应具有互补性。

### 2.2 指标选择
- **KV$ 感知指标：P-token**（new prefill tokens）
  - 定义为：若将请求路由到某个实例，需**新计算的前缀 token 数量**，即 `P-token = len(prompt) - KV$.hit_len(prompt)`。
  - 相比直接用 KV$ 命中率（1 - hit ratio），P-token 还隐式考虑了排队中的 prefill 负载，能更好地避免超载实例，从而在保持类似命中率的同时改善负载均衡。
- **负载均衡指标：BS**（batch size）
  - 使用实例当前 batch size（运行中+排队中的请求数），它准确反映 decode 工作负载。
  - 相比 total tokens 指标，BS 对 decode 延迟的指示更稳定：batch size 小的时候 token 较多并不必然导致慢，而 BS 直接关联 decode 计算压力。

### 2.3 调度算法流程（伪代码描述）
1. 接收到新请求 `req`；
2. 对每个实例 i，并行收集并计算：
   - `new_tokens_i = P_tokens.update(req.prompt)`（即 `len(prompt) - KV$.hit_len(req.prompt)`）；
   - `work_i = BS.update(1)`（即当前实例 batch size）；
3. 计算每个实例的调度分数：`score_i = new_tokens_i × work_i`；
4. 路由请求到 `score` 最小的实例。

### 2.4 失败条件分析与检测
- **理论上乘法可能失败的情形**：当出现 KV$ 热点时，即某些前缀被重复访问但只缓存在少数实例上，若这些请求导致的 P-token 下降无法被 batch size 的上升抵消，则请求持续涌向热点实例，造成负载不平衡。
- **边界条件推导**：将请求按 KV$ 前缀分为类 c，M 为拥有该类前缀缓存的实例集合，M̄ 为其他实例；设 x 为类 c 请求占总请求比例，|M| 为缓存实例数。若满足 `x/x̄ ≤ |M|/|M̄|`，则即使在最坏情况下（所有类 c 请求都路由到 M），热点实例的 batch size 也不会超过非热点实例，乘法方法有效。
- **实证观察**：在论文所用四条真实工作负载中，所有采样类均满足该条件，说明乘法失败情形在实际中极其罕见。
- **检测与缓解**：设计两阶段检测器：
  - 第一阶段：实时监控 `x/x̄` 和 `|M|/|M̄|`，一旦违反边界条件则报警；
  - 第二阶段：报警后，仅当连续 `2|M|` 个该类请求在热点实例上的乘积分数仍小于非热点实例时，才过滤掉热点实例，即将热点实例从路由候选中移除，避免过载。

## 3. 实验设计：数据集、基准与对比方法

### 3.1 数据集与工作负载
- **真实工作负载轨迹**（含请求内容哈希与时间戳）：
  - **ChatBot (Qwen)**：类 ChatGPT 的开源轨迹；
  - **Agent (Qwen)**：LLM API 调用 agent 服务的开源轨迹；
  - **Coder**：从阿里巴巴百炼（Bailian）收集的编码 agent 专用集群日轨迹；
  - **ToolAgent (Kimi)**：Kimi 开源的 agent 服务轨迹。
- 覆盖聊天、API 调用、编码 agent、工具 agent 等主要 LLM 应用场景。

### 3.2 模型与硬件
- **模型**：Qwen2-7B（dense），Qwen3-30B（MoE），以及生产部署中的 Qwen3.5-27B。
- **测试集群**：16 张 NVIDIA H20 GPU，每张 96GB HBM；路由器运行于 160 核 Intel Xeon CPU、1TB 内存的服务器；实例运行 vLLM-v1。

### 3.3 对比方法（Baselines）
- **vLLM (vLLM-v1)**：仅负载均衡的调度策略（JSQ 变种）；
- **Bailian**：百炼生产调度器，线性组合 KV$ 命中率与归一化 batch size；
- **Dynamo (ai-Dynamo)**：NVIDIA 流行框架，线性组合 prefill token 数与 total tokens；
- **llm-d**：模拟式调度，基于 VIDUR 模拟器预测 TTFT；
- **Preble**：混合过滤+线性回退的研究型调度器；
- **PolyServe**：模拟式多 SLO 调度器，目标并非纯负载均衡而是形成负载梯度便于自动扩缩。

### 3.4 实验设置
- 所有策略均重实现于论文自研的高性能 Rust 路由器框架，保证 apples-to-apples 对比，并验证重实现不比原实现慢。
- 对需要调参的基线，均针对每个工作负载仔细调优到最优。
- 轨迹按测试床能力缩放，默认将平均到达率缩放至测试床最大处理能力的一半，并测试不同请求率下的敏感性。

## 4. 资源与算力

- **测试床**：16 × NVIDIA H20 GPU（96GB HBM each），路由器为 160 核 CPU / 1TB DRAM 服务器。
- **生产部署**：百炼的 Qwen3.5-27B 集群，包含**数百张 GPU**（具体数量/配置保密）；用于 canary release 对比实验时，LMETRIC 集群与原调度集群接收相同每 GPU 请求速率（1/3 vs 2/3 流量分流，集群规模相应调整）。
- **论文未明确说明**：训练或调优耗时、模拟器开发/调参的具体算力成本、每条轨迹重放的具体 GPU 时间等。

## 5. 实验数量与充分性

### 5.1 实验种类
- **四类组合方法深入分析实验**（§4）：vLLM 基线、线性组合（权重扫描）、过滤式（阈值扫描）、模拟式（好/差调优 vs 线性最优）在各轨迹上的 TTFT/TPOT 百分位对比。
- **指标选择消融实验**（§5.1）：P-token vs 1-KV hit ratio；BS vs #Tokens，并辅以命中率、排队 prefill token、batch size vs total tokens 关系等机制分析。
- **乘法失败条件分析**（§5.2）：真实轨迹中监控 `x/x̄` 与 `|M|/|M̄|`；构造一个含 KV$ 热点的对抗性工作负载进行验证。
- **端到端主实验**（§6.1）：4 条轨迹 × 不同模型/请求率组合，对比 vLLM、Dynamo、llm-d、Bailian，报告 TTFT/TPOT 的 CDF、均值、P99 等。
- **请求率敏感性实验**：多条轨迹在不同到达率下的表现。
- **研究型调度器对比**（§6.2）：与 Preble、PolyServe 在 ChatBot 工作负载上对比，并分析 Preble 过滤分支使用率、PolyServe 负载分布等机制。
- **生产环境 canary 测试**（§6.3）：真实集群上的对比，观察均值 TTFT/TPOT 下降。

### 5.2 充分性评估
- **优点**：实验覆盖多种工作负载（聊天/agent/coder）、多种模型架构（dense/MoE）、多种调度范式（负载均衡、线性、过滤、模拟），并有机制层面的分析（KV$ hit ratio、负载平衡剖面），同时包含消融和故障模式分析，整体较充分。
- **限制**：主实验仅在 16 GPU 的单一硬件（H20）上进行，未覆盖其他 GPU 类型、更大规模集群；模型仅测试 Qwen 系列两种规模，缺乏更多模型（如 Llama、更大的 MoE）的验证；模拟式基线（llm-d）的实现为论文自行改造/重写，可能与其原系统存在细微差异；Preble/PolyServe 的对比仅在一个工作负载上详细展示，虽然论文称其他工作负载结果类似，但未全部给出。

## 6. 主要结论与发现

- **乘法指标（P-token × BS）可同时实现 KV$ 感知与负载均衡，且无需超参数调优**。
- 相比 vLLM（负载均衡为主），LMETRIC 在 ChatBot 工作负载上将平均 TTFT 降低 **92%**、平均 TPOT 降低 **24%**；相比百炼现有生产调度器，平均 TTFT 降低 **39%**、平均 TPOT 降低 **51%**。
- 相比最强基线 llm-d，LMETRIC 在 ChatBot 上可将 P99 TPOT 降低 13%，且 TTFT 相当；在 ToolAgent 上虽然平均 TTFT 略高（约 10%），但 TPOT 降低 30%。
- 相比 Preble，LMETRIC 平均/ P99 TTFT 分别降低 56%/45%，平均/ P99 TPOT 降低 8%/16%。
- 相比 PolyServe，LMETRIC 在所有请求率下均取得更低 TTFT/TPOT，因为 PolyServe 为自动扩缩主动制造负载梯度，牺牲了延迟。
- 乘法失败的数学条件（KV$ 热点导致 batch size 无法抵消 P-token 优势）在实际工作负载中极少出现，且可通过两阶段检测器检测并缓解。
- 生产 canary 验证：LMETRIC 在数百 GPU 的 Qwen3.5-27B 集群上有效，均值 TTFT/TPOT 显著下降。

## 7. 优点

- **极简且有效**：用最简单的乘法组合替代复杂线性调参、过滤阈值或模拟器，避免手工调优和模型/硬件相关的开发，部署成本低。
- **理论分析扎实**：不仅给出经验结果，还从数学上推导了乘法方法的适用条件和失败边界，并设计检测器，方法论完整。
- **机制性实验深入**：对“为什么选 P-token 而非 KV hit ratio”“为什么选 BS 而非 #Tokens”等设计决策提供了数据支撑，包括命中率、排队 token、batch size 与 token 数的关系等分析。
- **公平对比**：所有策略统一重实现在高效 Rust 路由器中，明确验证不慢于原实现，基线超参均调试到最佳；客观比较了不同组合策略的代价。
- **生产验证**：实际部署于阿里巴巴百炼，并用 canary 分流对比验证，说服力强。
- **可复现性**：开源代码和轨迹，便于后续研究。

## 8. 不足与局限

- **硬件/模型覆盖有限**：实验仅在 16×H20 GPU 测试床上进行，GPU 类型单一；模型仅验证了 Qwen2-7B、Qwen3-30B 和 Qwen3.5-27B，缺少其他主流模型（如 Llama、更大规模 MoE）的验证，结论泛化性需更多证据。
- **集群规模局限**：最大实验规模为 16 GPU，生产集群虽然数百 GPU 但细节不公开，无法分析大规模下的可扩展性问题，且未讨论路由器在处理上千实例时的吞吐瓶颈。
- **请求率设置特殊**：默认到达率设为测试床最大处理能力的一半，模拟百炼避免过载的配置，但这种“半负载”可能不覆盖高过载或极低负载场景；虽做了不同请求率实验，但其中部分轨迹（如 ToolAgent）出现与 llm-d 的差距，说明简单指标并非总是最优。
- **模拟器基线公平性存疑**：llm-d/VIDUR 经过作者自行改造（增加 KV$ 建模、Rust 重写、并行化）才能达到论文中的表现，且作者承认原始实现调度延迟高；这可能导致“模拟式方法”被低估或高估，无法代表所有模拟式实现。
- **故障模式检测器只是充分/必要条件分析**：论文指出等式 (2) 只是必要条件，实际检测器带有启发式（如连续 2|M| 次过滤），其误报/漏报率和极端场景下的鲁棒性未充分评估。
- **PD-disaggregation 仅简要讨论**：论文聚焦 PD-colocation，对分离式 prefill/decode 部署只给出定性观点，没有实验验证。
- **生产部署信息不透明**：集群规模、流量细节、SLO 配置均保密，无法独立复现 canary 结果。
- **未涉及多模型/异构部署**：虽然论文声称逻辑分区后适用，但没有在异构 GPU 或混合模型场景下验证。

（完）
