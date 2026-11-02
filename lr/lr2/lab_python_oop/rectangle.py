from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_NAME = "Прямоугольник"

    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.figure_color = FigureColor(color)

    @classmethod
    def get_figure_name(cls) -> str:
        return cls.FIGURE_NAME

    def area(self) -> float:
        return float(self.width * self.height)

    def __repr__(self) -> str:
        return "{name}: цвет = {color}, ширина = {width}, высота = {height}, площадь = {area:.2f}".format(
            name=self.get_figure_name(),
            color=self.figure_color.color,
            width=self.width,
            height=self.height,
            area=self.area()
        )