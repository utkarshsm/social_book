from django.shortcuts import render
from .models import CustomUser
# Create your views here.
def home(request):
    # user_data = CustomUser.objects.all()
    user_data = CustomUser.objects.filter(public_visibility=1)
    print(user_data)
    return render(request,'users/home.html',{'CustomUser':user_data})