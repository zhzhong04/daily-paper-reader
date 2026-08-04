---
title: "CondenseFlow: Scalable Latent Space Collaboration via Semantic Compression for Multi-Agent Systems"
title_zh: CondenseFlow：通过语义压缩实现可扩展的多智能体潜在空间协作
authors: "Xiaoyu Chen, Fengge Wu, Zhao Junsuo, Yun Fan"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.669.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 针对多智能体通信的KV缓存压缩，属于智能体基准的缓存机制
tldr: "在多智能体系统中，全状态潜在通信虽语义丰富但内存随协作轮数线性增长。CondenseFlow提出潜在思想压缩器（LTC），利用可学习语义探针将KV缓存压缩为固定大小表示，使通信复杂度降至O(1)，并理论证明压缩误差可受控累积。在七个基准、六个模型上，KV缓存内存减少超过99%，推理延迟约降低20%，为基于智能体的缓存机制提供了高效方案。"
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 665, \"height\": 365, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1619, \"height\": 1072, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 792, \"height\": 492, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 793, \"height\": 422, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 803, \"height\": 307, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1646, \"height\": 545, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1643, \"height\": 544, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 669, \"height\": 248, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 584, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 664, \"height\": 288, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 547, \"height\": 431, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 697, \"height\": 286, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 837, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 802, \"height\": 273, \"label\": \"Table\"}]"
motivation: 多智能体全状态潜在通信内存开销随协作轮数线性增长。
method: 引入潜在思想压缩器（LTC），用可学习语义探针把KV缓存压成固定大小表示，实现O(1)通信复杂度。
result: "在七项基准和六个模型上，KV缓存内存降低超过99%，推理延迟降低约20%。"
conclusion: 为多智能体系统的缓存压缩和高效通信提供了可扩展方案。
---

## Abstract
Full-state latent communication in LLM-based multi-agent systems offers richer semantics than text but suffers from memory overhead scaling linearly with collaboration rounds. We propose CondenseFlow , which introduces the Latent Thought Condenser (LTC) —a lightweight module using learnable semantic probes to compress KV caches into fixed-size representations, achieving 𝒪(1) communication complexity regardless of context length. We theoretically prove that compression error is bounded by attention concentration and accumulates controllably across rounds. On seven benchmarks spanning six models, CondenseFlow reduces KV cache memory by over 99% and inference latency by approximately 20% compared to dense transfer with negligible accuracy degradation, while outperforming text-based methods by 1.7 percentage points on average across all configurations. Code is available at https://github.com/xxy33/condenseflow.

---

## 论文详细总结（自动生成）

# CondenseFlow：通过语义压缩实现可扩展的多智能体潜在空间协作——论文详细总结

## 1. 核心问题与研究动机

### 背景与问题
- 大语言模型（LLM）正从文本生成工具演变为具备感知、规划与行动能力的自主智能体，多智能体协作（如 MetaGPT、ChatDev、AutoGen）成为重要发展方向。
- 当前主流多智能体系统以**自然语言**作为通信媒介，但离散文本存在固有信息瓶颈——将连续内部推理状态压缩为离散 token 会不可避免丢失不确定性估计和细粒度语义信息。
- 新兴的**潜在空间通信**（latent space communication）直接传输 Transformer 内部表示（如 KV 缓存），语义保真度更高，但面临严重的"内存墙"问题：
  - 内存占用随层数、隐藏维度、序列长度和协作轮数呈 **O(R·T·L·dh)** 线性增长；
  - 对于 14B 参数模型，单次工作记忆传输可达数 GB 量级；
  - 在消费级硬件或带宽受限环境中构成实际部署障碍。
- **核心矛盾**：如何在保留潜在通信高保真优势的同时，严格限制资源消耗，使通信复杂度与交互深度无关。

### 研究意义
- 将高效潜在通信形式化为**语义压缩问题**，为多智能体协作中的缓存机制提供了一种可扩展、理论上可解释的解决方案。

## 2. 方法论

