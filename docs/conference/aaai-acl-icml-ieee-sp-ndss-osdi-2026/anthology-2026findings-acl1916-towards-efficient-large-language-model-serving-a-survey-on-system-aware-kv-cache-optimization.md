---
title: "Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization"
title_zh: 面向高效大语言模型服务：系统感知KV缓存优化综述
authors: "Jiantong Jiang, Peiyu Yang, Rui Zhang, Feng Liu"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1916.pdf"
tags: ["query:awc"]
score: 5.0
evidence: 系统感知的KV缓存优化综述，覆盖调度、放置与保留
tldr: 该综述从系统行为视角对面向LLM服务的KV缓存优化进行了梳理，将其组织为执行与调度（时间）、放置与迁移（空间）、表示与留存（结构）三个维度，并进一步分析了跨行为协同设计和行为-目标关联。相关技术为构建高效的缓存调度与驱逐策略提供了系统化的分类和启发，有助于在代理等复杂工作流下定位缓存管理问题。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 807, \"height\": 384}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 804, \"height\": 495}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 809, \"height\": 256}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1672, \"height\": 1532}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 813, \"height\": 371}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1659, \"height\": 527}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1916/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 806, \"height\": 369}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 790, \"height\": 445}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1646, \"height\": 416}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 806, \"height\": 333}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1649, \"height\": 828}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 799, \"height\": 378}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1650, \"height\": 854}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1667, \"height\": 749}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1581, \"height\": 2338}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1567, \"height\": 2428}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 802, \"height\": 352}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1916/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 805, \"height\": 356}]"
motivation: 为LLM服务中KV缓存造成的存储昂贵问题提供系统性的技术梳理与协同设计展望。
method: 从时间、空间和结构三个维度对KV缓存优化方法进行分类，并分析跨行为协同设计。
result: 识别出多个行为与目标之间的关联点，指出未来研究机会。
conclusion: 该综述为KV缓存基础设施的设计提供了系统性参考。
---

## Abstract
Despite the rapid advancements of large language models (LLMs), LLM serving systems remain memory-intensive and costly. The key-value (KV) cache, which stores KV tensors during autoregressive decoding, is crucial for enabling low-latency, high-throughput LLM inference serving. In this survey, we focus on system-aware KV infrastructure for serving LLMs (abbreviated as sKis). We revisit recent work from a system behavior perspective, organizing existing efforts into three dimensions: execution and scheduling (temporal), placement and migration (spatial), and representation and retention (structural). Furthermore, we analyze cross-behavior co-design affinity and behavior-objective links, highlighting future opportunities. Our work systematizes a rapidly evolving area, providing a foundation for understanding and innovating KV cache designs in modern LLM serving infrastructure.

---

## 论文详细总结（自动生成）

# 面向高效大语言模型服务：系统感知KV缓存优化综述——详细中文总结

## 1. 论文的核心问题与整体含义

- **研究背景**：大语言模型（LLM）在各类应用中展现出卓越能力，但其服务推理过程仍面临严重的内存密集与高成本问题。Transformer架构的LLM以自回归方式逐token生成文本，为避免重复计算，服务系统采用键值（KV）缓存存储已生成的中间KV张量。随着提示与输出长度不断增长，KV缓存可达到数百万token规模，成为服务内存瓶颈的核心。
- **核心问题**：如何在**服务阶段（serving-time）**、以**KV缓存为主要优化目标**、**在不重训练模型或修改模型架构的前提下**，系统性提升LLM服务的吞吐量、延迟、内存占用等系统指标。
- **论文定位（sKis）**：作者将研究范围定义为“系统感知的KV服务基础设施”（system-aware KV infrastructure for serving LLMs，简称sKis），强调从**系统行为视角**而非算法/模型视角来审视KV优化方法。
- **关键区别**：相较于更广泛的LLM效率工作，本文刻意排除了三类相关工作：长上下文记忆增强、内核融合/算子调度、训练期间的KV压缩或KV复用微调——它们或改变模型本身，或并非以KV缓存为主要优化对象。

