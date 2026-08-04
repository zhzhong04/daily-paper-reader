---
title: "Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction"
title_zh: Judge Q：基于可训练查询的KV缓存驱逐信息保留优化
authors: "Yijun Liu, Yixuan Wang, Yuzhuang Xu, Shiyu Ji, Yang Xu, Qingfu Zhu, Wanxiang Che"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40497/44458"
tags: ["query:awc"]
score: 8.0
evidence: 面向LLM的KV缓存驱逐方法，可迁移至智能体系统
tldr: LLM的KV缓存随序列长度线性增长，驱逐策略常用预填充阶段的最后窗口作为查询来计算重要性分数，容易只看局部而丢失全局信息。本文提出Judge Q，在嵌入层加入可训练的软令牌列表，使驱逐查询能捕获全局上下文。该方法只微调嵌入层，计算开销小，无需改变整体结构。实验表明在长序列基准上，Judge Q能更准确地保留关键信息，提高缓存效率和下游解码质量，对多智能体系统中共享KV缓存也有参考意义。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有KV缓存驱逐只依赖最后窗口查询，忽略全局信息。
method: 引入软令牌列表，仅调整嵌入层训练查询。
result: 提升长序列缓存命中率和推理质量。
conclusion: 提供新的KV缓存驱逐训练范式。
---

## Abstract
Large language models (LLMs) utilize key-value (KV) cache to store historical information during sequence processing. The size of KV cache grows linearly as the length of the sequence extends, which seriously affects memory usage and decoding efficiency. Current methods for KV cache eviction typically utilize the last window from the pre-filling phase as queries to compute the KV importance scores for eviction. Although this scheme is simple to implement, it tends to overly focus on local information, potentially leading to the neglect or omission of crucial global information. To mitigate this issue, we propose **Judge Q**, a novel training method which incorporates a soft token list. This method only tunes the model’s embedding layer at a low training cost. By concatenating the soft token list at the end of the input sequence, we train these tokens' attention map to the original input sequence to align with that of the actual decoded tokens. In this way, the queries corresponding to the soft tokens can effectively capture global information and better evaluate the importance of the keys and values within the KV cache, thus maintaining decoding quality when KV cache is evicted. Under the same eviction budget, our method exhibits less performance degradation compared to existing eviction approaches. We validate our approach through experiments conducted on models such as Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3, using benchmarks including LongBench, RULER, and Needle-in-a-Haystack. Results indicate an improvement of approximately 1 point on the LongBench and over 3 points on RULER. This proposed methodology can be seamlessly integrated into existing open-source models with minimal training overhead, thereby enhancing performance in KV cache eviction scenarios.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义

- **研究背景**：大语言模型（LLM）依赖 KV 缓存存储历史信息，但 KV 缓存大小随输入序列长度线性增长，在长序列场景中会严重占用显存并拖慢推理速度。
- **现存问题**：主流的 KV 缓存驱逐方法（如 SnapKV、H2O、PyramidKV）通常使用预填充阶段的"最后窗口"（last window）作为查询来计算键值对的重要性分数，然后保留 Top-k 重要内容。这种方案虽然实现简单，但存在两个明显缺陷：
  - **过度关注局部信息**：仅依赖输入末尾的局部窗口，容易忽略输入中段的全局关键信息。
  - **问题位置敏感**：当问题不出现在输入末尾时，这类方法的性能下降尤为显著（论文实验证实，调整问题位置后性能下降约 10%）。
- **核心发现**：论文通过实验发现，若直接使用**实际解码令牌**的查询来计算 KV 重要性分数进行裁剪，效果远优于现有的所有驱逐方法，可视为该任务的理论上界。但由于预填充阶段解码令牌尚不可知，需要一种方法在预填充阶段近似这一理想方案。
- **核心贡献**：提出 **Judge Q**，通过引入少量可训练"软令牌"，在预填充阶段近似实际解码令牌的全局注意力模式，从而更准确地评估 KV 缓存中键值对的重要性，兼顾压缩率与生成质量。

## 2. 方法论：核心思想、技术细节与流程

### 核心思想
- 在模型词汇表中追加一组**可训练软令牌（soft tokens）**，通过训练使其对输入序列的注意力图（attention map）与真实解码令牌的注意力图对齐，从而让软令牌能够"预判"哪些键值对对于后续解码最关键。
- 推理时利用这些软令牌的注意力分数作为 KV 驱逐的依据。

### 关键技术细节
- **训练目标**：最小化软令牌注意力图与真实响应令牌注意力图之间的均方误差（MSE）。公式如下：
  - 软令牌注意力图：  
    `A_soft = (1/n) Σ Attention(Prompt, Soft_i)`
  - 真实响应注意力图：  
    `A_resp = (1/m) Σ Attention(Prompt, Resp_j)`
  - 损失函数：  
    `L = MSE(A_soft, A_resp)`
- **参数效率**：只微调模型中**嵌入层中与软令牌对应的那一小部分参数**，其余所有模型权重完全冻结，训练成本极低。

### 训练与推理流程
1. **训练阶段**：将软令牌列表拼接到输入末尾，将真实响应也分别拼接到输入末尾，分别计算两者对原始输入（Prompt）的注意力图，通过 MSE 损失对齐二者。
2. **预填充阶段**：将 n 个软令牌追加到输入末尾，前向传播后计算软令牌对全部输入 token 的注意力分数，保留分数最高的 Top-k 个键值对，其余丢弃。
3. **解码阶段**：移除软令牌，使用裁剪后的 KV 缓存从原始输入末尾继续解码。

## 3. 实验设计

