import os
import shutil
import tomllib

with open("config.toml","rb") as config_file:
    config = tomllib.load(config_file)

DOWNLOADS_FOLDER = os.path.expanduser(config["directories"]["downloads"])
FILES_FOLDER = os.path.expanduser(config["directories"]["organized_files"])
KEEP_COPY = config["options"]["keep_copy"]


if not DOWNLOADS_FOLDER.endswith("/"):
    DOWNLOADS_FOLDER = DOWNLOADS_FOLDER + "/"

if not FILES_FOLDER.endswith("/"):
    FILES_FOLDER = FILES_FOLDER + "/"


os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)
os.makedirs(FILES_FOLDER, exist_ok=True)


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
        print(f"File already exists: {destination_path}")
    else:
        if KEEP_COPY:
            shutil.copy(origin_path, destination_path)
            print(f"Copied {file_name} to {course}/{section}")
        else:
            shutil.move(origin_path, destination_path)
            print(f"Moved {file_name} to {course}/{section}")

