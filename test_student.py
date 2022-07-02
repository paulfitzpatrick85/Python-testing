import unittest
from student import Student
from datetime import timedelta


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # addind cls to classmethod decorator acts on class method instead of instance of the class
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):  
        print('setUp')
        self.student = Student('John', 'Doe')
        # self must be added to every referance to self.student now self.student is an instance variable

    def tearDown(self):  # let us see when teardown is run
        print('tearDown')

    def test_full_name(self):
        print('test_full_name')  # show when test is run
        # create instance of student
        # student = Student("John", "Doe")  --- removed due to 'setUp' for refactoring/d.r.y
        # use asset equal to see if calling full name method returns expected value
        # in this case, the first and last name sep by a space
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_alert_santa(self):
        print('test_alert_santa')
        # student = Student("John", "Doe")
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)  # only one arg is passed as it's checking for true/false rather than comparing


    def test_email(self):
        print('test_email')
        # student = Student("John", "Doe")

        self.assertEqual(self.student.email, "john.doe@email.com")


    def test_apply_extension(self):
        old_end_date = self.student.end_date  # redeclare current instance of end date
        self.student.apply_extension(5)  # number of days required
        # print('test_apply_extension')
        # check if end_date is same as old_end_Date plus time delta of 5 days
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5)) 


# run test without having to specify unittest module
if __name__ == "__main__":
    unittest.main()