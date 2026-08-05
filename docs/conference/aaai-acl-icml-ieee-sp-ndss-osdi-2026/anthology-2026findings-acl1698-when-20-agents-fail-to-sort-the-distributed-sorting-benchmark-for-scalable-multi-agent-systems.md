---
title: "When 20 Agents Fail to Sort: The Distributed Sorting Benchmark for Scalable Multi-Agent Systems"
title_zh: 当20个智能体排序失败：面向可扩展多智能体系统的分布式排序基准
authors: "Xin Yang, Junhao Wang, Bintao Tang, Xuxin Cheng, Cao Liu, Ke Zeng, Wenyuan Jiang"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1698.pdf"
tags: ["query:awc"]
score: 4.0
evidence: 多智能体系统中基于共享键值存储的协作机制
tldr: LLM多智能体系统在扩展时协调失败频发，本文提出分布式排序基准MAS-BENCH，隔离通信约束下的协调问题。发现随智能体数量增长，共享状态、惯例对齐和终止一致性持续失败。为缓解这些问题，提出CAMOC，一种基于协作感知信息共享和早期全局元数据的轻量级方案，提升多智能体规模扩展能力。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1698/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 785, \"height\": 773, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1698/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1649, \"height\": 416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1698/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1477, \"height\": 526, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1652, \"height\": 633, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1474, \"height\": 434, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 688, \"height\": 284, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1686, \"height\": 272, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 589, \"height\": 248, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1658, \"height\": 590, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 751, \"height\": 213, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 810, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 545, \"height\": 215, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 811, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 619, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1698/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 503, \"height\": 252, \"label\": \"Table\"}]"
motivation: 多智能体系统在规模扩大时协调能力脆弱，缺乏针对性基准。
method: 提出MAS-BENCH基准和基于协作感知信息共享的CAMOC方案。
result: 实验显示智能体数量增加时成功率骤降，CAMOC有所缓解。
conclusion: 该基准揭示多智能体协调瓶颈，为信息共享设计提供参考。
---

## Abstract
Current LLM-based multi-agent systems remain fragile under scaling, even on algorithmically trivial tasks. We introduce MAS-BENCH, a distributed-sorting benchmark that isolates coordination under explicit communication constraints: each agent observes only a local segment and must collectively produce a globally consistent order via broadcasting, peer-to-peer messaging, or a shared key-value store. Across LLM-based agents, success drops sharply as the number of agents grows, exposing persistent failures in shared state, convention alignment, and consistent termination. To mitigate these breakdowns, we propose CAMOC, a lightweight, drop-in proof-of-concept built on collaboration-aware information sharing, early global metadata exchange, and single-commit verification. CAMOC substantially improves coordination success and efficiency across backends, with the largest gains under shared-state interaction. Overall, MAS-BENCH provides a diagnostic benchmark and CAMOC offers a practical step toward more reliable large-scale LLM collaboration, highlighting a gap between individual reasoning and collective correctness.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 核心问题与整体含义（研究动机与背景）

- **研究背景**：大规模语言模型（LLM）驱动的多智能体系统近年来被视为扩展AI能力的重要方向。然而，多数成功的多智能体系统依赖大量人工搭建的脚手架（如预定义角色、任务分解模板、工程化流程），这使得"真正的自主协作"与"流程工程"之间的界限变得模糊。
- **核心研究问题**：论文提出一个尖锐的问题——当我们移除大多数人工脚手架、强制执行对称通信时，当前基于LLM的智能体能否可靠地协作完成一个简单但有结构的多智能体任务？
- **任务选择**：论文选择了**分布式排序**作为研究对象——算法上近乎平凡（局部排序极易完成），但在协调上极具挑战性（智能体必须通过通信达成全局一致的顺序）。这保证了失败率主要反映的是智能体间的协调缺陷，而非个体推理能力不足。
- **核心发现**：实验表明，随着智能体数量增加，成功率急剧下降，暴露了共享状态、惯例对齐、一致终止等系统性协调失败，揭示了个体推理能力与集体正确性之间存在显著鸿沟。

## 2. 论文提出的方法论

### 2.1 MAS-BENCH 基准

- **问题设定**：N个智能体，每个智能体观察到长度为K的局部数据段，必须通过通信环境E输出全局非递减的排序段。任务实例定义为元组 t = (N, K, E, l)。
- **三种通信范式**：
  - **P2P消息传递**：通过 `send_to(msg, id)` / `recv()` 进行定向消息传递。
  - **广播（Broadcasting）**：通过 `broadcast(msg)` / `recv()` 实现一对多消息广播。
  - **共享K-V存储**：通过 `read(k)` / `write(k, v)` 读写共享键值存储，写操作覆盖旧值。
