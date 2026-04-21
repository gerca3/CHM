import math


def func(num) -> float:
    return math.log10(num + 5) - math.cos(num)

def main():
    x, eps, q = map(float, input().split())
    a = eps * (1 - q) / q
    p = x - func(x)
    while abs(p) > a:
        y = func(x)
        p = x - y
        x = y
    
    print(f"Найденный корень: {x}")

if __name__ == "__main__":
    main()