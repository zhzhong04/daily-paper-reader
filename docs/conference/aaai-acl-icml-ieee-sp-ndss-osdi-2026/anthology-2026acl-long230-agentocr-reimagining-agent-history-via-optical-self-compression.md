---
title: "AgentOCR: Reimagining Agent History via Optical Self-Compression"
title_zh: AgentOCR：通过光学自压缩重塑智能体历史
authors: "Lang Feng, Fuchao Yang, Feng Chen, Xin Cheng, Haiyang Xu, Zhenglin Wan, Ming Yan, Bo An"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.230.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 面向智能体历史的段式光学缓存，消除多轮工作流中的重复渲染
tldr: 基于RL的多轮智能体系统常常因文本历史快速增长而产生高昂的令牌和内存开销。本文提出AgentOCR，利用视觉令牌的高信息密度，将累积的观测-动作历史渲染为紧凑图像，并设计段式光学缓存，将历史分解为可哈希段并维护视觉缓存，消除冗余重复渲染。进一步引入智能体自压缩，让智能体主动发出压缩率。该方法有效降低多轮扩展成本，提升部署效率。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1584, \"height\": 771}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1586, \"height\": 767}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 807, \"height\": 588}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 988, \"height\": 2020}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 977, \"height\": 2004}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1651, \"height\": 532}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1657, \"height\": 588}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1502, \"height\": 245}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 794, \"height\": 353}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 808, \"height\": 547}]"
motivation: LLM智能体多轮交互历史膨胀导致令牌和内存成本激增。
method: 用渲染图像表示历史，提出段式光学缓存和自压缩机制。
result: 有效消除冗余渲染，降低令牌和内存开销。
conclusion: AgentOCR为可扩展多轮智能体提供高效历史压缩方案。
---

## Abstract
Recent advances in large language models (LLMs) enable agentic systems trained with reinforcement learning (RL) over multi-turn interaction, but practical deployment is bottlenecked by rapidly growing textual histories that inflate token and memory costs. We introduce AgentOCR, a framework that exploits visual tokens’ superior information density by representing the accumulated observation-action history as a compact rendered image. To make multi-turn rollouts scalable, AgentOCR proposes segment optical caching. By decomposing history into hashable segments and maintaining a visual cache, this mechanism eliminates redundant re-rendering. Beyond fixed rendering, AgentOCR introduces agentic self-compression, where the agent actively emits a compression rate and is trained with compression-aware reward to adaptively balance task success and token efficiency. We conduct extensive experiments on challenging agentic benchmarks, ALFWorld and search-based QA. Remarkably, AgentOCR preserves over 95% of text-based agent performance while substantially reducing token consumption (>50%), yielding consistent token and memory efficiency. Further analysis validates a 20 × rendering speedup from optical caching and effective self-compression balancing. Our code is available at https://github.com/langfengQ/AgentOCR.

---

## 论文详细总结（自动生成）

# AgentOCR 论文详细总结

## 1. 核心问题与研究动机

- **背景**：大语言模型（LLM）的进步使得基于强化学习（RL）的多轮交互智能体系统成为可能，但实际部署面临严重瓶颈。
- **核心问题**：在长时间多轮交互中，智能体必须不断累积历史观测与动作序列，导致上下文文本令牌数量迅速膨胀，带来：
  - 超出有限上下文窗口；
  - 注意力预填充（prefill）和 KV-cache 管理的推理延迟与计算成本剧增；
  - 内存占用持续增长。
- **关键洞察**：视觉令牌（visual tokens）具有比文本更高的信息密度（如 DeepSeek-OCR 所示将文本渲染为图像可实现约 10× 压缩），因此可以将智能体的历史记录以“文本作为图像”的形式进行视觉化压缩，从而大幅降低令牌开销。
- **整体意义**：提出一种“光学记忆”（optical memory）方式重新定义智能体历史，使得高密度视觉表示能够支持严格的智能体推理，同时显著降低资源消耗，向资源高效、可扩展的多轮智能体迈进一步。

## 2. 方法论

### 2.1 核心思想
- 将累计的观测-动作历史渲染为紧凑图像，智能体基于视觉历史进行策略决策；
- 通过“段式光学缓存”（Segment Optical Caching）消除多轮渲染中的重复计算；
- 通过“智能体自压缩”（Agentic Self-Compression）让智能体主动调节视觉压缩率，实现任务成功与令牌效率的动态平衡。

### 2.2 光学记忆编码（Optical Memory Encoding）
- 维护外部记忆缓冲区 `M_t`，存储交互记录（observation-action 对）；
- 使用确定性渲染器 `R(h_t; ψ)` 将文本历史渲染为 RGB 图像 `I_t`；
- 智能体策略为视觉-语言策略：`a_t ~ π_θ(·|I, I_t)`；
- 渲染超参数 `ψ` 包括字体、字号、颜色、留白、图像宽高等。

