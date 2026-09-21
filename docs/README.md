<div class="dpr-home-notice-card dpr-home-panel">
  <div class="dpr-home-notice-header dpr-home-panel-header">
    <h3 class="dpr-home-notice-title">公告与更新</h3>
    <a class="dpr-home-notice-tutorial" href="#/tutorial/README">使用教程 <span aria-hidden="true">›</span></a>
  </div>
  <div class="dpr-home-notice-entry">
    <time class="dpr-home-notice-date" datetime="2026-07-20">07.20</time>
    <div>
      <strong class="dpr-home-notice-entry-title">反馈功能上线</strong>
      <span class="dpr-home-notice-entry-summary">新增反馈功能，欢迎大家踊跃反馈各种建议，我们会第一时间查看并协调处理。</span>
    </div>
  </div>
  <div class="dpr-home-notice-entry">
    <time class="dpr-home-notice-date" datetime="2026-07-19">07.19</time>
    <div>
      <strong class="dpr-home-notice-entry-title">首页新增社区统计</strong>
      <span class="dpr-home-notice-entry-summary">现在可以看到今天看论文的人数和项目加入人数。</span>
    </div>
  </div>
  <div class="dpr-home-site-stats" data-dpr-site-stats hidden aria-live="polite">
    <span>今天有 <strong class="dpr-home-site-stat-value" data-dpr-daily-readers>--</strong> 人在看论文</span>
    <span class="dpr-home-site-stat-separator" aria-hidden="true">·</span>
    <span>昨天有 <strong class="dpr-home-site-stat-value" data-dpr-yesterday-readers>--</strong> 人在看论文</span>
    <span class="dpr-home-site-stat-separator" aria-hidden="true">·</span>
    <span>已有 <strong class="dpr-home-site-stat-value" data-dpr-fork-count>--</strong> 人加入 Daily Paper Reader</span>
    <span class="dpr-home-history">
      <button type="button" class="dpr-home-history-trigger" data-dpr-history-trigger aria-label="查看最近 14 天阅读趋势"><span aria-hidden="true">🔍</span></button>
      <span class="dpr-home-history-popover" data-dpr-history-popover role="tooltip">
        <span class="dpr-home-history-header">近 14 天阅读趋势</span>
        <span class="dpr-home-history-meta">
          <span data-dpr-history-range>--</span>
          <span>峰值 <strong data-dpr-history-peak>--</strong></span>
        </span>
        <span class="dpr-home-history-chart" data-dpr-history-chart></span>
      </span>
    </span>
  </div>
</div>

<div class="dpr-home-dashboard-grid">
<section class="dpr-home-dashboard-card dpr-home-report-card">
  <div class="dpr-home-dashboard-header">
    <div>
      <span class="dpr-home-dashboard-kicker">2026-09-21</span>
      <h3 class="dpr-home-dashboard-title">今日汇总</h3>
    </div>
    <strong class="dpr-home-dashboard-count">共 7 篇</strong>
  </div>
  <dl class="dpr-home-dashboard-stats">
    <div class="dpr-home-dashboard-stat"><dt>累计更新</dt><dd>1 次</dd></div>
    <div class="dpr-home-dashboard-stat"><dt>精读</dt><dd>3</dd></div>
    <div class="dpr-home-dashboard-stat"><dt>速读</dt><dd>4</dd></div>
  </dl>
  <p class="dpr-home-dashboard-body">最近更新：2026-09-21 22:42:56 UTC<br>状态：成功</p>
</section>
<section class="dpr-home-dashboard-card dpr-home-brief-card">
  <div class="dpr-home-dashboard-header">
    <div>
      <span class="dpr-home-dashboard-kicker">合并后生成</span>
      <h3 class="dpr-home-dashboard-title">今日简报</h3>
    </div>
    <strong class="dpr-home-dashboard-count">AI</strong>
  </div>
  <div class="dpr-home-dashboard-body">