### 2.1 核心思想
- 提出 **CondenseFlow** 框架，通过引入 **潜在思想压缩器（Latent Thought Condenser, LTC）**——一个轻量级模块——将完整的 KV 缓存压缩为固定大小的语义摘要表示，实现 **O(1) 通信复杂度**，与上下文长度和协作轮数无关。
- 与启发式剪枝方法不同，LTC 通过**端到端学习**发现对协作最有价值的信息模式。

### 2.2 关键技术细节
- **可学习语义探针（Learnable Semantic Probes）**：
  - 一组可学习的探针向量 Qc ∈ R^(K×dh)，每个探针作为"语义询问器"，沿特定维度检测和聚合上游思维流中的关键信息；
  - 探针通过交叉注意力自动发现有价值的信息模式，而非依赖注意力分数统计的启发式规则。
- **交叉注意力聚合（Cross-Attention Aggregation）**：
  - 对第 l 层的缓存 (K^(l), V^(l))，探针与键向量计算语义相关性并生成聚合权重；
  - 通过加权求和将键和值压缩为 K×dh 的固定大小表示。
- **架构设计**：
  - 跨层参数共享（所有 Transformer 层使用相同探针）；
  - 层归一化稳定压缩表示；
  - 以 Qwen3-14B 为例，LTC 参数量仅约 0.15M，不足基座模型参数的 0.01%。
- **训练目标**：
  - **重建损失**：使压缩后的 KV 缓存与完整缓存在下游注意力计算上功能等价；
  - **覆盖正则化**：最大化平均注意力分布的熵，防止探针坍缩、确保均匀覆盖原始序列；
  - **正交正则化**：约束探针间的两两相似度，鼓励互补特征捕获。
- **协作管线**：
  - 每轮智能体接收原始问题 q 和上一轮压缩缓存 M_prev；
  - 压缩表示作为 KV 前缀拼接（而非追加），保证上下文开销恒定为 O(K)；
  - 历史信息通过迭代蒸馏隐式传播，防止上下文无界增长。

### 2.3 理论保证
- **压缩误差界**：证明压缩误差由原始注意力分布的集中度（attention concentration）决定，误差上界为 2(1−ρ)·V_max·√n_q，其中 ρ 衡量 top-K 位置捕获的注意力质量占比。
- **多轮行为**：最坏情况下累积误差随轮数线性增长（R·δ），但实证中呈亚线性增长，因为 LTC 学会优先保留对下游推理关键的信息。

## 3. 实验设计

### 3.1 基准与数据集（7 个 benchmark，覆盖 3 类推理任务）
| 任务类别 | 数据集 |
|---------|--------|
| 数学推理 | AIME 2024、AIME 2025、HMMT 2025 |
| 科学推理 | GPQA-Diamond、MedQA |
| 代码生成 | MBPP-Plus、LiveCodeBench |

### 3.2 模型（6 个）
- **小规模**：Qwen3-8B-Instruct、LLaMA-3.1-8B-Instruct、Gemma-2-9b-it
- **中规模**：Qwen3-14B、DeepSeek-R1-Distill-Qwen-14B、Ring-mini-2.0

### 3.3 对比方法（3 种范式）
- **TextMAS**：自然语言通信；
- **Dense-Latent**：完整 KV 缓存传输；
- **CondenseFlow**：LTC 压缩后传输。

### 3.4 评估协议
- **标准协议**：四智能体顺序流水线（规划者→批评者→优化者→求解者），评估典型协作深度下的压缩保真度；
- **压力测试协议**：迭代求解者-批评者交互（最高 20 轮），评估扩展交互下的鲁棒性，以 AIME 2025 为测试平台。

## 4. 资源与算力

- **训练成本**：LTC 训练约需 **4 GPU-hours**（单张 NVIDIA A100-80G）。
- **推理配置**：所有实验在 **NVIDIA A100-80G** GPU 上完成；标准协议使用单 GPU；压力测试使用单 GPU + 梯度检查点以支持扩展序列。
- **说明**：文中未明确报告训练/推理的具体 GPU 数量、总 GPU 小时数或能耗等更细粒度数据。

