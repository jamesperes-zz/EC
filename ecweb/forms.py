from django import forms
from django.contrib.auth import forms as auth_forms
from .models import BasicUser, Student
from PIL import Image
from django.core.files import File


class CreateUserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='Confirm Password',
        max_length=128,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = BasicUser
        fields = [
            'avatar', 'first_name',
            'last_name', 'email',
            'password', 'confirm_password'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return super(CreateUserForm, self).clean()

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UpdateUserFormAdmin(CreateUserForm):
    password = auth_forms.ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, instead "
            "a hash is created from them, and is "
            "saved in the database. "
        )
    )


class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = BasicUser
        fields = ('avatar', 'x', 'y', 'width', 'height', )
        widgets = {
            'avatar': forms.FileInput(attrs={
                'accept': 'image/*'  # this is not an actual validation! don't rely on that!
            })
        }

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.avatar)
        cropped_image = image.crop((x, y, w + x, h + y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.avatar.path)

        return photo


class AttendanceForm(forms.Form):
    class_id = forms.CharField(
        label='Class id', max_length=100, widget=forms.HiddenInput())
    students = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(), required=False)
