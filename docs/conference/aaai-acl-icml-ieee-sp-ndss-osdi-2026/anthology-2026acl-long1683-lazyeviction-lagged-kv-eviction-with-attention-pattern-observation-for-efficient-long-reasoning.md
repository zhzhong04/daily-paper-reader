---
title: "LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning"
title_zh: LazyEviction：结合注意力模式观测的滞后KV驱逐以支持高效长程推理
authors: "Haoyue Zhang, Hualei Zhang, Xiaosong Ma, Jie Zhang, Song Guo"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1683.pdf"
tags: ["query:awc"]
score: 6.0
evidence: 基于注意力模式观测的滞后KV驱逐策略，面向高效长程推理
tldr: LazyEviction针对长推理任务中KV缓存占用过高的问题，揭示Token重要性重复出现的现象，即大量token在多次解码步骤后会重新获得高注意力，而现有压缩方法无法捕捉这一点。为此提出基于观测窗口的滞后驱逐框架，避免对周期关键token的误驱逐。实验证明该方法在降低内存开销的同时提升了长程推理质量，为推理类代理工作流的缓存驱逐提供了新思路。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1683/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1556, \"height\": 526, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1683/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1579, \"height\": 468, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1683/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1634, \"height\": 522, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1683/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1623, \"height\": 549, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1683/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1485, \"height\": 800, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1683/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 604, \"height\": 611, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1683/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 784, \"height\": 474, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 792, \"height\": 1097, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 707, \"height\": 710, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 773, \"height\": 321, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 609, \"height\": 419, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 758, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 797, \"height\": 642, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 642, \"height\": 253, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 766, \"height\": 638, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 787, \"height\": 368, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 815, \"height\": 366, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1683/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 823, \"height\": 362, \"label\": \"Table\"}]"
motivation: 解决长程推理中KV缓存内存开销大且现有方法无法捕捉token重要性重复的现象。
method: 提出基于观测窗口的滞后驱逐框架，依据注意力模式延迟驱逐可能再次关键的token。
result: 实验显示LazyEviction在降低内存的同时提升长推理任务的生成质量。
conclusion: 该工作为长推理场景的KV缓存驱逐提供了更稳健的策略。
---

## Abstract
Large Language Models (LLMs) exhibit enhanced capabilities by Chain-of-Thought reasoning. However, the extended reasoning sequences introduce significant GPU memory overhead due to increased key-value (KV) cache. Existing KV cache compression methods mitigate memory bottlenecks but struggle in long reasoning tasks. In this paper, we analyze attention patterns in reasoning tasks and reveal a **Token Importance Recurrence** phenomenon: a large proportion of tokens regain high attention after multiple decoding steps, which is failed to capture by existing works and may lead to unpredictable eviction on such periodically critical tokens. To address this, we propose **LazyEviction**, an observation window-based lagged eviction framework retaining latent recurring tokens by prioritized eviction based on tokens’ recurrence patterns. Extensive experiments demonstrate that LazyEviction reduces KV cache by 50% 70% while maintaining comparable accuracy, outperforming existing KV cache baselines. Our implementation code can be found at https://github.com/Halo-949/LazyEviction.

---

## 论文详细总结（自动生成）

# LazyEviction：结合注意力模式观测的滞后KV驱逐以支持高效长程推理

## 1. 论文的核心问题与整体含义

- **背景**：大语言模型（LLM）通过思维链（Chain-of-Thought, CoT）推理展现出强大的能力，但长推理序列（如数学与编程任务中可达16k token）导致KV缓存急剧膨胀，对GPU显存造成巨大压力。例如，在批大小为32时，KV缓存可能超过100GB，超出高端GPU的容量。
- **核心问题**：现有KV缓存压缩方法在长推理任务中性能严重退化。论文通过分析推理任务中的注意力模式，揭示了此前被忽略的 **Token Importance Recurrence（TIR）** 现象——即大量token在经历多个解码步骤后会重新获得高注意力权重。这类"周期性关键token"包含推理链中的条件信息、中间结论和初始问题条件，对验证、回溯和总结等推理能力至关重要。
- **整体含义**：现有的贪婪式驱逐策略（如基于当前注意力或累积注意力的方法）会在这些token的低注意力间隙将其误驱逐，造成不可逆的知识断裂和推理性能骤降。论文提出的LazyEviction通过"滞后决策 + 模式预测"避免了这一陷阱。

## 2. 论文提出的方法论

### 2.1 核心思想

LazyEviction 将KV驱逐从**逐步骤的贪婪决策**转变为**窗口化的滞后驱逐**：每隔W步才执行一次驱逐决策，利用观测窗口捕捉token注意力的周期性变化，保留"潜伏但可能重现"的token。

### 2.2 关键技术细节

