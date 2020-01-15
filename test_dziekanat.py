#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from dziekanat import Course,Teacher, Student

class TestCourse(unittest.TestCase):
    def test_init(self):
        course = Course(name="Matematyka")
        self.assertEqual("Matematyka", course.name)

    def test_generate_id(self):
        self.assertEqual(1, Course.generate_id())


class TestTeacher(unittest.TestCase):
    def test_init(self):
        teacher = Teacher(name ="Jan Kowalski")
        self.assertEqual("Jan Kowalski", teacher.name)

    def test_generate_id(self):
        self.assertEqual(1, Teacher.generate_id())
        Teacher.generate_id()
        self.assertEqual(3, Teacher.generate_id())

class TestStudent(unittest.TestCase):
    def test_init(self):
        student = Student(name="Konrad Stalmach")
        self.assertEqual("Konrad Stalmach", student.name)

    def test_generate_id(self):
        self.assertEqual(1, Student.generate_id())

if __name__ == '__main__':
    unittest.main()
