---
title: "AgentOCR: Reimagining Agent History via Optical Self-Compression"
title_zh: AgentOCR：通过光学自压缩重塑智能体历史
authors: "Lang Feng, Fuchao Yang, Feng Chen, Xin Cheng, Haiyang Xu, Zhenglin Wan, Ming Yan, Bo An"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.230.pdf"
tags: ["query:agent-cache"]
score: 4.0
evidence: 面向智能体历史压缩的分段光学缓存
tldr: 多轮交互的智能体系统因文本历史快速膨胀而受限于token和内存成本。AgentOCR将累积的观察-动作历史渲染为信息密度更高的紧凑图像，并提出分段光学缓存：将历史分解为可哈希段并维护视觉缓存，消除重复渲染。进一步引入智能体自压缩，让智能体主动选择压缩率。实验表明该方法显著降低多轮训练的开销。该工作提供了一种面向智能体历史的高效缓存方案，但针对的是视觉缓存而非KV缓存。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1584, \"height\": 771, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1586, \"height\": 767, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 807, \"height\": 588, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 988, \"height\": 2020, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long230/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 977, \"height\": 2004, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1651, \"height\": 532, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1657, \"height\": 588, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1502, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 794, \"height\": 353, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long230/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 808, \"height\": 547, \"label\": \"Table\"}]"
motivation: 多轮智能体历史快速膨胀，token与内存开销高。
method: 将历史渲染为图像，用分段可哈希缓存和智能体主动压缩降低冗余。
result: 实验表明显著减少重渲染开销和内存占用。
conclusion: 光学分段缓存可为大规模多轮智能体训练提供可扩展记忆管理。
---

## Abstract
Recent advances in large language models (LLMs) enable agentic systems trained with reinforcement learning (RL) over multi-turn interaction, but practical deployment is bottlenecked by rapidly growing textual histories that inflate token and memory costs. We introduce AgentOCR, a framework that exploits visual tokens’ superior information density by representing the accumulated observation-action history as a compact rendered image. To make multi-turn rollouts scalable, AgentOCR proposes segment optical caching. By decomposing history into hashable segments and maintaining a visual cache, this mechanism eliminates redundant re-rendering. Beyond fixed rendering, AgentOCR introduces agentic self-compression, where the agent actively emits a compression rate and is trained with compression-aware reward to adaptively balance task success and token efficiency. We conduct extensive experiments on challenging agentic benchmarks, ALFWorld and search-based QA. Remarkably, AgentOCR preserves over 95% of text-based agent performance while substantially reducing token consumption (>50%), yielding consistent token and memory efficiency. Further analysis validates a 20 × rendering speedup from optical caching and effective self-compression balancing. Our code is available at https://github.com/langfengQ/AgentOCR.

---

## 论文详细总结（自动生成）

# AgentOCR 论文详细中文总结

## 1. 论文的核心问题与整体含义

- **研究动机**：近年来，基于大语言模型（LLM）的智能体系统通过多轮交互进行强化学习（RL）训练取得了显著进展。然而，在实际部署中，智能体需要在多轮决策循环中缓冲完整的轨迹历史（观察与动作序列），导致输入上下文以文本 token 形式迅速膨胀。这带来两大核心瓶颈：
  - **token 预算耗尽**：超长上下文迅速触及现有 LLM 的上下文窗口上限；
  - **计算成本高昂**：注意力 prefill 与 KV-cache 管理的开销随序列长度呈超线性增长。
- **核心含义（核心贡献）**：论文提出 **AgentOCR** 框架，将智能体的交互历史从"文本字符串"重新构想为"动态图像序列"，利用**视觉 token 的信息密度优势**（参考 DeepSeek-OCR，视觉模态比文本 token 可压缩约 10 倍）实现高效的历史表示，从而从根本上缓解多轮智能体系统中的 token 与内存成本瓶颈。

## 2. 论文提出的方法论

### 2.1 光学记忆编码（Optical Memory Encoding）
- 维护外部记忆缓冲器 \( M_t \)，存储交互记录（观察-动作对）。
- 定义确定性渲染器 \( R \)，将文本化历史 \( h_t = \text{Fetch}(M_{t-1}) \) 渲染为 RGB 图像 \( I_t = R(h_t; \psi) \)，其中 \( \psi \) 为渲染超参数（字体、颜色、边距、分辨率等）。
- 多模态策略 \(\pi_\theta(\cdot | I, I_t)\) 同时接收任务指令 \( I \) 与历史图像 \( I_t \) 来采样动作。

