import re
# Введём строку на русском
original_line = input()

# Изменим значения нач. на А на аа
line_aa = re.sub(pattern=r"(А)", repl="аа",
                 string=original_line, count=0, flags=re.MULTILINE)
print(f"Изменённая строка: {line_aa}")

# Подсчитаем количество "р"
counting_r = len(re.findall(pattern=r"\bр\w+",
                            string=original_line, flags=re.MULTILINE))
print(f"Количество слов начинающихся на букву 'р': {counting_r}")