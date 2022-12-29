from rest_framework import serializes 
from models import *
from django.contrib.auth.models import User

class UserSerializer(serializes.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','password']
        