---
title: "ContrastKV: Robust KV Cache Eviction via Contrastive Signal Fusion for Multi-Query Generalization"
title_zh: ContrastKV：通过对比信号融合实现多查询泛化的鲁棒KV缓存驱逐
authors: "Xingchi Chen, Peiyuan Zong, Ziqiang Gao, Qing Li, Yong Jiang, Fa Zhu, Hui Li"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.417.pdf"
tags: ["query:agent-cache"]
score: 6.0
evidence: 面向多查询泛化的鲁棒KV缓存驱逐算法，可迁移至智能体工作流中的缓存驱逐需求
tldr: 论文针对长上下文推理中KV缓存内存占用问题，指出查询感知的驱逐难以在多查询间泛化，而现有依赖单一代理查询的方法在高驱逐率下不稳定。为此提出ContrastKV，通过对比信号融合语义与非语义信号，形成鲁棒的查询无关驱逐算法。实验证明在多查询问答等场景下有效提高驱逐决策的鲁棒性，可缓解高驱逐率带来的性能损失，可作为智能体工作流中KV缓存驱逐的基础方法。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1573, \"height\": 496, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 794, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 779, \"height\": 901, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 774, \"height\": 871, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long417/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1579, \"height\": 911, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1653, \"height\": 1425, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 521, \"height\": 468, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1654, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 800, \"height\": 219, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1645, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 800, \"height\": 253, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 800, \"height\": 256, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 798, \"height\": 256, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1652, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long417/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1660, \"height\": 1802, \"label\": \"Table\"}]"
motivation: 现有KV缓存驱逐算法在高驱逐率下决策脆弱，且查询感知方法难以泛化到多个下游查询。
method: 提出对比信号融合机制，联合利用语义与非语义信号，构造鲁棒的查询无关KV缓存驱逐算法。
result: 在多查询设置中显著提升缓存驱逐的鲁棒性，并保持较高性能。
conclusion: 融合互补信号可实现更稳健的KV缓存驱逐，适用于多查询/多下游任务场景。
---

## Abstract
Large Language Models (LLMs) face significant memory and latency overheads during long-context inference due to the growing KV cache, especially in Knowledge Base Question Answering (KBQA) settings that require support for multiple downstream queries. Query-aware eviction methods do not generalize across queries, while existing query-agnostic approaches rely on a single proxy query, leading to fragile eviction decisions under high eviction ratios. We propose ContrastKV, a robust query-agnostic KV cache eviction algorithm for multi-query generalization. ContrastKV introduces a contrastive signal fusion mechanism that jointly exploits complementary semantic and non-semantic signals. By contrasting semantic consistency with structural robustness, the method constructs a more reliable eviction criterion that alleviates the blind spots of single-query proxies. The framework integrates efficient signal generation, parallel importance scoring, and multi-level fusion across heads and layers. Experiments show that ContrastKV outperforms state-of-the-art methods, retaining up to 92% accuracy with only 20% of the KV cache budget, while reducing decoding latency by approximately 50% and significantly lowering GPU memory usage.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机与背景）

- **核心问题**：大语言模型（LLM）在长上下文推理中，因 KV 缓存随序列长度增长而产生严重的显存占用和延迟开销。在知识库问答（KBQA）等场景中，一个大型知识库需支撑多个下游查询，KV 缓存膨胀问题尤为突出。
- **现有方法的不足**：
  - **查询感知（Query-aware）方法**（如 SnapKV、Ada-KV）依据当前查询语义决定驱逐策略，但无法在多查询场景下泛化，一旦查询变化，缓存中的关键信息可能已被错误清除。
  - **查询无关（Query-agnostic）方法**（如 KVzip）不依赖具体查询，但其依赖单一代理查询（如知识库重建提示词）近似全局最优，在高驱逐率（如保留比例低于 30%）下决策边界脆弱，性能显著下降。
- **核心观察**：从集合论视角看，理想通用查询应覆盖所有可能查询的重要 KV 对之并集，单一代理查询难以做到；理论上 KV 缓存可压缩至 5%，但现有方法实际仅能稳定压缩至约 30%，存在较大的优化空间。
- **论文整体含义**：提出一种用对比信号构造更可靠驱逐判据的思路，以缩小理论压缩极限与实际性能之间的差距，使 KV 缓存在多查询场景下仍可高比例压缩而不显著损失精度。

---

## 2. 论文提出的方法论

### 2.1 核心思想

