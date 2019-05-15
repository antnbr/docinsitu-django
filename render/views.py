from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article

# initial view
def render_view(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'render/render_view.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'render/article_detail.html', {'article': article})
