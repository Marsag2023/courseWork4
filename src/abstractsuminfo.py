from abc import ABC, abstractmethod


class AbstractSuminfo(ABC):
    """
    Абстрактный класс, может использоваться при обработке
    других сервисов поиска вакансий
    """

    @abstractmethod
    def output_screen(self):
        pass

    @abstractmethod
    def output_file_csv(self):
        pass

    @abstractmethod
    def output_file_json(self):
        pass

    @abstractmethod
    def output_file_excel(self):
        pass
