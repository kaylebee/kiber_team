import math

def solve_quadratic_equation(a, b, c):
    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c

    # Если дискриминант меньше нуля, корней нет
    if discriminant < 0:
        return "Нет действительных корней"

    # Если дискриминант равен нулю, один корень
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Один корень: x = {x}"

    # Если дискриминант больше нуля, два корня
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Два корня: x1 = {x1}, x2 = {x2}"

# Пример использования
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

result = solve_quadratic_equation(a, b, c)
print(result)