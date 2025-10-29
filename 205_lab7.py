# Annalise Sean, CST205

from PIL import Image
import numpy as np
from colorthief import ColorThief
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from math import sqrt

image_path = r"C:\Users\Annalise Sean\Desktop\cst205\hornet.png"  # using the same stupid image of hornet because I love this thing

# Task 1
def grayscale_average(img_path):
    img = Image.open(img_path).convert('RGB')
    np_img = np.array(img)
    avg_gray = np.mean(np_img, axis=2).astype(np.uint8)
    return Image.fromarray(avg_gray)

# Task 2
def grayscale_luminance(img_path):
    img = Image.open(img_path).convert('RGB')
    np_img = np.array(img)
    lum_gray = (0.299 * np_img[:, :, 0] +
                0.587 * np_img[:, :, 1] +
                0.114 * np_img[:, :, 2]).astype(np.uint8)
    return Image.fromarray(lum_gray)

# Task 3
def get_dominant_color(img_path):
    color_thief = ColorThief(img_path)
    return color_thief.get_color(quality=1)

def count_color_occurrences(img_path, target_rgb):
    img = Image.open(img_path).convert('RGB')
    np_img = np.array(img)
    matches = np.all(np_img == target_rgb, axis=-1)
    return np.sum(matches)

# Task 4
def patch_numpy_asscalar():
    def patch_asscalar(a):
        return a.item()
    setattr(np, "asscalar", patch_asscalar)

def rgb_to_lab(rgb_tuple):
    rgb = sRGBColor(*rgb_tuple, is_upscaled=True)
    return convert_color(rgb, LabColor)
patch_numpy_asscalar()

# Task 5
def euclidean_distance(c1, c2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

def lab_distance(lab1, lab2):
    return sqrt((lab1.lab_l - lab2.lab_l) ** 2 +
                (lab1.lab_a - lab2.lab_a) ** 2 +
                (lab1.lab_b - lab2.lab_b) ** 2)

# running these things
avg_gray_img = grayscale_average(image_path)
lum_gray_img = grayscale_luminance(image_path)
dominant_rgb = get_dominant_color(image_path)
occurrences = count_color_occurrences(image_path, dominant_rgb)
lab_color = rgb_to_lab(dominant_rgb)

# compare apple
apple1_rgb = (176, 63, 81)
apple2_rgb = (185, 77, 89)
apple1_lab = rgb_to_lab(apple1_rgb)
apple2_lab = rgb_to_lab(apple2_rgb)

# outputting those things
print("Dominant RGB Color:", dominant_rgb)
print("Occurrences in image:", occurrences)
print("L*a*b* of dominant color:")
print(f"  L: {lab_color.lab_l:.2f}, a: {lab_color.lab_a:.2f}, b: {lab_color.lab_b:.2f}")
print("Apple RGB Euclidean Distance:", euclidean_distance(apple1_rgb, apple2_rgb))
print("Apple L*a*b* Color Distance:", lab_distance(apple1_lab, apple2_lab))

# saving those things
avg_gray_img.save("hornet_grayscale_avg.png")
lum_gray_img.save("hornet_grayscale_lum.png")