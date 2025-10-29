# Annalise Sean, CST205

# Task 1: Color dictionary
color_dictionary = {
    "green": (0, 128, 0),
    "blue": (0, 0, 255),
    "magenta": (255, 0, 255),
    #"greenery": (132, 189, 0),     #I just wanted to keep this for future reference because it still is a nice color :)
    "emerald": (0, 152, 116),       #I found emerald on the list of pantone yearly colors and those are my favorite gemstones so I had to switch over
    "honeysuckle": (203, 101, 134),
    "blue iris": (91, 94, 166)
}

# Task 2: Printing RGB channel
print(f"The red channel of honeysuckle has value {color_dictionary['honeysuckle'][0]}.")
print(f"The green channel of emerald has value {color_dictionary['emerald'][1]}.")
print(f"The blue channel of blue iris has value {color_dictionary['blue iris'][2]}.")

# Task 3: Extracting specific channel values
tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141,125,83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        }, 
        {
            "color": (35,22,19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
      }
    ]
}

# Task 4: Get RGB from user
rgb_input = input("Enter RGB values separated by spaces (e.g. 250 250 70): ")
r, g, b = map(int, rgb_input.split())

color_list = [(r, g, b)]  # store tuple in list

print(f"Thank you, your RGB color is ({r}, {g}, {b})")

# Task 5: Prints individual channels
def print_rgb_channels(color_list):
    r, g, b = color_list[0] 
    print(f"The red channel intensity is: {r}")
    print(f"The green channel intensity is: {g}")
    print(f"The blue channel intensity is: {b}")

#Task 6: Convert to hexadecimal
def rgb_to_hex(color_list):
    r, g, b = color_list[0]
    hex_value = "#{:02X}{:02X}{:02X}".format(r, g, b)
    print(f"The hexadecimal value of your color is: {hex_value}")
    return hex_value

#Task 7: Convert back to RGB and store in list
def hex_to_rgb(hex_string):
    hex_string = hex_string.lstrip("#")
    rgb_tuple = tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4))
    print(f"The RGB values for {hex_string.upper()} are: {rgb_tuple}")
    return [rgb_tuple] 

