import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')

    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)
    finally_roots = []

    if len(roots) == 0:
        print('Нет корней')
    else:
        for el in roots:
            if el > 0:
                finally_roots.append(el**0.5)
                finally_roots.append(el**0.5 * (-1))
            elif el == 0:
                finally_roots.append(0)

    if len(finally_roots) == 1:
        print(f'Один корень: {finally_roots[0]}')
    elif len(finally_roots) == 2:
        print(f'Два корня: {finally_roots[0]} и {finally_roots[1]}')
    elif len(finally_roots) == 3:
        print(f'Три корня: {finally_roots[0]}, {finally_roots[1]}, {finally_roots[2]}')
    elif len(finally_roots) == 4:
        print(f'Четыре корня: {finally_roots[0]}, {finally_roots[1]}, {finally_roots[2]}, {finally_roots[3]}')

if __name__ == "__main__":
    main()