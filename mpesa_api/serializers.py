from rest_framework import serializers
from .models import *


class LipaNaMpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LipaNaMpesaOnline
        fields = '__all__'


class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = '__all__'
