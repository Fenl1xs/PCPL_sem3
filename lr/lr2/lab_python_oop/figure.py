from abc import ABC,abstractmethod
class Figure(ABC):
    @classmethod
    @abstractmethod
    def get_figure_name(cls) -> str:
        pass
    @abstractmethod
    def area(self) -> float:
        pass