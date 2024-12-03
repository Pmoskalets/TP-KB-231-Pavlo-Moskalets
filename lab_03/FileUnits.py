import unittest
import tempfile
import os
import csv
from io import StringIO
import sys

from lab_02 import addNewElement, deleteElement, modifyStudent, load_data, save_data, display_students, students # type: ignore


class StudentDirectoryTests(unittest.TestCase):

    def setUp(self):
        # Створюємо тимчасовий файл для тестів
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8')
        self.temp_filename = self.temp_file.name
        self.temp_file.close()

    def tearDown(self):
        # Видаляємо тимчасовий файл після тестів
        if os.path.exists(self.temp_filename):
            os.remove(self.temp_filename)

    def test_add_student(self):
        initial_count = len(students)
        addNewElement()  # Додати нового студента (перевірити через мок)
        self.assertGreater(len(students), initial_count)
        self.assertEqual(students[-1]["name"], "New Student")  # Очікується конкретна назва

    def test_remove_student(self):
        students.append({"name": "Sample Student", "phone": "123456", "email": "test@domain.com", "address": "123 Street"})
        initial_count = len(students)
        deleteElement()  # Видалити елемент (через мок ввод)
        self.assertLess(len(students), initial_count)
        self.assertNotIn({"name": "Sample Student"}, students)

    def test_modify_student(self):
        students.append({"name": "John Doe", "phone": "000111222", "email": "john@example.com", "address": "456 Avenue"})
        modifyStudent()  # Оновити дані студента (через мок)
        self.assertEqual(students[0]["email"], "updated@example.com")  # Очікується конкретний email

    def test_load_data(self):
        mock_data = [
            {"name": "Alice", "phone": "555111222", "email": "alice@mail.com", "address": "789 Road"},
            {"name": "Bob", "phone": "555333444", "email": "bob@mail.com", "address": "123 Boulevard"}
        ]

        with open(self.temp_filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "address"])
            writer.writeheader()
            writer.writerows(mock_data)

        load_data(self.temp_filename)
        self.assertEqual(len(students), len(mock_data))
        self.assertEqual(students[0]["name"], "Alice")

    def test_save_data(self):
        students.append({"name": "Charlie", "phone": "999888777", "email": "charlie@domain.com", "address": "999 Park"})
        save_data(self.temp_filename)

        with open(self.temp_filename, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["name"], "Charlie")

    def test_display_students(self):
        students.append({"name": "Test User", "phone": "123456789", "email": "testuser@example.com", "address": "No Address"})
        captured_output = StringIO()
        sys.stdout = captured_output

        display_students()
        sys.stdout = sys.__stdout__  # Повертаємо stdout назад

        self.assertIn("Test User", captured_output.getvalue())
        self.assertIn("123456789", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
