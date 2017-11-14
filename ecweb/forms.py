from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email',
                  'date_joined', 'is_staff', 'avatar')
