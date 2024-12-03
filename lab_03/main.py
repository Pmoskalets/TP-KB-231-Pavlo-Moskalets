# main.py
from StudentList import StudentList # type: ignore
from FileUtils import FileUtils # type: ignore
from Student import Student

def display_menu():
    print("\nAvailable actions:")
    print("[1] Add a new student")
    print("[2] Update an existing student")
    print("[3] Delete a student")
    print("[4] Display all students")
    print("[5] Exit")
    return input("Choose an option: ").strip()

def handle_create(student_list):
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()
    phone = input("Enter student phone: ").strip()
    email = input("Enter student email: ").strip()
    address = input("Enter student address: ").strip()
    new_student = Student(name, phone, email, address)
    student_list.add_student(new_student)
    print("Student successfully added.")

def handle_update(student_list):
    print("\n--- Update Student ---")
    current_name = input("Enter the name of the student to update: ").strip()
    print("Enter new details (press Enter to keep current value):")
    updated_name = input("New name: ").strip() or None
    updated_phone = input("New phone: ").strip() or None
    updated_email = input("New email: ").strip() or None
    updated_address = input("New address: ").strip() or None
    student_list.update_student(current_name, updated_name, updated_phone, updated_email, updated_address)
    print("Student details updated.")

def handle_delete(student_list):
    print("\n--- Delete Student ---")
    name = input("Enter the name of the student to delete: ").strip()
    student_list.delete_student(name)
    print(f"Student '{name}' removed, if they existed.")

def handle_print(student_list):
    print("\n--- Student Directory ---")
    student_list.print_all()

def main():
    student_list = StudentList()
    file_path = "students_directory.csv"

    # Load students from the file
    FileUtils.load_from_csv(file_path, student_list)
    print("Welcome to the Student Management System!")

    while True:
        action = display_menu()
        if action == "1":
            handle_create(student_list)
        elif action == "2":
            handle_update(student_list)
        elif action == "3":
            handle_delete(student_list)
        elif action == "4":
            handle_print(student_list)
        elif action == "5":
            FileUtils.save_to_csv(file_path, student_list)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
