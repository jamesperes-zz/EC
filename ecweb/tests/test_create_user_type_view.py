from django.test import TestCase
from django.shortcuts import resolve_url as r
from ecweb.models import (
    ClassRoom,
    BasicUser,
    Student,
    Teacher,
    Coordinator
)


class TestCreateUserTypeView(TestCase):
    """ Testing createuser system """

    def setUp(self):
        user = BasicUser.objects.create_superuser(
            username='admin',
            password='1234abc',
            email="admin_test@admin.com"
        )
        Coordinator.objects.create(user=user)
        self.data_coordinator = {
            'first_name': 'admin',
            'last_name': 'test',
            'email': 'admin_test@test.com',
            'password': '123456ab',
            'confirm_password': '123456ab'
        }
        self.data_teacher = {
            'first_name': 'admin2',
            'last_name': 'test2',
            'email': 'admin_test2@test.com',
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

    def test_create_object_type_coordinator(self):
        self._test_create_object(
            data=self.data_coordinator,
            url=self.url_coordinator,
            model=Coordinator,
        )

    def test_create_object_type_teacher(self):
        self._test_create_object(
            data=self.data_teacher,
            url=self.url_teacher,
            model=Teacher,
        )

    def _test_create_object(self, data, model, url):
        response = self.client.post(url, data)
        instance = model.objects.get(
            user__email=data['email']
        )
        self.assertIsInstance(instance, model)
        self.assertRedirects(response, r('home_dashboard'))
