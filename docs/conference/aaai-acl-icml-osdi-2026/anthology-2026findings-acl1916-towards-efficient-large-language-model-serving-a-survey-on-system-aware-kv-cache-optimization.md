---
title: "Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization"
title_zh: 面向高效大语言模型服务：系统感知KV缓存优化综述
authors: "Jiantong Jiang, Peiyu Yang, Rui Zhang, Feng Liu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1916.pdf"
tags: ["query:awc"]
score: 6.0
evidence: 面向LLM服务的KV缓存优化综述，涵盖调度、放置与保留等系统行为
tldr: 大语言模型服务受限于内存开销和成本，KV缓存是解码阶段的关键优化对象。该综述从系统行为视角梳理KV缓存优化研究，归纳为执行与调度、放置与迁移、表示与保留三个维度，并分析跨行为协同设计与目标关联。它为智能体工作流中的缓存调度、复用与驱逐提供了系统化的技术图谱和设计启示。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 807, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 804, \"height\": 495, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 809, \"height\": 256, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1672, \"height\": 1532, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 813, \"height\": 371, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1659, \"height\": 527, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 806, \"height\": 369, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 790, \"height\": 445, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1646, \"height\": 416, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 806, \"height\": 333, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1649, \"height\": 828, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 799, \"height\": 378, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1650, \"height\": 854, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1667, \"height\": 749, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1581, \"height\": 2338, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1567, \"height\": 2428, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 802, \"height\": 352, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 805, \"height\": 356, \"label\": \"Table\"}]"
motivation: LLM服务内存密集且昂贵，KV缓存优化是提升吞吐与延迟的关键。
method: 从系统行为视角综述KV缓存优化，划分三个维度并分析协同设计与目标关联。
result: 系统化梳理现有技术，指出未来方向，为构建高效KV服务基础设施提供参考。
conclusion: 为KV缓存优化提供结构化分析框架，可指导智能体工作流中的缓存管理设计。
---

## Abstract
Despite the rapid advancements of large language models (LLMs), LLM serving systems remain memory-intensive and costly. The key-value (KV) cache, which stores KV tensors during autoregressive decoding, is crucial for enabling low-latency, high-throughput LLM inference serving. In this survey, we focus on system-aware KV infrastructure for serving LLMs (abbreviated as sKis). We revisit recent work from a system behavior perspective, organizing existing efforts into three dimensions: execution and scheduling (temporal), placement and migration (spatial), and representation and retention (structural). Furthermore, we analyze cross-behavior co-design affinity and behavior-objective links, highlighting future opportunities. Our work systematizes a rapidly evolving area, providing a foundation for understanding and innovating KV cache designs in modern LLM serving infrastructure.

---

## 论文详细总结（自动生成）

# 面向高效大语言模型服务：系统感知KV缓存优化综述

## 一、核心问题与整体含义

- **研究背景**：大语言模型（LLM）在各类应用中展现出卓越能力，但其服务系统面临严重的内存密集和成本高昂问题。LLM 采用自回归方式逐 token 生成，为避免重复计算先前 token 的注意力，服务系统引入 KV cache（键值缓存）存储中间 KV 张量。然而，随着上下文窗口和批量请求规模不断增长，KV cache 可能达到数百万 token，造成显著的内存瓶颈。
- **核心问题**：如何在不重新训练模型、不修改 Transformer 架构的前提下，通过服务期的系统级优化手段，缓解 KV cache 带来的内存和带宽压力，从而提升 LLM 服务的吞吐量、降低延迟。
- **研究定位**：论文提出了 **sKis**（system-aware KV infrastructure for serving LLMs）这一研究范围，即：在服务（推理）期间运行、以 KV cache 为主要优化目标、旨在提升系统指标且无需重训练的方法。这区别于更广泛的 LLM 效率研究（如长上下文记忆增强、内核融合、训练期 KV 压缩等）。
- **核心贡献**：首次将 KV cache 优化纳入**时间—空间—结构**的三维行为空间进行系统化分析，提供了一种与模型和内核细节解耦的稳定分类视角，有助于在该快速演进领域定位新方法和发现研究空白。

