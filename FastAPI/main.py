from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from pathlib import Path
from ml import run_and_display, save_images, AttentionStore
import torch

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Diffusion-based montage generator with FastAPI"}

@app.get("/api")
async def root():
    return {"message": "Diffusion-based montage generator with FastAPI"}

@app.post("/api/generate_and_save")
async def generate_and_save(prompt: str, file_name: str):
    controller = AttentionStore()

    images, x_t = run_and_display([prompt], controller, latent=None, run_baseline=False, generator=torch.Generator().manual_seed(3546)) 
    preview_url = save_images(images, file_name)

    return {"Preview_url": preview_url}
    

