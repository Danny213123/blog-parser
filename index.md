---
title: ROCm Blogs
myst:
  html_meta:
    "description lang=en": "AMD ROCm™ software blogs"
    "keywords": "AMD GPU, MI300, MI250, ROCm, blog"
    "property=og:locale": "en_US"
---
<style>

.bd-main .bd-content .bd-article-container {
max-width: 100%;
}
.bd-sidebar-secondary {
display: none;
}

#buttonWrapper:hover {
border-color: hsla(231, 99%, 66%, 1);
transform: scale(1.05);
background-color: var(--hover-background-colour);
}

#buttonWrapper:hover {
border-color: hsla(231, 99%, 66%, 1);
transform: scale(1.05);
background-color: var(--hover-background-colour);
}

#buttonWrapper {
border-color: #A9A9A9;
background-color: var(--original-background);
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
max-height: 210px;
object-fit: cover;
}

.large-sd-card.sd-card-body {
width: 100%;
height: 15%;
}

.small-sd-card {
width: 45px;
height: 0;
display: none;
box-shadow: 0 0 50px rgba(0,0,0,0.5);
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
<!--
Updated 2024 October 10
Generated 2025-02-10 10:11:19
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
:img-top: ./artificial-intelligence/training_rocm_pt/images/Training2.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/training_rocm_pt/README.html" class="small-card-header-link">
    <h2 class="card-header">Enhancing AI Training with AMD ROCm Software</h2>
</a>
<p class="paragraph">AMD's GPU training optimizations deliver peak performance for advanced AI models through ROCm software stack....                                         </p>
<div class="date">January 31, 2025 by Emad Barsoum</div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/2025-01-20-gpu-op.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./software-tools-optimization/gpu-operator-exporter/README.html" class="small-card-header-link">
    <h2 class="card-header">Announcing the AMD GPU Operator and Metrics Exporter</h2>
</a>
<p class="paragraph">This post announces the AMD GPU Operator for Kubernetes and and the Device Metrics Exporter, including instructions for getting started with these new...</p>
<div class="date">January 29, 2025 by <a href="././authors/farshad-ghodsian.html">Farshad Ghodsian</a>, <a href="././authors/matt-elliott.html">Matt Elliott</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./artificial-intelligence/LLM_Inference/images/Thumbnail_497.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/LLM_Inference/README.html" class="small-card-header-link">
    <h2 class="card-header">Best practices for competitive inference optimization on AMD Instinct™ MI300X GPUs</h2>
</a>
<p class="paragraph">Learn how to optimize large language model inference using vLLM on AMD's MI300X GPUs for enhanced performance and efficiency....                         </p>
<div class="date">January 29, 2025 by <a href="././authors/andy-luo.html">Andy Luo</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./artificial-intelligence/mosaicml-composer/images/thumbnail-390.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/mosaicml-composer/README.html" class="small-card-header-link">
    <h2 class="card-header">Distributed fine-tuning of MPT-30B using Composer on AMD GPUs</h2>
</a>
<p class="paragraph">This blog uses Composer, a distributed framework, on AMD GPUs to fine-tune MPT-30B in single node as well as multinode...                                </p>
<div class="date">January 28, 2025 by <a href="././authors/vara-lakshmi-bayanagari.html">Vara Lakshmi Bayanagari</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/chip.jpeg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/vision-mamba/README.html" class="small-card-header-link">
    <h2 class="card-header">Vision Mamba on AMD GPU with ROCm</h2>
</a>
<p class="paragraph">This blog explores Vision Mamba (Vim), an innovative and efficient backbone for vision tasks and evaluate its performance on AMD GPUs with ROCm....      </p>
<div class="date">January 24, 2025 by <a href="././authors/sean-song.html">Sean Song</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/2025-01-09-containers.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./software-tools-optimization/rocm-containers/README.html" class="small-card-header-link">
    <h2 class="card-header">Getting started with AMD ROCm containers: from base images to custom solutions</h2>
</a>
<p class="paragraph">Getting started with AMD ROCm containers: from base images to custom solutions...                                                                        </p>
<div class="date">January 16, 2025 by <a href="././authors/matt-elliott.html">Matt Elliott</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./ecosystems-and-partners/ansys-fluent-performance/images/Ansys_Fluent_benchmarks_Blog.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./ecosystems-and-partners/ansys-fluent-performance/README.html" class="small-card-header-link">
    <h2 class="card-header">Boosting Computational Fluid Dynamics Performance with AMD Instinct™ MI300X</h2>
</a>
<p class="paragraph">The blog introduces CFD Ansys Fluent benchmarks and provides hands-on guide on installing and running four different Fluent models on AMD GPUs using R...</p>
<div class="date">January 14, 2025 by Martin Huarte</div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./artificial-intelligence/triton_server_vllm/images/232285500_AMD_EPYC_Siena_beautyshot_02.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/triton_server_vllm/README.html" class="small-card-header-link">
    <h2 class="card-header">Triton Inference Server with vLLM on AMD GPUs</h2>
</a>
<p class="paragraph">This blog provides a how-to guide on setting up a Triton Inference Server with vLLM backend powered by AMD GPUs, showcasing robust performance with se...</p>
<div class="date">January 08, 2025 by <a href="././authors/fabricio-flores.html">Fabricio Flores</a>, Tiffany Mintz, <a href="././authors/eliot-li.html">Eliot Li</a>, Yao Liu, Ted Themistokleous, Brian Pickrell, Vish Vadlamani</div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./artificial-intelligence/image-caption/images/tabby-cat.PNG
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/image-caption/README.html" class="small-card-header-link">
    <h2 class="card-header">Transformer based Encoder-Decoder models for image-captioning on AMD GPUs</h2>
</a>
<p class="paragraph">The blog introduces image captioning and provides hands-on tutorials on three different Transformer-based encoder-decoder image captioning models: ViT...</p>
<div class="date">December 03, 2024 by <a href="././authors/vara-lakshmi-bayanagari.html">Vara Lakshmi Bayanagari</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./ecosystems-and-partners/fortran-journey/images/Next-Gen-Fortran.jpeg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./ecosystems-and-partners/fortran-journey/README.html" class="small-card-header-link">
    <h2 class="card-header">Introducing AMD's Next-Gen Fortran Compiler</h2>
</a>
<p class="paragraph">In this post we present a brief preview of AMD's [Next-Gen Fortran Compiler](https://github.com/amd/InfinityHub-CI/blob/main/fortran/README.md), our n...</p>
<div class="date">November 13, 2024 by <a href="././authors/justin-chang.html">Justin Chang</a>, <a href="././authors/brian-cornille.html">Brian Cornille</a>, <a href="././authors/michael-klemm.html">Michael Klemm</a>, <a href="././authors/johanna-potyka.html">Johanna Potyka</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./artificial-intelligence/bnb-8bit/images/precision.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/bnb-8bit/README.html" class="small-card-header-link">
    <h2 class="card-header">Quantized 8-bit LLM training and inference using bitsandbytes on AMD GPUs</h2>
</a>
<p class="paragraph">Learn how to use bitsandbytes’ 8-bit representations techniques, 8-bit optimizer and LLM.int8, to optimize your LLMs training and inference using ROCm...</p>
<div class="date">November 13, 2024 by <a href="././authors/vara-lakshmi-bayanagari.html">Vara Lakshmi Bayanagari</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./artificial-intelligence/sglang/images/cat.jpeg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/sglang/README.html" class="small-card-header-link">
    <h2 class="card-header">SGLang: Fast Serving Framework for Large Language and Vision-Language Models on AMD GPUs</h2>
</a>
<p class="paragraph">Discover SGLang, a fast serving framework designed for large language and vision-language models on AMD GPUs, supporting efficient runtime and a flexi...</p>
<div class="date">November 13, 2024 by <a href="././authors/michael-zhang.html">Michael Zhang</a>, Hai Xiao, Hui Liu, Yineng Zhang</div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./artificial-intelligence/ddp-training-pytorch/images/ddp-amd.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/ddp-training-pytorch/README.html" class="small-card-header-link">
    <h2 class="card-header">Distributed Data Parallel training on AMD GPU with ROCm</h2>
</a>
<p class="paragraph">This blog demonstrates how to speed up the training of a ResNet model on the CIFAR-100 classification task using PyTorch DDP on AMD GPUs with ROCm....   </p>
<div class="date">November 01, 2024 by <a href="././authors/sean-song.html">Sean Song</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/nlp.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/ctranslate2/README.html" class="small-card-header-link">
    <h2 class="card-header">CTranslate2: Efficient Inference with Transformer Models on AMD GPUs</h2>
</a>
<p class="paragraph">Optimizing Transformer models with CTranslate2 for efficient inference on AMD GPUs...                                                                    </p>
<div class="date">October 24, 2024 by <a href="././authors/michael-zhang.html">Michael Zhang</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/torchtune_blog.jpeg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/torchtune/README.html" class="small-card-header-link">
    <h2 class="card-header">Torchtune on AMD GPUs How-To Guide: Fine-tuning and Scaling LLMs with Multi-GPU Power</h2>
</a>
<p class="paragraph">Torchtune is a PyTorch library that enables efficient fine-tuning of LLMs. In this blog we use Torchtune to fine-tune the Llama-3.1-8B model for summa...</p>
<div class="date">October 24, 2024 by <a href="././authors/fabricio-flores.html">Fabricio Flores</a></div>
:::

::::

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
:img-top: ./images/stone-ridge.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./ecosystems-and-partners/stone-ridge/README.html" class="small-card-header-link">
    <h2 class="card-header">Stone Ridge Expands Reservoir Simulation Options with AMD Instinct™ Accelerators</h2>
</a>
<p class="paragraph">Stone Ridge Technology (SRT) pioneered the use of GPUs for high performance reservoir simulation (HPC) nearly a decade ago with ECHELON, its flagship ...</p>
<div class="date">June 10, 2024 </div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/siemens.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./ecosystems-and-partners/Siemens/README.html" class="small-card-header-link">
    <h2 class="card-header">Siemens taps AMD Instinct™ GPUs to expand high-performance hardware options for Simcenter STAR-CCM+</h2>
</a>
<p class="paragraph">Siemens recently announced that its Simcenter STAR-CCM+ multi-physics computational fluid dynamics (CFD) software now supports AMD Instinct™ GPUs for ...</p>
<div class="date">May 16, 2024 </div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/university-of-michigan-bioinformatics.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./ecosystems-and-partners/university-of-michigan/README.html" class="small-card-header-link">
    <h2 class="card-header">AMD Collaboration with the University of Michigan offers High Performance Open-Source Solutions to the Bioinformatics Community</h2>
</a>
<p class="paragraph">We are thrilled to share the success story of a 1.5-year collaboration between AMD and the University of Michigan, Ann Arbor where we used the AMD Ins...</p>
<div class="date">May 16, 2024 </div>
:::

::::

<div class="container">
  <h2>Applications & models</h2>
  <a href="blog/category/applications-models.html">
    <button id="buttonWrapper">
      See All >>
    </button>
  </a>
</div>

::::{grid} 1 2 2 3
:margin 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/2024-10-31-inference-with-llama-3.2-vision.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/llama3_2_vision/README.html" class="small-card-header-link">
    <h2 class="card-header">Inference with Llama 3.2 Vision LLMs on AMD GPUs Using ROCm</h2>
</a>
<p class="paragraph">Meta's Llama 3.2 Vision models bring multimodal capabilities for vision-text tasks. This blog explores leveraging them on AMD GPUs with ROCm for effic...</p>
<div class="date">October 23, 2024 by <a href="././authors/sean-song.html">Sean Song</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./artificial-intelligence/sdxl-multinode-oke/images/multinode-image.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/sdxl-multinode-oke/README.html" class="small-card-header-link">
    <h2 class="card-header">Multinode Fine-Tuning of Stable Diffusion XL on AMD GPUs with Hugging Face Accelerate and OCI's Kubernetes Engine (OKE)</h2>
</a>
<p class="paragraph">This blog demonstrates how to set-up and fine-tune a Stable Diffusion XL (SDXL) model in a multinode Oracle Cloud Infrastructure’s (OCI) Kubernetes En...</p>
<div class="date">October 15, 2024 by <a href="././authors/douglas-jia.html">Douglas Jia</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/thumbnail.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./artificial-intelligence/speculative-decoding/README.html" class="small-card-header-link">
    <h2 class="card-header">Speed Up Text Generation with Speculative Sampling on AMD GPUs</h2>
</a>
<p class="paragraph">This blog will introduce you to assisted text generation using Speculative Sampling. We briefly explain the principles underlying Speculative Sampling...</p>
<div class="date">October 15, 2024 by <a href="././authors/vara-lakshmi-bayanagari.html">Vara Lakshmi Bayanagari</a></div>
:::

::::

<div class="container">
  <h2>Software tools & optimizations</h2>
  <a href="blog/category/software-tools-optimizations.html">
    <button id="buttonWrapper">
      See All >>
    </button>
  </a>
</div>

::::{grid} 1 2 2 3
:margin 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/2024-10-31-amd-smi.jpeg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./software-tools-optimization/amd-smi-overview/README.html" class="small-card-header-link">
    <h2 class="card-header">Getting to Know Your GPU: A Deep Dive into AMD SMI</h2>
</a>
<p class="paragraph">This post introduces AMD System Management Interface (amd-smi), explaining how you can use it to access your GPU’s performance and status data...        </p>
<div class="date">September 17, 2024 by <a href="././authors/matt-elliott.html">Matt Elliott</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/2024-10-31-amd-rocm-offline-installer.jpeg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./software-tools-optimization/rocm-offline-installer/README.html" class="small-card-header-link">
    <h2 class="card-header">Introducing the AMD ROCm™ Offline Installer Creator: Simplifying Deployment for AI and HPC</h2>
</a>
<p class="paragraph">Presenting and demonstrating the use of the ROCm Offline Installer Creator, a tool enabling simple deployment of ROCm in disconnected environments in ...</p>
<div class="date">September 10, 2024 by <a href="././authors/matt-elliott.html">Matt Elliott</a></div>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./software-tools-optimization/tf_profiler/images/tf_profiler_thumbnail.jpeg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="./software-tools-optimization/tf_profiler/README.html" class="small-card-header-link">
    <h2 class="card-header">TensorFlow Profiler in practice: Optimizing TensorFlow models on AMD GPUs.</h2>
</a>
<p class="paragraph">TensorFlow Profiler measures resource use and performance of models, helping identify bottlenecks for optimization. This blog demonstrates the use of ...</p>
<div class="date">June 18, 2024 by <a href="././authors/fabricio-flores.html">Fabricio Flores</a></div>
:::

::::

<h2> Stay informed</h2>
<ul>
  <li><a href="blog/atom.xml"> Subscribe to our <i class="fa fa-rss fa-rotate-270"></i> RSS feed</a></li>
  <li><a href="https://github.com/ROCm/rocm-blogs"> Watch our GitHub repo </a></li>
</ul>
