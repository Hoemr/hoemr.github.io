---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

<div class="diffusion-equation" aria-label="Reverse-time diffusion equation">
  <div class="diffusion-equation__label">reverse-time diffusion</div>
  <div class="diffusion-equation__math">\(\displaystyle
    \mathrm{d}\mathbf{x}_t =
    \left[\mathbf{f}(\mathbf{x}_t,t)-g(t)^2\nabla_{\mathbf{x}}\log p_t(\mathbf{x}_t)\right]\mathrm{d}t
    + g(t)\,\mathrm{d}\bar{\mathbf{w}}_t
  \)</div>
</div>

I received my B.S. degree in Statistics from Wuhan University of Technology (WHUT, 武汉理工大学). Currently, I am a Ph.D. candidate in Computational Mathematics at the School of Mathematics, South China University of Technology (SCUT, 华南理工大学), advised by Prof. [Delu Zeng](https://scholar.google.com.hk/citations?user=08RCdoIAAAAJ&hl=zh-CN). I also collaborate with researchers at **SCUT** ([Junmei Yang](https://dblp.uni-trier.de/pid/157/9330.html), [Min Chen](https://people.ece.ubc.ca/minchen/), [Jiacheng Li](https://openreview.net/profile?id=~Jiacheng_Li9), [Shigui Li](https://scholar.google.com.hk/citations?user=Fm039ikAAAAJ&hl=zh-CN)), **RIKEN-AIP** ([Qibin Zhao](https://qibinzhao.github.io/), [Jian Xu](https://xujianscut.github.io/JianXu.github.io/about/), [Zerui Tao](https://scholar.google.com/citations?hl=zh-CN&user=vcEOMXkAAAAJ), [Yuning Qiu](https://www.researchgate.net/profile/Yuning-Qiu-3), [Chao Li](https://chaoliatriken.github.io/)), **Columbia University** ([John Paisley](https://scholar.google.com.hk/citations?user=r31_fYQAAAAJ)), **University of Waterloo** ([Zhou Wang](https://ece.uwaterloo.ca/~z70wang/)), **Tsinghua University** ([Shian Du](https://shiandu.github.io/)), and **Shanghai Jiaotong University** ([Wenjing Lu](https://scholar.google.com.hk/citations?hl=zh-CN&user=yVw0XEMAAAAJ)).

My research focuses on probabilistic modeling and generation, including **deep generative modeling**, **density ratio estimation** (DRE) and **LLM post-training**, with particular interests in diffusion models, normalizing flows, and stochastic interpolation. I aim to develop mathematically grounded methods for probabilistic inference. Recently, I am also interested in applying DRE to post-training (LLM alignment, preference optimization) for trustworthy and safe LLM. 
I have published papers at top AI conferences (ICLR, NeurIPS, ICML, CVPR) and journals (IEEE T-IM, PR, ESWA, IoTJ, Neurocomputing). 

I also serve as a reviewer for JMLR, ICML, NeurIPS, ICLR, CVPR, ECCV, AAAI, UAI, ACM MM, IEEE T-MM, IEEE T-ETCI, Internet of Things Journal (IoTJ), Expert Systems with Applications (ESWA), EAAI...

Feel free to reach me at 📧 <a href="mailto:weichen.work&#64;qq.com">weichen.work&#64;qq.com</a> / <a href="mailto:weichen001.work&#64;foxmail.com">weichen001.work&#64;foxmail.com</a>.


<span class='anchor' id='news'></span>
# <span class="section-number">01</span> News
<ul class="news-list">
<li>2026.07: Our paper about <em>implicit variational rejection sampling</em> is accepted to <strong>UAI 2026</strong>. <a href="#xu2026implicit">[Paper ↓]</a></li>
<li>2026.05: Our paper about <em>disentangled preference optimization</em> is accepted to <strong>ICML 2026</strong>. <a href="#chen2026towards">[Paper ↓]</a></li>
<li>2026.01: Our paper about <em>minimum path variance principle for DRE</em> is accepted to <strong>ICLR 2026</strong>. <a href="#chen2026a">[Paper ↓]</a></li>
<li>2025.10: Our paper about <em>diffusion informer for time series modeling</em> is accepted to Expert Systems With Applications (ESWA). <a href="#li2025diffinformer">[Paper ↓]</a></li>
<li>2025.10: Our paper about <em>wavelet diffusion for time series modeling</em> is accepted to IEEE T-IM. <a href="#li2025generative">[Paper ↓]</a> <a href="https://mp.weixin.qq.com/s/ITAwphWcT7076ttHctvcaw?scene=1&click_id=4">[News]</a></li>
<li>2025.09: Our paper about <em>diffusion modeling acceleration</em> is accepted to <strong>NeurIPS 2025</strong>. <a href="#li2025evodiff">[Paper ↓]</a> <a href="https://mp.weixin.qq.com/s/mviiMgexMub_os4oSIdwiQ">[News]</a></li>
<li>2025.09: Our paper about <em>normalizing flow</em> is accepted to Pattern Recognition (PR). <a href="#chen2025entropy">[Paper ↓]</a></li>
<li>2025.08: Our paper about <em>diffusion models for low-level CV</em> is accepted to Neurocomputing. <a href="#lin2025reciprocalla">[Paper ↓]</a></li>
<li>2025.05: Our paper about <em>stable & efficient density ratio estimation</em> is accepted to <strong>ICML 2025</strong>. <a href="#chen2025dequantified">[Paper ↓]</a></li>
<li>2022.02: Our paper about <em>efficient continuous normalizing flow</em> is accepted to <strong>CVPR 2022</strong>. <a href="#du2022flow">[Paper ↓]</a></li>
</ul>

<span class='anchor' id='publications'></span>
# <span class="section-number">02</span> Publications

<div class="academic-panel scholar-panel">
  <div class="panel-heading">
    <div class="panel-title">Google Scholar</div>
    <div class="panel-updated">Last updated: <span id="gs-updated">—</span></div>
  </div>
  <div class="metric-grid">
    <div class="metric">
      <div class="metric-value" id="gs-citations">—</div>
      <div class="metric-label">Total Citations</div>
    </div>
    <div class="metric">
      <div class="metric-value" id="gs-hindex">—</div>
      <div class="metric-label">h-index</div>
    </div>
    <div class="metric">
      <div class="metric-value" id="gs-i10index">—</div>
      <div class="metric-label">i10-index</div>
    </div>
    <a class="metric metric-link" href="https://scholar.google.com/citations?user=r5fgeWQAAAAJ" target="_blank" rel="noopener">
      <div class="metric-value">View&nbsp;→</div>
      <div class="metric-label">Profile</div>
    </a>
  </div>
</div>

<div class="academic-panel research-overview">
  <div class="panel-title">Research Overview</div>
  <div class="topic-grid">
    <a href="#" class="filter-link topic-card active" id="filter-all" onclick="showTopic('all'); return false;">
      <div class="topic-card-title">All Papers</div>
      <div class="topic-card-meta">15 papers</div>
    </a>
    <a href="#" class="filter-link topic-card topic-generative" id="filter-generative" onclick="showTopic('generative'); return false;">
      <div class="topic-card-title">Deep Generative Modeling</div>
      <div class="topic-card-meta">5 papers · Diffusion / Variational Inference</div>
    </a>
    <a href="#" class="filter-link topic-card topic-llm" id="filter-llm" onclick="showTopic('llm'); return false;">
      <div class="topic-card-title">LLM Post-Training</div>
      <div class="topic-card-meta">1 paper · Preference Optimization</div>
    </a>
    <a href="#" class="filter-link topic-card topic-dre" id="filter-dre" onclick="showTopic('dre'); return false;">
      <div class="topic-card-title">Density Ratio Estimation</div>
      <div class="topic-card-meta">4 papers · Score-based methods</div>
    </a>
    <a href="#" class="filter-link topic-card topic-ts" id="filter-ts" onclick="showTopic('ts'); return false;">
      <div class="topic-card-title">Time Series Forecast</div>
      <div class="topic-card-meta">5 papers · ODE / Diffusion</div>
    </a>
  </div>
</div>

<span class='anchor' id='deep-generative-modeling'></span>

## Deep Generative Modeling

<div id="section-generative">

<span class='anchor' id='xu2026implicit'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">UAI 2026</div>
<img src="images/ivrs.svg" alt="Implicit Variational Rejection Sampling overview" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Implicit Variational Rejection Sampling**](https://openreview.net/forum?id=fqSPFeDbOU), Jian Xu, Shigui Li, **`Wei Chen`**, Jiacheng Li, Zhiqi Lin, Delu Zeng*, Xinghao Ding, John Paisley, Qibin Zhao* <a href="#" onclick="return copyBib('xu2026implicit', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**UAI 2026** \| [**Paper**](https://openreview.net/forum?id=fqSPFeDbOU) \| [**arXiv**](https://arxiv.org/abs/2606.14235)

- Combines flexible implicit proposal distributions with rejection sampling, using a discriminator to estimate the proposal-to-posterior density ratio.
- Introduces the Implicit Resampling Evidence Lower Bound (IR-ELBO), yielding a tighter variational bound and improved posterior approximation.
</div>
</div>

<span class='anchor' id='li2025evodiff'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">NeurIPS 2025</div>
<img src="images/evodiff.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**EVODiff: Entropy-aware Variance Optimized Diffusion Inference**](https://arxiv.org/abs/2509.26096), Shigui Li, **`Wei Chen`**, Delu Zeng* <a href="#" onclick="return copyBib('li2025evodiff', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**NeurIPS 2025** \| [**Paper**](https://arxiv.org/abs/2509.26096) \| [**Code**](https://github.com/ShiguiLi/EVODiff) \| [**News&#127881;**](https://mp.weixin.qq.com/s/mviiMgexMub_os4oSIdwiQ)

- Proposes EVODiff, a fast inference method for diffusion models that optimizes conditional entropy during denoising.
- Generates higher-quality images with fewer steps (e.g., 25% fewer steps on ImageNet-256) while significantly reducing artifacts.
</div>
</div>


<span class='anchor' id='chen2025entropy'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">PR 2025</div>
<img src="images/eiw_flow.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Entropy-informed weighting channel normalizing flow for deep generative models**](https://doi.org/10.1016/j.patcog.2025.112442), **`Wei Chen`**#, Shian Du#, Shigui Li#, Delu Zeng*, John Paisley <a href="#" onclick="return copyBib('chen2025entropy', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Pattern Recognition (PR) 2025** \| [**Paper**](https://doi.org/10.1016/j.patcog.2025.112442) \| [**Code**](https://github.com/ShianDu/EIW-Flow)

- Proposes EIW-Flow, which adaptively assigns channel-wise weights and shuffles latent variables in normalizing flows.
- Achieves state-of-the-art density estimation on CIFAR-10, CelebA, and ImageNet with negligible extra cost.
</div>
</div>


<span class='anchor' id='lin2025reciprocalla'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">Neurocomputing 2025</div>
<img src="images/reciprocalla.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process**](https://doi.org/10.1016/j.neucom.2025.131438), Zhiqi Lin, **`Wei Chen`**, Jian Xu, Delu Zeng*, Min Chen <a href="#" onclick="return copyBib('lin2025reciprocalla', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Neurocomputing 2025** \| [**Paper**](https://doi.org/10.1016/j.neucom.2025.131438)

- Proposes a reciprocal diffusion process within DDPM that iteratively enhances low-light images.
- Introduces a Luminance Adjustment Block for robust global brightness control, recovering details in dark regions.
</div>
</div>


<span class='anchor' id='du2022flow'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">CVPR 2022</div>
<img src="images/toflow.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**To-Flow: Efficient Continuous Normalizing Flows with Temporal Optimization Adjoint with Moving Speed**](https://arxiv.org/abs/2203.10335), Shian Du#, Yihong Luo#, **`Wei Chen`**#, Jian Xu, Delu Zeng* <a href="#" onclick="return copyBib('du2022flow', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**CVPR 2022** \| [**Paper**](https://arxiv.org/abs/2203.10335) \| [**Code**](https://github.com/ShianDu/TO-FLOW)

- Proposes To-Flow, which optimizes the evolutionary time of neural ODEs via coordinate descent to speed up continuous normalizing flow training.
- Accelerates training by ~20% without sacrificing generation quality, and is compatible with existing regularization methods.
</div>
</div>


</div>

<span class='anchor' id='llm-post-training'></span>

## LLM/MLLM Post-Training

<div id="section-llm">

<span class='anchor' id='chen2026towards'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">ICML 2026</div>
<img src="images/po_db.png" alt="Disentangled Preference Optimization" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Towards Disentangled Preference Optimization Dynamics: Suppress the Loser, Preserve the Winner**](https://openreview.net/pdf?id=TaNH4XiQ6P), **`Wei Chen`**, Yubing Wu, Junmei Yang, Delu Zeng*, Qibin Zhao, John Paisley, Min Chen, Zhou Wang <a href="#" onclick="return copyBib('chen2026towards', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**ICML 2026** \| [**Paper**](https://arxiv.org/pdf/2604.18239) \| [**Code**](https://github.com/IceyWuu/DisentangledPreferenceOptimization)

- Reveals that diverse preference optimization objectives share the same update direction and differ only in two scalar weights, and identifies a simple condition (*disentanglement band*) for the desired learning pathway.
- Proposes a plug-and-play *reward calibration* method that rebalances updates to stay within this band, improving LLM alignment without modifying the base objective.
</div>
</div>


</div>

<span class='anchor' id='density-ratio-estimation'></span>

## Density Ratio Estimation

<div id="section-dre">

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#b45309;z-index:100;border-radius:0 0 4px 0;">Preprint 2026</div>
<img src="images/osdre.png" alt="OS-DRE" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**One-Step Score-Based Density Ratio Estimation**](https://arxiv.org/abs/2604.10672), **`Wei Chen`**, Qibin Zhao, John Paisley, Junmei Yang, Delu Zeng* <a href="#" onclick="return copyBib('chen2026one', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**arXiv 2026** \| [**Paper**](https://arxiv.org/abs/2604.10672) \| [**Code**](https://github.com/Hoemr/OpenDRE)

- Proposes OS-DRE, a solver-free framework that decomposes the time score into spatial and temporal parts, with the temporal part solved analytically.
- Enables accurate density ratio estimation with only *one* function evaluation, combining the speed of classical methods with the accuracy of score-based approaches.
</div>
</div>


<span class='anchor' id='chen2026a'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">ICLR 2026</div>
<img src="images/mvp.jpg" alt="MVP" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**A Minimum Variance Path Principle for Accurate and Stable Score-Based Density Ratio Estimation**](https://arxiv.org/abs/2602.00834), **`Wei Chen`**, Jiacheng Li, Shigui Li, Zhiqi Lin, Junmei Yang, John Paisley, Delu Zeng* <a href="#" onclick="return copyBib('chen2026a', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**ICLR 2026** \| [**Paper**](https://arxiv.org/abs/2602.00834) \| [**Code**]()

- Resolves the path-dependence paradox in score-based methods by identifying the overlooked *path variance* term in training objectives.
- Derives a closed-form variance expression and learns optimal, data-adaptive interpolation paths automatically, achieving state-of-the-art DRE accuracy.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#b45309;z-index:100;border-radius:0 0 4px 0;">Preprint 2025</div>
<img src="images/isadre.png" alt="ISA-DRE" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Diffusion Secant Alignment for Score-Based Density Ratio Estimation**](https://arxiv.org/abs/2509.04852), **`Wei Chen`**, Shigui Li, Jiacheng Li, Jian Xu, Zhiqi Lin, Junmei Yang, Delu Zeng*, John Paisley, Qibin Zhao <a href="#" onclick="return copyBib('chen2025diffusion', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**arXiv 2025** \| [**Paper**](https://arxiv.org/abs/2509.04852) \| [**Code**]()

- Replaces high-variance tangent-based learning targets with their interval integral (*secant*), which is provably lower-variance and smoother for neural networks to learn.
- Achieves accurate density ratio estimation with fewer function evaluations, and handles large distribution discrepancies more robustly than prior methods.
</div>
</div>


<span class='anchor' id='chen2025dequantified'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">ICML 2025</div>
<img src="images/d3re.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Dequantified Diffusion-Schrödinger Bridge for Density Ratio Estimation**](https://arxiv.org/pdf/2505.05034?), **`Wei Chen`**, Shigui Li, Jiacheng Li, Junmei Yang, John Paisley, Delu Zeng* <a href="#" onclick="return copyBib('chen2025dequantified', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**ICML 2025** \| [**Paper**](https://arxiv.org/pdf/2505.05034?) \| [**Code**](https://github.com/Hoemr/Dequantified-Diffusion-Bridge-Density-Ratio-Estimation.git)

- Proposes D3RE, a unified framework that handles the density-chasm and support-chasm problems where existing methods fail.
- Combines diffusion bridges with optimal transport to expand support coverage and stabilize score learning, enabling robust estimation even for very different distributions.
</div>
</div>


</div>

<span class='anchor' id='time-series-forecast'></span>

## Time Series Forecast

<div id="section-ts">

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">Neural Computing 2024</div>
<img src="images/deepara.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**DeepAR-Attention probabilistic prediction for stock price series**](https://doi.org/10.1007/s00521-024-09916-3), Jiacheng Li, **`Wei Chen`**, Zhiheng Zhou, Junmei Yang, Delu Zeng* <a href="#" onclick="return copyBib('li2024deepar', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Neural Computing and Applications 2024** \| [**Paper**](https://doi.org/10.1007/s00521-024-09916-3)

- Proposes DeepAR-Attention, combining DeepAR with attention mechanisms for probabilistic stock price forecasting.
- Captures complex temporal dependencies and provides uncertainty-aware predictions for financial time series.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">IEEE IoTJ 2024</div>
<img src="images/ODE_LSTM.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Neural ordinary differential equation networks for fintech applications using IoT**](https://doi.org/10.1109/JIOT.2024.3376748), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Delu Zeng*, Zhiheng Zhou <a href="#" onclick="return copyBib('li2024neural', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**IEEE Internet of Things Journal (IoTJ) 2024** \| [**Paper**](https://doi.org/10.1109/JIOT.2024.3376748) 

- Develops neural ODE network approaches that model continuous-time dynamics for fintech applications in IoT.
- Captures irregularly sampled financial data more naturally than discrete-time models.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">IEEE T-IM 2025</div>
<img src="images/evolvinformer.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting**](https://doi.org/10.1109/TIM.2025.3581667), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng* <a href="#" onclick="return copyBib('li2025evolvinformer', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**IEEE Trans on Instrumentation and Measurement (T-IM) 2025** \| [**Paper**](https://doi.org/10.1109/TIM.2025.3581667)

- Proposes EvolvInformer, which integrates neural ODE solvers with sparse attention for long-sequence power load forecasting.
- Reduces forecasting error by 29.7% (MSE) while maintaining logarithmic memory complexity.
</div>
</div>


<span class='anchor' id='li2025generative'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">TIM 2025</div>
<img src="images/wavediff.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Generative Self-Supervised Time-Series Forecasting Leveraging Wavelet Diffusion**](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11197480), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng* <a href="#" onclick="return copyBib('li2025generative', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**IEEE Trans on Instrumentation and Measurement (T-IM) 2025** \| [**Paper**](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11197480) \| [**News&#127881;**](https://mp.weixin.qq.com/s/ITAwphWcT7076ttHctvcaw?scene=1&click_id=4)

- Proposes TimeWaveDiff, a lightweight self-supervised framework that combines wavelet decomposition with diffusion modeling for time series.
- Captures multi-scale periodic patterns and achieves superior long-term forecasting accuracy with significantly lower computational cost.
</div>
</div>


<span class='anchor' id='li2025diffinformer'></span>

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">ESWA 2025</div>
<img src="images/diffinformer.jpg" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Diffinformer: Diffusion Informer model for long sequence time-series forecasting**](https://doi.org/10.1016/j.eswa.2025.129944), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng* <a href="#" onclick="return copyBib('li2025diffinformer', event)" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Expert Systems with Applications (ESWA) 2025** \| [**Paper**](https://doi.org/10.1016/j.eswa.2025.129944)

- Proposes Diffinformer, which combines conditional diffusion models with Informer's efficient sparse attention for long-sequence time series forecasting.
- Achieves consistent improvements over existing methods across five large-scale real-world datasets.
</div>
</div>

</div>

<span class='anchor' id='honors'></span>
# <span class="section-number">03</span> Honors and Awards
<div class="quiet-note">
  <div class="entry-title">Highlights</div>
  <div class="entry-meta">More awards are being updated.</div>
  <ul>
    <li><b>2021.10</b> — None</li>
  </ul>
</div>

<span class='anchor' id='education'></span>
# <span class="section-number">04</span> Education
<div class="entry-list">
<div class="profile-entry">
  <img src="images/scut.png" alt="SCUT">
  <div>
    <div class="entry-title">Ph.D. Candidate in Computational Mathematics</div>
    <div class="entry-detail">School of Mathematics, South China University of Technology (SCUT)</div>
    <div class="entry-meta">2022.06 – 2026.06 (now)</div>
  </div>
</div>
<div class="profile-entry">
  <img src="images/scut.png" alt="SCUT">
  <div>
    <div class="entry-title">M.S., Successive Master–Doctor Program in Computational Mathematics</div>
    <div class="entry-detail">School of Mathematics, South China University of Technology (SCUT)</div>
    <div class="entry-meta">2021.09 – 2022.06</div>
  </div>
</div>
<div class="profile-entry">
  <img src="images/whut.png" alt="WHUT">
  <div>
    <div class="entry-title">B.S. in Statistics</div>
    <div class="entry-detail">School of Mathematics and Statistics, Wuhan University of Technology (WHUT)</div>
    <div class="entry-meta">2017.09 – 2021.06</div>
  </div>
</div>
</div>

<span class='anchor' id='talks'></span>
# <span class="section-number">05</span> Invited Talks
<div class="entry-list talk-list">
<div class="talk-entry">
  <div class="entry-title">Invited Talk · University of Waterloo</div>
  <div class="entry-detail"><b>Topic:</b> "From Density Ratios to Preference Dynamics: Diagnosing and Calibrating Preference Optimization"</div>
  <div class="entry-meta">June 30, 2026</div>
</div>
<div class="talk-entry">
  <div class="entry-title">Online Keynote Speaker · University of Waterloo</div>
  <div class="entry-detail"><b>Topic:</b> "One-Step Score-Based Density Ratio Estimation: From 'Accurate or Fast' to 'Accurate and Fast'"</div>
  <div class="entry-meta">Feb 2026</div>
</div>
</div>

<span class='anchor' id='internships'></span>
# <span class="section-number">06</span> Internships
<div class="entry-list">
<div class="profile-entry">
  <img src="images/AIP.png" alt="RIKEN AIP">
  <div>
    <div class="entry-title">RIKEN AIP — Tensor Learning Team</div>
    <div class="entry-meta">2026.02 – 2026.05</div>
    <div class="entry-detail">Supervisor: <a href="https://qibinzhao.github.io/">Qibin Zhao</a> · <a href="https://qibinzhao.github.io/">Team Page</a></div>
  </div>
</div>
</div>

<span class='anchor' id='visitors'></span>
# <span class="section-number">07</span> Visitors
<div class="visitor-counter" data-visitor-counter data-endpoint="{{ site.visitor_counter_endpoint }}">
  <div class="visitor-counter__metric">
    <span class="visitor-counter__symbol">N<sub>unique</sub></span>
    <strong class="visitor-counter__value" data-unique-visitors aria-live="polite">—</strong>
    <span class="visitor-counter__label">all-time visitors</span>
  </div>
  <div class="visitor-counter__metric">
    <span class="visitor-counter__symbol">N<sub>today</sub></span>
    <strong class="visitor-counter__value" data-today-unique aria-live="polite">—</strong>
    <span class="visitor-counter__label">visitors today</span>
  </div>
  <div class="visitor-counter__metric">
    <span class="visitor-counter__symbol">Σ views</span>
    <strong class="visitor-counter__value" data-total-views aria-live="polite">—</strong>
    <span class="visitor-counter__label">page views</span>
  </div>
  <div class="visitor-counter__status" data-counter-status>Loading anonymous visitor statistics…</div>
</div>
<script src="{{ '/assets/js/visitor-counter.js' | relative_url }}" defer></script>

<script>
var bibData = {
  "xu2026implicit": "@inproceedings{xu2026implicit,\n  title={Implicit Variational Rejection Sampling},\n  author={Xu, Jian and Li, Shigui and Chen, Wei and Li, Jiacheng and Lin, Zhiqi and Zeng, Delu and Ding, Xinghao and Paisley, John and Zhao, Qibin},\n  booktitle={Conference on Uncertainty in Artificial Intelligence},\n  year={2026},\n  url={https://openreview.net/forum?id=fqSPFeDbOU}\n}",
  "li2025evodiff": "@inproceedings{li2025evodiff,\n  title={EVODiff: Entropy-aware Variance Optimized Diffusion Inference},\n  author={Shigui Li and Wei Chen and Delu Zeng},\n  booktitle={The Annual Conference on Neural Information Processing Systems},\n  year={2025},\n  url={https://openreview.net/forum?id=rKASv92Myl}\n}",
  "chen2025entropy": "@article{chen2025entropy,\n  title={Entropy-informed weighting channel normalizing flow for deep generative models},\n  author={Chen, Wei and Du, Shian and Li, Shigui and Zeng, Delu and Paisley, John},\n  journal={Pattern Recognition},\n  pages={112442},\n  year={2025},\n  publisher={Elsevier}\n}",
  "lin2025reciprocalla": "@article{lin2025reciprocalla,\n  title={ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process},\n  author={Lin, Zhiqi and Chen, Wei and Xu, Jian and Zeng, Delu and Chen, Min},\n  journal={Neurocomputing},\n  pages={131438},\n  year={2025},\n  publisher={Elsevier}\n}",
  "du2022flow": "@inproceedings{du2022flow,\n  title={To-flow: Efficient continuous normalizing flows with temporal optimization adjoint with moving speed},\n  author={Du, Shian and Luo, Yihong and Chen, Wei and Xu, Jian and Zeng, Delu},\n  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n  pages={12570--12580},\n  year={2022}\n}",
  "chen2026towards": "@inproceedings{chen2026towards,\n title={Towards Disentangled Preference Optimization Dynamics: Suppress the Loser, Preserve the Winner},\n author={Wei Chen and Yubing Wu and Junmei Yang and Delu Zeng and Qibin Zhao and John Paisley and Min Chen and Zhou Wang},\n booktitle={International Conference on Machine Learning},\n year={2026},\n url={https://openreview.net/forum?id=TaNH4XiQ6P}\n}",
  "chen2026a": "@inproceedings{chen2026a,\n  title={A Minimum Variance Path Principle for Accurate and Stable Score-Based Density Ratio Estimation},\n  author={Wei Chen and Jiacheng Li and Shigui Li and Zhiqi Lin and Junmei Yang and John Paisley and Delu Zeng},\n  year={2026},\n  url={https://openreview.net/forum?id=vf16PZJWD1}\n}",
  "chen2026one": "@article{chen2026one,\n  title={One-Step Score-Based Density Ratio Estimation},\n  author={Chen, Wei and Zhao, Qibin and Paisley, John and Yang, Junmei and Zeng, Delu},\n  journal={arXiv preprint arXiv:2604.10672},\n  year={2026}\n}",
  "chen2025diffusion": "@article{chen2025diffusion,\n  title={Diffusion Secant Alignment for Score-Based Density Ratio Estimation},\n  author={Chen, Wei and Li, Shigui and Li, Jiacheng and Xu, Jian and Lin, Zhiqi and Yang, Junmei and Zeng, Delu and Paisley, John and Zhao, Qibin},\n  journal={arXiv preprint arXiv:2509.04852},\n  year={2025}\n}",
  "chen2025dequantified": "@inproceedings{chen2025dequantified,\n  title={Dequantified Diffusion-Schr\\\"odinger Bridge for Density Ratio Estimation},\n  author={Wei Chen and Shigui Li and Jiacheng Li and Junmei Yang and John Paisley and Delu Zeng},\n  booktitle={International Conference on Machine Learning},\n  year={2025},\n  url={https://openreview.net/forum?id=zvyHCOcwsw}\n}",
  "li2024deepar": "@article{li2024deepar,\n  title={DeepAR-Attention probabilistic prediction for stock price series},\n  author={Li, Jiacheng and Chen, Wei and Zhou, Zhiheng and Yang, Junmei and Zeng, Delu},\n  journal={Neural Computing and Applications},\n  volume={36},\n  number={25},\n  pages={15389--15406},\n  year={2024},\n  publisher={Springer}\n}",
  "li2024neural": "@article{li2024neural,\n  title={Neural ordinary differential equation networks for fintech applications using Internet of Things},\n  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zeng, Delu and Zhou, Zhiheng},\n  journal={IEEE Internet of Things Journal},\n  year={2024},\n  publisher={IEEE}\n}",
  "li2025evolvinformer": "@article{li2025evolvinformer,\n  title={Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting},\n  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu},\n  journal={IEEE Transactions on Instrumentation and Measurement},\n  year={2025},\n  publisher={IEEE},\n  doi={10.1109/TIM.2025.3581667}\n}",
  "li2025generative": "@article{li2025generative,\n title={Generative Self-Supervised Time Series Forecasting Leveraging Wavelet Diffusion},\n author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu},\n journal={IEEE Transactions on Instrumentation and Measurement},\n year={2025},\n publisher={IEEE},\n doi={10.1109/TIM.2025.3619658}\n}",
  "li2025diffinformer": "@article{li2025diffinformer,\n  title={Diffinformer: Diffusion Informer model for long sequence time-series forecasting},\n  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu},\n  journal={Expert Systems with Applications},\n  year={2025},\n  publisher={Elsevier},\n  doi={10.1016/j.eswa.2025.129944}\n}"
};

function copyBib(key, event) {
  if (event) {
    event.preventDefault();
  }

  var bib = bibData[key];
  if (bib) {
    navigator.clipboard.writeText(bib).then(function() {
      alert('BibTeX copied to clipboard!');
    }, function(err) {
      console.error('Failed to copy: ', err);
    });
  }

  return false;
}

// Topic filter: anchor-to-topic mapping (for News section links)
var anchorToTopic = {
  'xu2026implicit': 'generative',
  'li2025evodiff': 'generative',
  'chen2025entropy': 'generative',
  'lin2025reciprocalla': 'generative',
  'du2022flow': 'generative',
  'chen2026towards': 'llm',
  'chen2026a': 'dre',
  'li2025diffinformer': 'ts',
  'li2025generative': 'ts',
  'li2025evolvinformer': 'ts',
  'chen2025dequantified': 'dre'
};

var topicSections = {
  'generative': document.getElementById('section-generative'),
  'llm': document.getElementById('section-llm'),
  'dre': document.getElementById('section-dre'),
  'ts': document.getElementById('section-ts')
};

function showTopic(topicId) {
  // Update filter link active state
  var filterLinks = document.querySelectorAll('.filter-link');
  filterLinks.forEach(function(link) { link.classList.remove('active'); });
  var activeLink = document.getElementById('filter-' + topicId);
  if (activeLink) activeLink.classList.add('active');

  if (topicId === 'all') {
    // Show all sections
    Object.values(topicSections).forEach(function(section) {
      if (section) section.classList.remove('topic-hidden');
    });
  } else {
    // Hide all, then show only the selected topic
    Object.values(topicSections).forEach(function(section) {
      if (section) section.classList.add('topic-hidden');
    });
    var targetSection = topicSections[topicId];
    if (targetSection) targetSection.classList.remove('topic-hidden');

    // Scroll to the section anchor
    var sectionAnchors = {
      'generative': 'deep-generative-modeling',
      'llm': 'llm-post-training',
      'dre': 'density-ratio-estimation',
      'ts': 'time-series-forecast'
    };
    var anchorId = sectionAnchors[topicId];
    if (anchorId) {
      var el = document.getElementById(anchorId);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
}

// Handle hash navigation from News section links
window.addEventListener('hashchange', function() {
  var hash = window.location.hash.substring(1);
  if (hash && anchorToTopic[hash]) {
    showTopic(anchorToTopic[hash]);
    // Scroll to the anchor after the section becomes visible
    setTimeout(function() {
      var target = document.getElementById(hash);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 50);
  } else if (hash) {
    // Anchor not in topic mapping (e.g., Research Overview subsection links)
    showTopic('all');
    setTimeout(function() {
      var target = document.getElementById(hash);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 50);
  }
});

// On page load: if URL has a hash, activate the correct topic
document.addEventListener('DOMContentLoaded', function() {
  var hash = window.location.hash.substring(1);
  if (hash && anchorToTopic[hash]) {
    showTopic(anchorToTopic[hash]);
    setTimeout(function() {
      var target = document.getElementById(hash);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
  } else {
    showTopic('all');
  }
});
</script>
