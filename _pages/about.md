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

My research focuses on probabilistic inference and generation, including **deep generative modeling** and **density ratio estimation** (DRE), with particular interests in diffusion models, normalizing flows, and stochastic interpolation. I aim to develop mathematically grounded methods for probabilistic inference. Recently, I am also interested in applying DRE to large language model (LLM) alignment and safety. 
I have published papers at top AI conferences (ICLR, NeurIPS, ICML, CVPR) and journals (IEEE T-IM, PR, Neurocomputing, ESWA). <a href="https://scholar.google.com/citations?user=r5fgeWQAAAAJ"><img id='gs-badge' src="https://img.shields.io/badge/citations-80-blue?logo=googlescholar&logoColor=green&labelColor=f6f6f6&style=flat" alt="Google Scholar"></a>

Feel free to reach me at 📧 <a href="mailto:weichen.work&#64;qq.com">weichen.work&#64;qq.com</a> / <a href="mailto:weichen_work&#64;126.com">weichen_work&#64;126.com</a>.


# 🔥 News
<ul style="max-height: 300px; overflow-y: auto; padding-right: 10px; padding-left: 20px; scrollbar-width: thin; scrollbar-color: #888 #f0f0f0; margin: 0;">
<li style="margin-bottom: 8px;">2026.01: Our paper about <em>minimum path variance principle for DRE</em> is accepted to <strong style="color: #d32f2f;">ICLR 2026</strong>.</li>
<li style="margin-bottom: 8px;">2025.10: Our paper about <em>diffusion informer for time series modeling</em> is accepted to Expert Systems With Applications (ESWA).</li>
<li style="margin-bottom: 8px;">2025.10: Our paper about <em>wavelet diffusion for time series modeling</em> is accepted to IEEE T-IM.</li>
<li style="margin-bottom: 8px;">2025.09: Our paper about <em>diffusion modeling acceleration</em> is accepted to <strong style="color: #d32f2f;">NeurIPS 2025</strong>.</li>
<li style="margin-bottom: 8px;">2025.09: Our paper about <em>normalizing flow</em> is accepted to Pattern Recognition (PR).</li>
<li style="margin-bottom: 8px;">2025.08: Our paper about <em>diffusion models for low-level CV</em> is accepted to Neurocomputing.</li>
<li style="margin-bottom: 8px;">2025.05: Our paper about <em>stable & efficient density ratio estimation</em> is accepted to <strong style="color: #d32f2f;">ICML 2025</strong>.</li>
<li style="margin-bottom: 8px;">2022.02: Our paper about <em>efficient continuous normalizing flow</em> is accepted to <strong style="color: #d32f2f;">CVPR 2022</strong>.</li>
</ul>

# 📝 Publications 

## Deep Generative Modeling

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">NeurIPS 2025</div>
<img src="images/evodiff.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**EVODiff: Entropy-aware Variance Optimized Diffusion Inference**](https://openreview.net/forum?id=rKASv92Myl), Shigui Li, **`Wei Chen`**, Delu Zeng* <a href="#" onclick="copyBib('li2025evodiff')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**NeurIPS 2025** \| [**Paper**](https://openreview.net/pdf?id=rKASv92Myl) \| [**Code**](https://github.com/ShiguiLi/EVODiff) \| [**News&#127881;**](https://mp.weixin.qq.com/s/mviiMgexMub_os4oSIdwiQ)

- Introduces an information-theoretic view: successful denoising reduces conditional entropy in reverse transitions.
- Proposes EVODiff, a reference-free diffusion inference framework that optimizes conditional variance to reduce transition and reconstruction errors, improving sample quality and reducing inference cost.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">PR 2025</div>
<img src="images/eiw_flow.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Entropy-informed weighting channel normalizing flow for deep generative models**](https://doi.org/10.1016/j.patcog.2025.112442), **`Wei Chen`**#, Shian Du#, Shigui Li#, Delu Zeng*, John Paisley <a href="#" onclick="copyBib('chen2025entropy')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Pattern Recognition (PR) 2025** \| [**Paper**](https://doi.org/10.1016/j.patcog.2025.112442) \| [**Code**](https://github.com/ShianDu/EIW-Flow)

