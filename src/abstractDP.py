from abc import ABC, abstractmethod


class AbstractDP(ABC):
    """
    Абстракный класс, может использоваться при обработке
    других сервисов поиска вакансий
    """

    @abstractmethod
    def save_info(self):
        pass

    @abstractmethod
    def sort_by_payment(self):
        pass

    @abstractmethod
    def delete_of_file(self):
        pass
