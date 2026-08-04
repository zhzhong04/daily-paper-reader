---
title: "SubGCache: Accelerating Graph-based RAG with Subgraph-level KV Cache"
title_zh: SubGCache：基于子图级KV缓存加速图检索增强生成
authors: "Qiuyu Zhu, Liang Zhang, Qianxiong Xu, Cheng Long, Jie Zhang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40827/44788"
tags: ["query:agent-cache"]
score: 6.0
evidence: 对不同查询复用代表子图的预计算KV缓存，可迁移至Agent间跨上下文复用
tldr: 图检索增强生成中不同查询常检索到相似子图，导致重复计算KV缓存和推理延迟。SubGCache基于子图嵌入对查询聚类，为每个簇构造代表子图并预计算其KV缓存，查询时直接复用簇内预计算缓存。实验表明该方法在降低推理延迟的同时保持生成质量。这项工作展示了跨查询复用KV缓存的有效手段，对智能体间跨上下文共享KV缓存具有直接借鉴价值。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40827/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1843, \"height\": 557, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40827/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1823, \"height\": 903, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40827/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 852, \"height\": 866, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40827/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 867, \"height\": 788, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40827/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1522, \"height\": 1320, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40827/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1560, \"height\": 1036, \"label\": \"Table\"}]"
motivation: 不同查询检索到相似子图时重复计算KV缓存，造成图RAG推理延迟高。
method: 按子图嵌入聚类查询，构造每类代表子图并预计算KV缓存，簇内查询复用缓存。
result: 在图形RAG任务上显著降低推理延迟，同时保持输出质量。
conclusion: 为跨上下文KV缓存复用提供了聚类与预计算的通用技术，可启发Agent缓存共享。
---

## Abstract
Graph-based retrieval-augmented generation (RAG) enables large language models (LLMs) to incorporate structured knowledge via graph retrieval as contextual input, enhancing more accurate and context-aware reasoning. We observe that for different queries, it could retrieve similar subgraphs as prompts, and thus we propose SubGCache, which aims to reduce inference latency by reusing computation across queries with similar structural prompts (i.e., subgraphs). Specifically, SubGCache clusters queries based on subgraph embeddings, constructs a representative subgraph for each cluster, and pre-computes the key-value (KV) cache of the representative subgraph. For each query with its retrieved subgraph within a cluster, it reuses the pre-computed KV cache of the representative subgraph of the cluster without computing the KV tensors again for saving computation. Extensive experiments on three datasets across multiple LLM backbones and graph-based RAG frameworks demonstrate that SubGCache consistently reduces inference latency with comparable and even improved generation quality, achieving up to 6.68x reduction in time-to-first-token (TTFT).

---

## 论文详细总结（自动生成）

# SubGCache 论文详细中文总结

## 1. 核心问题与研究动机（背景与问题定义）

图检索增强生成（Graph-based RAG）为大语言模型（LLM）集成结构化外部知识提供了新范式——从文本图（textual graph）中检索与查询相关的子图并作为上下文输入，以支持更精准的实体关系推理。但在实际场景中，查询往往以**批量（in-batch）**方式提交（如学术图谱上的批量问答），而批内不同查询检索到的子图往往**高度重叠**，甚至完全相同。

现有方法为每个查询独立执行完整的图检索与LLM推理，导致**大量重复计算**——特别是对重复子图反复计算KV（Key-Value）缓存，造成显著的推理延迟。论文揭示了这一被忽视的效率瓶颈，并明确了两个核心挑战：

- **结构冗余的识别**：不同查询检索到的子图在节点标识、局部上下文或图拓扑上并不完全相同，如何有效比较和判断它们是否存在有意义的重叠？这一问题无法用文本级精确词匹配解决。
- **结构冗余的利用**：即使识别出重叠，不同查询的子图通常只是**部分共享**，并不完全一致。如何在部分重叠的结构上复用计算，同时不损失推理所需的上下文关联？

**整体含义**：论文首次将图RAG从单查询处理范式拓展到**批查询高效处理**范式，为图RAG的低延迟部署提供了一种即插即用的缓存框架。

