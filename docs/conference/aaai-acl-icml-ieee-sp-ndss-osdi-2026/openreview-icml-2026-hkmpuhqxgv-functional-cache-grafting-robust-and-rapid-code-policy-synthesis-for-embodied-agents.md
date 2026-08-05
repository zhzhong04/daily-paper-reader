---
title: "Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents"
title_zh: 功能缓存嫁接：具身智能体代码策略的鲁棒快速合成
authors: "Saehun Chun, Wonje Choi, Sera Choi, Sanghyun Ahn, Honguk Woo"
date: 2026-04-30
pdf: "https://openreview.net/pdf/e6cbcea9f9e647f6863524749cc0e7f8e7a6545b.pdf"
tags: ["query:awc"]
score: 8.0
evidence: 提出FCGraft，通过缓存可复用的代码骨架与提示级Transformer键来加速具身智能体策略生成。
tldr: 本文针对CodeLLM为具身智能体生成代码策略时预填充计算重复、解码鲁棒性差的问题，提出FCGraft框架。它维护一个包含已验证代码骨架及其提示级Transformer键的缓存库，通过功能缓存嫁接实现快速策略合成，避免重复的预填充开销，同时提升API匹配与安全防护的稳定性。实验表明该方法能显著降低延迟并提高策略生成鲁棒性，为智能体代码策略合成提供了高效的缓存复用机制。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: CodeLLM为具身智能体生成代码策略时面临重复预填充延迟高与纯生成解码鲁棒性差的问题。
method: 提出功能缓存嫁接（FCGraft），维护已验证代码骨架库及其提示级Transformer键，在生成新策略时复用缓存。
result: 实验验证FCGraft在缩短解码延迟和减少API错误等方面优于全生成式基线。
conclusion: 功能级缓存可同时提升具身智能体代码策略合成的速度与鲁棒性。
---

## Abstract
Code-writing large language models (CodeLLMs) generate executable code policies for embodied agents by translating natural language goals and environmental constraints into structured control programs. However, policy generation in open-domain embodied environments suffers from two fundamental limitations:
(i) delayed decoding caused by repetitive prefill computation over long prompts, and
(ii) limited robustness due to fully generative decoding, which often produces API mismatches, missing safety guards, and unstable control logic. To address these limitations, we present FCGraft, a Functional Cache Grafting framework.
FCGraft maintains a library of function-level validated code skeletons and their associated prompt-level Transformer key–value (KV) caches, and synthesizes new policies by retrieving relevant functions and grafting their KV caches when a new task is provided. Given retrieved function caches, FCGraft performs cache grafting via stitching, which composes cached function segments into a composite policy, and patching, which locally adapts only the necessary code regions to satisfy task-specific parameters and constraints with minimal additional decoding. By eliminating redundant prefill computation, this approach reduces generation latency, while reusing validated control structures improves robustness over prompt-level caching methods RAGCache, achieving $18.31\$% higher task success rate and $2.3\times$ faster policy synthesis.

---

## 论文详细总结（自动生成）

# 中文总结

## 1. 核心问题与整体含义

- **研究动机**：代码大语言模型（CodeLLM）通过将自然语言目标与环境约束翻译为结构化控制程序，为具身智能体生成可执行代码策略。但在开放域具身环境中，该过程存在两个根本性局限：
  - **延迟问题**：长提示词导致重复的预填充（prefill）计算，解码过程被显著延迟。
  - **鲁棒性问题**：完全生成式解码容易产生 API 不匹配、缺失安全防护、控制逻辑不稳定等错误。
- **整体含义**：代码策略合成既需要快速响应，又需要高可靠性，二者之间存在矛盾。本文提出功能缓存嫁接（FCGraft）框架，试图通过函数级代码复用同时解决效率与鲁棒性问题。

## 2. 方法论

- **核心思想**：FCGraft 维护一个**函数级已验证代码骨架库**，每个骨架关联其**提示级 Transformer 键值（KV）缓存**。面对新任务时，检索最相关的函数，将其 KV 缓存“嫁接”到新策略生成过程中，从而避免重新对完整提示做预填充。
- **关键技术细节**：
  - **拼接（stitching）**：将多个缓存函数段组合成一个复合策略，使整体策略结构继承已验证的代码模块。
  - **修补（patching）**：仅对局部代码区域做必要的适配性修改，以匹配任务特定参数和约束，并将额外解码量降至最低。
