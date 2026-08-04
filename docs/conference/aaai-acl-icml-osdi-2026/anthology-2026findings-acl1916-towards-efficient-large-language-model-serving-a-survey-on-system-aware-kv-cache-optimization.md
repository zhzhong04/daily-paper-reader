---
title: "Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization"
title_zh: 面向高效大语言模型服务：系统感知KV缓存优化综述
authors: "Jiantong Jiang, Peiyu Yang, Rui Zhang, Feng Liu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1916.pdf"
tags: ["query:agent-cache"]
score: 6.0
evidence: 系统感知KV缓存优化综述，涵盖调度/驱逐、放置、迁移与结构保留，直接关联缓存调度与驱逐
tldr: KV缓存是LLM服务内存瓶颈，但缺少从系统行为角度的系统化梳理。该综述从执行与调度（时间）、放置与迁移（空间）、表示与保留（结构）三个维度组织现有KV缓存优化工作，并分析跨行为协同设计与行为-目标联系。文章总结了当前进展并指出未来机会。它为Agent服务工作流中的KV缓存调度与驱逐提供了系统级参考架构，但未专门讨论Agent间跨上下文共享。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 807, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 804, \"height\": 495, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 809, \"height\": 256, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1672, \"height\": 1532, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 813, \"height\": 371, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1659, \"height\": 527, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 806, \"height\": 369, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 790, \"height\": 445, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1646, \"height\": 416, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 806, \"height\": 333, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1649, \"height\": 828, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 799, \"height\": 378, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1650, \"height\": 854, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1667, \"height\": 749, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1581, \"height\": 2338, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1567, \"height\": 2428, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 802, \"height\": 352, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 805, \"height\": 356, \"label\": \"Table\"}]"
motivation: LLM服务内存开销巨大，KV缓存是延迟吞吐关键，但缺乏系统行为角度的综述。
method: 从执行调度、放置迁移、表示保留三个维度归类KV优化文献，并分析跨行为协同设计。
result: 系统梳理了相关工作，指出调度、迁移与结构优化之间的协同机会和未来方向。
conclusion: 提供KV缓存系统优化的全景参考，可支撑Agent工作流缓存调度与驱逐研究。
---

## Abstract
Despite the rapid advancements of large language models (LLMs), LLM serving systems remain memory-intensive and costly. The key-value (KV) cache, which stores KV tensors during autoregressive decoding, is crucial for enabling low-latency, high-throughput LLM inference serving. In this survey, we focus on system-aware KV infrastructure for serving LLMs (abbreviated as sKis). We revisit recent work from a system behavior perspective, organizing existing efforts into three dimensions: execution and scheduling (temporal), placement and migration (spatial), and representation and retention (structural). Furthermore, we analyze cross-behavior co-design affinity and behavior-objective links, highlighting future opportunities. Our work systematizes a rapidly evolving area, providing a foundation for understanding and innovating KV cache designs in modern LLM serving infrastructure.

---

## 论文详细总结（自动生成）

# 面向高效大语言模型服务：系统感知KV缓存优化综述

## 1. 核心问题与整体含义（研究动机和背景）

- **研究背景**：大语言模型（LLM）在各类应用中表现优异，但其推理服务（serving）存在严重的内存密集和成本高昂问题。KV缓存（KV cache）在自回归解码过程中存储中间张量，是实现低延迟、高吞吐LLM服务的关键，但随着提示词和输出长度的增长，KV缓存可达数百万token，构成主要内存瓶颈。
- **核心问题**：现有针对KV缓存优化的综述多按生命周期阶段或优化层次组织，缺乏从**系统行为视角**（system behavior perspective）对KV缓存基础设施的系统化梳理。作者提出一个新的研究范畴 **sKis**（system-aware KV infrastructure for serving LLMs，即面向LLM服务的系统感知KV基础设施），其定义为满足以下条件的方法：①在服务（推理）期间运行；②以KV缓存为主要优化目标；③无需重新训练基础LLM权重或修改Transformer架构，旨在改进系统指标。
- **与更广泛LLM效率工作的区别**：排除了①长上下文内存增强、②内核融合/算子调度、③训练时KV压缩和带KV复用的微调等方向，聚焦于服务时、KV中心、系统感知的优化方法。

## 2. 方法论：核心思想、关键技术细节

本文是一篇**综述论文**，不提出新方法，而是提出了一套分类学框架和组织方法，对现有文献进行系统化归类和交叉分析。

### 2.1 三维分类学框架

