from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class Attendance(models.Model):
    attendance = models.DateField(blank=True)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class StudentTests(models.Model):
    date_test = models.DateField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), null=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    attendance = models.ManyToManyField(Attendance)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class ClassRoom(models.Model):
    students = models.ForeignKey(User)
    youtube = models.URLField(blank=True)
    pdf = models.FileField(upload_to="media/", blank=True)


class Menssage(models.Model):
    menssage = models.TextField(blank=True)
    user = models.ForeignKey(User)


class Confirmed(models.Model):
    user = models.ForeignKey(User)
    go = models.BooleanField(default=False)
    dgo = models.BooleanField(default=False)
    dknow = models.BooleanField(default=False)


class Calendar(models.Model):
    event = models.TextField(blank=True)
    date_start = models.DateField(blank=True, null=True,)
    date_end = models.DateField(blank=True, null=True,)
    title = models.CharField(max_length=30, blank=True)
    local = models.CharField(max_length=30, blank=True)
    menssage = models.ManyToManyField(Menssage, blank=True)
    confirm = models.ManyToManyField(Confirmed, blank=True)
