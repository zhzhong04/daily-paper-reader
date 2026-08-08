---
title: Fairness and Stability for Shared Resource Allocation Problems
title_zh: 共享资源分配问题的公平性与稳定性
authors: "Jiazhu Fang, Qizhi Fang, Minming Li, Wenjing Liu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38735/42697"
tags: ["query:agent-cache"]
score: 4.0
evidence: 研究多个体共享资源的分配公平性与稳定性，理论可迁移至共享缓存资源管理。
tldr: 多个智能体共享异构资源时，其效用不仅取决于资源类型还取决于共享人数，如何公平且稳定地分配成为核心问题。论文针对单调非减与单调非增两类价值函数，系统考察最大最小份额公平、无嫉妒性、纳什稳定及其知识放宽概念，刻画了分配方案的可行性。研究成果为共享缓存等协作资源的管理提供了公平性与稳定性的理论参考。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
motivation: 多智能体共享异构资源时，效用受共享人数影响，需要公平且稳定的分配方案。
method: 针对单调价值函数，分析最大最小份额公平、无嫉妒性和纳什稳定等经典性质的可行性。
result: 刻画了不同价值函数下公平与稳定概念的共存条件与分配规则。
conclusion: 为共享资源（如缓存）的协作分配提供了公平与稳定性的理论支撑。
---

## Abstract
This paper investigates the problem of shared resource allocation, where a set of agents must be assigned to heterogeneous resources, with each agent allocated exactly one resource and each resource potentially shared by multiple agents. An agent’s utility for a given resource is jointly determined by the resource's type and the number of agents sharing it. We focus on two fundamental classes of monotone valuations: monotone nondecreasing and monotone nonincreasing, where an agent’s utility respectively increases or decreases with the number of agents sharing the resource. Within this shared resource framework, we examine classical notions of fairness and stability, including maximin-share fairness, envy-freeness, Nash stability, and two epistemic relaxations—epistemic envy-freeness and epistemic Nash stability—as well as swap stability. We propose formal definitions adapted to this setting and systematically analyze the relationships among these concepts. The primary contributions of this work consist of establishing existence and computational complexity results for each notion under both monotonicity assumptions and developing polynomial-time algorithms in cases where fair or stable allocations are guaranteed to exist.

---

## 论文详细总结（自动生成）

根据提供的论文内容，以下是对《共享资源分配问题的公平性与稳定性》（Fairness and Stability for Shared Resource Allocation Problems）一文的结构化总结。

## 1. 论文的核心问题与整体含义（研究动机和背景）

- 该论文研究的是**共享资源分配问题（Shared Resource Allocation Problem）**：有一组智能体（agents）和一组异构资源（resources），每个智能体必须被分配到一个资源，且每个资源可同时被多个智能体共享。
- 关键特征：智能体对资源的效用不仅取决于资源本身，还取决于**共享该资源的智能体人数**。这一设定突破了传统公平分配（fair division）中“一个资源只能被一个人独占”的假设。
- 论文聚焦两类自然的价值函数：
  - **单调非减（monotone nondecreasing）**：效用随共享人数增加而增加（如喜欢社交的拼车乘客）。
  - **单调非增（monotone nonincreasing）**：效用随共享人数增加而降低（如厌恶拥挤的乘客）。
- 研究目标：将经典公平性（公平份额、无嫉妒性）与稳定性（纳什稳定、交换稳定）概念推广至共享场景，系统地刻画这些概念在这两类价值函数下的**存在性**与**计算复杂度**，并在可行时给出多项式时间算法。
- 该模型适用于拼车、云计算服务器调度等现实场景，填补了共享资源条件下公平分配系统性研究的空白。

## 2. 论文提出的方法论：核心思想、关键技术细节