## 2. 方法论：核心思想与关键技术

SubGCache 是一个轻量级、即插即用的子图级 KV 缓存框架，包含三个核心步骤：

### （1）基于子图相似性的查询聚类（Query Clustering）

- **子图嵌入**：利用图RAG中预训练好的**GNN编码器**（以SentenceBERT节点特征初始化）将每个检索到的子图编码为图嵌入向量，该嵌入同时编码**语义**和**结构**信息。
- **层次聚类**：对嵌入向量执行层次聚类（hierarchical clustering），将子图重叠度高的查询自动归入同一簇，从而在**结构层面**而非文本层面识别冗余。

### （2）代表性子图构造（Representative Subgraph Construction）

- 对于每个簇，将簇内所有查询检索到的子图进行**节点与边的并集合并**，构造一个代表性子图。
- 该代表性结构统一保留簇内共享的关系上下文，作为跨查询复用的缓存单元——这是与文本级缓存（如句子、文档块）的关键区别。

### （3）子图级KV缓存复用（Subgraph-level Cache Reuse）

- **簇级顺序处理**：逐簇处理查询。对当前簇，先将代表性子图构造成prompt前缀（Prefix），输入LLM**一次性计算其KV张量**并缓存于GPU显存。
- **查询级复用**：簇内每个查询只需解码/缓存自身新增的问题token，共享前缀对应的KV缓存直接复用，显著减少prefill阶段延迟。
- **显存管理**：一个簇处理完毕即释放其KV缓存，再处理下一簇，确保可扩展性和显存效率。
- **灵活性**：通过调节聚类数量可控制缓存复用粒度——簇越多越贴近单查询模式，簇越少复用收益越大；当每查询独立成簇时自动退化为标准图RAG。

## 3. 实验设计

### 数据集与场景

| 数据集 | 类型 | 用途 |
|--------|------|------|
| **Scene Graph** | 场景图数据集 | 基于场景图的问答 |
| **OAG** (Open Academic Graph) | 学术异质图 | 学术知识问答 |
| **DBLP** | 学术引用图 | 学术知识问答（附录中报道） |

### 框架与对比方法

- **基准图RAG框架**：G-Retriever（基于检索节点/边重建子图）、GRAG（基于k-hop自我网络直接检索子图）。
- **对比设置**：原版模型 vs. 原版模型+SubGCache（即 G-Retriever+SubGCache 和 GRAG+SubGCache）。
- **LLM骨干**：Llama-3.2-3B、Llama-2-7B、Mistral-7B、Falcon-7B，共4种不同架构与规模。
- **推理设置**：仅推理（inference-only），LLM参数冻结。

### 主要评测指标

- **ACC**（准确率，%）
- **RT**（整体响应时间，ms）
- **TTFT**（首token时间，ms）
- **PFTT**（prefill+首token时间，ms）

## 4. 资源与算力

**论文未明确报告**使用的GPU型号、数量、训练轮次或能耗等细节。可以确认的是：实验全部在**推理阶段**完成，LLM权重保持冻结，无需微调；GNN编码器为图RAG框架本身预训练好的组件，SubGCache未引入额外训练开销。具体硬件配置在正文中未提及。

## 5. 实验数量与充分性评估

论文的实验较为充分，具体包括:

- **主实验**：在2个主要数据集（Scene Graph、OAG）× 4种LLM骨干 × 2种图RAG框架，共16组配置，对比了4个指标；另在DBLP上有补充实验（见附录G）。
- **批大小影响实验**：分别以50、100、150、200个批量查询进行扩展性验证（表2），且在多种LLM骨干上均有补充（附录E）。
- **聚类数量影响分析**：在{1,2,3,4,5,10,20}七个聚类数量下对比准确率与TTFT的权衡（图3）。
- **开销分析**：对比LLM响应时间与簇处理时间的拆解分析（图4），并在{1,2,3,4,5,10,20,30,40,50}多个聚类配置下验证。
- **其他消融/补充**：案例分析（附录D）、不同链接策略对比（附录F）。

