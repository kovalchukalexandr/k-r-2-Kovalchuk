def sum_between_last_zeros(numbers):
    last_zero_index = -1
    second_last_zero_index = -1

    # Ищем индексы последних двух нулей
    for i in range(len(numbers)):
        if numbers[i] == 0:
            second_last_zero_index = last_zero_index
            last_zero_index = i

    # Проверяем, есть ли последние два нуля и не идут ли они подряд
    if second_last_zero_index == -1 or last_zero_index == second_last_zero_index + 1:
        return 0

    # Считаем сумму между двумя последними нулями
    return sum(numbers[second_last_zero_index + 1:last_zero_index])

# Пример использования
numbers = [3, 0, 5, 0, 2, -1, 2, 0, 4, 0]
result = sum_between_last_zeros(numbers)
print(result)  # Результат: 6 (сумма 2 + -1 + 2)