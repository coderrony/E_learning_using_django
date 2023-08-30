from django.contrib import admin
from .models import Category, TeacherArticle, AskQuestion, AnsQuestion, StudentQuestion, SolvedByTeacher
# Register your models here.


@admin.register(TeacherArticle)
class TeacherAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug']


@admin.register(AskQuestion)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['pk', "user", 'article']


@admin.register(AnsQuestion)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'ans_question']


@admin.register(StudentQuestion)
class StudentQuestionAdmin(admin.ModelAdmin):

    list_display = ['user', 'title']


@admin.register(SolvedByTeacher)
class SolvedByTeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'ans_question']


admin.site.register(Category)
