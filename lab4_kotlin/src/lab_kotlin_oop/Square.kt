package lab_kotlin_oop

class Square(side: Double, colorName: String) : Rectangle(side, side, colorName) {
    override val name = "Квадрат"


    override fun toString(): String {
        val side = width
        return "Фигура: $name, ширина: $side, цвет: ${color.color}, площадь: ${area()}"
    }
}