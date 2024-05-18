from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import TemplateView

CustomUser = get_user_model()

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Account is not activated by admin.')
        else:
            return HttpResponse('Invalid login credentials')

    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

class HomeView(TemplateView):
    template_name = 'home.html'
