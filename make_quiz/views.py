from django.shortcuts import render, redirect
from .models import Quizzes
from .forms import QuizzesForm
from content_management.models import TeacherArticle
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from typing import Final
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.


@login_required(login_url="login")
def make_quizzes(request, pk):

    article = TeacherArticle.objects.get(pk=pk)
    article_quiz = Quizzes.objects.filter(
        user=request.user, article=article).count()

    if article_quiz <= 4:

        form = QuizzesForm()
        if request.method == "POST":
            form = QuizzesForm(request.POST)
            if form.is_valid():
                quiz = form.save(commit=False)
                quiz.user = request.user
                quiz.article = article
                quiz.save()
                article_quiz = Quizzes.objects.filter(
                    user=request.user, article=article).count()
                if article_quiz != 5:
                    messages.success(request, f"{article_quiz} Quiz created")
                return redirect("quizzes", pk)
        return render(request, "quizzes.html", context={"form": form, "quizCount": article_quiz})
    else:
        messages.warning(
            request, f"You Have Made {article_quiz} quizzes for the students ")
        return redirect("home")


@login_required(login_url="login")
def solve_quiz(request, slug):
    article = TeacherArticle.objects.get(slug=slug)
    article_quizzes = Quizzes.objects.filter(article=article)

    return render(request, "solveQuiz.html", context={"article_quizzes": article_quizzes, "teacherArticle": article})


@login_required(login_url="login")
def quiz_result(request, pk, slug):
    user = User.objects.get(pk=pk)
    article = TeacherArticle.objects.get(slug=slug)

    resultArr = []
    submitOne = request.POST.get("exampleRadios1").strip()
    submitTwo = request.POST.get("exampleRadios2").strip()
    submitThree = request.POST.get("exampleRadios3").strip()
    submitFour = request.POST.get("exampleRadios4").strip()
    submitFive = request.POST.get("exampleRadios5").strip()
    quizzes = Quizzes.objects.filter(user=user, article=article)

    if quizzes[0].correct_answer.strip() == submitOne:
        resultArr.append({
            "submission": True,
            "quiz": quizzes[0]
        })
    else:
        resultArr.append({
            "submission": submitOne,
            "quiz": quizzes[0]
        })

    if quizzes[1].correct_answer.strip() == submitTwo:
        resultArr.append({
            "submission": True,
            "quiz": quizzes[1]
        })
    else:
        resultArr.append({
            "submission": submitTwo,
            "quiz": quizzes[1]
        })

    if quizzes[2].correct_answer.strip() == submitThree:
        resultArr.append({
            "submission": True,
            "quiz": quizzes[2]
        })
    else:
        resultArr.append({
            "submission": submitThree,
            "quiz": quizzes[2]
        })
    if quizzes[3].correct_answer.strip() == submitFour:
        resultArr.append({
            "submission": True,
            "quiz": quizzes[3]
        })
    else:
        resultArr.append({
            "submission": submitFour,
            "quiz": quizzes[3]
        })
    if quizzes[4].correct_answer.strip() == submitFive:
        resultArr.append({
            "submission": True,
            "quiz": quizzes[4]
        })
    else:
        resultArr.append({
            "submission": submitFive,
            "quiz": quizzes[4]
        })

    print(resultArr)

    return render(request, "solveQuiz.html", context={"resultArr": resultArr})
