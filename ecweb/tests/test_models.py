from django.test import TestCase
from ecweb.models import (
    ClassRoom,
    BasicUser,
    Student,
    Teacher
)


class ClassRoomModelTest(TestCase):
    def setUp(self):
        self.classroom = ClassRoom.objects.create(
            number_class='01',
            level="upper"
        )
        self.BasicUser = BasicUser.objects.create(
            email="test@ec.com",
            first_name="TestName",
            last_name="TestLastName"
        )

    def test_create(self):
        self.assertTrue(ClassRoom.objects.exists())

    def test_int_number_class(self):
        number = 1
        self.assertEqual(number, int(self.classroom.number_class))

    def test_str_level(self):
        self.assertEqual('upper', str(self.classroom.level))

    def test_student_forengkey(self):
        self.student = Student.objects.create(
            user=self.BasicUser,
            classroom=self.classroom,
            cod=1
        )
        self.assertTrue(Student.objects.exists())

    def test_teacher_forengkey(self):
        self.teacher = Teacher.objects.create(
            user=self.BasicUser
        )
        self.assertTrue(Teacher.objects.exists())


class BasicUserModelTest(TestCase):
    def setUp(self):
        self.basic_user = BasicUser.objects.create(
            email="test@ec.com",
            password="abcd1234ec",
            first_name="TestName",
            last_name="TestLastName"
        )
        self.student = Student.objects.create(user=self.basic_user,
                                              cod=1,
                                              type_of_course='1-month'
                                              )

    def test_create(self):
        self.assertTrue(BasicUser.objects.exists())

    def test_student_exists(self):
        self.assertTrue(Student.objects.exists())

    def test_create_student(self):
        print(self.student)
        self.assertEqual(self.basic_user.first_name, self.student.first_name)

    def test_is_instance_of_BasicUser(self):
        self.assertIsInstance(self.basic_user, BasicUser)

    def test_str_method(self):
        object_name = '{} {}'.format(
            self.basic_user.first_name,
            self.basic_user.last_name
        )
        self.assertEqual(object_name, str(self.basic_user))

    def test_if_login_pass(self):
        login = self.client.login(
            email=self.student.email,
            password="abcd1234ec"
        )
        self.assertTrue(login)

    def test_default_image_profile(self):
        avatar_image_url = self.basic_user.avatar
        self.assertEqual('avatars/user_default.png', avatar_image_url)
