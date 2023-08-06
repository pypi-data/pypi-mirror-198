from pathlib import Path
import shutil
import os
from colorit import *
import sys


name_extensions = {
    "images": (".jpeg", ".png", ".jpg", ".svg"),
    "video": (".avi", ".mp4", ".mov", ".mkv"),
    "documents": (".doc", ".docx", ".pdf", ".xlsx", ".pptx", ".txt"),
    "music": (".mp3", ".ogg", ".wav", ".amr"),
    "archives": (".zip", ".gz", ".tar"),
    "unknown": ""
}


RUSS_SYMB = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ?<>,!@#[]#$%^&*()-=; "
ENG_SYMB = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "y",
    "",
    "e",
    "yu",
    "ya",
    "je",
    "i",
    "ji",
    "g",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
    "_",
)

TRANS = {}

# current_path = Path("C:\\test_sorted")  поганий кейс(

for c, t in zip(RUSS_SYMB, ENG_SYMB):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()


def normalize(name: str) -> str:
    return name.translate(TRANS)


def unpack_arch(
    archive_path, current_path
):  
    shutil.unpack_archive(archive_path, rf"{current_path}\\archives")


def create_folder(folder: Path):  # створення папок для сортування
    for name in name_extensions.keys():
        if not folder.joinpath(name).exists():
            folder.joinpath(name).mkdir()


def bypass_files(path_folder):
    create_folder(path_folder)
    for item in path_folder.glob("**/*"):
        if item.is_file():
            sort_file(item, path_folder)
        if item.is_dir() and item.name not in list(name_extensions):
            if os.path.getsize(item) == 0:
                shutil.rmtree(item)
            if item.name in name_extensions:
                continue



def sort_file(
    file: Path, path_folder: Path
):  # сорт
    if file.suffix in name_extensions["images"]:
        file.replace(path_folder.joinpath("images", f"{normalize(file.stem)}{file.suffix}"))

    elif file.suffix in name_extensions["documents"]:
        file.replace(path_folder.joinpath("documents", f"{normalize(file.stem)}{file.suffix}"))

    elif file.suffix in name_extensions["music"]:
        file.replace(path_folder.joinpath("music", f"{normalize(file.stem)}{file.suffix}"))

    elif file.suffix in name_extensions["video"]:
        file.replace(path_folder.joinpath("video", f"{normalize(file.stem)}{file.suffix}"))
    
    elif file.suffix in name_extensions["archives"]:
        shutil.unpack_archive(file, path_folder)
        os.remove(file)

    else:
        file.replace(path_folder.joinpath("unknown",f"{normalize(file.stem)}{file.suffix}"))
        
        


def sorting(pathh):
    flag = False
    try:
        current_path = Path(pathh)
    except IndexError:
        print("Type path to folder")
        # return None
    if not current_path.exists():
        print("Folder is not exist. Try again.")
        return color(f"Folder is not exist. Try again.",Colors.red)
    result_list = list(current_path.iterdir())
    bypass_files(current_path)
    flag = True
    for i in result_list:
        print(i, "- sorted")
    return color("Done",Colors.blue) if flag == True else color("Something went wrong",Colors.red)



# .\HW6m.py C:\test_sorted