**（1）Recurrence Interval Tracking（复发间隔跟踪）**
- 维护时间戳向量 TS_t，当token i 在某步骤t获得超过阈值α的注意力分数时，更新其最新激活时间戳 TS_t[i] = t。
- 引入 **Maximum Recurrence Interval（MRI）** 记录token两次连续激活之间的最长间隔，更新公式：
  - MRI_t = max{ MRI_{t-1}, TS_t − TS_{t-1} }
- MRI=0 表示token生成后从未被激活；MRI越大表示复发周期越长。

**（2）MRI-Centric Eviction（MRI中心驱逐策略）**

在每个决策步骤 t = kW（k ∈ N+），当缓存大小超过预算B时执行驱逐。重要性分数由两个启发式组成：

- **H1-Score（生存概率）**：衡量token在其MRI范围内重新变重要的可能性，公式为：
  - H1_t[i] = 2σ(−(t − TS_t[i]) / MRI_t[i])
  - 其中σ为sigmoid函数。当距离上次激活的时间越接近MRI，token未来重新重要的概率非线性下降。
  
- **H2-Score（频率先验）**：优先保留MRI较小的token（即更频繁复发的token），公式为：
  - H2_t[i] = 2σ(−MRI_t[i] − 1)
  - 若MRI=0，则H2=0。

最终综合分数为：I_t[i] = H1_t[i] + H2_t[i]（当MRI≠0时）；I_t[i] = H1_t[i]（当MRI=0时）。

**（3）驱逐策略**
- 始终保留最近W个KV对以维持局部连贯性。
- 从其余KV中选择分数最高的B−W个保留。

## 3. 实验设计

### 3.1 评测模型

| 模型 | 参数量 | 类型 |
|------|--------|------|
| DeepSeek-R1-Distill-Llama-8B | 8B | 推理蒸馏模型 |
| DeepSeek-R1-Distill-Qwen-7B | 7B | 推理蒸馏模型 |
| Qwen3-4B | 4B | Qwen系列推理模型 |
| QwQ-32B | 32B | Qwen系列推理模型 |
| Llama-3.1-8B-Instruct | 8B | 非推理模型（用于通用任务） |

### 3.2 评测数据集

- **数学推理**：GSM8K（1319样本）、MATH-500（500样本）、AIME（美国数学邀请赛）
- **科学QA**：GPQA Diamond（研究生级科学问答）
- **编程**：LiveCodeBench（随机抽样5%，即58样本）
- **通用长文本生成**：PIQA（引导CoT式长回答）、SQuALITY（长文档摘要）

### 3.3 对比方法

- **FullKV**（无压缩，上界参考）
- **TOVA**（基于当前注意力的驱逐）
- **H2O**（基于累积注意力的Heavy Hitter保留）
- **CAKE**（级联自适应驱逐）
- **RaaS**（基于时间戳的动态更新，最相关工作）
- **R-KV**（基于token相似性的冗余驱逐）

### 3.4 关键超参数

- 观测窗口W设为80% token MRI阈值的对应值（通过1%样本离线统计）
- 注意力阈值α：DS-Llama-8B设为0.0005，DS-Qwen-7B/Qwen3-4B/QwQ-32B设为0.0001
- 最大生成token数：GSM8K为4096、MATH-500/GPQA为8192、AIME/LiveCodeBench为16384

## 4. 资源与算力

- **硬件**：实验在 NVIDIA V100（32GB）GPU 上进行，操作系统为Ubuntu 20.04、CUDA 12.8。
- **未明确说明**：论文未明确说明所用GPU的确切数量和并行方式，但从描述来看实验规模较大。
- **参考信息**：论文提到若在100B级模型（如DeepSeek-R1）上评估MATH-500的500个样本，在8张A100 GPU上也需要数天，这也是未进行该实验的原因。
- **预统计开销**：确定W的MRI分析仅需2–20个样本，约10–40分钟，相对整体评测时间（7–20小时）开销微乎其微。

## 5. 实验数量与充分性

### 实验规模概览

- **主实验**（表1）：4个模型 × 3个数学数据集（GSM8K r=50%、MATH-500 r=50%、AIME r=30%），共12组对比。
- **域外推广**（表2）：2个模型 × 2个非数学数据集（GPQA Diamond r=50%、LiveCodeBench r=40%），共4组对比。
- **压缩比-精度权衡**（图5）：在3个数据集上、多个压缩比（r=10%~70%），对DS-Llama-8B和DS-Qwen-7B分别评测。
- **通用长文本场景**（表3）：Llama-3.1-8B-Instruct在PIQA（r=30%）和SQuALITY（r=20%）上的对比。
- **消融实验**（表4-5）：①基线方法+观测窗口机制的对比；②重要性分数组件消融（w/o H1、w/o H2）。
- **记忆效率**（图6）：KV缓存内存随输出长度的变化。
- **延迟与吞吐**（表8、图7）：不同预算下的单步延迟、批量推理吞吐量对比。
- **超参数敏感性**（表9-10）：W和α的不同取值。
- **分数函数形式探讨**（表6）：sigmoid/exp/tanh/log等函数的组合比较。

