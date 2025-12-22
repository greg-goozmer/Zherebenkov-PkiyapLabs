import kotlin.math.sqrt

fun readCoefficient(name: String): Double {
    while (true) {
        print("Введите коэффициент $name: ")
        try {
            return readLine()!!.toDouble()
        } catch (e: NumberFormatException) {
            println("Ошибка: коэффициент должен быть действительным числом. Попробуйте снова.")
        }
    }
}

fun main(args: Array<String>) {
    val coefficients = mutableListOf<Double>()

    if (args.size >= 3) {
        for (i in 0..2) {
            try {
                coefficients.add(args[i].toDouble())
            } catch (e: NumberFormatException) {
                println("Некорректный аргумент: ${args[i]}. Будет запрошен ввод с клавиатуры.")
                coefficients.clear()
                break
            }
        }
    }

    if (coefficients.size < 3) {
        coefficients.clear()
        coefficients.add(readCoefficient("A"))
        coefficients.add(readCoefficient("B"))
        coefficients.add(readCoefficient("C"))
    }

    val (a, b, c) = coefficients

    if (a == 0.0) {
        println("Коэффициент A не может быть равен нулю для биквадратного уравнения")
        return
    }

    val discriminant = b * b - 4 * a * c

    when {
        discriminant < 0 -> println("Действительных корней нет")
        discriminant == 0.0 -> {
            val y = -b / (2 * a)
            if (y < 0) {
                println("Действительных корней нет")
            } else {
                val x1 = sqrt(y)
                val x2 = -sqrt(y)
                println("Уравнение имеет два корня: x1 = ${"%.3f".format(x1)}, x2 = ${"%.3f".format(x2)}")
            }
        }
        else -> {
            val y1 = (-b - sqrt(discriminant)) / (2 * a)
            val y2 = (-b + sqrt(discriminant)) / (2 * a)

            val roots = mutableListOf<Double>()

            if (y1 >= 0) {
                roots.add(sqrt(y1))
                roots.add(-sqrt(y1))
            }
            if (y2 >= 0) {
                roots.add(sqrt(y2))
                roots.add(-sqrt(y2))
            }

            when {
                roots.isEmpty() -> println("Действительных корней нет")
                roots.size == 2 -> println("Уравнение имеет два корня: x1 = ${"%.3f".format(roots[0])}, x2 = ${"%.3f".format(roots[1])}")
                roots.size == 4 -> println("Уравнение имеет четыре корня: x1 = ${"%.3f".format(roots[0])}, x2 = ${"%.3f".format(roots[1])}, x3 = ${"%.3f".format(roots[2])}, x4 = ${"%.3f".format(roots[3])}")
            }
        }
    }
}