from django.test import TestCase
from ecweb.models import ClassRoom, User, Student, Teacher
import datetime


class ClassRoomModelTest(TestCase):
    def setUp(self):
        self.classroom = ClassRoom.objects.create(
            number_class='01',
            nivel="upper"
        )
        self.user = User.objects.create(
            email="test@ec.com",
            first_name="TestName",
            last_name="TestLastName",
            cod=1,
        )

    def test_create(self):
        self.assertTrue(ClassRoom.objects.exists())

    def test_int_number_class(self):
        number = 1
        self.assertEqual(number, int(self.classroom.number_class))

    def test_str_nivel(self):
        self.assertEqual('upper', str(self.classroom.nivel))

    def test_student_forengkey(self):
        self.student = Student.objects.create(
            user=self.user,
            classroom=self.classroom
        )
        self.assertTrue(Student.objects.exists())

    def test_teacher_forengkey(self):
        self.teacher = Teacher.objects.create(
            user=self.user,
            classroom=self.classroom
        )
        self.assertTrue(Teacher.objects.exists())


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@ec.com",
            password="abcd1234ec",
            first_name="TestName",
            last_name="TestLastName",
            cod=1,
            type_of_course="6-month"
        )

    def test_create(self):
        self.assertTrue(User.objects.exists())
