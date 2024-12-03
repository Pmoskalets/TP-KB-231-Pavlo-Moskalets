from Student import Student

class StudentRegistry:
    def __init__(self):
        self._records = []

    def add(self, student):
        """Додає нового студента та сортує список за іменем."""
        self._records.append(student)
        self._records.sort(key=lambda s: s.name)

    def remove(self, student_name):
        """Видаляє студента за ім’ям."""
        for record in self._records:
            if record.name == student_name:
                self._records.remove(record)
                print(f"Student '{student_name}' has been removed.")
                return
        print(f"Student '{student_name}' not found.")

    def modify(self, student_name, name=None, phone=None, email=None, address=None):
        """Оновлює дані студента за його ім’ям."""
        for record in self._records:
            if record.name == student_name:
                record.modify(name=name, phone=phone, email=email, address=address)
                print(f"Student '{student_name}' has been updated.")
                return
        print(f"Student '{student_name}' not found.")

    def show_all(self):
        """Виводить усіх студентів."""
        if not self._records:
            print("The registry is empty.")
        else:
            for record in self._records:
                print(record.details())

    def find(self, student_name):
        """Пошук студента за ім’ям."""
        return next((record for record in self._records if record.name == student_name), None)
