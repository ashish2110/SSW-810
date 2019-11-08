from collections import defaultdict
import os
from prettytable import PrettyTable


class Repository():

    def __init__(self, directory_name):
        self.d_name = directory_name
        self.student_repository = {}
        self.instructor_repository = {}
        self.grade = []

        try:
            files = os.listdir(self.d_name)
        except FileNotFoundError:
            raise FileNotFoundError(f"No such directory name '{self.d_name}' ")
        else:
            self.grade = self.grade_read(self.d_name + "/grades.txt")
            for cwid, name, \
                dept in self.file_reading_gen(self.d_name + "/students.txt",
                                              3, sep="\t", header=False):
                self.student_repository[cwid] = Student(cwid, name, dept,
                                                        self.grade)
            for cwid, name, \
                dept in self.file_reading_gen(self.d_name + "/instructors.txt",
                                              3, sep="\t", header=False):
                self.instructor_repository[cwid] = Instructors(cwid, name,
                                                               dept,
                                                               self.grade)

            students = self.file_reading_gen(self.d_name + "/students.txt", 3,
                                             sep="\t", header=False)
            instructors = self.file_reading_gen(self.d_name + "/instructors.txt", 3,
                                                sep="\t", header=False)
            grades = self.file_reading_gen(self.d_name + "/grades.txt", 4,
                                           sep="\t", header=False)

            # self.student_prettytable()
            # self.instructor_prettytable()

    def instructor_prettytable(self):
        pt = PrettyTable(field_names=['CWID', 'NAME', 'DEPT', 'COURSE',
                                      'STUDENTS'])
        li = []
        for cwid, details in self.instructor_repository.items():
            # print(details.student_count)
            for course, count in details.student_count.items():
                li.append([cwid, details.name, details.dept, course, count])
                pt.add_row([cwid, details.name, details.dept, course, count])
        print(pt)
        return(li)

    def student_prettytable(self):
        pt = PrettyTable(field_names=['CWID', 'NAME', 'COMPLETED COURSES'])
        li = []
        for cwid, details in self.student_repository.items():
            # print(details.course_grade)
            li.append([cwid, details.name,
                       [x for x in details.course_grade.keys()]])
            pt.add_row([cwid, details.name,
                        [x for x in details.course_grade.keys()]])
        print(pt)
        return(li)

    def grade_read(self, grade_path):
        grade_list = []
        for s_id, course, grade, \
            p_id in self.file_reading_gen(grade_path,
                                          4, sep='\t', header=False):
            grade_list.append([s_id, course, grade, p_id])
        return grade_list

    def file_reading_gen(self, path, fields, sep, header):
        """generator function file_reading_gen to read field-separated text
        files and yield a tuple with all of the values from a single line
        in the file on each call to next()"""
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError(f"Couldn't open input file '{path}' \
                for reading")
        else:
            with fp:
                count = 1
                for line in fp:
                    line = line.rstrip('\n')
                    if len(line.split(sep)) < fields or \
                       len(line.split(sep)) > fields:
                        raise ValueError(f"ValueError: Input file\n\
                            has {len(line.split(sep))} fields \
                            on line {count}\n \
                            but expected {fields}")
                    elif (not header):
                        # print(line.split(sep=sep))
                        yield line.split(sep=sep)
                    header = False
                    count += 1


class Student():

    def __init__(self, cwid, name, dept, grades):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.course_grade = defaultdict(lambda: [])
        self.add_course_grade(cwid, grades)

    def add_course_grade(self, cwid, grades):
        for s_id, course, grade, p_id in grades:
            if s_id == cwid:
                self.course_grade[course].append(grade)


class Instructors():
    def __init__(self, cwid, name, dept, grades):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.student_count = defaultdict(lambda: 0)
        self.add_student_count(cwid, grades)

    def add_student_count(self, cwid, grades):
        for s_id, course, grade, p_id in grades:
            if p_id == cwid:
                self.student_count[course] += 1


def main():
    stevens = Repository("F:/desktop/lectures/SSW-810/assignments/week9")
