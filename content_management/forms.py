from django import forms
from .models import TeacherArticle, Category, AskQuestion, AnsQuestion, StudentQuestion


class TeacherArticleForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      empty_label="Select Category")

    class Meta:
        model = TeacherArticle
        fields = ["category", "article_image", "title", "description"]


class AskQuestionForm(forms.ModelForm):
    aks_question = forms.CharField(
        required=True, label="Ask Question", widget=forms.TextInput(attrs={"placeholder": "Write Question"}))

    class Meta:
        model = AskQuestion
        fields = ["aks_question"]


class StudentQuestionForm(forms.ModelForm):

    class Meta:
        model = StudentQuestion
        exclude = ('created_at', "user",)
