# 日报 · 2026-09-21

- 最近生成时间：2026-09-21 22:42:56 UTC
- 今日累计更新：1 次
- 今日累计推荐总数：7
- 精读区：3
- 速读区：4

## 今日简报（AI）
今天围绕长会话推理的 KV 缓存落位与 Agent 工具调用进度读取，精读了两篇 8.0 分工作，并速览了 4 篇 H100 前缀复用与共享缓存相关研究。最值得看的方向是 KV 缓存在 GPU/CPU/SSD 间的放置策略，以及让服务系统直接读取工具调用进度而非重复猜测。普通读者可优先读这两篇精读，再结合 PrefixBench-H100 了解首字延迟的实测特征。

## 精读区
1. [Where Should the KV Cache Live? Placement Policies Across GPU, CPU, and SSD for Long-Lived Sessions](/202609/21/2609.16215v1-where-should-the-kv-cache-live-placement-policies-across-gpu-cpu-and-ssd-for-long-lived-sessions) （8.0/10）
2. [Ask the Tool, Don't Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It](/202609/21/2609.18849v1-ask-the-tool-dont-guess-agent-tool-calls-hold-their-progress-and-the-serving-system-should-read-it) （8.0/10）
3. [Decomposing Predictive Kubernetes Autoscaling for Large Language Model Serving Under Long Startup Delays](/202609/21/2609.20874v1-decomposing-predictive-kubernetes-autoscaling-for-large-language-model-serving-under-long-startup-delays) （8.0/10）

## 速读区
1. [PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving](/202609/21/2609.19657v1-prefixbench-h100-characterizing-prefix-reuse-and-time-to-first-token-in-h100-llm-serving) （7.0/10）
2. [Shared KV Caching for Replicated 27B Inference: Correctness Failures and Performance Boundaries](/202609/21/2609.15021v1-shared-kv-caching-for-replicated-27b-inference-correctness-failures-and-performance-boundaries) （6.0/10）
3. [Marginal utility, matrix factorization, and the Key-Value (KV) cache: a unified information-economic framework for sovereign geo-mining inference](/202609/21/2609.20068v1-marginal-utility-matrix-factorization-and-the-key-value-kv-cache-a-unified-information-economic-framework-for-sovereign-geo-mining-inference) （6.0/10）
4. [MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems](/202609/21/2609.21533v1-mace-memory-agent-co-evolution-with-adaptive-memory-graphs-for-multi-agent-systems) （6.0/10）

---
使用键盘方向键可在日报/论文之间快速切换。
