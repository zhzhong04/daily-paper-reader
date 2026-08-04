---
title: "AgentOCR: Reimagining Agent History via Optical Self-Compression"
title_zh: 智能体光学自压缩：重塑智能体历史
authors: "Lang Feng, Fuchao Yang, Feng Chen, Xin Cheng, Haiyang Xu, Zhenglin Wan, Ming Yan, Bo An"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.230.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 面向智能体历史的分段光学缓存机制，属于智能体缓存机制
tldr: 大语言模型智能体系统在长程交互中面临历史文本膨胀导致的token和内存开销问题。本文提出AgentOCR，利用视觉token的高信息密度，将观测-行动历史渲染为紧凑图像，并设计分段光学缓存机制，按可哈希分段管理视觉缓存，避免重复渲染。实验结果验证了该框架能显著降低智能体历史存储与计算成本，为大规模多轮交互训练提供可扩展的缓存方案。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1584, \"height\": 771, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1586, \"height\": 767, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 807, \"height\": 588, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 988, \"height\": 2020, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 977, \"height\": 2004, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1651, \"height\": 532, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1657, \"height\": 588, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1502, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 794, \"height\": 353, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 808, \"height\": 547, \"label\": \"Table\"}]"
motivation: 智能体系统多轮交互的历史记录快速膨胀，导致token与存储成本成为大规模训练的瓶颈。
method: 提出视觉自压缩与分段光学缓存，将历史渲染成紧凑图像并按可哈希分段维护缓存，同时让智能体主动发射压缩率。
result: 实验表明该框架显著降低历史存储和渲染开销，支持更长的多轮训练轨迹。
conclusion: 光学自压缩与分段缓存为智能体历史管理提供了全新高效的范式。
---

## Abstract
Recent advances in large language models (LLMs) enable agentic systems trained with reinforcement learning (RL) over multi-turn interaction, but practical deployment is bottlenecked by rapidly growing textual histories that inflate token and memory costs. We introduce AgentOCR, a framework that exploits visual tokens’ superior information density by representing the accumulated observation-action history as a compact rendered image. To make multi-turn rollouts scalable, AgentOCR proposes segment optical caching. By decomposing history into hashable segments and maintaining a visual cache, this mechanism eliminates redundant re-rendering. Beyond fixed rendering, AgentOCR introduces agentic self-compression, where the agent actively emits a compression rate and is trained with compression-aware reward to adaptively balance task success and token efficiency. We conduct extensive experiments on challenging agentic benchmarks, ALFWorld and search-based QA. Remarkably, AgentOCR preserves over 95% of text-based agent performance while substantially reducing token consumption (>50%), yielding consistent token and memory efficiency. Further analysis validates a 20 × rendering speedup from optical caching and effective self-compression balancing. Our code is available at https://github.com/langfengQ/AgentOCR.

---

## 论文详细总结（自动生成）

## 论文详细中文总结

### 1. 核心问题与整体含义（研究动机与背景）

- **核心问题**：基于大语言模型（LLM）的智能体系统在多轮交互过程中需要持续缓存和累积历史观测—行动记录，导致输入上下文迅速膨胀，造成严重的 **token消耗** 与 **内存开销** 问题，制约了基于强化学习（RL）的长程智能体训练与部署的可扩展性。
- **关键观察**：视觉token（如DeepSeek-OCR等研究所揭示）相比文本token具有更高的信息密度，将文本渲染为图像可将token占用压缩约10倍。
- **研究含义**：本文提出 **AgentOCR** 框架，将智能体的交互历史从"纯文本字符串"重新构想为"动态图像序列"，利用视觉token的高信息密度来压缩历史表示，为大规模多轮智能体训练提供了一种全新的、可扩展的缓存机制与效率范式。

---

### 2. 方法论：核心思想、关键技术细节与算法流程

#### 2.1 总体思想

AgentOCR摒弃传统文本历史输入方式，将智能体的观测—行动历史渲染为一张紧凑的图像，并让视觉语言模型（VLM）基于该光学记忆进行多轮决策，从而大幅降低token消耗。

#### 2.2 光学记忆编码（Optical Memory Encoding）
- 维护一个外部**记忆缓冲区** Mt，存储截至第 t 步的交互记录（观测—行动对）。
- 定义一个确定性的**渲染器 R**，将文本历史 ht 映射为RGB图像 It = R(ht; ψ)，其中 ψ 为渲染超参数（字体、颜色、图像尺寸等）。
- 智能体策略建模为**视觉语言策略**：at ∼ πθ(· | I, It)，即依据任务指令与历史图像采样行动。

