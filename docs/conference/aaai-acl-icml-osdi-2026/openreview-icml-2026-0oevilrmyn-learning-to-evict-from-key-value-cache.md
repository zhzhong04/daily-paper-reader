---
title: Learning to Evict from Key-Value Cache
title_zh: 从键值缓存学习驱逐策略
authors: "Luca Moschella, Laura Manduchi, Ozan Sener"
date: 2026-04-30
pdf: "https://openreview.net/pdf/875c835732794c107c4793b6fb93559f5ecd4c2c.pdf"
tags: ["query:agent-cache"]
score: 7.0
evidence: 训练逐头RL智能体预测token效用并执行驱逐，是可用于智能体调度的动态预测头方法
tldr: 现有KV缓存驱逐依赖基于近期性或历史注意力的启发式指标，仅间接预测token未来效用且计算开销大。KVP将驱逐问题建模为强化学习，基于预计算生成轨迹为每个注意力头训练轻量级RL智能体，利用键值向量学习按预测未来用处排序，并由整体奖励引导。每个头学会专门化驱逐策略，在保持生成质量的同时降低缓存占用，为动态预测驱动的缓存驱逐提供了通用框架，可迁移到智能体调度场景。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 启发式驱逐指标只是token未来效用的间接代理，准确性和效率均有不足。
method: 将KV驱逐建模为RL问题，用预计算轨迹训练逐头RL智能体，学习基于键值向量的token排序。
result: 学习到的驱逐策略在保持生成质量下减少缓存内存，优于启发式方法。
conclusion: 学习式驱逐为预测驱动的缓存管理提供新途径，对未来智能体调度有借鉴意义。
---

## Abstract
The growing size of Large Language Models (LLMs) makes efficient inference challenging, primarily due to the memory demands of the autoregressive Key-Value (KV) cache. Existing eviction or compression methods reduce cost but rely on heuristics, such as recency or past attention scores, which serve only as indirect proxies for a token’s future utility and introduce computational overhead. We reframe KV cache eviction as a reinforcement learning (RL) problem: learning to rank tokens by their predicted usefulness for future decoding. To this end, we introduce KV Policy (KVP), a framework of lightweight per-head RL agents trained on pre-computed generation traces using only key and value vectors. Each agent learns a specialized eviction policy guided by a holistic reward, derived from future utility, that evaluates the quality of the ranking across all cache budgets, requiring no modifications to the underlying LLM or additional inference. Evaluated across two model families on the long-context benchmark RULER (up to 128K tokens) and the multi-turn dialogue benchmark OASST2-4k, KVP significantly outperforms strong baselines. Zero-shot tests on standard downstream tasks (BoolQ, LongBench passage retrieval, GovReport) further show that KVP generalizes beyond its training distribution and to considerably longer sequence lengths. These results demonstrate that learning to predict future token utility is a powerful and scalable paradigm for adaptive KV cache management.

---

## 论文详细总结（自动生成）

## 论文总结：从键值缓存学习驱逐策略（KV Policy, KVP）

### 1. 核心问题与整体含义

- **研究背景**：大语言模型（LLM）规模不断增大，自回归解码过程中的键值（Key-Value, KV）缓存对内存的需求成为高效推理的主要瓶颈。
- **现有方法的不足**：已有的 KV 缓存驱逐或压缩方法多依赖启发式指标（如 token 的近期性、历史注意力分数），这些指标只是 token 未来效用的间接代理，既不准确，还会引入额外计算开销。
- **核心问题**：如何直接预测 token 在将来解码中的实际价值，并据此做出更优的缓存驱逐决策，从而在保持生成质量的前提下压缩缓存占用。
- **整体含义**：该工作将 KV 缓存驱逐重新定义为强化学习（RL）问题，探索“学习预测未来效用”这一新范式，为自适应缓存管理提供了可扩展的通用框架。

### 2. 方法论

- **核心思想**：把缓存驱逐看作一个排序问题——学习将 token 按其对未来解码的有用性进行排序，然后驱逐排名最低的 token。作者将这一过程建模为强化学习，不同于以往基于手工规则的启发式方法。
- **技术细节**：
  - 提出 **KV Policy (KVP)** 框架：为每个注意力头训练一个轻量级 RL 智能体。
  - 训练数据：使用**预计算的生成轨迹**（pre-computed generation traces），不需要在线交互或修改底层 LLM。
  - 输入特征：智能体仅使用 KV 缓存中的**键（key）和值（value）向量**，不依赖注意力分数或其他额外特征。
  - 奖励设计：采用一个**整体奖励（holistic reward）**，基于 token 的未来实际效用计算，能够评价所有缓存预算（budget）下的排序质量，从而引导每个智能体学习专门化的驱逐策略。
  - 推理阶段：无需修改底层 LLM 或增加额外推理开销，训练好的智能体直接用于驱逐决策。
