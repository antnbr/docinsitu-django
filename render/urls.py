from django.urls import path
from . import views

urlpatterns = [
    path('writer/new/', views.writer_new_view, name='writer_new_view'),
    path('writer/response/', views.writer_response_view, name='writer_response_view'),
    path('writer/new/q<int:pk>/edit/', views.writer_new_edit_view, name='writer_new_edit_view'),
    path('writer/new/q<int:pk>/snap/', views.writer_new_snap_view, name='writer_new_snap_view'),
    path('writer/response/a<int:pk>/edit/', views.writer_response_edit_view, name='writer_response_edit_view'),
    path('writer/response/a<int:pk>/snap/', views.writer_response_snap_view, name='writer_response_snap_view'),
    # path('timeline/', views.timeline_view, name='timeline_view'),
]
