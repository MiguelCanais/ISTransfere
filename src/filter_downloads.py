import os
import shutil
import tomllib

with open("config.toml","rb") as config_file:
    config = tomllib.load(config_file)

DOWNLOADS_FOLDER = os.path.expanduser(config["directories"]["downloads"])
FILES_FOLDER = os.path.expanduser(config["directories"]["organized_files"])
KEEP_COPY = config["options"]["keep_copy"]
DEBUG = config["options"]["debug"]


if not DOWNLOADS_FOLDER.endswith("/"):
    DOWNLOADS_FOLDER = DOWNLOADS_FOLDER + "/"

if not FILES_FOLDER.endswith("/"):
    FILES_FOLDER = FILES_FOLDER + "/"



os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)
os.makedirs(FILES_FOLDER, exist_ok=True)


def print_debug(s):
    if DEBUG: print(s)

new_files = []
for raw_file in os.listdir(DOWNLOADS_FOLDER):
    
    origin_path = DOWNLOADS_FOLDER + raw_file

    if not os.path.isfile(origin_path): continue

    args = raw_file.split('.',maxsplit=2)

    course = args[0]
    section = args[1]
    file_name = args[2]

    os.makedirs(FILES_FOLDER+course, exist_ok=True)
    os.makedirs(f"{FILES_FOLDER}{course}/{section}", exist_ok=True)

    destination_path = f"{FILES_FOLDER}{course}/{section}/{file_name}"

    if os.path.isfile(destination_path):
        print_debug(f"File already exists: {destination_path}")
    else:
        new_files.append(raw_file)
        if KEEP_COPY:
            shutil.copy(origin_path, destination_path)
            print_debug(f"Copied {file_name} to {course}/{section}")
        else:
            shutil.move(origin_path, destination_path)
            print_debug(f"Moved {file_name} to {course}/{section}")


print(f"Organized {len(new_files)} new files in {FILES_FOLDER}")
