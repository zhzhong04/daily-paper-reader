---
title: "ContrastKV: Robust KV Cache Eviction via Contrastive Signal Fusion for Multi-Query Generalization"
title_zh: ContrastKV：基于对比信号融合的鲁棒KV缓存驱逐算法
authors: "Xingchi Chen, Peiyuan Zong, Ziqiang Gao, Qing Li, Yong Jiang, Fa Zhu, Hui Li"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.417.pdf"
tags: ["query:awc"]
score: 6.0
evidence: 提出基于对比信号融合的鲁棒查询无关KV缓存驱逐算法，可迁移到多查询场景的多智能体缓存驱逐。
tldr: 本文针对长上下文推理中KV缓存内存开销大、查询感知驱逐方法在多个下游查询间泛化差的问题，提出ContrastKV。该方法通过对比机制融合语义与非语义信号，在不依赖特定查询的情况下做出鲁棒的驱逐决策。实验表明在高驱逐率下ContrastKV显著提升了多查询场景的推理质量，为多智能体或多查询系统的缓存驱逐提供了通用有效的方法。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1573, \"height\": 496, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 794, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 779, \"height\": 901, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 774, \"height\": 871, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1579, \"height\": 911, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1653, \"height\": 1425, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 521, \"height\": 468, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1654, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 800, \"height\": 219, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1645, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 800, \"height\": 253, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 800, \"height\": 256, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 798, \"height\": 256, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1652, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1660, \"height\": 1802, \"label\": \"Table\"}]"
motivation: 长上下文推理中KV缓存占用大，现有查询感知驱逐无法跨查询泛化，查询无关方法又依赖脆弱代理查询。
method: 设计对比信号融合机制，结合语义一致性与非语义结构信号，实现查询无关的鲁棒驱逐。
result: 实验显示高驱逐率下多查询泛化性能优于现有方法。
conclusion: 对比多信号可有效提升KV缓存驱逐在多查询场景下的鲁棒性。
---

## Abstract
Large Language Models (LLMs) face significant memory and latency overheads during long-context inference due to the growing KV cache, especially in Knowledge Base Question Answering (KBQA) settings that require support for multiple downstream queries. Query-aware eviction methods do not generalize across queries, while existing query-agnostic approaches rely on a single proxy query, leading to fragile eviction decisions under high eviction ratios. We propose ContrastKV, a robust query-agnostic KV cache eviction algorithm for multi-query generalization. ContrastKV introduces a contrastive signal fusion mechanism that jointly exploits complementary semantic and non-semantic signals. By contrasting semantic consistency with structural robustness, the method constructs a more reliable eviction criterion that alleviates the blind spots of single-query proxies. The framework integrates efficient signal generation, parallel importance scoring, and multi-level fusion across heads and layers. Experiments show that ContrastKV outperforms state-of-the-art methods, retaining up to 92% accuracy with only 20% of the KV cache budget, while reducing decoding latency by approximately 50% and significantly lowering GPU memory usage.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与研究动机

- **问题背景**：在长上下文推理（long-context inference）中，大语言模型（LLM）的 KV 缓存（Key-Value Cache）随上下文长度增长而大幅膨胀，带来严重的内存和延迟开销。例如，以 Qwen2.5-14B 处理 120K token 输入时，KV 缓存约需 33GB 内存，超过了模型自身的 28GB 参数量。
- **核心场景**：知识库问答（KBQA）类任务——用户将大规模知识库（结构化知识、代码仓库、文档集合或历史对话日志）一次性输入给模型，随后接连提出多个下游查询。知识库比查询和答案长多个数量级，导致 KV 缓存巨大且需要在多个查询间复用。
- **现有方法缺陷**：
  - *查询感知（Query-aware）方法*（如 SnapKV、Ada-KV）：根据当前查询语义做驱逐决策，在 KBQA 多查询场景下难以泛化，性能严重下降；
  - *查询无关（Query-agnostic）方法*（如 KVzip）：不依赖具体查询，但依赖**单一代理查询（single proxy query）**来近似理想驱逐标准，存在"盲区"问题——单个查询无法覆盖多样化的下游查询需求。
- **关键洞察**：在高驱逐率（如保留比例 <30%）下，现有查询无关方法的泛化稳定性显著下降。理论上 KV 缓存可压缩至 5%（如 H2O 所示），而实践中现有方法在 30% 保留率左右就开始失效，说明存在较大的改进空间。
- **解决方法方向**：受集成学习（ensemble learning）中"多样性降低泛化误差"原理启发，论文提出**对比信号融合**的思想：通过显式对比语义信号与结构信号，构造更鲁棒的驱逐准则。

## 2. 方法论：ContrastKV

### 2.1 核心思想

将 KV 缓存驱逐问题形式化为**对比选择任务（contrastive selection task）**：不再依赖单一代理查询，而是使用双信号——**正（语义）信号**和**负（结构）信号**——并通过融合函数 `F` 将两者组合为更鲁棒的重要性估计，最终用于选出保留的 KV 对。

### 2.2 三个主要阶段

