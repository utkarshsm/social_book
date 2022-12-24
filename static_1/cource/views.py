from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request,'cource/courceone.html' , {'title':'Learn_Django','cname':'Django'})