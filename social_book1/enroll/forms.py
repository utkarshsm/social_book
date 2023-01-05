from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from .models import Book

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','age','birth_date','address','public_visibility']
        # labels = {'email':'Email'}
        
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
        

class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'category', 'cover', 'pdf')