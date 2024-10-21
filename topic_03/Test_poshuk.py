import bisect

def find_insert_position(sorted_list, element):
    # Використовуємо bisect_left для пошуку позиції вставки
    position = bisect.bisect_left(sorted_list, element)
    return position

# Приклад використання
sorted_list = [1, 3, 4, 7, 9]
element = 5
position = find_insert_position(sorted_list, element)
print(f"Позиція для вставки елемента {element}: {position}")
