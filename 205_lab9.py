# Annalise Sean, CST205
# I know I probably won't get credit since I was absent but I still wanted to try

# Task 1
# begins at line 325 but the code is saying 527 idk I just looked myself. 527 is a blank line on the website

# Task 2
"""
This class represents an image object.  To create
:py:class:`~PIL.Image.Image` objects, use the appropriate factory
functions.  There's hardly ever any reason to call the Image constructor
directly.

* :py:func:`~PIL.Image.open`
* :py:func:`~PIL.Image.new`
* :py:func:`~PIL.Image.frombytes`
"""

# Task 3

from PIL import Image
import inspect

print("Image class starts at line:", inspect.getsourcelines(Image.Image)[1])
print("Docstring:\n", inspect.getdoc(Image.Image))

img = Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\metaknight2.png") # I think it's funny

print(dir(img))

# example attribute?
print("Bands:", img.getbands())

# Task 4–6

class Song:
    def __init__(self, name, artist, genre, length, album, cover_image=None):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.length = length  
        self.album = album
        self.cover_image = cover_image  

    def play(self):
        print(f"Now playing: {self.name} by {self.artist}")

    def get_length_minutes(self):
        minutes = self.length // 60
        seconds = self.length % 60
        return f"{minutes}m {seconds}s"

    def show_cover(self):
        if self.cover_image:
            self.cover_image.show()
        else:
            print("No cover image available.")

# three songs with cover images loaded as Pillow Image objects
song1 = Song(
    "Moon Waltz",
    "Cojum Dip",
    "Metal",
    287,
    "Cojum Dip",
    Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\cojumdipalbum.jpg")
)
song2 = Song(
    "Rule #4: Fish in a Birdcage",
    "Fish in a Birdcage",
    "Alternative/Indie",
    181,
    "Fish in a Birdcage",
    Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\fishinbirdcagealbum.jpg")
)
song3 = Song(
    "my time",
    "bo en",
    "J-pop",
    315,
    "pale machine",
    Image.open(r"C:\Users\Annalise Sean\Desktop\cst205\palemachinealbum.jpg")
)

for s in (song1, song2, song3):
    print(f"{s.name} | {s.artist} | {s.genre} | {s.get_length_minutes()} | {s.album}")