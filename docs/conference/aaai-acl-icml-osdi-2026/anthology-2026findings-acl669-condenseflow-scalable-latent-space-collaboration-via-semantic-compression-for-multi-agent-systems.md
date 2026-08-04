---
title: "CondenseFlow: Scalable Latent Space Collaboration via Semantic Compression for Multi-Agent Systems"
title_zh: CondenseFlow：基于语义压缩的可扩展多智能体潜在空间协作
authors: "Xiaoyu Chen, Fengge Wu, Zhao Junsuo, Yun Fan"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.669.pdf"
tags: ["query:agent-cache"]
score: 9.0
evidence: 将KV缓存压缩为固定大小表示，实现多智能体通信与缓存共享的O(1)复杂度
tldr: "基于LLM的多智能体系统在全状态潜在通信时，内存开销随协作轮次线性增长。CondenseFlow提出潜在思想冷凝器，用可学习语义探针将KV缓存压缩为固定大小表示，使通信复杂度降为O(1)。理论证明压缩误差受注意力集中度控制且随轮次可控累积。在七个基准、六个模型上，缓存内存减少超99%，推理延迟降低约20%，性能损失可忽略，为多智能体管道中共享缓存提供了高效方案。"
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 665, \"height\": 365, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1619, \"height\": 1072, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 792, \"height\": 492, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 793, \"height\": 422, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 803, \"height\": 307, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1646, \"height\": 545, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1643, \"height\": 544, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 669, \"height\": 248, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 584, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 664, \"height\": 288, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 547, \"height\": 431, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 697, \"height\": 286, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 837, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 802, \"height\": 273, \"label\": \"Table\"}]"
motivation: 多智能体潜在通信的内存开销随上下文长度线性增长，导致协作轮次增多时难以扩展。
method: 引入潜在思想冷凝器，利用可学习语义探针将KV缓存压缩为固定大小表示，实现与上下文长度无关的通信。
result: "在七个基准、六个模型上，KV缓存内存减少超99%，推理延迟降低约20%，性能损失可忽略。"
conclusion: 表明语义压缩能有效缓解多智能体缓存共享开销，并提供理论误差保证。
---

## Abstract
Full-state latent communication in LLM-based multi-agent systems offers richer semantics than text but suffers from memory overhead scaling linearly with collaboration rounds. We propose CondenseFlow , which introduces the Latent Thought Condenser (LTC) —a lightweight module using learnable semantic probes to compress KV caches into fixed-size representations, achieving 𝒪(1) communication complexity regardless of context length. We theoretically prove that compression error is bounded by attention concentration and accumulates controllably across rounds. On seven benchmarks spanning six models, CondenseFlow reduces KV cache memory by over 99% and inference latency by approximately 20% compared to dense transfer with negligible accuracy degradation, while outperforming text-based methods by 1.7 percentage points on average across all configurations. Code is available at https://github.com/xxy33/condenseflow.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、核心问题与整体含义（研究动机与背景）
- **背景**：大语言模型（LLM）正从单纯的文本生成工具演化为自主智能体，多智能体协作（如 MetaGPT、ChatDev、AutoGen）成为重要方向。传统多智能体系统以自然语言作为通信媒介，但文本是离散符号，存在固有的信息瓶颈，会丢失不确定性估计和细粒度语义信息。
- **潜在空间通信的兴起**：为突破文本瓶颈，近期研究开始让智能体直接传输 Transformer 内部表示（如 KV 缓存），实现高保真信息交换。然而，全状态潜在通信面临严重的“内存墙”问题：内存占用随层数、隐藏维度、序列长度和协作轮数线性增长，复杂度为 O(R·T·L·dh)。对 14B 参数模型，单次传输工作记忆可达数 GB，严重阻碍在消费级硬件或带宽受限环境中的部署。
- **核心挑战**：如何在保留潜在通信高保真优势的同时，严格限定资源消耗，使通信开销与交互深度无关。
- **论文含义**：提出 CondenseFlow，通过语义压缩将 KV 缓存转化为固定大小表示，实现 O(1) 通信复杂度，使潜在空间多智能体协作真正可扩展。

## 二、方法论：核心思想、关键技术细节与算法流程
### 2.1 核心思想
- 将“高效潜在通信”形式化为**语义压缩问题**：学习映射 φθ，将完整工作记忆（每层 K、V 矩阵，形状 T×dh）压缩为固定大小的语义摘要（形状 K×dh，K≪T），从而每轮通信复杂度为 O(1)，且不随上下文长度或协作轮数增长。

