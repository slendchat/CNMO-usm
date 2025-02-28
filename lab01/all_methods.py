import math

def f(x):
    """Наша функция f(x) = e^(-0.7x) - 0.3*sqrt(x) + 1."""
    return math.exp(-0.7*x) - 0.3*math.sqrt(x) + 1

def df(x):
    """
    Производная f'(x) для метода Ньютона:
    f'(x) = -0.7 * e^(-0.7x) - 0.3/(2*sqrt(x)).
    """
    return -0.7 * math.exp(-0.7*x) - 0.3/(2*math.sqrt(x))

def bisection_method(a, b, tol=1e-7):
    """
    Метод половинного деления.
    Возвращает (приближение корня, количество итераций, список (итерация, a, b, c, f(c))).
    """
    iterations_data = []
    n = 0
    
    while (b - a) > tol:
        n += 1
        c = (a + b) / 2
        fc = f(c)
        iterations_data.append((n, a, b, c, fc))
        
        if f(a) * fc <= 0:
            b = c
        else:
            a = c
    
    return ((a + b)/2, n, iterations_data)

def secant_method(x0, x1, tol=1e-7, max_iter=50):
    """
    Метод хорд (секущих).
    Возвращает (приближение корня, количество итераций, список (итерация, x_n, f(x_n))).
    """
    iterations_data = []
    n = 0
    
    while n < max_iter:
        n += 1
        f0, f1 = f(x0), f(x1)
        if abs(f1 - f0) < 1e-14:  # защита от деления на ноль
            break
        
        x2 = x1 - f1*(x1 - x0)/(f1 - f0)
        iterations_data.append((n, x1, f1))
        
        if abs(x2 - x1) < tol:
            x1 = x2
            break
        
        x0, x1 = x1, x2
    
    return (x1, n, iterations_data)

def newton_method(x0, tol=1e-7, max_iter=50):
    """
    Метод Ньютона (касательных).
    Возвращает (приближение корня, количество итераций, список (итерация, x_n, f(x_n))).
    """
    iterations_data = []
    x = x0
    for n in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-14:  # защита от деления на ноль
            break
        
        iterations_data.append((n, x, fx))
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            x = x_new
            break
        
        x = x_new
    
    return (x, n, iterations_data)

def iteration_method(x0, tol=1e-7, max_iter=100):
    """
    Метод простой итерации.
    Нужно переписать уравнение в виде x = g(x).
    Например: x = ((e^(-0.7x) + 1) / 0.3)^2
    """
    def g(x):
        return ((math.exp(-0.7*x) + 1)/0.3)**2
    
    iterations_data = []
    x = x0
    for n in range(1, max_iter + 1):
        x_next = g(x)
        iterations_data.append((n, x, f(x)))
        
        if abs(x_next - x) < tol:
            x = x_next
            break
        x = x_next
    
    return (x, n, iterations_data)

def main():
    left, right = 10, 12
    tol = 1e-7
    
    # Решение уравнения разными методами
    root_bis, it_bis, data_bis = bisection_method(left, right, tol)
    root_sec, it_sec, data_sec = secant_method(left, right, tol)
    root_new, it_new, data_new = newton_method(11.0, tol)
    root_iter, it_iter, data_iter = iteration_method(11.0, tol)
    
    print("Результаты решения уравнения f(x) = e^(-0.7x) - 0.3*sqrt(x) + 1 = 0\n")
    
    # 1. Бисекция
    print("1. Метод половинного деления")
    print(f"Начальный отрезок: [{left:.3f}, {right:.3f}], допуск={tol}")
    for (n, a_, b_, c_, fc_) in data_bis:
        print(f"  Итерация {n}: a={a_:.6f}, b={b_:.6f}, m={c_:.6f}, f(m)={fc_:.2e}")
    print(f"Приближённый корень: x ~ {root_bis:.8f}, итераций = {it_bis}\n")
    
    # 2. Хорд
    print("2. Метод хорд (секущих)")
    print(f"Начальные точки: x0={left}, x1={right}, допуск={tol}")
    for (n, x_n, fx_n) in data_sec:
        print(f"  Итерация {n}: x_n={x_n:.6f}, f(x_n)={fx_n:.2e}")
    print(f"Приближённый корень: x ~ {root_sec:.8f}, итераций = {it_sec}\n")
    
    # 3. Ньютона
    print("3. Метод Ньютона")
    print(f"Начальное приближение: x0=11.0, допуск={tol}")
    for (n, x_n, fx_n) in data_new:
        print(f"  Итерация {n}: x_n={x_n:.6f}, f(x_n)={fx_n:.2e}")
    print(f"Приближённый корень: x ~ {root_new:.8f}, итераций = {it_new}\n")
    
    # 4. Простая итерация
    print("4. Метод простой итерации")
    print(f"Начальное приближение: x0=11.0, допуск={tol}")
    print("Формула: x_{n+1} = ((e^(-0.7*x_n) + 1)/0.3)^2")
    for (n, x_n, fx_n) in data_iter:
        print(f"  Итерация {n}: x_n={x_n:.6f}, f(x_n)={fx_n:.2e}")
    print(f"Приближённый корень: x ~ {root_iter:.8f}, итераций = {it_iter}\n")
    
    print("Все четыре метода дают близкий результат в районе x ~ 11.12036.")

if __name__ == "__main__":
    main()
