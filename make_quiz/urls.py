
from django.urls import path
from .import views

urlpatterns = [
    path("quizzes/<pk>/", views.make_quizzes, name="quizzes"),
    path("solve-Quiz/<slug>/", views.solve_quiz, name="solveQuiz"),
    path("solve-result/<pk>/<slug>", views.quiz_result, name="quizResult"),

]
