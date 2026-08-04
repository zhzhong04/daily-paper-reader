---
title: "Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents"
title_zh: 功能缓存嫁接：面向具身智能体的鲁棒快速代码策略合成
authors: "Saehun Chun, Wonje Choi, Sera Choi, Sanghyun Ahn, Honguk Woo"
date: 2026-04-30
pdf: "https://openreview.net/pdf/e6cbcea9f9e647f6863524749cc0e7f8e7a6545b.pdf"
tags: ["query:agent-cache"]
score: 6.0
evidence: 在具身智能体代码生成中跨不同上下文复用有效代码骨架的提示级KV缓存
tldr: 代码编写大模型在具身智能体策略生成中面临长提示重复预计算导致解码延迟和全生成式解码鲁棒性差等问题。FCGraft构建函数级已验证代码骨架库，并关联保存提示级Transformer键值缓存，通过功能缓存嫁接将已有缓存复用于新任务提示，避免重复预计算。实验表明在开放域环境中显著加快策略合成并提高鲁棒性，为跨上下文KV缓存复用提供了可迁移的方法支撑。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 代码策略生成中长提示重复预计算导致延迟，且全生成式解码容易出现API不匹配与安全缺失。
method: 构建函数级代码骨架与提示级KV缓存库，通过缓存嫁接复用有效代码片段的KV缓存，加快生成。
result: 显著降低解码延迟，提高代码策略合成鲁棒性，减少API调用错误。
conclusion: 展示了跨上下文KV缓存复用的实用技术，可支撑智能体工作流中的缓存高效利用。
---

## Abstract
Code-writing large language models (CodeLLMs) generate executable code policies for embodied agents by translating natural language goals and environmental constraints into structured control programs. However, policy generation in open-domain embodied environments suffers from two fundamental limitations:
(i) delayed decoding caused by repetitive prefill computation over long prompts, and
(ii) limited robustness due to fully generative decoding, which often produces API mismatches, missing safety guards, and unstable control logic. To address these limitations, we present FCGraft, a Functional Cache Grafting framework.
FCGraft maintains a library of function-level validated code skeletons and their associated prompt-level Transformer key–value (KV) caches, and synthesizes new policies by retrieving relevant functions and grafting their KV caches when a new task is provided. Given retrieved function caches, FCGraft performs cache grafting via stitching, which composes cached function segments into a composite policy, and patching, which locally adapts only the necessary code regions to satisfy task-specific parameters and constraints with minimal additional decoding. By eliminating redundant prefill computation, this approach reduces generation latency, while reusing validated control structures improves robustness over prompt-level caching methods RAGCache, achieving $18.31\$% higher task success rate and $2.3\times$ faster policy synthesis.

---

## 论文详细总结（自动生成）

## 论文总结

### 1. 核心问题与整体含义（研究动机与背景）

- **背景**：代码编写大语言模型（CodeLLMs）被用于将自然语言目标与环境约束翻译为可执行代码策略，驱动具身智能体在开放域环境中完成任务。
- **核心问题**：现有策略生成方式存在两大瓶颈：
  1. **解码延迟高**：长提示词反复执行预填充（prefill）计算，导致生成速度慢。
  2. **鲁棒性不足**：完全生成式解码容易出现 API 不匹配、缺少安全防护、控制逻辑不稳定等问题。
- **整体含义**：该方法旨在解决具身智能体代码策略生成中的“速度”与“可靠性”矛盾，为跨上下文的提示级 KV 缓存复用提供了实用技术路径。

### 2. 方法论：核心思想、关键技术细节与算法流程

