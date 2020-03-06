import os

import requests
from django.core.mail import send_mail

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status

from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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
        user.average_rating = calculate_average_review(id=user.id)
        user.save()
        serializer = UserCreateSerializer(user, context={"request": request})
        return JsonResponse(serializer.data)
    except User.DoesNotExist:
        return Response(data={}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_service(request, service_name, *args, **kwargs, ):
    try:
        user = User.objects.get(service__service_name=service_name)
        serializer = UserCreateSerializer(user, context={"request": request})
        return JsonResponse(serializer.data)
    except User.DoesNotExist:
        return Response(data={}, status=404)


# Category views
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def categories(request, *args, **kwargs):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def category_detail(request, category_name, *args, **kwargs):
    try:
        category = Category.objects.get(category_name=category_name)
        serializer = CategorySerializer(category, context={"request": request})
        return JsonResponse(serializer.data, safe=False)
    except Category.DoesNotExist:
        return Response(data={}, status=404)


# Service Views
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def services(request, *args, **kwargs):
    serviceArray = []
    services = Service.objects.all()
    for service in services:
        user = User.objects.filter(service=service.id)
        serializer1 = UserCreateSerializer(user, context={"request": request}, many=True)
        serializer = ServiceSerializer(service)
        data = {'service': serializer.data, 'professional': serializer1.data}
        serviceArray.append(data)
    print(serviceArray)
    return JsonResponse(serviceArray, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def most_popular_services(request, *args, **kwargs):
    serviceArray = []
    services = Service.objects.all().order_by('-searches')[:6]
    for service in services:
        user = User.objects.filter(service=service.id)
        serializer1 = UserCreateSerializer(user, context={"request": request}, many=True)
        serializer = ServiceSerializer(service)
        data = {'service': serializer.data, 'professional': serializer1.data}
        serviceArray.append(data)
    return JsonResponse(serviceArray, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def service_category(request, category, *args, **kwargs):
    serviceArray = []
    services = Service.objects.filter(category__category_name=category)
    for service in services:
        user = User.objects.filter(service=service.id)
        serializer1 = UserCreateSerializer(user, context={"request": request}, many=True)
        serializer = ServiceSerializer(service)
        data = {'service': serializer.data, 'professional': serializer1.data}
        serviceArray.append(data)
    return JsonResponse(serviceArray, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def service_detail(request, service_name, *args, **kwargs):
    try:
        service = Service.objects.get(service_name=service_name)
        service.searches += 1
        service.save()
        serializer = ServiceSerializer(service)
        user = User.objects.filter(service=service.id)
        serializer1 = UserCreateSerializer(user, context={"request": request}, many=True)
        return JsonResponse({'service': serializer.data, 'professionals': serializer1.data}, safe=False)
    except Service.DoesNotExist:
        return Response(data={}, status=404)


# Review views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review(request, reviewee_id, *args, **kwargs):
    if request.method == 'POST':
        data = request.data
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        reviews = Review.objects.filter(reviewee=reviewee_id, )
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


# Report view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def report(request, *args, **kwargs):
    data = request.data
    serializer = ReportSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        complainant_email = data['complainant_email']
        complainant_fname = data['complainant_fname']
        complainant_lname = data['complainant_lname']
        complain_against = data['complain_against']
        complaint = data['complaint']
        subject = f'Complaint against {complain_against}'
        message = f' User by the name {complainant_fname} {complainant_lname} has raised a complaint against user of id {complain_against}.\nComplainant email is {complainant_email}\n\nComplaint:\n{complaint}'
        send_mail(subject, message, os.environ.get('email'), [os.environ.get('email')])
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Reset password, send activation email and resend activation email.
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


# calculate reviewers average
def calculate_average_review(id):
    try:
        reviews = Review.objects.filter(reviewee=id)
        total_rating = 0
        counter = 0
        for review in reviews:
            total_rating = total_rating + review.rating
            counter = counter + 1

        average_rating = round(total_rating / counter)
        return average_rating
    except Review.DoesNotExist:
        return 1
