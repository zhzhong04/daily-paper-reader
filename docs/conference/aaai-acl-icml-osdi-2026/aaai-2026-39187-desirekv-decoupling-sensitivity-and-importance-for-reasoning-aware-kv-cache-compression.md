---
title: "DesireKV: Decoupling Sensitivity and Importance for Reasoning-Aware KV Cache Compression"
title_zh: DesireKV：解耦敏感性与重要性的推理感知KV缓存压缩
authors: "Pengyu Cheng, Jiacheng Wang, Tianle Chen, Bei Liu, Xiaofeng Hou, Jiacheng Liu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39187/43148"
tags: ["query:agent-cache"]
score: 4.0
evidence: 面向推理的KV缓存压缩，适用于长推理轨迹的缓存驱逐，但非智能体特定
tldr: 链式推理产生的长序列会占用大量KV缓存，而推理文本具有重复逻辑和低信息密度的特点。DesireKV构建由注意力重要性和量化敏感性组成的二维坐标体系，对推理关键token施加专门保护，并作出差异化压缩决策。该方法能在压缩缓存的同时保留推理所需信息，但并未涉及智能体工作流中的缓存调度与跨智能体复用。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39187/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 861, \"height\": 327, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39187/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 422, \"height\": 336, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39187/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 418, \"height\": 337, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39187/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1835, \"height\": 921, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39187/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 826, \"height\": 854, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39187/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 820, \"height\": 224, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39187/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 705, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39187/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1837, \"height\": 869, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39187/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 876, \"height\": 254, \"label\": \"Table\"}]"
motivation: 推理序列特征使现有KV压缩方法次优，需要保护对推理至关重要的token。
method: 构造基于注意力和量化敏感性的二维坐标，推理关键token保护并差异化压缩。
result: 在压缩KV缓存的同时保持推理质量，优于现有通用压缩方法。
conclusion: 结合敏感性与重要性的推理感知压缩可更有效地处理长推理轨迹。
---

## Abstract
Large language models performing chain-of-thought (CoT) reasoning generate extensive intermediate sequences that consume substantial memory through key-value (KV) cache storage. Unlike conventional text generation, reasoning sequences exhibit unique characteristics, including repetitive logic patterns and low information density, making existing KV cache compression methods suboptimal. We propose DesireKV, a novel compression framework that first constructs a two-dimensional coordinate system based on attention-derived importance and outlier-based quantization sensitivity. It then applies a dedicated protection mechanism for tokens critical to the reasoning process itself. Our approach makes differentiated compression decisions: retaining important and sensitive tokens, quantizing important but insensitive tokens, and evicting unimportant tokens. Through comprehensive evaluation on reasoning benchmarks, we demonstrate that DesireKV achieves up to 2.93× throughput improvement while maintaining nearly 99% of original reasoning accuracy.

---

## 论文详细总结（自动生成）

# DesireKV：解耦敏感性与重要性的推理感知KV缓存压缩——论文深度解析

## 1. 核心问题与研究动机

- **背景瓶颈**：大语言模型在链式推理（Chain-of-Thought）任务中会生成极长的中间推理过程，例如 DeepSeek-R1 在数学竞赛题上可输出超过 32K tokens。在批处理大小为 8 时，KV 缓存可占约 32.8GB 显存，远超模型权重本身（约 15.5GB），形成严重内存瓶颈。
- **独特挑战**：论文指出推理序列与普通文本生成存在本质差异，导致现有 KV 缓存压缩方法失效，具体包括三个核心挑战：
  - **重要性动态演化**：早期看似不重要的 token 可能在后期成为逻辑推理的关键锚点，传统的基于当前注意力分数的驱逐策略会破坏长程逻辑依赖。
  - **量化敏感性异质**：数学表达式和逻辑算子对量化误差极度敏感，而解释性文本则高度鲁棒；统一量化策略要么浪费精度资源，要么损害关键内容。
  - **实时压缩决策**：推理时必须在线决定压缩策略，无法依赖离线全序列敏感性分析，而许多现有方法依赖离线分析。
- **核心洞察**：与假设 token 重要性与量化敏感性呈正相关或相关的直觉相反，作者通过实证发现，推理序列中 token 的**上下文重要性与量化敏感性高度解耦**（R²=0.018，近乎零相关）。这一发现为差异化压缩策略提供了理论前提。

## 2. 方法论：DesireKV 框架

### 核心思想

DesireKV 构建一个二维决策空间，基于**注意力派生的重要性**（Importance）与**基于异常值分析的量化敏感性**（Sensitivity）两个正交维度，将 token 划分为四个象限：

