import os
import glob
import re
from typing import List
from PIL import Image
import argparse


def sorted_numerically(file_list):
    """파일 이름 안의 숫자 기준 정렬 (1.png, 2.png, 10.png ...)."""
    def extract_num(f):
        m = re.search(r"(\d+)", os.path.basename(f))
        return int(m.group(1)) if m else float("inf")
    return sorted(file_list, key=extract_num)


def load_images(image_paths: List[str]) -> List[Image.Image]:
    images = []
    for p in image_paths:
        # RGBA → 나중에 공통 캔버스에 붙일 거라 그대로 둬도 되고 RGB로 바꿔도 됨
        img = Image.open(p).convert("RGBA")
        images.append(img)
    return images


def resize_images(images: List[Image.Image], width: int = None, height: int = None) -> List[Image.Image]:
    if width is None and height is None:
        return images

    resized = []
    for img in images:
        if width is not None and height is not None:
            new_size = (width, height)
        else:
            w, h = img.size
            if width is not None:
                ratio = width / float(w)
                new_size = (width, int(h * ratio))
            else:
                ratio = height / float(h)
                new_size = (int(w * ratio), height)
        resized.append(img.resize(new_size, Image.BILINEAR))
    return resized


def make_gif(
    image_paths: List[str],
    output_path: str,
    duration: int = 100,
    loop: int = 0,
    width: int = None,
    height: int = None,
) -> None:
    if not image_paths:
        raise ValueError("No images found to create GIF.")

    print(f"[INFO] Found {len(image_paths)} images.")
    for idx, p in enumerate(image_paths):
        print(f"  [{idx:03d}] {p}")

    images = load_images(image_paths)
    images = resize_images(images, width=width, height=height)

    # ✅ 모든 프레임을 같은 크기의 '풀 프레임'으로 강제
    base_w, base_h = images[0].size
    canvas_frames = []
    for img in images:
        # 완전 흰 배경 캔버스 위에 한 장씩 얹기
        canvas = Image.new("RGBA", (base_w, base_h), (255, 255, 255, 255))
        canvas.paste(img, (0, 0), img)  # 알파 사용
        # GIF는 팔레트(P) 모드를 더 잘 처리하므로 변환
        canvas_frames.append(canvas.convert("P", palette=Image.ADAPTIVE))

    first_frame = canvas_frames[0]
    frames = canvas_frames[1:] if len(canvas_frames) > 1 else []

    print(f"[INFO] Saving GIF to: {output_path}")
    first_frame.save(
        output_path,
        save_all=True,
        append_images=frames,
        duration=duration,
        loop=loop,
        disposal=2,   # 이전 프레임 지우고 새 프레임을 그림 → 회색선 누적 방지
        # ⚠ optimize는 쓰지 않는다. (부분 프레임 잘림 문제 방지)
    )
    print("[INFO] Done.")


def main():
    parser = argparse.ArgumentParser(description="Create a GIF from multiple images.")
    parser.add_argument("--input-dir", type=str, required=True)
    parser.add_argument("--pattern", type=str, default="*.png")
    parser.add_argument("--output", type=str, default="output.gif")
    parser.add_argument("--duration", type=int, default=100)
    parser.add_argument("--loop", type=int, default=0)
    parser.add_argument("--width", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    args = parser.parse_args()

    search_pattern = os.path.join(args.input_dir, args.pattern)
    image_paths = sorted_numerically(glob.glob(search_pattern))

    make_gif(
        image_paths=image_paths,
        output_path=args.output,
        duration=args.duration,
        loop=args.loop,
        width=args.width,
        height=args.height,
    )


if __name__ == "__main__":
    main()
