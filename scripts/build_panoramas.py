import json
import hashlib
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "sources.json"
INDEX_FILE = ROOT / "index.json"
CONVERTER = ROOT / "scripts" / "cubemap_convert.py"


def md5_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def load_json(path, default):
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def download_file(url: str, target: Path):
    print(f"Downloading: {url}")
    urllib.request.urlretrieve(url, target)


def run_converter(input_hdr: Path, output_dir: Path):
    cmd = [
        sys.executable,
        str(CONVERTER),
        "--input", str(input_hdr),
        "--output", str(output_dir),
        "--face-size", "2048",
    ]
    subprocess.run(cmd, check=True)


def main():
    sources = load_json(SOURCES_FILE, [])
    index = load_json(INDEX_FILE, [])

    index_set = set(index)
    updated = False

    for entry in sources:
        url = entry["url"]
        pano_id = md5_hash(url)
        output_dir = ROOT / pano_id

        if pano_id in index_set and output_dir.exists():
            print(f"Skipping existing panorama: {pano_id}")
            continue

        with tempfile.TemporaryDirectory() as tmp:
            hdr_path = Path(tmp) / "source.hdr"

            download_file(url, hdr_path)
            run_converter(hdr_path, output_dir)

        index.append(pano_id)
        index_set.add(pano_id)
        updated = True

        print(f"Added panorama: {pano_id}")

    if updated:
        save_json(INDEX_FILE, index)
        print("index.json updated")
    else:
        print("No new panoramas")


if __name__ == "__main__":
    main()
