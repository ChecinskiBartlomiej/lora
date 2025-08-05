#!/usr/bin/env python3
import subprocess
import sys
from accelerate.utils import write_basic_config
from pathlib import Path

def main():

    write_basic_config()
    cwd = Path(__file__).resolve().parent
    data_dir = cwd / "data" / "without_txt"
    output_dir = cwd / "model"

    cmd = [
        "accelerate", "launch", "train_text_to_image_lora.py",
        "--pretrained_model_name_or_path", "CompVis/stable-diffusion-v1-4",
        "--train_data_dir", str(data_dir),
        "--caption_column", "text",            
        "--dataloader_num_workers", "8",
        "--resolution", "512",
        "--center_crop",
        "--random_flip",
        "--train_batch_size", "1",
        "--gradient_accumulation_steps", "4",
        "--max_train_steps", "15000",
        "--learning_rate", "1e-04",
        "--max_grad_norm", "1",
        "--lr_scheduler", "cosine",
        "--lr_warmup_steps", "0",
        "--output_dir", str(output_dir),
        "--checkpointing_steps", "500",
        "--validation_prompt", "A summer afternoon by the lakeshore, soft brushstrokes, interplay of light and shadow, pastel color palette, in an Impressionist mood",
        "--seed", "1337"
    ]

    print("Starting training:\n", " ".join(cmd), "\n")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("Training error:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

