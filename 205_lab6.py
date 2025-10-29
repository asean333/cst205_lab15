# Annalise Sean, cst205

from PIL import Image

# Task 1 - double negative

im = Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\hornet.png")

# 1st negative
neg1 = [(255 - p[0], 255 - p[1], 255 - p[2]) for p in im.getdata()]
im.putdata(neg1)
im.save(r"C:\Users\Annalise Sean\Desktop\cst205\hornet_negative.png")

# 2nd negatve (restores)
neg2 = [(255 - p[0], 255 - p[1], 255 - p[2]) for p in neg1]
im.putdata(neg2)
im.save(r"C:\Users\Annalise Sean\Desktop\cst205\hornet_restored.png")
im.show()

# explanation: I applied the negative filter twice which pretty much just makes the image 'normal' again

##############################

# Task 2 - sunset filter

# -50 for green and -125 for blue?

im = Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\hornet.png")

# reduce green and blue
sunset = [(p[0], max(p[1] - 50, 0), max(p[2] - 125, 0))
          for p in im.getdata()
          ]
im.putdata(sunset)
im.save(r"C:\Users\Annalise Sean\Desktop\cst205\hornet_sunset.png")
im.show()

# explanation: I reduced both the green and blue channels by 50 and 125 respectively which brings out the red, but by not removing AS much green it gives it a slightly oranger tint

##############################

# Task 3 - sepia

def sepia(p):
    # tint shadows
    if p[0] < 63:
        r, g, b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
    # tint midtones
    elif p[0] < 192:
        r, g, b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
    # tint highlights
    else:
        r = int(p[0] * 1.08)
        g, b = p[1], int(p[2] * 0.5)
    return (r, g, b)

im = Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\hornet.png")

# sepia
sepia_list = [sepia(p) for p in im.getdata()]
im.putdata(sepia_list)
im.save(r"C:\Users\Annalise Sean\Desktop\cst205\hornet_sepia.png")
im.show()


# explanation: I made it 'yellower' by bringing out a bit more red and reduced blue which kind of warms up the midtones and softens the highlights


##########################################################################################

'''# code for negative

from PIL import Image
im2 = Image.open('images/penguin.jpg')

negative_list = [(255-p[0], 255-p[1], 255-p[2])
                           for p in im2.getdata()]

im2.putdata(negative_list)
im2.show()

# code for grayscale

from PIL import Image
im2 = Image.open('images/penguin.jpg')

new_list = [ ( (a[0]+a[1]+a[2])//3, ) * 3
                   for a in im2.getdata() ]

im2.putdata(new_list)
im2.show()

# reduce red

def reduce_red(picture):
   new_list=[]
 
   for p in picture.getdata():
       new_list.append((p[0]//2, p[1], p[2]))
     
   picture.putdata(new_list)
   picture.show()

reduce_red(im2)

# decrease red using map

from PIL import Image
im2 = Image.open('images/tent_roof.jpg')

def map_red(pixel):
   return (pixel[0]//2, pixel[1], pixel[2])

new_list = map(map_red, im2.getdata())

im2.putdata(list(new_list))
im2.show()


# python map() function

def hello_fn(someone):
   return f'Hello, {someone}!'

map(hello_fn, ['Joanna', 'Albert'])

'''