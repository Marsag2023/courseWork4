from getvacancy import GetVacancies
from dataprocessing import DataProcessing
from summaryinformation import SummaryInformation


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    :return:
    """
    while True:
        vacancies = GetVacancies('', '')  # создаем экземпляр класса
        code, name = vacancies.get_params()  # Получаем значения города  и профессии
        vacancies = GetVacancies(code, name)  # создаем экземпляр класса с введенными пользователем значениями
        file_vacant = vacancies.get_vacancy_from_api()  # запрашиваем НН.ру и получаем вакансии и записываем в файл
        try:
            if len(file_vacant) != 0:
                break
        except Exception:
            print("Попробуйте выбрать другой город или специальность")
    vacancies_filter = DataProcessing()  # создаем экземпляр класса фильтрации информации от НН.ру
    vacancies_filter.save_info()  # фильтруем информацию от НН.ру и записываем в файл
    payment = vacancies_filter.sort_by_payment()  # сортировка вакансий по начальной зарплате
    output_vacancies = SummaryInformation(payment)   # вывод информации на экран, в файлы JSON, CSV, Exsel
    output_vacancies.output_screen()  # Выводит информацию на экран
    output_vacancies.output_file_json()  # Выводит информацию в файл json
    output_vacancies.output_file_csv()  # Выводит информацию в файл csv
    output_vacancies.output_file_excel()  # Выводит информацию в файл excel
    print("Вся информация по выбранным Вами вакансиям сохранена в различных форматах в папке data")
    print("До новых встреч")


if __name__ == "__main__":
    user_interaction()
