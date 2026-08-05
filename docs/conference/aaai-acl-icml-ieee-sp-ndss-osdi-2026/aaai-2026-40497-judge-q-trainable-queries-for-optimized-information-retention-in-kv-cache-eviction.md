---
title: "Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction"
title_zh: Judge Q：面向KV缓存驱逐信息保留优化的可训练查询
authors: "Yijun Liu, Yixuan Wang, Yuzhuang Xu, Shiyu Ji, Yang Xu, Qingfu Zhu, Wanxiang Che"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40497/44458"
tags: ["query:awc"]
score: 7.0
evidence: 可训练查询的KV缓存驱逐方法，可直接迁移到基于LLM的代理系统缓存驱逐策略
tldr: 大语言模型的KV缓存随序列增长不断膨胀，现有驱逐策略多依赖局部窗口，易丢失全局关键信息。Judge Q 提出可训练的软令牌查询，仅微调嵌入层即可学习更准确的KV重要性评分，从而在驱逐时保留重要信息。实验证明该方法能提升内存效率和解码性能。其训练式驱逐思路可直接迁移到基于LLM的代理系统中，优化多智能体场景下的缓存驱逐策略。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 现有KV缓存驱逐仅关注局部窗口，忽略全局信息，导致关键信息被错误淘汰。
method: Judge Q 通过引入可训练的软令牌列表，仅调整嵌入层来学习KV重要性评分，实现信息保留优化。
result: 实验显示该方法提高了缓存驱逐的信息保留能力，降低了内存占用并提升解码效率。
conclusion: Judge Q 为LLM缓存驱逐提供了一种训练式改进方案，可扩展到代理系统的缓存管理。
---

## Abstract
Large language models (LLMs) utilize key-value (KV) cache to store historical information during sequence processing. The size of KV cache grows linearly as the length of the sequence extends, which seriously affects memory usage and decoding efficiency. Current methods for KV cache eviction typically utilize the last window from the pre-filling phase as queries to compute the KV importance scores for eviction. Although this scheme is simple to implement, it tends to overly focus on local information, potentially leading to the neglect or omission of crucial global information. To mitigate this issue, we propose **Judge Q**, a novel training method which incorporates a soft token list. This method only tunes the model’s embedding layer at a low training cost. By concatenating the soft token list at the end of the input sequence, we train these tokens' attention map to the original input sequence to align with that of the actual decoded tokens. In this way, the queries corresponding to the soft tokens can effectively capture global information and better evaluate the importance of the keys and values within the KV cache, thus maintaining decoding quality when KV cache is evicted. Under the same eviction budget, our method exhibits less performance degradation compared to existing eviction approaches. We validate our approach through experiments conducted on models such as Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3, using benchmarks including LongBench, RULER, and Needle-in-a-Haystack. Results indicate an improvement of approximately 1 point on the LongBench and over 3 points on RULER. This proposed methodology can be seamlessly integrated into existing open-source models with minimal training overhead, thereby enhancing performance in KV cache eviction scenarios.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：大语言模型（LLM）在长序列场景中依赖 KV cache 存历史信息，但 KV cache 随序列长度线性增长，带来严重的内存占用和推理效率瓶颈。
- **现有方法的缺陷**：当前主流 KV cache 驱逐方法（如 H2O、SnapKV、PyramidKV 等）通常在预填充阶段直接选取输入末尾的局部窗口作为查询，来计算各键值对的重要性分数并驱逐低分项。这种策略简单，但过度关注局部信息，容易忽略全局关键内容；尤其当问题不在输入末尾时，性能会显著下降。
- **关键观察**：
  - 若直接用**实际解码 token** 的查询来选择保留的键值对，可获得接近理论上限的生成质量；
  - 但解码 token 在预填充阶段不可得。
- **核心问题**：能否在预填充阶段使用一种可训练的查询替代真实解码 token，从而更准确地识别对后续生成至关重要的键值对，提升 KV cache 驱逐的信息保留率？

## 2. 方法论

**核心思想**：引入一组可训练的“软令牌”（soft tokens），通过最小化其注意力图与真实解码 token 注意力图之间的差异，训练软令牌“模仿”解码 token 的查询行为，从而在预填充阶段用软令牌的注意力分数作为 KV 重要性评分。

**关键技术细节**：

- **软令牌定义**：在模型词汇表中追加 n 个可训练 token（实验中取 n=32），仅训练这些 token 对应的嵌入向量，模型其余参数全部冻结，训练成本极低。
- **训练数据构造**：使用 ShareGPT 数据集中 50,000 个样本，每个样本含 prompt 和 response 两部分。
- **训练目标**：
  - 构造两个输入序列：
    - `Input_soft = Concat(Prompt, Soft)`
    - `Input_resp = Concat(Prompt, Resp)`
  - 分别计算软令牌和响应 token 对 prompt 的注意力分数，并对 token 维度进行平均，得到注意力图 \(A_{soft}\) 和 \(A_{resp}\)。
  - 最小化二者之间的均方误差（MSE）：\(L = \| A_{soft} - A_{resp} \|_2^2\)。
- **推理阶段流程**：
  1. 将训练好的软令牌拼接到输入序列末尾；
  2. 在预填充阶段计算软令牌对输入序列的注意力图；
  3. 根据注意力分数保留 top-k 键值对，驱逐其余部分；
  4. 删除软令牌，仅使用修剪后的 KV cache 继续解码。

## 3. 实验设计