## 2. 论文提出的方法论：核心思想与关键技术细节

本论文是综述论文，其“方法论”体现在对现有研究组织方式上：提出了一个**行为导向的三维分类体系**，将KV缓存优化映射到三个系统行为空间。

### 2.1 时间维度：执行与调度（Temporal Behavior）
- **KV中心调度（KV-centric Scheduling, KVS）**：将KV特征整合进运行时决策：
  - **请求级**：基于预测KV用量的调度以平衡预填充—解码干扰（如TetriInfer）；基于KV复用率感知的调度（如RadixAttention、Preble、Mooncake）。
  - **Token级**：判断哪些KV条目参与注意力计算，如Quest、SparQAttention、RefreshKV。
  - **内核级**：FlashInfer根据查询与KV长度调度CUDA线程块。
- **流水线与重叠（Pipelining and Overlapping, OVLP）**：在计算、I/O与通信之间重叠执行以隐藏KV相关延迟。论文按模式细分为：计算—计算重叠、计算—I/O重叠、I/O—通信重叠，并区分了各方法的粒度和转移路径。
- **硬件感知执行（Hardware-aware Execution, HAE）**：
  - **分离式推理**：将预填充与解码阶段部署到不同计算池（如Splitwise、DistServe、Mooncake、MuxServe的SM分区共置）。
  - **计算卸载**：将部分计算迁移至CPU（如FastDecode、Neo）、计算存储驱动器CSD（InstInfer）或存内计算PIM（PAPI、AttAcc）。

### 2.2 空间维度：放置与迁移（Spatial Behavior）
- **内存层级KV编排（Memory Hierarchy KV Orchestration, MHO）**：
  - **跨设备内存层级**：在GPU HBM、CPU DRAM与SSD之间迁移KV缓存。多数方法为“重要性感知”型（如ArkVale、OmniKV、ClusterKV），仅在GPU保留轻量级代理信号以引导预取；另一类从系统成本优化角度出发（如FlexGen的带宽/延迟约束成本模型）；最近还扩展至基于CXL（Compute Express Link）的共享/分离内存池设计。
  - **GPU内内存层级**：在片上L1/L2缓存与片外HBM之间异步预取KV块（如AsyncKV、PRESERVE）。
- **计算设备KV编排（Compute Device KV Orchestration, CDO）**：在具备计算能力的设备之间放置和移动KV，涵盖集群内编排（常与PD分离结合，如DistServe的拉取式KV传输）、远端KV流式传输（CacheGen的位流编码与自适应流式）以及异构加速器（PIM、CSD）上的注意力卸载。

### 2.3 结构维度：表示与留存（Structural Behavior）
- **KV缓存压缩（KV Cache Compression, KVCC）**：
  - **量化**：从早期8/4-bit统一量化发展到混合精度量化，关键洞见包括①KV非对称量化（key按通道、value按token）；②异常值处理（更高位宽存储或专用技术）；③向量量化（VQ）用于极低比特场景（1–2 bit）。表3对比了23种方法的粒度、精度模式、重要区域、异常值处理和平均比特数。
  - **低秩近似**：对缓存KV张量、KV投影权重或QKV注意力子空间进行低秩约束（如xKV、Palu、LoRC）。论文指出，符合sKis范围的仅限无需额外训练参数的方法。
  - **结构压缩**：通过剪枝（丢弃层/头/通道/token子集）或合并（融合相似单元）修改缓存组织方式，由注意力分数、相似性或查询范数引导（如表5所示）。
- **KV缓存留存管理（KV Cache Retention Management, KVRM）**：
  - **分配与复用**：虚拟化分配（vLLM的PagedAttention页面调度）、结构化索引实现提示共享（RadixAttention的基数树）、标准化KV布局便于内核调度。
  - **驱逐（Eviction）**：基于预算丢弃低重要性token的KV状态。表6对比了28种驱逐方法，呈现三项洞见：静态驱逐（预填充后一次确定）vs. 动态驱逐（解码中在线更新）；驱逐策略通常保留近期窗口、注意力汇（attention sink）token，以及由注意力分数或启发式信号选择的额外token；预算分配从均匀走向按层、按头的自适应分配。

