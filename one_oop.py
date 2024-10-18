import re
def check_decimal_number(input_str):
    # pattern - проверка числе (явл. ли дробным)
    pattern = r'^[+-]?\d*\.\d+$|^([+-]?\d+\.)|(\.\d+)$|^[+-]?\d+$'
    # Выполним проверку, является ли данное число дробным
    if re.match(pattern, input_str):
        parts = input_str.split('.')
        if len(parts) == 2:
            integer_part = parts[0].lstrip('+').lstrip('-')
            fractional_part = parts[1]
            # Выделяем целую и дробную часть
            print("Целая часть:", len(integer_part))
            print("Дробная часть:", len(fractional_part))
        else:
            number = input_str.lstrip('+').lstrip('-')
            if '.' in number:
                fractional_part = number.split('.')[1]
                print("Целая часть: 0")
                print("Дробная часть:", len(fractional_part))
            else:
                print("Целая часть:", len(number))
                print("Дробная часть: 0")
    else:
        print("Введенная строка не является десятичным числом с целой и дробной частью.")
input_str = input("Введите строку: ")
check_decimal_number(input_str)