## 二、方法论

论文采用**系统行为导向的分类体系**，将现有 KV cache 优化工作划分为三个维度、七个子类：

### 1. 时间维度：KV 执行与调度（§3）

- **KV 中心调度（KVS）**：在请求级将 KV 使用特征融入运行时调度决策，如基于预测 KV 用量的负载均衡（TetriInfer）、高复用优先调度（RadixAttention、Mooncake）；在 token 级决定哪些 KV 条目参与注意力计算，如周期性全上下文与子集注意力交替的刷新策略（RefreshKV）；在内核级根据 query/KV 长度调度注意力线程块（FlashInfer）。
- **流水线与重叠（OVLP）**：通过将计算、I/O 和通信重叠来隐藏 KV 相关延迟。论文按模式总结了四种重叠类型：计算-计算重叠（如 CPU 注意力计算与 GPU 线性运算并行）、计算-I/O 重叠（如 GPU 计算与 KV 在 HBM 和 L2 之间的预取）、I/O-通信重叠（如 GPU KV 预取与集合通信并行）。
- **硬件感知执行（HAE）**：将 KV 相关操作适配到底层异构硬件，包括**解耦式推理**（将 prefill 和 decode 分配给不同算力池，如 Splitwise、DistServe、Mooncake）和**计算卸载**（将部分计算迁移至 CPU、计算存储驱动器 CSD、存内计算 PIM 等辅助设备）。

### 2. 空间维度：KV 放置与迁移（§4）

- **内存层级 KV 编排（MHO）**：
  - **跨设备层级**：在 GPU HBM 与 CPU DRAM/SSD/CXL 等慢速但容量更大的存储之间迁移 KV。多数方法为**重要性感知型**，如 ArkVale、OmniKV、ClusterKV 等将完整 KV 卸载至 CPU，GPU 仅保留轻量代理信号引导预取；另一类从系统成本角度优化放置，如 FlexGen 利用成本模型在 GPU/CPU/磁盘间分配 KV。
  - **GPU 内层级**：在片上 L1/L2 与片外 HBM 之间迁移 KV，如 AsyncKV 的异步 L2 预取、PRESERVE 的图级优化避免缓存污染。
- **计算设备层 KV 编排（CDO）**：在具备计算能力的设备间放置和移动 KV，支持分布式或异构服务，如 Intra-cluster 编排（DistServe、TraCT 利用 CXL 共享内存）、远程 KV 流式传输（CacheGen 的位流编码与自适应流式传输）以及向异构加速器的卸载。

### 3. 结构维度：KV 表示与保留（§5）

- **KV 缓存压缩（KVCC）**：
  - **量化**：从固定 8/4-bit 发展到混合精度，关键洞察包括：key 和 value 的离群模式不同需非对称量化（通常 key 按通道、value 按 token）；离群值处理至关重要（如 KVQuant、OTT）；近年向量量化（VQ）方法可达到极低比特（1-2 bit，如 CQ、VQ-LLM、NSNQuant）。
  - **低秩近似**：对缓存的 KV 张量、KV 投影权重（WK, WV）或 QKV 注意力子空间进行低秩分解（如 xKV、Palu、LoRC）。
  - **结构压缩**：通过剪枝（丢弃层/头/通道/token 单位）或合并（将单元融合为共享形式）减少 KV 内存。
- **KV 保留管理（KVRM）**：
  - **分配与复用**：结构感知方法重新设计 KV cache 布局，如 PagedAttention 的虚拟化分页、RadixAttention 的基数树前缀共享、FlashInfer 的块稀疏可组合格式。
  - **驱逐**：在预算下丢弃不重要的 token KV。论文从模式（静态 vs. 动态）、驱逐策略（保留最近窗口/注意力汇聚 token + 轻量信号选择）、预算策略（均匀 vs. 分层/分头自适应）三个维度系统比较了代表性方法。

