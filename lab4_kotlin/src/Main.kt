import lab_kotlin_oop.Circle
import lab_kotlin_oop.Rectangle
import lab_kotlin_oop.Square

fun main() {
    val rectangle = Rectangle(3.0, 4.0, "синий")
    val circle = Circle(5.0, "красный")
    val square = Square(2.0, "зеленый")

    println(rectangle)
    println(circle)
    println(square)
}