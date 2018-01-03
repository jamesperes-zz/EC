from django.test import TestCase
from django.urls import reverse as r
from ecweb.models import ClassRoom, Teacher, Student, BasicUser


class TestClassroomDetailView(TestCase):

    def setUp(self):
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
            level='begginner',
            turn='morning'
        )
        self.classroom.students.set([student1, student2])
        self.classroom.teachers.set([teacher])

        self.classroom_detail_url = r(
            'classroom_detail_view', kwargs={'slug': self.classroom.slug}
        )

        self.client.login(
            username='user3@gmail.com',
            password='123'
        )

    def test_classroom_detail_not_loged_user(self):
        self.client.logout()

        response = self.client.get(self.classroom_detail_url, follow=True)

        self.assertTemplateUsed(response, 'registration/login.html')
