import json
from django.test import TestCase
from django.urls import reverse as r
from ecweb.models import ClassRoom, Teacher, Student, BasicUser
from django.utils.http import urlencode


class TestClassroomUpdateView(TestCase):

    def setUp(self):
        user = BasicUser.objects.create_superuser(
            username='admin',
            password='1234abc',
            email="admin_test@admin.com"
        )

        user1 = BasicUser.objects.create(
            username='user1',
            password='123',
            email="user1@gmail.com"
        )

        user2 = BasicUser.objects.create(
            username='user2',
            password='123',
            email="user2@gmail.com",
        )

        user3 = BasicUser.objects.create(
            username='user3',
            password='123',
            email="user3@gmail.com",
            is_staff=True
        )

        student1 = Student.objects.create(
            user=user1,
            cod=2,
            type_of_course='1-month'
        )

        student2 = Student.objects.create(
            user=user2,
            cod=3,
            type_of_course='1-month'
        )

        teacher = Teacher.objects.create(
            user=user3
        )

        self.classroom = ClassRoom.objects.create(
            number_class=1,
            level='Beginner',
            turn='morning'
        )
        self.classroom.students.add(student1, student2)
        self.classroom.teachers.add(teacher)

        self.classroom_update_url = r(
            'classroom_update_view', kwargs={'slug': self.classroom.slug}
        )

        self.client.login(
            username='admin_test@admin.com',
            password='1234abc',
        )

    def test_classroom_update_not_loged_user(self):
        self.client.logout()

        response = self.client.get(self.classroom_update_url, follow=True)

        self.assertTemplateUsed(response, 'registration/login.html')

    def test_classroom_update_template(self):

        response = self.client.get(self.classroom_update_url, follow=True)
        self.assertTemplateUsed(response, 'ecweb/classroom/update_classroom.html')

    def test_classroom_form_invalid(self):

        response = self.client.put(
            self.classroom_update_url,
            {'name':'Some Name'}
        )

        form = response.context['form']

        self.assertEquals(response.status_code, 200)
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.as_p())

    def test_classroom_form_valid_does_changed(self):
        response = self.client.get(self.classroom_update_url)
        data = response.context['form'].initial

        data['number_class'] = self.classroom.number_class
        data['students'] = [str(student.pk) for student in data['students']]
        data['teachers'] = [str(teacher.pk) for teacher in data['teachers']]

        response = self.client.post(
            self.classroom_update_url,
            data,
            follow=True
        )

        message = list(response.context['messages'])[0]

        self.assertEquals(str(message), 'The classroom does changed.')
