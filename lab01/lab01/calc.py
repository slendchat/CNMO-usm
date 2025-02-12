import math

def f(x):
    return math.exp(-0.7 * x) - (0.3 * math.sqrt(x) - 1)

def bisection_method(a, b, tol=0.0000001):
    while (b - a) / 2 > tol:
        mid = (a + b) / 2
        print(f"[+]центр отрезка: {mid:.7f}")
        f_a = f(a)
        f_b = f(b)
        f_mid = f(mid)

        if f_a < 0:
            print(f"[!]левая точка f({a:.7f}) < 0")
        else:
            print(f"[!]левая точка f({a:.7f}) > 0")

        if f_mid < 0:
            print(f"[!]центр f({mid:.7f}) < 0")
        else:
            print(f"[!]центр f({mid:.7f}) > 0")

        if f_b < 0:
            print(f"[!]правая точка f({b:.7f}) < 0")
        else:
            print(f"[!]правая точка f({b:.7f}) > 0")
        
        if f_a * f_mid < 0:
            b = mid
        else:
            a = mid
        interval = b-a
        print(f"[i]длина интервала: {interval:.7f}")
    return (a + b) / 2

# Интервал, на котором ищем пересечение
interval_a = 11.115
interval_b = 11.125

# Найдём корень
root = bisection_method(interval_a, interval_b)
print(f"Точка пересечения: {root:.10f}")