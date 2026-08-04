---
title: "When KV Cache Reuse Fails in Multi-Agent Systems: Cross-Candidate Interaction is Crucial for LLM Judges"
title_zh: 当KV缓存复用在多智能体系统中失效：跨候选交互对LLM评审至关重要
authors: "Sichu Liang, Zhenglin Wang, Chujiajia, Pengfei Xia, Hui Zang, Deyu Zhou"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.327.pdf"
tags: ["query:agent-cache"]
score: 8.0
evidence: 分析多智能体系统中跨上下文KV缓存复用，揭示其对LLM评审的失效模式并提出一致性指标JCR
tldr: 多智能体流水线中，LLM评审对多个候选回答进行聚合，该场景常用KV缓存复用加速预fill。论文发现，对生成agent有效的复用策略可能严重扰动评审模型的选择，即使端任务准确率看似稳定，评审结果也与稠密预fill不一致。为此引入评审一致性率（JCR）并给出诊断手段，强调在跨上下文缓存共享时需谨慎评估对下游agent的影响。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 691, \"height\": 727, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1447, \"height\": 875, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 797, \"height\": 318, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 804, \"height\": 1040, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 797, \"height\": 362, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 793, \"height\": 305, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 804, \"height\": 297, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 801, \"height\": 602, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1244, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1319, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long327/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1327, \"height\": 381, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1649, \"height\": 752, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 800, \"height\": 284, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 797, \"height\": 465, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 794, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 797, \"height\": 249, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 801, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 795, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1356, \"height\": 597, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long327/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1562, \"height\": 2275, \"label\": \"Table\"}]"
motivation: KV缓存复用在多智能体评审中可能严重影响评审行为，产生与稠密预fill不一致的结果。
method: 通过GSM8K、MMLU和HumanEval实验，量化KV缓存复用对LLM评审的影响，并定义评审一致性率（JCR）进行诊断。
result: 发现对执行agent有效的复用策略会扰动评审选择，JCR揭示了一致性风险。
conclusion: 评估跨上下文KV缓存复用时，必须同时考虑其对下游评审agent行为的影响，而不只关注速度提升。
---

## Abstract
Multi-agent LLM systems routinely generate multiple candidate responses that are aggregated by an LLM judge. To reduce the dominant prefill cost in such pipelines, recent work advocates KV cache reuse across partially shared contexts and reports substantial speedups for generation agents. In this work, we show that these efficiency gains do not transfer uniformly to judge-centric inference. Across GSM8K, MMLU, and HumanEval, we find that reuse strategies that are effective for execution agents can severely perturb judge behavior: end-task accuracy may appear stable, yet the judge’s selection becomes highly inconsistent with dense prefill. We quantify this risk using Judge Consistency Rate (JCR) and provide diagnostics showing that reuse systematically weakens cross-candidate attention, especially for later candidate blocks. Our ablation further demonstrates that explicit cross-candidate interaction is crucial for preserving dense-prefill decisions. Overall, our results identify a previously overlooked failure mode of KV cache reuse and highlight judge-centric inference as a distinct regime that demands dedicated, risk-aware system design.

---

## 论文详细总结（自动生成）

## 《When KV Cache Reuse Fails in Multi-Agent Systems》论文总结

### 1. 论文核心问题与整体含义

- **研究动机**：多智能体（Multi-Agent）LLM系统通常由多个执行Agent生成候选回答，再由一个LLM评审（LLM Judge）聚合并选出最佳候选。这种流水线中，各Agent与评审之间反复交换上下文，导致大量预填充（prefill）计算冗余。为降低计算成本，近年来许多工作提出KV缓存复用（KV Cache Reuse），在部分共享上下文中复用已计算的KV缓存，并报告了针对生成Agent的显著加速效果。
- **核心问题**：论文指出，这些效率收益**并不能均匀地迁移到评审Agent（judge-centric）的推理场景**。KV缓存复用在执行Agent上有效，却可能严重扰动评审行为——端任务准确率看似稳定，但评审对候选的选择与稠密预填充（dense prefill）高度不一致，即存在**决策非不变性（decision non-invariance）**。
- **整体含义**：论文揭示了KV缓存复用一个此前被忽视的失败模式，强调评审为中心的推理是一个**独立的、需要专门风险感知系统设计**的推理场景。仅监控任务指标（如准确率）会掩盖潜在的评审选择不稳定性，这对归因、解释和可审计性等下游属性有重要影响。

### 2. 论文提出的方法论