- 借鉴集成学习中的多样性原理：互补信号的对比可以降低泛化误差。
- 不再依赖单一代理查询，而是同时使用**正信号（语义信号）**与**负信号（结构信号）**，通过对比两者生成更鲁棒的驱逐判据，覆盖更多潜在重要 KV 对。

### 2.2 三个关键阶段

1. **对比信号生成（Contrastive Signal Generation）**：
   - 正信号 `q_pos`：采用知识库重建提示词，长度与知识库一致（`t_pos = n`）。
   - 负信号 `q_neg`：随机生成一段**最大熵噪声序列**（长度 `t_neg` 远小于 n），每个 token 从词汇表中均匀采样，与知识库语义无关，用于提供纯结构基线，凸显“注意力汇（attention sink）”token。

2. **并行重要性评分（Parallel Importance Scoring）**：
   - 将正负信号与完整 KV 缓存并行输入 LLM，独立计算注意力矩阵。
   - 对每个层 `l` 和注意力头 `h`，取跨 query 组和 token 维度上的最大注意力分数作为该 KV 对的重要性得分：

   ```
   S_l,h = max_{g=1..G; i=1..t_pos/neg} A_l,h[g, i] ∈ R^n
   ```

3. **对比融合机制（Contrastive Fusion）**——两级融合：
   - **Head-level Fusion（头级融合）**：以 β 分位数设置上下阈值，防止低注意力总和的注意力头被整体清除。若某位置在正负信号中均高（≥1−β 分位），则提升为 1.0；若均低（≤β 分位），则置 0；否则保留正信号原始分数。从而保证每个头都保留少量高潜力 KV 对。
   - **Layer-level Fusion（层级融合）**：对头级融合中未做出明确决策的位置，根据 min-max 归一化后的负信号分数对正信号分数做增量增益（增益强度由超参数 γ 控制），公式如下：

   ```
   Ŝ_neg_i = (S_neg_i − min(S_neg)) / (max(S_neg) − min(S_neg))
   Ŝ_i = min(S_pos_i + γ · Ŝ_neg_i, max(S_pos_i))
   ```

   - 该机制不覆盖主语义信号，仅在边界处温和提升结构上稳健的 token。

---

## 3. 实验设计

### 3.1 评测基准

- 使用 **SCBench** 基准的 11 个数据集，覆盖四类长文本能力：字符串检索（String Retrieval）、语义检索（Semantic Retrieval）、全局信息（Global Information）、多任务处理（Multi-tasking）。
- 参数研究选用每类中一个代表性数据集；主实验和消融实验使用其余 8 个数据集（每类 2 个）。

### 3.2 对比方法

- **查询感知方法**：SnapKV、Ada-KV（含 Ada-SnapKV 变体）。
- **查询无关方法**：KVzip（当前 SOTA）。
- 各基线均采用原始论文配置（如 SnapKV 的 pooling kernel=7、observation window=32；KVzip 的 chunk size=2K）。

### 3.3 评估指标

- 各数据集按任务类型选择指标：ROUGE（En.Sum）、Pass@1（Code.RepoQA）、Accuracy（其余）。

---

## 4. 资源与算力

- 论文未明确报告 GPU 数量、训练时长或总算力投入。
- 实验环境仅提及：PyTorch 2.1、Python 3.10、CUDA 12.1；Qwen2.5-7B 实验使用 1×RTX 4080 SUPER（32GB），Llama3.1-8B 使用 1×RTX 4090（48GB），Qwen2.5-14B 实验未注明具体 GPU。
- 附录 A.5 云-边协同可行性实验中，使用 H800 80GB（模拟云端）与 RTX 4090 24GB（模拟边缘端）。
- 总体而言，实验以单卡推理为主，未涉及集群级大规模训练/评测算力。

---

## 5. 实验数量与充分性

### 主要实验组

- **主实验（表 1）**：Qwen2.5-7B 与 Llama3.1-8B 在 8 个基准上、2 种预算（10%、20%）下的系统对比；另在 Qwen2.5-14B 上补充模型规模泛化验证。
- **保留率变化实验（表 2）**：Qwen2.5-7B 上测试 10% 至 100% 共 10 档预算比例。
- **消融实验（表 3）**：分别验证 head-level 融合与 layer-level 融合的独立贡献，及其组合效果。
- **效率实验（表 4）**：基于陌生代码库（TheoremExplainAgent，发布于模型训练之后）构造 10 个问题，评测解码延迟与显存占用。
- **附加热敏实验**：对比样本选择（随机串 vs. 知识库前 10%）、β/t_neg/γ 参数扫描、注意力分数可视化、云-边协同预实验。

