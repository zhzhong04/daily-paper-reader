---
title: "When KV Cache Reuse Fails in Multi-Agent Systems: Cross-Candidate Interaction is Crucial for LLM Judges"
title_zh: 当KV缓存复用在多智能体系统中失效：跨候选交互对LLM法官至关重要
authors: "Sichu Liang, Zhenglin Wang, Chujiajia, Pengfei Xia, Hui Zang, Deyu Zhou"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.327.pdf"
tags: ["query:cache-reuse"]
score: 9.0
evidence: 研究多智能体LLM法官流程中KV缓存复用的失效问题
tldr: 多智能体LLM系统中常由LLM法官聚合多个候选回答，为降低prefill开销，现有工作主张在部分共享上下文间复用KV缓存，并报告了生成智能体的显著加速。本文发现这些效率收益并不能统一迁移到法官为中心的推理中：在GSM8K、MMLU和HumanEval上，对执行智能体有效的复用策略可能严重扰动法官行为，使端任务准确率看似稳定但法官选择与稠密prefill高度不一致。作者提出法官一致性率（JCR）量化该风险，并提供诊断工具，提示跨候选交互对法官至关重要。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 691, \"height\": 727, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1447, \"height\": 875, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 797, \"height\": 318, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 804, \"height\": 1040, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 797, \"height\": 362, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 793, \"height\": 305, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 804, \"height\": 297, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 801, \"height\": 602, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1244, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1319, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1327, \"height\": 381, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1649, \"height\": 752, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 800, \"height\": 284, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 797, \"height\": 465, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 794, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 797, \"height\": 249, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 801, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 795, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1356, \"height\": 597, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1562, \"height\": 2275, \"label\": \"Table\"}]"
motivation: 多智能体LLM系统中KV缓存复用虽能加速生成智能体，但对法官为中心的推理可能造成严重扰动，现有复用策略未经充分验证。
method: 通过GSM8K、MMLU和HumanEval上的实验分析复用策略对法官行为的影响，并提出法官一致性率（JCR）作为量化诊断指标。
result: 发现有效于执行智能体的复用策略会显著降低法官决策一致性，端任务准确率看似稳定但选择不可复现。
conclusion: 跨候选交互是法官可靠推理的关键，KV缓存复用需谨慎设计，JCR可作为评估与诊断工具。
---

## Abstract
Multi-agent LLM systems routinely generate multiple candidate responses that are aggregated by an LLM judge. To reduce the dominant prefill cost in such pipelines, recent work advocates KV cache reuse across partially shared contexts and reports substantial speedups for generation agents. In this work, we show that these efficiency gains do not transfer uniformly to judge-centric inference. Across GSM8K, MMLU, and HumanEval, we find that reuse strategies that are effective for execution agents can severely perturb judge behavior: end-task accuracy may appear stable, yet the judge’s selection becomes highly inconsistent with dense prefill. We quantify this risk using Judge Consistency Rate (JCR) and provide diagnostics showing that reuse systematically weakens cross-candidate attention, especially for later candidate blocks. Our ablation further demonstrates that explicit cross-candidate interaction is crucial for preserving dense-prefill decisions. Overall, our results identify a previously overlooked failure mode of KV cache reuse and highlight judge-centric inference as a distinct regime that demands dedicated, risk-aware system design.

---

## 论文详细总结（自动生成）

## 论文详细中文总结

### 一、核心问题与研究动机

- **研究背景**：多智能体 LLM（MAS）系统通常由多个执行智能体生成候选答案，再由一个中心 LLM 法官（Judge）在单一上下文中联合比较这些候选并输出最终答案与最佳智能体编号。这类流水线中，各智能体的输入上下文存在大量重叠，导致重复的 prefill 计算开销极高。
- **已有方案的局限**：近年来提出的 KV 缓存复用技术（如跨前缀近似复用、KVCOMM 等）在生成智能体（execution agents）侧取得了显著加速效果。但这些工作主要从执行智能体视角评估，默认效率收益能均匀迁移到流水线的所有组件中。
- **本文发现的核心问题**：KV 缓存复用在法官为中心的推理（judge-centric inference）中**不具备决策不变性（decision non-invariance）**——复用策略可能保持答案正确率看似不变，但法官选择的最佳智能体与 dense prefill 结果产生显著分歧。这一失败模式在之前的研究中完全未被关注。
- **研究意义**：法官必须执行跨候选的联合比较与相对推理，这与生成任务在本质上是不同的推理模式；此论文首次系统性地揭示 KV 缓存在这种模式下的失效风险，提出法官中心推理是需要专门风险感知系统设计的独立场景。

---

### 二、研究方法论

#### 核心思想
以"法官决策一致性"为核心关注点，对比 dense prefill 与不同 KV 复用策略在法官侧的行为差异，并通过注意力诊断与消融实验定位失败机制。