| 象限 | 特征 | 压缩策略 |
|------|------|----------|
| Q1 | 低重要性 + 低敏感性 | 驱逐 |
| Q2 | 高重要性 + 低敏感性 | 量化（较低精度） |
| Q3 | 高重要性 + 高敏感性 | 保留全精度 |
| Q4 | 低重要性 + 高敏感性 | 驱逐/降级与动态平衡 |

作者统计发现约 27.17% 的 token 落入 Q2 象限，即"重要但不过敏"的 token 是此前单准则方法从未开发过的压缩空间。

### 三阶段技术流程

**① 基于注意力的重要性评估（Attention-based Importance）**

- 采用与 RPC 类似的 selector window 机制：每生成 P 个 token 进行一次压缩操作，用最近 R 个 token 构成的窗口作为"选择器"，评估历史 P 个 token 对当前推理状态的重要性。
- 通过多注意力头聚合注意力分数，计算公式为：

  \[
  I_{i,l}^{raw} = \frac{1}{R \cdot H} \sum_{r=1}^{R} \sum_{h=1}^{H} \text{Attn}_h^{(l)}(q_{t-r+1}^{(h)}, k_i^{(l,h)})
  \]

- 随后施加滑动窗口平滑（window size = w），强化语义相邻 token 的连续聚合。

**② 基于异常值的敏感性测量（Outlier-based Sensitivity）**

- 核心思想：激活值中的极端异常值（outliers）通常落在量化鲁棒范围之外，对量化误差极敏感。
- 对每个 key 向量按块（block size = 64）划分，在每个块内执行 IQR（四分位距）异常值检测：

  \[
  x \in O_b \iff x < Q_1^{(b)} - 1.5 \cdot \text{IQR}_b \quad \text{或} \quad x > Q_3^{(b)} + 1.5 \cdot \text{IQR}_b
  \]

- 每块的敏感性分数为异常值与块均值的平均绝对偏差：

  \[
  \text{OutlierScore}_b = \frac{1}{|O_b|} \sum_{x \in O_b} |x - \mu_b|
  \]

- 最终逐层聚合、跨压缩窗口归一化，得到 token 级敏感性分数。

**③ 推理感知的 token 保护（Reasoning-Aware Protection）**

- 用生成置信度 \( p_i = \max_v \text{softmax}(o_i)[v] \) 作为推理转移点的代理信号：当上一个 token 的置信度骤降（低于阈值 λ），判定当前 token 可能标志着推理逻辑的转折，将其标记为"受保护 token"，保持全精度存储。
- 该机制弥补了纯注意力驱动的不足：实证表明，在保护 20% token 的场景下，注意力驱动的策略仅达到 42.9% pass@1，加入置信度感知的混合策略提升至 44.2%，逼近无压缩的 46.7%。

### 最终决策逻辑

在每次周期压缩时，DesireKV 对每个 token 执行**差异化三路决策**：

- **高重要性 + 高敏感性** → 保留全精度（BF16）；
- **高重要性 + 低敏感性** → 量化至低比特（如 4~8 bit）；
- **低重要性** → 直接驱逐（不考虑敏感性）。

## 3. 实验设计

### 模型与数据集

- **模型**：DeepSeek-R1-Distill-Qwen-7B、DeepSeek-R1-Distill-Llama-8B 两个开源推理模型。
- **数据集**（共 4 个推理基准）：
  - GSM8K（数学）
  - MATH（500 样本测试集）
  - AIME2024（竞赛数学）
  - GPQA-Diamond（研究生级科学推理）
- **设置**：temperature=0.6，最大生成长度 32,786 tokens；Pass@1 指标（GPQA 在 Qwen 模型上使用 Pass@2 以缓解整体性能下降）。

### 对比方法

- **量化类**：KIVI 两种配置（K8V4 保守 6-bit、K4V4 激进 4-bit）
- **驱逐类**：RPC（推理模型专用注意力驱逐）
- **混合类**：DDKS（驱逐+量化混合；由于无公开实现，作者基于 RPC 扩展自行实现）

### 关键结果

- **主表结果**：DesireKV 在 Qwen-7B 上平均损失仅 1.2%（平均位宽 3.0 bit），在 Llama-8B 上仅 1.0%（平均位宽 2.9 bit）；相比 RPC 在 AIME2024 上损失 21.5%（Qwen）/7.2%（Llama），DesireKV 仅损失 1.3%/0.9%，优势显著。
- **效率评估**（NVIDIA H20 GPU）：在 32K tokens 时，比 BF16 节省约 55% 内存，较 RPC 额外降低 11.6%；在 96GB 显存约束下吞吐量较 BF16 提升 193.1%（约 2.93×）。
- **消融实验**：分别移除重要性评估（-I）、敏感性测量（-S）、保护机制（-P），验证了三个组件各自的贡献；其中去除敏感性量化导致性能下降最明显，验证了敏感性感知是核心。

