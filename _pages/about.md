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
I have published more than 10 papers at the top international AI conferences or articles with total <a href='https://scholar.google.com/citations?user=r5fgeWQAAAAJ'>google scholar citations <strong><span id='total_cit'>60+</span></strong></a> (<a href="https://scholar.google.com/citations?user=r5fgeWQAAAAJ"><img src="https://img.shields.io/badge/citations-60-blue?logo=googlescholar&logoColor=green&labelColor=f6f6f6&style=flat" alt="Google Scholar"></a>).

Feel free to reach me at weichen_work@126.com! 😃


# 🔥 News
- *2026.01*: Our paper about *minimum path variance principle for DRE* is accepted to ICLR 2026.
- *2025.10*: Our paper about *diffusion informer for time series modeling* is accepted to Expert Systems With Applications (ESWA).
- *2025.10*: Our paper about *wavelet diffusion for time series modeling* is accepted to IEEE TIM.
- *2025.09*: Our paper about *diffusion modeling acceleration* is accepted to NeurIPS 2025.
- *2025.09*: Our paper about *normalizing flow* is accepted to Pattern Recognition (PR).
- *2025.08*: Our paper about *diffusion models for low-level CV* is accepted to Neurocomputing.
- *2025.05*: Our paper about *stable & efficient density ratio estimation* is accepted to ICML 2025. 
- *2022.02*: Our paper about *efficient continuous normalizing flow* is accepted to CVPR 2022. 

# 📝 Publications 

## Deep Generative Modeling

<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">NeurIPS 2025</div><img src='images/evodiff.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**EVODiff: Entropy-aware Variance Optimized Diffusion Inference**](https://openreview.net/forum?id=rKASv92Myl), Shigui Li, **`Wei Chen`**, Delu Zeng* <a href="#" onclick="copyBib('@conference{li2025evodiff, title={EVODiff: Entropy-aware Variance Optimized Diffusion Inference}, author={Li, Shigui and Chen, Wei and Zeng, Delu}, booktitle={NeurIPS}, year={2025}, url={https://openreview.net/forum?id=rKASv92Myl}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**NeurIPS 2025** \| [**Paper**](https://openreview.net/pdf?id=rKASv92Myl) \| [**Code**](https://github.com/ShiguiLi/EVODiff) \| [**News&#127881;**](https://mp.weixin.qq.com/s/mviiMgexMub_os4oSIdwiQ)

- Introduces an information-theoretic view: successful denoising reduces conditional entropy in reverse transitions.
- Proposes EVODiff, a reference-free diffusion inference framework that optimizes conditional variance to reduce transition and reconstruction errors, improving sample quality and reducing inference cost.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">PR 2025</div><img src='images/eiw_flow.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Entropy-informed weighting channel normalizing flow for deep generative models**](https://doi.org/10.1016/j.patcog.2025.112442), **`Wei Chen`**#, Shian Du#, Shigui Li#, Delu Zeng*, John Paisley <a href="#" onclick="copyBib('@article{chen2025eiwflow, title={Entropy-informed weighting channel normalizing flow for deep generative models}, author={Chen, Wei and Du, Shian and Li, Shigui and Zeng, Delu and Paisley, John}, journal={Pattern Recognition}, year={2025}, publisher={Elsevier}, doi={10.1016/j.patcog.2025.112442}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Pattern Recognition (PR) 2025** \| [**Paper**](https://doi.org/10.1016/j.patcog.2025.112442) \| [**Code**](https://github.com/ShianDu/EIW-Flow)

- Proposes EIW-Flow, enhancing normalizing flows with channel-wise weights and latent variable shuffling.
- Achieves state-of-the-art density estimation with minimal computational overhead.
</div>
</div>