- **输入顺序结构**：通过**逆序率** ρ(l) = Inv(l) / C(NK, 2) 量化输入的无序程度，生成五类输入族：asc、near_asc、random、near_desc、desc。
- **评估指标**：
  - **成功率（SR）**：所有智能体提交段与真实段完全一致的比例。
  - **轮数（R）**：最大工具调用轮数，衡量交互延迟。
  - **Token效率（TE）**：每10万token内成功排序的元素数。
  - **通信比例（CR）**：通信相关token占总token的比例。

### 2.2 CAMOC 协调方案

- **三个设计原则**：
  1. **协作感知（Collaboration-Awareness）**：智能体不仅共享数据，还共享假设、临时角色和分区假设，减少后续澄清需求。例如要求其他智能体"请分享你的本地列表"。
  2. **全局元数据（Global Metadata）**：早期主动交换粗粒度全局信号（如近似值范围、分区草图、进度状态），而非按需通信，以加速信息流动。
  3. **单次提交（One-shot Commitment）**：智能体做单次临时提交后进行最轻量验证，替代多轮反复验证——因为多轮验证会稀释上下文并放大不一致。
- **实现方式**：CAMOC 作为即插即用协调层，通过修改系统提示词注入行为约束，无需对底层LLM进行任何重训练。

## 3. 实验设计

### 3.1 评估模型

| 模型 | 架构特点 |
|------|----------|
| DeepSeek-V3.1 | 混合专家架构 |
| Qwen3-Next-80B-A3B | 激活参数约30B的MoE模型 |
| GPT-OSS-120B | OpenAI开源模型 |

三种模型代表了不同的训练策略和扩展规模，适用于压力测试。

### 3.2 实验场景

- **主干实验**：3个模型 × 3种通信后端 × 5类输入族 × 多种智能体数量（N=1, 3, 5, 10, 20）× 多种段长度（K=1, 5, 10），完整交叉覆盖。
- **消融实验**：在完整CAMOC基础上，分别移除协作家识/全局元数据组件（Abl. message）和单次提交组件（Abl. submit）。
- **扩展实验**（附录G.3）：新增两个任务——分布式最大值（松耦合）和分布式前缀和（中耦合），用于验证结论的可迁移性。
- **基线对比**：以不加入CAMOC修改的标准提示词协议（Base）为基线，同时对比两种消融变体。

### 3.3 Benchmark 特点

- 确定性正确性判定（全局拼接后必须严格非递减）
- 三个对称通信接口
- 多个规模的系统化扩展分析

## 4. 资源与算力

- **硬件**：NVIDIA GH200 GPU（120 GB HBM），默认4节点×4 GPU/节点=共16块GPU，每节点288 CPU核心。
- **服务框架**：SGLang v0.5.4.post1，多节点张量并行（TP=16）。
- **运行限制**：每任务12小时墙钟时间限制。
- **推理成本**：总计3150条日志、约2.117亿token消耗（其中通信token约1120万，占5.29%），基于OpenRouter定价的中点估算总成本约70.62美元（范围[20.35, 120.89]美元）。
- **不可复现性说明**：论文未披露具体训练/推理总耗时，但给出了上述资源配比和价格估算。

## 5. 实验数量与充分性

- **总量庞大**：主干实验约2,200次运行（附录G.1），加上扩展任务与诊断实验，具有一定的统计效力。所有数字均为多次重复运行的聚合结果。
- **多维覆盖**：3模型 × 3后端 × 5输入族 × 4个N × 3个K的交叉网格，加上2个消融条件，覆盖了较大的参数空间。
- **统计检验**：在消融比较中使用了Welch's t检验，发现Qwen3在P2P后端存在一个统计显著的回归（p < 0.05），并做了归因分析（附录G.4）。
- **客观与公平性**：
  - 优点：所有模型使用相同的提示结构、相同的工具接口、相同的评估协议；解码参数不做逐模型微调（使用SGLang默认值）；每个实验设置多次重复以缓解随机性。
  - 潜在不足：模型范围有限（均为公开模型，未包含闭源商业模型如GPT-4或Claude）；不同模型的API服务框架相同，但模型的工具调用解析器不同（如deepseekv3 parser），可能引入细微差异。

## 6. 主要结论与发现

