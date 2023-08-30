
from django.urls import path
from .import views

urlpatterns = [
    path("article/", views.teacher_article, name="article"),
    path("article_details/<slug>/",
         views.articleDetails, name="articleDetails"),
    path("answer/<pk>/<slug>/", views.ans_question, name="answer"),
    path("question_received/<slug>/",
         views.question_received, name="question_received"),
    path("category/<pk>", views.searchByCategory, name="searchByCategory"),
    path("student-question-form/",
         views.student_question_form, name="studentQusForm"),
    path("question-section/",
         views.question_section, name="questionSection"),
    path("solved-question-form/<pk>",
         views.question_form_solved, name="solvedQuestionForm"),

]