- 论文严格定义了共享资源分配问题的实例，并形式化地推广了以下核心概念：
  - **Maximin Share（MMS）**：智能体 i 的 MMS 值 = 通过提出最优的分配向量 x 所能保证的最差资源效用（max min over resources）。
  - **Envy-Freeness（EF，无嫉妒性）**：任何智能体不嫉妒其他智能体所获资源，且不嫉妒空资源（防止所有智能体挤在一个资源上的平凡解）。
  - **Nash Stability（NS，纳什稳定）**：任何智能体单方面迁移到其他资源无法提高效用。
  - **Epistemic Envy-Freeness（EEF）**和**Epistemic Nash Stability（ENS）**：基于信息受限（只知道自身资源状况）的松弛概念。
  - **Swap Stability（SS）**：不存在能同时改善双方效用的交换对。
- 技术路线与算法：
  - **单调非增值函数下的 MMS**：提出了 Algorithm 1（计算单智能体 MMS 分配向量）和 Algorithm 2（基于 n 个 MMS 向量构造全局 MMS 分配），证明可在多项式时间内完成。
  - **单调非增值函数下的 NS**：提出 Algorithm 3，通过迭代把未分配智能体放入其偏好资源，在内部循环中反复将“有偏离动机”的智能体移动到效用最大化资源，维持纳什稳定性，时间复杂度为 O(n²)。
  - **单调非增值函数下的 ENS**：Algorithm 3 输出的 NS 天然满足 ENS。
  - **单调非增值函数下的 EEF 与 ENS**：Algorithm 4 先使所有智能体聚到资源 1，再循环将能提高效用的智能体移动到最优资源，得到 ENS；由于 ENS 蕴含 EEF（该条件下），EEF 也可多项式求解。
  - **计算复杂性归约**：通过构造特殊实例，将 MMS/NS/EF 存在性问题归约为经典 NP-complete 问题（如 X3C 或 SAT 类问题）的实例，证明其 NP-hard 与 NP-complete 性。
- 概念间关系（图1、图2）：
  - 单调非增：EF ⇒ EEF ⇒ MMS ⇒ ENS ⇒ NS 等传导关系；
  - 单调非减：NS ⇒ ENS ⇒ EEF 等传导关系，MMS 蕴含 NS。

## 3. 实验设计与 benchmark

- **这篇论文是纯理论型论文，没有设计任何仿真实验或数据集**。
- 论文的“实验结果”均以定理、命题、观察和证明形式给出，核心验证方式是**严格的数学证明与计算复杂性归约**，而非以实证数据驱动的 benchmark 对比。
- 作为对照，论文在引言和相关工作部分与以下模型进行了“理论对比”：
  - 经典公平分配（可分/不可分资源，MMS/EF 等）
  - 群体公平分配（group fairness）
  - 匿名享乐博弈 / 拥塞博弈（congestion games）
  - 宿舍分配 / 室友匹配模型
- 但未进行任何表格化、数据化的实验对比。

## 4. 资源与算力

- **论文未提及任何算力资源信息**，如 GPU 型号、数量、训练时长等。
- 因为本文不涉及机器学习训练、大规模数值模拟或需要计算资源的实验，所以无需也无法提供该类信息。

## 5. 实验数量与充分性

- **该论文没有传统意义上的实验（无实验组数量、无消融实验）**，因此无法从实验次数角度评价其充分性。
- 从理论验证角度看，论文的覆盖面较充分：
  - 覆盖了两类价值函数（非增、非减）下的 6 类核心概念（MMS、EF、NS、EEF、ENS、SS）的存在性与复杂度。
  - 通过 Table 1 系统汇总了所有主要结果。
  - 对每个“不存在”的负结果均给出具体反例（如 Example 1、2、3，见附录）。
  - 对每个“存在”的正结果均给出构造性证明或多项式算法。
- 局限：部分复杂度结论（如 EF 在非增值函数下的 NP-completeness）是在“异质单调性”（部分非增、部分非减）的假设下证明的，而并非在纯单调非增的估值类下得到。

