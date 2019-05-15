from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_view, name='render_view'),
    path('article/<int:pk>', views.article_detail, name='article_detail'),
]
