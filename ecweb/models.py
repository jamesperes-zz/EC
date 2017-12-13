from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from .utils.li import nivel_list, type_list


class Attendance(models.Model):
    attendance = models.DateField(blank=True)

    def __str__(self):
        return self.attendance


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
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    type_of_course = models.CharField(max_length=30, choices=type_list,
                                      blank=True)

    attendance = models.ManyToManyField(Attendance, blank=True)
    grades = models.ManyToManyField(StudentTests, blank=True)

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


class Youtube(models.Model):
    description = models.CharField(max_length=50, blank=True)
    link = models.CharField(max_length=255, blank=True)


class Pdf_file(models.Model):
    description = models.CharField(max_length=50, blank=True)
    file = models.FileField(upload_to="media/", blank=True)




class ClassRoom(models.Model):
    number_class = models.IntegerField(blank=True)
    nivel = models.CharField(max_length=30, choices=nivel_list, blank=True)
    students = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube = models.ManyToManyField(Youtube, blank=True)
    pdf = models.ManyToManyField(Pdf_file, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.number_class, self.nivel)

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

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
