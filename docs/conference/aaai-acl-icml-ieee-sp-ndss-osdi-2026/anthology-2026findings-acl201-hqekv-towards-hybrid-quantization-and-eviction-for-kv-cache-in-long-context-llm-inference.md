---
title: "HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference"
title_zh: HqeKV：面向长上下文LLM推理的KV缓存混合量化与驱逐
authors: "He Wang, Yu Gu (谷峪), Fangfang Li, Zhigang Wang, Zhenghao Liu (刘正皓), Ning Wang, Xiaohua Li, Ge Yu (于戈)"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.201.pdf"
tags: ["query:agent-cache"]
score: 6.0
evidence: 提出KV缓存混合量化与驱逐策略，可迁移至多智能体缓存驱逐场景
tldr: 长上下文LLM推理中KV缓存带来严重显存开销，现有压缩方法仅单独使用量化或驱逐，且重要性估计不准确。HqeKV提出混合压缩框架，将量化和驱逐结合，根据缓存数据的重要性进行细粒度自适应压缩。实验表明该方法在保持推理质量的同时显著降低显存占用。虽然面向单模型推理，其驱逐策略可迁移至多智能体协作共享缓存场景。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl201/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 743, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl201/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1536, \"height\": 591, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl201/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 792, \"height\": 466, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl201/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 792, \"height\": 468, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl201/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 742, \"height\": 369, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl201/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 804, \"height\": 191, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl201/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1576, \"height\": 414, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 802, \"height\": 167, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 802, \"height\": 217, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 624, \"height\": 200, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 726, \"height\": 345, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1655, \"height\": 1018, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 807, \"height\": 567, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 803, \"height\": 171, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 806, \"height\": 539, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 803, \"height\": 201, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1439, \"height\": 1699, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1614, \"height\": 456, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1380, \"height\": 1184, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl201/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1576, \"height\": 414, \"label\": \"Table\"}]"
motivation: 长上下文LLM推理中KV缓存显存开销大，现有量化或驱逐方法效果不佳。
method: 提出HqeKV混合压缩框架，将量化与驱逐结合，按缓存重要性自适应选择压缩粒度。
result: 在长上下文推理任务上显著降低显存占用并保持生成质量。
conclusion: 混合压缩是更优的KV缓存管理方式，并可启发多智能体缓存驱逐策略。
---

## Abstract
The autoregressive inference in large language models requires repeated computation across transformer layers. While caching intermediate key-value (KV) pairs eliminates redundancy, it introduces severe memory overhead, particularly in long-context settings. Most existing cache compression methods operate solely on either quantization or eviction, based on importance estimation of cached data. However, they are limited by coarse compression choices and inaccurate importance assessment, leading to suboptimal inference quality. To address this, we propose HqeKV, a hybrid compression framework built on both quantization and eviction, offering finer-grained compression options that adapt smoothly to the varying importance of cached KV pairs. An integrated optimizer automatically selects the best compression action for each cached element, maximizing quality while insulating end-users from tedious low-level tuning details. We further design a joint K–V importance metric to provide more accurate importance assessment results so that the optimizer can make smarter decisions. Additionally, HqeKV supports flexible conversion policies across multiple quantization precision levels, to further reduce quality degradation. Extensive experiments show that HqeKV improves output quality under the same memory constraints, outperforming state-of-the-art alternatives. Code is available at https://github.com/skywclouds/HqeKV.

---

## 论文详细总结（自动生成）

## HqeKV：面向长上下文 LLM 推理的 KV 缓存混合量化与驱逐框架——论文深度解读

### 1. 核心问题与研究动机

