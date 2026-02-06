---
title: Video & Audio Provenance on Arm in the Age of AI
description: Integrating transparent provenance - disclosing whether media is AI-generated or AI-edited, and also what other AI processing has occurred on any media - is necessary for accountability in domains like journalism, security, and regulated industries. This project uses C2PA 2.3 to record such actions as signed, machine-verifiable assertions attached to the asset. This reduces deepfake proliferation and fraud by providing a method to verify provenance. Additionally it tracks authorised and potential unauthorised use of models to analyse the asset.
subjects:
- ML
- Security
- Edge AI
requires-team:
- No
platform:
- AI
- Laptops and Desktops
sw-hw:
- Software
support-level:
- Self-Service
- Arm Ambassador Support
publication-date: 2026-02-06
license:
status:
- Hidden
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

  Generative AI has created a trust gap:
  - Images, videos, and audio may be AI-generated or heavily manipulated - this can lead to deepfakes, and fraud.
  - This AI-enhancement or editing can occur in real-time - i.e. a person can livestream themeself, but use ML to change their appearance and voice.
  - Moreover, the use of AI models to scan images, video, and audio (e.g. facial or voice recognition) is often opaque, with no actual changes to the underlying data.
  - Viewers rarely know whether AI analysis was performed, or what conclusion was reached.

  Integrating transparent provenance - disclosing whether media is AI-generated or AI-edited, and also what other AI processing has occurred on any media - is necessary for accountability in domains like journalism, security, and regulated industries. This project uses C2PA 2.3 to record such actions as signed, machine-verifiable assertions attached to the asset. This reduces deepfake proliferation and fraud by providing a method to verify provenance. Additionally it tracks authorised and potential unauthorised use of models to analyse the asset.

  [Arm is a founder member of the C2PA Standards Group.](https://newsroom.arm.com/blog/c2pa-fights-disinformation) The Coalition for Content Provenance and Authenticity (C2PA) specification lets creators and platforms attach cryptographically signed metadata to content like:
  - images 📷
  - videos 🎥
  - audio 🎧
  - documents 📄

  That metadata can include:
  -	who created it
  -	what tool was used (camera, Photoshop, generative AI, etc.)
  -	what edits were made and when
  -	whether AI was involved

  Anyone can later verify this info to see if the content is authentic or has been tampered with.

  The best place to start would be with processing on static audio or video files, but we encourage you to ultimately target a streamed data format - i.e. streamed audio or video, and to perform the inference and record the actions in real-time. 

  You should leverage an Arm-powered device, such as a Windows-on-Arm laptop, Apple Silicon MacBook, Arm-powered mobile phone, or Raspberry Pi.


  ### Project Summary

  Build and evaluate a comprehensive AI-augmented audio/video capture and provenance system on an Arm-powered device (e.g. Windows-on-Arm laptop)
  - captures streamed media with a camera or microphone,
  - runs AI models on-device (i.e. face/object/keyword/sentiment detection, upscaling/filters/enhancements),
  - generates C2PA Content Credentials that transparently disclose:
    - which models were run,
  	- their effect/impact on the image or video

  and demonstrates how this provenance enables trust and auditability in real-world use cases such as content integrity validation and responsible media pipelines.

  You should be able to show your source code, along with documentation/instructions/comments, a short demo video or images to show the project in action, and a short document describing your decisions and how you implemented the project.


    ## What will you use?
  You should be willing to learn about, or already familiar with:
  - Programming and building a basic application on your chosen platform/OS
  - C2PA and the concepts behind content provenance and authentication
  - Deploying optimised inference models on Arm-powered CPU via frameworks with KleidiAI integration (e.g. PyTorch)


  ## Resources from Arm and our partners
  - Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)
  - Arm / Cambridge University edX course: [AI at the Edge on Arm (Mobile)](https://www.edx.org/learn/computer-science/arm-education-ai-at-the-edge-on-arm)
  - Learning Path: [Vision LLM Inference on Android with KleidiAI](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/vision-llm-inference-on-android-with-kleidiai-and-mnn/)
  - Learning Path: [Build a Hands-Free Selfie Android Application with MediaPipe](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-android-selfie-app-using-mediapipe-multimodality/)
  - Arm Developer: [Edge AI](https://developer.arm.com/edge-ai)
  - External Documentation: [Windows on Arm Environments – Linaro wiki](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)

  ## Support Level

  This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

  You are also welcome to contact Arm-Developer-Labs@arm.com to enquire about further support.

  ## Benefits 

  Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

  To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.
---

<img class="image image--xl" src="/Arm-Developer-Labs/images/learn_on_Arm_banner.png" loading="lazy" decoding="async" />

## Description

### Why is this important?

Generative AI has created a trust gap:
- Images, videos, and audio may be AI-generated or heavily manipulated - this can lead to deepfakes, and fraud.
- This AI-enhancement or editing can occur in real-time - i.e. a person can livestream themeself, but use ML to change their appearance and voice.
- Moreover, the use of AI models to scan images, video, and audio (e.g. facial or voice recognition) is often opaque, with no actual changes to the underlying data.
- Viewers rarely know whether AI analysis was performed, or what conclusion was reached.

Integrating transparent provenance - disclosing whether media is AI-generated or AI-edited, and also what other AI processing has occurred on any media - is necessary for accountability in domains like journalism, security, and regulated industries. This project uses C2PA 2.3 to record such actions as signed, machine-verifiable assertions attached to the asset. This reduces deepfake proliferation and fraud by providing a method to verify provenance. Additionally it tracks authorised and potential unauthorised use of models to analyse the asset.

[Arm is a founder member of the C2PA Standards Group.](https://newsroom.arm.com/blog/c2pa-fights-disinformation) The Coalition for Content Provenance and Authenticity (C2PA) specification lets creators and platforms attach cryptographically signed metadata to content like:
- images 📷
- videos 🎥
- audio 🎧
- documents 📄

That metadata can include:
-	who created it
-	what tool was used (camera, Photoshop, generative AI, etc.)
-	what edits were made and when
-	whether AI was involved

Anyone can later verify this info to see if the content is authentic or has been tampered with.

The best place to start would be with processing on static audio or video files, but we encourage you to ultimately target a streamed data format - i.e. streamed audio or video, and to perform the inference and record the actions in real-time. 

You should leverage an Arm-powered device, such as a Windows-on-Arm laptop, Apple Silicon MacBook, Arm-powered mobile phone, or Raspberry Pi.


### Project Summary

Build and evaluate a comprehensive AI-augmented audio/video capture and provenance system on an Arm-powered device (e.g. Windows-on-Arm laptop)
- captures streamed media with a camera or microphone,
- runs AI models on-device (i.e. face/object/keyword/sentiment detection, upscaling/filters/enhancements),
- generates C2PA Content Credentials that transparently disclose:
  - which models were run,
	- their effect/impact on the image or video

and demonstrates how this provenance enables trust and auditability in real-world use cases such as content integrity validation and responsible media pipelines.

You should be able to show your source code, along with documentation/instructions/comments, a short demo video or images to show the project in action, and a short document describing your decisions and how you implemented the project.


  ## What will you use?
You should be willing to learn about, or already familiar with:
- Programming and building a basic application on your chosen platform/OS
- C2PA and the concepts behind content provenance and authentication
- Deploying optimised inference models on Arm-powered CPU via frameworks with KleidiAI integration (e.g. PyTorch)


## Resources from Arm and our partners
- Repository: [AI on Arm course](https://github.com/arm-university/AI-on-Arm)
- Arm / Cambridge University edX course: [AI at the Edge on Arm (Mobile)](https://www.edx.org/learn/computer-science/arm-education-ai-at-the-edge-on-arm)
- Learning Path: [Vision LLM Inference on Android with KleidiAI](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/vision-llm-inference-on-android-with-kleidiai-and-mnn/)
- Learning Path: [Build a Hands-Free Selfie Android Application with MediaPipe](https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-android-selfie-app-using-mediapipe-multimodality/)
- Arm Developer: [Edge AI](https://developer.arm.com/edge-ai)
- External Documentation: [Windows on Arm Environments – Linaro wiki](https://linaro.atlassian.net/wiki/spaces/WOAR/pages/29005479987/Windows+on+Arm+Environments)

## Support Level

This project is designed to be self-serve but comes with opportunity of some community support from Arm Ambassadors, who are part of the Arm Developer program. If you are not already part of our program, [click here to join](https://www.arm.com/resources/developer-program?#register).

You are also welcome to contact Arm-Developer-Labs@arm.com to enquire about further support.

## Benefits 

Standout project contributions to the community will earn digital badges. These badges can support CV or resumé building and demonstrate earned recognition.

To receive the benefits, you must show us your project through our [online form](https://forms.office.com/e/VZnJQLeRhD). Please do not include any confidential information in your contribution. Additionally if you are affiliated with an academic institution, please ensure you have the right to share your material.