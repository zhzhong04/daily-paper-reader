---
title: "Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction"
title_zh: Judge Q：面向KV缓存驱逐优化的可训练查询
authors: "Yijun Liu, Yixuan Wang, Yuzhuang Xu, Shiyu Ji, Yang Xu, Qingfu Zhu, Wanxiang Che"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40497/44458"
tags: ["query:agent-cache"]
score: 4.0
evidence: 基于可训练查询的KV缓存驱逐，通用驱逐方法而非面向智能体
tldr: KV缓存驱逐方法通常用前缀阶段最后一个窗口作为查询来计算重要性分数，容易忽略全局信息。Judge Q提出可训练查询（软token列表），仅微调模型嵌入层，让查询学习更全面的重要性度量。实验表明该方法可改善信息保留和生成质量，但对智能体工作流调度与跨Agent缓存复用并未涉及。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40497/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 882, \"height\": 883, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40497/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 871, \"height\": 549, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40497/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1849, \"height\": 510, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40497/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 883, \"height\": 549, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40497/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 899, \"height\": 340, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40497/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 899, \"height\": 344, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40497/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 884, \"height\": 357, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40497/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1830, \"height\": 1578, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40497/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 882, \"height\": 744, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40497/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 883, \"height\": 243, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40497/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 715, \"height\": 242, \"label\": \"Table\"}]"
motivation: 现有驱逐方法使用前缀最后窗口计算重要性，聚焦局部而忽略全局信息。
method: 引入软token列表作为可训练查询，微调嵌入层以优化KV驱逐的重要性评分。
result: 与基线相比提升了缓存信息保留与生成质量。
conclusion: 可训练查询能够更准确地评估token重要性，改进KV缓存驱逐效果。
---

## Abstract
Large language models (LLMs) utilize key-value (KV) cache to store historical information during sequence processing. The size of KV cache grows linearly as the length of the sequence extends, which seriously affects memory usage and decoding efficiency. Current methods for KV cache eviction typically utilize the last window from the pre-filling phase as queries to compute the KV importance scores for eviction. Although this scheme is simple to implement, it tends to overly focus on local information, potentially leading to the neglect or omission of crucial global information. To mitigate this issue, we propose **Judge Q**, a novel training method which incorporates a soft token list. This method only tunes the model’s embedding layer at a low training cost. By concatenating the soft token list at the end of the input sequence, we train these tokens' attention map to the original input sequence to align with that of the actual decoded tokens. In this way, the queries corresponding to the soft tokens can effectively capture global information and better evaluate the importance of the keys and values within the KV cache, thus maintaining decoding quality when KV cache is evicted. Under the same eviction budget, our method exhibits less performance degradation compared to existing eviction approaches. We validate our approach through experiments conducted on models such as Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3, using benchmarks including LongBench, RULER, and Needle-in-a-Haystack. Results indicate an improvement of approximately 1 point on the LongBench and over 3 points on RULER. This proposed methodology can be seamlessly integrated into existing open-source models with minimal training overhead, thereby enhancing performance in KV cache eviction scenarios.

---

## 论文详细总结（自动生成）

# Judge Q：面向KV缓存驱逐优化的可训练查询——论文详细总结

## 1. 论文的核心问题与整体含义

- **研究背景**：大语言模型（LLMs）在长序列处理中依赖 KV（键值）缓存存储历史信息，而 KV 缓存大小随序列长度线性增长，导致内存占用和推理效率成为严重瓶颈。因此，KV 缓存驱逐（KV Cache Eviction）成为重要的优化方向。
- **现有方法的缺陷**：目前主流的预填充（pre-filling）阶段驱逐方法（如 H2O、SnapKV、PyramidKV 等）通常选取输入序列最后一段窗口内的 token 作为查询（query），来计算各键值对的重要性分数并执行驱逐。该做法虽然在实现上简单，但具有两个明显局限：
  1. 过度聚焦局部信息（如最后窗口中的局部上下文），容易忽略全局关键信息；
  2. 若最后窗口恰好不包含问题/关键指令，这些方法的性能会显著下降。
- **关键观察**：
  - （1）现有驱逐方法在"问题前移"的提示调整下性能明显劣化，说明其重要性评估存在信息缺失；
  - （2）若直接使用实际解码 token 对应的 query 来选择保留的 KV 对，可显著优于所有现有预填充阶段驱逐方法，可视为该类方法理论上的性能上界。
