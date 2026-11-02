from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_NAME = "Квадрат"

    def __init__(self, side: float, color: str):
        super().__init__(width=side, height=side, color=color)
        self.side = side

    @classmethod
    def get_figure_name(cls) -> str:
        return cls.FIGURE_NAME

    def __repr__(self) -> str:
        return "{name}: цвет = {color}, сторона = {side}, площадь = {area:.2f}".format(
            name=self.get_figure_name(),
            color=self.figure_color.color,
            side=self.side,
            area=self.area()
        )