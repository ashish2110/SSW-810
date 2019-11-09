import unittest
from HW09_Ashish_Negi import Repository


class TestModuleUniversityGenerator(unittest.TestCase):
    def test_student_prettytable(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/SSW-810")
        self.assertEqual(stevens.student_prettytable(),
                         [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, None], ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, None], ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], {'SSW 540', 'SSW 564'}, {'CS 545', 'CS 501', 'CS 513'}], ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, {'CS 545', 'CS 501', 'CS 513'}], ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], {'SSW 567', 'SSW 540', 'SSW 555', 'SSW 564'}, {'CS 545', 'CS 501', 'CS 513'}], ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], {'SYS 800', 'SYS 671', 'SYS 612'}, None], ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 671', 'SYS 612'}, {'SSW 810', 'SSW 540', 'SSW 565'}], ['11658', 'Kelly, P', 'SYEN', [], {'SYS 800', 'SYS 671', 'SYS 612'}, {'SSW 810', 'SSW 540', 'SSW 565'}], ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], {'SYS 800', 'SYS 671', 'SYS 612'}, {'SSW 810', 'SSW 540', 'SSW 565'}], ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], {'SYS 800', 'SYS 671', 'SYS 612'}, None]])

    def test_instructor_prettytable(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/SSW-810")
        self.assertEqual(stevens.instructor_prettytable(),
                         [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 2], ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]])

    def test_major_prettytable(self):
        stevens = Repository("F:/desktop/lectures/SSW-810/assignments/SSW-810")
        self.assertEqual(stevens.major_prettytable(),
                         [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']], ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
