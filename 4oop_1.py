# Создать базовый класс с функцией – сумма прогрессии. Создать производные классы:
# арифметическая прогрессия и геометрическая прогрессия. Каждый класс имеет два поля
# типа double. Первое – первый член прогрессии, второе – постоянная разность
# (для арифметической) и постоянное отношение (для геометрической). Определить функцию
# вычисления суммы, где параметром является количество элементов прогрессии.


first_term = int(input("Введите первое число прогрессии: "))
common_difference = int(input("Введите последнее число прогрессии: "))
N = int(input("Введите количество элементов прогрессии: "))


class Progression:
    # Выведем значения first_term и common_difference
    def __init__(self, first_term, common_difference):
        self.first_term = first_term
        self.common_difference = common_difference


    def sum(self, n):
        raise NotImplementedError("Этот метод следует переопределить в производных классах.")

# Создадим класс для нахождения арифметической прогрессии
class ArithmeticProgression(Progression):
    def __init__(self, first_term, common_difference):
        super().__init__(first_term, common_difference)

    # Выведем форму суммы первых n членов арифметической прогрессии
    def sum(self, n):
        return n / 2 * (2 * self.first_term + (n - 1) * self.common_difference)


# Создадим класс для нахождения геометрической прогрессии
class GeometricProgression(Progression):
    def __init__(self, first_term, common_ratio):
        super().__init__(first_term, common_ratio)

    # Выведем форму суммы первых n членов геометрической прогрессии
    def sum(self, n):
        if self.common_difference == 1:
            return n * self.first_term
        else:
            return self.first_term * (1 - self.common_difference**n) / (1 - self.common_difference)


arithmetic_progression = ArithmeticProgression(first_term, common_difference)
geometric_progression = GeometricProgression(first_term, common_difference)

print(f"Сумма первых {N} членов арифметической прогрессии:", arithmetic_progression.sum(N))
print(f"Сумма первых {N} членов геометрической прогрессии:", geometric_progression.sum(N))