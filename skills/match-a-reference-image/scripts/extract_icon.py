#!/usr/bin/env python3
"""
extract_icon.py: lift an icon/graphic out of a cropped reference image onto
a transparent background, using edge-connected flood fill to identify the
true background (not simple global color-distance thresholding, which
incorrectly deletes enclosed same-colored details like white grid lines
inside a white-outlined icon).

Usage:
    python3 extract_icon.py <input.png> <output.png> [--low 14] [--high 40] [--bg-thresh 48]

Arguments:
    input.png   A tight crop containing one icon/graphic on a roughly solid
                background (a card fill color, a page background, etc).
                Crop generously first and look at the result before running
                this: if the crop caught a border or divider line, tighten
                the crop rather than trying to fix it here.
    output.png  Where to save the RGBA result with the background removed.

Options:
    --low        Distance below which a pixel is considered fully background
                 (fully transparent). Default 14.
    --high       Distance above which a pixel is considered fully icon
                 (fully opaque). Between low and high, alpha ramps smoothly
                 for clean antialiased edges. Default 40.
    --bg-thresh  Distance threshold used to decide which pixels *could* be
                 background at all, before the edge-connectivity check.
                 Default 48. Raise this if background shows through as a
                 faint halo; lower it if enclosed icon details are vanishing.

How it works:
    1. Sample the background color from the crop's own edge pixels (median,
       so a stray icon pixel touching one edge doesn't skew it).
    2. Compute each pixel's color distance from that background color.
    3. Threshold at --bg-thresh to get a "background-ish" mask.
    4. Run connected-component labeling on that mask, and keep only the
       components that touch the image border: this is the actual
       background. Any background-colored pixels fully enclosed by icon
       content (e.g. a white grid line surrounded by green) are NOT
       connected to the border and are correctly left alone.
    5. Within the true-background region, ramp alpha smoothly between --low
       and --high for antialiasing. Everywhere else stays fully opaque.

If the result still shows a faint rectangle or stray line, the crop itself
is including part of a neighboring border/divider: go back and tighten the
crop box rather than tuning thresholds further.
"""

import sys
import argparse
import numpy as np
from PIL import Image
from scipy import ndimage


def extract_icon(input_path, output_path, low=14, high=40, bg_thresh=48):
    im = Image.open(input_path).convert("RGBA")
    arr = np.array(im).astype(np.float32)
    rgb = arr[:, :, :3]
    h, w = rgb.shape[0], rgb.shape[1]

    edge_pixels = np.concatenate(
        [rgb[0, :], rgb[-1, :], rgb[:, 0], rgb[:, -1]], axis=0
    )
    bg_color = np.median(edge_pixels, axis=0)

    dist = np.sqrt(((rgb - bg_color) ** 2).sum(axis=2))

    bgish = dist < bg_thresh
    labeled, _ = ndimage.label(bgish)
    border_labels = (
        set(labeled[0, :]) | set(labeled[-1, :]) | set(labeled[:, 0]) | set(labeled[:, -1])
    )
    border_labels.discard(0)
    true_bg = np.isin(labeled, list(border_labels))

    soft_alpha = np.clip((dist - low) / (high - low), 0, 1) * 255
    alpha = np.where(true_bg, soft_alpha, 255)

    arr[:, :, 3] = np.minimum(arr[:, :, 3], alpha)
    out = Image.fromarray(arr.astype(np.uint8), "RGBA")
    out.save(output_path)
    return bg_color


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="Path to the cropped source image")
    parser.add_argument("output", help="Path to save the transparent result")
    parser.add_argument("--low", type=float, default=14, help="Distance below which a pixel is fully transparent")
    parser.add_argument("--high", type=float, default=40, help="Distance above which a pixel is fully opaque")
    parser.add_argument("--bg-thresh", type=float, default=48, help="Threshold for the initial background-ish mask")
    args = parser.parse_args()

    bg = extract_icon(args.input, args.output, args.low, args.high, args.bg_thresh)
    print(f"Sampled background color: {bg.round(1).tolist()}")
    print(f"Saved: {args.output}")
    print("Now composite it onto a swatch matching your TARGET background and Read it before using it for real.")


if __name__ == "__main__":
    main()
