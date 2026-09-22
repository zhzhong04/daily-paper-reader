# 日报 · 2026-09-22

- 最近生成时间：2026-09-22 22:20:45 UTC
- 今日累计更新：1 次
- 今日累计推荐总数：3
- 精读区：2
- 速读区：1

## 今日简报（AI）
今日精读2篇、速读1篇，聚焦大模型长会话中KV缓存该放GPU、CPU还是SSD，以及多副本27B推理共享缓存的正确性与性能边界。最值得看的是缓存分层放置策略（9.0分）和共享缓存的失效风险与性能上限（8.0分），速读篇则用H100实测前缀复用与首token延迟。普通读者可优先读第一篇，再结合速读的H100数据判断自己场景该不该做前缀复用或分层缓存。

## 精读区
1. [Where Should the KV Cache Live? Placement Policies Across GPU, CPU, and SSD for Long-Lived Sessions](/202609/22/2609.16215v1-where-should-the-kv-cache-live-placement-policies-across-gpu-cpu-and-ssd-for-long-lived-sessions) （9.0/10）
2. [Shared KV Caching for Replicated 27B Inference: Correctness Failures and Performance Boundaries](/202609/22/2609.15021v1-shared-kv-caching-for-replicated-27b-inference-correctness-failures-and-performance-boundaries) （8.0/10）

## 速读区
1. [PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving](/202609/22/2609.19657v1-prefixbench-h100-characterizing-prefix-reuse-and-time-to-first-token-in-h100-llm-serving) （7.0/10）

---
使用键盘方向键可在日报/论文之间快速切换。
