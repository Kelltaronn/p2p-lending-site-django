#Imports:
from typing import Any
import Bank_database.models as model
from django import forms
from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm ,UsernameField,UserCreationForm
from django.forms.widgets import TextInput

class Szamlaform(forms.ModelForm):
    class Meta:
        model=model.Szamla
        fields = [
                "aktualis_osszeg",
                "szamla_tulajdonos",
                "szamla_tipus",
        ]

class AddToBalanceForm(forms.Form):
    osszeg = forms.FloatField()

class Userform(AuthenticationForm):
    #def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
    #    super().__init__(request, *args, **kwargs)
    #username = forms.CharField(widget=TextInput(attrs={'class': 'span2','placeholder': 'Email'}))
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control","id":"floatingInput","placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete":"current-password", "class":"form-control" ,"id":"floatingPassword","placeholder":"Password"}))

class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control","id":"floatingInputUser","placeholder":"Username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control","id":"floatingPassword1"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control","id":"floatingPassword2"}))