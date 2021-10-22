from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'todo/home.html')

# Create your views here.
def signupuser(request):
  if request.method == 'GET':
      return render(request, 'todo/signup.html', {'form': UserCreationForm()})
  else:
      if request.POST['password1'] == request.POST['password2']:

          try:
              # check
              user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
              user.save()
              login(request, user)
              return redirect('currenttodos')
          except IntegrityError:
              return render(
                request,
                'todo/signup.html',
                {
                    'form': UserCreationForm(),
                    'error': 'That username has alredy been taken'
                }
              )

      else:
        # Tell the use that password do not much
        return render(
            request,
            'todo/signup.html',
            {
                'form': UserCreationForm(),
                'error': 'Password did not match'
            })


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html', {'form' : AuthenticationForm()})
    else:
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )

        if user is None:
            return render(request,
                'todo/login.html', 
                { 
                    'form': AuthenticationForm(),
                    'error': 'Username or password are not correct'
                }
            )
        else:
            login(request, user)
            return redirect('currenttodos')


def currenttodos(request):
    return render(
        request,
        'todo/currenttodos.html',
        ) 
