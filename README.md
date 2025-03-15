# Criminal Composite Sketch Generation Framework Using Generative Models

This project introduces a framework for creating composite sketches by leveraging generative AI models to effectively reflect both concrete and abstract witness descriptions.



## Introduction

Despite the widespread use of CCTV systems, composite sketches remain crucial evidence in criminal investigations, especially for cases where CCTV footage is unavailable or unclear. Traditional montage creation methods in Korea heavily rely on the "recall" principle, where witnesses describe specific facial features that are then combined by sketch artists.

Our project addresses the limitations of traditional methods by developing a framework that:
- Automatically generates sketches from textual descriptions
- Captures both concrete facial features and abstract impressions
- Significantly reduces creation time (under 30 seconds)
- Allows for partial text modifications to refine images

Check out our [paper/report](AI_team_paper.pdf)

## Features

- **Text-to-Image Generation**: Convert witness descriptions directly into composite sketches
- **Comprehensive Description Processing**: Handle both specific features ("round face", "thick eyebrows") and abstract impressions ("looks trustworthy", "appears meticulous")
- **Rapid Generation**: Create sketches in under 30 seconds
- **Interactive Refinement**: Modify specific parts of the description to update corresponding features in the image


## Generative Models

We developed and compared two generative models:

1. **DALL-E with VQ-GAN**:
   - Uses klue/roberta-large as text encoder for Korean language support
   - Employs VQ-GAN as image decoder for improved detail rendering

2. **Stable Diffusion with LoRA**:
   - Fine-tuned the pre-trained Korean stable diffusion model (my-korean-stable-diffusion-v1-5)
   - Implemented Low-Rank Adaptation (LoRA) to optimize for limited computing resources

### Model Comparison

| Model | TIFA Score | User Rating |
|-------|------------|-------------|
| Stable Diffusion | 0.50/1 | 3.17/5 |
| DALL-E | 0.53/1 | 2.96/5 |

We selected **Stable Diffusion** as our primary model based on superior user evaluation scores, particularly in handling the nuances of montage creation.


<!-- 
## 📊 Sample Results

Our framework allows for precise control over generated features through text modification:


| Description Change | Result |
|-------------------|--------|
| Age: "40s" → "20s" | [Younger appearance] |
| Gender: "Male" → "Female" | [Gender transformation] |
| Face shape: "Square" → "Oval" | [Changed face contour] |
| Hair part: "Left" → "Right" | [Modified hairstyle] |
| Added: "Has double eyelids" | [Updated eye features] |
| Eyebrow: "Thick" → "Thin" | [Refined eyebrow appearance] |
-->

## ⚠️ Limitations

Current limitations include:
- Occasional image distortions characteristic of generative models
- Incomplete representation of very lengthy descriptions
- Imperfect image updates in response to text modifications



## Team

- Chaeyeon Yang (Front-end)
- Janghyeon Roh (AI engineering)
- Mir An (AI engineering)
- Seungyeon An (Back-end)
- Sujin Hwang (AI engineering)




*Department of Data Technology, Convergence Software School, Myongji University*