### 2.3 段式光学缓存（Segment Optical Caching）
- 将完整历史 `h_t` 分割为独立文本段 `Split(h_t) = (ℓ_1, ..., ℓ_K)`；
- 维护按内容哈希索引的每 episode 缓存 `C(e) = {(k(ℓ), I(ℓ))}`；
- 缓存命中直接复用图像；未命中则渲染并插入缓存；
- 最终通过垂直堆叠所有段图像得到完整光学记忆图像：`I_t = Stack(I(ℓ_{t,i}))`；
- **复杂度优势**：每步渲染成本只与未命中段数 `U_t` 相关（通常 `U_t << K_t`）而非全历史长度；空间复杂度由唯一段数量决定，避免每步重复存储完整图像。

### 2.4 智能体自压缩（Agentic Self-Compression）
- **压缩决策**：智能体通过结构化标签 `<compression> c_t </compression>` 输出压缩因子 `c_t ≥ 1`，作用于渲染图像；
- 图像尺寸缩放公式：  
  `size(I_{t+1}) = (⌊H_{t+1}/√c_t⌋, ⌊W_{t+1}/√c_t⌋)`，从而减少视觉令牌数；
- **压缩感知奖励**：
  - 仅在 episode 成功时给予压缩奖励：`r_comp^t = ln(c_t)`（若 `Isucc(τ)=1`），否则为 0；
  - 总奖励为 `\tilde{r}_t = r_t + λ·r_comp^t`；
  - 采用**间歇式奖励注入**（每 K 次训练迭代注入一次压缩奖励，`K=5`），避免智能体过度贪婪地追求压缩而损害任务表现；
- 使用 GRPO 等 RL 优化器训练策略（公式见原论文 Eq. (2)）。

### 2.5 算法流程（伪代码概要）
- **环境包装器**：负责物理环境步进、更新记忆、Split 历史、查缓存/渲染、堆叠图像、按压缩率 Resize、计算压缩感知奖励（仅在成功且间歇性注入）。
- **策略 rollout**：智能体根据图像和历史生成动作与环境动作，同时解析 `<compression>` 标签得到压缩率，执行步骤并存储 transition，训练阶段用 RL 更新策略。

## 3. 实验设计

### 3.1 数据集 / 场景
- **ALFWorld**（具身任务）：模拟家庭环境，包含 3827 个任务，覆盖六个子任务：Pick & Place、Look、Clean、Heat、Cool、Pick2 & Place；每 episode 最多 50 步。
- **Search-based QA**（搜索式问答）：采用 Search-R1 的 QA 数据集，包含：
  - 单跳任务：NQ、TriviaQA、PopQA；
  - 多跳任务：HotpotQA、2WikiMultiHopQA、MuSiQue、Bamboogle；
  - 智能体通过 E5 检索器从知识库检索 top-3 文档，最多 4 步查询交互。

### 3.2 对比方法
- **Text (w/o RL)**：纯文本历史 + 文本模型；
- **OCR (w/o RL)**：光学记忆图像 + VLM（无 RL）；
- **Text + GRPO**：原始文本历史 + GRPO RL 训练；
- **AgentOCR**：光学记忆 + GRPO（本文方法）。

### 3.3 模型与实现细节
- 骨干模型：Qwen2.5-VL-3B/7B-Instruct（光学变体），Qwen2.5-3B/7B-Instruct（文本变体）；
- 所有方法保持相同训练设置与超参数；
- AgentOCR 超参数：`λ=0.01`，`K=5`；
- 文本上下文最大长度：ALFWorld 5120 tokens，Search QA 14000 tokens；光学历史对应 2048 和 4096 tokens；
- 最大响应长度 512 tokens，学习率 1e-6，rollout 温度 1.0（验证时分别 0.4 / 0.0）。

## 4. 资源与算力

- 论文明确说明：
  - Qwen2.5-VL-3B 实验：2×H100 GPU；
  - Qwen2.5-VL-7B 实验：4×H100 GPU；
- 训练轮数：总共 150 次迭代；
- 其他细节：ALFWorld rollout 16 samples/iteration，每个 sample 8 条轨迹；Search QA 128 samples/iteration，每个 sample 8 条轨迹；mini-batch 256，无 KL 损失。

## 5. 实验数量与充分性