### 评测基准
- **LongBench**：多任务长上下文理解基准，涵盖单文档问答、多文档问答、摘要、少样本学习、合成任务、代码理解等 6 大类共 16 个子任务。
- **RULER**：长上下文检索与推理基准，测试序列长度设为 8192 和 32768 两种。
- **Needle-in-a-Haystack**：长文本检索压力测试，文档深度百分比间隔为 10%，长度范围 4000 至 32000。

### 测试模型
- Llama-3.1-8B-Instruct
- Mistral-7B-Instruct-v0.3
- 另外在 Llama-3.2-1B-Instruct（数据质量消融）和 DeepSeek-R1-Distill-Llama-8B（文本续写任务）上有补充实验。

### 对比方法（Baselines）
- **StreamingLLM**：启发式保留初始 token + 局部窗口。
- **H2O**：基于累计注意力分数进行动态驱逐。
- **SnapKV**：使用局部窗口注意力分数 + 池化机制。
- **PyramidKV**：在 SnapKV 基础上按层动态分配预算。

### 预算设置
- LongBench：KV 缓存大小为 128 / 256 / 512。
- RULER：KV 缓存大小为 256 / 512 / 1024。

### 训练数据
- ShareGPT 数据集子集（50,000 个样本，45,000 来自通用领域，5,000 来自计算机领域）。
- 软令牌数量 n = 32。

## 4. 资源与算力

- **论文未明确报告** GPU 型号、数量及具体训练时长等算力信息。仅在训练配置中提到使用 ShareGPT 50,000 个样本进行训练、仅微调嵌入层参数、序列长度与基线设定保持一致。
- 由于只训练嵌入层中极小一部分参数（软令牌对应的嵌入向量），可合理推断其训练开销远低于全量微调或 LoRA 等常见方案，但论文未给出确切数字。

## 5. 实验数量与充分性

### 实验数量
- **LongBench**：2 个模型 × 3 种预算 × 16 个子任务，共 96 组对比结果。
- **RULER**：2 个模型 × 2 种长度 × 3 种预算，共 12 组对比。
- **Needle-in-a-Haystack**：1 个模型（附可视化结果）。
- **关键 KV 命中率实验**：Judge Q vs SnapKV 在 3 种预算下的对比。
- **文本续写任务**：MATH-500 和 AIME24 两个数据集，预算分别为输出长度的 25%。
- **消融实验**：
  - 数据质量：ShareGPT vs C4 vs Wikipedia vs GitHub。
  - 模型生成响应 vs 原始响应。
  - 软令牌数量（n）对训练损失和可训练参数量的影响。
- **Prompt 位置调整稳定性测试**：将问题移到开头后比较各方法的性能退化比例。

### 充分性与客观性评估
- **优点**：实验覆盖了多个主流基准、两种不同架构的模型、多种预算条件，并有消融和案例分析，整体设计较全面。
- **不足**：
  - 只针对 8B/7B 规模的模型，未验证更大规模（如 70B+）模型。
  - 训练数据仅来自 ShareGPT 单一来源，未在更大规模、更多领域的数据上验证。
  - 所有基线使用相同的局部窗口大小（32），虽然公平但对某些基线可能并非最优配置。
  - 理论分析较薄弱，缺乏对软令牌为何能有效泛化到未见数据的深入解释。

## 6. 主要结论与发现

- **Judge Q 在三个基准上均一致优于现有预填充阶段的 KV 驱逐方法**：LongBench 提升约 1 分，RULER 提升超过 3 分（最高接近 10 分），Needle-in-a-Haystack 上显著超过基线。
- **低预算场景下优势更明显**：KV 缓存预算越小，Judge Q 相对基线的提升幅度越大，说明其信息保留效率更高。
- **关键 KV 命中率更高**：Judge Q 的键值对命中率比最佳基线 SnapKV 高约 8 个百分点，说明其更接近"使用实际解码令牌"的理论上界。
- **对问题位置更鲁棒**：将问题从输入末尾移到开头后，Judge Q 的性能损失不超过 7%，低于基线的约 10%。
- **训练数据质量影响显著**：使用模型生成的响应优于直接使用原始数据；ShareGPT 作为训练数据优于 C4、Wikipedia 和 GitHub。
- **软令牌数量存在最优平衡点**：n = 32 左右在训练成本和泛化性能之间达到最佳权衡。

## 7. 优点

- **轻量高效**：只训练嵌入层的极小部分参数，训练成本极低，可无缝适配任何开源模型。
- **思路新颖**：将"软令牌对齐实际解码令牌注意力图"作为训练目标，从理论上逼近 KV 驱逐的性能上界，角度独特。
- **普适性强**：不改变模型结构，不增加推理时计算负担，可作为即插即用模块与其他方法结合。
- **实验详尽**：在 3 大基准、2 种模型、多种预算下验证，并补充了命中率分析、位置鲁棒性测试、数据质量消融和案例分析。
- **效果显著**：特别是在低预算（高压缩率）场景下提升幅度大，实际应用价值高。

## 8. 不足与局限

- **算力信息缺失**：未报告 GPU 型号、数量和训练耗时，影响可复现性和成本评估。
- **模型规模覆盖有限**：仅在 7B/8B 级模型上验证，未测试更大规模模型下的有效性。
- **训练数据单一**：只用了 ShareGPT 的 50k 样本，未充分验证训练数据规模与多样性对方法的影响。
- **理论解释不足**：缺乏对软令牌注意力对齐为何能泛化到不同任务和长序列的深入理论分析。
- **基线配置可能非最优**：统一使用窗口大小 32 虽保证了公平，但个别基线在更大窗口下可能有更好表现。
- **对长序列极度场景的验证有限**：RULER 最长 32K，未测试 100K+ 超长文本下的表现。
- **未来工作缺失**：论文提到计划实现解码过程中的流式驱逐，说明当前方法仍以预填充阶段静态驱逐为主，动态场景下可能有局限。

（完）
