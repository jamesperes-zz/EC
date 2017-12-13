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