- **基准模型**：
  - Llama-3.1-8B-Instruct
  - Mistral-7B-Instruct-v0.3
  - 额外用于扩展实验的模型：Llama-3.2-1B-Instruct（数据质量探索）、DeepSeek-R1-Distill-Llama-8B（文本续写任务）。
- **Benchmarks**：
  - **LongBench**（多任务长上下文理解，含单文档 QA、多文档 QA、摘要、少样本、合成、代码等子任务）
  - **RULER**（长上下文真实能力评估，序列长度 8192 和 32768）
  - **Needle-in-a-Haystack**（长文本检索压力测试）
  - 额外任务：MATH-500 和 AIME24（用于文本续写型 KV cache 驱逐评估）
- **对比方法**：
  - StreamingLLM（固定保留初始 token 和局部窗口）
  - H2O（累积注意力分数）
  - SnapKV（局部窗口注意力 + 池化）
  - PyramidKV（分层预算分配的 SnapKV 变体）
  - 还对比了全量 KV cache（Full KV）和基于真实解码 token 的“理论上限”。
- **实验设置**：
  - KV cache 预算：128、256、512（LongBench）；256、512、1024（RULER）
  - 局部窗口大小统一为 32，软令牌数量同样设为 32，保证公平对比。

## 4. 资源与算力

- **论文未明确说明**训练所使用的 GPU 型号、数量、训练时长等具体算力信息。
- 仅提及训练数据为 ShareGPT 子集 50,000 条样本，训练目标是冻结模型全部参数、仅微调嵌入层中软令牌对应的少量参数，因此计算开销较低，但**没有给出实际的浮点运算量、GPU 小时数等量化数据**。

## 5. 实验数量与充分性

- **实验组数较多**：
  - LongBench 上覆盖 16 个子任务、4 种方法对比、3 种预算，共数百个指标；
  - RULER 上覆盖 2 种模型、2 种序列长度、3 种预算；
  - Needle-in-a-Haystack 实验；
  - 额外做了“问题位置调整”的鲁棒性实验；
  - 关键键值命中率实验（与 SnapKV 对比）；
  - 文本续写任务（MATH-500、AIME24）；
  - 数据质量消融（ShareGPT vs. 模型生成 vs. C4/Wikipedia/GitHub）；
  - 软令牌数量消融（验证 n=32 的合理性）；
  - 案例分析（NarrativeQA 实例）。
- **充分性评价**：
  - **优点**：实验覆盖多个主流 benchmark 和多种模型，预算设置统一，且与所有基线在相同局部窗口和配置下对比，公平性较好；消融实验覆盖了训练数据质量和软令牌数量两个关键变量。
  - **不足**：
    - 算力信息缺失，难以评估资源成本；
    - 训练数据仅 5 万条，且主要来自 ShareGPT，未验证更广泛数据来源的泛化性；
    - 未在更大规模模型（如 70B 级）上验证；
    - 未提供推理额外开销（软令牌引入的前向计算时间）的量化分析。

## 6. 主要结论与发现

- Judge Q 在相同驱逐预算下，相比已有预填充阶段驱逐方法，LongBench 平均分提升约 1 分（最高达 2.6 分），RULER 提升超过 3 分（最高接近 10 分），Needle-in-a-Haystack 上显著优于所有基线。
- 低预算时提升更明显，说明训练式查询在资源受限场景下更有优势。
- 软令牌能有效提高“关键键值命中率”——与基于真实解码 token 的选择重叠率比 SnapKV 高约 8 个百分点，更接近理论上限。
- 在问题位置移动到输入开头时，Judge Q 的性能损失（<7%）小于基线（约 10%），证明其对全局信息的利用更充分。
- 训练数据质量对结果影响大：使用模型生成响应优于原始数据集响应；ShareGPT 数据优于 C4、Wikipedia、GitHub 等预训练语料的组合。
- 软令牌数量设为 32 时，在训练成本与泛化性能平衡上最优。

## 7. 优点

- **轻量训练**：仅微调嵌入层中极少量参数，可无缝集成到现有开源模型，训练成本低。
- **方法新颖**：将可训练软令牌作为“查询代理”来对齐真实解码 token 的注意力分布，巧妙地绕过了解码 token 不可预知的问题。
- **公平评估**：统一了局部窗口大小、池化方式等设置，实验基准可靠；同时引入“关键键值命中率”这一指标，直接度量与理论上限的差距。
- **全面实验**：覆盖多任务、多模型、多预算，并包含鲁棒性分析、数据质量消融、软令牌数量消融和案例分析，验证充分。
- **实际意义**：在低内存预算下显著优于既有方法，对内存受限的推理部署具有实际价值。

## 8. 不足与局限

- **算力信息缺失**：未报告 GPU 型号、数量、训练时间等，读者难以评估复现成本。
- **训练数据局限**：仅使用 ShareGPT 子集，数据域覆盖有限；虽然验证了数据内容的影响，但未说明训练数据规模对最终性能的敏感程度。
- **模型规模覆盖窄**：实验仅涉及 7B/8B 级模型，未验证在更大或更小模型上的有效性。
- **推理开销未量化**：软令牌拼接会增加预填充阶段的注意力计算量，论文未给出额外时延或内存开销的具体数据。
- **理论基础较弱**：软令牌对齐真实解码 token 的注意力图是一种启发式训练目标，缺少理论解释为何该目标能保证最优驱逐。
- **应用限制**：方法针对预填充阶段的静态驱逐设计，未扩展至流式动态驱逐场景（论文提到这是未来工作）。

（完）
