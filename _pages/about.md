---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I received my B.S. degree in Statistics from Wuhan University of Technology (WHUT, 武汉理工大学). Currently, I am a Ph.D. candidate in Computational Mathematics at the School of Mathematics, South China University of Technology (SCUT, 华南理工大学), advised by Prof. [Delu Zeng](https://scholar.google.com.hk/citations?user=08RCdoIAAAAJ&hl=zh-CN). I also collaborate with [John Paisley (Columbia University)](https://scholar.google.com.hk/citations?user=r31_fYQAAAAJ), [Junmei Yang (SCUT)](https://dblp.uni-trier.de/pid/157/9330.html), [Qibin Zhao (RIKEN-AIP)](https://qibinzhao.github.io/), [Jiacheng Li (SCUT)](https://openreview.net/profile?id=~Jiacheng_Li9), [Shigui Li (SCUT)](https://scholar.google.com.hk/citations?user=Fm039ikAAAAJ&hl=zh-CN), [Jian Xu (SCUT / RIKEN-AIP)](https://xujianscut.github.io/JianXu.github.io/about/), [Shian Du (Tsinghua University)](https://shiandu.github.io/).

My research focuses on `deep generative modeling` and `density ratio estimation`, with particular interests in diffusion models, normalizing flows, and stochastic interpolation. I aim to develop mathematically grounded methods for probabilistic inference.
I have published more than 5 papers at the top international AI conferences or articles with total <a href='https://scholar.google.com/citations?user=r5fgeWQAAAAJ'>google scholar citations <strong><span id='total_cit'>50+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=r5fgeWQAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).


# 🔥 News
- *2025.10*: Our paper about *diffusion informer for time series modeling* is accepted to Expert Systems With Applications (ESWA).
- *2025.09*: Our paper about *diffusion modeling acceleration* is accepted to NeurIPS 2025.
- *2025.09*: Our paper about *normalizing flow* is accepted to Pattern Recognition (PR).
- *2025.05*: Our paper about *stable & efficient density ratio estimation* is accepted to ICML 2025. 
- *2022.02*: Our paper about *efficient continuous normalizing flow* is accepted to CVPR 2022. 

# 📝 Publications 

## Deep Generative Modeling

<div class='paper-box'>
<div class='paper-box-text' markdown="1">

**To-Flow: Efficient Continuous Normalizing Flows with Temporal Optimization Adjoint with Moving Speed**, Shian Du#, Yihong Luo#, Wei Chen#, Jian Xu, Delu Zeng*

