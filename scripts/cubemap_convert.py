import numpy as np
import cv2
import py360convert
import sys
import time
import argparse
from pathlib import Path

FACE_MAP = {
    "R": "px",
    "L": "nx",
    "U": "py",
    "D": "ny",
    "F": "pz",
    "B": "nz"
}

WEBP_QUALITY = 92


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert equirectangular HDR panorama to cubemap (WebP)"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input HDR panorama"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output directory for cubemap faces"
    )
    parser.add_argument(
        "--face-size",
        type=int,
        default=2048,
        help="Cubemap face resolution (default: 2048)"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    start_total = time.time()

    input_path = Path(args.input).resolve()
    output_dir = Path(args.output).resolve()

    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading HDR: {input_path}")
    img = cv2.imread(str(input_path), cv2.IMREAD_UNCHANGED)

    if img is None:
        print("ERROR: failed to load HDR image")
        sys.exit(2)

    print("Applying tone mapping...")
    tonemap = cv2.createTonemapReinhard(
        gamma=2.2,
        intensity=-0.5,
        light_adapt=0.9,
        color_adapt=0.0
    )


    ldr = tonemap.process(img)
    ldr = np.clip(ldr * 255, 0, 255).astype("uint8")

    print("Converting to cubemap...")
    cube = py360convert.e2c(
        ldr,
        face_w=args.face_size,
        mode="bilinear",
        cube_format="dict"
    )

    for face, data in cube.items():

        face_name = FACE_MAP[face]
        out_file = output_dir / f"{face_name}.webp"

        cv2.imwrite(
            str(out_file),
            data,
            [cv2.IMWRITE_WEBP_QUALITY, WEBP_QUALITY]
        )

        print(f"Saved {out_file.name}")

    print(f"Done in {round(time.time() - start_total, 2)} sec")
    print(f"Output: {output_dir}")


if __name__ == "__main__":
    main()