### 2.2 Latent Thought Condenser（LTC）模块
- **可学习语义探针**：一组可学习向量 Qc ∈ R^{K×dh}（K 为压缩维度，默认 64）。每个探针作为一个“语义询问器”，通过端到端学习发现协作中最有价值的信息模式（如数值、逻辑连接词、结构标记），而非依赖启发式注意力统计。
- **交叉注意力聚合**：对第 l 层缓存 (K^(l), V^(l))，计算探针与 Key 的相关性：
  - A^(l) = softmax(Qc K^(l)^T / √dh) ∈ R^{K×T}
  - 压缩结果：K̃^(l) = A^(l) K^(l)，Ṽ^(l) = A^(l) V^(l) ∈ R^{K×dh}
  - 相当于将原始 T 个位置加权聚合为 K 个语义摘要向量。
- **轻量设计**：所有 Transformer 层共享同一探针矩阵，仅层归一化参数逐层独立，参数总量约 0.15M（对于 14B 模型不到 0.01%）。

### 2.3 训练目标
- **重建损失**：让压缩后的 KV 缓存与原始缓存在下游注意力输出上一致：L_recon = (1/L) Σ_l ||Attn(Qs, K^(l), V^(l)) − Attn(Qs, K̃^(l), Ṽ^(l))||_F²（Qs 为采样查询）。
- **正则化**：
  - 覆盖正则化：最大化平均注意力分布的熵，防止探针坍缩到少数位置。
  - 正交正则化：约束探针两两相似度，鼓励互补特征捕捉。
- 完整损失：L = L_recon + λ1·L_cover + λ2·L_orth。

### 2.4 协作流程
- 每个智能体接收原始问题 q 和前一轮的压缩缓存 M_{i−1}，推理得到完整缓存 M_full，经 LTC 压缩为 M_prev，再传给下一智能体。每轮用新压缩表示**替换**而非追加历史，保证上下文开销恒为 O(K)。
- 最终智能体解码文本答案。
- 理论保证：压缩误差受注意力集中度 ρ 控制，上界为 2(1−ρ)·V_max·√n_q；多轮误差最坏线性累积（R·δ），实际呈亚线性。

## 三、实验设计
### 3.1 基准与数据集（7 个基准，覆盖三类任务）
- **数学推理**：AIME 2024、AIME 2025、HMMT 2025
- **科学推理**：GPQA-Diamond、MedQA
- **代码生成**：MBPP-Plus、LiveCodeBench

### 3.2 模型（6 个）
- 小规模：Qwen3-8B-Instruct、LLaMA-3.1-8B-Instruct、Gemma-2-9b-it
- 中规模：Qwen3-14B、DeepSeek-R1-Distill-Qwen-14B、Ring-mini-2.0

### 3.3 对比方法
- **TextMAS**：自然语言通信
- **Dense-Latent**：传输完整 KV 缓存（潜在通信上界）
- **CondenseFlow**：本文方法（LTC 压缩）
- 另与 KV 压缩方法比较：Random Pruning、H2O、SnapKV（在相同压缩率下）

### 3.4 评估协议
- **标准协议**：四智能体顺序流水线（Planner → Critic → Refiner → Solver），评估典型协作深度下的压缩保真度。
- **压力测试协议**：迭代 Solver-Critic 交互，最多 20 轮，用 AIME 2025 测试鲁棒性，考察上下文累积效应。

### 3.5 消融实验
- 压缩维度 K 与交互轮数的联合效应（热图分析，K=16/64/128/256 等）。
- 损失函数各组件（有无覆盖正则、正交正则）的贡献。
- 与选择性压缩方法（Random/H2O/SnapKV）的对比。

## 四、资源与算力
- **训练资源**：LTC 训练使用单张 NVIDIA A100-80G，约 4 GPU 小时（50,000 步，batch size 64，学习率 1e-4，余弦衰减）。
- **推理资源**：所有实验均在 NVIDIA A100-80G GPU 上进行；标准协议单卡运行，压力测试协议单卡加梯度检查点。
- **说明**：论文未明确给出总 GPU 数量、并行策略或端到端完整训练总耗时（仅给出 LTC 模块训练成本），但所报资源开销较低，符合模块轻量化的主张。

