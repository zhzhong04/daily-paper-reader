# 日报 · 2026-09-27

- 最近生成时间：2026-09-27 21:53:41 UTC
- 今日累计更新：1 次
- 今日累计推荐总数：5
- 精读区：1
- 速读区：4

## 今日简报（AI）
今天扫描了 5 篇 LLM 推理系统论文，其中精读《When Fancy Eviction Fails: Rethinking Cache Replacement For LLM Prefix Reuse》（8.0/10），速读聚焦 KV Cache 管理与稀疏注意力优化。最值得看的是前缀复用场景下"花哨淘汰策略"为何失效这一反思性结论，以及《The KV Cache Working Set》（7.0/10）提出的在线容量规划思路，两者都直指推理服务的内存瓶颈。普通读者可先从 KV Cache 容量估算入手，理解显存与吞吐的取舍，再回看淘汰策略的适用边界。

## 精读区
1. [When Fancy Eviction Fails: Rethinking Cache Replacement For LLM Prefix Reuse](/202609/27/2609.28870v1-when-fancy-eviction-fails-rethinking-cache-replacement-for-llm-prefix-reuse) （8.0/10）

## 速读区
1. [ARM: Attention with Routed-Memory for Learnable Sparse Control](/202609/27/2609.24417v1-arm-attention-with-routed-memory-for-learnable-sparse-control) （7.0/10）
2. [The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems](/202609/27/2609.27746v1-the-kv-cache-working-set-online-capacity-planning-for-llm-inference-systems) （7.0/10）
3. [Bridging LLM Serving and CXL-SSDs with Chunk-Aware KV Cache Management](/202609/27/2609.26828v1-bridging-llm-serving-and-cxl-ssds-with-chunk-aware-kv-cache-management) （6.0/10）
4. [StateComp: Learning When to Compress History in Long Horizon Agents](/202609/27/2609.27298v1-statecomp-learning-when-to-compress-history-in-long-horizon-agents) （6.0/10）

---
使用键盘方向键可在日报/论文之间快速切换。