- **背景**：大语言模型（LLM）的自回归推理需要在各 Transformer 层中对已处理的 token 反复计算，产生大量冗余计算；KV Cache（键-值缓存）虽可消除该冗余，却带来严重的内存瓶颈。
- **问题**：在长上下文场景（如 128k token）下，KV Cache 的显存占用随序列长度线性增长，甚至可超过模型本身的权重内存，成为制约推理效率和批次大小的核心瓶颈。
- **现有方法局限**：
  - **纯量化方法**：精度选择粗糙，通常只用单一低精度（如 FP16→2bit），最多支持两种混合精度，无法匹配不同缓存条目间差异化的信息密度，量化粒度与转换策略缺乏自适应性。
  - **纯驱逐方法**：直接丢弃“重要性低”的 KV 对，虽避免反量化开销、推理更快，但常带来明显的质量下降。
  - **现有重要性度量不准确**：多数方法只依赖累积注意力权重（仅考虑 K 向量），忽略 V 向量信息；某些方法考虑 V 的方式缺乏理论支撑（如只取 V 的 1-范数），导致压缩决策欠优。
  - **已有量化+驱逐集成工作**（如 EVICPRESS、MiniKV）多为工程层面的拼接，压缩粒度粗，缺乏算法层面的深度协同优化。
- **核心主张**：通过将量化与驱逐融合、扩展精度选择粒度、设计更准确的 K-V 联合重要性度量，以及自动优化各精度分配比例，能在相同内存约束下显著提升推理质量。

### 2. 方法论：核心思想与技术细节

#### 2.1 总体框架（图 1）

HqeKV 在 prefill 阶段和 decoding 阶段均进行缓存压缩，核心结构如下：

- **五个压缩档位**：FP16（全精度）、4-bit、2-bit、1-bit 量化、驱逐（eviction）。缓存 KV 对按重要性升序排列，分别落入不同档位：
  - 最重要 → 高精度甚至不压缩（FP16/4-bit）
  - 中等重要 → 2-bit/1-bit
  - 最不重要 → 驱逐
- **压缩流程**：prefill 阶段生成 Q、K、V 后，用联合 K-V 重要性度量引导将 K、V 分配到五个精度档位；decoding 阶段每生成 T 个 token 触发一次周期性重量化。
- **离线优化器**：用 Tree-structured Parzen Estimator（TPE）搜索最优精度比例分配，使用户只需输入目标平均比特数，无需手动调节。
- **统一的内存约束表达**（公式 3）：

```
4δ₁ + 2δ₂ + δ₃ = B_avg        （平均比特数约束）
δ₁ + δ₂ + δ₃ + δ₄ = 1          （比例总和为 1）
```

其中 δ₁、δ₂、δ₃、δ₄ 分别对应 4-bit、2-bit、1-bit 和驱逐的比例。以 δ₃、δ₄ 为自由变量，用 TPE 搜索最优解。

#### 2.2 联合 K-V 重要性度量（核心创新 1）

- **理论依据**：作者从量化误差的期望表达式（公式 2）出发，推导出量化误差主要由数据的极值（range）决定。量化中每个值被映射到最近的量化中心，期望转换损失可以表示为各量化区间内数据到中心距离的加权平方和。
- **经验验证**：
  - 数值积分模拟显示转换损失与数据的 max/min 范围正相关；
  - 从真实 KV Cache 中抽取 token 做实验，发现 range 与转换损失的 Pearson 相关系数在 4/2/1-bit 和驱逐下均高于 0.91，显著高于随机向量上的相关系数。
- **新度量设计**：
  - K 的重要性：累积注意力权重（沿用此前工作）。
  - V 的重要性：累积注意力权重 × 该 token 的 V 向量范围（range）。
  - 理由：注意力公式中 O = Softmax(QK^⊤/√d)·V，V 对输出贡献被注意力权重加权，故联合两者更合理。
- **分块处理**：由于 K 和 V 的量化维度不同，KV Cache 被划分为大小为 G 的 chunk，以 chunk 内 token 的平均重要性作为该块的代表重要性。

#### 2.3 精度专属量化策略（核心创新 2）

- **发现**：不同量化策略在不同比特宽度下表现差异明显：
  - 4-bit：uniform（均匀）量化优于 normalized（归一化）量化；
  - 2-bit：两者接近，uniform 略优；
  - 1-bit：normalized 量化远优于 uniform（表 2/3）。
- **策略选择**：4-bit 和 2-bit 采用 uniform 量化，1-bit 采用 normalized 量化。
- **量化维度**：K 采用 per-channel 量化，V 采用 per-token 量化，分组大小 G=32。
- **概率分布依据**：此前 NQKV 工作已确认 KV Cache 数据近似正态分布，这解释了 normalized 量化在低位宽优势的来源——它按照标准正态分布的分位数放置量化中心，更匹配低位宽下的数据分布形态。

