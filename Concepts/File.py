# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

import os
with open("c:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\poems.txt", "r") as f:
    if ('twinkle' in f.read()):
        print("Twinkle is in the file.")
    else:
        print("Twinkle is not in the file.")

# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file Hi-score.txt which is either blank or contains the previous Hi-Score. You need to write a program whenver game() breaks the Hi-score.

import random


def game():
    score = random.randint(1, 100)
    print(f"The score is: {score}")
    return score


score = game()

with open("c:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\Hi-score.txt", "r") as f:
    prev_score = int(f.read())
if (score > prev_score):
    with open("c:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\Hi-score.txt", "w") as f:
        f.write(str(score))


# Write a program to generate multiplication tables from 2 to 20 and write it to the differed files. Place these files in a folder for 13-yr old.

def tables():
    for i in range(2, 21):
        table = ''
        for j in range(1, 11):
            table += f"{i} x {j} = {i*j}\n"
        with open(f"c:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\Tables\\{i}.txt", 'w') as f:
            f.write(table)


tables()

# A File contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file.

with open("C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\replace.txt", "r") as f:
    text = f.read()
if ("Donkey" in text):
    text = text.replace("Donkey", "######")
    with open("C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\replace.txt", "w") as f:
        f.write(text)

# Repeat above program for a list of such words to be censored.

# Write a program to mine a log file and find out whether it contains 'python'.

with open('C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\log.txt', 'r') as f:
    text = f.read()
if ('python' in text):
    print("Python is in the file.")
else:
    print("Python is not in the file.")

# Write a program to mine a log file and find out whether it contains 'python' and on which line number.

count = 0
text = " "
with open('C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\log.txt', 'r') as f:
    while (text != ""):
        count += 1
        text = f.readline()
        if ('python' in text):
            break
print(f"Python is in the file at line {count}")

# Write a program to make a copy of a text file "this.txt"

with open("C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\log.txt", "r") as f:
    text = f.read()
    with open("C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\this.txt", "w") as f:
        f.write(text)

# Write a program to find out whether a file is identical & matches the content of another file

with open("C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\log.txt", "r") as f:
    file1 = f.read()
with open("C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\this.txt", "r") as f:
    file2 = f.read()

if (file1 == file2):
    print("Both files are identical")
else:
    print("Both files are not identical")

# Write a program to wipe out the contents of a file using python.

with open("C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\this.txt", "w") as f:
    f.write("")
    f.flush()  # In-Built Function

# Write a python program to rename a file to 'renamed_by_python.txt'


oldname = input("Enter the name of the file to rename: ")
newname = input("Enter the new name of the file: ")

with open(f"C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\{oldname}", "r") as f:
    text = f.read()

with open(f"C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\{newname}", "w") as f:
    os.remove(
        f"C:\\Users\\rithi\\OneDrive\\Desktop\\python\\Concepts\\{oldname}")
    text = f.write(text)
