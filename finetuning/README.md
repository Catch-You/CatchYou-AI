## Fine-Tune RunwayML's Stable Diffusion v1-5 with LoRA - Google Colab

This directory contains the Colab Notebook `finetune_colab_gpu.ipynb` for fine-tuning a stable diffusion model using the LoRA technique. 

**Cost-Effective Fine-Tuning:**

This approach utilizes Google Colab Pro's T4 GPU option, significantly reducing the cost compared to deploying a GPU-enabled AWS machine. 

**train_text_to_image_lora.py:**

This script is a modified version of the script available on ([Hugging Face's diffusers library]( https://github.com/huggingface/diffusers/blob/main/examples/text_to_image/train_text_to_image_lora.py))

The original script provides a framework for training a Stable Diffusion model with LoRA (Linear Regression Adapters) for text-to-image generation. However, this version has been adapted for the following purposes:

Manual Model Loading: The script loads the scheduler, tokenizer, text encoder, VAE, and Unet models manually. This allows for fine-tuning the model from another LoRA model. 
Korean Text Support: The original tokenizer has been replaced with a Korean tokenizer and text encoder to handle text data in Korean.

**Final Model**

The final version of the model, trained using this script, can be found [here](https://huggingface.co/SujinHwang/criminal-sketch-lora-v2-2).

**Additional Information:**

- The LoRA technique allows for efficient fine-tuning of large models like Stable Diffusion with a smaller dataset.
- For detailed information about LoRA, refer to the LoRA: Locally Reparameterized Adaptation for Fine-tuning Large Language Models: ([LoRA: Low-Rank Adaptation of Large Language Models](https://huggingface.co/papers/2106.09685)) paper.

