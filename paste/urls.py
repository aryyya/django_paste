from django.urls import path
from . import views

urlpatterns = [
    path('paste/', views.paste_list),
    path('paste/<int:pk>/', views.paste_detail)
]
