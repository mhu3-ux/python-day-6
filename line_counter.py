from pathlib import Path

lyrics_path = Path(__file__).with_name("lyrics.txt")
line_count = 0

with lyrics_path.open("r", encoding="utf-8") as file:
    for line in file:
        line_count += 1

print("Total number of lines:", line_count)git remote -v
