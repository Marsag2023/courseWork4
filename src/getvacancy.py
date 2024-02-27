import requests
import json
from abstracthh import AbstractGet
from mixinlog import MixinLog


class GetVacancies(AbstractGet, MixinLog):

    def __init__(self, code, name):
        super().__init__()
        self.code_country: int = code
        self.name_vacancy: str = name
        self.url = 'https://api.hh.ru/vacancies'
        self.all_vacancy: list = []

    def get_vacancy_from_api(self):  # json словарь
        """
        Получаем информацию по вакансиям с сайта НН.ру
        :return:
        """
        param_response = {'text': f'NAME:{self.name_vacancy}', 'area': {self.code_country},
                          "only_with_salary": "true", 'per_page': 100}
        response = requests.get(f"{self.url}", param_response)
        try:
            response.status_code == 200
        except ValueError:
            print("Вакансии не найдены")
        else:
            self.all_vacancy = json.loads(response.text)['items']
        if len(self.all_vacancy) == 0:
            print("Вакансии не найдены")
        else:
            with open("../data/all_vacancy.json", 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.all_vacancy, ensure_ascii=False))
                print(f" Найдено вакансий: {len(self.all_vacancy)} ")
        return self.all_vacancy