1. **对比信号生成（Contrastive Signal Generation）**：
   - *正信号*：采用与 KVzip 相同的**知识库重建提示（knowledge base reconstruction prompt）**作为 `q_pos`，长度与知识库相同（`t_pos = n`）；
   - *负信号*：生成一个**最大熵噪声序列（Maximum Entropy Noise Sequence）**作为 `q_neg`，长度 `t_neg ≪ n`，每个 token 从词表均匀分布独立采样。该序列提供纯结构基线，用于捕捉"注意力汇聚（attention sink）"token，即无论语义内容如何都会获得高注意力得分的 token。

2. **并行重要性评分（Parallel Importance Scoring）**：
   - 将正、负信号并行送入模型（而非串行处理两条加长序列），避免延迟增加；
   - 对每一层 `l` 和 KV 头 `h`，计算注意力矩阵并做切片，取 group 维度和 token 维度的最大值作为重要性分数向量（公式 8）：
     ```
     S = max( A_bar[h, g, i] )  over g=1..G, i=1..t
     ```
   - 该聚合分数被称为"最大交叉注意力分数"。

3. **对比融合机制（Contrastive Fusion Mechanism）**——两级融合：
   - **Head 级融合（Head-level Fusion）**（公式 9）：
     - 对不同注意力头设置上下阈值（β 分位数和 1−β 分位数）；
     - 正负分数**同时高**的 token 提升为 1.0（很可能可泛化），**同时低**的置为 0.0（很可能是冗余），否则保留正信号分数；
     - 确保每个头保留少量高潜力的 KV 对，防止某些头因整体注意力量低而被全部驱逐。
   - **Layer 级融合（Layer-level Fusion）**（公式 10）：
     - 对未被 head 级融合直接决定的 token，用 min-max 归一化后的负信号分数 `S_neg_hat` 作为增益系数，以比例 `γ` 提升正分数（同时截断到正分数最大值）；
     - 使得在负信号下相对突出但正信号中非 top 的 token 也能被略微提升，细化驱逐边界而不覆盖主要语义信号。
   - 融合函数是**固定而非学习**的，以保持跨模型和任务的解释性与鲁棒性。

### 2.3 理论形式化

- 目标：最大化查询分布 `Q` 上重要 KV 对的期望覆盖率，约束保留数量 `|KV_retained| ≤ α·n`，其中 `α < 0.3`（公式 7）；
- 理想通用查询记为 `K_ideal = ∪_{q∈Q} K_q`（公式 4），单一代理查询无法近似该并集，而互补信号可构造更全面的近似。

## 3. 实验设计

### 3.1 基准与数据集

- **Benchmark**：SCBench（Li et al., 2025），包含 11 个数据集，覆盖四种长文本能力类别：
  - 字符串检索（String Retrieval）；
  - 语义检索（Semantic Retrieval）；
  - 全局信息（Global Information）；
  - 多任务处理（Multi-tasking）。
- **主实验**使用其中 8 个数据集，每个类别两个；参数研究使用每类别一个代表性数据集。
- **评估指标**：ROUGE（En.Sum）、Pass@1（Code.RepoQA），其余均为 Accuracy。

### 3.2 模型

- Qwen2.5-7B-Instruct-1M（RTX 4080 SUPER, 32GB）
- Llama3.1-8B-Instruct（RTX 4090, 48GB）
- Qwen2.5-14B-Instruct-1M（模型无关性验证）
- 全部以 bfloat16 精度运行。

### 3.3 对比方法

- **查询感知**：SnapKV（max pooling kernel=7, observation window=32）、Ada-KV（自适应预算分配）；
- **查询无关**：KVzip（chunk size m = 2K，使用官方实现）。

### 3.4 主要实验内容

- **主性能对比**：在 20% 和 10% KV 缓存预算下，两个模型（7B、8B）的 8 个数据集结果，以及 14B 模型的补充实验；
- **不同预算比率的归一化性能对比**（表 2，预算比率从 10% 到 100%）；
- **消融实验**（表 3）：单独使用 head 级融合、单独使用 layer 级融合、两者结合的贡献；
- **效率实验**（表 4）：解码延迟和 GPU 内存占用分析；
- **附录中的参数研究**：β、t_neg、γ 三个超参数的敏感性分析；
- **负样本选择验证**（表 5）：对比随机字符串与知识库前 10% 内容作为负样本的效果；
- **云边协同初步可行性实验**（表 10）。

## 4. 资源与算力

- 论文在实验设置中仅提及 GPU 型号与显存（RTX 4080 SUPER 32GB、RTX 4090 48GB、H800 80GB），但**未明确说明 GPU 数量、训练时长或推理总时间等具体算力投入**；
- 未提及任何训练过程（方法本身无需训练，仅推理阶段运行算法）；
- 附录中提及了一次 H800（云）与 RTX 4090（边）的协同可行性验证实验，模型为 Qwen2.5-7B-Instruct-1M，知识库为 480K tokens。

## 5. 实验数量与充分性

### 实验组数较多且覆盖较全面

