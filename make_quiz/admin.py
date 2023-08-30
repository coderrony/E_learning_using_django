from django.contrib import admin
from .models import Quizzes
# Register your models here.


@admin.register(Quizzes)
class QuizzesAdmin(admin.ModelAdmin):

    list_display = ['user', 'question', "correct_answer"]
