#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from dziekanat import Course, Teacher, Student, PersonName


class TestCourse(unittest.TestCase):
    def test_init(self):
        course = Course(name="Matematyka")
        self.assertEqual("Matematyka", course.name)

    def test_generate_id(self):
        self.assertEqual(1, Course.generate_id())


class TestTeacher(unittest.TestCase):
    def test_init(self):
        teacher = PersonName(name ="Jan",surname = 'Kowalski')
        self.assertEqual("JanKowalski", teacher.name + teacher.surname)



    def test_generate_id(self):
        self.assertEqual(1, Teacher.generate_id())
        Teacher.generate_id()
        self.assertEqual(3, Teacher.generate_id())

class TestStudent(unittest.TestCase):
    def test_init(self):

        student = PersonName(name="Konrad", surname='Stalmach')
        self.assertEqual("KonradStalmach", student.name + student.surname)

    def test_generate_id(self):
        self.assertEqual(1, Student.generate_id())

# class TestStudentRepository(unittest.TestCase):



if __name__ == '__main__':
    unittest.main()

