import math


def func(num) -> float:
    return math.log10(num + 5) - math.cos(num)

def main():
    a, b, eps = map(float, input().split())
    n = 0
    while True:
        if (func(a) * func(a) ** n) < 0:
            xh = b
            x_0 = a
        else:
            xh = a
            x_0 = b
        x = x_0 - ((xh - x_0) / (func(xh) - func(x_0)) * func(x_0))
        x_0 = x
        n += 1
        if abs(func(x)) < eps:
            break
    
    
    print(f"Найденный корень: {x}")

if __name__ == "__main__":
    main()