- **公式/算法流程**（原文未给出具体公式，以下为文字描述）：
  1. 收集预计算生成轨迹，提取键值向量与对应的未来效用标签；
  2. 为每个注意力头初始化轻量级 RL 智能体；
  3. 以键值向量为状态/特征，以驱逐排序动作为策略，用整体奖励进行策略优化；
  4. 学习完成后，各头智能体在推理时协同决定缓存驱逐。

### 3. 实验设计

- **数据集与基准**：
  - 长上下文基准 **RULER**：支持最多 128K token，用于评估长序列下的缓存管理能力。
  - 多轮对话基准 **OASST2-4k**：评估多轮对话场景下的表现。
  - 零样本下游任务：**BoolQ**、**LongBench passage retrieval**、**GovReport**，用于测试泛化能力。
- **模型族**：在两个不同模型家族上进行了评估（原文未指明具体模型名称）。
- **对比方法**：与“强基线”（strong baselines）对比，但原文未列出具体基线名称（如常见的 H2O、Scissorhands、StreamingLLM 等）。
- **评估维度**：生成质量、缓存内存占用、跨任务与跨长度泛化能力。

### 4. 资源与算力

- 原文摘要及元数据中**未明确说明**使用的 GPU 型号、数量、训练时长或总计算量。
- 仅强调 KVP 是“轻量级”逐头 RL 智能体，且训练基于预计算轨迹，但具体硬件配置与训练成本无从得知。

### 5. 实验数量与充分性

- **实验组数**：摘要中提及的正式评估包括两个模型家族、两个主基准（RULER、OASST2-4k）以及三个零样本下游任务。
- **充分性**：
  - 覆盖了长上下文与多轮对话两类核心场景，并验证了跨任务、跨序列长度的零样本泛化，实验设计较全面。
  - 但原文摘要未提供具体数据表格、消融实验（如奖励设计影响、逐头 vs 共享智能体、不同缓存预算对比等）以及统计显著性信息，因此难以从当前文本完全判断实验的严谨性。
  - 对比的“强基线”未列出名称，削弱了可复现性和公平性评估的透明度。

### 6. 主要结论与发现

- KVP 在长上下文基准和对话基准上均**显著优于强基线**。
- 在零样本测试中，KVP 能够**泛化到训练分布之外的场景和更长的序列长度**，表明其学习到的驱逐策略具有一定通用性。
- 作者认为，“学习预测 token 未来效用”是一种**强大且可扩展的自适应 KV 缓存管理范式**，为未来进一步研究提供了新方向。

### 7. 优点

- **问题重构新颖**：首次将 KV 缓存驱逐显式建模为 RL 排序问题，摆脱启发式依赖。
- **部署友好**：训练过程离线，推理时无需修改 LLM 或增加额外推理开销，实用性强。
- **轻量级设计**：逐头智能体规模小，且仅依赖键值向量，特征获取成本低。
- **奖励设计全面**：整体奖励覆盖所有缓存预算，能引导智能体学习全局最优排序策略。
- **泛化表现好**：零样本实验证明方法可迁移到未见任务和更长序列，说明学到的是较本质的 token 效用表征。

### 8. 不足与局限

- **训练依赖预计算轨迹**：需要提前生成大量高质量轨迹，数据收集成本可能较高。
- **实验细节不透明**：未列出基线名称、具体模型族、消融实验和超参设置，难以独立复现和验证。
- **范围有限**：只验证了两个模型家族和三类下游任务，缺乏对更大规模模型（如 70B+）和更多任务（如代码、数学）的验证。
- **未讨论硬件效率**：尽管智能体轻量，但逐头部署可能引入额外内存或调度开销，原文未作分析。
- **潜在风险**：RL 训练可能存在过拟合于轨迹分布的风险，对未见分布的真实效用预测能力仍需更广泛评估。
- **缺少理论分析**：未对学习到的驱逐策略的最优性或收敛性给出理论保证，目前主要依赖经验结果。

（完）
