# Annalise Sean, CST205

#color_list = [ (227, 66, 52), (205, 96, 144), (28, 134, 238) ]


# color_list[0] is (227, 66, 52)
# color_list[1] is (205, 96, 144)
# ...
# color_list[0][0] is the red channel of color_list[0]
# color_list[0][1] is the green channel of color_list[0]
# color_list[0][2] is the blue channel of color_list[0]
# color_list[1][0] is the red channel of color_list[1]
# color_list[1][1] is the green channel of color_list[1]
# ...

#if color_list[0][0] > color_list[0][1] and color_list[0][0] > color_list[0][2]:
#    print('The color is reddish')
#elif color_list[0][1] > color_list[0][0] and color_list[0][1] > color_list[0][2]:
#    print('The color is greenish')
#else:
#    print('The color is blueish')

# /////////////////////////////////////////////////////////////////

#color_list = [ (250, 250, 250), (245, 50, 245), (100, 231, 231) ]

# TASK 1
#if color_list[0][0] > color_list[0][1] and color_list[0][0] > color_list[0][2]:
#    print('The color is reddish')
#elif color_list[0][1] > color_list[0][0] and color_list[0][1] > color_list[0][2]:
#    print('The color is greenish')
#elif color_list[0][2] > color_list[0][0] and color_list[0][2] > color_list[0][1]:
#    print('The color is blueish')
# TASK 2
#elif color_list[0][0] == color_list[0][1] and (color_list[0][0] or color_list[0][1]) > color_list[0][2]:
#    print('The color is a shade of yellow')
#elif color_list[0][0] == color_list[0][2] and (color_list[0][0] or color_list[0][2]) > color_list[0][1]:
#    print('The color is a shade of magenta')
#elif color_list[0][1] == color_list[0][2] and (color_list[0][1] or color_list[0][2]) > color_list[0][0]:
#    print('The color is a shade of cyan')
#else:
#    print('The color is a shade of gray, black, or white')

# //////////////////////////////////////////////////////////////////////////////

# Get RGB input from user
rgb_input = input("Enter RGB values separated by spaces (e.g. 250 250 70): ")
r, g, b = map(int, rgb_input.split())

color_list = [ (r, g, b) ]

# TASK 1
if color_list[0][0] > color_list[0][1] and color_list[0][0] > color_list[0][2]:
    print('The color is reddish')
elif color_list[0][1] > color_list[0][0] and color_list[0][1] > color_list[0][2]:
    print('The color is greenish')
elif color_list[0][2] > color_list[0][0] and color_list[0][2] > color_list[0][1]:
    print('The color is blueish')
# TASK 2
elif color_list[0][0] == color_list[0][1] and color_list[0][0] > color_list[0][2]:
    print('The color is a shade of yellow')
elif color_list[0][0] == color_list[0][2] and color_list[0][0] > color_list[0][1]:
    print('The color is a shade of magenta')
elif color_list[0][1] == color_list[0][2] and color_list[0][1] > color_list[0][0]:
    print('The color is a shade of cyan')
else:
    print('The color is a shade of gray, black, or white')