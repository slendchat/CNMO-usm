import numpy as np

# Данные из варианта 11
x = np.array([0.119, 0.718, 1.342, 2.859, 3.948])
y = np.array([-0.572, -2.015, -3.342, -6.752, -6.742])

def lagrange_poly(xi, yi):
    """
    Возвращает numpy.poly1d полином Лагранжа,
    проходящий через узлы (xi, yi).
    """
    n = len(xi)
    P = np.poly1d([0.0])
    for i in range(n):
        # начинаем с единицы для базиса L_i(x)
        Li = np.poly1d([1.0])
        for j in range(n):
            if j != i:
                # умножаем на (x - xj)/(xi - xj)
                Li *= np.poly1d([1.0, -xi[j]]) / (xi[i] - xi[j])
        # добавляем вклад y_i * L_i(x)
        P += yi[i] * Li
    return P

# строим полином
P = lagrange_poly(x, y)

# выводим полином и его коэффициенты
print("Интерполяционный полином Лагранжа (P):")
print(P)
print("\nКоэффициенты [от x^4 до константы]:")
print(P.coeffs)

