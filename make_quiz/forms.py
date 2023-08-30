from django import forms
from .models import Quizzes


class QuizzesForm(forms.ModelForm):
    class Meta:
        model = Quizzes
        exclude = ('created', "user", "article")
