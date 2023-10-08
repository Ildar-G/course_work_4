import os
from abc import ABC, abstractmethod

import requests as requests


class Api(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class HeadHunter(Api):
    """Класс для работы с API HeadHunter"""

    url = 'https://api.hh.ru/vacancies'

    def __init__(self, text: str, per_page: int, city: int):
        self.text = text
        self.per_page = per_page
        self.area = city

    def get_info(self):
        """Перечень вакансий"""

        response = requests.get(self.url, params=self.__dict__)
        info = response.json()['items']
        return info


class SuperJob(Api):
    """Класс для работы с API SuperJob"""

    API_KEY = {'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')}
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, text: str, t=None, c=None):
        self.keyword = text
        self.t = t
        self.c = c

    def get_info(self):
        """Список вакансий"""
        response = requests.get(self.url, headers=self.API_KEY, params=self.__dict__)
        info = response.json()['objects']
        return info
