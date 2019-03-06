from . import views

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('paste/', views.PasteList.as_view()),
    path('paste/<int:pk>/', views.PasteDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
