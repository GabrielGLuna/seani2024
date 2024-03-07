from django import forms

from career.models import Career
from exam.models import Stage


class CandidateForm(forms.Form):
    name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    user_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput)
    career = forms.ModelChoiceField(Career.objects.all(),
                                    empty_label="Seleccione una carrera")
    stage = forms.ModelChoiceField(Stage.objects.all(),
                                   empty_label="Seleccione una etapa")

  