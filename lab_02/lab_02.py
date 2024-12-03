import csv
import sys

# Ім'я файлу для збереження за замовчуванням
DEFAULT_FILE = "students_directory.csv"

# Список студентів
students = []

# Вивід списку студентів
def display_students():
    if not students:
        print("The student directory is currently empty.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Address: {student['address']}")
    print()

# Додавання студента
def add_student():
    name = input("Enter student's name: ").strip()
    phone = input("Enter student's phone number: ").strip()
    email = input("Enter student's email: ").strip()
    address = input("Enter student's address: ").strip()

    student_data = {"name": name, "phone": phone, "email": email, "address": address}

    # Зберігаємо список у впорядкованому вигляді за ім'ям
    position = next((i for i, student in enumerate(students) if name < student["name"]), len(students))
    students.insert(position, student_data)

    print(f"Student '{name}' has been added.\n")

# Видалення студента
def remove_student():
    name_to_remove = input("Enter the name of the student to remove: ").strip()
    for i, student in enumerate(students):
        if student["name"] == name_to_remove:
            del students[i]
            print(f"Student '{name_to_remove}' has been removed.\n")
            return
    print(f"Student '{name_to_remove}' not found.\n")

# Оновлення даних студента
def modify_student():
    name_to_modify = input("Enter the name of the student to update: ").strip()
    for i, student in enumerate(students):
        if student["name"] == name_to_modify:
            new_name = input(f"New name (current: {student['name']}): ").strip() or student["name"]
            new_phone = input(f"New phone (current: {student['phone']}): ").strip() or student["phone"]
            new_email = input(f"New email (current: {student['email']}): ").strip() or student["email"]
            new_address = input(f"New address (current: {student['address']}): ").strip() or student["address"]

            students.pop(i)
            updated_student = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}
            position = next((j for j, s in enumerate(students) if new_name < s["name"]), len(students))
            students.insert(position, updated_student)

            print(f"Student '{name_to_modify}' has been updated.\n")
            return
    print(f"Student '{name_to_modify}' not found.\n")

# Завантаження даних із CSV
def load_data(file_name):
    global students
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            students = [row for row in csv_reader]
        print(f"Data loaded from '{file_name}'.\n")
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty directory.\n")
        students = []

# Збереження даних у CSV
def save_data(file_name):
    try:
        with open(file_name, mode='w', encoding='utf-8', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])
            csv_writer.writeheader()
            csv_writer.writerows(students)
        print(f"Data saved to '{file_name}'.\n")
    except Exception as e:
        print(f"Error saving data: {e}\n")

# Основне меню
def main_menu():
    file_name = DEFAULT_FILE
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    load_data(file_name)

    while True:
        action = input("Choose an action: [A add, U update, R remove, D display, Q quit]: ").strip().lower()
        if action == "a":
            add_student()
        elif action == "u":
            modify_student()
        elif action == "r":
            remove_student()
        elif action == "d":
            display_students()
        elif action == "q":
            save_data(file_name)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Запуск програми
if __name__ == "__main__":
    main_menu()