**CVPR 2022** \| [**Paper**](https://arxiv.org/abs/2203.10335) \| [**Code**](https://github.com/ShianDu/TO-FLOW)

- Continuous normalizing flows (CNFs) via neural ODEs are costly to train on large datasets; To-Flow proposes *temporal optimization* by alternately optimizing network weights and evolutionary time (coordinate descent) with temporal regularization for stability.
- **Key result**: accelerates flow training by about 20% while maintaining performance.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><img src='images/evodiff.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**EVODiff: Entropy-aware Variance Optimized Diffusion Inference**](https://openreview.net/forum?id=rKASv92Myl), Shigui Li, Wei Chen, Delu Zeng*

**NeurIPS 2025** \| [**Code**](https://github.com/ShiguiLi/EVODiff)

- Introduces an information-theoretic view: successful denoising reduces conditional entropy in reverse transitions.
- Proposes EVODiff, a reference-free diffusion inference framework that optimizes conditional variance to reduce transition and reconstruction errors, improving sample quality and reducing inference cost.
</div>
</div>


<div class='paper-box'>
<div class='paper-box-image'><img src='images/reciprocalla.jpg' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process**](https://doi.org/10.1016/j.neucom.2025.131438), Zhiqi Lin, Wei Chen, Jian Xu, Delu Zeng*, Min Chen

**Neurocomputing 2025** \| [**DOI**](https://doi.org/10.1016/j.neucom.2025.131438)

- Proposes a reciprocal diffusion process (between low-light and well-exposed images) within a score-based DDPM framework via drift adjustment, with the low-light image as an endpoint state rather than only a conditional input.
- Introduces a Luminance Adjustment Block for robust global luminance control, suppressing noise and preserving details.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><img src='images/eiw_flow.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Entropy-informed weighting channel normalizing flow for deep generative models**](https://doi.org/10.1016/j.patcog.2025.112442), Wei Chen#, Shian Du#, Shigui Li#, Delu Zeng*, John Paisley

**Pattern Recognition 2025** \| [**DOI**](https://doi.org/10.1016/j.patcog.2025.112442) \| [**Code**](https://github.com/ShianDu/EIW-Flow)

- Proposes Entropy-Informed Weighting Channel Normalizing Flow (EIW-Flow), enhancing multi-scale normalizing flows with a regularized, feature-dependent operation that generates channel-wise weights and shuffles latent variables before splitting.
- Empirically achieves state-of-the-art density estimation and competitive sample quality with minimal computational overhead on multiple benchmarks.
</div>
</div>


## Density Ratio Estimation

<div class='paper-box'><div class='paper-box-image'><img src='images/d3re.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Dequantified Diffusion-Schrödinger Bridge for Density Ratio Estimation**](https://openreview.net/forum?id=zvyHCOcwsw), Wei Chen, Shigui Li, Jiacheng Li, Junmei Yang, John Paisley, Delu Zeng*

**ICML 2025** \| [**Paper**](https://openreview.net/forum?id=zvyHCOcwsw) \| [**Code**](https://github.com/Hoemr/Dequantified-Diffusion-Bridge-Density-Ratio-Estimation.git)

- Proposes D3RE, a unified framework for robust and stable density ratio estimation under distribution mismatch (density-chasm / support-chasm), addressing instability from divergent time scores near boundaries.
- Introduces dequantified diffusion bridge interpolant (DDBI) for support expansion and stabilized time scores; further extends to dequantified Schrödinger bridge interpolant (DSBI) to enhance accuracy and efficiency.
</div>
</div>


## Time Series Forecast

<div class='paper-box'>
<div class='paper-box-text' markdown="1">

**DeepAR-Attention probabilistic prediction for stock price series**, Jiacheng Li, Wei Chen, Zhiheng Zhou, Junmei Yang, Delu Zeng*

**Neural Computing and Applications 2024**

- Proposes a DeepAR-Attention probabilistic forecasting approach for stock price series.
</div>
</div>


<div class='paper-box'>
<div class='paper-box-text' markdown="1">

**Neural ordinary differential equation networks for fintech applications using Internet of Things**, Jiacheng Li, Wei Chen, Yican Liu, Junmei Yang, Delu Zeng*, Zhiheng Zhou

**IEEE Internet of Things Journal 2024**

- Develops neural ODE network approaches for fintech applications in IoT settings.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><img src='images/evolvinformer.jpg' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting**](https://doi.org/10.1109/TIM.2025.3581667), Jiacheng Li, Wei Chen, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng*

**IEEE Transactions on Instrumentation and Measurement 2025** \| [**DOI**](https://doi.org/10.1109/TIM.2025.3581667)

- Proposes EvolvInformer: integrates an ODE solver into a ProbSparse self-attention decoder to model continuous-time hidden state dynamics for nonstationary long-sequence load forecasting.
- Reports a 29.7% MSE reduction versus state-of-the-art baselines while preserving logarithmic memory complexity.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><img src='images/diffinformer.jpg' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Diffinformer: Diffusion Informer model for long sequence time-series forecasting**](https://doi.org/10.1016/j.eswa.2025.129944), Jiacheng Li, Wei Chen, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng*

**Expert Systems with Applications 2025** \| [**DOI**](https://doi.org/10.1016/j.eswa.2025.129944)

- Proposes Diffinformer: combines conditional diffusion models with Informer’s ProbSparse attention distilling mechanism, incorporating diffusion outputs into the decoder to better capture long-range dependencies.
- Demonstrates consistent improvements over corresponding baselines across five large-scale datasets under limited computational resources.
</div>
</div>


# 🎖 Honors and Awards
  - *2021.10* None. 

  # 📖 Educations
  - *2022.06 - 2026.06 (now)*, Ph.D. Candidate in Computational Mathematics, School of Mathematics, South China University of Technology (SCUT). 
  - *2021.09 - 2022.06*, M.S., Successive Master–Doctor Program in Computational Mathematics, School of Mathematics, South China University of Technology (SCUT).
  - *2017.09 - 2021.06*, B.S. in Statistics, School of Mathematics and Statistics, Wuhan University of Technology (WHUT). 

  # 💬 Invited Talks
  - *2021.06*, None. 

  # 💻 Internships
  - *2026.02 - 2026.05*, [Tensor Learning Team of RIKEN AIP](https://qibinzhao.github.io/), Japan.
