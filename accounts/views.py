from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
# Create your views here.


def signUp(request):
   signfrom = SignUpForm()
   if request.method == 'POST':
      signfrom = SignUpForm(data=request.POST)
      if signfrom.is_valid():
         user = signfrom.save()
         auth_login(request,user)
         username = signfrom.cleaned_data.get('username')
         return redirect('home')
 
   return  render(request,'accounts/signup.html',{'form':signfrom})


   
def home(request):
    return render(request,"accounts/msg.html")