论文还提出了**行为×目标矩阵**（表 7）和**行为间协同设计亲和网络**（图 6），通过统计文献中 70% 以上论文报告的增益方向及 Tanimoto 归一化共现频率，揭示了各行为维度对延迟、吞吐、内存、I/O、能耗等目标的作用模式和跨行为设计的协同强度。

## 三、实验设计

- **论文性质**：这是**综述论文，并未开展新的实验**。
- **分析对象**：论文系统梳理了超过 130 个已有方法（发表于 ICML、NeurIPS、ACL、OSDI、SOSP、ASPLOS 等顶级会议及重要 arXiv 预印本）。
- **分析框架**：
  - 构建了完整的分类映射表（表 9），标注每个方法的主类别和次类别（G#）。
  - 构建了行为×目标矩阵（表 7），统计各行为维度对系统目标的影响方向和文献密度。
  - 构建了行为间协同设计的亲和网络（图 6），基于加权共现频率（主类别权重 1、次类别权重 0.5），经 Tanimoto 系数归一化后保留阈值以上边。
- **基准与对比**：论文本身不定义新 benchmark，但附录 G.3 详细审查了现有 LLM 推理基准实践，包括客户端工具（LLMPerf、GenAI-Perf/NVIDIA NIM）和基准套件（MLPerf Inference、LLM-Inference-Bench、BALI），指出指标定义和测量方式存在不一致性问题，并倡导统一的 sKis 基准。
- **分析产出的定性结论**：归纳了 7 个关键观察（O1-O7）和 6 个开放挑战（C1-C6）。

## 四、资源与算力

- 论文在 Limitations 中**明确声明未进行任何新实验**（"this survey conducts no new experiments"），因此**没有报告任何 GPU 型号、数量、训练或推理时长等算力使用信息**。
- 论文审慎地避免跨论文聚合原始加速比或内存数字，因为报告增益与模型、硬件、工作负载和基线选择高度耦合，这也反映了对算力评测可比性的审慎态度。

## 五、实验数量与充分性

- **实验数量**：不适用（综述论文）。
- **充分性与分析深度**：
  - 覆盖面较广：涵盖 7 个子类、130+ 方法，包含量化、低秩、结构压缩等方向的细粒度对比表（表 3、4、5、6）。
  - 分析方法有一定客观性：使用统计标志（≥70% 论文报告增益）和量化归一化方法计算协同强度，而非纯主观归纳。
  - 然而，行为×目标矩阵中的相关性和协同网络反映的是**文献共现模式**而非经过验证的性能增益，论文也明确承认这一点。
  - 论文指出多数现有方法的评估存在不足：通常在受控工作负载下评估、对突发流量/多租户场景的鲁棒性分析有限、尾延迟指标报告稀疏、能耗指标极少报告。

## 六、主要结论与发现

论文归纳了 7 个关键观察（O1-O7）：

- **O1**：结构类方法（KVCC、KVRM）研究最多，主导了内存节省方面的成果，其他方法（如迁移、复用）间接产生内存收益；社区倾向于关注内存效率。
- **O2**：时间类行为（KVS、OVLP、HAE）最直接地影响延迟和吞吐，但尾延迟报告非常稀疏。
- **O3**：空间类方法主要针对互连 I/O，常与 OVLP 协同使用以隐藏传输延迟。
- **O4**：**能耗问题最被忽视**，尽管许多方法减少了内存/计算强度，理论上应带来能耗收益。
- **O5**：质量损失是普遍现象——时间方法可能造成请求处理不一致，空间方法可能丢失 KV 数据，结构方法直接降低 KV 精度。关键在于确保退化可控。
- **O6**：HAE-CDO 是最强的协同设计模式：利用设备异构性的计算布局往往与 KV 共置/传输协同设计。
- **O7**：KVCC 尽管流行但与系统其他行为耦合较少，暗示了错失的协同设计机会。