### 2.4 交叉分析方法
- **行为×目标矩阵**（表7）：将七类行为与五项服务目标（平均延迟、尾部延迟、吞吐量、GPU内存、互连I/O、能量）关联，以直接/间接影响级别标注，并用星号标记≥70%论文报告增益的高流行指标。
- **行为—行为协同设计亲和网络**（图6）：基于对每篇论文主/次分类标签赋权（主分类权重1、次分类权重0.5），计算加权共现矩阵，经Tanimoto系数归一化后，阈值θ=0.14以上绘制连接边，反映文献中的协同设计模式。

## 3. 实验设计

- **论文性质**：本论文为综述文章，**没有开展新的实验验证**。作者明确声明：“This survey conducts no new experiments”。
- **分析样本**：系统整理并分类了约150余篇发表于2023年至2026年的代表性工作，覆盖ICLR、ICML、NeurIPS、ACL、EMNLP、ASPLOS、ISCA、OSDI、SOSP、FAST、ATC、EuroSys、SIGCOMM、HPCA、DAC、FPGA、MLSys、SIGMOD等众多顶级会议及重要arXiv预印本。
- **分析手段**：采用三类系统化分析工具——
  1. **行为×目标矩阵分析**：基于文献中报告的性能增益的频率统计；
  2. **协同设计亲和网络**：基于文献中行为类别共现的加权归一双模网络；
  3. **对比表**：与相关综述的系统性差异对比（表1/表8）。
- **Benchmark实践评价**：附录G.3.1回顾了现有benchmark工具（如LLMPerf、GenAI-Perf、MLPerf Inference、BALI等），指出指标定义和测量方式存在不一致，并提出统一benchmark的设计原则建议（附录G.3.2），包括可信度量指标（P99尾部延迟、SLO违规率、goodput、语义违规率）、KV相关资源指标（KV缓存内存占用、有效位宽、KV命中率、KV相关停顿时间等）以及三类压测负载（多租户突发负载、长上下文负载、异构/领域偏移负载）。

## 4. 资源与算力

- **未涉及**：由于论文是综述论文，未开展新实验，因此**完全没有提及自身使用的GPU型号、数量或训练时长**。
- **间接信息**：附录讨论中提到，本文结论综合自公共论文和开源实现报告的结果，“主要基于主流平台和常见配置”下的实验数据，但不保证在所有硬件或规模上具有普遍性。作者特意避免跨论文聚合原始加速比或内存数字，理由是这些增益与模型、硬件、工作负载和基线选择紧密耦合。

## 5. 实验数量与充分性

- **实验数量**：论文没有自己的实验，因此不存在通常意义上的消融实验或多数据集验证。
- **“实验”充分性评估**：
  - 从综述覆盖广度来看，其分析样本量大（约150+篇论文），覆盖面广（跨ML、NLP、系统、架构多个社区），分类粒度细（7个子类别），交叉分析维度多（行为×目标、行为×行为），能够较好地支撑其主要结论。
  - 从客观性来看，论文明确区分了“文献共现反映的协同设计模式”与“经过验证的性能增益”，在行为-行为亲和网络部分特别声明“该亲和度反映的是文献中的协同设计模式，而非经验证的性能提升”。
  - 然而，由于不开展实验，论文无法验证某些结论的实际有效性。例如，能量方向“未开发”的观察、KVCC与其他行为协同的“错失机会”等判断，均基于文献计量而非实测性能数据，存在一定的推断性偏差风险。

## 6. 论文的主要结论与发现

