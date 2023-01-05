from django.shortcuts import render,HttpResponseRedirect,redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login,logout
from django.core.mail import send_mail
from .models import CustomUser
from .models import Book
from .forms import BookAddForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core import serializers
# sighnup view function.

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            to = fm.cleaned_data.get('email')
            send_mail(              #added the send email functionality
                "Thanks For Registration",
                "You have successfully Signed Up and your credentials are sequered with us",
                'testem2129@gmail.com',
                [to],
                )
    else:    
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})

# login view function
def user_login(request):
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
          uname = fm.cleaned_data['username']
          upass = fm.cleaned_data['password']
          user = authenticate(username=uname,password=upass)
          if user is not None:
              login(request,user)
              return HttpResponseRedirect('/')
          
    else:      
        fm = AuthenticationForm()
    return render(request,'login.html', {'form':fm})
# profile
def user_profile(request):
    return render(request, 'profile.html')


def authsell(request):
    # user_data = CustomUser.objects.all()
    user_data = CustomUser.objects.filter(public_visibility=1)
    print(user_data)
    return render(request,'authsell.html',{'CustomUser':user_data})

def home(request):
    books = Book.objects.order_by('id').values()
    # books = Book.objects.order_by('fk').values()
    if books.exists():              #this checks if user has uploaded any file or not  
        return render(request, 'home.html', {'books': books})
    else:                #if user has not uploaded any file it will redirect it to upload file section
        return redirect('/add/')
    
    
    
def add_book(request):
    if request.method == 'POST':
        form = BookAddForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            # instance = form.save(commit=False)
            # instance.author = request.CustomUser
            # instance.save()
            messages.success(request, "Book added successfully")
            return redirect('home')
    else:
        form = BookAddForm()
    return render(request, 'add_book.html', {'form': form})

def delete_book(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        messages.success(request, "Book deleted successfully")
        return redirect('home')
    else:
        return redirect('home')
    
class ufileView(APIView):
    # authentication_classes = [JWTAuthentication]
    
    permission_classes = [IsAuthenticated]             
    
    def get(self, request):
        Book_json = serializers.serialize("json", Book.objects.all())
        content = {"Book_json":Book_json}
        return JsonResponse(content)
    # def get modelAPI(request):
    #     SomeModel_json = serializers.serialize("json", SomeModel.objects.all())
    #     data = {"SomeModel_json": SomeModel_json}
    #     return JsonResponse(data)