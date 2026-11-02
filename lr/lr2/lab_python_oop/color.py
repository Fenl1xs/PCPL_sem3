class FigureColor:
    def __init__(self, color: str = "прозрачный"):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):
        self._color = value