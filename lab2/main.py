from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import Fore, Back, Style, init

init(autoreset=True)

def main():
    print(Fore.CYAN + '_' * 20)

    myRectangle = Rectangle('Прямоугольник', 10, 10, "Синий")
    myRectangle.print_shape()
    myRectangle.repr()

    print(Fore.CYAN + "_" * 20)

    myCircle = Circle("Круг", 10, "Зеленый")
    myCircle.print_shape()
    myCircle.repr()

    print(Fore.CYAN + "_" * 20)

    mySquare = Square("Квадрат", 10, "Красный")
    mySquare.print_shape()
    mySquare.repr()

    print(Fore.CYAN + "_" * 20)

if __name__ == "__main__":
    main()
