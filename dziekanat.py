#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import List,Optional,NamedTuple
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
    def __init__(self, id: ID, name:PersonName) :
        self.id = id
        self.name = name


    @classmethod
    def generate_id_teacher(cls, name: str) -> str:
        return ''.join([c for c in name if c != ' ']) + '_' + str(len(name))

    pass

class Student:
    def __init__(self, id: ID, name: PersonName):
        self.id = id
        self.name = name

    @classmethod
    def generate_id_student(cls, name: str) -> str:

        return ''.join([c for c in name if c != ' ']) + '_' + str(len(name))

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
    def __init__(self, id:str, course_id:str,term:str,teacher_id:str,students:List[id]):
        self.teacher_id=teacher_id

        self.id = id
        self.course_id=course_id
        self.term=term
        self.students = students
    pass


class CourseGrade:
    def __init__(self,course_id:Optional[str], grade:float,student_id:Optional[str],teacher_id:Optional[str]) -> None:
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


    def add_lesson(self,course_id: ID, term: Date, teacher_id: ID, student_id: List[ID])->None:

        self.__lessons.append(Lesson(id=self.__lessons[-1].id+1 if self.__lessons else 1,course_id=course_id,term=term,teacher_id=teacher_id,students=student_id))

        pass

    def get_student_timetable(self, student_id: ID)-> List[CourseGrade]:

        return

    #def view_teacher_timetable(teacher_id: ID)-> None

    #def view_student_timetable(student_id: ID)-> None

    #def get_teacher_timetable(teacher_id: ID): List[Lesson]

class GradeManager:
    def __init__(self, course_grades:List[CourseGrade],teacher_handle:TeacherRepository,students_handle:StudentRepository,courses_handle:CourseRepository):
        self.__course_grades=course_grades
        self.__teacher_handle=teacher_handle
        self.__students_handle=students_handle
        self.__courses_handle=courses_handle

    #def add_course_grade(course_id: ID, grade: float, student_id: ID, teacher_id: ID):

    #def view_student_grades(student_id: ID) -> None

    #def view_teacher_grades(teacher_id: ID)-> None

    #def get_student_grades(student_id: ID) -> List[CourseGrade]

    #def get_teacher_grades(teacher_id: ID) -> List[CourseGrade]









