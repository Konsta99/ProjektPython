#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import List,Optional,NamedTuple
from enum import Enum
from abc import ABC

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
    day: Day

class ID(NamedTuple):
    ID: int





class Course:
    def __init__(self, id: ID, name:str) :
        self.id = id
        self.name = name


class Teacher:
    def __init__(self, id: ID, name:PersonName) :
        self.id = id
        self.name = name
    pass


class Student:
    def __init__(self, id: ID, name: PersonName):
        self.id = id
        self.name = name
    pass

class CourseRepository:
    def __init__(self, courses : List[Course]) :
        self.courses = courses[Course]
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
    def __init__(self, id:str, course_id:str,term:str,teacher_id:str,students:List[id]):
        self.teacher_id=teacher_id
        self.id = id
        self.course_id=course_id
        self.term=term
        self.students = students
    pass


class CourseGrade(ABC):
    def __init__(self,course_id:Optional[str], grade:float,student_id:Optional[str],teacher_id:Optional[str]) -> None:
        self.teacher_id=teacher_id
        self.grade = grade
        self.course_id=course_id
        self.student_id=student_id
    pass

class LessonManager(ABC):
    def __init__(self, lessons:List[Lesson],teacher_handle:TeacherRepository,students_handle:StudentRepository,courses_handle:CourseRepository):
        self.__lessons=lessons
        self.__teacher_handle=teacher_handle
        self.__students_handle=students_handle
        self.__courses_handle=courses_handle

    #def add_lesson(course_id: ID, term: Date, teacher_id: ID, student_id: List[ID]):

    #def get_student_timetable(student_id: ID -> List[Lesson]:

    #def view_teacher_timetable(teacher_id: ID:int)-> -> None:

    #def view_student_timetable(student_id: ID) -> None

    #def get_teacher_timetable(teacher_id: ID: int) -> List[Lesson]


class GradeManager:
    def __init__(self, course_grades:List[CourseGrade],teacher_handle:TeacherRepository,students_handle:StudentRepository,courses_handle:CourseRepository):
        self.__course_grades=course_grades
        self.__teacher_handle=teacher_handle
        self.__students_handle=students_handle
        self.__courses_handle=courses_handle

    #add_course_grade(course_id: ID, grade: float, student_id: ID, teacher_id: ID):

    #def view_student_grades(student_id: ID) -> None

    #def view_teacher_grades(teacher_id: ID)-> None

    #def get_student_grades(student_id: ID) -> List[CourseGrade]

    #def get_teacher_grades(teacher_id: ID) -> List[CourseGrade]





