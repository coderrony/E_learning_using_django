from django.db import models
from content_management.models import TeacherArticle
from django.contrib.auth.models import User
# Create your models here.


class Quizzes(models.Model):
    article = models.ForeignKey(
        TeacherArticle,  on_delete=models.CASCADE, related_name="quiz_article")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="quiz_user")
    question = models.CharField(max_length=265)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user)
