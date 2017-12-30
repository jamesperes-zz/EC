from django.test import TestCase
from django.shortcuts import resolve_url as r
from ecweb.models import (
    ClassRoom,
    BasicUser,
    Student,
    Teacher,
    Coordinator
)
from ecweb.forms import CreateUserForm, StudentForm

class TestCreateStudentView(TestCase):
    """ Testing createuser system """

    def setUp(self):
        user = BasicUser.objects.create_superuser(
            username='admin',
            password='1234abc',
            email="admin_test@admin.com"
        )
        Coordinator.objects.create(user=user)
        self.data = {
            'first_name': 'admin',
            'last_name': 'test',
            'email': 'admin_test3@test.com',
            'password': '123456ab',
            'confirm_password': '123456ab',
            'cod': 1,
            'type_of_course': '1-month'
        }
        self.url = r('create-student')

        self.client.login(
            username='admin_test@admin.com',
            password='1234abc'
        )
        self.response = self.client.get(self.url)

    def test_get_response_status(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(
            self.response,
            'registration/create_student.html'
        )

    def test_forms_used(self):
        userform = self.response.context['userform']
        studentform = self.response.context['studentform']
        self.assertIsInstance(userform, CreateUserForm)
        self.assertIsInstance(studentform, StudentForm)

    def test_create_object(self):
        response = self.client.post(self.url, self.data)
        student = Student.objects.get(
            user__email=self.data['email']
        )
        self.assertIsInstance(student, Student)
        self.assertRedirects(response, r('home_dashboard'))

    def test_password_validation(self):
        self.data['confirm_password'] = '789010abc'
        response = self.client.post(self.url, self.data)
        userform = response.context['userform']
        self.assertTrue(userform.errors)
        self.assertIn("Passwords don't match", userform.errors['confirm_password'])
