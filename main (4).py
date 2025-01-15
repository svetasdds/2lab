import math

def task1():
    # If13: Найти среднее из трёх чисел
    print("\nЗадача 1: Найти среднее из трёх чисел.")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    # Определение среднего
    numbers = [a, b, c]
    numbers.sort()
    middle = numbers[1]
    print(f"Среднее число: {middle}\n")


def task2():
    # Задача 2: Количество точек в области
    print("\nЗадача 2: Определить количество точек в заданной области (чёрная зона, вариант 29).")
    r = float(input("Введите радиус окружности (r): "))
    n = int(input("Введите количество точек: "))
    points = []
    for i in range(n):
        x, y = map(float, input(f"Введите координаты точки {i + 1} (x y): ").split())
        points.append((x, y))

    def is_in_black_area(x, y, r):
        in_circle = x**2 + y**2 <= r**2  # Точка в круге
        in_lower_half = y <= 0  # Точка в нижней полуплоскости
        outside_triangle = y < -x and y < x  # Точка вне треугольника
        return in_circle and in_lower_half and outside_triangle

    count = 0
    for x, y in points:
        if is_in_black_area(x, y, r):
            count += 1

    print(f"Количество точек в чёрной области (вариант 29): {count}\n")


def task3():
    # Задача 3: Исследование ряда на сходимость
    print("\nЗадача 3: Исследовать ряд на сходимость.")
    x = float(input("Введите значение x: "))
    epsilon = float(input("Введите epsilon (e): "))
    g = float(input("Введите g: "))

    n = 1
    sum_series = 0
    is_divergent = False

    while True:
        numerator = math.factorial(2 + n)  # Числитель: (2 + n)!
        denominator = (x**n) * (2**(2*n + 1))  # Знаменатель: x^n * 2^(2n+1)
        u_n = numerator / denominator

        sum_series += u_n

        if abs(u_n) < epsilon:
            print(f"Ряд сходится. Сумма: {sum_series}")
            break
        elif abs(u_n) > g:
            print("Ряд расходится.")
            is_divergent = True
            break

        n += 1

    if not is_divergent:
        print(f"Сумма ряда: {sum_series}")
        print(f"Количество итераций: {n}\n")


# Основная программа
while True:
    print("Выберите задачу для выполнения:")
    print("1: Найти среднее из трёх чисел (задача 1)")
    print("2: Определить количество точек в области (задача 2)")
    print("3: Исследовать ряд на сходимость (задача 3)")
    print("0: Выход")
    
    choice = input("Ваш выбор: ")
    
    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "0":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.\n")
