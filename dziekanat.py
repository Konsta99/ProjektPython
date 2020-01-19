#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import List,NamedTuple
from enum import Enum


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5

class PersonName(NamedTuple):
    name: str
    surname: str

class Date(NamedTuple):
    hour:str
    day:Day

class ID(NamedTuple):
    ID: int




class Course:
    def __init__(self, name:str) :
        self.id=Course.generate_id()
        self.name = name

    highest_id:ID=0

    @classmethod
    def generate_id(cls) -> ID:
        Course.highest_id+=1
        return Course.highest_id

    pass




class Teacher:
    def __init__(self, name:PersonName) :
        self.id = Course.generate_id()
        self.name = name

    highest_id: ID = 0

    @classmethod
    def generate_id(cls) -> ID:
        Teacher.highest_id += 1
        return Teacher.highest_id
    pass

class Student:
    def __init__(self, name: PersonName):
        self.id = Student.generate_id()
        self.name = name

    highest_id: ID = 0

    @classmethod
    def generate_id(cls) -> ID:
        Student.highest_id += 1
        return Student.highest_id

    def __repr__(self):
        return Student.highest_id

    pass

class CourseRepository:
    def __init__(self, courses : List[Course]) :
        self.courses = courses
        pass




class TeacherRepository:
    def __init__(self, teachers:List[Teacher]) :
        self.teachers = teachers
        pass

class StudentRepository:
    def __init__(self, students : List[Student]) :
        self.students= students
    pass

class Lesson:
    def __init__(self, id:ID, course_id:ID,term:Date,teacher_id:ID,students:List[ID]):
        self.teacher_id=teacher_id
        self.id = id
        self.course_id=course_id
        self.term=term
        self.students = students



class CourseGrade:
    def __init__(self,course_id:ID, grade:float,student_id:ID,teacher_id:ID) -> None:
        self.teacher_id=teacher_id
        self.grade = grade
        self.course_id=course_id
        self.student_id=student_id
    pass



class LessonManager:
    def __init__(self, lessons:List[Lesson],teacher_handle:TeacherRepository,students_handle:StudentRepository,courses_handle:CourseRepository):

        self.__lessons=lessons
        self.__teacher_handle=teacher_handle
        self.__students_handle=students_handle
        self.__courses_handle=courses_handle

    # def __repr__(self):
    #     return "Zajecia ID "+ str(self.__lessons) + "    Teacher ID:" + str(self.__teacher_handle) +"     Studenci ID:" + str(self.__students_handle) +    "       ID przedmiotu:"+str(self.__courses_handle)
    # pass





    def add_lesson(self,course_id: ID, term: Date, teacher_id: ID, student_id: List[ID])->None:

        self.__lessons.append(Lesson(id=self.__lessons[-1].id+1 if self.__lessons else 1,course_id=course_id,term=term,teacher_id=teacher_id,students=student_id))

        pass



    def get_teacher_timetable(self, teacher_id: ID)-> List[Lesson]:

        teacher_timetable=[]

        for lesson in self.__lessons:
            if lesson.teacher_id == teacher_id:
                teacher_timetable.append(lesson)

        return teacher_timetable




    def view_teacher_timetable(self, teacher_id: ID)-> None:

        for teacher in self.__teacher_handle.teachers:
            if teacher.id == teacher_id:
                print(teacher.name)
        for lesson in self.__lessons:
            if lesson.teacher_id == teacher_id:
                for Course in self.__courses_handle.courses:
                    if lesson.course_id == Course.id:
                        print(Course.name)
                print(lesson.term)




    def get_student_timetable(self, student_id: ID)-> List[Lesson]:

        student_timetable = []

        for lesson in self.__lessons:
            for student in lesson.students:
                if student_id == student:
                    student_timetable.append(lesson)

        return student_timetable



    def view_student_timetable(self, student_id: ID)-> None:

        print (self.get_student_timetable(student_id=student_id))



class GradeManager:

    def __init__(self, course_grades:List[CourseGrade],teacher_handle:TeacherRepository,students_handle:StudentRepository,courses_handle:CourseRepository):

        self.__course_grades=course_grades
        self.__teacher_handle=teacher_handle
        self.__students_handle=students_handle
        self.__courses_handle=courses_handle


    def add_course_grade(self, course_id: ID, grade: float, student_id: ID, teacher_id: ID) -> None:

        self.__course_grades.append(CourseGrade(course_id = course_id, grade = grade, student_id = student_id, teacher_id = teacher_id))



    def get_teacher_grades(self, teacher_id: ID) -> List[CourseGrade]:

        teacher_grades = []

        for grade in self.__course_grades:

                if teacher_id == grade.teacher_id:

                    teacher_grades.append(grade)

        return teacher_grades


    def view_teacher_grades(self, teacher_id: ID)-> None:
        print (self.get_teacher_grades(teacher_id=teacher_id))


    def get_student_grades(self, student_id: ID) -> List[CourseGrade]:

        student_grades = []

        for grade in self.__course_grades:
            for student in grade.student_id:
                if student_id == student:
                    student_grades.append(grade)

        return student_grades



    def view_student_grades(self, student_id: ID) -> None:
        print(self.get_student_grades(student_id=student_id))



        # for student in self.__students_handle.students:
        #     if Student.id == student_id:
        #         print(student.name)
        #
        # for grade in self.__course_grades__:
        #     if Course.students == student_id:
        #         for Course in self.__courses_handle__.courses:
        #             if lesson.course_id == Course.id:
        #                 print(Course.name)
        #         print(grade.grade)













