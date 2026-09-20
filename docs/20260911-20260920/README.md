# 日报 · 2026-09-11 ~ 2026-09-20

- 最近生成时间：2026-09-20 02:51:24 UTC
- 今日累计更新：1 次
- 今日累计推荐总数：12
- 精读区：6
- 速读区：6

## 今日简报（AI）
本期日报扫完 12 篇（精读 6、速读 6），主线明显落在 LLM 推理的 KV 缓存、内存与冷启动优化上。

最值得看的是精读里 9.0 分的《AgentKV: Phase-Aware KV Eviction for Agentic LLMs》——按阶段做 KV 淘汰的思路，以及 8.0 分的 Serverless 动态切片降冷启动延迟。

普通读者可先读 AgentKV 抓"阶段感知"这个核心，再扫速读里的 HBM 动态重划分与 Prefix Sharing 排序化，串起缓存—内存—调度这条线。

## 精读区
1. [AgentKV: Phase-Aware KV Eviction for Agentic LLMs](/20260911-20260920/2609.14872v1-agentkv-phase-aware-kv-eviction-for-agentic-llms) （9.0/10）
2. [Reducing Cold-Start Latency in Serverless Applications via Dynamic Slicing](/20260911-20260920/2609.14040v1-reducing-cold-start-latency-in-serverless-applications-via-dynamic-slicing) （8.0/10）
3. [Shared KV Caching for Replicated 27B Inference: Correctness Failures and Performance Boundaries](/20260911-20260920/2609.15021v1-shared-kv-caching-for-replicated-27b-inference-correctness-failures-and-performance-boundaries) （8.0/10）
4. [Where Should the KV Cache Live? Placement Policies Across GPU, CPU, and SSD for Long-Lived Sessions](/20260911-20260920/2609.16215v1-where-should-the-kv-cache-live-placement-policies-across-gpu-cpu-and-ssd-for-long-lived-sessions) （8.0/10）
5. [Ask the Tool, Don't Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It](/20260911-20260920/2609.18849v1-ask-the-tool-dont-guess-agent-tool-calls-hold-their-progress-and-the-serving-system-should-read-it) （8.0/10）
6. [PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving](/20260911-20260920/2609.19657v1-prefixbench-h100-characterizing-prefix-reuse-and-time-to-first-token-in-h100-llm-serving) （8.0/10）

## 速读区
1. [Dynamic HBM Repartitioning for Multi-Turn MoE Serving](/20260911-20260920/2609.13537v1-dynamic-hbm-repartitioning-for-multi-turn-moe-serving) （7.0/10）
2. [Prefix Sharing Is a Sorting Problem](/20260911-20260920/2609.13692v1-prefix-sharing-is-a-sorting-problem) （7.0/10）
3. [Collaborative Memory for Multi-Agent VLM Systems](/20260911-20260920/2609.17921v1-collaborative-memory-for-multi-agent-vlm-systems) （7.0/10）
4. [Calibrate, Then Route: A Measured Study of Learned Request Routing for Disaggregated LLM Serving](/20260911-20260920/2609.16206v1-calibrate-then-route-a-measured-study-of-learned-request-routing-for-disaggregated-llm-serving) （6.0/10）
5. [Fast-Convergent Meta-RL via Gradient-Clustered BS Sampling for Edge Caching](/20260911-20260920/2609.16370v1-fast-convergent-meta-rl-via-gradient-clustered-bs-sampling-for-edge-caching) （6.0/10）
6. [Taming the Agentic RAN: Stability-Guaranteed Arbitration of Autonomous AI Agents in O-RAN](/20260911-20260920/2609.18857v1-taming-the-agentic-ran-stability-guaranteed-arbitration-of-autonomous-ai-agents-in-o-ran) （6.0/10）

---
使用键盘方向键可在日报/论文之间快速切换。
