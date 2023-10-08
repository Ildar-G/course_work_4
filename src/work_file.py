from abc import ABC
import json


class Working_file(ABC):
    """Абстрактный класс для работы с файлами"""

    @staticmethod
    def read():
        pass

    @staticmethod
    def write():
        pass


class Json_file(Working_file):
    """Класс для работы с JSON-файлами"""
    @staticmethod
    def read_json():

        """Чтениe из JSON-файла"""
        with open('vacancies.json', 'r', encoding='utf-8') as file:
            info = json.load(file)
            return info

    @staticmethod
    def write_json(info):
        """Запись информации в JSON-файл"""

        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(info, file, indent=4, ensure_ascii=False)

    @staticmethod
    def add_json(info):
        """Добавление информации в JSON-файл"""

        all_info = Json_file.read_json()
        for i in info:
            all_info.append(i)
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(all_info, file, indent=4, ensure_ascii=False)