## 6. 论文的主要结论与发现

- **MMS（最大最小份额）**：
  - 单调非增值函数下，MMS 值可在多项式时间计算，且 MMS 分配总存在并有效可算；
  - 单调非增值函数下，这是与经典公平分配（NP-hard）的显著对比；
  - 单调非增值函数下，MMS 分配不一定存在，判定是否存在 MMS 分配是 NP-complete。
- **EF 与 NS**：
  - 单调非增值函数下：NS 总存在并可 O(n²) 时间求解；EF 可能不存在（存在两资源反例）；
  - 单调非增值函数下：NS 不一定存在，判定其存在性是 NP-complete；但两资源或所有智能体效用函数相同的情况下 NS 保证存在；
  - 单调非增值下 EF 的复杂性为开放问题。
  - EF 与 NS 在相反单调性下互推（非增下 EF ⇒ NS；非减下 NS ⇒ EF）。
- **EEF 与 ENS（知识松弛）**：
  - 单调非增值函数下：EEF 和 ENS 总存在且可多项式时间计算；
  - 单调非增值函数下：ENS 总存在且可多项式时间计算，EEF 可能不存在；
  - 因此，缺乏完全信息时（知识松弛）往往能恢复可行性。
- **SS（交换稳定）**：
  - 任何社会福利最大化的分配也是交换稳定的（无需单调性假设），因此 SS 分配总存在且可有效求解（结果见附录）。
- **整体定位**：第一项对共享资源分配公平与稳定性的系统性理论框架，为后续研究奠定了基础。

## 7. 优点

- **模型新颖且更贴近现实**：突破了资源不可共享的传统假设，将“共享人数”造成的正/负外部性作为效用核心，可建模拼车、服务器调度等场景。
- **定义严谨**：对 MMS、EF、NS 等概念给出了适应共享场景且避免平凡解（如空资源嫉妒条件）的推广，定义清晰且自然。
- **结论完整**：Table 1 清晰汇总了两种单调估值函数下 6 个概念的存在性+复杂度+算法，覆盖面广。
- **计算复杂性分析有价值**：明确了哪些问题可多项式求解（MMS/NS/ENS/EEF），哪些是 NP-complete（MMS/NS/EF/SS 求解等），为工程实践指明边界。
- **算法设计有启发性**：Algorithm 1（最小资源锚定转移）、Algorithm 2（贪心指派）、Algorithm 3（维护稳定性的迭代修复）都具有较强的构造性，便于复用。
- **对开放问题的讨论诚实且有价值**：明确指出 EF 在单调非增值函数下的存在性仍是开放问题。

## 8. 不足与局限

- **缺乏实证研究**：论文属于纯理论证明，没有进行真实场景（如拼车、调度）的仿真实验，难以直观评估算法在实际应用中的性能表现（如运行时间、用户满意度）。
- **复杂度结论在部分假设下受限**：EF 的 NP-complete 证明依赖“异质单调性”假设；在纯单调非增值函数下 EF 的复杂度尚未定论，核心结论完整性稍显不足。
- **EGS 求解未展示算法细节**：交换稳定的多项式算法和福利最大化分配 NP-hard 的结果放在了附录，正文没有详细阐述。所涉及的“福利最大化分配”本身 NP-hard 也为 SS 求解带来一定实用限制。
- **单调性假设是强假设**：现实中的共享资源效用不一定严格单调，可能是先增后减（如拥挤度临界点）等更复杂函数，论文的结果不能直接迁移。
- **未涉及混合动作空间**：仅考虑一对一映射（智能体到资源），未考虑智能体可以部分使用多个资源或选择不参与的情况（不同于群组活动选择博弈的 opt-out 设定）。
- **开放问题仍较多**：如单调非增值函数下 EF 的存在性、MMS 与 Pareto 最优结合等，论文未能给出完整答案。

（完）