基于这些观察，论文提出 6 个开放挑战（C1-C6）：

- **C1. SLO 驱动的尾延迟控制**：需将 SLO 违规归因到具体的 KV 行为路径上，建立标准化的抢占与降级语义。
- **C2. 能耗感知的 sKis**：建立服务期能耗模型，按请求/token 度量能耗，探索能耗友好的 KV 粒度和布局。
- **C3. 可信且高效的 sKis**：结构方法可能损害鲁棒性而平均精度指标无法反映，需关注最坏情况失败和质量下界；sKis 技术还可作为防御机制（如 KV 驱逐防御越狱攻击）。
- **C4. 可泛化的 HAE-CDO**：使该模式可跨异构拓扑（NVLink、NVSwitch、PCIe、CXL）移植并适应多租户场景。
- **C5. 协同优化与中间语义**：研究在共享预算下的联合决策（驱逐、卸载、预取的共同优化），利用细粒度中间语义（如"GPU 可回收""GPU 已压缩""CPU 已压缩"等状态转换）形式化协同策略。
- **C6. 统一基准**：倡导统一的 sKis benchmark，涵盖可信指标（尾延迟、SLO 违规率、goodput、语义违规率）、KV 相关资源指标（KV 内存占用、有效位宽、KV 命中率、KV 相关 stall、有效带宽利用率）、三类压力工作负载（多租户/突发、长上下文、异构/域偏移）和报告标准。

## 七、优点

- **新颖的分类视角**：首次从系统行为（时间-空间-结构）而非生命周期或优化层级出发组织 KV 缓存优化文献，提供了一个与模型/内核细节解耦的稳定透镜，在快速演进领域中具有更强的持久性。
- **跨行为分析**：不仅分类，还构建了行为×目标矩阵和协同设计亲和网络，揭示了单看某一维度无法发现的研究空白和协同机会。
- **范围界定清晰**：明确定义 sKis 的边界（服务期、KV 中心、无需重训练、系统指标），并区分了次要类别关联（G# 映射表），为读者提供了完整的跨领域交叉参考。
- **细粒度对比表**：量化方法、低秩方法、结构压缩、驱逐策略等均提供了多维度对比（粒度、精度模式、离群处理、平均位宽、驱逐/预算策略等），便于研究者快速定位技术差异。
- **实践洞察**：明确指出压缩方法的内存节省不一定转化为端到端系统收益，低比特量化在 I/O 受限工作负载中更可能带来吞吐收益等务实结论。
- **前瞻性方向**：提出能耗感知、可信赖性、中间语义、统一基准等尚未充分开发的领域，对未来研究具有指导价值。

## 八、不足与局限

- **论文自身的局限声明**：
  - 领域快速发展，可能遗漏同等价值的贡献。
  - 未进行新实验，结论基于公开论文和开源实现报告的结果，主要受限为主流平台和常见配置条件下的结论，泛化性受限。
  - 故意不跨论文聚合性能数字，因为报告增益与模型/硬件/工作负载/基线强耦合——这也意味着无法给出可量化的综合对比结论。
- **分类主观性**：每篇论文仅标注 1-2 个主类别，部分方法的次要贡献被省略或未详述，可能丢失某些跨维度联系的细节。
- **文献共现不代表性能验证**：协同设计亲和网络反映的是"哪些行为常在同一篇论文中出现"，而非"哪些行为组合已验证有效"。
- **未能深入评估鲁棒性**：论文指出现有方法的评估在突发流量、多租户场景、尾延迟和能耗方面明显不足，但综述本身也未提供这类实验来弥补这些空白。
- **应用限制**：sKis 范围严格限定为服务期的免重训练优化，因此不覆盖通过修改模型架构（如 DeepSeek-V2 的 MLA、原生稀疏注意力）或重新训练实现 KV 缩减的重要研究方向，这在一定程度上限制了讨论的完整性。

（完）