- **RQ1 — 性能概况**：即使在局部排序平凡的情况下，全局正确性受限于跨智能体协调。Base协议下，Broadcasting上DeepSeek-V3.1成功率最高（80.8%），GPT-OSS-120B仅55.6%；Shared K-V后端是全模型的重大失败模式（DeepSeek 38.2%、GPT-OSS 25.6%）。
- **RQ2 — 通信拓扑影响**：通信拓扑不是表面选择，而是从根本上改变失败面。广播有利于快速收敛（R约8-17轮）；P2P可能产生大量协商开销（DeepSeek R≈38轮，GPT-OSS CR≈22-23%）；共享K-V在朴素协议下最脆弱。
- **RQ3 — 缩放效应**：存在明确的**协调缩放定律**。从N=1到N=20，Broadcasting下SR从100%降至38.6%（K=10时）；P2P下降至22.8%。轮数R随N增大而增加，TE急剧下降，CR上升，表明新增智能体主要引入协调开销而非并行加速。
- **RQ4 — CAMOC有效性**：CAMOC在三种后端和所有模型上显著提升成功率与效率，在Shared K-V后端增益最大——DeepSeek从38.2%提升至84.7%（+46.5pp），Qwen3从33.7%提升至67.2%（+33.5pp），GPT-OSS从25.6%提升至56.5%（+30.9pp）。每正确实例的token成本降低约一半。
- **RQ5 — 消融归因**：消息级协调（协作感知+全局元数据）主要提升效率并稳定共享状态交互；结构化提交（单次提交）主要提升正确性、防止不一致终止。两者结合取得最佳效果。
- **失败模式分类**：识别出五类系统化失败——边界不匹配、过早提交、过期K-V读取、数值幻觉、惯例错位。

## 7. 优点

- **任务设计的精妙性**：选择分布式排序作为基准是一个高招——它算法上平凡但协调上复杂，能干净地剥离个体推理能力，专门探测集体协调能力。正确性判定是确定性的，不需要人工评估或LLM裁判。
- **系统化的变量控制**：从通信范式（3种）、智能体规模（5档）、段长度（3档）、输入结构（5类）四个维度系统隔离影响因子，矩阵设计完整。
- **指标体系的完整性与成本-效率兼顾性**：同时覆盖有效性（SR）和协调成本（R、TE、CR），能刻画"成功但低效"与"高效但失败"等不同失败模式。
- **CAMOC的实用性和可迁移性**：即插即用、无需重新训练的协调层设计，可迁移性验证合理；在松/中/紧三类耦合任务上的扩展实验（Distributed Max、Prefix Sum、Sorting）表明其适用边界清晰可信。
- **透明度高**：附录给出了完整的提示词文本（含CAMOC注入的逐字条款）、命令分派契约表（表5）、算法伪代码（Algorithms 1-3），可复现性强。
- **坦率的统计归因**：对Qwen3在P2P上的负结果做了明确的组件级归因（One-shot Commitment抑制了迭代精化），没有掩盖负面发现。

## 8. 不足与局限

- **任务单一性**：基准核心仅覆盖分布式排序，虽扩展了Distributed Max和Prefix Sum两个补充任务，但这些都属于有确定全局真值、可程序化验证的合成任务；完全不涉及开放式生成、协商、规划等无唯一最优解的语义任务。
- **通信拓扑覆盖有限**：仅评估三种基本通信基元（广播、P2P、共享K-V），未覆盖分层拓扑、自适应拓扑、gossip协议、异步或消息可能丢失的网络环境。真实系统中的消息不可靠性和异步性可能改变失败模式。
- **智能体同质性限制**：所有智能体使用相同的LLM和相同的固定提示词，未探索异构智能体（不同模型/角色/专业化的混合）可能与协调协议产生的不同交互效应。
- **后端接口摩擦未完全消除**：Shared K-V在N=1时仍有20%失败率（附录G.2分析为接口摩擦而非协调问题），说明基准本身可能混入了"工具使用难度"和"协调难度"两个因素，不完全纯净。
- **统计显著性与模型覆盖**：消融分析中仅发现一个统计显著的回归点；且仅测试了三个开源/开放权重的模型，未涵盖闭源商业模型（如GPT-4系列、Claude系列），结论的普适性受到限制。
- **应用安全边界明确**：论文自身承认，该基准和CAMOC是评估工具而非部署就绪的艺术品，不可直接用于安全关键或真实世界的决策系统。
- **扩展任务的耦合度梯度可能不够精细**：从松耦合（最大值）到中耦合（前缀和）再到紧耦合（排序），三者之间缺乏更密集的耦合强度梯度，不利于精确刻画"增益随耦合强度变化的曲线"。

（完）