### 充分性评估

- **充分性较高**：覆盖 3 种规模模型、8+ 个基准、2 种压缩预算、多组消融与参数研究，对核心方法的验证较系统。
- **客观性良好**：采用公开基准 SCBench，且效率实验使用模型训练后发布的数据，避免参数记忆污染。
- 部分不足之处：未见与更近期查询无关方法（如 CompactOR）在主实验中的对比；未见对长上下文（>128K）与超大模型（>14B）的验证；效率实验仅报告单次结果，未提供方差或置信区间。

---

## 6. 论文的主要结论与发现

- **ContrastKV 在多查询场景下显著优于现有方法**：在 20% KV 预算下保持全量缓存的约 92% 精度，较 SOTA 查询无关方法（KVzip）提升约 22 个百分点；在 10% 极端预算下仍保持约 74% 精度。
- **查询感知方法在多查询设置下几乎失效**：SnapKV、Ada-KV 在字符串检索等任务上最低降至 0.2%~6%，验证了其对单查询过拟合的缺陷。
- **高驱逐率下 ContrastKV 的优势大幅体现**：预算充足（≥50%）时与 KVzip 接近；预算低至 40% 以下时，优势越来越大，这正是 KV 驱逐技术最有价值的操作区间。
- **两级融合均有效，head-level 融合贡献更大**：尤其对字符串检索任务提升高达 42.22%，反映其对多查询泛化的核心支撑作用。
- **效率收益明显**：20% 预算下解码延迟减少约 50%，显存占用从 7.8GB 降至 1.5GB（近似线性缩减）。
- **云-边协同部署可行性初步验证**：在边缘端（RTX 4090）运行 20% 预算的 ContrastKV 缓存，可在不 OOM 的情况下达到与云端全量缓存接近的准确率，同时解码速度更快。

---

## 7. 优点

- **思想创新性强**：将集成学习中的“多样性降低泛化误差”原则引入 KV 驱逐，用正/负对比信号突破单一代理查询的盲区，理论动机清晰。
- **方法设计巧妙**：
  - 负信号采用最大熵随机噪声序列，短小（≤128 tokens）且语义无关，计算开销极小。
  - 正负信号并行评分，避免双序列串行计算所带来的额外延迟。
  - 两级融合机制兼顾全局覆盖（head-level）与局部精度（layer-level），在不掩盖主语义信号的前提下提升了决策鲁棒性。
- **实用性突出**：高驱逐率下仍能保持较好的准确率，直接改善了资源受限场景下的部署可行性；驱逐缓存可跨查询复用，一次性成本在实际多轮问答中被摊薄。
- **工程验证完整**：除学术基准外，还采用模型训练发布之后出现的真实代码库进行问答验证，排除参数记忆干扰，结论更有说服力。
- **融合函数固定而非学习**：避免了额外的训练/微调开销，增强了跨模型、跨任务的泛化性与可解释性。

---

## 8. 不足与局限

- **无法解决 prefill 阶段的显存溢出**：若知识库在预填充阶段就超出显存容量，ContrastKV 无法提供缓解，只能处理已成功生成 KV 缓存之后的问题。
- **驱逐阶段时间长**：正信号长度与知识库等长，注意力计算时间复杂度高，驱逐过程本身耗时较多（依赖于多查询场景摊薄成本）。
- **超参数依赖人工设定**：β、γ、t_neg 均需手动选择，虽敏感性分析显示范围较宽，但缺乏自适应调节机制。
- **基准覆盖有限**：SCBench 主要集中在英文检索与推理任务，未涉及多语言、多模态或流式/动态知识库；云-边协同框架仅为初步构想，尚无完整系统实现。
- **大规模模型验证不足**：最大测试模型为 Qwen2.5-14B，未在更大规模（如 70B+）或 MoE 架构上验证有效性。
- **效率实验报告不完整**：解码延迟与显存为 10 个查询的平均值，未报告标准差；未与传统序列化（先重建后驱逐）的时间开销做对比报告。
- **风险提示**：随机负信号的特异性在不同语言/领域知识库中的稳定性、以及对注意力分布极度不均匀模型（如 DeepSeek-V3）的适用性，仍需进一步研究。

（完）
