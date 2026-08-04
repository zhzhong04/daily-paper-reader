---
title: "Context as a Tool: Context Management for Long-Horizon SWE-Agents"
title_zh: 上下文即工具：面向长周期软件工程智能体的上下文管理
authors: "Shukai Liu, Bo Jiang, Jian Yang, Yizhi Li, Jinyang Guo, Xianglong Liu, Bryan Dai"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.findings-acl.1032.pdf"
tags: ["query:agent-cache"]
score: 4.0
evidence: 面向长周期智能体的主动上下文管理
tldr: 长周期软件工程智能体常因追加式上下文维护或被动压缩导致上下文爆炸、语义漂移和推理退化。本文提出Cat范式，将上下文维护抽象为可调用工具，并设计由稳定任务语义、浓缩长时记忆和高保真短期交互组成的结构化上下文工作区，使智能体能够主动进行压缩与调度。在长周期SWE任务上的实验表明，该方法有效控制上下文增长并提升推理准确度。该工作为智能体工作流中的上下文/缓存管理提供了重要参考，但未直接涉及KV缓存。
source: ACL-2026-Findings
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1032/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 719, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1032/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 798, \"height\": 690, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1032/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1501, \"height\": 1097, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1032/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 825, \"height\": 420, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1032/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 668, \"height\": 400, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1032/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 663, \"height\": 401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-findings/anthology-2026findings-acl1032/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 820, \"height\": 488, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1032/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 642, \"height\": 743, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1032/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1503, \"height\": 1196, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-findings/anthology-2026findings-acl1032/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 680, \"height\": 387, \"label\": \"Table\"}]"
motivation: 长周期智能体因追加式上下文维护导致上下文爆炸和推理退化。
method: 提出Cat范式，将上下文维护工具化并加入智能体决策，使用结构化上下文工作区。
result: 实验显示该方法在长周期SWE任务上提升了推理质量与效率。
conclusion: 主动上下文管理是缓解长周期智能体上下文失稳的有效方式。
---

## Abstract
Agents based on large language models have recently shown strong potential on real-world software engineering (SWE) tasks that require long-horizon interaction with repository-scale codebases. However, most existing agents rely on append-only context maintenance or passively triggered compression heuristics, which often lead to context explosion, semantic drift, and degraded reasoning in long-running interactions. We propose Cat, a new context management paradigm that elevates context maintenance to a callable tool integrated into the decision-making process of agents. Cat formalizes a structured context workspace consisting of stable task semantics, condensed long-term memory, and high-fidelity short-term interactions, and enables agents to proactively compress historical trajectories into actionable summaries at appropriate milestones. To support context management for SWE-agents, we propose a trajectory-level supervision framework, CaT-Generator, based on an offline data construction pipeline that injects context-management actions into complete interaction trajectories. Using this framework, we train a context-aware model, SWE-Compressor. Experiments on SWE-Bench-Verified demonstrate that SWE-Compressor reaches a 57.6% solved rate and significantly outperforms ReAct-based agents and static compression baselines, while maintaining stable and scalable long-horizon reasoning under a bounded context budget.

---

## 论文详细总结（自动生成）

## 论文总结

### 1. 核心问题与整体含义（研究动机与背景）

- **研究背景**：基于大语言模型的智能体在真实世界软件工程（SWE）任务中展现出巨大潜力，这类任务需要智能体与仓库规模的代码库进行长周期（long-horizon）交互（可多达数百轮）。
- **核心问题**：现有大多数智能体依赖**追加式（append-only）上下文维护**（如 ReAct 范式）或**被动触发的压缩启发式**，在长时间运行中常导致：
  - **上下文爆炸**（context explosion）：历史交互不断累积，迅速占满上下文窗口；
  - **语义漂移**（semantic drift）：早期信息被淹没或被噪声干扰；
  - **推理退化**（degraded reasoning）：模型在冗长上下文中难以保持稳定有效的决策。
- **核心论点**：在长周期交互任务中，上下文管理不应是外部强加的约束或后处理步骤，而应被**内化为模型自身的可学习能力**（model capability）。基于此，论文提出 **CAT**（Context as a Tool）范式，将上下文管理提升为与代码编辑、命令执行等环境交互工具同等地位的**可调用、可规划的工具**，使智能体能够主动、动态地管理自身上下文。

### 2. 方法论：核心思想、关键技术细节

#### 2.1 核心思想
CAT 将上下文维护从被动的启发式压缩转变为**主动的、工具化的决策行为**。智能体在每一步生成时，像选择其他外部工具一样，评估是否调用上下文管理工具，从而实现上下文的自适应、动态管理。

