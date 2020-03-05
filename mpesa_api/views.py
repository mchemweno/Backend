from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import LipaNaMpesaOnline


# Create your views here.

class LipaNaMpesaCallBackURLView(CreateAPIView):
    queryset = LipaNaMpesaOnline.objects.all()
    serializer_class = LipaNaMpesaSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data)
