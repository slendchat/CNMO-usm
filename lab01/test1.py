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
        
        if f(a)*fc <= 0:
            b = c
        else:
            a = c
    
    return ( (a + b)/2, n, iterations_data )

def secant_method(x0, x1, tol=1e-7, max_iter=50):
    """
    Метод хорд (секущих).
    Возвращает (приближение корня, количество итераций, список (итерация, x_{n}, f(x_{n}))).
    """
    iterations_data = []
    n = 0
    
    while n < max_iter:
        n += 1
        f0, f1 = f(x0), f(x1)
        if abs(f1 - f0) < 1e-14:  # защита от деления на 0
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
    for n in range(1, max_iter+1):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-14:  # защита от деления на 0
            break
        
        iterations_data.append((n, x, fx))
        x_new = x - fx/dfx
        
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
    for n in range(1, max_iter+1):
        x_next = g(x)
        iterations_data.append((n, x, f(x)))
        
        if abs(x_next - x) < tol:
            x = x_next
            break
        x = x_next
    
    return (x, n, iterations_data)

def main():
    # Параметры
    left, right = 10, 12
    tol = 1e-7
    
    # Считаем корни разными методами
    root_bis, it_bis, data_bis = bisection_method(left, right, tol)
    root_sec, it_sec, data_sec = secant_method(left, right, tol)
    root_new, it_new, data_new = newton_method(10.0, tol)
    root_iter, it_iter, data_iter = iteration_method(10.0, tol)
    
    with open("res.md", "w", encoding="utf-8") as f_out:
        f_out.write("# Результаты решения уравнения\n\n")
        f_out.write("Уравнение:\n")
        f_out.write(r"$$ f(x) = e^{-0.7x} - 0.3\sqrt{x} + 1 = 0 $$")
        f_out.write("\n\n")
        
        # 1. Бисекция
        f_out.write("## 1. Метод половинного деления\n")
        f_out.write(r"Начальный отрезок: $[%.3f,\; %.3f]$, допуск $=%.1e$" 
                    % (left, right, tol))
        f_out.write("\n\n")
        for (n, a_, b_, c_, fc_) in data_bis:
            f_out.write(
                rf"Итерация {n}: $a={a_:.6f},\, b={b_:.6f},\, m=\frac{{a+b}}{{2}}={c_:.6f},\, f(m)={fc_:.2e}$  \\" 
                "\n"
            )
        f_out.write("\n")
        f_out.write(rf"Приближённый корень: $x \approx {root_bis:.8f}$, итераций = {it_bis}\n\n")
        
        # 2. Хорд (Секущих)
        f_out.write("## 2. Метод хорд (секущих)\n")
        f_out.write(r"Начальные точки: $x_0=%.1f,\; x_1=%.1f$, допуск $=%.1e$" % (left, right, tol))
        f_out.write("\n\n")
        for (n, x_n, fx_n) in data_sec:
            f_out.write(
                rf"Итерация {n}: $x_n={x_n:.6f},\, f(x_n)={fx_n:.2e}$  \\" 
                "\n"
            )
        f_out.write("\n")
        f_out.write(rf"Приближённый корень: $x \approx {root_sec:.8f}$, итераций = {it_sec}\n\n")
        
        # 3. Метод Ньютона
        f_out.write("## 3. Метод Ньютона\n")
        f_out.write(r"Начальное приближение: $x_0=10.0$, допуск $=%.1e$" % tol)
        f_out.write("\n\n")
        for (n, x_n, fx_n) in data_new:
            f_out.write(
                rf"Итерация {n}: $x_n={x_n:.6f},\, f(x_n)={fx_n:.2e}$  \\" 
                "\n"
            )
        f_out.write("\n")
        f_out.write(rf"Приближённый корень: $x \approx {root_new:.8f}$, итераций = {it_new}\n\n")
        
        # 4. Метод простой итерации
        f_out.write("## 4. Метод простой итерации\n")
        f_out.write(r"Начальное приближение: $x_0=10.0$, допуск $=%.1e$" % tol)
        f_out.write("\n\n")
        f_out.write(r"Перепишем уравнение в виде: $x = g(x) = \left(\frac{e^{-0.7x} + 1}{0.3}\right)^2$")
        f_out.write("\n\n")
        for (n, x_n, fx_n) in data_iter:
            f_out.write(
                rf"Итерация {n}: $x_n={x_n:.6f},\, f(x_n)={fx_n:.2e}$  \\" 
                "\n"
            )
        f_out.write("\n")
        f_out.write(rf"Приближённый корень: $x \approx {root_iter:.8f}$, итераций = {it_iter}\n\n")
        
        f_out.write("---\n")
        f_out.write("**Все четыре метода дают близкий результат в районе **")
        f_out.write(rf"$x \approx 11.12036$.\n")

if __name__ == "__main__":
    main()
