from django.urls import path

from . import views

urlpatterns = [
    # for lipa na mpesa online use
    path('lnm/', views.LipaNaMpesaCallBackURLView),

    # for c2b urls i.e confirmation and validatiom
    path('c2b_confirmation/', views.C2bConfirmationURLView),
    path('c2b_validation/', views.C2bValidationURLView)
]
