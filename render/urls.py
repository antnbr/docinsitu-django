from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_view, name='render_view'),
]
