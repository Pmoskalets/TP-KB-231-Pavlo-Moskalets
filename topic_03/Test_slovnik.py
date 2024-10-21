def test_dict_functions():
    # Створюємо початковий словник для тестування
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Початковий словник:", my_dict)

    # 1. Метод update() - оновлює словник новими парами ключ-значення
    my_dict.update({'d': 4, 'e': 5})
    print("Після update({'d': 4, 'e': 5}):", my_dict)

    # 2. Оператор del - видаляє пару ключ-значення за ключем
    del my_dict['b']  # Видаляє елемент з ключем 'b'
    print("Після del my_dict['b']:", my_dict)

    # 3. Метод clear() - очищає словник, видаляючи всі елементи
    my_copy_dict = my_dict.copy()  # Створюємо копію для демонстрації, щоб оригінал зберегти
    my_copy_dict.clear()
    print("Після clear() копія словника:", my_copy_dict)

    # 4. Метод keys() - повертає всі ключі словника
    keys = my_dict.keys()
    print("Ключі словника після keys():", keys)

    # 5. Метод values() - повертає всі значення словника
    values = my_dict.values()
    print("Значення словника після values():", values)

    # 6. Метод items() - повертає всі пари ключ-значення як кортежі
    items = my_dict.items()
    print("Пари ключ-значення після items():", items)

if __name__ == "__main__":
    test_dict_functions()
