import re

# Значения шестнадцатиричного идентификатора цвета в HTML
test_cases = ['#FFFFFF', '#FF3421', '#00ff00', '232323', 'f#fddee', '#fd2']

def is_hex_color(code):
    # В данной строке идёт проверка шестнадцатиричного цвета
    hex_color_pattern = r'^#[0-9A-Fa-f]{6}$|^#[0-9A-Fa-f]{3}$'

    # Проверяем, соответствует ли строка шаблону
    return re.match(hex_color_pattern, code) is not None


results = {case: is_hex_color(case) for case in test_cases}

print(results)

