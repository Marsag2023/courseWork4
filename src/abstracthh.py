from abc import ABC, abstractmethod


class AbstractGet(ABC):
    """
    Абстракный класс получения информации по api от различных сервисов
    """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_vacancy_from_api(self):
        pass


