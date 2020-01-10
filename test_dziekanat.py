#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from dziekanat import Course,Teacher, Student

class Test_Course(unittest.TestCase):
    def test_init(self):
        course = Course(id="RB01", name="Matematyka")
        self.assertEqual("Matematyka", course.name)

class Test_Teacher(unittest.TestCase):
    def test_init(self):
        teacher = Teacher(id="111", name="Adam Kowalski")
        self.assertEqual("111", teacher.id)
        self.assertEqual("Adam Kowalski", teacher.name)

class Test_Student(unittest.TestCase):
    def test_init(self):
        student = Student(id="302915", name="Konrad Stalmach")
        self.assertEqual("302915", student.id)
        self.assertEqual("Konrad Stalmach", student.name)


if __name__ == '__main__':
    unittest.main()