- **时间维度 — 执行与调度（Execution & Scheduling）**：关注KV数据何时被访问、计算或调度。细分为：
  - **KV中心调度（KVS）**：将KV特性集成到运行时决策中。请求级（如基于KV使用预测的TetriInfer、复用感知的RadixAttention和Preble）、token级（如Quest、RefreshKV）、内核级（如FlashInfer）。
  - **流水线与重叠（OVLP）**：通过重叠计算、I/O和通信来隐藏KV相关延迟。分为计算-计算重叠、计算-I/O重叠、I/O-通信重叠三类模式。
  - **硬件感知执行（HAE）**：将KV相关操作适配到底层异构硬件。包括**分离式推理**（prefill-decode分离，如Splitwise、DistServe、Mooncake）和**计算卸载**（卸载到CPU、计算存储驱动CSD、存内计算PIM等）。
- **空间维度 — 放置与迁移（Placement & Migration）**：关注KV缓存被放置或迁移到何处。细分为：
  - **内存层级KV编排（MHO）**：跨设备内存层级（GPU HBM/CPU DRAM/SSD/CXL内存/L1-L2缓存）放置和迁移KV条目。多数方法基于重要性感知，在GPU上只保留关键KV，将完整KV卸载到CPU，并用轻量代理信号指导预取；部分方法从系统成本建模角度优化。
  - **计算设备KV编排（CDO）**：在具备计算能力的设备间放置和移动KV，支持分布式或异构服务。包括集群内编排（常与PD分离耦合）、远程KV传输（如CacheGen对KV张量编码并在网络上自适应传输）以及异构加速器（PIM、CSD）上的注意力卸载。
- **结构维度 — 表示与保留（Representation & Retention）**：关注KV数据如何被压缩或管理。细分为：
  - **KV缓存压缩（KVCC）**：包括**量化**（如KIVI、KVQuant、ZipCache、CQ等，比较粒度、精度模式、异常值处理、平均比特数）、**低秩近似**（如xKV、Palu，针对缓存KV、KV投影权重W_K/W_V、QKV注意力子空间三类目标）、**结构压缩**（剪枝和合并，如CHAI头部剪枝、ThinK通道剪枝、KVMerger和CaM的KV合并）。
  - **KV缓存保留管理（KVRM）**：包括**分配与复用**（虚拟化分配如PagedAttention和vAttention、前缀共享结构如RadixAttention的基数树、标准化KV布局如FlashInfer）和**驱逐**（H2O、Scissorhands、StreamingLLM等，比较驱逐模式、驱逐策略、预算策略）。

### 2.2 交叉分析方法

- **行为×目标矩阵**：将每种行为对服务目标（平均延迟、尾延迟、吞吐量、GPU内存、互连I/O、能耗/功耗、质量影响）的直接影响/间接影响进行标注，并统计研究密度和增益报告比例。
- **行为-行为协同设计亲和网络**：基于文献共现频率构建Jaccard/Tanimoto归一化的协同设计亲和矩阵，以网络形式可视化跨行为协同设计模式。

## 3. 实验设计

- **综述性质说明**：这是一篇综述论文，**没有开展新的实验**。作者明确指出："This survey conducts no new experiments."
- **"实验"替代方案**：作为替代，作者通过以下方式实现了系统分析：
  - **文献梳理**：覆盖了约200篇相关论文，全部标注了发表venue（ICML、NeurIPS、ACL、SOSP、OSDI、ISCA、ASPLOS等），并按7个子类别给出了完整的论文映射表（Table 9）。
  - **量化分析**：构建了行为×目标矩阵（Table 7）和行为-行为协同设计亲和网络（Figure 6），其中基于每篇论文的主/次分类标签，采用主类权重1、次类权重0.5的加权方案计算共现强度，再经Tanimoto归一化处理得到相对协同强度。
  - **模型辅助分析**：统计了各方法报告的性能增益，以"≥70%论文报告该目标增益"作为高流行度标记。
- **基准/数据集**：本文是综述，无自身benchmark；但作者在附录G.3中系统梳理了现有LLM推理基准实践，指出了客户端工具（LLMPerf、GenAI-Perf）和基准套件（MLPerf Inference、LLM-Inference-Bench、BALI）的现状与不足，并提出了统一sKis基准的设计原则（指标、工作负载、报告标准）。
- **对比方法**：与已有综述（Miao et al. 2023、Yuan et al. 2024、Zhou et al. 2024b等共10篇）进行了覆盖度对比，认为自己的综述在"KV-centric（专注KV）、Serving only（仅服务）、No retrain（无需重训练）、System metrics（系统指标）"四个维度上均为✓，并以"系统行为"作为组织原则，区别于现有综述的"优化层""生命周期阶段"等组织方式。

## 4. 资源与算力

- **未提及**：论文中**没有说明任何GPU型号、数量、训练/推理时长或具体算力消耗**。
- **原因**：作为综述论文，不涉及新实验，因此不需要报告算力。作者在局限性中也指出，其结论是基于"已发表论文和开源实现中报告的结果"，而这些结果与具体模型、硬件、工作负载和基线选择密切相关，因此刻意避免跨论文汇总raw speedup或内存数字。

## 5. 实验数量与充分性

