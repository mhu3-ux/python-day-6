print("Dear Class")

import random
random_int = random.randint(1,10)
print(random_int)

deck_of_cards = ["King of Spades", "8 of Hearts"]
random_card = random.choice(deck_of_cards)
print(random)

import math
answer = math.sqrt(64)
print(answer)

with open("demo.text","w") as file:
    file.write("File I/O is sooo fun")


name = input("What is your name? ")

with open("guest_list.text", "a") as file:
    file.write(name + "\n")


name = input("What is your name? ")

with open("guest_list.text", "a") as file:
    file.write(name + "\n")


with open("logs.txt","r") as file:
    for each_line in file:
        line_number = line_number + 1
        if "password" in each_line:
            print(each_line)
            print("The line number is:", line_number)


from pathlib import Path

lyrics_path = Path(__file__).with_name("lyrics.txt")
line_count = 0

with lyrics_path.open("r", encoding="utf-8") as file:
    for line in file:
        line_count += 1

print("Total number of lines:", line_count)