---
title: Arm-based Quadruped and Humanoid Robotics for Physical AI use-cases
description: Design and implement original software systems for low-cost Arm-based quadruped or humanoid robots, demonstrating physical AI through on-device perception, decision-making, and control.
subjects:
- ML
- Performance and Architecture
- Physical AI
- Edge AI
requires-team:
- No
platform:
- AI
- IoT
- Automotive
sw-hw:
- Software
- Hardware
support-level:
- Self-Service
- Arm Ambassador Support
publication-date: 2026-02-06
license:
status:
- Published
badges:
- trending
- recently_added
donation:
layout: article
sidebar:
  nav: projects
full_description: |-
  <img class="image image--xl" src="/Arm-Developer-Labs/images/learn_on_Arm_banner.png" loading="lazy" decoding="async" />

  ## Description

  ### Why is this important?

  [Arm provides a foundational compute platform for Physical AI](https://newsroom.arm.com/blog/the-next-platform-shift-physical-and-edge-ai-powered-by-arm)

  Low-cost Arm-powered robotic platforms — both quadruped and humanoid — are rapidly lowering the barrier to entry for Physical AI: systems that perceive, reason, and act in the real world. Quadruped platforms such as PuppyPi, Waveshare SpotMicro-style robots, OpenDog derivatives, and Raspberry Pi / RK3588-based kits have already made dynamic locomotion accessible. In parallel, compact humanoid and biped platforms are available with Arm-based compute, servo-actuated joints, and open software stacks.

  These robots typically integrate:
  -	Arm CPUs (Cortex-A class, often paired in heterogeneous SoCs with NPUs or GPUs)
  -	Cameras, IMUs, joint encoders, and force sensors
  -	Real-time motor control running alongside Linux-based AI stacks

  This combination makes them ideal testbeds for exploring physical AI under real-world constraints: latency, power, noisy sensors, contact dynamics, and safety-critical control — all running fully on-device, without reliance on cloud inference.

  By leveraging efficient Arm-native ML frameworks (e.g. PyTorch + ExecuTorch, LiteRT, ONNX Runtime, or accelerated ROS 2 pipelines), developers can study how modern AI models behave when tightly coupled to physical embodiment, whether quadrupedal or humanoid. Arm-based systems enable tight perception–action loops, reducing the latency from sensing a photon or audio wave to taking a meaningful physical action.

  **Example Platforms**
  Quadruped 
  - [PuppyPi - Raspberry Pi 4/5](https://www.hiwonder.com/products/puppypi?variant=40213129003095&srsltid=AfmBOoonusv8sBF3hP6LMvyvBAXPVJh7eW0V60FU7IDGaPfYcz7cseXH)
  - [ROSPug - Jetson Nano](https://www.hiwonder.com/products/rospug?srsltid=AfmBOop83H4FhIvFPY9-fYUyQ2a0xrh9-_gfr4aHVuy15X8owRgYV2PL)
  Humanoid / Biped
  - [TonyPi - Raspberry Pi 4/5](https://www.hiwonder.com/products/tonypi?variant=31753114681431&srsltid=AfmBOoosUcEQONClryEw_jPzqkrezui8d5BkTunVcWUTKhbD_xikG_10)
  Boards
  - [Raspberry Pi 4, 5, CM4](https://www.raspberrypi.com/products/compute-module-4/?variant=raspberry-pi-cm4001000)
  - [Rockchip RK3566 or 3588](https://www.waveshare.com/core3566.htm?srsltid=AfmBOorJELpnCGbrB3pV489O_RIOvnExIjj8q84sPlp-N4W3b4_wsfRj)
  - [Nvidia Jetson Nano - Heterogeneous SoC with Arm-powered CPU for control and orchestration](https://www.nvidia.com/en-gb/autonomous-machines/embedded-systems/jetson-nano/product-development/)

  Participants may use off-the-shelf mechanical platforms or open 3D-printable designs. **Mechanical design is not a focus of this project.**


  ### Project Summary

  Design and implement an original software application for a low-cost Arm-based quadruped or humanoid robot that demonstrates intelligent interaction with the physical world.

  This project is **not** about assembling a robot kit, configuring firmware, or running stock demos. Robot platforms are treated as execution targets, not solutions. Each submission must demonstrate original software design and clearly articulated system architecture.

  Your goal is to architect how sensing, perception, inference, decision-making, and control software operate together on Arm hardware under real-world physical constraints.

  Each project must:
  -	Implement a custom software application written by the participant
  -	Define a clear software architecture (modules, data flow, control loops)
  -	Run all AI inference on-device
  -	Integrate inference into a closed-loop control system
  -	Demonstrate measurable impact on physical robot behaviour

  Projects that only run vendor demo code will not be considered sufficient.

  **Example Project Areas**

  Physical AI applications
  - Vision-based locomotion (Terrain classification, obstacle detection, or foothold selection using cameras)
  - Multi-sensor fusion for balance and navigation (Fuse camera, IMU, and joint feedback for state estimation, slip detection, or recovery behaviours)
  - Learning-based control (Neural policies (MLPs or lightweight transformers) for gait adaptation, balance, or stepping)
  - Human–robot interaction (Gesture recognition, visual tracking, or local natural-language command processing).
  - Embodied exploration (Curiosity-driven navigation or semantic mapping in indoor environments).

  Software architecture and optimisation
  -	Designing low-latency perception–decision–action pipelines
  -	Integrating ML inference into real-time control loops
  -	Optimising models for latency, power, and memory footprint
  -	Evaluating different ROS 2 or non-ROS architectural patterns

  Utilise your creativity and try out unusual applications or techniques. Explore different sensor options, frameworks, and robot behaviours. You are welcome to also submit other variants of robotics (e.g. robotic arm, autonomous drones and other vehicles), provided the project demonstrates the same closed-loop, on-device physical AI principles. 

  ## Resources from Arm and our partners
  - Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)
  - Arm / Cambridge University edX course: [AI at the Edge on Arm (Mobile)](https://www.edx.org/learn/computer-science/arm-education-ai-at-the-edge-on-arm)
  - Arm Developer: [Edge AI](https://developer.arm.com/edge-ai)
  - Arm Developer: [Automotive](https://developer.arm.com/automotive)

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of 
  the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/
  developer-program?#register).

  You are also welcome to contact Arm-Developer-Labs@arm.com to enquire about further support.

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and 
  demonstrate earned recognition.

  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

<img class="image image--xl" src="/Arm-Developer-Labs/images/learn_on_Arm_banner.png" loading="lazy" decoding="async" />

## Description

### Why is this important?

[Arm provides a foundational compute platform for Physical AI](https://newsroom.arm.com/blog/the-next-platform-shift-physical-and-edge-ai-powered-by-arm)

Low-cost Arm-powered robotic platforms — both quadruped and humanoid — are rapidly lowering the barrier to entry for Physical AI: systems that perceive, reason, and act in the real world. Quadruped platforms such as PuppyPi, Waveshare SpotMicro-style robots, OpenDog derivatives, and Raspberry Pi / RK3588-based kits have already made dynamic locomotion accessible. In parallel, compact humanoid and biped platforms are available with Arm-based compute, servo-actuated joints, and open software stacks.

These robots typically integrate:
-	Arm CPUs (Cortex-A class, often paired in heterogeneous SoCs with NPUs or GPUs)
-	Cameras, IMUs, joint encoders, and force sensors
-	Real-time motor control running alongside Linux-based AI stacks

This combination makes them ideal testbeds for exploring physical AI under real-world constraints: latency, power, noisy sensors, contact dynamics, and safety-critical control — all running fully on-device, without reliance on cloud inference.

By leveraging efficient Arm-native ML frameworks (e.g. PyTorch + ExecuTorch, LiteRT, ONNX Runtime, or accelerated ROS 2 pipelines), developers can study how modern AI models behave when tightly coupled to physical embodiment, whether quadrupedal or humanoid. Arm-based systems enable tight perception–action loops, reducing the latency from sensing a photon or audio wave to taking a meaningful physical action.

**Example Platforms**
Quadruped 
- [PuppyPi - Raspberry Pi 4/5](https://www.hiwonder.com/products/puppypi?variant=40213129003095&srsltid=AfmBOoonusv8sBF3hP6LMvyvBAXPVJh7eW0V60FU7IDGaPfYcz7cseXH)
- [ROSPug - Jetson Nano](https://www.hiwonder.com/products/rospug?srsltid=AfmBOop83H4FhIvFPY9-fYUyQ2a0xrh9-_gfr4aHVuy15X8owRgYV2PL)
Humanoid / Biped
- [TonyPi - Raspberry Pi 4/5](https://www.hiwonder.com/products/tonypi?variant=31753114681431&srsltid=AfmBOoosUcEQONClryEw_jPzqkrezui8d5BkTunVcWUTKhbD_xikG_10)
Boards
- [Raspberry Pi 4, 5, CM4](https://www.raspberrypi.com/products/compute-module-4/?variant=raspberry-pi-cm4001000)
- [Rockchip RK3566 or 3588](https://www.waveshare.com/core3566.htm?srsltid=AfmBOorJELpnCGbrB3pV489O_RIOvnExIjj8q84sPlp-N4W3b4_wsfRj)
- [Nvidia Jetson Nano - Heterogeneous SoC with Arm-powered CPU for control and orchestration](https://www.nvidia.com/en-gb/autonomous-machines/embedded-systems/jetson-nano/product-development/)

Participants may use off-the-shelf mechanical platforms or open 3D-printable designs. **Mechanical design is not a focus of this project.**


### Project Summary

Design and implement an original software application for a low-cost Arm-based quadruped or humanoid robot that demonstrates intelligent interaction with the physical world.

This project is **not** about assembling a robot kit, configuring firmware, or running stock demos. Robot platforms are treated as execution targets, not solutions. Each submission must demonstrate original software design and clearly articulated system architecture.

Your goal is to architect how sensing, perception, inference, decision-making, and control software operate together on Arm hardware under real-world physical constraints.

Each project must:
-	Implement a custom software application written by the participant
-	Define a clear software architecture (modules, data flow, control loops)
-	Run all AI inference on-device
-	Integrate inference into a closed-loop control system
-	Demonstrate measurable impact on physical robot behaviour

Projects that only run vendor demo code will not be considered sufficient.

**Example Project Areas**

Physical AI applications
- Vision-based locomotion (Terrain classification, obstacle detection, or foothold selection using cameras)
- Multi-sensor fusion for balance and navigation (Fuse camera, IMU, and joint feedback for state estimation, slip detection, or recovery behaviours)
- Learning-based control (Neural policies (MLPs or lightweight transformers) for gait adaptation, balance, or stepping)
- Human–robot interaction (Gesture recognition, visual tracking, or local natural-language command processing).
- Embodied exploration (Curiosity-driven navigation or semantic mapping in indoor environments).

Software architecture and optimisation
-	Designing low-latency perception–decision–action pipelines
-	Integrating ML inference into real-time control loops
-	Optimising models for latency, power, and memory footprint
-	Evaluating different ROS 2 or non-ROS architectural patterns

Utilise your creativity and try out unusual applications or techniques. Explore different sensor options, frameworks, and robot behaviours. You are welcome to also submit other variants of robotics (e.g. robotic arm, autonomous drones and other vehicles), provided the project demonstrates the same closed-loop, on-device physical AI principles. 

## Resources from Arm and our partners
- Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)
- Arm / Cambridge University edX course: [AI at the Edge on Arm (Mobile)](https://www.edx.org/learn/computer-science/arm-education-ai-at-the-edge-on-arm)
- Arm Developer: [Edge AI](https://developer.arm.com/edge-ai)
- Arm Developer: [Automotive](https://developer.arm.com/automotive)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of 
the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/
developer-program?#register).

You are also welcome to contact Arm-Developer-Labs@arm.com to enquire about further support.

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and 
demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.