'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
import unittest


class TestStudentLists(unittest.TestCase):
    # DRY
    def setUp(self):  # Arrange part of AAA structure
        self.test_class = ClassList(2)

    def test_cant_create_class_with_negative_students(self):
        with self.assertRaises(StudentError):
            self.test_class = ClassList(-2)
            self.test_class = ClassList(0)

    def test_add_student_check_student_in_list(self):
        # action  part of AAA structure
        self.test_class.add_student('Test Student')
        # assert  part of AAA structure
        self.assertIn('Test Student', self.test_class.class_list)

        self.test_class.add_student('Another Test Student')
        self.assertIn('Test Student', self.test_class.class_list)
        self.assertIn('Another Test Student', self.test_class.class_list)

    def test_add_student_already_in_list(self):
        self.test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            self.test_class.add_student('Test Student')

    # D TODO write a test that adds and removes a student,
    # and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        # test_class = ClassList(2)
        self.test_class.add_student('Test Student')
        self.test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', self.test_class.class_list)

    # D TODO write a test that adds some example students,
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_add_remove_students_not_in_list(self):
        self.test_class.add_student('Dwight')  # in class list
        with self.assertRaises(StudentError):
            self.test_class.remove_student('Andy')

    # D TODO write a test that removes a student from an
    # empty list, and asserts a StudentError is raised
    def test_removes_student_fom_an_empty_list(self):
        self.test_class.class_list = []
        with self.assertRaises(StudentError):
            self.test_class.remove_student('John')

    def test_is_enrolled_when_student_present(self):
        self.test_class.add_student('Snoop Dogg')
        self.test_class.add_student('Martha Stewart')
        self.assertTrue(self.test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(self.test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        self.assertFalse(self.test_class.is_enrolled('Snoop Dogg'))

    # Done TODO write a test that adds some example students to a test class,
    # then, call is_enrolled for a student who is not enrolled.
    # Use assertFalse to verify is_enrolled returns False.
    def test_is_enrolled_not_enrolled(self):
        self.test_class.add_student('Pam')
        self.test_class.add_student('stanley')
        self.assertFalse(self.test_class.is_enrolled('ryan'))

    def test_string_with_students_enrolled(self):
        self.test_class.add_student('Taylor Swift')
        self.test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(self.test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    # TODO write a test for index_of_student when the class_list list is empty.
    # Assert index_of_student returns None for a student if the list is empty.
    # use assertIsNone.
    def test_index_of_student_student_is_none_if_classlist_is_empty(self):
        # Arrange in setUp
        index = self.test_class.index_of_student('Test Student')  # action
        self.assertIsNone(index)

    # TODO write another test for index_of_student. In the case when the
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_student_is_none_classlist_not_empty(self):
        self.test_class.add_student('Michael')
        self.test_class.add_student('Angela')
        index = self.test_class.index_of_student('James')
        self.assertIsNone(index)

    # TODO write a test for your new is_class_full method when the class is full.
    # use assertTrue.
    def test_is_class_full(self):
        self.test_class.add_student('Kelly')
        self.test_class.add_student('Kevin')
        full = self.test_class.is_class_full()
        self.assertTrue(full)

    # TODO write a test for your new is_class_full method for when is empty,
    # and when it is not full. Use assertFalse.
    def test_is_class_full_empty(self):
        full = self.test_class.is_class_full()
        self.assertFalse(full)

    if __name__ == '__main__':
        unittest.main()
