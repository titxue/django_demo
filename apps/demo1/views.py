from django.views.generic import DetailView

from demo2.models import MyModel


# Create your views here.
class TestView(DetailView):
    model = MyModel
