import os
from pathlib import Path

YEAR = '2025'
MAX_DAYS = 12
INPUT_FILE_NAME = 'input.txt'
TEST_FILE_NAME = 'test.txt'


for day in range(8, MAX_DAYS + 1):
    day_str = str(day).zfill(2)
    folder = Path(f"./{YEAR}/day_{day_str}")
    folder.mkdir(parents=True, exist_ok=True)

    files_to_make = ["part_1.py", "part_2.py", INPUT_FILE_NAME, TEST_FILE_NAME]

    for file in files_to_make:
        file_to_make = folder / file
        file_to_make.touch()
        if file.startswith("part"):
            with open(file_to_make, 'w') as o:
                o.write(f"from aoc_utils import *\n\ninp = read_input({YEAR}, {day})\ntest = read_input({YEAR}, {day}, filename='test')")



