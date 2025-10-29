# Annalise Sean, CST205

from PIL import Image

# blank canvas
def create_canvas(width=600, height=400, color=(255, 255, 255)):  
    return Image.new('RGB', (width, height), color)

# color distance
def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

# chroma key
def chromakey(src, bg, refp, threshold=150):  
    for x in range(src.width):
        for y in range(src.height):
            cur_pixel = src.getpixel((x, y))
            if color_distance(cur_pixel, refp) < threshold:
                src.putpixel((x, y), bg.getpixel((x, y)))
    return src

img3 = Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\metaknight3.png")
img2 = Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\metaknight2.png")
img1 = Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\metaknight1.png")

# Task 1 

canvas = create_canvas()
canvas.paste(img1, (50, 50))
canvas.paste(img2, (200, 190))
canvas.paste(img3, (280, 50))
canvas.show()

# Task 2

canvas = create_canvas()
canvas.paste(img1, (10, 10))
canvas.paste(img2, (240, 220))
canvas.paste(img3, (300, 10))
canvas.show()

# Task 3

bg = create_canvas(color=(0, 255, 0))  # you're green now
ref_color = (255, 255, 255)            # replace white

# gonna make him look real stupid
result = chromakey(img1.copy(), bg, ref_color)
result.show()