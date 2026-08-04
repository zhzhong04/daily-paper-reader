---
title: "RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction"
title_zh: RetentiveKV：面向不确定性感知的多模态KV缓存驱逐的状态空间记忆
authors: "Sihao Liu, YuFan Xiong, Zhonghua Jiang, Zhaode Wang, Chengfei Lv, Shengyu Zhang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.934.pdf"
tags: ["query:agent-cache"]
score: 6.0
evidence: 面向不确定性感知的多模态KV驱逐方法，处理令牌的延迟重要性问题
tldr: 针对多模态大语言模型中视觉token存在延迟重要性而导致被过早驱逐的问题，RetentiveKV提出熵驱动的KV缓存优化方法，避免离散剪枝破坏空间连续性。该方法在长视觉上下文中有效降低内存消耗并保持模型性能，为多模态场景下的缓存驱逐提供了新思路。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl934/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1613, \"height\": 516, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl934/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 792, \"height\": 461, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl934/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1648, \"height\": 946, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl934/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1635, \"height\": 515, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl934/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1563, \"height\": 1138, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl934/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 822, \"height\": 383, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl934/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 745, \"height\": 302, \"label\": \"Table\"}]"
motivation: 视觉token具有延迟重要性以及离散剪枝破坏空间连续性问题，现有持久性假设在多模态下不适用。
method: 采用熵驱动的KV缓存优化，保留可能后期关键的视觉token并维护空间连续性。
result: 在长视觉上下文任务上降低内存与计算开销，同时保持了多模态大模型的生成质量。
conclusion: 提出了一种针对多模态KV缓存不确定性的驱逐方法，可迁移至其他延迟重要性场景。
---

## Abstract
Multimodal Large Language Models face severe challenges in computational efficiency and memory consumption due to the substantial expansion of the visual KV cache when processing long visual contexts. Existing KV cache compression methods typically rely on the "persistence of importance" hypothesis to prune tokens. However, this approach proves fragile in multimodal settings due to two key issues: 1) Visual tokens display "deferred importance," initially exhibiting low salience but becoming pivotal during later decoding, which can lead to premature eviction. 2) Discrete pruning disrupts the inherent spatial continuity of visual cues. To address these challenges, we propose RetentiveKV, an entropy-driven KV cache optimization method that reformulates KV eviction from "discrete context truncation" to "continuous memory evolution" based on State Space Models. Our method leverages information entropy to quantify the information potential of low-attention tokens and integrates tokens scheduled for eviction into a continuous state space through entropy-guided state transitions, enabling their dynamic reactivation when semantic relevance arises during subsequent decoding. Extensive experiments on multimodal benchmarks demonstrate that RetentiveKV achieves 5.0 × KV cache compression and 1.5 × decoding acceleration.

---

## 论文详细总结（自动生成）

# RetentiveKV：面向不确定性感知的多模态KV缓存驱逐的状态空间记忆

## 1. 论文的核心问题与整体含义（研究动机和背景）

多模态大语言模型（MLLMs）在处理长视觉上下文和高分辨率输入时，视觉 token 数量激增，导致 KV cache 大幅扩张，带来严峻的计算效率和内存消耗问题。现有的 KV cache 压缩方法大多依赖 **"重要性持久性"（persistence of importance）假设**——即认为初始注意力得分高的 token 在后续解码中依然关键，并据此进行剪枝。然而，论文指出这一假设在多模态场景下存在两个关键缺陷：

- **延迟重要性（Deferred Importance）现象**：视觉 token 在早期解码阶段往往表现出低注意力显著性，但在后续生成关键视觉相关回答时才被激活。基于初始重要性的剪枝会提前驱逐这些"潜在关键"token，造成不可逆的信息丢失。
- **视觉连续性坍塌（Visual Continuity Collapse）**：视觉 token 具有内在的空间连续性和跨 patch 相关性，而离散的 KV 驱逐操作会割裂这种连续表征，破坏视觉信息的空间拓扑结构。

针对上述问题，论文提出 **RetentiveKV**——一种基于状态空间模型（State Space Models, SSM）的熵驱动 KV 缓存优化方法，将 KV 驱逐从"离散上下文截断"重构为"连续记忆演化"，旨在保留低注意力 token 中蕴含的潜在多模态信息，同时维持视觉表征的空间连续性。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 2.1 核心思想

RetentiveKV 的核心思想是：**不彻底丢弃低注意力 token，而是将其压缩吸收进一个连续状态空间中**，该状态空间能随着解码过程动态演化，并在后续语义相关时被重新激活和检索。同时，通过状态更新的递归结构天然保持视觉 token 的空间连续性。

### 2.2 关键技术组件

论文提出的框架由三个核心组件构成：

**（1）熵引导的 KV 保持估计器（Entropy-Guided KV Retention Estimator）**

