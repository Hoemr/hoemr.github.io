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

[**EVODiff: Entropy-aware Variance Optimized Diffusion Inference**](https://openreview.net/forum?id=rKASv92Myl), Shigui Li, **`Wei Chen`**, Delu Zeng*

<details><summary>Bib</summary>

```
@conference{li2025evodiff,
  title={EVODiff: Entropy-aware Variance Optimized Diffusion Inference},
  author={Li, Shigui and Chen, Wei and Zeng, Delu},
  booktitle={NeurIPS},
  year={2025},
  url={https://openreview.net/forum?id=rKASv92Myl}
}
```

</details>

**NeurIPS 2025** \| [**Paper**](https://openreview.net/pdf?id=rKASv92Myl) \| [**Code**](https://github.com/ShiguiLi/EVODiff) \| [**News&#127881;**](https://mp.weixin.qq.com/s/mviiMgexMub_os4oSIdwiQ)

- Introduces an information-theoretic view: successful denoising reduces conditional entropy in reverse transitions.
- Proposes EVODiff, a reference-free diffusion inference framework that optimizes conditional variance to reduce transition and reconstruction errors, improving sample quality and reducing inference cost.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">PR 2025</div><img src='images/eiw_flow.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Entropy-informed weighting channel normalizing flow for deep generative models**](https://doi.org/10.1016/j.patcog.2025.112442), **`Wei Chen`**#, Shian Du#, Shigui Li#, Delu Zeng*, John Paisley

<details><summary>Bib</summary>

```
@article{chen2025eiwflow,
  title={Entropy-informed weighting channel normalizing flow for deep generative models},
  author={Chen, Wei and Du, Shian and Li, Shigui and Zeng, Delu and Paisley, John},
  journal={Pattern Recognition},
  volume={},
  number={},
  pages={},
  year={2025},
  publisher={Elsevier},
  doi={10.1016/j.patcog.2025.112442}
}
```

</details>

**Pattern Recognition (PR) 2025** \| [**Paper**](https://doi.org/10.1016/j.patcog.2025.112442) \| [**Code**](https://github.com/ShianDu/EIW-Flow)

- Proposes Entropy-Informed Weighting Channel Normalizing Flow (EIW-Flow), enhancing multi-scale normalizing flows with a regularized, feature-dependent operation that generates channel-wise weights and shuffles latent variables before splitting.
- Empirically achieves state-of-the-art density estimation and competitive sample quality with minimal computational overhead on multiple benchmarks.
</div>
</div>


<div class='paper-box'>
<div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">Neurocomputing 2025</div><img src='images/reciprocalla.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process**](https://doi.org/10.1016/j.neucom.2025.131438), Zhiqi Lin, **`Wei Chen`**, Jian Xu, Delu Zeng*, Min Chen

<details><summary>Bib</summary>

```
@article{lin2025reciprocallallie,
  title={ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process},
  author={Lin, Zhiqi and Chen, Wei and Xu, Jian and Zeng, Delu and Chen, Min},
  journal={Neurocomputing},
  volume={},
  number={},
  pages={},
  year={2025},
  publisher={Elsevier},
  doi={10.1016/j.neucom.2025.131438}
}
```

</details>

**Neurocomputing 2025** \| [**Paper**](https://doi.org/10.1016/j.neucom.2025.131438)

- Proposes a reciprocal diffusion process (between low-light and well-exposed images) within a score-based DDPM framework via drift adjustment, with the low-light image as an endpoint state rather than only a conditional input.
- Introduces a Luminance Adjustment Block for robust global luminance control, suppressing noise and preserving details.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">CVPR 2022</div><img src='images/toflow.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**To-Flow: Efficient Continuous Normalizing Flows with Temporal Optimization Adjoint with Moving Speed**](https://arxiv.org/abs/2203.10335), Shian Du#, Yihong Luo#, **`Wei Chen`**#, Jian Xu, Delu Zeng*

<details><summary>Bib</summary>

```
@conference{du2022toflow,
  title={To-Flow: Efficient Continuous Normalizing Flows with Temporal Optimization Adjoint with Moving Speed},
  author={Du, Shian and Luo, Yihong and Chen, Wei and Xu, Jian and Zeng, Delu},
  booktitle={CVPR},
  year={2022},
  url={https://arxiv.org/abs/2203.10335}
}
```

</details>

**CVPR 2022** \| [**Paper**](https://arxiv.org/abs/2203.10335) \| [**Code**](https://github.com/ShianDu/TO-FLOW)

- Continuous normalizing flows (CNFs) via neural ODEs are costly to train on large datasets; To-Flow proposes *temporal optimization* by alternately optimizing network weights and evolutionary time (coordinate descent) with temporal regularization for stability.
- **Key result**: accelerates flow training by about 20% while maintaining performance.
</div>
</div>


## Density Ratio Estimation

<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">ICLR 2026</div><div style="width: 100%; height: 200px; background: #f5f5f5; display: flex; align-items: center; justify-content: center; border: 2px dashed #ddd;"><span style="color: #999;">Coming Soon</span></div></div>
<div class='paper-box-text' markdown="1">

[**Don't Forget Its Variance! The Minimum Path Variance Principle for Accurate and Stable Score-Based Density Ratio Estimation**](), **`Wei Chen`**, Jiacheng Li, Shigui Li, Zhiqi Lin, Junmei Yang, John Paisley, Delu Zeng*

<details><summary>Bib</summary>

```
@conference{chen2026dontforgetitsvariance,
  title={Don't Forget Its Variance! The Minimum Path Variance Principle for Accurate and Stable Score-Based Density Ratio Estimation},
  author={Chen, Wei and Li, Jiacheng and Li, Shigui and Lin, Zhiqi and Yang, Junmei and Paisley, John and Zeng, Delu},
  booktitle={ICLR},
  year={2026}
}
```

</details>

**ICLR 2026**

- Score-based methods have emerged as a powerful framework for density ratio estimation (DRE), but they face an important paradox in that, while theoretically path-independent, their practical performance depends critically on the chosen path schedule.
- We resolve this issue by proving that tractable training objectives differ from the ideal, ground-truth objective by a crucial, overlooked term: the path variance of the time score.
- To address this, we propose MinPV (**Min**imum **P**ath **V**ariance) Principle, which introduces a principled heuristic to minimize the overlooked path variance. Our key contribution is the derivation of a closed-form expression for the variance, turning an intractable problem into a tractable optimization.
- By parameterizing the path with a flexible Kumaraswamy Mixture Model, our method learns a data-adaptive, low-variance path without heuristic selection. This principled optimization of the complete objective yields more accurate and stable estimators, establishing new state-of-the-art results on challenging benchmarks.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">ICML 2025</div><img src='images/d3re.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Dequantified Diffusion-Schrödinger Bridge for Density Ratio Estimation**](https://openreview.net/forum?id=zvyHCOcwsw), **`Wei Chen`**, Shigui Li, Jiacheng Li, Junmei Yang, John Paisley, Delu Zeng*

<details><summary>Bib</summary>

```
@conference{chen2025d3re,
  title={Dequantified Diffusion-Schr{\"o}dinger Bridge for Density Ratio Estimation},
  author={Chen, Wei and Li, Shigui and Li, Jiacheng and Yang, Junmei and Paisley, John and Zeng, Delu},
  booktitle={ICML},
  year={2025},
  url={https://openreview.net/forum?id=zvyHCOcwsw}
}
```

</details>

**ICML 2025** \| [**Paper**](https://openreview.net/forum?id=zvyHCOcwsw) \| [**Code**](https://github.com/Hoemr/Dequantified-Diffusion-Bridge-Density-Ratio-Estimation.git)

- Proposes D3RE, a unified framework for robust and stable density ratio estimation under distribution mismatch (density-chasm / support-chasm), addressing instability from divergent time scores near boundaries.
- Introduces dequantified diffusion bridge interpolant (DDBI) for support expansion and stabilized time scores; further extends to dequantified Schrödinger bridge interpolant (DSBI) to enhance accuracy and efficiency.
</div>
</div>


## Time Series Forecast

<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">Neural Computing 2024</div><img src='images/deepara.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**DeepAR-Attention probabilistic prediction for stock price series**](https://doi.org/10.1007/s00521-024-09916-3), Jiacheng Li, **`Wei Chen`**, Zhiheng Zhou, Junmei Yang, Delu Zeng*

<details><summary>Bib</summary>

```
@article{li2024deeparattention,
  title={DeepAR-Attention probabilistic prediction for stock price series},
  author={Li, Jiacheng and Chen, Wei and Zhou, Zhiheng and Yang, Junmei and Zeng, Delu},
  journal={Neural Computing and Applications},
  volume={},
  number={},
  pages={},
  year={2024},
  publisher={Springer},
  doi={10.1007/s00521-024-09916-3}
}
```

</details>

**Neural Computing and Applications 2024** \| [**Paper**](https://doi.org/10.1007/s00521-024-09916-3)

- Proposes a DeepAR-Attention probabilistic forecasting approach for stock price series.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">IEEE IoTJ 2024</div><img src='images/ODE_LSTM.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Neural ordinary differential equation networks for fintech applications using Internet of Things**](https://doi.org/10.1109/JIOT.2024.3376748), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Delu Zeng*, Zhiheng Zhou

<details><summary>Bib</summary>

```
@article{li2024neuralode,
  title={Neural ordinary differential equation networks for fintech applications using Internet of Things},
  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zeng, Delu and Zhou, Zhiheng},
  journal={IEEE Internet of Things Journal},
  volume={},
  number={},
  pages={},
  year={2024},
  publisher={IEEE},
  doi={10.1109/JIOT.2024.3376748}
}
```

</details>

**IEEE Internet of Things Journal (IoTJ) 2024** \| [**Paper**](https://doi.org/10.1109/JIOT.2024.3376748) 

- Develops neural ODE network approaches for fintech applications in IoT settings.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">IEEE T-IM 2025</div><img src='images/evolvinformer.png' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting**](https://doi.org/10.1109/TIM.2025.3581667), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng*

<details><summary>Bib</summary>

```
@article{li2025evolvinformer,
  title={Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting},
  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu},
  journal={IEEE Transactions on Instrumentation and Measurement},
  volume={},
  number={},
  pages={},
  year={2025},
  publisher={IEEE},
  doi={10.1109/TIM.2025.3581667}
}
```

</details>

**IEEE Transactions on Instrumentation and Measurement (T-IM) 2025** \| [**Paper**](https://doi.org/10.1109/TIM.2025.3581667)

- Proposes EvolvInformer: integrates an ODE solver into a ProbSparse self-attention decoder to model continuous-time hidden state dynamics for nonstationary long-sequence load forecasting.
- Reports a 29.7% MSE reduction versus state-of-the-art baselines while preserving logarithmic memory complexity.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div style="position: absolute; top: 0; left: 0; background: #00369f; color: white; padding: 2px 8px; font-size: 12px; font-weight: 600; border-radius: 0 0 4px 0;">ESWA 2025</div><img src='images/diffinformer.jpg' alt="sym" width="100%"></div>
<div class='paper-box-text' markdown="1">

[**Diffinformer: Diffusion Informer model for long sequence time-series forecasting**](https://doi.org/10.1016/j.eswa.2025.129944), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng*

<details><summary>Bib</summary>

```
@article{li2025diffinformer,
  title={Diffinformer: Diffusion Informer model for long sequence time-series forecasting},
  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu},
  journal={Expert Systems with Applications},
  volume={},
  number={},
  pages={},
  year={2025},
  publisher={Elsevier},
  doi={10.1016/j.eswa.2025.129944}
}
```

</details>

**Expert Systems with Applications (ESWA) 2025** \| [**Paper**](https://doi.org/10.1016/j.eswa.2025.129944)

- Proposes Diffinformer: combines conditional diffusion models with Informer's ProbSparse attention distilling mechanism, incorporating diffusion outputs into the decoder to better capture long-range dependencies.
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
<div class='paper-box'>
<div class='paper-box-image'><img src='images/AIP.png' alt="RIKEN AIP" width="100%" style="max-width: 300px;"></div>
<div class='paper-box-text' markdown="1">

**RIKEN Center for Advanced Intelligence Project (AIP)** - Tensor Learning Team

*2026.02 - 2026.05*

Mentor: [Qibin Zhao](https://qibinzhao.github.io/)

[[Team Page](https://qibinzhao.github.io/)]

</div>
</div>
