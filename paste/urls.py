from . import views

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('pastes/', views.PasteList.as_view(), name='paste-list'),
    path('pastes/<int:pk>/', views.PasteDetail.as_view(), name='paste-detail'),
    path('pastes/<int:pk>/highlight/', views.PasteHighlight.as_view(), name='paste-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