#### 2.4 解码阶段的策略

- **周期性重量化**：每生成 T=32 个 token 后，对所有 KV Cache 重新执行压缩。
- **精度跃迁冗余性分析**：统计显示，从低精度跃迁到更高精度的 token 比例极小（K Cache 约 3.33%，V Cache 约 3.39%），因此重量化时可只保留不高于当前精度的转换，跳过低→高转换，大幅降低计算开销。

#### 2.5 优化器细节

- 使用 TPE 进行 200 次迭代搜索；
- 损失函数：`L = L_c + L_reg`，其中 L_c 为模型在标定数据（wikitext-2 拼接的 16k token 序列）上量化输出与全精度输出的交叉熵；L_reg = αx₃ + βx₄ 为正则项，用于抑制过低精度（1-bit、驱逐）的比例；
- 标定数据与评测数据（LongBench）不重叠；
- 保留最不重要的 2 个 chunk 固定为全精度，以降低量化损失。

### 3. 实验设计

#### 3.1 评测基准与数据集

- **LongBench**：21 个数据集、6 大任务类别（单文档 QA、多文档 QA、摘要、few-shot、合成任务、代码补全），中英双语，长上下文理解标准基准；
- **AIME-2025**：30 道 2025 年美国数学邀请赛题目，考验多步逻辑推理。

#### 3.2 模型

- Llama-3.1-8B-Instruct（上下文长度 128k）
- Qwen3-8B（上下文长度 128k）

#### 3.3 对比方法

- 单精度量化：KIVI-2、OTT-2
- 混合精度量化：ZipCache-3.2、KVTuner-3.25
- 驱逐方法：CAKE-3.2 / CAKE-3.25
- 全精度 FP16 基线

#### 3.4 压缩配置

| 方法 | 平均比特数 |
|---|---|
| HqeKV-2 / KIVI-2 / OTT-2 | 2 bit |
| HqeKV-2.8 vs ZipCache-2.8 | 2.8 bit |
| HqeKV-3.2 vs ZipCache-3.2 / CAKE-3.2 | 3.2 bit |
| HqeKV-3.25 vs KVTuner-3.25 / CAKE-3.25 | 3.25 bit |

#### 3.5 评测维度

1. **推理质量**：LongBench 各任务分数 & AIME-2025 准确率；
2. **推理可扩展性**：最大可支持批量大小（不同上下文长度）、显存占用（不同批量大小）；
3. **延迟**：TTFT（首 token 时间）、TPOT（每 token 时间）；
4. **周期重量化开销**：三次重量化的实际耗时；
5. **综合性能**：雷达图（准确率、灵活性、用户友好度、吞吐量、内存效率五维对比）。

### 4. 资源与算力

- **硬件**：单块 NVIDIA RTX A6000 GPU（48GB 显存）；
- **算力说明**：
  - 论文仅说明实验在该 GPU 上进行，未披露具体训练/评测总时长；
  - 离线精度比例搜索（3.2-bit 配置）耗时 **7 分 46 秒**，作者认为这一一次性成本可接受；
  - 周期重量化时间实测为 0.52s / 0.36s / 0.33s（三个周期），确认该开销可忽略。

### 5. 实验数量与充分性分析

#### 5.1 实验规模

论文的实验量较为充分，主要包括：

| 实验类别 | 数量/覆盖面 |
|---|---|
| LongBench 主评测 | 2 个模型 × 21 个数据集 × 多种压缩配置 |
| AIME-2025 评测 | Qwen3-8B，HqeKV-2 vs KIVI-2 |
| 可扩展性实验 | 最大 batch size（8 种上下文长度）、显存占用（多 batch）、TTFT、TPOT（2 种上下文） |
| 消融实验 | 8 组系统消融 + range-only 消融 + 超参数 α/β 扫描 + 搜索迭代数对比 |
| KVTuner 补充对比 | 在 Qwen3-8B 上随机配置的补充实验 |

#### 5.2 充分性与公平性