## 五、实验数量与充分性
- **实验总量**：7 个基准 × 6 个模型的标准协议测试（共 42 个模型-任务组合，每个结果 5 次运行取均值±标准差）；压力测试（1 个基准、1 个模型，20 轮）；4 组消融（压缩维度热图、损失组件、替代压缩方法、有效秩分析）；另有案例研究（AIME 2025 具体题目）。
- **充分性评价**：
  - **优点**：覆盖多类任务、多规模模型，既评估压缩保真度（标准协议）又评估长程鲁棒性（压力测试）；包含理论分析、有效秩实证和消融，证据链条完整。
  - **不足**：压力测试仅在一个基准（AIME 2025）和单一模型（Qwen3-14B）上进行，泛化结论有限；训练数据与评估基准刻意分离，但训练数据量较小（各 1000 样本），可能限制跨域泛化；所有模型均为同构、同规模，未涉及异构模型协作。

## 六、主要结论与发现
- **内存效率**：CondenseFlow 相比 Dense-Latent 将 KV 缓存内存减少 99% 以上（如 Qwen3-14B 在 10 轮时从 5.03 GB 降至 0.01 GB），且不随交互深度增长。
- **推理延迟**：每轮推理时间保持稳定（约 44 秒），累计时间在 10 轮时比 Dense-Latent 降低约 20%（457s vs 569s）。
- **准确性**：
  - 与 Dense-Latent 相比，平均精度下降低于 2%（小模型约 1.6%、中模型约 1.2%），代码生成任务上甚至持平或反超。
  - 与 TextMAS 相比，在所有配置上平均提升 1.7 个百分点。
- **长程鲁棒性**：压力测试中，TextMAS 和 Dense-Latent 在 4-5 轮后显著退化（20 轮时降至 12% 和 21%），而 CondenseFlow 在 20 轮内保持 58% 以上准确率，验证了固定大小压缩可有效避免上下文累积造成的“约束遗忘”和“注意力分散”。
- **压缩维度**：K=64 是最优平衡点；K=16 导致早期坍缩；K>64 收益递减且后期退化模式接近 Dense-Latent。
- **有效秩分析**：所有模型 KV 缓存中位有效秩低于 50（38–49），且中规模模型有效秩更低，解释了压缩在更大模型上精度损失更小的现象。

## 七、优点
1. **明确的问题形式化**：将潜在通信效率问题转化为语义压缩问题，并给出严格的压缩误差上界（基于注意力集中度）和多轮误差累积分析，理论支撑扎实。
2. **轻量且高效的设计**：LTC 参数仅 0.15M，跨层共享探针，训练成本极低（4 GPU 小时），但带来 99%+ 内存缩减和 20% 延迟下降，实用性强。
3. **学习型压缩优于启发式剪枝**：通过端到端学习自动发现语义关键信息，避免了随机剪枝/H2O/SnapKV 等选择式方法的信息丢失，在相同压缩率下精度显著更高。
4. **鲁棒性验证充分**：压力测试明确展示了文本和全状态潜在方法在长程协作下的退化现象，而 CondenseFlow 保持稳定，这一发现对多智能体系统设计有重要启示。
5. **低秩假设与实证结合**：通过有效秩分析验证了 KV 缓存的低秩特性，为压缩维度选择提供了理论依据，也解释了模型规模扩大时压缩效果更好的原因。
6. **可复现性**：提供了代码仓库、完整超参数、提示词模板和案例研究，便于复现。

## 八、不足与局限
1. **训练依赖**：LTC 需要预训练，相比无训练的全量传输方法增加了部署复杂度（虽有低训练成本，但不适用于零样本场景）。
2. **压缩比上限**：当 K<32 时精度显著下降，存在信息论意义上的压缩极限，无法进一步突破。
3. **同构模型假设**：所有智能体必须具有相同的 KV 缓存维度；异构模型协作需要额外适配层，可能引入新误差，论文未验证。
4. **长序列覆盖不足**：压力测试虽达 20 轮，但单条序列超过 8192 个 token 的超长上下文场景未充分验证。
5. **任务领域有限**：仅涵盖数学、科学、代码，法律、金融等专业领域可能需要特定语义探针才能达到最佳效果。
6. **可解释性与伦理风险**：潜在通信降低了智能体间信息交换的透明度，难以审计和检测恶意或异常行为，同时效率提升可能降低滥用门槛（如自动生成虚假信息）。
7. **实验上的具体局限**：
   - 压力测试仅使用单一基准和单一模型，结论外推需谨慎。
   - 与 TextMAS 的比较可能受提示词设计影响，未完全控制文本通信的提示优化变量。
   - 训练数据与评估基准来源不同（有意设计），但训练域（GSM8K、MBPP）与评估域（如 AIME、GPQA）复杂度差异大，泛化机制依赖潜在语义结构相似性假设，缺少直接证据。

（完）
