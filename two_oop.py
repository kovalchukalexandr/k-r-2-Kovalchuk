sequence = [1, 2, 2, 3, 1, 0, -1, -1, -2, -2]

def max_monotonic_length(sequence):
    if not sequence:
        return 0

    max_length = 1
    current_length = 1
    is_non_decreasing = True
    is_non_increasing = True

    for i in range(1, len(sequence)):
        # Проверяем на убывание
        if sequence[i] >= sequence[i - 1]:
            if is_non_increasing:
                is_non_increasing = False
                current_length = 1
            current_length += 1
        # Проверяем на возрастание
        elif sequence[i] <= sequence[i - 1]:
            if is_non_decreasing:
                is_non_decreasing = False
                current_length = 1
            current_length += 1
        else:
            current_length = 1

        # После мы проверяем, какая из последовательностей больше(для ответа)
        max_length = max(max_length, current_length)  # Обновляем максимальную длину

    return max_length

result = max_monotonic_length(sequence)
print("Длина максимальной монотоности: ", result)