### 2.2 分段光学缓存（Segment Optical Caching）
- **问题**：每次从零重新渲染整个历史 → 延迟高、冗余计算多。
- **核心方案**：
  - 将历史上下文拆分为独立文本段 \(\text{Split}(h_t) = (\ell_{t,1}, \ldots, \ell_{t,K_t})\)；
  - 建立逐回合缓存 \( C^{(e)} = \{(k(\ell), I(\ell))\} \)，键为段的哈希值；
  - **缓存命中**时直接取用已渲染图像；**缓存未命中**时渲染并插入缓存（见原文 Eq. 4-5）；
  - 最终通过垂直堆叠段图像构建完整光学记忆：\( I_t = \text{Stack}(I(\ell_{t,i}))_{i=1}^{K_t} \)（Eq. 6）。
- **复杂度优势**：缓存命中仅需字典查找与图像堆叠，渲染开销降为 \( O(U_t) \)（\( U_t \) 为未命中段数），空间复杂度由 \( O(T) \) 张全历史图像降为 \( O(|C^{(e)}|) \) 张唯一段图像。
- **与朴素缓存（naive cache）的对比**：朴素缓存只增不减地累积渲染像素，空间仍随 rollout 长度线性增长；分段缓存按内容去重，同时降低时间和空间开销。

### 2.3 智能体自压缩（Agentic Self-Compression）
- **压缩决策**：将渲染器暴露为可执行工具，策略通过 `<compression> c_t </compression>` 结构化标签输出压缩因子 \( c_t \geq 1 \)，对渲染图像进行空间下采样：
  \[
  \text{size}(I_{t+1}) = \left( \left\lfloor \frac{H_{t+1}}{\sqrt{c_t}} \right\rfloor, \left\lfloor \frac{W_{t+1}}{\sqrt{c_t}} \right\rfloor \right) \quad \text{(Eq. 7)}
  \]
  压缩因子越大，视觉 token 数越少。
- **压缩感知奖励（Compression-aware Reward）**：
  - 奖励仅在回合成功时给予：\( r_t^{\text{comp}} = \ln(c_t) \) 若 \( I_{\text{succ}}(\tau)=1 \)，否则为 0（Eq. 8）；
  - 总奖励 \( \tilde{r}_t = r_t + \lambda r_t^{\text{comp}} \)，\(\lambda\) 控制任务性能与压缩效率的权衡；
  - 采用**间歇式强化调度**（每 \( K \) 个训练迭代注入一次压缩奖励，实验中默认 \( K=5 \)），防止智能体因贪婪追求压缩奖励而过度压缩导致性能崩溃。
- **训练算法**：兼容任意智能体 RL 算法，论文以 GRPO 为代表，给出裁剪替代目标（Eq. 2）。

## 3. 实验设计

### 3.1 数据集与场景
| Benchmark | 类型 | 特征 |
|---|---|---|
| ALFWorld | 具身任务（模拟家庭环境） | 长视野决策，6 类子任务（Pick & Place、Look、Clean、Heat、Cool、Pick2 & Place） |
| Search-based QA | 多轮工具使用与检索问答 | 检索文本密度高，分为单跳（NQ、TriviaQA、PopQA）与多跳（HotpotQA、2Wiki、MuSiQue、Bamboogle） |

### 3.2 对比方法
1. **Text (w/o RL)**：原始文本历史 + 文本模型，无 RL；
2. **OCR (w/o RL)**：光学历史图像 + VLM，无 RL；
3. **Text + GRPO**：原始文本历史 + GRPO 强化学习（强基线）；
4. **AgentOCR**（本文）：光学历史 + GRPO，支持自压缩。

### 3.3 模型配置
- 文本模型：Qwen2.5-3B/7B-Instruct；
- 视觉模型：Qwen2.5-VL-3B/7B-Instruct；
- 所有方法保持训练设置与超参数一致，确保公平对照。

## 4. 资源与算力

- **GPU 配置**：
  - Qwen2.5-VL-3B-Instruct（ALFWorld 与 search-based QA）：2×H100 GPU；
  - Qwen2.5-VL-7B-Instruct：4×H100 GPU。
- **训练时长**：论文仅说明训练总时长为 **150 个迭代**（iterations），未报告具体的墙钟时间（wall-clock time）或总 GPU 小时数。
- **其他计算相关超参**：学习率 1e-6，rollout 采样配置、温度参数等在附录 B.2 中给出，但未提供端到端的总体算力消耗估计。

## 5. 实验数量与充分性

### 实验组数概览
1. **主实验**：两个 benchmark × 两个模型规模（3B/7B），报告各子任务成功率与 token 消耗；
2. **视觉-文本压缩分析**：在 7B 模型上固定压缩因子 \( c_t \in [1.0, 2.0] \) 扫掠 6 个档位，分析 token 节省与性能的权衡曲线；
3. **缓存机制消融**：对比 no cache / naive cache / Ours（分段缓存），报告渲染延迟、增长率、峰值内存与节省率；
4. **自压缩机制消融**：在 3B 模型上对比 4 种配置（无 RL±自压缩、RL+密集奖励 K=1、RL+间歇奖励 K=5）；
5. **案例研究**：展示 HotpotQA 上完整多轮检索轨迹（图 8-9）。

