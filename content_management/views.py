from django.shortcuts import render, redirect
from .models import Category, TeacherArticle, AskQuestion, AnsQuestion, StudentQuestion, SolvedByTeacher
from .forms import TeacherArticleForm, AskQuestionForm, StudentQuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
# Create your views here.


def home(request):
    categories = Category.objects.all()
    articles = TeacherArticle.objects.all()
    return render(request, "home.html", context={"categories": categories, "articles": articles})


@login_required(login_url="login")
def teacher_article(request):
    form = TeacherArticleForm()
    if request.method == "POST":
        form = TeacherArticleForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.slug = article.title.replace(
                " ", "-") + "-" + str(uuid.uuid4())
            article.save()
            messages.success(request, "Article Created Successfully!")
            return redirect("home")
    return render(request, "TeacherArticle.html", context={"form": form})


def articleDetails(request, slug):

    article = TeacherArticle.objects.get(slug=slug)
    student_question = AskQuestion.objects.filter(article=article)
    form = AskQuestionForm()

    return render(request, "articleDetails.html", context={"article": article, "form": form, "student_question": student_question})


@login_required(login_url="login")
def ans_question(request, pk, slug):
    qus = AskQuestion.objects.get(pk=pk)

    if request.method == "POST":
        ans = request.POST.get("ans")
        ansQuestion = AnsQuestion.objects.create(
            question=qus, user=request.user, ans_question=ans)
        ansQuestion.save()
        messages.warning(request, "Answer saved!")

    return redirect("articleDetails", slug)


@login_required(login_url="login")
def question_received(request, slug):
    article = TeacherArticle.objects.get(slug=slug)
    form = AskQuestionForm()
    if request.method == "POST":
        form = AskQuestionForm(request.POST)

        if form.is_valid():
            qus = form.save(commit=False)
            qus.user = request.user
            qus.article = article
            qus.save()
            messages.success(request, "Question Added!")
    return redirect("articleDetails", slug)


def searchByCategory(request, pk):
    categoryArticles = TeacherArticle.objects.filter(category__pk=pk)
    categories = Category.objects.all()
    return render(request, "home.html", context={"categoryArticles": categoryArticles, "categories": categories})


@login_required(login_url="login")
def student_question_form(request):
    form = StudentQuestionForm()
    if request.method == "POST":
        form = StudentQuestionForm(request.POST)
        if form.is_valid():
            student_from = form.save(commit=False)
            student_from.user = request.user
            student_from.save()
            messages.success(
                request, "Your Question will be answer as soon possible")
            return redirect("home")
    return render(request, "studentQus.html", context={"form": form})


@login_required(login_url="login")
def question_section(request):
    studentQuestion = StudentQuestion.objects.all()
    return render(request, "questionSection.html", context={"studentQuestion": studentQuestion})


@login_required(login_url="login")
def question_form_solved(request, pk):

    studentQuz = StudentQuestion.objects.get(pk=pk)
    print(studentQuz)
    print(request.POST)
    if request.method == "POST":
        ans = request.POST.get("ans")
        SolvedByTeacher.objects.create(
            question=studentQuz, user=request.user, ans_question=ans).save()
        messages.success(request, "Question Answered Saved Successfully")
    return redirect("questionSection")
