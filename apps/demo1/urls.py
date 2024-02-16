from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.demo1.views import TestView, TestView_2

router = DefaultRouter()
router.register(r'demo_1', TestView_2)
urlpatterns = [
    path("demo1/", TestView.as_view()),
    path('', include(router.urls)),
]
