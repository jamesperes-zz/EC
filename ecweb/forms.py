from django import forms
from django.contrib.auth import forms as auth_forms
from .models import User
from PIL import Image
from django.core.files import File


class CreateUserFormAdmin(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'avatar', 'first_name',
            'last_name', 'email', 'password',
            'cod', 'type_of_course', 'is_active',
            'is_staff', 'attendance', 'grades'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super(CreateUserAdmin, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UpdateUserFormAdmin(CreateUserFormAdmin):
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
        model = User
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