#### 2.3 分段光学缓存（Segment Optical Caching）
- **动机**：每一步从头渲染全量历史代价过高，是延迟瓶颈。
- **分段表示**：将历史上下文切分为独立文本段 Split(h) = (ℓ1, ..., ℓK)。
- **内容键缓存**：按环境实例维护一个以内容哈希 k(ℓ) 为键、以段渲染图像 I(ℓ) 为值的缓存字典 C(e) = {(k(ℓ), I(ℓ))}。
- **查缓存与组装**：每一步先对段做哈希查询；缓存命中则直接取图，缓存缺失则渲染并存入缓存；最后将各段图像按顺序**垂直拼接**为完整光学记忆图像 It = Stack(I(ℓt,1), ..., I(ℓt,Kt))。
- **复杂度优势**：渲染成本为 O(Ut)（Ut 为缓存未命中段数），通常 Ut ≪ Kt；空间复杂度为 O(|C(e)|) 张唯一段图像，而非 O(T) 张全历史图像。

#### 2.4 智能体自压缩（Agentic Self-Compression）
- **压缩决策**：将渲染器暴露为一个可执行工具，策略通过结构化标签 `<compression>ct</compression>` 主动选择压缩因子 ct ≥ 1。
- **空间下采样**：图像按 size(It+1) = (⌊Ht+1/√ct⌋, ⌊Wt+1/√ct⌋) 缩放到新尺寸，从而减少视觉token数量。
- **压缩感知奖励**：
  - r_comp_t = ln(ct)（若回合成功 Isucc(τ)=1），否则为 0；
  - 总奖励 ˜rt = rt + λ·r_comp_t，其中 λ 控制任务性能与压缩效率的权衡；
  - 采用**间歇式奖励调度**：仅在每 K 次训练迭代注入压缩奖励，避免智能体过度贪婪地追求压缩而损害任务性能。

#### 2.5 RL 训练流程
- 以 **GRPO（Group Relative Policy Optimization）** 为代表算法，优化带裁剪的替代目标函数（Eq. 2）。
- 算法流程（Algorithm 1 & 2）：
  1. 环境执行动作 at，返回新观测与奖励；
  2. 更新记忆，对历史分段、查缓存/渲染/拼接，得到光学记忆图像；
  3. 按压缩因子 ct 缩放图像；
  4. 计算压缩奖励并注入总奖励；
  5. 策略生成下一步动作与新的压缩因子，循环直至回合结束。

---

### 3. 实验设计

#### 3.1 数据集与基准（Benchmark）
| 基准 | 特点 | 任务类型 |
|---|---|---|
| **ALFWorld** | 长程具身决策，3,827 个任务 | 6 类家务任务：Pick & Place、Look（光照检查）、Clean、Heat、Cool、Pick2 & Place |
| **Search-based QA**（Search-R1 数据集） | 文本密集的多轮工具调用与信息检索 | 单跳 QA（NQ、TriviaQA、PopQA）+ 多跳 QA（HotpotQA、2WikiMultiHopQA、MuSiQue、Bamboogle） |

#### 3.2 对比方法（Baselines）
- **Text (w/o RL)**：文本历史输入，无RL的纯文本模型；
- **OCR (w/o RL)**：光学记忆图像输入，无RL的VLM；
- **Text + GRPO**：直接对原始文本上下文做RL的强基线；
- **AgentOCR**：光学记忆 + GRPO 强化学习训练。

#### 3.3 模型配置
- 文本模型：Qwen2.5-3B/7B-Instruct；
- 视觉模型：Qwen2.5-VL-3B/7B-Instruct；
- 控制变量：各方法保持相同的训练设置与超参数。

---

### 4. 资源与算力

- 实验使用 **H100 GPU**：
  - Qwen2.5-VL-**3B** 模型（ALFWorld 和 search-based QA）：**2×H100**；
  - Qwen2.5-VL-**7B** 模型：**4×H100**；
- 训练总时长：**150 次迭代（iterations）**；
- 其他配置：学习率 1e-6，GRPO组大小 8，ALFWorld 最大每回合 50 步，search-based QA 最大 4 步；
- 论文未详细报告训练的总墙钟时间、能耗等更细粒度的算力统计。

---

### 5. 实验数量与充分性

论文开展了**四组主要实验**，覆盖面较全面：