### 充分性与客观性评价

**优点**：
- 覆盖4种不同规模的推理模型（4B–32B），模型类型包括Llama蒸馏版和Qwen系列，具有一定多样性。
- 跨越数学、科学、编程三个推理域 + 通用QA和摘要场景，验证了方法的泛化性。
- 消融实验设计合理：通过给基线加观测窗口来排除"窗口内KV数量增多"这一混淆变量，结论可信度较高。
- 与最相关工作RaaS的差异分析详细，从数学定义上论证了LazyEviction的推广性（RaaS被指出无法处理长输入场景）。

**不足**：
- 未在100B级大规模模型（如DeepSeek-R1、Qwen3-Max）上验证，论文承认这是资源限制。
- 数学类评测为主，非数学数据集规模有限（LiveCodeBench仅抽样58样本）。
- 实验主要采用贪婪解码（非采样），对采样解码下的适用性未作探讨。
- 未明确评估统计显著性（如多次运行的标准差）。

## 6. 论文的主要结论与发现

1. **揭示TIR现象**：推理任务中超过95%的token表现出注意力重要性的周期性复发（MRI > 1），这些token对应推理链中的关键条件、中间结论和汇总信息，具有不可替代性。
2. **现有方法失败归因**：无论是基于当前注意力（TOVA）还是累积注意力（H2O）的驱逐，都无法捕捉token在低注意力间隔后重新变重要的模式，导致误驱逐。
3. **观测窗口的可行性**：统计发现约80%的token MRI不足175（在约8k输出长度下），说明通过合理窗口大小可以覆盖大多数复发token。
4. **方法有效性**：LazyEviction在30%~50%的KV预算下达到与FullKV相当甚至更优的精度（如MATH-500上75.2% vs FullKV的74.8%），且一致优于所有现有基线。
5. **通用性**：在非推理任务（PIQA、SQuALITY）上同样有效，说明不完全依赖推理任务特有的超长MRI特性。
6. **计算开销可控**：复杂度分析显示LazyEviction在一个窗口内的复杂度为O(WB + BlogB)，低于H2O和RaaS的O[W(B+BlogB)]。实验证明在长序列下λ低于TOVA，且支持更大batch size可实现最高4.28倍FullKV吞吐。

## 7. 优点

- **问题发现具有原创性**：TIR现象的揭示深化了对推理任务中注意力动态的理解，超越了"重击者（heavy hitter）"静态假设。
- **方法设计优雅**："滞后驱逐"的直觉简单而有力——与其在每一步冒险驱逐可能复活的token，不如观察一段时间再做决定。将驱逐频率从每步降低到每W步本身也带来了计算优势。
- **理论支撑完善**：将KV驱逐建模为多步动态优化问题（附录D），从理论上分析了分数函数的设计原则，并在附录中对不同函数形式做了系统性比较。
- **消融设计严谨**：通过给基线方法添加"观测窗口"来排除混淆变量，验证了MRI跟踪本身的贡献而非仅是窗口内额外KV的贡献。
- **工程性考量充分**：论文详细分析了计算复杂度、内存波动、实际吞吐和延迟，证明了方法不仅精度高，也具备实际部署价值。
- **与RaaS的边界清晰**：承认RaaS是自身的一个特例场景，并论证了更一般化的解决框架，学术诚信和定位明确。

## 8. 不足与局限

- **窗口大小W的选取依赖离线统计**：需要从1%测试样本中预统计MRI分布来确定W，虽然开销小但存在数据泄漏风险（论文在Limitations中讨论了可以通过验证集或上线预热方式缓解，但步骤上更繁琐）。
- **W和α需要手动调优**：两者在不同模型、任务上需要单独确定，论文虽给出敏感性分析但缺乏自适应调整机制。
- **大规模模型未经验证**：实验限于4B–32B模型，TIR现象在100B级模型上的表现尚不明确。
- **动态输入长度下的稳定性**：论文的公式推导假设了逐token的注意力可观测性，对于并行解码（如推测解码）或批量推理场景的适配性未被探索。
- **非推理场景提升有限**：论文承认在C4等纯语言建模任务中，TIR的MRI较小（<10），LazyEviction与H2O/RaaS等累积注意力方法的性能差异不显著。
- **长上下文输入场景未覆盖**：论文的框架理论上对Prefill token也会因长时间不复发而驱逐，但未在长文档输入的推理场景（如LongBench）中进行验证。

（完）
