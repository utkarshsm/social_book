from django.shortcuts import render
from rest_framework.views import APIView
from serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.
class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializes.errors,'messsage':'something went wrong'})
        
        serializes.save()
        user = User.objects.get(username= serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
            
            
        return Response({'status':200,'payload':serializes.data,'token':str(token_obj)})