- **优点**：
  - 消融覆盖全面：逐项去除四项创新（重要性度量、精度专属量化策略、优化器、驱逐）均导致性能下降，且对每项创新做了独立验证；
  - 对 ZipCache 和 KVTuner 的 OOM / CUDA ERROR 问题做了标注（*符号），并用非失败列计算平均值，处理诚实透明；
  - 补充了与 KVTuner 在 Qwen3-8B 上的对比（因 KVTuner 未开源 Qwen3 配置，采用随机配置，但结果仍显示 HqeKV 更优）。
- **潜在不足**：
  - 仅评测 8B 规模模型，未覆盖更大规模（如 70B）或 MoE 架构；
  - 对比方法的超参数可能未逐一针对各数据集优化，存在一定的基线偏差风险；
  - 雷达图中的“用户友好度”“灵活性”等维度属于定性判断，主观性较强。

### 6. 主要结论与发现

1. **混合压缩优于单一压缩**：在相同内存约束下，HqeKV 同时使用量化和驱逐，在所有压缩配置上全面超越纯量化（KIVI、OTT、ZipCache、KVTuner）和纯驱逐（CAKE）方法。
2. **量化误差与数据范围正相关**：通过理论推导（公式 2）和实证（PCC ≥ 0.91）确立了 range 作为转换损失指标的有效性，由此设计联合 K-V 重要性度量比仅用注意力权重更准确。
3. **不同比特宽度适合不同量化策略**：4/2-bit 用 uniform、1-bit 用 normalized，比统一使用一种策略可显著降低转换损失。
4. **TPE 离线搜索可高效求解最优精度分配**：200 次迭代即可收敛，耗时约 8 分钟。
5. **具体性能提升**：HqeKV-3.2 在 LongBench 上从 CAKE-3.2 的 40.30 分提升至 49.91 分，提升约 23.8%；在 AIME-2025 上 HqeKV-2 准确率（0.20）优于 KIVI-2（0.17）。
6. **内存效率与扩展性**：HqeKV 在多数上下文长度下支持最大 batch size，平均显存占用比 OTT 降低 29.6%、比 ZipCache 降低 8.3%、比 KVTuner 降低 8.6%。

### 7. 方法亮点

- **五档细粒度压缩**：从 FP16 到驱逐的五个压缩档位，突破此前最多两种精度的限制，能更平滑地适配缓存重要性的连续变化。
- **理论驱动的度量设计**：不依赖经验直觉，而是从量化误差的数学期望出发推导出 range 指标，并用 Pearson 相关系数及真实数据验证，为 V 向量重要性提供了理论依据。
- **精度-策略联合优化**：首次系统分析不同量化策略在各比特宽度下的表现差异，并在不同精度上采用定制策略。
- **用户友好的自动化**：内置 TPE 优化器自动搜索精度比例，免去用户手动调参。
- **工程实现高效**：自定义 Triton/CUDA kernel 将反量化与矩阵乘法融合，并对量化值做密集比特打包，减少存储开销。
- **周期性重量化的降本设计**：利用“低→高精度跃迁比例极小”的统计观察，跳过该转换，降低了重量化成本。

### 8. 不足与局限性

- **优化器无法个性化**：离线搜索的精度分配比例与用户群体或任务类型无关，无法针对特定场景做个性化优化。
- **1-bit 精度损失仍显著**：虽然 normalized 量化缓解了 1-bit 下的精度损失，但极端压缩档位仍会带来可感知的质量下降。
- **重量化间隔敏感**：解码阶段的固定重量化间隔 T 是经验设定，可能在不同上下文长度或模型上引入延迟和质量波动。
- **多模态扩展未验证**：HqeKV 在纯文本 LLM 上验证，其行为在多模态架构（如视觉-语言模型）中需进一步研究。
- **实验覆盖有限**：仅评测 8B 级别模型，未覆盖更大规模模型；硬件仅限单块 A6000，未在多卡分布式推理场景下验证。
- **TTFT 略有劣势**：相比 KIVI 和 KVTuner，HqeKV 的 TTFT 有秒级差距（最多约 2 秒），虽在可接受范围内，但对于对延迟极为敏感的服务场景可能有影响。
- **公平性风险**：对 KVTuner 在 Qwen3-8B 上的对比使用随机配置而非其官方最优配置，可能被质疑对比的公平性（虽然结果是 HqeKV 更优，但实验设计仍需注意）。

---

（完）
