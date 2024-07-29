from django import forms
from django.contrib.auth.models import User
from TodoApp.models import Todos

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"firstName"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"LastName"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"UserName"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),

        }

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","content"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}),
            "content":forms.TextInput(attrs={"class":"form-control","placeholder":"Content"}),
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","content","status"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}),
            "content":forms.TextInput(attrs={"class":"form-control","placeholder":"Content"}),
            "status":forms.CheckboxInput(attrs={"class":"form-check","placeholder":"Content"}),

        }