### 充分性评估
- **优点**：覆盖不同任务类型（具身 + 检索）、不同模型规模、多个消融维度（缓存策略、压缩调度、奖励设计），实验设计较为全面；
- **潜在不足**：
  - 视觉模型仅用 Qwen2.5-VL 一个系列，未覆盖其他 VLM 架构（论文在 Limitations 中已承认）；
  - 主实验每类任务没有报告多次运行的方差（seeds）；
  - 搜索 QA 的域外（OOD）数据虽有标记（†/⋆），但未单独深入分析 OOD 泛化差距；
  - 未与现有 token 压缩方法（如提示压缩、检索式记忆）直接对比，仅与文本基线和基于 OCR 的朴素方法对比。

## 6. 论文的主要结论与发现

1. **光学历史可大幅降低 token 消耗**：AgentOCR 在 ALFWorld 上节省约 55-62% 的平均 token，峰值节省 56-64%；在 search-based QA 上平均节省 51-57%，峰值节省高达 **73.8%-80.9%**。
2. **RL 训练弥合性能差距**：未经 RL 的 OCR 基线性能显著下降（如 ALFWorld 7B 仅 25.3%，而文本基线 31.3%）；经 GRPO 训练后，AgentOCR 在两个 benchmark 上恢复到文本基线 95% 以上的性能（如 ALFWorld 7B 达 81.2% vs. 基线 81.8%；搜索 QA 7B 达 40.1% vs. 41.9%）。
3. **分段光学缓存高效**：相比无缓存（平均 3509 ms/步），分段缓存平均渲染时间降至 168.77 ms，实现 **20.79× 加速**；缓存内存峰值降低 26.82%。
4. **自压缩需配合 RL 与间歇奖励**：无 RL 时自压缩几乎无效；密集奖励（K=1）导致过度压缩（平均 \( c_t=4.91 \)），成功率骤降至 45.3%；间歇奖励（K=5）在几乎不损失性能（78.2% vs. 78.4%）的情况下，将平均视觉 token 从 458.1 降至 381.7。
5. **存在稳健压缩阈值**：约 55% token 节省（\( c_t=1.2 \)）以内可保持 95%+ 相对性能；超过该阈值性能加速衰减，且搜索任务比 ALFWorld 对压缩更敏感。

## 7. 优点

- **问题定位精准**：直击多轮智能体 RL 训练中长上下文 token/memory 膨胀的关键痛点，具有实际工程价值。
- **方法创新性强**：
  - 将"视觉即压缩"的思想系统化应用于智能体历史管理，而非仅用于文档理解；
  - 分段哈希缓存设计简洁而高效（按内容去重，同时优化时间与空间复杂度）；
  - 自压缩机制将压缩率作为策略动作融入 RL 框架，实现端到端自适应，且压缩奖励仅在成功时给与 + 间歇注入，保证了"效率是次要目标、任务成功是首要目标"的正确优化导向。
- **实验分析深入**：压缩阈值分析、缓存机制的三方对比、自压缩调度消融等揭示了方法的工作机理和边界条件。
- **可复现性好**：提供伪代码（Algorithm 1/2）、公开代码仓库、渲染超参数详表、完整 prompt 模板。

## 8. 不足与局限

- **VLM 架构覆盖有限**：仅评估 Qwen2.5-VL 系列，未测试 DeepSeek-OCR、Qwen3-VL 等其他视觉编码器；不同 patch 分辨率与 tokenization 策略可能显著影响压缩效率与性能，框架原则上是模型无关的，但缺少实证。
- **渲染超参数未系统探索**：字体、行距、色彩、分辨率等固定为默认值，未进行敏感性分析；次优渲染设置可能损害文本可读性并影响推理。
- **历史模态假设限制**：当前仅适用于以文本为主的交互历史（观察、动作、工具输出）可渲染为"文本即图像"；对于 GUI 截图、科学图表、复杂表格等本质多模态的历史内容，方法尚不适用，限制了应用范围（论文明确承认）。
- **性能差距不可忽略**：尽管保留 95%+ 性能，但搜索 QA 域外任务（如 Bamboogle）仍存在约 1.4-2.4 个百分点的绝对下降；部分 ALFWorld 子任务（如 Heat、Cool）差距更明显。
- **实验稳健性信息不足**：未报告多次运行的均值和方差，难以判断性能差异的统计显著性；未与更多现有长上下文压缩/记忆基线对比。
- **计算报告不完整**：未给出端到端训练时间、总 GPU 小时、推理延迟对比（除渲染外的整体端到端延迟），削弱了对"高效"声明的量化支撑。
- **与 KV-cache 优化的关系未被详尽讨论**：论文聚焦视觉缓存，未深入探讨光学压缩后的图像 token 与 Transformer KV-cache 管理之间的耦合优化空间。

（完）
