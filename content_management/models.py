from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class TeacherArticle(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_upload")
    article_image = models.ImageField(
        upload_to="articleImg", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="article_category")
    title = models.CharField(max_length=256)
    slug = models.SlugField(blank=True, max_length=500)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AskQuestion(models.Model):
    article = models.ForeignKey(
        TeacherArticle, on_delete=models.CASCADE, related_name="article_comment")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment")
    aks_question = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str:
        return str(self.aks_question)


class AnsQuestion(models.Model):
    question = models.ForeignKey(
        AskQuestion, on_delete=models.CASCADE, related_name="student_question")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="answered_user")
    ans_question = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str:
        return str(self.user)


class StudentQuestion(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="student_question")
    title = models.CharField(max_length=256)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SolvedByTeacher(models.Model):
    question = models.ForeignKey(
        StudentQuestion, on_delete=models.CASCADE, related_name="solved_question")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="solved_teacher")
    ans_question = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str:
        return str(self.user)