- 定义了**跨模态注意力熵**：计算文本 token 对视觉 token 的注意力分布的信息熵，公式为：
  \[
  H_{l,i}^{t} = -p_v(\alpha_{l,i}^{t}) \cdot \log p_v(\alpha_{l,i}^{t})
  \]
- 提出**保持分数（Retention Score）**，将即时注意力得分与跨模态注意力熵加权结合：
  \[
  R_{l,i}^{t} = \lambda \alpha_{l,i}^{t} + (1-\lambda)H_{l,i}^{t}
  \]
  其中 \(\lambda \in [0,1]\) 平衡两者贡献。高熵表示文本 token 对视觉 token 的注意力分布分散，意味着视觉上下文具有较高的不确定性，可能在未来解码中变得相关。

**（2）熵引导的状态转换（Entropy-Guided State Transition）**

- 将传统离散 KV 驱逐重构为连续状态更新：
  \[
  S_t = H_t S_{t-1} + A_t (k_t^\top v_t)
  \]
  其中 \(H_t\) 为保留矩阵（由交叉熵 sigmoid 变换后控制衰减），\(A_t\) 为吸收矩阵（由累积注意力控制注入强度）。
- 状态空间的大小与序列长度和视觉分辨率无关，保持 **O(1) 内存开销**。

**（3）查询条件下的状态检索（Query-Conditioned State Retrieval）**

- 设计了**双状态架构**（灵感来自人类记忆的层级结构）：
  - **视觉主导状态（Visual-Dominant State, \(S_V\)）**：保持视觉 patch 的空间拓扑结构，分解为正交的水平/垂直扫描子状态，以根 patch 为锚点，基于空间距离（曼哈顿距离）调制衰减。
  - **召回导向状态（Recall-Oriented State, \(S_T\)）**：捕获长期语义依赖，维护固定长度滑动窗口，将窗口外但高熵的非 Heavy-Hitter token 压缩进入该状态。
- 解码时通过门控因子 \(\gamma_t = \sigma(W_r \cdot H_t + b_r)\) 动态调节从状态中检索的信息与局部注意力输出的融合比例：
  \[
  O_t = \text{Attn}_{\text{local}}(q_t, K_{\text{local}}, V_{\text{local}}) + \gamma_t \cdot O_S^{(t)}
  \]

论文还提供了 SSM 形式的注意力重写公式：\(SSM(Q, K, V) = Q_t \left( \sum_{i=1}^{t} \gamma^{t-i}(K_i^\top V_i) \right)\)，通过循环更新实现固定内存的上下文压缩。

## 3. 实验设计

### 3.1 模型架构

在三种多模态模型架构上验证：
- **LLaVA-v1.5-7B**：广泛使用的多模态指令微调基线
- **Qwen3-VL-4B** 和 **Qwen3-VL-8B**：代表性高效通用多模态模型

### 3.2 评估基准（8个）

| 类别 | 基准 |
|------|------|
| 专家级推理 | MMMU |
| 文档/场景文本理解 | DocVQA, TextVQA |
| 数学视觉推理 | MathVista |
| 整体感知 | MMStar, BLINK |
| 对话与具身 AI | MMCoQA, ALFRED |

### 3.3 对比方法

- **重要性中心剪枝方法**：H2O、SnapKV
- **模态感知压缩方法**：LOOK-M、Meda、SAINT
- 此外还将 **Full Cache**（完整KV缓存）作为上界参考

### 3.4 评估维度

- 主实验：各基准上的准确率对比
- 效率分析：解码延迟和 GPU 内存占用
- 消融研究：对各组件分别移除测试
- 不同缓存预算（5%~60%）下的性能稳定性测试

## 4. 资源与算力

论文在效率分析部分提及使用 **单个 NVIDIA A100 Tensor Core GPU** 进行评估，但**未明确说明**：
- GPU 总数量
- 训练/微调时长
- 具体能耗

虽然提供了解码延迟和内存占用的量化数据（如 5% 预算下内存从 2.24 GiB 降至 0.23 GiB，加速 1.75×），但缺少训练阶段算力开销的完整披露。这是实验描述中信息覆盖不完整的一处。

## 5. 实验数量与充分性

### 5.1 实验数量

论文共开展了以下实验：
1. **主实验**：3个模型 × 8个基准 = 24 组主要性能对比
2. **效率分析**：4 种压缩比例下的延迟与内存测量
3. **消融研究**：3 组关键组件移除实验（熵指标 EM、模态无关状态 MA、查询检索 QR）
4. **缓存预算灵敏度实验**：从 5% 到 60% 的多档预算下与基线方法对比

### 5.2 充分性与公平性评估

**充分之处：**
- 覆盖了从 4B 到 8B 多种参数规模的模型，且包含 LLaVA 与 Qwen3-VL 两类架构，验证了方法的架构无关性。
- 基准覆盖面广，涵盖文档理解、数学推理、对话、具身 AI 等多样任务。
- 消融研究验证了各核心组件的贡献。

