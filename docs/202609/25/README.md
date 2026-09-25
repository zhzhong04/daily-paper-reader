# 日报 · 2026-09-25

- 最近生成时间：2026-09-25 21:52:55 UTC
- 今日累计更新：1 次
- 今日累计推荐总数：7
- 精读区：2
- 速读区：5

## 今日简报（AI）
今日精读2篇、速读5篇，聚焦LLM前缀复用场景下的缓存替换与H100服务前缀复用、首token时延特征。最值得看的是《When Fancy Eviction Fails》对花哨淘汰策略的反思（9.0分），以及PrefixBench-H100对H100真实服务中前缀复用与TTFT的实测刻画（8.0分）。普通读者可先读这两篇精读，再按兴趣速览Dynamo显存生命周期快速恢复、KV缓存工作集容量规划与风险可控淘汰三篇。

## 精读区
1. [When Fancy Eviction Fails: Rethinking Cache Replacement For LLM Prefix Reuse](/202609/25/2609.28870v1-when-fancy-eviction-fails-rethinking-cache-replacement-for-llm-prefix-reuse) （9.0/10）
2. [PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving](/202609/25/2609.19657v1-prefixbench-h100-characterizing-prefix-reuse-and-time-to-first-token-in-h100-llm-serving) （8.0/10）

## 速读区
1. [Fast Recovery for LLM Serving via Decoupled Device Memory Lifetime in Dynamo](/202609/25/2609.25451v1-fast-recovery-for-llm-serving-via-decoupled-device-memory-lifetime-in-dynamo) （7.0/10）
2. [The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems](/202609/25/2609.27746v1-the-kv-cache-working-set-online-capacity-planning-for-llm-inference-systems) （7.0/10）
3. [Risk-Controlled KV-Cache Eviction: From Memory Budgets to Risk Targets](/202609/25/2609.27981v1-risk-controlled-kv-cache-eviction-from-memory-budgets-to-risk-targets) （7.0/10）
4. [TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](/202609/25/2609.21172v1-tierkv-long-context-on-device-llms-via-predictive-multi-tier-kv-caching) （6.0/10）
5. [When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression](/202609/25/2609.29875v1-when-can-agents-forget-their-reasoning-iclr-for-long-horizon-agent-context-compression) （6.0/10）

---
使用键盘方向键可在日报/论文之间快速切换。
