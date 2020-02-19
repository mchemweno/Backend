
from django.urls import path, include
from . import views
from .views import *

app_name = 'professionals_app'
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('userlist/', views.user_list),
    path('userlist/<str:email>/', views.user_detail),
    path('userlist/service/<str:service_name>', views.user_service),
    path('categories/', views.categories),
    path('categories/<str:category_name>', views.category_detail),
    path('services/', views.services),
    path('services/<str:service_name>', views.service_detail),
    path('users/activate/<str:uid>/<str:token>', views.get),
    path('users/password-reset/<str:uid>/<str:token>', views.reset),
]
