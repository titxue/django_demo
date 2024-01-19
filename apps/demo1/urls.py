from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.demo1.views import TestView

router = DefaultRouter()
urlpatterns = [
    path("demo1/", TestView.as_view()),
]
