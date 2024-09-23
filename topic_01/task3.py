def find_discriminant(a, b, c):
    # Формула дискримінанту
    D = b**2 - 4*a*c
    return D

# Тестування функції
a = 1
b = -3
c = 2

discriminant = find_discriminant(a, b, c)
print(f"Дискримінант рівняння {a}x^2 + {b}x + {c} = 0: D = {discriminant}")
