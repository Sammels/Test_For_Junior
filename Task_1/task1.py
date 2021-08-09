import os
import re
import xml.etree.ElementTree as ET
import settings
from glob import glob
from platform import system

# Импортнуть либо xml


# 1. Проверить ОС, и выявить Windows, или Linux.
def check_os():
    os_ckecked = system()
    print ("Основаня система: ", os_ckecked)

# 2. Ищем в папке файл config.xml
def find_xml():
    os.chdir(settings.dir_path)
    for file in glob("*.xml"):
        return file

# 3. Считываем файл конфига, парся source_path,destination_path,file_name,
# Cохраняем в отдельные переменные. (Принимаем результат п.2) 
# return source_path, destination_path, file_name

def scan_xml():
    # Определяем вызов функции
    source_path = ""
    destination_path = ""
    file_name = ""

    # Берем и открываем файл.
    file = find_xml()

    open_file = open(file, "r")
    read_open_file = open_file.read()

    # Разобратся позже
    # # Решение для Винды
    win_source_path = read_open_file[43:66]
    print("Windows path: ", win_source_path)

    # # Решение для Линукса
    linx_source_path = read_open_file[191:210]
    print("Linux path: ", linx_source_path)

    # # Пока тут. Пробую в ручную
    print(read_open_file.find(""))

    # Закрываем фаил
    #open_file.close()
    

# 4. Используя эти переменные как пути реализуем копирование файлов.
# Принимаем п.3 source_path, destination_path, file_name, 
# Реализуем копироние по указанным переменным.

def copy_file(scan_xml):
    pass

check_os()
scan_xml()