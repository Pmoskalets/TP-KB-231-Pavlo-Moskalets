# Введення рядка для тестування
test_string = "   привіт, СВІТ!   "

# Тестування функцій:
print("Оригінальний рядок:", repr(test_string))

# 1. strip() - Видаляє пробіли на початку і в кінці
stripped_string = test_string.strip()
print("strip():", repr(stripped_string))

# 2. capitalize() - Перший символ великий, решта маленькі
capitalized_string = stripped_string.capitalize()
print("capitalize():", repr(capitalized_string))

# 3. title() - Кожне слово починається з великої літери
titled_string = stripped_string.title()
print("title():", repr(titled_string))

# 4. upper() - Всі літери великі
upper_string = stripped_string.upper()
print("upper():", repr(upper_string))

# 5. lower() - Всі літери маленькі
lower_string = stripped_string.lower()
print("lower():", repr(lower_string))
