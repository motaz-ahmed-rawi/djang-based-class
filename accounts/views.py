from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
# Create your views here.


# def signUp(request):
#    signfrom = SignUpForm()
#    if request.method == 'POST':
#       signfrom = SignUpForm(data=request.POST)
#       if signfrom.is_valid():
#          user = signfrom.save()
#          auth_login(request,user)
#          username = signfrom.cleaned_data.get('username')
#          return redirect('home')

# def check_login(request):
#       if request.user.is_authenticated ==True:
#           return True
#       else:  return redirect('login') 

def signUp(request):
   signform=SignUpForm()
   if request.method=='POST':
      signForm=SignUpForm(request.POST)
      if  signForm.is_valid():
          user=signForm.save()
          auth_login(request,user)
          return redirect('home')

 
   return  render(request,'accounts/signup.html',{'form':signform})



@login_required
def home(request):
   return render(request,"accounts/msg.html")
   