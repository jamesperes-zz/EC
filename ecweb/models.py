from django.db import models
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from .utils.li import level_choices, type_list, test_choices


from django.contrib.auth.models import AbstractUser


class BasicUser(AbstractUser):
    email = models.EmailField(_('email address'), null=False, blank=False, unique=True)

    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True)

    avatar = models.ImageField(
        upload_to='avatars/profiles',
        default='avatars/user_default.png',
        blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Student(models.Model):
    user = models.OneToOneField(BasicUser, on_delete=models.CASCADE)
    cod = models.IntegerField(blank=False, null=False)
    type_of_course = models.CharField(max_length=30, choices=type_list, blank=False, null=False)

    def __str__(self):
        return self.user.first_name


class Teacher(models.Model):
    user = models.OneToOneField(BasicUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.first_name



class Coordinator(models.Model):
    user = models.OneToOneField(BasicUser, on_delete=models.CASCADE)
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
