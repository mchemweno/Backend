from django.urls import path, include

from . import views

app_name = 'professionals_app'
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # users urls
    path('userlist/', views.user_list),
    path('userlist/<str:email>/', views.user_detail),
    path('userlist/service/<str:service_name>', views.user_service),
    # categories urls
    path('categories/', views.categories),
    path('categories/<str:category_name>', views.category_detail),
    # service urls
    path('services/', views.services),
    path('services/<str:service_name>', views.service_detail),
    path('services/category/<str:category>', views.service_category),
    path('popular', views.most_popular_services),
    # review urls
    path('reviews/<int:reviewee_id>', views.review),
    # activation and password reset urls
    path('users/activate/<str:uid>/<str:token>', views.get),
    path('users/password-reset/<str:uid>/<str:token>', views.reset),
]