- Proposes EIW-Flow, enhancing normalizing flows with channel-wise weights and latent variable shuffling.
- Achieves state-of-the-art density estimation with minimal computational overhead.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">Neurocomputing 2025</div>
<img src="images/reciprocalla.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process**](https://doi.org/10.1016/j.neucom.2025.131438), Zhiqi Lin, **`Wei Chen`**, Jian Xu, Delu Zeng*, Min Chen <a href="#" onclick="copyBib('lin2025reciprocalla')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Neurocomputing 2025** \| [**Paper**](https://doi.org/10.1016/j.neucom.2025.131438)

- Proposes a reciprocal diffusion process within DDPM for low-light image enhancement.
- Introduces Luminance Adjustment Block for robust global luminance control.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">CVPR 2022</div>
<img src="images/toflow.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**To-Flow: Efficient Continuous Normalizing Flows with Temporal Optimization Adjoint with Moving Speed**](https://arxiv.org/abs/2203.10335), Shian Du#, Yihong Luo#, **`Wei Chen`**#, Jian Xu, Delu Zeng* <a href="#" onclick="copyBib('du2022flow')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**CVPR 2022** \| [**Paper**](https://arxiv.org/abs/2203.10335) \| [**Code**](https://github.com/ShianDu/TO-FLOW)

- CNFs via neural ODEs are costly; To-Flow proposes temporal optimization via coordinate descent.
- Accelerates flow training by about 20% while maintaining performance.
</div>
</div>


## Density Ratio Estimation

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">ICLR 2026</div>
<img src="images/minpv.png" alt="MinPV" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Don't Forget Its Variance! The Minimum Path Variance Principle for Accurate and Stable Score-Based DRE**](https://openreview.net/forum?id=vf16PZJWD1), **`Wei Chen`**, Jiacheng Li, Shigui Li, Zhiqi Lin, Junmei Yang, John Paisley, Delu Zeng* <a href="#" onclick="copyBib('chen2026dont')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**ICLR 2026** \| [**Paper**](https://openreview.net/forum?id=vf16PZJWD1) \| [**Code**]()

- Resolves the path schedule paradox in score-based DRE by identifying the overlooked path variance term.
- Proposes MinPV Principle with closed-form variance expression for tractable optimization.
- Achieves state-of-the-art results on challenging DRE benchmarks.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">ICML 2025</div>
<img src="images/d3re.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Dequantified Diffusion-Schrödinger Bridge for Density Ratio Estimation**](https://openreview.net/forum?id=zvyHCOcwsw), **`Wei Chen`**, Shigui Li, Jiacheng Li, Junmei Yang, John Paisley, Delu Zeng* <a href="#" onclick="copyBib('chen2025dequantified')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**ICML 2025** \| [**Paper**](https://openreview.net/forum?id=zvyHCOcwsw) \| [**Code**](https://github.com/Hoemr/Dequantified-Diffusion-Bridge-Density-Ratio-Estimation.git)

- Proposes D3RE, a unified framework for robust DRE under distribution mismatch.
- Introduces dequantified diffusion/SCHRödinger bridge interpolants for support expansion and stabilized scores.
</div>
</div>


## Time Series Forecast

<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">Neural Computing 2024</div>
<img src="images/deepara.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**DeepAR-Attention probabilistic prediction for stock price series**](https://doi.org/10.1007/s00521-024-09916-3), Jiacheng Li, **`Wei Chen`**, Zhiheng Zhou, Junmei Yang, Delu Zeng* <a href="#" onclick="copyBib('li2024deepar')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**Neural Computing and Applications 2024** \| [**Paper**](https://doi.org/10.1007/s00521-024-09916-3)

