# Annalise Sean, 205

# Task 1

from PIL import Image

# RGB pixel data (3 rows 2 columns)
pixels = [
    [(54, 54, 54), (204, 82, 122)],
    [(71, 71, 71), (232, 22, 93)],
    [(54, 54, 54), (168, 167, 167)]
]

# new RGB image (width = 2 height = 3)
rgb_img = Image.new('RGB', (2, 3))

for y in range(3):
    for x in range(2):
        rgb_img.putpixel((x, y), pixels[y][x])

rgb_img.show()


# Task 2

# dimensions (width = 29, height = 28)
width, height = 29, 28

# grayscale values from file
with open('mona_lisa.txt') as f:
    data = [int(val) for line in f for val in line.strip().split()]

gray_img = Image.new('L', (width, height))
gray_img.putdata(data)

gray_img = gray_img.transpose(Image.ROTATE_270) # it was showing up as sideways I'm rotating this thing

scaled = gray_img.resize((width * 10, height * 10), Image.NEAREST) # scaling up

scaled.show()