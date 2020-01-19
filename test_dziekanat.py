#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import dziekanat as dz
class TestCreating(unittest.TestCase):


    def Test_lesson(self):
        students = []
        for id in range(1, 10):
            person_name = "Ben" + str(id)
            person_surname = "Student" + str(id)
            t = dz.Student(dz.PersonName(person_name, person_surname))
            students.append(t)
        course=dz.Course("Matematyka")

        person_name = "John" + str(1)
        person_surname = "Snow" + str(1)
        t = dz.Teacher(dz.PersonName(person_name, person_surname))
        zajecia=dz.Lesson(dz.ID(1),course_id=course.id,term=dz.Date("13:00",day=dz.Day["MON"]),teacher_id=t.id,students=[i.id for i in students])
        self.assertEqual(1 ,zajecia.teacher_id)


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



if __name__ == '__main__':
    unittest.main()
