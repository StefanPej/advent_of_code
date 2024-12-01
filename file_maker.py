import os
from pathlib import Path

YEAR = '2024'
MAX_DAYS = 25
INPUT_FILE_NAME = 'input.txt'


for day in range(1, MAX_DAYS + 1):
    day_str = str(day).zfill(2)
    folder = Path(f"./{YEAR}/{day_str}")
    folder.mkdir(parents=True, exist_ok=True)

    files_to_make = ["part_1.py", "part_2.py", INPUT_FILE_NAME]

    for file in files_to_make:
        file_to_make = folder / file
        file_to_make.touch()


