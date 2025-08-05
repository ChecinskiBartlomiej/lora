import json
from pathlib import Path
import shutil

cwd = Path(__file__).resolve().parent
data_dir = cwd / "data"
with_txt_dir = data_dir / "with_txt"
without_txt_dir = data_dir / "without_txt"
output_path = with_txt_dir / "metadata.jsonl"

jpg_files = sorted(p for p in with_txt_dir.iterdir() if p.suffix.lower() == ".jpg")

with output_path.open("w", encoding="utf-8") as f:
    for idx, jpg_path in enumerate(jpg_files):
        txt_path = jpg_path.with_suffix(".txt")
        text = txt_path.read_text(encoding="utf-8").strip()
        entry = {
            "file_name": jpg_path.name,
            "text": text
        }
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

for path in with_txt_dir.iterdir():
    if path.suffix.lower() in {".jpg", ".jsonl"}:
        shutil.copy2(path, without_txt_dir / path.name)