#### 关键概念与定义
- **候选生成范式**：两种常见的多智能体协作模式
  - **渐进式精炼（Progressive Refinement）**：候选按顺序生成，后续智能体可参考先前候选
  - **并行探索（Parallel Exploration）**：各智能体独立生成，彼此不参考
- **法官输入顺序**：支持 no-shuffle（固定顺序）与 shuffle（随机置换）两种设定，用于隔离内容判断与顺序效应

#### 核心指标：JCR（Judge Consistency Rate）
- 定义为复用方法与 dense prefill 在相同候选集与相同呈现顺序下选择同一候选的百分比
- 用于量化复用策略相对 dense prefill 的**决策非不变性**，补充了仅看端任务准确率的不足

#### 对比的缓存构建策略

1. **Dense Prefill（稠密预填充）**：完整重新计算法官 KV 缓存，作为行为参照基准
2. **Naïve Reuse（朴素复用）**：仅通过位置对齐（RoPE 重索引）将执行侧缓存的候选块直接缝合到法官上下文中，不考虑前缀偏差
3. **KVCOMM（锚点偏移校正）**：为每个候选块检索锚点并预测偏移量进行校正；使用共享性判据在不可靠时回退到 dense 计算
4. **PAL-KV（汇集锚点查找）**：本文提出的一种最小化变体，将 KVCOMM 的锚点检索范围从"智能体专用池"改为"全部智能体锚点池的并集"，用于探测"智能体身份"是否是失败的主因

#### 机制诊断方法
- **注意力诊断**：分析法官第一个 token 生成时的注意力分布，按区域（前缀 + 4 个候选槽）统计相对注意力质量
- **掩码消融（Masking Ablation）**：在保持法官风格提示格式不变的前提下，显式阻断候选间的交叉注意力（候选 i 不能看到候选 1:i-1），验证跨候选交互的必要性

---

### 三、实验设计

#### 基准数据集
- **GSM8K**：小学数学推理（完整测试集 1,319 题）
- **MMLU**：多领域知识问答（153 道抽样子集，seed=888）
- **HumanEval**：Python 代码生成（完整 161 题，Pass@1 评估）

#### 候选生成设置
- 每个示例生成 N=4 个候选答案
- 执行智能体使用温度 0.2，法官使用温度 0
- **固定候选集**：候选文本只生成一次，对所有法官侧方法使用完全相同的候选文本，隔离法官侧缓存构造的影响

#### 对比方法
- Dense Prefill（参照）
- Naïve Reuse（位置对齐缝合）
- KVCOMM（锚点偏移校正 + 共享性判据）
- PAL-KV（汇集锚点）
- 额外对比：EPIC、CacheClip、SamKV（原用于 RAG 场景的三类代表性 KV 复用基线，适配到法官侧）

#### 消融实验设置
1. 锚点池大小（5/10/15/20）
2. 候选数量（2/3/4/5）
3. 模型系列与规模（Llama-3.1/3.2、Qwen-2.5，3B–72B）
4. 槽位对齐稳定化变体（Slot-Aligned）
5. 方向性试点：交互感知选择性重计算（Direction i）、风险感知门控（Direction ii）

---

### 四、资源与算力

- **主实验硬件**：2 张 NVIDIA RTX 4090 GPU（24GB/张）
- **大规模模型扩展**：8 张 Ascend 910B NPU（64GB/卡）
- **精度与配置**：bfloat16，最大生成长度 512 tokens
- **注意**：论文**未报告具体的训练/推理时长**、端到端延迟或能耗数据；没有提供端到端性能收益的系统级量化

---

### 五、实验数量与充分性评估

#### 数量维度
- **主实验**：3 个数据集（GSM8K、MMLU、HumanEval）× 2 种生成范式（渐进/并行）× 2 种排序设定（固定/打乱）= 12 组核心条件
- **每组的指标**：Acc.、JCR、Reuse Rate 三指标同时报告
- **消融实验**：锚点规模（4 档）、候选数（4 档）、模型规模（2 系列 × 5 档）、3 个额外基线（EPIC/CacheClip/SamKV）、2 个方向性试点
- **辅助诊断**：注意力可视化（含 token 级图）、掩码消融、t-SNE 语义分析、JCR 后果分级（harmful/helpful/benign/joint-error）、dense prefill 稳健性探测（置信度、顺序扰动投票、JCR-Vote）

#### 充分性评价
- **优点**：实验覆盖面较广，从多维度（数据、模型、候选数量、锚点规模、排序扰动）验证了结论的稳健性；JCR 结果跨设置一致地低，佐证了现象的系统性
- **不足**：
  - 主实验模型规模偏小（3B），更大规模仅做了有限扩展
  - 未覆盖 MoE 架构和异构模型间的法官-执行跨模型复用
  - 所有实验基于同一开源推理栈（HuggingFace Transformers），未验证不同 serving 系统下的稳定性
  - 额外基线（EPIC 等）为 RAG 场景适配，可能未完全发挥各方法在法官侧的最佳效果

