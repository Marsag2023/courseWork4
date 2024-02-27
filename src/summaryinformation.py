import csv
import json
import pandas as pd
from abstractsuminfo import AbstractSuminfo


class SummaryInformation(AbstractSuminfo):
    """
    Вывод информации на экран, в файлы JSON, CSV, Exsel 

    """
    def __init__(self, result_list):
        self.result_list = result_list

    def output_screen(self):
        """
        Выводит информацию на экран
        :return:
        """
        for result in self.result_list:
            print(f"""Город: {result['city']}
Должность: {result['profession']}
Требование: {result['requirement']}
Ответственность : {result['responsibility']}
Зарплата от {result['salary_from']} до {result['salary_to']} {result['salary_currency']}
Ссылка на сайт hh.ru: {result['url']}\n""")

    def output_file_csv(self):
        """
        Выводит информацию в файл csv
        :return:
        """
        with open("../data/result.csv", 'w', encoding='UTF-8', newline='') as csvfile:
            fieldnames = ['city', 'profession', 'requirement', 'responsibility', 'salary_from', 'salary_to',
                          'salary_currency', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for line in self.result_list:
                writer.writerow(line)

    def output_file_json(self):
        """
        Выводит информацию в файл JSON
        :return:
        """
        with open("../data/result.json", 'w', encoding='UTF-8') as file:
            file.write(json.dumps(self.result_list, ensure_ascii=False))

    def output_file_excel(self):
        """
        Выводит информацию в файл excel
        :return:
        """
        pd.read_csv("../data/result.csv", sep=",",
                    encoding="UTF-8").to_excel("../data/result.xlsx", index = None)
