import unittest
from HW09_Ashish_Negi import Repository


class TestModuleUniversityGenerator(unittest.TestCase):
    def test_student_prettytable(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/week9/test")
        self.assertEqual(stevens.student_prettytable(),
                         [['10103', 'Baldwin, C', ['SSW 567']]])

    def test_instructor_prettytable(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/week9/test")
        self.assertEqual(stevens.instructor_prettytable(),
                         [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 1]])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
