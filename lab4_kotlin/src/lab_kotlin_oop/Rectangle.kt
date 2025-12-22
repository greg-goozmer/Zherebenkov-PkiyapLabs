package lab_kotlin_oop


open class Rectangle(protected val width: Double, private val height: Double, colorName: String) : Figure() {
    override val name = "Прямоугольник"
    val color = Color(colorName)

    override fun area(): Double {
        return width * height
    }

    override fun toString(): String {
        return "Фигура: $name, ширина: $width, высота: $height, цвет: ${color.color}, площадь: ${area()}"
    }
}