1. **主实验（Table 1 & 2）**：在 ALFWorld 6 类子任务 + search-based QA 7 个子数据集上，对比 3B/7B 两种规模下的 4 种方法（Text、OCR、Text+GRPO、AgentOCR），报告成功率/精确匹配分数与 token 成本；
2. **视觉—文本压缩分析（Figure 3）**：在 7B 模型上扫描压缩因子 ct ∈ [1.0, 2.0]，分析 token 节省与任务性能的非线性权衡曲线；
3. **缓存机制消融（Table 3）**：对比 No Cache、Naive Cache、AgentOCR 分段光学缓存，从渲染延迟、增长速度、峰值内存、内存节省等维度评估；
4. **自压缩机制消融（Table 4）**：在 3B 模型上拆解"无RL/有RL"×"无自压缩/有自压缩"，并分析密集奖励（K=1）与间歇奖励（K=5）的差异；
5. **案例研究（Case Study）**：展示 HotpotQA 上多轮交互轨迹与自适应压缩行为。

**充分性评估**：
- **优点**：实验覆盖两种差异明显的任务类型（具身决策 vs 文本密集检索）、两种模型规模、多种基线与消融组合，证据链条完整，能较好地支撑核心论点；
- **不足**：未见对更多VLM架构（如DeepSeek-OCR）的跨模型验证；未对渲染参数敏感性做系统扫描；渲染成本与端到端训练总开销的对比未量化。

---

### 6. 主要结论与发现

1. **性能保持**：AgentOCR 在 ALFWorld 上（3B: 78.2%、7B: 81.2%）与文本 Agent（79.9%、81.8%）差距约 1%；在 search-based QA 上保留 Text+GRPO 基线 95% 以上的性能（7B: 40.1% vs 41.9%）；
2. **Token 大幅削减**：平均 token 消耗减少 **50.7%–61.7%**，峰值 token 最高减少 **80.9%**；
3. **渲染加速**：分段光学缓存相比无缓存方案实现 **20.79× 渲染加速**，相比朴素缓存还额外节省 **26.82% 峰值缓存内存**；
4. **静态压缩存在权衡瓶颈**：固定压缩因子在 ~55% token 节省内可保持 95%+ 性能，但继续压缩会引发非线性性能崩塌；
5. **智能体自压缩有效**：通过间歇奖励调度（K=5），智能体学习到温和的压缩策略（平均 ct=1.28），在几乎不掉点的情况下进一步减少视觉 token（458.1 → 381.7）；
6. **RL 是自压缩生效的关键**：无RL时模型学不会调节压缩率；密集压缩奖励（K=1）会导致过度压缩（ct=4.91）与性能暴跌（45.3%）。

---

### 7. 优点

- **视角新颖**：将"文本转图像"的 OCR 思想引入智能体历史管理，提出"光学记忆"概念，开辟了智能体上下文压缩的新方向；
- **方案系统性**：从渲染编码、缓存加速到RL训练形成了完整闭环，不是单一技巧的堆叠；
- **缓存设计精巧**：分段级、内容哈希的缓存机制既能复用重复内容，又能控制缓存内存随唯一段数而非步数增长，兼具时间与空间效率；
- **自压缩机制有洞察力**：让智能体自主决定压缩率，并设计"压缩奖励仅在成功回合生效 + 间歇式奖励注入"的机制，有效抑制贪婪压缩行为，体现了对RL训练动态的深入理解；
- **实验证据质量较高**：多维度的消融（缓存、压缩、RL调度）清楚分离了各组件贡献，分析扎实；
- **写作清晰**：算法伪代码、渲染参数和Prompt模板全部公开，可复现性强；
- **开源**：代码已在 GitHub 公开。

---

### 8. 不足与局限

- **VLM 泛化性有限**：仅验证了 Qwen2.5-VL 系列；未测试 DeepSeek-OCR、Qwen3-VL 等其他视觉 tokenizer/编码策略下的表现，结果可能受特定视觉编码器归纳偏置影响；
- **渲染超参数未系统分析**：字体大小、行距、颜色等固定配置对下游推理的敏感性未探索，次优渲染可能损害文本可读性与布局理解；
- **应用场景局限**：当前仅支持以文本为主的历史（观测、行动、工具输出）；GUI 截图、科学图表、复杂表格等固有视觉元素的混合模态历史尚未覆盖；
- **文本压缩比未充分拆解**：">50% token 减少"是对比文本代理的端到端结果，但文本 token 与视觉 token 的准确换算关系在不同配置下可能变化，缺乏更细粒度的报告；
- **未见更极限的规模验证**：未在更大模型（如 14B/72B）或不一致上下文（如数百轮）下测试，长尾扩展性证据有限；单一看似"高信息密度"并未量化任务成功对视觉细节的真实需求，任务场景偏窄；
- **资源成本未完整披露**：未报告训练总墙钟时间、渲染的CPU/GPU占用比率、完整端到端能效对比等，对"Green AI"主张的量化支撑不够完整。

---

（完）