### 六个关键观察（O1–O7）
- **O1**：结构类方法（KV压缩与留存管理）研究最多，主导内存节省贡献；时间类和空间类方法通过迁移或复用间接带来内存收益，反映出社区偏向内存效率。
- **O2**：时间类行为（KVS、OVLP、HAE）最直接作用于延迟与吞吐量，但**尾部延迟报告严重稀疏**，多数方法仅报告平均延迟。
- **O3**：空间类方法主要针对互连I/O，且常与OVLP配对使用——通过将KV传输与计算重叠来有效隐藏传输延迟。
- **O4**：**能量/功耗目标被严重忽视**，尽管许多方法降低了内存或计算强度，理论上应能转化为能量收益，但极少有论文报告能量指标。
- **O5**：质量损耗是普遍存在的横切问题：时间类行为可能导致请求处理不一致，空间类行为可能遗漏KV数据，结构类行为直接降低KV精度；关键问题在于这些劣化是否“可控”。
- **O6**：**HAE–CDO（硬件感知执行与计算设备KV编排）是最强的协同设计模式**，如Splitwise在PD分离时将层间KV传输与预填充阶段计算重叠。
- **O7**：**KVCC（KV缓存压缩）在协同设计网络中相对孤立**——尽管其研究热度最高，但缺乏与其他行为的系统性协同，错失了联合优化机会。

### 六个开放挑战（C1–C6）
- **C1. SLO驱动的尾部控制**（源于O2）：需要将SLO违规归因到具体的KV行为和路径，建立标准化的抢占与降级语义。
- **C2. 能量感知的sKis**（源于O4）：集成功耗分析到运行时决策，建立服务期能耗模型，按请求/token度量能量，研究能量友好的KV粒度和布局。
- **C3. 可信赖且高效的sKis**（源于O5）：结构性方法可能删除“低显著性但关键”的上下文导致灾难性错误，需要暴露最坏情况失败、质量下界，使可信赖性可行为归因、SLO感知。
- **C4. 可泛化的HAE–CDO**（源于O6）：当前策略多针对特定网络拓扑或单租户环境，需跨NVLink/NVSwitch/PCIe/CXL等异构拓扑可移植，并适应多租户场景。
- **C5. 协同优化与中间语义**（源于O7）：在共享的带宽与延迟约束下联合决定驱逐、卸载和预取策略；引入“粗粒度语义状态”（如“GPU上可回收”“GPU上已压缩”“CPU上已压缩”等中间状态）将协同优化形式化为状态迁移。
- **C6. 统一Benchmark**：标准化的指标定义、代表性压力工作负载和报告规范（详见附录G.3.2）。

## 7. 优点

- **新颖的分类视角**：作者声称是首个将KV缓存优化组织为“时间-空间-结构”行为空间的工作，这一视角独立于模型和内核细节，为该快速演进的领域提供了较稳定的分析透镜。
- **系统化的交叉分析方法**：行为×目标矩阵与行为—行为协同设计亲和网络的提出，使综述超越了简单文献罗列，能基于文献计量揭示研究热点与盲区。
- **构建了“主分类+次分类”的双层映射体系**：既保持正文的聚焦，又通过完整对照表（表9）提供全景式类别映射，兼顾易读性与信息完整性。
- **透明的方法论披露**：对协同设计亲和网络的计算过程（权重分配、共现矩阵、Tanimoto归一化、阈值设定）做了详细说明，可复现性强。
- **深度洞察有实用价值**：如“量化中异常值占主导地位”“KV压缩的系统集成薄弱”“尾部延迟的报告缺失”等观察，为从业者提供了具体的优化切入点。
- **明确的范围边界**：清晰定义了sKis的排他性标准（排除了训练期压缩、注意力机制重设计等方法），使综述定位准确，避免了范围蔓延。

## 8. 不足与局限

