from PIL import Image
from transformers import pipeline
from pathlib import Path

cwd = Path(__file__).resolve().parent
data_dir = cwd / "data"
with_txt_dir = data_dir / "with_txt"

captioner = pipeline(
    task="image-to-text", 
    model="Salesforce/blip-image-captioning-base",
    device=0,
    generate_kwargs={
        "max_length": 50,
        "num_beams": 5,
        "early_stopping": True
    }
)

for path_jpg in with_txt_dir.iterdir():
    path_txt = path_jpg.with_suffix(".txt")
    image = Image.open(path_jpg).convert("RGB")
    result = captioner(image)
    caption = result[0]["generated_text"]
    with open(path_txt, "w", encoding="utf-8") as f:
        f.write(caption)
