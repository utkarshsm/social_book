from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login,logout
from django.core.mail import send_mail
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
    return render(request, 'enroll/signup.html', {'form': fm})

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
              return HttpResponseRedirect('/profile/')
          
    else:      
        fm = AuthenticationForm()
    return render(request,'enroll/login.html', {'form':fm})
# profile
def user_profile(request):
    return render(request, 'enroll/profile.html')