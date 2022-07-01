import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        # create instance of student
        student = Student("John", "Doe")
        # use asset equal to see if calling full name method returns expected value
        # in this case, the first and last name sep by a space
        self.assertEqual(student.full_name, 'John Doe')

    def test_alert_santa(self):
        student = Student("John", "Doe")
        student.alert_santa()

        self.assertTrue(student.naughty_list)  # only one arg is passed as it's checking for true/false rather than comparing


# run test without having to specify unittest module
if __name__ == "__main__":
    unittest.main()