- **核心思想**：以“评审视角”重新审视KV缓存复用，引入**Judge Consistency Rate（JCR，评审一致性率）**作为关键指标，量化KV复用相对于稠密预填充保留评审选择行为（而非仅最终答案）的能力。
- **问题定义**：设输入问题为 x，N 个执行Agent各自以特定角色提示 pᵢ 生成候选回答 yᵢ，评审Agent J 以评审提示 p_J 在**单一上下文**中对全部候选进行联合推理，输出最终答案 ŷ 与所选候选索引 î：(ŷ, î) = J(p_J, x, y₁:ₙ)。
- **候选生成模式**：定义了两种常见生成方式——渐进式精炼（Progressive Refinement，后生成者看到前序候选）和并行探索（Parallel Exploration，候选互相独立）。
- **四种评审侧缓存构建策略对比**：
  - **Dense Prefill**：完整重算评审KV缓存，作为参考基准。
  - **Naïve Reuse**：仅做位置对齐（RoPE重索引）和拼接，直接复用执行侧缓存块，不做任何修正。
  - **KVCOMM**：基于锚点（anchor）检索偏移量对复用块做修正，按Agent分池，满足可靠性判据才复用，否则回退稠密计算。
  - **PAL-KV（Pooled-Anchor Lookup）**：论文设计的探针方法，仅将锚点检索范围从Agent专属池改为所有Agent的锚点池并集，用于检验Agent身份是否是主导瓶颈。
- **JCR定义**：在相同候选集合与展示顺序下，KV复用与稠密预填充选择同一候选的样本比例（shuffle时用相同排列并映射回原始候选ID）。
- **诊断机制**：
  - **注意力诊断**：分析评审首token生成时对各区域的注意力分布，发现复用方法弱化了后续候选块（later slots）的跨候选注意力。
  - **遮蔽消融（Masking Ablation）**：在密集预填充下显式阻断跨候选注意力，发现JCR急剧崩溃（接近随机水平），从而直接证明跨候选交互对评审决策的必要性。
- **两个探索性优化方向**：
  - **方向一：交互感知的选择性上下文保留（interaction-preserving reuse）**——通过全局筛选交互关键token做选择性重算。
  - **方向二：元推理与风险感知回退门控（risk-aware gating）**——用简单分类器识别“普遍安全”（universally safe）的复用实例，对不安全实例回退稠密计算。

### 3. 实验设计

- **Benchmarks（数据集）**：
  - **GSM8K**（小学数学推理，1,319题全量测试集）
  - **MMLU**（多领域知识问答，153题固定验证子集，seed=888）
  - **HumanEval**（代码生成，161个Python任务全量）
- **候选生成**：每个示例生成 N=4 个候选；固定候选集（执行侧不用复用，同一候选文本用于所有评审侧方法）；评估no-shuffle和shuffle两种候选排列。
- **对比方法**：
  - Dense Prefill（基准）
  - Naïve Reuse（纯位置对齐拼接）
  - KVCOMM（锚点偏移修正，anchor pool size=5）
  - PAL-KV（锚点池化检索探针）
  - 三个额外的RAG类KV复用基线：EPIC、CacheClip、SamKV（均适配到评审侧设置）。
- **主实验矩阵**：3个数据集 × 2种候选生成模式 × 2种shuffle设置 × 4种方法（含Dense基准），同时记录Acc、JCR、Reuse Rate三个指标。
- **消融实验**：
  - 锚点池大小（5/10/15/20）
  - 候选数量（2/3/4/5）
  - 模型家族与规模（Llama-3.1/3.2系列3B–72B、Qwen-2.5系列；另用8×Ascend 910B扩展更大规模）
  - 槽位对齐变体（Slot-Aligned）
  - 注意力诊断的三种聚合视角（完整选择语句、跨head、跨layer）
  - JCR不匹配的后果分层（Harmful/Helpful/Benign/Joint-error）
  - 稠密预填充的参考鲁棒性（置信度探针、10次随机顺序投票参考）
- **附加分析**：任务难度与JCR解耦分析（t-SNE可视化 + ACC Counts vs JCR Counts联合分布）；GSM8K案例研究。

### 4. 资源与算力

- **主实验硬件**：2张 NVIDIA RTX 4090 GPU（24GB）；更大规模模型扩展实验使用 8张 Ascend 910B NPU（64GB/卡）。
- **模型精度**：bfloat16；最大生成长度512 tokens。
- **训练时长**：论文未提及训练时长——本文是推理优化研究，**不涉及模型训练**，只涉及推理阶段的前向计算和缓存复用策略，因此没有训练时间报告。
- **辅助模型**：CacheClip和SamKV使用CPU上的Llama-3.2-1B-Instruct作为辅助打分模型。
- 需要指出的是，文中**未报告端到端延迟或吞吐量**的具体数值，Reuse Rate作为效率替代指标。

### 5. 实验数量与充分性

- **实验数量**：实验较为丰富。主实验覆盖3个数据集×2种生成模式×2种排序设置×4种方法，共48组设置指标；另有锚点规模、Agent数量、模型规模（8种规模）、3个额外基线（3个数据集×2种模式）、2个方向探索的实验，以及注意力诊断、遮蔽消融、案例研究、鲁棒性探针等多个补充实验。
- **充分性评价**：
  - ✅ **覆盖面较广**：跨推理、知识、代码三个任务域；跨两种候选生成范式；跨多种模型家族和规模（3B到72B）；消融设计系统化。
  - ✅ **设置较为客观**：固定候选集以隔离评审侧影响；shuffle对照设计合理；以密度预填充为行为参考而非绝对正确基准；补充了稠密预填充本身的鲁棒性分析（置信度、顺序敏感性），公平性意识较强。
  - ⚠️ **局限**：模型最大72B，未覆盖真正前沿超大模型（如数百B级）和MoE架构；实验固定在同一推理栈（HuggingFace Transformers）；未报告端到端延迟/吞吐；两类候选生成均使用同质Agent（同角色prompt）。
  - ⚠️ **轻微不平衡**：消融实验主要基于shuffle下的MMLU Progressive Refinement，其他设置下的消融覆盖相对较少。

