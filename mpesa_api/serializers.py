from rest_framework import serializers
from .models import *


class LipaNaMpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model= LipaNaMpesaOnline
        #fields =