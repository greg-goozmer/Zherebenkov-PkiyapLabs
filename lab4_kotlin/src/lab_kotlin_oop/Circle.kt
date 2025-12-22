package lab_kotlin_oop

import kotlin.math.PI
import kotlin.math.pow

class Circle(private val radius: Double, colorName: String) : Figure() {
    override val name = "Круг"
    private val color = Color(colorName)

    override fun area(): Double {
        return PI * radius.pow(2)
    }

    override fun toString(): String {
        return "Фигура: $name, радиус: ${radius}, цвет: ${color.color}, площадь: ${area()}"
    }
}