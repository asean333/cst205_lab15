# Annalise Sean

# Task 1

from PIL import Image

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

    # Task 2
    # readable string representation
    def __str__(self):
        return f"'{self.name}' by {self.artist} [{self.genre}] - {self.get_length_minutes()} from '{self.album}'"

    # Task 3
    # compare songs by name and artist
    def __eq__(self, other):
        if isinstance(other, Song):
            return self.name == other.name and self.artist == other.artist
        return False

# bumping part of task 1 down here it seems to work better
# three songs with cover images Pillow Image objects
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

# try __str__ method
print(str(song1))
print(str(song2))
print(str(song3))

# try __eq__ method
print(song1 == song2)
print(song1 == Song("Moon Waltz", "Cojum Dip", "Metal", 287, "Cojum Dip"))

# Task 4
# The MyWidget subclass inherits from QtWidgets.QWidget

# Task 5

class MyImage:
     # load from file
    def __init__(self, filename):
        self.image = Image.open(filename)

    # convert to grayscale
    def grayscale(self):
        self.image = self.image.convert("L")

    # resize to half original dimensions
    def shrink(self):
        width, height = self.image.size
        self.image = self.image.resize((width // 2, height // 2))

    # crop centered box from image
    def crop_center(self, width, height):
        img_width, img_height = self.image.size
        left = (img_width - width) // 2
        top = (img_height - height) // 2
        right = left + width
        bottom = top + height
        self.image = self.image.crop((left, top, right, bottom))

    # save edited image to new file
    def save(self, outname):
        self.image.save(outname)

test_img = MyImage(r"C:\Users\Annalise Sean\Desktop\cst205\cojumdipalbum.jpg")
test_img.grayscale()
test_img.shrink()
test_img.crop_center(100, 100)
test_img.save(r"C:\Users\Annalise Sean\Desktop\cst205\mirrormoonwaltz.jpg")