## 5. 实验数量与充分性评估

### 实验规模
- **标准协议**：6 模型 × 7 基准 = 42 个配置组合，每个结果取 5 次运行均值±标准差，统计严谨；
- **压力测试**：20 轮交互下的精度退化、内存扩展、推理时间三类分析；
- **消融实验**：
  - 压缩维度 K 与交互轮数的联合效应分析（图 4 热力图）；
  - 三种损失组分的贡献消融（重建损失、覆盖正则、正交正则）；
  - 与其他 KV 压缩方法（Random Pruning、H2O、SnapKV）在同等压缩比下的对比；
- **补充分析**：有效秩分析（验证低秩假设）、逐任务类别误差分析、案例研究（展示三种方法在 10 轮后对同一 AIME 题目的具体表现）。

### 充分性评价
- **优点**：实验覆盖面广（多模型规模、多任务类型、多交互深度）、统计报告规范（均值±标准差）、多角度验证（精度、内存、延迟、消融）。
- **不足**：
  - 所有模型均为同构（相同 KV 维度），未验证异构模型场景；
  - 未涉及超长单序列（>8192 token）场景；
  - 训练数据与评估基准的领域分布可能影响泛化结论的可推广性。

## 6. 主要结论与发现

- **显著内存削减**：相比 Dense-Latent，KV 缓存内存减少超过 99%，在 10 轮交互时从 5.03 GB 降至 0.01 GB；
- **推理延迟降低**：10 轮时累计推理时间从 569 秒降至 457 秒，约减少 20%；且 CondenseFlow 每轮时间保持稳定（约 44 秒），而基线随上下文增长持续上升；
- **精度保持**：与 Dense-Latent 相比精度下降小于 2%，且随模型规模增大差距缩小（小模型平均 1.6% → 中模型 1.2%）；
- **超越文本方法**：平均优于 TextMAS 方法 1.7 个百分点；
- **解决上下文累积退化**：TextMAS 和 Dense-Latent 在 4-5 轮后精度显著下降（20 轮时分别降至 12% 和 21%），而 CondenseFlow 在 20 轮内精度始终保持在 58% 以上；
- **压缩维度选择**：K=64 为最优均衡点，K=16 时性能快速坍缩，K>64 收益递减。

## 7. 方法亮点

- **理论框架完备**：首次为多智能体潜在通信建立压缩误差的形式化分析框架，证明误差受注意力集中度约束，并证明学习式聚合方法的表达能力上界不低于最优选择策略；
- **学习式压缩优于启发式选择**：基于交叉注意力聚合保留语义信息，避免剪枝方法硬性丢弃 token 导致的信息损失；
- **极低参数开销**：约 0.15M 参数（不足基座模型 0.01%），跨层共享探针，训练成本仅约 4 GPU-hours；
- **O(1) 通信复杂度的优雅设计**：将多轮历史通过迭代蒸馏隐式压缩为固定大小表示，从根本上规避上下文累积问题；
- **实证分析的深度**：有效秩分析从数据层面验证压缩可行性，案例研究直观展示三种方法在处理长程约束保持和状态一致性上的差异。

## 8. 不足与局限

- **训练依赖**：与无训练的完整传输方法（如 LatentMAS）相比，LTC 需要预训练，增加部署复杂度；
- **压缩比上限**：当压缩维度 K 低于 32 时精度显著下降，存在信息论意义上的压缩极限；
- **同构模型假设**：当前设计假设所有智能体共享相同 KV 维度，异构模型需要额外适配层对齐表示空间，可能引入新误差源；
- **超长序列验证不足**：压力测试仅到 20 轮，单条序列超过 8192 token 的情况未被充分验证；
- **任务特定性**：法律、金融等专业领域可能需要领域适配的语义探针；
- **伦理风险**：潜在通信使智能体间信息交换的透明度降低，增加对非预期或对抗行为检测的难度；效率提升可能降低自动化虚假信息生成的滥用门槛——作者对此明确提出了警示，建议未来开发潜在通信协议的审计机制。

**（完）**
