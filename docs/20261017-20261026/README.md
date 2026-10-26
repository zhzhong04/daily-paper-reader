# 日报 · 2026-10-17 ~ 2026-10-26

- 最近生成时间：2026-10-26 13:54:06 UTC
- 今日累计更新：1 次
- 今日累计推荐总数：6
- 精读区：2
- 速读区：4

## 今日简报（AI）
本期日报围绕 LLM Agent 的缓存与记忆系统，共筛选 6 篇论文，并精读 2 篇（均 8.0 分）：SARIA 用 DRAM-SSD 协同重载实现持久化感知 KV 缓存，SPECMEM 则通过实时内存管理加速 Agent 的工具调用。
最值得看的方向是“把 Agent 的记忆当作可调度资源”：KV 缓存跨层级持久化与工具调用时的实时内存管理，两者都指向降低重复计算与延迟。
普通读者可先读这两篇精读论文的架构图与实验部分，再按需浏览速读中关于经验记忆取舍（REM）与共享内存缓冲（Muffin）的思路，用于自己的 Agent 工程选型。

## 精读区
1. [SARIA: Persistence-Aware KV Caching with Coordinated DRAM--SSD Reload for LLM Agents](/20261017-20261026/2610.31169v1-saria-persistence-aware-kv-caching-with-coordinated-dram--ssd-reload-for-llm-agents) （8.0/10）
2. [SPECMEM: Accelerating Agentic Tool Calling via Live Memory Management](/20261017-20261026/2610.31840v1-specmem-accelerating-agentic-tool-calling-via-live-memory-management) （8.0/10）

## 速读区
1. [Adaptive Deadline- and Energy-Aware Caching Algorithms in Dynamic Multi-UAV Edge Networks](/20261017-20261026/2610.30768v1-adaptive-deadline--and-energy-aware-caching-algorithms-in-dynamic-multi-uav-edge-networks) （7.0/10）
2. [REM: What to Store, When to Recall, What to Forget in Experience Memory for Coding Agents](/20261017-20261026/2610.27377v1-rem-what-to-store-when-to-recall-what-to-forget-in-experience-memory-for-coding-agents) （6.0/10）
3. [Muffin - A Shared Memory Buffer for Asynchronous AI Agents](/20261017-20261026/2610.31355v1-muffin---a-shared-memory-buffer-for-asynchronous-ai-agents) （6.0/10）
4. [KVStream: Adaptive Parallel Storage Management for KV Caching in Large-Scale LLM Serving](/20261017-20261026/2610.31827v1-kvstream-adaptive-parallel-storage-management-for-kv-caching-in-large-scale-llm-serving) （6.0/10）

---
使用键盘方向键可在日报/论文之间快速切换。
