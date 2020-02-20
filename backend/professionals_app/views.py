import requests
from django.core.checks import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from djoser.conf import django_settings

from rest_framework import status


# Create your views here.


# User views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request, *args, **kwargs):
    users = User.objects.all()
    serializer = UserCreateSerializer(users, context={"request": request}, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, email, *args, **kwargs):
    try:
        user = User.objects.get(email__contains=email)
        serializer = UserCreateSerializer(user, context={"request": request})
        return JsonResponse(serializer.data)
    except User.DoesNotExist:
        return HttpResponse(status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_service(request, service_name, *args, **kwargs):
    try:
        user = User.objects.get(service__service_name__contains=service_name)
        serializer = UserCreateSerializer(user, context={"request": request}, )
        return JsonResponse(serializer.data)
    except User.DoesNotExist:
        return HttpResponse(status=404)


# Category views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def categories(request, *args, **kwargs):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_detail(request, category_name, *args, **kwargs):
    try:
        category = Category.objects.get(category_name__contains=category_name)
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data, safe=False)
    except Category.DoesNotExist:
        return HttpResponse(status=404)


# Service Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def services(request, *args, **kwargs):
    service = Service.objects.all()
    serializer = ServiceSerializer(service, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Service_category(request, category_service, *args, **kwargs):
    try:
        service = Service.objects.get(category_contains=category_service)
        serializer = ServiceSerializer(service)
        return JsonResponse(serializer.data, safe=False)
    except Service.DoesNotExist:
        return HttpResponse(status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def service_detail(request, service_name, *args, **kwargs):
    try:
        service = Service.objects.get(service_name__contains=service_name)
        serializer = ServiceSerializer(service)
        service.searches + 1
        return JsonResponse(serializer.data, safe=False)
    except Category.DoesNotExist:
        return HttpResponse(status=404)


@api_view(['GET'])
def get(request, uid, token, *args, **kwargs):
    protocol = 'https://' if request.is_secure() else 'http://'
    web_url = protocol + request.get_host()
    post_url = web_url + '/professionals_app/users/activation/'
    post_data = {'uid': uid, 'token': token}
    response = requests.post(post_url, data=post_data)
    if response.status_code == 204:
        return render(request, 'professionals_app/success_activation.html')
    else:
        return render(request, 'professionals_app/unsuccessful_activation.html')


@api_view(['GET', 'POST'])
def reset(request, uid, token, *args, **kwargs):
    if request.POST:
        new_password = request.POST.get('new_password')
        re_new_password = request.POST.get('re_new_password')
        post_data = {'uid': uid, 'token': token, 'new_password': new_password, 're_new_password': re_new_password}

        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + '/professionals_app/users/reset_password_confirm/'

        response = requests.post(post_url, data=post_data)
        if response.status_code == 204:
            return render(request, 'professionals_app/success_reset.html')
        else:
            return render(request, 'professionals_app/unsuccessful_reset.html')
    else:
        return render(request, 'professionals_app/reset_password.html')