<p>今天围绕长会话推理的 KV 缓存落位与 Agent 工具调用进度读取，精读了两篇 8.0 分工作，并速览了 4 篇 H100 前缀复用与共享缓存相关研究。最值得看的方向是 KV 缓存在 GPU/CPU/SSD 间的放置策略，以及让服务系统直接读取工具调用进度而非重复猜测。普通读者可优先读这两篇精读，再结合 PrefixBench-H100 了解首字延迟的实测特征。</p>
  </div>
</section>
<section class="dpr-home-dashboard-card dpr-home-deep-card">
  <div class="dpr-home-dashboard-header">
    <div>
      <span class="dpr-home-dashboard-kicker">今日累计</span>
      <h3 class="dpr-home-dashboard-title">精读推荐</h3>
    </div>
    <strong class="dpr-home-dashboard-count">3 篇</strong>
  </div>
  <div class="dpr-home-dashboard-body">
<ul class="dpr-home-dashboard-paper-list"><li><span class="dpr-home-dashboard-paper-title" title="Where Should the KV Cache Live? Placement Policies Across GPU, CPU, and SSD for Long-Lived Sessions">Where Should the KV Cache Live? Placement Policies Across GPU, CPU, and SSD for Long-Lived Sessions</span></li><li><span class="dpr-home-dashboard-paper-title" title="Ask the Tool, Don&#x27;t Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It">Ask the Tool, Don&#x27;t Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It</span></li><li><span class="dpr-home-dashboard-paper-title" title="Decomposing Predictive Kubernetes Autoscaling for Large Language Model Serving Under Long Startup Delays">Decomposing Predictive Kubernetes Autoscaling for Large Language Model Serving Under Long Startup Delays</span></li></ul>
  </div>
  <div class="dpr-home-dashboard-tags"><span class="dpr-home-dashboard-tag">awc <strong>1</strong></span><span class="dpr-home-dashboard-tag">cold-start <strong>1</strong></span><span class="dpr-home-dashboard-tag">mas-cache <strong>1</strong></span></div>
</section>
<section class="dpr-home-dashboard-card dpr-home-skim-card">
  <div class="dpr-home-dashboard-header">
    <div>
      <span class="dpr-home-dashboard-kicker">今日累计</span>
      <h3 class="dpr-home-dashboard-title">速读推荐</h3>
    </div>
    <strong class="dpr-home-dashboard-count">4 篇</strong>
  </div>
  <div class="dpr-home-dashboard-body">
<ul class="dpr-home-dashboard-paper-list"><li><span class="dpr-home-dashboard-paper-title" title="PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving">PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving</span></li><li><span class="dpr-home-dashboard-paper-title" title="Shared KV Caching for Replicated 27B Inference: Correctness Failures and Performance Boundaries">Shared KV Caching for Replicated 27B Inference: Correctness Failures and Performance Boundaries</span></li><li><span class="dpr-home-dashboard-paper-title" title="Marginal utility, matrix factorization, and the Key-Value (KV) cache: a unified information-economic framework for sovereign geo-mining inference">Marginal utility, matrix factorization, and the Key-Value (KV) cache: a unified information-economic framework for sovereign geo-mining inference</span></li></ul>
  </div>
  <div class="dpr-home-dashboard-tags"><span class="dpr-home-dashboard-tag">cache-reuse <strong>2</strong></span><span class="dpr-home-dashboard-tag">awc <strong>1</strong></span><span class="dpr-home-dashboard-tag">mas-cache <strong>1</strong></span></div>
</section>
</div>

<div class="dpr-home-promo-card dpr-home-panel">
  <div class="dpr-home-panel-header">
    <h3 class="dpr-home-promo-title">社区与支持</h3>
  </div>
  <p class="dpr-home-promo-copy">欢迎通过 Star、Fork、Issue 或 PR 一起完善 Daily Paper Reader。</p>
  <div class="dpr-home-promo-meta">
    <span>QQ群 <strong>583867967</strong></span>
    <span class="dpr-home-promo-separator" aria-hidden="true">·</span>
    <span>已有 <strong>1,491</strong> 人参与交流</span>
  </div>
</div>
