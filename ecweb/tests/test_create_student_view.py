from django.test import TestCase
from django.shortcuts import resolve_url as r
from ecweb.models import (
    ClassRoom,
    BasicUser,
    Student,
    Teacher,
    Coordinator
)


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
            'email': 'admin_test@test.com',
            'password': '123456ab',
            'confirm_password': '123456ab'
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
