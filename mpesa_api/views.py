from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import LipaNaMpesaOnline


# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def LipaNaMpesaCallBackURLView(request):
    print(request.data)