- **核心思想**：提出 **FCGraft（Functional Cache Grafting）** 框架，通过复用已验证代码骨架的 Transformer 键值（KV）缓存，避免对新任务提示重复预填充，同时利用已验证的控制结构提升鲁棒性。
- **关键技术细节**：
  - **函数级代码骨架库**：维护一个包含函数级已验证代码骨架及其关联的提示级 KV 缓存的库。
  - **缓存嫁接（Cache Grafting）**：当新任务到来时，检索相关函数并直接嫁接其 KV 缓存。
  - **两种拼接机制**：
    - **Stitching（缝合）**：将检索到的多个函数缓存片段组合成复合策略。
    - **Patching（补丁）**：仅对必要的代码区域进行局部适配，以满足任务特定参数与约束，同时尽可能减少额外解码。
- **算法流程（文字描述）**：
  1. 任务输入后，先从函数库中检索与任务相关的代码骨架及其 KV 缓存。
  2. 通过 stitching 将缓存的函数片段按策略逻辑组合为整体。
  3. 通过 patching 对局部代码进行微调，适配当前任务的具体参数和约束。
  4. 仅对新增或修改的部分进行少量解码，从而省去对整条长提示的重复预填充。

### 3. 实验设计

- **数据集 / 场景**：论文针对开放域具身环境中的策略生成，但提供的摘要中未明确列出具体环境名称或 benchmark（如 ALFRED、VirtualHome 等）。
- **对比方法**：与提示级缓存方法 **RAGCache** 进行了对比。
- **主要指标**：任务成功率（Task Success Rate）与策略合成速度（Policy Synthesis Speed）。
- **结果摘要**：
  - 相比 RAGCache，任务成功率提升 **18.31%**。
  - 策略合成速度提升 **2.3 倍**。

### 4. 资源与算力

- 摘要及元数据中 **未明确说明** 使用了何种 GPU 型号、数量、训练时长或推理时资源配置。无法从现有材料中获知具体算力细节。

### 5. 实验数量与充分性

- 从摘要和元数据看，仅提到与 RAGCache 的对比结果，未提及多场景 benchmark、消融实验、不同模型规模测试或误差分析。
- **充分性评估**：
  - 由于仅有单一对比方法和两个核心指标，实验结果**覆盖不够全面**。
  - 未展示不同任务复杂度、不同缓存命中率、不同模型基座下的详细数据，**客观性与公平性难以完全验证**。
  - 若论文正文包含更丰富实验，则需以正文为准，但当前材料无法支撑更强结论。

### 6. 主要结论与发现

- FCGraft 通过函数级缓存嫁接，能够**显著降低解码延迟**，加快策略合成速度。
- 通过重用已验证的控制结构，**减少 API 调用错误**，提升代码策略合成的鲁棒性。
- 相比 RAGCache 等提示级缓存方法，FCGraft 在任务成功率与速度上均有明显优势。
- 研究证明了跨上下文 KV 缓存复用的实用可行性，可支撑具身智能体工作流中的高效缓存利用。

### 7. 优点

- **思路新颖**：将缓存粒度从“整段提示”下沉到“函数级代码骨架”，实现更精细的跨任务缓存复用。
- **双机制设计**：缝合（stitching）与补丁（patching）结合，兼顾全局组合与局部适配，既省算力又不失灵活性。
- **缓解预填充瓶颈**：直接规避了长提示重复 prefill 的计算开销，具有显著的效率价值。
- **提升鲁棒性**：复用已验证代码结构，有助于减少 API 不匹配和缺失安全防护等问题。

### 8. 不足与局限

- **实验信息不足**：摘要中未提供具体 benchmark、任务域细节和消融实验，难以评估方法的泛化边界。
- **对比方法单一**：仅对比 RAGCache，未与其他代码生成基线（如直接生成、RAG、微调方法等）进行综合比较。
- **算力披露缺失**：未说明实验硬件配置，不利于可复现性评估。
- **潜在偏差风险**：函数库的构建质量、缓存覆盖范围、检索的准确率都可能显著影响最终效果，但文中未给出相应敏感性分析。
- **应用限制**：依赖函数库中已存在的代码骨架，对于全新未知任务或需要全新逻辑的场景，缓存嫁接的收益可能受限。

---

（完）