<div class='paper-box'>
<div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">Neurocomputing 2025</div><img src='images/reciprocalla.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process**](https://doi.org/10.1016/j.neucom.2025.131438), Zhiqi Lin, **`Wei Chen`**, Jian Xu, Delu Zeng*, Min Chen <a href="#" onclick="copyBib('@article{lin2025reciprocallallie, title={ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process}, author={Lin, Zhiqi and Chen, Wei and Xu, Jian and Zeng, Delu and Chen, Min}, journal={Neurocomputing}, year={2025}, publisher={Elsevier}, doi={10.1016/j.neucom.2025.131438}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Neurocomputing 2025** \| [**Paper**](https://doi.org/10.1016/j.neucom.2025.131438)

- Proposes a reciprocal diffusion process within DDPM for low-light image enhancement.
- Introduces Luminance Adjustment Block for robust global luminance control.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">CVPR 2022</div><img src='images/toflow.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**To-Flow: Efficient Continuous Normalizing Flows with Temporal Optimization Adjoint with Moving Speed**](https://arxiv.org/abs/2203.10335), Shian Du#, Yihong Luo#, **`Wei Chen`**#, Jian Xu, Delu Zeng* <a href="#" onclick="copyBib('@conference{du2022toflow, title={To-Flow: Efficient Continuous Normalizing Flows with Temporal Optimization Adjoint with Moving Speed}, author={Du, Shian and Luo, Yihong and Chen, Wei and Xu, Jian and Zeng, Delu}, booktitle={CVPR}, year={2022}, url={https://arxiv.org/abs/2203.10335}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**CVPR 2022** \| [**Paper**](https://arxiv.org/abs/2203.10335) \| [**Code**](https://github.com/ShianDu/TO-FLOW)

- CNFs via neural ODEs are costly; To-Flow proposes temporal optimization via coordinate descent.
- Accelerates flow training by about 20% while maintaining performance.
</div>
</div>


## Density Ratio Estimation

<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">ICLR 2026</div><img src='images/minpv.png' alt="MinPV" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Don't Forget Its Variance! The Minimum Path Variance Principle for Accurate and Stable Score-Based DRE**](), **`Wei Chen`**, Jiacheng Li, Shigui Li, Zhiqi Lin, Junmei Yang, John Paisley, Delu Zeng* <a href="#" onclick="copyBib('@conference{chen2026minpv, title={Don\\\"t Forget Its Variance! The Minimum Path Variance Principle for Accurate and Stable Score-Based Density Ratio Estimation}, author={Chen, Wei and Li, Jiacheng and Li, Shigui and Lin, Zhiqi and Yang, Junmei and Paisley, John and Zeng, Delu}, booktitle={ICLR}, year={2026}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**ICLR 2026**

- Resolves the path schedule paradox in score-based DRE by identifying the overlooked path variance term.
- Proposes MinPV Principle with closed-form variance expression for tractable optimization.
- Achieves state-of-the-art results on challenging DRE benchmarks.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">ICML 2025</div><img src='images/d3re.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Dequantified Diffusion-Schrödinger Bridge for Density Ratio Estimation**](https://openreview.net/forum?id=zvyHCOcwsw), **`Wei Chen`**, Shigui Li, Jiacheng Li, Junmei Yang, John Paisley, Delu Zeng* <a href="#" onclick="copyBib('@conference{chen2025d3re, title={Dequantified Diffusion-Schr\\\"odinger Bridge for Density Ratio Estimation}, author={Chen, Wei and Li, Shigui and Li, Jiacheng and Yang, Junmei and Paisley, John and Zeng, Delu}, booktitle={ICML}, year={2025}, url={https://openreview.net/forum?id=zvyHCOcwsw}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**ICML 2025** \| [**Paper**](https://openreview.net/forum?id=zvyHCOcwsw) \| [**Code**](https://github.com/Hoemr/Dequantified-Diffusion-Bridge-Density-Ratio-Estimation.git)

- Proposes D3RE, a unified framework for robust DRE under distribution mismatch.
- Introduces dequantified diffusion/SCHRödinger bridge interpolants for support expansion and stabilized scores.
</div>
</div>


## Time Series Forecast

