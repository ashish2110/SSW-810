import unittest
from HW09_Ashish_Negi import Repository


class TestModuleUniversityGenerator(unittest.TestCase):
    def test_student_prettytable(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/SSW-810")
        self.assertEqual(stevens.student_prettytable(),
                        [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], {'SSW 555', 'SSW 540'}, None], ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], {'SSW 555', 'SSW 540'}, {'CS 501', 'CS 546'}], ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 501', 'CS 546'}], ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], None, None], ['11717', 'Kernighan, B', 'CS', [], {'CS 570', 'CS 546'}, {'SSW 810', 'SSW 565'}]])

    def test_instructor_prettytable(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/SSW-810")
        self.assertEqual(stevens.instructor_prettytable(),
                         [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], ['98762', 'Hawking, S', 'CS', 'CS 501', 1], ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1]])

    def test_major_prettytable(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/SSW-810")
        self.assertEqual(stevens.major_prettytable(),
                         [['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']], ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]])

    def test_instructor_table_db(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/SSW-810")
        print(stevens.instructor_table_db("F:/desktop/lectures/SSW-810/assignments/SSW-810/810_startup.db"))
        self.assertEqual(stevens.instructor_table_db("F:/desktop/lectures/SSW-810/assignments/SSW-810/810_startup.db"),
                         [['98762', 'Hawking, S', 'CS', 'CS 501', 1], ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], ['98764', 'Cohen, R', 'SFEN', 'CS 546', 1]])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
