from django.test import TestCase
from django.urls import resolve


from ecweb import views


class UrlsTest(TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.home_dashboard)

    def test_home_page_not_loged_returns_login_html(self):
        response = self.client.get('/', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_student_resolve_user_detail_view(self):
        found = resolve('/student/')
        self.assertEqual(found.func, views.user_detail)

    def test_dashboard_resolve_home_dashboard_view(self):
        found = resolve('/dashboard/')
        self.assertEqual(found.func, views.home_dashboard)

    def test_create_student_resolve_create_student_view(self):
        found = resolve('/create-student/')
        self.assertEqual(found.func, views.create_student_view)

    def test_create_student_not_logged_returns_login_html(self):
        response = self.client.get('/create-student/', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_create_user_resolve_create_user_type_view(self):
        found = resolve('/create-user/coordinator')

        self.assertEqual(found.kwargs, {'user_type': 'coordinator'})
        self.assertEqual(found.func, views.create_user_type_view)

    def test_create_user_not_logged_returns_login_html(self):
        response = self.client.get('/create-user/coordinator', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_classrooms_resolve_ClassRoomListView(self):
        found = resolve('/classrooms/')
        self.assertEqual(found.view_name, 'classroom_view')

    def test_classrooms_not_logged_returns_login_html(self):
        response = self.client.get('/classrooms/', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_classrooms_detail_resolve_class_room_detail_view(self):
        found = resolve('/classrooms/beginner-morning-2/detail')

        self.assertEqual(found.kwargs, {'slug': 'beginner-morning-2'})
        self.assertEqual(found.view_name, 'classroom_detail_view')

    def test_classrooms_detail_not_logged_returns_login_html(self):
        response = self.client.get('/classrooms/beginner-morning-2/detail', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_classrooms_edit_resolve_class_room_edit_view(self):
        found = resolve('/classrooms/beginner-morning-2/edit')

        self.assertEqual(found.kwargs, {'slug': 'beginner-morning-2'})
        self.assertEqual(found.view_name, 'classroom_update_view')

    def test_classrooms_edit_not_logged_returns_login_html(self):
        response = self.client.get('/classrooms/beginner-morning-2/edit', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_classrooms_edit_resolve_class_room_delete_view(self):
        found = resolve('/classrooms/beginner-morning-2/delete')

        self.assertEqual(found.kwargs, {'slug': 'beginner-morning-2'})
        self.assertEqual(found.view_name, 'classroom_delete_view')

    def test_classrooms_delete_not_logged_returns_login_html(self):
        response = self.client.get('/classrooms/beginner-morning-2/delete', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_classrooms_create_resolve_class_room_create_view(self):
        found = resolve('/classrooms/create/')
        self.assertEqual(found.view_name, 'classroom_create_view')

    def test_classrooms_create_not_logged_returns_login_html(self):
        response = self.client.get('/classrooms/create', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_class_resolve_list_classes_view(self):
        found = resolve('/class/1/')

        self.assertEqual(found.kwargs, {'class_room_id': 1})
        self.assertEqual(found.func, views.list_classes_view)

    def test_class_not_logged_returns_login_html(self):
        response = self.client.get('/class/1', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_class_attendances_resolve_class_view(self):
        found = resolve('/class/1/attendances/')

        self.assertEqual(found.kwargs, {'class_id': 1})
        self.assertEqual(found.func, views.class_view)

    def test_class_attendances_not_logged_returns_login_html(self):
        response = self.client.get('/class/1/attendances', follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')
