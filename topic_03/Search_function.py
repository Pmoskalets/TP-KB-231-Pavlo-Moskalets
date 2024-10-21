def test_list_functions():
    # Створюємо початковий список для тестування
    my_list = [3, 1, 4, 1, 5]
    print("Початковий список:", my_list)

    # 1. Метод extend() - додає елементи іншого списку в кінець
    my_list.extend([9, 2, 6])
    print("Після extend([9, 2, 6]):", my_list)

    # 2. Метод append() - додає елемент в кінець списку
    my_list.append(8)
    print("Після append(8):", my_list)

    # 3. Метод insert() - вставляє елемент на задану позицію
    my_list.insert(2, 7)  # Вставляє число 7 на індекс 2
    print("Після insert(2, 7):", my_list)

    # 4. Метод remove() - видаляє перше входження значення
    my_list.remove(1)  # Видаляє перше входження числа 1
    print("Після remove(1):", my_list)

    # 5. Метод sort() - сортує список за зростанням
    my_list.sort()
    print("Після sort():", my_list)

    # 6. Метод reverse() - змінює порядок елементів на зворотний
    my_list.reverse()
    print("Після reverse():", my_list)

    # 7. Метод copy() - створює копію списку
    copied_list = my_list.copy()
    print("Копія списку після copy():", copied_list)

    # 8. Метод clear() - очищає список
    my_list.clear()
    print("Після clear() список:", my_list)

if __name__ == "__main__":
    test_list_functions()
