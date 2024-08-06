# import shuti
# from pathlib import PurePath
import shutil
from pathlib import Path
import time

# str1 = "Далі сама операція порівняння рядків. Після перетворення обох рядків у однаковий регістр, вони порівнюються"
# str2 = "Далі сама операція порівняння рядків. ПІСЛЯ ПЕРЕТВОРЕННЯ ОБОХ РЯДКІВ У ОДНАКОВИЙ РЕГІСТР, ВОНИ ПОРІВНЮЮТЬСЯ" 

# res = str1.casefold() == str2.casefold() 
# print(res)

# shutil.make_archive("base_name", "zip", root_dir=None, base_dir=None) 
# shutil.unpack_archive('example', extract_dir=None, format='zip')


# my_dir = Path("./docu")
# my_dir.mkdir(parents=True, exist_ok=False)

# my_dir.rmdir()

# path = Path("./docu")

file_path = Path("./docu/expml.txt")


# file_path.write_text("Це значення за замовчуванням. Якщо виникає помилка декодування, буде викинуто виключення UnicodeDecodeError.", encoding="utf-8")

# if my_dir.exists():
#     print(f"{my_dir} is it")

# if my_dir.is_dir():
#     print(f"{my_dir} is directory")

# if file_path.is_file():
#     print(f"{file_path} is file")


# Вихідний і цільовий файли
# source = Path('./docu/expml.txt')
# destination = Path('./expml.txt')

# # Копіювання файла
# shutil.move(destination,source)

file_stat = file_path.stat().st_size
print(file_stat)

creation_time = file_path.stat().st_birthtime
modification_time = file_path.stat().st_mtime
print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")

if file_path.exists():
    file_path.unlink(missing_ok=True)
    print(f"{file_path.name} was deleted")
else: 
    print(f"{file_path.name} is not in this dir")