- 主实验：2 个主模型 × 8 个数据集 × 2 个预算级别（20%、10%），加上 14B 模型的补充实验；
- 预算比率扫描实验：10 个档位（10%–100%）的归一化性能对比；
- 消融实验：3 组（无融合、仅 head 级、仅 layer 级、完整方法）；
- 参数敏感性实验：3 个超参数（β 四个值、t_neg 四个值、γ 四个值）；
- 负样本消融实验：2 种设置 × 2 个预算级别；
- 效率评测：10 个知识库问题的延迟与内存统计；
- 云边协同可行性实验：单一配置验证。

### 评价

- **优点**：实验覆盖面较广，涵盖三种模型规模（7B/8B/14B）、四种能力类别、多个预算级别；消融实验清晰验证了各组件贡献；对超参数有敏感性分析；并验证了模型无关性。
- **局限**：主要基准限于 SCBench 一个 benchmark（尽管其包含多个子任务）；查询感知方法的对比仅各取一个代表；效率实验中仅 10 个问题，样本量较小；云边协同实验仅为初步验证（单一模型、单一知识库）。

## 6. 主要结论与发现

1. **核心性能**：在仅保留 **20% KV 缓存预算**时，ContrastKV 保持了原模型 **92% 的准确率**；在极端 **10% 预算**下仍保持 74% 的准确率，显著优于现有查询无关方法（KVzip 在 20% 预算下仅为约 70%）。
2. **对比优势**：在 20% 预算下，ContrastKV 比 SOTA 查询无关方法平均高出 22%；在字符串检索类任务上优势最为显著（如 Qwen2.5-7B 模型的 Retr.Prefix-Suffix 从 2.40% 提升到 27.2%）。
3. **预算感知行为**：当预算充足（≥50%）时，ContrastKV 略落后于 KVzip；但当预算降至 40% 以下（实际有意义的压缩场景）时，ContrastKV 开始显示显著优势。
4. **消融验证**：Head 级融合是主要性能驱动（尤其对字符串检索提升达 42.22%），Layer 级融合提供进一步细化（组合提升达 45.81%）。
5. **效率提升**：使用 20% KV 缓存时，解码延迟从 110.81 ms/token 降至 55.28 ms/token（约 50% 降幅）；GPU 内存从 7.8GB 降至 1.5GB（约 81% 节省），且内存使用随预算近似线性变化。
6. **泛化性**：在三种不同规模的模型上均取得一致结果，验证了方法的模型无关性。
7. **云边协同**：初步实验显示在边缘设备（RTX 4090）使用 ContrastKV 驱逐后的缓存（20% 预算）可以获得 92% 的准确率且避免 OOM，同时解码速度高于云端全缓存运行。

## 7. 优点

- **创新性的对比信号机制**：首次在 KV 缓存驱逐中引入"正（语义）+ 负（结构）"对比信号，以集成学习多样性原理为理论支撑，突破了单一代理查询的盲区；
- **计算友好**：正负信号并行评分，避免了串行处理两条长序列带来的额外延迟；负信号长度极短（t_neg ≤ 128），几乎不增加成本；
- **无训练、可解释**：融合函数为固定线性形式，不引入学习参数，保持了跨模型和任务的鲁棒性和可解释性；
- **两级融合设计合理**：Head 级融合捕捉局部（per-head）关键信息，Layer 级融合细化全局决策，层次清晰、互补明确；
- **充分的问题分析**：从集合论视角形式化了单代理查询的根本局限（公式 3、4），为方法设计提供了理论依据；
- **实际部署导向**：不仅报告准确率，还系统测量了延迟和内存，并探索了云边协同部署方案，贴近真实应用需求。

## 8. 不足与局限

- **预填充阶段内存溢出无法缓解**：如果模型在 prefill 阶段因长知识库输入发生 OOM，ContrastKV 无法解决——这也是大多数 KV 缓存驱逐方法的通病；
- **正样本计算开销高**：由于正样本与知识库等长，注意力计算的时间复杂度高，驱逐算法本身耗时较长。论文回应是驱逐后的缓存可跨多查询复用，且在驱逐完成前系统可先使用全量缓存服务，但在单查询场景下该开销可能难以摊销；
- **基准覆盖有限**：仅使用 SCBench 一个 benchmark（尽管包含多数据集），缺乏在真实 KBQA 任务或更多样化长文本任务上的验证；
- **查询感知基线较弱**：作为对比的查询感知方法（SnapKV、Ada-KV）在多查询场景下表现极差，对比略显"降维打击"，缺乏与更新或更强查询无关方法的对比；
- **效率实验样本量小**：仅用 10 个知识库问题评估延迟和内存，统计稳定性有限；
- **云边协同尚处雏形**：论文仅提出初步概念框架和单一配置的可行性实验，未系统评估传输开销、多用户并发、边缘设备异构性等实际问题；
- **超参数为手工设置**：β、γ、t_neg 虽然做了敏感性分析，但未提出自适应选择机制，跨任务/模型使用时可能需要人工调整。
- **方法的公平性考虑**：由于算法的驱逐阶段本身需要额外计算，论文未将驱逐时间纳入端到端延迟的对比中，可能高估了实际加速效果。

（完）
