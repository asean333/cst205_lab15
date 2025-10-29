# Annalise Sean, CST205, 9/26/2025

from PIL import Image
from glob import glob

# compute median of odd-length integers
def my_median(values):
    sorted_vals = sorted(values)
    mid_index = len(sorted_vals) // 2
    return sorted_vals[mid_index]

# compute median RGB value at pixel
def median_pixel(images, x, y):
    red, green, blue = [], [], []

    for img in images:
        r, g, b = img.getpixel((x, y))
        red.append(r)
        green.append(g)
        blue.append(b)

    return (
        my_median(red),
        my_median(green),
        my_median(blue)
    )

# create new image with median RGB values
def median_image(images, output_filename):
    width, height = images[0].size
    result = Image.new("RGB", (width, height))

    for row in range(height):
        for col in range(width):
            median_rgb = median_pixel(images, col, row)
            result.putpixel((col, row), median_rgb)

    result.save(output_filename)
    print(f"Saved: {output_filename}")

# Task 2
images_task2 = [
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task2_images\img_1.png"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task2_images\img_2.png"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task2_images\img_3.png")
]
median_image(images_task2, "task2.png")

# Task 3
images_task3 = [
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\zi5uCS1rT0.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\AdWLrEX9jK.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\bpoQ3CCQME.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\C6jqwts7Po.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\ciUac3xbEu.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\Drkvv0rPyI.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\GWYn2kQYvo.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\lh2ezwNUR6.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\lHemWWywA6.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\OJbgEgP8EE.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\OLPCdimSmt.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\QfWE9x5q2I.png").convert("RGB"),
    Image.open(r"C:\Users\Annalise Sean\Desktop\hw2_images\hw2_images\task3_images\wHd8pqjwlY.png").convert("RGB")
]
median_image(images_task3, "task3.png")