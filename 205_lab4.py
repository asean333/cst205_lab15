# Annalise Sean, CST205

# he says use pickle not python shelve because we havn't talked about the latter yet

import pickle
audio_formats = ["flac", "m4a", "mp3", "wav", "ogg", "aiff"]

#with open('pickled', 'wb') as my_file:
#with open("tarantella.txt", 'r') as my_file:
with open('pickled_audio_formats.pkl', 'wb') as file:
    # store pickled version of audio_formats
     pickle.dump(audio_formats, file)

import pickle

#with open('pickled', 'rb') as my_file:
#    my_list = pickle.load('tarantella.txt')

#print(my_list[0])

with open('pickled_audio_formats.pkl', 'rb') as file:
    my_list = pickle.load(file)

print(my_list[0])  


# Task 1: Line Count
# there's like 18 lines source I looked

with open("tarantella.txt", "r") as file:
    lines = file.readlines()

# making sure not to count title
poem_lines = [line.strip() for line in lines[1:] if line.strip()]
print(f"Line count (excluding title): {len(poem_lines)}")

# Task 2: Word Count

with open("tarantella.txt", "r") as file:
    lines = file.readlines()

# get rid of title
poem_text = " ".join(lines[1:])
# rid of punctuation
for char in [",", ".", ":", ";", "!", "?", "'", "’"]:
    poem_text = poem_text.replace(char, "")
words = poem_text.split()

print(f"Word count (excluding title): {len(words)}")

# Task 3: Reminders

reminders = []

while True:
    reminder = input("Enter a reminder. (Enter 'n' if done.)\n")
    if reminder.lower() == 'n':
        break
    reminders.append(reminder)

print("\nHere are your reminders:")
for item in reminders:
    print(item)

# Task 4: Better Reminders

import pickle
import os

filename = "reminders.pkl"

# Load existing reminders
if os.path.exists(filename):
    with open(filename, "rb") as file:
        reminders = pickle.load(file)
    print("Previous reminders:")
    for item in reminders:
        print(item)
else:
    reminders = []

# add new
while True:
    reminder = input("Enter a reminder. (Enter 'n' if done.)\n")
    if reminder.lower() == 'n':
        break
    reminders.append(reminder)

# save updated
with open(filename, "wb") as file:
    pickle.dump(reminders, file)

print("\nHere are your reminders:")
for item in reminders:
    print(item)