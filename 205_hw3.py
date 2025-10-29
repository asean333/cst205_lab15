# Annalise Sean, CST205

# functions.py
# Author: Annalise
# CST 205 — Multimedia Programming
# Date: 10/19/2025
# Description: Image search and manipulation functions using Pillow

from PIL import Image
from image_info import image_info

def my_search(term: str) -> str:
    term = term.lower()
    best_match = "no results"
    max_score = 0

    for entry in image_info:
        score = 0
        title = entry["title"].lower()
        tags = [tag.lower() for tag in entry["tags"]]

        if term == title:
            score += 1
        score += tags.count(term)

        if score > max_score:
            max_score = score
            best_match = entry["id"]

    return best_match

def apply_sepia(img: Image.Image) -> Image.Image:
    sepia_img = Image.new("RGB", img.size)
    pixels = img.getdata()
    new_pixels = []

    for r, g, b in pixels:
        tr = int(0.393 * r + 0.769 * g + 0.189 * b)
        tg = int(0.349 * r + 0.686 * g + 0.168 * b)
        tb = int(0.272 * r + 0.534 * g + 0.131 * b)
        new_pixels.append((min(tr, 255), min(tg, 255), min(tb, 255)))

    sepia_img.putdata(new_pixels)
    return sepia_img

def apply_negative(img: Image.Image) -> Image.Image:
    neg_img = Image.new("RGB", img.size)
    pixels = img.getdata()
    new_pixels = [(255 - r, 255 - g, 255 - b) for r, g, b in pixels]
    neg_img.putdata(new_pixels)
    return neg_img

def apply_grayscale(img: Image.Image) -> Image.Image:
    gray_img = Image.new("RGB", img.size)
    pixels = img.getdata()
    new_pixels = []

    for r, g, b in pixels:
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        new_pixels.append((gray, gray, gray))

    gray_img.putdata(new_pixels)
    return gray_img

def apply_thumbnail(img: Image.Image) -> Image.Image:
    width, height = img.size
    thumb_img = img.copy()
    thumb_img = thumb_img.resize((width // 2, height // 2))
    return thumb_img