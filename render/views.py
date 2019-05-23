from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Subject
from .models import Article
from .models import Snap

from .forms import ArticleForm
from .forms import SnapForm

# initial view
def writer_new_view(request):
    questions = Subject.objects.all().order_by('published_date')
    return render(request, 'render/writer/writer_new_view.html', {'questions': questions})

def writer_response_view(request):
    questions = Subject.objects.filter(published_date__lte=timezone.now())
    # print(questions)
    articles = Article.objects.filter(published_date__lte=timezone.now())
    # print(articles)
    snaps = Snap.objects.filter(published_date__lte=timezone.now())
    # print(snaps)
    return render(request, 'render/writer/writer_response_view.html', {'questions': questions})

def writer_new_edit_view(request, pk):
    question = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('writer_new_view')
    else:
        form = ArticleForm()
    return render(request, 'render/writer/writer_new_edit_view.html', {'question': question}, {'form': form})

def writer_new_snap_view(request):
    question = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = SnapForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('writer_new_view')
    else:
        form = SnapForm()
    return render(request, 'render/writer/writer_new_snap_view.html', {'question': question}, {'form': form})

def writer_response_edit_view(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('writer_new_view')
    else:
        form = ArticleForm()
    return render(request, 'render/writer/writer_new_edit_view.html', {'form': form})

def writer_response_snap_view(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('writer_new_view')
    else:
        form = ArticleForm()
    return render(request, 'render/writer/writer_new_edit_view.html', {'form': form})