<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">Neural Computing 2024</div><img src='images/deepara.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**DeepAR-Attention probabilistic prediction for stock price series**](https://doi.org/10.1007/s00521-024-09916-3), Jiacheng Li, **`Wei Chen`**, Zhiheng Zhou, Junmei Yang, Delu Zeng* <a href="#" onclick="copyBib('@article{li2024deeparattention, title={DeepAR-Attention probabilistic prediction for stock price series}, author={Li, Jiacheng and Chen, Wei and Zhou, Zhiheng and Yang, Junmei and Zeng, Delu}, journal={Neural Computing and Applications}, year={2024}, publisher={Springer}, doi={10.1007/s00521-024-09916-3}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Neural Computing and Applications 2024** \| [**Paper**](https://doi.org/10.1007/s00521-024-09916-3)

- Proposes DeepAR-Attention for probabilistic stock price forecasting.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">IEEE IoTJ 2024</div><img src='images/ODE_LSTM.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Neural ordinary differential equation networks for fintech applications using IoT**](https://doi.org/10.1109/JIOT.2024.3376748), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Delu Zeng*, Zhiheng Zhou <a href="#" onclick="copyBib('@article{li2024neuralode, title={Neural ordinary differential equation networks for fintech applications using Internet of Things}, author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zeng, Delu and Zhou, Zhiheng}, journal={IEEE Internet of Things Journal}, year={2024}, publisher={IEEE}, doi={10.1109/JIOT.2024.3376748}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**IEEE Internet of Things Journal (IoTJ) 2024** \| [**Paper**](https://doi.org/10.1109/JIOT.2024.3376748) 

- Develops neural ODE network approaches for fintech applications in IoT settings.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">IEEE T-IM 2025</div><img src='images/evolvinformer.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting**](https://doi.org/10.1109/TIM.2025.3581667), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng* <a href="#" onclick="copyBib('@article{li2025evolvinformer, title={Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting}, author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu}, journal={IEEE Transactions on Instrumentation and Measurement}, year={2025}, publisher={IEEE}, doi={10.1109/TIM.2025.3581667}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**IEEE Transactions on Instrumentation and Measurement (T-IM) 2025** \| [**Paper**](https://doi.org/10.1109/TIM.2025.3581667)

- Proposes EvolvInformer: integrates ODE solver with ProbSparse attention for long-sequence load forecasting.
- Achieves 29.7% MSE reduction while preserving logarithmic memory complexity.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">ESWA 2025</div><img src='images/diffinformer.jpg' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Diffinformer: Diffusion Informer model for long sequence time-series forecasting**](https://doi.org/10.1016/j.eswa.2025.129944), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng* <a href="#" onclick="copyBib('@article{li2025diffinformer, title={Diffinformer: Diffusion Informer model for long sequence time-series forecasting}, author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu}, journal={Expert Systems with Applications}, year={2025}, publisher={Elsevier}, doi={10.1016/j.eswa.2025.129944}}'); return false;" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Expert Systems with Applications (ESWA) 2025** \| [**Paper**](https://doi.org/10.1016/j.eswa.2025.129944)

- Proposes Diffinformer: combines conditional diffusion models with Informer's ProbSparse attention.
- Demonstrates consistent improvements across five large-scale datasets.
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
<div class='paper-box'>
<div class='paper-box-image' style="max-width: 150px;"><img src='images/AIP.png' alt="RIKEN AIP" width="100%"></div>
<div class='paper-box-text' markdown="1">

**RIKEN Center for Advanced Intelligence Project (AIP)** - Tensor Learning Team

*2026.02 - 2026.05*

Mentor: [Qibin Zhao](https://qibinzhao.github.io/) \| [[Team Page](https://qibinzhao.github.io/)]

</div>
</div>

<script>
function copyBib(bib) {
  navigator.clipboard.writeText(bib).then(function() {
    alert('BibTeX copied to clipboard!');
  }, function(err) {
    console.error('Failed to copy: ', err);
  });
}
</script>