**充分性评价**：实验覆盖面较广，跨越了模型规模（3B到7B）、架构（Llama/Mistral/Falcon）、数据集类型（场景图、学术图）、框架（两种主流图RAG方法）等多个维度，且做了延迟拆解和开销分析，整体较为系统、客观。**不足之处**在于：

- 所有实验均为英文学术/场景图问答，缺乏多语言或更丰富领域的验证；
- 未与其他KV缓存复用方法（如Prompt Cache、RAGCache）进行直接对比；
- 缺少不同簇数下代表性子图合并规模（token数量）的具体统计。

## 6. 主要结论与发现

1. **显著降低推理延迟**：SubGCache在每个数据集、每种LLM骨干上均一致地大幅减少各项延迟指标。典型结果包括：
   - G-Retriever+SubGCache 在Scene Graph上实现 **6.68× TTFT加速**（Llama-2-7B），响应时间最高 **5.76× 降低**；
   - PFTT最大降幅达 **18.90×**（GRAG+Falcon-7B，Scene Graph）；
   - 在OAG上TTFT最高加速 **6.52×**，响应时间最高 **5.11×**。

2. **保持甚至提升生成质量**：准确率多数情况持平或提升：
   - Scene Graph上最高提升 **9.00%**（GRAG+Mistral-7B）；
   - 少数情况下轻微下降（最多 −1.00%），源于合并上下文引入的轻微噪声。

3. **聚类数量的权衡非单调**：较粗聚类（少簇）增强缓存复用但增加prompt长度；较细聚类（多簇）保留更多查询特定上下文但复用减少。TTFT与准确率随簇数变化并非线性关系。

4. **聚类开销极低**：簇处理时间占比在Scene Graph上低于2.1%，OAG上最大约6%；且该时间不随簇数单调增加（各簇规模更小导致编码成本降低）。

5. **良好扩展性**：批大小从50增至200时，SubGCache依然保持一致的延迟降低与质量稳定。

## 7. 方法亮点与优点

- **解决了一个真问题**：揭示了图RAG在批量查询场景下的结构冗余这一此前被忽视的效率瓶颈，为后续研究打开新方向。
- **即插即用的通用设计**：不要求修改底层图RAG模型或LLM，仅作为外层缓存模块即可接入，实验证实跨模型、跨框架通用。
- **结构级缓存新范式**：第一次将prompt缓存引入图RAG场景，并以**子图**（而非句子/文档块）作为缓存单元，突破了文本级精确匹配假设，提出了部分共享结构复用的一般策略。
- **工程角度优雅**：利用GNN嵌入做结构感知聚类相对轻量；簇级KV缓存的构造-复用-释放流程简洁清晰，兼顾效率与显存控制。
- **实验报告透明**：延迟指标拆分为RT、TTFT、PFTT，能清晰地定位prefill阶段的实际收益；并单独剖析了聚类处理开销。

## 8. 不足与局限性

- **算力与部署细节缺失**：未报告GPU型号、数量和具体推理吞吐环境，可复现性和工程参考价值稍打折扣。
- **公平性风险**：SubGCache可以认为是“作弊”式地利用了批内查询的相似性——如果一个批内查询子图本身无重叠（如完全不同的主题），缓存复用收益会显著下降；论文未讨论这种最坏情况下的性能衰减。
- **代表性子图合并引入噪声**：部分场景下合并导致准确率下降（最多1%），说明合并策略还有改进空间；论文也未深入分析合并上下文对LLM生成质量影响的结构性原因。
- **缺乏与其他缓存方法的直接对比**：论文未与Prompt Cache、RAGCache等现有文本级KV缓存方法在同一实验设置下比较，难以定位SubGCache在通用KV缓存方法谱系中的相对地位。
- **聚类数量需人工预设**：实际部署中需要调节簇数以权衡延迟与质量，缺乏自动选择聚类粒度的准则。
- **图规模扩展性存疑**：OAG数据集中聚类处理开销已达6%（相对较大），在更大规模图或更复杂图（如知识图谱）上，GNN编码与代表性子图合并的计算开销可能成为新瓶颈。
- **仅限推理阶段**：不适用于需要对LLM进行微调或持续学习的场景。

---

（完）
