from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import views

router = DefaultRouter()
router.register(r'pastes', views.PasteViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Paste API')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view)
]