- Proposes DeepAR-Attention for probabilistic stock price forecasting.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">IEEE IoTJ 2024</div>
<img src="images/ODE_LSTM.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Neural ordinary differential equation networks for fintech applications using IoT**](https://doi.org/10.1109/JIOT.2024.3376748), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Delu Zeng*, Zhiheng Zhou <a href="#" onclick="copyBib('li2024neural')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**IEEE Internet of Things Journal (IoTJ) 2024** \| [**Paper**](https://doi.org/10.1109/JIOT.2024.3376748) 

- Develops neural ODE network approaches for fintech applications in IoT settings.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">IEEE T-IM 2025</div>
<img src="images/evolvinformer.png" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting**](https://doi.org/10.1109/TIM.2025.3581667), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng* <a href="#" onclick="copyBib('li2025evolvinformer')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**IEEE Trans on Instrumentation and Measurement (T-IM) 2025** \| [**Paper**](https://doi.org/10.1109/TIM.2025.3581667)

- Proposes EvolvInformer: integrates ODE solver with ProbSparse attention for long-sequence load forecasting.
- Achieves 29.7% MSE reduction while preserving logarithmic memory complexity.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">ESWA 2025</div>
<img src="images/diffinformer.jpg" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Generative Self-Supervised Time-Series Forecasting Leveraging Wavelet Diffusion**](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11197480), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng* <a href="#" onclick="copyBib('li2025generative')" style="color: #666; font-size: 0.9em;">[Bib]</a>

**IEEE Trans on Instrumentation and Measurement (T-IM) 2025** \| [**Paper**](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11197480)

- TimeWaveDiff: a lightweight self-supervised framework that integrates wavelet decomposition and diffusion modeling to capture multiscale periodicities and robustly learn complex noise patterns in measurement signals.
- Achieves superior long-term forecasting accuracy with significantly reduced computational cost.
</div>
</div>


<div class="paper-box">
<div class="paper-box-image" style="position: relative;">
<div class="paper-badge" style="position:absolute;top:0;left:0;padding:2px 8px;font-size:12px;font-weight:600;color:white;background:#00369f;z-index:100;border-radius:0 0 4px 0;">ESWA 2025</div>
<img src="images/diffinformer.jpg" alt="sym" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