- **研究目标**：设计一种新的方案，在不依赖未来解码 token 的前提下，从预填充阶段即可评估出与"实际解码 token 选择"高度接近的关键 KV 对，从而在给定预算下最大化信息保留并维持生成质量。

## 2. 论文提出的方法论

**核心思想：**
- 提出一种名为 **Judge Q** 的轻量训练框架。其核心是向模型的词表中引入一组**可训练的软 token（soft tokens）**，仅微调模型嵌入（embedding）层中这些软 token 对应的参数（其余模型参数完全冻结），以极低的训练成本使软 token 学习"如何识别对后续解码最重要的 KV 对"。

**训练阶段：**
- 将软 token 序列拼接在原始输入（prompt）末尾：
  - Input_soft = Concat(Prompt, Soft)
  - Input_resp = Concat(Prompt, Resp)
- 分别计算软 token 与真实响应 token 相对于 prompt 部分的注意力分布（沿 token 维取平均），得到注意力图 A_soft 与 A_resp。
- 使用 **MSE（均方误差）损失** 最小化两者差距：
  - L = MSE(A_soft, A_resp)
- 训练数据来自 ShareGPT 的 50,000 条样本（45,000 条通用领域 + 5,000 条计算机领域），且使用模型自生成响应比原始数据集响应效果更好。软 token 数量默认取 n=32。
- 由于仅训练 embedding 层中极少部分参数，训练开销极低。

**推理阶段（预填充阶段驱逐）：**
- 同样将 n 个软 token 拼接至输入序列末尾；
- 在预填充阶段计算软 token 对整个输入的注意力图（式 3）；
- 依据注意力分数保留 Top-k 最高分的 KV 对，丢弃其余 KV 对；
- 完成驱逐后移除软 token，使用裁剪后的 KV 缓存进行后续解码。

**方法本质：**
- 软 token 作为可训练的"查询探针"，其注意力信号近似"真实解码 token 的注意力模式"，因此能够更好地捕捉全局信息并指导 KV 驱逐，逼近理论性能上界（即使用实际解码 token 进行驱逐的效果）。

## 3. 实验设计

**评估基准：**
- **LongBench**：多任务长上下文理解（含单文档问答、多文档问答、摘要、少样本、合成、代码等 16 个子任务）
- **RULER**：长上下文基准，测试序列长度设为 8192 和 32768
- **Needle-in-a-Haystack**（大海捞针）：长文本中的精确检索测试

**评测模型：**
- Llama-3.1-8B-Instruct
- Mistral-7B-Instruct-v0.3
- 辅助探索实验另用 Llama-3.2-1B-Instruct 和 DeepSeek-R1-Distill-Llama-8B

**对比基线方法（Baselines）：**
- StreamingLLM（保留初始 token + 局部窗口）
- H2O（累积注意力分数）
- SnapKV（局部窗口注意力 + 池化）
- PyramidKV（SnapKV + 跨层动态预算分配）
- 另与 Full KV（不驱逐）作完整对照

**预算设置：**
- LongBench：KV 缓存预算 128 / 256 / 512
- RULER：预算 256 / 512 / 1024，两种序列长度
- 基线局部窗口大小 = 32；Judge Q 软 token 数量 = 32，保证一致对比

## 4. 资源与算力

- 论文正文**未明确报告** GPU 型号、数量及具体训练时长。
- 仅说明训练数据规模（ShareGPT 子集 50,000 条样本），且训练代价极低——由于仅微调 embedding 层中软 token 对应的极少量参数，其余模型权重完全冻结。
- 从方法设计推断计算需求较低，但具体资源配置（如 A100/H100 数量、训练时间等）文中没有提供，这在复现时需注意。

## 5. 实验数量与充分性

论文实验较为丰富，主要包括：

