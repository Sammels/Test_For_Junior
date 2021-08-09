import os
from shutil import copy
from shutil import SameFileError, SpecialFileError, ExecError
from lxml import etree
from xmltodict import parse


# Парсим
def check_file(xml_path: str, xsd_path: str) -> bool:
    xsd_file_name = xsd_path
    schema_root = etree.parse(xsd_file_name)
    schema = etree.XMLSchema(schema_root)

    xml_filename = xml_path
    xml = etree.parse(xml_filename)

    return schema.check_file(xml)


if __name__ == "__main__":
    path = os.curdir + "/config.xml"
    # Открываем файл, считываем
    try:
        with open(os.curdir + "/config.xml", "r") as xml_file:
            xml_dict = parse(xml_file.read())
            xml_file.close()
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        print('Отказано. Недостаточный уровень прав.ё')
    except Exception as exc:
        print(f'Ошибка: {exc}')

    if any(xml_dict) and check_file(path, "schema.xsd"):
        dict_config = xml_dict['config']['file']

        for work_dict in dict_config:
            src, dst, fname = work_dict['@sourse_path'], work_dict['@destination_path'], work_dict['@file_name']
            try:
                copy(src + fname, dst + fname, follow_symlinks=True)
            except SameFileError:
                print('{} и {} те же каталоги'.format(src, dst))
            except SpecialFileError:
                print('Выполнение операции неподдерживаемой в специальном фа ')
            except ExecError:
                print('Команда не может быть выполненна.')
            except Exception as exc:
                print(f'Error happened: {exc}')
    else:
        print('data from xml invalid')
