import json
import os
from collections import defaultdict
from abstractDP import AbstractDP


class DataProcessing(AbstractDP):
    def __init__(self):
        self.data_sort = []
        self.payment_1 = []
        self.payment_2 = []
        self.payment_3 = []
        self.payment_4 = []
        self.payment_5 = []
        self.payment_6 = []

    def save_info(self):
        """
        Фильтрует файл и сохраняет в файл  необходимые значения

        """
        data = defaultdict(None)
        file_path = os.path.abspath("../data/all_vacancy.json")
        with open(file_path, 'r', encoding='UTF-8') as file:
            if len("../data/all_vacancy.json") > 0:
                counter = 0
                for inform in json.load(file):
                    if inform["snippet"]["requirement"] is None:
                        requirement = "НЕТ"
                    else:
                        requirement = inform["snippet"]["requirement"]
                    if inform["snippet"]["responsibility"] is None:
                        responsibility = "НЕТ"
                    else:
                        responsibility = inform["snippet"]["responsibility"]
                    if inform["salary"]["from"] is None:
                        salary_from = 0
                    else:
                        salary_from = inform["salary"]["from"]
                    if inform["salary"]["to"] is None:
                        salary_to = 0
                    else:
                        salary_to = inform["salary"]["to"]
                    if inform["salary"]["currency"] == "USD" or inform["salary"]["currency"] == "EUR":
                        salary_currency = "RUB"
                        salary_from = salary_from * 100
                        salary_to = salary_to * 100
                    else:
                        salary_currency = inform["salary"]["currency"]
                    data = {
                            'city': inform["area"]["name"],
                            'profession': inform["name"],
                            "requirement": requirement,
                            "responsibility": responsibility,
                            'salary_from': int(salary_from),
                            'salary_to': int(salary_to),
                            'salary_currency': salary_currency,
                            'url': inform["alternate_url"]
                        }
                    self.data_sort.append(data)
                    counter += 1
                with open("../data/vacancy.json", 'w', encoding='UTF-8') as file1:
                    file1.write(json.dumps(self.data_sort, ensure_ascii=False))
                print(f"В городе {data['city']} найдено вакансий -- {counter} ")
            else:
                print("Вакансии по этой специальности  не найдены")

    def sort_by_payment(self):
        """
        Сортировка вакансий по начальной зарплате
        :return:
        """
        file_path = os.path.abspath("../data/vacancy.json")
        with open(file_path, 'r', encoding='UTF-8') as file:
            for inform in json.load(file):
                if 0 <= int(inform['salary_from']) < 100000:
                    self.payment_1.append(inform)
                elif 100000 <= int(inform['salary_from']) < 200000:
                    self.payment_2.append(inform)
                elif 200000 <= int(inform['salary_from']) < 300000:
                    self.payment_3.append(inform)
                elif 300000 <= int(inform['salary_from']) < 400000:
                    self.payment_4.append(inform)
                elif 400000 <= int(inform['salary_from']) < 500000:
                    self.payment_5.append(inform)
                else:
                    self.payment_6.append(inform)
        print(f'1. C начальной заработной платой в диапазоне от 0 до 100 тысяч руб. вакансий : {len(self.payment_1)}')
        print(f'2. C начальной заработной платой в диапазоне от 100 до 200 тысяч руб. вакансий: {len(self.payment_2)}')
        print(f'3. C начальной заработной платой в диапазоне от 200 до 300 тысяч руб. вакансий: {len(self.payment_3)}')
        print(f'4. C начальной заработной платой в диапазоне от 300 до 400 тысяч руб. вакансий: {len(self.payment_4)}')
        print(f'5. C начальной заработной платой в диапазоне от 400 до 500 тысяч руб. вакансий: {len(self.payment_5)}')
        print(f'6. C начальной заработной платой больше 500 тысяч рублей найдено вакансий : {len(self.payment_6)}\n')
        while True:
            choice = int(input("Введите корректное число строки, какие вакансии Вы хотели бы просмотреть\n"))
            try:
                if choice in [1, 2, 3, 4, 5, 6]:
                    break
            except ValueError:
                print("Ошибка: введите корректное число")
        if choice == 1:
            return self.payment_1
        elif choice == 2:
            return self.payment_2
        elif choice == 3:
            return self.payment_3
        elif choice == 4:
            return self.payment_4
        elif choice == 5:
            return self.payment_5
        else:
            return self.payment_6

    def delete_of_file(self):
        pass