- **LongBench 主实验**：2 个模型 × 3 种预算 × 16 个子任务，覆盖多任务多场景；
- **RULER 主实验**：2 个模型 × 2 种序列长度 × 3 种预算；
- **Needle-in-a-Haystack**：视觉热力图对比，文档长度 4,000～32,000，深度间隔 10%；
- **关键 KV 命中率（Critical KV Hit Rate）分析**：对比 Judge Q 与 SnapKV 在预算 128/256/512 下与实际解码 token 选择的 KV 对重叠率；
- **提示词调整鲁棒性实验**：将问题从末尾移到开头，测量各方法性能下降比例；
- **文本续写任务**（MATH-500、AIME24）：将 Judge Q 应用于 DeepSeek-R1-Distill-Llama-8B，按输出长度 25% 的预算做续写阶段 KV 驱逐；
- **数据质量消融**：共享（ShareGPT）vs. 模型自生成响应 vs. C4/Wikipedia/GitHub 数据；
- **软 token 数量消融**：验证 n=32 附近训练代价与泛化性能达到最佳平衡；
- **案例分析（Case Study）**：展示 NarrativeQA 上 Judge Q 与 SnapKV 的具体回答差异。

**评价**：
- 实验覆盖面较广，主实验+多项消融+案例共 8 类不同实验，在 AAAI 论文中属于相对充分。
- 对比方法选择主流且有代表性；预算、窗口大小等设置保持了一致性，公平性较好。
- 但也存在**局限**：① 仅测试了 8B/7B 规模模型，未覆盖更大参数或更多架构；② 中文任务、多语言能力没有专门验证；③ 未报告多次运行方差与统计显著性检验。

## 6. 论文的主要结论与发现

1. 现有 KV 缓存驱逐方法因依赖最后窗口作为查询来源，倾向于关注局部信息，在问题位置变化时性能明显退化；
2. 使用真实解码 token 指导的 KV 驱逐接近理论性能上界，而 Judge Q 训练出的软 token 可有效逼近该上界；
3. 在相同预算下，Judge Q 在 LongBench 上平均提升约 1 分（最高达 2.6 分），在 RULER 上持续领先 3 分以上（最高近 10 分），且预算越低提升越明显；
4. Judge Q 的关键 KV 命中率较最佳基线 SnapKV 高约 8 个百分点，说明其驱逐决策更接近"理论最优选择"；
5. 在问题前置的鲁棒性测试中，Judge Q 的性能损失低于基线（<7% vs. 约 10%）；
6. 在长输出续写任务（AIME24，输出 >10,000 tokens，仅保留 25% KV 缓存）中显著优于 SnapKV；
7. 使用模型自生成响应作为训练数据优于直接使用原始数据，且训练数据的内容多样性对方法效果影响显著。

## 7. 优点

- **轻量高效**：仅微调 embedding 层中软 token 部分参数，训练成本极低，易于适配任意开源模型；
- **直击要害**：从"实际解码 token 是最优驱逐依据"这一观察出发，将软 token 的注意力模式对齐到真实解码 token，目标清晰且合理；
- **方法论新颖**：将"可训练查询"思想引入 KV 驱逐领域，不同于传统基于启发式或局部窗口的方法；
- **通用性强**：框架与具体模型架构解耦，可作为即插即用模块增强现有驱逐方法（如与 SnapKV、PyramidKV 等结合）；
- **实验扎实**：多基准、多模型、多预算全面验证，并额外引入命中率指标、提示调整鲁棒性测试和长输出续写等维度；
- **开源可复现**：提供了代码仓库。

## 8. 不足与局限

- **算力信息缺失**：未报告 GPU 型号、数量、训练时长等关键资源数据，影响可复现性和成本评估；
- **模型规模有限**：仅验证了 7B/8B 级别模型，未在更大规模（如 70B）或不同架构（如 MoE）上验证；
- **训练数据覆盖面有限**：主要使用 ShareGPT 子集，虽补充了 C4/Wikipedia/GitHub 对比，但各领域数据比例和多样性仍有限；
- **驱逐后不更新**：当前方法仅在预填充阶段生效，解码过程不再动态调整 KV 缓存；作者也在结论中指出流式驱逐是未来工作；
- **无统计显著性分析**：论文未报告多次运行的方差结果，无法判断提升是否统计显著；
- **只针对预填充阶段的静态驱逐**：对于长生成场景（输出很长）的适用性还需要更多验证，虽然 AIME24 实验有一定补充；
- **应用范围**：方法面向通用 LLM 推理场景，未考虑多智能体（multi-agent）协作中的跨会话 KV 缓存复用、调度等更复杂的系统级优化；
- **理论上界依赖 Full KV 生成**：使用 Full KV 生成的响应来标定"上界"有一定合理性，但 Full KV 生成质量本身也存在偏差，可能不完全代表已标注答案的最优 KV 选择。

（完）
