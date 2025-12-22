package lab_kotlin_oop

abstract class Figure {
    abstract val name: String
    abstract fun area(): Double
    abstract override fun toString(): String
}