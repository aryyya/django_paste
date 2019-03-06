from . import views

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('paste/', views.paste_list),
    path('paste/<int:pk>/', views.paste_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
