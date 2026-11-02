import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
class Circle(Figure):
    FIGURE_NAME='Круг'
    def __init__(self,radius:float,color:str):
        self.radius=radius
        self.figure_color=FigureColor(color)
    @classmethod
    def get_figure_name(cls) ->str:
        return cls.FIGURE_NAME
    def area(self) -> float:
        return math.pi*(self.radius**2)
    def __repr__(self) ->str:
        return "{name}:цвет={color},радиус={radius},площадь={area:.2f}".format(
            name=self.get_figure_name(),
            color=self.figure_color.color,
            radius=self.radius,
            area=self.area()
        )