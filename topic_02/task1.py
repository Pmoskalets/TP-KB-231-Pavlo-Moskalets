import math

# Функція для розрахунку дискримінанта
def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

# Функція для пошуку коренів квадратного рівняння
def find_roots(a, b, c):
    discriminant = calculate_discriminant(a, b, c)

    if discriminant > 0:
        # Два різних корені
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Два корені: x1 = {root1}, x2 = {root2}"
    elif discriminant == 0:
        # Один корінь
        root = -b / (2 * a)
        return f"Один корінь: x = {root}"
    else:
        # Коренів немає (уявні корені)
        return "Коренів немає (уявні корені)"

# Приклад використання
a = 1
b = -3
c = 2
result = find_roots(a, b, c)
print(result)
