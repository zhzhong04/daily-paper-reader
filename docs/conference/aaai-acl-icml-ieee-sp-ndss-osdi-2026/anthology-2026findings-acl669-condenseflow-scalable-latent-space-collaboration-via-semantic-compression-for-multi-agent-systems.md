---
title: "CondenseFlow: Scalable Latent Space Collaboration via Semantic Compression for Multi-Agent Systems"
title_zh: CondenseFlow：通过语义压缩实现多智能体系统的可扩展潜空间协作
authors: "Xiaoyu Chen, Fengge Wu, Zhao Junsuo, Yun Fan"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.669.pdf"
tags: ["query:awc"]
score: 7.0
evidence: 将KV缓存压缩为固定大小表示用于多智能体通信，属于智能体缓存机制
tldr: "基于LLM的多智能体系统中，全状态潜空间通信语义丰富但内存开销随协作轮数线性增长。本文提出CondenseFlow，引入轻量级模块Latent Thought Condenser（LTC），利用可学习语义探针将KV缓存压缩为固定大小表示，实现O(1)通信复杂度，并证明压缩误差受注意力集中度约束且跨轮可控。在七个基准和六个模型上，相比稠密传输，KV缓存内存减少超过99%，推理延迟降低约20%。该工作为多智能体协作提供可扩展的语义压缩通信方案。"
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 665, \"height\": 365}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1619, \"height\": 1072}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 792, \"height\": 492}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 793, \"height\": 422}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl669/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 803, \"height\": 307}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1646, \"height\": 545}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1643, \"height\": 544}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 669, \"height\": 248}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 584, \"height\": 252}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 664, \"height\": 288}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 547, \"height\": 431}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 697, \"height\": 286}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 837, \"height\": 343}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl669/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 802, \"height\": 273}]"
motivation: 多智能体潜空间通信内存开销随协作轮数线性增长，限制可扩展性。
method: 提出Latent Thought Condenser模块，用可学习语义探针将KV缓存压缩为固定大小表示，实现O(1)通信复杂度。
result: "在七个基准六种模型上KV缓存内存降低超99%，推理延迟降低约20%，且压缩误差可控。"
conclusion: 语义压缩能显著降低多智能体通信内存开销，是可扩展潜空间协作的有效方案。
---

## Abstract
Full-state latent communication in LLM-based multi-agent systems offers richer semantics than text but suffers from memory overhead scaling linearly with collaboration rounds. We propose CondenseFlow , which introduces the Latent Thought Condenser (LTC) —a lightweight module using learnable semantic probes to compress KV caches into fixed-size representations, achieving 𝒪(1) communication complexity regardless of context length. We theoretically prove that compression error is bounded by attention concentration and accumulates controllably across rounds. On seven benchmarks spanning six models, CondenseFlow reduces KV cache memory by over 99% and inference latency by approximately 20% compared to dense transfer with negligible accuracy degradation, while outperforming text-based methods by 1.7 percentage points on average across all configurations. Code is available at https://github.com/xxy33/condenseflow.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **背景与动机**：基于 LLM 的多智能体系统中，传统文本通信存在离散符号带来的信息瓶颈，会丢失连续推理状态中的不确定性估计与细粒度语义。近期“潜空间通信”（直接传递 Transformer 内部表示）虽然保真度更高，但存在严重的“内存墙”问题：全状态 KV 缓存传输的内存开销随协作轮数、层数、隐藏维度和序列长度线性增长，复杂度为 O(R·T·L·d_h)，在 14B 模型上单次传输可达数 GB，难以扩展到消费级硬件或带宽受限环境。
- **核心问题**：如何在保留潜空间通信高保真优势的同时，严格限制资源消耗，使通信开销不随交互深度增长。
- **整体含义**：论文提出 CondenseFlow，把“高效的潜空间通信”重新定义为“语义压缩问题”，用固定大小的压缩表示替代完整 KV 缓存，使多智能体协作的通信复杂度降为 O(1)，为大规模潜空间协作提供可行的基础设施方案。

## 2. 方法论