### 额外动机实验

- **保护采样验证**（表1）：outlier 感知保护（44.6%）远优于随机保护（37.9%），逼近无压缩（46.7%）。
- **推理感知验证**（表2）：注意力+置信度混合保护（44.2%）优于纯注意力（42.9%）。

## 4. 资源与算力

- 论文仅提及在 **NVIDIA H20 GPU** 上完成吞吐与内存效率评估实验，未明确说明 GPU 数量与具体训练/推理耗时数据。
- 所有方法均基于开源模型进行推理评估（无需训练），但作者**未披露**每次实验的墙钟时间、不同方法的具体运行开销或多次运行的方差统计。

## 5. 实验数量与充分性

### 实验规模

- 2 个模型 × 4 个数据集的主实验；
- 3 组消融变体（-I / -S / -P）；
- 2 组动机验证实验（outlier 保护、推理感知保护）；
- 2 组效率测量（显存占用、吞吐）。

### 充分性评价

- **优点**：覆盖了主流推理基准、两大开源推理模型、三种代表性压缩范式（量化/驱逐/混合）的对比；消融设计干净、归因清晰。
- **不足**：
  - **无重复运行统计**：未见标准误差或多次运行均值，对 pass@1 这类高方差指标来说，缺乏可靠性佐证；
  - **GPQA 设置不一致**：Qwen 模型上采用 Pass@2 而非 Pass@1，可能掩盖该模型上的真实降级程度；
  - **潜在不公平对比**：DDKS 无官方实现，由作者自行扩展 RPC 完成，可能未达其最佳性能；P/R 等参数据称对齐，但没有给出具体数值；
  - **未覆盖极端长上下文**：最大 32K tokens 验证，尚未触及 64K-128K 推理长度段，而论文动机恰恰涉及这类极端场景；
  - **仅两个 7-8B 规模模型**：未验证更大规模（如 32B/70B）上的普适性。

## 6. 主要结论与发现

1. **重要性-敏感性解耦是真实存在的**：推理序列中上下文重要性与量化敏感性几乎正交（R²≈0.018），且 Q2 类型（重要但不过敏）token 占比可观（27.17%），构成此前未开发的压缩空间。
2. **异常值是量化敏感性的有效指标**：IQR 异常值得分与实际量化重建误差呈正相关，可在线计算、无需离线分析。
3. **推理感知保护是必要的**：生成置信度的骤降可有效识别推理转折点，弥补纯注意力评分对关键 token 的遗漏。
4. **差异化三路策略优于单准则方法**：在约 3 bit 平均位宽下，DesireKV 达到约 5.5× 压缩比、约 55% 显存节省、2.93× 吞吐提升，同时保持近 99% 的原始推理准确率（0.3%-1.7% 损失）。

## 7. 方法亮点

- **新颖的核心洞察**：首次系统性地提出并实证验证推理序列中"重要性-敏感性"解耦现象，为 KV 缓存压缩奠定新视角；
- **在线适用性**：所有评估（注意力选择窗口、IQR 异常值分析、置信度阈值）均可在推理过程中实时完成，不依赖未来信息或离线分析；
- **混合策略而非单一策略**：驱逐、量化、全精度三类操作的有机结合，比"非驱逐即量化"的对立框架更具灵活性；
- **计算开销低**：分块 IQR 统计避免全向量计算，周期式压缩机制（每 P tokens）摊薄在线分析开销，实测吞吐表现优于更重的量化方法；
- **可解释性强的分类框架**：二维四象限的决策逻辑清晰直观，使压缩行为可理解和可调试。

## 8. 不足与局限

- **硬件配置披露不完整**：未给出 H20 的数量、单卡还是多卡、以及具体运行的时间开销，复现性受限；
- **实验覆盖面有限**：仅在 7B/8B 规模验证，未测试更大模型；长上下文仅到 32K，而动机指向 128K 级别；未评测代码、多跳 QA 等其他推理类型；
- **GPQA 的实验设置存在偏差风险**：对 Qwen 模型改用 Pass@2，使对比口径不一致；
- **基线公平性问题**：DDKS 为自行实现，缺少权威版本校准；RPC/KIVI 的超参数对齐描述模糊，存在潜在的调优偏差风险；
- **保护机制依赖单一信号**：仅用生成置信度作为推理转移的代理，对置信度校准较差的模型可能失效；
- **阈值选取依赖网格搜索**：λ、P、R、位宽分配等依赖人工网格搜索确定，缺乏自适应策略，跨场景迁移可能需要重新调参；
- **未提供源代码**：目前未见开放实现，影响可复现与工程落地。

---

（完）