**不够充分之处：**
- **模型规模梯度有限**：最大仅到 8B 参数，缺乏更大规模（>30B）的验证，论文自身也在 Limitation 中承认了这一局限。
- **缺少与最新方法的横向比较**：如未与 FastV 等论文中提到的其他方法定量对比。
- **部分基准上优势不明显**：如 MMMU 上相对 Full Cache 仍有明显差距，但论文未深入讨论压缩带来的不可避免性能损失与收益的权衡边界。
- **缺乏统计分析**：未报告多次运行的标准差或显著性检验，难以判断性能差异的统计可靠性。

## 6. 论文的主要结论与发现

1. **RetentiveKV 显著优于现有 KV 压缩基线**：在 8 个基准上均超越 H2O、SnapKV、LOOK-M、Meda、SAINT 等对比方法。
2. **有效性验证**：实现了 **5.0× KV 缓存压缩**和 **1.5× 解码加速**，在 5% 极限预算下可达到 1.75× 加速。
3. **熵驱动机制的优越性**：跨模态注意力熵能有效识别"延迟关键"token，避免了重要性中心方法的过早驱逐问题。
4. **连续状态空间优于离散剪枝**：通过状态压缩而非离散删除，在极端预算（5%~10%）下性能显著优于基线，尤其体现在 "Text Needle In A Haystack" 任务上（表现几乎翻倍于 Meda）。
5. **双状态架构有效缓解跨模态干扰**：将视觉与文本状态分离比统一状态空间平均性能提升 3.1%。
6. **消融实验确认各组件必要性**：状态保留+查询检索机制是性能贡献最大的组件，移除后性能下降 4.6%~5.4%。

## 7. 优点

### 方法层面
- **问题洞察深刻**：精准识别了多模态 KV 压缩中"延迟重要性"和"视觉连续性坍塌"两个此前被忽视的问题，并通过可视化实验（图1、图2）提供了实证支持。
- **理论框架新颖**：将 KV 驱逐从离散剪枝重构为连续状态演化，借鉴 SSM 的递归结构，在概念上实现了从"丢弃"到"压缩保留"的范式转变。
- **熵作为前瞻性指标的设计巧妙**：利用高熵反映"不确定性"和"潜在相关性"，弥补了纯注意力分数只看当下、不看未来的缺陷。
- **双状态设计兼顾空间与语义**：视觉主导状态保留空间拓扑，召回导向状态捕获长程语义，体现了对人类记忆层级结构的合理类比。
- **内存效率 O(1)**：与视觉分辨率无关的固定状态空间开销，理论上具有很好的可扩展性。

### 实验层面
- 多模型、多基准、多预算的全面评估体系。
- 同时报告了性能和效率两个维度的结果，不仅有准确率比较，还有延迟和内存数据。
- 消融实验设计清晰，逐一验证了各组件的独立贡献。

## 8. 不足与局限

### 实验覆盖局限
- **模型规模受限**：最大仅验证到 8B 参数，未覆盖大规模模型（>30B）。论文自述"延迟重要性"现象是否随模型容量增大而增强仍是开放问题。这一局限意味着在更大模型上，熵驱动保留机制的有效性尚缺乏实证确认。
- **模态覆盖有限**：仅涉及视觉-语言两种模态，未涵盖音频、视频等。虽然论文指出 RetentiveKV 的"连续演化"范式在原理上模态无关，但缺少实际验证。
- **未提供训练/微调阶段的开销数据**：论文完全聚焦于推理阶段优化，但对于熵估计器、门控因子等组件是否需要额外训练或引入推理开销，说明不够透明。

### 方法局限
- **超参数敏感性未充分探讨**：保留阈值 \(\tau\)、权重系数 \(\lambda\)、滑动窗口大小 \(W\) 等超参数对性能的影响未见敏感性分析。
- **门控因子依赖熵的简化假设**：\(\gamma_t\) 仅由当前熵决定，可能忽略了查询内容与检索状态之间的细粒度语义匹配度。
- **公式复杂度较高**：状态更新和查询检索涉及矩阵运算，虽然在内存上有优势，但其实际计算效率在极端长序列下的表现仍需更多实验支撑。

### 偏差风险
- 论文观察到的"延迟重要性"现象基于特定任务（VQA）的注意力可视化，其在不同任务类型（如纯感知任务 vs. 推理任务）中的普遍性程度未系统量化。
- 实验在英文基准上进行，缺乏多语言场景验证，可能遗漏语言多样性的影响。

### 应用限制
- 对保持较高压缩比下的质量保证阈值（即技术最小可行的压缩率边界）未做明确定义。尤其是在对输出保真度要求极高的应用场景（如医疗影像问答、法律文档理解），5% 预算下压缩带来的精度损失（4%~7%）是否可接受仍有待探讨。
- 方法的实际部署需要修改现有 Transformer 注意力层为 SSM 风格的递归计算，与当前广泛使用的 FlashAttention 等硬件优化内核的兼容集成方式论文未作阐述。

---

（完）
