from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from .utils.li import level_choices, type_list, test_choices


class MyUserManager(BaseUserManager):
    def _create_user(self,
                     email,
                     password,
                     is_staff,
                     is_superuser,
                     **extra_fields
                     ):
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(
            email, password, True, True, **extra_fields)
        return user


class StudentTests(models.Model):
    date_test = models.DateField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.date_test


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    cod = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), null=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    avatar = models.ImageField(
        upload_to='avatars/profiles',
        default='avatars/user_default.png',
        blank=True
    )
    type_of_course = models.CharField(max_length=30, choices=type_list,
                                      blank=True)
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

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()



class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class ClassRoom(models.Model):
    number_class = models.IntegerField(blank=True)
    level = models.CharField(max_length=30, choices=level_choices, blank=True)
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return '{}: {}'.format(self.number_class, self.level)



class Youtube(models.Model):
    description = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description


class PdfFile(models.Model):
    description = models.CharField(max_length=50, blank=True)
    file = models.FileField(upload_to="media/", blank=True)

    def __str__(self):
        return self.description


class Class(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    date = models.DateField()
    lesson = models.TextField()
    videos = models.ManyToManyField(Youtube, blank=True)
    files = models.ManyToManyField(PdfFile, blank=True)
    attendances = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return "{}: {}".format(self.date, self.lesson[:30])


class Test(models.Model):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=50, choices=test_choices)

    def __str__(self):
        return "{}: {}".format(self.date, self.lesson[:30])


class TestGrade(models.Model):
    test_event = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.FloatField()


class Menssage(models.Model):
    menssage_text = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Confirmed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    go = models.BooleanField(default=False)
    dgo = models.BooleanField(default=False)
    dknow = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class Calendar(models.Model):
    event = models.TextField(blank=True)
    date_start = models.DateField(blank=True, null=True,)
    date_end = models.DateField(blank=True, null=True,)
    title = models.CharField(max_length=30, blank=True)
    local = models.CharField(max_length=30, blank=True)
    menssage = models.ManyToManyField(Menssage, blank=True)
    confirm = models.ManyToManyField(Confirmed, blank=True)

    def __str__(self):
        return self.title
