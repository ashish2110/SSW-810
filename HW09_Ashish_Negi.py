from collections import defaultdict
import os
from prettytable import PrettyTable
import sqlite3

class Repository():

    def __init__(self, directory_name):
        self.d_name = directory_name
        self.student_repository = {}
        self.instructor_repository = {}
        self.grade = []

        try:
            files = os.listdir(self.d_name)
        except FileNotFoundError:
            print(f"No such directory name '{self.d_name}' ")
        else:
            self.grade = self.grade_read(self.d_name + "/grades.txt")
            for cwid, name, \
                dept in self.file_reading_gen(self.d_name + "/students.txt",
                                              3, sep="\t", header=True):
                self.student_repository[cwid] = Student(cwid, name, dept,
                                                        self.grade)
            for cwid, name, \
                dept in self.file_reading_gen(self.d_name + "/instructors.txt",
                                              3, sep="\t", header=True):
                self.instructor_repository[cwid] = Instructors(cwid, name,
                                                               dept,
                                                               self.grade)

            self.major_1 = Major()
            for major, flag, \
                course in self.file_reading_gen(self.d_name + "/majors.txt", 
                                                3, sep="\t", header=True):
                self.major_1.add_courses(major, flag, course)
            self.major_1.student_remain_courses(self.student_repository)
            self.major_prettytable()
            self.student_prettytable()
            self.instructor_prettytable()
            self.instructor_table_db(self.d_name + "/810_startup.db")
            self.check_cwid_grades()

    def major_prettytable(self):
        pt = PrettyTable(field_names=['DEPT', 'REQUIRED', 'ELECTIVES'])

        li = []
        for key, details in self.major_1.major_req_courses.items():
            li.append([key, sorted(details),
                       sorted(self.major_1.major_ele_courses[key])])
            pt.add_row([key, sorted(details),
                       sorted(self.major_1.major_ele_courses[key])])
        print(pt)
        #print(li)
        return(li)

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
        # print(li)
        return(li)

    def instructor_table_db(self, db_path):

        db = sqlite3.connect(db_path)
        li = []
        pt = PrettyTable(field_names=['CWID', 'NAME', 'DEPT', 'COURSE',
                                      'STUDENTS'])

        query = """SELECT InstructorCWID, Name, Dept, Course, count(*)
                FROM instructors, grades
                WHERE InstructorCWID=CWID
                GROUP BY InstructorCWID, Course"""
        for row in db.execute(query):
            li.append(list(row))
            pt.add_row(list(row))

        print(pt)
        # print(li)
        return(li)

    def student_prettytable(self):
        pt = PrettyTable(field_names=['CWID', 'NAME', 'MAJOR', \
                                      'COMPLETED COURSES', \
                                      'REMAINING REQUIRED', \
                                      'REMAINING ELECTIVES'])
        li = []
        for cwid, details in self.student_repository.items():
            # print(details.course_grade)
            li.append([cwid, details.name, details.dept,
                       sorted([x for x in details.course_grade.keys()]),
                       details.req_courses, details.ele_courses])
            pt.add_row([cwid, details.name, details.dept,
                        sorted([x for x in details.course_grade.keys()]),
                        details.req_courses, details.ele_courses])
        print(pt)
        # print(li)
        return(li)

    def grade_read(self, grade_path):
        grade_list = []
        for s_id, course, grade, \
            p_id in self.file_reading_gen(grade_path,
                                          4, sep='\t', header=True):
            grade_list.append([s_id, course, grade, p_id])
        return grade_list

    def check_cwid_grades(self):
        grade_list = []
        for grade in self.grade:
            if grade[0] not in self.student_repository:
                print(f"Warning: '{grade[0]}' not present in students text file")
            if grade[3] not in self.instructor_repository:
                print(f"Warning: '{grade[3]}' not present in instructors text file")

    def file_reading_gen(self, path, fields, sep, header):
        """generator function file_reading_gen to read field-separated text
        files and yield a tuple with all of the values from a single line
        in the file on each call to next()"""
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            print(f"Couldn't open input file '{path}' \
                for reading")
        else:
            with fp:
                count = 1
                for line in fp:
                    line = line.rstrip('\n')
                    if len(line.split(sep)) < fields or \
                       len(line.split(sep)) > fields:
                        print(f"ValueError: Input file {path} \
                            has {len(line.split(sep))} fields \
                            on line {count} \
                            but expected {fields}")
                        exit()
                    elif (not header):
                        # print(line.split(sep=sep))
                        yield line.split(sep=sep)
                    header = False
                    count += 1


class Major():

    def __init__(self):
        self.major_req_courses = defaultdict(lambda: [])
        self.major_ele_courses = defaultdict(lambda: [])

    def add_courses(self, major, flag, course):
        if flag == 'R':
            self.major_req_courses[major].append(course)
        elif flag == 'E':
            self.major_ele_courses[major].append(course)

    def student_remain_courses(self, student_dict):
        for cwid, details in student_dict.items():
            completed_courses = set([x for x, y in details.course_grade.items()
                                    if y[-1] in
                                    ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']])
            details.req_courses = set(self.major_req_courses[details.dept]) - \
                completed_courses
            details.ele_courses = set(self.major_ele_courses[details.dept]) - \
                completed_courses
            if len(details.ele_courses) < \
               len(self.major_ele_courses[details.dept]):
                details.ele_courses = None
            if len(details.req_courses) <= 0:
                details.req_courses = None


class Student():

    def __init__(self, cwid, name, dept, grades):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.course_grade = defaultdict(lambda: [])
        self.req_courses = {}
        self.ele_courses = {}
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
    stevens = Repository("F:/desktop/lectures/SSW-810/assignments/SSW-810")