#### 2.2 结构化上下文工作区（Structured Context Workspace）
CAT 将上下文建模为三个功能段的统一工作区，在第 t 步的形式化表示为：

```
C(t) = ( Q, M(t), I(k)(t) )
```

- **Q（固定语义锚点）**：不可压缩部分，包括系统提示和关键用户意图，为任务提供稳定的语义锚定。
- **M(t)（长期记忆）**：历史轨迹的高保真浓缩摘要，随推理过程动态更新，存储已完成子任务、尝试过的策略及结果、重要环境反馈、持续约束等。
- **I(k)(t)（短期工作记忆）**：最近 k 步 ReAct 交互的完整记录，保留细粒度的近期环境反馈。

初始化时 C(1) = (Q, ∅, ∅)，随着推理推进，智能体持续更新近期交互与长期摘要，并通过上下文管理工具动态调整 M(t) 的内容与结构。

#### 2.3 上下文管理作为一等工具（First-Class Tool）
- CAT 将上下文管理操作显式建模为**可调用的工具操作**，与文件编辑、命令执行等环境交互工具置于同一决策层级。
- 智能体在以下场景中会**主动触发**上下文管理：
  - 子任务完成、需要阶段性总结时；
  - 轨迹过长、历史压缩对维持运行效率必要时；
  - 后续推理受益于简洁的结构化摘要而非冗长原始日志时。

#### 2.4 CaT-Generator：轨迹级监督框架（两阶段）

**Phase I：基础 ReAct 轨迹生成**
- 部署标准 ReAct 智能体在受控环境中执行完整交互，**禁用上下文管理工具**，仅允许环境相关动作。
- 生成原始轨迹 `Tbase`，保留尽可能多的中间推理、失败模式和环境反馈。

**Phase II：轨迹重构与压缩操作注入**
1. **压缩点位置生成**：基于多类信号识别候选插入位置，包括：
   - 上下文扩展信号（上下文长度持续增长、token 利用率下降）；
   - 结构化边界信号（子任务完成、策略切换、中间里程碑）；
   - 错误修正信号（多次失败后出现新可行方向）。
2. **分段上下文构建**：在候选位置将可见上下文分割为固定段 Q、近期高保真段 I(k)、可压缩历史段。
3. **长期记忆块生成**：调用高容量 LLM（与推理模型同主干）生成结构化长期记忆块 M(ai)，作为压缩工具调用的 Observation。
4. **轨迹拼接与最小侵入注入**：在原始轨迹的关键步骤插入独立的上下文管理工具调用，对应 Observation 为生成的记忆块，保持原始环境交互顺序不变。
5. **拒绝采样微调**：在轨迹级（丢弃未完成任务或不可恢复错误轨迹）和步骤级（过滤压缩行为不合理的轨迹，如频繁调用但信息增益极低、语义漂移严重等）两个层面筛选高质量 SFT 数据。

最终通过在上述 SFT 数据上微调获得 **SWE-Compressor** 模型。

### 3. 实验设计

#### 3.1 评测基准
- **SWE-Bench-Verified**：包含 500 个手工筛选的高质量实例，来自 12 个真实 GitHub 仓库，以 **解决率（solved rate, Pass@1）** 为主要评测指标。

#### 3.2 训练数据
- 从 **SWE-smith** 和 **SWE-ReBench** 两个开源数据集收集原始实例。
- 使用 CaT-Generator 自动生成交互轨迹并经过拒绝采样，得到 **CAT-Instruct**（20k 条 SFT 实例，含上下文管理技能）。
- 额外收集 **BASE-INSTRUCT**（20k 条 SFT 实例，不含上下文管理技能），用于训练基线模型，确保公平对比。

#### 3.3 模型与配置
- 基础模型：**Qwen2.5-Coder-32B**；训练：AdamW 优化器（weight decay 0.01）、余弦学习率调度（warm-up 0.1，峰值学习率 5×10⁻⁵）、最多 3 epochs、上下文长度 65,536 tokens。
- 推理框架：**OpenHands**，可调用工具包括 execute_bash、str_replace_editor、submit 和 context（上下文管理工具）；温度固定为 0.0；评测时最多允许 500 轮交互。

#### 3.4 对比基线
- **ReAct 基线**：无显式上下文管理，上下文窗口耗尽即提前终止。
- **Threshold-Compression 基线**：仅当上下文长度超过预设阈值时触发压缩，压缩方案与 CAT 相同（保留系统提示、关键用户意图和最近 k 条消息，对更早消息进行摘要）。
- 两者均使用与 SWE-Compressor 相同的基础模型和摘要器，在 BASE-INSTRUCT 上 SFT。
- 另外还对比了多种闭源/开源系统（如 GPT-5.1、Claude-3.5-Sonnet、Gemini-2.5-Pro、DeepSeek-R1、Qwen3-Coder-480B 等）。

