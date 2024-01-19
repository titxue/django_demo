from django.urls import path
from rest_framework.routers import DefaultRouter

from demo2.views import MyModelDetailView

router = DefaultRouter()
urlpatterns = [
    path("demo2/", MyModelDetailView.as_view()),
]
