---
title: "AI-Defined IVI & ADAS Prototyping on Arm-powered Radxa Orion O6"
description: "Modern vehicles are rapidly evolving into AI-defined, software-centric systems, where user experience, safety, and functionality are increasingly shaped by real-time data processing and on-device intelligence rather than fixed-function hardware.
This project involves prototyping an AI-defined IVI system on the Arm-powered Radxa Orion O6."
subjects:
  - "ML"
  - "Performance and Architecture"
  - "Physical AI"
  - "Edge AI"
  - "Graphics"
requires-team:
  - "No"
platform:
  - "AI"
  - "Automotive"
sw-hw:
  - "Software"
  - "Hardware"
support-level:
  - "Self-Service"
  - "Arm Ambassador Support"
publication-date: 2026-02-06
license:
status:
  - "Published"
badges:
  - recently_added
  - trending
donation:
---

## Description

### Why is this important?

Modern vehicles are rapidly evolving into AI-defined, software-centric systems, where intelligence is distributed across the vehicle and behavior is shaped by data, perception, and continuous software updates rather than fixed-function ECUs.

In this context, In-Vehicle Infotainment (IVI) and Advanced Driver Assistance Systems (ADAS) are no longer isolated domains. IVI acts as the primary human–machine interface, while ADAS increasingly relies on AI perception, sensor fusion, and real-time decision support. Together, they form a unified, AI-driven vehicle experience—connecting driver awareness, safety feedback, and contextual information through a common software platform.

These systems must boot quickly, render complex UIs smoothly, handle multimedia reliably, and process AI workloads in real time, all under tight power, thermal, and cost constraints.

Arm-based SoCs underpin most automotive compute platforms. The Radxa Orion O6 provides a practical environment for prototyping AI-defined IVI and ADAS concepts, enabling developers to explore how graphics, system software, and on-device AI inference can coexist on a single edge compute platform.

### Project Summary

The Radxa Orion O6 is a high-performance Armv9 platform featuring Cortex-A720 and Cortex-A520 CPUs, an Arm Immortalis-G720 GPU, the Arm China Zhouyi NPU, and up to 64GB of LPDDR5 memory. While commonly used for Arm-powered workstations, edge servers, and industrial AI deployments, its heterogeneous compute architecture also makes it well suited for automotive prototyping that spans IVI and ADAS workloads.

In this project, participants will prototype an AI-defined vehicle system that demonstrates how IVI and ADAS-style perception and inference can interact within a shared software architecture.

The IVI application should combine:
-	A GPU-accelerated graphical user interface (GUI) acting as the primary human–machine interface
-	Multimedia services such as navigation, vehicle telemetry, video/audio streaming, internet radio, or gaming
-	System-level integration, including boot sequencing, background services, and inter-process communication
-	ADAS-inspired AI/ML-driven functionality that actively shapes system behavior, such as:
       1.	Driver monitoring (e.g. attention, drowsiness, or distraction detection)
       2.	In-cabin perception (e.g. sound classification, occupant presence)
       3.	Context-aware automation (e.g. adaptive UI, media muting, or alerts based on inferred events)

For example, an AI service might analyze camera or audio input and dynamically modify the UI, pause media, or trigger a **simulated** safety alert—illustrating how AI models become first-class components in vehicle software architecture.

A possible development path for an AI-defined IVI and ADAS prototype could be:
1.	Establish a stable platform baseline with verified graphics, audio, input, and system services.
2.	Build a minimal full-screen, GPU-accelerated IVI UI that can restart cleanly and reliably.
3.	Introduce system services incrementally, validating startup order, failure handling, and recovery.
4.	Integrate one or more simulated ADAS or in-cabin AI pipelines, defining clear interfaces between perception, inference, and UI behavior.
5.	Run inference on the CPU initially, with optional acceleration using the onboard NPU, or the GPU (which supports Vulkan)

Creativity is encouraged; this project is about exploring how AI transforms vehicle behavior, not just adding ML as an isolated feature. The emphasis is on understanding architecture and interaction between IVI and ADAS, not on production-grade autonomy.

This project does not aim to implement certified ADAS, functional safety mechanisms, or real-world vehicle control. All ADAS functionality should be simulated or based on recorded data. The focus is rapid prototyping, learning, and architectural exploration.

Extensions
- Multi-display layouts (cluster + center stack)
- Power and boot-time profiling
- Offline-first (no internet connectivity) design considerations


## What will you use?
You should be willing to learn about, or already familiar with:
- Programming: Python or C/C++  
- Modern Linux Graphics stacks (e.g. Wayland/X11, GPU-accelerated UI frameworks)
- Multimedia pipelines
- System service integration and communication
- ML/AI inference at the edge and in physical systems


## Resources from Arm and our partners
- [Radxa Orion O6](https://radxa.com/products/orion/o6/)
- [Radxa Orion O6 Documentation](https://radxa.com/products/orion/o6/#documentation)
- [Arm Learning Paths](https://learn.arm.com/)
- [Arm Courses, EdKits, and other Education Resources](https://arm-university.github.io/online-resources-arm/)
- [Arm Developer - Automotive](https://developer.arm.com/automotive)


## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

You are also welcome to contact Arm-Developer-Labs@arm.com to enquire about further support.

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