### 4. 资源与算力

- **论文未明确说明**具体的 GPU 型号、数量、训练时长等算力信息。
- 仅提供了训练超参数（模型规模 32B、训练 3 epochs、批处理相关细节未给出）和推理设置（500 轮交互预算、温度 0.0）。
- 数据量约为 40k SFT 实例（20k CAT-Instruct + 20k BASE-Instruct）。

### 5. 实验数量与充分性

论文共进行了**五组主要实验**：

| 实验 | 目的 |
|------|------|
| 主实验（表 2） | 在 SWE-Bench-Verified 上与多种基线和商业/开源系统对比整体性能 |
| Token 使用分析（图 4） | 分析 CAT 在交互过程中上下文 token 数量的变化趋势与轨迹存活率 |
| 上下文可扩展性对比（图 5） | 在不同交互轮次预算下对比 CAT 与 ReAct 的性能和上下文使用 | 
| 任务难度分层分析（图 6） | 按任务难度（easy/medium/hard）分层对比 CAT 与基线 |
| 交互预算与 token 效率（表 3） | 在不同最大交互步数（150/500）下对比各方法的性能与 token 消耗 |

- **充分性评价**：实验设计较为全面，覆盖了整体性能、上下文效率、可扩展性、难度适应性和消融对比（CAT vs. Base SFT），多角度验证了方法的有效性。
- **公平性**：基线与 CAT 使用相同基础模型、相同 SFT 数据预算和相同推理框架，对比较为公平。但未提供多次运行的方差信息（温度固定为 0，可能方差较小）。

### 6. 主要结论与发现

- **SWE-Compressor 在 SWE-Bench-Verified 上达到 57.6% 的解决率**，在 32B 模型规模的 agent 后训练设定下达到 SOTA，显著优于 ReAct（49.8%）和 Threshold-Compression（53.8%）。
- CAT 有效控制上下文增长：平均上下文 token 数在约 100 轮后稳定在 32k 以下，且保持稳定不持续增长。
- **CAT 具有更好的可扩展性**：随交互预算增大（可达 500 轮），性能持续上升；ReAct 则约在 60 轮后饱和并开始下降。
- 在中等和困难任务上，CAT 的性能提升幅度更大，说明其对复杂长周期推理更有效。
- CAT 在相同交互预算下使用更少的 token，实现了性能与效率的良好平衡。

### 7. 优点

- **方法论创新性强**：将上下文管理从被动启发式提升为主动的、可调用的工具，为长周期 agent 的上下文管理提供了新范式。
- **结构化上下文设计合理**：固定语义锚点 + 浓缩长期记忆 + 高保真短期记忆的三段式设计，兼顾任务稳定性与细粒度信息保留。
- **训练框架完整**：CaT-Generator 提出两阶段离线轨迹重构管线，实现了轨迹级监督，使模型不仅学会何时压缩、如何压缩，还能学习压缩结果如何影响后续推理。
- **实验验证充分**：通过多角度分析（token 效率、交互预算扩展、难度分层、消融）系统验证了方法的有效性。
- **代码与数据可复现性强**：使用公开数据集（SWE-Bench-Verified、SWE-smith、SWE-ReBench）和开源基础模型。

### 8. 不足与局限

- **压缩时机的监督信号为启发式**：CaT-Generator 通过上下文增长、阶段边界等启发式信号选择压缩位置，可能不是全局最优，缺乏最小化工具调用或最大化信息增益的原则性目标函数。
- **摘要信息保真度缺乏验证**：CAT 依赖 LLM 生成的长期记忆块，但未包含显式验证机制来检测压缩记忆中的幻觉、遗漏或不一致，也未量化摘要误差在数百轮交互中的累积效应。
- **实验范围有限**：主要在 SWE-Bench-Verified 单一基准上评估，缺乏在更广泛任务类型（如 Web 导航、深度研究等）上的泛化验证，跨领域的适用性有待考察。
- **未涉及 KV 缓存优化**：方法的定位是上下文管理（通过文本摘要控制上下文规模），并未直接讨论或利用 KV 缓存机制。从系统效率角度看，压缩操作本身也需额外计算代价，论文未对此进行成本分析。
- **资源消耗未透明公开**：论文未报告训练所需的具体算力（GPU 数量、训练时间等），不利于复现和成本评估。
- **性能对比的局限性**：虽然与多种商业系统对比具有参考价值，但由于不同商业模型版本迭代快，且论文方法使用 32B 参数模型（与部分商业模型规模差距大），性能对比的意义主要在于证明方法的竞争力而非直接可比性。

---

（完）
