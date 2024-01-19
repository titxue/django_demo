from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views.generic import DetailView

from demo2.models import MyModel


class Demo2View(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        return Response({"message": "Hello, world!"})


class MyModelDetailView(DetailView):
    model = MyModel


@api_view(['GET'])
def view_name(request):
    pass
