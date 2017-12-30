"""EC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('ecweb.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='registration/change-password.html'),),
    path('forget-password/done', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/forget-done.html'),),
    path('forget-password/', auth_views.PasswordResetView.as_view(
        template_name='registration/forget-password.html',
        success_url='done'), name='forget_password'),
    url(r'^password/reset/\
        (?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/forget-confirm.html',),
        name='password_reset_confirm',
        ),
    url(r'^password/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/forget-complete.html'),
        name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
