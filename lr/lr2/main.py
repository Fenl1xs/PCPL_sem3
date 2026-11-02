from colorama import init, Fore, Style
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    init(autoreset=True)

    n = 5

    rect = Rectangle(width=n, height=n, color="синий")
    circ = Circle(radius=n, color="зеленый")
    sq = Square(side=n, color="красный")

    print(Fore.CYAN + Style.BRIGHT + "=== Результаты работы программы (N = {}) ===".format(n))
    print(Fore.BLUE + repr(rect))
    print(Fore.GREEN + repr(circ))
    print(Fore.RED + repr(sq))


if __name__ == "__main__":
    main()