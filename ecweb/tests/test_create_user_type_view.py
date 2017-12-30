from django.test import TestCase
from django.shortcuts import resolve_url as r
from ecweb.models import (
    ClassRoom,
    BasicUser,
    Student,
    Teacher
)


class TestCreateUserTypeView(TestCase):
    """ Testing createuser system """

    def setUp(self):
        BasicUser.objects.create_superuser(
            username='admin',
            password='1234abc',
            email="admin_test@admin.com"
        )
        self.data = {
            'first_name': 'admin',
            'last_name': 'test',
            'email': 'admin_test@test.com',
            'password': '123456ab',
            'confirm_password': '123456ab'
        }
        self.url_coordinator = r('create-user', 'coordinator')
        self.url_teacher = r('create-user', 'teacher')

        self.client.login(
            username='admin_test@admin.com',
            password='1234abc'
        )

    def test_response_status_with_type_coordinator(self):
        response = self.client.get(self.url_coordinator)
        self.assertEqual(200, response.status_code)

    def test_response_status_with_type_teacher(self):
        response = self.client.get(self.url_teacher)
        self.assertEqual(200, response.status_code)
