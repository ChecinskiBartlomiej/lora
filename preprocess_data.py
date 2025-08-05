from pathlib import Path
from PIL import Image

cwd = Path(__file__).resolve().parent
data_dir = cwd / "data"
with_txt_dir = data_dir / "with_txt"

def remove_small_and_big_images(source_dir: Path, min_width: int = 512, min_height: int = 512, max_pixels: int = 178_956_970): 
    Image.MAX_IMAGE_PIXELS = None 
    for img_path in source_dir.iterdir():
        with Image.open(img_path) as img:
            width, height = img.size
        if width < min_width or height < min_height or width * height > max_pixels:
            print(f"Removing {img_path.name} ({width}×{height})")
            img_path.unlink()

def remove_excess_images(source_dir: Path, max_count: int = 999):
    jpg_files = [p for p in source_dir.iterdir()]
    total = len(jpg_files)
    if total > max_count:
        for extra in jpg_files[max_count:]:
            print(f"Removing {extra.name}")
            extra.unlink()
    else:
        print(f"There are <= {max_count} images")

def rename_images(source_dir: Path):
    jpg_files = sorted([p for p in source_dir.iterdir()])
    for idx, img_path in enumerate(jpg_files, start=1):
        new_name = f"{idx:03d}.jpg"
        new_path = source_dir / new_name
        if img_path.name != new_name:
            print(f"Renaming {img_path.name} -> {new_name}")
            img_path.rename(new_path)

if __name__ == "__main__":
    remove_small_and_big_images(with_txt_dir)
    remove_excess_images(with_txt_dir, 999)
    rename_images(with_txt_dir)