- **主要实验**：两个 benchmark（ALFWorld 与 Search-based QA），两个模型尺寸（3B、7B），对比四种方法（Text w/o RL、OCR w/o RL、Text+GRPO、AgentOCR），在 ALFWorld 有 6 个子任务细粒度结果，Search 有 7 个子数据集结果。
- **压缩分析实验**：在不同压缩因子（1.0~2.0）下考察相对性能与令牌节省率，识别“鲁棒压缩区间”。
- **缓存机制消融**：对比 no cache、naive cache、segment cache（3 组），报告渲染时间、增长速度、峰值内存、内存节省。
- **自压缩消融**：无 RL、有 RL 但不同奖励间隔（K=1、K=5），以及是否有自压缩（共 5 配置），报告成功率和视觉令牌数。
- **案例研究**：展示 HotpotQA 上的完整轨迹，说明自压缩率动态选择。

**充分性评价**：
- 实验覆盖多个维度的消融，包括缓存、自压缩、压缩因子、模型规模、任务类型，较为系统。
- 对比公平：保持骨干模型同族、设置一致，基线与 RL 变体齐全。
- 不足：仅在两个 benchmark 上评估，未覆盖更广泛的 GUI、网页、多模态环境；未跨不同 VLM 架构进行比较；部分实验仅使用 3B 模型（自压缩消融），未报告 7B 上的对应结果。

## 6. 主要结论与发现

- **性能保持**：AgentOCR 在 ALFWorld 上（3B/7B）达到 78.2%/81.2%，与 Text+GRPO（79.9%/81.8%）几乎持平；Search QA 上保留超过 95% 的性能（7B：40.1% vs 41.9%）。
- **令牌减少显著**：平均令牌消耗减少超过 50%（ALFWorld 约 55–62%，Search 约 51–57%），峰值令牌可减少高达 80.9%。
- **缓存加速**：段式光学缓存较无缓存渲染加速 20.79×，较 naive cache 提升约 3.5 倍；峰值内存较 naive cache 节省 26.82%，且时间增长为负（-1.23 ms/step），表明随着缓存预热，渲染需求反而减少。
- **自压缩有效**：间歇奖励（K=5）下，智能体学习到适度压缩（平均 ct=1.28），将平均视觉令牌从 458.1 降至 381.7，同时成功率达 78.2%（接近未压缩的 78.5%）；而密集奖励（K=1）会导致过度压缩（ct=4.91）使成功率暴跌至 45.3%。
- **静态压缩存在阈值**：压缩因子约 1.2 时可保持 95% 以上性能与约 50-55% 令牌节省，超过此阈值则性能加速衰减；不同任务敏感性差异大（ALFWorld 对压缩鲁棒，Search 对文本细节敏感）。

## 7. 优点与亮点

- **新颖的视角**：将历史记录视为“光学记忆”，利用视觉令牌高信息密度，突破文本上下文的效率瓶颈。
- **工程上可行**：段式光学缓存基于内容哈希，简单高效，显著消除重复渲染，且缓存空间随唯一段数而非步数增长。
- **智能化压缩**：将压缩率作为动作之一，通过 RL 学习自适应权衡，并设计间歇奖励避免贪婪压缩，机制可迁移到不同 RL 算法。
- **实验完备性**：同时验证了性能、令牌效率、渲染速度、内存占用、压缩因子敏感性和自压缩行为，提供了深入且多角度的分析。
- **算法无关性**：框架兼容多种智能体 RL 优化器（如 GRPO），易于推广。
- **开放源码**：公开代码，便于复现。

## 8. 不足与局限

- **模型架构局限**：仅使用 Qwen2.5-VL，未验证 DeepSeek-OCR 等不同视觉 tokenizer 或 patch 分辨率的 VLM；不同视觉编码器的归纳偏置可能影响性能与压缩效率。
- **渲染参数未系统探索**：字体大小、行距、颜色、分辨率等固定，未研究这些选择对下游推理的影响。
- **历史类型受限**：当前假设历史主要是文本内容（可渲染为文字图像）；未覆盖 GUI 截图、科学图表、复杂表格等固有视觉元素的多模态历史。
- **任务覆盖有限**：仅在具身和搜索问答两个 benchmark 验证，缺乏 GUI 控制、网页交互、长程复杂规划等更多场景的评估。
- **部分消融规模较小**：自压缩消融仅在 3B 模型上进行，未在 7B 或更大模型上验证。
- **性能差距风险**：在 search QA 上相对 Text+GRPO 仍损失约 2-5% 性能（7B：40.1% vs 41.9%；3B：34.2% vs 36.4%），压缩在复杂文本推理任务上存在固有精度损失。
- **未讨论实际 KV-cache 内存与推理延迟端到端收益**：实验重点在令牌数和渲染时间，未给出整体系统级 latency/throughput 对比。

（完）