- **实验数量**：无自身实验，但文献分析的广度很大——覆盖了7个子类别的约200篇论文，并按时间顺序排列了完整的分类映射表。
- **充分性分析**：
  - ✅ 分析维度较为全面：行为×目标矩阵覆盖6类服务目标，行为-行为协同网络覆盖7类行为的全组合。
  - ✅ 多个观察（O1-O7）基于统计证据（如≥70%论文报告某类增益）而非主观判断。
  - ⚠️ 局限性在于：由于方法涉及的不同硬件平台、模型、工作负载差异巨大，作者明确避免汇总具体的加速比或内存节省数字，这虽然保证了公平性，但也使得定量结论的精确性受限。
  - ⚠️ 作者承认"鉴于相关工作的广泛性和该领域的快速演变，可能遗漏了一些同样有价值的贡献"。
  - ⚠️ 部分分类决策带有主观性（如将某些方法归为主类或次类），但作者提供了完整映射表供读者检验。

## 6. 主要结论与发现

### 关键观察（O1-O7）

- **O1**：结构类工作（压缩、驱逐）研究最多，主导内存节省；其他行为（迁移、复用）间接产生内存收益，反映学界对内存效率的偏向。
- **O2**：时间行为（KVS、OVLP、HAE）最直接作用于延迟和吞吐，但**尾延迟的报告非常稀少**。
- **O3**：空间方法主要针对互连I/O，通常与OVLP配合以隐藏迁移延迟。
- **O4**：**能耗是研究空白**，尽管许多方法减少了内存或计算强度，理应对能量有益，但几乎无人报告或优化能耗。
- **O5**：质量损失是普遍的，各类方法都面临质量退化风险，关键在于使退化可控。
- **O6**：HAE-CDO（硬件感知执行与计算设备KV编排）是最强的协同设计模式。
- **O7**：KVCC虽然热门，但与其他行为协同设计较少，存在被孤立的趋势。

### 开放挑战（C1-C6）

- **C1**：SLO驱动的尾延迟控制（←O2），需要标准化的抢占和降级语义。
- **C2**：能耗感知sKis（←O4），需建立服务时能耗模型，按请求/token度量能耗。
- **C3**：可信和高效sKis（←O5），需要暴露最坏情况失败和质量下限，使可信度可归因于具体行为。
- **C4**：可泛化的HAE-CDO（←O6），需跨异构拓扑（NVLink、NVSwitch、PCIe、CXL）可移植。
- **C5**：协同优化和中间语义（←O7），如联合决策驱逐、卸载和预取，利用中间语义（如GPU上可回收、GPU上压缩、CPU上压缩等状态）实现精细协同。
- **C6**：统一基准，解决工具间指标定义和度量不一致的问题。

## 7. 优点

- **新颖的视角**：首次将KV缓存优化系统化为"时间-空间-结构"行为空间三维框架，与模型和内核细节解耦，提供了一个在快速演进领域中相对稳定的分析透镜。
- **跨行为分析深度突出**：不同于一般综述仅按类别罗列方法，本文通过行为×目标矩阵和行为-行为协同亲和网络揭示了方法间的关联模式和空白区域，如发现KVCC孤立化和能耗研究空白。
- **定位清晰**：明确定义sKis范围边界，与更广泛的LLM效率工作区分，使读者的认知框架清晰。
- **可复现的分类体系**：提供了完整的论文分类映射表（含主类和次类标注）以及协同网络的详细计算方法（含归一化公式和阈值），便于读者检验和扩展。
- **丰富的统计洞察**：以≥70%论文报告增益作为高流行度标记，通过客观统计而非主观判断得出结论。
- **实践指导性强**：附录E给出各方向的详细takeaways；附录G系统梳理了基准实践并提出了设计原则，对社区有实际贡献。

## 8. 不足与局限

- **无新实验**：作者明确指出本综述不进行新实验，结论完全基于公开论文报告的结果。这意味着：①无法统一各方法在同一条件下的公平比较；②无法验证某些分析结论（如协同设计模式是否真的带来实际性能增益）——作者承认亲和度反映的是"文献中的共现模式"而非"验证过的性能增益"。
- **可能遗漏相关工作**：领域快速演进，部分有价值的贡献可能未被覆盖。
- **数据噪音风险**：各论文报告的增益与其模型、硬件、工作负载、基线选择密切相关，作者避免汇总原始加速比等数字，虽然避免了误导，但也限制了对整体收益规模的量化判断。
- **结论泛化性受限**：相关结论主要基于主流平台和常见配置下的公开实现，可能不适用于所有硬件/软件栈。
- **分类主观性**：一篇论文可能涉及多个类别，作者虽按主贡献归入1-2个主类，主/次分类决策仍带有主观性；次类标注（G#）较为保守，可能导致协同网络低估某些关联。
- **评测标准不统一**：作者指出现有工具间指标定义和度量不一致，sKis社区尚缺乏统一基准，这也在一定程度上影响了本文文献分析的可比性基础。

（完）
