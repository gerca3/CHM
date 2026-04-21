import math


def func(num) -> float:
    return math.log10(num + 5) - math.cos(num)

def main():
    a, b = map(float, input("Введите границы отрезка через запятую: ").split(", "))
    if a >= 5 or b >= 5:
        raise ValueError("Ошибка! Введите число меньше 5!")
    limit = pow(10, -3)

    while True:
        c = (a + b) / 2
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
        if (b - a) <= limit:
            break
    
    x = (a + b) / 2
    print(f"Найденный корень: {x:.6f}")

if __name__ == "__main__":
    main()