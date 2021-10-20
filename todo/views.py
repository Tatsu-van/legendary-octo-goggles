from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupuser(request):
  if request.method == 'GET':
      return render(request, 'todo/signup.html', {'form': UserCreationForm()})
  else:
      if request.POST['password1'] == request.POST['password2']:
          return redirect('currenttodos')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html') 
