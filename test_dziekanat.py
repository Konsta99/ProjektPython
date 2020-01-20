#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import dziekanat as dz
from dziekanat import Course, Teacher, Student, PersonName

class TestCreating(unittest.TestCase):


    def test_lesson(self):

        students = []
        for id in range(1, 11):
            person_name = "Ben" + str(id)
            person_surname = "Student" + str(id)
            t = dz.Student(dz.PersonName(person_name, person_surname))
            students.append(t)
        course=dz.Course("Matematyka")
        person_name = "John" + str(1)
        person_surname = "Snow" + str(1)
        t = dz.Teacher(dz.PersonName(person_name, person_surname))

        t2=dz.Teacher(dz.PersonName("Jan","pawel"))
        zajecia=dz.Lesson(dz.ID(1),course_id=course.id,term=dz.Date("13:00",day=dz.Day["MON"]),teacher_id=t.id,students=[i.id for i in students])


        self.assertEqual(1 ,zajecia.teacher_id)
        self.assertEqual(1,zajecia.course_id)
        self.assertEqual('MON',zajecia.term.day.name)
        tch=dz.TeacherRepository([t,t2])
        students_repo=dz.StudentRepository(students)
        courses=dz.CourseRepository([course])
        lessons=dz.LessonManager([zajecia], teacher_handle=tch,students_handle=students_repo,courses_handle=courses)
        self.assertEqual(2,t2.id)
        lessons.add_lesson(course_id=course.id, term=dz.Date("12:00", day=dz.Day["TUE"]), teacher_id=tch.teachers[0].id, student_id=[i.id for i in students_repo.students[0:5]])

        self.assertEqual(2,len(lessons.get_teacher_timetable(dz.ID(1))))
        self.assertEqual(2,len(lessons.get_student_timetable(dz.ID(1))))
        self.assertEqual(1,len(lessons.get_student_timetable(dz.ID(6))))
        grade_manager=dz.GradeManager([],tch,students_repo,courses)
        grade_manager.add_course_grade(courses.courses[0].id,4,students_repo.students[0].id,t.id)
        self.assertEqual(4,grade_manager.course_grades[0].grade)
        self.assertEqual(1, grade_manager.course_grades[0].student_id)
        lessons.view_teacher_timetable(dz.ID(1))
        print ("student")
        lessons.view_student_timetable(dz.ID(2))
        grade = grade_manager.get_student_grades(dz.ID(1))[0].grade
        grade2=grade_manager.get_teacher_grades(dz.ID(1))[0].grade
        self.assertEqual(4,grade)
        self.assertEqual(4,grade2)

class TestCourse(unittest.TestCase):
    def test_init(self):
        course = dz.Course(name="Matematyka")
        self.assertEqual("Matematyka", course.name)
        self.assertEqual(1,course.id)




class TestTeacher(unittest.TestCase):
    def test_init(self):

        teacher = dz.Teacher(dz.PersonName(name ="Jan",surname=" Kowalski"))
        self.assertEqual("Jan", teacher.name.name)
        self.assertEqual(1, dz.Teacher.generate_id())
        self.assertEqual(2, dz.Teacher.generate_id())

class TestStudent(unittest.TestCase):
    def test_init(self):
        student = dz.Student(dz.PersonName(name="Konrad" ,surname="Stalmach"))
        self.assertEqual("Konrad", student.name.name)
        self.assertEqual(1,student.id)


        teacher = PersonName(name ="Jan",surname = 'Kowalski')
        self.assertEqual("JanKowalski", teacher.name + teacher.surname)



    def test_generate_id(self):
        self.assertEqual(1, Teacher.generate_id())
        Teacher.generate_id()
        self.assertEqual(3, Teacher.generate_id())

class TestStudents(unittest.TestCase):
    def test_init(self):

        student = PersonName(name="Konrad", surname='Stalmach')
        self.assertEqual("KonradStalmach", student.name + student.surname)

class TestLessonManager(unittest.TestCase):
    def test_init(self):

        zajecia = dz.Lesson(dz.ID(1), course_id=dz.ID(1), term=dz.Date("13:00",day=dz.Day["MON"]), teacher_id=dz.ID(1),students=[dz.ID(1)])
        self.assertEqual(1, zajecia.course_id.ID)





# class TestStudentRepository(unittest.TestCase):



if __name__ == '__main__':
    unittest.main()
