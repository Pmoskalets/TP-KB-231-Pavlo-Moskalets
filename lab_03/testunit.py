import unittest
from Student import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("Pavlo", "0631234567", "pavlo@example.com", "123 Main St")
        self.assertEqual(student.name, "Pavlo")
        self.assertEqual(student.phone, "0631234567")
        self.assertEqual(student.email, "pavlo@example.com")
        self.assertEqual(student.address, "123 Main St")

    def test_update_student(self):
        student = Student("Pavlo", "0631234567", "pavlo@example.com", "123 Main St")
        student.update(phone="0639876543", email="pavlo_new@example.com")
        self.assertEqual(student.phone, "0639876543")
        self.assertEqual(student.email, "pavlo_new@example.com")

if __name__ == "__main__":
    unittest.main()