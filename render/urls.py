from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_view, name='render_view'),
    path('article/<int:pk>', views.article_detail, name='article_detail'),
    path('article/new/', views.article_new, name='article_new'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
]