### 核心思想
- 引入轻量级模块 **Latent Thought Condenser（LTC）**，用可学习的“语义探针”（learnable semantic probes）将每个 Transformer 层的 KV 缓存压缩为固定 K 维表示（默认 K=64），从而把每轮通信量限制为常数，避免上下文无限累积。

### 关键技术细节
- **问题形式化**：智能体完成推理后的工作记忆为 M_full = {(K^(l), V^(l))}_{l=1}^{L}，K^(l), V^(l) ∈ R^{T×d_h}。目标是学习映射 φ_θ，将其压缩为 M_gist = {(K̃^(l), Ṽ^(l))}，维度为 R^{K×d_h}，其中 K ≪ T。
- **可学习语义探针**：探针矩阵 Q_c ∈ R^{K×d_h} 可看作 K 个“语义询问器”，通过端到端训练自动发现对协作最有价值的信息模式，而非采用基于注意力统计的启发式剪枝。
- **跨注意力聚合**：对每一层缓存，用探针与原始 Key 计算注意力权重 A^(l) = softmax(Q_c (K^(l))^T / √d_h)，然后线性聚合得到 K̃^(l) = A^(l)K^(l)，Ṽ^(l) = A^(l)V^(l)。
- **架构与参数**：所有 Transformer 层共享同一组探针，仅 LayerNorm 参数逐层独立；在 Qwen3-14B 上总参数约 0.15M，不到模型参数的 0.01%。
- **训练目标**：
  - 重建损失：让压缩前后注意力输出尽可能一致；
  - 覆盖正则：最大化平均注意力分布的熵，防止探针坍缩；
  - 正交正则：约束探针两两正交，鼓励互补特征提取。
- **协作流程**：每个 Agent 接收原始问题 q 和上一轮压缩表示 M_{prev}，生成当前轮 KV，经 LTC 压缩后传给下一 Agent；每轮用“替换”而非“追加”历史表示，保证上下文上界为 O(K)。最终 Agent 解码输出答案。
- **理论保障**：论文证明压缩误差上界为 2(1−ρ)V_max√n_q，其中 ρ 为注意力集中度；误差随轮数最坏线性累积，但实际呈亚线性增长。LTC 学习的连续聚合矩阵覆盖了最优硬选择矩阵，因此其表达能力足以达到该误差上界。

## 3. 实验设计

### Benchmark 与数据集
- **数学推理**：AIME 2024、AIME 2025、HMMT 2025
- **科学推理**：GPQA-Diamond、MedQA
- **代码生成**：MBPP-Plus、LiveCodeBench
- 共 **7 个基准**，覆盖三类推理能力。

### 模型
- **小规模模型**：Qwen3-8B-Instruct、LLaMA-3.1-8B-Instruct、Gemma-2-9b-it
- **中等规模模型**：Qwen3-14B、DeepSeek-R1-Distill-Qwen-14B、Ring-mini-2.0
- 共 **6 种模型**。

### 对比方法
- **TextMAS**：纯文本通信；
- **Dense-Latent**：完整 KV 缓存传输；
- **CondenseFlow**：本文提出的 LTC 压缩通信；
- 另外在消融中对比了 **Random Pruning、H2O、SnapKV** 等 KV 压缩方法。

### 评测协议
- **标准协议**：Planner → Critic → Refiner → Solver 四 Agent 顺序流水线，评估典型协作深度下的压缩保真度。
- **压力测试协议**：Solver-Critic 多轮迭代，在 AIME 2025 上测试最长 20 轮的上下文累积鲁棒性。

## 4. 资源与算力

- 论文明确说明：LTC 训练在 **单张 NVIDIA A100-80G** 上约需 **4 GPU 小时**。
- 推理实验也基于 A100-80G：标准协议用单卡，压力测试用单卡并开启梯度检查点。
- 整体训练开销很低，因为 LTC 参数量极小（约 0.15M）。

## 5. 实验数量与充分性