- **无实验验证**：作为纯综述，论文的所有结论均基于对公共文献的定性/定量梳理和推断，无法对方法间的相对优劣做出实证裁定。作者也对此坦诚声明。
- **可能的文献遗漏**：作者承认“在快速演进的研究领域中可能遗漏了某些同样有价值的贡献”，尽管已尽可能全面收录。
- **结论的泛化性受限**：所总结的方法性能结果“主要基于主流平台和常见配置”，对特定硬件或非典型工作负载的适用性难以保证。作者有意不聚合跨论文的加速比数字，这既是审慎的选择，也限制了读者对“哪种方法实际更有效”的直观判断。
- **评价偏差风险**：用于判断“直接/间接影响”和“≥70%论文报告增益”的统计，基于论文作者自己报告的结果而非独立复现，可能存在发表偏见（上报增益的工作更易发表）。
- **协同设计亲和的解释力有限**：论文将行为-行为共现解释为“协同设计模式”，但共现不等于经过验证的有效协同，作者也坦承了这一点，虽降低了误导风险，但也使得该分析更多是“假设生成”而非“结论验证”。
- **面向特定部署场景**：虽然时间-空间-结构视角本身硬件无关，但对具体方法的大量讨论仍以GPU为中心架构为主，对其他硬件平台（如TPU、NPU等）覆盖不足。
- **可信赖性讨论深度有限**：虽然提出了可信赖性挑战，但

### 8. 不足与局限（续）

- **可信赖性讨论深度有限（续）**：虽然论文提出了可信赖性挑战（C3），指出结构类压缩方法可能删除“低显著性但关键”的上下文并导致不可恢复的错误，但该部分仍停留在问题提出层面，未能系统梳理已有工作中关于质量保障、故障恢复或安全降级的工程实践，也未针对“如何量化最坏情况失败”给出可操作的评价框架或案例。换言之，挑战定义清晰，但解决路径的文献梳理与方案比较仍显单薄。
- **对具体方法的公平比较缺失**：论文虽构建了多维分类体系，但在每个子类别内部，几乎没有对同类别方法进行横向对比或性能排序的尝试（如表3、表5、表6主要是分类罗列而非量化对比）。作者有意回避跨论文聚合指标，避免了“苹果对橘子”式的误比，但也使读者难以回答“同属KV驱逐的A方法与B方法，哪个在何种场景下更优”这类实际部署中最关心的问题。
- **对行业闭源系统覆盖不足**：论文分析的多为学术研究与开源系统，对工业界闭源部署中的KV缓存管理实践（如部分商业LLM服务所采用的专有调度、离线层间KV整理或专用推理芯片上的缓存设计）缺乏描述，可能使某些观测结论与真实规模化生产环境存在偏差。

## 9. 总体评价与展望

- **总体定位**：这是一篇组织严谨、视角独特、覆盖面广的领域综述，其最大贡献不在于罗列方法，而在于提出了一个“行为空间”分析框架，使快速膨胀的KV缓存优化文献获得了可比较、可追踪、可推断研究趋势的结构化坐标系。作为面向系统研究者的“地图”，它的价值显著高于其作为方法选择指南的价值。
- **对社区的实际作用**：论文揭示的若干结构性盲区——尤其是**能量指标的缺失**、**尾部延迟与SLO归属研究的稀疏**、**KV压缩与其他系统行为的协同断层**——为后续研究者指出了清晰的切入点；其提出的统一Benchmark设计原则（附录G.3.2）亦有望推动该领域从“各自为政的评测”走向“可对标的评测”。
- **推荐阅读方式**：建议读者根据自身需求分层次使用本文——若需全局把握研究格局，可精读正文与六个关键观察（O1–O7）；若需选定具体优化方向，可结合表3/表5/表6的逐方法对比表定位候选方案；若需开展协同设计研究，则图6的亲和网络与开放挑战C1–C6提供了直接的选题灵感。
- **未来展望**：随着CXL内存池、分离式推理架构与异构计算设备的普及，空间类行为与硬件感知执行的重要性预计将进一步上升；而如何在KV压缩的极限压缩率与可信赖性之间取得工程可接受的平衡，可能是接下来数年该领域最值得关注的核心矛盾。

（完）
