from django.views.generic import DetailView
from rest_framework import viewsets

from demo2.models import MyModel


# Create your views here.
class TestView(DetailView):
    model = MyModel


class TestView_2(viewsets.ModelViewSet):
    queryset = MyModel.objects.filter()