---

### 六、主要结论与发现

1. **法官决策在 KV 复用下不具不变性**：KV 复用可显著改变法官选择的候选，即使端任务准确率保持稳定。这一现象在渐进式精炼和并行探索两种范式下均一致出现。
2. **准确率与 JCR 可解耦**：Acc. 可能看似稳定，但 JCR 可能大幅下降，说明仅监控任务指标会完全遗漏法官选择行为的扰动。相关性分析（ACC Counts vs. JCR Counts）显示二者仅弱相关。
3. **打乱顺序（shuffle）放大不一致性**：shuffle 使所有复用方法的 JCR 进一步显著下降（最高降幅超过 40 个百分点），表明复用对布局高度敏感，前面候选的整体配置决定了各候选块的有效前缀条件。
4. **跨候选交互是关键机制**：注意力诊断显示，复用方法对后续候选块的注意力显著弱化且更不稳定；掩码消融证明，切断跨候选注意（即便保持法官格式不变）会导致 JCR 骤降到接近随机水平（N=4 时约为 25–32%）。
5. **智能体身份不是主导瓶颈**：PAL-KV（汇集锚点）在固定布局下有小幅提升，但在 shuffle 下不能缓解 JCR 下降，说明主要驱动因素是变化的跨候选上下文/布局，而非智能体身份产生偏移分布差异。
6. **现有修复手段无法恢复不变性**：增加锚点池规模、增加候选数量（虽然提升 Acc）、扩大模型规模，均不能可靠恢复 JCR；EPIC、CacheClip、SamKV 等局部修复基线同样无法达到 dense prefill 的 JCR 水平。
7. **两个有前景的缓解方向**：① 交互感知的上下文选择性保留（部分恢复交叉候选可见性，JCR 提升有限）；② 元推理驱动的风险感知门控（安全实例分类器 AUC=0.82，可大幅提升 JCR 但以牺牲复用率为代价）。

---

### 七、论文优点

1. **发现了一个此前被忽略的系统性失败模式**：这是首次专门研究 KV 缓存复用对多智能体系统中法官组件的影响，填补了重要空白。
2. **提出 JCR 作为关键诊断指标**：精准捕捉"准确率看似稳定但决策行为被扰动"的现象，为法官侧缓存评估提供了有效工具。
3. **方法设计精巧**：通过 PAL-KV 作为受控探针（仅修改锚点检索范围），严格分离"智能体身份"与"跨候选交互"两个变量；通过掩码消融隔离"格式"与"交互"的作用。
4. **实验设计严谨**：固定候选集、相同打乱排列、逐方法 JCR 指示聚合等设计有效控制了混淆变量。
5. **深入的自省与分析**：附录中对 dense prefill 自身稳健性的探测（顺序投票、JCR-Vote、置信度）表明 JCR 衡量的是系统行为一致性而非把 dense 当绝对 oracle，增强了结论的可信度。
6. **后果分级分析**：将 JCR 不匹配分为 harmful/helpful/benign/joint-error 四类，揭示了不一致的后果严重性而非止步于行为指标。
7. **诚实承认局限**：讨论部分明确指出实验协议、模型规模、部署栈等限制，并给出了可复现的完整提示词模板和实现细节。

---

### 八、不足与局限

1. **模型规模覆盖有限**：主实验仅使用 3B 级模型，更大规模（70B+）仅做了有限验证；不保证结论能迁移到前沿规模模型或 MoE 架构。
2. **判定协议单一**：结论基于"联合多候选选择 + 结构化输出"这一特定判断协议；pairwise ranking、输出重写等不同协议下的敏感度可能不同。
3. **未覆盖异构模型复用**：未系统评估跨模型家族/架构（如强法官对弱生成器、混合家族 MAS）的法官侧 KV 复用行为。
4. **缺乏端到端系统量化**：只报告了法官侧的 Reuse Rate，未提供完整系统的延迟/吞吐/能耗收益数据——虽然这符合论文"集中剖析法官阶段"的定位，但削弱了对实际部署指导的完整性和可操作性。
5. **精度与数值稳定性**：锚点偏移补丁是近似方法，在部分参数设置下可能导致数值不稳定，影响效果验证；论文未充分讨论这一风险。
6. **缓解方案不成熟**：两个试点方向（交互感知重计算、风险门控）的收益有限（提升 JCR 但以牺牲复用率或增加额外延迟为代价），且尚未形成完整的工程方案。
7. **法官固有偏置问题未做区分**：论文未分析 KV 复用是否放大了法官固有的位置偏好等偏差，仅关注"与 dense 相比的行为变化"，不涉及法官绝对公平性。
8. **结果受部署栈影响**：所有实验基于固定开放源码推理栈，不同 serving 系统、注意力实现、缓存管理策略可能改变量化结果。

---

（完）