### 实验量
- 标准协议下在 6 个模型 × 7 个基准上各做 5 次重复，报告均值±标准差，共覆盖大量配置；
- 压力测试分析了 1–20 轮交互下的准确率、内存和推理时间变化；
- 消融实验包括：压缩维度 K 与轮数的联合影响、三个损失项的去留分析、与 H2O/SnapKV 等方法的对比；
- 附录还包含有效秩分析、逐任务误差分析、案例研究。

### 充分性与公平性评价
- **优点**：覆盖模型规模多样（8B 到 14B）、任务类型多样（数学/科学/代码），且对随机种子多次重复，统计上较规范；压力测试和消融设计能有效支撑主要结论。
- **潜在不足**：
  - 推理模型均限于同构模型，未验证跨模型/异构场景；
  - 标准协议只到 4 个 Agent，协作规模本身不算大；
  - 所有实验均在 A100 上进行，未涉及更低端硬件或带宽受限环境的实测；
  - 训练数据与评测基准不同源，但训练集规模较小（各 1000 条），泛化机制依赖“可迁移的语义结构”假设，需要更多验证。

## 6. 主要结论与发现

- **极高的压缩效率**：相比 Dense-Latent，CondenseFlow 将 KV 缓存内存减少超过 99%（例如 Qwen3-14B 在 10 轮时从 5.03GB 降到 0.01GB），且通信量不随轮数增长。
- **推理延迟降低**：在 10 轮压力测试中，CondenseFlow 累计耗时 457 秒，Dense-Latent 为 569 秒，总时间减少约 20%；单轮耗时保持稳定，而基线随上下文增长而上升。
- **准确率保持良好**：与 Dense-Latent 相比，小规模模型平均下降约 1.6%，中等规模模型约 1.2%，总体“可忽略”；平均比 TextMAS 高 1.7 个百分点。
- **鲁棒性突出**：在 20 轮压力测试中，TextMAS 和 Dense-Latent 在 4–5 轮后准确率显著下滑（分别从 54%/63% 降至 12%/21%），CondenseFlow 始终保持在 58% 以上，表明固定大小压缩能有效缓解上下文累积导致的推理退化。
- **压缩维度选择**：K=64 是最优权衡；K=16 时性能迅速崩溃，K 超过 64 后收益递减且后期仍会出现类似 Dense-Latent 的退化。

## 7. 优点

- **方法设计新颖且实用**：用“可学习语义探针 + 跨注意力聚合”把 KV 缓存压缩问题转化为可微的语义摘要学习，避免了启发式剪枝的硬性信息丢失，同时保持了极小的参数开销。
- **理论保障完整**：给出了注意力输出误差上界的严格证明，并说明连续聚合矩阵表达能力不低于最优选择策略，为方法的有效性提供了原理性支撑。
- **实验覆盖面较广**：多基准、多模型、双协议、完整消融，加上内存/延迟/有效秩/案例研究，证据链较为完整。
- **清晰的可扩展性优势**：将上下文通信从“随轮数线性增长”变为“常数级”，直接解决了潜空间多智能体系统最关键的扩展瓶颈。

## 8. 不足与局限

- **需要训练**：LTC 不是零训练方法，必须预训练后才能使用；虽然训练成本低，但相比训练免费的 LatentMAS 等增加了部署复杂度。
- **压缩比存在上限**：K 低于 32 时准确率显著下降，说明存在信息论层面的压缩极限，无法无限压缩。
- **同构模型假设**：当前 LTC 假设所有 Agent 的 KV 维度和表示空间一致；异构模型协作需要额外适配层，可能引入新的误差源。
- **长上下文验证不足**：压力测试最多 20 轮，但未充分验证单条序列超过 8192 token 的极长上下文场景。
- **任务领域偏向**：评测集中在数学、代码和科学推理，法律、金融等专业领域可能需要领域适应性的语义探针。
- **可解释性与安全性**：潜空间通信降低了智能体间信息交换的透明度，可能增加检测恶意或意外行为的难度，也存在被滥用于自动化虚假信息生成的风险；论文只在“限制与伦理”中提及，未提供具体审计机制。
- **案例研究代表性有限**：附录中的 AIME 案例仅为单个示例，虽然生动地说明了失败模式，但不足以证明整体方法的因果机制。

（完）
