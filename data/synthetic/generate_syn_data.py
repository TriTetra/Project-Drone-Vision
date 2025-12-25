import os
import random
import torch 
import argparse
import sys
import json
import matplotlib.pyplot as plt
from PIL import Image
from tdqm import tqdm
from diffusers import AutoPiplineForText2Image, DPMSolverMultistepScheduler

DEFAULT_NEGATIVE_PROMPT = "angled view, tilted camera, perspective, horizon, sky visible, buildings, roads, road markings, text, watermark, people, vehicles, trees, shadows, 3d objects, circles, triangles, rounded corners, overlapping shapes, grid pattern, symmetry, cartoon, illustration, low quality, blurry, distorted"


def setup_environment(save_dir):
    if 'google.colab' in sys.modules:
        from google.colab import drive
        drive.mount('/content/drive')

    os.makedirs(save_dir, exist_ok=True)
    print(f"Saving generated images to: {save_dir}")



def load_propmts(json_path):
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Prompt JSON file not found: {json_path}")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list):
        return data
    return data.get("prompts", [])



def load_model(device_id="cuda"):

    if not torch.cuda.is_available():
        print("CUDA is not available. Switching to CPU.")
        device = "cpu"
        dtype = torch.float32
        variant = None
    else:
        device = f"cuda:{device_id}"
        dtype = torch.float16
        variant = "fp16"

    print(f"Loading model on device: {device} with dtype: {dtype}")

    try:
        pipe = AutoPiplineForText2Image.from_pretrained(
            "stabilityai/stable-diffusion-xl-base-1.0",
            torch_dtype=dtype,
            variant=variant,
            use_safetensors=True,
        )

        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        pipe.enable_vae_tiling()

        try:
            pipe.enable_xformers_memory_efficient_attention()
            print("XFormers enabled for memory efficient attention.")
        except Exception as e:
            print(f"XFormers not available: {e}")
        return pipe, device
    
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")
    

def generate_image(pipe, prompt, negative_prompt, device, guidance_scale=8.5, num_inference_steps=50):
    seed = torch.randint(0, 2**32 - 1, (1,)).item()
    generator = torch.Generator(device).manual_seed(seed)

    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        width=1024,
        height=1024,
        generator=generator,
        clip_skip=2
    ).images[0]

    return image, seed   


def generate_batch(pipe, device, prompts, output_dir, count_per_prompt, neg_prompt):
    total_generated = 0
    print(f"Generating {count_per_prompt} images for each of {len(prompts)} prompts...")

    for i, propt_text in enumerate(prompts):
        for j in tqdm(range(count_per_prompt), desc=f"Grup {i+1}"):
            try:
                image, seed = generate_image(
                    pipe = pipe,
                    device = device,
                    prompt = propt_text,
                    negative_prompt = neg_prompt
                )

                filename = f"syn_p{i+1:02d}_{j+1:03d}_seed{seed}.jpg"
                save_path = os.path.join(output_dir, filename)
                image.save(save_path, quality=95, optimize=True)

                total_generated += 1
            
            except Exception as e:
                print(f"Error generating image for prompt '{propt_text}': {e}") 
                continue
    
    print(f"Total images generated: {total_generated}")
    create_summary_grid(output_dir)


def create_summary_grid(folder_path):
    print("Creating summary grid...")
    files = []
    
    for f in os.listdir(folder_path):
        if f.endswith('.jpg'):
            files.append(f)
    
    files = sorted(files)

    if not files:
        raise ValueError("No images found to create summary grid.")
    
    num_show = min(9, len(files))
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))
    axes = axes.flatten()

    for idx, ax in enumrate(axes):
        if idx < num_show:
            img = Image.open(os.path.join(folder_path, files[idx]))
            ax.imshow(img)
            ax.set_title(files[idx], fontsize=8)
        ax.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(folder_path, 'summary_grid.jpg'), dpi=150)
    plt.close()
    print("Summary grid saved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modüler Sentetik Veri Üretici")
    parser.add_argument("--output", type=str, default="data/synthetic/output", help="Çıktı klasörü")
    parser.add_argument("--prompts_file", type=str, required=True, help="JSON formatında prompt dosyası")
    parser.add_argument("--count", type=int, default=5, help="Prompt başına üretilecek sayı")
    parser.add_argument("--negative_prompt", type=str, default=DEFAULT_NEGATIVE_PROMPT, help="Negatif prompt")

    args = parser.parse_args()

    setup_environment(args.output)

    try:
        prompt_list = load_propmts(args.prompts_file)
        print(f"Yüklenen {len(prompt_list)} prompt.")
    except Exception as e:
        print(f"Prompt yükleme hatası: {e}")
        sys.exit(1)

    pipe, device = load_model()

    generate_batch(
        pipe = pipe,
        device = device,
        prompts = prompt_list,
        output_dir = args.output,
        count_per_prompt = args.count,
        neg_prompt = args.negative_prompt
    )
  