### 6. 论文主要结论与发现

- **KV缓存复用在评审场景中非行为保持（not behavior-preserving）**：复用方法可以显著改变评审对候选的选择，即使端任务准确率接近稠密预填充，JCR仍可能大幅偏低（在shuffle下部分低至约20%）。
- **Accuracy与JCR解耦**：任务正确性与选择一致性是部分解耦的维度；仅看Acc会掩盖潜在的决策不稳定性。
- **顺序扰动（shuffle）放大不一致性**：复用方法高度依赖候选布局；候选排列变化导致JCR大幅下降，说明复用对前序候选配置的近似不稳定。
- **跨候选交互是核心机制**：注意力诊断显示复用系统性地削弱对后续候选块的注意力；遮蔽消融直接证明跨候选交互对保持稠密预填充决策至关重要。
- **Agent身份不是主导瓶颈**：PAL-KV（锚点池化）仅在固定布局下有微小增益，shuffle下与KVCOMM类似，说明失败主要由变化的跨候选上下文/布局驱动。
- **规模扩大无法可靠恢复一致性**：增大模型规模改善Acc但不改善JCR；增加候选数提高Acc但降低JCR；增大锚点池提高复用率但无助于恢复JCR。
- **现有RAG类局部修复方法（EPIC/CacheClip/SamKV）同样无法恢复评审侧不一致性**，最佳JCR仅约34%。
- **缓解方向可行但代价大**：交互感知选择保留部分提升JCR但增益有限；保守门控大幅提升JCR但以大幅牺牲复用率为代价（Reuse率可低至5%），说明两类方向都未真正解决问题，需要更精细的评审感知设计。

### 7. 优点

- **问题定位精准且新颖**：首次系统性地揭示KV缓存复用对LLM评审的失败模式，指出“效率优化改变推理过程”这个以往未被重视的变量，不同于将评审不稳定归因于模型局限或任务偏差的既有文献。
- **指标设计有针对性**：JCR直接测量复用相对稠密预填充的选择行为保留度，比单独看任务准确率更能暴露隐患；补充JCR-Vote、Consequentiality分析，使指标更稳健。
- **方法论严谨、诊断层次丰富**：
  - PAL-KV作为受控探针很巧妙——仅改变检索范围而保持复用机制不变，从而定位“Agent身份”这个变量。
  - 遮蔽消融设计干净——保持相同评审格式但阻断跨候选注意力，直接分离了“格式不兼容”与“交互缺失”。
  - 注意力可视化覆盖多层级（token、head、layer、完整选择语句），证据链完整。
- **实验设计公平意识强**：固定候选集隔离变量；不把稠密预填充当作绝对oracle，显式分析其鲁棒性（顺序敏感性、置信度）；shuffle与no-shuffle双设置对照。
- **反方证据考虑充分**：尝试了锚点扩大、模型扩大、多种基线、多种探针来排除替代解释，使“跨候选交互被破坏”这一核心归因更有说服力。
- **与系统实践结合紧密**：讨论的交互感知复用和风险感知门控方向贴合实际部署需求，对未来评审感知KV加速系统设计有直接指导意义。

### 8. 不足与局限

- **实验覆盖有限**：最大模型72B，未覆盖前沿更大规模模型与MoE架构；仅用同质Agent（相同角色prompt），未测试异构Agent（如强评审+弱生成、混合模型家族）；未做跨模型/跨架构的KV复用评估。
- **部署栈单一**：全部实验基于HuggingFace Transformers，不同推理框架（如vLLM）、注意力实现、缓存管理策略可能影响结论的绝对数值。
- **效率度量不完整**：只报告Reuse Rate作为效率代理，缺少端到端延迟、吞吐、能耗等系统级指标，效率与质量的具体权衡未被量化。
- **协议依赖性强**：研究发现基于特定评审协议（联合多候选选择+结构化输出），不同评审协议（如成对比较）、输出格式或候选格式可能改变敏感性大小（作者也承认这一局限）。
- **案例研究代表性有限**：附录GSM8K案例恰逢两个正确候选高度相似（Agent 1和Agent 4），属于隐含打平场景，从中难以完全区分“真正的选择改变”与“任意打破平局”的边界；不过作者也坦承这反映的是归因不稳定性而非答案质量下降。
- **缓解方案尚未闭合**：两个探索方向的增益有限或代价过高（或降低复用率、或增加延迟），说明问题仍未真正解决，论文停留在“识别问题+初步方向”而非“完整解决方案”。
- **安全性讨论不足**：虽然提到高价值场景（医疗、金融、法律）的风险，但未给出应用级安全指南，仅在Limitation中提示需要领域专属评估。

（完）
