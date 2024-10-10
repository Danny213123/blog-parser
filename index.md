---
title: ROCm Blogs
myst:
  html_meta:
    "description lang=en": "AMD ROCm™ software blogs"
    "keywords": "AMD GPU, MI300, MI250, ROCm, blog"
    "property=og:locale": "en_US"
---

<!--
Updated August 29 2024
-->

<h1><a href="blog/atom.xml"><i class="fa fa-rss fa-rotate-270"></i></a> AMD ROCm™ Blogs</h1>

<script>
  const buttonWrapper = document.getElementById('buttonWrapper');

  const observer = new MutationObserver((mutationsList) => {
    for (const mutation of mutationsList) {
      if (mutation.type === 'attributes' && mutation.attributeName === 'data-mode') {
        console.log(`Data mode changed to: ${newMode}`);
        if (newMode === 'light') {
          buttonWrapper.style.setProperty('--original-background', 'white');
          buttonWrapper.style.setProperty('--hover-background-colour', 'white');
        } else {
          buttonWrapper.style.setProperty('--original-background', 'black');
          buttonWrapper.style.setProperty('--hover-background-colour', 'black');
        }
      }
    }
  });
</script>

<style>
  .bd-main .bd-content .bd-article-container {
    max-width: 100%;
  }
  .bd-sidebar-secondary {
    display: none;
  }
  .sd-card-large.sd-card {}
  #buttonWrapper:hover {
    border-color: hsla(231, 99%, 66%, 1);
    transform: scale(1.05);
    background-color: var(--hover-background-colour);
  }
  .small-sd-card-large.sd-card {}
  #buttonWrapper:hover {
    border-color: hsla(231, 99%, 66%, 1);
    transform: scale(1.05);
    background-color: var(--hover-background-colour);
  }
  #buttonWrapper {
    border-color: #A9A9A9;
    background-color: var(--original-background)
    text-align: center;
    font-weight: bold;
    font-size: 12px;
    border-radius: 1px;
    transition: transform 0.2s, border-color 0.2s;
  }
  h2 {
    margin: 0;
    font-size: 1.5em;
  }
  .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    box-sizing: border-box;
    width: 100%;
  }
  .read-more-btn {
    font-size: 20px;
    padding: 10px;
    font-weight: bold;
    cursor: pointer;
    display: inline-block;
    align-items: center;
    text-decoration: none;
    overflow: hidden;
    gap: 7px;
    display: block;
    text-align: left;
    margin-left: 0;
    margin-top: 10px;
  }
  .read-more-btn-small {
    font-size: 15px;
    padding: 10px;
    font-weight: bold;
    cursor: pointer;
    display: inline-block;
    align-items: center;
    text-decoration: none;
    overflow: hidden;
    gap: 7px;
    display: block;
    text-align: left;
    margin-left: 0;
    margin-top: 10px;
  }
  .arrows {
    font-size: 20px;
    display: inline-block;
    font-weight: bold;
    transition: transform 0.3s ease, color 0.3s ease, font-size 0.3s ease;
  }
  .read-more-btn:hover .arrows {
    transform: translateX(8px);
  }
  .arrows-small {
    font-size: 15px;
    display: inline-block;
    font-weight: bold;
    transition: transform 0.3s ease, color 0.3s ease, font-size 0.3s ease;
  }
  .read-more-btn-small:hover .arrows-small {
    transform: translateX(10px);
  }
  .date {
    font-size: 13px;
    font-weight: 300;
    line-height: 22.5px;
    text-transform: none;
    margin-bottom: 10px;
  }
  .paragraph {
    font-size: 16px;
    line-height: 24px;
    margin-bottom: 10px;
  }
  .large-sd-card-img-top.sd-card-img-top {
    width: 100%;
    height: 21vw;
    object-fit: cover;
  }
  .small-sd-card-img-top.sd-card-img-top {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .large-sd-card.sd-card-body {
    width: 100%;
    height: 15%;
  }
  .small-sd-card.sd-card-body {
    width: 100%;
    height: 0;
    display: none;
  }
  .bd-content .sd-card .sd-card-footer {
    border-top: none;
  }
  .card-header {
    font-size: 16px;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    line-height: 1.4;
    margin-bottom: 10px;
  }
  .paragraph {
    font-size: 12px;
    font-family: 'Arial', sans-serif;
    line-height: 1.4;
    margin-bottom: 10px;
  }
</style>

<div class="container">
  <h2>Ecosystems and partners</h2>
  <a href="blog/category/ecosystems-and-partners.html">
    <button id="buttonWrapper">
      See All >>
    </button>
  </a>
</div>

::::{grid} 1 2 2 3
:margin 2

:::{grid-item-card}
:padding: 1
:link: ./ecosystems-and-partners/stone-ridge/README
:link-type: doc
:img-top: ./images/stone-ridge.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card

+++
<a href=".\ecosystems-and-partners\stone-ridge\README.html" class="card-header-link">
  <h2 class="card-header">Stone Ridge Expands Reservoir Simulation Options with AMD Instinct™ Accelerators</h2>
</a>
<p class="paragraph">Stone Ridge Technology (SRT) pioneered the use of GPUs for high performance reservoir simulation (HPC) nearly a decade ago with ECHELON...</p>
<div class="date">June 10, 2024</div>
:::

:::{grid-item-card}
:padding: 1
:link: ./ecosystems-and-partners/university-of-michigan/README
:link-type: doc
:img-top: ./images/university-of-michigan-bioinformatics.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card

+++
<a href="./ecosystems-and-partners/university-of-michigan/README.html" class="card-header-link">
  <h2 class="card-header">AMD Collaboration with the University of Michigan!</h2>
</a>
<p class="paragraph">Long read DNA sequencing technology is revolutionizing genetic diagnostics and precision medicine by helping us discover structural variants and assem... </p>
<div class="date">May 16, 2024</div>
:::

:::{grid-item-card}
:padding: 1
:link: ./ecosystems-and-partners/Siemens/README
:link-type: doc
:img-top: ./images/siemens.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card

+++
<a href="./ecosystems-and-partners/Siemens/README.html" class="card-header-link">
  <h2 class="card-header">Explore AMD Collaboration with Siemens on Simcenter STAR-CCM+</h2>
</a>
<p class="paragraph">Siemens recently announced that its Simcenter STAR-CCM+ multi-physics computational fluid dynamics (CFD) software now supports AMD Instinct™ GPUs... </p>
<div class="date">May 16, 2024</div>
:::
::::

<div class="container">
  <h2>Recent Posts</h2>
  <a href="blog.html">
    <button id="buttonWrapper">
      See All >>
    </button>
  </a>
</div>

::::{grid} 1 2 2 3
:margin 2

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/jax-triton/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/jax-triton/README.html" class="small-card-header-link">
    <h2 class="card-header">Supercharging JAX with Triton Kernels on AMD GPUs</h2>
</a>
<p class="paragraph">In this blog post we guide you through developing a fused dropout activation kernel for matrices in Triton, calling the kernel from JAX, and benchmark...</p>
<div class="date">October 09, 2024 by <a href="./authors\clint-greene.html">Clint Greene</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/int8-quantization/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/int8-quantization/README.html" class="small-card-header-link">
    <h2 class="card-header">Leaner LLM Inference with INT8 Quantization on AMD GPUs using PyTorch</h2>
</a>
<p class="paragraph">This blog demonstrates how to use AMD GPUs to implement and evaluate INT8 quantization, and the derived inference speed-up of Llama family and Mistral...</p>
<div class="date">October 03, 2024 by <a href="./authors\douglas-jia.html">Douglas Jia</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./software-tools-optimization/amd-smi-overview/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./software-tools-optimization/amd-smi-overview/README.html" class="small-card-header-link">
    <h2 class="card-header">Getting to Know Your GPU: A Deep Dive into AMD SMI</h2>
</a>
<p class="paragraph">This post introduces AMD System Management Interface (amd-smi), explaining how you can use it to access your GPU’s performance and status data...        </p>
<div class="date">September 17, 2024 by <a href="./authors\matt-elliott.html">Matt Elliott</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./software-tools-optimization/rocm-offline-installer/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./software-tools-optimization/rocm-offline-installer/README.html" class="small-card-header-link">
    <h2 class="card-header">Introducing the AMD ROCm™ Offline Installer Creator: Simplifying Deployment for AI and HPC</h2>
</a>
<p class="paragraph">Presenting and demonstrating the use of the ROCm Offline Installer Creator, a tool enabling simple deployment of ROCm in disconnected environments in ...</p>
<div class="date">September 10, 2024 by <a href="./authors\matt-elliott.html">Matt Elliott</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/jax-mixed-precision/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/jax-mixed-precision/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Guide to modify our JAX-based nanoGPT model for mixed-precision training, optimizing speed and efficiency on AMD GPUs with ROCm....                      </p>
<div class="date">September 06, 2024 by <a href="./authors\douglas-jia.html">Douglas Jia</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/image-classification/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/image-classification/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Image Classification with BEiT, MobileNet, and EfficientNet on AMD GPU...                                                                                </p>
<div class="date">September 03, 2024 by <a href="./authors\vara-lakshmi-bayanagari.html">Vara Lakshmi Bayanagari</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./high-performance-computing/seismic-stencils/part-1/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./high-performance-computing/seismic-stencils/part-1/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Seismic Stencil Codes - Part 1...                                                                                                                        </p>
<div class="date">August 29, 2024 by <a href="./authors\justin-chang.html">Justin Chang</a>, Ossian O'Reilly</div>
:::

:::{grid-item-card}
:padding: 1
:link: ./high-performance-computing/seismic-stencils/part-2/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./high-performance-computing/seismic-stencils/part-2/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Seismic Stencil Codes - Part 1...                                                                                                                        </p>
<div class="date">August 29, 2024 by <a href="./authors\justin-chang.html">Justin Chang</a>, Ossian O'Reilly</div>
:::

:::{grid-item-card}
:padding: 1
:link: ./high-performance-computing/seismic-stencils/part-3/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./high-performance-computing/seismic-stencils/part-3/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Seismic Stencil Codes - Part 1...                                                                                                                        </p>
<div class="date">August 29, 2024 by <a href="./authors\justin-chang.html">Justin Chang</a>, Ossian O'Reilly</div>
:::

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/mlperf-inf-4-1/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/mlperf-inf-4-1/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Benchmarking Machine Learning using ROCm and AMD GPUs: Reproducing Our MLPerf Inference Submission...                                                    </p>
<div class="date">August 28, 2024 by Meena Arunachalam, Miro Hodak, Jeremy Arnold, <a href="./authors\eliot-li.html">Eliot Li</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/llm-tasks/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/llm-tasks/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Performing natural language processing tasks with LLMs on ROCm running on AMD GPUs...                                                                    </p>
<div class="date">August 21, 2024 by <a href="./authors\eliot-li.html">Eliot Li</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/timeseries_transformers/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/timeseries_transformers/README.html" class="small-card-header-link">
    <h2 class="card-header">Using AMD GPUs for Enhanced Time Series Forecasting with Transformers.</h2>
</a>
<p class="paragraph">Time series forecasting (TSF) predicts future behavior using past data. This guide focuses on implementing Transformers for TSF, covering preprocessin...</p>
<div class="date">August 19, 2024 by <a href="./authors\fabricio-flores.html">Fabricio Flores</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/grok1/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/grok1/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Inferencing with Grok-1 on AMD GPUs...                                                                                                                   </p>
<div class="date">August 09, 2024 by <a href="./authors\eliot-li.html">Eliot Li</a>, <a href="./authors\luise-chen.html">Luise Chen</a>, <a href="./authors\lei-shao.html">Lei Shao</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./artificial-intelligence/roberta_amp/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./artificial-intelligence/roberta_amp/README.html" class="small-card-header-link">
    <h2 class="card-header">Optimizing RoBERTa: Fine-Tuning with Mixed Precision on AMD</h2>
</a>
<p class="paragraph">No Description...                                                                                                                                        </p>
<div class="date">July 29, 2024 by <a href="./authors\fabricio-flores.html">Fabricio Flores</a></div>
:::

:::{grid-item-card}
:padding: 1
:link: ./high-performance-computing/graphs/README
:link-type: doc
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
+++
<a href="./high-performance-computing/graphs/README.html" class="small-card-header-link">
    <h2 class="card-header">No Title</h2>
</a>
<p class="paragraph">Graph analytics on AMD GPUs using Gunrock...                                                                                                             </p>
<div class="date">July 29, 2024 by <a href="./authors\thomas-gibson.html">Thomas Gibson</a>, <a href="./authors\muhammad-osama.html">Muhammad Osama</a></div>
:::

::::

<h2> Stay informed</h2>
<ul>
  <li><a href="blog/atom.xml"> Subscribe to our <i class="fa fa-rss fa-rotate-270"></i> RSS feed</a></li>
  <li><a href="https://github.com/ROCm/rocm-blogs"> Watch our GitHub repo </a></li>
</ul>