- **算法流程（文字说明）**：输入新任务 → 从函数缓存库检索候选代码骨架 → 利用对应 KV 缓存执行拼接，形成策略主体 → 对需要适配的部分进行局部修补 → 输出可执行策略。
- **核心优势**：
  - 消除冗余预填充，降低生成延迟；
  - 复用已验证控制结构，避免全生成式解码带来的 API 错误与安全漏洞；
  - 相比提示级缓存方法（如 RAGCache），在粗粒度缓存之上进一步细化为函数级粒度，复用更为精准高效。

## 3. 实验设计

- **数据集 / 场景**：摘要中仅指出面向“开放域具身环境”，未明确说明具体使用哪个具身智能体 benchmark（如 ALFRED、Minecraft、VirtualHome 等），也未列出具体任务数量。
- **对比方法**：
  - **RAGCache**：提示级缓存方法，是文中的主要对比基线；
  - **全生成式基线**：未给出具体模型名称，推测为不使用缓存的完整 CodeLLM 生成方法。
- **对比结果**：FCGraft 在任务成功率上比 RAGCache 高 **18.31%**，策略合成速度快 **2.3 倍**。

## 4. 资源与算力

- 摘要中**未提及**任何硬件资源信息，包括 GPU 型号、GPU 数量、训练或推理时长、缓存库规模等。
- 若需了解算力开销，需要参考论文正文的实验设置部分。

## 5. 实验数量与充分性

- 从已有摘要可见至少包含一组**与 RAGCache 的整体对比实验**。
- 但当前文本未展示：
  - 多组不同 benchmark 的对比；
  - 消融实验（如去掉拼接、去掉修补、不同缓存粒度的影响）；
  - 跨不同 CodeLLM 模型（如 GPT、CodeLlama、DeepSeek-Coder 等）的泛化实验；
  - 任务难度分布、成功率方差、失败模式分析等。
- **客观性评价**：从摘要报告的主指标看结果具有吸引力，但仅凭摘要无法判断实验是否充分、对照组是否公平、是否存在选择偏差。需进一步阅读正文确认统计显著性与误差棒等信息。

## 6. 主要结论与发现

- 功能缓存嫁接可以**同时提升速度与鲁棒性**，解决了代码策略生成中“快速生成”与“可靠生成”之间的两难。
- 实验证明 FCGraft 在解码延迟、任务成功率等方面显著优于 RAGCache 与全生成式基线。
- 该研究验证了“函数级缓存复用”这一思路对具身智能体代码策略合成的有效性。

## 7. 优点

- **方法新颖性强**：将缓存粒度从提示级细化到函数级，并提出“拼接 + 修补”的混合生成策略，兼具复用性与局部灵活性。
- **问题定位准确**：同时击中 CodeLLM 策略生成的两大痛点——预填充计算开销和全生成式解码不稳定性。
- **工程可落地性好**：通过复用已验证代码骨架，天然降低 API 错误和安全防护缺失风险，对真实具身系统较友好。
- **效果提升显著**：成功率提升 18.31%、速度提升 2.3 倍，属于较可观的性能增益。

## 8. 不足与局限

- **实验信息不完整**：从摘要无法获知具体场景、任务数、模型种类等关键实验细节，难以评估结论的普适性。
- **缺少消融与敏感性分析**：未提及缓存库规模、检索质量、骨架覆盖度等因素对性能的影响。
- **潜在偏差风险**：若 RAGCache 等基线未做足够调优，或实验任务偏向缓存友好型结构，则结果可能高估方法优势。
- **应用限制**：函数级缓存的构建依赖大量已验证代码骨架，如何自动化积累并维护高质量骨架库是一个实际问题；同时，缓存嫁接处理全新领域或非结构化任务时可能适用性有限。
- **算力与资源未披露**：难以判断该方法在实际部署中的资源成本，例如 KV 缓存存储开销、检索延迟和缓存更新代价。
- **安全验证不明确**：摘要提到“安全防护”提升，但未说明验证框架与失败边界。

（完）
