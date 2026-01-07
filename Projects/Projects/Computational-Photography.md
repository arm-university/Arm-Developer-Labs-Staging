---
title: "Develop a Novel Computational Photography Pipeline"
description: "This self-service project "
subjects:
    - "ML"
    - "Graphics"
requires-team:
    - "No"
platform:
    - "Mobile"
    - "Laptops and Desktops"
    - "AI"
sw-hw:
    - "Software"
support-level: 
    - "Self-Service"
    - "Arm Ambassador Support"
    - "Direct Support from Arm"
publication-date: 2026-01-07
license:
status:
    - "Published" 
donation:

---

![super-resolution](./images/Super-resolution_example_closeup.png)

### Description

**Why this is important?** 

For end users, one of the most important factors when selecting a new smart phone is the camera and the associated features. Features, such as night-mode image or extreme digital zoom leverage neural networks to improve various aspects of an image such as signal-to-noise (SNR) ratio. For example, the Google Pixel 10 Pros new, [pro-res zoom](https://blog.google/products/pixel/google-pixel-pro-res-zoom/) feature uses on-device diffusion models to fill in any missing information with generative AI when zooming in. 

With the availability of Arm's scalable matrix extension (SME2) in commercial handsets, this CPU feature enables more advanced and capable neural networks to run locally on device, allowing more devices to run neural networks as part of their photographic pipeline and enabling a more portable software that isn't written for a specific Neural Processing Unit (NPU).

**Project Summary**

This challenge is to create a novel Computational Photography pipeline on an Arm-based device. This could involve running 

You must implement one of the following pipelines:

- Night-Mode imaging: improving the SNR of photographs taken in low light conditions
- Portrait-Mode image: Applying Bokeh blur effects on the background segments of a portrait photograph
- Neural-Ray denoising:
- Pipeline that leverages GenAI-based models (e.g., style-transfer models)

The objective is to optimize your pipeline for both inference latency and perceived image quality and the technical criteria, of your project, on which you will be judged, are as follows:
- Must use a quantized neural network, preferably less that 16-bits (i.e. quantized to less the FP16)
- Preferably use the [ML Extensions for Vulkan](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/)
- Preferably use the Executorch runtime, designed for running neural networks with the [Arm Neural Technology backend](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/arm-neural-technology-in-executorch-1-0)
- Algorithms should run on an Arm-based CPU with single-instruction multiple data (SIMD) such as [SVE](https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions) or [SME](https://www.arm.com/technologies/sme2) or an [Neural-Graphics](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics) enabled GPU (either simulation or physical handset once available)

## Prerequisites

- Experience with traditional image processing algorithms (e.g., convolution, filters).
- Intermediate experience or willingness to learn about machine learning for graphics and photography (e.g., neural ray denoising).
- Familiarity with build systems and associated tools such as CMake, docker.
- Experience with object-orientated programming and scripting with langauges such as C++ and Python.
- Some experience or willingness to learn about low-level programming and using APIs such as Vulkan.

## Resources from Arm and our partners

- Blog: [Neural Camera Denoising with Arm SME2](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/unlocking-the-power-of-neural-camera-denoising-with-arm-sme2)
- Software: [Reference AI Camera Pipelines](https://gitlab.arm.com/kleidi/kleidi-examples/ai-camera-pipelines)
- Blog: [Neural Graphics](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics)
- Software: [Arm KleidiCV](https://gitlab.arm.com/kleidi/kleidicv)
- Software: [Vkdt open source photography workflow](https://github.com/hanatos/vkdt)
- Blog: [SME2 enabled devices](https://newsroom.arm.com/blog/arm-c1-cpu-cluster-on-device-ai-performance)
- Blog: [Arm Neural Technolog in Executorch 1.0](https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/arm-neural-technology-in-executorch-1-0)
- Tutorial: [Demonstation using Arm VGF backend](https://github.com/pytorch/executorch/blob/main/examples/arm/vgf_minimal_example.ipynb)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register). Additionally, if you would like to engage with this project and need assistance with access to hardware, please email  us at Arm-Developer-Labs@arm.com. 

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.

## Attributions

By User:Omegatron - Created by User:Omegatron using the GIMP, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=1836856