[**Diffinformer: Diffusion Informer model for long sequence time-series forecasting**](https://doi.org/10.1016/j.eswa.2025.129944), Jiacheng Li, **`Wei Chen`**, Yican Liu, Junmei Yang, Zhiheng Zhou, Delu Zeng* <a href="#" onclick="copyBib('li2025diffinformer')" style="color: #666; font-size: 0.9em;">[Bib]</a>

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
<div class="paper-box">
<div class="paper-box-image" style="max-width: 100px; position: relative;">
<img src="images/AIP.png" alt="RIKEN AIP" style="width:100%;">
</div>
<div class="paper-box-text" markdown="1">

**RIKEN AIP** - Tensor Learning Team

*2026.02 - 2026.05*

Mentor: [Qibin Zhao](https://qibinzhao.github.io/) | [[Team Page](https://qibinzhao.github.io/)]

</div>
</div>

<script>
var bibData = {
  "li2025evodiff": "@inproceedings{li2025evodiff,\n  title={EVODiff: Entropy-aware Variance Optimized Diffusion Inference},\n  author={Shigui Li and Wei Chen and Delu Zeng},\n  booktitle={The Annual Conference on Neural Information Processing Systems},\n  year={2025},\n  url={https://openreview.net/forum?id=rKASv92Myl}\n}",
  "chen2025entropy": "@article{chen2025entropy,\n  title={Entropy-informed weighting channel normalizing flow for deep generative models},\n  author={Chen, Wei and Du, Shian and Li, Shigui and Zeng, Delu and Paisley, John},\n  journal={Pattern Recognition},\n  pages={112442},\n  year={2025},\n  publisher={Elsevier}\n}",
  "lin2025reciprocalla": "@article{lin2025reciprocalla,\n  title={ReciprocalLA-LLIE: Low-light image enhancement with luminance-aware reciprocal diffusion process},\n  author={Lin, Zhiqi and Chen, Wei and Xu, Jian and Zeng, Delu and Chen, Min},\n  journal={Neurocomputing},\n  pages={131438},\n  year={2025},\n  publisher={Elsevier}\n}",
  "du2022flow": "@inproceedings{du2022flow,\n  title={To-flow: Efficient continuous normalizing flows with temporal optimization adjoint with moving speed},\n  author={Du, Shian and Luo, Yihong and Chen, Wei and Xu, Jian and Zeng, Delu},\n  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n  pages={12570--12580},\n  year={2022}\n}",
  "chen2026dont": "@inproceedings{chen2026dont,\n  title={Don't Forget Its Variance! The Minimum Path Variance Principle for Accurate and Stable Score-Based Density Ratio Estimation},\n  author={wei chen and jiacheng li and shigui li and zhiqi lin and junmei yang and john paisley and delu zeng},\n  booktitle={International Conference on Learning Representations},\n  year={2026},\n  url={https://openreview.net/forum?id=vf16PZJWD1}\n}",
  "chen2025dequantified": "@inproceedings{chen2025dequantified,\n  title={Dequantified Diffusion-Schr\\\"odinger Bridge for Density Ratio Estimation},\n  author={Wei Chen and Shigui Li and Jiacheng Li and Junmei Yang and John Paisley and Delu Zeng},\n  booktitle={International Conference on Machine Learning},\n  year={2025},\n  url={https://openreview.net/forum?id=zvyHCOcwsw}\n}",
  "li2024deepar": "@article{li2024deepar,\n  title={DeepAR-Attention probabilistic prediction for stock price series},\n  author={Li, Jiacheng and Chen, Wei and Zhou, Zhiheng and Yang, Junmei and Zeng, Delu},\n  journal={Neural Computing and Applications},\n  volume={36},\n  number={25},\n  pages={15389--15406},\n  year={2024},\n  publisher={Springer}\n}",
  "li2024neural": "@article{li2024neural,\n  title={Neural ordinary differential equation networks for fintech applications using Internet of Things},\n  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zeng, Delu and Zhou, Zhiheng},\n  journal={IEEE Internet of Things Journal},\n  year={2024},\n  publisher={IEEE}\n}",
  "li2025evolvinformer": "@article{li2025evolvinformer,\n  title={Integrating Ordinary Differential Equations with Sparse Attention for Power Load Forecasting},\n  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu},\n  journal={IEEE Transactions on Instrumentation and Measurement},\n  year={2025},\n  publisher={IEEE},\n  doi={10.1109/TIM.2025.3581667}\n}",
  "li2025generative": "@article{li2025generative,\n title={Generative Self-Supervised Time Series Forecasting Leveraging Wavelet Diffusion},\n author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu},\n journal={IEEE Transactions on Instrumentation and Measurement},\n year={2025},\n publisher={IEEE},\n doi={10.1109/TIM.2025.3619658}\n}",
  "li2025diffinformer": "@article{li2025diffinformer,\n  title={Diffinformer: Diffusion Informer model for long sequence time-series forecasting},\n  author={Li, Jiacheng and Chen, Wei and Liu, Yican and Yang, Junmei and Zhou, Zhiheng and Zeng, Delu},\n  journal={Expert Systems with Applications},\n  year={2025},\n  publisher={Elsevier},\n  doi={10.1016/j.eswa.2025.129944}\n}"
};

function copyBib(key) {
  var bib = bibData[key];
  if (bib) {
    navigator.clipboard.writeText(bib).then(function() {
      alert('BibTeX copied to clipboard!');
    }, function(err) {
      console.error('Failed to copy: ', err);
    });
  }
}
</script>
